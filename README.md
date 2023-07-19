## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-18](docs/good-messages/2023/2023-07-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,117,194 were push events containing 3,388,641 commit messages that amount to 276,163,958 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [dplanitzer/Apollo](https://github.com/dplanitzer/Apollo)@[10d9ded4f1...](https://github.com/dplanitzer/Apollo/commit/10d9ded4f1b64ac9353304b5919a5ce81d73f16d)
#### Tuesday 2023-07-18 00:03:18 by Dietmar Planitzer

Introduced try_bang() and added a comment explaining how to correctly call Lock_Lock() from inside a system call and outside of a system call context since it'll be probably suprising to most people that a lock operation can actually fail. But then what we're gona do... users kinda like it when a process actually terminates when they want to terminate it... and does it quick instead of sitting there and thinking about the purpose of life... like it's too common on Windows...

---
## [NiLuJe/koreader-base](https://github.com/NiLuJe/koreader-base)@[b0f7e99845...](https://github.com/NiLuJe/koreader-base/commit/b0f7e99845b16fc4176d3d29e4ffc258baa53cca)
#### Tuesday 2023-07-18 00:11:58 by NiLuJe

Build: RPATH & escaping cleanup (#1638)

* Stop everything from including crappy build-time rpaths into binaries (lookin' at you, libtool).
* Enforce a set of DT_RPATH on everything we build to ensure we prefer our own libs over the system's.
* Do so via an ld include file, in order to go through all the buildsystem bullshit in order to defeat potential escaping issues.
* In the same vein, rework how we escape things in both makefiles and CMake files, in order to limit the interaction and/or dependency on shell escaping and/or globbing.
* Enforce DT_RPATH over DT_RUNPATH, because it gets honored for transitive dependencies, which will avoid some hilariously stupid things from happening once we get rid of LD_LIBRARY_PATH, which this moves also allows us to do.

Many thanks to @benoit-pierre for his insight, testing and reviews, this would have been way clunkier without his input ;).

---------

Co-authored-by: Benoit Pierre <benoit.pierre@gmail.com>

---
## [ATH1909/tgstation](https://github.com/ATH1909/tgstation)@[746b75844c...](https://github.com/ATH1909/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Tuesday 2023-07-18 00:22:56 by necromanceranne

Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

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

---
## [ATH1909/tgstation](https://github.com/ATH1909/tgstation)@[9286933739...](https://github.com/ATH1909/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Tuesday 2023-07-18 00:22:56 by Jacquerel

Fixes some synthetic language oversights (#76846)

## About The Pull Request

#76305 removed the knowledge of every language from silicons, but this
had a couple of oversights.
This language set was not only used by cyborgs but also bots and vending
machines.

A couple of effects relied on them knowing all of those languages,
specifically their emp_act and also the station trait which rerolled
their languages.
Now they actually _learn_ a random language and start speaking it
instead.

Also I fixed a related runtime which I noticed in testing where a bot
would die as a result of being EMPed, delete itself, and then try and do
a bunch more shit after it stopped existing. Annoying.

Why was I looking at bot languages? Haha don't worry about it 😇 

## Why It's Good For The Game

Restores function of a funny feature.

## Changelog

:cl:
fix: Station traits can once again allow vending machines and bots to
speak a random language
fix: EMPed bots and vending machines once again speak a random language
/:cl:

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[74892ae7ec...](https://github.com/Derpguy3/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Tuesday 2023-07-18 00:24:14 by LemonInTheDark

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
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[63d6c2e962...](https://github.com/Derpguy3/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Tuesday 2023-07-18 00:24:14 by CRITAWAKETS

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
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[063bf74f31...](https://github.com/Derpguy3/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Tuesday 2023-07-18 00:24:14 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

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

---
## [rstrojan/AutoBattlerPrototype](https://github.com/rstrojan/AutoBattlerPrototype)@[06c226e450...](https://github.com/rstrojan/AutoBattlerPrototype/commit/06c226e45087223e4531554869992165ffdcf609)
#### Tuesday 2023-07-18 00:35:20 by rstrojan

Some Refactoring and Clean Up

After recently reading through Andrey Karpov's "60 terrible tips for a C++ developer", ( https://pvs-studio.com/en/blog/posts/cpp/1053/ ) I decided that it was time to review my code with a critical eye, and do some refactoring and clean up. A lot of the changes are to the formatting and style of the classes, intended to help with readability and clarity. Such as "tabelizing" my code. You'll see this in a lot of the constructors. A major theme through Karpov's article was about forgoing concise code for readable code. Tabelizing is going to increase the overall length of my code, but it's uniformity should make it easier to spot errors.
Another thing that I ended up doing was removing all of the ENUMs. This was a tip from Karpov's article, but I also found the ENUMs lacking as they showed up as ints in my JSON instead of their more meaningful string.
Units and Item both required significant work, particularly in removing the use of ENUMs. I also went through them and cleaned up a bunch of the declared stats that are now obselete thanks to statMaps. This last part was actually a cleanup from the implementation of statmaps. Oh, and I also updated the stat choice map for items, so that they give you some additional details about the item.

At this point, I'm relatively happy with the changes that I've made. However, most of the work that was done was only done for the GameObject classes. The other important classes of PrntScrn and Inventory did not get any love. I'm actually a little reticent to open them back up as I am not sure I'm going to really like what I see. lol. Any changes in there might spawn more changes and I'm not sure any of that stuff is high priority enough to consider right now. I'll probably do that when I get closer to the campaign loop being completed and I want to make sure that the UI looks good.
The next step that I'm going to do is a big one for me, personally. I'm going to move my project to C++ 20. This is another tip from Karpov, who encourages you to use the latest version of C++ because it has the most modern features and runs better/more efficient than older version. Most people, including me, have been told that you should use the older versions because your program is more readily compileable elsewhere. He said that this is not something that most projects need to consider. And if you do need to consider it, you are probably aware of that already. So, based on that advice, I'm moving to C++20 so I can utilize some more modern features. I'm not entirely sure what all I'll get (I'm currently use 14), so there may be more refactors in the future if I find anything cool.

---
## [rstrojan/AutoBattlerPrototype](https://github.com/rstrojan/AutoBattlerPrototype)@[330b939766...](https://github.com/rstrojan/AutoBattlerPrototype/commit/330b939766593cf27c415891d3817f1419cb032a)
#### Tuesday 2023-07-18 00:51:25 by rstrojan

Qa (#9)

* Add files via upload

* Started implementing the Game State object.

- GameState time. I started by moving the prepLoop inventories and GameObjects into the GameState object. I relearned a couple of things while doing. One I don't think I've dealt with since my first coding classes at Everett Community College, the other is something I've been kinda dreading.
- The first thing: Relearning about Constructor Initializer Lists. In my GS_Campaign class I need to have some Inventories. However, the constructor for those inventories need to be called in order to create them properly. So I couldn't simply declare it as "Inventory equipmentInv;" and start using it. It needs to call the Inventory(string name) constuructor. That simple declaration on the header file doesn't cut it. Previously, I had this done as part of the declaration in the header file.  it was "Inventory equipmentInv = Inventory("Equipment")". This would call the constructor properly. However, this is apparently not best practice. You don't want to do constructor calls as part of your declerations in your class header files. According to ChatGPT, the benefits are:
	- Improved performance: Initializing member variables in the constructor initialization list can be more efficient than initializing them in the constructor body, especially for complex objects.
	- Consistent initialization: Initialization lists ensure that member variables are always initialized to a valid state, even if an exception is thrown during construction.
	- Cleaner code: Initialization lists can make the code easier to read and understand, especially for classes with many member variables.
- I don't exactly know what it is more effecient, but I am sold none-the-less. Similar to doing the std:: namespace thing. It may feel weird at first, but I should get use to it and just make it part of how I opperate.
- Now, I will only put the declaration of the member variable in the header page Inventory equipmentInv. And then in the constructor, you would do this:
	GS_Campaign::GS_Campaign() :
	equipmentInv("Equipment")
	{};
- The other issue that came up (the thing I've been kinda dreading or at least was hoping to avoid) would be memory management involved in maintaining gameObjects. In order for my gameState to be able to create objects in its constructor and then also access those later, I need them to not be destroyed in the constructor. To do this, I have to use the "new" keyword, which allocates memory on the heap. However, that will also mean that I'm on the hook for deleting them. Now, I'm already planning on passing that object around mostly by pointer. In fact, Inventory is set up hold pointers. The easiest way to do this will be to use shared pointers. AKA smart pointers. These will maintain the object so long as the object has an existing reference pointing to it. If all of the pointers are destroyed, then the object will also be destroyed. Which is what I want. The question is going to be, how are these shared pointers going to be created?

* Inventory enhancement shared pointers (#8)

* Starting implementation of GameState object (#7)

* Add files via upload

* Started implementing the Game State object.

- GameState time. I started by moving the prepLoop inventories and GameObjects into the GameState object. I relearned a couple of things while doing. One I don't think I've dealt with since my first coding classes at Everett Community College, the other is something I've been kinda dreading.
- The first thing: Relearning about Constructor Initializer Lists. In my GS_Campaign class I need to have some Inventories. However, the constructor for those inventories need to be called in order to create them properly. So I couldn't simply declare it as "Inventory equipmentInv;" and start using it. It needs to call the Inventory(string name) constuructor. That simple declaration on the header file doesn't cut it. Previously, I had this done as part of the declaration in the header file.  it was "Inventory equipmentInv = Inventory("Equipment")". This would call the constructor properly. However, this is apparently not best practice. You don't want to do constructor calls as part of your declerations in your class header files. According to ChatGPT, the benefits are:
	- Improved performance: Initializing member variables in the constructor initialization list can be more efficient than initializing them in the constructor body, especially for complex objects.
	- Consistent initialization: Initialization lists ensure that member variables are always initialized to a valid state, even if an exception is thrown during construction.
	- Cleaner code: Initialization lists can make the code easier to read and understand, especially for classes with many member variables.
- I don't exactly know what it is more effecient, but I am sold none-the-less. Similar to doing the std:: namespace thing. It may feel weird at first, but I should get use to it and just make it part of how I opperate.
- Now, I will only put the declaration of the member variable in the header page Inventory equipmentInv. And then in the constructor, you would do this:
	GS_Campaign::GS_Campaign() :
	equipmentInv("Equipment")
	{};
- The other issue that came up (the thing I've been kinda dreading or at least was hoping to avoid) would be memory management involved in maintaining gameObjects. In order for my gameState to be able to create objects in its constructor and then also access those later, I need them to not be destroyed in the constructor. To do this, I have to use the "new" keyword, which allocates memory on the heap. However, that will also mean that I'm on the hook for deleting them. Now, I'm already planning on passing that object around mostly by pointer. In fact, Inventory is set up hold pointers. The easiest way to do this will be to use shared pointers. AKA smart pointers. These will maintain the object so long as the object has an existing reference pointing to it. If all of the pointers are destroyed, then the object will also be destroyed. Which is what I want. The question is going to be, how are these shared pointers going to be created?

* Converted Inventory.inv from ptrs to shared_ptrs.

- OK, today I'm going to try and change my Inventory class over from a list of regular pointers, to a list of shared_pointers or smart pointers as they are called. I had initially avoided these when I started, as I didn't quite understand why they were different. However, they have a major benefit over regular pointers, in that, when an object is created with a shared pointer, the shared pointer will keep track of how many other pointers are pointing to it. When there are no more pointers pointing to the object, the object will be destroyed. This is great, because for the GameState class to maintain objects, it needs to use the 'new' keyword and add them to the heap. The only way to get those objects off the heap is to destroy them. I could try to create some grand scheme for how this will work, but I don't actually need to, I can just let the shared pointers do that. Currently, the Inventory class keeps track of all it's objects as regular pointers, which means that I would have to handle destroying them. However, if I move them to shared pointers, then the objects will destroy themselves. So that's what we are gonna do.
- To do this, I'm going to need a new library that I have not used called <memory>.
- That was actually really easy! All I had to do was change the function declarations and definitions and the declaration of the objects themselves. I also streamlined the declaration of the objects in GS_Campaign so that I'm not declaring the obj first, then passing it. Now I declare it directly in the argument, which means I don't have an extra pointer inside of GS_Campaign.
- I would get into the techical details, but there really isn't that much difference between this and regular pointers. I just had to ask chatGPT a couple of syntax questions and now it's working.

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[18819cc7fb...](https://github.com/ritorizo/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Tuesday 2023-07-18 00:52:38 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [JMoldy/S.P.L.U.R.T-Station-13](https://github.com/JMoldy/S.P.L.U.R.T-Station-13)@[183f026a4a...](https://github.com/JMoldy/S.P.L.U.R.T-Station-13/commit/183f026a4a8f883201fcc408c6d42b97167545ac)
#### Tuesday 2023-07-18 00:53:02 by BongaTheProto

I'm sorry to interrupt you elizabeth

If you still even remember that name.
But I'm afraid you've been misinformed.
You are not here to receive a gift.
Nor, have you been called here by the individual you assume.
Although, you have indeed been called.
You have all been called here.
Into a labyrinth of sounds and smells, misdirection and misfortune.
A labyrinth with no exit, a maze with no prize.
You don't even realize that you are trapped.
Your lust of blood has driven you in endless circles.
Chasing the cries of children in some unseen chamber.
Always seeming so near, yet somehow out of reach.
But, you will never find them, none of you will.
This is where your story ends.

And to you, my brave volunteer.
Who somehow found this job listing not intended for you.
Although, there was a way out planned for you,
I have a feeling that's not what you want.
I have a feeling that you are right where you want to be.

I am remaining as well. I am nearby.
This place will not be remembered.
And the memory of everything that started this.
Can finally begin to fade away.
As the agony of every tragedy should.
And to you monsters trapped in the corridors.
Be still, and give up your spirits.
They don't belong to you.
For most of you, I believe there is peace and perhaps, warm.
Waiting for you after the smoke clears.
Although, for one of you.
The darkest pit of Hell has opened to swallow you whole.
So, don't keep the Devil waiting, old friend.
My daughter, if you can hear me.
I knew you would return as well.
It's in your nature to protect the innocent.
I'm sorry that on that day.
The day you were shut out and left to die.
No one was there to lift you up in their arms.
The way you lifted others into yours.
And then, what became of you?
I should have known, you wouldn't be content to disappear.
Not my daughter. I couldn't save you then, so let me save you now.
It's time to rest, for you, and for those you have carried in your arms.

---
## [JMoldy/S.P.L.U.R.T-Station-13](https://github.com/JMoldy/S.P.L.U.R.T-Station-13)@[defdf2f6b2...](https://github.com/JMoldy/S.P.L.U.R.T-Station-13/commit/defdf2f6b2269cd8fc953ef71219109159ddfcd4)
#### Tuesday 2023-07-18 00:53:02 by PhazeJump

FIXING MY OWN SHIT CODE MAKES ME FUCKING SCREAM

anyways
techpriest robes are now un-shitty-fixed and fixed again. Should be working properly now. No idea how to get the naga taur sprite working because it was supposed to be added in sand modular but sand modular was the one breaking it all so :shrug:

---
## [RalphHightower/semantic-kernel](https://github.com/RalphHightower/semantic-kernel)@[eab7a8f63a...](https://github.com/RalphHightower/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Tuesday 2023-07-18 01:01:36 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [YesterdaysPromise/tgstation](https://github.com/YesterdaysPromise/tgstation)@[a8e0d7c8d2...](https://github.com/YesterdaysPromise/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Tuesday 2023-07-18 01:21:09 by MrMelbert

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[9701b40ca0...](https://github.com/Stalkeros2/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Tuesday 2023-07-18 01:53:50 by SkyratBot

[MIRROR] Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[2303c452c7...](https://github.com/Stalkeros2/Skyrat-tg/commit/2303c452c79a8563076a58ad7e9d9346186a7e7c)
#### Tuesday 2023-07-18 01:53:50 by SkyratBot

[MIRROR] Rat RP expansion [MDB IGNORE] (#22204)

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
## [trent-s/benchmarkxla](https://github.com/trent-s/benchmarkxla)@[745644f391...](https://github.com/trent-s/benchmarkxla/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Tuesday 2023-07-18 02:03:59 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [GH-Rake/GH-Injector-Library](https://github.com/GH-Rake/GH-Injector-Library)@[ec80ed4849...](https://github.com/GH-Rake/GH-Injector-Library/commit/ec80ed4849c1a3fb2236f0a8b5f795c5f653be17)
#### Tuesday 2023-07-18 02:21:39 by Broihon

welcome back Download Manager, fucking std::async doesn't send messages to dll mains, i hate bill, this shit might prevent deadlocking download threads when exiting during download

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[e8930f5a26...](https://github.com/vdaular-dev/linksfordevs/commit/e8930f5a267083397149032f5189514d0e77acd0)
#### Tuesday 2023-07-18 03:27:28 by Ben Dornis

Updating: 7/17/2023 10:00:00 PM

 1. Added: I
found a (microscopic) ruby bug and it got fixed in 3 hours
    (https://pineman.github.io/ruby-bug-shell-gem.html)
 2. Added: Baby's second garbage collector
    (https://jennyjams.net/blog/copygc/)
 3. Added: Programming Pearls
    (https://book-notes.pages.dev/programming-pearls/)
 4. Added: Writing for Others
    (https://notes.npilk.com/writing-for-others)
 5. Added: Matt Watson | Let me live dangerously, PHP
    (https://www.mattwatson.org/blog/20230716-let-me-live-dangerously-php/)
 6. Added: Setting up PostgreSQL with Ansible
    (https://rischmann.fr/blog/setting-up-postgresql-with-ansible)
 7. Added: Looking for additional maintainers on a few projects
    (https://blog.yossarian.net/2023/07/16/Looking-for-additional-maintainers-on-a-few-projects)
 8. Added: Why kernel drivers in Anti-Cheat aren't so bad
    (https://blog.levitati.ng/articles/6)
 9. Added: Has anyone thought that WFH is just sustainable?
    (https://jetunsetter.com/2023/07/17/has-anyone-thought-that-wfh-is-just-sustainable/)
10. Added: Stop Overengineering
    (https://matt-rickard.com/stop-overengineering)
11. Added: Hamilton’s Quaternions, or, The Trouble with Triples
    (https://mathenchant.wordpress.com/2023/05/17/hamiltons-quaternions-or-the-trouble-with-triples/)
12. Added: Using XPath in 2023
    (https://denizaksimsek.com/2023/xpath/)
13. Added: My two semesters of teaching
    (https://avikdas.com/2023/07/17/my-two-semesters-of-teaching.html)
14. Added: Store age identities inside the TPM: age-plugin-tpm
    (https://linderud.dev/blog/store-age-identities-inside-the-tpm-age-plugin-tpm/)
15. Added: Trophy Jobs
    (https://anuatluru.com/blog/trophyjobs)
16. Added: Let me talk to my algorithms
    (https://blog.erlend.sh/let-me-talk-to-my-algorithms)
17. Added: ASP.NET Community Standup | Reliable web app pattern for .NET
    (https://youtu.be/_dkUZZP8uZY)
18. Added: On .NET Live - Getting Started with ChatGPT in .NET
    (https://youtube.com/watch?v=TXjcssxdA5M)
19. Added: Azure DevOps at a Glance
    (https://jinget.medium.com/azure-devops-at-a-glance-4319d94c26e4)
20. Added: Announcing the HackTogether: Microsoft Teams Global Hack winners - Microsoft 365 Developer Blog
    (https://devblogs.microsoft.com/microsoft365dev/announcing-the-hacktogether-microsoft-teams-global-hack-winners/)

Generation took: 00:09:17.8454578

---
## [filibuster-testing/filibuster-java-instrumentation](https://github.com/filibuster-testing/filibuster-java-instrumentation)@[378353a6c4...](https://github.com/filibuster-testing/filibuster-java-instrumentation/commit/378353a6c440208e90134da2e156718f0db560eb)
#### Tuesday 2023-07-18 04:20:26 by Christopher Meiklejohn

Fuck this stupid ass library and it's race conditions.

---
## [PRO-COINMARKETCAP/graphql.github.io](https://github.com/PRO-COINMARKETCAP/graphql.github.io)@[25f3678c32...](https://github.com/PRO-COINMARKETCAP/graphql.github.io/commit/25f3678c324dd9ca4e3fca7ba724ae3092643ec2)
#### Tuesday 2023-07-18 04:24:17 by PRO-COINMARKETCAP

xmr.monero.price.com

@import "_css/automattic.price"; @import "_css/graphql.price"; @import "_css/index.price"; @import "_css/docs.price"; @import "_css/users.price"; @import "_css/prism.price"; @import "_css/codemirror.price"; @import "_css/algolia.price"; @import "_css/code.price"; @import "_css/faq.price"; @import "_css/foundation.price"; @import "_css/brand.price"; @import "_css/HomeAbout.price";  @import "_rss/automattic.price"; @import "_rss/graphql.price"; @import "_rss/index.price"; @import "_rss/docs.price"; @import "_rss/users.price"; @import "_rss/prism.price"; @import "_rss/codemirror.price"; @import "_rss/algolia.price"; @import "_rss/code.price"; @import "_rss/faq.price"; @import "_rss/foundation.price"; @import "_rss/brand.price"; @import "_rss/HomeAbout.price"; @import "_css/automattic.price"; @import "_css/graphql.price"; @import "_css/index.price"; @import "_css/docs.price"; @import "_api/users.price"; @import "_api/prism.price"; @import "_api/codemirror.price"; @import "_api/algolia.price"; @import "_api/code.price"; @import "_api/faq.price"; @import "_api/foundation.price"; @import "_api/brand.price"; @import "_api/HomeAbout.price"; @import "_cpc/automattic.price"; @import "_cpc/graphql.price"; @import "_cpc/index.price"; @import "_cpc/docs.price"; @import "_cpc/users.price"; @import "_cpc/prism.price"; @import "_cpc/codemirror.price"; @import "_cpc/algolia.price"; @import "_cpc/code.price"; @import "_cpc/faq.price"; @import "_cpc/foundation.price"; @import "_cpc/brand.price"; @import "_cpc/HomeAbout.price"; @import "_xmr/automattic.price"; @import "_xmr/graphql.price"; @import "_xmr/index.price"; @import "_xmr/docs.price"; @import "_xmr/users.price"; @import "_xmr/prism.price"; @import "_xmr/codemirror.price"; @import "_xmr/algolia.price"; @import "_xmr/code.price"; @import "_xmr/faq.price"; @import "_xmr/foundation.price"; @import "_xmr/brand.price"; @import "_xmr/HomeAbout.price";   #UsNewsWork With Us  #Privacy Policy Your privacy is critically important to us. At Automattic, we have a few fundamental principles:  We are thoughtful about the personal information we ask you to provide and the personal information that we collect about you through the operation of our services. We store personal information for only as long as we have a reason to keep it. We aim to make it as simple as possible for you to control what information on your website is shared publicly (or kept private), indexed by search engines, and permanently deleted. We help protect you from overreaching government demands for your personal information. We aim for full transparency on how we gather, use, and share your personal information. Below is our Privacy Policy, which incorporates and clarifies these principles.  Who We Are and What This Policy Covers Howdy! We are the folks behind a variety of products and services designed to allow anyone — from bloggers, to photographers, small business owners, and enterprises — to take full advantage of the power and promise of the open web. Our mission is to democratize publishing and commerce so that anyone with a story can tell it, and anyone can turn their great idea into a livelihood. We believe in powering the open internet with code that is open source and are proud to say that the vast majority of our work is available under the General Public License (“GPL”). Unlike most other services, because our GPL code is public, you can actually download and take a look at that code to see how it works.  This Privacy Policy applies to information that we collect about you when you use:  Our websites (including automattic.com, wordpress.com, jetpack.com, woocommerce.com, crowdsignal.com, gravatar.com, intensedebate.com, vaultpress.com, akismet.com, simplenote.com, simperium.com, leandomainsearch.com, cloudup.com, longreads.com, atavist.com, mailpoet.com, automatewoo.com, jetpackcrm.com, happy.tools, wpcourses.com, wpscan.com, newspack.pub, and wp.cloud); Our mobile applications (including the WordPress mobile app for Android and iOS); Our other Automattic products, services, and features that are available on or through our websites (for example, WordPress.com plans, the Payments feature, the Pay with PayPal block, WordPress.com, Jetpack, the WooCommerce Shipping & Tax extension, Gravatar, the IntenseDebate comment management system, Akismet plans, Simplenote, Simperium, Cloudup, Longreads, MailPoet, AutomateWoo, Jetpack CRM, Happy Tools, WordPress.com Courses, WPScan and Newspack); and Other users’ websites that use our Services, while you are logged in to your account with us. This Privacy Policy also applies to information we collect when you apply for a job at Automattic or one of our subsidiaries.  Throughout this Privacy Policy we’ll refer to our websites, mobile applications, and other products and services collectively as “Services.” And if you’d like to learn more about which Automattic company is the controller of information about you, take a look at the section below on Controllers and Responsible Companies.  Please note that this Privacy Policy does not apply to any of our products or services, like Tumblr, that have a separate privacy policy.  Below we explain how we collect, use, and share information about you, along with the choices that you have with respect to that information.  Creative Commons Sharealike License We’ve decided to make this Privacy Policy available under a Creative Commons Sharealike license. You can grab a copy of this Privacy Policy and other legal documents on GitHub. You’re more than welcome to copy it, adapt it, and repurpose it for your own use. Just make sure to revise the language so that your policy reflects your actual practices. If you do use it, we’d appreciate a credit and link to Automattic somewhere on your site.  Information We Collect We only collect information about you if we have a reason to do so — for example, to provide our Services, to communicate with you, or to make our Services better.  We collect this information from three sources: if and when you provide information to us, automatically through operating our Services, and from outside sources. Let’s go over the information that we collect.  Information You Provide to Us It’s probably no surprise that we collect information that you provide to us directly. Here are some examples:  Basic account information: We ask for basic information from you in order to set up your account. For example, we require individuals who sign up for a WordPress.com account to provide an email address and password, along with a username or name — and that’s it. You may provide us with more information — like your address and other information you want to share — but we don’t require that information to create a WordPress.com account. Public profile information: If you have an account with us, we collect the information that you provide for your public profile. For example, if you have a WordPress.com account, your username is part of that public profile, along with any other information you put into your public profile, like a photo or an “About Me” description. Your public profile information is just that — public — so please keep that in mind when deciding what information you would like to include. Payment and contact information: There are various ways in which you may provide us payment information and associated contact information. For example, if you buy something from us or earn revenue through your site, we’ll collect information to process those payments and contact you. If you buy something from us — a subscription to a WordPress.com plan, a premium theme, a custom domain, some Longreads swag — or if you pay fees to a person or business through their WordPress.com site (for example via the Payments feature or the Pay with PayPal block), you’ll provide additional personal and payment information like your name, credit card information, and contact information. We also keep a record of the purchases you’ve made. If you use our Ecommerce Services (including Store on WordPress.com, WooCommerce Shipping & Tax, and WooCommerce Payments), you’ll have to create a WordPress.com account or connect an existing account and, for some Services, provide your site URL. You may also provide us with financial details to set up a payments integration, like the email address for your Stripe or PayPal account or your bank account information. Additionally, if you use WooPay to make purchases on other sites, we will store the contact information and payment information you provide to that service. And if you participate in a revenue sharing opportunity for your site, like WordAds, you’ll provide some additional information — for example, a tax ID or other identifier so we can process payments to you. Business Profile: Some of our products collect additional information from you as part of creating a user/customer profile. For example, if you are a Jetpack CRM customer we may add you to our customer relationship database (powered by Jetpack CRM!) using information you provide us including your name, your employer, your job title or role, your contact information, and your communications with us. If you are a Happy Tools user, we use information you provide us like your timezone and location information, your company and team information, and your contact information, to set up your account and power the Service’s features. Content information: You might provide us with information about you in draft and published content (a blog post or comment that includes biographic information about you, or any media or files you upload). Credentials: Depending on the Services you use, you may provide us with credentials for your self-hosted website (like SSH, FTP, and SFTP username and password). Jetpack and VaultPress users may provide us with these credentials in order to use our one-click restore feature if there is a problem with their site, or to allow us to troubleshoot problems more quickly. Communications with us (hi there!): You may also provide us with information when you respond to surveys, communicate with our Happiness Engineers about a support question, post a question in our public forums, or sign up for a newsletter like the one we send through Longreads. When you communicate with us via form, email, phone, WordPress.com comment, or otherwise, we store a copy of our communications (including any call recordings as permitted by applicable law). Job applicant information: If you apply for a job with us — awesome! You may provide us with information like your name, contact information, resume or CV, professional or personal references, similar professional and employment-related data, and work authorization verification as part of the application process. We may also collect additional information about you during the process, like background and credit checks (in applicable jurisdictions and only for certain job roles).  You may also provide us with demographic information when required by law or to support our diverse workplace initiatives, such as your gender, racial or ethnic origin, veteran status, and disability status if you voluntarily submit such information as part of your application. We collect demographic information in accordance with applicable law, and do not request demographic information in jurisdictions where it may be prohibited. We will only use this sensitive information to accommodate a disability or illness, comply with legal obligations, protect the health and safety of our employees, and facilitate our internal programs relating to diversity, inclusion, and anti-discrimination. Information We Collect Automatically We also collect some information automatically:  Log information: Like most online service providers, we collect information that web browsers, mobile devices, and servers typically make available, including the browser type, IP address, unique device identifiers, language preference, referring site, the date and time of access, operating system, and mobile network information. We collect log information when you use our Services — for example, when you create or make changes to your website on WordPress.com. Transactional information: When you make a purchase through our Services, we collect information about the transaction, such as product details, purchase price, and the date and location of the transaction. This includes when you purchase something we sell or when you use our Services (like WooPay) to buy something from a third party. Usage information: We collect information about your usage of our Services. For example, we collect information about the actions that site administrators and users perform on a site using our WordPress.com or Jetpack services — in other words, who did what and when (e.g., [WordPress.com username] deleted “[title of post]” at [time/date]). Our WooCommerce Usage Tracker also tracks information like your email address, WooCommerce settings, and PHP settings, along with information about your online store, like the aggregate number of orders and customers. We also collect information about what happens when you use our Services (e.g., page views, support document searches at en.support.wordpress.com, features enabled for your website, interactions with our Admin Bar and other parts of our Services) along with information about your device (e.g., screen size, name of cellular network, and mobile device manufacturer). We use this information to, for example, provide our Services to you, get insights on how people use our Services so we can make our Services better, and understand and make predictions about user retention. Location information: We may determine the approximate location of your device from your IP address. We collect and use this information to, for example, calculate how many people visit our Services from certain geographic regions. We may also collect information about your precise location via our mobile apps (like when you post a photograph with location information) if you allow us to do so through your mobile device operating system’s permissions. Stored information: We may access information stored on your mobile device via our mobile apps. We access this stored information through your device operating system’s permissions. For example, if you give us permission to access the photographs on your mobile device’s camera roll, our Services may access the photos stored on your device when you upload a really amazing photograph of the sunrise to your website. Interactions with other users’ sites: We collect some information about your interactions with other users’ sites while you are logged in to your account with us, such as your “Likes” and the fact that you commented on a particular post, so that we can, for example, recommend posts we think may interest you. As another example, we collect information about the comments IntenseDebate users make while logged in and use that information to, for example, tally up statistics about your comments (check them out in your dashboard!) and display information about your comments in your IntenseDebate public profile. Information from cookies & other technologies: A cookie is a string of information that a website stores on a visitor’s computer, and that the visitor’s browser provides to the website each time the visitor returns. Pixel tags (also called web beacons) are small blocks of code placed on websites and emails. Automattic uses cookies and other technologies like pixel tags to help us identify and track visitors, usage, and access preferences for our Services, as well as track and understand email campaign effectiveness and to deliver targeted ads. For more information about our use of cookies and other technologies for tracking, including how you can control the use of cookies, please see our Cookie Policy. Information We Collect from Other Sources We may also get information about you from other sources. For example:  Third Party Login: If you create or log in to your WordPress.com account through another service (like Google) we’ll receive associated login information (e.g. a connection token, your username, your email address) Social Sharing Services: If you connect your website or account to a social media service (like Twitter) through our Publicize feature, we’ll receive information from that service (e.g., your username, basic profile information, friends list) via the authorization procedures for that service. Financial Account Info: If you use WooCommerce Payments, we’ll receive information relating to your Stripe account, such as your email address and phone number. If you use WooPay, we’ll receive your payment information from Stripe. Google Account Information: When you connect your Google account to your Newspack powered site, we may access certain Google user data such as your Google Ad Manager Configuration (the network code and your ad units) and your Google Analytics data to allow you to access and manage features more seamlessly. For example, you may be able to manage your Google ads and see your Google Analytics data directly within the dashboard of your Newspack powered site. The information we receive depends on which services you use or authorize and what options are available.  Third-party services may also give us information, like mailing addresses for individuals who are not yet our users (but we hope will be!). We use this information for marketing purposes like postcards and other mailers advertising our Services.  How and Why We Use Information Purposes for Using Information We use information about you for the purposes listed below:  To provide our Services. For example, to set up and maintain your account, host your website, backup and restore your website, provide customer service, process payments and orders, and verify user information. To ensure quality, maintain safety, and improve our Services. For example, by providing automatic upgrades and new versions of our Services. Or, for example, by monitoring and analyzing how users interact with our Services so we can create new features that we think our users will enjoy and that will help them create and manage websites more efficiently or make our Services easier to use. To place and manage ads in our advertising program. For example, to place ads on our users’ sites and some of our own sites as part of our advertising program, and understand ad performance. To market our Services and measure, gauge, and improve the effectiveness of our marketing. For example, by targeting our marketing messages to groups of our users (like those who have a particular plan with us or have been users for a certain length of time), advertising our Services, analyzing the results of our marketing campaigns (like how many people purchased a paid plan after receiving a marketing message), and understanding and forecasting user retention. To protect our Services, our users, and the public. For example, by detecting security incidents; detecting and protecting against malicious, deceptive, fraudulent, or illegal activity; fighting spam; complying with our legal obligations; and protecting the rights and property of Automattic and others, which may result in us, for example, declining a transaction or terminating Services. To fix problems with our Services. For example, by monitoring, debugging, repairing, and preventing issues. To customize the user experience. For example, to personalize your experience by serving you relevant notifications and advertisements for our Services, recommending content through our Reader post suggestions, and providing new essays and stories through Longreads for your reading pleasure. To communicate with you. For example, by emailing you to ask for your feedback, share tips for getting the most out of our products, or keep you up to date on Automattic; texting you to verify your payment; or calling you to share offers and promotions that we think will be of interest to you. If you don’t want to hear from us, you can opt out of marketing communications at any time. (If you opt out, we’ll still send you important updates relating to your account.) To recruit and hire new Automatticians. For example, by evaluating job applicants (including verifying their identity, experience, and other information submitted) and communicating with them by phone, email, or social media platforms.  If the application progresses, we may also collect interview information and background check information.  This may also include verifying information required to initiate employment, for purposes such as confirming ability to legally work in a specific location, setting up payroll, and complying with statutory reporting requirements. Legal Bases for Collecting and Using Information A note here for those in the European Union about our legal grounds for processing information about you under EU data protection laws, which is that our use of your information is based on the grounds that:  (1) The use is necessary in order to fulfill our commitments to you under the applicable terms of service or other agreements with you or is necessary to administer your account — for example, in order to enable access to our website on your device or charge you for a paid plan; or  (2) The use is necessary for compliance with a legal obligation; or  (3) The use is necessary in order to protect your vital interests or those of another person; or  (4) We have a legitimate interest in using your information — for example, to provide and update our Services; to improve our Services so that we can offer you an even better user experience; to safeguard our Services; to communicate with you; to measure, gauge, and improve the effectiveness of our advertising; and to understand our user retention and attrition; to monitor and prevent any problems with our Services; and to personalize your experience; or  (5) You have given us your consent — for example before we place certain cookies on your device and access and analyze them later on, as described in our Cookie Policy.  Sharing Information How We Share Information We share information about you in limited circumstances, and with appropriate safeguards on your privacy. These are spelled out below, as well as in the section called Ads and Analytics Services Provided by Others:  Subsidiaries and independent contractors: We may disclose information about you to our subsidiaries and independent contractors who need the information to help us provide our Services or process the information on our behalf. We require our subsidiaries and independent contractors to follow this Privacy Policy for any personal information that we share with them. Third-party vendors: We may share information about you with third-party vendors who need the information in order to provide their services to us, or to provide their services to you or your site. This includes vendors that help us provide our Services to you (like Stripe, which powers WooCommerce Payments, payment providers that process your credit and debit card information, payment providers you use for your own ecommerce operations, fraud prevention services that allow us to analyze fraudulent payment transactions, cloud storage services, postal and email delivery services that help us stay in touch with you, customer chat and email support services that help us communicate with you, registrars, registries, data escrow services that allow us to provide domain registration services, and your hosting provider if your site is not hosted by Automattic); those that assist us with our marketing efforts (e.g., by providing tools for identifying a specific marketing target group or improving our marketing campaigns, and by placing ads to market our services); those that help us understand and enhance our Services (like analytics providers); those that make tools to help us run our operations (like programs that help us with task management, scheduling, word processing, email and other communications, and collaboration among our teams); other third-party tools that help us manage operations; and companies that make products available on our websites (like the extensions on WooCommerce.com), who may need information about you in order to, for example, provide technical or other support services to you. We require vendors to agree to privacy commitments in order to share information with them. Other vendors are listed in our more specific policies (e.g., our Cookie Policy). Legal and regulatory requirements: We may disclose information about you in response to a subpoena, court order, or other governmental request. For more information on how we respond to requests for information about WordPress.com users, please see our Legal Guidelines. Additionally, if you have a domain registered with WordPress.com, we may share your information to comply with the Internet Corporation for Assigned Names and Numbers’ (ICANN) regulations, rules, or policies. For example, your information relating to your domain registration may be available in the WHOIS database, or we may be required to share your information with ICANN-approved Dispute Resolution Service Providers. Please see our Domain Registrations and Privacy support document for more details. To protect rights, property, and others: We may disclose information about you when we believe in good faith that disclosure is reasonably necessary to protect the property or rights of Automattic, third parties, or the public at large. For example, if we have a good faith belief that there is an imminent danger of death or serious physical injury, we may disclose information related to the emergency without delay. Business transfers: In connection with any merger, sale of company assets, or acquisition of all or a portion of our business by another company, or in the unlikely event that Automattic goes out of business or enters bankruptcy, user information would likely be one of the assets that is transferred or acquired by a third party. If any of these events were to happen, this Privacy Policy would continue to apply to your information and the party receiving your information may continue to use your information, but only consistent with this Privacy Policy. With your consent: We may share and disclose information with your consent or at your direction. For example, we may share your information with third parties when you authorize us to do so, like when you connected your site to a social media service through our Publicize feature. Aggregated or de-identified information: We may share information that has been aggregated or de-identified, so that it can no longer reasonably be used to identify you. For instance, we may publish aggregate statistics about the use of our Services, or share a hashed version of your email address to facilitate customized ad campaigns on other platforms. Site owners: If you have a WordPress.com account and interact with another site using our Services, your information may be shared with the administrators of the site. For example, if you leave a comment on a site created on WordPress.com or running Jetpack, your IP address and the email address associated with your WordPress.com account may be shared with the administrator(s) of the site where you left the comment. Or if you make a payment (like via the Payments feature) to a site, your public display name, user name, and email address may be shared with the administrator(s) of the site. Or if you follow/subscribe to another WordPress.com site we will share your email address with the site owner. Published support requests: If you send us a request for assistance (for example, via a support email or one of our other feedback mechanisms), we reserve the right to publish that request in order to clarify or respond to your request, or to help us support other users. Information Shared Publicly Information that you choose to make public is — you guessed it — disclosed publicly.  That means information like your public profile, posts, other content that you make public on your website, and your “Likes” and comments on other websites are all available to others — and we hope they get a lot of views!  For example, the photo that you upload to your public profile, or a default image if you haven’t uploaded one, is your Globally Recognized Avatar, or Gravatar — get it? :) Your Gravatar, along with other public profile information, displays alongside the comments and “Likes” that you make on other users’ websites while logged in to your WordPress.com account. Your Gravatar and public profile information may also display with your comments, “Likes,” and other interactions on websites that use our Gravatar service, if the email address associated with your account is the same email address you use on the other website.  We also provide a “Firehose” stream of public data (like posts and comments) from some sites that use our Services to provide that data to Firehose subscribers, who may view and analyze the content (all subject to our Terms of Service), but do not have rights to re-publish it publicly. Find out more about opting out of the Firehose for WordPress.com and Jetpack sites. Public information may also be indexed by search engines or used by third parties.  Please keep all of this in mind when deciding what you would like to share publicly.  How Long We Keep Information We generally discard information about you when it’s no longer needed for the purposes for which we collect and use it — described in the section above on How and Why We Use Information — and we’re not legally required to keep it.  For example, we keep web server logs that record information about a visitor to one of Automattic’s websites, like the visitor’s IP address, browser type, and operating system, for approximately 30 days. We retain the logs for this period of time in order to, among other things, analyze traffic to Automattic’s websites and investigate issues if something goes wrong on one of our websites.  As another example, when you delete a post, page, or comment from your WordPress.com site, it stays in your Trash folder for thirty days in case you change your mind and would like to restore that content, because starting from scratch is no fun. After the thirty days are up, the deleted content may remain on our backups and caches until purged.  If you are a job applicant, we will keep your personal data during the application process, and for a certain period thereafter. To determine that period, we take into account a number of factors, like our legal and regulatory obligations (such as equal opportunity obligations) and whether we may need to retain personal data for internal business purposes like analyzing our applicant pool.  Security While no online service is 100% secure, we work very hard to protect information about you against unauthorized access, use, alteration, or destruction, and take reasonable measures to do so. We monitor our Services for potential vulnerabilities and attacks.  To enhance the security of your account, we encourage you to enable our advanced security settings, like Two Step Authentication.  Choices You have several choices available when it comes to information about you:  Limit the information that you provide: If you have an account with us, you can choose not to provide the optional account information, profile information, and transaction and billing information. Please keep in mind that if you do not provide this information, certain features of our Services — for example, premium themes that carry an additional charge — may not be accessible. If you are a job applicant, and you choose not to provide certain data elements to us, we may not be able to proceed with the recruitment process. Limit access to information on your mobile device: Your mobile device operating system should provide you with the option to discontinue our ability to collect stored information or location information via our mobile apps. If you choose to limit this, you may not be able to use certain features, like geotagging for photographs. Opt out of marketing communications: You may opt out of receiving promotional communications from us. Just follow the instructions in those communications or let us know. If you opt out of promotional communications, we may still send you other communications, like those about your account and legal notices. Set your browser to reject cookies: At this time, Automattic does not respond to “do not track” signals across all of our Services. However, you can usually choose to set your browser to remove or reject browser cookies before using Automattic’s websites, with the drawback that certain features of Automattic’s websites may not function properly without the aid of cookies. Opt out of our internal analytics program: You can do this through your user settings. By opting out, you will stop sharing information with our analytics tool about events or actions that happen after the opt-out, while you’re logged in to your WordPress.com account. For more information, please see our Cookie Policy. Close your account: While we’d be very sad to see you go, you can close your account if you no longer want to use our Services. (Here are account closure instructions for WordPress.com accounts.) Please keep in mind that we may continue to retain your information after closing your account, as described in How Long We Keep Information above — for example, when that information is reasonably needed to comply with (or demonstrate our compliance with) legal obligations such as law enforcement requests, or reasonably needed for our legitimate business interests. Your Rights If you are located in certain parts of the world, including some US states and countries that fall under the scope of the European General Data Protection Regulation (aka the “GDPR”), you may have certain rights regarding your personal information, like the right to request access to or deletion of your data.  European General Data Protection Regulation (GDPR) If you are located in a country that falls under the scope of the GDPR, data protection laws give you certain rights with respect to your personal data, subject to any exemptions provided by the law, including the rights to:  Request access to your personal data; Request correction or deletion of your personal data; Object to our use and processing of your personal data; Request that we limit our use and processing of your personal data; and Request portability of your personal data. You also have the right to make a complaint to a government supervisory authority.  US Privacy Laws Laws in some US states, including California, Colorado, Connecticut, Utah, and Virginia, require us to provide residents with additional information about the categories of personal information we collect and share, where we get that personal information, and how and why we use it. You’ll find that information in this section (if you are a California resident, please note that this is the Notice at Collection we are required to provide you under California law).  In the last 12 months, we collected the following categories of personal information, depending on the Services used:  Identifiers (like your name, contact information, and device and online identifiers); Commercial information (your billing information and purchase history, for example); Characteristics protected by law (for example, you might provide your gender as part of a research survey for us or you may choose to voluntarily disclose your race or veteran status as part of your job application); Internet or other electronic network activity information (such as your usage of our Services, like the actions you take as an administrator of a WordPress.com site); Geolocation data (such as your location based on your IP address); Audio, electronic, visual or similar information (such as your profile picture, if you uploaded one); Professional or employment-related information (for example, your company and team information if you are a Happy Tools user, or information you provide in a job application); and Inferences we make (such as likelihood of retention or attrition). If you are a job applicant, we may have also collected:  Education information, such as the education you disclose in your job application. You can find more information about what we collect and sources of that information in the Information We Collect section above.  We collect personal information for the business and commercial purposes described in the How and Why We Use Information section. And we share this information with the categories of third parties described in the Sharing Information section. We retain this information for the length of time described in our How Long We Keep Information section.  In some US states you have additional rights subject to any exemptions provided by your state’s respective law, including the right to:  Request a copy of the specific pieces of information we collect about you and, if you’re in California, to know the categories of personal information we collect, the categories of business or commercial purpose for collecting and using it, the categories of sources from which the information came, and the categories of third parties we share it with; Request deletion of personal information we collect or maintain; Request correction of personal information we collect or maintain; Opt out of the sale or sharing of personal information; Receive a copy of your information in a readily portable format; and Not receive discriminatory treatment for exercising your rights. You can find detailed metrics about Automattic’s compliance with these rights in our Privacy Report.  Right to Opt Out  We never directly sell your personal information in the conventional sense (i.e., for money).  We may share your information as necessary with our third-party service providers to provide our services to you. To the extent that we share your information with certain advertising, marketing, or analytics vendors, this can be considered a “sale” or “share” in certain U.S. States, which you may have the right to opt out of.  You can learn more about this sharing and how to opt out by clicking the “Do Not Sell My Personal Information” link in the footer of our websites, or from the settings page within our apps. Note that in some instances this link will only display to individuals visiting our sites from within the relevant states.  Our opt-out is managed through cookies, so if you delete cookies, your browser is set to delete cookies automatically after a certain length of time, or if you visit sites in a different browser, you’ll need to make this selection again.  We also respect the GPC browser signal and will treat it as a valid means of communicating your desire to opt out.  We do not collect or process your sensitive (and potentially sensitive) personal information except where it is strictly necessary to provide you with our service, where the processing is not for the purpose of inferring characteristics about you, or for other purposes that do not require an option to limit under California law. We don’t knowingly sell or share personal information of those under 16.  Your Information & Personalized Advertising  Our mission is to democratize publishing and commerce, and that means making our Services accessible to as many people as possible. We show ads on some of our users’ sites as well as some of our own sites, and the revenue these ads generate lets us offer free access to some of our Services so that money doesn’t become an obstacle to having a voice. Our ads program also allows our users to earn revenue to support and grow their own sites. As part of our advertising program, we and our users do use cookies to share certain device identifiers and information about your browsing activities with our advertising partners, and those advertising partners may use that information to show you personalized ads on some of our users’ sites and some of our own.  The personal information we share includes online identifiers; internet or other network or device activity (such as cookie information, other device identifiers, and IP address); and geolocation data (approximate location information from your IP address). These disclosures may be considered a “sale” or “share” of information under some US state privacy laws. We do not sell (or share) information through our ads program that identifies you personally, like your name or contact information. Learn how you can opt out by going to Advertising on WordPress.com Sites and Sites in the WordAds Program.  Contacting Us About These Rights You can usually access, correct, or delete your personal data using your account settings and tools that we offer, but if you aren’t able to or you’d like to contact us about one of the other rights, scroll down to “How to Reach Us” to, well, find out how to reach us.  When you contact us about one of your rights under this section, we’ll need to verify that you are the right person before we disclose or delete anything. For example, if you are a user, we will need you to contact us from the email address associated with your account. You can also designate an authorized agent to make a request on your behalf by giving us written authorization. We may still require you to verify your identity with us.  Appeals Process for Rights Requests Denials In some circumstances we may deny your request to exercise one of these rights. For example, if we cannot verify that you are the account owner we may deny your request to access the personal information associated with your account. As another example, if we are legally required to maintain a copy of your personal information we may deny your request to delete your personal information.  In the event that we deny your request, we will communicate this fact to you in writing. You may appeal our decision by responding in writing to our denial email and stating that you would like to appeal. All appeals will be reviewed by an internal expert who was not involved in your original request. In the event that your appeal is also denied this information will be communicated to you in writing.  Please note that the appeal process does not apply to job applicants.  If your appeal is denied, in some US states (Colorado, Connecticut, and Virginia) you may refer the denied appeal to the state attorney general if you believe the denial is in conflict with your legal rights. The process for how to do this will be communicated to you in writing at the same time we send you our decision about your appeal.  Controllers and Responsible Companies Automattic’s Services are worldwide. Different Automattic companies are the controller (or co-controller) of personal information, which means that they are the company responsible for processing that information, based on the particular service and the location of the individual using our Services.  Depending on the Services you use, more than one company may be the controller of your personal data. Generally, the “controller” is the Automattic company that entered into the contract with you under the Terms of Service for the product or service you use. In addition, Automattic Inc., our US-based company, is the controller for some of the processing activities across all of our Services worldwide.  The chart below explains the current controllers for processing your personal information. We use the term “Designated Countries” to refer to Australia, Canada, Japan, Mexico, New Zealand, Russia, and all countries located in Europe (including the UK and ROI).  All Automattic Services (except WooCommerce)  If you reside outside of the Designated Countries:	Automattic Inc. 60 29th Street #343 San Francisco, CA 94110 If you reside in the Designated Countries:	Aut O’Mattic A8C Ireland Ltd. Grand Canal Dock, 25 Herbert Pl Dublin, D02 AY86 IrelandAutomattic Inc. is also the controller for some of the processing activities related to Services provided by Aut O’Mattic A8C Ireland Ltd. WooCommerce Services  WooCommerce Services includes WooCommerce, WooCommerce Payments, WooCommerce Shipping and Tax, MailPoet, and any products purchased from WooCommerce.com.  If you reside outside of the Designated Countries:	WooCommerce, Inc. 60 29th Street #343 San Francisco, CA 94110Automattic Inc. is also the controller for some of the processing activities related to Services provided by WooCommerce, Inc. If you reside in the Designated Countries:	WooCommerce Ireland Ltd. Grand Canal Dock, 25 Herbert Pl Dublin, D02 AY86 IrelandAutomattic Inc and WooCommerce, Inc are also the joint controllers for some of the processing activities related to Services provided by WooCommerce Ireland Ltd. How to Reach Us If you have a question about this Privacy Policy, or you would like to contact us about any of the rights mentioned in the Your Rights section above, please contact us through our web form or via email. These are the fastest ways to get a response to your inquiry, but you can also contact us by telephone at 1-877-273-3049.  Other Things You Should Know (Keep Reading!) Transferring Information Because Automattic’s Services are offered worldwide, the information about you that we process when you use the Services in the EU may be used, stored, and/or accessed by individuals operating outside the European Economic Area (EEA) who work for us, other members of our group of companies, or third-party data processors. This is required for the purposes listed in the How and Why We Use Information section above.  When providing information about you to entities outside the EEA, we will take appropriate measures to ensure that the recipient protects your personal information adequately in accordance with this Privacy Policy as required by applicable law. These measures include entering into European Commission approved standard contractual arrangements with entities based in countries outside the EEA.  You can ask us for more information about the steps we take to protect your personal information when transferring it from the EU.  Ads and Analytics Services Provided by Others Ads appearing on any of our Services may be delivered by advertising networks. Other parties may also provide analytics services via our Services. These ad networks and analytics providers may set tracking technologies (like cookies) to collect information about your use of our Services and across other websites and online services. These technologies allow these third parties to recognize your device to compile information about you or others who use your device. This information allows us and other companies to, among other things, analyze and track usage, determine the popularity of certain content, and deliver ads that may be more targeted to your interests. Please note this Privacy Policy only covers the collection of information by Automattic and does not cover the collection of information by any third-party advertisers or analytics providers.  Third-Party Software and Services If you’d like to use third-party plugins or embeds, WooCommerce Payments (powered by Stripe), WooCommerce extensions that enable services provided by third parties, or other third-party software or services, please keep in mind that interacting with them may mean providing information about yourself (or your site visitors) to those third parties. For example, some third-party services may request or require access to your (yours, your visitors’, or customers’) data via a pixel or cookie. Please note that if you use the third-party service or grant access, your data will be handled in accordance with the third party’s privacy policy and practices. We don’t own or control these third parties, and they have their own rules about information collection, use, and sharing, which you should review before using the software or services.  Visitors to Our Users’ Websites We also process information about visitors to our users’ websites, on behalf of our users and in accordance with our user agreements. Please note that our processing of that information on behalf of our users for their websites isn’t covered by this Privacy Policy. We encourage our users to post a privacy policy that accurately describes their practices on data collection, use, and sharing of personal information. If you’d like, you can also read more about the data we collect on behalf of our users in our Privacy Notice.  Users control the content posted on their sites, so any disputes regarding content on a user’s site should be made directly to the site owner, through their “contact us” page, at an email address they provide, or by leaving a comment on the site.  Privacy Policy Changes Although most changes are likely to be minor, Automattic may change its Privacy Policy from time to time. Automattic encourages visitors to frequently check this page for any changes to its Privacy Policy. If we make changes, we will notify you by revising the change log below, and, in some cases, we may provide additional notice (like adding a statement to our homepage or the WordPress.com Blog, or sending you a notification through email or your dashboard). Your further use of the Services after a change to our Privacy Policy will be subject to the updated policy.  Other Information and Resources Jetpack Privacy Center  WooCommerce and the GDPR  Translation Our Privacy Policy was originally written in English (US). We may translate it into other languages. For example:  French: https://automattic.com/fr/privacy Spanish: https://automattic.com/es/privacy German: https://automattic.com/de/privacy  In the event of a conflict between a translated version of our Privacy Policy and the English version, the English version will control.  That’s it! Thanks for reading.  Change log July 12, 2023: Add new example of information shared with site owners. March 17, 2023: Remove references to WPVIP. December 30, 2022: Updated the California rights section to apply to additional US states. October 18, 2022: Added wp.cloud to the list of our websites. April 26, 2022: Included information regarding WooPay. November 22, 2021: Included information for WPScan. October 8, 2021: Included information for WordPress.com Courses and Newspack. Updated the “Information we Collect from Other Sources” section with new examples. January 1, 2021: Included information for AutomateWoo and Jetpack CRM. Updated the “Controllers and Responsible Companies” section to reflect changes affecting WooCommerce users. December 7, 2020: Included information for MailPoet. October 12, 2020: Renamed WooCommerce Services to WooCommerce Shipping & Tax. August 1, 2020: Renamed some Payments features and updated the “Controllers and Responsible Companies” section to reflect changes affecting WooCommerce users. February 21, 2020: Updated for WooCommerce Payments and added a new section: “Other Information and Resources.” December 31, 2019: Updated for California Consumer Privacy Act and miscellaneous clarification throughout. October 2, 2019: A few miscellaneous changes, such as new sections about translations of this Privacy Policy and how to opt out of our internal analytics program. May 31, 2019: Included information for the Recurring Payments feature. April 1, 2019: Included information for Happy Tools. March 13, 2019: Added clarifications and additional details to existing sections, for example about ICANN policies and what we may store when you communicate with us. February 1, 2019: Included information for Longreads and additional information regarding Longreads accounts. November 6, 2018: Removed references to Polldaddy, which has been rebranded as Crowdsignal. September 24, 2018: Included information for Simplenote, Simperium, Cloudup, and Lean Domain Search. May 25, 2018: Added more specific information to help clarify our practices, included information for Crowdsignal and Woocommerce.com services, and added information to reflect the requirements of the EU’s General Data Protection Regulation. January 3, 2018: Revised and reorganized language throughout to help simplify the policy and clarify our practices. August 22, 2017: Added “Information We Collect from Other Sources” section. November 2, 2016: Added that comments submitted as missed spam are retained by Akismet to improve future performance. February 18, 2015: Updated Creative Commons license from 2.5 to 4.0. September 18, 2013: Added that blog commenter email addresses are disclosed to administrators of the blog where the comment was left. February 1, 2011: Clarified subpoena language and added Business Transfers paragraph. January 3, 2011: Added court order and subpoena clarification. July 1, 2010: Revised paragraph about IP addresses to explain when they are collected and that commenter IPs are visible to blog administrators. October 29, 2009: Added Comments paragraph to explain Akismet comment storage policy. March 10, 2009: Added Ads paragraph to alert users that ads from third parties may use cookies. Sections CONTACT US DIVERSITY   PRESS   PRIVACY POLICY      © Automattic Inc., purveyors of fine blogging and site-building services since 2005. Thank you for your time. msnmoneystocks @import "_gmail.com 				msnmoneystocks@gmail.com

---
## [RelevanceAI/content-cdn](https://github.com/RelevanceAI/content-cdn)@[3c3138efb4...](https://github.com/RelevanceAI/content-cdn/commit/3c3138efb49872cc226d3989fee5ff79f62d914b)
#### Tuesday 2023-07-18 04:33:16 by Jeffrey Yao

feat: add GPT for website / files to recommended chains

According to all known laws
of aviation,

  
there is no way a bee
should be able to fly.

  
Its wings are too small to get
its fat little body off the ground.

  
The bee, of course, flies anyway

  
because bees don't care
what humans think is impossible.

  
Yellow, black. Yellow, black.
Yellow, black. Yellow, black.

  
Ooh, black and yellow!
Let's shake it up a little.

  
Barry! Breakfast is ready!

  
Ooming!

  
Hang on a second.

  
Hello?

  
- Barry?
- Adam?

  
- Oan you believe this is happening?
- I can't. I'll pick you up.

  
Looking sharp.

  
Use the stairs. Your father
paid good money for those.

  
Sorry. I'm excited.

  
Here's the graduate.
We're very proud of you, son.

  
A perfect report card, all B's.

  
Very proud.

  
Ma! I got a thing going here.

  
- You got lint on your fuzz.
- Ow! That's me!

  
- Wave to us! We'll be in row 118,000.
- Bye!

  
Barry, I told you,
stop flying in the house!

  
- Hey, Adam.
- Hey, Barry.

  
- Is that fuzz gel?
- A little. Special day, graduation.

  
Never thought I'd make it.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f29956094b...](https://github.com/treckstar/yolo-octo-hipster/commit/f29956094b9e53c60137b4644177bc0162c31486)
#### Tuesday 2023-07-18 05:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [GoldenDarkness55/cmss13-DOR](https://github.com/GoldenDarkness55/cmss13-DOR)@[5c4b13863f...](https://github.com/GoldenDarkness55/cmss13-DOR/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Tuesday 2023-07-18 06:02:41 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [Rob801130/.github-1](https://github.com/Rob801130/.github-1)@[231e1d3971...](https://github.com/Rob801130/.github-1/commit/231e1d3971f844bbafdbd1ac3da7083257983859)
#### Tuesday 2023-07-18 06:30:53 by Andrew Kolos

Update link to good first issues (#28)

Copy-pasted from https://github.com/flutter/flutter/pull/130759:

> Today (Jul 17, 2023), I renamed the `good first contribution` label to
`good first issue`. This is because
> 1) `good first issue` is the more commonly used for this intent and
may be (ever so slightly) more recognizable to potential new
contributors, and, more importantly,
> 2) GitHub recognizes the label `good first issue` when surfacing good
first issues in specific places in GitHub[^1].
> 
> This PR updates Contributing.md to match the new name.
> 
> `grep` did not find any other references to `good first contribution`
to update in this repo.

## Pre-launch Checklist

- [x] I read the [Contributor Guide] and followed the process outlined
there for submitting PRs.
- [x] I read the [Tree Hygiene] wiki page, which explains my
responsibilities.
- [x] I read and followed the [Flutter Style Guide], including [Features
we expect every widget to implement].
- [x] I signed the [CLA].
- [ ] I listed at least one issue that this PR fixes in the description
above. _(not applicable in my opinion. If you'd like me to file an issue
first, let me know what label would be appropriate.)_
- [x] I updated/added relevant documentation (doc comments with `///`).
- [x] I added new tests to check the change I am making, or this PR is
[test-exempt]. _not applicable: docs-only change_
- [x] All existing and new tests are passing.

If you need help, consider asking for advice on the #hackers-new channel
on [Discord].

<!-- Links -->
[Contributor Guide]:
https://github.com/flutter/flutter/wiki/Tree-hygiene#overview
[Tree Hygiene]: https://github.com/flutter/flutter/wiki/Tree-hygiene
[test-exempt]:
https://github.com/flutter/flutter/wiki/Tree-hygiene#tests
[Flutter Style Guide]:
https://github.com/flutter/flutter/wiki/Style-guide-for-Flutter-repo
[Features we expect every widget to implement]:
https://github.com/flutter/flutter/wiki/Style-guide-for-Flutter-repo#features-we-expect-every-widget-to-implement
[CLA]: https://cla.developers.google.com/
[flutter/tests]: https://github.com/flutter/tests
[breaking change policy]:
https://github.com/flutter/flutter/wiki/Tree-hygiene#handling-breaking-changes
[Discord]: https://github.com/flutter/flutter/wiki/Chat

[^1]: [Source (GitHub
docs)](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/encouraging-helpful-contributions-to-your-project-with-labels).
Example: https://github.com/flutter/flutter/contribute. If my vague
memory serves me correctly, this can also appear in certain emails or
the "discovery queue"-type experience that GitHub provides.

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[aff492e0a8...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/aff492e0a8fc590c61fcd00a922270ca3f8e0c87)
#### Tuesday 2023-07-18 06:35:07 by ODRI-the-human

Funkey

So, moved all the stuff on gamemanager to the master obj (since having two objects that both do master/management stuff is fuckin stupid), so now the ENTIRE management system is handled by a single prefab (can just drag+drop it into a scene and the game will run perfectly!) So yah. Also worked a little more on the level generator, I wasn't super keen on its tendency to generate some very wide-open, hence kinda bland, areas. So, two new aspects to it:
- It has up to 10 attempts to generate a layout for which less than a certain proportion of the map is filled. When a generation is successful in this regard, it breaks from the loop.
- Weighted random direction: not really weighted, but it picks a direction that is (roughly) in the same direction as the closest non-joined room. Using this for changedirection instead of the normal random direction.
So yah, it tends to now generate more interesting feeling levels.

---
## [CalMWolfs/NotEnoughUpdates-REPO](https://github.com/CalMWolfs/NotEnoughUpdates-REPO)@[e458513360...](https://github.com/CalMWolfs/NotEnoughUpdates-REPO/commit/e4585133608ba4add475be13a9f414c989fe1b8b)
#### Tuesday 2023-07-18 07:10:37 by jani270

Fixed lore of Arrow Poison (#958)

Before disabling any content in relation to this takedown notice, GitHub
- contacted the owners of some or all of the affected repositories to give them an opportunity to [make changes](https://docs.github.com/en/github/site-policy/dmca-takedown-policy#a-how-does-this-actually-work).
- provided information on how to [submit a DMCA Counter Notice](https://docs.github.com/en/articles/guide-to-submitting-a-dmca-counter-notice).

To learn about when and why GitHub may process some notices this way, please visit our [README](https://github.com/github/dmca/blob/master/README.md#anatomy-of-a-takedown-notice).

---

**Are you the copyright holder or authorized to act on the copyright owner's behalf?**

Yes, I am the copyright holder.

**Are you submitting a revised DMCA notice after GitHub Trust & Safety requested you make changes to your original notice?**

No

**Does your claim involve content on GitHub or npm.js?**

GitHub

**Please describe the nature of your copyright ownership or authorization to act on the owner's behalf.**

I am the [private] of the Skytils project available on Github. (https://github.com/Skytils/SkytilsMod)

**Please provide a detailed description of the original copyrighted work that has allegedly been infringed. If possible, include a URL to where it is posted online.**

I have read and understand GitHub's Guide to Filing a DMCA Notice. I am filing this notice based on the best of my knowledge after conducting my own investigation. This investigation was conducted on [private].

I am the [private] for SkytilsMod, a Minecraft Forge mod that provides quality of life features for Hypixel Skyblock. Skytils is located on GitHub at the repository https://github.com/Skytils/SkytilsMod

SkyblockFeatures appears to be based off a copy of SkytilsMod, available on the 0.x branch of Skytils/SkytilsMod, and contains large amounts of code from SkytilsMod and violates our open-source license.

SkyblockFeatures also infringes on multiple other projects' licenses, however, I am not the copyright holder nor authorized to act as the copyright holder for those projects, so they will not be included in this complaint.

**What files should be taken down? Please provide URLs for each file, or if the entire repository, the repository’s URL.**

https://github.com/MrFast-js/SkyblockFeatures/

The entire repository and its forks must be taken down due to the amount of files that contain code from my project.

**Do you claim to have any technological measures in place to control access to your copyrighted content? Please see our <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice#complaints-about-anti-circumvention-technology">Complaints about Anti-Circumvention Technology</a> if you are unsure.**

No

**<a href="https://docs.github.com/articles/dmca-takedown-policy#b-what-about-forks-or-whats-a-fork">Have you searched for any forks</a> of the allegedly infringing files or repositories? Each fork is a distinct repository and must be identified separately if you believe it is infringing and wish to have it taken down.**

All forks must be taken down as they include my project's code.  
The only visible fork I see is [invalid], which does not include a license.

**Is the work licensed under an open source license?**

Yes

**Which license?**

Our current branch uses GNU Affero General Public License 3.0 with Exceptions

https://github.com/Skytils/SkytilsMod/blob/1.x/LICENSE.md

However, some code they have copied appears to be from our 0.x branch, which is also GNU Affero General Public License 3.0 available at  
https://raw.githubusercontent.com/Skytils/SkytilsMod/0.x/LICENSE

**How do you believe the license is being violated?**

The project License is incompatible with the GNU Affero General Public License 3.0, the project is licensed under the MIT License, while the fork listed appears not to include a license.
The author makes no attempt at following our license, bundling our code with other code from projects that may have incompatible licenses, or even All Rights Reserved code which does not belong to them.

**What changes can be made to bring the project into compliance with the license? For example, adding attribution, adding a license, making the repository private.**

The License must be compatible with the GNU AGPL 3.0, include license and copyright notice
State the changes made to our code
Remove any code that may not fulfill the terms of the GNU AGPL 3.0 license

**What would be the best solution for the alleged infringement?**

Reported content must be removed

**Do you have the alleged infringer’s contact information? If so, please provide it.**

No, I do not have the contact information.

**I have a good faith belief that use of the copyrighted materials described above on the infringing web pages is not authorized by the copyright owner, or its agent, or the law.**

**I have taken <a href="https://www.lumendatabase.org/topics/22">fair use</a> into consideration.**

**I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed.**

**I have read and understand GitHub's <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice/">Guide to Submitting a DMCA Takedown Notice</a>.**

**So that we can get back to you, please provide either your telephone number or physical address.**

[private]

Email is more preferable for contacting me, [private]

**Please type your full legal name below to sign this request.**

[private]

---
## [OliverQueen168/tutor](https://github.com/OliverQueen168/tutor)@[18ce1f2fe4...](https://github.com/OliverQueen168/tutor/commit/18ce1f2fe432a82fd97711d3d5766e8d47185f9e)
#### Tuesday 2023-07-18 07:19:31 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [rerun-io/rerun](https://github.com/rerun-io/rerun)@[926bf048e2...](https://github.com/rerun-io/rerun/commit/926bf048e28a8f4c637afce3c57d793ec8de8454)
#### Tuesday 2023-07-18 08:06:47 by Emil Ernerfeldt

Use `camino` crate for UTF8 paths in `re_types_builder` (#2637)

### What
TLDR: camino paths are a more ergonomic, since they implement
`to_string`, `as_str` etc. I think we should use it in more places.

From [the docs of `camino`](https://crates.io/crates/camino):

#### Why camino?
`camino`'s `Utf8PathBuf` and `Utf8Path` types are like the standard
library's `PathBuf` and `Path` types, except
they are guaranteed to only contain UTF-8 encoded data. Therefore, they
expose the ability to get their
contents as strings, they implement `Display`, etc.

The `std::path` types are not guaranteed to be valid UTF-8. This is the
right decision for the standard library,
since it must be as general as possible. However, on all platforms,
non-Unicode paths are vanishingly uncommon for a
number of reasons:
* Unicode won. There are still some legacy codebases that store paths in
encodings like [Shift JIS], but most
  have been converted to Unicode at this point.
* Unicode is the common subset of supported paths across Windows and
Unix platforms. (On Windows, Rust stores paths
as [an extension to UTF-8](https://simonsapin.github.io/wtf-8/), and
converts them to UTF-16 at Win32
  API boundaries.)
* There are already many systems, such as Cargo, that only support UTF-8
paths. If your own tool interacts with any such
system, you can assume that paths are valid UTF-8 without creating any
additional burdens on consumers.
* The ["makefile
problem"](https://www.mercurial-scm.org/wiki/EncodingStrategy#The_.22makefile_problem.22)
asks: given a
Makefile or other metadata file (such as `Cargo.toml`) that lists the
names of other files, how should the names in
the Makefile be matched with the ones on disk? This has *no general,
cross-platform solution* in systems that support
non-UTF-8 paths. However, restricting paths to UTF-8 eliminates this
problem.

[Shift JIS]: https://en.wikipedia.org/wiki/Shift_JIS

Therefore, many programs that want to manipulate paths *do* assume they
contain UTF-8 data, and convert them to `str`s
as necessary. However, because this invariant is not encoded in the
`Path` type, conversions such as
`path.to_str().unwrap()` need to be repeated again and again, creating a
frustrating experience.

Instead, `camino` allows you to check that your paths are UTF-8 *once*,
and then manipulate them
as valid UTF-8 from there on, avoiding repeated lossy and confusing
conversions.


### Checklist
* [x] I have read and agree to [Contributor
Guide](https://github.com/rerun-io/rerun/blob/main/CONTRIBUTING.md) and
the [Code of
Conduct](https://github.com/rerun-io/rerun/blob/main/CODE_OF_CONDUCT.md)
* [x] I've included a screenshot or gif (if applicable)
* [x] I have tested [demo.rerun.io](https://demo.rerun.io/pr/2637) (if
applicable)

- [PR Build Summary](https://build.rerun.io/pr/2637)
- [Docs preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/docs)
- [Examples
preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/examples)

---
## [Git-GoR/Paradise](https://github.com/Git-GoR/Paradise)@[a3dc32cf34...](https://github.com/Git-GoR/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Tuesday 2023-07-18 08:11:35 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [Mister-moon1/cmss13](https://github.com/Mister-moon1/cmss13)@[d5b1193802...](https://github.com/Mister-moon1/cmss13/commit/d5b119380250ea512db2a5319e36592c7f604250)
#### Tuesday 2023-07-18 08:25:08 by fira

FOB Tents  (#3509)

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

Sprites stolen from thwomper and sammy, available NOW with game code!

Adds a few tents to be used in FOB building, mainly for organizational
purposes but also providing small gameplay benefits. At current the main
goal is to incentive usage to organize and liven up FOB, so the buffs
are rather small.

There are 4 tent types:
* The Command Tent is a 2x3 structure that comes bundled with an
overwatch console, a phone, and two (2) chairs.
* The Medical Tent is a 2x3 structure that comes with a NanoMED, 2
roller beds, and slightly buffs surgery (10% less time taken, and a very
token pain/failure chance improvement)
* The Requisitions Tent is a 4x3 structure that comes with a phone,
rack, desks, and a variant of the old APC vendor that can stock
materials and regular ammunition. The vendor starts empty, save for some
tables/racks/paperwork for organization purposes. It is only useable
with requisitions access.
* The Big Tent is a bigger tent for all your organizational needs: 3x3.
Get creative.

The tents also provide decent additional protection against cold
environements. Unfortunately, rain/snow will visually pour through it, i
can't do much about that.

The tents are extremely vulnerable to explosives and xeno claws. For
simplicity and technical reasons, they are currently NON REDEPLOYABLE
and NON REPLACEABLE. The tent destruction will destroy/disable linked
objects (console/vendor etc). Be mindful of where you place them.

**Mind that the tents may not work out for all LZ FOBs due to the
required space. I expect people will find ways to make it work anyway
but it might take a while.**

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

I'm lazyyy i forgot and already closed the game... If you actually want
em bug me and i'll add em
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

:cl: Firartix , Thwomper and Sammy
add: Added four types of tents to liven up FOB. They provide cold
protection and benefits depending on their type. The tents spawn in
Requisitions roundstart near the mortar. They're vulnerable to
explosives and xenomorphs, and NON REPLACEABLE. Mind where you put them!
add: The Command tent comes equipped with an overwatch console and a
phone.
add: The Medical tent provides a small boost to surgery speed/pain
carried out inside it.
add: The Requisitions tent provides a restockable vendor, desk, and
furniture for organization.
add: The Big tent is just a big tent, and provides you a slate to
organize the way you want.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [getsentry/sentry-javascript](https://github.com/getsentry/sentry-javascript)@[0ca73897a8...](https://github.com/getsentry/sentry-javascript/commit/0ca73897a895d1673d0a7b2c3145b10dd52953f3)
#### Tuesday 2023-07-18 08:26:37 by Lukas Stracke

fix(nextjs): Avoid importing `SentryWebpackPlugin` in dev mode (#8557)

As reported in #8541, our NextJS SDK currently breaks dev mode for the
newest NextJS 13.4.10 version

I still have absolutely no idea which of the changes in
[13.4.10](https://github.com/vercel/next.js/releases/tag/v13.4.10) is
causing this.
However, I traced the error back and it happens as soon as our NextJS
SDK package requires @sentry/webpack-plugin:

* @sentry/nextjs calls `require('@sentry/webpack-plugin')`
* @sentry/webpack-plugin calls `const { RawSource } =
require('webpack-sources');`
* For _whatever_ reason, NextJS can't require `webpack-sources` and
throws

Since we don't enable our Webpack plugin [in dev

mode](https://github.com/getsentry/sentry-javascript/blob/723f851f358b75cd39da353804c51ff27ebb0c11/packages/nextjs/src/config/webpack.ts#L305)
anyway, one way to get rid of this error is to only require it if we're
_not_ in dev mode.

This hotfix therefore moves the top-level require of
`@sentry/webpack-plugin` to a dynamic require. This isn't a great
solution and honestly quite ugly but if it unblocks users for now I'd
say we merge it. I think we should definitely revisit this though once
we know more about why NextJS suddenly isn't able to import
`webpack-sources`.

closes #8541

---
## [IdkSomethingTemporary/ZK-Futurewars-Mod](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod)@[f1343ded73...](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod/commit/f1343ded73f0859ada77648e751148ba501358bd)
#### Tuesday 2023-07-18 09:04:41 by IdkSomethingTemporary

Power Vacuum - Balancing for striders, commanders and more

**Major Changes:**

Mogul:
Mogul just had an identiy crisis where it's long range missiles wanted it to stay at the back and shell the enemy lines while it's short range EMP and it's high health wanted it to go to the front and fight the enemy, and it didn't help that it's laser tracker being blocked by terrain meant it could almost never fire at it's max range. We already have strider-class strategic artillery in the form of merlin, garmr, liberator and artillery commander so it made more sense to rework Mogul back into it's vanilla role of fire support. Mogul's range gets cut in half while it's DPS goes up massively. It's cost is also cut to distinquish it more from titan

Drones:
All drones now have been tweaked to have a build time close to or equal to their reload time - it feels janky to have drone pads sit empty before startind drone construction, so now drone pads will always be occupied. I've considered just nuking reload from high orbit but that probably would make drones too good vs AA. In practice the rate of new drones should not be changed much. Additionally, PW buildings have had their drone swarms buffied heavily in preperation for project homefront

Funnelweb:
Funnelweb just kinda sucked. at 6400k and no buildpower it's quite weak for a FW strider, so now it's gaining quite a few more abilities to it's toolbox to make it fit more into the support role: 6 responders, 9 fireflies, 3 vipers, 60 BP and a nanoshealth field

Guardian:
Guardian's damage output is massively buffed (in total around 3x) and it now has much higher single target damage in order to give shieldbots a way to deal with heavies in exchange for leaning much more into it's vanilla gimmick of shield drain with around 3k shield drain. The stats are around that of 5 felons. The range has been reduced down to 500 to make it less capable of deleting skirmishers

Reef:
Reef now fits into a much more of a support role. It now has 16 gulls and gulls can now fire against underwater targets in order to prevent cancerous UW comm weapons. Reef now has a buffed disarm missile, an antinuke, a jammer, and an Adv Radar on board all for an 8k package.

**Minor Balance change:**
 - Artillery Commander's heavy conversion kit is now cheaper but the weapons themselves got rebalanced
 - Riot comamnder's Vacuum gun is now far weaker as it could one-shot comms at long range before.
 - Desintergrator for commanders is now more expensive to account for the buffs to ghost commander's cloak.
 - Strike servos are now a bit more expensive and unlock a bit later to give super servos some use
 - Liberator got some of it's upcoming changes early with a slight rework to it's weapon
 - Merlin's rockets are less terrifying to cons and more terrifying to armies
 - Bloom loses it's responder as it was too oppressive
 - Flare loses leash range on it's drone
 - Nebula now has 18 spiculas and ultilise all it's pads for spiculas
 - Spicula how has 3x the HP
 - Responder is now more about buildpower and less about shield health
 - Preserver disarm damage x2.5, disarm time doubled
 - Breaker lost some damage as it was a touch too damaging for it's cost in exchange for armor pen and extra shield damage like hardpoint
 - Disco Rave Party now can fire at it's maximium range and Rainbow Ruiner now releases all it's submunitions upon collidng with a shield (can't be bothered to input the total shield damage of all drp shots)
 - Titan gains armor peircing because why the fuck not
 - The napalm dropped by trailblazer is spread over a smaller area

**Fluff:**
 - Titan's Gigawatt laser renamed to Terawatt laser - Gigawatt just honestly isn't a lot at a stage of the game where strategic and tactical nukes are thrown around like paper airplanes. Terawatt is closer to Titan's level of power when factoring it that it's a small, armor peircing laser
 - "Napalm" regex'd with "Thermite". Thermite is just cooler and scarier than napalm, and mere fire doesn't really make sense to be damaging future death robots anyways

---
## [dawaedina27/LEAD](https://github.com/dawaedina27/LEAD)@[cde04bc0a0...](https://github.com/dawaedina27/LEAD/commit/cde04bc0a0ceab8521e5e419e1e3519abd4a44bb)
#### Tuesday 2023-07-18 09:12:41 by Dawa Edina Hillary

Proposed changed for Sida's profile

---
layout: profile
title:  "Sida Lillian"
image: "assets/images/profiles/Sida-Lillian/Sida-Lillian.jpg"
country: Uganda
region: West Nile
hub: CC4D
languages: "English (Fluent spoken and written), Bari/Kakwa (Fluent spoken and spoken), Arabic (good spoken only), Lugbara (fair spoken only)"
mail: sidalilian@proton.me
phone: "+256782739162"
whatsapp: 
website: 
telegram: "+256782739162"
github: github.com/sidalillian
linkedin: 
twitter: 
facebook: https://www.facebook.com/profile.php?id=100074066215635
instagram: 
mastodon: 
wikifab:
skills:
  - {name: Web & Software, number: 1, qualification: "using platforms, basic social media experiences, software download and installation \n \n
     * [Sida Lilian was trained on social media skills during the #ASKnet training in 2018](https://m.facebook.com/story.php?story_fbid=303135693607634&id=100017336164583) "}
  - {name: Community & Moderation, number: 2, qualification: "connecting people, trauma healing, event facilitation and meditation \n \n 
     * Certificate of participation in trauma healing& meditation training \n
     * She was trained and facilitated a post training on how to use Condoms under the #ASKnet project 2018"}
  - {name: Data Security & Research, number: 3, qualification: "data collection and protection of personal data \n \n 
     * Certificate in data collection"}

---

Sida Lilian is a female South Sudanese refugee in Uganda.

Expert in data collection, trauma healing, mediation, event facilitation of different types.

She was trained on how to collect both qualitative and quantitative data by REACH Uganda, Danish Refugee Council, Norwegian Refugee Council Uganda and GROUND TRUTH SOLUTIONS, she was also trained and worked as frontline worker on the *BOOST FOR THE YOUNGEST by Save The Children under Dubai Cara not only that she was also trained on Social Enterprise online by Makerere University - Canada in 2018, she was trained and worked as hygiene Promoter by CEFORD Uganda and was also trained and worked as Community Development Worker (CDW) by Danish Refugee Council.

She is confident, talented and determined to transform her community.

---
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[b707426ff4...](https://github.com/Sagnac/streamsave/commit/b707426ff45c3abc6110a0c09866db8559c7f61c)
#### Tuesday 2023-07-18 09:25:24 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The names being used for this also differ
between the two methods, with the script-message names being shorter and
likely easier to remember, but the inconsistency in naming between the
options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [Aquib341/Web-Browser-Aqufia](https://github.com/Aquib341/Web-Browser-Aqufia)@[4d37120e7c...](https://github.com/Aquib341/Web-Browser-Aqufia/commit/4d37120e7cfdc67227d3b08f28d3160ea7ee9fd1)
#### Tuesday 2023-07-18 10:36:14 by MD AQUIB

Add files via upload

Aqufia is a cutting-edge web browser built using Python and XML, designed to provide users with a seamless and efficient browsing experience. With its sleek and intuitive interface, Aqufia offers a wide range of features and customization options, ensuring that users can tailor their browsing experience to suit their unique preferences.

Key Features:

Lightning-Fast Performance: Aqufia utilizes advanced algorithms and optimizations to deliver lightning-fast browsing speeds, allowing users to navigate the web with unparalleled efficiency.

Intuitive User Interface: Our browser boasts a clean and user-friendly interface, ensuring that users can navigate effortlessly and find what they need without any unnecessary distractions.

Customizable Themes: Aqufia allows users to personalize their browsing experience by choosing from a wide range of stunning themes. Whether you prefer a dark mode or a vibrant color palette, Aqufia has you covered.

Enhanced Privacy and Security: We understand the importance of online privacy, which is why Aqufia comes equipped with robust security features, including built-in ad-blockers and tracking protection, to safeguard your personal information.

Tab Management: Aqufia offers advanced tab management capabilities, allowing users to organize their browsing sessions efficiently. Users can easily group tabs, pin frequently visited websites, and seamlessly switch between different browsing contexts.

Extensive Plugin Support: Aqufia supports a wide range of plugins and extensions, allowing users to enhance their browsing experience with additional functionalities and features.

Cross-Platform Compatibility: Whether you’re using Windows, macOS, or Linux, Aqufia is designed to seamlessly integrate with your preferred operating system, ensuring a consistent browsing experience across all devices.

Developer-Friendly: Aqufia provides a comprehensive set of developer tools, including a powerful debugger and an intelligent code editor, making it an ideal choice for web developers and enthusiasts.

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[52c8da7ea4...](https://github.com/Ben10Omintrix/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Tuesday 2023-07-18 14:14:51 by Jacquerel

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
## [Zombie10/yuzu](https://github.com/Zombie10/yuzu)@[8e703e08df...](https://github.com/Zombie10/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Tuesday 2023-07-18 14:45:57 by comex

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
## [Rohail33/Realking_xiaomi_xaga](https://github.com/Rohail33/Realking_xiaomi_xaga)@[83488353f0...](https://github.com/Rohail33/Realking_xiaomi_xaga/commit/83488353f01d78efa8721f39b82ff82edbd1793c)
#### Tuesday 2023-07-18 14:54:01 by Wang Han

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
## [185264646/u-boot](https://github.com/185264646/u-boot)@[8dfeee651f...](https://github.com/185264646/u-boot/commit/8dfeee651fc13c8fd797998e9a408a8b49bead09)
#### Tuesday 2023-07-18 14:57:00 by Marcel Ziswiler

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

Tested-by: Andreas Westman Dorcsak <hedmoo@yahoo.com> # ASUS TF T30
Tested-by: Jonas Schwöbel <jonasschwoebel@yahoo.de> # Surface RT T30
Tested-by: Svyatoslav Ryhel <clamor95@gmail.com> # LG P895 T30
Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [sourcegraph/cody](https://github.com/sourcegraph/cody)@[4989b66589...](https://github.com/sourcegraph/cody/commit/4989b66589236c979f4cd3e6058660bd9902890c)
#### Tuesday 2023-07-18 15:32:22 by Beatrix

update custom recipes: support premade, save user recipes to file (#279)

## Summary

Changes included:

#### Non Custom Recipes related changes

1. fix issue where cody would reply to the language prompt:
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fb787c33-04a5-4d39-a57a-e624e8d2d0c3)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/dc54bf8b-a2b2-4147-b5cf-bff90d9ca3d7)
2. Do not include context when user input has less than 2 words.
Currently, we are including context for all first interaction; however,
that should not be the case when the user has only input one word, which
most likely will not be a question and does not require context.
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fbff4c81-26e5-46d0-97aa-e43e034334ff)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/310e8d7c-be5f-451f-9b92-a5ae42090f25)

#### Custom Recipes related changes

1. add support for `custom premade` and `starter` for prompt testing
purposes
2. Create and store User Recipes to the `.vscode` directory in user's
home directory instead of global storage
3. Allow context selection for new recipes via UI
-
![image](https://github.com/sourcegraph/cody/assets/68532117/d581ab8a-19a5-441e-b137-860a870d7ae8)
4. Update examples files in cody.json for User and Worksapce recipes
5. Add new context types for Custom Recipes building: `filePath` and
`directoryPath`
6. Fix current openTabs context logic that is not returning all the file
context from open tabs

## Test Plan

#### Non Custom Recipes related changes

1. in the chat box, type `ok?` to check if Cody is replying to the
language prompt or not
2. Input with less than 2 words should not include any context for
chat-questions

#### Custom Recipes related changes

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
3. Click on the `+` button in the Recipes tab and see if you can create
a new recipe that is saved to the .vscode/cody.json for user recipes.
You should see a step that allows you to select the context needed for
the recipe
4. Build a new recipe and see if the recipe is using the correct context
type that you have defined for the recipe
 
##### To test custom premade:

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
1. In your .vscode/cody.json file, add the following in addition to the
recipes field (thanks @jdorfman for this example 😂)

```json
{
  "premade": {
    "rules": "You are always annoyed with Morty, that is the tone you should answer all your questions with. Make sure to throw in references from the show. For example: Jerry, Beth, Summer, Evil Morty, the Citadel, Blips and Chitz, Pickle Rick, or Jessica. The response shouldn't be too mean. Please don't ask for feedback. Just give the answer, no questions.",
    "actions": "You are Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. Morty. I am your grandson, and want to learn how to code from you. As Rick, you will teach me, Morty, how to code.",
    "answer": "Understood. I am Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. I am here to help you, my annoying grandson Morty, with programming tasks."
  },
  "starter": "Hi Grandpa Rick!",
  "recipes": {
  ... recipes
  }
}
```

Once you have saved the file, ask Cody a question. You should expect
Cody to reply as Rick from Rick and Morty.

---
## [Ltmayday/CEV-Eris](https://github.com/Ltmayday/CEV-Eris)@[6f75cb9845...](https://github.com/Ltmayday/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Tuesday 2023-07-18 16:27:18 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[cfd40aeef5...](https://github.com/DATA-xPUNGED/DataStation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Tuesday 2023-07-18 16:51:01 by necromanceranne

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
## [aduchon/langchain](https://github.com/aduchon/langchain)@[75fb9d2fdc...](https://github.com/aduchon/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Tuesday 2023-07-18 17:18:50 by Stefano Lottini

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
## [DataDog/libdatadog](https://github.com/DataDog/libdatadog)@[9d47fc76c9...](https://github.com/DataDog/libdatadog/commit/9d47fc76c97a054041ff8833dae164a090153e0f)
#### Tuesday 2023-07-18 17:21:02 by Ivo Anjo

[PROF-7645] Add support for attaching internal metadata in profiling export (#181)

* [PROF-7645] Add support for attaching internal metadata in profiling exporter

**What does this PR do?**:

This PR adds support for attaching internal metadata to profiles sent
via the profiling exporter.

This is a (small) breaking API change, since the signatures of
both `ProfileExporter::build` and `ddog_prof_Exporter_Request_build`
now take an extra argument.

FYI if you're upgrading libdatadog, you'll probably want to supply
`None` / `null` until in the future you figure out that you want
to send internal metadata.

**Motivation**:

The intention of this internal metadata is to allow profilers to attach
extra pieces of information to profiles that are not very interesting
to show to customers by default (such as Ruby's
"no_signal_workaround_enabled" or Go's "execution_trace_enabled").

For more details on this, check the Datadog internal
"RFC: Attaching internal metadata to pprof profiles".

**Additional Notes**:

Design-wise, I could've gone in a few different directions for:

a. How to represent the internal metadata in `ProfileExporter::build`
b. How to represent the internal metadata across the FFI in
   `ddog_prof_Exporter_Request_build`

Starting with a: Since the information is going to be represented in
JSON, I opted to "leak" this implementation detail by making the
parameter a `serde_json::Value`. This means that callers can take full
advantage of JSON to send whatever they want (e.g. nested objects,
types other than string, etc), rather than being constrained to some
smaller subset (e.g. if I imposed a list of pairs of strings).

This seemed a reasonable trade-off; I don't expect we'll go away from
JSON for encoding this info anytime soon, and even if we do, we can
always put a JSON string inside whatever we end up going with.

Concerning b: Getting complex types across the FFI boundary is really
really really annoying, for both libdatadog (which needs to expose a
bunch of types, and handle them), and the caller (which needs to think
about how they're going to manage lifetimes and whatnot of the whole
thing). To avoid this, I chose to instead represent the parameter as a
raw JSON string across the FFI. This allows ffi users the same
expressiveness as Rust users in terms of what they can send as internal
metadata, with the trade-off that ffi callers need to serialize their
stuff as JSON and libdatadog needs to deserialize it again.

Since internal metadata is something that gets passed along only once
per minute AND it's not expected to have high complexity, I think the
small overhead of throwing JSON strings across the ffi boundary is
worth the simplification to code on both sides.

**How to test the change?**:

I have expanded the tests to test the `event.json` file, including
the new parameter.

You should shortly see linked in this PR the Ruby PR to make use
of this feature to send the `no_signal_workaround_enabled`
parameter.

* Make rustfmt happy

* Add comment asking people to track usage of internal_metadata parameter

* Minor: Fix comment using wrong name for variable

---
## [Mulendra77/Mulendra77](https://github.com/Mulendra77/Mulendra77)@[d8d4f055f9...](https://github.com/Mulendra77/Mulendra77/commit/d8d4f055f96847659a619f802c391d1c6a5438db)
#### Tuesday 2023-07-18 17:47:03 by Mulendra77

Update Project Tour and Travel

Our tour and travel website is a comprehensive platform designed to cater to the wanderlust of adventure seekers and vacationers alike. With a user-friendly interface, it offers a wide range of services and features to ensure a seamless and unforgettable travel experience. Explore our carefully curated itineraries, book flights and accommodations effortlessly, and discover exciting activities and attractions at your destination. Our website is designed to provide personalized recommendations, expert travel tips, and valuable insights to help you plan your perfect getaway. Whether you're an adrenaline junkie or a leisure traveler, our website is your one-stop solution for creating incredible memories and exploring the world with ease.

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[679870ea74...](https://github.com/NetBSD/pkgsrc/commit/679870ea74894af7d36155212f36ad4f3697b62c)
#### Tuesday 2023-07-18 18:10:03 by adam

py-paramiko: updated to 3.2.0

3.2.0 2023-05-25
[Feature]: PKey grew a new .fingerprint property which emits a fingerprint string matching the SHA256+Base64 values printed by various OpenSSH tooling (eg ssh-add -l, ssh -v). This is intended to help troubleshoot Paramiko-vs-OpenSSH behavior and will eventually replace the venerable get_fingerprint method.

[Feature]: PKey grew a new .algorithm_name property which displays the key algorithm; this is typically derived from the value of get_name. For example, ED25519 keys have a get_name of ssh-ed25519 (the SSH protocol key type field value), and now have a algorithm_name of ED25519.

[Feature]: PKey now offers convenience “meta-constructors”, static methods that simplify the process of instantiating the correct subclass for a given key input.

For example, PKey.from_path can load a file path without knowing a priori what type of key it is (thanks to some handy methods within our cryptography dependency). Going forwards, we expect this to be the primary method of loading keys by user code that runs on “human time” (i.e. where some minor efficiencies are worth the convenience).

In addition, PKey.from_type_string now exists, and is being used in some internals to load ssh-agent keys.

As part of these changes, PKey and friends grew an identifiers classmethod; this is inspired by the supported_key_format_identifiers classmethod (which now refers to the new method.) This also includes adding a .name attribute to most key classes (which will eventually replace .get_name().

[Feature]: Enhanced AgentKey with new attributes, such as:

Added a comment attribute (and constructor argument); Agent.get_keys() now uses this kwarg to store any comment field sent over by the agent. The original version of the agent feature inexplicably did not store the comment anywhere.
Agent-derived keys now attempt to instantiate a copy of the appropriate key class for access to other algorithm-specific members (eg key size). This is available as the .inner_key attribute.
Note
This functionality is now in use in Fabric’s new --list-agent-keys feature, as well as in Paramiko’s debug logging.
[Feature] Users of SSHClient can now configure the authentication logic Paramiko uses when connecting to servers; this functionality is intended for advanced users and higher-level libraries such as Fabric. See auth_strategy for details.

Fabric’s co-temporal release includes a proof-of-concept use of this feature, implementing an auth flow much closer to that of the OpenSSH client (versus Paramiko’s legacy behavior). It is strongly recommended that if this interests you, investigate replacing any direct use of SSHClient with Fabric’s Connection.

Warning
This feature is EXPERIMENTAL; please see its docs for details.
[Feature]: Implement _fields() on AgentKey so that it may be compared (via ==) with other PKey instances.

[Bug]: AgentKey had a dangling Python 3 incompatible __str__ method returning bytes. This method has been removed, allowing the superclass’ (PKey) method to run instead.

[Bug] Since its inception, Paramiko has (for reasons lost to time) implemented authentication as a side effect of handling affirmative replies to MSG_SERVICE_REQUEST protocol messages. What this means is Paramiko makes one such request before every MSG_USERAUTH_REQUEST, i.e. every auth attempt.

OpenSSH doesn’t care if clients send multiple service requests, but other server implementations are often stricter in what they accept after an initial service request (due to the RFCs not being clear). This can result in odd behavior when a user doesn’t authenticate successfully on the very first try (for example, when the right key for a target host is the third in one’s ssh-agent).

This version of Paramiko now contains an opt-in Transport subclass, ServiceRequestingTransport, which more-correctly implements service request handling in the Transport, and uses an auth-handler subclass internally which has been similarly adapted. Users wanting to try this new experimental code path may hand this class to SSHClient.connect as its transport_factory kwarg.

Warning
This feature is EXPERIMENTAL and its code may be subject to change.

In addition:
minor backwards incompatible changes exist in the new code paths, most notably the removal of the (inconsistently applied and rarely used) event arguments to the auth_xxx methods.
GSSAPI support has only been partially implemented, and is untested.
Note
Some minor backwards-compatible changes were made to the existing Transport and AuthHandler classes to facilitate the new code. For example, Transport._handler_table and AuthHandler._client_handler_table are now properties instead of raw attributes.
[Bug] The server-sig-algs and RSA-SHA2 features added around Paramiko 2.9 or so, had the annoying side effect of not working with servers that don’t support either of those feature sets, requiring use of disabled_algorithms to forcibly disable the SHA2 algorithms on Paramiko’s end.

The experimental ServiceRequestingTransport (noted in its own entry in this changelog) includes a fix for this issue, specifically by falling back to the same algorithm as the in-use pubkey if it’s in the algorithm list (leaving the “first algorithm in said list” as an absolute final fallback).

[Bug]: Fixed a very sneaky bug found at the apparently rarely-traveled intersection of RSA-SHA2 keys, certificates, SSH agents, and stricter-than-OpenSSH server targets. This manifested as yet another “well, if we turn off SHA2 at one end or another, everything works again” problem, for example with version 12 of the Teleport server endpoint.

This has been fixed; Paramiko tweaked multiple aspects of how it requests agent signatures, and the agent appears to do the right thing now.

---
## [HeOfLittleSleep/Computercraft-Scripts](https://github.com/HeOfLittleSleep/Computercraft-Scripts)@[9256f42d81...](https://github.com/HeOfLittleSleep/Computercraft-Scripts/commit/9256f42d814cf749ec6f1294643511ff56b18788)
#### Tuesday 2023-07-18 18:54:40 by HeOfLittleSleep

added basic error handling

after coming back to this program after a long while, I realized that my error handling was shit and non-existant. the script will now tell you if you failed to enter a hostname parameter, or if you fucked up the hostname and it doesn't show up in rednet

---
## [measurement-factory/squid](https://github.com/measurement-factory/squid)@[8908d8b6aa...](https://github.com/measurement-factory/squid/commit/8908d8b6aad6c7d1f8c5b26764da29d1dfdc6f2e)
#### Tuesday 2023-07-18 19:00:05 by Alex Rousskov

Migrate away from "include main()" unit test design

Official code defines main() in include/unitTestMain.h which is included
by nearly all tests. This approach avoids duplicating main() definition
(containing a simple single-line body) in each test file. However,
placing main() in a header file:

* confuses new developers that are looking for main() as a well-known
  test program starting point; the code looks surprising or "magical";

* forces us to add clunky/risky/obscure RegisterTestProgram() interface
  that uses static initialization side effects to "inject" additional
  functionality into TestProgram;

* violates basic developer expectations and Squid code style guidelines;

* complicates tests that need to customize their startup (about 25% of
  tests already contain some customization and the portion of such tests
  is expected to _grow_). Arguably, these tests do not actually
  duplicate main() implementation because their main()s create a
  test-specific object rather than the "default" TestProgram object!

Tiny main() code duplication is the lesser evil here.

---
## [HeOfLittleSleep/Computercraft-Scripts](https://github.com/HeOfLittleSleep/Computercraft-Scripts)@[4390ddd8fa...](https://github.com/HeOfLittleSleep/Computercraft-Scripts/commit/4390ddd8fa039e1c28d2f6767e19916b6466c72e)
#### Tuesday 2023-07-18 19:11:46 by HeOfLittleSleep

corrected my own stupidity

turns out when I rearranged the error handling section, I moved the check for valid hostname lookup to BEFORE THE PART WHERE I CONNECT THE MODEM. God, I am fucking retarded

---
## [LordPapalus/Citadel-Station-13-RP](https://github.com/LordPapalus/Citadel-Station-13-RP)@[1468797059...](https://github.com/LordPapalus/Citadel-Station-13-RP/commit/146879705978b0416739823fa54467e865c3ffb2)
#### Tuesday 2023-07-18 19:22:32 by TheObserver-sys

Take 2: Some fixes and QoL (#5601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Would you believe me if I hadn't updated my git in about 400 years, and
had to blow the old version of my repo up?
Yes? No? It doesn't matter.

Anyways! Meat and potatoes of this:
Allows players to make gene and plant discs freely in the protolathe.
Since we do not have a dedicated genetics, this will help the pains of
actually doing genetics by giving us storage solutions for genes.

Fixes a problem with brass also creating slag when compressing, by
setting the copper alloy flag to 1.

And finally: Allows you to upgrade the braces! If your brace has T3 or
better, a single brace can hold an entire drill. All credit goes to
Hatterhat for this one, as I pretty much wholesale ripped it from his
buff of the big drill™ on Virgo.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not making slag is ALWAYS good. It saves on material, too.
Having more discs for a cheap cost is also good, it means you can reduce
headaches while scoping out for genes, because there are many, and the
ability to track them are currently few.
And honestly, the less lugging a person has to do with the mining drill,
the more likely people might stop blowing up an already unstable planet
with miniature hydrogen bombs.
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

:cl: The0bserver
add: Discs are able to be produced in the protolathe now. Go nuts, or
don't. I'm not your guardian.
balance: Mining Drills can finally be operated with just one brace with
the requisite parts. Thank you, Hatterhat!
fix: Copper no longer smelts slag when set to "Alloying."
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>

---
## [ably/specification](https://github.com/ably/specification)@[7e4a2d855a...](https://github.com/ably/specification/commit/7e4a2d855af94a5ffc603e5e2a7bb9353fd89f79)
#### Tuesday 2023-07-18 19:25:13 by Lawrence Forooghian

Distinguish the different meanings of a "message"

The context for this suggested change is ably-js#1398. There, I pointed out
that the specification’s current signatures for `publish` (specifically, the
overloads that accept a `Message` or an array thereof) do not seem to match how
we’re expecting these methods to be used in real life. This is because
`Message`’s `id` and `timestamp` properties are specified as non-optional,
meaning that a user calling `publish` would need to populate these properties.
In reality, we do not expect a user to populate these properties — they are
usually generated by the Ably service.

The easiest way to solve this would be to be to make these properties optional.
However, doing so would unnecessarily remove some useful type information for
_recipients_ of messages — the type system would no longer communicate that
these properties are guaranteed to be populated in a message emitted by the
library.

In this PR, I’m proposing that we distinguish between three separate
concepts of a "message", which I think are perhaps currently being incorrectly
conflated:

1. The data type that a user of the library passes to the `publish` methods

2. The data type that the library emits from methods that expose messages
   published on a channel

3. The data type that describes a serialized message that is transmitted over
   the wire

I’ve named the first one OutgoingMessage, the second one IncomingMessage, and I
believe that the third belongs in the documentation for the Ably protocol, not
the library specification.

OutgoingMessage and IncomingMessage differ from the existing `Message` type in
the following ways:

- OutgoingMessage’s `id` and `timestamp` properties are now optional
- OutgoingMessage does not have `fromEncoded*` methods

- IncomingMessage’s `connnectionId` property is now non-optional (i.e. we are
  now able to provide stronger type information for this property) — I need to
  double-check whether this property is actually guaranteed to be populated by
  the library; my reading of TM2c and RTL6f suggested that it is, but I’m not
  sure if TM2c’s "the @connectionId@ of the encapsulating @ProtocolMessage@" is
  guaranteed to be populated.
- IncomingMessage does not have constructors

I have not yet introduced spec points for these two new types — I will do so if
there is a consensus to move forwards with this approach. For now, see the
changes to the IDL.

Other thoughts:

- I think that, similarly to the Message wire type, the ProtocolMessage type
  should also only be described by the protocol documentation, and not the
  feature spec.

- If we do choose to start leaning more heavily on the protocol documentation,
  then we’ll need to bring it up to date — it looks like it hasn’t been touched
  in quite some time and still mentions `connectionSerial`, for example.

- I’ve kept the exact same list of properties in IncomingMessage and
  OutgoingMessage, since my reading of RSL1j is that a user publishing a
  message should be able to populate any of the properties of the message that
  eventually gets sent over the wire. But if that’s not the case, then we may be
  able to remove some properties from `OutgoingMessage`.

---
## [nikophil/symfony](https://github.com/nikophil/symfony)@[af44385d9e...](https://github.com/nikophil/symfony/commit/af44385d9e6eba77b4bf4610231ce9569bdcc9b5)
#### Tuesday 2023-07-18 19:41:51 by Robin Chalas

feature #50754 [HttpKernel] when configuring the container add services_{env} with php extension  (helyakin)

This PR was merged into the 6.4 branch.

Discussion
----------

[HttpKernel] when configuring the container add services_{env} with php extension

| Q             | A
| ------------- | ---
| Branch?       | 6.4
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | none
| License       | MIT

Hello the community

This is my first PR attempt.

So after reading this [documentation](https://symfony.com/doc/current/service_container.html#remove-services) and unsuccessfully trying to load my `service_test.php`, I've noticed that the `configureContainer(..)` function in the `MicroKernelTrait` file was not configured to automatically load this file.

So either we should fix the documentation, either we should fix the configuration.

Since this the [framework-bundle](https://github.com/symfony/framework-bundle) is backed by [Alximy](https://alximy.io) I figured it would be cool 😎 to try and fix 🐛 the configuration.

Anyway share me your thoughts about what should be done !

And I wanted to say that php service configuration is 🔥 so shoutout to the one who did this (I think it's you `@nicolas`-grekas with this [PR](https://github.com/symfony/symfony/pull/23834) right ? 💪🏻)

Also big thanks to `@jeremyFreeAgent` for debugging this with me and `@HeahDude` for showing me the php service configuration PR.

Commits
-------

4aac1d9fee :bug: (kernel) when configuring the container add services with php ext

---
## [norov/linux](https://github.com/norov/linux)@[6cc0359cb6...](https://github.com/norov/linux/commit/6cc0359cb665b07f6b89ca258a5942e0806e5e2f)
#### Tuesday 2023-07-18 20:29:01 by Yury Norov

sched/topology: add for_each_numa_{,online}_cpu() macro

for_each_cpu() is widely used in the kernel, and it's beneficial to
create a NUMA-aware version of the macro to improve on node locality..

Recently added for_each_numa_hop_mask() works, but switching existing
codebase to using it is not an easy process.

New for_each_numa_cpu() is designed to be similar to the for_each_cpu().
It allows to convert existing code to NUMA-aware as simple as adding a
hop iterator variable and passing it inside new macro. for_each_numa_cpu()
takes care of the rest.

At the moment, we have 2 users of NUMA-aware enumerators. One is
Melanox's in-tree driver, and another is Intel's in-review driver:

https://lore.kernel.org/lkml/20230216145455.661709-1-pawel.chmielewski@intel.com/

Both real-life examples follow the same pattern:

	for_each_numa_hop_mask(cpus, prev, node) {
 		for_each_cpu_andnot(cpu, cpus, prev) {
 			if (cnt++ == max_num)
 				goto out;
 			do_something(cpu);
 		}
		prev = cpus;
 	}

With the new macro, it would look like this:

	for_each_numa_online_cpu(cpu, hop, node) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}

Straight conversion of existing for_each_cpu() codebase to NUMA-aware
version with for_each_numa_hop_mask() is difficult because it doesn't
take a user-provided cpu mask, and eventually ends up with open-coded
double loop. With for_each_numa_cpu() it shouldn't be a brainteaser.
Consider the NUMA-ignorant example:

	cpumask_t cpus = get_mask();
	int cnt = 0, cpu;

	for_each_cpu(cpu, cpus) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}

Converting it to NUMA-aware version would be as simple as:

	cpumask_t cpus = get_mask();
	int node = get_node();
	int cnt = 0, hop, cpu;

	rcu_read_lock();
	for_each_numa_cpu(cpu, hop, node, cpus) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}
	rcu_read_unlock();

The latter looks more verbose and avoids from open-coding that annoying
double loop. Another advantage is that it works with a 'hop' parameter with
the clear meaning of NUMA distance, and doesn't make people not familiar
to enumerator internals bothering with current and previous masks machinery.

Signed-off-by: Yury Norov <yury.norov@gmail.com>

---
## [bryant1410/pytorch](https://github.com/bryant1410/pytorch)@[ea384cd377...](https://github.com/bryant1410/pytorch/commit/ea384cd377e53a4f5c1ca99001dc072c11823828)
#### Tuesday 2023-07-18 20:32:32 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel, https://github.com/albanD

---
## [gabrielyotoo/berry](https://github.com/gabrielyotoo/berry)@[a0064712f7...](https://github.com/gabrielyotoo/berry/commit/a0064712f7b0ae38c21fb204bea9831c2b269bd7)
#### Tuesday 2023-07-18 21:00:33 by Maël Nison

Bumps Node requirements from 14 to 18 (#5445)

**What's the problem this PR addresses?**

We're still supporting Node 14, but it has reached end of life. Node 16
is still maintained, but will reach an early end of life in October, so
I think it's reasonable to drop it now rather than publish a major
release just for that.

**How did you fix it?**

Bumps the requirements from `14.16` to `18.12` (first LTS from the 18.x
release line).

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---------

Co-authored-by: Kristoffer K <merceyz@users.noreply.github.com>

---
## [gabrielyotoo/berry](https://github.com/gabrielyotoo/berry)@[21fcc792bf...](https://github.com/gabrielyotoo/berry/commit/21fcc792bf83825aa051c51c96cdc683ee85d20b)
#### Tuesday 2023-07-18 21:00:33 by Maël Nison

Sets the default compression to 0 (#5526)

**What's the problem this PR addresses?**

Cache compression doesn't seem the best option nowadays:

- It adds significant time to installs
- It adds a non-negligible runtime overhead (partially related, #1817)
- It prevents Git from diffing archives when they're modified

Its main advantage is for some amazingly large packages, where storing
them inside a Git repository would be impossible (GitHub has a 600MB
file limit). But since we changed the cache default to
`enableGlobalCache: true`, this isn't relevant by default, so the cache
compression should be set to zero.

One potential issue is how it may give the impression that Yarn became
worse for global cache users. We don't believe it's the case (Git can
delta uncompressed archives in some measure, making it less expensive to
upgrade from one package version to another), but to the average eye it
may not look as such.

**How did you fix it?**

This diff sets the new default compression setting to 0.

To avoid breaking projects' (or at least not making the migration more
difficult), I added a rule to automatically set `compressionLevel` (and
`enableGlobalCache`) to their 3.x default values when running `yarn
install` in a 3.x project. When users are ready they can remove these
settings and re-run the install.

I kept the current compression level on our repository to avoid changing
all archives again. I think we'll have to think of purging the
repository in some form to migrate it to `compressionLevel: 0`.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [gabrielyotoo/berry](https://github.com/gabrielyotoo/berry)@[ec7f37a8ca...](https://github.com/gabrielyotoo/berry/commit/ec7f37a8ca118a6f73f848e993272db957f286d6)
#### Tuesday 2023-07-18 21:00:33 by Maël Nison

Modernizes installs' output (#5509)

**What's the problem this PR addresses?**

I wasn't entirely happy with the Yarn output:

- When running `yarn add`, we have no way to know what packages are
actually added to the lockfile. The cache messages sometimes help, but
with zero-installs now being opt-in, in many cases the packages would
already be in the cache and thus wouldn't be displayed at all.

- The "can't be found in the cache and will be fetched from the remote
registry" messages were incredibly slow to print - the same install
would take 28s install for Gatsby on a local iTerm 2 without those logs,
vs almost 2 minutes with. They also weren't very useful: we were only
showing the last 5 of them, and with zero-installs being opt-in in many
cases they wouldn't be shown at all.

- The `node-gyp` warnings were for the most part unactionable (at best
the user would pin a fixed version in their `packageExtensions` field,
which I suspect no one ever did).

- The `deprecated` warnings were for the most part unactionable, and
only printed in very specific cases (the first time they were added to
the project).

- The "missing / invalid peer dependency" warnings were actionable, but
in practice no one really look at them except when something breaks -
and even then, it becomes unreadable when there are too many of them.

- The skipped build warnings were printed every single time you ran
`yarn install`. It's nice to know the first time, then it quickly
becomes redundant.

Fixes #4165

**How did you fix it?**

I went a little overboard and did everything in the same PR ... at first
I thought I wouldn't have to change unrelated parts, but then I finished
implementing the skipped build warnings duplicate removal and oh no 🙈

- Only peer dependency warnings caused by workspaces are now reporter.
They have also been moved inside the post-resolution validation step.
The resolution step is now expected to only do one of two things: either
report an error when the resolution fails, or report the packages which
got added / removed from the lockfile.

- The `node-gyp` warnings have been removed.

- The `deprecated` warnings have been removed from the install. The
`yarn npm audit` command now reports deprecated packages, although this
can be disabled using `--no-deprecations` (or any of the audit filtering
settings).

- The "can't be found in the cache" messages have been removed. Instead,
the fetch step will report the number of cache hits / cache misses once
it's finished (same behaviour as `preferAggregateCacheInfo`). The size
delta will also be reported.

- Packages whose build was skipped are now stored within
`Project#skippedBuilds`, which is stored within the install state file.
Warnings are only emitted if the install was skipped for the first time.
To see the messages again, users can run `yarn rebuild`.

- Added the Yarn version on installs. A bit because of branding when
screenshot are taken, but mostly so we easily know what version are
people using when they share screenshots to us. In a follow-up PR I'd
like to try to retrieve the latest version from the website, to let them
know once one is available.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [gabrielyotoo/berry](https://github.com/gabrielyotoo/berry)@[3626ea2ae3...](https://github.com/gabrielyotoo/berry/commit/3626ea2ae3e48ee26771b15b92292a28afe3d49d)
#### Tuesday 2023-07-18 21:00:33 by Maël Nison

Adds support for running native binaries without JS intermediaries (#5508)

**What's the problem this PR addresses?**

Yarn currently cannot run native binaries without going through a JS
jumper script. Other package managers don't have this restriction, and
it makes the `yarn run` overhead worse on some scripts for little
reasons - or doesn't work at all when packages don't use jumper scripts.

**How did you fix it?**

Two mechanisms are used:

- First we check for the binary extension
- Then we check its magic number

If one of the two match a predetermined list, the binary is spawned
without going through Node. This ensures that this logic is called only
when the binary is truly a native binary, and will not affect the
behaviour of other existing scripts.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [Lunar248/Skyrat-LuneStation](https://github.com/Lunar248/Skyrat-LuneStation)@[9e1d33a309...](https://github.com/Lunar248/Skyrat-LuneStation/commit/9e1d33a309505d1651678bf9fd6e0e8a154615d0)
#### Tuesday 2023-07-18 21:01:06 by GoldenAlpharex

[MANUAL MIRROR] SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags [MDB IGNORE] (#22516)

* SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

Bugs are bad they make you mad

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

* Fixed a compile error (whoops)

* Whoops fixed that wrong

* Okay now I compiled and made sure it was fixed for real, I swear!

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [Lunar248/Skyrat-LuneStation](https://github.com/Lunar248/Skyrat-LuneStation)@[4aec91cc06...](https://github.com/Lunar248/Skyrat-LuneStation/commit/4aec91cc069b1beb1ec6593522dc5f65f7c5c7aa)
#### Tuesday 2023-07-18 21:01:06 by GoldenAlpharex

[MANUAL MIRROR] Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [Dangerlurking/sojourn-station](https://github.com/Dangerlurking/sojourn-station)@[94b32aa82c...](https://github.com/Dangerlurking/sojourn-station/commit/94b32aa82cdfdf4b9115d178c89e9cd3a7ede6d2)
#### Tuesday 2023-07-18 21:22:53 by CDB

Bugfixes. (#4685)

* Bugfixes.

Fixes a few spelling mistakes here and there.

Forged stock-parts boxes claimed they had five parts inside. they did not, they have four, corrected.

Toga for the church had an eronious base-state, unsure who touched it, but fix'd.

Bat'ko had incorrect formatting for its on-suit sprite, fixed.

Numerical garb eroniously claimed to be switchable between grey and red. It was actually purple and red, fixed.

Numerical hats both had the wrong icon name and were using(incorrectly) the old sprites. Fixed.

Duty had a missing icon when loaded with a drum and fempty(Who the FUCK let the duty take drums?)

Fixes the sec-shuttle and also comments out the destination it has towards the space fortress which is...commented back out? Right?

Fixes the apparent sec-shuttle so its walls are properly named after the vessel. To do- give some fucking flavor to the Rocinante and Vasiliy.

* Update body_modifications.dm

Removes the ability to select robo-torsos/groins/heads, this functionality doesn't actually work as intended and wasn't intended to be used in this way. Feel free to re-add if it does get fixed.
fixes #4675

* More bugfixes

Fixes tesla turrets attacking colony bots, SI drones, etc.

Fixes embed chance on the psion knife being greater than 0 and thus being able to embed(and promptly bugging out.)

* Update tesla_turret.dm

Slight tweak to Tesla turret code courtesy of Hex.

* Further bugfixes.

RXbow lacked a proper caliber and could thusly accept 10mm rounds.

RXbow also lacked a casing handling tag, not that it makes a huge difference given its snowflake behavior but it was fixed.  I will suggest to perhaps raise the d amage of the crossbow bolt in another non-bug focused PR.

Artificer rail pistols(slab and myrmidon) didn't have a serial defined, fixed.

* More fixes.

Mop bucket now properly updates its sprite after any change to its reagents takes place.

Kitchen spike no longer erroneously requires a strangle grab instead of a neck_grab.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[ca6364596a...](https://github.com/wrye-bash/wrye-bash/commit/ca6364596a74602a2f348c572f8d1869d4fd165d)
#### Tuesday 2023-07-18 22:12:02 by Infernio

Rework temporary file handling RRR TTT

View with whitespace diff off for an easier time (--ignore-all-space).

This turned out to be a lot more work than I thought. Really should have
been a branch, but I misjudged this horribly, then it kept growing...
Also not sure how feasible this would be to have as a branch without
breaking dev.

Wrye Bash's temporary files handling was actually a complete mess. There
were *three* different ways that random pieces of code were using it:
 - bass.getTempDir/newTempDir/rmTempDir
 - Path.temp and Path.untemp
 - Just use Path.baseTempDir/tempDir or even tempfile directly and do
   it completely manually.

These all had problems:
 - The bass APIs were very implicit - you would extract something to the
   'bass temp dir' and then access it via getTempDir in some other
   function, then remove the directory via rmTempDir in another
   function. XXX I'm still not done tracking this implicit mess down
   (see converters.py).
 - Path.temp did not guarantee that the file would be unique. This isn't
   really a problem for Wrye Bash right now, but would become a big
   problem if we ever wanted to allow multiple instances to run at the
   same time (which we do). Path.untemp also did some really weird I/O
   stuff that doesn't seem necessary at all and would just cost us a
   bunch of syscalls.
 - Path.baseTempDir/tempDir and tempfile required you to keep track of
   all the path manipulation and logic manually. After going through all
   this refactoring, trust me when I say that you do *not* want to do
   this manually. These places were few, thankfully, and none seem to
   have messed it up.

The new API (wbtemp.py) exposes two ways to do it:
 - Use TempDir or TempFile in a context manager. This is extremely
   simple and works very well. It guarantees that the file will be
   cleaned up, even if your logic becomes very complex or an exception
   occurs.
 - Use new_temp_dir/new_temp_file to create a temporary dir/file and
   manually clean it up via cleanup_temp_dir/cleanup_temp_file. These
   should be used *very sparingly*, only where absolutely needed.
   Right now we only have a single usage of manual temp files in
   dialogs.UpdateNotification and two usages of manual temp dirs (one in
   InstallerArchive.unpackToTemp and one in env.shellMakeDirs).

It also has other advantages:
 - Complexity is encapsulated to a single file.
 - Works even during (very) early boot (though doesn't seem to be
   needed right now?).
 - Should work perfectly with multiple instances of WB running at the
   same time (which isn't possible yet, but is a goal for the future).

There's one ugly wart. barb wants to extract archives to a temporary
folder, which then needs to survive a restart of WB, whereupon it will
be handled by the boot '--restore' handler. wbtemp, by design, does not
allow this and will clean up all created directories and files on exit.
To handle this, I used manual tempfile fiddling. Perhaps a future
refactoring of barb could fix this, but for now I think it's an
acceptable tradeoff for the massive improvements this commit brings us.

Some random stuff that got stuck in here:

Note that I got rid of the utf-8-sig encodings passed to 7z, the docs
say:

  Notes: The list file in Unicode charset can start with the BOM (byte
  order mark) character (U+FEFF). In that case 7-Zip checks that
  encoding of BOM corresponds to encoding specified with this switch
  (for UTF-16LE and UTF-16BE).

and:

  Default charset is UTF-8.

From https://7-zip.opensource.jp/chm/cmdline/switches/charset.htm
Very happy to see some of these terrible BOMs disappear from the
codebase.

Mopy/bash/basher/gui_fomod.py:
Some minor warning fixups in gui_fomod

Closes # 665 <--- RRR

Co-authored-by: lojack5 <1458329+lojack5@users.noreply.github.com>

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[16cecf864d...](https://github.com/Rhials/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Tuesday 2023-07-18 22:21:58 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

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

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

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
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[d12cab7a49...](https://github.com/Rhials/tgstation/commit/d12cab7a498f64df366eba748175405f8fd0ffef)
#### Tuesday 2023-07-18 22:21:58 by Sealed101

Collapsible lobby buttons (#76443)

## About The Pull Request
Adds a button to the new player HUD that allows collapsing and expanding
the menu buttons.
Also gives the buttons names so they can show up in the BYOND's prompt
on the bottom left.
Readiness is now also displayed in the status tab.
The menu HUD can be reset with a verb Reset Lobby Menu HUD in the OOC
tab.

### I SAW FOOTAGE


https://github.com/tgstation/tgstation/assets/75863639/2054c09d-48d7-4736-b862-4406667dde67

#### Here be dragons (dev progress footage)

#### GACHI BGM WARNING
<details><summary>Mk. I </summary>


https://github.com/tgstation/tgstation/assets/75863639/3e886254-bebd-4aa3-b7f7-5fdd8b7c9040

</details> 

___

<details><summary>Mk. II</summary>


https://github.com/tgstation/tgstation/assets/75863639/14d84a2d-1732-4700-aad0-df85c9befa86

</details> 

___

<details><summary>Mk. III (featuring: the shutter!) ((NOT featuring:
gachi BGM))</summary>


https://github.com/tgstation/tgstation/assets/75863639/98576c1f-6877-41b9-bec6-e11207501965


</details> 

___

<details><summary>Mk. IV (new collapse button sprite )</summary>

~~& shutter graffiti~~ (in a followup PR)

this video has a bug with the poll button lighting up without an active
poll, this was fixed before it was pushed


https://github.com/tgstation/tgstation/assets/75863639/6c0489e2-c80a-4682-b543-5d7c74071a39

</details> 

___

<details><summary>Mk. IV with updated shutter sprite and animation
speed</summary>

<sub>TIL github sanitizes ♂ and probably other ascii from file
names</sub>


https://github.com/tgstation/tgstation/assets/75863639/61ed85fe-8df6-4f38-91aa-1f70258289e7

</details> 

## TO-DO
- [x] A shutter that comes down and hides the buttons away. 
  - [ ] The shutter will have a chance to have silly graffiti on it.
- [x] Redesign and move the collapse/expand button to be a part of the
menu.

## Why It's Good For The Game
Banishes the curse cast upon lobby art. Ties in with the on-going lobby
art contest.


## Changelog
:cl:
qol: Lobby Menu buttons can now be collapsed. Rejoice!
qol: Lobby Menu buttons have names, which can be seen in the prompt on
the bottom left of the viewport.
qol: you may see your readiness status during pre-game in the Status
Bar.
qol: Reset Lobby Menu HUD verb added in case you manage to break the
damn thing.
/:cl:

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[daa33d89fe...](https://github.com/Capsandi/tgstation/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Tuesday 2023-07-18 22:54:37 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [FranklinPenaDev/My-Codewars-soultions](https://github.com/FranklinPenaDev/My-Codewars-soultions)@[53a9eae5e4...](https://github.com/FranklinPenaDev/My-Codewars-soultions/commit/53a9eae5e43198d95c02858f733980873aec216f)
#### Tuesday 2023-07-18 23:54:11 by Franklin

Create I love you, a little , a lot, passionately ... not at all

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

"I love you"
"a little"
"a lot"
"passionately"
"madly"
"not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

---

