## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-23](docs/good-messages/2023/2023-08-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,234,397 were push events containing 3,455,699 commit messages that amount to 274,908,520 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 75 messages:


## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[34306b4266...](https://github.com/Hatterhat/Skyrat-tg/commit/34306b4266e0cc8219d0bb9ca809350ec4035d3f)
#### Wednesday 2023-08-23 01:04:00 by SkyratBot

[MIRROR] Buffs Heretic ash ascension [MDB IGNORE] (#23114)

* Buffs Heretic ash ascension (#77618)

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

* Buffs Heretic ash ascension

---------

Co-authored-by: DaydreamIQ <62606051+DaydreamIQ@users.noreply.github.com>

---
## [AllyTally/VVVVVV](https://github.com/AllyTally/VVVVVV)@[86d90a1296...](https://github.com/AllyTally/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Wednesday 2023-08-23 01:23:12 by Misa

Add color support to Windows console output, properly

This adds color support to the output of the console on Windows. Now if
you're using Windows 10 build 1511 or later (I think it's build 1511
anyway; they added more VT sequence support in later versions), you will
see colors by default. This isn't due to Windows helping in any way;
this commit has to specifically enable it with SetConsoleMode() because
by default, Windows won't enable color support unless we enable it. (Or
if it's enabled in the registry, but having to go through the registry
to enable basic shit like that is completely fucking stupid.)

I tested this in my Windows 10 virtual machine and it's completely
working.

---
## [sennhann29/codecov-api](https://github.com/sennhann29/codecov-api)@[e2c6b1c425...](https://github.com/sennhann29/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Wednesday 2023-08-23 01:41:56 by Giovanni M Guidini

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
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[2d4d23dbf1...](https://github.com/Fikou/tgstation/commit/2d4d23dbf1e2cc23ed2046534011561e443060f7)
#### Wednesday 2023-08-23 01:43:13 by Timberpoes

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
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[3645fa7d89...](https://github.com/Fikou/tgstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Wednesday 2023-08-23 01:43:13 by distributivgesetz

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
## [the-die/linux](https://github.com/the-die/linux)@[4542057e18...](https://github.com/the-die/linux/commit/4542057e18caebe5ebaee28f0438878098674504)
#### Wednesday 2023-08-23 01:44:29 by Linus Torvalds

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
## [Mirino97/space-station-14](https://github.com/Mirino97/space-station-14)@[31607a0be0...](https://github.com/Mirino97/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Wednesday 2023-08-23 01:45:08 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [useCallback/hhvm](https://github.com/useCallback/hhvm)@[05f943817e...](https://github.com/useCallback/hhvm/commit/05f943817eff455abc73505caf582c889c3fb349)
#### Wednesday 2023-08-23 01:47:51 by Vincent Lee

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
## [mahmud8bd/Food_Delivery_System_SpringBoot_Angular](https://github.com/mahmud8bd/Food_Delivery_System_SpringBoot_Angular)@[cca0c868a2...](https://github.com/mahmud8bd/Food_Delivery_System_SpringBoot_Angular/commit/cca0c868a24671de41e10dab6e135b21105f6819)
#### Wednesday 2023-08-23 02:16:11 by Mahmudul Hasan

Update README.md

"Welcome to the Food Delivery System built with Spring Boot and Angular! This platform offers a streamlined solution for online food ordering and delivery. With our intuitive user interface, customers can easily browse through menus, place orders, and make secure payments.

Key Features:

🍔 Menu Exploration: Explore a diverse range of restaurant menus with an interactive and user-friendly interface.

🛒 Effortless Ordering: Simplified ordering process with the ability to customize items according to preferences.

🚴‍♂️ Real-time Tracking: Keep track of your order's status in real-time, from preparation to doorstep delivery.

💳 Secure Payments: Experience worry-free transactions through integrated secure payment gateways.

🌐 Responsive Design: Enjoy a seamless experience on any device, thanks to the responsive design of our application.

📝 Reviews and Ratings: Share your thoughts by leaving reviews and ratings for the restaurants you've ordered from.

👤 User Profiles: Manage your profile information, order history, and delivery addresses effortlessly.

This repository contains both the Spring Boot backend and Angular frontend codebases, ensuring a well-structured and cohesive system. Whether you're interested in exploring the backend logic or diving into frontend UI/UX implementation, this repository has it all.

Join us in revolutionizing the food delivery experience. Your cravings, our responsibility. Happy ordering!"

Feel free to adjust this description to fit your specific project details and style.

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[cd8a55f9d5...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/cd8a55f9d54bd82fca9605e88169c96d79558f5d)
#### Wednesday 2023-08-23 02:50:52 by Rhials

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
#### Wednesday 2023-08-23 02:50:52 by Jacquerel

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
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[f84e468b36...](https://github.com/diphons/D8G_Kernel_oxygen/commit/f84e468b3684ec08dd79d9642bbce0a86cc7c28a)
#### Wednesday 2023-08-23 03:01:03 by George Spelvin

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

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[09cd04a05b...](https://github.com/diphons/D8G_Kernel_oxygen/commit/09cd04a05b44d784eae73872573e4c9881d9dfd0)
#### Wednesday 2023-08-23 03:01:51 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [newstools/2023-the-star](https://github.com/newstools/2023-the-star)@[e18c7c0fa3...](https://github.com/newstools/2023-the-star/commit/e18c7c0fa3d5bdaf292dd134aaed820824e0b509)
#### Wednesday 2023-08-23 03:03:47 by Billy Einkamerer

Created Text For URL [www.the-star.co.ke/counties/central/2023-08-22-life-in-jail-for-man-from-hell-with-appetite-for-defiling-little-boys-girls]

---
## [newstools/2023-the-star](https://github.com/newstools/2023-the-star)@[e268049b04...](https://github.com/newstools/2023-the-star/commit/e268049b042988e739a3d76f070ddfbc04ee92f4)
#### Wednesday 2023-08-23 03:07:25 by Billy Einkamerer

Created Text For URL [www.the-star.co.ke/counties/counties/central/2023-08-22-life-in-jail-for-man-from-hell-with-appetite-for-defiling-little-boys-girls]

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[f0dc574c37...](https://github.com/ZephyrTFA/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Wednesday 2023-08-23 03:14:38 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[e04b290791...](https://github.com/Mission23/Mission23/commit/e04b290791082da5183c86e9f6e39382b6c02378)
#### Wednesday 2023-08-23 03:24:31 by Micah

The yellow metal box…

The yellow metal box inside his suitcase just shot a stream of air directly at me.

Smells funny  

That is my dog Dex in art on top. He’s the second victim in this tragedy. Was in a kennel after my foreclosure eviction that shouldn’t have happened. They engineered it too. 

Jim Allen from Kentucky I’m told was the first. He lived in Cobb county we became friends after meeting on Google+ because we were both blue blooded Kentuckians. Good guy. His sin, he helped me out loaning me $200. Then they asked him to do shit against me, he refused. 

The CIA nor Gilead Sciences likes to be told no. 

We do have one somber task to do… Death certificates. The Creator is going to be giving us every name, time and date of death and manner. He can also tell us who was there. Not just for this tragedy, but every one the CIA has done. 

They will be accepted. As soon as he stops ringing the bell. Did you see MY earthquake predictions? First time ever. I’m that awesome. J/K

---
## [1nfinityusk/StoryFi](https://github.com/1nfinityusk/StoryFi)@[2e38f7ef65...](https://github.com/1nfinityusk/StoryFi/commit/2e38f7ef65bd7c7465e022e16e8b1fc6d9eebd90)
#### Wednesday 2023-08-23 03:26:33 by 1nfinityusk

Update README.md

Business plan for investors

Vision and goals:
Our vision is to support low-income creators who are struggling with branding and provide an environment where they can focus on creating. 

We aim to be a platform where creators can self-produce by providing a low-cost, yet objective, fun, and game-specific UI/UX. 

We also support creators' growth and fulfillment of their need for recognition through psychological safety and community building.
Market and competitiveness:
To solve the challenges faced by creators, we provide low-cost web applications with excellent UI/UX. 

Competitive differentiators include the creation of a unique techno-artist market, daily assistance from AI agents and AI producers, game-like elements, and in-game rewards in cryptocurrency.
Solutions and added value:
The web application we provide offers a low-cost yet excellent UI/UX for low-income creators struggling with branding.

They can utilize self-production-specific features and tools to build their own brand story and interact with AI producers. 

This improves the efficiency and results of their production activities.
Marketing and growth strategy:
The marketing strategy includes the free roll-out of a beta version of the diagnostic tool and the creation of a community. It will raise awareness of the tool as an essential tool for music artists through the use of influencers and the provision of brand stories and interaction with AI producers. As a growth strategy, after achieving the PMF, the service will be expanded to be offered as an individual personal producer service, and community-based marketing will be developed to encourage communication and exchange of skills between creators.

Revenue model:
Our revenue model is a subscription model with the first month free. Customers pay USD 8 per month and have access to all features of the platform. For corporate plans, we offer a new business development program for $25 000. Additional revenue is generated by offering in-game cryptocurrency rewards and adding unique options.
Sales and marketing strategy:
Initially, a beta version of the diagnostic tool will be rolled out for free to build a community of creators. Use influencers to build brand awareness, build brand stories and start offering the ability to interact with AI producers. Attract demand, particularly from music artists, and utilize them as power users.
Growth strategy:
After achieving PMFs through artist connections, we will first establish the service as an individual personal producer service. We will then grow the platform by developing community-based marketing in the form of a fusion of gaming and real life that promotes communication and the exchange of skills between creators. Sa.

Why do we want to do this business:
As a creator myself, I have experienced the current situation where low-income creatives are struggling with branding. From that experience, they needed mentors and producers they could consult on a daily basis. Through this project, I want to provide an environment where low-income creatives can focus on production and help them grow and succeed.


ターゲットオーディエンスの詳細:

1.平均年収300万円
2.国：アジア、US、ヨーロッパ
3.20-35
4.クラブミュージックのアーティスト

テクノロジーとプラットフォーム:

1.Azure open AI
2.python,go
3,Azure strage

AIプロデューサーの役割:

AIプロデューサーがどのようにクリエイターをサポートするかの詳細。
AIの具体的な機能や利点。

Ai producer service

Linking the generative AI,

Develop the artist's brand story and promotional plan.

Just by answering a few simple questions,

verbalise your definition of Personal Identity

(values, strengths, weaknesses, core values,

worldview, talents, catchphrases).


It will compile the verbalised Identity into an original brand, and output it as a game map of what needs to be done, concretised for each Artist.



AI-based personal mentor function

Your dedicated AI Producer will answer any questions you have about your branding.
You can ask questions to the AI producer at any time,

and he will interact with you by mentions of your activities (twitter, instagram, tiktok, etc.) and other social media to do.

Create your own branding map.

Enjoy a brand story adventure with your own personalised world map, generated based on your favourite images.
It will compile the verbalised Identity into an original brand

and output it as a game map of what needs to be done,

concretised for each Artist.

ゲーム要素と仮想通貨報酬:

アクションプランをそのままRPGゲームのクエストのような体験にする。
AIプロデューサーとの対話そのもので恋愛要素を盛り込む

1.ユーザーが指示された行動を行うたびに報酬として受け取る
2.人気に応じて報酬が受け取られる


パートナーシップとコラボレーション:

日本国外の音楽フェス


KPIsと成功の指標:

Marketing Strategy Overview
Year
DAU
Strategy
Budget ($)
Channel
Action
2023
800
1. Use influencer, 2. Use techno artist, 3. Event sponsored
63k
1. FB, Twitter, LinkedIn, 2. Offline event
1.use prototype for free
2.event sponsored
3. to B sakes in Japan
2024
8000
1. Community marketing, 2. Air drop macerating, 3. Event sponsored
189
 
 
 
 
1. Discord community, 2. Telegram, 3. Offline event
1.community management
2.event sponsored 3. to B sakes in Japan
2025
80000
1. Make owned media, 2. Event organized, 3. Community marketing
693
1. Owned media, 2. Discord and Telegram, 3. Own event
1. Use prototype for free, 2. Event sponsored, 3. To B sales in Japan
2026
400000
1. Event organized, 2. Ambassador, 3. Community marketing, 4. Market shift
1818
1.ambassador program share by SNS
2.discord and telegram
3.Go to business person target
1. Community management, 2. Event sponsored, 3. To B sales in Japan
2027
800000
1. Event organized, 2. Ambassador, 3. Community marketing, 4. Market shift
4046
Not provided
1. Make original media, 2. Community management, 3. Organize own event, 4. Planning ambassador program, 5. Research for another target and get PMF using advertisements.

 



リスクと課題:

リスク：法的な規制、似たようなサービスによる模倣
対策：データアセットや学習情報をいつでも移管できるようにしておき、法規制に応じて改変を用意にする。似たようなサービスについてはクラブカルチャーのようなニッチなマーケットでコアなファンを囲い込み、UI/UXに力をいれることで独自カルチャーの形成により参入障壁をつくる。

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[8084d68664...](https://github.com/diphons/D8G_Kernel_oxygen/commit/8084d68664aaddfc969486b24af5761f92cf0bf4)
#### Wednesday 2023-08-23 04:04:22 by Wang Han

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

---
## [theonetruejesse/mSync](https://github.com/theonetruejesse/mSync)@[58dd2560c7...](https://github.com/theonetruejesse/mSync/commit/58dd2560c72a99a985d88cfd885fa90a42e00705)
#### Wednesday 2023-08-23 04:32:24 by Ethan Kim

Refactored, Twilio MVP almost done

Evil S.I.S to find a shore
A beast that doesn't quiver anymore
And we could crush some plants to paint my walls
And I won't try to fight the weekend wars

---
## [theonetruejesse/mSync](https://github.com/theonetruejesse/mSync)@[f700131bca...](https://github.com/theonetruejesse/mSync/commit/f700131bca678c5f6f57f54ce7a308fe642b34aa)
#### Wednesday 2023-08-23 04:34:32 by Ethan Kim

Trying to get the hang of merges

Was I? I was too lazy to bathe
Or paint or write or try to make a change
Now I can shoot a gun to kill my lunch
And I don't have to love or think too much

---
## [akshay-srini/learning](https://github.com/akshay-srini/learning)@[332441d24a...](https://github.com/akshay-srini/learning/commit/332441d24a823cf73cb113869efcf10e005d52d0)
#### Wednesday 2023-08-23 04:45:58 by akshay-srini

Fuck off AND EAT SHIT

You better suck ma dick nigga

---
## [Pariah919/TerraGov-Marine-Corps](https://github.com/Pariah919/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/Pariah919/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Wednesday 2023-08-23 04:59:12 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [glhfcarlos/GameHeadSpaceCrusaders](https://github.com/glhfcarlos/GameHeadSpaceCrusaders)@[8c9e6a1447...](https://github.com/glhfcarlos/GameHeadSpaceCrusaders/commit/8c9e6a144793cddd27d83d802bd3404b140c646b)
#### Wednesday 2023-08-23 05:15:24 by anihie

Merge pull request #5 from glhfcarlos/main

please god fuck this shit i want this to work

---
## [WordlessMeteor/LoL-DIY-Programs](https://github.com/WordlessMeteor/LoL-DIY-Programs)@[cb82b3e754...](https://github.com/WordlessMeteor/LoL-DIY-Programs/commit/cb82b3e7545ed0c9f29a3dc3225bfd3a3c35fbdf)
#### Wednesday 2023-08-23 06:18:17 by WordlessMeteor

更新了自定义脚本5、9、10和整合版文件，以及添加了一个新功能【Updated Customized Programs 5, 9 and 10 and Added A New Function】

一、程序更新综述（Program Update Summary of Version 2.8 -> 3.1 - QiXi Version）
七夕已经过了，回归正常生活，你是否终日忙碌，却总觉心中有一份空虚？你是否曾苦苦追寻，终为冰冷的现实而折腰？也许，你和心中的那个TA，只是少了一座桥梁、一次良机、一场缘分。话已至此，那就不妨来试试这个新程……🤐（手动电视台无信号）
The Chinese Valentine's Day has passed. Back to normal, do you fulfill your life all day, but still find somewhere void in your heart? Did you ever find someone hard, but finally give into the grim reality? Maybe you just need a magpie bridge, an opportunity and a fate, to get you together with the he/she in your mind. Hearing this, you really don't want to try this new pro... (Manually out of TV signal) (No, thanks!)
本次更新主要添加了一个用来汇总曾经与一名指定的召唤师（主召唤师）在同一场对局的召唤师的信息的程序，同时在撰写代码的过程中修改了其它脚本的代码写法（别问怎么发现的，问就是大部分代码还是复制粘贴的），以更加服从某种潜规则。例如，在查战绩脚本和查模式脚本中，许多数据框的标题字典的键值对顺序得到更新，这样属于同一层次的键能够聚在一起，并按首字母大小排序（当然不纯按首字母大小排序，因为有些键是经过处理的），方便后续更新。此外，也是基于这个想法，我在主目录中添加了一个Excel表格，里面记录了一些重要数据框的标题中英文信息，并给出每个标题（或者说特征，如果用人工智能的术语的话）在工作表中的序号。（提醒一下，如果想要复现代码中那些后缀“_display_order”的列表，只需要将整个工作表按照`OutputOrder`进行升序排列即可。）
In this update, a new program is added to collect information of summoners that once fought with a specific summoner (main summoner) in a same match, and code in some other programs are modified while coding for the new program (If you must ask how I found the problems to modify, I'll answer that most code came from copying and pasting), so that they obey some underlying principle. For example, in Customized Programs 5 and 9, the order of key-value pairs in many dataframes' corresponding header dictionaries is updated, so that keys of the same levels can be gathered together and arranged by the ascending order of the capital letter (of course not completely, because some keys are processed), making it easier for the later update. Besides, inspired by this idea, I added an Excel workbook in the home directory, which records the Chinese and English headers of some important dataframes and give the order to arrange the headers (or features if using the AI term) in sheets. (Note that to recur any list variable postfixxed with "_display_order", the user only need to rearrange the corresponding sheet in the ascending order of the `OutputOrder` column.)
只要玩过这个程序的人，就会发现，基于寻找近期一起玩过的玩家的需求，应该只需要呈现召唤师名称之类的信息就够了吧，没有必要再去呈现该玩家的当局数据。对于这个问题，我有两点想说：其一，有的时候，该脚本的用户不是为了无差别地寻找那个曾经有意无意和自己一起并肩作战许久的玩家，可能还是会带有一点倾向性，比如战绩好一点的，那我肯定更愿意和他一起排。很正常的心态。我本人倒是不是特别看重这点，但是总有人有这种需求，那么不妨去满足这种需求，就是说添加这种反映对局表现的信息（反正我自己不看就是了，别人想看就看）。众所周知，目前反映对局表现，有一个非常权威的指标，就是对局评分。目前对局评分有三种算法：第一种是英雄联盟内置的评分机制，通过这个评分可以得知一名玩家是不是可以拿到S-级以上的评分；第二种是WeGame和掌上英雄联盟记录的评分，由此来评选MVP和SVP；第三种是OPScore，用来评选MVP和ACE。但是遗憾的是，目前我并没有找到其详细算法的资料，所以只能等日后相关算法公布后再添加评分功能。其二，在生活中我一直遵循的一个原则是，数据多了可以删，少了就没法造了。迁移到程序设计，数据一多，后来的开发者就可以选择在这些数据上做研究，当然他们也可以忽视多出来的数据，但是最重要的是有选择的余地了；数据一少，那后来的开发者要想用到某些数据，还得自己再写代码。虽然我的代码不一定美观，数据不一定有用，但是起码应该给别人选择的余地：他们看了可以不采用，但是我不提供的话，他们连看的机会都没有。
Anyone that plays with this program will notice that to satisfy the demand for finding the recently played summoners, information like summonerName should be enough, and there's no necessity of displaying his/her match data. I got two points to explain. First, sometimes users of this program are not finding the player that teamed or preteamed with the users themselves with a sense of equality: they may behave some priority, for example someone did a good job in several matches, so then I'm going to play with him/her. That's a very common thought. I myself don't stress this priority actually, but since there will always be someone that has this requirement, then it's of no harm to satisfy it, that is, to add the data that reflects the performance of a player (I won't check them, but if someone wants, just do it). As is known to all, there is currently an authoritative index to reflect the in-game performance, that is, the match score. At present there're 3 algorithms to calculate this score: first, the internal scoring system in LoL, which tells whether a player has scored a level over S-; second, the scores recorded in WeGame and the Tencent Mobile LoL Assistant, which evaluates the MVP and the SVP; third and last, the OPScore used by OP.GG, which selects the MVP and the ACE. But pitifully, I didn't put my hands on any information about their specific algorithm, so let's wait to add the scores for some time when the algorithms are made public. Second, one principle I always obey, even in my life, is that excessive data can be deleted, but a lack of data is hard to make up. Applying this principle in programming, once more data are provided, the later developers can decide to research on extra data, and they can also neglect them; the most important point I want to express is they got choices. But once data are not sufficiently provided, then the developer has to write the code themselves for the use of some data, if they become necessary some day. I know my code might not be clean, and my data might not be useful, but the developers should have right to choose: they can say "I don't want to use these data/code" after scannig my code, but if I don't provide, they don't even have a chance to glimpse at it.
最后，可以注意到整合版文件也发生了变化。然而，编译出来的时候，与源文件完全没区别——只是改了一处注释而已。至于为什么改这处注释，也是在编辑这个求缘脚本（姑且先这么叫吧，可能有点小怪，但是我想不出什么简洁的称呼来代替“自定义脚本11”或者“查近期一起玩过的玩家的脚本”。要不叫“七夕限定版程序”？）的时候，发现注释中没有列全游戏状态。
Finally, users may notice that there's a change in the consolidated program. But actually the files generated by compiling the new program are no different than the those generated by compiling the old program: only an annotation is perfected. As for why I change it, I just found the annotation doesn't list all of the gameflow states when editing this new program.
二、实现细节（Implementation Details）
注：以下修改在求缘脚本中都生效。求缘脚本将不再单独说明。
Note: These modifications are applied in Customized Program 9, so they won't be listed repeated.
1. 输入的召唤师的玩家通用唯一识别码变量一律命名为“current_puuid”。（自定义脚本5第215、796和1019行。）
The puuid variable of the input summoner is named "current_puuid" now. (Lines 215, 796 and 1019 in Customized Program 5.)
2. 删除了一句注释，因为在第243行已经出现了比较完整的声明。（自定义脚本5原代码第364行。）
Removed an annotation, since a relatively complete declaration has been in Line 243. (Line 364 originally in Customized Program 5.)
3. 完成了一处时间优化：添加了一处break语句，使得在从排位信息中寻找狂暴模式的数据时，如果找到狂暴模式的编号，则直接退出循环。（自定义脚本5第370行。）
Finished a time optimization: added a "break" statement, so that when the program is searching for the TFT turbo data from the rank data, if the index of TFT turbo is determined, then the program will exit the loop. (Line 370 in Customized Program 5.)
4. 完善了一处程序控制：现在，在获取召唤师的最近200场对局失败的输出提示下，可以选择输入任意字符以退出获取，重新切换召唤师，甚至退出程序。（自定义脚本5第456至462行。）
Improved a program running direction control. Now, when the program outputs a hint on the failure of getting a summoner's recent 200 matches, the user can input any non empty string to exit the getting step, switch for another summoner and even exit the program. (Lines 456～462 in Customized Program 5.)
5. 所有与游戏模式名称相关的变量和键一律命名为“gameModeName”。（自定义脚本5第467、478、524、527、736、811和814行。）
All variables related to the name of game modes are named "gameModeName". (Lines 467, 478, 524, 527, 736, 811 and 814 in Customized Program 5.)
6. 修复了使用FindPostPatch函数时的一个警告问题：传递变量时，FindPostPatch函数的第一个参数应当是具体的一个版本号（字符串），而不是版本号列表gameVersion。（之前这样还能正常运行我是没想到的，一定是Python在编译时用了什么隐式类型转换。）（自定义脚本5第539和826行。）
Fixxed a warning when the program calls the `FindPostPatch` function: during passing parameters, the first parameter of `FindPostPatch` function should be a specific patch string, instead of the patch list `gameVersion`. (But it's surprising that the program still operated as normal in the past. Python must have used some implicit type conversion when compiling.)
7. 调整了一处输出提示。（自定义脚本5第693行。）
Adjusted an output. (Line 693 in Customized Program 5.)
8. 更新了对局信息标题字典和时间轴标题字典。没有新增内容，主要是调整了键值对的顺序。（自定义脚本5第1067和1242行。）
Updated the game information header and game timeline header dictionaries. No content is added. Mainly adjusted the order of key-value pairs. (Lines 1067 and 1242 in Customized Program 5.)
9. 更新了对局信息标题字典和时间轴标题字典在赋值时的条件控制。主要调整了迭代器i的取值。（自定义脚本5第1109至1184和1249至1266行。）
Updated the conditions of the if-statements when assigning values to the game information header and game timeline header dictionaries. Mainly adjusted values of the iterator `i`. (Lines 1109～1184 and 1249～1266 in Customized Program 5.)
10. 更新了用来控制对局信息数据框和对局时间轴数据框的标题显示顺序的列表。（自定义脚本5第1190和第1301行）。
Updated the lists to control the display order of headers of the game information header and game timeline header dictionaries. (Lines 1190 and 1301 in Customized Program 5.)
11. 游戏模式相关的变量名中的“info”一律改为“queues”。此外将“headers”替换为了“header”。（自定义脚本9第62、64至66、73、75、78至82、84、86、87、90、91、93、94、96、97、99、100、102至110、112至119、139和144行。）
All "info"s in the name of the game mode variables are substituted by "queues". "headers" is replaced with "header", in addition. (Lines 62, 64～66, 73, 75, 78～82, 84, 86, 87, 90, 91, 93, 94, 96, 97, 99, 100, 102～110, 112～119, 139 and 144 in Customized Program 9.)
12. 更新了游戏模式标题字典。新增了“showQuickPlaySlotSelection”键。（自定义脚本9第64行。）
Updated the game mode header dictionary. Added a key "showQuickPlaySlotSelection". (Line 64 in Customized Program 9.)
13. 更新了游戏模式标题字典在赋值时的条件控制。主要调整了迭代器i的取值。（自定义脚本9第76、85、88、89、92和95行。）
Updated the conditions of the if-statements when assigning values to the game mode header dictionary. Mainly adjusted values of the iterator `i`. (Lines 76, 85, 88, 89, 92 and 95 in Customized Program 9.)
14. 更新了游戏模式数据框的标题显示顺序的列表。（自定义脚本9第105行。）
Updated the list to control the display order of headers of the game mode header dictionary. (Lines 105 in Customized Program 9.)
15. 修正了一处英语用法：in entirety可以使用entirely以更加简洁地表达。（自定义脚本9第146行。）
Improves an English usage: "In entirety" can be replaced by "entirely" for a more brief expression. (Customized Program 146.)
16. 相比查战绩脚本，求缘脚本主要实现了近期一起玩过的玩家数据框的建立（自定义脚本11第578至738行，与对局信息和时间轴数据框的建立大同小异）、元数据的建立（自定义脚本11第741至793行）、柱状图的输出（自定义脚本11第795至919行）、游戏状态反馈（自定义脚本11第948至972行）和选英雄阶段队友识别（自定义脚本11第973至1018行）。
Compared with CUstomized Program 5, Customized Program 9 mainly achieved the creation of the dataframe that stores information of recently played summoners (Lines 578～738 of Customized Program 11 of no big difference with game info and game timeline dataframes), the creation of recently player summoner metadata (Lines 741～793 in Customized Program 11), output of bar charts (Lines 795～919 in Customized Program 11), hints on the summoners' gameflow state (Lines 948～972 in Customized Program 11) and recognition of allies during champ select (Lines 937～1018 in Customized Program 11).
17. 新增了一个Excel工作簿，用于呈现主要数据框的结构和输出时排序的思路。关于如何阅读该工作簿，详见说明文档。
Added an Excel workbook to display the structure of main dataframes and the idea of the arrangement order for output. Please refer to README to learn more details about how to read this workbook.
18. 修改了一处注释：添加了一种游戏状态。（整合版文件第465行。）
Modified an annotation: added a gameflow state. (Line 465 in Consolidated Program.)
19. 修正了提到的的脚本命名格式：在“Program”和“[数字]”、“Program”和“[Number]”之间各添加了一个空格。（说明文档第76和237行。）
Modified the format for naming the programs: added a space between "Program" and "[数字]" and between "Program" and "[Number]". (Lines 76 and 237 in README.)
20. 移除了一条未来规划，因为现在这条未来规划已经实现了。（原说明文档第108行。）
Removed a future plan, because it's achieved now. (Line 108 in the original README.)
21. 添加了对求缘脚本和主数据框结构工作簿的说明。（说明文档第107至116、118至159、268至277和279至320行。）
Added instructions on Customized Program 11 and the main dataframe structure workbook. (Lines 107～116, 118～159, 268～277 and 279～320 in README.)
三、未来规划（Future Plan）
目前暂时没有什么想要开发的功能了。可能未来会研究一下私有存储库用来存放说明文档要呈现的图片是否可行。如果有什么好玩的需求，欢迎私戳WordlessMeteor#5282！
I don't have any function to develop for now. Maybe I'll study if it's possible to store the pictures of README in a private repository. If you have some interesting ideas, welcome to contact WordlessMeteor#5282.

---
## [rwuwon/dotfiles](https://github.com/rwuwon/dotfiles)@[08aceb088d...](https://github.com/rwuwon/dotfiles/commit/08aceb088d94bbd6daa4390fa2ad4fad09f53353)
#### Wednesday 2023-08-23 06:31:37 by Raymond Wu Won

Swap DVI-DP cable for DVI-DVI cable

Nvidia GTX 1050 Ti doesn't really care that the adapter cable is used,
but the Intel integrated graphics won't work with a DVI-DP cable (which
my motherboard manual does document, by the way). When my binary Nvidia
drivers from the Debian repo got messed up during the recent Debian 11
to Debian 12 upgrade, it made troubleshooting very confusing when I
couldn't get output to appear on both displays at the same time.

Previously, I think I opted for a DVI-DP cable due to the pain of
connecting DVI plugs to their sockets (it's worse than USB!), but I've
now simplified this setup in case future-me needs to rely on the
integrated graphics again.

As a side benefit, GRUB now appears on my main display (via DVI-DVI)
rather than secondary display (HDMI-VGA). It appears that DP (despite in
theory having the highest quality) is prioritised last both in
behaviour, and my graphics card ports layout?

---
## [jeffreyhasan10/CODSOFT](https://github.com/jeffreyhasan10/CODSOFT)@[04f4b8728e...](https://github.com/jeffreyhasan10/CODSOFT/commit/04f4b8728e9c408b858257dc1770608e9b3ee855)
#### Wednesday 2023-08-23 06:43:17 by Jeffrey Hasn

 Readme.txt

This tribute website celebrates the incredible career of football legend Lionel Messi. Known for his unparalleled talent and achievements on the pitch, Messi has solidified himself as one of the greatest to ever play the game.

The site includes:

An introduction highlighting Messi's background, early life, and road to stardom. Key facts and stats provide an overview of his success.
A timeline of career highlights from his early days in Argentina to breaking records with Barcelona and Argentina. Major trophies, milestones, and defining moments are highlighted.
A collection of Messi's greatest goals with embedded videos allowing you to relive his magical moments. Long-range free kicks, mazy solo runs, and important cup final goals are included.
An interactive stats section with animated counters showing Messi's unbelievable numbers. Toggle between goals, assists, trophies and more.
A responsive photo gallery with high quality images spanning his historic career.
The site design pays tribute to Messi with a modern, sleek interface and seamless user experience across desktop and mobile. Animations and parallax effects bring his story to life.

Whether you're a lifelong fan or just discovering his brilliance, this is the ultimate hub to explore the legend of Lionel Messi!

---
## [schlig/Bridgewars](https://github.com/schlig/Bridgewars)@[b468503ef2...](https://github.com/schlig/Bridgewars/commit/b468503ef2fb111f2ea97bb8091cbce146d565d8)
#### Wednesday 2023-08-23 06:55:41 by schlig

emotional anguish

too much shit for me to remember was added

---
## [XDuskAshes/duskkernel](https://github.com/XDuskAshes/duskkernel)@[4ae548b3d5...](https://github.com/XDuskAshes/duskkernel/commit/4ae548b3d57a6cd47e6f9162f07b9a3e314f30de)
#### Wednesday 2023-08-23 06:58:48 by XDuskAshes

rebrand, begin to rework

CC-Linux was something ambitious, but absolutely stupid in hindsight.

I did enjoy making it, but it ended as a crapshoot, and never really
went anywhere. Therefore, with my recent work on dawn, I decided to
remake CC-Linux from the ground up with a new name: "Dusk Kernel". This
will be both like and unlike Linux itself, more taking inspiration and
such.

This commit made 8/23/23, at almost 3 in the morning, running on 0 hours
of sleep.

---
## [Biki-das/react-1](https://github.com/Biki-das/react-1)@[ac1a16c67e...](https://github.com/Biki-das/react-1/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Wednesday 2023-08-23 07:00:48 by Sebastian Markbåge

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
## [SoMainline/linux](https://github.com/SoMainline/linux)@[b59b31b866...](https://github.com/SoMainline/linux/commit/b59b31b866133bf21195eceabb86d8a3f2a5e2d6)
#### Wednesday 2023-08-23 07:08:58 by Linus Torvalds

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
## [kirillzyusko/react-native-keyboard-controller](https://github.com/kirillzyusko/react-native-keyboard-controller)@[84f94eb639...](https://github.com/kirillzyusko/react-native-keyboard-controller/commit/84f94eb6393e930b9debe75d2a763c523e02d130)
#### Wednesday 2023-08-23 09:21:07 by Kirill Zyusko

refactor: react on tag changes (#216)

## 📜 Description

Improved `KeyboardAwareScrollView` example - now it react on `TextInput`
focus changes 🙂

## 💡 Motivation and Context

I highlighted key changes below:

### Interpolation depends on previous keyboard size

Before it was a fixed number (0). But since the size of the keyboard can
be different per different `TextInput` types - we have to interpolate
value from previous keyboard size to the new one. Otherwise the
animation when keyboard changes its size looks slightly ugly (will have
a jump in beginning).

Just as an example let's imagine, that the keyboard is changing size
from `200` to `300` and you need to scroll from `100` to `200`. The
current scroll position is `100` and you interpolate as before from 0 to
300. In this case, when keyboard size grows from 200 to 300 first
scrollTo will scroll to ~160. So 60% of the smooth transition will be
missed 😔

If we interpolate from `previousKeyboardSize`, then we will interpolate
from `200` to `300` (as expected) and we'll have a smooth transition for
all distance.

### Assure `TextInput` is not overlapped by `Keyboard` in `onEnd`
handler

Sometimes `onMove` handler can be missed. It happens in two cases:
- on iOS when TextInput was changed - keyboard transition is instant and
`onMove` will not be triggered;
- on Android when TextInput was changed and keyboard size wasn't
changed.

To handle these cases I've decided to run `scrollTo` in `onEnd` handler.
For plain transition it will not have any effect, because scroll
position already will be as the desired one.

However for cases above it'll handle TextInput focus changes and will
assure, that the `TextInput` is always above the Keyboard 🙂

### Back transition

To assure smooth back transition I've introduced
`scrollBeforeKeyboardMovement` (updated whenever `TextInput` becomes a
focus). Later this variable is used in interpolation, when keyboard
hides.

Also I do a layout substitution in `onEnd` handler:

```tsx
const prevLayout = layout.value;
layout.value = measureByTag(e.target);
// ...
layout.value = prevLayout;
```

This is needed because we need to remember "initial layout" (before
keyboard movement) in order to perform beautiful back transition.

> I'm more than sure, that this implementation is not perfect and still
has some bugs (it is still not clear how to handle a case, when you
scroll TextInput off-screen (under keyboard or under header - which back
transition do we need to apply in this case?)). But it resolves some of
the problems that were reported and shows how to use new API of the
library. So in order to unlock a release process I'm leaving this
implementation as is - maybe later I'll come up with more sophisticated
approach which will handle even more cases, but for now as an example
it's good to go.

## 📢 Changelog

### JS
- added documentation for `KeyboardAwareScrollView` describing the flow
of execution;
- removed combination of `useWorkletCallback` + direct `worklet`
directive;
- interpolate transition based
- run additional `scrollTo` in `onEnd` handler to assure that there will
be no overlap with `TextInput` and `Keyboard` - handles a case when
focus changed, but keyboard size was not changed;
- removed `console.log` that were used for debugging 🙂 

## 🤔 How Has This Been Tested?

Tested manually on:
- iPhone 14 Pro;
- Pixel 7 Pro;

## 📸 Screenshots (if appropriate):

|Before|After|
|------|-----|
|<video
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/f9e41c28-0082-4dad-8495-57e48ee97c74">|<video
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/c43d85ce-0cdb-4bc6-b269-895e3e094ad8">|

## 📝 Checklist

- [x] CI successfully passed

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[609b258f59...](https://github.com/TaleStation/TaleStation/commit/609b258f59753bb99155b7836e9ae9e4e5909c23)
#### Wednesday 2023-08-23 09:27:08 by TaleStationBot

[MIRROR] [MDB IGNORE] Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#7376)

Original PR: https://github.com/tgstation/tgstation/pull/77654
-----
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

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f04cff9deb...](https://github.com/TaleStation/TaleStation/commit/f04cff9deba8879724c7d3f8b53dbc261d26702d)
#### Wednesday 2023-08-23 09:27:28 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#7344)

Original PR: https://github.com/tgstation/tgstation/pull/77632
-----
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

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [neovide/neovide](https://github.com/neovide/neovide)@[937decd850...](https://github.com/neovide/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Wednesday 2023-08-23 10:05:50 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[9ccd6ecd74...](https://github.com/PKRoma/Terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Wednesday 2023-08-23 10:30:44 by Mike Griese

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[37d8f6162b...](https://github.com/Ben10Omintrix/tgstation/commit/37d8f6162bbef0c9cbeaf07cdba7cb93eb843e2a)
#### Wednesday 2023-08-23 11:31:09 by LukasBeedellCodestuff

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
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[05e1cac249...](https://github.com/T-J-Teru/binutils-gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Wednesday 2023-08-23 11:38:36 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[34940906e0...](https://github.com/git-for-windows/git/commit/34940906e0b662d07ade74a631445df3f6694aa0)
#### Wednesday 2023-08-23 11:49:59 by Johannes Schindelin

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
## [Git-GoR/Paradise](https://github.com/Git-GoR/Paradise)@[2d10818063...](https://github.com/Git-GoR/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Wednesday 2023-08-23 12:18:00 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[f3fc60ed65...](https://github.com/Warfan1815/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Wednesday 2023-08-23 12:28:13 by morrowwolf

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
## [TheQuinbox/quinoth](https://github.com/TheQuinbox/quinoth)@[d997d91160...](https://github.com/TheQuinbox/quinoth/commit/d997d911607681b08868acb704f21538a0f95549)
#### Wednesday 2023-08-23 13:38:34 by Quin

Hard-code redirect_uris and scopes. I will probably grow to hate myself for this, but this is an internal wrapper, it cleans it up, and external apps can fuck off, this is how it works, for now.

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[c5d6ecad00...](https://github.com/KingDragoness/ProjectHypatios/commit/c5d6ecad008f884d76abd24dd5cdaf1be497b3ce)
#### Wednesday 2023-08-23 13:51:31 by KingDragoness

Hypatios 1.5.6b16 (Liquidator DONE, YESSSSSSSSSSSSSSS)
• MAYBE scrap Fortima and replaces with “Liquidator” for level 7
o Fort War levels now only available through the Sewers level.
• Liquidator floor plans:
o 5 - Penthouse, 4 – Liquidator, 3 – Casino, 2 – Naraka Bar, 1 – Basement
o Penthouse not available currently.
• Naraka Bar bartender NPC
o Dialogue: “Welcome to hell!”, nihilism philosophy driven.
o Robotic arm animation
• Tie materials with subicon
• New subcategory icon: “Cocktails”
o Cocktail is under the branch of alcohol. This needs to be addressed in favourite menu.
• “Interact_NarakaBar_Menu”: buy cocktail and etc.
o List of buttons
o Wait 10 seconds to prepare…
o Two types buyables:
 Alcohols will be added to inventory immediately.
 Cocktails will have to wait 10 seconds. Once done, it will create 3d model of the glass/cup.
• Naraka Bar 3d models:
o Tequila cup model
o More beverage bottles
• Naraka Bar:
o Buy consumables, alcohols, tequilas, alcohol suppressor (monitor menu screen)
o Red themed bar (hell)
 Fireplace, fire, lava
 Stone walls, organic cave structure
• Mining extractor on the basements.
• Replace level 7: “Liquidator” (4th iteration and I want to cry)
o As is the original concept (since march 2022 for fuck sake) and suitable for Hypatios’ sci-fi concept. [See Pinterest concept]
 Blue tint color
o DJ songs, can be set through the Chamber Controller (Mobius UI)
 Liquidator, Maxim, Afiliator, Industrialization, Samsara, Izit
o Enemies: Ultraspider, Mercenary, Seaver, Infernos, Healing bot
o Multiple floors.

---
## [nmacs/shield-linux-kernel](https://github.com/nmacs/shield-linux-kernel)@[75bfb9aff4...](https://github.com/nmacs/shield-linux-kernel/commit/75bfb9aff45e44625260f52a5fd581b92ace3e62)
#### Wednesday 2023-08-23 14:39:07 by Josef Bacik

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
## [archy-bold/not-enough-musk-spambot](https://github.com/archy-bold/not-enough-musk-spambot)@[58dac4888a...](https://github.com/archy-bold/not-enough-musk-spambot/commit/58dac4888a1d3a9043e187ef2e4eccbff207ac7e)
#### Wednesday 2023-08-23 14:48:33 by Simon Archer

💯 Only thing more insane than a nazi is a nazi on meth
I have spaceships
A ground up rewrite is underway that simplifies the X codebase dramatically.
Occasional use of Ketamine is a much better option, in my opinion. I have a prescription for when my brain chemistry sometimes goes super negative.
It makes no sense
Precisely
Although there are some bad things in the world, remember that there are many good things too
𝕏 as humanity’s collective consciousness
Will greatly improve the esthetics.
A trillion dollar market cap for this platform is not out of the question

---
## [nmacs/shield-linux-kernel](https://github.com/nmacs/shield-linux-kernel)@[4d6fa57b4d...](https://github.com/nmacs/shield-linux-kernel/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Wednesday 2023-08-23 14:48:58 by Jason A. Donenfeld

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
## [Shrutibarapatre/Digital-Marketing-task-1](https://github.com/Shrutibarapatre/Digital-Marketing-task-1)@[f486824ef8...](https://github.com/Shrutibarapatre/Digital-Marketing-task-1/commit/f486824ef801bc3afa5b9a432aec5d22287821c3)
#### Wednesday 2023-08-23 15:05:58 by Shrutibarapatre

Add files via upload

🍃 Sip the Essence of Tranquility with Megamalai Briar Tea! 🍵✨

Introducing the epitome of natural goodness – Megamalai Briar Tea! 🌱 Immerse yourself in the serene beauty of the Megamalai hills, where every sip transports you to a world of calm and rejuvenation. 🏞️

🌿 Discover the Magic: Grown amidst lush tea gardens and pristine landscapes, our Briar Tea is handpicked with care, ensuring you get nothing but the finest leaves filled with flavor and health benefits.

🌺 Taste the Elegance: Indulge in a cup of sophistication with every brew. Megamalai Briar Tea boasts a unique blend of robust flavors and delicate aromas that dance on your taste buds.

🌱 Health in Every Sip: Packed with antioxidants and natural goodness, our tea offers a range of health benefits. From boosting your immune system to enhancing mental clarity, it's more than a beverage – it's an investment in your well-being!

☕ Elevate Your Tea Ritual: Whether you're a tea connoisseur or just beginning your journey, Megamalai Briar Tea is here to elevate your tea-drinking experience. It's time to treat yourself to the luxury you deserve.

🌄 Connect with Nature: As you sip on Megamalai Briar Tea, connect with the untouched beauty of nature. Let every cup remind you to take a moment to appreciate the simple joys around us.

Experience the allure of Megamalai Briar Tea today. Elevate your senses, nurture your health, and savor the magic in every sip. ✨🍃

#MegamalaiBriarTea #SipTheMagic #TeaTimeBliss #NatureInACup

---
## [Shrutibarapatre/Digital-Marketing-task-1](https://github.com/Shrutibarapatre/Digital-Marketing-task-1)@[ed7f349ce9...](https://github.com/Shrutibarapatre/Digital-Marketing-task-1/commit/ed7f349ce9094acc07d904e15d1708732e07cb7e)
#### Wednesday 2023-08-23 15:09:09 by Shrutibarapatre

Third Post

✨🍃 Experience Pure Bliss with Briar Megamalai Tea! 🍵✨

🌱 Embrace the Elegance: Step into a world of refinement and exquisite taste with Briar Megamalai Tea. From the heart of the Megamalai hills, we bring you the essence of nature's beauty in every tea leaf.

🍃 Nature's Gift: Our tea is a true gift from Mother Nature herself. Grown amidst pristine landscapes, the tea leaves are nurtured by fresh mountain air and clear, cool waters, resulting in a tea that's pure, unadulterated, and filled with vitality.

☕ Sip & Soothe: Indulge in a cup that's more than just a beverage; it's a moment of tranquility in your busy day. Briar Megamalai Tea's soothing aroma and rich flavor offer a break from the chaos, allowing you to find serenity in every sip.

🌞 Awaken Your Senses: Each cup is an awakening of your senses – from the earthy undertones to the delicate, floral notes, let your palate dance with delight as you savor the Megamalai magic.

🌿 Wellness in Every Brew: Beyond the taste, our tea is packed with antioxidants and natural goodness that nourish your body and mind. Elevate your well-being one cup at a time.

🌄 Share the Magic: Tag a friend who deserves a taste of tranquility in their life. Gift them the experience of Briar Megamalai Tea and spread the love for this exquisite tea.

✨ Brew. Sip. Enjoy. Repeat. ✨

Savor the extraordinary with Briar Megamalai Tea. Elevate your tea ritual, cherish the moment, and let the essence of Megamalai Hills fill your cup and your soul. ☕🍃

#BriarMegamalaiTea #SipTheMagic #NatureInACup #TeaLover #Wellness #SerenityInEverySip

---
## [CommE2E/comm](https://github.com/CommE2E/comm)@[23b508c561...](https://github.com/CommE2E/comm/commit/23b508c561978fb9b36bc3b5c1f8890da1d1cdb7)
#### Wednesday 2023-08-23 16:10:24 by Ginsu Eddy

[native] fix broken messaging experience from forcing incorrect message height measurements

Summary:
A quick and dirty approach to fixing forcing the incorrect height measurements where we revert back to the solution where we measure just the inner message and the inline engagement.

The issue with this solution was that the `RetrySend` component was not visible because I was initially not considering this element when we were forcing the height for composed messages.

However, **we don't need to consider** this element when we are forcing the height. We only need to force the height of the message that is being measured (which is the inner message and the inline engagement). So I believe an alternate solution that could work here is we can place the `RetrySend` component outside of the `View` with the `viewStyle` (see inline comment below for more clarity) so we aren't considering `RetrySend` in the first place when we force the height.

Placing `RetrySend` outside this `View` should be find since in theory an `InlineEngagement` and `RetrySend` should never be rendered at the same time since you can't edit, react, or create a sidebar on a failed local message.

I am aware that with this solution we are losing the benefits of reducing the amount of repeated code and localizing the height-warning logic in the same place that the height-forcing logic is in; however, some of the other solutions that I am exploring are a little more complicated/I need to spend a bit more time testing than I initially expected and I want to get something out soon to unblock native releases asap.

Here is the [[ https://linear.app/comm/issue/ENG-4672/forcing-height-of-whole-message-breaks-timestamp-expansion-experience | Linear exchange ]] where @ashoat and I discuss moving forward with this approach

Depends on D8920

Test Plan:
Tested these flows and confirmed the following with forcing the height measurement

- Rendered the composed messages (text/multimedia) and the messages did not shift like they do when I force an incorrect height
- Rendered the robotext messages and the messages did not shift like they do when I force an incorrect height
- Tested adding/removing reactions
- Tested adding sidebar
- Tested editing
- Tested sending a failed message and confirmed that `RetrySend` was visible
- Tapped on the message and saw that the timestamp is visible
- Tested reply message and everything worked like before
- Tested copy message and everything worked like before
- Tested horizontal message gesture (reply/sidebar) and everything worked like before

{F704435}

Please note that the strange visual behavior with replying and editing messages was already here prior to any changes with the new inline engagement. I figured these issues are outside the scope of the inline engagement project and they should get addressed soon when we build out the new message action bottomsheet/tooltip

EDIT: whoops realized I didn't show Tested sending a failed message and confirmed that `RetrySend` was visible. Here it is:
{F704487}

Reviewers: ashoat, tomek, atul

Reviewed By: ashoat

Subscribers: ashoat, tomek

Differential Revision: https://phab.comm.dev/D8921

---
## [jonathanpeppers/java.interop](https://github.com/jonathanpeppers/java.interop)@[77800dda83...](https://github.com/jonathanpeppers/java.interop/commit/77800dda83c2db4d90b501c00069abc9880caaeb)
#### Wednesday 2023-08-23 16:29:08 by Jonathan Pryor

[Java.Interop.Tools.Expressions] Add Java.Interop.Tools.Expressions (#1046)

Fixes: https://github.com/xamarin/java.interop/issues/616

Context: https://github.com/xamarin/java.interop/issues/14
Context: ff4053cb1e966ebec1c16f97211b9ded936f2707
Context: da5d1b8103bb90f156b93ebac9caa16cfc85764e
Context: 4787e0179b349ab5ee0d0dd03d08b694acea4971
Context: 41ba34856ab119ea6e22ab103320180143fdf03d

Remember `jnimarshalmethod-gen` (176240d2)?  And it's crazy idea to
use the `System.Linq.Expressions`-based custom marshaling
infrastructure (ff4053cb, da5d1b81) to generate JNI marshal methods
at build/packaging time.  And how we had to back burner it because
it depended upon `System.Reflection.Emit` being able to write
assemblies to disk, which is a feature that never made it to .NET Core,
and is still lacking as of .NET 7 (xamarin/java.interop#616)?

Add `src/Java.Interop.Tools.Expressions`, which contains code which
uses Mono.Cecil to compile `Expression<T>` expressions to IL.

Then update `jnimarshalmethod-gen` to use it!

~~ Usage ~~

	% dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp \
	  --jvm /Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home/lib/jli/libjli.dylib \
	  -o _x \
	  -L bin/TestDebug-net7.0 \
	  -L /usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0

First param is assembly to process; `Java.Interop.Export-Tests.dll`
is handy because that's what the `run-test-jnimarshal` target in
`Makefile` processed.

  * `-v -v` is *really* verbose output

  * `--keeptemp` is keep temporary files, in this case
    `_x/Java.Interop.Export-Tests.dll.cecil`.

  * `--jvm PATH` is the path to the JVM library to load+use.

  * `-o DIR` is where to place output files; this will create
    `_x/Java.Interop.Export-Tests.dll`.

  * `-L DIR` adds `DIR` to library resolution paths; this adds
    `bin/TestDebug/net7.0` (dependencies of
    `Java.Interop.Export-Tests.dll`) and
    `Microsoft.NETCore.App/7.0.0-rc.1.22422.12` (net7 libs).

By default the directories containing input assemblies and the
directory containing `System.Private.CoreLib.dll` are part of the
default `-L` list.

When running in-tree, e.g. AzDO pipeline execution, when
`--jvm PATH` isn't specified, `jnimarshalmethod-gen`
will attempt to read the path in `bin/Build*/JdkInfo.props`
a'la `TestJVM` (002dea4a).  This allows an in-place update in
`core-tests.yaml` which does:

	dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp -o bin/TestDebug-net7.0

~~ Using `jnimarshalmethod-gen` output ~~

What does `jnimarshalmethod-gen` *do*?

	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll.orig > beg.il
	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll      > end.il
	% git diff --no-index beg.il end.il
	# https://gist.github.com/jonpryor/b8233444f2e51043732bea922f6afc81

is a ~1KB diff which shows, paraphrasing greatly:

	public partial class ExportTest {
	    partial class '__<$>_jni_marshal_methods' {
	        static IntPtr funcIJavaObject (IntPtr jnienv, IntPtr this) => …
	        // …
	        [JniAddNativeMethodRegistration]
	        static void __RegisterNativeMembers (JniNativeMethodRegistrationArguments args) => …
	    }
	}
	internal delegate long _JniMarshal_PP_L (IntPtr jnienv, IntPtr self);
	// …

wherein `ExportTest._<$>_jni_marshal_methods` and the `_JniMarshal*`
delegate types are added to the assembly.

This also unblocks the desire stated in 4787e017:

> For `Java.Base`, @jonpryor wants to support the custom marshaling
> infrastructure introduced in 77a6bf86.  This would allow types to
> participate in JNI marshal method ("connector method") generation
> *at runtime*, allowing specialization based on the current set of
> types and assemblies.

What can we do with this `jnimarshalmethod-gen` output?  Use it!

First, make sure the tests work:

	# do this *before* running above `dotnet jnimarshalmethod-gen.dll` command…
	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 103 ms - Java.Interop.Export-Tests.dll (net7.0)

Then after running the above `dotnet jnimarshalmethod-gen.dll` command,
re-run the tests:

	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Total tests: 17
	     Passed: 17

`core-tests.yaml` has been updated to do this.

~~ One-Off Tests ~~

One-off tests: ensure that the generated assembly can be decompiled:

	% ikdasm  bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll
	% monodis bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll

	% ikdasm  _x/Java.Interop.Export-Tests.dll
	% monodis _x/Java.Interop.Export-Tests.dll
	# which currently fails :-(

Re-enable most of `Java.Interop.Export-Tests.dll` for .NET 7;
see 41ba3485, which disabled those tests.

To verify the generated IL, use the [dotnet-ilverify][0] tool:

	dotnet tool install --global dotnet-ilverify

Usage of which is "weird":

	$HOME/.dotnet/tools/ilverify bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  --tokens --system-module System.Private.CoreLib \
	  -r 'bin/TestDebug-net7.0/*.dll' \
	  -r '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0/*.dll'
	All Classes and Methods in /Volumes/Xamarin-Work/src/xamarin/Java.Interop/_x/Java.Interop.Export-Tests.dll Verified.
	# no errors!

where:

  * `--tokens`: Include metadata tokens in error messages.
  * `--system-module NAME`: set the "System module name".  Defaults
    to `mscorlib`, which is wrong for .NET 5+, so this must be set to
    `System.Private.CoreLib` (no `.dll` suffix!).
  * `-r FILE-GLOB`: Where to resolve assembly references for the
    input assembly.  Fortunately file globs are supported…

~~ Removing `System.Private.CoreLib` ~~

`System.Private.CoreLib.dll` is *private*; it's not part of the
public assembly surface area, so you can't use
`csc -r:System.Private.CoreLib …` and expect it to work.  This makes
things interesting because *at runtime* everything "important" is in
`System.Private.CoreLib.dll`, like `System.Object`.

Specifically, if we do the "obvious" thing and do:

	newTypeDefinition.BaseType = assemblyDefinition.MainModule
	    .ImportReference (typeof (object));

you're gonna have a bad type, because the resulting IL for
`newTypeDefinition` will have a base class of
`[System.Private.CoreLib]System.Object`, which isn't usable.

Fix this by:

 1. Writing the assembly to a `Stream`.
 2. Reading the `Stream` from (1)
 3. Fixing all member references and assembly references so that
    `System.Private.CoreLib` is not referenced.

If `jnimarshalmethod-gen.dll --keeptemp` is used, then a `.cecil`
file is created with the contents of (1).

Additionally, and unexpectedly -- [jbevain/cecil#895][1] -- Mono.Cecil
adds a reference to the assembly being modified.  Remove the declaring
assembly from `AssemblyReferences`.

[0]: https://www.nuget.org/packages/dotnet-ilverify
[1]: https://github.com/jbevain/cecil/issues/895

---
## [PelicanPlatform/pelican](https://github.com/PelicanPlatform/pelican)@[bc56423c42...](https://github.com/PelicanPlatform/pelican/commit/bc56423c4210dfa1e9a480bf5e449edd1acbc000)
#### Wednesday 2023-08-23 16:29:48 by Justin Hiemstra

Local lint & Director CLI hookup + bug fixes

PR #7 introduced a framework for including the Director in the Pelican CLI,
toward making all Pelican services available under a single binary. This commit
extends that PR to hook the Director package up to the CLI, the Pelican's
configuration mechanisms, and to actually sort out a few bugs related to the
untested director code.

It should be noted that there are currently a few hacks in the code that need
clearing up before any merge, but as of now the commit makes the following
possible:
`pelican director serve --cache-port 8000`
This will serve the Director's cache-redirection service on port 8000 using a gin
engine. When we've figured out how to handle Origin redirects and implemented an
origin-redirect service, we'll be able to do:
`pelican director serve --cache-port 8000 --origin-port 8001`
to split apart the two endpoints.

As for the local lint... I'm still trying to figure out how to shut that feature
off in my editor. Sorry for the noise!

---
## [iamtushsharma/UBREAKABLE_FOG](https://github.com/iamtushsharma/UBREAKABLE_FOG)@[c82d766680...](https://github.com/iamtushsharma/UBREAKABLE_FOG/commit/c82d7666801acf3b4145b7a5f403198f070d087f)
#### Wednesday 2023-08-23 16:49:08 by iamtushsharma

Sales Analysis

Excited to share my latest project  using Power BI! 🚀. 

Power BI is truly a game-changer in the world of data analysis, offering a powerful and interactive machine that turns raw data into meaningful insights. 📈🔍

In this project, I embarked on a fascinating journey through various operations:
1⃣ Data Gathering 📊: I collected data from diverse sources to ensure a comprehensive understanding of the subject.
2⃣ Data Cleaning 🧹: A crucial step to ensure accurate and reliable results, I meticulously cleaned the data to eliminate any inconsistencies or errors.
3⃣ Data Transformation 🔄: Transforming data is where the magic happens! I leveraged Power BI's capabilities to reshape and structure the data for optimal analysis.
4⃣ Data Visualization 📊: Visualizing data is an art, and Power BI provides an incredible canvas. I crafted stunning visuals that bring insights to life, making complex information easily digestible.
5⃣ Sharing Insights 📢: Collaboration is key, and I used Power BI to share my findings, empowering stakeholders with actionable insights.

I invite you all to explore my Power BI project and provide your invaluable insights. Your feedback is instrumental in refining my work and enhancing the effectiveness of my ideas. Let's continue to learn and grow together! 💡🤝 #powerbi #powerbidashboard #analytics #dataanalysis #insights #continuousimprovement

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6f6b05868d...](https://github.com/treckstar/yolo-octo-hipster/commit/6f6b05868d62e750bb18b68eaf2370fe3005c4ea)
#### Wednesday 2023-08-23 17:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [MikeKuwait/cmss13](https://github.com/MikeKuwait/cmss13)@[1ea79a2ed8...](https://github.com/MikeKuwait/cmss13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Wednesday 2023-08-23 17:25:05 by Ben

Zombie Rework (#4060)

# About the pull request

The goal for this PR is to rework zombies into being a fast and
numerous, but weaker, entity. As it stands a zombie has too many
advantages where a hold against them is essentially a fool's errand.

CURRENT PLAN (Will adjust as needed)
Zombies will be FASTER but much weaker than current iteration, with
weaker attacks. They will be designed around being a foe that can be
taken down quicker but if they close the distance, the threat of
infection spells a death sentence.

# Explain why it's good for the game

This will be hard to balance, and as such will be taking feedback before
I submit this for review. This is current position of Zombies:

- Tough: Extreme (25% ?!) brute modifier, with fire modifier on top,
making them very tanky and requiring clips to take down one
- self-revive: They WILL come back up, coupled with toughness, they are
a feared opponent.
- Strength: Claws inflict superslow at 40 brute damage, one of the
highest damage levels.
- Numerous: They have the numbers to put lesser drones and even entire
hives to shame

Overall, they are very overtuned and makes playing against them not that
fun. My plan is to have it so they are much weaker, with their threat
being from infections.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Zombie attacks deal less damage and only slow down targets (not
superslow as they currently do)
balance: Zombie resistances have been reduced heavily, making them far
more susceptible to brute damage. Their speed has been doubled to
compensate
balance: Black goo on tiles now requires you to not wear shoes to have
chance for infection
fix: Zombie attacks now only apply effects such as slow and infection if
the attack is valid (if the zombie is able to attack)
/:cl:

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[6f81efeb82...](https://github.com/i3roly/glibc_ddwrt/commit/6f81efeb829ab0b64dd771df1c6ac830241089f8)
#### Wednesday 2023-08-23 17:41:07 by gagan sidhu

[4.14.323/v53418] update glibc(2.38) and kernel(4.14.323)

- note hopefully this fixes the issue with no wifi interfaces.

- i updated glibc because these guys decided to add strlcpy and strlcat.
  so then i made the choice to recompile anything that used these
  functions (from libbsd). so a lot of stuff that was linked to libbsd
  is now linked without it (except frr because i forgot)

-  kernel 6.1 seems like a no go. it's too big. i could remove tcpdump
   but the problem is it's still going to be a tight fit, and i'd have
   to probably remove other things. i don't know. plus i've lost the
   appetite to update the kernel after linux kernel devs decided they're
   bigger than gLIBC with their 64 bit time crap.
        -now if you build glibc for kernels 5.0 and newer, there will
        probably be userspace breakage for any programs compiled on
        earlier versions, which defeats the entire principle of glibc.

        -so since the linux development team thinks they're bigger than
        the library that makes them, i don't think i should invest any
        more time in trying to stay up to date.

i've had a top build for over 4 years as of this september,
        - with all the buttons working, and the LEDs.
        - if that support fizzles out in the next year or two, i don't
        think it'll be a bad thing.
                -in fact, i thought this update may be pointless, since
                the previous build seems great.
                        -BUT since some of you guys just love to update
                        your stuff, i decided to spin the build anyways.

i was busy taking over the "redneck swap" so that's why i also haven't
updated. anyways i'm getting bored because i've done too many things and
mitt STILL think he's "the math guy" with "the business sense". i
haven't seen mitt do a fraction of what i have. all i've seen mitt do is
hold a picket sign SUPPORTING the vietnam war

https://www.nytimes.com/2012/09/12/us/politics/at-stanford-romney-stood-ground-on-vietnam.html

and his followers think he's the "Mormon John Lennon"

cool world--sorry, i mean GLOBAL ECKANAMY, bro.

P.S. I DID NOT TEST THIS BUILD BUT I DON'T SEE WHY IT WOULDN'T WORK. i
am at 41 days uptime and i'm trying to keep ti going.

---
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[b0ec1e4098...](https://github.com/Rustybuckets6601/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Wednesday 2023-08-23 17:58:58 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0dd3e66aef...](https://github.com/tgstation/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Wednesday 2023-08-23 18:06:55 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[f08ce907dd...](https://github.com/Nerev4r/Skyrat-tg/commit/f08ce907ddc90398f56e449a2dc29e1d1ea22278)
#### Wednesday 2023-08-23 18:08:21 by SkyratBot

[MIRROR] Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome [MDB IGNORE] (#23012)

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

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

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [bulentcoskun/guava](https://github.com/bulentcoskun/guava)@[8a676ade61...](https://github.com/bulentcoskun/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Wednesday 2023-08-23 18:35:16 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [uebelack/briefe.app](https://github.com/uebelack/briefe.app)@[8485bd9528...](https://github.com/uebelack/briefe.app/commit/8485bd95289820499a67cd5b292764e027981300)
#### Wednesday 2023-08-23 18:38:25 by David Uebelacker

:tada: Keep in mind always the four constant Laws of Frisbee:
	(1) The most powerful force in the world is that of a disc
	   straining to land under a car, just out of reach (this
	   force is technically termed "car suck").
	(2) Never precede any maneuver by a comment more predictive
	   than "Watch this!"
	(3) The probability of a Frisbee hitting something is directly
	   proportional to the cost of hitting it.  For instance, a
	   Frisbee will always head directly towards a policeman or
	   a little old lady rather than the beat up Chevy.
	(4) Your best throw happens when no one is watching; when the
	   cute girl you've been trying to impress is watching, the
	   Frisbee will invariably bounce out of your hand or hit you
	   in the head and knock you silly.

---
## [gameur-5500/Infinite-Apps](https://github.com/gameur-5500/Infinite-Apps)@[3ad74e53b5...](https://github.com/gameur-5500/Infinite-Apps/commit/3ad74e53b525150510685640a05c053b0292329b)
#### Wednesday 2023-08-23 18:46:57 by ErrSys

Big update!

+ Custom welcome message: welcome message will now depend on the time if its the morning it'll say Good Morning if its the afternoon or the evening it'll say Have a good day and if its the night it'll say Good night!
+ Clicking on infinite apps logo now redirect you to the welcome page!
+ Removed custom fav icons!
+ Updated main.css:
- Fixed a visual bug with responsive menu!
+ Renamed some functions and variables in AppLoading.js and NavMenu.js!

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[d4074241c1...](https://github.com/sqnztb/Skyrat-tg/commit/d4074241c1677b3baee2cd3f925e05173c9c7d59)
#### Wednesday 2023-08-23 18:50:42 by SkyratBot

[MIRROR] convert the eyeball a basic monster [MDB IGNORE] (#23043)

* convert the eyeball a basic monster (#77411)

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

* convert the eyeball a basic monster

---------

Co-authored-by: Ben10Omintrix <138636438+Ben10Omintrix@users.noreply.github.com>

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[94c3d31fab...](https://github.com/sqnztb/Skyrat-tg/commit/94c3d31fabb9d64c9f71d1ef6635fcd3856c5019)
#### Wednesday 2023-08-23 18:50:42 by SkyratBot

[MIRROR] Refactors Morphs into Basic Mobs (there is now a swag action for morphification) [MDB IGNORE] (#23046)

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

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

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Dangerlurking/sojourn-station](https://github.com/Dangerlurking/sojourn-station)@[1895bd5c51...](https://github.com/Dangerlurking/sojourn-station/commit/1895bd5c511012ac1978d52aea8f6810a90fcf08)
#### Wednesday 2023-08-23 19:13:02 by CDB

Im so sick of bugs. (#4739)

* Mother fucker. Im so sick of bugs.

Cigarettes no longer(seem to) cause kidney damage to people with unclean living.

psion void armor has correct slowdown for shoes and doesn't use slowdown on other pieces of armor. Additionally, no longer allows ears to flop outside of it. It's a fucking space suit, why would they be out?

Opifex medbelt no longer selectable, sorry powergamers.

Removes change_appearance from baseline armor vest. Why? It is the parent to MANY MANY MANY fucking items and thus caused MANY MANY MANY items to have erronious change_appearance procs that only had two options for the base parent item. This is why we don't put fucking procs on BASE PARENT items that affect DOZENS of other items. Fixes a few others, WO plate has no unique sprite and now has a proper working change appearance. CO does have a unique sprite, it is gone.

Fixes #4732
Fixes #4734
fixes #4724

* Update psi_Larmor.dm

---
## [Dobsgw/kernel_xiaomi_sm8250-n0](https://github.com/Dobsgw/kernel_xiaomi_sm8250-n0)@[efc24fba1b...](https://github.com/Dobsgw/kernel_xiaomi_sm8250-n0/commit/efc24fba1b039210f786cfe7f2fa1e7ffe94fdba)
#### Wednesday 2023-08-23 19:24:03 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[d1f3ee55e6...](https://github.com/norbert-acedanski/supernatural-guide/commit/d1f3ee55e63dd5b2def45ab1dd35a83cd4eae13f)
#### Wednesday 2023-08-23 19:32:48 by Norbert Acedanski

Add Demon, Witch, Angel, Fallen Angel, Prophet, Archangel Lucifer, Demon Crowley appearances.
Update GOD description, add disable method.
Add Darkness clues and disable methods.
S11E22

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[a2ee4ec813...](https://github.com/lizardqueenlexi/orbstation/commit/a2ee4ec813c38741d593e5e1731764458c77b811)
#### Wednesday 2023-08-23 19:52:06 by Jacquerel

Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

---
## [makesoftwaresafe/libbpf](https://github.com/makesoftwaresafe/libbpf)@[b064c40d94...](https://github.com/makesoftwaresafe/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Wednesday 2023-08-23 20:14:09 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [makesoftwaresafe/libbpf](https://github.com/makesoftwaresafe/libbpf)@[d7e583a6ea...](https://github.com/makesoftwaresafe/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Wednesday 2023-08-23 20:14:09 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [nstester/gcc](https://github.com/nstester/gcc)@[6619b3d4c1...](https://github.com/nstester/gcc/commit/6619b3d4c15cd754798b1048c67f3806bbcc2e6d)
#### Wednesday 2023-08-23 20:15:05 by Jivan Hakobyan

Improve quality of code from LRA register elimination

This is primarily Jivan's work, I'm mostly responsible for the write-up and
coordinating with Vlad on a few questions.

On targets with limitations on immediates usable in arithmetic instructions,
LRA's register elimination phase can construct fairly poor code.

This example (from the GCC testsuite) illustrates the problem well.

int  consume (void *);
int foo (void) {
  int x[1000000];
  return consume (x + 1000);
}

If you compile on riscv64-linux-gnu with "-O2 -march=rv64gc -mabi=lp64d", then
you'll get this code (up to the call to consume()).

        .cfi_startproc
        li      t0,-4001792
        li      a0,-3997696
        li      a5,4001792
        addi    sp,sp,-16
        .cfi_def_cfa_offset 16
        addi    t0,t0,1792
        addi    a0,a0,1696
        addi    a5,a5,-1792
        sd      ra,8(sp)
        add     a5,a5,a0
        add     sp,sp,t0
        .cfi_def_cfa_offset 4000016
        .cfi_offset 1, -8
        add     a0,a5,sp
        call    consume

Of particular interest is the value in a0 when we call consume. We compute that
horribly inefficiently.   If we back-substitute from the final assignment to a0
we get...

a0 = a5 + sp
a0 = a5 + (sp + t0)
a0 = (a5 + a0) + (sp + t0)
a0 = ((a5 - 1792) + a0) + (sp + t0)
a0 = ((a5 - 1792) + (a0 + 1696)) + (sp + t0)
a0 = ((a5 - 1792) + (a0 + 1696)) + (sp + (t0 + 1792))
a0 = (a5 + (a0 + 1696)) + (sp + t0)  // removed offsetting terms
a0 = (a5 + (a0 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (a0 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (-3997696 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (-3997696 + 1696)) + ((sp - 16) + -4001792)
a0 = (-3997696 + 1696) + (sp -16) // removed offsetting terms
a0 = sp - 3990616

That's a pretty convoluted way to compute sp - 3990616.

Something like this would be notably better (not great, but we need both the
stack adjustment and the address of the object to pass to consume):

   addi sp,sp,-16
   sd ra,8(sp)
   li t0,-4001792
   addi t0,t0,1792
   add sp,sp,t0
   li a0,4096
   addi a0,a0,-96
   add a0,sp,a0
   call consume

The problem is LRA's elimination code is not handling the case where we have
(plus (reg1) (reg2) where reg1 is an eliminable register and reg2 has a known
equivalency, particularly a constant.

If we can determine that reg2 is equivalent to a constant and treat (plus
(reg1) (reg2)) in the same way we'd treat (plus (reg1) (const_int)) then we can
get the desired code.

This eliminates about 19b instructions, or roughly 1% for deepsjeng on rv64.
There are improvements elsewhere, but they're relatively small.  This may
ultimately lessen the value of Manolis's fold-mem-offsets patch.  So we'll have
to evaluate that again once he posts a new version.

Bootstrapped and regression tested on x86_64 as well as bootstrapped on rv64.
Earlier versions have been tested against spec2017.  Pre-approved by Vlad in a
private email conversation (thanks Vlad!).

Committed to the trunk,

gcc/
	* lra-eliminations.cc (eliminate_regs_in_insn): Use equivalences to
	to help simplify code further.

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[afb791ca88...](https://github.com/Monkestation/Monkestation2.0/commit/afb791ca88904597f332a8efdd7a151e532f3237)
#### Wednesday 2023-08-23 20:53:30 by Jacquerel

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
## [ray2301/spot-on](https://github.com/ray2301/spot-on)@[f863b2facc...](https://github.com/ray2301/spot-on/commit/f863b2facc4f8a61ec5a37f95159e5b108219067)
#### Wednesday 2023-08-23 20:59:23 by ray2301

Update downloader.py

'''
    Module for downloading tracks based on list[Track] and swapping metadata after processing

    batch_download - download multiple tracks, precise search or not
    download_track - casual track download that relies on first youtube search result
    precise_download - filters by duration and chooses closest one
'''

import os
import spoton.structs as structs
import yt_dlp
import music_tag
import requests
from fuzzywuzzy import fuzz
from unidecode import unidecode
import re
import concurrent.futures as cf

class Downloader:
    def __init__(self, download_path: str, workers: int):
        self.ytdlp_options = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }],
            'quiet': True,
            'nooverwrites': True,
            'noprogress': False,
        }

        #structure for saving album covers as album_name: imgpath
        self.album_covers = {}
        self.download_path = f'{download_path}'
        self.__create_dir(download_path)

        self.pool = cf.ThreadPoolExecutor(max_workers=workers)



    def batch_download(self, tracks: list[structs.Track], precise=False):
        download_func = self.download_track
        if precise:
            download_func = self.precise_download

        for i in tracks:
            self.pool.submit(download_func, i)

        self.pool.shutdown(wait=True)
        self.__cleanup()

    def download_track(self, track: structs.Track):
        artists = ", ".join(track.track_artists).replace('?', '').replace('!', '').replace('"', '').replace('/', '_').replace(':', '_').replace('*', '_').replace('|', '_')
        track_name = track.track_name.replace('.', '_').replace('/', '_').replace('"', '_').replace('?', '_').replace('!', '_').replace(':', '_').replace('*', '_').replace('|', '_')
        request_query = f'{artists} - {track_name} Provided to YouTube by audio'

        savepath = os.path.join(self.download_path, f"{', '.join(track.track_artists)} - {track_name}")

        if not self.__file_exists(savepath + '.m4a'):
            ytdlp_options = self.ytdlp_options.copy()
            ytdlp_options['outtmpl'] = savepath
            with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
                ydl.download([request_query])
            self.__change_metadata(savepath, track)
        else:
            print(f"Skipped {track.track_name}, already downloaded.")

    @staticmethod
    def remove_remaster_addon(track_title):
        # Regular expression pattern to match " - year Remaster" add-on
        remaster_pattern = r'\s-\s\d{4}\sRemaster$'
        
        # Remove the remaster add-on from the track title
        track_title_cleaned = re.sub(remaster_pattern, '', track_title)
        
        return track_title_cleaned, track_title

    def precise_download(self, track: structs.Track):
        artists = ", ".join(track.track_artists).replace('?', '').replace('!', '').replace('"', '').replace('/', ' - ').replace(':', ' - ').replace('*', '').replace('|', '_')
        track_name = track.track_name.replace('.', '').replace('/', ' - ').replace('"', '').replace('?', '').replace('!', '').replace(':', ' - ').replace('*', '').replace('|', '_')
        
        # Remove the " - year Remaster" add-on from the track title
        track_name_cleaned, original_track_name = self.remove_remaster_addon(track_name)
        
        request_query = f'{artists} - {track_name_cleaned} Auto-generated by YouTube'

        print(f"\033[1;32mSearching for: {request_query.replace(' Auto-generated by YouTube', '')}\033[0m")

        # List of filter phrases and words
        filter_list = ["live", "Lyrics", "acoustic", "remix", "instrumental", "karaoke", "mix", "vinyl", "in the style of", "harry styles cover", "made famous by", "8-bit", "jazz all stars", "sped up", "origonally performed", "tritube to", "hits remix",
                   "cover", "piano", "original by", "studio allstars", "tribute to", "tribute band", "santanarama", "project", "tribute", "made popular by", "16-bit",
                   "acoustic covers", "acoustic cover", "orchestra", "dj adam", "tribute", "barry white experience", "twinkle twinkle little rock star", "lullaby version",
                   "guitar tribute", "smooth jazz all stars", "soundtrack wonder band", "string quartet", "mardi gras", "piano acoustic", "susan may","pop music workshop", "performed by", "top hit",
                   "pancadão gd som", "originally by", "remake", "the cover girl", "slowgrind re-mixers", "michael marc", "instrumental unplugged", "cover hits", "versiones", "various artists",
                   "white knight instrumental", "the bohemian champions", "spencer group", "piano dreamers", "instrumental version", "in the syle of", "electric dust", "mc chill baby",
                   "dj top gun", "medley", " remix cover", "djomla ks", "acoustic hits", "unknown artist", "piano version", "piano company", "the film band",
                   "rock the cradle", "the cat and owl", "kings of acoustra", "the crazy diamonds", "party allstars", "revival band", "sweet little band", "song masters",
                   "famous flames", "baby lullabies", "chillout lounge", "judson mancebo", "brothers group", "rowdy heart music", "u.s.a. classics", "full remix", "bawello",
                   "mobile melody", "live 2022", "live 2023", "live 2021", "live 2020", "in the style of", "acoustic vibes", "artisti vari", "phantombeatsamr", "asmr", "rossella ferrari",
                   "studio sound group", "asara", "banana hut", "emeraude claire", " deep sleep hypnosis", "originally performed", "remix now", "dance guru", "fitness version",
                   "radio flyer", "recovered band", "mixed", "417Hz", "Karaoké", "chords"]

        # Create a regex pattern for matching the filter words
        filter_pattern = r'\b(?:' + '|'.join(filter_list) + r')\b|\(|\)'

        ytdlp_options = self.ytdlp_options.copy()
        ytdlp_options['default_search'] = 'ytsearch7'

        duration_s = track.duration_ms // 1000

        with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
            info = ydl.extract_info(request_query, download=False)

            if not info:
                raise Exception(f'Failed to extract data for {track_name}')
            else:
                entries = info['entries']
                best_match = None
                fuzzy_results = []

                for entry in entries:
                    youtube_duration = entry.get('duration', 0)  # Duration in seconds
                    duration_diff = abs(youtube_duration - duration_s)

                    # Check if the difference in durations is within the allowed threshold (9 seconds)
                    if duration_diff <= 9 and youtube_duration <= duration_s + 9:
                        title = entry.get('title', '').lower()  # Get lowercase title for comparison

                        # Create a translation table to replace characters
                        translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")

                        # Transliterate the title to ASCII characters and apply replacements
                        title_translated = title.translate(translation_table)
                        title_ascii = unidecode(title_translated)

                        # Transliterate the track name to ASCII characters and apply replacements
                        track_name_translated = track_name.translate(translation_table)
                        track_name_ascii = unidecode(track_name_translated)

                        # Perform fuzzy matching with the ASCII versions of title and track name
                        title_similarity = fuzz.partial_ratio(track_name_ascii.lower(), title_ascii)

                        # Check if the title similarity score is above a certain threshold (e.g., 80%)
                        if title_similarity >= 85:
                            title_matches = re.search(filter_pattern, title_ascii)
                            # Check if the title contains filter words not in the search term
                            if title_matches and not any(filter_word in track_name.lower() for filter_word in filter_list):
                                continue  # Skip this entry if it matches the filter and the search term doesn't contain the filter word

                            fuzzy_results.append((title, title_similarity))
                            best_match = entry

                # Print all the fuzzy matching results
                print("\033[1;32mFuzzy Matching Results:\033[0m")
                for result_title, result_similarity in fuzzy_results:
                    print(f"Title: {result_title}, Fuzzy Match Percentage: {result_similarity}%")

        ytdlp_options['default_search'] = 'auto'

        if best_match:
            url = best_match['webpage_url']
            print(f"\033[1;32mURL: {url}\033[0m")
            chosen_video_title = best_match.get('title', 'Unknown Title')

            # Create a list to store the tracks with exact title and length matches
            exact_matches = []

            for result_title, result_similarity in fuzzy_results:
                if result_similarity >= 85 and result_title == chosen_video_title:
                    youtube_duration = best_match.get('duration', 0)
                    duration_diff = abs(youtube_duration - duration_s)

                    # Check for exact length match or up to 9 seconds difference
                    if duration_diff <= 9:
                        exact_matches.append((result_title, result_similarity, duration_diff))
            
            if exact_matches:
                # Sort the exact_matches list by duration difference
                exact_matches.sort(key=lambda x: x[2])
                
                # Choose the track with the lowest duration difference
                chosen_video_title, chosen_fuzzy_match_percentage, chosen_fuzzy_duration_diff = exact_matches[0]

                print(f"\033[1;32mChosen: \033[0m\033[1;33m{chosen_video_title}\033[0m\033[1;32m, Track Similarity: \033[0m\033[1;32m{chosen_fuzzy_match_percentage}%, Length Difference: {chosen_fuzzy_duration_diff} seconds\033[0m")

            else:  # If there are no exact matches
                # Calculate the difference in track durations
                chosen_youtube_duration = best_match.get('duration', 0)
                chosen_fuzzy_duration_diff = abs(chosen_youtube_duration - duration_s)
                print(f"\033[1;32mChosen: \033[0m\033[1;33m{chosen_video_title}\033[0m\033[1;32m, Track Similarity: \033[0m\033[1;32m{result_similarity}%\033[0m, Length Difference: \033[1;32m{chosen_fuzzy_duration_diff} seconds\033[0m")

            savepath = os.path.join(self.download_path, f"{artists} - {track_name}")
            if not self.__file_exists(savepath + '.m4a'):
                ytdlp_options['outtmpl'] = savepath
                with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
                    ydl.download([url])
                self.__change_metadata(savepath, track)
                print(f"\033[1;32mDownloading {track_name}...\033[0m")
            else:
                print(f"\033[1;36mSkipped {track_name}, already downloaded.\033[0m")
        else:
            print(f"\033[1;31mNo suitable track found for {track_name}. Skipping download.\033[0m")


    def __change_metadata(self, audio_path: str, track: structs.Track):
        imgpath = self.__get_album_image(track)
        f = music_tag.load_file(audio_path + '.m4a')

        if not f:
            raise Exception(f'Failed to change metadata for {track.track_name} at {audio_path}')
        else:

            f['artist'] = ', '.join(track.track_artists)
            f['album'] = track.album_name
            f['albumartist'] = ', '.join(track.album_artists)
            f['title'] = track.track_name  # Use the modified track name for tagging
            if imgpath:
                with open(imgpath, 'rb') as imgf:
                    f['artwork'] = imgf.read()
            else:
                raise Exception(f'Failed to set album cover for {track.track_name}')
            
            if track.disk_number:
                f['discnumber'] = track.disk_number
            if track.track_number:
                f['tracknumber'] = track.track_number
            if track.total_tracks:
                f['year'] = release_year

            f.save()

            # Cleanup: Remove the album cover image file
            if imgpath:
                os.remove(imgpath)  # This line was added for cleanup


    def __get_album_image(self, track: structs.Track) -> str:
        sanitized_album_name = track.album_name.replace('.', '').replace('/', ' - ').replace('"', '').replace('?', '').replace('!', '').replace(':', ' - ').replace('*', '').replace('|', '_')

        filename = f'{sanitized_album_name}'
        resp = requests.get(track.image_url)
        imgpath = os.path.join(self.download_path, filename) + '.jpg'

        if resp.status_code == 200:
            with open(imgpath, 'wb') as f:
                f.write(resp.content)
        else:
            raise(Exception(f'Failed to download cover image for {track.track_name}'))

        self.album_covers[track.album_name] = imgpath

        return self.album_covers[track.album_name]


    def __file_exists(self, filepath: str) -> bool:
        return os.path.exists(filepath)


    def __cleanup(self):
        for i in self.album_covers:
            os.remove(self.album_covers[i])
        self.album_covers = {}

    def __create_dir(self, path: str):
        if not os.path.exists(f'{path}'):
            os.mkdir(f'{path}')

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[a8e3003ef6...](https://github.com/KenAdeniji/WordEngineering/commit/a8e3003ef60629b08964c5aa292fc295a655563a)
#### Wednesday 2023-08-23 21:43:29 by Ken Adeniji

2023-08-23T13:44:00 ... 2023-08-23T14:29:00 http://github.com/KenAdeniji/WordEngineering/blob/main/IIS/WordEngineering/2018-05-03Correspondence/2023-08-23T1344CarrieStanulov_carrie@180engineering.com_Database_OurStrengthOurNumbers_TiesAreUnchange.txt Carrie Stanulov 180engineering mailto:carrie@180engineering.com Telephone: (312) 882-9323 4300 Commerce Court Suite 315 Lisle, Illinois (IL) 60532 United States of America (USA) http://calendly.com/carrie180/20min Ken Adeniji 4762 Canvasback Common Fremont, California (CA) 94555 United States of America (USA) +1 (510) 796-8121 mailto:KenAdeniji@hotmail.com http://kenadeniji.wordpress.com http://kenadeniji.wordpress.com/2015/11/20/ken-adenijis-resume http://kenadeniji.wordpress.com/2015/12/06/2015-10-23doctoraldissertation 2023-08-23T09:00:00 ... 2023-08-23T09:11:00 Interview. Database. 2023-08-23T11:20:00 Our strength ... our numbers. PGA Tour Superstore. 4990 Dublin Boulevard. Dublin, California (CA) 94568. 2023-08-23T12:00:00 Ties are unchange. Departed from Dublin/Pleasanton BART Station. Arriving at Bay Fair BART Station. A Caucasian male and 2 Caucasian females were talking. Orange equipment with black lettering 4*4 written to the East. 2023-08-23T09:00:00 ... 2023-08-23T09:11:00 Illinois Tool Works (ITW). Chicago, Illinois (IL). 2023-08-22T13:54:00 Every e-mail, I receive ... store in my database. 2023-08-22T13:47:00 The ability ... to save and cost a life. 2023-08-22T13:51:00 20 Minute Introduction Meeting 9:00am - 9:30am, Wednesday, August 23, 2023 Pacific Time - US & Canada +1 510-796-8121 A calendar invitation has been sent to your email address. Simple. Automated. Scheduling. We're seeking a Sr. Software Developer with C#, C++, and SQL experience for the design and development of applications for automated cutting and assembly machinery in the Dallas/ Fort Worth Area!! Pay Rate: $90-$150K DOE Hybrid FTE: Requires 3 days On-Site Relocation Approved Travel: 10% to FL site occasionally Must haves: -Bachelor’s degree in Computer Science or related. -6+ years of software development experience -Proficiency in C# and C++ -Proficiency in SQL -Strong experience in Agile/Scrum environments -Prefer experience with applications for products with moving parts, machinery, etc. -Prefer experience with Angular, but can train. Email Resume to carrie@180engineering.com Do you have availability to jump on a call with me this week? Sign onto Calendly to find a date/ time that works best for you! https://calendly.com/carrie180/20min Regards, Carrie Stanulov – Senior Recruiting Specialist (E) carrie@180engineering.com (P) 312-882-9323 (A) 4300 Commerce Ct. Suite 315 | Lisle, IL 60532 Sr. Software Developer

---
## [adump1v/platform_frameworks_base](https://github.com/adump1v/platform_frameworks_base)@[282a1c1332...](https://github.com/adump1v/platform_frameworks_base/commit/282a1c133245b78512ee15abe0aad2b713a42c7c)
#### Wednesday 2023-08-23 23:35:02 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [wintrsatoru/anoop](https://github.com/wintrsatoru/anoop)@[d3181372c8...](https://github.com/wintrsatoru/anoop/commit/d3181372c8798455e9ee5014205ca566eb29cab9)
#### Wednesday 2023-08-23 23:46:42 by Andre

The Rizzler Rizzly bear The boy who cried rizz Abraham Rizzcoln Adolf Rizzler Rizzy Neutron A degree in quantum rizzics Barrack Rizzbama Need a rizztraining order Anakin RizzWalker Rizzard of Oz Lord of the Rizz Performed a rizzerruction Rizzosaurus Rex From the village hidden in the rizz Offering rizztituation and rizzarations Glenn Rizzmire Rizz Khalifa Martin Luther Rizz Kamala Harizz Rizzy Hendrix/ Jimi Hendrizz Rizzilicious Rizziliguous Rizziologist Rizzillionaire Rizz Ranger The Rizz reaper Leader of the rizzistance Chrizz Brown Rizzdolph the Rizz-Nosed Reindeer Wolverizz Head coch of the Memphis Rizzlies Prisoner of Rizzkaban Rizzaholic Rizza Parks Rizz Hemsworth Albert Rizzenstein Playing Rizzident Evil Mike Rizzowski Franklin D Rizzevelt Queen Erizzabeth Kyle Rizzenhouse Walt Rizzney Signed the declaration of rizzdependence From the state of Rizzouri Rizz Al Ghul Corona Virizz Rizztafarian Rizzie Smalls R(izz) Kelly Rizzil War Veteran Rizz and Morty Gerald of Rizzia Alvin and the Rizzmunks Otto Von Rizzmark The last Rizzort Got a ticket for the polar rizzpress/ exprizz Artirizzal Intelligence Natural Rizzastar First Rizzponder Member of the nation of Rizzlam Crizztiano Rizzaldo Rizzaldinho The Grand rizzard Ghost of Rizzmiss Past 13 rizzons why Are the rizz rizz fruit One of the three Rizzmirals 7 Rizzlords of the sea Qualified for rizzlemaina Sent to prizzon George Rizzington Theodore Rizzevelt The little boy from Rizzario Plays for Real Madrizz The last rizzbender Found the derizzative of the function Lando Cal- rizz- ian Aurizztic/ Diagnosed with Aurizzim Jack the rizzer Grew up in Rizzadelphia Rizzatron Dwayne the Rizz Johnson Master of the Rizzic Arts Osama Rizz Laden Frosty the rizzman The rizziah Fell into the economic rizzession Rizzas in Paris Chuck Norizz Sir Rizz- a- lot Rules the Rizzatine Empire Rizzioactive Cooking Rizzatouille Forizz Gump A Diet sometimes involves Blue Rizzberries The nightmare before Rizzmas Rizzeree Damian Rizzard In the Marvel rizzamatic universe Undergoing Celluar rizzpiration Plagiarizzim Thesaurizz Rizzmas Tree Rizzmas Present Rizzimus Prime/ Optirizz Prime Cardiopulmonary rizzuscitation Be Generizz to that person Charizzard Isaac Rizzton Little Rizz Rizzing Hood Arnold Schwarzenrizzer Rizz Archives Rizz in peace Elvis Rizzley Cloudy with a Chance of Rizz Rizzapedia Rizzachu Rizzitenship New years rizzolution Listening to 103.5 Rizz FM Opened the 8th gate of rizz He’s the rizzkage Caught in a rizzjutsu Used the sharizzan / rizzegan The 6 paths of rizz Searched the 7 chests at rizzky reels Jehovah’s rizzness Playing GOW Rizznarok Listens to Rizzamore Shot with his rizztol Harizzment Lightning McRizz Winner of the Rizzton cup Went through the 5 stages of rizz Mentally rizztarded Domestic terrorizz Rizzy senses are tingling Fell into the rizzlyverse With great rizz comes great rizzponsibility Sees with peripheral rizzion Eats at Texas Rizzhouse Rizzael Rizzatello Calcurizz Playing on max rizzolution Wishing a happy rizzday Rizzday adams Rizzcord Moderator Reptilian Rizz Call of Duty: Warizzone

The Rizzler Rizzly bear The boy who cried rizz Abraham Rizzcoln Adolf Rizzler Rizzy Neutron A degree in quantum rizzics Barrack Rizzbama Need a rizztraining order Anakin RizzWalker Rizzard of Oz Lord of the Rizz Performed a rizzerruction Rizzosaurus Rex From the village hidden in the rizz Offering rizztituation and rizzarations Glenn Rizzmire Rizz Khalifa Martin Luther Rizz Kamala Harizz Rizzy Hendrix/ Jimi Hendrizz Rizzilicious Rizziliguous Rizziologist Rizzillionaire Rizz Ranger The Rizz reaper Leader of the rizzistance Chrizz Brown Rizzdolph the Rizz-Nosed Reindeer Wolverizz Head coch of the Memphis Rizzlies Prisoner of Rizzkaban Rizzaholic Rizza Parks Rizz Hemsworth Albert Rizzenstein Playing Rizzident Evil Mike Rizzowski Franklin D Rizzevelt Queen Erizzabeth Kyle Rizzenhouse Walt Rizzney Signed the declaration of rizzdependence From the state of Rizzouri Rizz Al Ghul Corona Virizz Rizztafarian Rizzie Smalls R(izz) Kelly Rizzil War Veteran Rizz and Morty Gerald of Rizzia Alvin and the Rizzmunks Otto Von Rizzmark The last Rizzort Got a ticket for the polar rizzpress/ exprizz Artirizzal Intelligence Natural Rizzastar First Rizzponder Member of the nation of Rizzlam Crizztiano Rizzaldo Rizzaldinho The Grand rizzard Ghost of Rizzmiss Past 13 rizzons why Are the rizz rizz fruit One of the three Rizzmirals 7 Rizzlords of the sea Qualified for rizzlemaina Sent to prizzon George Rizzington Theodore Rizzevelt The little boy from Rizzario Plays for Real Madrizz The last rizzbender Found the derizzative of the function Lando Cal- rizz- ian Aurizztic/ Diagnosed with Aurizzim Jack the rizzer Grew up in Rizzadelphia Rizzatron Dwayne the Rizz Johnson Master of the Rizzic Arts Osama Rizz Laden Frosty the rizzman The rizziah Fell into the economic rizzession Rizzas in Paris Chuck Norizz Sir Rizz- a- lot Rules the Rizzatine Empire Rizzioactive Cooking Rizzatouille Forizz Gump A Diet sometimes involves Blue Rizzberries The nightmare before Rizzmas Rizzeree Damian Rizzard In the Marvel rizzamatic universe Undergoing Celluar rizzpiration Plagiarizzim Thesaurizz Rizzmas Tree Rizzmas Present Rizzimus Prime/ Optirizz Prime Cardiopulmonary rizzuscitation Be Generizz to that person Charizzard Isaac Rizzton Little Rizz Rizzing Hood Arnold Schwarzenrizzer Rizz Archives Rizz in peace Elvis Rizzley Cloudy with a Chance of Rizz Rizzapedia Rizzachu Rizzitenship New years rizzolution Listening to 103.5 Rizz FM Opened the 8th gate of rizz He’s the rizzkage Caught in a rizzjutsu Used the sharizzan / rizzegan The 6 paths of rizz Searched the 7 chests at rizzky reels Jehovah’s rizzness Playing GOW Rizznarok Listens to Rizzamore Shot with his rizztol Harizzment Lightning McRizz Winner of the Rizzton cup Went through the 5 stages of rizz Mentally rizztarded Domestic terrorizz Rizzy senses are tingling Fell into the rizzlyverse With great rizz comes great rizzponsibility Sees with peripheral rizzion Eats at Texas Rizzhouse Rizzael Rizzatello Calcurizz Playing on max rizzolution Wishing a happy rizzday Rizzday adams Rizzcord Moderator Reptilian Rizz Call of Duty: Warizzone

---

