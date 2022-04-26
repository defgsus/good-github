## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-25](docs/good-messages/2022/2022-04-25.md)


1,771,292 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,771,292 were push events containing 2,845,623 commit messages that amount to 211,201,450 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [Legate-Maxson/thewasteland](https://github.com/Legate-Maxson/thewasteland)@[59a018d95a...](https://github.com/Legate-Maxson/thewasteland/commit/59a018d95a11eaed40605e2dccb5b549c6c6e2ba)
#### Monday 2022-04-25 00:08:27 by Kirie Saito

NCR Minor Changes (includes Corporal Timelock) (#130)

* adds timelocks to NCR roles

* NCR minor changes

* adds master corporal pins (for RP)

* flavor change

* Update ncr.dm

* yeah that shotgun sucks ass

* Actually makes this shit work, I am an idiot

* typo

* Name was kinda dogshit, changed it

* one binos, not two

---
## [NotZeetaa/android_kernel_xiaomi_sm8250](https://github.com/NotZeetaa/android_kernel_xiaomi_sm8250)@[38b0bd0f25...](https://github.com/NotZeetaa/android_kernel_xiaomi_sm8250/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Monday 2022-04-25 00:15:31 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

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
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Den-Xero/Journeyman_Game](https://github.com/Den-Xero/Journeyman_Game)@[796d38e2c7...](https://github.com/Den-Xero/Journeyman_Game/commit/796d38e2c7e86b63a1e168ad32b7ae0f591cb43e)
#### Monday 2022-04-25 00:17:42 by McConnell2111

Added Custom Keybinds again this time on my own branch

i have time to rant today so what shall we talk about? ooo F1 that was good today, boring ass redbull 1,2 but the madlad lando p3 which was pog. le clair got fked on the same corner he came off in quali which was dumb af. ooo also the LCS finals was today a quick 3-0 for EG which is eh but they did do the same thing as G2 which is intresting since they are in the same bracket as eachother for MSI so thats spicy but G2's real enemy is T1 with Faker the beast. erm what else.... pfft i dunno got any good series to watch? still waiting on moon knight new ep and halo but its weekly which is lame. yeah thats about it from me this time. cya next time.

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[cd1b891d79...](https://github.com/CursedBirb/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Monday 2022-04-25 00:55:53 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[e99b3624ef...](https://github.com/Stalkeros2/Skyrat-tg/commit/e99b3624ef3a041e76e3e8f34577effe07ca41d9)
#### Monday 2022-04-25 01:26:51 by SkyratBot

[MIRROR] Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. [MDB IGNORE] (#13029)

* Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug.

Co-authored-by: Vladin Heir <44104681+VladinXXV@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [djkramer123/vgstation13](https://github.com/djkramer123/vgstation13)@[b879dddba0...](https://github.com/djkramer123/vgstation13/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Monday 2022-04-25 01:31:18 by rob

adds sound effects to surgery steps (#31850)

* the everything

* nmb

* ok

* dfdffdfsds

* ssssssssssssssssssssskurfusr

* fuck yoiu damian fuck you!!!!!

* DAMIANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

* D

---
## [YinSum2002/Project3](https://github.com/YinSum2002/Project3)@[64d4e97a71...](https://github.com/YinSum2002/Project3/commit/64d4e97a713155d872bbfc32ebe3214d7f908801)
#### Monday 2022-04-25 01:37:10 by justin

Sorry it took so long, but I finished the framework for game 2. The spaceship part works, but nothing else does. My plan is to share the next parts of this project once I get them tomorrow, and we can work on fixing up game 2 tomorrow night so you have time to look at the new parts. I'll do my best to framework them while you're busy.

---
## [ettoreleandrotognoli/rathena](https://github.com/ettoreleandrotognoli/rathena)@[d617d9f083...](https://github.com/ettoreleandrotognoli/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Monday 2022-04-25 02:00:17 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [SuperNovaa41/tgstation](https://github.com/SuperNovaa41/tgstation)@[55336d1e53...](https://github.com/SuperNovaa41/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Monday 2022-04-25 02:38:35 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [yasuhirokimura/magit](https://github.com/yasuhirokimura/magit)@[ab801de538...](https://github.com/yasuhirokimura/magit/commit/ab801de53827a232b7806362fb08ca804f27c6d0)
#### Monday 2022-04-25 02:44:47 by Jonas Bernoulli

magit-section-context-menu: Support non-section branches

We use section keymaps to implement context-sensitive menus but
branches are not always represented using sections.  To support
such "painted branches" anyway use fake sections, which closely
mirror the commit section in which the click occurred.

This admittedly is ugly and somewhat risky, but seems to work well.
`magit-section-update-highlight' would break due to this hack, so
we avoid calling it.  If it turns out that things also break due
to this kludge, then we might have to revert.

---
## [Samarth-Khatri/next.js](https://github.com/Samarth-Khatri/next.js)@[91146b23a2...](https://github.com/Samarth-Khatri/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Monday 2022-04-25 03:04:11 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [MFScalzo/TechnologyProject](https://github.com/MFScalzo/TechnologyProject)@[3a98f3d0ce...](https://github.com/MFScalzo/TechnologyProject/commit/3a98f3d0cec37fff8b17cc5ac43337aad07213a9)
#### Monday 2022-04-25 04:15:20 by Matt Scalzo

Finish HiveClient.scala and use in main()

Bunch of headaches with uploading the file to hdfs then into a hive
table. It is really annoying how the path changes depending on what
library you are using, some need hdfs://url stuff/path some just need
the path, and some just need the path to the parent folder since the
account for a bunch of files... Anyhow I ran into two notable bugs:
1. Hive expects data of type Timestamp to be in the form "YYYY-MM-DD
   HH:mm:SS" while the schema we were provided and what we made puts in
   the format "YYYY-MM-DD HH:mm" leaving off the seconds. This causes
   Hive to not recognize it as a Timestamp type. So as I have changed
   its data type to string for now... Not really our fault here, more
   the fault of whoever created the schema and the Sample Output
   Example.
2. There seems to be some sort of "bug", or maybe unintended
   consequence, of how we drop the table then create it on hive. As of
   this commit, when you rerun our JAR in the same session, a null row is
   added to the table everytime you rerun it. I am pretty sure this is a
   side effect of dropping the table then recreating it with the same
   name and schema right afterword but I have been unable to figure out
   how to solve this issue. These null rows will be excluded due to
   almost any sensible query so it is not a big deal.
Anyway, yeah, producer should be done after this is merged into the main
branch!!!!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3f18dadd1a...](https://github.com/tgstation/tgstation/commit/3f18dadd1a5d654aafc2c37539ff917580bfe0b2)
#### Monday 2022-04-25 04:36:13 by san7890

Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[446f280757...](https://github.com/PKRoma/Terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Monday 2022-04-25 06:44:36 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [LuisFelipeCoelho/acts](https://github.com/LuisFelipeCoelho/acts)@[6e1fd31474...](https://github.com/LuisFelipeCoelho/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Monday 2022-04-25 07:13:13 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [MineClone2/MineClone2](https://github.com/MineClone2/MineClone2)@[5f126c4686...](https://github.com/MineClone2/MineClone2/commit/5f126c468650577ea0baefb5d79b81835fe33579)
#### Monday 2022-04-25 07:30:31 by cora

add hypercopyrighted end crystal beam texture

This texture has the following poem written by me, cora, encoded in its
pixeldata. I the author hereby release both the texture file and the
poem as cc0.

Additionally I explicitly consent with its inclusion into MineClone2,
MineClone5 and Mineclonia as well as any other minetest game for this
day and all the days to come.

Shall though betray me with a texture, mate
I'll smile at though just like a summer's day
The raindrop particles - no laggy state
But spring is coming, really, soon it's may

As If the seasons meant a damn to us
They do not exist in mineclone at all
unreal water flow, iron never rusts
but copper does in summer and in fall

But what this literally is about
because this damn thing is really silly
you see somehow they had to say it loud

I would bring that quote with painting lilys
but plagerism everywhere you see
so this will just be good enough for me

---
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[86d77f6a5b...](https://github.com/T-J-Teru/binutils-gdb/commit/86d77f6a5be904f13c633f10bdf77ff3dd69db94)
#### Monday 2022-04-25 09:16:31 by Andrew Burgess

gdb: don't try to use readline before it's initialized

While working on a different patch, I triggered an assertion from the
initialize_current_architecture code, specifically from one of
the *_gdbarch_init functions in a *-tdep.c file.  This exposes a
couple of issues with GDB.

This is easy enough to reproduce by adding 'gdb_assert (false)' into a
suitable function.  For example, I added a line into i386_gdbarch_init
and can see the following issue.

I start GDB and immediately hit the assert, the output is as you'd
expect, except for the very last line:

  $ ./gdb/gdb --data-directory ./gdb/data-directory/
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  ----- Backtrace -----
  ... snip ...
  ---------------------
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  Quit this debugging session? (y or n) ../../src.dev-1/gdb/ser-event.c:212:16: runtime error: member access within null pointer of type 'struct serial'

Something goes wrong when we try to query the user.  Note, I
configured GDB with --enable-ubsan, I suspect that without this the
above "error" would actually just be a crash.

The backtrace from ser-event.c:212 looks like this:

  (gdb) bt 10
  #0  serial_event_clear (event=0x675c020) at ../../src/gdb/ser-event.c:212
  #1  0x0000000000769456 in invoke_async_signal_handlers () at ../../src/gdb/async-event.c:211
  #2  0x000000000295049b in gdb_do_one_event () at ../../src/gdbsupport/event-loop.cc:194
  #3  0x0000000001f015f8 in gdb_readline_wrapper (
      prompt=0x67135c0 "../../src/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.\nA problem internal to GDB has been detected,\nfurther debugging may prove unreliable.\nQuit this debugg"...)
      at ../../src/gdb/top.c:1141
  #4  0x0000000002118b64 in defaulted_query(const char *, char, typedef __va_list_tag __va_list_tag *) (
      ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ", defchar=0 '\000', args=0x7fffffffa6e0)
      at ../../src/gdb/utils.c:934
  #5  0x0000000002118f72 in query (ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ")
      at ../../src/gdb/utils.c:1026
  #6  0x00000000021170f6 in internal_vproblem(internal_problem *, const char *, int, const char *, typedef __va_list_tag __va_list_tag *) (problem=0x6107bc0 <internal_error_problem>, file=0x2b976c8 "../../src/gdb/i386-tdep.c",
      line=8455, fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:417
  #7  0x00000000021175a0 in internal_verror (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:485
  #8  0x00000000029503b3 in internal_error (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.") at ../../src/gdbsupport/errors.cc:55
  #9  0x000000000122d5b6 in i386_gdbarch_init (info=..., arches=0x0) at ../../src/gdb/i386-tdep.c:8455
  (More stack frames follow...)

It turns out that the problem is that the async event handler
mechanism has been invoked, but this has not yet been initialized.

If we look at gdb_init (in gdb/top.c) we can indeed see the call to
gdb_init_signals is after the call to initialize_current_architecture.

If I reorder the calls, moving gdb_init_signals earlier, then the
initial error is resolved, however, things are still broken.  I now
see the same "Quit this debugging session? (y or n)" prompt, but when
I provide an answer and press return GDB immediately crashes.

So what's going on now?  The next problem is that the call_readline
field within the current_ui structure is not initialized, and this
callback is invoked to process the reply I entered.

The problem is that call_readline is setup as a result of calling
set_top_level_interpreter, which is called from captured_main_1.
Unfortunately, set_top_level_interpreter is called after gdb_init is
called.

I wondered how to solve this problem for a while, however, I don't
know if there's an easy "just reorder some lines" solution here.
Looking through captured_main_1 there seems to be a bunch of
dependencies between printing various things, parsing config files,
and setting up the interpreter.  I'm sure there is a solution hiding
in there somewhere.... I'm just not sure I want to spend any longer
looking for it.

So.

I propose a simpler solution, more of a hack/work-around.  In utils.c
we already have a function filtered_printing_initialized, this is
checked in a few places within internal_vproblem.  In some of these
cases the call gates whether or not GDB will query the user.

My proposal is to add a new readline_initialized function, which
checks if the current_ui has had readline initialized yet.  If this is
not the case then we should not attempt to query the user.

After this change GDB prints the error message, the backtrace, and
then aborts (including dumping core).  This actually seems pretty sane
as, if GDB has not yet made it through the initialization then it
doesn't make much sense to allow the user to say "no, I don't want to
quit the debug session" (I think).

---
## [That-sANiceDonkey/ViolenceRepo](https://github.com/That-sANiceDonkey/ViolenceRepo)@[ced03aa891...](https://github.com/That-sANiceDonkey/ViolenceRepo/commit/ced03aa891a3982054a6eeb832fc3adb3eb6ba44)
#### Monday 2022-04-25 09:40:15 by LukeOx

Fuck you Unreal, Fuck you Github. Suck my dick v1.your mum

---
## [Aberchio/kernel_xiaomi_vayu](https://github.com/Aberchio/kernel_xiaomi_vayu)@[7d856201c2...](https://github.com/Aberchio/kernel_xiaomi_vayu/commit/7d856201c2350c0c1d09646e99c7c733a250199b)
#### Monday 2022-04-25 10:11:15 by Wang Han

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
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: Jagaddhita Jalu <jaguarexodus@gmail.com>

---
## [FeenieRU/Skyrat-tg](https://github.com/FeenieRU/Skyrat-tg)@[cd2bd18cf8...](https://github.com/FeenieRU/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Monday 2022-04-25 11:56:35 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [TheArkProjectLLC/TAP-1](https://github.com/TheArkProjectLLC/TAP-1)@[b9b5d09b56...](https://github.com/TheArkProjectLLC/TAP-1/commit/b9b5d09b56af733070a358f945a4bb623ecd4300)
#### Monday 2022-04-25 12:33:41 by TheArkProjectLLC

Please Support Us & Then Watch What Happens.

As salaamu alaikum Ummah/Family,
I'm asking all of you to please support me in this movement.

A MODERN DAY (Hijrah) TIME HAS DICTATED AND DETERMINED FREEDOM, JUSTICE & EQUALITY
The Perfect Time To Build Our Own Economic System 
Let's make this movement vital. 

1.) Why celebrate the murder of innocent people of color, and then, call it Black History month?
2.) Do you believe that people of color would be better off here in America governing themselves?
3.) Do you believe that the people of Color are systematically oppressed?

Active Revolutionist from Chicago, by way of New Jersey, Atlanta, Birmingham, and now NOLA; dedicating his life to establish a truly independent economic system for the poor and oppressed peoples of America first. Fighting for those faces you see and don't see on the websites: 
www.thearkprojectllc.com www.thebeepinc.com www.beepblackwallstreetbooks.com www.cannabisalisticthc.com

(Podcast): www.spreaker.com/user/16458796
(WhatsApp): https://wa.me/message/JTOS2LDQNU27E1
(Our Survey): www.thearkprojectllc.survey.fm/systematic-oppression

I'm Muslim, I'm Black and I'm American so I guess I have three strikes against me LOL. I'm here reaching out to those concerned about the great divides that no-one wants to address and I'm here to address them head-on (Social Injustice, Islamophobia, Systematic Oppression, etc...). 

I'm the author of these books: 
"Oh, Say Can You See!?" (Secrets) & Truth Is In The Art which shows how passionate I am about what was done and what continues to be done and ignored.

The best book against Systematic Oppression along with an excellent book of poetry intertwined with historical documents that will make you think twice about what's going on (wrong) in the World.

Our Mission, Active Revolutionist, Comparative Religion, Freedom of Speech, The Real Black Voice, Black Lives Matter, Pain Joy Pain, Muslim and Black in America, Oh, Say Can You See Secrets, Truth is in the Art, Willie Lynch, Systematic Oppression, Social Injustice, Islamophobia, Civil Rights, Human Rights, Standing against hate, Black Economic Empowerment Plan, Systemic Oppression of Black, Social Injustice in America, Best Social Injustice Books, Willie Lynch and the Bible

---
## [FreshROMs/android_kernel_samsung_exynos9610_mint](https://github.com/FreshROMs/android_kernel_samsung_exynos9610_mint)@[0df1bbd14c...](https://github.com/FreshROMs/android_kernel_samsung_exynos9610_mint/commit/0df1bbd14cd0b64b23da677a66311e94c076da4a)
#### Monday 2022-04-25 12:34:34 by George Spelvin

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
Signed-off-by: John Vincent <git@tenseventyseven.cf>

---
## [Undying-star/Sonic-into-overdrive](https://github.com/Undying-star/Sonic-into-overdrive)@[f4ea606418...](https://github.com/Undying-star/Sonic-into-overdrive/commit/f4ea606418cae2c02b4934a28b521857ab3c0096)
#### Monday 2022-04-25 12:54:11 by Undying-star

SAM DO THE FUCKING SEGA SCREEN I GIVE YOU THE SPRITES GOD DAMNIT

---
## [trollertroll/Merchant-Station-13](https://github.com/trollertroll/Merchant-Station-13)@[0d9a7145d9...](https://github.com/trollertroll/Merchant-Station-13/commit/0d9a7145d9426ef21f98e3ff656f1f64cca64140)
#### Monday 2022-04-25 14:38:37 by troller

Fuck you *fixes ministation*

I think it's playable now!

---
## [Dnouv/RC4Community](https://github.com/Dnouv/RC4Community)@[ddc933b9cc...](https://github.com/Dnouv/RC4Community/commit/ddc933b9cc0e4d53f4041682d01789ee8477ee0a)
#### Monday 2022-04-25 14:54:58 by Sidharth Mohanty

Official Project License Christening Commit (#147)

@sidmohanty11  was nominated by @Dnouv  and seconded unanimously by all in attendance for creating this milestone commit:

@sidmohanty11 @samad-yar-khan @demonicirfan @Sing-Li @RonLek @Dnouv 

On this "Good Friday 2022"  team members meeting,  @Sing-Li was moved to tears by the open source team spirit and camaraderie displayed (seldom seen in "day job" meetings nowadays)  Thanks for sharing  ! :pray: all !

License choice was voted on by team members (between Apache 2, MIT and GPL):

@sidmohanty11 @samad-yar-khan  @demonicirfan @Sing-Li  @RonLek  @Dnouv @debdutdeb @dudanogueira @abhinavkrin @engelgabriel 

All team members - please post a daytime bitmap of an environment near you  (on this comment)  to "remember this time".    Thanks.

---
## [trollertroll/Merchant-Station-13](https://github.com/trollertroll/Merchant-Station-13)@[9518e920d9...](https://github.com/trollertroll/Merchant-Station-13/commit/9518e920d985e71d741901480010159d1cd03f5e)
#### Monday 2022-04-25 15:07:35 by troller

adds plant gene manipulator

fuck you make a pr before commiting

---
## [Forgind/msbuild](https://github.com/Forgind/msbuild)@[a572dc6b79...](https://github.com/Forgind/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Monday 2022-04-25 17:04:16 by Forgind

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
## [Crozzers/screen_brightness_control](https://github.com/Crozzers/screen_brightness_control)@[3c736e2679...](https://github.com/Crozzers/screen_brightness_control/commit/3c736e26793d47cea4f834e936723482a1c6b12d)
#### Monday 2022-04-25 17:06:36 by Crozzers

Enable cross platform documentation building regardless of OS specific imports.

So when Pdoc would try to import `windows.py`, it would fail if you were building docs on Linux because `windows.py` imports various Windows only libraries that aren't available on Linux.
Furthermore, some of these Windows only objects are used in type hints which are evaluated by Pdoc, meaning I cannot just do what I did in commit 5d5d085.

What we do instead is override Pdoc's module import function (`pdoc.extract.load_module`) to intercept ImportError/ModuleNotFoundError exceptions. Using the exception we then can figure
out what it is that cannot be imported, eg: `from ctypes.wintypes import BOOL`. Once we know this, we then create a fake library in a temporary directory like so:

dummy_imports/dummies/
|-- ctypes/
   |-- __init__.py
   |-- wintypes.py

These fake libraries contain module-level `__getattr__` functions that respond to any request (eg: `from ctypes.wintypes import BOOL`) and return a dummy object that looks like
what you asked for, but is worthless. This allows OS specific imports and type hints to exist as long as the dummy objects are never used within actual code.
This is roughly how these fake modules and dummy objects behave:
```
from ctypes import rando_object
type(rando_object)
> <class 'dummy_imports.DummyObject'>
repr(rando_object)
> 'ctypes.rando_object'
```

Honestly, this is a hack but it's kinda cool at the same time.

---
## [farie82/Paradise](https://github.com/farie82/Paradise)@[6082c95eb3...](https://github.com/farie82/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Monday 2022-04-25 17:29:30 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [SuperNovaa41/tgstation](https://github.com/SuperNovaa41/tgstation)@[50689f89a4...](https://github.com/SuperNovaa41/tgstation/commit/50689f89a40e5e7a2732a0c5fb38c787b69f7d28)
#### Monday 2022-04-25 19:03:45 by LemonInTheDark

Action button refactor/rework: Enhanced Dragging (#65180)

About The Pull Request

I noticed a lot of strange and un-intuitive behavior in action buttons, and got stung by the bloat bug. Damn it hug #58027
I'll do my best to explain what I've changed and why, might get a bit long.
If you want a better idea, read the commits. Most of em are pretty solid, if long.

Whelp. Here we go.
How do action buttons currently work

All action buttons are draggable, to any place on the screen. They're held in an actions list on the player's mob.
Their location in this list determines their position on the top of the screen. If one is dragged away from the top, its position in the list is "saved". This looks really bad.
If two buttons are dragged over each other, their positions swap. (inside the actions list too)
If a button is shift clicked, it is brought back to the position it started at.
If the action collapse button that you likely just mentally edit out is alt clicked, it resets the position of all action buttons on the screen.
If an action is ctrl clicked, it is "locked". This prevents any future position changes, and also enables a saving feature. With this saving feature, locked button positions persist between rounds. So your first o2 canister will always start where you saved it, etc.
Actions and buttons are a one to one link. While there is functionality to share action buttons between two players, this means showing the same object to both. So one player can move a button on another's screen. Horrendous.
This also makes code that modifies properties of the screen object itself very clunky.
Why is this bad

A: None knew pretty much any of this information. It is actually documented, just in a horribly formatted screen tip on the collapse button, you know the one we all mentally delete from the hud.
B: None of this is intuitive. Dragging buttons makes the hud look much worse, and you get no feedback that you even can drag them. Depressing
C: We use actions to make new options clear to the player. This means players can have a lot of action buttons on the hud. This gets cluttery
D: The collapse button is useless. It lets you clear your screen if someone like me fucks up and gives you 2000 actions, but outside of that it just hides all information from you. You never want to see none of your action buttons, just a filtered list of them.
E: On a technical level, they're quite messy, and not fully functionally complete. This is depressing.
What I've done

Assuming the above to be true, how do we fix them?
Well first I'm going to go over everything I changed, including links to major commits. I'll then describe the finished product, and why I made the decisions I did.

Oh and I've moved some of the more niche or technical discussion to dropdowns. Hopefully this makes finding the major functional changes easier

Adds helper procs for turning screen_loc strings into more manageable arrays. This doesn't fully support all of the screen_loc spec, but it's enough for what I'm doing. (f54865f)

Uses these helper procs to improve existing code (6273b93)

Fixes an issue with tooltip code itself. If you tried to hold down a mouse button while dragging onto a tooltip enabled object, it would silently fail. The js made assumptions about the order args came in, which broke when buttons were held down (e0e42f6)

Adds a signal linked to /client/Click(). Surprised we didn't have this before honestly (c491a4a)

Makes /client/MouseDrag() return parent. If we don't do this, any overrides of MouseDrag will never actually be called (2190b2a)
Refactors how action buttons work under the hood (53ccce2)
Basically, rather then generating one button per action, we generate one button per viewer

Starts to change button behavior, more cleanup

Changes the mouse cursor when an action button is dragged. Hopefully
this makes moving things feel less like an accident, and makes you doing
it more clear

Removes the moved and locked vars. This will be more relevant later, but
for now:

Moved exists as a sort of budget "We've been dragged" variable. We can
handle this more cleanly, and the movable type doesn't care about it

Locked is a very old variable that is also not something that the
movable type "owns". It's more an action button thing that's been moved
down.
It exists so an action can be locked in place, and in that locking, be
treated as a "saved location"
(21e20fc)

Because I've nuked move, we don't need to directly set our button's
position. We can use the default_button_position var instead. This is
quite handy.

Please ignore position_action, I will explain that later
(83e265e)

Removes the buttons locked pref

It was another obscure part of action buttons, basically do buttons
start "locked" or not. See previous discussion of locked
(b58b1bd)

Major rework starts here

Alright. Sorry for this, this is where me not commiting regularly starts
to suck. I'll do my best though.

Rather then figuring out an action button's position via a combination
of the moved and ordered vars, we use a separate location var to store
one of a few defines. This makes life later much easier.

Adds tooltip support for dragging action buttons. The way the tooltip
just froze in place when dragging really bugged me, and lead to some
nasty visual artifacts.
This is a bit messy because the drag procs are horrible, but it's
workable

Dropping a button on another button will no longer swap their positions
Behavior instead depends on the target button.

If it's a part of a group (A concept I will explain later) the dragged
button is simply inserted before it in the group's list.

If it's floating on the general hud, we instead position the dragged
button to its right. There's extra logic here to ensure buttons will
never overflow the screen, but I'll get into that later.

Alright. That's most of the refactoring. Time for the larger behavior
changes.

Adds a button palette. This is a separate dropdown that renders
underneath buttons.

image

The idea is to allow for a conceptual separation between "important"
buttons and the ones that end up cluttering the screen.

You can click on the dropdown to open it, then any later clicks that
don't involve actions in some way will autoclose it.

My goal is to come up with an alternative for the action button that
just acted as a way to hide all buttons on screen. Not convinced it saw
much use.

As a side effect of removing that, I've moved its tooltip stuff to the
palette. I've properly formatted it, so hopefully it's easier to read
then the jumble that we used to have.

(You can alt click the palette button to reset all button positions)

Oh and the palette can scroll, since as you'll see later it has a
limited size.
image

Moving on from that, I've added what amounts to action landing buttons.
These allow buttons to rejoin groups, or be positioned at the end of a
line of buttons.
image

They've got a 32x32 hitbox, and only show up when dragging. Hopefully
this makes the system more clear just by dragging an action.

Oh and I've changed how button position updating works. The old system
of calling update_action_buttons on mob every time an action button
changes position is gone, mostly because I've setup more robust
grouping. Will discuss when I get to huds

(0d1e93f)
Adds the backbone behind action button position changes (94133bd)

Moves hud defines to the global folder, safer this way (7260117)

Adds color changing to the palette button, giving some heads up for buttons being inserted into the palette automatically
image
image
Ensures a landing button is always shown, even if it needs to break the
max row rule
Makes palettes auto contract if they have no buttons inside them
Prevents palettes from being opened if they have no buttons inside them
(f9417f3)
How it looks
2022-02-26.02-30-10.mp4
Why It's Good For The Game

Players have more control over the clutter on their screen.
Buttons are available, but not in the way,
Since any player move of a button saves it, any lack of clarity in the way buttons work will be forced out by buttons not just resetting when a new game starts.
We don't overlap any existing screen elements, unless the upper button list gets really long.
The code is much less crummy (I think, may have made it worse it's hard for me to judge my own work)

If it ends up not being as usable as I'd like, I'll rip out the existing changes and just implement the qol and backend stuff. I think it's worth doing though.
Changelog

cl
add: Expanded heavily on action buttons
add: Adds an action button dropdown that sits just under the normal list in the top left. You can drag new buttons onto it to insert them. Click on it to show its contents, do what you want to do, then click again anywhere to contract it. Alt click it to reset all button positions
add: Action buttons will now remember their position between rounds. So if you really like your flashlight right next to your player for some reason, we support that now
add: When you start to drag an action button, docking ports will appear in places that it can be inserted into. (Outside of just floating somewhere on your screen of course)
del: Removed action button locking, and the associated preference. I'm reasonably sure literally none uses this, but if you do hit me up
qol: Dragging an action button will now give you an outline of its size around your cursor
fix: You can no longer cause the screen to expand by putting an action button on the edge of widescreen, and then resizing to standard.
refactor: Refactors action and button code significantly. lots of little things.
/cl

---
## [AnturK/tgstation](https://github.com/AnturK/tgstation)@[d411393e72...](https://github.com/AnturK/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Monday 2022-04-25 20:05:40 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [AnturK/tgstation](https://github.com/AnturK/tgstation)@[4652d4bb63...](https://github.com/AnturK/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Monday 2022-04-25 20:05:40 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [AnturK/tgstation](https://github.com/AnturK/tgstation)@[b86cf89125...](https://github.com/AnturK/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Monday 2022-04-25 20:05:40 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [tukaan/tukaan](https://github.com/tukaan/tukaan)@[b8566316c1...](https://github.com/tukaan/tukaan/commit/b8566316c1423f928ab69b6f8bc0014d6a1c3376)
#### Monday 2022-04-25 20:35:43 by rdbende

Add #StandWithUkraine badge

And Russian warship, go fuck yourself as well

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[201cb8a948...](https://github.com/Buildstarted/linksfordevs/commit/201cb8a948fbc0c1f4f2325e8048cca00a6e15e0)
#### Monday 2022-04-25 23:07:52 by Ben Dornis

Updating: 4/25/2022 11:00:00 PM

 1. Added: nix-shell, but make it lovely
    (https://t-ravis.com/post/nix/nix-make/)
 2. Added: .NET Framework April 2022 Cumulative Update Preview
    (https://devblogs.microsoft.com/dotnet/framework-april-2022-updates/)
 3. Added: Intro to BPF CO-RE
    (https://layalina.io/2022/04/23/intro-to-bpf-co-re.html)
 4. Added: Start with Who, not Why
    (https://softwaredoug.com/blog/2022/04/23/start-with-who.html)
 5. Added: The Trouble With Rewrites
    (https://solutionspace.blog/2022/04/25/the-trouble-with-rewrites/)
 6. Added: The Problem with Software Methodologies
    (https://www.chrisbehan.ca/posts/the-problem-with-software-methodologies)
 7. Added: To vendor, or not to vendor
    (https://penkovski.com/post/to-vendor-or-not-to-vendor/)
 8. Added: Speeding up Prettier locally and on your CI with dprint
    (https://david.deno.dev/posts/faster-prettier-with-dprint/)
 9. Added: Six things I sort of believe about making music/art
    (https://www.johnwhiles.com/posts/music-production-lessons.html)
10. Added: Monolith in Cloud
    (https://nsirap.com/posts/062-monolith-in-cloud/)
11. Added: Tricks for dealing with “reviewer’s block”, for the beginner engineer
    (https://www.karthiknaidu.xyz/tricks-for-dealing-with-reviewers-block-for-the-beginner-engineer/)
12. Added: One year of sales
    (https://nts.strzibny.name/one-year-of-sales/)
13. Added: Can you use a WebP file as an Open Graph Protocol image?
    (https://www.ctrl.blog/entry/webp-ogp.html)
14. Added: Criticisms & Curation
    (https://fujixweekly.com/2022/04/24/criticisms-curation/)
15. Added: Deploy any Web App to Lambda in 60 seconds | Kevin Wang's Blog
    (https://thekevinwang.com/2022/04/25/any-web-app-on-lambda/)
16. Added: CRT Manufacturing
    (https://vintagetek.org/crt-manufacturing/)

Generation took: 00:07:40.5730326
 Maintenance update - cleaning up homepage and feed

---
## [jukibom/FlyDangerous](https://github.com/jukibom/FlyDangerous)@[65e91af8a2...](https://github.com/jukibom/FlyDangerous/commit/65e91af8a2aa81d550acbd2561f2e8d994d4d2bb)
#### Monday 2022-04-25 23:18:04 by Jay Faulkner

fix: incorrect conversion to / from milliseconds on leaderboard

bloody hell don't I feel daft writing that whatever-the-fuck-that-was

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[4dc039d93c...](https://github.com/UnderMybrella/usa/commit/4dc039d93c003c6cd183dfe74c0f310d9ab87cfc)
#### Monday 2022-04-25 23:57:23 by MarkiSpider

Update 64 files @ Mon, 25 Apr 2022 23:57:21 GMT
This site update changes karen-archive.html, case-directory.html, thealienalliance.html, thebutterflysoldiers.html, schedule.html, aretheyalium.html, logs.html, images.html, theoracle.html, michaeljackson.html, logs.html, user.html, zeusandfriends.html, thebannerborn.html, reviews.html, dashboard.html, idkbro.html, thecaptain.html, thedude.html, oopsalbangers.html, inhumanresources.html, 914222-195242514914101.html, ijustmadeyoulookunderthere.html, the-d_.html, user8118151241161251919.html, iinhumanresources.html, terfwar.html, departments.html, moriarty.html, auth.html, cases.html, usa-home.html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, legal.html, girlofthe21stcentury.html, capitalism.html, MichaelJackson.html, fuckem.html, NerdFiction.html, shatteredbysomeone.html, terrorblycute.html, everyone.html, messenger.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, lolgotyou.html, sexygoldarms.html, thefounders.html, the-baboonies.html

---

