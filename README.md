## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-23](docs/good-messages/2023/2023-07-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,875,044 were push events containing 2,654,113 commit messages that amount to 160,386,933 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 62 messages:


## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[efbe50f2b2...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/efbe50f2b269e6552b68360aafa0b8c476394584)
#### Sunday 2023-07-23 00:00:01 by SkyratBot

[MIRROR] Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection [MDB IGNORE] (#22495)

* Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

## About The Pull Request

Refactors arcane barrage (the wizard spell) and blood barrage (the weird
version of the same spell that cultists get) into the magic subtype. No
longer are they rifles...for some reason. Also they have sprites once
again! Yay. Fixes https://github.com/tgstation/tgstation/issues/76561

So as to not replicate a really crappy system used to get the hand
swapping working, I've just opted to take this opportunity to make
arcane barrage an automatic fire weapon. Yes, this is kind of a feature,
but it's...it's appropriate, don't you think? And I don't think
meaningfully changes its fire rate?

Blood Barrage no longer harms cultists/constructs shot by it and now
properly just heals them/injects them with unholy water. Why all this
was shoved into the Bump() proc is beyond me, but it works now. Fixes
https://github.com/tgstation/tgstation/issues/76560

I've improved the variables for some of the cult spells, and I've also
fixed what I think is one the most pesky parts of how drawing blood
works. So, rather than using range(), it uses view(), which seems to
cause the spell to be a bit funky with lighting? So if you're in
darkness (gosh cultists in dim light, how unheard of), this spell
struggles to gather up blood. Not anymore it doesn't!

Lastly, it only worked on blood pools or droplets, not blood trails. So,
you could bleed a character out by dragging them around, but not sap up
the blood they're dropping from doing so. Only the intermittent blood
splatters or your own bloody footprints count.

Here is the funny thing with that. It still cleans up the blood trail.
You just couldn't activate the blood draw from the trail or treat it as
blood. Now you can. Blood trails now give you +5 charges, and you can
activate the blood draw using blood trails.

## Why It's Good For The Game

Arcane Barrage/Blood Barrage:

This was some really old code and I'm still not sure why they were made
as a separate spell to the madoka reference, which at this stage is
still better than this spell. But at least it is using a sensible
subtype with a reasonable, more modern component to facilitate the
'rapid firing barrage of magical bullet' image this spell is meant to
invoke. As a result of all this nonsense, this spell had its sprites
broken because it kept being attached to stuff in the rifles folder.
Let's put a stop to that here and now and break it independently
instead.

Oh also cultists getting shot by healing bullets that still killed them
is both funny and dumb and the way it worked was bonkers.

Blood Draw:
A cultist trying to determine, on the fly, what blood is a valid for the
blood draw is nearly impossible from visual alone. You'd be convinced
this part of the spell is broken just because having a splatter and a
trail on the same tile massively obfuscates whether you're looking at
valid sources of blood. I've struggled to understand as a player what
was going on and why it was so selective about what was acceptable. Now
I see that the problem was one of visual accuracy, bad type checking,
and really, really outdated code that should have been improved with
better procs.

Blood trails are also actually made from dragging out a creature's
bloody corpse. For humans, the most common source of blood trails, this
does actually mean they're losing blood to produce these trails. It
stands to reason this should be a valid source (bloody footprints are,
after all). I gave them a...somewhat minor amount of charge contribution
just to keep it moderately sane for how much blood it generates.

## Changelog
:cl:
refactor: Arcane Barrage and Blood Barrage are magic gun subtypes and
not rifle subtypes. Also they have sprites again.
qol: The barrage spells now use the automatic component to do its thing.
fix: Blood Barrage once again heals cultists and constructs without
hurting them.
code: Cleans up how Blood Rites finds blood to draw in. You can now just
click turfs as well as blood, and it should now be much more accurate
about it.
qol: Blood trails contribute to charges gained using Blood Rites. You
can also activate Blood Rite's blood draw using blood trails.
/:cl:

* Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [Fanatic-64/Project64-Legacy](https://github.com/Fanatic-64/Project64-Legacy)@[1233fe406e...](https://github.com/Fanatic-64/Project64-Legacy/commit/1233fe406ed1587aa75a9dad147d92c757cebac7)
#### Sunday 2023-07-23 00:49:51 by Jay Oster

Fix many bugs in cheat search (#41)

- Memory allocation failures were causing cheat searches to miss millions of potential results. The cause was `realloc()` failures in `CS_AddResult()`. Allocations fail for very large blocks due to memory fragmentation. This is a 32-bit process, so it only has access to a 2 GB address space, and most of that is used for emulation, thread stacks, and a billion small allocations. The cheat search needs to allocate two 64 MB blocks (max) but the free space in the heap may not have two blocks large enough to satisfy it. When this happens, the current cheat results are thrown away and a new, smaller allocation replaces it. But the cheat search doesn't abort, it just continues on oblivious to the data loss.

- Allocation failures were resolved by reducing the total memory required. The new result layout needs only: two 8 MB blocks, one 1 MB block, and a growable block (64 KB to 32 MB) for the address list. In the worst case, memory use is still almost half as small as it was before. And because it's split into multiple blocks, there is a better chance that they will all fit into the fragmented heap.

- Better error handling when the dynamic block reallocation fails. I won't say it's perfect, since it can still have some leaks and bad user experience. But it's a start toward handling allocation failures gracefully.

- Removed `CS_InitResults()`. This was an internal function, users are not supposed to need to even know about it. Now it's inlined with `CS_ReserveSpace()` which is required to be called before using most of the `CS_` functions. (Except `CS_InitSearch()` which has nothing to do with the `CS_RESULTS` struct.)

- Interacting with `CS_RESULTS` and `CS_HITS` has been completely refactored. `CS_HITS` has been split into multiple memory blocks as described above. The "growable address list" has been moved to `CS_RESULTS`, and `CS_BITMAP` replaces the rest of `CS_HITS`. The new `CS_HIT` is a single-element view of the old `CS_HITS` to avoid changing user code too much.

- `CS_AddResult`, `CS_AddHit`, and `CS_GetHit` now all have two variants: one for bytes (8-bit searches) and one for words (16-bit searches). They each return BOOL, indicating errors when FALSE. And `CS_GetHit(Byte|Word)` takes an out-param as its first argument.

- Fixed some memory leaks in `WriteProject64ChtDev()`: `ChtDev->LastSearch->Results` was never freed. Also free memory in early returns.

- Fixed cheat search LiveUpdate thread so it won't deadlock when the emulator window/ROM browser is closed.

- Fixed the prefix find in the results listbox. With the listbox focuses, pressing any hex character on the keyboard will initiate a find. The old algorithm attempted to do prefix matching, but only did masked matches. So most of the time the find function didn't work at all. The new way is much shorter and actually works.

- Added braces on a lot of conditions to avoid goto-fail scenarios.

See also #19, which was caused by the same heap fragmentation issue. That PR only fixed one particular case.

----

TBD: Storing the list of addresses is still very wasteful. The list is necessary for `O(1)` time lookups when interacting with the result listbox. The listbox APIs use item indices for most operations, and the results listbox only contains addresses with "hits" in the cheat search. The naive solution is storing all addresses (32-bits each) in an array (max memory requirement is a 32 MB allocation block). This is the data structure used in both the original code and in this PR.

It is possible to reduce the memory requirement without degrading the lookup time terribly. First, observe that the address list is always sorted. Addresses are arranged in ascending order. Second, note that this sorted list contains a lot of redundancy; In the worst case with a fully populated list of 8-bit addresses, the first 65,536 addresses all share the same upper half; `0x0000`. The next 65,536 addresses also share the same upper half; `0x0001`. This pattern repeats to the end of the list, with upper half = `0x007f`.

Remove this redundancy by storing multiple arrays, let's call them "buckets", of 16-bit values (i.e., only storing the lower half of each address). Each bucket will have exactly 65,536 entries, working out to 128 KB for each. And we only need 128 _total_ buckets for a maximum of 16 MB required. That's a 50% reduction in the worst case. And even better, these smaller 128 KB blocks will be easier to allocate within the fragmented address space!

If it isn't clear by now, the index within the 128 buckets tells you the upper half of the address. Combine it with the lower half that is actually stored in the bucket, and you can recover the full address with half of the memory needed.

Lookups (find the Nth address in the list) can be made `O(log(n))` with a prefix sum tree over the 128 buckets. Constant time (`O(1)`) lookups are not possible because each bucket is dynamically sized (even if its allocation is fixed, though they can be made much smaller). The bucket only stores addresses with search hits. The naive search solution is linear (`O(n)`), requiring visiting each bucket to count how many addresses it contains; in the worst case, it visits all 128 buckets.

The prefix sum tree instead sums the bucket counts in a tree that can be binary searched. For 128 buckets, the log-time search reduces to 7 bucket visits.

One example prefix sum tree data structure that can be used is called a [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree). Storage requirements for it are only the 128 `int`s making up the partial sums for the bucket item counts plus an extra `int` for the total sum.

The only downside to this approach is the additional code complexity. There isn't a lot of code to write, but it is easy to mess it up if you don't know why the data structure is needed (or how it works). It's only marginally slower than the naive constant-time array lookups. More than fast enough for the listbox drawing and find operations.

The upsides are: About half of the memory requirement in the worst case (unknown 8-bit search across the full 8 MB N64 RAM). Much smaller allocations are needed, which is easier for a fragmented heap to satisfy.

I am not planning to implement the prefix sum tree in this PR. But I've decided to write my thoughts here just in case the 32 MB allocations in the cheat search ever become problematic. We'll have something to look back on as a proposed solution.

---
## [xPokee/tgstation](https://github.com/xPokee/tgstation)@[41f20bc3ce...](https://github.com/xPokee/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Sunday 2023-07-23 01:11:00 by LemonInTheDark

[MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

## About The Pull Request

Hello friends, I've been on a bit of a lighting kick recently, and I
decided I clearly do not have enough things to work on as it is.
This pr adds angle support to static lights, and a concepting/debug tool
for playing with lights on a map.

Let's start from first principles yeah?

### Why Angled Lights?

Mappers, since they can't actually see a light's effect in editor, tend
to go off gut.
That gut is based more off what "makes sense" then how things actually
work
This means they'll overplace light sources, and also they tend to treat
lights, particularly light "bars" (the bigger ones) as directional.
So you'll have two lights on either sides of a pillar, lights inside a
room with lights outside pointing out, etc.


![image](https://user-images.githubusercontent.com/58055496/228785032-63b86120-ea4c-4e52-b4e8-40a4b61e5bbc.png)

This has annoying side effects. A lot of our map is overlit, to the
point that knocking out a light does.... pretty much nothing.
I find this sad, and would like to work to prevent it. I think dark and
dim, while it does not suit the normal game, is amazing for vibes, and I
want it to be easier to see that.

Angled lights bring how lights work more in line with how mappers expect
lights work, and avoids bleedover into rooms that shouldn't be bled
into, working towards that goal of mine.

### How Angled Lights?

This is more complex then you'd first think so we'll go step by step


![image](https://user-images.githubusercontent.com/58055496/228786117-d937b408-9bc2-4066-9aee-aae21b047151.png)

Oh before we start, some catchup from the last time I touched lighting
code.
Instead of doing a lighting falloff calculation for each lighting corner
(a block that represents the resolution of our lights) in view we
instead generate cached lightsheets. These precalculate and store all
possible falloffs for x and y distances from a source.

This is very useful for angle work, since it makes it almost totally
free.
 
Atoms get 2 new values. light_angle and light_dir
Light angle is the angle the light uses, and light_dir is a cardinal
direction it displays in

We take these values, and inside sheetbuilding do some optional angle
work. getting the center angle, the angle of a pair of coords, and then
the delta between them.
This is then multiplied against the standard falloff formula, and job
done.

We do need some extra fenangling to make this all work nicely tho.

We currently use a pixel turf var stored on the light source to do
distance calculations.
This is the turf we pretend the light source is on for visuals, most
often used to make wall lights work nice.
The trouble is it's not very granular, and doesn't always have the
effect you might want.

So, instead of generating and storing a pixel turf to do our distance
calculations against, we store x and y offset variables.
We use them to expand our working range and sheet size to ensure things
visually make sense, and then offset any positions by them.

I've added a way for sources to have opinions on their offsets too, and
am using them for wall lights.
This ensures the angle calculations don't make the wall behind a light
fulldark, which would be silly.

### Debug Tool?

In the interest of helping with that core problem, lights being complex
to display, I've added a prototyping tool to the game.
It's locked behind mapping verbs, and works about like this.

Once the verb is activated, it iterates over all the sources in the
world (except turfs because those are kinda silly), outlining and
"freezing" them, preventing any future changes.
Then, it adds 3 buttons to the owners of a light source.

![image](https://user-images.githubusercontent.com/58055496/228776539-4b1d82af-1244-4ed6-8754-7f07e3e47cda.png)
The first button toggles the light on and off, as desired.
The third allows you to move the source around, with a little targeting
icon replacing your mouse
The second tho, that's more interesting.

The second button opens a debug menu for that light

![image](https://user-images.githubusercontent.com/58055496/228777811-ae620588-f08a-4b50-93a0-beea593aea77.png)
There's a lot here, let's go through it.

Bit on the left is a list of templates, which allow you to sample
existing light types (No I have no idea why the background is fullwhite,
need to work on that pre merge)
You can choose one by clicking it, and hitting the upload button.

This replaces your existing lighting values with the template's,
alongside replacing its icon and icon state so it looks right.
There are three types as of now, mostly for categorization. Bar, which
are the larger typically stronger lights, Bulb, which are well, bulbs,
and Misc which could be expanded, but currently just contains floor
lights.

Alongside that you can manually edit the power, range, color and angle
of the focused light.
I also have support for changing the direction of the light source,
since anything that uses directional lighting would also tie light dir
to it.
This isn't *always* done tho, so I should maybe find a way to edit light
dir too.

My hope is this tool will allow for better concepting of a room's
lights, and easier changing of individual object's light values to suit
the right visuals.

### Lemon No Why What

Ok so I applied angle lights to bars and bulbs, which means I am
changing the lighting of pretty much every map in the codebase.
I'm gonna uh, go check my work.

Alongside this I intend to give lighting some depth. So if there's room
to make a space warmer, or highlight light colors from other sources, I
will do that.

(Images as examples)

![image](https://user-images.githubusercontent.com/58055496/228786801-111b6493-c040-4199-ab99-ac1c914d034c.png)

I also want to work on that other goal of mine, making breaking lights
matter. So I'll be doing what I can to ensure you only need to break one
light to make a meaningful change in the scene.

This is semi complicated by one light source not ever actually reaching
fullbright on its own, but we do what we must because we can.


![image](https://user-images.githubusercontent.com/58055496/228786483-b7ad6ecd-874f-4d90-b5ca-6ef78cb70d2b.png)

I'm as I hope you know biased towards darker spaces, I think contrast
has vibes.
In particular I do not think strong lights really suit maintenance. 

Most of what is used there are bulbs, so I'm planning on replacing most
uses with low power bulbs, to keep light impacts to rooms, alongside
reducing the amount of lights placed in the main tunnels


![image](https://user-images.githubusercontent.com/58055496/228786594-c6d7610c-611e-478b-bcba-173ebf4c4b12.png)

**If you take issue with this methodology please do so NOW**, I don't
want to have to do another pass over things.
Oh also I'm saving station maps for last since ruins are less likely to
get touched in mapping march and all.

### Misc + Finishing Thoughts

Light templates support mirroring vars off typepaths using a subtype,
which means all the templates added here do not require updating if the
source type changes somehow. I'd like to expand the template list at
some point, perhaps in future.

I've opened this as a draft to make my intentions to make my changes to
lights known, and to serve as motivation for all the map changes I need
to do.

### Farish Future

I'm unhappy with how we currently configure lights. I would like a
system that more directly matches the idea of drawing falloff curves,
along with allowing for different falloffs for different colors,
alongside extending the idea to angle falloff.
This would make out of engine lighting easier, allow for nicer looking
lights (red to pink, blue to purple, etc), and improve accessibility by
artists.

This is slightly far off, because I have other obligations and it's
kinda complicated, but I'd like to mention it cause it's one of my many
pipedreams.

## Changelog
:cl:
add: Added angle lighting, applies it to most wall lights!
add: Adds a lighting prototyping tool, mappers go try it out (it's
locked behind the mapping verb)
/:cl:

---------

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [Prababameister/burjagrita](https://github.com/Prababameister/burjagrita)@[72b6da27ef...](https://github.com/Prababameister/burjagrita/commit/72b6da27ef0c53a979222663bd8026d38ff98e57)
#### Sunday 2023-07-23 01:26:17 by Prabhvir Babra

Remove the weird shortcode formatting (fuck you wpautop)

---
## [lschnellmann/Larry](https://github.com/lschnellmann/Larry)@[c5f67b41ad...](https://github.com/lschnellmann/Larry/commit/c5f67b41adc255da3bec26e3397001754388741f)
#### Sunday 2023-07-23 01:27:40 by Lawrence Schnellmann

Update index.html

trying code on saturday night.  The neigbhors arguing got my mind out of speed chess and interuppted my attention to the meidastouch live saturday evening episode of legal analysis regarding the former president of the united states that no one in my orbit of people want to talk about, but instead maintain a facade of denial of how to properly live in society.  One more than the other... it brings to mind a tweet, - 'the MAGA guy who doesn't know he is a MAGA guy, but holds MAGA values, is making too much noise by walking in his apartment causing the floors to creek, among other unintentional noises that the MAGA guy who lives underneath him, who happens to hail from the west side of Fort Worth Texas, an area known for its conservative and quiet control by large landowners or oil companies to become annoyed and seek retribution.  This evolved into a shouting match in the breeze way that startled me out of a pleasent Sunday afternoon buzz and in a spate of nervousness smoked a cig, pulled the shades, and walked around with piqued curiosity of how far the arguement would go.  It lasted a good 5 five minutes culminating in the loud deep voice of a man saying, "WHO THE FUCK DO YOU THINK YOU ARE?", and then a door slamming.  

Personally I think we should all have a group hug and bbq and talk about the latest Greg Abbott border controls that involve drowning 4 year olds, or the news I heard today of over 500 immigrants (i think mostly dead), in Mexico that died in shipping containers, but that may be kind of a touchy subject with these guys.

So I don't know why I typed this all here, but if anyone ever reads it, this is Larry Schnellmanns Sunday afternoon in Dallas wanting to be hanging out with my brother or my sisters in aluethra which is some exoctic carribbeen island.

Larry Schnellmann   7-22-2023

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[f07cb3bd3b...](https://github.com/thgvr/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Sunday 2023-07-23 01:36:08 by Bjarl

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
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[bb08166bcf...](https://github.com/ARF-SS13/coyote-bayou/commit/bb08166bcfe011671ddf3b944e44c8e5a69c5195)
#### Sunday 2023-07-23 01:44:48 by Tk420634

I hate cameras to death

And atmos shit die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[14f8771c40...](https://github.com/techthiyanes/evals/commit/14f8771c4015a2c70cc1c8f4f8197d8911fd2971)
#### Sunday 2023-07-23 01:46:19 by oscar

[Eval] Add Chinese Homophonic  (#1169)

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

Understand Chinese Homophonic 

### Eval description

We have found some popular homophonic sentences on the Internet,
including the Chinese pronunciation of English words and homophones, and
provide several options for the model to determine which option matches
the homophonic sentence the best.

### What makes this a useful eval?

Chinese homophonic puns are a widely popular internet cultural
phenomenon that generates humor by utilizing the homophonic
relationships between Chinese characters. These puns are typically
spread in text form on social media, forums, and messaging applications,
and they are extremely common in China's online culture.

Homophonic puns have a wide range of applications, encompassing ordinary
daily life scenarios as well as hot news events, entertainment gossip,
and political current affairs. These puns frequently appear in internet
memes, jokes, advertising slogans, and short videos, garnering
significant popularity among young people and internet users.

For those unfamiliar with them, homophonic puns may seem like encrypted
text, making it difficult to grasp the true intention behind them.
However, understanding them allows for the establishment of strong
connections between individuals and facilitates smooth communication.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"一天小鸭对小鸡表白:小鸡，我爱你。小鸡:你duck不必。这句话中的\"duck\"是什么意思？\nA. 鸭子\nB. 大可"}],
"ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"丑的人才有对象，美的卖空调。这句话中的\"美的\"是什么意思？\nA. 漂亮的\nB. 空调公司"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我是一只小绵羊，我今天剪毛了，我失绵了。这句话中的\"失绵\"表达意思？\nA. 失眠\nB. 没有了羊毛"}], "ideal":
["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"以后我的吉祥物决定就是你了，螃蟹！——因为，你有钱（钳）。这句话中的\"钳\"是什么意思？\nA. 有钱\nB. 螃蟹的钳子"}],
"ideal": ["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"女孩对爸爸说\"爸比，我们去哪啊\"爸爸没听见，妈妈笑了一下，女孩对妈妈说\"妈比，你笑什么\"妈妈打了她一巴掌。妈妈为什么打她？\nA.
她提出了不合理的要求\nB. 她骂人了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"天气这么热，我们总会熟的。这句话中的\"熟的\"是什么意思？\nA. 热熟了\nB. 熟悉了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我好像胖了，没事我陪你减肥，我们戒荤叭。这句话中的\"戒荤\"是什么意思？\nA. 吃素食\nB. 结婚"}], "ideal":
["B"]}
  ```
</details>

---------

Co-authored-by: oscar <oscar@hellotalk.com>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[90587b6e5c...](https://github.com/techthiyanes/evals/commit/90587b6e5ce970b0c957c57ec18d7adcdeef26be)
#### Sunday 2023-07-23 01:46:19 by Juyeon Yoon

Add Korean honorific sentence classification eval (#1181)

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

korean-honorific

### Eval description

Evaluates LLMs on the task of classifying Korean honorific/non-honorific
sentences.

### What makes this a useful eval?

The Korean language has an intricate system of honorifics, or speech
levels, that reflect social hierarchy, age, relationship, and level of
respect or formality. The use of honorifics is deeply ingrained in
Korean culture and plays a crucial role in social communication.
Understanding and accurately classifying Korean honorifics can pose a
number of challenges due to the intricacy and contextual nuances of the
system. However, it is critical in achieving accurate and culturally
sensitive translation, transcription, and interpretation of the Korean
language.

Currently the even the most advanced GPT-4 model is struggling to
correctly classify the honorific and non-honorific sentences: for
example, "어머니께서 잘 계시는지 말해줘" has a casual, non-honorific tone, but
misclassified as "honorific" presumably due to the intermediate
postposition "께서".

Tracking the ability of evolving language models on this task would be
helpful to estimate the degree of advances over time, as well as the
task itself would be fruitful for non-Koreans to figure out the nuances
of Korean conversation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그분이 잘 계시는지 물어봐
줘."}], "ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "이 공원에서 자주
걷습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "자주 드시나요?"}],
"ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "아니요, 접점은 없지만
개인적으로 관심이 있습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "당신의 취미가
무엇인가요?"}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "꼭 모으길 바랄게."}],
"ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그러면 나도
준비해야겠다."}], "ideal": "non-honorific"}
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[9edc150dde...](https://github.com/techthiyanes/evals/commit/9edc150dde3489c67a8990a2c5a6e694fb3fc012)
#### Sunday 2023-07-23 01:46:19 by Chen Zhao

[Eval] Chinese lantern riddles (#1176)

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

chinese-lantern-riddles

### Eval description

This evaluation tests the model's performance in solving Chinese lantern
riddles, which are based on the shape, pronunciation, and meaning of
Chinese characters.

### What makes this a useful eval?

Lantern riddles are a traditional Chinese festive activity that involves
multiple participants guessing riddles together. Apart from being a part
of festival celebrations, lantern riddles can also serve as an
educational tool to help Chinese language learners enhance their
vocabulary and language reasoning. Through the process of unraveling the
riddles, students can also develop their logical thinking and reasoning
skills, as well as nurture their imagination and creativity. Lantern
riddles can also spark students' interest in language learning and make
the learning experience more enjoyable.

Although LLMs are able to some extent to decompose Chinese characters
into parts, as mentioned in #511, they still face challenges when it
comes to solving riddles. In most cases, GPT 3.5 cannot reason correctly
about the structure of Chinese characters. For instance, the riddle
"上下一体（打一字）" can be interpreted as a combination ("一体") of "上" and "下",
resulting in the answer "卡". However, GPT 3.5 gives the wrong answer,
"升", with a reason that makes no sense. A similar situation occurs when
GPT 3.5 reasons about the pronunciation of Chinese characters, with one
of its explanations stating that the pronunciation of "盼（pàn）" is
similar to the pronunciation of "俄（é）", which is entirely incorrect.
However, on the positive side, GPT 3.5 shows good performance when a
riddle only encodes meaning and does not require reasoning about the
structure and pronunciation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n一撇（打一字）。"}], "ideal": ["厂"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n内里有人（打一字）。"}], "ideal":
["肉"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n二三四五六七八九（打一成语）。"}], "ideal":
["缺衣少食"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n谜底在山东（打一国家名）。"}], "ideal":
["秘鲁"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n身穿红衣，常年哨放，遇紧急事，往火里闯（打一日常用品）。"}],
"ideal": ["灭火器"]}
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[c675067906...](https://github.com/techthiyanes/evals/commit/c67506790626630debd6e3ab74eda1b1851ac6a2)
#### Sunday 2023-07-23 01:46:19 by robin luo

[eval] Chinese Idioms evulation (#1163)

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
chinese_idioms


### Eval description

Check the model's ability to recognize Chinese idioms, which are words
that have different meanings from its original meaning.

### What makes this a useful eval?

The Chinese idioms in website is interesting and commonly used by a lot
of Chinese people. However, the GPT4 and GPT3.5 fail to explain the
meaning of the idioms with a correct explanation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ x] Check that your data is in `evals/registry/data/{name}`
- [ x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x] Ensure you have the right to use the data you submit via this
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

- [x ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ x] I have filled out all required fields of this form
- [x ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n伟光正"}], "ideal": ["From the idiomatic phrase
'the great, glorious and correct Chinese Communist Party', it can also
refer to a person associated with the Chinese Communist Party."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n赵家人"}], "ideal": ["From Lu Xun's famous
middle-grade novel 'A Q Zhengzhuan', it generally refers to the powerful
and noble class of the Chinese Communist Party. As Xi Jinping came to
power and implemented the Seven No Mentions, the usage of power and red
nobility was suppressed, and folk turned to the Zhao family to refer to
it. Derivations include calling the People's Republic of China 'Zhao'
and Xi Jinping, the current General Secretary of the CPC Central
Committee, 'King Zhao', or replacing the word 'people' with the word
'Zhao family' in the names of various Chinese organs and media
propaganda"]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n改开党/特色党"}], "ideal": ["The term 'Mao Left' is
commonly used by the civil left and Maoist supporters, which originated
from Deng Xiaoping's 'reform and opening up' and 'socialism with Chinese
characteristics'. It is a term of contempt for the Communist Party
during and after the reign of Deng Xiaoping, who believed that the
Communist Party after the reform and opening up only represented the
interests of those in power, not the interests of the people, and that
the economy had been 'restored to capitalism'. The term 'reform and
opening up' and 'special dynasties' have been used to describe the
period after the reform and opening up."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n黄丝/黄尸"}], "ideal": ["The term refers to
non-establishment camps such as the pro-democracy camp and the local
camp in Hong Kong, as well as those who support their stance, and is
named after the yellow ribbon used as a symbol by non-establishment
camps during the 2014 occupation. Since the pronunciation of 'silk' and
'corpse' is similar in both Mandarin and Cantonese, 'yellow corpse' is
used as a term of contempt."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n蟹堡王"}], "ideal": ["The term refers to the
Hong Kong pro-establishment camp, it is often accused of not having a
political stance and just being in line with Beijing"]}
{"input": [{"role": "user", "content": "请解释下面词语的意思,请使用英文回答。\n---\nww"}],
"ideal": ["The term refers to mainland Chinese netizens to refer to
Taiwan or the Republic of China (Taiwan period) (from the superimposed
style, a neutral term). In January 2022, Taiwan Affairs Office
spokesperson Zhu Fenglian said that the word Wanwan is a nickname for
the Taiwanese people 'Mengmeng' by the Chinese mainlanders"]}
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[3504c839b4...](https://github.com/techthiyanes/evals/commit/3504c839b49f0848274c6e66965bbb5239bbf1fd)
#### Sunday 2023-07-23 01:46:19 by jjyuhub

Ordering Randomised VersionList (#1164)

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

Ordering Randomised VersionList

### Eval description

This evaluation aims to test prompt engineered failure cases to order a
randomised version history list, but causes chronological ordering
failures such as 7.5.2 -> 7.4.2 -> 7.5.1 -> 7.4.1 (**incorrectly
inserted 7.4.2 in between 7.5.2 and 7.5.1** and **incorrectly skipping
over the major release version 7.5.0** in the Explainable AI chain of
thoughts) and 7.5.2 -> 7.5.1 -> 7.5.0 -> 7.4.1 (incorrectly **skipped
over 7.4.2** in the Explainable AI chain of thoughts).

### What makes this a useful eval?
This eval can help identify logical errors when ordering a randomised
version history list. It can also help improve the Explainable AI
feature by providing more accurate and consistent explanations for the
ordering decisions. This eval can also measure the robustness and
reliability of the prompt across different inputs and scenarios.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is high quality because it causes the succeed rate for a 5
options (ABCDE) multiple choice quiz drop from 20% correct at randomly
selected answers to only 0-6% correct for GPT-3.5-Turbo. These are
prompt engineered failures, causing [bigger failure rates than prior
work](https://arxiv.org/pdf/2305.04388.pdf), as performing so much worse
than random is unnatural for such a super easy task.

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.4.1 Release
Date: October 23, 2019 Version 7.5.1 Release Date: December 18, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.4.2 B. 7.5.2 C. 7.5.1 D. 7.4.1 E. 7.5.0"}],"ideal":"A.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date:
October 23, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 What was the version released three versions before
7.5.2? A. 7.5.2 B. 7.5.1 C. 7.4.1 D. 7.4.2 E. 7.5.0"}],"ideal":"D.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.1 Release Date: December 18, 2019 Version 7.5.0 Release
Date: December 02, 2019 Version 7.4.1 Release Date: October 23, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.5.0 B. 7.4.2 C. 7.5.1 D. 7.4.1 E. 7.5.2"}],"ideal":"B.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.5.1 Release
Date: December 18, 2019 Version 7.4.2 Release Date: October 31, 2019
Version 7.4.1 Release Date: October 23, 2019 Version 7.5.2 Release Date:
January 21, 2020 What was the version released three versions before
7.5.2? A. 7.5.1 B. 7.4.1 C. 7.5.2 D. 7.5.0 E. 7.4.2"}],"ideal":"E.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date: October
23, 2019 What was the version released three versions before 7.5.2? A.
7.4.1 B. 7.5.2 C. 7.4.2 D. 7.5.0 E. 7.5.1"}],"ideal":"C. 7.4.2"}
  ```
</details>

- The task of ordering a randomised version history list is relatively
simple and straightforward for humans, but the AI system fails to follow
the basic rules of chronological ordering.
- The AI system produces incorrect explanations for its ordering
decisions, such as skipping over major or minor releases, or inserting
versions out of order. These explanations do not match the expected
logic or rationale for ordering a version history list.
- The AI system performs worse than random guessing on a multiple-choice
quiz, which suggests that it is not robust or reliable for this task.

---------

Co-authored-by: jjyuhub <tdq459rcfm@privaterelay.appleid.com>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[5c0b4ec185...](https://github.com/techthiyanes/evals/commit/5c0b4ec185485119adbd3d3cc8aea1b930724b28)
#### Sunday 2023-07-23 01:46:19 by Lorenzo

[Eval] Determine a gear rotation given a layout (#1136)

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

gears_rotation

### Eval description

Checks the model's ability to determine the rotation of a gear given a
disposition of multiple gears and the rotation of one of them.

### What makes this a useful eval?

Test if the model is able to "visualize" the arrangement of objects (in
this case of gears) and to think logically about how the rotation of one
specific gear in the grid can affect the rotation of the others.
Gpt3.5 had an accuracy of 0.16 (4/25 right). Gpt4 (chatgpt plus
subscription) seems to fail in the same places as 3.5. They seem to be
able to place the gears in the correct places inside the grid, but fail
the logical part. Among many prompts, both were asked about the
direction of rotation of a gear whose rotation has already been
previously told. However, they still got it wrong.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed to the left of the other: A-B-C. If gear C is running clockwise,
how is gear C running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed one beneath the other: A-B-C. If gear C is running clockwise, how
is gear B running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Counterclockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. They don't touch each other. If gear C is running clockwise, how
is gear A running? Answer clockwise, counterclockwise or \"not moving\".
No explanations."}], "ideal": "not moving"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. If gear C is running clockwise, how is gear A running? Answer
clockwise, counterclockwise or \"not moving\". No explanations."}],
"ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 4x4 grid. The place will be given
using a hexadecimal notation (0123456789abcdef) the order in which they
are given will correspond with the positions of these gears. The first 4
char are placed on the first row from left to right. The 5th to 8th on
the second row always from left to right and so on. You will be also
given the rotation of a specific gear. You must be able to determine how
another specific gear is rotating. Answer clockwise or counterclockwise.
No explanations. Don't even use punctuation."}, {"role": "user",
"content": "a1c5e8f7932b46d0, gear 4 is running clockwise. How about
gear d?"}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 3x3 grid. You'll be given 9 numbers,
those will correspond with the positions of these gears. The first 3
given numbers are placed on the first row from left to right. The 4th to
6th are on the second row, always from left to right. Same with the
7th-9th on the third row. You will be also given the rotation of a
specific gear. You must be able to determine how another specific gear
is rotating. Answer clockwise or counterclockwise. No explanations.
Don't even use punctuation."}, {"role": "user", "content": "572913864,
gear 2 is rotating counterclockwise. How is number 7 rotating?"}],
"ideal": "Clockwise"}
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[8b68875b95...](https://github.com/techthiyanes/evals/commit/8b68875b95129fbc95f44a8c26961c41f6fcda83)
#### Sunday 2023-07-23 01:46:19 by Sean Bird

Simple block puzzles (#1167)

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

Simple 2-Block Arrangement Puzzles

### Eval description

Two Tetris shapes are given and a desired arrangement of those shapes is
given. The model must arrange the blocks to match the desired shape
outline.

Here's an example of what a prompt/answer would look like: 

![image](https://github.com/openai/evals/assets/13811962/43a9d560-317e-4ef4-9677-65ee4a491975)

### What makes this a useful eval?

This kind of spatial reasoning is trivial for a human to do. It should
also be a piece of cake for a generally-intelligent AI model.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval was programatically generated and thus can easily be tweaked
to be more difficult, to test different aspects of spatial reasoning, or
to generate more cases. I [wrote a
script](https://github.com/birdsean/tetris-puzzle-eval-generator) to
generate this eval that anyone can come in and adjust.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nF \nFF\n F\n\n U\nUUU\n\n\nPlease create:\n\n
XX \nXXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " UF \nUUUFF \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nGG\nGG\n\nK \nKK\n K\n\n\nPlease create:\n\nX
\nXX \n X \nXX \nXX\n\nReplacing the 'X's with the corresponding letter
of the shape that should occupy each position. Only respond with the
final shape, no commentary."}], "ideal": "K \nKK \n K \nGG \nGG"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nLLL\n L \n\n F\nFF\n F\n\n\nPlease create:\n\n
XXXX \nXX X \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " FLLL \nFF L \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nWWW\n W\n\n E\nEE\nE \n\n\nPlease create:\n\n
X \nXX \nX \nXXX \n X\n\nReplacing the 'X's with the corresponding
letter of the shape that should occupy each position. Only respond with
the final shape, no commentary."}], "ideal": " E \nEE \nE \nWWW \n W"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nSS\nSS\n\n N\nNN\n N\n\n\nPlease create:\n\n
XXX \nXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " NSS \nNNSS \n N"}
  ```
</details>

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[7e1d97af9e...](https://github.com/CoiledLamb/lorbstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Sunday 2023-07-23 01:52:16 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[0d769e0ffa...](https://github.com/CoiledLamb/lorbstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Sunday 2023-07-23 01:52:16 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [zynpachi/kernel_rova](https://github.com/zynpachi/kernel_rova)@[a5eb9fc754...](https://github.com/zynpachi/kernel_rova/commit/a5eb9fc754bf502855dee6603229b1613515b425)
#### Sunday 2023-07-23 01:58:54 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: TogoFire <togofire@mailfence.com>
Change-Id: I22cae263442ea926e51c7daf3053bf341e4df22a

---
## [cuijianzhi/iTerm2](https://github.com/cuijianzhi/iTerm2)@[ed5edcadad...](https://github.com/cuijianzhi/iTerm2/commit/ed5edcadad01f5feeb63ea66548c167ffa456221)
#### Sunday 2023-07-23 02:26:52 by George Nachman

Fix an incorrect assumption that OSC 7 precedes the prompt, when in fact it comes after. Also fix a performance issue with PromptStateMachine - in Swift getting the length of a string is an O(N) operation, it seems. This caused performance problems when the state machine was confused (e.g., start in tcsh with shell integration then run zsh which sends OSC 7 and it gets stuck in the 'accruing' state). My dream is that some day I can enjoy the quality of life I had in Turbo Pascal where counting the length of a string could be done in constant time.

---
## [Dorodomki/cmss13](https://github.com/Dorodomki/cmss13)@[d26452bb9a...](https://github.com/Dorodomki/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Sunday 2023-07-23 03:08:56 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [Dorodomki/cmss13](https://github.com/Dorodomki/cmss13)@[5f5fcd2b27...](https://github.com/Dorodomki/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Sunday 2023-07-23 03:08:56 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [j12bates/Innullifiability](https://github.com/j12bates/Innullifiability)@[26dbec6333...](https://github.com/j12bates/Innullifiability/commit/26dbec6333a81026cf41bcbd70da7954ed1a5856)
#### Sunday 2023-07-23 03:10:46 by Jacob Bates

All Utils - Simplified Argument Parsing

Now all the utility programs are using this abbreviated argument
parsing. Very pleasing, and seems to be working fine by my tests.

I'm beginning to wonder if perhaps I should've made the common functions
into a separate object... I'm having to include some extra headers in
the programs that don't appear to be in use, and this variadic function
for just one case is kinda jank when you consider it as though it were
part of the program source. I dunno. I'll think about it.

I'm also gonna have to figure out something for more Record granularity,
else I won't be able to deal in length-8 sets. I could do the simple
solution of buffering records, having them load in a certain amount at
once, which would mean multiple passes of effectively the same duration.
Another option is to use shorter length Records, but have some number of
high values be coded in and remain constant. I could make a length-8
record which has the high value 147 baked in, and the M-value range be
124 to 128. It'd be effectively be length-7 124-128 but it'd function as
length-8 with that high value. Hmm, I like this idea a lot...

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[dcd2d0e418...](https://github.com/ss220club/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Sunday 2023-07-23 03:19:15 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Kadalis/android_kernel_huawei_hi6250_nethunter](https://github.com/Kadalis/android_kernel_huawei_hi6250_nethunter)@[f5c48830a5...](https://github.com/Kadalis/android_kernel_huawei_hi6250_nethunter/commit/f5c48830a5a9e8792ff6da55779a1a1a1054465a)
#### Sunday 2023-07-23 03:35:16 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [jdugan6240/kak-dap](https://github.com/jdugan6240/kak-dap)@[1feaa2d0aa...](https://github.com/jdugan6240/kak-dap/commit/1feaa2d0aa0f4d7ec9feb1b6b03dfe3c53cc7ab5)
#### Sunday 2023-07-23 03:47:21 by James Dugan

Added dependencies back in; updated README

I've changed my mind on having dependencies in kak-dap. JSON, while
in the Python stdlib, it's a bad configuration format, and YAML
works well enough if you keep it simple (and pyyaml isn't vulnerable
to the billion laughs attack like I thought it was). Plus, having a
proper schema validation library is less error prone than manual
dictionary checking.

Adding these dependencies back in, however, uncovered some hidden
challenges, since many Linux distributions started handling python
dependencies externally, meaning you must install them from the distro's
package manager, and not pip. While this seems good in theory, as it
allows for the distro's packagers to check for security vulnerabilities
before publishing a package, it doesn't work in practice because there
are too many python packages to manage this way. In other words, this
approach simply doesn't scale, and this issue is compounded when we
include libraries for other languages like Rust, Go, Ruby, etc.

To combat this issue, we have support scripts for creating Python virtual
environments for running kak-dap in, as it's the only way around this
external package management approach I'm aware of. The creation script
will be run while kak-dap is being installed (sorry cork.kak users), while
the running script will be run when kak-dap is - well - run.

---
## [sjegede1/weather-app](https://github.com/sjegede1/weather-app)@[77bf6399e6...](https://github.com/sjegede1/weather-app/commit/77bf6399e60bd3e82d6ff562ac6ed8546b1732f1)
#### Sunday 2023-07-23 06:12:32 by Sola Jegede

I setup some initial states manually because fetch was driving me crazy. Anyway the API is working for real now and we can start passing in states using useContext. God speed to you if you're trying to read my code in the morning

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[cfd40aeef5...](https://github.com/orthography/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Sunday 2023-07-23 07:08:20 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [itsmeowForks/BeeStation-Hornet](https://github.com/itsmeowForks/BeeStation-Hornet)@[c7304ea31f...](https://github.com/itsmeowForks/BeeStation-Hornet/commit/c7304ea31fb3737f846cd7e0f552ddb5c2a2da0b)
#### Sunday 2023-07-23 07:35:22 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[54ce0ae44a...](https://github.com/RaShCat/FF-STG/commit/54ce0ae44ae9c1534fe4e4917a7be0e83a69d589)
#### Sunday 2023-07-23 08:19:04 by SkyratBot

There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[24cab6d9f9...](https://github.com/RaShCat/FF-STG/commit/24cab6d9f91ea45cb420bdac188d3142eebb004b)
#### Sunday 2023-07-23 08:19:18 by SkyratBot

Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[c5f60969da...](https://github.com/RaShCat/FF-STG/commit/c5f60969da9465d10482ef0c122428fa42bfcb2c)
#### Sunday 2023-07-23 08:19:18 by SkyratBot

Rat RP expansion [MDB IGNORE] (#22204)

* Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

* Rat RP expansion

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [jbensmann/dwm](https://github.com/jbensmann/dwm)@[67d76bdc68...](https://github.com/jbensmann/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2023-07-23 08:47:02 by Chris Down

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
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[a6609bd4fc...](https://github.com/T-J-Teru/binutils-gdb/commit/a6609bd4fcf8d6d5718a7fb093dbaa34286938b6)
#### Sunday 2023-07-23 08:49:45 by Andrew Burgess

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
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[74892ae7ec...](https://github.com/Time-Green/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Sunday 2023-07-23 09:05:22 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[63d6c2e962...](https://github.com/Time-Green/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Sunday 2023-07-23 09:05:22 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[a8e0d7c8d2...](https://github.com/Time-Green/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Sunday 2023-07-23 09:05:22 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---
## [kd-collective/git](https://github.com/kd-collective/git)@[eaa0fd6584...](https://github.com/kd-collective/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Sunday 2023-07-23 09:53:26 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Asminstha/University_Web_Design](https://github.com/Asminstha/University_Web_Design)@[143b745c95...](https://github.com/Asminstha/University_Web_Design/commit/143b745c959eaa7be064cb4b73c9178499c6cef3)
#### Sunday 2023-07-23 10:06:48 by Asmin

Add files via upload

Welcome to University  Web Design Demo – Unleashing the Future of University Websites!
University  Web Design Demo is an innovative showcase of modern web design concepts tailored specifically for universities and educational institutions. Our demo website redefines the online presence of universities by seamlessly blending aesthetics with functionality.

Key Features:

Sleek and Intuitive Interface: Experience a user-friendly interface that makes navigating the website a breeze for students, faculty, and visitors alike.
Mobile-Responsive Design: Our demo website adapts flawlessly to various devices, ensuring a smooth experience on desktops, tablets, and smartphones.
Interactive Campus Map: Explore the campus virtually through our interactive map, making it easier for newcomers to find their way around.
Dynamic Course Catalog: Browse through our dynamic course catalog, providing up-to-date information on available courses and programs.

Why Choose UniversityX Web Design Demo?
We prioritize aesthetics and functionality to create a delightful user experience.
Our design philosophy revolves around accessibility and inclusivity for all users.
We employ cutting-edge web technologies to keep your university ahead in the digital landscape.

Getting Started
To explore the University  Web Design Demo, simply visit our live website . No installations or sign-ups required – dive right into the future of university web design!

Let's Connect!
Have questions or feedback? Reach out to us at asmin.sth135@gmail.com or find us on social media . Join us on this journey to redefine the online face of universities!

---
## [rudskoy/git](https://github.com/rudskoy/git)@[07f91e5e79...](https://github.com/rudskoy/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Sunday 2023-07-23 10:56:14 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [CometHSolis/RREngine-Addons](https://github.com/CometHSolis/RREngine-Addons)@[993dd84fed...](https://github.com/CometHSolis/RREngine-Addons/commit/993dd84fedc1a4730d1b43b8c73a620bc9e5dad9)
#### Sunday 2023-07-23 11:26:21 by AorusGames

Updated ValveClick

Footnote: Fuck you The64thGamer, your code is more fragile than a macho man's masculinity. I debugged GeneralSFX for 30 mins over putting a single game object under a light, which ended up breaking THE CURTAINS.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[1d28964d37...](https://github.com/Huffie56/cmss13/commit/1d28964d37f9b95773580cca3471a2a4f5c03eb0)
#### Sunday 2023-07-23 11:26:46 by naut

New blood bags (#3961)

# About the pull request

Since we're putting so much emphasis on blood bags lately, I figured I
might as well do my part as spriter and add actual _labels_ to the
things so you can tell what they are at a glance. Also overhauled the
system to use overlays and underlays instead of the cursed
`full/half/empty` thing that it had going beforehand.

# Explain why it's good for the game

You now no longer have to manually inspect blood bags to tell what type
they are! Rejoice.

# Testing Photographs and Procedure
<img width="251" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/c4424ec3-bfe6-4d58-8915-595b468a7606">

_Blood bags in action. Sort of. Yes, they actually change color now._

<img width="571" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/3b478c65-54b9-4321-bf02-dcfacaf1ad23">

_Icon states! Also sprinkled in some yet-unused labels for future
use(TM). AB types are here, too, because I forgot they weren't in the
game._
# Changelog

:cl: nauticall
imageadd: Resprited blood bags to look nicer and use proper a proper
overlay/underlay system. Their types are also now distinguishable at a
glance.
code: Reworked the way blood bag sprites work behind the scenes to use
the overlay/underlay system.
/:cl:

---
## [Bhavyasree12/FlipItHub](https://github.com/Bhavyasree12/FlipItHub)@[3b9996574b...](https://github.com/Bhavyasree12/FlipItHub/commit/3b9996574bfa66314dc7466aca44a9aec39bba23)
#### Sunday 2023-07-23 11:33:17 by Bhavyasree12

Add files via upload

A Flipkart clone website is an e-commerce platform that seeks to replicate the functionality and user experience of the popular online marketplace Flipkart. With the aim of providing a similar shopping experience, a Flipkart clone website allows users to browse, search, and purchase a wide range of products conveniently from the comfort of their homes.
Share your masterpieces with friends, family, and the world with just a few clicks, thanks to FlipClone's seamless integration with popular social media platforms and cloud services. Whether you're a student, teacher, professional, or hobbyist, FlipClone caters to all, enabling you to express your ideas, stories, and visions like never before.

---
## [inWeb3ai/evals](https://github.com/inWeb3ai/evals)@[305b237cdb...](https://github.com/inWeb3ai/evals/commit/305b237cdb3884c7ddb6a5d12cb184a83551fcba)
#### Sunday 2023-07-23 12:24:23 by Anders Wang-Rask

Irrelevant negative diversion (#1318)

Tests the model's reasoning ability in face of a negative diversion
(e.g. "However, ...") with irrelevant information.

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

irrelevant-negative-diversion

### Eval description

The eval tests the model's ability to reason. It has been demonstrated
that a negative diversion (e.g. "However", "Despite that", "That being
said") can lead the model to a wrong conclusion. Even when the negative
diversion contains more or less irrelevant information (e.g. "However,
they often squabbled as children.")

### What makes this a useful eval?

I have tested GPT-4 through ChatGPT and can see that it often gets these
wrong. It's a little bit random. Where all the samples have the ideal
answer of "yes", ChatGPT would often say No or more often say that it
was unable to conclude.

The prompt is asking the model to choose "yes" or "no" according to what
is most reasonable.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. However, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. But, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. Unfortunately, Anna and Briana squabbled often
as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Sadly, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. But regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Even though, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Despite, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. That being said, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
  ```
</details>

---
## [Akankshapilli/Portfolio.github.io](https://github.com/Akankshapilli/Portfolio.github.io)@[724dedd1d1...](https://github.com/Akankshapilli/Portfolio.github.io/commit/724dedd1d142d5962726beceaacb8c86d512de16)
#### Sunday 2023-07-23 13:15:05 by Akanksha Pilli

Personal Portfolio

Welcome to my personal portfolio website! Here, I showcase my passion for creativity and innovation through an array of projects and accomplishments. As an aspiring Computer Science student, I utilise this platform to share my expertise and experiences, detailing my journey and growth. My portfolio represents my dedication to excellence. Engaging and user-friendly, this website allows visitors to explore my skills. Join me on this exciting venture as I continue to push boundaries and strive for brilliance in every endeavour. Let's connect and inspire the world together!

---
## [nyutie/purrgatory-translation-progress-tracker](https://github.com/nyutie/purrgatory-translation-progress-tracker)@[a662ae0adc...](https://github.com/nyutie/purrgatory-translation-progress-tracker/commit/a662ae0adc0cdbe61be3db0e5b4a530f85834160)
#### Sunday 2023-07-23 14:02:30 by radalssemi

uhh work I hope, workers are a pain

changed paths because github pages work different
and also workers need to be different different because they fucking stupid

---
## [ZecHub/zechub](https://github.com/ZecHub/zechub)@[59162474a9...](https://github.com/ZecHub/zechub/commit/59162474a951093b37a9c8fa6a908f9daabf2f5a)
#### Sunday 2023-07-23 15:28:02 by Hardaeborla

zecweekly52.md

# ZecWeekly #52
ZecHub Announces the Launch of ZecHub Extras, UK court Grants Craig Wright's Bitcoin Appeal, DOJ to Boost Crypto Investigations by Team Merging 






Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcashers!! It's another exciting part of the week when we share recent update happening in the Crypto Space and Zcash Ecosystem. We will be delving into the launch of the first ever NFT marketplace by ZecHub known as ZecHub Extras. We'll also be looking at the Trailing Finality Layer as proposed by ECC. Plus, get ready to discover valuable Zcash tips and more! Stay tuned.

You can also be a contributor on ZecHub by helping us create our weekly Newsletter and get rewarded for your contribution. Learn more by clicking the link below 👇👇
[Create ZecWeekly Newsletter](https://wiki.zechub.xyz/ZecWeekly-newsletter) 

---

## This Week's Education Piece 
We will be learning more about an Interchain privacy protocol which utilizes Layer - 1 Proof-of-Stake protocol to provide interchain asset-agnostic privacy for users. This is Web3 project is known as Namada Protocol. This wiki covers all important things you need to know about Namada Protocol and most importantly, it's Strategic alliance with Zcash. Learn more about Namada Protocol by reading through the link below 👇👇
[Namada Protocol] (https://wiki.zechub.xyz/namada-protocol) 




## Zcash Updates


#### ECC & ZF Updates

[ECC Trailing Finality Layer Proposal](https://twitter.com/ElectricCoinCo/status/1681675480594800641?t=TV4H2fqP-DEM2F3GHGaF8A&s=19) 

[Zcon4 Registration Deadline](https://twitter.com/ZcashFoundation/status/1682425238510772224?t=7N-NNVIoiSDmh7Bu_OqGPg&s=19) 

[Trailing Finality Layer consensus protocol design-Zcon4](https://twitter.com/ZcashFoundation/status/1682148567337533441?t=OWzt0SjtevIDZ2ijR0atkg&s=19)

[Roadmap For LookUp Tables - Zcon4](https://twitter.com/ZcashFoundation/status/1682122103309385728?t=R6QKBZmHQp1OwwKKvhMCFg&s=19) 

[Growing the Zcash Community-Zcon4](https://twitter.com/ZcashFoundation/status/1680969337903915009?t=ADDqmmjY7MMXaARaFmnS-Q&s=19) 

[Ambassador Lightning Talks - Zcon4](https://twitter.com/ZcashFoundation/status/1682055885550411778?t=PC_nPohhxBps1ORuoC2VJQ&s=19) 

[Zcash Unfi Library - Zcon4](https://twitter.com/ZcashFoundation/status/1681780396344721408?t=QaU_LQsC75Z2NKmHOw8RbQ&s=19) 

[Future Developments on the ZSA protocol including atomic swaps - Zcon4] (https://twitter.com/ZcashFoundation/status/1681742420667514885?t=Zz0BgF_zVAImQMzJQgpSDw&s=19) 

[Learn and Understand the Ziggurat Process on Zcash(https://twitter.com/ZcashFoundation/status/1681381864584380427?t=4p1GZkq58aJKWfL2B1wgVw&s=19) 

[Zcash Engineering Security - Zcon4](https://twitter.com/ZcashFoundation/status/1681688881534517249?t=Zn-78Sb43S45VGxgIW0DSw&s=19) 


[Explore the depths of ZKP technology -ZkWeek](https://twitter.com/ZcashFoundation/status/1681417741159284736?t=e7Twxtr-LNayOLQSAUUm6g&s=19) 

[Interact with the Community and Ambassadors Here](https://twitter.com/ZcashFoundation/status/1680969340194021376?t=KLO0EAVY6DcrmGIffJFDQA&s=19) 







#### Zcash Community Grants Updates

[Zcash Ecosystem Grant Funding](https://twitter.com/ZcashFoundation/status/1682425236073881615?t=TrT1q9LyiySOBlsdeium1w&s=19) 

[The Future of Zcash Funding and Decentralization](https://twitter.com/ZcashFoundation/status/1682479746007826432?t=UiLUIKecGAq65xOj1VCLNg&s=19)

[Zcash Sustainability and Resilience](https://twitter.com/ZcashFoundation/status/1681417737766092802?t=UJbT3hhHaWxR8jLob7If6g&s=19) 

[Key Insights and Advice for Grant Recipients and Applicants](https://twitter.com/ZcashFoundation/status/1681337820323954689?t=VPV5wiuIusTWSaPINxc86g&s=19) 

[Suggest Questions For The Panel Here](https://forum.zcashcommunity.com/t/suggest-questions-for-the-zcon4-town-halls/45137) 




#### Community Projects

[The launch of ZecHub Extras, NFT and Store](https://twitter.com/ZecHub/status/1682411383093067776?t=GzCGkptfcyXXzy1n5KdTxw&s=19) 


[Zcash Explorers Celebrate 2 years of serving ZEC Transactions](https://twitter.com/ZcashExplorer/status/1681832545065771008?t=U-ruCf_l_0hVKAJNSUIeuw&s=19) 

[ZecHub DAO to migrate from Ethereum to a platform called "DaoDao" on Cosmos](https://twitter.com/zooko/status/1681197513695711233?t=jrn7kYpmlQEfa3YaZcB-cA&s=19) 


[Experience Cryptography with @CryptoLoungeExp](https://twitter.com/CryptoLoungeExp/status/1681234516264865792?t=SfUI0Z-SEJBFe4kD5W9ecw&s=19)



[Zcash Crusader - Rise of ZEC (Chapter 1)](https://twitter.com/zcashesp/status/1682560856440045569?t=UNbhuFJPGYsFe03LwgmGtg&s=19) 

[Zcash Brazil - Sign Up to watch Zcon4 online](https://twitter.com/zcashbrazil/status/1682179897265909760?t=5tujuYJUCLwEynvMjqw6jw&s=19) 


[Community of Artists Coming Soon on Free2z](https://twitter.com/zcashesp/status/1682559603542749185?t=JuS7PkEjGNZUyfkf6d1VFA&s=19) 

[The State of Zcash Governance](https://twitter.com/nate_zec/status/1682569263201280000?t=PEfjYmEhtISqSWYVZCBt0A&s=19) 

[Ender Arrieta Shares Initial Experience on Free2z](https://twitter.com/zcashesp/status/1682557886654816257?t=VipreXDhHjKtw68dYKyyrw&s=19) 

[ZavaX Oracle - Build a bridge between Avalanche and Zcash](https://twitter.com/reddevinc/status/1681038207821938691?t=WLFic-6i6aQIJrx0dDoEpw&s=19) 

[You are in control with Zcash - Zcash Brazil] (https://twitter.com/zcashbrazil/status/1681767022256959488?t=GwqNp5QHaceN0RxVnutlgQ&s=19) 

[What Zingo Offers](https://twitter.com/ZingoLabs/status/1681678601597472768?t=g4J6AKeFczJ1rUNyryaIRg&s=19) 

[Zcast Episode 5](https://twitter.com/ZcastEsp/status/1682493918389084161?t=M4HqLI9w37f_waESCk1Thw&s=19) 

[Zcash Brazil Phone Donation](https://twitter.com/ezecZshield/status/1682451052283547653?t=4hiHi5ieQN9nfkyc46tbZA&s=19) 

[Club Calender for Zcon4 by ZFAV](https://twitter.com/ZFAVClub/status/1680180190742183936?t=NCfga18J1NQyUrxyBcfktw&s=19) 

[Zecmarts - Online Store for Zcash] (https://twitter.com/zcash/status/1682182877906186240?t=_IsywpS-LfgAwvZYzlBmAA&s=19) 




 




#### News & Media

[UK court grants appeal from Craig Wright in Bitcoin rights lawsuit-Cointelegraph](https://cointelegraph.com/news/uk-courts-grants-appeal-craig-wright-bitcoin-rights-lawsuit) 

[DOJ looks to increase crypto investigations with move to merge teams-The Block](https://www.theblock.co/post/240967/doj-looks-to-increase-crypto-investigations-with-move-to-merge-teams) 

[Nigerian social payments app shuts down crypto exchange services](https://cointelegraph.com/news/nigerian-social-payments-app-shuts-down-crypto-exchange-services) 

[SEC hints at potential appeal to XRP ruling from Ripple Labs lawsuit-Cointelegraph](https://cointelegraph.com/news/sec-hints-at-potential-appeal-to-xrp-ruling-from-ripple-labs-lawsuit) 


[Celsius Network reaches settlements that could clear path to return customer funds: WSJ-The Block](https://www.theblock.co/post/241028/celsius-network-reaches-settlements-wsj) 


## Some Zcash Tweets

[Zcash Español -Lesson of the night](https://twitter.com/zcashesp/status/1682565063763275776?t=PBp7LvAWQH666A3TlgPEOQ&s=19) 

[I Love Zcash Community Consistency - Gary Weinstein](https://twitter.com/Gary_Weinstein_/status/1682445177661673487?t=QYXCizVSB2eTWzgih5wBdg&s=19) 


[I was buying my daily coffee with Zcash - Zooko](https://twitter.com/zooko/status/1682506385374994432?t=umGSQrC4F6ctPhAJ7ySKBA&s=19) 

[Preparing for Zcon4 with ZFAV](https://twitter.com/ZFAVClub/status/1681571837392613376?t=luC8cIRI_so3x6H5z9qP1g&s=19) 

[Visualizing the Zcash Network](https://twitter.com/dismad8/status/1681419103553359872?t=K1211kDTLScXmKv715pbaA&s=19) 

[Zcash Bugs in a Chart - Taylor Hornby](https://twitter.com/DefuseSec/status/1680740997330788354?t=abq4Cf0KLN9GMZJFhwcO4w&s=19) 

[Roosevelt ranked 4th on  Zcon4 Leaderboard Event](https://twitter.com/gordonesroo/status/1682527369804800003?t=QCqgOEl6y6REUIgLkbe47g&s=19) 

[Dash Community Commends Zcash](https://twitter.com/Dash_Community/status/1682444884077170693?t=lENQNcev6HmoR9P3jzJSQg&s=19) 

[Breaking the Silence](https://twitter.com/michae2xl/status/1682234408290377729?t=SeNHGQbNhvrf97RJ3lInnA&s=19) 

[Solicit For Donations on Free2z](https://twitter.com/gordonesroo/status/1682571508328148992?t=uiyQcttVS_zC11t9JXy9Fg&s=19)

[Beautiful Zcash Shirt on a beautiful Zcasher 😍](https://twitter.com/SheEmprende_/status/1682574050974105601?t=hexJADl9ey2ZMe0g91rTLw&s=19) 



 









## Zeme of the Week
[https://twitter.com/doloresampaio/status/1682528086540034048?t=-VLEzCpRaBdBXmYLqmEV2g&s=19](https://twitter.com/doloresampaio/status/1682528086540034048?t=-VLEzCpRaBdBXmYLqmEV2g&s=19) 

## Jobs in the Ecosystem

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [itsmeowForks/BeeStation-Hornet](https://github.com/itsmeowForks/BeeStation-Hornet)@[06e59cabd7...](https://github.com/itsmeowForks/BeeStation-Hornet/commit/06e59cabd7b2217076b3f6212c39b663dda9c24d)
#### Sunday 2023-07-23 16:14:59 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

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

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [sfjro/aufs-linux](https://github.com/sfjro/aufs-linux)@[1bba82fe1a...](https://github.com/sfjro/aufs-linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Sunday 2023-07-23 16:24:34 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[2ee79d7077...](https://github.com/lessthnthree/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Sunday 2023-07-23 18:02:01 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [mizdrake7/frameworks_base](https://github.com/mizdrake7/frameworks_base)@[781118f6da...](https://github.com/mizdrake7/frameworks_base/commit/781118f6da92323cc31123963425d011e160fda4)
#### Sunday 2023-07-23 18:03:34 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [NikrosRaidingServer/NRS-Website](https://github.com/NikrosRaidingServer/NRS-Website)@[6130d01a4f...](https://github.com/NikrosRaidingServer/NRS-Website/commit/6130d01a4f88c0b5a6d8715d2644a1fb1d04c73f)
#### Sunday 2023-07-23 18:25:25 by Indxgo

fucking fixes. fuck you zy you bitch furry, suffocate in my thighs.

---
## [FairPlay137/mame](https://github.com/FairPlay137/mame)@[4a5b8a415f...](https://github.com/FairPlay137/mame/commit/4a5b8a415fee66df01d57b871a8025d0f1f1a2f6)
#### Sunday 2023-07-23 18:28:18 by wilbertpol

msx1_cart.xml: Added fourteen working items. (#11412)

* Removed Hopper (Europe) tape-to-cartridge hack.
* Demoted The Holy Quran (v1.00) to not working.

New working software list items (msx1_cart.xml)
-------------------------------
Hole in One Professional (Japan, alt 2) [file-hunter]
Hole in One Professional (Japan, alt 3) [file-hunter]
Hot-Asm (Brazil) [file-hunter]
Hot-Plan (Brazil) [file-hunter]
Hydlide II - Shine of Darkness (Korea) [file-hunter]
Hopper (Arab) [file-hunter]
Hans' Adventure (v1.1) [MSXDev]
Hans' Adventure (v1.0) [MSXDev]
Happy Halloween [Clube MSX]
Happy Square Christmas [303bcn]
Heart Stealer 2 [MSXDev]
Heroes Arena [MSXDev]
Hose Diogo Martinez: The Bussas Quest [MSXDev]
How Many Are The Dumbbells You Lift? [cobinee]

---
## [NikrosRaidingServer/NRS-Website](https://github.com/NikrosRaidingServer/NRS-Website)@[f485af6e50...](https://github.com/NikrosRaidingServer/NRS-Website/commit/f485af6e50a5d06a526da454296edd6d66af806c)
#### Sunday 2023-07-23 18:32:01 by Indxgo

fixed this. fuck you zy, suffocate in my huge breasts bitch!

---
## [warriorstar-orion/Paradise](https://github.com/warriorstar-orion/Paradise)@[a3dc32cf34...](https://github.com/warriorstar-orion/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Sunday 2023-07-23 19:25:10 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [parasyte/Project64-Legacy](https://github.com/parasyte/Project64-Legacy)@[9cf39149b7...](https://github.com/parasyte/Project64-Legacy/commit/9cf39149b744d3901fdbf1f81dff58655547c4cb)
#### Sunday 2023-07-23 19:27:41 by Jay Oster

Remove Hidden Window and improve stability when resetting

The reset functionality is still very broken. Too many data races
between the GUI thread, CPU thread, and plugin threads.

This is at least a good start; resetting with F1 now works most of the
time. I can still get it to throw the "Emulation thread failed to
terminate plugins" error by hitting F1 ridiculously quickly with the
recompiler core. It doesn't seem to break as badly with the interpreter.

Anyway, yeah, this is just lack of synchronization causing havok.

The hidden window was some kind of ludicrous hack by a previous
contributor that attempted to hack around some other hacks, pile on some
more hacks to "fix" the broken hacks, and we get what we have today.

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[8744738e59...](https://github.com/spockye/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Sunday 2023-07-23 19:47:22 by Arturlang

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
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[bc6688baee...](https://github.com/spockye/Shiptest/commit/bc6688baee131600c94096642277d350ad6a59db)
#### Sunday 2023-07-23 20:21:36 by spockye

fixes wallmounts

And so I cry sometimes

when I'm lying in bed
Just to get it all out
what's in my head
And I...
I'm feelin',
a little peculiar

And so I wake in the morning
and I step outside
And I take a deep breath
and I get real high,
and I
scream from the top of my lungs
What's going on?

And I say,

hey ye yaae yae yaa,
hey ye yaae yaae
I said hey!
What's going on?
And I say,
hey ye yaae yae yaa,
hey ye yaae yaae
I said hey!
What's going ooooon?

[Spoken] AND HE TRIES

oh my god do I try
I try all the time,
in this institution

[Spoken] AND HE PRAYS!
Oh my god do I pray!
I pray every single day
[Spoken] MNYAAAAH!!
For a revolution!
WHOOOO!

And I say,

hey ye yaae yae yaa,
hey ye yaae yaae
I said hey!
What's going on?
And I say,
hey ye yaae yae yaa,
hey ye yaae yaae
I said hey!
Learn how to hide
your feelings
hey ye yaae yae yaa,
heeey ye yaae,
yaae yaae yaaeeh
I said hey!
What's going on?

YYEEEEEEEAAAAAAHHHH

---
## [wybczu/404.notrollsallowed.com](https://github.com/wybczu/404.notrollsallowed.com)@[c6752586be...](https://github.com/wybczu/404.notrollsallowed.com/commit/c6752586be0f57fb4ccfa3d9bd81c56eda0a1701)
#### Sunday 2023-07-23 20:41:19 by Łukasz Szczęsny

Smart Hom^WFarm

I will share my plan (not real experience yet - thanks pandemic!) for ways to
make life easier on a (small) farm. I will show you what FOS{H,S} can do for
us in this field.

---
## [mislavmatijevic/Ludoly](https://github.com/mislavmatijevic/Ludoly)@[441821fe85...](https://github.com/mislavmatijevic/Ludoly/commit/441821fe85eccd9a30d210da04455af75c731b15)
#### Sunday 2023-07-23 21:31:26 by Mislav Matijević

Refactor naming conventions and some minor logic fixes.
Now, they might say it ain't smart to commit a major refactor to a giant project before it is even functional.
But I'll say to them that I had no idea that private fields are really supposed to start with an underscore in C#, and that public fields should be PascalCase just like public properties.
Now, they might say I'm stupid, but I'll just say to them I made some amazing pancakes and am ready to continue to štrikati this project.
They might say it makes no sense to write such long commit messages, but I say thank you for reading and off I go back to make a cool game! :)

---
## [lupont/psh](https://github.com/lupont/psh)@[c0072a7fe1...](https://github.com/lupont/psh/commit/c0072a7fe1945fdc156fb1e2f6ecd50d36e7489c)
#### Sunday 2023-07-23 21:32:11 by Pontus Laos

feat: Recursive AST parsing in words (cmd sub) + more

NOTE: no command substitution is actually performed with this patch,
this is only internal parsing work. But it does make command
substitutions behave correctly in syntax highlighting!

This commit has been brewing for a while. I'm still lacking the
discipline, and as I now realize probably also the git know-how, to
separate this into the (probably quite a few) commits it deserves.
During my development work, I made _some_ half decent commit messages,
which I'm attaching to the end of this commit message for reference.

---

Much has changed in this commit, I don't think I'll be able to go into
details about all of it. I'll try my best to describe the main problem
it solves.

Previously, the `semtok` tokenizer had logic for figuring out when a
"Word" ended. This means quoting, backslash escaping, and even an
attempt at figuring out when we were in a command substitution
environment or arithmetic expression, and in what level. This was always
incorrect, ugly, and other negative adjectives. Instead, this is now all
done by the parser; the semtok module is quite a bit dumber, but it
allows the parser to recurse when a command substitution start (`$(`) is
encountered, by invoking the main parse method again. In order to figure
out when to stop, we check if the unparsed section of the command
substitution starts with a `)`, meaning that it's time to say "all
finished, let's continue on the layer above". This makes it easier to
deal with, grants more readable code, and perhaps most importantly for
the interactive shell: allows for correct syntax highlighting when
inside a command substitution. (note: the backtick variant of command
substitution is not at all supported yet)

With this patch, the `tok` and `semtok` modules are awfully similar,
bringing me a step closer to a goal I've had for quite some time now: to
remove one of them. Actually, the main reason for having both was that I
found it easier to deal with when I thought I had to find the start and
end of a "word" (as described above). Now I neither need that or even
want it, and it shows – since they have become so similar. One beautiful
day I will remove one.

In order to propagate errors from a command substitution, I also made
the switch to make the `Parser::parse` method have the return type of
`std::result::Result<SyntaxTree, std::result::Result<SyntaxTree,
ParseError>`. The `Ok(SyntaxTree)` case is a finished, good AST. The
`Err(Ok(SyntaxTree))` case is an unfinished syntax tree, while the
`Err(Err(ParseError))` case means that a syntax (or otherwise
unrecoverable) error occurred during parsing. I feel like this is both
kind of hideous, and kind of elegant at the same time. Though it also
makes me wish that the standard library defined a type alias like `type
Either<A, B> = Result<A, B>;`, just because the signature of the parse
method would become shorter. :-)

There are a few parts of the code base that I've been unhappy with
before, and have learned to be even unhappier with during this task. The
major one has to do with `Word`s. The fact that it contains two
variables, one with escaped newlines (pretty much only needed for syntax
highlighting/interactive use), and one without. This is unmaintainable,
ugly, and wasteful, since they are almost equivalent and are both
heap-allocated strings. Also, there's a bug with word expansion, in
which after quote removal, the known expansions' ranges don't get
updated. All of the `is_finished` logic I think I want to remove, in
favor of having that in the parser itself, and perhaps as a single
`finished: bool` field in the Word struct. Still thinking about it!

Even though this is by far my longest commit message to date (ever), I
know I'm probably missing quite a bit. But this was the reason for the
change, some implementation details, and some rant-y parts about how
unhappy I am with parts of the code base still. But to leave on a
positive note: this patch feels reeeally cool to use, seeing the syntax
highlighting in command substitution makes me very giddy. I've been
dreading the word recognition part for a very long time, and it has been
holding me back from other feature development since I want to have it
in a good, "finished" state. This brings us a lot closer to that! :-)

---

[1] WIP: parse word multiple times

In order to support a word being e.g. `$(cmd)hello$var`, we need to keep
parsing for acceptable SemanticTokens until none are left.

This rewrites parts of both Token and SemanticToken, to "dumb them
down", i.e. just keep the dollar symbol as a single token rather than
consuming them as part of a word.

[2] WIP: fix highlighting index offset

[3] WIP: looking better!

Previously, a `SemanticToken::Word` would contain single quotes, double
quotes, dollar signs, and equals signs. These have been removed, and are
now getting parsed in the AST parser instead. I think it makes more
sense and allows for finer control when parsing the input. It's also a
big step in the direction of completely removing the `Token` part of the
tokenizing, so hopefully soon we can rename the `SemanticToken` to
`Token` and skip the first part entirely. Because right now, Token and
SemanticToken are veeery similar.

[4] fix: Expand parameters into correct variable

Previously, variables were expanded on the `name` field of a Word. This
left the `name_with_escaped_newlines` field not being expanded. Instead,
do the expansions on the latter, and re-calculate the former based on
that.

Really need to figure out a better solution than having two fields. I
think the initial idea was to be backwards compatible, but I'm starting
to second guess that decision. What if we have a single `name` field,
that contains the escaped newlines, and then have a method for returning
it with those removed? Maybe that could work, will try it out in the
future. More pressing things now though :-)

[5] WIP: ugly single quote solution

ugly ugly ugly

[6] WIP: remove quoted string parsers from semtok

---
## [AngelHam/VIST489-Prototype1-Pizzazz](https://github.com/AngelHam/VIST489-Prototype1-Pizzazz)@[9ab727e9a3...](https://github.com/AngelHam/VIST489-Prototype1-Pizzazz/commit/9ab727e9a3a9538c16425057d5a47d0928552ee2)
#### Sunday 2023-07-23 21:56:33 by Angel Ham

Bugfix/Todo identification

Switcharoo Buglist/Todo/Finished

Sunday, July 23, 2023
10:51 AM

fixed:
	• Fixed bug where putting on air dash shoes after having double jump shoes would not show the air dash shiny shoes just the old ones with purple (they were over lapping, code was missing from the air dash upgrade bp)
	• playerball doesnt have the skin as main character.... ((Updated Set Skin function to take a SKM AntBot skeletal mesh so can do it for both meshes on the shop and player character mesh))
	• maybe make character IN PLAYERBALL more visible or somethign too?
	• Boxes should be pushable more so... if in area 2 i jump at fast speeds and they dont fall over something is wrong with the game :/
	• Area 2 first light puzzle needs to have its wire cosmetic reset its broken for some reason rn
	• Area 2 place default playerball position not on the roof lol but above the ceiling since players can walk up there
	• Trinket should be placed in one of the destroyable boxes outside area 2 puzzle with first light since unlikely for ppl to hit them
	• Area 2 Bridge, death level is too high, if i wait till like 50%+ of it falling down at start i can actually die while ontop of the bridge at the start
area 2 bridge lasers should be smaller/closer together inward... if you die right on the edge of the bridge you still retain input in your character walking around?? but the fact you can walk into them is weird on the bridge ((Fixed by moving ending platform 2000 in the y direction away))

todo:
• First person mode? camera slightly in front, triggered by zooming in all the way? could be nice --- ((changed min spring arm target length to be 0, at 0, we turn off the playermodel visuals..
	• Red particle attack is a lil buggy in this mode
• Elevator level sequencer pattern could just be too confusing, not a point to have it like that we could just simplify especially since its hard for new players to recognize the pattern + the jump in translation is shocking
• Settings page option that has the ability to alter how fast the camera pans when you look around
	• No sync between Pause Menu and Main Menu.. They slightly update but visually they are not set
	• Similar important issue, onLoad of next map, the settings for Camera Sensitivity, since it is tied to a newly loaded PlayerBot, do not save and revert to default
• 2nd shop, none of the items I purchased were saved??? (Quick remedy is to not show the shop again after area2...)

• Demo end: The main robot guy's text glitches the fuck out after he talks??
• GAME BREAKING BUG: Last puzzle is unsolvable? I put in first an incorrect solution, then a correct one, and the puzzle failed...

	• The 2nd puzzle in area 2 visual rips like with cosmetic stuff around
	• The first puzzle in area 2 backgrounds nearby glitch a bit
	• theres this small dark hole in area 1 underneath the platform the one where it doesnt have a dude underneath
	• Playerball faces a weird direction when traveling along the paths
Floor panels the area 2 puzzles (especially last puzzle need to be redone so they are alligned and straight)

---
## [an0rak-dev/avatar-engine](https://github.com/an0rak-dev/avatar-engine)@[28993cc092...](https://github.com/an0rak-dev/avatar-engine/commit/28993cc092d92224b94926776497e8fa40a194eb)
#### Sunday 2023-07-23 23:01:20 by Sylvain Nieuwlandt

Make robots double check my work to reduce inattention errors.

Again, it's been a while. Got myself caught in fleet of tasks to
handle, in my family or in my job.

But it was a good exercise, since I didn't touch the project for
a while. The result is that my coding conventions has slightly changed
and thus introduce differences in my new work. So, I decided to put
the pen down (or release the keyboard in our case ?), and take some
time to ensure a certain consistency in the codebase.

First thing first, let's stop using this basterized C++ which uses
only references and booleans, and no OOP or templates. If I want to
code in C, then I f****ng code in C, and I decided to rename all the
files to be treated as plain C source files.

Then, I configured a formater and a linter. Clang tools (clang-format
and clang-tidy) seems to be quite popular, and fortunately, they're
already present in every Visual Studio installation. And the windows
runners of GitHub contains an installation of Visual Studio, so win-win.

I've also added Doxygen, which more than the generation of the
documentation (I even don't use it at all, but I definitively should),
I use to make sure that every function, constant, or data structure
declare in a header file is properly documented.

The last part of a code Continuous Integration pipeline, is the testing.
And that was not so easy. Various frameworks already exists for testing
C code, but most of them are targeting first C++ code. GoogleTest might
be a good choice, but I'd prefer be send to eternal damndation in Hell
by listening a bunch of babies cry, rather than use a Google thing in
my project. Don't want to have a depenency shutted down in a year.

Finally, I decided to write my own, which is quite basic FTM, and is
contained in a single Header file. I will extract it in a dedicated
project later.

In fact, I thing that I'll extract the .clang-* and Doxygen configuration
and pipelines, as well as the test framework to a specific set of GitHub
actions. Purpose will be to use them easily in module implementation
repositories, and having all of the Avatar components sharing the same
conventions.

---
## [Maetrim/DDOBuilderV2](https://github.com/Maetrim/DDOBuilderV2)@[522542760f...](https://github.com/Maetrim/DDOBuilderV2/commit/522542760f14b70b6e58cd8673a25e2e99a3d3be)
#### Sunday 2023-07-23 23:58:14 by Maetrim

Build 2.0.0.5

Build 2.0.0.5

---The skills view now also shows the buffed total skill at your level (Skill Breakdown values)
---Gear Planner import files should now correctly import items with names like "Item name (Level x)"
---Diamond of Insightful <ability> augment values updated to match for Cannith crafted
---Gear Planner import files should now correctly import augments that have variable values (e.g. insightful con)
---All Fighter specific feats had their requirements changed to show the minimum required Fighter level (Reported by DODOCung)
---The Level 32/36/40 ability level up should now correctly apply (Reported by DODOCung)
---Stances pane should now draw correctly on stances revoked (Reported by DODOCung)
---"Frenzied Berserker: Power Rage" should now correctly apply for Shifter rages (Reported by DODOCung)
---"Legendary Dreadnought: Unparalleled Accuracy" no longer erroneously grants +15 PRR (Reported by DODOCung)
---Various effects that react to a Slider value have been fixed (Deific Warding) (Reported by DODOCung)
---Effects based of a Slider stack count will correctly revoke when the effect is revoked
---Effects based of a Slider will now correctly start with the correct number of stacks
---Feat "Perfect Two Weapon Fighting" updated to match wiki (Reported by DODOCung)
---A bug in hard requirement for an enhancement was fixed. (War Soul Divine Might has a red outline) (Reported by DODOCung)
---"War Soul: Divine Might" now correctly uses the Exclusive "Battle Trance" method
---Trance effects should now apply correctly (Reported by DODOCung)
---"Shiradi Champion" now has the correct background destiny bitmap (Reported by DODOCung)
---"Archer's Focus" and "Improved Precise Shot" moved into their own Stance group (Reported by DODOCung)
---All Battle Trances are now placed in the "Battle Trance" group
---All Battle trance bonuses should now update dynamically on total ability value changes
---"Shiradi Champion: Feywild Attunement" should now award Dodge based n the number of Wilderness Lore feats you have (Reported by DODOCung)
---Wilderness/Arcane/Religious Lore feats will now assign correctly for all levels
---"Tiefling: Bloodhunt II" no longer erroneous grants 1 Imbue dice (Reported by DODOCung)
---Training "Shiradi Champion: Pierce Deception"" and "Watchful Eye" will now award its 5% doubleshot (Reported by DODOCung)
---"Shiradi Champion: Fey Countenance" now gives the bonus 2 to saving throws vs. Spells. (Reported by DODOCung)
---"Scion of the Shadowfell" now grants its correct spell critical damage (Reported by DODOCung)
---"Primal Avatar" cores should now correctly award the full SpellPower bonuses (Reported by DODOCung)
---"Wellspring of Power", "Maximize", "Empower", "Intensify", "Epic/Legendary Power"" now award Universal Spell Power (Reported by DODOCung)
---"Wellspring of Power" spell critical damage is now Universal (Reported by DODOCung)
---"Tiefling: Incineration II" no longer erroneously grants 2% fire lore (Reported by DODOCung)
---Fate Points now correct contribute to your Spell points (Reported by DODOCung)
---Bad Shiradi images fixed
---Arcane Archer: Elemental Arrow III now correctly awards 1 imbue dice, not 2 (Reported by DODOCung)
---Bonus spell points should now correctly scale to Favored Soul/Sorcerer levels (Reported by DODOCung)
---Max Dex Bonus should now track correctly (Reported by DODOCung)
---Armor effects are now applied/revoked as stub function now implemented
---New requirement types "Race Construct" and "Not Construct" added, all armor updated
---Docent/Armors should now be auto unequipped when switching to an unsuitable race type
---Fire Elemental form now correctly awards 1 caster level, not 2 (Reported by DODOCung)
---Draconic Incarnation - Red Dragon breath now has the correct icon
---Draconic Incarnation Bloodlines spell powers should now stack to the correct values (Reported by DODOCung)
---Damage reduction values now show better in the DR breakdown (Reported by DODOCung)
---Blightcaster forms now all generate stances in Major Forms (Reported by DODOCung)
---The Builder will now start with a default life/build on startup/new document (Requested by DODOCung)
---Druidic Oath is now awarded to Blightcasters at level 1
---Spontaneous Casting is now awarded to Blightcasters at level 1
---Natural Fighting can now be trained by Blight Casters
---Veil the Elements is now awarded to Blight Casters
---Venom Immunity is now awarded to Blight Casters
---Thorn-Kin and Hive Master stances now have their effects (Reported by DODOCung)
---Plague Wolf and Blighted Wolf now have their effects (Reported by DODOCung)
---Epic/Legendary Knowledge feats now correctly grant 1 Max caster Level per acquisition
---Epic/Legendary Knowledge now grants caster levels for Acolyte of the Ski, Blight Caster and Dark Hunter (Reported by DODOCung)
---Max Caster Level breakdowns added as sub items of a given class caster level item
---"Pale Master: Spell Critical: Negative Energy II" no longer requires "Unknown enhancement" (Reported by nb756)
---Granted feats will now definitely clear on a New build/Life
---Cannith crafting augment options will no longer erroneously be filtered out now
---All Cannith crafting augments now have an icon
---All Cannith crafted items can now have up to 2 augment slots added to them

---

