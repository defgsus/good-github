## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-14](docs/good-messages/2023/2023-08-14.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,184,258 were push events containing 3,222,857 commit messages that amount to 254,892,239 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 55 messages:


## [git-for-windows/git](https://github.com/git-for-windows/git)@[8e2e8a75e8...](https://github.com/git-for-windows/git/commit/8e2e8a75e800d9240eb705e05988a0c1976e03d6)
#### Monday 2023-08-14 00:36:46 by Johannes Schindelin

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
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[c968edab30...](https://github.com/Ical92/tgstation/commit/c968edab306659606da4f39bc178851a5a24405c)
#### Monday 2023-08-14 00:53:18 by carlarctg

Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

## About The Pull Request

Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror or the cursed springs
are the most accessible sources)

Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the shuttle has just less than half of its usual refueling
time left. However, it gives the cargo budget an influx of 3000 credits!

Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

## Why It's Good For The Game

First off, here is my reasoning for why these need altering at all.

Players will always naturally gravitate to the wackiest and
most-out-there options, in this case this applies to shuttles. It's why
the Monastery or the Asteroid or Daniel are reasonably common sights,
more common than some of the 'boring' shuttle options that don't need
unlock with an emag.

The problem here, as I see it, is that there is no incentive
what-so-ever to NOT purchase these 'wacky' shuttles. Some of the
shuttles in the code are just way too stupid to be seen on most or even
some rounds (Arena, Disco Inferno?), so they require rare unlocks to
occur. Wacky shuttles being spammed round after round are bad due to
several reasons:
1. Players will run every joke to the ground. Wacky conditionless
shuttles take up a large amount of space in the shuttle memeplex, so
they are disproportionately seen in comparison to any of the
less-extravagant but more grounded and actually interesting options.
(Medisim? Monkeys anyone?). This ends up making the wacky shuttles
actually *less* wacky and just the stale and boring options.
2. Wacky shuttles affect the end-round quite a lot. This is fine, of
course, but not when these wacky shuttles can be seen every round.
3. These wacky shuttles don't have proper facilities. None of them have
a good medical section, or emergency supplies, or enough room. This gets
pretty annoying pretty fast.
4. One Funny Guy (the quintessential example being the clown with a dead
captain's ID) is all but guaranteed to try to buy the funniest and most
annoying shuttle to piss off the rest of the crew. With how Funny and
Annoying these shuttles are, not to mention how dirt-cheap they are (or
literally give you money!), they're easily the most seen alternate
shuttles, which isn't good when they alter how the round-end plays so
heavily.

> Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror is the most accessible
source)

The Wabbajack has a endless source of voluntary Polymorphs with a
comically low price, which means it is purchased endlessly by crew, not
to mention being literally a source of free syndiborgs and xenos. While
I'm not a balanceposter, this does come with some annoyances especially
for antagonists who just randomly get blown up by an assault borg. This
is fine and fun every so often, but not as a common occurrence, not as a
guaranteed every-round option. I think it's an excellent candidate for
an unlock condition.

> Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the emergency shuttle is more than halfway refueled.
However, it gives the cargo budget an influx of 3000 credits!

This is LITERALLY 'haha grief shuttle', I have no idea how it even got
in as a condition-less shuttle. You see the captain buy it For No Raisin
Lul 2 minutes in, sigh to yourself, and secure an EVA suit when the
shuttle lands to try to survive in the unbelievably cramped space.
(Someone always blows it up.)

Instead of being JUST Grief Shuttle, now it has some interesting reasons
to exist. Revs and you're dirt-poor? Nukies just declared war after the
Clown bought ten crates of creampie dufflebags? Buy this shuttle and get
an influx of money.

> Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

This one isn't as egregious as the above, but I believe my personal
dislike of it extends to a game design level, to an extent. One person
can buy this shuttle and the crew as a whole are left to groan as they
prepare for a noisy, confusing shuttle in which everyone is ten tiles
shifted to their left as their sprite does the most ridiculous dance
seen in SS13 history. 'Just turn the music off!': I'm glad this is an
option, but it doesn't change how much this shuttle alters things. It's
fine as a sendoff to a nice, chill greenshift, but as a constant sight
in red shifts it's just... frustrating. And purchased BECAUSE it's
frustrating, to the short-lived schadenfreude of one person and the
frustration of others.

And then the unbreakable disco machine. Why is it unbreakable. If the
crew doesn't want to listen to the thing, let them break it? Buy Disco
Inferno if you want an unbreakable disco.

Some of these changes are probably over-the-top, but remember that these
will still be seen in-game, just a bit rarer. Worst case scenario the
shuttle replacement event will let them have their time in the
limelight.

## Changelog

:cl:
balance: Lepton Violet (wabbajack) shuttle must be unlocked by having
some form of polymorph happen in-game first (Pride Mirror or the cursed
springs are the most accessible sources)
balance: Scrapheap shuttle can only be bought if the Cargo budget is
below 600 credits, and the shuttle has just less than half of its usual
refueling time left. However, it gives the cargo budget an influx of
3000 credits!
qol: Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.
/:cl:

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[dc6ddd821b...](https://github.com/Ical92/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Monday 2023-08-14 00:53:18 by Cheshify

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
## [MrStonedOne/tgstation](https://github.com/MrStonedOne/tgstation)@[6c34d93be7...](https://github.com/MrStonedOne/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Monday 2023-08-14 01:06:58 by necromanceranne

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
## [MrStonedOne/tgstation](https://github.com/MrStonedOne/tgstation)@[95ec0e6545...](https://github.com/MrStonedOne/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Monday 2023-08-14 01:06:58 by necromanceranne

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
## [fifteenhex/linux](https://github.com/fifteenhex/linux)@[0a2c2baafa...](https://github.com/fifteenhex/linux/commit/0a2c2baafa312ac4cec4f0bababedab3f971f224)
#### Monday 2023-08-14 01:26:05 by Linus Torvalds

proc: fix missing conversion to 'iterate_shared'

I'm looking at the directory handling due to the discussion about f_pos
locking (see commit 797964253d35: "file: reinstate f_pos locking
optimization for regular files"), and wanting to clean that up.

And one source of ugliness is how we were supposed to move filesystems
over to the '->iterate_shared()' function that only takes the inode lock
for reading many many years ago, but several filesystems still use the
bad old '->iterate()' that takes the inode lock for exclusive access.

See commit 6192269444eb ("introduce a parallel variant of ->iterate()")
that also added some documentation stating

      Old method is only used if the new one is absent; eventually it will
      be removed.  Switch while you still can; the old one won't stay.

and that was back in April 2016.  Here we are, many years later, and the
old version is still clearly sadly alive and well.

Now, some of those old style iterators are probably just because the
filesystem may end up having per-inode mutable data that it uses for
iterating a directory, but at least one case is just a mistake.

Al switched over most filesystems to use '->iterate_shared()' back when
it was introduced.  In particular, the /proc filesystem was converted as
one of the first ones in commit f50752eaa0b0 ("switch all procfs
directories ->iterate_shared()").

But then later one new user of '->iterate()' was then re-introduced by
commit 6d9c939dbe4d ("procfs: add smack subdir to attrs").

And that's clearly not what we wanted, since that new case just uses the
same 'proc_pident_readdir()' and 'proc_pident_lookup()' helper functions
that other /proc pident directories use, and they are most definitely
safe to use with the inode lock held shared.

So just fix it.

This still leaves a fair number of oddball filesystems using the
old-style directory iterator (ceph, coda, exfat, jfs, ntfs, ocfs2,
overlayfs, and vboxsf), but at least we don't have any remaining in the
core filesystems.

I'm going to add a wrapper function that just drops the read-lock and
takes it as a write lock, so that we can clean up the core vfs layer and
make all the ugly 'this filesystem needs exclusive inode locking' be
just filesystem-internal warts.

I just didn't want to make that conversion when we still had a core user
left.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [Drillur/LORED](https://github.com/Drillur/LORED)@[0fb494abd6...](https://github.com/Drillur/LORED/commit/0fb494abd64f291dcc61b2abadd080db50ba637e)
#### Monday 2023-08-14 02:16:39 by Drillur

Save Day

Worked on Save shit all day. What a nightmare, I hate ResourceSaver and everything about it. For some reason, my new method of saving causes 0.5 sec lag, and the file is 2mb and miles long. isn't that rly cool and awesome?

also, started Wallet. probably did something else too, who knows

this is the worst kind of progress. it was all necessary, but it felt awful the whole time

---
## [buddhablake/blakes_blog](https://github.com/buddhablake/blakes_blog)@[dd514ffbd0...](https://github.com/buddhablake/blakes_blog/commit/dd514ffbd01b50270196c65cfc107b72c578c3b4)
#### Monday 2023-08-14 02:46:04 by Blake Douglass

added top level page blog is no longer index and go fuck yourself

---
## [Moo-Ack-Productions/MCprep](https://github.com/Moo-Ack-Productions/MCprep)@[a34b01aa69...](https://github.com/Moo-Ack-Productions/MCprep/commit/a34b01aa69f7e215a0cd6ec46665e1c15a0a78ca)
#### Monday 2023-08-14 02:51:13 by mahid

Added type annotations and use of Path
Replaced some instances of os.path with the Path object from pathlib for
readability. Also added type annotations to MCprepEnv as we're moving
towards that. This also means MCprep will not work at all in Blender
2.7x due to the use of new syntax.

This will be the first in a long process of modernizing MCprep's code
with 2.8 style code. Blender 2.7x users may not be happy, but it's for
the better. If anything, 6 years worth of 2.7x support was a mistake (in
my opinion), as it limited what we could do and opened MCprep to even
more bugs (like in Blender 2.93 with make_annotations, which ironically
now is deprecated).

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c3b31a7813...](https://github.com/treckstar/yolo-octo-hipster/commit/c3b31a7813941cdd37d353ff17aa37583932e066)
#### Monday 2023-08-14 03:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [bxtshit/External-Leak](https://github.com/bxtshit/External-Leak)@[b1db983876...](https://github.com/bxtshit/External-Leak/commit/b1db983876140bced76cdbe89fbfcb3df4b28458)
#### Monday 2023-08-14 03:23:32 by bxtshit

leak of a source of a mf who lovveesss scamming!!

you get what you deserve, fuck this god damn comm, everyone in here cant fucking code.

---
## [FrancescoVassalli/evals](https://github.com/FrancescoVassalli/evals)@[30e35436be...](https://github.com/FrancescoVassalli/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Monday 2023-08-14 04:05:02 by Nazar

Hard russian computer science tasks  (#1323)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[e80cf8f358...](https://github.com/Iamgoofball/-tg-station/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Monday 2023-08-14 05:47:10 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[8e3dfc2af2...](https://github.com/CliffracerX/Skyraptor-SS13/commit/8e3dfc2af2f3ca87e9f07669033c1ec2a6102073)
#### Monday 2023-08-14 06:28:03 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[8744738e59...](https://github.com/retlaw34/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Monday 2023-08-14 06:45:09 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [IN2-Moist/2Take1-Moist-Script](https://github.com/IN2-Moist/2Take1-Moist-Script)@[fb48803cff...](https://github.com/IN2-Moist/2Take1-Moist-Script/commit/fb48803cff3308eb41f6208292bdcca5d5ff3590)
#### Monday 2023-08-14 07:11:51 by IN2_Moist

3.0.2.9 Release

Moist Script Natives Module Fully updated with new natives and extra parameters added in the last dlc update.
Added  Spawn Options on Online Player Features
Moved Spawn Functions from Griefing & Troll Section into Spawn Options
Fixed Issue with the Orbital Obliteration not getting set correctly when finished with any orbital feature
Added  NoGod4U in Troll and Annoying (removes god mode if not protected)
Added StunGunGod to Griefing puts player on job screen and shoots tazer shots at them fast and when they exit job screen god disables long enough to get a kill on them Need to Spectate for it to work properly
Added Force To MOC Mission Launch Screens
Added Send to Del Pero (Requires them to be in a ceo/mc to work)
Any Vehicle Lock-on Missiles (Players) Now fully compatible with Raiju and Other Jets. Same Fire Control as normal disabled for jet to fire.
Re-Tweaked speeds and applying force to Stealth Mode Bombs (Still not happy with results but it works for now)
Stealth Mode Bombs now have a long Effect Duration so for Gas Bombs if you stay close enough to their location of impact the gas just keeps triggering.
Added Excessive / Modified Health Detection checks for free mode beast and ignores ballistic armour.
Removed Script event Hooks for RC Detection Now using a faster method and will detect them after restarting script in session. also detects Personal RC Vehicles with a different icon on radar
Big Changes to god mode detection, still not finished completely but it does not seem to trigger falsely now, new checks and new methods to improve reliability
Teleport Player Features Updated so if no vehicle is detected it will use the new player teleport if vehicle is detected will use the old method of mine.
Updated the Set 10k Bounty on Session to Random Bounty Values
Added New Player Attributes: RC, Player fading (as going into interior and going to job screen) invulnerable detection (not just a god mode check!
Improved Interior Detection
Added Flare Counter Measures for any vehicle
Probably a whole lot more there i missed so much been working on since last update not finished it all so just releasing what seems to be working well from that.

---
## [sst-inc/Vexential-Inc.](https://github.com/sst-inc/Vexential-Inc.)@[b9ff2c11a5...](https://github.com/sst-inc/Vexential-Inc./commit/b9ff2c11a5d831fbdcea25366d43e4be04040fe9)
#### Monday 2023-08-14 07:33:08 by mushroomthatcodes

calendar !!!!

fucking hell this shit is trying to make me kill myself but ya i made the fucking calendar

---
## [iliyaxox/Bubberstation](https://github.com/iliyaxox/Bubberstation)@[a1609c4536...](https://github.com/iliyaxox/Bubberstation/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Monday 2023-08-14 07:37:33 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**

https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [seokbeomKim/melpa](https://github.com/seokbeomKim/melpa)@[4872ef038d...](https://github.com/seokbeomKim/melpa/commit/4872ef038dbbf67008bfa7951574ee372d6ff68d)
#### Monday 2023-08-14 09:15:52 by Jonas Bernoulli

Distribute all back-ends with the emacsql package

There are two reasons for this.

- Going forward, packages that use `emacsql' and SQLite should use
  the best back-end that can be used with the Emacs instance in use,
  either `emacsql-sqlite-builtin`, `emacsql-sqlite-module`, or as a
  last resort `emacsql-sqlite'.

  That means that if we didn't bundle the back-end libraries with
  `emacsql' itself, these packages would have to depend on all three
  back-end packages in addition to `emacsql' itself.  (Alternatively
  they could not depend on any of the back-end packages, and instead
  make the user install the appropriate back-end, when they try to
  use the package.  That's a bad user experience and there likely
  would be bugs, making it even more painful.)

- EmacSQL is now distributed on NonGNU Elpa as well.  While we at
  Melpa encourages the creation of separate packages for optional
  extensions (which are not useful to all users, or which have
  additional dependencies) the Emacs maintainers prefer everything to
  be distribute as one package, even if that means that `defvar' and
  `declare-function' declarations are necessary to keep the compiler
  happy.

  I still think our way is usually better, but since three of the
  back-end libraries have to be distributed with the main package
  anyway, we might as well give in here and bundle the other three
  as well.

For the time being, we have to continue to *also* distribute the
back-end libraries as separate packages.

Several third-party packages depend on the existing `emacsql' and
`emacsql-sqlite' packages.  These packages should be updated to only
depend on `emacsql', but the latest released versions of these
packages will continue to depend on `emacsql-sqlite' as well.  If we
removed the recipe for that, that would remove the latest release of
that package from Melpa, not just the snapshot version.

This is the current roadmap:

0. Include all back-ends in `emacsql'.
1. Update dependant packages to only depend on `emacsql'.
2. Make changes to `emacsql', which are enabled by the former two
   steps, and which are blocking the creation of a new `emacsql'
   release.  (These changes are related to the addition of the
   additional SQLite back-ends.  So this is a bit of a chicken and
   egg problem, and this commit (0) is the first step to break out
   of that.)
3. Create an `emacsql' release.
4. Wait for new releases of all dependant packages.
5. Change the separate back-end packages to warn the user, asking
   them to remove all of these packages.
6. After waiting some more, remove the separate back-end packages.

While a back-end is installed as part of `emacsql' and as a separate
package, it is undefined which version is loaded, but until step (5)
the two versions should be the same, so it doesn't matter.

---
## [2003dipu/12-beginner-python-projects-with-Kyle-Ying](https://github.com/2003dipu/12-beginner-python-projects-with-Kyle-Ying)@[f56ff1e4b7...](https://github.com/2003dipu/12-beginner-python-projects-with-Kyle-Ying/commit/f56ff1e4b7d8d7ce14b8fd635cd1958e4f2ecf47)
#### Monday 2023-08-14 09:44:43 by Dipu Singha

Create Python beginner 12 Projects

# 12 Beginner Python Projects

Welcome to the "12 Beginner Python Projects" repository! This collection of projects is designed to help you learn and practice Python programming in an engaging and hands-on way. Whether you're a complete beginner or looking to reinforce your programming skills, these projects offer a great opportunity to explore various aspects of Python and its applications.

## Project List

1. **Madlibs**
   Have a blast creating your own hilarious stories by replacing placeholders with user-inputted words. This project introduces you to basic input/output and string manipulation in Python.

2. **Guess the Number (Computer)**
   Dive into the world of computer-generated random numbers! Build a simple guessing game where the computer selects a number and the player attempts to guess it. Get comfortable with conditional statements and loops.

3. **Guess the Number (User)**
   Put a twist on the previous project! This time, you'll choose a number and let the computer try to guess it. Explore concepts of randomness and decision-making in your Python code.

4. **Rock Paper Scissors**
   Play the timeless game of Rock Paper Scissors against the computer. Learn about conditional statements, random choices, and creating interactive experiences in your programs.

5. **Hangman**
   Bring the classic word-guessing game to life! Develop a program that selects a random word and lets the player guess letters until they either solve the word or run out of attempts. Strengthen your skills in strings and loops.

6. **Tic-Tac-Toe**
   Explore creating a two-player Tic-Tac-Toe game using Python. Learn about data structures, nested loops, and user input validation while building a competitive and strategic game.

7. **Tic-Tac-Toe AI**
   Take your Tic-Tac-Toe game to the next level by implementing an AI opponent. Discover basic artificial intelligence concepts and algorithms to create an opponent that can challenge players.

8. **Binary Search**
   Delve into fundamental searching algorithms by creating a program that performs a binary search on a sorted list. Learn about efficient searching techniques and algorithm design.

9. **Minesweeper**
   Embrace the intricacies of logic and board games with Minesweeper. Develop a simplified version of this classic game that involves revealing cells on a grid while avoiding hidden mines.

10. **Sudoku Solver**
    Tackle the fascinating world of puzzles by building a program that can solve Sudoku grids. Dive into algorithmic problem-solving and recursion as you craft a solver for this number-placement challenge.

11. **Photo Processing**
    Explore the artistic side of programming! Create a program that can apply various filters and effects to images. Get hands-on experience with image manipulation libraries in Python.

12. **Markov Chain Composer**
    Unleash your inner composer by building a program that generates music using Markov chains. Dive into probabilistic models and sequencing to create algorithmically generated musical pieces.

## How to Use
Each project is located in its own directory within this repository. You can navigate to each project's directory to find the Python code and any accompanying resources or instructions. Feel free to explore, modify, and expand upon the projects to enhance your learning experience.

## Getting Started
If you're new to programming or Python, start with the projects at the beginning of the list, as they gradually introduce concepts and increase in complexity. As you become more comfortable, challenge yourself with the later projects to deepen your understanding of programming techniques.

## Contribution
If you've come up with improvements, bug fixes, or additional projects, we encourage you to contribute to this repository. Fork the repository, make your changes, and submit a pull request to share your ideas with the community.

## License
This repository is under the [MIT License](LICENSE), allowing you to freely use, modify, and distribute the code for personal or educational purposes.

Get ready to embark on a journey of learning and creativity with these 12 Beginner Python Projects! Happy coding! 🚀🐍

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[e2c6b1c425...](https://github.com/codecov/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Monday 2023-08-14 09:59:18 by Giovanni M Guidini

fix: lru_cache issues + meta info missing  (#72)

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[028416a56e...](https://github.com/argilla-io/argilla/commit/028416a56e1eb05defe9dffcd03de5d1744bdcf2)
#### Monday 2023-08-14 10:05:22 by Natalia Elvira

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
## [isaacphysics/isaac-react-app](https://github.com/isaacphysics/isaac-react-app)@[dda179a4ad...](https://github.com/isaacphysics/isaac-react-app/commit/dda179a4ad61131c4d044bbd20e02f47a743a926)
#### Monday 2023-08-14 10:31:31 by James Sharkey

Prevent doubling of copy-pasted maths keeping A11Y

This is difficult. The sr-only class does not stop the contents from
appearing on the clipboard, which is a different sort of accessibility
violation in itself, because it makes the pasted text (e.g. for
conversion into Braille or to be used elsewhere) confusing.

The obvious fix is to replace the span text with an aria-label. But
aria-label is prohibited on non-interactive content like spans:
https://w3c.github.io/aria/#aria-label

To fix this, we can add an aria-role to the KaTeX element. The obvious
one is role="math". This works fine for NVDA on Chrome/Firefox but
breaks VoiceOver because that just states "maths" and ignores the label.
Breaking VoiceOver is a no-go, since that is basically the main option
on MacOS and iOS.

Fortunately, most browsers and screenreaders ignore the ARIA spec and
will respect aria-label on a non-interactive element. This means that
the role can be left out and we can still use a span. But VoiceOver
still ignores the maths, or else reads it out followed by "empty group".
Using the non-standard role="text" fixes this on Safari and iOS for
VoiceOver, but Chrome on MacOS still gets the annoying "empty group".

Since everything here is non-standards-compliant, I don't know what to
do. This proposal gives the best experience for a novice user with
screenreader settings "out-of-the-box", and that is our target audience.
This is a dramatic improvement for everyone not using a screenreader,
and will only be noticeable to VoiceOver users on Chrome on MacOS.
I think that is the best we can do unless/until VoiceOver is fixed.

KaTeX makes accessibility really hard, as does poor cross-browser
standardisation for maths generally . . .

---
## [feugy/next.js](https://github.com/feugy/next.js)@[e06880ea4c...](https://github.com/feugy/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Monday 2023-08-14 12:23:50 by Josh Story

Implement new forking technique for vendored packages. (#51083)

## Vendoring

Updates all module resolvers (node, webpack, nft for entrypoints, and nft for next-server) to consider whether vendored packages are suitable for a given resolve request and resolves them in an import semantics preserving way.

### Problem

Prior to the proposed change, vendoring has been accomplished but aliasing module requests from one specifier to a different specifier. For instance if we are using the built-in react packages for a build/runtime we might replace `require('react')` with `require('next/dist/compiled/react')`.

However this aliasing introduces a subtle bug. The React package has an export map that considers the condition `react-server` and when you require/import `'react'` the conditions should be considered and the underlying implementation of react may differ from one environment to another. In particular if you are resolving with the `react-server` condition you will be resolving the `react.shared-subset.js` implementation of React. This aliasing however breaks these semantics because it turns a bare specifier resolution of `react` with path `'.'` into a resolution with bare specifier `next` with path `'/dist/compiled/react'`. Module resolvers consider export maps of the package being imported from but in the case of `next` there is no consideration for the condition `react-server` and this resolution ends up pulling in the `index.js` implementation inside the React package by doing a simple path resolution to that package folder.

To work around this bug there is a prevalence of encoding the "right" resolution into the import itself. We for instance directly alias `react` to `next/dist/compiled/react/react.shared-subset.js` in certain cases. Other times we directly specify the runtime variant for instance `react-server-dom-webpack/server.edge` rather than `react-server-dom-wegbpack/server`, bypassing the export map altogether by selecting the runtime specific variant. However some code is meant to run in more than one runtime, for instance anything that is part of the client bundle which executes on the server during SSR and in the browser. There are workaround like using `require` conditionally or `import(...)` dynamically but these all have consequences for bundling and treeshaking and they still require careful consideration of the environment you are running in and which variant needs to load.

The result is that there is a large amount of manual pinning of aliases and additional complexity in the code and an inability to trust the package to specify the right resolution potentially causing conflicts in future versions as packages are updated.

It should be noted that aliasing is not in and of itself problematic when we are trying to implement a sort of lightweight forking based on build or runtime conditions. We have good examples of this for instance with the `next/head` package which within App Router should export a noop function. The problem is when we are trying to vendor an entire package and have the package behave semantically the same as if you had installed it yourself via node_modules

### Solution

The fix is seemingly straight forward. We need to stop aliasing these module specifiers and instead customize the resolution process to resolve from a location that will contain the desired vendored packages. We can then start simplifying our imports to use top level package resources and generally and let import conditions control the process of providing the right variant in the right context.

It should be said that vendoring is conditional. Currently we only vendor react pacakges for App Router runtimes. The implementation needs to be able to conditionally determine where a package resolves based on whether we're in an App Router context vs a Page Router one.

Additionally the implementation needs to support alternate packages such as supporting the experimental channel for React when using features that require this version.

### Implementation

The first step is to put the vendored packages inside a node_modules folder. This is essential to the correct resolving of packages by most tools that implement module resolution. For packages that are meant to be vendored, meaning whole package substitution we move the from `next/(src|dist)/compiled/...` to `next/(src|dist)/vendored/node_modules`. The purpose of this move is to clarify that vendored packages operate with a different implementation. This initial PR moves the react dependencies for App Router and `client-only` and `server-only` packages into this folder. In the future we can decide which other precompiled dependencies are best implemented as vendored packages and move them over.

It should be noted that because of our use of `JestWorker` we can get warnings for duplicate package names so we modify the vendored pacakges for react adding either `-vendored` or `-experimental-vendored` depending on which release channel the package came from. While this will require us to alter the request string for a module specifier it will still be treating the react package as the bare specifier and thus use the export map as required.

#### module resolvers
The next thing we need to do is have all systems that do module resolution implement an custom module resolution step. There are five different resolvers that need to be considered

##### node runtime
Updated the require-hook to resolve from the vendored directory without rewriting the request string to alter which package is identified in the bare specifier. For react packages we only do this vendoring if the `process.env.__NEXT_PRIVATE_PREBUNDLED_REACT` envvar is set indicating the runtime is server App Router builds. If we need a single node runtime to be able to conditionally resolve to both vendored and non vendored versions we will need to combine this with aliasing and encode whether the request is for the vendored version in the request string. Our current architecture does not require this though so we will just rely on the envvar for now

##### webpack runtime
Removed all aliases configured for react packages. Rely on the node-runtime to properly alias external react dependencies. Add a resolver plugin `NextAppResolverPlugin` to preempt perform resolution from the context of the vendored directory when encountering a vendored eligible package.

##### turbopack runtime
updated the aliasing rules for react packages to resolve from the vendored directory when in an App Router context. This implementation is all essentially config b/c the capability of doing the resolve from any position (i.e. the vendored directory) already exists

##### nft entrypoints runtime
track chunks to trace for App Router separate from Pages Router. For the trace for App Router chunks use a custom resolve hook in nft which performs the resolution from the vendored directory when appropriate.

##### nft next-server runtime
The current implementation for next-server traces both node_modules and vendored version of packages so all versions are included. This is necessary because the next server can run in either context (App vs Page router) and may depend on any possible variants. We could in theory make two traces rather than a combined one but this will require additional downstream changes so for now it is the most conservative thing to do and is correct

Once we have the correct resolution semantics for all resolvers we can start to remove instances targeting our precompiled instances for instance making `import ... from "next/dist/compiled/react-server-dom-webpack/client"` and replacing with `import ... from "react-server-dom-webpack/client"`

We can also stop requiring runtime specific variants like `import ... from "react-server-dom-webpack/client.edge"` replacing it with the generic export `"react-server-dom-webpack/client"`

There are still two special case aliases related to react
1. In profiling mode (browser only) we rewrite `react-dom` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`. This can be moved to using export maps and conditions once react publishses updates that implement this on the package side.
2. When resolving `react-dom` on the server we rewrite this to `react-dom/server-rendering-stub`. This is to avoid loading the entire react-dom client bundle on the server when most of it goes unused. In the next major react will update this top level export to only contain the parts that are usable in any runtime and this alias can be dropped entirely

There are two non-react packages currently be vendored that I have maintained but think we ought to discuss the validity of vendoring. The `client-only` and `server-only` packages are vendored so you can use them without having to remember to install them into your project. This is convenient but does perhaps become surprising if you don't realize what is happening. We should consider not doing this but we can make that decision in another discussion/PR.

#### Webpack Layers
One of the things our webpack config implements for App Router is layers which allow us to have separate instances of packages for the server components graph and the client (ssr) graph. The way we were managing layer selection was a but arbitrary so in addition to the other webpack changes the way you cause a file to always end up in a specific layer is to end it with `.serverlayer`, `.clientlayer` or `.sharedlayer`. These act as layer portals so something in the server layer can import `foo.clientlayer` and that module will in fact be bundled in the client layer.

#### Packaging Changes
Most package managers are fine with this resolution redirect however yarn berry (yarn 2+ with PnP) will not resolve packages that are not defined in a package.json as a dependency. This was not a problem with the prior strategy because it was never resolving these vendored packages it was always resolving the next package and then just pointing to a file within it that happened to be from react or a related package.

To get around this issue vendored packages are both committed in src and packed as a tgz file. Then in the next package.json we define these vendored packages as `optionalDependency` pointing to these tarballs. For yarn PnP these packed versions will get used and resolved rather than the locally commited src files. For other package managers the optional dependencies may or may not get installed but the resolution will still resolve to the checked in src files. This isn't a particularly satisfying implemenation and if pnpm were to be updated to have consistent behavior installing from tarballs we could actually move the vendoring entirely to dependencies and simplify our resolvers a fair bit. But this will require an upstream chagne in pnpm and would take time to propogate in the community since many use older versions

#### Upstream Changes

As part of this work I landed some other changes upstream that were necessary. One was to make our packing use `npm` to match our publishing step. This also allows us to pack `node_modules` folders which is normally not supported but is possible if you define the folder in the package.json's files property.

See: #52563

Additionally nft did not provide a way to use the internal resolver if you were going to use the resolve hook so that is now exposed

See: https://github.com/vercel/nft/pull/354

#### additional PR trivia
* When we prepare to make an isolated next install for integration tests we exclude node_modules by default so we have a special case to allow `/vendored/node_modules`

* The webpack module rules were refactored to be a little easier to reason about and while they do work as is it would be better for some of them to be wrapped in a `oneOf` rule however there is a bug in our css loader implementation that causes these oneOf rules to get deleted. We should fix this up in a followup to make the rules a little more robuts.


## Edits
* I removed `.sharedlayer` since this concept is leaky (not really related to the client/server boundary split) and it is getting refactored anyway soon into a precompiled runtime.

---
## [Volcanware/Envy-Client](https://github.com/Volcanware/Envy-Client)@[e752caf05a...](https://github.com/Volcanware/Envy-Client/commit/e752caf05ab09e137eebffafaba61a605d6ac9d1)
#### Monday 2023-08-14 13:12:44 by Volcan

Added Baritone Follow to Bot Module || Fuck you Hardline for making me go to sleep

---
## [robertxgray/crawl](https://github.com/robertxgray/crawl)@[1880023187...](https://github.com/robertxgray/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Monday 2023-08-14 13:18:43 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [anifort/langchain](https://github.com/anifort/langchain)@[16af5f8690...](https://github.com/anifort/langchain/commit/16af5f86905705096552507f8739b5cfcaa77aa4)
#### Monday 2023-08-14 13:35:09 by niklub

Add LabelStudio integration (#8880)

This PR introduces [Label Studio](https://labelstud.io/) integration
with LangChain via `LabelStudioCallbackHandler`:

- sending data to the Label Studio instance
- labeling dataset for supervised LLM finetuning
- rating model responses
- tracking and displaying chat history
- support for custom data labeling workflow

### Example

```
chat_llm = ChatOpenAI(callbacks=[LabelStudioCallbackHandler(mode="chat")])
chat_llm([
    SystemMessage(content="Always use emojis in your responses."),
        HumanMessage(content="Hey AI, how's your day going?"),
    AIMessage(content="🤖 I don't have feelings, but I'm running smoothly! How can I help you today?"),
        HumanMessage(content="I'm feeling a bit down. Any advice?"),
    AIMessage(content="🤗 I'm sorry to hear that. Remember, it's okay to seek help or talk to someone if you need to. 💬"),
        HumanMessage(content="Can you tell me a joke to lighten the mood?"),
    AIMessage(content="Of course! 🎭 Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"),
        HumanMessage(content="Haha, that was a good one! Thanks for cheering me up."),
    AIMessage(content="Always here to help! 😊 If you need anything else, just let me know."),
        HumanMessage(content="Will do! By the way, can you recommend a good movie?"),
])
```

<img width="906" alt="image"
src="https://github.com/langchain-ai/langchain/assets/6087484/0a1cf559-0bd3-4250-ad96-6e71dbb1d2f3">


### Dependencies
- [label-studio](https://pypi.org/project/label-studio/)
- [label-studio-sdk](https://pypi.org/project/label-studio-sdk/)

https://twitter.com/labelstudiohq

---------

Co-authored-by: nik <nik@heartex.net>

---
## [fdncred/nushell](https://github.com/fdncred/nushell)@[ad49c17eba...](https://github.com/fdncred/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Monday 2023-08-14 13:39:44 by Kiryl Mialeshka

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
## [aritradey-CS/Aritra_Dey](https://github.com/aritradey-CS/Aritra_Dey)@[0611b79e0b...](https://github.com/aritradey-CS/Aritra_Dey/commit/0611b79e0bd4ce59b0366e3326ecc942f2e10eae)
#### Monday 2023-08-14 16:02:28 by Aritra Dey

Create README.md

Sure, here's a short description for your personal website project:

"Welcome to my personal website! This platform serves as a hub for my professional journey and thoughts. At the heart of this site is my resume, showcasing my skills, experience, and educational background. As you explore, you'll also find a collection of insightful blog posts where I share my ideas and experiences. With a clean and user-friendly design, this website aims to provide visitors with an easy way to learn about me, my accomplishments, and engage with my thoughts through the blog section. Feel free to navigate through the various sections and get to know more about me and my journey in the world of technology and beyond."

---
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[7f1d53e719...](https://github.com/cnleth/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Monday 2023-08-14 16:02:47 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

## About The Pull Request
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

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[31f1924324...](https://github.com/cnleth/tgstation/commit/31f1924324b04086f24034aaf754d5f85cb595a8)
#### Monday 2023-08-14 16:02:47 by san7890

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

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
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
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
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[b22ff1a4eb...](https://github.com/cnleth/tgstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Monday 2023-08-14 16:02:47 by Sealed101

Laser pointer update: Shining Through Walls Edition (feat. fixes!) (#77007)

# _PR PSA_


![augh](https://github.com/tgstation/tgstation/assets/75863639/6dc87fc7-65a3-4b7c-9b8d-a1432cacbe93)


## About The Pull Request
Cleans up code for laser pointers, fixing some bugs like the
forever-charging state or affecting dead cats along the way.
Remaining charge is now available upon examine.
Canonizes #45834 by implementing an upgrade to the laser pointers:
installing a bluespace crystal into a laser with tier 3 or higher laser
diode lets it shine through walls. Using an upgraded laser uses twice
the charge of a normal one. Of course, you can only shine it on
something if you can see the target behind the wall, like via x-ray or
thermals. Mesons don't count, however.
If one tries to jam a crystal into a pointer with a tier 1/2 laser (or a
tier 1/2 laser in a pointer with an installed crystal), _something_ will
get teleported, crushing the crystal.
You can uninstall the crystal with wirecutters or a hemostat. The
pointer will _hint_ on closer examination (`examine_more`) at a
possibility of a crystal being installed if you upgrade the laser
(different messages for tier 1/2/3,4).
Removes one stupid 1% increase for a recharge chance per process tick if
your laser was in a full recharge state because it was insignificant and
irrelevant.

i've had a branch for this for almost 9 months and i was always laying
it off for some day later. today i just completely fucked the branch.
whoops. i'm not even sure at this point what else did i fix while here,
double whoops

## Why It's Good For The Game
Closes #45834 - Canonizes a bug into a feature.
Fixes #77003 - lol
Cleaner code, possibly more robust even.
Seeing the remaining charge was not available at all and the only hint
was when you tried shining the pointer on something. That sucks.

## Changelog
:cl:
add: you can upgrade laser pointers with a bluespace crystal to let them
shine through walls at double the power cost, if the laser in the
pointer is of tier 3 or higher.
qol: laser pointer charge can be seen by examining it
fix: fixed laser pointers luring dead cats when shone upon
code: laser pointer code cleaned up a tad
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[f3fc60ed65...](https://github.com/Steelpoint/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Monday 2023-08-14 16:23:21 by morrowwolf

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
## [aplaice/anki-ultimate-geography](https://github.com/aplaice/anki-ultimate-geography)@[90e1e3dfff...](https://github.com/aplaice/anki-ultimate-geography/commit/90e1e3dfff699da113346e4ae1522ff0c8f5479e)
#### Monday 2023-08-14 17:10:56 by aplaice

Expand SADR country info mentioning alternative names (#570)

Fix #561.

As discussed in #561, saying that "Sahara Zachodnia" (Western Sahara)
is also known as SADR (in the Polish version), is ambiguous and
potentially misleading, since Western Sahara is both the name of the
geographic area (ignoring political associations) and one of the names
used for the partially recognised state.  However, AFAICT, we have the
exact same situation for Artsakh, in Polish, (Górski
Karabach (Nagorno-Karabakh) also known as Artsakh, where
Nagorno-Karabakh can refer both to the country and the geographical
area.).  Also, since we're generally dealing with countries, here, it
should be clear that we mean Western Sahara (the country) rather than
WS (the area), so I think my initial worry was overblown.

I'm not 100% sure if I have the correct gender for conosciuto in
Italian (should it agree with Repubblica.. or with stato?).

The same question holds for Czech — should známý agree with
..republika or with stát?

I've gone with agreement with stát for Czech (male) and with
republic (female) for Italian, because in the former the second clause
is separated only with a comma, while in the latter it's separated by
a semicolon.  The choice of separator was based on precedence in other
cases (Faroe islands and Taiwan).

---
## [Pariah919/TerraGov-Marine-Corps](https://github.com/Pariah919/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/Pariah919/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Monday 2023-08-14 17:59:39 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [DalasNoin/langchain](https://github.com/DalasNoin/langchain)@[75fb9d2fdc...](https://github.com/DalasNoin/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Monday 2023-08-14 19:16:29 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[66b8748091...](https://github.com/Rex9001/Rex_Tg/commit/66b87480915434f1184ac257c9ed0f1f3fe87c58)
#### Monday 2023-08-14 19:27:10 by carlarctg

Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races. 

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[87f707dfa8...](https://github.com/Rex9001/Rex_Tg/commit/87f707dfa8dd901310f72585c6f701035bc653ee)
#### Monday 2023-08-14 19:27:10 by DeerJesus

Adds the Storage Implanter to the spy kit. (#77452)

## About The Pull Request

Adds the storage implanter to the spy kit to make it decent.

## Why It's Good For The Game
This PR hopes to bring Spy at least a little more in-line with the rest
of the syndie-kit specials, so it doesn’t feel like a complete dud to
get.

Spy absolutely sucks as a syndie-kit and getting it is basically
throwing away 20 TC. Not all of them should be equally powerful but all
of them should be at least more satisfying to get. Spy is so bad that
it’s listed in the official wiki as ‘honestly not that good’. It’s also
_barely_ even above 25 telecrystals as the switchblade is a black market
uplink item, not a syndicate uplink item, and not even that good of an
item at that! And the chameleon kit inside isn’t even a full chameleon
kit! Pitiful. Compare it to stealth right below it which totals to _36_
telecrystals.

Adding a storage implant adds a relatively useful item to the kit that
still fits with the entire theme of ‘stealth and deception’, as you can
be searched without having anything on you. To be stealthy, and deceive
people. Like you should. Given the fact that searches are quite common.
It doesn’t make it TOO overpowered as the rest of the gear is still ‘not
that great’.


## Changelog

:cl:
balance: added the storage implanter to the syndie-kit tactical 'spy'
kit to make it decent.
/:cl:

Co-authored-by: oilysnake <63020759+oilysnake@users.noreply.github.com>

---
## [ABS-Helmet/tgstation](https://github.com/ABS-Helmet/tgstation)@[dc0e5caca7...](https://github.com/ABS-Helmet/tgstation/commit/dc0e5caca763769242fe9254d95049ac0468bf64)
#### Monday 2023-08-14 19:29:48 by Sheits

Base Female sprite tweaks (#77407)

## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite 

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs


![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)


## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

---
## [ABS-Helmet/tgstation](https://github.com/ABS-Helmet/tgstation)@[3dc75f84f2...](https://github.com/ABS-Helmet/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Monday 2023-08-14 19:29:48 by YakumoChen

Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#77174)

## About The Pull Request

Authored with help and love from @Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---
## [ztrottie/minishell-42](https://github.com/ztrottie/minishell-42)@[739e365e6f...](https://github.com/ztrottie/minishell-42/commit/739e365e6fb72b72793a9cce64e6676a054f7f9a)
#### Monday 2023-08-14 19:32:33 by selfix123

Merge pull request #42 from ztrottie/unset

fuck you criss de projet de marde

---
## [racckun/site](https://github.com/racckun/site)@[037e847ba1...](https://github.com/racckun/site/commit/037e847ba11dfa0b920bd88579aa138955ad330d)
#### Monday 2023-08-14 20:43:35 by raccoon

There once was a ship that put to sea The name of that ship was the Billy o' Tea The winds blew hard, her bow dipped down Blow, me bully boys, blow (huh) Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go She had not been two weeks from shore When down on her, a right whale bore The captain called all hands and swore He'd take that whale in tow (huh) Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go Before the boat had hit the water The whale's tail came up and caught her All hands to the side, harpooned and fought her When she dived down below (huh) Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go No line was cut, no whale was freed The captain's mind was not on greed But he belonged to the Wellerman's creed She took that ship in tow (huh) Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go For 40 days or even more (ooh) The line went slack then tight once more All boats were lost, there were only four And still that whale did go Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go As far as I've heard, the fight's still on The line's not cut, and the whale's not gone The Wellerman makes his regular call To encourage the captain, crew and all Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go Soon may the Wellerman come To bring us sugar and tea and rum One day, when the tonguin' is done We'll take our leave and go

---
## [AzerothWarsLR/WarcraftLegacies](https://github.com/AzerothWarsLR/WarcraftLegacies)@[b90e5aa63d...](https://github.com/AzerothWarsLR/WarcraftLegacies/commit/b90e5aa63d8044e4dbd78809d789f0d9018077c9)
#### Monday 2023-08-14 20:52:39 by Technopig1992

Scourge changes3.6.2 (#2019)

* ATCBTN's Invoke Spiders

Added ATC Icons for Invoke Spiders ability on both Gilneas and Druid's Invoke Spiders ability

* Minor Holy Light (sunfury)

Changed Minor Holy Light ability:
Changed name to Crimson Renewal.
Changed special visual effect to a red alt of HolyLightSpecialArt.
Changed ICON to  fit in line wtih above changes.
Changed associated tooltips.

* Lordaeron Changes for 3.6.2 + Misc

Reduce level of Dark Wizard creeps 8>6.
Silverhand squire build time 7s>5s
Reduced total  strength Uther loses after Capital Palace is destroyed.  -25>-15 Strength.
Uther base Strength reduced 43>40
Reduced Lord Barov’s Damage 150>120.
Uther’s Devotion Aura armor bonus reduced 2.5>2.5, 5.5>4.0, 7.5>6, 10>8.

Other:
Lowered dark wizard level 8>6.
Lowered death revenant level 9>7.
Added 2 x improved rocket towers at Goblin starting base.
Added  1 x rocket tower at Goblin starting base
added 1 x Burrow for Goblin at starting base.
Added 3 x Improved Gaurd Tower at Zal'farrak for Trolls

* ScourgeChanges3.6.2

Unholy Frenzy ability added to Necromancer
Skeletal Warrior stats changed:
Base attack increased 11>16.
HP increased 300>500.
Base defense lowered 2>1.
Skeletal Mage stats Increased:
Base attack increased 11>15.
HP increased 300>450.
Death Knight stats increased
Base damage increased 33>36.
HP increased 1350>1550.
Base defense increased 3>4.
Death Pact hit points converted increased 100%>125%.
Death Pact cast ranged increased 800>1000.
Essence of Blight hit points restored increased 18>19
Essence of Blight cast range increased 250>275.

Other:
Personal Tank mana increased 0>1250

---
## [ztrottie/minishell-42](https://github.com/ztrottie/minishell-42)@[600d950a24...](https://github.com/ztrottie/minishell-42/commit/600d950a24889243f221a3f045c5a8338cf36a5c)
#### Monday 2023-08-14 21:03:01 by Zackary Trottier

Merge pull request #46 from ztrottie/fuck-you

criss de marde

---
## [rayzchen/pyeod](https://github.com/rayzchen/pyeod)@[72bc9786aa...](https://github.com/rayzchen/pyeod/commit/72bc9786aa325730d1426168199ce1311bd1e53f)
#### Monday 2023-08-14 21:30:50 by Cheesy-Brik

Add commenting elements

We should really refactor the packing methods, kinda a pain in the ass to use rn.
Too much boilerplate imo

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[385ab7a166...](https://github.com/afirpo/tgstation/commit/385ab7a1667250947d480725949bec924ce4ac8a)
#### Monday 2023-08-14 22:08:54 by Pickle-Coding

Changeling armblade gets 35% armour penetration + better wounding. (#77416)

## About The Pull Request
Gives the changeling armblade an armour penetration of 35%. Sets their
bare_wound_bonus to 10 (from 20), and a wound_bonus of 10 (from -20).
## Why It's Good For The Game
The wound bonuses basically gave massive punishment if they attacked
anything but the skin. It honestly felt kinda lame. The better wounding
potential will help bring a bloodier and more exciting atmosphere when a
changeling whips out the blade.

The armour penetration will help reduce dragged out fights that get a
little silly, while keeping the wounding more consistent.
## Changelog
:cl:
balance: Changeling arm blade has an armour penetration of 35%.
balance: Changeling arm blade has a wound bonus of 10, from -20.
balance: Changeling has a bare wound bonus of 10, from 20.
/:cl:

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[38235dce1d...](https://github.com/afirpo/tgstation/commit/38235dce1d1644be32d1758dcc18734a17e61b1d)
#### Monday 2023-08-14 22:08:54 by carlarctg

Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5abafddaea...](https://github.com/tgstation/tgstation/commit/5abafddaea2373b5e367a7ac658d6cab6499b70c)
#### Monday 2023-08-14 22:11:31 by carlarctg

Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [TeshariEnjoer/FluffySTG](https://github.com/TeshariEnjoer/FluffySTG)@[de855cbd7b...](https://github.com/TeshariEnjoer/FluffySTG/commit/de855cbd7ba68b36713c0d9ba3f93de1d9d237ee)
#### Monday 2023-08-14 22:24:22 by SkyratBot

Science Resprite! (With Sovl!) [MDB IGNORE] (#22861)

* Science Resprite! (With Sovl!) (#77314)

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

* Science Resprite! (With Sovl!)

* Update vending.dm

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [chinmay54321/credit-repair-service](https://github.com/chinmay54321/credit-repair-service)@[2a0659d094...](https://github.com/chinmay54321/credit-repair-service/commit/2a0659d094b86f76eaf1b7f287f2ee82bdc5145d)
#### Monday 2023-08-14 23:05:17 by chinmay54321

Update README.md


With the increasing power of interest rates today, it is essential for most people to rely on their cash. Whenever there are things that mainly determine their needs or wants, it is easier for them to acknowledge and understand that using cash is better. However, some problems related to cash might be a problem; thus, using a credit card is a convenient way to use it daily. 

A credit card was already proven that having it is helpful and can quickly bring a supportive hand whenever the consumer is in need. It is also convenient to use as you can easily have a great source to pay for what you will have with the money you worked hard for. Yet, it is best to be aware that having it can also be a disadvantage for you which may lead you to a poor credit score and negate your purchases in the future. In the end, you don’t have to worry anymore, as credit repair assistance is there to help you and bring positive results for your credit. 

Some may be wondering what are credit repair services as it is worth mentioning in every credit transaction. It is worth mentioning as it brings good credit repair companies to be seen amidst the busy and occupied world we have today. Through time, good credit repair companies became popular as they quickly gained recognition and helped most consumers regarding their credit problems. Because of the excellent reputation good credit repair companies are bringing today, people gain confidence in using their credit cards again. Because credit repair assistance is relevant to be seen in today’s world, it is slowly becoming essential in a busy yet occupied world. With the good credit repair companies are doing, it is now a better world and perspective for people regarding their credit. They became wiser and eager to learn more about how to use it properly along the way. They needed it for most of their purchases in life. 

From wondering what are credit repair services to how I can enjoy more of life with the credit, I have today. It is a good thing that people are now gaining the confidence they have been working on from the day they earned money until they are capable enough to have a credit card under their name. Indeed, it was an accomplishment yet, fulfilling moment for a credit card holder to gain that confidence over and over again. Ultimately, it completes how you want to live your life, along with the goals and promises you entrusted yourself with. https://creditrepairnow.ca/

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[07899ea877...](https://github.com/sarcasticadmin/uronode/commit/07899ea87781aa2093a938a660601fa0ff716e25)
#### Monday 2023-08-14 23:14:22 by n1uro

11/05/2013 v2.0
Clean up of some code... I had a copy of 1.0.8 from 2008 I recovered. I did
have a version 1.0.9 in production but can't seem to locate it for some
reason so starting from memory using 1.0.8. Thanks to Brett WA7V for
supplying me with some teaser code :-)

Updated version! We're on 2.0... finally! (yea, big news right? Maybe
not!)

Moved the "Who" commmand to the list of basic internal node commands.
I can't recall why on earth I had it defined with MOTD. Perhaps it may
come to me later but for now I can't recall. I may have to move it
somewhere else, but I believe it has to do something with logging
features or something along those lines. For now, you need to define
MOTD as a compile selective to have the <Who (call)> defined.

Fixed the sysop shell warning, this needed to be a tad more specific
in my point of view... then again who am I? Also cleaned up the return
prompt as it could be confusing if the incoming connection was done via
NetRom. I removed the default FlexNet Identifier out. Now it just says:
"Welcome back.".

In regards to the "Who" command; I see what was going on here and where
I left off with it! Logging and the "Who" command pretty much go hand in
hand - so they're combined. The initial design of FlexNode was to have a
MOTD based off of the logging of when the user last was on, otherwise if
they did not exist, push the "new user" screen to them. The down and
dirty quick fix is to simply remove it from netrom connections into the
system! Who cares if you get a MOTD on a flex/ax25 or a telnet connect
into the system!

With the above said, I changed the sequence of "configure" to ask if the
sysop/admin wishes to log user connects into the system. In the future I
will either move this to be included with protocols or I may simply hard
code it in as a defaulted option, and move the "Who" command as being
defined into TCP/IP functions. For now, it's hard coded in as a selected
option but will NOT display for NetRom connects.

While I was at it, I changed some of the routines in the configure script.
Nothing major but did improve upon a few things. While doing this, and
running "make upgrade" I noticed that flexd.conf was being overwritten!
OUCH! I'm surprised this went on for as long as it did. I *think* I did
this to force people to add the new lines in flexd.conf that K2BJG/SK had
asked me to do.

Created a man page for flexd.conf(5)! I'm surprised no one asked me why this
was missing! It explains further how to create the file. Keep in mind, this
also works on Xnet as well as Flexnet. If this doesn't help you figure out
how to create this file or edit the sample one... I don't honestly know what
to tell you. In doing such, it also forced me to change the generated
Makefile so that "install upgrade" and "install man" installs it.

Changed the licensing! This is (I'll admit) very personal and _must_
remain as is! I could fill a TB hard disk with reasons and debates
as to why it's no longer GPL code. Please insure you are in an area
where you can use this code. Thank you.

Fixed an ANSI bug I had in the "Users" command which was driving me nuts!
On NetRom, it would change the prompt to magenta which it shouldn't. What
I did as a fix was to force a removal of ANSI on the prompt for NetRom
based connects... simple enough. There may be other ANSIs for me to fix
and I'll cross those bridges when I get to them. Found another in gateway.c
and fixed the netrom ANSI to properly reflect that once a connection was
made, it was "systems GO" (green) without changing the Node's ID string.

Created a COLORS file which somewhat explains the hows/whys of not only
how I came up with a schema, but when it should and should NOT be used. It
may also be used as a quick reference guide for the local sysop. It's a nice
little cheat sheet one may print and keep near their keyboard if they want.

Added text to both the colors.hlp and help.hlp file for a users better
understanding of the color schema and how to gain colors to their terminal
if they so choose to have it. See my wishlist below for more information on
where I wish to go with this.

Added an item to the Wish List located further below in this file. With so
many spend-thrifty hams, do I really need to go through the code and match
it with the most up-to-date version(s) of GCC for compiling? I originally
developed the code using GCC version 2.95, now I'm compiling it on version
4.2.4 and it's not showing any errors during compile. If you have a specific
version of GCC you're using, please submit that and proper hardware for me
to run it on and I'll be more than happy to march forward :-)

Changed the inactivity timeout message so that it does NOT show
the FlexNet node call and gives a more specific message as to why the user
was disconnected. This was a call I originally edited and have now cleaned
up in node.c. There may be more of such messages. I can only test so much
and for so long :)

Made some more ANSI cleanups - in regards to Status and Users commands. I
had them as magenta and they should only be bright white as they don't
fit into any real category except for local system informations. For these
I had to make routine changes as well as ANSI changes in user.c and in
command.c. Also fixed the ANSI for version in NetRom. It currently had none.
This was done in command.c. Also cleaned up Links and Routes ANSI in command.c
and other places where needed. Originally I had the Routes as yellow which
even though it points the ax25-interface that NetRom is encapsulated under,
it's really more for NetRom "route"-ing... so changed it to cyan to keep with
the schema.

Found a disaster in ANSI routines for the Links command and the variant
switches along with it! The ANSI ran to the table which I did not want
to have happen and I believe I was very diligent in cleaning this up
in ver 1.0.8 or 1.0.9. In any event, I recall doing this and now I have
repeated my work... thus taken time away from more important tasks *sigh*.
These were worked in router.c. I also cleaned up other places where ANSI
ran over other strings that it shouldn't, and where it may have engaged
prior to where it should. Such instances are when it would highlight over
the Node-ID string (ex: MYNODE:mycall-5}). This really made my skin crawl
and I *know* I fixed this before... who knows perhaps I made a cleaner
routine than I had.

I recall doing a LOT of code clean-up, and it appears I need to revisit this
again. When I'm done, hopefully I can get rid of a few hundred lines of code
that's simply commented out for testing purposes only. The sizes of your
binaries should not be affected by this and I believe I've been diligent
to clean up the configure script to somewhat automate this process for you.
This task will be excessively time consuming! If anything it'd be an excuse
for a maintenance release!

Fixed a minor routine in ipc.c in regards to the Msg command. I deliberately
did NOT add ANSI to this because in a way the Msg command I feel is a tad
intrusive such as with an instant message, however I did clean up how an
incoming message was handled to the recipient. It now (in my opinion)
shows a cleaner screen.

I found Craig Small's old axdigi code and made an elf compile. In layman's
terms, it's a static binary and should run as-is for you. This binary
claims to be fully automagic in regards to crossport digipeating unless you
make changes to your interfaces in which you should restart it. This binary
also should NOT require /etc/ax25/axdigi.conf anymore. I have the other
binary so if you think you need it, let me know.

Added an install for axdigi in Makefile.in under "install bin".  Previously
this file was not included, now it is. I may write a shell script to launch
the daemons for you... keep an eye on this file for further info!

------

Known Critical Bugs:
(see below 3 lines)

Known NON-Critical Bugs:
** Wow! I don't think I have any now ** :-)
{but I'm sure I just jinxed myself!}

Wish-list:
GCC updating? Is it necessary??
Auto ANSI detector
Who file sorter
-----------

Development Information (aka Disclaimer):
URONode is developed on an IBM eSeries 330 eServer with dual 1.2GHz CPUs
The OS is Debian Linux 4 using kernel 2.4.27, libax25 v0.0.11,
ax25-tools v0.0.8 and ax25-apps v0.0.6. This software comes with
absolutely NO guarantees so crash n burn at your own risk. We all may
be surprised and find out that it actually DOES something useful!
URONode may not run 100% depending on environmental conditions specific
to your system.

------------

Comments/suggestions? email: brian@support.uroweb.net
Gripes??? cat gripes > /dev/null :-) just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.uroweb.net/pub/ax25/

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[c00f3e84dc...](https://github.com/sarcasticadmin/uronode/commit/c00f3e84dcc98f552da2ee19e1175714c5c3282d)
#### Monday 2023-08-14 23:14:22 by n1uro

26/05/2013 v2.1

Fixed a bug in gateway.c where the finger "stop" ansi was white instead
of red (for stop). This was one I missed not having proper routing yet
to fully test. Thanks Brett WA7V for the link!!

Made another change in gateway.c in regards to the handling of the
flexnet destinations listing when using Flex/AX25 ONLY. There is a
reason for this (believe it or not) and that's in the shell and netrom
interfaces they both begin the destinations list with the string
"Flexnet Destinations:". This may cause neighbor URONode/AWZNode/etc
systems using flexd to improperly parse flexnet destinations from each
other. At the moment, I don't have the facilities to properly test this
but am hoping to work something out.

Thanks to Bob K2JJT, I added an include for socket.h in ipc.c. While I
never saw any errors here, I don't believe I've ever tested or compiled
on a Slackware system... Bob uses Slack. K2JJT reported adding this to
ipc.c helped him fix issues with his compile as it was griping about
AF_NETROM. Adding it here made no difference so since it helps Slackware
I'm all for being multi-distro compatable as much as humanly possible.

In reviewing 2.0 changes, it had me look more into the shell function
for sysops. I made a change that more defines which shell you may be
in when you do a 'w' or a 'who' in a linux shell via the node. This
was changed in system.c

Made a patch to node.c where if called from a shell, it would coredump.
Now, if it's called from a shell it simply exits back to the shell
prompt. I believe the same is in other "node" variants to which
the documentation directs the local sysop not to call the node from
a prompt, however KI6ZHD felt this was an issue. Being harmless in
nature to the function of my design I felt it wasn't harmful to add
it in. This patch was provided by David Ranch KI6ZHD. Thanks to him
for providing this, and eliminating any accidental core files on your
hard drives, and to Steven, K6SPI for coding the patch.

Thanks to David KI6ZHD for motivating me to do something I wanted to do
but put it way on the back burner, and to Barry K2MF for his elite C
skills. MHeard now will only print up to the 20 most recent heards. With
the initial routine, it would just dump either the global list heard
or if the user selected a specific interface the entire list for that
interface. At first, it worked fine for telnet and/or ax25/flex
connections but in NetRom it was double spacing. This was fixed by me. I
chose 20 to leave room for system headers and prompt returns. In a
standard 80x25 terminal screen, with a full listing, this should fill
the entire screen without a need for the end user to scroll up and
should help keep some traffic down on a busy network.

Made a change in gateway.c to eliminate the "trying state" message only
in NetRom when trying to connect to a remote NetRom node. This should
keep the node more in compliance with Software2000 specifications.

There was chatter within the BPQ32 user group on Yahoo that URONode was
not releasing any keep-alive timers. Please, this is NOT the duty of
a node Front End to control what the native protocol stack is designed
to do. This is totally sysop configurable. To flag this I strongly
suggest the following be added to your scripts:
echo "600000" > /proc/sys/net/ax25/ax0/idle_timeout
echo "600000" > /proc/sys/net/ax25/ax1/idle_timeout
echo "600000" > /proc/sys/net/ax25/ax2/idle_timeout
and so on... one line for each ax25 interface. This will break the
keep-alive virtual circuit Netrom AND IP will use for transport, and
thus break your IP as well. If you're running IP through an ax25
interface I suggest you leave this defaulted to 0 (disabled).

Rewrote the auto-find routine in gateway.c in do_connect so that first
order of preference for connects searches the destis table from flexd
BEFORE checking the netrom nodes and mheard tables, THEN it will search
for the destination in the netrom nodes if not found in the destis
table and prior to searching the mheard list. If you don't use flexnet,
then this shouldn't be an issue for you. As of this time, I'm unsure
if this would create any bugs if you don't define FlexNet during
the configure procedure. If it does, please file a report on the
online forum at https://www.n1uro.net/forum for me!

Made some changes in util.c and gateway.c in regards to duplicate ax25
route connection attempts. If you attempt to connect twice through the
same path, same call, etc, to clarify the error handling. This was
something I worked with K2MF on in regards to MFNOS. This does not mean
you can't make a connect on the same interface you came in on, you will
get a loop warning but the connect will attempt. If you connect from
the node, and try to connect to <callsign>, loop back into the node,
and try to connect to the same <callsign> again, you will NOT be allowed
to connect. URONode will tell you that a duplicate connection is not
allowed.

Cleaned up the do_routes routine in command.c. Shortened "Quality" to
"Qual" and renamed "Destinations" to "Nodes". After all, netrom doesn't
really use "Destinations", that's more a flexnet thing. Still more
cleanup to do in there *sigh*.

While I was at the do_routes, I noticed missing ansi in do_routes and
do_nodes. This has been fixed (and was previously in 1.0.10). I also
cleaned up the ansi routine in do_destinations in router.c to match
that of the netrom counterpart routines in command.c. Again, this was
done in 1.0.10 *double sigh*.

Rather than include an i686 elf of Craig Small's axdigi cross-port
digipeater which probably would NOT work on a Raspberry PI, I added
it into the Makefile by default. I also added an additional routine
in the configure script to check to insure that this file is made.

I also had to update axdigi.c so that it wouldn't error on the newer
(as if I run newer ha!) gcc. This was done for strcpy so that it
wouldn't produce errors as it does. I suspect in the "OLD" days of
linux/gcc it may have been OK as I consider Craig to be one of the
"village elders" of the packet system on linux.

Added a man page for axdigi. READ THIS VERY CAREFULLY!! To digi through
linux you *must* know some specific information and you might have to
educate your users on how exactly to cross-port digi through you if
they intend to do such. It's not something normally visible to them!
I may add a node-help file on digi...but for now please study the man
page on how. It works and works very slick as I've been testing it for
a couple of months. Mheard also will learn digi paths and use them to
connect to digipeated nodes if need be.

Cleaned up do_nodes in command.c. Shortened Quality to Qual, and the
equivilant of Obs. This will use less chars per line when doing a
node <node> or node * . I've been wanting to do this but saved
it for one of those rainy day things. Guess today was that rainy day?

Cleaned up more code and hope to have it finished before 2.1's final
release. So far I'm doing flexd.c at this point. FYI; code cleanup will
be a 2-fold process. First; I'll be formatting each file so it's at a
level of consistency. Second, things I have commented out for testing
that aren't needed may be permanently removed. I may leave a few things
in in case someone desires to say add a 'Welcome." message to netrom
(which is NOT Software2000 compliant!).

Speaking of which, I see I introduced a bug when ANSI is defined for
a specific user which violates Software2000 specs. I believe I did this
as a fail-safe in the prompt routine however now I see it's not needed
with all the other ANSI cleanups I've done. This change (deletion)
was done in node.c where I forced a shutoff of ANSI upon NetRom connects
only, as NetRom does not display the MOTD.

I rewrote a bit of the reconnect string. The "reconnect" in uronode.conf
should be set to OFF. All connections with the exception of NetRom WILL
reconnect. NetRom defaults to off, however with the {S|D} flags you may
manually request you stay connected. Eventually I will remove this flag
in the file so it will become moot. Please change it now to OFF! This
was done in gateway.c. Previously, these flags were moot in NetRom
connects. With the default to OFF, this keeps the NetRom in URONode
Software2000 compliant. A NetRom disconnect should *never* send any
text back whether it's a user or robot/script. Now a user can request
staying connected to URONode from a incoming NetRom connection. For
clarity sake, this only affects the user IF they connect INTO URONode
via NetRom. The "S" flag works for ax25/Flex/NetRom outbound connects.
A user connecting INTO URONode via ax25/Flex/IP will still automatically
be reconnected after an outbound connect.

N1UAN reports make install fails to install the config files. He's
correct. Changed Makefile.in so that "make install" also includes
make installconf which run by itself will install just the config
files for /etc/ax25.

I'm also working on changing the configure script to have some
"eye candy". This will be a continuing work in progress. You'll see it
as it comes. You will need the package "whiptail" in order to see this
new configuration routine. I don't know if this is standard amongst
ALL distributions, however I do know it comes default in debian and
debian based systems. If this *is* too much of an issue, I'll revert
back to the old method.

Almost forgot about an ANSI bug in extcmd.c where if you created an
external command in the node and the user was in via NetRom, when the
node issued "Welcome back." the ansi did NOT clear the color. I found
this in ver 2.0 and thought I fixed it, apparently not (age catching
up to me?) In any event, this is now fixed and working properly again.
Since most people don't use the +512 Color flags I'm sure it was missed.

Found a non-critical bug in cmdparse.s in regards to running external
commands - where it would automatically input a line feed before it
executed the command. This was the only routine which did this. A
routine like this really got under my skin and I was determined to find
and fix this finally... this was a routine I never changed, and that
was halted today (28 July 2013). Instead of totally removing this line
of code, I changed it to now display "Executing command... " and where
ANSI is defined, it is, naturally, green.

Found a non-critical bug in the Info command where it would show as
the first string to the user: "Help command for help" then it would push
the uronode.info file. This is very wrong. While the Info command does
use the routine of do_help in command.c, Info is an independent internal
command and this should not have occurred. This is now fixed with ANSI
if permissions display ANSI.

Updated the outdated INSTALL text document. It had some now misleading
pieces of information in it as some paths and make options have been
changed. Since no one has said anything to this, I'll assume no one
RTFM? (not surprised! email me and say in the subject line: surprise!
if you do!)

Went through the example config files and heavily commented them so for
new installs, it explains each line more specifically in hopes less
misconfigured systems will be created. I also found some typos as to
man page references - fixed. Also updated some of the help files in
regards to the new changes in relation to the "stay" sub command when
connecting out from URONode.

Note: in node.c I modified the pre-provided segfault patch to now
push text to the local console instructing the local sysop or user
what/how to properly execute the node. This will (I hope) force
some RTFM to occur. Syslog logging was also added in the event this
occurs. Actually, after thinking about this, I figured I'd dummy it up
a bit and have it launch a login anyway. This depends that the local
administrator/sysop -properly configures their box- and does the
following:
1 - add a line in /etc/services to point tcp/3694 to uronode
2 - add uronode as a service in inetd or xinetd
3 - insure you have a local telnet client on the box
4 - enjoy!
You will be reminded about this during the login, and syslog will
reflect a local console login as well.I strongly urge you not to open
2 shells and tail your syslog in one while you try to run URONode from
the console. Wink

Cleaned up a minor routine in do_nodes which lays in command.c where
under an incoming NetRom connect, a user who did "Nodes" received
an extra line feed if the columns were all equal at 4 per row. This
was a bit under my skin... fixed/changed. While I was at it, I changed
the output string when doing "Nodes *" from 'Nodes:' to "Detailed
nodes listing:' which actually makes more sense since it is a detailed
list.

Fixed a minor bug in the way the prompts were handled under certain
telnet clients. This was reported also by Marius Petrescu yo2loj. Under
telnet, I added a carriage return (/r) along with the line feed (/n).
Thank you Marius for the report.

In doing the above, I made an error in the non-ANSI telnet prompt where
the (/r) was also chopping off the first letter of a callsign! OOPS!
This was reported by Ted K1YON. Fixed.

Slightly rewrote the way meminfo() was being handled. While I may have
created a bug in 2.4 and lower kernels, this now should work in 2.6 and
higher kernels. I guess the phrase "if it's not broke don't fix it"
doesn't apply anymore?

FINALLY - split the CHANGES file into a new page!! This makes it easier
for me to input the change notes instead of having to scroll down for 30
seconds Smile Call me lazy but don't call me late for supper! <G>

04/09/2013 v2.2

Made multiple .c file edits to reflect the new libax25-devel .h files.
Currently these were pointing to the older kernel_*.h files and on newer
linux systems was preventing compile. Now URONode should work fine.

Added Marius Petrescu to the URONode team! With his c version of ripv2d,
Marius will (and already has) make a huge impact on the future of
URONode! Welcome Marius to the team! Made a reflection of this in the
configure script.

Marius brought to my attention the issue in the log timer routine where
it was forcing 32-bit. He supplied code to fix this in both system.c and
flexd.c.

While in discussions, Marius brought it to my attention that Ubuntu (and
this includes Mint and any other Ubuntu backed distributions) where they
run as he calls it a "fortified libc6" which segfaults on every (what it
thinks is suspicious) buffer accesses to prevent overflows however this
libc6 itself causes buffer overflowing. Why on earth did the Ubuntu team
ever do this?? Anyway, we're investigating how we're going to handle
this issue. I personally have verified URONode to compile and work on
the new kernel 3.x series on Debian and Fedora.

Known Critical Bugs:
(see below 3 lines)

Known NON-Critical Bugs:
Status memory/swap reporting fix

Wish-list:
Who file sorter
pactor - requested by sv1uy
-----------

Development Information (aka Disclaimer):
URONode is developed on an IBM eSeries 330 eServer with dual 1.2GHz CPUs
The OS is Debian Linux 4 using kernel 2.4.27, libax25 v0.0.11,
ax25-tools v0.0.8 and ax25-apps v0.0.6. This software comes with
absolutely NO guarantees so crash n burn at your own risk. We all may
be surprised and find out that it actually DOES something useful!
URONode may not run 100% depending on environmental conditions specific
to your system.

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org
Gripes??? cat gripes > /dev/null Smile just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[9306979a7c...](https://github.com/sarcasticadmin/uronode/commit/9306979a7cf3be455ea0e44474de5cb732b7b52d)
#### Monday 2023-08-14 23:14:22 by n1uro

04/09/2013 v2.2

Made multiple .c file edits to reflect the new libax25-devel .h files.
Currently these were pointing to the older kernel_*.h files and on newer
linux systems was preventing compile. Now URONode should work fine.

Added Marius Petrescu to the URONode team! With his c version of ripv2d,
Marius will (and already has) make a huge impact on the future of
URONode! Welcome Marius to the team! Made a reflection of this in the
configure script.

Marius brought to my attention the issue in the log timer routine where
it was forcing 32-bit. He supplied code to fix this in both system.c and
flexd.c.

While in discussions, Marius brought it to my attention that Ubuntu (and
this includes Mint and any other Ubuntu backed distributions) where they
run as he calls it a "fortified libc6" which segfaults on every (what it
thinks is suspicious) buffer accesseD to prevent overflows however this
libc6 itself causes buffer overflowing. Why on earth did the Ubuntu team
ever do this?? Anyway, we're investigating how we're going to handle
this issue. I personally have verified URONode to compile and work on
the new kernel 3.x series on Debian and Fedora.

In "fixing" the prompt bug earlier reported by Marius, I made an error in
the non-ANSI telnet prompt where the (/r) was also chopping off the first
letter of a callsign! OOPS! This was reported by Ted K1YON. Fixed.

** Key news of this release: ROSE is a LOT more user friendly, AND it also
has the ability to display color screens to the end user. This now means
that URONode is an 8-prompt system! 4 main prompts, and 4 color prompts.
The prompt system is designed to show the end user what protocol/method
they used to connect into URONode with. Also proper SSIDs are displayed
to match that of how the end user connected. I did this because seeing
other nodes, they don't and when (as a user) connect into, for example,
a NetRom node who's ssid is -12 and the node displays something
-=totally=- different, I often wonder if I connected to the proper node.

The new prompt schema is:
telnet   :	user@<sysop>.ampr.org:/uronode$
netrom   :	<none> - this keeps in spec with Software2000
flex/ax25:	=>
rose     :	-=>

Each matches with its own colors as well if you run the ansi flag. The
goodbye message for rose is also different than it is for flex/ax25 and
telnet links. The new RoseID flag is used as a personalized message to
the remote user to say a nice goodbye, and to remind them of your Rose
information. The (V)ersion command also has a rose column added to show
the remote user your rose information. An example of this is included
in the uronode.conf.5 man page.

With such, a new uronode.conf file string called RoseID has been created.
Details are in the file. You must keep the single quotes ' ' around the
string for it to display properly. You have been warned. Also, I've added
a default ExtCmd called ROSe so those who connect remotely can get rose
addresses for now. I'm sure I'll be changing this in the future.

Also, I decided to eliminate the permissions flag for use of hidden interfaces.
Reason being is if a sysop flags an interface to be hidden, they did so for a
specific reason. With that, I moved the ANSI flag from 512 in it's place to
64. This was also changed in the man page uronode.perms.5.

In regards to PBBS forwarding, I -=URGE=- you to read BBS.txt. Since
there's no need for me to rewrite it, please heed my warning here. This
is not something critical, just informational to help you improve your
link with URONode systems.

Fixed a cosmetic bug in regards to windows->linux emulation where when
logging in, sentences were not getting properly wrapped. This was done
in node.c. Other emulations such as PuTTY do not give you in windows
full linux-type emulation. Higher profile programs such as SecureCRT
will. For a free/shareware program I suggest MobiXterm. This also
gives you a raw Xserver emulated screen. Of course, there are no issues
if you use a standard linux console.

Added a .pid file to flexd, code supplied by Jaroslav, OK2JRQ and other
patches such as installer edits, etc. The only patches he supplied that I
have yet to add is the install location patch, and one he feels is good
for non-interactive. Source installs need to be interactive, if not you
would not be compliling - just my honest opinion. I can see in the case
of a possible distro package this may not be desired. The distros for now
can hash that out on their own.

Many more cosmetic bugs fixed/changed. Moreso in ROSE but I did find a
few others in there which needed my attention. I have noticed windows terminal
based programs such as PuTTY have an issue determining \n based line feeds
vs \r carriage returns in C code. This mainly seems to affect the various
8 prompts. It seems if I put both in the code, Windows is happy but *nx
may issue an added line-feed. I had thought I cleaned these all up but
I introduced a couple old ones and some new ones with the ROSE work.

01/10/2014 -2.2 released!

Known Critical Bugs:
SYSop command does NOT spawn a shell anymore. This is due to the changes
with the UNIX98 file system. I'm debating on whether or not I wish to
continue to keep this or possibly eliminate this (for possible security
reasons). I see both PROs and CONs with it. Note: this ONLY affects those
systems which force the use of /dev/ptmx in which one needs to use SOCAT
to create static /dev/tty*# and /dev/pty*# pipes. This only affects the
Kernel 3-series

(see below 3 lines)

Known NON-Critical Bugs:
Status memory/swap reporting fix

Wish-list:
Who file sorter
pactor - requested by sv1uy
callsign sort in netrom - requested by ve2pkt
-----------

Development Information (aka Disclaimer):
URONode wass developed on an IBM eSeries 330 eServer with dual 1.2GHz CPUs
The OS is Debian Linux 4 using kernel 2.4.27, libax25 v0.0.11,
ax25-tools v0.0.8 and ax25-apps v0.0.6. This software comes with
absolutely NO guarantees so crash n burn at your own risk. We all may
be surprised and find out that it actually DOES something useful!
URONode may not run 100% depending on environmental conditions specific
to your system.

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org
Gripes??? cat gripes > /dev/null Smile just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet

Join our support mail list graciously donated by TAPR!
http://www.tapr.org/mailman/listinfo/uronode

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[620de5f710...](https://github.com/sarcasticadmin/uronode/commit/620de5f710c5abf3581a60a3b5f6c0e1de61a8ca)
#### Monday 2023-08-14 23:14:22 by n1uro

18/04/2016 - v2.6
Removed stale and unused axdigi.conf file. Thanks to David KI6ZHD for
pointing this out that I had a stale file in the archive. This file
belonged to another digi daemon I was going to revive instead of Craig
Small's multi-interface crossport digi daemon. I find that especially
with FlexNet, a multi-interface crossport digipeat system not only is
unique to the native linux kernel BUT is also very efficient. If you
have a stale copy of axdigi.conf floating around, please delete this.

Added a question to engage or disengage interactive configure/make mode.
This idea came to me from a query I received by KI6ZHD. If you choose NOT
to use interactive mode, than you must run make/make upgrade/make install
manually. Note: ALL options including rose and flexnet WILL BE COMPILED IN.

Tomasz SP2L was seeing carriage returns when administering his server
remotely and sending SIGHUP to flexd in the terminal messages confirming
the -HUP. Removed.

Added a version output for FlexD and tweeked the one for axdigi. Now both
helper daemons will display its versions based on URONode's version and
some very brief information about themselves. flexd -v or flexd -h
along with axdigi -v or axdigi -h will bring up this information.

Decided that since there's so many commands beginning with M I would move
the MHeard command to a Jheard command. This keeps the commandset more in
line with other systems except for TheNet and X1J-4, and separates that one
command away from the volume of M's. While at it I also made a JL for
Just heard Long. If you specify an interface, Jheard/JLong engages only for
that interface. Note - JLong will say: it may time out HFers. I also had to
modify Makefile and rework the help files to match. While at it I needed to
modify the uronode.8 MAN page.

Gave Makefile a more modernized compile line option. I'm hoping this will
keep URONode one of packet's better robust nodes.

I noticed some sites were violating Software2000's NetRom specifications
by defaulting reconnect on still in their uronode.conf files. I had thought
that I fixed this in an earlier release. Perhaps I did and then migrated
an old .c file back into the mix? (wouldn't be the first time I've done
that by mistake!) Anyway... three key things Software2000 was insistant upon
were NO CTEXT, NO RECONNECT, NO GOODBYE MESSAGES. If you've noticed, I've
taken ALL that out of URONode. These things were done as to not confuse
robot scripts such as PBBS mail forwarding sessions. While other systems
may wish to continue to violate the NetRom protocol (and others) I will
do everything in my power NOT to.

An anonymous user from sourceforge had a compiler warning on the
do_prompt cycle in config.c and provided a fix for it. I don't know if
the user is even a ham but their alias is dcb314, and we thank them. Their
report and fix which is included:
config.c:407:35: warning: logical 'or' of collectively exhaustive tests is always true [-Wlogical-op]
Source code is
if ((User.ul_type != AF_NETROM) || (User.ul_type != AF_INET) ||
(User.ul_type != AF_INET6)) {
Maybe better code
if ((User.ul_type != AF_NETROM) && (User.ul_type != AF_INET) &&
(User.ul_type != AF_INET6)) {
While I don't get the warning he had, the logistics seem to be fine. Thanks
again to dcb314 at sourceforge for their report.

I have made a diff file for JNOS2.0K that makes it a bit more user
compatible with URONode, and other linux-based nodes. For almost 30 years
TCP port 3694 has been used for inbound telnet for linux-based nodes, and
URONode is no exception... just as IP protocol 93 is for axip and UDP
port 93 is for axudp (again other systems love to violate protocols, we
try not to). Besides my little isms that I like in xNOS which I often
contributed to K2MF for MFNOS, I've began to do similar for JNOS. I'm adding
the .diff file in the main code distribution so if you do run JNOS 2.0K as
your PBBS TCP port 3694 is now recognized in JNOS with my patch. I have
as of this writing submitted it to Maiko for considerations, I don't know
if he's going to use it or not. If you do want to patch your JNOS 2.0K
copy it into your jnos source directory and run: patch -p1 -i jnos20k.diff
and you should see about a half dozen files updated. If Maiko doesn't wish
to include this and you want me to keep up to date with it, let me know.

With the recent CVE study on Winlink2000 and plain text passwords exposed, I
went through URONode to insure it wasn't posessing the same issue. By
default URONode doesn't ask for ANY passwords however it's highly suggested
that the sysop require passwords on any internet or amprnet interface. Before
yes, a sysop could require a password on an ax25/NetRom/Rose interface which
would be exposed. Now, if a sysop mistakenly tries to force a password
on RF, it will be ignored by the node so it's not exposed.

----------- Note on SystemD --------
In uronode.socket, you'll notice the line:
ListenStream=0.0.0.0:3694
This tells SystemD to listen on TCP socket 3694 for any IPv4 ONLY incoming
connection. If you wish to filter JUST your amprnet and IPv4 localhost
IPs make a line for each changing 0.0.0.0 to 127.0.0.1 and another for
your amprnet IP. This will by default filter any commercial IP requests
to URONode. If you want SystemD to try IPv6 *first*, don't enter in any
IP schemas and just list the port number. SystemD by default appears to
use IPv6 prior to IPv4.

You can verify the above by running systemctl status uronode.socket:
ystemctl status uronode.socket
● uronode.socket - URONode Server Activation Socket
   Loaded: loaded (/usr/lib/systemd/system/uronode.socket; enabled)
   Active: active (listening) since Mon 2016-03-07 15:30:39 EST; 6min ago
   Listen: 0.0.0.0:3694 (Stream)
 Accepted: 3; Connected: 1

----------- Wish-list: -----------
----------------------------------
Original Development Information (aka Disclaimer): URONode was developed
on an IBM eSeries 330 eServer with dual 1.2GHz CPUs The OS is Debian
Linux 4 using kernel 2.4.27, libax25 v0.0.11, ax25-tools v0.0.8 and
ax25-apps v0.0.6. This software comes with absolutely NO guarantees so
crash n burn at your own risk. We all may be surprised and find out that
it actually DOES something useful! URONode may not run 100% depending on
environmental conditions specific to your system.

URONode is GLPv2 code, and tested by it's main author on the following
platforms: Raspberry Pi ver. B, Debian 7.7 on a Core-i3, Ubuntu
12.0.4LTS on a Core-i3, Fedora ver. 21

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org Gripes??? cat gripes >
/dev/null :D just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet and https://uronode.sourceforge.net. You may
also find URONode in your distro's repositories. <dnf/yum or apt-cache>
search uronode

Join our support mail list graciously donated by TAPR!
http://www.tapr.org/mailman/listinfo/uronode

73 de Brian N1URO

---
## [sarcasticadmin/uronode](https://github.com/sarcasticadmin/uronode)@[9726c04b95...](https://github.com/sarcasticadmin/uronode/commit/9726c04b9557573b462d7a77efb0e79f8e80fca1)
#### Monday 2023-08-14 23:14:22 by n1uro

15/06/2017 - v2.8
In gateway.c I cleaned up the do_ping routing slightly. I was going to add
a default timer but instead decided to let the user hit enter for their own
"timer" of sorts. Users are also now instructed on the node to hit enter
in order to abort a ping.

Cleaned up do_nodes so now if there's a slime trail node, rather than prefix
it with a colon ":", now it will display ##TEMP: instead. This was sorta
bugging me on just how to handle these. While I was at it, I made a
modification to gateway.c so if a user tried to "C ##TEMP" it instructs the
end user to use the callsign-ssid. I can't think of any other node that does
this.

Thanks to Dave Hibbard (at Debian) for pointing out a dropped "t" in the word
"software" in flexd.c when the -v switch is used.

Cleaned up some prompt routines including the ipv4/ipv6 login sequences.
Before (especially with ipv6) if a callsign had no permissions to login via
the internet they were never informed how to gain access - they were simply
denied. I found this to somewhat make the node a bit unfriendly. Fixed.

With all the chatter on the 44-net list about IPv6, I've decided to get my
block active for further testing. In doing so, I noticed that if a user
telnetted in via IPv6 and made a NetRom connect out, the node failed to
inform them that they were connected... fixed.

As of this writing there's no outboud telnet or dns functions for IPv6
but that's not to say it's not in the works. Personally, I don't see a
true need for IPv6 outbound for amateur radio as the amprnet is going
quite strong however that's not to say things may not change either. If
anything, IPv6 through an HE.net tunnel works as slick as the amprnet
does with the exception of how it handles dynamic clients. Other than
that, it does appear to tunnel through your ISP filters as amprnet
does which is a plus.

----------- Note on SystemD --------
In uronode.socket, you'll notice the line:
ListenStream=0.0.0.0:3694
This tells SystemD to listen on TCP socket 3694 for any IPv4 ONLY incoming
connection. If you wish to filter JUST your amprnet and IPv4 localhost
IPs make a line for each changing 0.0.0.0 to 127.0.0.1 and another for
your amprnet IP. This will by default filter any commercial IP requests
to URONode. If you want SystemD to try IPv6 *first*, don't enter in any
IP schemas and just list the port number. SystemD by default appears to
use IPv6 prior to IPv4.

You can verify the above by running systemctl status uronode.socket:
ystemctl status uronode.socket
● uronode.socket - URONode Server Activation Socket
   Loaded: loaded (/usr/lib/systemd/system/uronode.socket; enabled)
   Active: active (listening) since Mon 2016-03-07 15:30:39 EST; 6min ago
   Listen: 0.0.0.0:3694 (Stream)
 Accepted: 3; Connected: 1

----------- Wish-list: -----------
----------------------------------
Original Development Information (aka Disclaimer): URONode was developed
on an IBM eSeries 330 eServer with dual 1.2GHz CPUs The OS is Debian
Linux 4 using kernel 2.4.27, libax25 v0.0.11, ax25-tools v0.0.8 and
ax25-apps v0.0.6. This software comes with absolutely NO guarantees so
crash n burn at your own risk. We all may be surprised and find out that
it actually DOES something useful! URONode may not run 100% depending on
environmental conditions specific to your system.

URONode is GLPv2 code, and tested by it's main author on the following
platforms: Raspberry Pi ver. B, Debian 7.7 on a Core-i3, Ubuntu
12.0.4LTS on a Core-i3, Fedora ver. 21

------------

Comments/suggestions? email: n1uro@n1uro.ampr.org Gripes??? cat gripes >
/dev/null :D just kidding!

This version will get you going for now. I'll post any changes to:
ftp://ftp.n1uro.net/packet and https://uronode.sourceforge.net. You may
also find URONode in your distro's repositories. <dnf/yum or apt-cache>
search uronode

Join our support mail list graciously donated by TAPR!
http://www.tapr.org/mailman/listinfo/uronode

73 de Brian N1URO

---

