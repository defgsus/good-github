## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-19](docs/good-messages/2022/2022-12-19.md)


2,216,118 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,216,118 were push events containing 3,221,133 commit messages that amount to 253,692,890 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [maesierra/adventOfCode2022](https://github.com/maesierra/adventOfCode2022)@[e4b29dfea2...](https://github.com/maesierra/adventOfCode2022/commit/e4b29dfea24acaf8816f39795d6f0e2ff5b49248)
#### Monday 2022-12-19 00:41:05 by Maria-Eugenia Sierra

day18

after a surprisely easy part 1, part 2 took me ages becasue I insisted on not doing the right solution, locate the empty spots and try to see (recursively) if it can reach the surface.
I insisted on using ranges or not thinking that I needed the recursion. It's slow as hell as I did not bother to memoize the recursion.

Fortunatelly I decided to use babylonjs playground to help me visualize and it help me a lot  https://playground.babylonjs.com/#9WMURK#3

go rant...
I miss map.hasKey() or contains_key and the ternaries. I don't waste my time in defining a variable every time I want to check if a map has a key.
And the lack of ternaries make me do so many unnecessary variables... yes I know the compiler will inline them, but I have to waste my brain power in
giving them a name. A naming it's a hard problem

Also I miss constructors. Yes, I know I can create a factory method that's effectively a constructor. But

  a) does not offer the security of a constructor to know all the initializations will go by one path. Yes outside your module,
     but inside your module you're not forced to use your initialization method
  b) you need to think on a name
  c) the IDE does not help. I don't remeber the last time I had to create a constructor manually. The IDE will do that for me. So I end up not doing on go because I have to do it manually

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[fe5d6c7b56...](https://github.com/Koshenko/mojave-sun-13/commit/fe5d6c7b568d550f403eb892ed47ffaf6b4fd28c)
#### Monday 2022-12-19 00:48:52 by Technobug14

Agriculture (#2230)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

---
## [mythaxis/mythaxis.github.io](https://github.com/mythaxis/mythaxis.github.io)@[7f31baae60...](https://github.com/mythaxis/mythaxis.github.io/commit/7f31baae60c4e72344ba8bca33ba194c16e170b3)
#### Monday 2022-12-19 01:17:40 by AndrewLeonHudson

Auto stash before merge of "master" and "origin/master"

Made me shit myself, god damn it

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[3775d9e5d1...](https://github.com/i3roly/CMI8788/commit/3775d9e5d1fbacad476f2faff2c725ab5b3c5060)
#### Monday 2022-12-19 01:22:53 by gagan sidhu

you bet your sweet ass it's accessing the mapped memory.

phil told me about this before too. i don't understand what the fuck is going on with legit DMA. it always does this.

mb i should just try to access it using the getaddress call or something.

anyways gonna let my mac take it easy for a bit because spotlight is probably rebuilding and i gave this thing a severe case of alzheimers over the past few hours.

---
## [OliOliOnsiPree/Skyrat-tg](https://github.com/OliOliOnsiPree/Skyrat-tg)@[24ae11ad6f...](https://github.com/OliOliOnsiPree/Skyrat-tg/commit/24ae11ad6f6af9c0b6dab12986b95943f0cdf1f8)
#### Monday 2022-12-19 01:23:50 by SkyratBot

[MIRROR] Adds a reagent injector component and BCI manipulators to all circuit labs [MDB IGNORE] (#17617)

* Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a reagent injector component and BCI manipulators to all circuit labs

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---
## [OliOliOnsiPree/Skyrat-tg](https://github.com/OliOliOnsiPree/Skyrat-tg)@[f4335e5184...](https://github.com/OliOliOnsiPree/Skyrat-tg/commit/f4335e5184da0a4643bab601ae11c59e9d411a6e)
#### Monday 2022-12-19 01:23:50 by SkyratBot

[MIRROR] Fishing Odds Code Improvements and Rescue Hooks [MDB IGNORE] (#17697)

* Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

* Fishing Odds Code Improvements and Rescue Hooks

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[7687a28e7c...](https://github.com/ShizCalev/tgstation/commit/7687a28e7ceecea6b9e0aacdb58a2271b063f9d3)
#### Monday 2022-12-19 01:34:48 by Sol N

refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#71869)

## About The Pull Request

After all, the Syndicate loves a good throwback.


![C6O47fPhAB](https://user-images.githubusercontent.com/116288367/207737104-3d24574f-02e0-433d-8ea7-6825ca4cb970.png)

This PR does a few things with the goal of reimplementing and
revitalizing syndicate traitor kits and the syndicate surplus crate.
Of note is that I have added in a way for limited stock items to share
their limited stock.

Following maintainer guidance the syndicate traitor kits have increased
in price and as a result some of the lower value ones have been
adjusted. I've given all active bundles current TC costs per item
knowing full well they will be inaccurate eventually.

<details>
  <summary>Changes as a result of my audit of syndikits</summary>
    
### UNCHANGED
Recon, Spai, Stealthy, Screwed, Sniper, Nukie Meta, Implants
Mad Scientist, Bees

Lord Singuloth is also unchanged and disabled, I think that it should
turn into a new supermatter themed kit maybe. outside of current scope.

### Gun Kit
Replaced emag with doorjack and gave it a chameleon holster, literally
moved 1 tc elsewhere

### Murderer
replaced emag again, no additions its a lot of tc and Just Good

### Hacker
added doorjack, otherwise unchanged

### Sabotage
no changes other than adding in extra bombs it didnt have

### James Bond
gave him some gadgets with the freedom implant, emp flashlight, and one
x4. also a cyanide pill and deck of cards for fun

### Ninja
Added in miner Jump Boots, smoke spell, and doorjack. dont just want it
to be space ninja

### Dark Lord
Added in new lightning bolt spell granter and made the desword default
to red. probably overbudget.

### White Whale
dehydrated carp added so you can ride it alongside the ones you grenade
out. hard to imagine changing this

### Mr Freeze
changed temperature gun to be cryo only so that i could give him the
cryo thermal pistol. cold attacks only.

### 2006 Traitor
doorjack.

</details> 

tl;dr theyre all about 30 tc worth of shit more or less some are more
but thats what rarity should be for
you can only buy from one type of syndicrate per round


![QOF1WO7CC6](https://user-images.githubusercontent.com/116288367/207739417-00ae6b81-b6aa-4774-a4bb-f2d880988ff4.gif)

Next up is the return of the surplus crate. 
Crate is generated, gives you gear **based on your progression at the
time of buying the crate**, you can use it all at the start and get some
chameleon kits and not a lot of dangerous weapons or wait till later.
I've changed the weight on some items here and there and given weight to
role and species locked items, though I will admit that latter is
unimportant because I set moth lanterns to be unable to appear in these
two crates.


![dreamseeker_t8abXysKqK](https://user-images.githubusercontent.com/116288367/206761978-96e2a51e-f9a5-48e4-a863-a9198fa15ea2.gif)

But who cares about that your eyes instantly went to the United Surplus
Crate and the United Surplus Key lets be honest.

The united surplus crate is 80 TC worth of uplink items relative to your
current progression when you purchase it and gives you a locked box. It
**will explode if you try to break it** so be careful with it. It gives
you 80 TC and costs 20 TC because it is impossible to open without key.
The rub of course is that the Syndicate forbids agents from buying more
than one surplus item of any kind, you need to find another traitor and
make them buy you a key to open your box. Or I guess you can share the
box?


![dreamseeker_ts0AZeiyfy](https://user-images.githubusercontent.com/116288367/207740388-3f688bba-5d71-48d2-8079-671bbed7e54e.gif)

Regardless, if the crate is opened with any other means it doesn't spawn
its contents, you need 2 traitor uplinks.
Both of these items have a 30 minute timer because you don't want a
crate that has 5 emp flashlights in it. You at least want one energy
sword.

I did a lot of code shit and changed various things to be proc based to
allow for more editing and interjection of things, as I wrote in code
comments making a crate thats locked to a specific set of progression
just means changing the proc that generates a list of valid uplink items
to check items' progression values to a specified value instead of your
characters progression.

Ok I think that goes over everything more or less????

## Why It's Good For The Game

I've heard that people liked these and I think they are quite fun, being
able to go from "i dunno what to do as a traitor" to "ah, of course, I
will become the Bombler" is a fun thing to be able to have, and people
like to get a bunch of random shit in the mail. Some of it even feels
free!!!!!!!!!!!!!!!!!!! Brain points go up!!!

The division of procs allows for more creativity with this system than
existed before as well as other possibilities for interacting with the
uplink handler in funny ways.

## Changelog

:cl:
add: the syndicate is once again distributing syndi-kits, some now with
new technology
add: a fresh batch of syndicate surplus crates have been sent out,
though they seem a bit lighter than before
add: in an effort to encourage cooperation, a traitor can now purchase
either the new United Surplus Syndicate Crate or its key, but not both
add: lightning bolt book granter for wizard event and one syndie-kit
bundle
add: temperature gun that only makes things colder for one syndie-kit
bundle
code: it is now possible to have uplink items share limited stock
bal: role-restricted items no longer can be delivered by the stray
syndicate drop pod event
/:cl:

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[6dd4839ef3...](https://github.com/ShizCalev/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Monday 2022-12-19 01:34:48 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.


![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.


![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[00e7d5d746...](https://github.com/ShizCalev/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Monday 2022-12-19 01:34:48 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [VoltageOS-Devices/android_kernel_asus_sdm660](https://github.com/VoltageOS-Devices/android_kernel_asus_sdm660)@[3b55b34cf9...](https://github.com/VoltageOS-Devices/android_kernel_asus_sdm660/commit/3b55b34cf950527df3718c9c902d9eff9618219f)
#### Monday 2022-12-19 02:05:03 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [kingcons/advent-of-code](https://github.com/kingcons/advent-of-code)@[c1cce45fd9...](https://github.com/kingcons/advent-of-code/commit/c1cce45fd9f2434c40073b2e559221a6a303bd4e)
#### Monday 2022-12-19 03:52:29 by Brit Butler

Solve the hell out of day 13.

This problem was an absolute nightmare for me. Was it my code?
No. Somehow I absolutely fucked my input file but it was still
parseable and I saw my code worked for the test data but not
the _actual_ production data and spent waaaay too many hours debugging
before I gave up and redownloaded the input data and sweet fuck am I
ever filled with white hot rage.

I have gone through at least three iterations of the actual code to
solve the issue trying to eliminate any possible place where a bug
lurks. This final iteration is actually the one I'm happiest with anyway.

---
## [kamser/kams-breaking-bad-react](https://github.com/kamser/kams-breaking-bad-react)@[d6243521c0...](https://github.com/kamser/kams-breaking-bad-react/commit/d6243521c03ccfeff6d9ee2c5e532486be8f8824)
#### Monday 2022-12-19 04:12:40 by kamser

Update the fucking shit stupid shitgit statusgit status

---
## [altude/altude](https://github.com/altude/altude)@[748ca335af...](https://github.com/altude/altude/commit/748ca335afedb233556a9b1a9ddcee5e074337cb)
#### Monday 2022-12-19 05:28:20 by altude

I just want relief from my stress

SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, THIS LIFE GOT MY HEAD SPINNIN' WONDER WHAT I'D DO IF I KNEW THESE WERE MY LAST MINUTES WONDER IF I HAD A WEEK TO LIVE, WOULD I STAY TRIPPIN'? WASTIN' EVERY DAY THAT I HAD LEFT TRYNA SELL TICKETS OR MAYBE CALL MY DAD , SAY I LOVE HIM AND LAUGH WITH HIM TAKE A COUPLE DAYS AND GET AWAY FROM THIS FAST LIVIN' I DON'T LOVE MY WORK THE WAY I DID MAN, THIS WHOLE BUSINESS HAS GOT ME FEELIN' JADED FRIENDS I HAD, NOW THEY ACT DIFFERENT, IT'S ALL SWITCHIN', WHOA, IT'S PRETTY HARD TO WATCH THOSE THINGS YOU USED TO LOVE TURN TO THINGS THAT YOU WISH YOU FORGOT REAL MOMENTS THAT MAKE YOU QUESTION THE THINGS THAT YOU WANT'S GOT ME GROWIN' MENTALLY, BUT STRESSIN' ME OUT 'TIL I DROP OVER THE TOP , THAT'S WHERE I LIVE ON A DAILY BASIS I ALWAYS FIND A WAY TO FIND THE BAD IN GOOD SITUATIONS IT'S SAD, HUH?, I LIVE MY LIFE ON THE EDGE, DON'T WANT THE MEDS I'M JUST TRYNA GET RELIEF FROM MY STRESS, YOU KNOW?  SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  THESE STRESS LEVELS ARE NOT HEALTHY I'M WAITIN' FOR THAT CALL SAYIN' RECORDS ARE NOT SELLING I WONDER WHEN THIS ALL DISAPPEARS AND THEY FORGET ME WILL I FEEL LIKE I FOUND WHO I WAS OR BE MORE EMPTY? I WONDER WAS I WRONG THINKIN' THIS IS WHERE GOD LED ME OR DID I GET INVOLVED WITH SOMETHIN' THAT WAS TOO HEAVY? I DRIVE UNTIL I'M LOST AND JUST SIT IN MY CAR YELLING MY INNER CRITIC TALKS, I'M JUST HOPIN' THAT GOD HELPS ME TO STOP STRESSIN'   SOME DAYS I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS, I JUST WANNA LEAVE IT I JUST WANT RELIEF FROM MY STRESS SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS, SOME DAYS, SOME DAYS I JUST WANNA LEAVE, YEAH I JUST WANNA LEAVE, YEAHSOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  LATE NIGHTS, STARIN' OUT THE WINDOW DOIN' 85 GOT MY STATE OF MIND, WALKIN' ON THAT GRAY LINE HOPIN' THAT MY STRESS DIES IT'S LIKE I HATE IT BUT I LOVE IT AT THE SAME TIME PRESSURE PUSHIN' ME FROM ALL SIDES INSECURITIES OF ALL KINDS, I'M A HOSTAGE TO MY OWN PRIDE MOST IMPORTANT THINGS IN LIFE TO ME ARE THINGS I KNOW I CAN'T BUY AYY, YEAH, IT'S ME IN PHASES I'M NOT IN THE MOOD, YEAH, TO MEET ANOTHER STRANGER I'M NOT IN THE MOOD, YEAH, TO HAVE A CONVERSATION AND TALK ABOUT A BUNCH OF THINGS THAT I DON'T FEEL AMAZED WITH GETTIN' TOO CLOSE TO ME , WOO, COULD BE DANGEROUS I DON'T LIKE THE ENERGY, I LEAVE THE SITUATION ALL THIS NEGATIVITY THAT I CAN'T GET AWAY FROM ALL THIS NEGATIVITY, I THINK I NEED A BREAK FROM I'M THANKFUL, BUT SOME DAYS, I JUST WANNA LEAVE THE NEGATIVITY IN MY HEAD I JUST WANT RELIEF FROM MY STRESS I JUST WANT RELIEF FROM MY STRESS  SOME DAYS, I DON'T WANNA SEE OR HAVE A BUNCH OF PEOPLE TO IMPRESS I JUST WANT RELIEF FROM MY STRESS, I JUST WANT RELIEF FROM MY STRESS  YO, …

---
## [reimakesgames/hybrid-conflict](https://github.com/reimakesgames/hybrid-conflict)@[3047b68ae3...](https://github.com/reimakesgames/hybrid-conflict/commit/3047b68ae3a65e182b877cf64bb177fd38815365)
#### Monday 2022-12-19 06:15:59 by reimakesgames

init-docs (#100)

* init-docs

i hate vercel, mkdocs, and literally everything else that makes it so hard to just host a simple static site
IS THERE ANYTHING THAT AUTOMATES DEPLOYING A STATIC SITE TO VERCEL??????????

* update

* oh my fucking god

---
## [jianghuanya6/Game-For-Peace](https://github.com/jianghuanya6/Game-For-Peace)@[e3afbf33dc...](https://github.com/jianghuanya6/Game-For-Peace/commit/e3afbf33dc03072a42679d949cbc60bf36beb616)
#### Monday 2022-12-19 07:45:12 by jianghuanya6

Version 1.20.13

[A new version of theme play - space travel]

The space center, a paradise for peaceful elites and China's space cooperation, was officially opened. Special soldiers, come to learn about space science, learn the spirit of space, and explore the universe together!

1. New scene - space center: in the paradise of creation, a new rocket launch base has been added, so special forces can watch the shocking scene of rocket launch from a close distance and feel the extraordinary achievements of modern space science and technology

2. New scene - space information station: the space information station is distributed all over the island. After entering, it can harvest delicious space vegetables and fruits and photonic chicken partners, and also can randomly convert the props in the backpack through the props conversion instrument, which is absolutely amazing

3. New play method - anti gravity device: there are specific rooms in the creation park area, and anti gravity devices will be placed. After use, it can make the gravity disappear for a short time, accompanied by a large number of suspended material balls for special soldiers to collect under weightlessness. Warm prompt: Avoid weight-loss fluid when collecting materials to avoid affecting the moving speed

4. New props - space mission card: after picking up, the special forces in the paradise will be recalled. After the recall process is started, the special forces will go into space by rocket to carry out the space rose cultivation task. After completing the task, they can return to the island with reward materials to continue fighting

5. New props - space fruits and vegetables: delicious fruits cultivated through space breeding can restore the health value and signal value of special forces after eating

6. New item - armor repair kit: damaged armor or helmet can be repaired after use

7. New props - super physical props: Four super physical props will be put in the paradise area. The super physical props will bring strong special abilities to special soldiers. Welcome to experience. Please note that the hypersomatic center can only be used in the paradise, and will become invalid after leaving the park

1) Hyperbody beacon transmitter: after use, it can scan the position of the enemy within the beacon range

2) Hyperbody grenade launcher: after use, you can launch air explosive grenades without limit for a certain period of time

3) Hyperbody - field medical station: after use, the upper limit of health value of oneself and team-mates will be increased. In addition, you can get self rescue defibrillator by interacting with the field medical station

4) Hyperbody Commander's Flag: after use, the damage value and defence of yourself and your teammates will be increased

[New mode of creative workshop - super body confrontation]

In order to deal with the potential crisis in the future, the special forces will test the latest combat technology: hyperbody terminal, strengthen their respective differential combat capabilities, continue to improve the terminal performance, and start a new hyperbody confrontation adventure!

In the hyperbody confrontation game, the special forces can choose eight different hyperbody terminals, which are loaded with the data and skills of eight career mentors. Flexible use of these capabilities and mutual assistance is the key to win the competition;

1. Commander: a team leader who is proficient in firearms, and strengthens the frontal combat capability through energy shield and team gain

2. Rocket boy: start the vector engine, control the air power, and coordinate with the time limited grenade launcher for precise guidance

3. Dimensional geek: master the core technology of hyperbody terminal, create something out of nothing, go back in time and space, and greatly improve the team's material acquisition

4. Field physician: an expert who studies battlefield recovery, can improve the health value of the whole team, and has strong self survival ability

5. Demolition Captain: a fully armed demolition master who controls the battlefield through special missiles and large-scale air attacks

6. Lightning spearhead: a highly mobile profession that moves through the battlefield, and enhances mobility to the extreme

7. Colorful pilots: indulge in mechanical design, use their own vehicles in various ways, and improve the combat effectiveness of the team

8. Phantom Hunter: a strong fighter in complex environment, hiding his own information, detecting the enemy's information, and killing him with one blow

At the same time, in the battle, the special forces can pick up the super unit, upgrade the terminal personalized, obtain health value and gun damage improvement, and have a variety of terminal extension plug-in skills for the special forces to choose and explore, creating the strongest individual;

[Classic Mode - New Content]

1. New firearm - MK20-H: Shooter's rifle of Scar gun family, which uses 7.62mm bullets and can shoot automatically. It has excellent shooting accuracy and good ergonomics; Its own heavy barrel and foot stand make it a powerful deterrent in medium and long distance operations. The disadvantages are slow firing speed and poor stability

2. New vehicle - G48 station wagon: It has the function of vehicle trunk. When approaching or getting on the vehicle, you can open the trunk interface through the backpack button to put or take out items. Refresh in the island, desert, snow and other maps

3. New vehicle - mountain bike: it is obtained by picking up, can be folded and put into the backpack. It has strong cross-country ability and low voice, and is suitable for single person concealed transfer. Simulate the real feel, and quickly click the forward key to speed up. In addition, long press the Jump key, you can accumulate strength to jump slightly and jump over some small obstacles. Refresh in the island, valley, rainforest, resort island, golden island and other maps

4. New accessory - impact gun holder: M16 A4, Mk47, SKS, SLR can be equipped. After assembly, the weapon will become fully automatic, and the stability will be sacrificed in exchange for full automatic continuous firing capability, with a controllable continuous firing speed lower than semi-automatic

5. New scene - Photon chicken nest: a building in the island has been occupied by Photon chicken team and left interesting footprints. Special soldiers are welcome to explore

[Balance adjustment and experience optimization]

1. New features of shooter rifles and sniper rifles: they can cause a temporary deterrent effect when hitting the target

2. Marksman Rifle Enhancement: slightly increase the body damage coefficient of marksman rifles

3. Ammunition weight adjustment: reduce the weight of arrows and rocket arrows

4. Optimization of combat experience: on the basis of automatic jumping climbing, independent climbing button and sliding climbing mode are added, and special forces can switch the jumping climbing mode in the settings

5. Vehicle experience optimization:

1) Motorcycle character riding animation optimization, including the optimization and effect improvement of character waist, hands, feet and other animations

2) Optimize the performance of role getting off the vehicle

6. Information display optimization:

1) When rescuing a teammate or self rescue, the progress of the rescued person will be displayed on the rescue mark of the teammate or self rescue

2) Optimize the performance icon of team killing prompt

3) During the recall phase, you can jump with the teammates of the same aircraft, and there is a light column on the ground of the punctuation position

4) During the parachute recall phase, when punctuating on the small map, the special effect prompt of new lighting column on the ground will be added

5) After being eliminated, you can enter the game watching stage to view the punctuation information of your teammates

6) Repeated chat messages will be folded, and the item marking information in the history will be more obvious

7. Optimization of special training island:

1) The new super body training ground can experience the professional play method of super body confrontation mode

2) A new weapon storage box is added in the outdoor shooting range area to improve the convenience of firearms collection

8. No UI shooting mode:

1) New dance speed change function, supporting 0 to 3 times speed adjustment range

2) New function of changing clothes. By default, the number and order of suites in the lobby are used

3) Add 2 slow shake effect operation templates

[Competition optimization]

1. Optimization of the championship base: the championship base will be comprehensively upgraded, and the hall of honor will be expanded, which will present the champion honor of previous peace elite events

[New functions and optimization of the system]

1. Peak Race Upgrade:

1) The entry action of the original peak segment can be unlocked after reaching the corresponding peak segment, and can be freely used in the hall and dance room this season and next season

2) The competition system of the peak competition has been upgraded, synchronizing with PEL2022's new map to refresh the material probability

The above adjustments will follow the SS20 season launch.

2. A new query entry for season benefits is added. The "season season benefits" interface will display the rewards that can be obtained during the season as a whole, which is convenient for special soldiers to view. This feature will go live with the SS20 season.

3. Download resource experience optimization:

1) The team leader selects a map or play method and clicks to start the game. If the team members do not download relevant resources, a pop-up will remind them to download relevant resources

2) When the team member finishes downloading, a pop-up prompt will be displayed to inform the team leader and relevant team members respectively, so that the team leader can quickly start the game

4. When adding friends to the game successfully, both parties will receive a reminder in the private chat interface, where they can chat with new friends and quickly launch a team invitation

5. Add one click to claim team athletic achievements

[Optimization of the mechanism of injuring teammates]

1. Technical upgrading: optimize the detection algorithm ability of malicious damage to teammates

2. The punishment is aggravated:

1) Penalty for extending the suspension time of maliciously injuring teammates' accounts

2) The account number of a teammate who has been seriously and maliciously injured for many times will be blocked

3) Face recognition detection will be added to the account of a teammate who has been seriously and maliciously injured for many times

3. Perfection of rules:

1) After the driver's vehicle hits an obstacle and his teammate is injured, the malicious damage caused by the teammate can trigger legitimate defense

2) After being carried by team-mates, you can choose the active disengagement function to prevent being carried maliciously by team-mates

[Problem Repair]

1. Fix the problem that the sound effect of landing disappears due to fist swing before jumping to the ground

2. Fix the problem of accidental loss of ammunition replacement animation

3. Fix the problem that the special training island can achieve reverse firing

4. Fix the problem that the character occasionally moves abnormally after falling to the ground

5. Fix the problem that the person perspective cannot be switched when the fire fight mode leaves the vehicle

6. Fix the problem that the occasional character moves quickly after being hit by a vehicle

7. Repair the problem of island map vehicle occasional subsidence

8. Fix the problem of occasionally frying wheat without voice input for a long time under the open wheat state

9. Fix the problem that the team member number and team member thumbnail number of the occasional mini map are wrong

10. Repair the problem of occasional material floating at the edge of island map

11. Fix the problem that the air raid shelter can be stuck in the extreme pursuit mode

12. Fix other known problems

[Performance optimization]

1. Optimized the map loading order, relieved the memory pressure, and reduced the crash probability during the game running

2. The model loading process was optimized. Asynchronous loading was adopted for some steps to avoid affecting the main thread of the game and reduce the jam caused by resource loading

3. The garbage collection mechanism was optimized to improve efficiency and reduce the sense of jamming

4. Optimized the animation resource loading logic, and solved the problem of long loading time for some high-end models

5. It optimizes the time consumption of some functions in the terrain loading process, and alleviates the possible jamming of long-distance vehicle movement

6. The loading sequence of characters has been further optimized to alleviate the stuttering caused by loading other characters and open to more maps

7. The loading process of materials has been further optimized. Asynchronous loading mode has been adopted to alleviate the jam caused by the main thread loading of the game and open to more maps

[Safety Optimization]

1. Technical strategy upgrade: The game optimizes multiple security strategies, including improving detection and recognition capabilities for perspective, self aiming, bullet tracking, acceleration and other plug-in functions

2. Optimization of punishment function: increase gradient punishment status display, and account in gradient punishment will display gradient punishment label in role information interface

3. Falcon system optimization:

1) Expand the recruitment of falcon system, so that more special soldiers can participate in falcon patrol and attack plug-in

2) The falcon patrol broadcast function is added, and falcon inspectors can send the patrol admission broadcast when conducting the inspection

3) The function of Falcon seizure prompt is added. After the illegal user is seized by Falcon patrol system, the inspector gets prompt in time

4. Upgrade of peripheral detection system: strengthen the detection and attack of illegal plug-ins, block the number of accounts that use illegal peripherals to bypass matching and isolation, and clear the segment points

5. Upgrade the violation information identification system to improve the game information environment:

1) Strengthen the crackdown on illegal behaviors of advertising voice, advertising accounts and friends in the lobby world chat channel

2) Strengthen the detection and attack of illegal avatars and nicknames in the game

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1c76ea5334...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Monday 2022-12-19 07:58:45 by SkyratBot

[MIRROR] Changes our map_format to SIDE_MAP [MDB IGNORE] (#18070)

* Changes our map_format to SIDE_MAP (#70162)

## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Changes our map_format to SIDE_MAP

* Modular!

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[7b658b3c0d...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/7b658b3c0d1b9c7b9672a0a1aa709d2789974190)
#### Monday 2022-12-19 08:18:22 by SkyratBot

[MIRROR] Drinking singulo ignores supermatter hallucinations and pulls nearby objects [MDB IGNORE] (#18157)

* Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.

![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

* Drinking singulo ignores supermatter hallucinations and pulls nearby objects

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [gladishd/The-Mangrove](https://github.com/gladishd/The-Mangrove)@[66139b7709...](https://github.com/gladishd/The-Mangrove/commit/66139b7709f3943e00c91e47f8d6585f2d1f75c9)
#### Monday 2022-12-19 08:36:01 by gladishd

Topic: Next up cookies! Login and Signup are counting on some kind of cookie middleware. Then we need like some sort of admin panel to identity verify info for politicians.

About: A cookie is a key-value pair that is stored in the browser. The browser attaches cookies to every HTTP request that is sent to the server.

Session Management in Node.js using ExpressJS and Express Session | Engineering Education (EngEd) Program | Section
https://www.section.io/engineering-education/session-management-in-nodejs-using-expressjs-and-express-session/

On the other hand, the session data is stored on the server-side, i.e., a database or a session store. Hence, it can accommodate larger amounts of data. To access data from the server-side, a session is authenticated with a secret key or a session id that we get from the cookie on every request.

⦁ package.json manages the dependencies for this project's tutorial ⦁ libraries: Express - Express-session - Cookie-parser ⦁ To set up the session, you need to set a couple of Express-session options... secret, resave, saveUninitialized, cookie: { maxAge: oneDay } ⦁ When a client sends a request, the server will set a session ID and set the cookie equal to that session ID. The cookie is then stored in the set cookie HTTP header in the browser. ⦁ index.html, app.css... ⦁ In the server app.js, import all the Node.js libraries like express, cookie-parser, express-session ⦁ Initialize the Express app. Add the Express-session options. ⦁ Parse the HTML form. ⦁ Set the Cookie-parser. ⦁ Set the authentication credentials. Add the endpoints. Listen to the port of the server. ⦁ Once you log in successfully, a session will be generated, and a cookie will be saved in the browser. In this case, since we don't have a database to save the session, we will console.log(req.session) and glance at how it looks.

Last time we tested signing up. Now we can upload straight to the real-time database. However we do it it would be convenient to do so within an established procedure!

The way we did it at Qooley.com, was you take a basic sign up form with email and password, thereby precluding the need for a username which can be registered instead as a continuation of the email address.

How to use cookies for persisting users in Nextjs - DEV Community 👩‍💻👨‍💻
https://dev.to/debosthefirst/how-to-use-cookies-for-persisting-users-in-nextjs-4617
To use cookies in NextJS, we need to install 2 packages. For this tutorial, we'll be using cookie and react-cookie. React-cookie allows us to set the cookie from the client-side while the cookie package lets us access the set cookie from the server-side. Install both packages by running npm install react-cookie cookie. Cookie-cutter is a tiny package that does the same thing as react-cookie.
With both packages installed, it's time to set a cookie. Usually we set a cookie for a user once they've successfully signed in or signed up to our application. To set a cookie on Sign in, follow the example that we have set in our application.

To ensure that every route in our application has access to the cookie, we need to wrap our APP component in a cookie provider.

Cookies go here. 🙂

We have made the cookies universally accessible from anywhere in the application, so that they can be used as a basis to store server-side session data related to that cookie. 😛

Todo: Deploy to something other than Heroku simply because Heroku is to be defunct, November.

https://github.com/thellllvirtuoso/Da-Repo We are making so much progress!

In the snippet above, we call the setCookie hook from react-cookies and set it to a default name. In our case, that's user. We then make a request to sign in a user by calling a function to log the user in. We take the response from that API call, stringify the data (cookies are formatted as text) and store that data in a cookie.

🥝 We also pass some additional options to the cookie including path - makes sure your cookie is accessible in all routes, 🥝 maxAge, how long from the time the cookie is set till it expires and 🥝 sameSite. Samesite indicates that this cookie can only be used on the site it originated from - It is important to set this to true to avoid errors within Firefox logs. What kind of errors does Firefox give if we don't set sameSite?

Firefox Changes to SameSite Cookie Behavior Can Break Salesforce Integrations
https://help.salesforce.com/s/articleView?id=000355255&type=1 The SameSite attribute on a cookie controls its cross-domain behavior. If no SameSite attribute is specified, Firefox sets cookies as SameSite=Lax by default. In previous versions of Firefox, the default was SameSite=None... The SameSite changes enhance security and privacy but require customers and... this regards the default cross-domain (SameSite) behavior of cookies.

Giving your app access to the Cookie. To ensure that every route in our application has access to the cookie, we need to wrap our APP component in a cookie provider.

Assuming that the app.js (_app.js) step is complete, we have wrapped our App component in the cookie provider.

Setting up the function to parse the cookie.

Next, we need to setup a function that will check if the cookie exists on the server, parse the cookie and return it. Create a new folder called helpers and within that add an index.js file see the code for parsing cookies.

React Bootstrap provides the Form which, upon submission of the onSubmit={this.submitForm} function, provides us with a destructurable form that is posted to the axios.post /auth/setLogin API route. This route simply puts the user email address on the server-side session object (for example, not posting to the database).

On the front-end, the /signup/saveUserToDatabase API route is posted with everything on the reqBody object, therefore this route is something to construct. On the /signup/saveUserToDatabase API route, we are posting the request body data (first onto the Express Session, then) on to the checking phase.

var userRef = db.collection('users').doc(user.email) upon which point we invoke the userRef.get() function and if this value has the .exists property, then we return res.status(200).json({ success: 'user already exists' }).

If the user does exist, then that's great; we don't continue with the rest of the code.

If the user does not exist, then we adjust the .isCustomer and .isLocal attributes on the data object and then invoke const response = await db.collection('useres').doc(userId).set(data), before return res.status(200).json({ error: err }).

The firebase object from the Firebase API is only used to invoke the .auth ... .createUserWithEmailAndPassword ... .then ... auth ... signInWithEmailAndPassword ... chain and subsequently the Router.push('/qooleybiz') is done after this chain of events, on the front-end.

Todo: Test everything out on the Front-end first! We need a back-end technically but all the functions can be carried out on the front-end!

In the newer version of Node JS, we are importing the firebaseConfig just the same as with the older version of Node JS.

Test firebase imports:

import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

const firebaseApp = firebase.initializeApp(firebaseConfig);

var db = firebaseApp.firestore()

Previously, at Qooley we had the most spectacular imports:

import * as firebase from 'firebase'

if (!firebase.apps.length) {
firebase.initializeApp(firebaseConfig)
}

Todo: Google OAuth Login.

Firebase makes Authentication easy for Engineers and Developers. Most Applications need to know the identity of the user so they can provide a customized experience, and keep their data secure.

Firebase supports lots of different ways for users to authenticate. Email Address, Facebook, Twitter, GitHub, Google. It can also integrate with your existing account system. You can build your own interface, or you can take advantage of our open-source UI that incorporates years of Google-based experience building server-side apps.

Three things happen. Callbacks allow you to personalize your app's experience for that particular user.

This unique id is used to identify your user and to what sides of the backend system they have access.

And of course, it works on Android, iOS, and the Web. That's Firebase All allowing you to focus on users, and not the signup infrastructure used to support them.

Firebase Authentication
https://firebase.google.com/docs/auth?authuser=0

The FirebaseUI Auth component implements best practices for authentication on mobile devices and websites, which can maximize sign-in and sign-up conversion for your app. It also handles edge cases like account recovery and account linking that can be security sensitive and error-prone to handle correctly.

The identity provider configuration is not found - React Native Firebase Authentication with FacebookAuthProvider - Stack Overflow
https://stackoverflow.com/questions/55522640/the-identity-provider-configuration-is-not-found-react-native-firebase-authent
https://console.firebase.google.com/u/0/project/the-midway-b98d8/authentication/providers

XLSX (.xlsx, .xlsm)—Wolfram Language Documentation
https://reference.wolfram.com/language/ref/format/XLSX.html
Idea: use Mathematica functions to translate our data into readable forms, then upload to Firebase.

This is going to be amazing.

{{"Office", "District", "Party", "CandidateName", "Municipality",
  "County", "State"},
The text replacement is to be done at index 3 (from 1, 2, 3, 4, 5, 6, 7).
change "REP" to "Republican", "DEM" to "Democrat", "LIB" to "Libertarian" and "KEY" to "Keystone Party"

grn: green
ind: independent
key: keystone party
lib: libertarian
rep: republican
swp: socialist worker's party

💡 XLSX (.xlsx, .xlsm)—Wolfram Language Documentation
https://reference.wolfram.com/language/ref/format/XLSX.html

💡Directory—Wolfram Language Documentation
https://reference.wolfram.com/language/ref/Directory.html

💡ReplaceAll (/.)—Wolfram Language Documentation
https://reference.wolfram.com/language/ref/ReplaceAll.html

💡Does Mathematica have a function equivalent to Matlab's "unique" function - Stack Overflow
https://stackoverflow.com/questions/2203737/does-mathematica-have-a-function-equivalent-to-matlabs-unique-function

💡https://g562.sitehost.iu.edu/Handouts/ManipulatingDataInMathematica.pdf

💡 list manipulation - Replacing within a column without extracting it/modifying data - Mathematica Stack Exchange
https://mathematica.stackexchange.com/questions/202350/replacing-within-a-column-without-extracting-it-modifying-data

🐍 python 3.x - How to force Discord to send a link without an embed? - Stack Overflow
https://stackoverflow.com/questions/65657144/how-to-force-discord-to-send-a-link-without-an-embed

Many apps want to leverage the power of an authentication system, but trying to sort out connections to various services and allowing an email login can be a lot of work. Thankfully, Firebase takes a lot of the work out of your hands and allows you to easily start with one service and add in additional services over time.

Email/Password

The most basic sign in option, this allows users to use their email/password to sign up/in. Enabling this is as easy as flipping the first toggle switch after clicking "Email/Password" from the Sign-In providers list, then clicking "Save".

Finally, we access the cookie within the component to check if the user already has a valid cookie on the server side before rendering the requested route.

Data from cookie: {"data":"data cookie data goes here from pages/loginCookies.js"}⭐

OK, let's revisit what happens once we access the cookie on the browser. Do we send it to the server, for reference? How does the server know what the cookie means? The .getInitialProps is something to behold!

Works Cited:

Getting Started with Firebase for the Web - Authentication - Terabyte Tiger
https://terabytetiger.com/lessons/getting-started-with-firebase-authentication

Firebase Authentication throws HTTP 400 "CONFIGURATION NOT FOUND" · Issue #8 · googleinterns/step167-2020
https://github.com/googleinterns/step167-2020/issues/8

Firebase console
https://console.firebase.google.com/u/0/project/the-midway-b98d8/authentication/providers

How to Activate Full-Screen Mode in Google Chrome
https://www.lifewire.com/activate-full-screen-mode-google-chrome-4103634#:~:text=For%20Chrome%20on%20macOS%2C%20in,Use%20the%20keyboard%20shortcut%20Ctrl%2BCommand%2BF.

We're on ******How to use cookies for persisting users in Nextjs - DEV Community 👩‍💻👨‍💻
https://dev.to/debosthefirst/how-to-use-cookies-for-persisting-users-in-nextjs-4617

https://stackoverflow.com/questions/16800056/switching-between-chrome-browser-windows

How to Make Google Chrome Full Screen: Mac and PC
https://www.businessinsider.com/guides/tech/how-to-full-screen-google-chrome#:~:text=An%20curved%20arrow%20pointing%20right.&text=To%20go%20full%20screen%20on,exit%20full%20screen%20in%20Chrome.

301 Moved Permanently
The HyperText Transfer Protocol (HTTP) 301 Moved Permanently redirect status response code indicates that the requested resource has been definitively moved to the URL given by the Location headers. A browser redirects to the new URL and search engines update their links to the resource.
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301

Is the response object available?

** Previously as seen on Qooley: the Express library provides the framework to set things like req.session.user = { email: user.email }, and then we are able to check for the presence of the sessions that are automatically maintained, that is autonomously integrated with the server via the Express library. Now, what we want to do is instead store an (expirable?) cookie on the local browser, which has already been done.
☑️

Now, what we need to do is send the cookie to the server and reference against something; perhaps the Firebase database itself can serve as our repository for the cookie reference. How can we turn our cookie into a session, server-side? Or can we log in without sessions?

First, let's look at the Authentication of the Cookie via Express app.
How to Authenticate Users in Your Node App with Cookies, Sessions, and Passport.js
https://www.freecodecamp.org/news/authenticate-users-node-app/
First, we set up our Express app and include the cookie-parser middleware. It parses the cookie header of the request, and adds it to req.cookies or req.signedCookies (if secret keys are being used) for further processing. What does it mean to use secret keys?

While browsing this article Session Cookie Authentication in Node.js (With Complete Examples)
https://www.sohamkamani.com/nodejs/session-cookie-authentication/ it looks like we can, instead of even having to host a server-side session, simply use the cookie itself as part of our request body, each time the client makes a request.

Session vs. Cookies| Difference between Session and Cookies - javatpoint
https://www.javatpoint.com/session-vs-cookies#:~:text=Difference%20table%20between%20Cookies%20and%20Session&text=A%20session%20stores%20the%20variables,or%20closes%20his%20web%20browser.

Todo: test settings like expiration dates for the cookies. The cookie will be created, stored in the Firebase database collection of cookies (coming soon!): (1) POST to this database when someone logs in. (2) DELETE from this collection when someone logs out. (3) GET from this collection (fetch) when someone wants to access data. (4) PUT to this collection when... someone logs in and refreshes the page? (to be determined).

---
## [gladishd/The-Mangrove](https://github.com/gladishd/The-Mangrove)@[1c4c483c46...](https://github.com/gladishd/The-Mangrove/commit/1c4c483c464406150ff0905820b80ae63774a537)
#### Monday 2022-12-19 08:36:01 by gladishd

Provided that some of the text is a bit wordy and the structure should have two buttons for Login and Signup, after the Welcome/Home Screen that starts out with a splash, we have Todo: When you click Signup you are prompted with a question, two more buttons that you can click; one of them is "I currently hold an official elected position/I am on the ballot" and the other is "I do not hold an official elected position and I am not on the ballot". If you click the first option (less wordy!) you get linked to the signup page specific for politicians.

And if you click the second option (I'm a voter) you go straight to the much simpler Signup page for regular users. Later tonight we can demo this via pipeline to an official name like politic.com... the signup process isn't the key right now, it's data collection; when we speak to potential angel investors or VCS or even family/family friends, they will probably ask how we are going to get all that information on politicians, because it seems that there's no official openly available database of every politician currently on the ballot for every district in the country.

Todo: Survey Page & Forum, designed for mobile view in Chrome DevTools with simulation of various screen sizes. Survey for feedback from our customers: ask about their experience, bug reports, satisfaction with the app. Forums so that the customers can chat and interact on the same platform.

Chat is risky, political, and chaotic. We introduce the terms V2P and limit V2V interaction, V for voter, P for politician... like in business how it's things like P2P or P2B or B2B etc.

On voters, Florida has a lot of info Vote-by-Mail Ballot Information and Status Lookup - Division of Elections - Florida Department of State
https://dos.myflorida.com/elections/for-voters/check-your-voter-status-and-polling-place/vote-by-mail-ballot-information-and-status-lookup/.

Creates in-line styles first, classes second so that we can crop the banner image. html - Crop image in CSS - Stack Overflow
https://stackoverflow.com/questions/26218954/crop-image-in-css. The banner image is in overlay format via positioning and margins html - How to overlay one div over another div - Stack Overflow
https://stackoverflow.com/questions/2941189/how-to-overlay-one-div-over-another-div.

Todo: Currently, clicking the top left Learn with Login tab yoinks us back to the homepage at the Login button. This should direct us to the database.

Here, unlike Jekyll where the base url is defined for the repository we can just write "/" signifying the base URL. The idea is to use dynamic variables to see more and explore more, while using static variables allows us to maintain what we have in the same medium.

When we were building Qooley, Kanishka went to a startup conference in Chicago - 1871 startup demos. The site was glitching out, and he left his jacket at a restaurant. When he came back, we learned what Sohan had been working through all along and it wasn't scary; Cross-Origin Resource Sharing.

Checking into a local corner store to pick up a smoothie, Kanishka spoke about the need for testing in four stages of testing, with the first stage being the localhost and the fourth stage being the production site at the domain named Qooley.com.

So when you use dynamic variables, you want to be able to access those variables from anywhere in the app, which could mean across domains if your app is split into two distinct repositories: qooley-frontend and qooley-webapp.

When building our site, we do the same on one repository instead of two.

Our three column layout provides Politico type of review functionality. javascript - How to create a 3 column layout structure in react.js - Stack Overflow
https://stackoverflow.com/questions/58277981/how-to-create-a-3-column-layout-structure-in-react-js

Design inspired by

(1) Politics, Policy, Political News- POLITICO
https://www.politico.com/

(2) Play Chess Online for free
https://play.chessbase.com/en/

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[81ca11b95a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/81ca11b95a59d5cf0eb0a066454b2903f4859503)
#### Monday 2022-12-19 09:09:06 by SkyratBot

[MIRROR] Basic Mob Carp: Retaliate Element [MDB IGNORE] (#18030)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[91d74cabf6...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/91d74cabf652013e4c12158a7a33f3d5a8e30e66)
#### Monday 2022-12-19 09:38:05 by SkyratBot

[MIRROR] Bodypart code cleanup, robotic limbs can actually be disabled through damage again. [MDB IGNORE] (#18093)

Bodypart code cleanup, robotic limbs can actually be disabled through damage again. (#71739)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

Cleans up various variables and code comments in bodypart code so that
it is easier to understand (hopefully) what the fuck is happening there.

Fixes a hilarious oversight. For what may have been an entire 2 year
span, robotic limbs were unable to be disabled whatsoever. Good stuff.

Lost all your limbs and now have only surplus prosthetics?
Congratulations! You're now more durable than even someone with proper
robotic limbs, as your arms do not contribute anything more than 10
damage (or 15 stamina) to your overall damage taken. Furthermore, taking
the maximum amount of damage is actually entirely meaningless to you.

Laugh as someone attempting to shoot your arms does almost no meaningful
damage once you hit the cap! It's all sunk cost! You can't have it blown
off anyway, because dismembering surplus limbs is gone!

Who knew getting into a horrible bluespace/goliath accident could have
such an impact on your combat prowess. Thanks Nanotrasen!

Anyway, these vars are ugly.

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
code: Makes a lot of the bodypart variables clearer as to what they do.
Includes more detailed code comments.
fix: Robotic limbs are no longer immune to being disabled through
reaching maximum damage.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [LyaaaaaGames/AIdventure_Localization](https://github.com/LyaaaaaGames/AIdventure_Localization)@[227cbe04ab...](https://github.com/LyaaaaaGames/AIdventure_Localization/commit/227cbe04abbecf08fb9c99704952b44ce942a2ab)
#### Monday 2022-12-19 09:40:40 by Lyaaaaaaaaaaaaaaa

Fixed errors in the tags and added TAG_ before the tags keys.

Fixed the following keys (French was in English and Spanish in French.
Also added TAG_ before the name.
- 1ST_PERSON
- 2ND_PERSON
- ADVENTURE
- CYBERPUNK
- DARK
- DYSTOPIAN
- FANTASY
- FEMALE_PROTAGONIST
- HISTORICAL
- HORROR
- LGBTQ
- LOREBOOK_INCLUDED
- MALE_PROTAGONIST
- MEDIEVAL
- MODERN_ERA
- MYSTERY
- PIRATE
- POST_APOCALYPTIC
- ROMANCE
- SCIENCE_FICTION
- STEAMPUNK
- THRILLER
- UPLIFTING
- WILD_WEST
- ZOMBIE

---
## [FRC-6390/FRC-Season-2023](https://github.com/FRC-6390/FRC-Season-2023)@[43fdb1ef24...](https://github.com/FRC-6390/FRC-Season-2023/commit/43fdb1ef24d0f5d9540bc592493a7d3e1cb37312)
#### Monday 2022-12-19 10:31:31 by Mathias

Oh boy, debug time

Using the new 2023 beta (JAVA 17!!!)

Set up the code for the base swerve drive train that is planned to be used.

Redid Custom PID System in Util to allow suppliers,
Added in Custom Limelight, REVLimitSwitch, and Debounced Controller

A simple wrapper class tbh, same thing new paint

The Limelight class manages all the networking tables making it easier to use.

The Debounced Control handles all of the controller inputs, removing clutter from the RobotContainer file, it also had the axis modification pre applied.

All the debounced systems have been updated to the new Trigger Api, with this calling instant commands through buttons presses are a bit more annoying but there is not much that can be done about this at the moment

Create a custom Swerve Module class to work with the new SwerveDriveKinimatics and SwerveDriveOdometry.
The new class gives us complete control over the module and adds in the now required features not yet supported by SDS

DesiredPosition 2.0 (WIP), Janus - The greek god of motion, Janus is the new name going forward for the Desired Position System. Janus is going under a complete rework from the ground up, being built on a better understanding of trajectories and autonomous routines using odometry

The new swerve module system allows us to use the WPILIB trajectories, Janus will attempt to take advantage of the same concept but done differently to allow easier use of the creation of such routines.

Added in a new system for test motors and subsystems, add the SystemTest interface to a subsystem will allow you to define a function that the TestSystem Command can cycle through to verify the functionality of hardware

Constants are there but most need the correct values put in, I put in all the ones I could find at the time.

Dashboard output needs to setup for the swerve modules and the addition of a limit switch sensor possibly for automatic offset alignment.

Autoselector for smartdash was set up

Everything needs testing a will most definitely break, will continue to add the rest of Janus, the smartdash data

Hopefully this will allow us to jump straight into auto routines as soon as we have a robot. Swervebot or Switchblade testing advised.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9e69e5d6ac...](https://github.com/tgstation/tgstation/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Monday 2022-12-19 10:34:06 by LemonInTheDark

Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes. 
Should really make a helper for this someday

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[7f1e80ca3d...](https://github.com/Huffie56/cmss13/commit/7f1e80ca3dd4800f54b5ff4dc3663dd1f804c28c)
#### Monday 2022-12-19 10:50:24 by carlarctg

MIDIs are now either 'Meme' or 'Atmospheric', players can toggle each option (#1939)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Updated savefile number from 19 to 20. Meme and atmospheric preferences
are enabled by default.

Admin sounds now need a selection between 'Meme' or 'Atmospheric' type.
Ideally, this would let players decide if they want to listen to hijack
or first drop songs without needing to listen to GOOD HITS or whatnot.

I am uncertain about the savefile bit of code. I don't fully understand
it.

As stated I don't care about GBP, so if the tags are teechnicallly
incorrect go ahead and change them or whatever.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.

As it says. Lots of people hate the memes and just want to listen to the
cool atmosphere. This is of course dependant on staff selecting the
right option, which is sometimes up to opinion, but I fully trust staff
will be able to handle this subjective affair correctly.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
refactor: Updated savefile number from 18 to 19. Meme and atmospheric
preferences are enabled by default.
admin: Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[70bcd3b6fb...](https://github.com/morrowwolf/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Monday 2022-12-19 11:15:01 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[aef93c4854...](https://github.com/mrakgr/The-Spiral-Language/commit/aef93c485489ff98839f615e4ed391cc6b2b9399)
#### Monday 2022-12-19 11:36:27 by Marko Grdinić

"7:10pm. Time to rest and relax. Tomorrow I'll crack that Python codegen.

https://youtu.be/PDVlri6HUwc?list=PLcMKLtS9oWYFJ0o2bAc-Bh5e7kSnpCAl6&t=791

This OST is banger.

12/19/2022

10:30am. Damn, I slept in late. Let's see, did I get any reply yet from the UPMEM guy? Ah, it was from 3 days ago. Damn, I should have checked it.

Sent him an email as well notified him on Reddit.

Now, let me just chill a little and I will get on with it.

10:55am. MahoAko and Saki are out. Let me read them and then I'll get started on the Python backend.

https://boards.4channel.org/a/thread/246488029/thoughts-on-ai-generated-manga-plots-and-art

They are working on manga drawing AI already in Tezuka's style.

https://boards.4channel.org/a/thread/246488029/thoughts-on-ai-generated-manga-plots-and-art#p246488313

The way it captured Tezuka's style is amazing. This ability to seamlessly immitate styles is the kind of ability I'd most like to have had as a human. It is way beyond my talent.

11:25am. Let me start.

```fs
    let rec binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (Codegen.C.refc_prepass' false (Set args) x).g_decr s BindsTailEnd x
    and binds g_decr (s : CodegenEnv) (ret : BindsReturn) (stmts : TypedBind []) =
        failwith ""
```

This is a good way to start things off. Yeah.

11:45am. Ugh.

```fs
    and binds' (defs : CodegenEnv) (x : TypedBind []) =
        let s = {defs with text = StringBuilder()}
        binds (nullable_vars_of x) defs s (BindsTailEnd(binds_last_data x |> data_term_vars |> Array.isEmpty)) x
        defs.text.Append(s.text) |> ignore
    and binds_loop (nulls : Dictionary<obj,Tag Set>) (defs : CodegenEnv) (s : CodegenEnv) ret (stmts : TypedBind []) =
        let rec loop i =
            if i < stmts.Length then
                let inline op a b c d = function
                    | TyFailwith(_,b) -> line s $"raise Exception({tup b})"; false
                    | e -> op a b c d e; true
                let x = stmts.[i]
                match x with
                | TyLet(d,trace,a) ->
                    try let d = data_free_vars d
                        Array.iter (fun (L(i,t)) -> cdef_show "" defs i (tyv t)) d
                        op nulls defs s (BindsLocal d) a
                    with :? CodegenError as e -> raise_codegen_error' trace e.Data0
                | TyLocalReturnOp(trace,a,_) ->
                    try op nulls defs s ret a
                    with :? CodegenError as e -> raise_codegen_error' trace e.Data0
                | TyLocalReturnData(d,trace) ->
                    try match ret with
                        | BindsLocal [||] | BindsTailEnd true -> if i = 0 then line s "pass"
                        | BindsTailEnd false -> line s $"return {tup d}"
                        | BindsLocal ret -> line s $"{args ret} = {args' d}"
                    with :? CodegenError as e -> raise_codegen_error' trace e.Data0
                    true
                |> function
                    | true -> print_nullables nulls s x; loop (i+1)
                    | false -> ()
        loop 0
```

Why am I passing booleans around in the Cython backend? Yeah, literally nobody is going to understand this. That is why I hate the backend so much. It started off well, but then I had to put in so many hacks. And as punchline at the end, its general performance is shit. Being 2x faster than Python does not mean much when the compilation times are destroyed and Python is already 1,000x slower than it should be anyway.

11:55am. Let me just combine the C and the F# backends.

```fs
    and binds (s : CodegenEnv) (x : TypedBind []) =
        Array.iter (function
            | TyLet(d,trace,a) -> try op s (Some d) a with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnOp(trace,a,_) -> try op s None a with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnData(d,trace) -> try line s (tup d) with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            ) x
```

Look at how clean it is.

```fs
    let rec binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (Codegen.C.refc_prepass' false (Set args) x).g_decr s BindsTailEnd x
    and binds g_decr (s : CodegenEnv) (ret : BindsReturn) (stmts : TypedBind []) =
        Array.iter (fun x ->
            let _ =
                let f (g : Dictionary<_,_>) = match g.TryGetValue(x) with true, x -> Seq.toArray x | _ -> [||]
                (f g_decr) |> Seq.map (fun (L(i,_)) -> $"del v{i}") |> line' s
            ()
            ) stmts
```

This is a good way to start it off.

12:10pm.

```fs
let lit = function
    | LitInt8 x -> sprintf "(<signed char>%i)" x
    | LitInt16 x -> sprintf "(<signed short>%i)" x
    | LitInt32 x -> sprintf "(<signed long>%i)" x
    | LitInt64 x -> sprintf "(<signed long long>%i)" x
    | LitUInt8 x -> sprintf "(<unsigned char>%i)" x
    | LitUInt16 x -> sprintf "(<unsigned short>%i)" x
    | LitUInt32 x -> sprintf "(<unsigned long>%i)" x
    | LitUInt64 x -> sprintf "(<unsigned long long>%i)" x
    | LitFloat32 x ->
        if x = infinityf then "(<float>float('inf'))"
        elif x = -infinityf then "(<float>float('-inf'))"
        elif Single.IsNaN x then "(<float>float())"
        else sprintf "(<float>%s)" (x.ToString("R") |> add_dec_point)
    | LitFloat64 x ->
        if x = infinity then "(<double>float('inf'))"
        elif x = -infinity then "(<double>float('-inf'))"
        elif Double.IsNaN x then "(<double>float())"
        else sprintf "(<double>%s)" (x.ToString("R") |> add_dec_point)
    | LitString x ->
        let strb = StringBuilder(x.Length+2)
        strb.Append '"' |> ignore
        String.iter (function
            | '"' -> strb.Append "\\\""
            | '\b' -> strb.Append @"\b"
            | '\t' -> strb.Append @"\t"
            | '\n' -> strb.Append @"\n"
            | '\r' -> strb.Append @"\r"
            | '\\' -> strb.Append @"\\"
            | x -> strb.Append x
            >> ignore
            ) x
        strb.Append '"' |> ignore
        strb.ToString()
    | LitChar x ->
        match x with
        | '\b' -> @"\b"
        | '\n' -> @"\n"
        | '\t' -> @"\t"
        | '\r' -> @"\r"
        | '\\' -> @"\\"
        | x -> string x
        |> sprintf "'%s'"
    | LitBool x -> if x then "1" else "0"
```

Sure is nasty. Let me clean this up.

```fs
let lit = function
    | LitInt8 x -> sprintf "%i" x
    | LitInt16 x -> sprintf "%i" x
    | LitInt32 x -> sprintf "%i" x
    | LitInt64 x -> sprintf "%i" x
    | LitUInt8 x -> sprintf "%i" x
    | LitUInt16 x -> sprintf "%i" x
    | LitUInt32 x -> sprintf "%i" x
    | LitUInt64 x -> sprintf "%i" x
    | LitFloat32 x ->
        if x = infinityf then "float('inf')"
        elif x = -infinityf then "float('-inf')"
        elif Single.IsNaN x then "float()"
        else x.ToString("R") |> add_dec_point
    | LitFloat64 x ->
        if x = infinity then "float('inf')"
        elif x = -infinity then "float('-inf')"
        elif Double.IsNaN x then "float()"
        else x.ToString("R") |> add_dec_point
    | LitString x ->
        let strb = StringBuilder(x.Length+2)
        strb.Append '"' |> ignore
        String.iter (function
            | '"' -> strb.Append "\\\""
            | '\b' -> strb.Append @"\b"
            | '\t' -> strb.Append @"\t"
            | '\n' -> strb.Append @"\n"
            | '\r' -> strb.Append @"\r"
            | '\\' -> strb.Append @"\\"
            | x -> strb.Append x
            >> ignore
            ) x
        strb.Append '"' |> ignore
        strb.ToString()
    | LitChar x ->
        match x with
        | '\b' -> @"\b"
        | '\n' -> @"\n"
        | '\t' -> @"\t"
        | '\r' -> @"\r"
        | '\\' -> @"\\"
        | x -> string x
        |> sprintf "'%s'"
    | LitBool x -> if x then "True" else "False"
```

Now it is fine.

12:15pm. Since I will be using Python's native tuples, the returns will be much simplified.

12:30pm.

```fs
    let rec binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (Codegen.C.refc_prepass' false (Set args) x).g_decr s BindsTailEnd x
    and binds g_decr (s : CodegenEnv) (ret : BindsReturn) (stmts : TypedBind []) =
        let tup_destruct (a,b) =
            if 0 < Array.length a then
                let a = Array.map (fun (L(i,_)) -> $"v{i}") a |> String.concat ", "
                let b = Array.map show_w (data_term_vars b) |> String.concat ", "
                sprintf "%s = %s" a b |> line s
        Array.iter (fun x ->
            let _ =
                let f (g : Dictionary<_,_>) = match g.TryGetValue(x) with true, x -> Seq.toArray x | _ -> [||]
                (f g_decr) |> Seq.map (fun (L(i,_)) -> $"del v{i}") |> line' s
            match x with
            | TyLet(d,trace,a) ->
                try op g_decr s (BindsLocal (data_free_vars d)) a
                with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnOp(trace,a,_) ->
                try op g_decr s ret a
                with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnData(d,trace) ->
                try match ret with
                    | BindsLocal l -> tup_destruct (l, d)
                    | BindsTailEnd -> line s $"return {tup_data d}"
                with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            ) stmts
    and op g_decr s (ret : BindsReturn) a =
        failwith ""
    and tup_term_vars x =
        let args = Array.map show_w x |> String.concat ", "
        if 1 < x.Length then sprintf "(%s)" args else args
    and tup_data x = tup_term_vars (data_term_vars x)
```

Perfect. It couldn't be any better. Most of the Ops I can just copy from the Cython backend.

Let me have breakfast here."

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[1a226283e5...](https://github.com/cmss13-devs/cmss13/commit/1a226283e5c108dffcb74746af5d36ba29d51058)
#### Monday 2022-12-19 12:02:26 by Diegoflores31

vamp lurker strain (#955)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a new strain for lurker (vampire is the name for now but i can be
changed i just lack the creativity) has less health than the average
lurker but its faster and slashes faster but deals less damage .

**### BASE STATS**
health : 390
armor : 20 
slash damage : 35
speed : 0.1 faster than base lurker // for reference cloaked speed is
0.2
slash speed : 2


Vamp lurker cannot cloak but has a larger kit of abilities focused on
dealing damage and healing making it a high risk high reward backliner
with skill based abilities rather than just stun.
### **Abilities :**

**Rush:** 
Shorter version of pounce (4 tiles) instead of stunning it will daze and
slightly screenshake the target .
damage : 30
cooldown : 6 seconds and 3 if you land it.

**Flurry:**
AOE attack that deals damage to the targets in front of you in a 1x3
area . if landed it will heal you by the same amount and apply a small
slow for the user ( very short second slow)
damage: 30
heal : 30
cooldown : 3 seconds if missed 

**Tail Jab:**
Targeted attack will deal a small amount of damage to the target and
knock him away from you . if you use it on a target in critical state it
will execute it healing you a LOT.
damage : 30
Execution damage : 80 with penetration
cooldown : 7 seconds 
heal : 150
critical state : this occurs when the target either paincrits or falls
INCONCIOUS

## Why It's Good For The Game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->
Lurker lacks strains and i looked up in the Trello that Lurker strain
was required . i tried to follow the indicators but kinda ended up with
something else i guess but i really like how it ended so i am making
this PR to see what you think about it.


## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: diegoflores31
add: Added a new strain for lurker "Vampire".
add: Vampire Lurker exchanges all of your abilities for a fast paced
combat style more focused into dealing damage and
mobility.
add: Active 1 : Rush . Pounces for a maximun of 4 tiles and slashes the
objetive once on impact . applying a screenshake and daze to the target
. Landing this ability reduces the cooldown by half. (cooldown 6
seconds)
add: Active 2 . Flurry : unleashes a 1X3 slash at the targeted direction
that slows your enemies on impact healing you by 30 hp . (cooldown 3
seconds)
add: Active 3 : Tail Jab : Attacks your enemies from a maximun of 2
tiles away while dealing a small amount of damage ( 20) and knocking
them down . if you attack a enemy that is on critical state it will deal
80 damage with penetration and heal you by 150 hp. (cooldown 7 seconds)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Shad0vvs <rtwdevelopment@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[bba6239bc1...](https://github.com/cmss13-devs/cmss13/commit/bba6239bc19510ecd235acc31ec75783751f9bcc)
#### Monday 2022-12-19 12:07:49 by Stan_Albatross

sniper sentries rebalance (#1951)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

halves sniper sentry range reduces accuracy a bit ups firerate 

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

being shot at from far offscreen is awful, this should make sniper
sentry a bit more of a threat when it does come into play while not
being able to hit you from half the map away

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: halved the sniper sentry's range to 10 tiles
balance: reduced the sniper sentry's accuracy by 20%
balance: reduced the sniper sentry's delay between shots from 2s to
1.25s
balance: reduced the plasma sentry's range to 10 tiles
balance: reduced the plasma sentry's delay between shots from 10s to 7s
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [robins/postgres](https://github.com/robins/postgres)@[8272749e8c...](https://github.com/robins/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Monday 2022-12-19 12:11:20 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [ACLANMILES00/app-dev](https://github.com/ACLANMILES00/app-dev)@[e2a5eb5cdc...](https://github.com/ACLANMILES00/app-dev/commit/e2a5eb5cdc0b69b0167788e1a756b17a3063cdc5)
#### Monday 2022-12-19 12:45:48 by ACLANMILES00

Update README.md

The boys is very brutal and gory
peacemaker is funny
vincenzo is amazing

the dark knight is the best superhero movie of all time
howl's moving castle is my first anime
parasite is my favorite korean movie

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[8f1ee35f1d...](https://github.com/harryob/cmss13/commit/8f1ee35f1de18e295fa29e4536ad00431e7f0d76)
#### Monday 2022-12-19 13:25:46 by carlarctg

Refactored weed crossing to utilize signals and list data. (#1960)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Refactored weed slowdown to work based on a signal sent to the recipient
carrying list data.

Added a variable for weed slowdown multiplier to species. Human Heroes
have 0.5 weed slowdown because haha funny. Transferred Yautja's weed
immunity to species.

Added an admin-only example item 'hiking boots' that halve weed
slowdown.

Removed a useless define for XVX.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
refactor: Refactored weed slowdown to work based on a signal sent to the
recipient carrying list data.
code: Added a variable for weed slowdown multiplier to species. Human
Heroes have 0.5 weed slowdown because haha funny. Transferred Yautja's
weed immunity to species.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Tercioo/Details-Damage-Meter](https://github.com/Tercioo/Details-Damage-Meter)@[b8851987bb...](https://github.com/Tercioo/Details-Damage-Meter/commit/b8851987bb559f42624ddbcef3336bed8f0c31cd)
#### Monday 2022-12-19 13:41:41 by Flamanis

Update SpecSpellList for DF live

Removals:
Shaman - Healing Stream Totem is usable by all specs
Druid - Survival Instincts is on both Guardian and Feral
Druid - Adaptive Swarm is used by multiple specs
Paladin - Avenging wrath is usable by all specs
Warlock - Grimoire of Sacrifice is usable by both Aff and Destro
Rogue - Shiv is usable by all specs
Hunter - Marksman and BM hunters have the same Kill Command. Survival does not.

Additions:
Hunter - BM gets Cobra Shot
Hunter - Survival has different Kill Shot and Muzzle (Interrupt) ids
Warrior - Protection has Spell Block
Evoker - Devastation has another ID for Eternity Surge (Kinda just added this one in for safety)
Priest - Discipline has Purge The Wicked talent which replaces Shadow Word Pain
Mage - Arcane Mage's Arcane Familiar
Paladin - Protection has Blessed Hammer and Blessing of Spellwarding
Druid - Balance has Wild Mushroom, and different spell ids for Moonkin Form, Starfire, and Starsure
Druid - Guardian has a different id for Berserk that the 'modifiers' are consolidated into
Monk - Mistweaver has Mana Tea
Demon Hunter - Vengeance has Sigil of Silence and Fracture
Demon Hunter - Havoc has Blur
Death Knights - Added the primary strikes. Heart Strike (Blood), Obliterate (Frost), Festering Strike (Unholy)

---
## [Empire-Strikes-Back/Kylo-Ren](https://github.com/Empire-Strikes-Back/Kylo-Ren)@[9266dc107a...](https://github.com/Empire-Strikes-Back/Kylo-Ren/commit/9266dc107a169b03272c3b27227f257ede0d397f)
#### Monday 2022-12-19 14:06:34 by Kylo-Ren

don't get cheap on me, Dodgson - it was Hammond's mistake

like Harstem I chose to do evil - sit in a high palce and speak

unlike Rich Hickey I no longer want to work for Money

I heard Jesus - about two masters, man going to Jericho, high places and palaces, blind leads the blind\

let my identity fruit be lychee
let my language be clojure, runtime jvm
like Iam Malcolm and everyone but bloodsucking lawyer I no longer agree with Hammond - to be a tool

:Samuel-L-Jackson be humble, sit down - you're about to get Black Snake owned

---
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[de662db397...](https://github.com/Profakos/orbstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Monday 2022-12-19 14:45:35 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [Sunilshelke/String-Questions-](https://github.com/Sunilshelke/String-Questions-)@[27629b4f38...](https://github.com/Sunilshelke/String-Questions-/commit/27629b4f38c63f4edc6af15781676c697e254c0e)
#### Monday 2022-12-19 15:42:46 by Sunil Shelke

Ptice

Ptice
Adrian, Bruno and Goran wanted to join the bird lovers’ club. However, they did not know that all applicants must pass an entrance exam. The exam consists of n questions, each with three possible answers: A, B and C.

Unfortunately, they couldn’t tell a bird from a whale so they are trying to guess the correct answers. Each of the three boys has a theory of what set of answers will work best:

Adrian claims that the best sequence is: A, B, C, A, B, C, A, B, C, A, B, C ...

Bruno is convinced that this is better: B, A, B, C, B, A, B, C, B, A, B, C ...

Goran laughs at them and will use this sequence: C, C, A, A, B, B, C, C, A, A, B, B ...

Write a program that, given the correct answers to the exam, determines who of the three was right – whose sequence contains the most correct answers.

Input Format
First line contains an integer n denoting number of questions.

Second line contains a string of n letters ‘A’, ‘B’ and ‘C’. These are, in order, the correct answers to the questions in the exam.

Last line contains the indices separated by space.

Output Format
On the first line, output m, the largest number of correct answers one of the three boys gets.

After that, output the names of the boys (in alphabetical order) whose sequences result in m correct answers.

Example 1
Input

5
BAACC
Output

3
Bruno
Explanation

Here only Bruno has most correct answers i.e. 3.

Example 2
Input

9
AAAABBBBB
Output

4
Adrian
Bruno
Goran
Explanation

Here all 3 have 4 correct answers.

Constraints
1 <= n <= 100

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Monday 2022-12-19 15:59:41 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

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

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [Tangerineje/PsychonautStation](https://github.com/Tangerineje/PsychonautStation)@[4fd404aa8f...](https://github.com/Tangerineje/PsychonautStation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Monday 2022-12-19 17:31:27 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [Tangerineje/PsychonautStation](https://github.com/Tangerineje/PsychonautStation)@[9499a1542b...](https://github.com/Tangerineje/PsychonautStation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Monday 2022-12-19 17:31:27 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [gonzus/AdventOfCode](https://github.com/gonzus/AdventOfCode)@[8d848cb5b7...](https://github.com/gonzus/AdventOfCode/commit/8d848cb5b702acbcdf7182b970808098431f455d)
#### Monday 2022-12-19 17:51:31 by Gonzalo Diethelm

2022 day 19

This is an awful, ugly, randomized brute-force solution.

I basically could not be arsed to come up with a good pruning strategy
for selecting the robots to build, as well as getting rid as early as
possible of useless tree branches.  Instead, I just choose randomly
whether to build each type of robot and run it a gazillion times,
keeping track of the best results so far.

On my M1 laptop part 1 takes 19s and part 2 takes 30s.

Shameful.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[3efa9b5382...](https://github.com/Bjarl/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Monday 2022-12-19 17:59:42 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [michaelbelong/ppuunnkk](https://github.com/michaelbelong/ppuunnkk)@[9a4b6af90d...](https://github.com/michaelbelong/ppuunnkk/commit/9a4b6af90da5101a3ad0c5380663c452385a659b)
#### Monday 2022-12-19 18:25:42 by pugson

fix chakra theme bullshit

fuck this stupid framework it’s literal garbage that no one should be using

---
## [Binbers/oldified-new](https://github.com/Binbers/oldified-new)@[6120721323...](https://github.com/Binbers/oldified-new/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Monday 2022-12-19 21:19:26 by carlarctg

Added various flasks to loadouts and canteen vendors. (#1802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Added a canteen (item) from an unused sprite.

Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

All flasks (and canteen (item)) can be selected in the character loadout
items menu at the bottom.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

The old W-Y flask looked more like a skull than the logo. The gold badge
bit was legacy from bay12.

> Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Legacy renaming.

> Added a canteen (item) from an unused sprite.

Cool sprite. Fucked up we didn't have canteens until now when, uh.
That's what people actually use in the military, not flasks. (To my
knowledge)

> Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

Canteens are the standard military container, W-Y flasks in the vendors
are a good Lore way to show how much of a WY suckup the USCM is.

> All flasks, vacuum and leather included, (and canteen (item)) can be
selected in the character loadout items menu at the bottom.

I think these flasks are cool ways to add flavor to your character, and
it's a shame most of them either weren't in the game or were in very
annoying to find places.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:

imageadd: Resprited the W-Y Flask. Removed the gold badge from the
former detective's flask.
add: Renamed the former detective's flask and bar flask into the brown
and black, respectively, leather flasks.
add: Added a canteen (item) from an unused sprite.
add: Canteens (item) and W-Y flasks can now be found in the canteen
(place) vendors.
add: All flasks, vacuum and leather included, (and canteen (item)) can
be selected in the character loadout items menu at the bottom.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [jeff0167/GameEngine_sfml](https://github.com/jeff0167/GameEngine_sfml)@[e934d3852e...](https://github.com/jeff0167/GameEngine_sfml/commit/e934d3852e40b930be5c29f1d6620868986d8a2a)
#### Monday 2022-12-19 22:40:00 by jefferen

Delete yaml-cpp

Omg dude took so long just to change branch, I just wanted to discard all changes, I wanted a copy of the development branch and everything that I currenly have opened, DISCARDED, forever. Why is is that I find my self copy and pasting and doing all sorts of manuveours that github was specificly made for to avoid, but I can't see any way out but having to find another push/pull system, out of the three available and at times finding no other option than resetting it all manually, by copy and paste, to get it to do what I want, cause no you're not allowed to stash those changes, dude I don't care. All I want is for my project to be the exact same one as the one in one of the branches on github, and I don't care about any differences on my project on disk, just discard(stash) and let me move on. I love github, this is how it is when you program alone I guess, no help

---

