## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-05](docs/good-messages/2022/2022-11-05.md)


1,837,650 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,837,650 were push events containing 2,522,005 commit messages that amount to 154,242,808 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [xubby/aed-project1](https://github.com/xubby/aed-project1)@[2d28f29e09...](https://github.com/xubby/aed-project1/commit/2d28f29e09af6f786b2b40cc9fc0d412e1c81ab9)
#### Saturday 2022-11-05 00:14:06 by ZeAntonioM

pain ahhhhhhhhhhhhhh i want to kill me, merge confilcts are fucking painfull

---
## [TrainsFrom132To1710/Traincraft-5](https://github.com/TrainsFrom132To1710/Traincraft-5)@[8ff6a4d2a9...](https://github.com/TrainsFrom132To1710/Traincraft-5/commit/8ff6a4d2a9c11fa5dfd0cfe7dac3852f4cd20a15)
#### Saturday 2022-11-05 00:23:16 by TheDoctor1138

Fixes

ironed out some bugs in the diagonal
fixed the speedsign
fixed some recipes
added another buffer
fixed some train stuff
fixed my bloody server because a child decided to grief it like the piece of cock sucking shit they are

---
## [nevimer/Skyrat-tg](https://github.com/nevimer/Skyrat-tg)@[7c9e26bb85...](https://github.com/nevimer/Skyrat-tg/commit/7c9e26bb85a40ee3f5a570fe4f51df3c4f350ea5)
#### Saturday 2022-11-05 00:48:22 by SkyratBot

[MIRROR] Fixes Some Incredulously Fucked Up Recycler Behavior [MDB IGNORE] (#17018)

* Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

* test one

Hey there!

Did you know that if you toss someone into a recycled emagger, that we delete _all_ of that mob's contents? You probably didn't because this shit is broken broken. Like, ow.

That's because we manually moved an item to nullspace, which caused a _slew_ of odd behavior in the Destroy chain for `obj/item` since it moves it to nullspace at a very specific point in time and makes all of it's assumptions on when you move the thing to nullspace. If it's in nullspace before you call qdel, you would shit out the ass with hanging references stuck on the mob (like `w_uniform` pointing to something in nullspace, like the image above).

All fixed now, though.

* I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

* i blanked

my guy hasn't moved for twenty minutes

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* wrong documentation

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Fixes Some Incredulously Fucked Up Recycler Behavior

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[7cb69c2a8b...](https://github.com/ThePiachu/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Saturday 2022-11-05 00:58:23 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [anarazel/postgres](https://github.com/anarazel/postgres)@[8272749e8c...](https://github.com/anarazel/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Saturday 2022-11-05 01:11:53 by Tom Lane

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
## [DerpFest-AOSP/frameworks_base](https://github.com/DerpFest-AOSP/frameworks_base)@[ecee552c79...](https://github.com/DerpFest-AOSP/frameworks_base/commit/ecee552c79745513a6f6ac154a976a187e3a7b81)
#### Saturday 2022-11-05 01:29:55 by Kuba Wojciechowski

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
## [Talon396/Talon396](https://github.com/Talon396/Talon396)@[2e954070b9...](https://github.com/Talon396/Talon396/commit/2e954070b9645eb2ea748ecda33b5683363d1b20)
#### Saturday 2022-11-05 02:31:00 by TalonFox

fix error cuz i dumb and cannot do english

The reasoning behind this commit was to logically explain that I'm not implying that I know it, rather I actually know how to use it. This is used to insure that the audience isn't confused by this move.

(Yes, this is intended to be a joke)
(I hate being a Sophomore in High School and having to do stupid stuff in Pre-AP English like this, you get what I'm saying?)

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[e8be775da4...](https://github.com/Paxilmaniac/Skyrat-tg/commit/e8be775da4892a20186105a69bdc8b0832fba1cb)
#### Saturday 2022-11-05 02:42:33 by Paxilmaniac

Adds a collection of some kinda random greyscaled, recolorable clothes options (#16961)

* that's a few dmis

* a few sprite changes

* i hate making greyscale configs

* oh the misery

* 2:29 AM

* a few small things

* adds the stuff around more

* amazing work boss, this is why you're the best

---
## [FlameArrow57/goonstation](https://github.com/FlameArrow57/goonstation)@[693f38836f...](https://github.com/FlameArrow57/goonstation/commit/693f38836f362b8083c1d0169c7e5c17196852f1)
#### Saturday 2022-11-05 03:12:43 by aloe

why do you set vis_flags if you aren't going to use vis_contents fuck you

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5b4ba051a0...](https://github.com/tgstation/tgstation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Saturday 2022-11-05 03:13:56 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

## About The Pull Request

Area contents isn't a real list, instead it involves filtering
everything in world
This is slow, and something we should have better support for.

So instead, lets manage a list of turfs inside our area. This is simple,
since we already move turfs by area contents anyway

This should speed up the uses I've found, and opens us up to using this
pattern more often, which should make dev work easier.

By nature this is a tad fragile, so I've added a unit test to double
check my work

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Builds sortedAreas on demand, caching until we mark the cache as
violated

It's faster, and it also has the same behavior

I'm not posting speed changes cause frankly they're gonna be a bit
scattered and I'm scared to.
@Mothblocks if you'd like I can look into it. I think it'll pay for
itself just off `reg_in_areas_in_z` (I looked into it. it's really hard
to tell, sometimes it's a bit slower (0.7), sometimes it's 2 seconds
(0.5 if you use the old master figure) faster. life is pain.)

## Why It's Good For The Game

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[83c75cac2c...](https://github.com/san7890/bruhstation/commit/83c75cac2c632a51eb8252b2d93b0cf0faa0a9ee)
#### Saturday 2022-11-05 03:18:27 by Jacquerel

Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)



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

---
## [briantopping/bazel](https://github.com/briantopping/bazel)@[2232c5b445...](https://github.com/briantopping/bazel/commit/2232c5b445f5264b31b53a698f5f0e726d9be249)
#### Saturday 2022-11-05 03:20:45 by Christopher Peterson Sauer

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
## [Nukechickenu64/Abaddon](https://github.com/Nukechickenu64/Abaddon)@[6c42446811...](https://github.com/Nukechickenu64/Abaddon/commit/6c424468115306d2e2a85cf13663c7507885382c)
#### Saturday 2022-11-05 06:31:54 by Nukechickenu64

fuck you paradise this my shit now idc if its cobblerigged to

---
## [morning-night-dream/platform](https://github.com/morning-night-dream/platform)@[1001e751f3...](https://github.com/morning-night-dream/platform/commit/1001e751f35ddf67cf72776300f909a742e78d37)
#### Saturday 2022-11-05 06:49:17 by takokun

Merge pull request #91 from morning-night-dream/feature/issue#90

#90 cockroach を構築する terraform を実装

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[2bcd667ed0...](https://github.com/dsmith328/LC13Master/commit/2bcd667ed0e9df8de548725e2d64b2f003c94a26)
#### Saturday 2022-11-05 06:53:11 by Lance

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

Update

Shy Look breach and icons.
Express Train, Cherry Blossom, and Child of the galaxy currently excluded

Update

Makes P-Bird and TSO kill themselves as opposed to QDEL so they don't avoid "on_mob_death" signals

Update

Ppodae deaths instead of QDEL

Shrimp Update

Shrimp Check for FF

---
## [sil3abdi/another-gitest](https://github.com/sil3abdi/another-gitest)@[fdf3835573...](https://github.com/sil3abdi/another-gitest/commit/fdf383557329bb7f01e8d40cc49e84d85b34dfd8)
#### Saturday 2022-11-05 09:57:07 by sil3abdi

Update README.md

oh my god that's so insane
oh my god that's such a shame

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[3dfeccbf27...](https://github.com/OrionTheFox/Skyrat-tg/commit/3dfeccbf27b8dc53c97c2e9db0f1bdc4fd000ebe)
#### Saturday 2022-11-05 10:28:59 by SkyratBot

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
## [kavishinsa/Prestige-Neopolis-Kokapet-Hyderabad](https://github.com/kavishinsa/Prestige-Neopolis-Kokapet-Hyderabad)@[80b66888a2...](https://github.com/kavishinsa/Prestige-Neopolis-Kokapet-Hyderabad/commit/80b66888a2e21b5aceab812631a16b0e671b6cd7)
#### Saturday 2022-11-05 12:20:10 by kavishinsa

Prestige Neopolis Hyderabad - Enjoy Seamless Connectivity

Since the start of the pandemic, sales of the luxury development of Prestige Neopolis have been on the rise, and demand remains high even now. There is a good appetite for luxury flats with high-end conveniences and thoughtful plans.

Several real estate experts believe that the demand for luxury real estate projects like Prestige Neopolis Hyderabad has not only increased but also that values have risen in the upcoming times. This is largely due to demand exceeding the source. They also point out that luxury real estate is a popular speculation vehicle among corporate bosses and that although they own several properties as part of their wealth construction, they mostly decide to settle in their dream home only at the end of their business career.

Situated at the project in Kokapet region, near the ring road in Hyderabad, the unit is designed with high rise floor and has several parking places. The unit is housed in a 30-story building overlooking the lush green lawns, the official dwelling of the state governor. 

The development offers a limited selection of 1/2/3 BHK residences and the homes have stunning views of serene environments. The global pandemic could slow down the investments of rich people. Come be a part of this opulent housing complex Prestige Neopolis Kokapet, Hyderabad.

For More Details:
Visit Here: https://bit.ly/3WwIKE3

---
## [oatmealine/n3ko-smp-modpack](https://github.com/oatmealine/n3ko-smp-modpack)@[7f5c4bbe75...](https://github.com/oatmealine/n3ko-smp-modpack/commit/7f5c4bbe7530a64d4cb8e6675d772859396ab276)
#### Saturday 2022-11-05 12:41:13 by Jill "oatmealine" Monoids

mod: BUTTONS FULLY WORK i think..\!\!\!

through a series of extremely convoluted unhinged access widener hacks and internal minecraft engine fuckery, i've managed to get it to treat my Audio Ogg File From The Web as its own native sound system sound. this SEEMS stable but there's no guarantee it won't cause a segfault the moment someone on a pc other than mine tries this

---
## [BrakusTapus/ToolBox](https://github.com/BrakusTapus/ToolBox)@[a23eec7f59...](https://github.com/BrakusTapus/ToolBox/commit/a23eec7f59d401063e4ad9d534559b6e50b35dea)
#### Saturday 2022-11-05 14:27:13 by BrakusTapus

holy shit this is prolly not even gonna work oh my god i hate imgui

---
## [HACKER-3000/waterthing](https://github.com/HACKER-3000/waterthing)@[16d43fb7af...](https://github.com/HACKER-3000/waterthing/commit/16d43fb7af6ffd95d2787528c8ccbc14476ecf98)
#### Saturday 2022-11-05 15:47:05 by HACKER3000

more stupid stuff

size issues on wt again

integer overflows due to some 1000s not being longs (god i hate that shit)

forgot a pair of () on gw

---
## [beagleboard/linux](https://github.com/beagleboard/linux)@[adee8f3082...](https://github.com/beagleboard/linux/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Saturday 2022-11-05 16:00:30 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [akhil-damarla/Data-IO-2022](https://github.com/akhil-damarla/Data-IO-2022)@[09bbafe8c0...](https://github.com/akhil-damarla/Data-IO-2022/commit/09bbafe8c0b269bc7a2b46a90fe83fb28f35ac18)
#### Saturday 2022-11-05 16:09:21 by akhil-damarla

delete all the stupid fucking files we dont fucking need cause its shit and I was a dumbass

---
## [c1x1x00xxPentium/terminal](https://github.com/c1x1x00xxPentium/terminal)@[9ccd6ecd74...](https://github.com/c1x1x00xxPentium/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Saturday 2022-11-05 16:15:16 by Mike Griese

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
## [fatimzehraa/minishell](https://github.com/fatimzehraa/minishell)@[21bbd2877a...](https://github.com/fatimzehraa/minishell/commit/21bbd2877a118c30c94014120b6b70d5ec29a3a7)
#### Saturday 2022-11-05 17:04:15 by fatima-zahra

fixing what merge ruined`:	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

Copyright (c) 2022 Author. All rights reserved.

Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
	0. You just DO WHAT THE FUCK YOU WANT TO.`

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[696d2d4f71...](https://github.com/BakaKaito/Mergebot.NET/commit/696d2d4f71c3f30e7e41b2496c22958ffa8ccbc5)
#### Saturday 2022-11-05 17:26:34 by Koi

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
## [anclandor/tgstation](https://github.com/anclandor/tgstation)@[b2be252eb6...](https://github.com/anclandor/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Saturday 2022-11-05 17:27:15 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[9d5df80e01...](https://github.com/swarm-game/swarm/commit/9d5df80e01334fac8118ed96de7bba1b71a123a5)
#### Saturday 2022-11-05 17:51:47 by Brent Yorgey

Copy requirements map to robot context when loading a new `ProcessedTerm` (#827)

Closes #540.

When we typecheck and capability check a new term, resulting in a `ProcessedTerm`, we already know the `Requirement`s for all the `def`s it contains.  This PR simply takes all those definition requirements and adds them to `robotContext . defReqs` just before installing the new `ProcessedTerm` in the CESK machine, so that if we ever encounter the name of any of the definitions inside an argument to `build` or `reprogram`---which we capability check at runtime---we will be able to properly match up names with their requirements.

This is a hack for several reasons:
- We really shouldn't be capability-checking arguments to `build` and `reprogram` at runtime in the first place---ideally we should be able to check everything statically.  But fixing that will require implementing #231 .
- We have to do this in three places in the code: when loading a new term into the base when the player hits Enter at the REPL; when executing `run`; and when running the solution from a scenario in the integration tests.  Ideally, there would be only one place, but I don't have a good idea at the moment how to refactor things properly.
- Technically, the names being defined shouldn't be in scope until after their corresponding `def` runs, so it's incorrect to dump them all into the `defReqs` prior to executing any of the `def`s.
    - However, doing it properly, with each name coming into scope with its requirements right after the `def` runs, is very tricky/annoying to implement for more reasons than I care to write about here (believe me, I tried, and it made my brain hurt).  For starters, we don't really have access to the robot state when stepping the CESK machine.
    - The only scenario where this would be a problem is if (1) there is already a name `x` defined, and then we (2) `run` a `.sw` file containing, first, a `build` command whose argument references `x`, and second, a redefinition of `x`.  In that case the `build` would incorrectly decide that the `x` in the argument to `build` has the requirements of the *second* `x` (the one that will be redefined later) even though the first `x` is the one that should still be in scope.  However, this seems like a very unlikely scenario (who would write a `.sw` file that depends on some specific name already being defined before it is run, but then redefines that same name later?) and I'd *much* rather have that obscure problem than the current very relevant and annoying one.

However, it's a simple hack that solves the issue and will be easy to get rid of later if and when we do something better.  I'm a big believer in doing things the right way, but in this instance I definitely think we should just do the simple thing that mostly works and then continue to make it better in the future.

---
## [Teistt/GameOff2022](https://github.com/Teistt/GameOff2022)@[c3140325ac...](https://github.com/Teistt/GameOff2022/commit/c3140325ac6872aa306d98ec940f9194661e2726)
#### Saturday 2022-11-05 20:39:23 by natha0

Fonctionnement Basique Shitty friends

-2 types de shitty friends:
   -Attack : lance une boule de feu destructrice en face du joueur
   -Heal : soigne une partie des blessures du corps et du coeur

---

