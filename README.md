## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-12](docs/good-messages/2022/2022-05-12.md)


1,790,075 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,790,075 were push events containing 2,904,163 commit messages that amount to 201,834,313 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a3c8013b45...](https://github.com/tgstation/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Thursday 2022-05-12 00:02:19 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

---
## [schqiushui/android_kernel_oneplus_sm8250](https://github.com/schqiushui/android_kernel_oneplus_sm8250)@[38b0bd0f25...](https://github.com/schqiushui/android_kernel_oneplus_sm8250/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Thursday 2022-05-12 00:39:13 by Linus Torvalds

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
## [ProjectIgnis/LFLists](https://github.com/ProjectIgnis/LFLists)@[4c4fe013b4...](https://github.com/ProjectIgnis/LFLists/commit/4c4fe013b453e19b0f137983f95c35d51842b83f)
#### Thursday 2022-05-12 01:10:43 by pyrQ

Rush whitelist: Added new Rush cards + official releases

From "Go Rush Deck - Galactica Arrive":
- Cosmo Titan
- Sorapuyo
- Transamu Klein
- Transamu Arrive
From "Megaroad Pack":
- Strong Strike Dragon Metagiastar F
- Sevens Road Magician (alt art)
- Sevens Road Witch (alt art)
- Magic Curtain
- Darkness Road
- Sevens Road Protection
- Omega Guitarna the Supreme Shining Superstar
- Princess Omega the Supreme Shining Superstar
- A.I. Bear Can
- Ama Lilith
- Psychic Omega Blast
- Cross Target
- Featuring Omega
- Shoulder Phone Nyan Nyan
- Oriental Tiger
- Imptailing Crisis
The "Yu-Gi-Oh! Rush Duel LP Volume 1" promo:
- Accel Wonder Pebble

In addition, the cards from "Go Rush Deck - Galactica Arrive", "Go Rush Deck - Jointech Attack", "Go Rush Deck Bonus Cards", the "Yu-Gi-Oh! SEVENS Luke! Explosive Supremacy Legend!! Volume 3" promo, the "Saikyō Jump June 2022" promo, and the "Yu-Gi-Oh! SEVENS My Road Academy Volume 1" promo are now out of pre-release.

ProjectIgnis/BabelCDB@3fc186d566c63b864da5f989dcdd75e66d566c1c

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[fb5cf9102e...](https://github.com/Hekzder/mojave-sun-13/commit/fb5cf9102e3f942b3b47e985a4dc19d671932b3e)
#### Thursday 2022-05-12 01:13:21 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

(cherry picked from commit 4610f700eb74a3a41555e69c4904ad897caf2d99)

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[9fbcb32a6d...](https://github.com/Hekzder/mojave-sun-13/commit/9fbcb32a6d72113b5ac781a61c5a6e12a47ebf5f)
#### Thursday 2022-05-12 01:13:21 by tralezab

Super Mega Mob Spawn Refactor (#63279)

About The Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining Mob Spawn Refactor

The Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining Mob Spawn Refactor is my attempt to clean up the file structure, the code, and the type tree for mob spawns.

    Splits mob spawn types into corpses (dead spawns) and ghost roles (living spawns you can possess). The vars that didn't make sense for corpses and vice versa for ghost roles are now appropriately there
    Because of above, there are no longer the fucking "death, roundstart, and instant" vars. thank god
    Removes a lot of single or very few used vars, whose properties can be applied on special().
    All Mob Spawns are given fitting folders instead of just being stuck in a single ghost roles file. Corpses are in the corpse folder, Ghost Roles are in the ghost role folder. Only exception are drones which should stay near their respective homes
    Just generally cleaner all around you know
    spider structures file renamed to spiderwebs now that spider eggs are gone

Why Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining Mob Spawn Refactor Is Good For The Game

The Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining Mob Spawn Refactor cleans up so many terrible cases and uses
Changelog For The Super Hyper Ultra Ultimate Deluxe Perfect Amazing Shining Mob Spawn Refactor

cl armhulen
refactor: Mob spawns are refactored, no more assortment of "random, instant, and roundstart" vars on every mob spawn type
refactor: if there are some minimal differences in how mob spawners feel, that's why!
/cl

(cherry picked from commit 82615e7462989739622d4ef135cc8647512ce141)

---
## [entrez/xNetHack](https://github.com/entrez/xNetHack)@[879897d885...](https://github.com/entrez/xNetHack/commit/879897d885462664cabcd521ca62fc3fd5a4fcf5)
#### Thursday 2022-05-12 02:27:36 by copperwater

Add black mold

A new monster? In xNetHack???

This has been planned for quite a while, and only now gotten around to.
The general idea is adding a member to the F class that actually might
pose a threat to the player rather than being firmly in assists-only
status. This is particularly relevant since F monsters grow on moldy
corpses.

The general details of the monster come from SporkHack's gray fungus,
via EvilHack which imported it fairly directly from there. Differences
include:
- It's named "black mold" rather than "gray fungus" because black mold
  is a real-life thing that can grow in living spaces, making the
  inhabitants sick.
- It's modeled after the other molds. It has similar stats, no active
  attacks, etc.
- It doesn't confer poison resistance when eaten. Instead it makes the
  consumer deathly ill when eaten. (Though this is curable by vomiting
  and is therefore labeled as FoodPois -- it's a little weird that the
  sickness from the passive attack is not curable by vomiting and the
  sickness from eating it is, but that's due to the different ways it's
  making you sick, one by having it in your digestive tract and one by
  inhaling spores.)
- It appears quite late for a F monster, with a difficulty of 8.
- The Brewing Patch applies to it, allowing black mold to be fermented
  in fruit juice to later turn to sickness.

Unlike in EvilHack, monster illness is not implemented and so the black
mold's passive attack does nothing when it hits a monster.

---
## [girls4bed/girls4bed](https://github.com/girls4bed/girls4bed)@[063989fb82...](https://github.com/girls4bed/girls4bed/commit/063989fb828afeff1129db6d0722e2d202f4a903)
#### Thursday 2022-05-12 02:31:28 by Zkmodelsgirlsageny

Girls 4 Bed Call Girl Party

ussian Lahore
#Fuckinggirls
Escort woman Lahore
Sexual satisfaction Lahore
#Hotelgirls
Call girl Lahore
Callgirls Lahore
#Teachergirls
Girl friend Lahore
Independent escorts Lahore
#Studentgirls
Greek Lahore

---
## [AaronSong321/dota2ai](https://github.com/AaronSong321/dota2ai)@[ac687b8232...](https://github.com/AaronSong321/dota2ai/commit/ac687b8232e09b5b27d3115a731a49437a329957)
#### Thursday 2022-05-12 04:48:24 by Aaron Song

Add team mekansm purchase mechanism, and fix many issues. (#61)

Fix chen using persuasion at allies; Fix crystal_maiden cancel frostbite;
Fix the issue that bots don't use abilities when their mana is not enough without mana cost reduction;
Bots now buy mekansm in terms of the team;
Fix ember_spirit rarely use abilities; Fix bounty_hunter don't use track;
Add bristleback hairball; Fix bristleback use quill_spray at unit targets
Fix alchemist berserkers_rage;
Add cm_stop_freezing_field, lycan_wolf_bite;
Stop using sven_strength_of_god, lycan_shapeshift when the target is too far away;
Increase the desire of jakiro using liquid_fire at towers;
Fix doom using devour at ancient targets;
Fix earth_spirit using boulding at unit targets;
Fix furion sprout bugs;
Cancel qop_sonic_wave losing argets after chasing;
Add a feature that bots avoid allies with winters_curse;
Notify teammates when buying team items;
Fix earth_spirit ability usage wrong target;
Fix abyssal_underlord use abilities at creeps;
Fix doom acquired abilities;
Fix ember_spirit abilities;
Decrease the desire of enigma using midnight_pulse at creeps;
Add faceless_void_time_walk_reverse;
Improve natures_prophet not blocking friend melee heroes;
Fix medusa bugs;
Add terrorblade demon_zeal, terror_wave;
Fix windrunner ability level up;
Avoid batrider using napalm when unnecessary;
Fix chen, doom using holy_persuasion or devour at high-level creeps;
Fix clinkz using death_pact at ancient creeps;
Fix earth_spirit, faceless_void using moving abilities at game start;
Low the desire enigma, jakiro using AOE at creeps;
Improve furion sprout to not block friends;
Avoid mirana using ultimate when enemies have dust or gem;
Add ogre_magi_smash;
Fix wraith_king summoning skeleton warriors;
Lower the desire of batrider, troll_warlord, treant using ultimate;
Add troll_warlord_rampage;
Avoid lion, spectre using ultimate when unncessary;
Force every bot to buy dust when enemy has invisibility abilities or items;

---
## [lamp-project/library](https://github.com/lamp-project/library)@[033884ce4c...](https://github.com/lamp-project/library/commit/033884ce4c6d5352b809088293ee9f6873141c3a)
#### Thursday 2022-05-12 04:49:56 by Sajjad shirazy

Stavrogin's Confession and The Plan of The Life of a Great Sinner: With Introductory and Explanatory Notes

---
## [flrsh/goonstation](https://github.com/flrsh/goonstation)@[bdad398f9e...](https://github.com/flrsh/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Thursday 2022-05-12 04:52:02 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[8e40aa744f...](https://github.com/clamor-s/u-boot/commit/8e40aa744f576cdf06ae1342bf4766beddd6f958)
#### Thursday 2022-05-12 04:57:36 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [kc446/flask-final](https://github.com/kc446/flask-final)@[c798134fbd...](https://github.com/kc446/flask-final/commit/c798134fbd72316b18ee41b10da60afa23f8c11f)
#### Thursday 2022-05-12 05:06:29 by kc446

that took a fucking ETERNITY to get working holy shit

---
## [Edzandpieces/rails-watch-list](https://github.com/Edzandpieces/rails-watch-list)@[ab39b195ec...](https://github.com/Edzandpieces/rails-watch-list/commit/ab39b195eca69ec72c33433f6910b34638cc9830)
#### Thursday 2022-05-12 05:32:41 by Edmund Oh

changed that fucking url to poster url. I hate my life

---
## [lengyuqu/gitea](https://github.com/lengyuqu/gitea)@[3725fa28cc...](https://github.com/lengyuqu/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Thursday 2022-05-12 06:07:38 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [hanterzhu/rathena](https://github.com/hanterzhu/rathena)@[d617d9f083...](https://github.com/hanterzhu/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Thursday 2022-05-12 08:30:20 by Aleos

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
## [LandSandBoat/server](https://github.com/LandSandBoat/server)@[69b7bb4322...](https://github.com/LandSandBoat/server/commit/69b7bb43228902ad0fb0648d8ec9f4fabe0241a4)
#### Thursday 2022-05-12 08:47:32 by NeuromancerXI

Fixes SQL Async Causes High CPU Load
Noticed very high CPU Load on an idle server instance. With the guidance
of zach2good, added a sleep condition to prevent the process from
running wild and eating CPU for breakfast, lunch, and dinner.

Co-authored-by: Zach Toogood <zrtoogood@gmail.com>

---
## [himar33/Furries-Annihilation](https://github.com/himar33/Furries-Annihilation)@[4fed9616ca...](https://github.com/himar33/Furries-Annihilation/commit/4fed9616cad623d41499098062ab9b1eba8be953)
#### Thursday 2022-05-12 10:22:07 by Marc Pavon Llop

Marc did not do this

Im Pol. Marc swapped pc with me. Pen didnt work in this pc. Fuck you wacom

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b76d1c1807...](https://github.com/mrakgr/The-Spiral-Language/commit/b76d1c1807fd3faad754934b5fef9aef566ce277)
#### Thursday 2022-05-12 11:15:05 by Marko Grdinić

"9:10am. The last volume of UQ Holder sure was an absolute turd. The rest had its good points, he should have just let the series unconcluded. I wish I had been reading vol 4 of Fable instead.

At any rate, before I move to the next task on my agenda, let me test Rhino a bit more. I need to make sure that Moi's exports are good on that water bottle.

9:40am. Let me start. First let me try out Rhino's poly export again. Good thing I did not uninstall it yesterday.

10am. Let me make the /wip/ post.

///

>>896672
>The quad remesher was actually better when it comes to doing NURBS to poly conversion in Rhino.
I've been concerned whether I am unfairly bashing Rhino since a water bottle which I've tested it on and the rig here which I did in Moi are two separate objects. The rig is boxy, while the bottle is curvy so the later should be a tougher job for the exporter. So I actually went out did a few obj exports from Rhino to Blender. I also exported the Rhino model into Moi and from there into obj. My conclussion - Moi's exporter is in fact way better than Rhino's and even if you are focusing on NURBS modeling in Rhino, it would be worth getting Moi just to get the better export functionality.

///

10:20am. Ok, I am done with that experiment. I really like Moi quite a bit. It is really too bad yesterday that I did not know about how great loft was. It would have saved me a lot of headache.

When something goes wrong like it often does in Moi and you are dealing with an undefined error, it is easy to waste more time than you'd imagine.

10:25am. First of all, let me clean up the assets a bit. I have the rig in 4 separate files. Let me collate into just one.

I won't bother reporting those rig grate errors as it would just waste my time.

10:25am. Done, now I have only a single file for the rig as it should be. I also unistalled Rhino 7. I will not be using it.

More is not better. Moi really demonstrates how a compact, refined design beats having a lot of features. I went the same route with Spiral.

NURBs are not going to get displaced by poly no matter how good Blender's tools get at it.

10:30am. Now...How about I export the rig and texture it? I kind of want to leave it aside, but since it won't take long at all, I should just get to it.

10:40am. I'll go with 50k faces, the mid range export for the rig. It would be an insane poly count for a game asset, but for illustrations I can go as far I want. Let me texture it. It should be easy.

...Ah crap. I'll need to UV unwrap it. Later, later. Let me texture it for the time being.

10:45am. No, it does an absolute crap job at it. Also I wonder, ah the GPU timeout got reversed when I uninstalled Rhino. What a pain.

I have no choice. Let me import it in Blender and unwrap it. I should also link the mesh data for the screws.

Oh, Moi was nice enough to do that on its own. Or maybe it was Blender itself during the import.

10:50am. I did not count on UV unwrapping being such a breeze here. I turns out that Moi puts in sharp edges and converting those into seams is quite easy. Let me pack these.

///

>>896723 (You)
Serious question, why would you use nurbs for any of this?
It would take literally seconds to get the same result with poly modeling and the end result would have perfect topology and almost certainly be sub 200 polys.
In fact, here you go. The differences can be accounted for with normals and texturing.

///

///

>>896728
>Serious question, why would you use nurbs for any of this?
There are bunch of benefits, but I just want to find the right way of modeling. There are 4 competing styles and I've been moving between them:

* Box modeling
* Subd modeling
* Sculpting
* NURBs

In you own model, you did the overall shape, but you didn't do that dent. The way I did it in Rhino is by cutting off a piece to the size, scaling it down and insetting before booleaning union it back again. If you took that approach, the boolean cleanup would take you a while and it would certainly take longer to do than a NURBs model. It is not like drawing a curve and revolving it is hard to do in NURBs.

Suppose you took a box modeling approach (no subdiv) you could draw a polyline and revolve it to get the bottle shape. I am guessing this is probably what you did in your own model. But unlike with the NURBs or the subdiv or the NURBs approach, you are now stuck with your target poly count. You could subdiv it, but you'd need to clean up the top and bottom parts so don't get pinching where the triangles meet.

https://www.youtube.com/watch?v=PSqHeCq7Kio&list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&index=11

With the subdiv approach rather than revolving a curve, you'd have to start with a plane and extrude and scale it upward. But then you'd have to apply the modifier anyway to get the bottle dent. You could try doing it without the boolean, but you'd have to do some real wizardry to get the shape directly. I wouldn't be able to do it without much effort at my level. It is really annoying to have to keep track of topology like this and I'd rather not do it unless I can't help it. I admire the techniques he showed me in that playlist, but subdiv modeling the right way is black magic.

///

///

>>896732
With the sculpting approach, the process would be the same as with NURBs. You'd probably want to start out with a very high poly model and downscale to get the appropriate count. Using high density meshes makes booleans even easier than they are with NURBs so the design itself would be easy and you wouldn't need to worry about cleaning up that dent, but you might need to retopo and need to put in extra effort during UV unwrapping afterwards. You can do a lot more with sculpting than you could with NURBs, but you would not benefit from the added flexibility of sculpting while modeling an object such as this. You'd need to spend time wrangling the Zremesher to get a good result. Retopoing by hand would not be that much different from box modeling it to begin with. Unlike retopoing a char model, you'd want precision for a model such as this so that in fact is the retopo approach you'd take, to box model it from scratch.

The NURBs approach would be the easiest for a hard surface object such as this and would give you the most succinct representation of it. You don't have to worry about the poly count or the topology. If you want to turn into a poly model you can export it as low or high as you need to. The sharp edges that Moi gives you out of the box can be converted into seams so UV unwrapping is no problem either.

///

11:45pm. Doing some /3/ posting.

Actually the seams might be a bit too aggressive in places, but they are fine overall.

Let me finally export the model into substance. I've decided to go with just a single UV tile. It is not problem for now.

First of all, let me change the GPU registry settings since Pt is complaining.

12:10pm. Now I am having some trouble with Substance. The imported modeling has those ugly normal shading artefacts that I'd epect for a badly topologized model such as this. They don't appear in Blender, but they sure do here.

12:15pm. Damn it, it is never easy is it? I am going to have to ask about this.

Before that, let me try exporting the smoothing groups.

There is also the compute tangent space per fragment option. I never looked into what it does, but maybe I could try turning it on.

https://forum.substance3d.com/index.php?topic=7034.0
> I just did a quick test, exporting from maya as a .fbx I get the result you are seeing, exporting as .obj I dont get the result and get what you should expect.  Looking at the mesh in maya the hard/soft edges are set correctly, however, you have a bunch of unwelded verts, and doing a quick weld fixed the issues with the .fbx.  Also, just quickly looking at the mesh, you need to clean up the N-gons, even though painter will try to triangulate it for you, you have more control if you do it yourself.

Hmmm, do I have unwelded verts?

Oh yeah, bunch of thme.

12:35pm. Let me ask on the Substace Painter forums. There is no point in bashing my head against this. I should just texture the thing normally and ignore the issues here.

https://community.adobe.com/t5/substance-3d-painter/ct-p/ct-substance-3d-painter?page=1&sort=latest_replies&lang=all&tabid=all

Damn it, I registered to the wrong forum. Let me ask here.

12:55pm. Fuck. Changing the conversation type ate my post!

...Thankfully it was backed up. Phew. It would have been annoying had that not been the case.

https://community.adobe.com/t5/substance-3d-painter-bugs/imported-object-from-blender-does-not-have-sharp-normals/idi-p/12938244#M27

I'll get an answer here at some point. Until then, I should just texture the thing. It is not like these strips will prevent me from doing that.

1:10pm. Let me take a break here. The auxuliaries really ate up my morning today. I'll get the texturing done, no problem today. After that I'll resume the Zbrush hard surface course."

---
## [MA5951/RapidReact](https://github.com/MA5951/RapidReact)@[2141fe4888...](https://github.com/MA5951/RapidReact/commit/2141fe4888a98d9bceaeaba218a59948a3996f63)
#### Thursday 2022-05-12 11:20:16 by EilonK05

End of Season 2022 ✨✡

Wow! What an incredible season we had :relaxed:
We learned so much and we are really proud of what we accomplished.

Simon we love you 💖❣ You taught us so much and we appreciate your help and efforts a lot.

To Asaf, you were a great a head of our lovely programming team (rashaz shshs) and we already miss you 😢
Thank you for making the iconic programming playlist and we are sure that we will come back to it the next season 🎶

We are incredibly excited for the next season and we can't wait.
Thank you to all of the people who took part in this amazing season 💕

Love you all,
Programming Team 2022

Co-Authored-By: Konata <42537566+konata-chan404@users.noreply.github.com>
Co-Authored-By: yoavkaplan123 <70645788+yoavkaplan123@users.noreply.github.com>
Co-Authored-By: noya-isaiah <67971686+noya-isaiah@users.noreply.github.com>
Co-Authored-By: Asaf Harel <45461162+Asaf-Harel@users.noreply.github.com>
Co-Authored-By: yuvalrader <45494935+yuvalrader@users.noreply.github.com>
Co-Authored-By: Simon Kharmatsky <22105518+ScarletMetal@users.noreply.github.com>

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[065a6f4e69...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/065a6f4e696de94e3fe42add1b63b0ea943072bb)
#### Thursday 2022-05-12 11:51:27 by AmyBSOD

New monsters

omg offensive gross irritating bad amy go to hell you evil demon!

---
## [robbertapir/tgstation](https://github.com/robbertapir/tgstation)@[cd1b891d79...](https://github.com/robbertapir/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Thursday 2022-05-12 11:53:34 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [chrfoyer/Yes_SEP2](https://github.com/chrfoyer/Yes_SEP2)@[1e7446260f...](https://github.com/chrfoyer/Yes_SEP2/commit/1e7446260f7d3da6a6cd68f8333e441b69016079)
#### Thursday 2022-05-12 11:54:52 by Raedrim

Alerts

What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.

---
## [scamdom/KKRT_12_kernel](https://github.com/scamdom/KKRT_12_kernel)@[cc6c60d979...](https://github.com/scamdom/KKRT_12_kernel/commit/cc6c60d979e819c57ede43fe68c058d5aeb17cab)
#### Thursday 2022-05-12 13:01:33 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [jocrl/cockroach](https://github.com/jocrl/cockroach)@[ac27006751...](https://github.com/jocrl/cockroach/commit/ac27006751f582e5d7718f349867d72a061ccb6c)
#### Thursday 2022-05-12 14:11:53 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03 p`, or
- `1:03 P`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Typing `1:03pm`, `1:03PM`, or other versions without the space before `PM` still do not
work.

Additionally, typing the keys in `1:03 pm` will lead to the input being `1:03 PMm`, as the
`M` autofill after `p` is typed. The `1:03 PMm` input in the text box is still
accepted, but it does look weird and will likely be annoying to users who will
delete the trailing `m`.

Alternate approaches not pursued

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[960ea8575a...](https://github.com/treckstar/yolo-octo-hipster/commit/960ea8575acb46687161c2221a8a58e0756079d1)
#### Thursday 2022-05-12 14:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [MMMiracles/tgstation](https://github.com/MMMiracles/tgstation)@[0504c0a2b4...](https://github.com/MMMiracles/tgstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Thursday 2022-05-12 15:21:17 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [ENGO150/WHY2](https://github.com/ENGO150/WHY2)@[b098af3ebf...](https://github.com/ENGO150/WHY2/commit/b098af3ebf1e042bf4f30ec215a3dd41e5d72450)
#### Thursday 2022-05-12 15:24:13 by ENGO150

separated build.sh into functions

uhm, yeah - the file was kinda shitty so..

---
## [webpro/wireit](https://github.com/webpro/wireit)@[c85c022769...](https://github.com/webpro/wireit/commit/c85c02276975a1a86cbf509a7e9a353d5f0a19a8)
#### Thursday 2022-05-12 15:46:37 by Alexander Marks

Error when trying to cache outside of package (#182)

It's currently not possible to locally cache an output file that isn't inside of the package directory. We check for this case when we delete and throw, but not when we cache. So if you are caching but have cleaning disabled, we would silently weirdly save the output file to a parent directory, and then not restore it.

Now this is an error.

Note we could in theory do this during analysis, but I'm not 100% confident in my ability to correctly detect this case given all of the possible magic glob syntax, so for now it's safer to just do it at runtime. (see https://github.com/google/wireit/issues/64).

Also note we could in theory support caching files outside of the package root, but we'd have to do something like a tarball for the local cache, instead of simply copying into `.wireit/<script>/cache/<hash>`. We should think carefully about whether we want to do that, though, so I'm not dealing with that for now.

Fixes https://github.com/google/wireit/issues/181

---
## [jws85/ergodox](https://github.com/jws85/ergodox)@[5350df4e36...](https://github.com/jws85/ergodox/commit/5350df4e3648ab030bc32e6da3f2e071285b397f)
#### Thursday 2022-05-12 16:25:48 by J. W. Smith

Swap from one-shots to vanilla mods

I'm getting a lot of stuck mods, and I am not so good at remembering
what keys I've pressed, so I end up repeatedly pressing mods until
everything comes unglued.

To be honest, I'd be happy if the OSM didn't have multi-tap to hold a
mod --- I will tap once for the one-shot, and I'll hold the key down,
but I almost never multi-tap to hold down.

There's a bug in QMK, issue 3963, that tracks a related issue.

A common recommendation is to integrate Callum Oakley's custom oneshot
implementation, see [1], and [2] for an example of its implementation.
I hear it has quirks of its own though.  I may try this in a free
moment (not any time soon).

[1] https://github.com/callum-oakley/qmk_firmware/blob/master/users/callum/oneshot.h
[2] https://github.com/iandunn/dotfiles/blob/6f87a52fba5340437dca16b7f1fd7d6cabf7eaf6/ergodox-ez/ordinaryish/keymap.c

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[789fd318e2...](https://github.com/mrakgr/The-Spiral-Language/commit/789fd318e217642de0ff90df56c5214ba3394941)
#### Thursday 2022-05-12 17:50:10 by Marko Grdinić

"2:30pm. Done with breakfast. Let me chill for a bit longer and then I will start texturing.

2:55pm. Let me start.

Focus me. Let me start texturing. First of all, let me do the roughness.

3:10pm. Are the UVs wrong, what is going on? It seems I really should have up the texture resolution higher. Right now even 4k feels too low. Since the texture has so many small pieces I could get better efficiency by lowering the pixel margin. I'll consider that later.

3:45pm. Focus me, stop responding in the /wip/ thread. Just put that later of dust on the rig and you are done.

4:40pm. That took a while. I have the render done. Let me post it.

5:10pm. No, it is really hard to add those smallish chamfers in Moi. Between the calculation failures and navigation difficulties, I am having a hell of a time. Let me try a bevel mod in Blender. That should do the trick.

I get shading issues almost immediately. What about the bevel shader?

https://docs.blender.org/manual/en/latest/render/shader_nodes/input/bevel.html

Cycles only.

For the smaller highlights I'd really want something like Blender's cavity.

5:40pm. I just wasted an hour messing with this for no reason. To begin with I knew I would not be able to take care of these small edges. There are too many of them and  trying to bevel thought would spike the model complexity significantly. From the start I intended to use something like a round edge shader. But it does not seem like Clarisse has it.

https://forum.isotropix.com/viewtopic.php?p=16361

Hmmm, I see. Using the curvature node I could apply a tiny bit of displacement or a bump. That should give a bit of a pop to the edges.

6:50pm. Done with lunch. Right now I am reading Fable and feeling drowsy.

The reaction on /wip/ is that I made the lighting too dark. Yeah. They're right. I'd never accept this on other poeople's renders, but when doing my own stuff I get too easily into subtle contrasts that don't mean anything. I think I made this same mistake with that vines render.

The problem is that Iray put in the shadows and the background and I had trouble dealing with that. I couldn't even save as png properly as it made the background fully transparent causing it to show up as white. I had to use jpg instead.

The way things are going I'll start obsessing about those small edges. Forget it.

Shaders exist for a reason. I'll stick to my plan and not worry about it. I'll believe that Clarisse will do a good job.

Whether I'll manage to get to the end of this project before I decide to start grinding 2d remains to be seen.

The truth is, I hate how much hassle Clarisse is compared to Blender.

7pm. I don't think I am really the target audience for them. But nevermind that.

Focus me. I need to make one last decision for the day. I know I was slow as a snail today, but I feel like I am more in my usual grove.

7:10pm. Done with vol 4 of Fable.

Ok, forget doing the render in Cycles. I've spent enough time on the rig. I only really intended to model and texture it and that is what I've done. Good job me. Tomorrow, what I should do is get back to the Zbrush course.

7:15pm. That Zbrush course will be special as it will be the last bit of 3d learning that I'll do. After that I'll seriously consider changing my whole appoeach. Thought I have the goal of finishing the room in 3d, I do not need to feel absolutely obligated to do that.

I am way over all limits of how long mastering 3d is taking me. Thanks to being so deep into it, I can alreay tell that the anon in /ic/ who was ranting that 3d takes a lot more than just 2d was right.

7:20pm. My feelings are a bit complicated. I am getting the urge to grind 2d, but I also want to do more stuff in Moi as I got the bug for it. Even right now, I do feel like setting up a cool render in Cycles.

And I kind of want to ditch Clarisse. At this point making whole cities and kitbashing assets is the furthest thing from my mind.

Deep down I feel like I could do 2d now.

3d has taught me that getting the result you want is all a matter of how much effort you put into it. Sculpting seemed hard, but then I spent a whole month on that base mesh and got it looking good in the end.

In 2d, the rules should not be any different even though begs think they are. I want to try layering stuff and working towards a better result.

7:25pm. Yeah, forget that grand plans. What do I want to do?

It is really quite nice that I got some skill in modeling, texturing and shading. I should just do just stimulates me directly and forget the really big things until I am ready for them.

Right now I am modeling my room. Imagine if I want to do the background beyond the balcony doors. Does it make sense to start modeling everything outside or would it be better for me to just take a photo and blur it a bit.

In the first place, imagine I could just draw it, would I be spending my time modeling all this?

In the VN will I aim for a photorealistic style? Of course not.

7:30pm. More, I want more. Let me get this Zbrush course out of the way. Right now not knowing hard surface sculpting well enough is my only real obstacle to finishing my apprenticeship as a 3d illustrator. After I have my fill of it, I'll have enough knowledge to stand on my own two feet. I already have an almost complete foundation, so what is spending another week to grasp this? Nothing.

7:35pm. As for that rig, what is preventing me from just posting a direct screen shot is that shading artefact on the side. I need to get an answer from the devs and resolve it first.

7:40pm. Zbrush, Zbrush, Zbrush...I'll change my mindset solely to getting through the course. There are interesting things to learn in it. For the next week I should go through it at a leisurely pace. After that I'll get serious about 2d.

7:45pm. Even though I'll be changing my focus to 2d, it is not like I won't have 3d at my beck and call.

Sigh, my fall seems to have no end. Deep learning, pen stylus neither will get me particularly closer to the Singularity that I seek. I can't do much without the algorithms to start me off on my path or the right hardware. Right now the research is focused on machine learning, but on machine learning that can be done on the GPU. The later is a much harder hurdle to clear, so it is not a wonder that I failed.

Since know enough when to call it quits, I should just have some fun in life. If ML is really meant to be, the agents that will turn my rough sketches into whole worlds will come to me. Until then I should just focus on the sketches."

---
## [jpfraneto/the-infinite-jest-v2](https://github.com/jpfraneto/the-infinite-jest-v2)@[c5751b0be5...](https://github.com/jpfraneto/the-infinite-jest-v2/commit/c5751b0be5fba01b2c10e21b2247673743f3a4e3)
#### Thursday 2022-05-12 18:21:02 by jpfraneto

Day 106. The functionality is looking great, I feel complete. Today I used the app as I was cooking lunch to my daughter and it is amazing to find a piece of cookie hidden in the middle of all the amazing amount of noise that there is. This is going to be useful in my life.

---
## [nik9000/elasticsearch](https://github.com/nik9000/elasticsearch)@[37ea6a8255...](https://github.com/nik9000/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Thursday 2022-05-12 20:10:54 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [SlayerIbn/i-rule-translations](https://github.com/SlayerIbn/i-rule-translations)@[2da56ed7da...](https://github.com/SlayerIbn/i-rule-translations/commit/2da56ed7daa171bca85e2e16fb3ff70acd0acd4b)
#### Thursday 2022-05-12 20:11:56 by SlayerIbn

"Bucle" is pure shit and doesn't have the meaning that I want, "Ciclo" is fucking perfect

---
## [Maetrim/DDOBuilder](https://github.com/Maetrim/DDOBuilder)@[6f3f489182...](https://github.com/Maetrim/DDOBuilder/commit/6f3f4891824676be5e33cc4515b25c5846f04815)
#### Thursday 2022-05-12 20:47:29 by Maetrim

Build 1.0.0.161

Fix: "Past Life: Tabaxi Trailblazer" now awards its +1 Trap save bonus
Fix: The equipment view will show the correct set bonus image where the name also matches an enhancement name (see Celerity)
Fix: Fury of the Wild: Primal Scream updated to also mention and affect Dexterity (Reported by Khalibano)
Fix: Item "Legendary Wild Flame" no longer has the "Trace of Madness" augment option (Reported by Hobgoblin)
Fix: The Filigree set bonus text for "Dragonsoul" is now correct at 5% spell critical damage (values were correct in effects) (Reported by Hobgoblin/Caarb)
Fix: Shiradi champion tree updated to match live. Tree version number increased as some enhancements changed. (Wiki updated)
Fix: Arcane Archer (Elf) Elemental Arrows I..IV text and effects updated (Reported by Khalibano)
Fix: Tabaxi Trailblazer Instinct and Improved Instinct now also apply to Quarterstaff as per the wiki
Fix: The "Spirit of the Beast" tooltip text will now display correctly (Reported by Khalibano)
Fix: Exalted Angel's T5 "Enhanced Meta: Intensify" description and effects updated (Reported by Khalibano)
Fix: The number of level 1 Druid spells available was increased by 1 (Reported by Khalibano)
Fix: Merfolk's Blessing is now correctly classed as a level 1 Druid spell (Reported by Khalibano)
Fix: Spell "Spike Growth" description, metamagics, MCL and effects updated (Reported by Khalibano)
Fix: Druid's will now pioritise spell craft on an auto skill point spend action
Fix: "Knock on the Sky" description updated in all 3 monk trees (Reported by Khalibano)
Fix: "Ninja Spy: Sting of the Ninja" description updated (Reported by Khalibano)
Fix: Epic (and Legendary) class options are no longer shown in the class and feats class selection drop menus as they are not selectable
Fix: Bad files which reference an Invalid tier 5 tree for class/destiny trees will now clear he bad data on load
Fix: Erroneous Tier5 lock outs in old files will now be cleared on load if the tree referenced no longer exists (Reported by Howiedoohan)

U54.1 Changes:
---Tabaxi "Sharp Claws" is now shown with an up arrow and is also a requirement for "Surprise Claws" (Wiki updated)
---Tabaxi Enhancement locations now match live
---Tabaxi "Feline Versatility" now has its correct main name

U55 Lamannia Preview support
---The maximum level is now 32
---Legendary levels are added after class(20) and Epic(10)
---Existing files will now correctly add Epic/Legendary levels as required on load
---Epic Destinies now have their Core4 (level 32) options
---8 More destiny APs are now available
---New Level 31+ Feats
------Legendary Power (Auto assigned)
------Legendary Knowledge (Auto assigned)
------Enhanced Elemental Dice (Epic Destiny)
------Legendary Point Blank Shot (Epic Destiny)
------Legendary Toughness (Epic Destiny)
------Shield Mastery Specialty (Epic Destiny)
------Single Weapon Specialty (Epic Destiny)
------Spell Specialty: Abjuration (Epic Destiny)
------Spell Specialty: Conjuration (Epic Destiny)
------Spell Specialty: Enchantment (Epic Destiny)
------Spell Specialty: Evocation (Epic Destiny)
------Spell Specialty: Illusion (Epic Destiny)
------Spell Specialty: Necromancy (Epic Destiny)
------Spell Specialty: Transmutation (Epic Destiny)
------Two Handed Specialty (Epic Destiny)
------Two Weapon Specialty (Epic Destiny)
------Wild Force (Epic Destiny)
---The main view now allows ability selection for level 32/36/40. 36/40 will be disabled until level cap increases.

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[e88f63cd33...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/e88f63cd33d7e9bd0322ddb33de4cd6a5fb15fa7)
#### Thursday 2022-05-12 21:41:32 by silicons

refactors some gun things (#4036)

* wow

* wack

* fix

* fix

* fuck you

* i am declaring war on gun devs

* fix

* fix

Co-authored-by: fake_vm_user <fake_vm_user>

---
## [donkras/fivem](https://github.com/donkras/fivem)@[02df4a52b1...](https://github.com/donkras/fivem/commit/02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9)
#### Thursday 2022-05-12 22:44:30 by blattersturm

tweak(client/core): nvidia, fuck you.

Apparently ba693365d151cb3d61e1fd1bc08f9f65f66d13ae wasn't enough to fix
the .toc corruption from nvPSShaderDiskCache.cpp/the NvShaderDiskCache
perf strategy.

Instead, this change just disables the shader cache entirely. Using a
hacky way.

---
## [donkras/fivem](https://github.com/donkras/fivem)@[6051b8790c...](https://github.com/donkras/fivem/commit/6051b8790c185b2435da75c2f41f59ec3be4578f)
#### Thursday 2022-05-12 22:44:30 by blattersturm

Revert "tweak(client/core): nvidia, fuck you."

The gift that keeps on giving: NVIDIA drivers. Some users seem to crash
in new places with `disable.txt` present and used.

Seriously?!

This reverts commit 02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9.

---
## [shobbs528/FinalProject_a3](https://github.com/shobbs528/FinalProject_a3)@[95bda50e70...](https://github.com/shobbs528/FinalProject_a3/commit/95bda50e70e6f127a320743f05666adca4861bcc)
#### Thursday 2022-05-12 23:37:44 by Samwich422

omg fucking god something went right

kay, the headlights are good now.

---
## [hannahrajarao/natural-language-processing](https://github.com/hannahrajarao/natural-language-processing)@[1835bcae56...](https://github.com/hannahrajarao/natural-language-processing/commit/1835bcae560610f7baf92f9e1b1f4604013602b4)
#### Thursday 2022-05-12 23:48:56 by Hannah Rajarao

Update phineasandferbtranscripts.txt

Episodes included:
Season 1:
A Hard Day's Knight/Transcript
Are You My Mummy?/Transcript
Bowl-R-Ama Drama/Transcript
Boyfriend From 27,000 B.C./Transcript
Candace Loses Her Head/Transcript
Comet Kermillian/Transcript
Crack That Whip/Transcript
Does This Duckbill Make Me Look Fat?/Transcript
Dude, We're Getting the Band Back Together/Transcript
Flop Starz
Get That Bigfoot Outa My Face!/Transcript
Got Game?/Transcript
Greece Lightning/Transcript

---

