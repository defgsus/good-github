## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-24](docs/good-messages/2022/2022-05-24.md)


1,654,147 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,654,147 were push events containing 2,699,534 commit messages that amount to 204,169,252 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[dbd9aa9c10...](https://github.com/willior/Action_RPG_1/commit/dbd9aa9c10b30b4ea96aaedf886529e2f5051f35)
#### Tuesday 2022-05-24 00:20:11 by willior

slime division / enemy death fixes

hitting a slime causes it to split. the newly created slime's max_health is set to that of the hit slime's after hit damage. also, the experience pools of both hit and newly created slimes get halved, meaning 1 "base" slime will give the same amount of experience as if it multiplied many times. eg. if the exp pool is 5000, killing the root slime with one hit rewards 5k. if it splits once before you can dispatch all of them, each reward 2.5k. etc. experience is an integer value so i'm not sure if it gets rounded up or not, but at that point the numbers are inconsequentially small.
next is a bigger fix, enemy death state. enemies were not getting set to there death state on no_health(); or rather, they would break out of their death state before getting deleted. this is why it appeared as though some enemies looked like they were starting an attack right before they exploded.
i think this mainly had to do with the way hit_stun is called, in that it was still called on a killing blow, so the hit_stun timeout would re-enable some behaviour that'd been disabled by the death... confusing spaghetti code shit. now, we check if state != DEATH before running hit_stun. we also stop all enemy timers when the no_health signal is emitted. sometimes we manually disable the animationTree and stop animation/play a death animation.
a lot of other minor adjustments which i won't list here cause i'm done.

---
## [z3DD3r/android_kernel_lge_hammerhead](https://github.com/z3DD3r/android_kernel_lge_hammerhead)@[b80545da3e...](https://github.com/z3DD3r/android_kernel_lge_hammerhead/commit/b80545da3e5824ee520e3a9c6d921c17564155a7)
#### Tuesday 2022-05-24 00:32:50 by z3DD3r

msm_thermal: simplified thermal driver

Thermal driver by franco.
This is a combination of 9 commits:

msm: thermal: add my simplified thermal driver.
Stock thermal-engine-hh goes crazy too soon and too often and offers no way for userland to tweak its parameters

Signed-off-by: franciscofranco <franciscofranco.1990@gmail.com>

msm: thermal: moar magic

Added a sample time between heat levels. The hotter it is, the longer
it should stay throttled in that same freq level therefore cooling this
down effectively.
Also due to this change freqs have been slightly adjusted.
Now the driver will start a bit earlier on boot.
Few cosmetic changes too because why the fuck not.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: reduce throttle point to 60C

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: rework previous patches

The changes on previous patches didn't really work out. Either the device
just reboots for infinity during boot because if it reaches high temperatures
and fails to throttle down fast enough to mitigate it, or it usually just
crashes the device while benchmarking on Geekbench or Antutu again because
when there's a big ass temp spike this doesn't mitigate fast enough.

These changes are confirmed working after testing in all scenarios previously
described.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: work faster with more thrust

Last commit was not enough, it mitigated most of the issues, but some users
were still having weird shits because temperature wasn't going down as fast
as it should. So now queue it every fucking 100ms in a dedicated high prio
workqueue. It's my last stance!

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm: thermal: offline cpu2 and cpu3 if things get REALLY rough

Just for safe measure put cpu2 and cpu3 to sleep if the heat gets way bad.
Also the polling time gets back to default stock 250ms since the earlier 100ms
change was just a band-aid for a nastier bug that got fixed in the mean time.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

msm_thermal: send OFF/ONLINE uevent in hotplug cases

Send the correct uevent after setting a CPU core online or offline.
This allows ueventd to set correct SELinux labels for newly created
sysfs CPU device nodes.

Bug: 28887345
Change-Id: If31b8529b31de9544914e27514aca571039abb60
Signed-off-by: Siqi Lin <siqilin@google.com>
Signed-off-by: Thierry Strudel <tstrudel@google.com>
[Francisco: slightly adapted from Qcom's original patch to apply]
Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

Revert "msm_thermal: send OFF/ONLINE uevent in hotplug cases"

Crashes everything if during early early boot the device is hot
and starts to throttle. It's madness!

This reverts commit 80e38963f8080c3c9d26374693dd0f0a88f8060b.

msm: thermal: return to original simplified driver

Some users still had a weird issue that I was unable to reproduce which
either consisted in cpu2 and cpu3 getting stuck in offline mode or after
a gaming session while charging the device would crash with "hw_reset"
and then the device would loop in bootloader -> boot animation forever
until the device cooled down.

My test was leaving the device charging during the night, brightness close
to max and running Stability Test app with the CPU+GPU suite. I woke up
and the device was still running it flawlessly. Rebooted while hot and it
booted just fine.

Since I was unable to reproduce the issue and @osm0sis flashed back to <r92
and was unable to reproduce it anymore here we go back to that stage.

Only change I made compared to that original driver was simply queue things
into a dedicated high prio wq for faster thermal mitigation. Rest is unchanged.

Signed-off-by: Francisco Franco <franciscofranco.1990@gmail.com>

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[20e4add487...](https://github.com/Tastyfish/-tg-station/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Tuesday 2022-05-24 00:34:09 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [ShayPunter/personal-site](https://github.com/ShayPunter/personal-site)@[d08613e6e8...](https://github.com/ShayPunter/personal-site/commit/d08613e6e8b9c82ab9c3ceb4c967e8818b8d0d79)
#### Tuesday 2022-05-24 00:55:15 by Shay Punter

Its 2am, I am done for the night, shit still doesn't work because of some stupid cant strigify function which didn't exist anymore, pls just work

---
## [Bm0n/Paradise](https://github.com/Bm0n/Paradise)@[ab7a358506...](https://github.com/Bm0n/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Tuesday 2022-05-24 01:00:04 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [HonoreDB/cockroach](https://github.com/HonoreDB/cockroach)@[25491bef8b...](https://github.com/HonoreDB/cockroach/commit/25491bef8b9b670e30f92bbbf8d1172989e57c90)
#### Tuesday 2022-05-24 01:02:32 by Aaron Zinger

sql: implement array functions for JSON arrays

My answer on
https://stackoverflow.com/questions/72347170/delete-element-from-jsonb-array-in-cockaroachdb/72351955#72351955
made me sad, and it's not the first time I've had trouble
manipulating a JSONB array.

There are a few different, non-mutually-exclusive ways we
could make this easier. We could allow aggregate(generator) functions
in scalar contexts. We could implement more JSON functions as needed.

This PR instead just overloads every function that takes a json[]
 argument (which is a datum type we don't allow in columns) to also
be able to take a json array argument, and alters the return type
accordingly. It's not particularly performance-optimized but we can
replace individual implementations if needed.

That said, this is an unauthorized spike, what do you think?

Release note (sql change): Built-in array functions array_append, array_prepend, array_cat, array_remove, array_replace, array_position, and array_positions may now be used with jsonb arrays.

---
## [TheRealScarHomie/mojave-sun-13](https://github.com/TheRealScarHomie/mojave-sun-13)@[8cbd42cf37...](https://github.com/TheRealScarHomie/mojave-sun-13/commit/8cbd42cf374bcb59ce9676d8b5c8dfc949523848)
#### Tuesday 2022-05-24 01:45:32 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

(cherry picked from commit d005d76f0bd201060b6ee515678a4b6950d9f0eb)

# Conflicts:
#	.github/CODEOWNERS
#	code/game/objects/items/devices/radio/radio.dm

---
## [Sunflair0/cash-grab](https://github.com/Sunflair0/cash-grab)@[caccf2c96f...](https://github.com/Sunflair0/cash-grab/commit/caccf2c96fe9dbbe74ead5f1cd9fb4ea9fb0919f)
#### Tuesday 2022-05-24 05:29:45 by Sunflair0

Create README.md

This is my take on a group assignment while attending Midlands Code Camp. We were instructed to create a whack-a-mole game. But, smacking all those moles made me sad, so I made my own verson where you are penalized for hitting those adorable buggers.
I added levels (I am very proud of the buttons), 4 lives, changed the graphics, added the cash and mole pop up options, the preview and action bar on the bottom, the scoreboard at the end; really, I changed everything except the mole pop ups.
I worked on this a long time because by the time I finished one module, I learned how to do another better and I re-did that. I got very familiar with Greensock and animations, used 3D Paint and Canva (for SVG conversion). In the end, I figured since I am a junior developer, it's ok to have the program a bit messy, because I am still learning. It also proves I wrote it myself!
I am aware that Lighthouse testing rates my speed low, and I am sorry. If you have suggestions for me, I am WIDE OPEN to constructive critism! Help me be a better coder.
I do hope you enjoy playing the game. Try it on all hardness levels, use up all the hearts and restart the game. My only regret is that I don't have a cute animation at the end when you pass the game. 
But, I may have one in the future! Stay tuned.

---
## [WheeledParasite/MovementSlasher](https://github.com/WheeledParasite/MovementSlasher)@[8f3095fbd7...](https://github.com/WheeledParasite/MovementSlasher/commit/8f3095fbd7c18e7d0d18237536f15d8cbf2636e0)
#### Tuesday 2022-05-24 08:05:21 by Mark Carson

Initial commit

Refactored code, renamed things, spread things apart, and fucked shit up. Enjoy!

Note: jumping and most movement functions are in a broken state

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2667ee35f5...](https://github.com/treckstar/yolo-octo-hipster/commit/2667ee35f5eb402e3225344ad396c92765369f8b)
#### Tuesday 2022-05-24 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [prymakD/CodeWars](https://github.com/prymakD/CodeWars)@[4b404e8e2b...](https://github.com/prymakD/CodeWars/commit/4b404e8e2b30fe18b37c7a07670a8806a1834d4a)
#### Tuesday 2022-05-24 08:57:29 by Danila

Vladimir has white skin, very long teeth and is 600 years old, but this
 is no problem because Vladimir
is a vampire.
Vladimir has never had any problems with being a vampire. In fact, he
is a very successful doctor
who always takes the night shift and so has made many friends among his
colleagues. He has a very
impressive trick which he shows at dinner partys: He can tell tell blood
 group by taste. Vladimir loves
to travel, but being a vampire he has to overcome three problems.
• First, he can only travel by train because he has to take his coffin
with him. (On the up side he
can always travel first class because he has invested a lot of money in
long term stocks.)
• Second, he can only travel from dusk till dawn, namely from 6 pm to
6 am. During the day he
has to stay inside a train station.
• Third, he has to take something to eat with him. He needs one litre
of blood per day, which he
drinks at noon (12:00) inside his coffin.
You should help Vladimir to find the shortest route between two given
cities, so that he can travel
with the minimum amount of blood. (If he takes too much with him, people
 will ask funny questions
like ”What do you do with all that blood?”)


Input
The first line of the input will contain a single number telling you the
 number of test cases.
Each test case specification begins with a single number telling you how
 many route specifications
follow.
Each route specification consists of the names of two cities, the
departure time from city one and
the total travelling time. The times are in hours. Note that Vladimir
can’t use routes departing earlier
than 18:00 or arriving later than 6:00.
There will be at most 100 cities and less than 1000 connections.
No route takes less than one hour
and more than 24 hours. (Note that Vladimir can use only routes with a
maximum of 12 hours travel
time (from dusk till dawn).) All city names are shorter than
32 characters.
The last line contains two city names. The first is Vladimir’s start
city, the second is Vladimir’s
destination.

Output
For each test case you should output the number of the test case
followed by ‘Vladimir needs #
litre(s) of blood.’ or ‘There is no route Vladimir can take.’

Sample Input
2
3
Ulm Muenchen 17 2
Ulm Muenchen 19 12
Ulm Muenchen 5 2
Ulm Muenchen
10
Lugoj Sibiu 12 6
Lugoj Sibiu 18 6
Lugoj Sibiu 24 5
Lugoj Medias 22 8
Lugoj Medias 18 8
Lugoj Reghin 17 4
Sibiu Reghin 19 9
Sibiu Medias 20 3
Reghin Medias 20 4
Reghin Bacau 24 6
Lugoj Bacau
Sample Output
Test Case 1.
There is no route Vladimir can take.
Test Case 2.
Vladimir needs 2 litre(s) of blood.

---
## [erikgrinaker/cockroach](https://github.com/erikgrinaker/cockroach)@[88b245aa46...](https://github.com/erikgrinaker/cockroach/commit/88b245aa469ee6302a25d3ac4cbe58b23927831d)
#### Tuesday 2022-05-24 09:20:20 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

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
## [mar3an/L2Private_DataPack](https://github.com/mar3an/L2Private_DataPack)@[3f7b6a5a3d...](https://github.com/mar3an/L2Private_DataPack/commit/3f7b6a5a3d7118b83531cb46864e022e67236a12)
#### Tuesday 2022-05-24 09:24:57 by mar3an

# Fix Dimensional Merchants Part I

- Part I: Dimensional Merchants
(Dimensional Merchants are now functional.)

- Part II: Lucky Pig
(Lucky Pig are not implemented yet.)

 - Dimensional Merchants is found in all cities, including starting villages

With it, you can get various pets and Gifts. To be the lucky owner, you must have a Hunting Helper Exchange Coupon or  High-Grade Hunting Helper Exchange Coupon , which can only be obtained through the Item Mall.
After receiving a coupon, you can exchange it for one of the pets.

Pets that can be obtained for coupons
 - Hunting Helper Exchange Coupon :
 - White Weasel (White Weasel)
 - Fairy Princess (Fairy Princess)
 - Wild Beast Fighter (Wild Beast Fighter)
 - Fox Shaman (Fox Shaman)

High Grade Hunting Helper Exchange Coupon :
 - Toy Knight
 - Spirit Shaman (Magic Spirit)
 - Owl (Owl)
 - Turtle Ascetic

---
## [EtraIV/MerchantStation13](https://github.com/EtraIV/MerchantStation13)@[f51ff8cdbd...](https://github.com/EtraIV/MerchantStation13/commit/f51ff8cdbd744bf998ea669bab7e523eb023baa9)
#### Tuesday 2022-05-24 09:58:34 by hamurlik

Adds simpson skintone (#138)

* Adds simpson skintone

The sign is a subtle joke. The shop is called "Sneed's Feed & Seed", where feed and seed both end in the sound "-eed", thus rhyming with the name of the owner, Sneed. The sign says that the shop was "Formerly Chuck's", implying that the two words beginning with "F" and "S" would have ended with "-uck", rhyming with "Chuck". So, when Chuck owned the shop, it would have been called "Chuck's Fuck and Suck".

Co-authored-by: EtraIV <34369281+EtraIV@users.noreply.github.com>

---
## [kmarulab/codeforces](https://github.com/kmarulab/codeforces)@[3ecb3499f3...](https://github.com/kmarulab/codeforces/commit/3ecb3499f38426051d1326dea2801cf5fa334bbb)
#### Tuesday 2022-05-24 10:08:05 by kkmaru

README.md

Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.
Input

The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.
Output

If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

---
## [NBtheMC/The-Adventurers-Guild](https://github.com/NBtheMC/The-Adventurers-Guild)@[f58a8a51c3...](https://github.com/NBtheMC/The-Adventurers-Guild/commit/f58a8a51c38002614e8e817ba084cb52cd320d63)
#### Tuesday 2022-05-24 10:32:47 by Eric Long

finished quest system.

oh god. oh holy fuck. i want to fucking die.

---
## [mjg/git](https://github.com/mjg/git)@[bdaf1dfae7...](https://github.com/mjg/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Tuesday 2022-05-24 11:50:56 by Tao Klerks

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
## [RobertHarnett/AuthenticatorPro](https://github.com/RobertHarnett/AuthenticatorPro)@[fd5737fd9b...](https://github.com/RobertHarnett/AuthenticatorPro/commit/fd5737fd9b55b9e36f6e423d5d26bf880afe0ed6)
#### Tuesday 2022-05-24 12:25:54 by Robert Harnett

56 New Icons + Complete Update of Existing Icons

# Authenticator Pro Pull Request Changelog

## TL;DR:
- Added 56 New Icons
- Updated any out of date icons (eg; Adobe).
- Remade some icons that looked low quality (eg: onshape), I admit I don't know how noticeable this is when scaled down but it allows for greater flexibility in the future if you ever decide to alter icon scaling.)
- Remade ones that were scaled incorrectly  to the 128x128 size (eg patreon).
- Note there's a fair few where they look nearly identical to existing icons, on some, the logo's have changed a tiny little bit such as a small colour change, on others they are essentially identical. At the stage where I was comparing any of the existing icons to remade icons I had done, I had basically done the hard part already and would only need to save as png, so If I remade one and it turned out to be the same I decided to still export and replace the existing icon because it looked like there was no Anti-Aliasing on the existing icons. 'onshape.png' is the clearest example of this.
- Deleted icons that are no longer needed, such as unnecessary dark mode versions, icons of services that don't exist, 'Version2' of any icons as these feel redundant, and icons of services that use a account under a different name eg: 'Yandex mail' falls under 'Yandex'.
- Updated missing_icons.txt

### Any feedback or issues please let me know, Im aware this is a large change so I don't expect it to be 100% perfect.

## Full Changelog:

### New Icons:
- Addiko Bank
- Advcash (+ Dark Mode)
- Automate.io
- Avanza
- Betfair
- BigMind
- Bitgo
- Brightbox
- Cake defi
- Call of Duty (+ Dark Mode)
- Cisco
- Clearscore (+ Dark Mode)
- Clubhouse (+ Dark Mode)
- Community America
- Crashplan
- Datto
- Degiro
- Ecobee[^Ecobee]
- Fastly
- Files.com
- Gaijin
- Google Cloud
- Hey
- Hodlenaut
- IBM
- ID.me
- idrive.com
- Intuit[^Intuit]
- Ionos
- Jovia
- Koofr
- Luno (+ Dark Mode)
- MacStadium (+ Dark Mode)
- Make
- Mercury (+ Dark Mode)
- Meta
- Morgan Stanley (+ Dark Mode) (Easily the most boring logo I've ever seen, not much I could do here)
- Nordlayer
- Nutstore
- Onehub
- Optimizely
- Oracle
- Pusher (+ Dark Mode)
- Rewind
- Runescape (+ Dark Mode)
- SEFCU
- Sony (+ Dark Mode)
- Standard Notes
- Strato
- Sync
- Trading 212
- Ubuntu One
- VMware
- VR Chat
- Whois
- Xero

### Updated Icons:
- 1and1
- 1password
- 3cx (Slightly darker grey)
- Adobe
- Airship
- Allegro
- Altaro
- Amazon
- Appveyor
- Arduino
- Asana
- Ascendex
- Atlassian
- Autodesk (+ Dark Mode)
- AWS (+ Dark Mode)
- Azure
- Basecamp
- Best Buy
- Binance
- Bitcoin
- Bitdefender
- Bitfinex
- Bitflyer
- Bitstamp (+ Dark Mode)
- Bittrex
- Blizzard
- Blockchain
- Bluehost
- Box
- Buildkite
- BunnyCDN
- Codeberg (+ Dark Mode)
- Codeship (+ Dark Mode)
- Coinjar (+ Dark Mode)
- Confluence
- Contabo
- Control D (+ Dark Mode)
- Crypto.com (+ Dark Mode)
- Dashlane (+ Dark Mode)
- Deutschebahn
- Direct Admin
- Discogs (+ Dark Mode)
- Discord
- Docker
- Dreamhost
- Dropbox
- Electronic Arts
- Envato
- Evernote
- Facebook
- Figma
- Filen (+ Dark Mode)
- Floatplane
- fmfw
- FTX
- Gemini
- Gitlab
- Gmail
- GoDaddy
- Google
- Google Drive
- Google Fi
- Google Fibre
- Google Pay
- Google Play
- Grammarly
- Hellosign
- Heroku
- Hitbtc
- Home Assistant
- Hotbit
- Humble Bundle[^Humble Bundle]
- Huobi
- Instagram
- Intigriti[^Intigriti]
- InVision
- IP Phone Forum
- Itglue
- Jagex
- Jelastic
- Jetbrains (+ Dark Mode)
- Jira
- Jottacloud
- Kaspersky
- Kraken
- Leaseweb
- Linkedin
- Linode
- Litebit
- Local Cryptos
- Local Monero
- Login.gov
- Maicoin
- Mailbox.org
- Mailchimp (+ Dark Mode)
- Mail.com
- Mailfence
- Mailgun
- Mailo
- Mapbox (+ Dark Mode)
- Mastodon
- Matomo
- Mega
- Microsoft
- Microsoft Todo
- Migros
- Mintos
- Monday.com
- Moneyforward
- Moneytree
- Moqups
- Myheritage
- Namecheap
- Name.com (+ Dark Mode)
- Netcup
- Nintendo[^Nintendo]
- Nuget
- Nulab
- NURI
- Onedrive
- Onshape
- Origin
- Outlook
- ovh
- Parsec
- Patreon
- Paykassa
- Paypal
- Paysafecard
- Plex
- Plurk
- Poloniex_Dark
- Private Internet Access
- Proxmox_dark
- Pushover
- Pypi
- Qnap
- Rackspace
- RealVNC
- Robinhood
- Roblox (+ Dark Mode)
- Roboform
- RocketbeansTV
- Salesforce
- Samsung[^Samsung]
- Scaleway
- Shortio
- Simplelogin
- Skype
- Slack
- Snapchat
- Socketlabs
- Solarwinds
- Sproutsocial
- Square
- Squarespace
- Stackpath (+ Dark Mode)
- Statuspage
- Steam (+ Dark Mode)
- Stormgain
- Surfshark
- Synology
- Team Viewer
- Telnyx
- Ting
- T-Mobile
- Tokopedia
- Tor Guard (+ Dark Mode)
- Trello
- Tresorit
- Tutanota
- Twilio
- Twitch
- Twitter
- Ultimaker
- United Domains
- Unlock Base
- Unstoppable Domains
- Updraft
- UpTimeRobot
- Visual Studio Online
- VK
- Voyager
- Vultr
- War Gaming
- Web.de
- Whale Fin
- wordfence
- Wyze (Again... Updated colour and text weight)
- ynab
- YoYo Games
- Zoho
- Zonda (+ Dark Mode)
- Zoom
- Zyxel (+ Dark)

### Deleted Icons:
Some of these have dark mode versions that are either not necessary because they are already legible in both light and dark mode or because they have an updated icon where this is now the case (I previewed them in my icon designer software with the same background colours used in the app to make sure they are clear to see).
- 34sp (Dark Mode)
- Adobe (Dark Mode)
- BasicAttentionToken is a crypto currency by Brave, it's not a service on its own and does not require a icon.
- Best Buy (Dark Mode)
- Box (Dark Mode)
- Crypton I can't find this service anywhere? Even reverse image searched the current icon and it seems it doesn't exist?
- Electronic Arts (Dark Mode)
- Google Cloud Platform (Now called 'Google Cloud')
- Google Pay (Dark Mode)
- Gildwars2 Uses Arenanet to login which already has a account.
- Hangouts (The service no longer exists)
- Integromat has rebranded into 'Make' have added a new icon for it.
- Integrity was misnamed, has simply been named 'Intigriti', icon still exists.
- Jetbrains2 (Removed the logo with the coloured line as it makes the logo really small, using just the square on its own is still within the brand guidelines.
- Patreon (Dark Mode)
- Netcup (Dark Mode)
- Oculus now exists under the 'Meta' name. I have deleted the old logo and created one for Meta.
- Office365 has rebranded as Microsoft365, I still wanted to keep a icon for office for user choice so have updated the icon and named it simply 'Office'
- Samsung[^Samsung]
- 'simpletax.co' looks 100% like a scam or very old proprietary software that almost no one uses. There's several hundred other services I would prefer we make an icon for first rather then this sketchy looking site. What caused this icon to be added? Was it a legitimate user request? I decided to remove it because I question it's legitimacy, while you could argue that's not for the job of someone submitting icons, I really hate this icon and don't want the icon selector to be clogged full of spammy random sites.
- Smashcast no longer exists.
- Starling Bank Developer (Renamed file to simply 'starlingbank')
- Statusmail (Is this an actual service, it seems to just be part of 'statuspage' which already has an icon.
- Synology (Dark Mode)
- Uplay, it's rebranded to 'Ubisoft Connect' and uses a ubisoft account which already has an icon.
- Yandex Mail (Uses a Yandex account which can be for multiple services, I have added a icon for 'Yandex'

### Updated 'missing_icons.txt':
- Removed names of added icons
- 'NordVPN Teams' has rebranded as Nord Layer, icon added.
- 'Bugzilla@Mozilla' uses the 'Mozilla' logo which already exists.
- 'Hover.com' is already added.
- TurboTax, Quickbooks, & Mint all use a shared 'Intuit' account
- removed 'Ukraine' because... well idk what it is other then a country, and I don't think an entire country has 2FA. Well I suppose it probably in a way does have two factor authentication to enter it right now but that's a differant thing entirely.
- Removed 'Samsung Smartthings' as far as im aware it uses a Samsung account.
- 'Remote Desktop Manager' & 'Online' could be any number of services, Im removing them as I don't actually know what the services are.
- 'Launchpad' uses Ubuntu One login, icon added.
- join.me uses 'LogMeIn' which already has an icon.

[^Ecobee]: Ecobee's Logo is rather thin text so this icon is based off of their app icon to improve legibility, funnily enough they seem to realise this problem themselves as they use the same solution for their favicon on their website.

[^Intigriti]: Previously misnamed as 'Integrity', not deleted, just renamed.

[^Intuit]: Their logo is just text which is hard to see so again I've based this icon off of their favicon.

[^Humble Bundle]: Both the old 'H' icon and the bag icon are within official brand guidelines and can both be used, I decided to change to the bag to reduce the use of typography in the icon set, this is a personal preference so let me know if you prefer to use the 'H'.

[^Nintendo]: Even on my Pixel 6 Pro which is both on the higher end of screen size and device PPI the current Nintendo logo is very small and hard to read, here I copied what Nintendo have done on their own website it regards to their favicon. This is again a personal preference to reduce the dependence on type heavy icons. Let me know if I should revert this change.

[^Samsung]: Samsung no longer use the rounded blue logo, so I have deleted it and made the 'samsung2' icon the primary and only Samsung logo.

---
## [rokonec/msbuild](https://github.com/rokonec/msbuild)@[a572dc6b79...](https://github.com/rokonec/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Tuesday 2022-05-24 12:26:36 by Forgind

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
## [robertlangenberg/acts](https://github.com/robertlangenberg/acts)@[6e1fd31474...](https://github.com/robertlangenberg/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Tuesday 2022-05-24 13:00:59 by Stephen Nicholas Swatman

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
## [arielvalentin/opentelemetry-ruby](https://github.com/arielvalentin/opentelemetry-ruby)@[45429c7d53...](https://github.com/arielvalentin/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Tuesday 2022-05-24 13:41:13 by Andrew Hayworth

Split CI builds by gems at top-level (#1249)

* fix: remove unneeded Appraisals for opentelemetry-registry

It's not actually doing anything, so we skip it.

* ci: remove ci-without-services.yml

We're going to bring back these jobs in the next few commits, but we can delete it right now.

* ci: remove toys/ci.rb

We're going to replicate this in Actions natively, so that we can get
more comprehensible build output.

* ci: replace toys.rb functionality with an explosion of actions + yaml

This replaces the "test it all in a loop" approach that `toys/ci.rb` was
taking, by leveraging some more advanced features of GitHub Actions.

To start, we construct a custom Action (not a workflow!) that can run
all the tests we were doing with `toys/ci.rb`. It takes a few different
inputs: gem to test, ruby version to use, whether or not to do rubocop,
etc. Then, it figures out where in the repo that gem lives, sets up ruby
(including appraisals setup, if necessary), and runs rake tests (and
then conditionally runs YARD, rubocop, etc).

Then, over in `ci.yml`, we list out all of the gems we currently have
and chunk them up into different logical groups:

- base (api, sdk, etc)
- exporters
- propagators
- instrumentation that requires sidecar services to test
- instrumentaiton that doesn't require anything special to test

For most groups, we set up a matrix build of operating systems (ubuntu,
macos, and windows) - except for the "instrumentation_with_services"
group, because sidecar services are only supported on linux.

For each matrix group (gem + os), we then have a build that has multiple
steps - and each step calls the custom Action that we defined earlier,
passing appropriate inputs. Each step tests a different ruby version:
3.1, 3.0, 2.7, or jruby - and we conditionally skip the step based on
the operating system (we only run tests against ruby 3.1 for mac /
windows, because the runners are slower and we can't launch as many at
once).

Notably, we have a few matrix exclusions here: things that wont build on
macos or windows, but there aren't many.

Finally, each group also maintains a "skiplist" of sorts for jruby -
it's ugly, but some instrumentation just doesn't work for our Java
friends. So we have a step that tests whether or not we should build the
gem for jruby, and then the jruby step is skipped depending on the
answer. We can't really use a matrix exclusion here because we don't use
the ruby version in the matrix at all - otherwise we'd have a *huge*
explosion of jobs to complete, when in reality we can actually install +
test multiple ruby versions on a single runner, if we're careful.

The net effect of all of this is that we end up having many different
builds running in parallel, and if a given gem fails we can *easily* see
that and get right to the problem. Builds are slightly faster, too.

The major downsides are:
- We need to add new gems to the build list when we create them.
- We can't cache gems for appraisals, which adds a few minutes onto the
  build times (to be fair, we weren't caching anything before)
- It's just kinda unwieldy.
- I didn't improve anything around the actual release process yet.

Future improvements could be:
- Figuring out how to cache things with Appraisals, because I gave up
  after a whole morning of fighting bundler.
- Dynamically generating things again, because it's annoying to add gems
  to the build matrices.

* feat: add scary warning to instrumentation_generator re: CI workflows

* fix: remove testing change

* ci: Add note about instrumentation_with_services

---
## [sAmenta/CodePlayground](https://github.com/sAmenta/CodePlayground)@[8ceda39d98...](https://github.com/sAmenta/CodePlayground/commit/8ceda39d9820c61aeb087420b4b006c479107802)
#### Tuesday 2022-05-24 15:07:53 by sAmenta

Sir Backsword met two men on the road. They asked to be his companions. They said that both of them had the same profession.
He decided to find out what they were: knights, merchants, or robbers.

Write a program that will help him decide if he can trust the strangers.
To answer this question, you need to read three booleans: firstAnswer, secondAnswer, and confession (each on a separate line):

firstAnswer and secondAnswer are what the two strangers themselves say about their profession.
We assume that no one will ever say that robbery is their profession, so true here means knight and false means merchant.
confession will be true only if they confess in good faith that they are robbers.
The strangers can't be trusted if their answers don't match or if they confess that they are robbers.
In this case, print false; otherwise, print true.

---
## [pity4yeats/linux](https://github.com/pity4yeats/linux)@[b041b525da...](https://github.com/pity4yeats/linux/commit/b041b525dab95352fbd666b14dc73ab898df465f)
#### Tuesday 2022-05-24 15:32:25 by Tony Luck

x86/split_lock: Make life miserable for split lockers

In https://lore.kernel.org/all/87y22uujkm.ffs@tglx/ Thomas
said:

  Its's simply wishful thinking that stuff gets fixed because of a
  WARN_ONCE(). This has never worked. The only thing which works is to
  make stuff fail hard or slow it down in a way which makes it annoying
  enough to users to complain.

He was talking about WBINVD. But it made me think about how we use the
split lock detection feature in Linux.

Existing code has three options for applications:

 1) Don't enable split lock detection (allow arbitrary split locks)
 2) Warn once when a process uses split lock, but let the process
    keep running with split lock detection disabled
 3) Kill process that use split locks

Option 2 falls into the "wishful thinking" territory that Thomas warns does
nothing. But option 3 might not be viable in a situation with legacy
applications that need to run.

Hence make option 2 much stricter to "slow it down in a way which makes
it annoying".

Primary reason for this change is to provide better quality of service to
the rest of the applications running on the system. Internal testing shows
that even with many processes splitting locks, performance for the rest of
the system is much more responsive.

The new "warn" mode operates like this.  When an application tries to
execute a bus lock the #AC handler.

 1) Delays (interruptibly) 10 ms before moving to next step.

 2) Blocks (interruptibly) until it can get the semaphore
	If interrupted, just return. Assume the signal will either
	kill the task, or direct execution away from the instruction
	that is trying to get the bus lock.
 3) Disables split lock detection for the current core
 4) Schedules a work queue to re-enable split lock detect in 2 jiffies
 5) Returns

The work queue that re-enables split lock detection also releases the
semaphore.

There is a corner case where a CPU may be taken offline while split lock
detection is disabled. A CPU hotplug handler handles this case.

Old behaviour was to only print the split lock warning on the first
occurrence of a split lock from a task. Preserve that by adding a flag to
the task structure that suppresses subsequent split lock messages from that
task.

Signed-off-by: Tony Luck <tony.luck@intel.com>
Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
Link: https://lore.kernel.org/r/20220310204854.31752-2-tony.luck@intel.com

---
## [Proxtx/material](https://github.com/Proxtx/material)@[ed6937a3b1...](https://github.com/Proxtx/material/commit/ed6937a3b1cff4c49e2f2a4c6273b3cb6b6d9f10)
#### Tuesday 2022-05-24 15:39:52 by Proxtx

heilige mutter jesus marie DANKE DANKE ahhh es geht endlich. Chrome ist ein arschloch. FUCK YOU CHROME. CHROME IS BUGGY AAHHHHHHHHHHHHHH

---
## [MrDoomBringer/tgstation](https://github.com/MrDoomBringer/tgstation)@[a137c15a79...](https://github.com/MrDoomBringer/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Tuesday 2022-05-24 15:50:09 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [transcom/mymove](https://github.com/transcom/mymove)@[8af1f5a031...](https://github.com/transcom/mymove/commit/8af1f5a03143dce4ab3c6aa01b8772cd2f41adb9)
#### Tuesday 2022-05-24 16:28:19 by Marty Boren

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
## [chapel-lang/chapel](https://github.com/chapel-lang/chapel)@[bf1082871e...](https://github.com/chapel-lang/chapel/commit/bf1082871e365ebaebf0057c1793ebcae9e963e7)
#### Tuesday 2022-05-24 17:18:17 by Andy Stone

Merge pull request #19851 from stonea/llvm_check_for_lclang_cpp

Add check to see if libclang-cpp-dev package is installed and ensure missing package errors get to user

I'm trying to install llvm 13 on my desktop to use it as the "system" LLVM when CHPL_LLVM=system.  Anyway, I must have forgotten to install a package because when I build Chapel I get this error:
`/usr/bin/ld: cannot find -lclang-cpp`

I figured out the missing package was: libclang-cpp-dev (after apt-getting it things work fine).
It's a better user experience if we can get printchplenv to guide the user towards installing the necessary packages. I see in chplenv/chpl_llvm.py (in the check_llvm_config function) we have some checking that looks for things like missing include files (due to missing packages) and produces some nice error messages. Unfortunately, these error messages never reach the user, rather you'll get this more confusing error:

`Exception: CHPL_LLVM=system but could not find an installed LLVM with one of the supported versions: 14, 13, 12, 11`

You can reproduce this by running sudo apt remove libclang-dev and running printchplenv. I think this is due to a bug where we produce the error message (and add it to some error log) but never actually report it to the user.

In this PR I fix this so we separate out the check for the presence of llvm_config from the other checks about include files (and now libs) and ensure that we run these checks when we're using the system LLVM.
I also add in the check for missing -lclang_cpp, you'll now get this message if it can't find it:

`Perhaps you need to install the libclang-cpp-dev package`

[Reviewed by @daviditen]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[55e9ba6f86...](https://github.com/mrakgr/The-Spiral-Language/commit/55e9ba6f8687a9cd7f979083dda6e5a15917ed1e)
#### Tuesday 2022-05-24 18:52:40 by Marko Grdinić

"It is really great that Fable translations are continuing. The manga is really good.

1:45pm. https://mangadex.org/chapter/1b00b4e9-6d32-4618-a0d2-e81d2fb45da9/1

The creases on the sofa are pretty nice here.

2:10pm. https://mangadex.org/chapter/7343c060-5664-4816-8069-571a139a69f4/1

Let me stop here, this was really fun. I need to get into the zone for my current task.

https://youtu.be/HiGYx_DADOQ
Render Nodes (BlenderMalt 1.0 preview)

https://youtu.be/HiGYx_DADOQ?t=298

This is decently advanced. It might be worth looking into, but this video is not much of a tutorial.

2:35pm. > To be honest, I'm still a bit confused about the advantage of Malt over the usual Eevee NPR methods (e.g., inverted hull, Freestyle, ShaderToRGB, etc.)
> Malt isn't as limited as Eevee, but it requires you to have knowledge of GLSL programming langauge. It takes time to learn Malt but its more versatile than Eevee in terms of non-photorealistic rendering.

2:50pm. https://youtu.be/tE99jgCCcNE
Malt Nodes Introduction (Updates in description)

Let me watch this.

2:55pm. https://youtu.be/X8YkWdhty7I
Blender Tutorial: 14 Non-photoreal Stylization Techniques (Advanced)

Let me watch this and then I am done with tutorials.

3:15pm. https://blenderartists.org/t/how-do-i-render-a-scene-where-most-of-the-lights-comes-from-grills/1381668/15

I got really good replies here.

3:30pm. Oh, the fast GI approximation is quite good. I thought that it might be a way, but when I tried clicking the setting yesterday I not get any result. It is not like I was paying careful attention to what things do. Let me watch a tutorial on it.

4:05pm. Decreasing the AO distance really does make the room a lot brighter. This is pretty good. But since I am on the warpath, I'll want to figure out the other stuff as well.

https://www.youtube.com/watch?v=X8YkWdhty7I
Blender Tutorial: 14 Non-photoreal Stylization Techniques (Advanced)

Let me finish this since I've started it.

4:20pm. Focus me, stop looking at that forum.

https://youtu.be/X8YkWdhty7I?t=227

I admit, I hadn't know that pixelization was so easy. I was wondering how they did that pixel art scene in Estab Life. It is really no trouble.

https://youtu.be/X8YkWdhty7I?t=537

Never heard about projected paint.

https://youtu.be/X8YkWdhty7I?t=655

Ah, I was wondering why Solidify had flipped normals. It is so it can be used as an inverted hull.

https://youtu.be/X8YkWdhty7I?t=769

So that is what window could be used for. Real time hatching.

https://youtu.be/X8YkWdhty7I?t=851

Style transfer with NNs.

4:45pm. https://www.youtube.com/watch?v=rXdeJ_sigf4

Illustration shader? What is that?

At any rate, the Creative Shrimp video on NPR methods was quite informative.

5pm. Ok, it is time to do my own stuff for a bit.

Ok, first off, let me try out Irradiance Maps in Eevee. After that my goal will be to get some good grill shadows on the walls. I'll pit Eevee vs Fast GI Cycles. Reality sure is amazing to be able to render all this so quickly. I really made a mistake in not making it my renderer of choice.

5:10pm. How BG show the irradiance volume points?

I can't find it. I know I saw it being done in some video.

https://youtu.be/fWtzzHB_HD4
EEVEE Blender 2.8 | Beginners Guide | Irradiance volume | Realistic renders

Let me watch this by Grant.

https://youtu.be/fWtzzHB_HD4?t=81

Ah, the outer box is not what I thought it would be.

5:20pm. It is really awkward that my room is not a cube. I guess I'll have to lower it so it does not go outside.

https://youtu.be/9SD0of-mOHo
Perfect Eevee bounce lighting with (and without) irradiance volume light probes in Blender

This had one the spheres.

...No, I misremembered. Nevermind this.

6pm. I realize now why being a lighting artist is a profession all on its own.

6:05pm. Ok, let me put a point light relatively close to the entryway.

6:20pm. https://youtu.be/XohMPGEofJU
Blender Addons for lighting

This is so damn hard. Just positioning the light and having it point where you want is hard with blender's default tools. Isn't there something to at least let me use it like a camera. This would be really good for sun, spot and area lights.

6:40pm. https://blender.stackexchange.com/questions/118568/is-there-a-way-to-drive-lamps-similar-to-how-you-can-drive-and-control-a-ca
> A quirk of Blender is that you can actually set any object to be the 'camera' and use the WASD movement controls while in Fly mode.

Wow, I never knew this.

6:45pm. https://engelik.gumroad.com/l/DQNYI
Blender Light Manager

Let me give this addon a try. It really is a pain in the ass to adjust lights the way I am doing it right now.

6:50pm. It works great. Being able to position the light in first person view and use buttons to duble and halve the intensity makes things a lot easier. Area light is not like what I thought it would be. It is actually a 180% cone. What its size does is regulate the softness of the shadows.

It seems Blender will crash if you add to many lights to the scene. Thankfully I had anticipated that and have been saving along the way.

7:15pm. Right now I am waiting for the irradiance volume to bake. It really takes up the whole rig. Reminds me of V-Ray renders.

7:40pm. It is no good. Should I try LuxCore?

7:45pm. Almost downloaded it. Let me watch the crash course on it.

https://youtu.be/66fLyb376x0
LuxCore Render For Blender Crash Course | Glass, Dispersion, Caustics and Light Tracing

Let me give this a try.

Irradiance maps are fairly nasty hacks. Fast GI gives me well lighted scenes, but the shadows are low quality and all the lights crashing into the grills make it pure white. Eevee can only get me so far. In actuality it is not that much better than solid view.

In actuality, my original plan of just slapping a HDRI was the soundest one. Because it failed I now find myself doing all kinds of dumb stuff.

Yeah, that is how people go crazy in life. The right thing fails, and you find yourself doing the wrong things in hopes that they work.

https://www.youtube.com/playlist?list=PLInnXO9jT2v_5n7PM8a6IBeTY8VjEahKZ

I thought this would be a single crash course. No way am I watching this. You know what? Forget it. I am going to try rendering in Luxcore tomorrow.

8pm. I should also give Malt a try. I know I am getting sidetracked at this point, but I am going to finish the 3d adventure very soon. After I am done with this it will be nothing, but modeling and drawing for me.

Let me make post in the /wip/ thread.

///

>>899198
It really very hard to get the lighting the way I want it to. Reality really beat Cycles as a renderer. I only got it to work in a reasonable amount of time with Cycles by turning on the Fast GI Approximation. But is not even close to being good. I've put in a lot of effort into this, but now that the day is over I realize that my original plan of simply putting in a HDRI and having it work was the most sensible one. It has the background and the sun, but it failed and now I find myself messing with all sorts of things to get it to work. Those attempts are all hacks.

I got some good replies to a thread I posted on on Blender Artists. What I will try doing next is LuxCore. It's an open source renderer that is supposedly decent at complex scenes like my own. If that fails I'll just get rid of the balcony doors and let the light stream in.

Some light setting tips I've discovered today:

* https://blender.stackexchange.com/questions/118568/is-there-a-way-to-drive-lamps-similar-to-how-you-can-drive-and-control-a-ca
* https://engelik.gumroad.com/l/DQNYI

Also, the following vid is a got overview of various NPR techniques.

https://www.youtube.com/watch?v=X8YkWdhty7I

I'll want to try out Malt before I wrap up this adventure. I want to start the drawing practice already. I do not at all enjoy messing with lighting.

///

///

>>899312
> if i hide all the crap build around, you can put a ruler next to that.
Yeah, I meant to suggest that you should hide the props on the model, but never got around to it.

I am not sure to suggest what to refine specifically on your model since I am not sure what a spacesuit should look like. But sculpting is a matter of perseverance. The only real sculpt I did was copy Flycat's base mesh. It took me almost a month while it took him a day, but in the end I got it to look good as he did. The beauty of 3d is that you can constantly refine your existing mesh.

I myself am reflecting why I failed to draw those bed creases in 2d, and the most likely reason is because I lost sense of the refining workflow and essentially just started scribling lines. If I was having trouble sculpting the bed creases in 3d, I'd have zoomed in and added extra geometry before getting it just right. But in 2d, if I zoom in I start seeing pixels and stop thinking. I should have taken a step further and opened a separate canvas and painted that tiny bed crease in full resolution instead of thinking something as simple as that would be beneath me. After that it would have been easy to downscale it and transplant it to a 50x50 grid on the actual painting.

The refining workflow is the secret to making good art. I have it in programming, I have it in 3d, but I need to grasp it in 2d. Once you have it, you can steadily get better through practice. Digital art is not about dexterity, if you lack accuracy there are all sorts of tools that can give you that. It is really about planning, much like programming.

///

Yeah, this is how I will affirm my determination. There is no reason why I couldn't 'kitbash' in 2d and do some shading work to integrate the objects afterwards. Immitating what a 3d program would do is not a bad idea. As for Malt, I want it because it has bevel shaders and Eevee does not. And it probably has light falloff, right now this is really killing me in Eevee. What Blender Guru said about making the light sources distant and increasing the power is right, but in this situation the portal light that really makes the scene work is past the grill. I could get a much better scene result with it if I could decrease its light falloff, but I can't.

8:50pm. Let me close here. I am tired. If I recall I have Fable waiting for me. I had to pry myself off it a couple of hours ago, but now the urge to read it has completely faded from memory. Also I got BRS so let me watch that as well. Time for some fun here."

---
## [facebook/flow](https://github.com/facebook/flow)@[a3202ac2ba...](https://github.com/facebook/flow/commit/a3202ac2ba360af4f08ac9963d9f1b3f99aa7a32)
#### Tuesday 2022-05-24 19:39:22 by Sam Zhou

[new-env][RFC] Precisely model implicitly defined `this` and `super` in `name_resolver`

Summary:
Unlike the old env, when we are resolving names in the new env, we only use the loc of the name and do not rely on the current scope tracked by the old env. This works extremely well for all kinds of ordinary names, since all of them have an explicit def loc in the source that can be used as a key. This kind of model breaks down for `this` and `super`, since they don't have a clear place of definition. As a result, they are currently not tracked in name resolver, and cause all the refinements on `this` and `super` to be untracked.

Some hacks can be used to overcome the problem, but they are not very clean:

1. Model `this` and `super` as a module scoped variable, and delegate to the old env for types.
    This actually kinda works, but it still leaves a lot of code that depends on scope being tracked by env for this and super.
2. In the parser, at each function, give this and super a unique location for definition.
    This is very unprincipled and leaks type checking behavior into parser.

If we look at the problem at a higher level, we will see that we are unnecessarily constrain ourselves with only location as the key in `Loc_env`. With this constraint in place, we cannot give two different writes the same location, which is what we hope for `this` and `super`: using the function loc as the def loc.

Instead, more generally, the loc env should be keyed by a write, and we can represent the write uniquely, including `this` and `super` as: `(def_loc_type, loc)`, where `def_loc_type` can be `OrdinaryNameLoc | ThisLoc | SuperLoc`. This setup gives us different namespaces of writes, so we now have the full expressive power to model writes. Changes in `env.ml, new_env.ml` are mostly for dealing with the new parameter `def_loc_type`.

Another big part of this diff is to track the reads and writes of `this` precisely in `name_resolver`. (`statement.ml` also needs to be updated, but it's more mechanical.) In summary, the following important changes are made:

- Reads of `this` and `super` are modeled as reads of ordinary name
- Writes of `this` and `super`
  - Have their special Val: `Val.this`, `Val.super`, so that the writes can be distinguished from ordinary name writes in new-env later.
  - Writes to `this` and `super` will be recorded to their own `write_entries`
  - Happens at each function, conditionally:
    - No writes of `this` and `super` in arrow functions, which correctly models the behavior that they bind the entry in upper scopes. As a result, havoc logic needs to be updated to not invalidate this and super vals.
    - For most functions, their def_loc are both the function loc.
    - For class methods, their def_loc are the method names (to reuse the loc already tracked in class sig).
  - Also happens at class properties, since they can use `this` and `super` and are modeled as functions as well in `func_sig`. The def loc is chosen to be the loc of the entire property.

This approach is not without its drawbacks. The biggest issue is that the implementation detail of choices of def loc for `this` and `super` now leaks into type inference stage. However, I think the benefit of accurate modeling out-weights the leaky abstraction here. In addition, it can remove a lot of coupling between syntactic and semantics analysis in the new env. After this change, the only remaining piece is `arguments`, which can be modeled using the same infrastructure introduced in this diff.

Changelog: [internal]

Reviewed By: mvitousek

Differential Revision: D35165546

fbshipit-source-id: 6979c2c6aec5ca21cf73ae4b9846db355d06edbe

---
## [ReadAlongs/SoundSwallower](https://github.com/ReadAlongs/SoundSwallower)@[782839a884...](https://github.com/ReadAlongs/SoundSwallower/commit/782839a88439238b5ed39ae2cd1568fe0f2e5554)
#### Tuesday 2022-05-24 20:48:47 by David Huggins-Daines

fix: fuck you, Visual C++, and your magic underscores

---
## [Chubbygummibear/Yogstation-TG](https://github.com/Chubbygummibear/Yogstation-TG)@[c3e823d052...](https://github.com/Chubbygummibear/Yogstation-TG/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Tuesday 2022-05-24 21:46:59 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---
## [Chubbygummibear/Yogstation-TG](https://github.com/Chubbygummibear/Yogstation-TG)@[8b77243ce9...](https://github.com/Chubbygummibear/Yogstation-TG/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Tuesday 2022-05-24 21:46:59 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[c77fb1e795...](https://github.com/pariahstation/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Tuesday 2022-05-24 23:18:29 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

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

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[d6548c56ff...](https://github.com/LemonInTheDark/tgstation/commit/d6548c56ffa60728e785752b86d6f0c36023dc0b)
#### Tuesday 2022-05-24 23:21:47 by LemonInTheDark

Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just foam, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[fde8ccd8fc...](https://github.com/LemonInTheDark/tgstation/commit/fde8ccd8fc25967b196d3361968829f76d32576c)
#### Tuesday 2022-05-24 23:22:36 by LemonInTheDark

Removes smoke and foam reactions

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

---
## [zoroarkcity/FargowiltasSouls](https://github.com/zoroarkcity/FargowiltasSouls)@[123ed3c9da...](https://github.com/zoroarkcity/FargowiltasSouls/commit/123ed3c9dad91f773440054f74957467af354a62)
#### Tuesday 2022-05-24 23:29:35 by terrynmuse

nerfed cultist life to 60k (was 80k)
cultist lighting adjusted during ritual
cultist ice mist p2 frost waves adjusted
cultist p2 vortexes track player better, improved consistency and made bolts fire successively faster (this is a nerf)
cultist nebula sphere now starts slow and then speeds up instead of other way around
cultist ancient lights have a stop-and-go thingy
cultist ancient doom is bigger (this is a NERF, they're easier to see)
cultist pillar glow lines very briefly
tweaked eri cage delay AGAIN
eri vortex indicates starting angles of lightning
eri p3 nebula speed nerfed
betsy indicates max range of electrospheres better
betsy electrosppheres immune to gutted heart now
renamed gutted heart creepers to gutted creepers
gutted heart now prevents projs from dealing damage after impacting it, preventing ml proj splash damage from hurting player after hitting a gutted creeper
slight tweak so pierce iframes cannot block gutted creeper contact damage on hostile enemies
king slime no more stunned
king slime p2 spike rain start velocity nerfed
removed ks enrage
altered devi's pause between attacks, generally longer now
nerfed wof hungry chain barrages, now 3 between world evil attacks (was 4)
plantera crystal leaf shots no longer have predictive aim, instead it's a spread shot and speed nerfed
adjusted rotting stat decreases, no longer stacks with living wasteland, has more visuals when applied
changed how cooldown on debuffs like webbed, frozen, stoned, etc. works, now youre immune to them applying again for 4 seconds from most sources after it wears off
added cursed from most enemies to above cooldown debuffs
adjusted backgrounds for class seal buff icons to make them more noticeable
jungle ench gives a weak dash
mutant gives healing when he enters p3, but increased damage of p3
lovestruck on nymph/devi causes you to spew hearts that heal them instead of instant healing
adjusted mutant nuke dust AGAIN
tweaked fossil revive internal implementation, nerfed revival iframes to 3sec (was 5) but gives invul on all iframe timers
fossil/abom wand both print you've revived to chat and combat text since i actually did not notice fossil activating
spaz shoots dark stars instead of fireballs when aiding reti ray spin
reti shoots homing dark stars instead of lasers below 50%
buffed hitbox of dark stars
twins no longer shoot rings of dark stars at 1 life, added text when they endure
prime has improved tells on which limbs he's activating in p2
nerfed golem fists, they can only punch once every 1.5sec (prevents them from machine gun punching next to a wall)
buffed golem fists/head, they track golem body better and don't lag behind when he jumps
fixed golem fists enraging and exploding in edge cases where fists clipped through blocks and "left temple" but you were still fighting in it
golem fist explosions are visible now

---
## [zoroarkcity/FargowiltasSouls](https://github.com/zoroarkcity/FargowiltasSouls)@[06fcd79d7f...](https://github.com/zoroarkcity/FargowiltasSouls/commit/06fcd79d7f11639d3cdda1bfd0d668d692c9c6c9)
#### Tuesday 2022-05-24 23:29:35 by terrynmuse

styx armour sprites real
fixed eri moons reattaching to him if you spawned another while moons were still falling
spirit champ grab grants iframes to prevent you from being multihit while in grab
reverted terra champ iframe mechanic, nerfed life
yoyo bag toggle ignores mutant presence and is in minimal effects
blender nerfed more
mutant has a glow telegraph when preparing to dash
tweaked delay again on mutant spears to glaives
fuck it, all tins have 30t cd
tried making skeletron (prime) not change targets after reticle lock-on, TEST IN MP
fiddled with mutant health bar colours
abom has clear telegraph for icicle fall border
abom scythes spin (before mega ray run) buffed, goes both directions now
abom telegraph for third sword adjusted
devi sparkling axe telegraphs where energy heart rays will fire

---
## [zoroarkcity/FargowiltasSouls](https://github.com/zoroarkcity/FargowiltasSouls)@[1c373747ad...](https://github.com/zoroarkcity/FargowiltasSouls/commit/1c373747ad5c7a47f7070daa3d4e3ccff159ad50)
#### Tuesday 2022-05-24 23:29:35 by terrynmuse

tweaked eri cage delay
increased spread on slime slinging slasher
buffed regurgitator hungry homing, reduced delay on spawning a new one, nerfed damage a lot when hungry isn't fully charged
berserked grants 10% increased damage, move speed, attack speed
rotting works on all npcs, including hostiles (was friendly only)
tweaked mutant eye sphere ring, fixed spawning 100 projs
naive attempt to fix confused left flips gravity
npcs become immune to most damage at 1 life in timestop, hopefully timber p1 doesnt shit a million heads now
changed eri contact debuffs from on fire/hexed to burning/berserked
adjusted timing on mutant p2 predictive dash and spin glow tells
reduced dust on mutant pillar fragments
sparkling adoration has a graze radius visual (toggleable)
reduced abom debuffs
improved abom tell from flaming scythes to dashes

---
## [SpyraxianJ/strung-along](https://github.com/SpyraxianJ/strung-along)@[3c221e7f2d...](https://github.com/SpyraxianJ/strung-along/commit/3c221e7f2d5adad24e71ecfdbc058bad877c6f73)
#### Tuesday 2022-05-24 23:37:07 by Tim Beau David

Fixed the character controller inconsistency issue

OH MY GOD HOLY SHIT I ACTUALLY FOUND THE LITTLE RAT BASTARD ERROR AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

I really thought this tiny little shit was going to be the end of me omg

---
## [Lunu-Lunu/Inkunzi-EU4](https://github.com/Lunu-Lunu/Inkunzi-EU4)@[b8962d8f56...](https://github.com/Lunu-Lunu/Inkunzi-EU4/commit/b8962d8f56e6d652b84feac334fc491d5a83e162)
#### Tuesday 2022-05-24 23:45:54 by supercow2

OMG OMG OLD ONES

i did it !!
-old ones event and modifier
-name changes
-other shit? don't remember

---

