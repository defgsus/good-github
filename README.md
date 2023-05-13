## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-12](docs/good-messages/2023/2023-05-12.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,032,151 were push events containing 3,372,137 commit messages that amount to 243,524,509 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [uvatbc/linux](https://github.com/uvatbc/linux)@[1bba82fe1a...](https://github.com/uvatbc/linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Friday 2023-05-12 00:00:02 by Darrick J. Wong

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
## [Rat-Time/Liberty-Station-13](https://github.com/Rat-Time/Liberty-Station-13)@[c3e6d8b901...](https://github.com/Rat-Time/Liberty-Station-13/commit/c3e6d8b90198a54e05d8d7e886aa5435c9a9af22)
#### Friday 2023-05-12 00:02:30 by KayZach

Add files via upload

Holy shit my first ever pr ever i probably broke six other things but i tested it
Unfucks the broken wire in Terra therma
Removes the light switch in medical so seb can see
fixes the morgue boxes that are facing the wrong way in capsa
adds a gambling table and some more plants to skylight

---
## [jnutt367/parables](https://github.com/jnutt367/parables)@[f54849c810...](https://github.com/jnutt367/parables/commit/f54849c810e46d0aa504607feb9676d95ec3e87d)
#### Friday 2023-05-12 00:03:33 by Jason Nutt (He/Him) Christian Developer/Creator

Update Home.module.css

To some who were confident of their own righteousness and looked down on everyone else, Jesus told this parable: “Two men went up to the temple to pray, one a Pharisee and the other a tax collector. The Pharisee stood by himself and prayed: ‘God, I thank you that I am not like other people—robbers, evildoers, adulterers—or even like this tax collector. I fast twice a week and give a tenth of all I get.’

“But the tax collector stood at a distance. He would not even look up to heaven, but beat his breast and said, ‘God, have mercy on me, a sinner.’

“I tell you that this man, rather than the other, went home justified before God. For all those who exalt themselves will be humbled, and those who humble themselves will be exalted.”

---
## [miampf/wave](https://github.com/miampf/wave)@[aff20b3f36...](https://github.com/miampf/wave/commit/aff20b3f366c38df91183a8dd5b90f815ba9b740)
#### Friday 2023-05-12 00:10:49 by miampf

done some shit, fixed the buildsystem again ig? sorry for the ugly commit :'')

---
## [TheFinalEntity/TGC1e](https://github.com/TheFinalEntity/TGC1e)@[1240de382d...](https://github.com/TheFinalEntity/TGC1e/commit/1240de382d9d970cbd159ba20a10954d697d912f)
#### Friday 2023-05-12 00:19:34 by TheFinalEntity

Added Edited BW05FFAP.CRE File

Hello,
I have been playing in a modded BGEE multiplayer run with some friends and we were having some trouble with the injured woman not spawning and/or being removed immediately after being manually spawned with the console. I took the liberty of fixing the issue, which actually happened to be really easy. Checking the creature file of the injured woman (BW05FFAP.CRE) I noticed that her class levels were set to 9/1/1, her HP was 5/54 and her state was set to diseased. I changed her state to normal and spawned her again and she stayed in game. I was able to complete the dialog with her with no issues.

I then checked the GLOBAL variable for the quest advancement via console CLUAConsole:GetGlobal("BW05_TGC1","GLOBAL"). This variable value should be 5 prior to conversing with her and 6 afterward. This was the case when I tested it. I then loaded a previous save to ensure that she would spawn properly after the enemies were defeated in the area in which she spawns and she spawned and conversed properly. The GLOBAL variable was also updated properly yet again.

I believe the issue was that her con is 9 and her current HP was 5 and whatever disease she had was applying a con penalty to her and thus reducing her total HP by 1/level for 9/1/1 levels and thus bringing her to negative HP. So when spawning her in the game with CurrentHP < 0 the game engine was statically removing her and since she wasn't reduced to 0 or less HP while spawned in game she didn't actually die and thus there would be no death animation/sound/text and no body left in game, since she was statically removed. I could be wrong, but this seems to be the case.

---
## [Gand0r/terminal](https://github.com/Gand0r/terminal)@[9ccd6ecd74...](https://github.com/Gand0r/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2023-05-12 01:14:36 by Mike Griese

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
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[4dae4ab28e...](https://github.com/Offroaders123/NBTify/commit/4dae4ab28e195f350a3793b58b1d437a4bc996ff)
#### Friday 2023-05-12 01:44:58 by Offroaders123

Internal Type Insecurities

While the types for the tags are nearly perfect (of course, they can't actually really be perfect), I realize that the `ListTag` and `CompoundTag` types aren't typed strong enough, out of everything in the library. I'm going to work on refactoring things as a whole, there's starting to be more things I see being able to make improvements to, because I can move logic for things both into dedicated functions, and to make use of stronger type checking which will ensure that values are actually what they are when they are being accessed. Right now, I'm not quite doing the full checking on the shapes and content of each tag, and that could cause more problems that could be uncaught, even with the types I currently have for things.

I'm going to further strengthen the checking on each value and structure individually, rather than asserting it through error catching at the entry points to each part of the API. So, essentially I want to make more use of internally representing values as unknown, and only having type definitions on the outside, then type checking within the library itself. What that means, the users will see the intended types of the library from the outside, but the library will instead start treating all values as `unknown`, since I want to intentionally find out their types, and remove any unsafe data (things like the unsupported types `Function`, `symbol`, `null`, `undefined` for example). I don't want to do this magically, I want to start purposefully managing these checks using the internal types within the library itself. Right now I just have to remember to add these checks in myself, wherever I know they haven't been sanitized yet. So I think this in part has to do with my now understanding of the uncertainty behind not having proper API type checks within the library, which will check if the incoming `CompoundTag` structures are valid, including valid properties and such. And I think this means it will (un?)realistically allow for the API to have `unknown` entry point values, and the library should be still type safe internally, where to the point it will not throw errors, because the proper checks are in place to actually be able to deduce the types of the NBT data object structures themselves, not only by the API types themselves.

This is just an idea as of now, so I may not end up going through making everything this solidly strict. I think that would be very good in terms of strictness and safety, but it might be redundant in a few (or, a lot) of places. So I may just implement these ideas in places of the library where it tends to be less safe or forgiving than others (`CompoundTag` entries, `ListTag` items).

I want to move the library into a more functionally-driven nature I think now too, driven by modules and smaller functions, instead of logic-obscuring classes which hide implementation details away. While I do like that structure of defining things (at least it was pretty nice at first), I am starting to see more problems where I want to use similar logic in other places, and I can't apply those in other places outside of that one use case. One big example was the SNBT to type definition generator logic. Both are very similar in what they do, and parse the NBT data tree, but they aren't similar enough to be a single class, and I don't want to use inheritance to find the similarities between the two. Sounds veery ugly. As a single class, which does it's own things though, I guess I do like that model. Maybe if it's just for simpler, more standalone things it can be ok. I think working on my other world data projects, I found that using functions to pass data between each other is more dynamic, in the fact that you don't have to relate two things together in order to be able to use them with each other. You just pass the value from one call into the next. You don't have to use encapsulation to pool all of the state into a singular place, instead you can pipe it into different canals that go to different places, and eventually go to the finish line. The rivers can at times cross paths too, and use the same roadway (sorry for these horrible analogies today), and break off again, using a different function to modify it's output just a little bit different than it's neighbor Angela, who simply uses the same river (function) to get from the starting line to the finish line. (not sure who Angela is, just dove into making the analogy worse)

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[2068ea9ab5...](https://github.com/MrMelbert/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Friday 2023-05-12 02:01:12 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[c2d75696c8...](https://github.com/Hatterhat/Skyrat-tg/commit/c2d75696c8d0012027bf97a15b2c0e332416b497)
#### Friday 2023-05-12 02:19:29 by SkyratBot

[MIRROR] Nerfs the firing speed of Syndicate/Russian mobs [MDB IGNORE] (#21047)

* Nerfs the firing speed of Syndicate/Russian mobs (#75247)

## About The Pull Request

Nerfs their firing speed from once every 0.2 seconds to once every 2.5
seconds

## Why It's Good For The Game

1. The mob that is NOT a 'burst' type mob, is firing every 0.2 seconds.
Kinda defeats the point of having them as two separate mobs, so this
aims to fix that.
2. Russian mobs. Turns out that letting them fire their strong-ass gun
every 0.2 seconds was kinda not a good idea. I had assumed making them a
Syndicate mob would be safe, and it technically is, it's just that
Syndicate mob is fucked itself.

## Changelog

:cl:
balance: Default Syndicate and Russian gunners now fire every 2.5
seconds instead of every 0.2
/:cl:

* Nerfs the firing speed of Syndicate/Russian mobs

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [CloudGeometry/kibana](https://github.com/CloudGeometry/kibana)@[3b6b7ad9b9...](https://github.com/CloudGeometry/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Friday 2023-05-12 02:33:35 by Pierre Gayvallet

SavedObjectsRepository code cleanup (#157154)

## Summary

Structural cleanup of the `SavedObjectsRepository` code, by extracting
the actual implementation of each API to their individual file (as it
was initiated for some by Joe a while ago, e.g `updateObjectsSpaces`)

### Why doing that, and why now?

I remember discussing about this extraction with Joe for the first time
like, what, almost 3 years ago? The 2.5k line SOR is a beast, and the
only reason we did not refactor that yet is because of (the lack of)
priorization of tech debt (and lack of courage, probably).

So, why now? Well, with the changes we're planning to perform to the SOR
code for serverless, I thought that doing a bit of cleanup beforehand
was probably a wise thing. So I took this on-week time to tackle this (I
know, so much for an on-week project, right?)

### API extraction

All of these APIs in the SOR class now look like:

```ts
  /**
   * {@inheritDoc ISavedObjectsRepository.create}
   */
  public async create<T = unknown>(
    type: string,
    attributes: T,
    options: SavedObjectsCreateOptions = {}
  ): Promise<SavedObject<T>> {
    return await performCreate(
      {
        type,
        attributes,
        options,
      },
      this.apiExecutionContext
    );
  }
```

This separation allows a better isolation, testability, readability and
therefore maintainability overall.

### Structure

```
@kbn/core-saved-objects-api-server-internal
  - /src/lib
    - repository.ts
    - /apis
      - create.ts
      - delete.ts
      - ....
      - /helpers
      - /utils
      - /internals
```    


There was a *massive* amount of helpers, utilities and such, both as
internal functions on the SOR, and as external utilities. Some being
stateless, some requiring access to parts of the SOR to perform calls...

I introduced 3 concepts here, as you can see on the structure:

#### utils

Base utility functions, receiving (mostly) parameters from a given API
call's option (e.g the type or id of a document, but not the type
registry).

#### helpers

'Stateful' helpers. These helpers were mostly here to receive the
utility functions that were extracted from the SOR. They are
instantiated with the SOR's context (e.g type registry, mappings and so
on), to avoid the caller to such helpers to have to pass all the
parameters again.

#### internals

I would call them 'utilities with business logic'. These are the 'big'
chunks of logic called by the APIs. E.g `preflightCheckForCreate`,
`internalBulkResolve` and so on.

Note that given the legacy of the code, the frontier between those
concept is quite thin sometimes, but I wanted to regroups things a bit,
and also I aimed at increasing the developer experience by avoiding to
call methods with 99 parameters (which is why the helpers were created).

### Tests

Test coverage was not altered by this PR. The base repository tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.test.ts`)
and the extension tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.{ext}_extension.test.ts`)
were remain untouched. These tests are performing 'almost unmocked'
tests, somewhat close to integration tests, so it would probably be
worth keeping them.

The new structure allow more low-level, unitary testing of the
individual APIs. I did **NOT** add proper unit test coverage for the
extracted APIs, as the amount of work it represent is way more
significant than the refactor itself (and, once again, the existing
coverage still applies / function here).

The testing utilities and mocks were added in the PR though, and an
example of what the per-API unit test could look like was also added
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/apis/remove_references_to.test.ts`).

Overall, I think it of course would be beneficial to add the missing
unit test coverage, but given the amount of work it represent, and the
fact that the code is already tested by the repository test and the
(quite exhaustive) FTR test suites, I don't think it's worth the effort
right now given our other priorities.

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [saltwaterterrapin/EvilHack](https://github.com/saltwaterterrapin/EvilHack)@[2b045340a7...](https://github.com/saltwaterterrapin/EvilHack/commit/2b045340a7a4072faadc2c62d3030c7c54374fdb)
#### Friday 2023-05-12 02:57:58 by k21971

Fix: aura of darkness could snuff out/curse other sources of darkness; shadow dragon scales aura of darkness hurting light haters.

Quite a few fixes in this commit:

* player or monster casting an aura of darkness was putting out or
diminishing sources of darkness (cursed magic lamps, shadow dragon
scales/dragon-scaled armor, Drow wielding the Staff of the Archmagi)
* same effect could curse the same source if using artifact_light() to
give off darkness
* Drow wearing shadow dragon scales/dragon-scaled armor were hurt by the
initial aura of darkness they cast

And while I was here, I noticed that blessed scrolls of light were not
putting out cursed magic lamps, and would augment or even bless sources
of darkness that used artifact_light(). So that's been addressed too.

Thanks terrapin for the assist.

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[f10b0dd42a...](https://github.com/ynot01/tgstation/commit/f10b0dd42aa996971f472edb7e65b3e504cb7ec5)
#### Friday 2023-05-12 04:01:29 by 13spacemen

Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[fe7ebd67cf...](https://github.com/ynot01/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Friday 2023-05-12 04:01:29 by LemonInTheDark

Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[0a1f7e8de2...](https://github.com/ynot01/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Friday 2023-05-12 04:01:29 by Hatterhat

Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [peff/git](https://github.com/peff/git)@[701783b690...](https://github.com/peff/git/commit/701783b6904ffc7a7afd93088a488df4f8a3ead6)
#### Friday 2023-05-12 04:09:39 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[ddf56cbdef...](https://github.com/newstools/2023-new-york-post/commit/ddf56cbdef649ff5d930dcf97c95f111724230ec)
#### Friday 2023-05-12 04:36:22 by Billy Einkamerer

Created Text For URL [nypost.com/2023/05/11/nyc-man-gets-16-years-to-life-for-slashing-his-ex-girlfriend/]

---
## [enso-org/enso](https://github.com/enso-org/enso)@[4b7afbfd36...](https://github.com/enso-org/enso/commit/4b7afbfd3619c22b6b31f2840fa807f0af41fb57)
#### Friday 2023-05-12 04:55:02 by Ilya Bogdanov

Fix blank input port (#6614)

Fixes #6485

Conflicting requirements for the widget tree caused the issue:
1. The span tree node had a connection, and the text of the `number1` label was changed to white (as per the `Connected` color state)
2. The node configuration did not consider it a valid port because the span tree kind was `Operation`, which is not a port usually. So the port shape was not displayed, making the label blend with the node background.

I fixed the issue by considering the existence of the current connection for `Operation` nodes. Remember that it does not turn the node into a port, so after removing the connection, it's not possible to connect it back. That makes sense, in my opinion, as the resulting AST is invalid anyway. But at least we can see the label on the invalid node.


https://github.com/enso-org/enso/assets/6566674/23934966-8f72-4675-abe3-78a3f0c0cda4

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[1a918a2e14...](https://github.com/Jackraxxus/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Friday 2023-05-12 05:07:01 by Jacquerel

Golem Rework (#74197)

This PR implements this design document:
https://hackmd.io/@Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[f3549a4aec...](https://github.com/Rex9001/Rex-station-/commit/f3549a4aeca6701a2969a63b7d4034d5bc560cb6)
#### Friday 2023-05-12 05:39:30 by Thunder12345

De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

---
## [CarlosSciData/Found_Stats_2023](https://github.com/CarlosSciData/Found_Stats_2023)@[84ee3a75e6...](https://github.com/CarlosSciData/Found_Stats_2023/commit/84ee3a75e6fbf6dbcd52b9392ee15c91156c9cc2)
#### Friday 2023-05-12 06:06:39 by CarlosSciData

Create FoundStats_2023_PS3.html

## Part 4 Reflection (25 pts)
Answer the following questions in a couple of sentences each. No right or wrong answers! (5 pts each)

1. Since we have reached the end of the first half of the term, reflect on your coding skills. How does where you are now compare to how you felt at the beginning of this term?

I think have definitely have more practice with R which makes me more comfortable using it in new ways.Unix/Linux looked more intimidating in the beginning then it actually was and I believe I have a solid foundation in it now.

2. What aspects of the class structure have been helpful and that you'd like to see continued?

I like how we have the ability to practice code during class and that it's not all just lecture. I also like how the homework is directly related to what we learned in class that week.

3. Are there aspects of the class structure that could be improved to help your learning?

Perhaps talking more about the logic of how these functions work. What I mean is spending more time defining things like what a string is or what an index is can help us when during our homework and in class practice. Especially in the beginning, spending more time getting us immersed in what the vocabulary of coding is. I wish the class what a bit longer honestly (like an extra 20 minutes) so that we can discuss the more conceptual while maintaining the in class practice.

4. Take a look at the syllabus schedule for the second half of the term. Are there any topics in particular that seem more exciting or useful for you?

I feel most excited about the statistics portion of the class because I want to know how use R for this purpose. I think this will be the majority of what I'll use R for in my research.

5. Are there any other basic coding skills that you wish we would have covered in this class, that we could try to incorporate in this class for next year?

Perhaps learning about how to translate the skills from one language into another. I feel like many coding languages have different vocabulary for the same thing. So for example, comparing R with Python might be a good way to apply our knowledge of R to another programming language.

---
## [nitromelon/akathon1_gamestore](https://github.com/nitromelon/akathon1_gamestore)@[42daeb1ec4...](https://github.com/nitromelon/akathon1_gamestore/commit/42daeb1ec4ba29538d68c42aea739f5aa9bd2698)
#### Friday 2023-05-12 06:53:33 by nitromelon

Bug this bug that I hate my life
Changes to be committed:
	modified:   src/lib/app/payment/file.svelte
	modified:   src/lib/app/product/file.svelte
	modified:   src/lib/app/product/game/file.svelte
	new file:   src/lib/app/product/product.ts
	modified:   src/lib/app/product/search/file.svelte
	modified:   src/lib/main_screen/cursor/c.svelte

---
## [nfagerlund/bevy-tablestakes](https://github.com/nfagerlund/bevy-tablestakes)@[11038ff4d8...](https://github.com/nfagerlund/bevy-tablestakes/commit/11038ff4d86cf0713cf02a3d018ec01be94d94eb)
#### Friday 2023-05-12 07:00:25 by Nick Fagerlund

Bah ok I can't construct a Cursor at all outside default().

(Though the public fields are mutable if need be.)

By the way! With this, everything actually seems to be working EXCEPT the
space-flattener system, which is fucked because we lost translation_mut() on
GlobalTransform. But, I think we can work around that, and outside the extract
schedule, too — after all, I just went to the trouble of adding that whole
PhysTransform system! But, I'll have to expand it and I think I'll have to make
almost everything adopt it, including the shadows themselves.

But yeah anyway my theory is that since PhysTransform gives us an effectively
global reference frame anyway, we should be able to use it in place of
GlobalTransform for this.

---
## [JameH2/Hbm-s-Nuclear-Tech-GIT](https://github.com/JameH2/Hbm-s-Nuclear-Tech-GIT)@[12f667937e...](https://github.com/JameH2/Hbm-s-Nuclear-Tech-GIT/commit/12f667937ec4ac3536aced79936f1ff224509adf)
#### Friday 2023-05-12 07:19:23 by JameH2

holy SHIT

GITHUB, HOW HARD IS IT TO RENAME A FUCKING FILE

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[6ad8cd0a63...](https://github.com/ianjoneill/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Friday 2023-05-12 07:48:14 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[fc1471c818...](https://github.com/Sonic121x/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Friday 2023-05-12 08:26:50 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [GaiaByTeamLime/firmware-v2](https://github.com/GaiaByTeamLime/firmware-v2)@[116a814e48...](https://github.com/GaiaByTeamLime/firmware-v2/commit/116a814e483e89163f0e95dd99671c289b54fa74)
#### Friday 2023-05-12 08:39:54 by jaschutte

Fixed a comment

Sander has stolen my sanity, I don't think I'll be the same man after this.
We reverted the revert, and for what? Just to create another pull-request?
Is this what my life has resorted too? Pull-requests for a single comment change?
Was it worth it? Was all this pain and suffering worth it? Just for a single correction in a comment?
I hope it is, as it has costed me my life. And with that, my sanity.
I am a changed man. I can never be the same.
Goodbye.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0e096e0971...](https://github.com/treckstar/yolo-octo-hipster/commit/0e096e09716d676918c8e16f223948ccfffa5760)
#### Friday 2023-05-12 10:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [AnimeAllstar/ubccsss.org](https://github.com/AnimeAllstar/ubccsss.org)@[17535fd8bd...](https://github.com/AnimeAllstar/ubccsss.org/commit/17535fd8bd547ba27171b824bb6722646b30d237)
#### Friday 2023-05-12 11:35:14 by csssbot

New review for CPSC 210 by ubcstudent2 (#443)

> The concepts in this course are useful. The course overall is good,
but I have a big issue with PraireLearn just makes everything so much
harder for no reason. In this class we use a system called PrairieLearn
for exams and practice exams. To put it frankly, this system is
horrible. First of all, why are we writing code in a web browser? This
course should learn from its pre-req CPSC 110 and move onto programming
in an IDE for exams and all practices. Also it should really have
autograders. Trying to match our answers with the solution when the
solution can be often coded in maybe ways is horrible.

For practice problems, you can only answer the question once, if you
want to try again, you have to creat another instance of the whole
practice set. The text editor is bulky and annoying. Exams seriously
tests more on predicting what the question writer wants. It is also very
hard to perfect grades, because of multiple choice. You can easily get 0
on a question if you just miss a few details.

PraireLearn randomizes the order of answer choices for some reason.
Consider this arbitrary case , if the question involves 3 variables,
usually the question would list the answer choices (1 1), (1 2), (2, 1),
(2, 2), (3, 1), (3, 2) or in some other order. With the order randomized
it could be (2, 2), (1 2), (1 1), (3, 1) , (2, 1), (3, 2). Which messes
up the flow of natural problem solving especially when the answer
choices are full sentences and you need to pick out which parts are
different.

PraireLearn randomizes variable names. Again, this makes every
unnecessarily harder for no reason. They love using arbitrary names with
no meaning at all like "smurf", "lorem", "ipsum." Again, you have to
look back and forth to the question. Even if they just used random
everyday words, it would make it easier.

The questions are just not that clear. If you have a slightly different
interpretation you can expect a maximum of 50% on that question.

Overall the course material is very very easy, but the PraireLearn
system just suck. 0/10. It adds so much extra resistance to the
otherwise very easy course material. CPSC 210 can easily be a 3 credit
course. Also its hard to wrap my head around how a "second year"
computer science course at "a good" university has so much overlap with
Programming 10, 11, 12 in highschools.

>
> Difficulty: 2/5
> Quality: 2/5
> <cite><a href=''>ubcstudent2</a>, Apr 27 2023, course taken during
2022W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: ubcstudent2
    authorLink: 
    date: 2023-04-27
    review: |
The concepts in this course are useful. The course overall is good, but
I have a big issue with PraireLearn just makes everything so much harder
for no reason. In this class we use a system called PrairieLearn for
exams and practice exams. To put it frankly, this system is horrible.
First of all, why are we writing code in a web browser? This course
should learn from its pre-req CPSC 110 and move onto programming in an
IDE for exams and all practices. Also it should really have autograders.
Trying to match our answers with the solution when the solution can be
often coded in maybe ways is horrible.
      
For practice problems, you can only answer the question once, if you
want to try again, you have to creat another instance of the whole
practice set. The text editor is bulky and annoying. Exams seriously
tests more on predicting what the question writer wants. It is also very
hard to perfect grades, because of multiple choice. You can easily get 0
on a question if you just miss a few details.
      
PraireLearn randomizes the order of answer choices for some reason.
Consider this arbitrary case , if the question involves 3 variables,
usually the question would list the answer choices (1 1), (1 2), (2, 1),
(2, 2), (3, 1), (3, 2) or in some other order. With the order randomized
it could be (2, 2), (1 2), (1 1), (3, 1) , (2, 1), (3, 2). Which messes
up the flow of natural problem solving especially when the answer
choices are full sentences and you need to pick out which parts are
different.
      
PraireLearn randomizes variable names. Again, this makes every
unnecessarily harder for no reason. They love using arbitrary names with
no meaning at all like "smurf", "lorem", "ipsum." Again, you have to
look back and forth to the question. Even if they just used random
everyday words, it would make it easier.
      
The questions are just not that clear. If you have a slightly different
interpretation you can expect a maximum of 50% on that question.
      
Overall the course material is very very easy, but the PraireLearn
system just suck. 0/10. It adds so much extra resistance to the
otherwise very easy course material. CPSC 210 can easily be a 3 credit
course. Also its hard to wrap my head around how a "second year"
computer science course at "a good" university has so much overlap with
Programming 10, 11, 12 in highschools.
      
    difficulty: 2
    quality: 2
    sessionTaken: 2022W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[ae7595b8e1...](https://github.com/microsoft/terminal/commit/ae7595b8e13d4764f4db7b4060eaf57d1b4ee82e)
#### Friday 2023-05-12 12:10:40 by Mike Griese

Add `til::property` and other winrt helpers (#15029)

## Summary of the Pull Request

This was a fever dream I had last July. What if, instead of `WINRT_PROPERTY` magic macros everywhere, we had actual templated versions you could debug into. 

So instead of 

```c++
WINRT_PROPERTY(bool, Deleted, false);
WINRT_PROPERTY(OriginTag, Origin, OriginTag::None);
WINRT_PROPERTY(guid, Updates);
```

you'd do 

```c++
til::property<bool> Deleted{ false };
til::property<OriginTag> Origin{ OriginTag::None };
til::property<guid> Updates;
```

.... and then I just kinda kept doing that. So I did that for `til::event`.

**AND THEN LAST WEEK**

Raymond Chen was like: ["this is a good idea"](https://devblogs.microsoft.com/oldnewthing/20230317-00/?p=107946)

So here it is. 

## Validation Steps Performed
Added some simple tests.

Co-authored-by: Leonard Hecker <lhecker@microsoft.com>

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[0e2df4ad2e...](https://github.com/Road-to-56-RP/roadto56rp/commit/0e2df4ad2e6ec87b9de6595a032b7dcb60629862)
#### Friday 2023-05-12 12:13:46 by Warlider

Right Opposition Buff, Japan Shuffle, Manchurian additions

Russia: [Do not share with wider public.]
- Made "Eliminate Right" and "Eliminate Left" decisions for alt hist communism, remove your advisors from the kill pool and add oppositions advisors to it.
- Blodless coup will now always succeed if the head of the NKVD was aligned. All the random paranoia spikes are still there tho so entirely possible to fuck up and trigger a civil war, or to purge heads of NKVD and be left with Beria, where the success rate is 50/50 like in vanilla.

Japan:
- Moved Menjiang development under Manchurian project and made it 35 days long.
- Made Expand Railways 35 days long. Focus for manchu level 1 railroad and japan is supposed to spend 70 days on it? No.
- Moved the template unlock for editing Japan's space marine division into Army Expansion Law.
- Moved JAP_nishina_okochi_directive in parrarel to Divine Wind. Both require costly engineering research i dont see why you should be forced to grab suicide tech before nuclear one.

Manchuria:
-Made Illegitimate Goverment be a timed idea. Takes 2 years to disappear.

R56 Manchuria WIP:
- Removed all the annoying is subject checks breaking the focus tree as soon as japan decides to even look at alt hist.
- Shuffled some other shit around. Gonna make it viable later.

---
## [BoBIsHere86/libgdx](https://github.com/BoBIsHere86/libgdx)@[e1d1fdc5fb...](https://github.com/BoBIsHere86/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Friday 2023-05-12 12:21:03 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [harsnyi/Szoftver_Projekt_Lab_Sivatagi_vizhalozat](https://github.com/harsnyi/Szoftver_Projekt_Lab_Sivatagi_vizhalozat)@[a3f71cdbbc...](https://github.com/harsnyi/Szoftver_Projekt_Lab_Sivatagi_vizhalozat/commit/a3f71cdbbc2f7d594b0db2cb1204faf3bc4e8bb3)
#### Friday 2023-05-12 12:35:28 by Bálint Erdélyi

Red 🔴 📛 sus 💦 💦. Red 🔴 🔴 suuuus. I 👁👄 👁 said 🤠🗣 💬👱🏿💦 red 👹 🔴, sus 💦 💦, hahahahaha 🤣 🤣. Why 🤔 🤔 arent you 👉😯 👈 laughing 😂 😂? I 👁🍊 👥 just made 👑 👑 a reference 👀👄🙀 👀👄🙀 to the popular 👍😁😂 😂 video 📹 📹 game 🎮 🎮 "Among 🇷🇴🎛 💰 Us 👨 👨"! How can you 👈 👈 not laugh 😂 😂 at it? Emergeny meeting 💯 🤝! Guys 👦 👨, this here guy 👨 👱🏻👨🏻 doesnt laugh 🤣 ☑😂😅 at my funny 😃😂 🍺😛😃 Among 💰 💰 Us 👨 👨 memes 🐸 😂! Lets 🙆 🙆 beat ✊👊🏻 😰👊 him 👴 👨 to death 💀💥❓ 💀! Dead 💀😂 ☠ body 💃 💃 reported ☎ 🧐! Skip 🐧 🏃🏼! Skip 🐧 🐧! Vote 🔝 🔝 blue 💙 💙! Blue 💙 💙 was not an impostor 😎 😠. Among 😂 🙆🏽🅰 us 👨 👨 in a nutshell 😠 😠 hahahaha 😂👌👋 😂. What?! Youre still 🤞🙌 🤞🙌 not laughing 😂 😂 your 👉 👉 ass 🍑 🅰 off 📴 📴☠? I 👁 👁 made 👑 👑 SEVERAL 💯 💯 funny 😀😂😛 😃❓ references 👀👄🙀 📖 to Among 💰 💑👨‍❤️‍👨👩‍❤️‍👩 Us 👨 🇺🇸 and YOU 👈🏼 😂👉🔥 STILL 🤞🙌 🙄 ARENT LAUGHING 😂 😂😎💦??!!! Bruh ⚠ 😳🤣😂. Ya 🙏🎼 🙀 hear 👂 👂 that? Wooooooosh 💦👽👾 💦👽👾. Whats 😦 😦 woooosh 🚁 🚁? Oh 🙀 🙀, nothing ❌ 🚫. Just the sound 👂 🔊 of a joke 😂 😂 flying ✈ ✈ over 😳🙊💦 🔁 your 👉 👉 head 💆 💆. Whats 😦 🤔 that? You 👈 👉 think 💭 💭 im 👌 💘 annoying 😠 😠? Kinda 🙅 🙅 sus 💦 💦, bro 👆 🌈☺👬. Hahahaha 😂 😂! Anyway 🔛 🔛, yea 😀 💯, gotta 👉 👉 go 🏃 🏃 do tasks ✔ 📋. Hahahaha 😂 😂!

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Friday 2023-05-12 13:18:45 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[00f8bcfe75...](https://github.com/Sealed101/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Friday 2023-05-12 13:51:58 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction
 
- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one. 

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[3fdd716da5...](https://github.com/DrDiasyl/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Friday 2023-05-12 15:48:53 by Cheshify

Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[43473a4dac...](https://github.com/DrDiasyl/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Friday 2023-05-12 15:48:53 by san7890

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [RealMalachi/SCE-Dust-Edition](https://github.com/RealMalachi/SCE-Dust-Edition)@[1b6370195b...](https://github.com/RealMalachi/SCE-Dust-Edition/commit/1b6370195ba7dd5a1dd2e49d49567491aa28f73e)
#### Friday 2023-05-12 16:19:08 by Malachi

6 button controller state update

Honestly surprised it didn't click to me until now. Instead of leaving CtrlXState as is, it check what it was the previous frame and does the appropriate handler. This gives CtrlXState a more active use for regular controllers, although it is an unusual edgecase that doesn't effect real hardwa- ...oh. Uhh, apparently it can effect broken controllers. Huh.
Keep in mind, this version can run into an error if you were holding up and down when on 6pad, when switch to a 3pad on the same frame while still holding those buttons down. However, I think that scenario is kind of retarded, and even if it were a massive deal, the regular controllers are just too simple to fix it...
I kept the old version(s) commented. An error is an error, and if you don't like that, I encourage you to find a method that best suits you. That, and having pseudo-controller modes to fix an obscure error is kind of funny

---
## [GuilleHoardings/Open-Assistant](https://github.com/GuilleHoardings/Open-Assistant)@[b9c60ed582...](https://github.com/GuilleHoardings/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Friday 2023-05-12 16:26:49 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [Harrymanual/Formula_1_Website_React](https://github.com/Harrymanual/Formula_1_Website_React)@[5c7d76beb3...](https://github.com/Harrymanual/Formula_1_Website_React/commit/5c7d76beb3e0db8d47b2a625376c027ac638274c)
#### Friday 2023-05-12 16:38:32 by Harrymanual

This update is the most amount ive learned ever this is crazy

i finally understand html and its ridiculous the doors that just got opened to me. i can legitimately build something that is so goddamn awesome its not funny. i completely understand html but also i need to chamge the teampage template back to css but thats a job for another time. this has been one of the biggest walls ive hit in coding but i feel like now im significantly more in tune witht the computer. i would love to get into some lower level coding. super ecited to progress so much further into the project. i feel like now ive hit this step i dont want to change it becaise its such a big chapter wrapped up and igenuinely think i can build something amazing on the drivers button

---
## [mrgerwin/LOZ2023](https://github.com/mrgerwin/LOZ2023)@[47de89fd9d...](https://github.com/mrgerwin/LOZ2023/commit/47de89fd9d79f2550fac1bd2023948a272131a0e)
#### Friday 2023-05-12 16:59:15 by 25kbrown

ok boomer...

...ang (I'm so funny lol please laugh  haha I hate everything imma go home and play chess)

---
## [HidemaruOwO/dotfiles](https://github.com/HidemaruOwO/dotfiles)@[79ffda5621...](https://github.com/HidemaruOwO/dotfiles/commit/79ffda5621780787efacd1f67c6615489586c500)
#### Friday 2023-05-12 17:02:43 by HidemaruOwO

🗑️ zsh関連の設定の削除 (.p10k.zsh, .zshrc, oh-my-zsh/.editorconfig, oh-my-zsh/.github/CODEOWNERS, oh-my-zsh/.github/FUNDING.yml, oh-my-zsh/.github/ISSUE_TEMPLATE/bug_report.yml, oh-my-zsh/.github/ISSUE_TEMPLATE/bug_report_omz.yml, oh-my-zsh/.github/ISSUE_TEMPLATE/config.yml, oh-my-zsh/.github/ISSUE_TEMPLATE/feature_request.yml, oh-my-zsh/.github/PULL_REQUEST_TEMPLATE.md, oh-my-zsh/.github/workflows/main.yml, oh-my-zsh/.github/workflows/project.yml, oh-my-zsh/.gitignore, oh-my-zsh/.gitpod.Dockerfile, oh-my-zsh/.gitpod.yml, oh-my-zsh/CODE_OF_CONDUCT.md, oh-my-zsh/CONTRIBUTING.md, oh-my-zsh/LICENSE.txt, oh-my-zsh/README.md, oh-my-zsh/SECURITY.md, oh-my-zsh/lib/bzr.zsh, oh-my-zsh/lib/cli.zsh, oh-my-zsh/lib/clipboard.zsh, oh-my-zsh/lib/compfix.zsh, oh-my-zsh/lib/completion.zsh, oh-my-zsh/lib/correction.zsh, oh-my-zsh/lib/diagnostics.zsh, oh-my-zsh/lib/directories.zsh, oh-my-zsh/lib/functions.zsh, oh-my-zsh/lib/git.zsh, oh-my-zsh/lib/grep.zsh, oh-my-zsh/lib/history.zsh, oh-my-zsh/lib/key-bindings.zsh, oh-my-zsh/lib/misc.zsh, oh-my-zsh/lib/nvm.zsh, oh-my-zsh/lib/prompt_info_functions.zsh, oh-my-zsh/lib/spectrum.zsh, oh-my-zsh/lib/termsupport.zsh, oh-my-zsh/lib/theme-and-appearance.zsh, oh-my-zsh/lib/vcs_info.zsh, oh-my-zsh/oh-my-zsh.sh, oh-my-zsh/plugins/1password/1password.plugin.zsh, oh-my-zsh/plugins/1password/README.md, oh-my-zsh/plugins/1password/_opswd, oh-my-zsh/plugins/1password/opswd, oh-my-zsh/plugins/adb/README.md, oh-my-zsh/plugins/adb/_adb, oh-my-zsh/plugins/ag/README.md, oh-my-zsh/plugins/ag/_ag, oh-my-zsh/plugins/alias-finder/README.md, oh-my-zsh/plugins/alias-finder/alias-finder.plugin.zsh, oh-my-zsh/plugins/aliases/.gitignore, oh-my-zsh/plugins/aliases/README.md, oh-my-zsh/plugins/aliases/aliases.plugin.zsh, oh-my-zsh/plugins/aliases/cheatsheet.py, oh-my-zsh/plugins/aliases/termcolor.py, oh-my-zsh/plugins/ansible/README.md, oh-my-zsh/plugins/ansible/ansible.plugin.zsh, oh-my-zsh/plugins/ant/README.md, oh-my-zsh/plugins/ant/_ant, oh-my-zsh/plugins/ant/ant.plugin.zsh, oh-my-zsh/plugins/apache2-macports/README.md, oh-my-zsh/plugins/apache2-macports/apache2-macports.plugin.zsh, oh-my-zsh/plugins/arcanist/README.md, oh-my-zsh/plugins/arcanist/arcanist.plugin.zsh, oh-my-zsh/plugins/archlinux/README.md, oh-my-zsh/plugins/archlinux/archlinux.plugin.zsh, oh-my-zsh/plugins/asdf/README.md, oh-my-zsh/plugins/asdf/asdf.plugin.zsh, oh-my-zsh/plugins/autoenv/README.md, oh-my-zsh/plugins/autoenv/autoenv.plugin.zsh, oh-my-zsh/plugins/autojump/README.md, oh-my-zsh/plugins/autojump/autojump.plugin.zsh, oh-my-zsh/plugins/autopep8/README.md, oh-my-zsh/plugins/autopep8/_autopep8, oh-my-zsh/plugins/aws/README.md, oh-my-zsh/plugins/aws/aws.plugin.zsh, oh-my-zsh/plugins/battery/README.md, oh-my-zsh/plugins/battery/battery.plugin.zsh, oh-my-zsh/plugins/bazel/README.md, oh-my-zsh/plugins/bazel/_bazel, oh-my-zsh/plugins/bbedit/README.md, oh-my-zsh/plugins/bbedit/bbedit.plugin.zsh, oh-my-zsh/plugins/bedtools/README.md, oh-my-zsh/plugins/bedtools/_bedtools, oh-my-zsh/plugins/bgnotify/README.md, oh-my-zsh/plugins/bgnotify/bgnotify.plugin.zsh, oh-my-zsh/plugins/bower/README.md, oh-my-zsh/plugins/bower/_bower, oh-my-zsh/plugins/bower/bower.plugin.zsh, oh-my-zsh/plugins/branch/README.md, oh-my-zsh/plugins/branch/branch.plugin.zsh, oh-my-zsh/plugins/brew/README.md, oh-my-zsh/plugins/brew/brew.plugin.zsh, oh-my-zsh/plugins/bundler/README.md, oh-my-zsh/plugins/bundler/_bundler, oh-my-zsh/plugins/bundler/bundler.plugin.zsh, oh-my-zsh/plugins/cabal/README.md, oh-my-zsh/plugins/cabal/cabal.plugin.zsh, oh-my-zsh/plugins/cake/README.md, oh-my-zsh/plugins/cake/cake.plugin.zsh, oh-my-zsh/plugins/cakephp3/README.md, oh-my-zsh/plugins/cakephp3/cakephp3.plugin.zsh, oh-my-zsh/plugins/capistrano/README.md, oh-my-zsh/plugins/capistrano/_capistrano, oh-my-zsh/plugins/capistrano/capistrano.plugin.zsh, oh-my-zsh/plugins/cargo/README.md, oh-my-zsh/plugins/cargo/cargo.plugin.zsh, oh-my-zsh/plugins/cask/README.md, oh-my-zsh/plugins/cask/cask.plugin.zsh, oh-my-zsh/plugins/catimg/README.md, oh-my-zsh/plugins/catimg/catimg.plugin.zsh, oh-my-zsh/plugins/catimg/catimg.sh, oh-my-zsh/plugins/catimg/colors.png, oh-my-zsh/plugins/celery/README.md, oh-my-zsh/plugins/celery/_celery, oh-my-zsh/plugins/charm/README.md, oh-my-zsh/plugins/charm/charm.plugin.zsh, oh-my-zsh/plugins/chruby/README.md, oh-my-zsh/plugins/chruby/chruby.plugin.zsh, oh-my-zsh/plugins/chucknorris/.gitignore, oh-my-zsh/plugins/chucknorris/README.md, oh-my-zsh/plugins/chucknorris/chucknorris.plugin.zsh, oh-my-zsh/plugins/chucknorris/fortunes/chucknorris, oh-my-zsh/plugins/cloudfoundry/README.md, oh-my-zsh/plugins/cloudfoundry/cloudfoundry.plugin.zsh, oh-my-zsh/plugins/codeclimate/README.md, oh-my-zsh/plugins/codeclimate/_codeclimate, oh-my-zsh/plugins/coffee/README.md, oh-my-zsh/plugins/coffee/_coffee, oh-my-zsh/plugins/coffee/coffee.plugin.zsh, oh-my-zsh/plugins/colemak/.gitignore, oh-my-zsh/plugins/colemak/README.md, oh-my-zsh/plugins/colemak/colemak-less, oh-my-zsh/plugins/colemak/colemak.plugin.zsh, oh-my-zsh/plugins/colored-man-pages/README.md, oh-my-zsh/plugins/colored-man-pages/colored-man-pages.plugin.zsh, oh-my-zsh/plugins/colored-man-pages/nroff, oh-my-zsh/plugins/colorize/README.md, oh-my-zsh/plugins/colorize/colorize.plugin.zsh, oh-my-zsh/plugins/command-not-found/README.md, oh-my-zsh/plugins/command-not-found/command-not-found.plugin.zsh, oh-my-zsh/plugins/common-aliases/README.md, oh-my-zsh/plugins/common-aliases/common-aliases.plugin.zsh, oh-my-zsh/plugins/compleat/README.md, oh-my-zsh/plugins/compleat/compleat.plugin.zsh, oh-my-zsh/plugins/composer/README.md, oh-my-zsh/plugins/composer/composer.plugin.zsh, oh-my-zsh/plugins/copybuffer/README.md, oh-my-zsh/plugins/copybuffer/copybuffer.plugin.zsh, oh-my-zsh/plugins/copydir/README.md, oh-my-zsh/plugins/copydir/copydir.plugin.zsh, oh-my-zsh/plugins/copyfile/README.md, oh-my-zsh/plugins/copyfile/copyfile.plugin.zsh, oh-my-zsh/plugins/copypath/README.md, oh-my-zsh/plugins/copypath/copypath.plugin.zsh, oh-my-zsh/plugins/cp/README.md, oh-my-zsh/plugins/cp/cp.plugin.zsh, oh-my-zsh/plugins/cpanm/README.md, oh-my-zsh/plugins/cpanm/_cpanm, oh-my-zsh/plugins/dash/README.md, oh-my-zsh/plugins/dash/dash.plugin.zsh, oh-my-zsh/plugins/debian/README.md, oh-my-zsh/plugins/debian/debian.plugin.zsh, oh-my-zsh/plugins/deno/README.md, oh-my-zsh/plugins/deno/deno.plugin.zsh, oh-my-zsh/plugins/dircycle/README.md, oh-my-zsh/plugins/dircycle/dircycle.plugin.zsh, oh-my-zsh/plugins/direnv/README.md, oh-my-zsh/plugins/direnv/direnv.plugin.zsh, oh-my-zsh/plugins/dirhistory/README.md, oh-my-zsh/plugins/dirhistory/dirhistory.plugin.zsh, oh-my-zsh/plugins/dirpersist/README.md, oh-my-zsh/plugins/dirpersist/dirpersist.plugin.zsh, oh-my-zsh/plugins/dnf/README.md, oh-my-zsh/plugins/dnf/dnf.plugin.zsh, oh-my-zsh/plugins/dnote/README.md, oh-my-zsh/plugins/dnote/_dnote, oh-my-zsh/plugins/docker-compose/README.md, oh-my-zsh/plugins/docker-compose/_docker-compose, oh-my-zsh/plugins/docker-compose/docker-compose.plugin.zsh, oh-my-zsh/plugins/docker-machine/README.md, oh-my-zsh/plugins/docker-machine/_docker-machine, oh-my-zsh/plugins/docker-machine/docker-machine.plugin.zsh, oh-my-zsh/plugins/docker/README.md, oh-my-zsh/plugins/docker/_docker, oh-my-zsh/plugins/docker/docker.plugin.zsh, oh-my-zsh/plugins/doctl/README.md, oh-my-zsh/plugins/doctl/doctl.plugin.zsh, oh-my-zsh/plugins/dotenv/README.md, oh-my-zsh/plugins/dotenv/dotenv.plugin.zsh, oh-my-zsh/plugins/dotnet/README.md, oh-my-zsh/plugins/dotnet/dotnet.plugin.zsh, oh-my-zsh/plugins/droplr/README.md, oh-my-zsh/plugins/droplr/droplr.plugin.zsh, oh-my-zsh/plugins/drush/README.md, oh-my-zsh/plugins/drush/drush.complete.sh, oh-my-zsh/plugins/drush/drush.plugin.zsh, oh-my-zsh/plugins/eecms/README.md, oh-my-zsh/plugins/eecms/eecms.plugin.zsh, oh-my-zsh/plugins/emacs/README.md, oh-my-zsh/plugins/emacs/emacs.plugin.zsh, oh-my-zsh/plugins/emacs/emacsclient.sh, oh-my-zsh/plugins/ember-cli/README.md, oh-my-zsh/plugins/ember-cli/_ember-cli, oh-my-zsh/plugins/ember-cli/ember-cli.plugin.zsh, oh-my-zsh/plugins/emoji-clock/README.md, oh-my-zsh/plugins/emoji-clock/emoji-clock.plugin.zsh, oh-my-zsh/plugins/emoji/README.md, oh-my-zsh/plugins/emoji/emoji-char-definitions.zsh, oh-my-zsh/plugins/emoji/emoji-data.txt, oh-my-zsh/plugins/emoji/emoji.plugin.zsh, oh-my-zsh/plugins/emoji/gemoji_db.json, oh-my-zsh/plugins/emoji/update_emoji.py, oh-my-zsh/plugins/emotty/README.md, oh-my-zsh/plugins/emotty/emotty.plugin.zsh, oh-my-zsh/plugins/emotty/emotty_emoji_set.zsh, oh-my-zsh/plugins/emotty/emotty_floral_set.zsh, oh-my-zsh/plugins/emotty/emotty_love_set.zsh, oh-my-zsh/plugins/emotty/emotty_nature_set.zsh, oh-my-zsh/plugins/emotty/emotty_stellar_set.zsh, oh-my-zsh/plugins/emotty/emotty_zodiac_set.zsh, oh-my-zsh/plugins/encode64/README.md, oh-my-zsh/plugins/encode64/encode64.plugin.zsh, oh-my-zsh/plugins/extract/README.md, oh-my-zsh/plugins/extract/_extract, oh-my-zsh/plugins/extract/extract.plugin.zsh, oh-my-zsh/plugins/fabric/README.md, oh-my-zsh/plugins/fabric/_fab, oh-my-zsh/plugins/fabric/fabric.plugin.zsh, oh-my-zsh/plugins/fancy-ctrl-z/README.md, oh-my-zsh/plugins/fancy-ctrl-z/fancy-ctrl-z.plugin.zsh, oh-my-zsh/plugins/fasd/README.md, oh-my-zsh/plugins/fasd/fasd.plugin.zsh, oh-my-zsh/plugins/fastfile/README.md, oh-my-zsh/plugins/fastfile/fastfile.plugin.zsh, oh-my-zsh/plugins/fbterm/README.md, oh-my-zsh/plugins/fbterm/fbterm.plugin.zsh, oh-my-zsh/plugins/fd/README.md, oh-my-zsh/plugins/fd/_fd, oh-my-zsh/plugins/fig/README.md, oh-my-zsh/plugins/fig/fig.plugin.zsh, oh-my-zsh/plugins/firewalld/README.md, oh-my-zsh/plugins/firewalld/firewalld.plugin.zsh, oh-my-zsh/plugins/flutter/README.md, oh-my-zsh/plugins/flutter/_flutter, oh-my-zsh/plugins/flutter/flutter.plugin.zsh, oh-my-zsh/plugins/fnm/README.md, oh-my-zsh/plugins/fnm/fnm.plugin.zsh, oh-my-zsh/plugins/forklift/README.md, oh-my-zsh/plugins/forklift/forklift.plugin.zsh, oh-my-zsh/plugins/fossil/README.md, oh-my-zsh/plugins/fossil/_fossil, oh-my-zsh/plugins/fossil/fossil.plugin.zsh, oh-my-zsh/plugins/frontend-search/README.md, oh-my-zsh/plugins/frontend-search/_frontend, oh-my-zsh/plugins/frontend-search/frontend-search.plugin.zsh, oh-my-zsh/plugins/fzf/README.md, oh-my-zsh/plugins/fzf/fzf.plugin.zsh, oh-my-zsh/plugins/gas/README.md, oh-my-zsh/plugins/gas/_gas, oh-my-zsh/plugins/gatsby/README.md, oh-my-zsh/plugins/gatsby/_gatsby, oh-my-zsh/plugins/gb/README.md, oh-my-zsh/plugins/gb/_gb, oh-my-zsh/plugins/gcloud/README.md, oh-my-zsh/plugins/gcloud/gcloud.plugin.zsh, oh-my-zsh/plugins/geeknote/README.md, oh-my-zsh/plugins/geeknote/_geeknote, oh-my-zsh/plugins/geeknote/geeknote.plugin.zsh, oh-my-zsh/plugins/gem/README.md, oh-my-zsh/plugins/gem/_gem, oh-my-zsh/plugins/gem/gem.plugin.zsh, oh-my-zsh/plugins/genpass/README.md, oh-my-zsh/plugins/genpass/genpass-apple, oh-my-zsh/plugins/genpass/genpass-monkey, oh-my-zsh/plugins/genpass/genpass-xkcd, oh-my-zsh/plugins/genpass/genpass.plugin.zsh, oh-my-zsh/plugins/gh/README.md, oh-my-zsh/plugins/gh/gh.plugin.zsh, oh-my-zsh/plugins/git-auto-fetch/README.md, oh-my-zsh/plugins/git-auto-fetch/git-auto-fetch.plugin.zsh, oh-my-zsh/plugins/git-escape-magic/README.md, oh-my-zsh/plugins/git-escape-magic/git-escape-magic, oh-my-zsh/plugins/git-escape-magic/git-escape-magic.plugin.zsh, oh-my-zsh/plugins/git-extras/README.md, oh-my-zsh/plugins/git-extras/git-extras.plugin.zsh, oh-my-zsh/plugins/git-flow-avh/README.md, oh-my-zsh/plugins/git-flow-avh/git-flow-avh.plugin.zsh, oh-my-zsh/plugins/git-flow/README.md, oh-my-zsh/plugins/git-flow/_git-flow, oh-my-zsh/plugins/git-flow/git-flow.plugin.zsh, oh-my-zsh/plugins/git-hubflow/README.md, oh-my-zsh/plugins/git-hubflow/git-hubflow.plugin.zsh, oh-my-zsh/plugins/git-lfs/README.md, oh-my-zsh/plugins/git-lfs/git-lfs.plugin.zsh, oh-my-zsh/plugins/git-prompt/README.md, oh-my-zsh/plugins/git-prompt/git-prompt.plugin.zsh, oh-my-zsh/plugins/git-prompt/gitstatus.py, oh-my-zsh/plugins/git/README.md, oh-my-zsh/plugins/git/git.plugin.zsh, oh-my-zsh/plugins/gitfast/README.md, oh-my-zsh/plugins/gitfast/_git, oh-my-zsh/plugins/gitfast/git-completion.bash, oh-my-zsh/plugins/gitfast/git-prompt.sh, oh-my-zsh/plugins/gitfast/gitfast.plugin.zsh, oh-my-zsh/plugins/gitfast/update, oh-my-zsh/plugins/github/README.md, oh-my-zsh/plugins/github/_hub, oh-my-zsh/plugins/github/github.plugin.zsh, oh-my-zsh/plugins/gitignore/README.md, oh-my-zsh/plugins/gitignore/gitignore.plugin.zsh, oh-my-zsh/plugins/glassfish/README.md, oh-my-zsh/plugins/glassfish/_asadmin, oh-my-zsh/plugins/glassfish/glassfish.plugin.zsh, oh-my-zsh/plugins/globalias/README.md, oh-my-zsh/plugins/globalias/globalias.plugin.zsh, oh-my-zsh/plugins/gnu-utils/README.md, oh-my-zsh/plugins/gnu-utils/gnu-utils.plugin.zsh, oh-my-zsh/plugins/golang/README.md, oh-my-zsh/plugins/golang/_golang, oh-my-zsh/plugins/golang/golang.plugin.zsh, oh-my-zsh/plugins/golang/templates/package.txt, oh-my-zsh/plugins/golang/templates/search.txt, oh-my-zsh/plugins/gpg-agent/README.md, oh-my-zsh/plugins/gpg-agent/gpg-agent.plugin.zsh, oh-my-zsh/plugins/gradle/README.md, oh-my-zsh/plugins/gradle/_gradle, oh-my-zsh/plugins/gradle/gradle.plugin.zsh, oh-my-zsh/plugins/grails/README.md, oh-my-zsh/plugins/grails/grails.plugin.zsh, oh-my-zsh/plugins/grc/README.md, oh-my-zsh/plugins/grc/grc.plugin.zsh, oh-my-zsh/plugins/grunt/README.md, oh-my-zsh/plugins/grunt/grunt.plugin.zsh, oh-my-zsh/plugins/gulp/README.md, oh-my-zsh/plugins/gulp/gulp.plugin.zsh, oh-my-zsh/plugins/hanami/README.md, oh-my-zsh/plugins/hanami/hanami.plugin.zsh, oh-my-zsh/plugins/helm/README.md, oh-my-zsh/plugins/helm/helm.plugin.zsh, oh-my-zsh/plugins/heroku/README.md, oh-my-zsh/plugins/heroku/heroku.plugin.zsh, oh-my-zsh/plugins/history-substring-search/README.md, oh-my-zsh/plugins/history-substring-search/history-substring-search.plugin.zsh, oh-my-zsh/plugins/history-substring-search/history-substring-search.zsh, oh-my-zsh/plugins/history-substring-search/update-from-upstream.zsh, oh-my-zsh/plugins/history/README.md, oh-my-zsh/plugins/history/history.plugin.zsh, oh-my-zsh/plugins/hitchhiker/.gitignore, oh-my-zsh/plugins/hitchhiker/README.md, oh-my-zsh/plugins/hitchhiker/fortunes/hitchhiker, oh-my-zsh/plugins/hitchhiker/hitchhiker.plugin.zsh, oh-my-zsh/plugins/hitokoto/README.md, oh-my-zsh/plugins/hitokoto/hitokoto.plugin.zsh, oh-my-zsh/plugins/homestead/README.md, oh-my-zsh/plugins/homestead/homestead.plugin.zsh, oh-my-zsh/plugins/httpie/README.md, oh-my-zsh/plugins/httpie/_httpie, oh-my-zsh/plugins/invoke/README.md, oh-my-zsh/plugins/invoke/invoke.plugin.zsh, oh-my-zsh/plugins/ionic/README.md, oh-my-zsh/plugins/ionic/ionic.plugin.zsh, oh-my-zsh/plugins/ipfs/LICENSE, oh-my-zsh/plugins/ipfs/README.md, oh-my-zsh/plugins/ipfs/_ipfs, oh-my-zsh/plugins/isodate/README.md, oh-my-zsh/plugins/isodate/isodate.plugin.zsh, oh-my-zsh/plugins/istioctl/README.md, oh-my-zsh/plugins/istioctl/istioctl.plugin.zsh, oh-my-zsh/plugins/iterm2/README.md, oh-my-zsh/plugins/iterm2/iterm2.plugin.zsh, oh-my-zsh/plugins/jake-node/README.md, oh-my-zsh/plugins/jake-node/jake-node.plugin.zsh, oh-my-zsh/plugins/jenv/README.md, oh-my-zsh/plugins/jenv/jenv.plugin.zsh, oh-my-zsh/plugins/jfrog/README.md, oh-my-zsh/plugins/jfrog/jfrog.plugin.zsh, oh-my-zsh/plugins/jhbuild/README.md, oh-my-zsh/plugins/jhbuild/jhbuild.plugin.zsh, oh-my-zsh/plugins/jira/README.md, oh-my-zsh/plugins/jira/_jira, oh-my-zsh/plugins/jira/jira.plugin.zsh, oh-my-zsh/plugins/jruby/README.md, oh-my-zsh/plugins/jruby/jruby.plugin.zsh, oh-my-zsh/plugins/jsontools/README.md, oh-my-zsh/plugins/jsontools/jsontools.plugin.zsh, oh-my-zsh/plugins/juju/README.md, oh-my-zsh/plugins/juju/juju.plugin.zsh, oh-my-zsh/plugins/jump/README.md, oh-my-zsh/plugins/jump/jump.plugin.zsh, oh-my-zsh/plugins/kate/README.md, oh-my-zsh/plugins/kate/kate.plugin.zsh, oh-my-zsh/plugins/keychain/README.md, oh-my-zsh/plugins/keychain/keychain.plugin.zsh, oh-my-zsh/plugins/kitchen/README.md, oh-my-zsh/plugins/kitchen/_kitchen, oh-my-zsh/plugins/kn/README.md, oh-my-zsh/plugins/kn/kn.plugin.zsh, oh-my-zsh/plugins/knife/README.md, oh-my-zsh/plugins/knife/_knife, oh-my-zsh/plugins/knife_ssh/README.md, oh-my-zsh/plugins/knife_ssh/knife_ssh.plugin.zsh, oh-my-zsh/plugins/kops/README.md, oh-my-zsh/plugins/kops/kops.plugin.zsh, oh-my-zsh/plugins/kube-ps1/README.md, oh-my-zsh/plugins/kube-ps1/kube-ps1.plugin.zsh, oh-my-zsh/plugins/kubectl/README.md, oh-my-zsh/plugins/kubectl/kubectl.plugin.zsh, oh-my-zsh/plugins/kubectx/README.md, oh-my-zsh/plugins/kubectx/kubectx.plugin.zsh, oh-my-zsh/plugins/kubectx/prod.png, oh-my-zsh/plugins/kubectx/stage.png, oh-my-zsh/plugins/lando/LICENSE, oh-my-zsh/plugins/lando/README.md, oh-my-zsh/plugins/lando/lando.plugin.zsh, oh-my-zsh/plugins/laravel/README.md, oh-my-zsh/plugins/laravel/_artisan, oh-my-zsh/plugins/laravel/laravel.plugin.zsh, oh-my-zsh/plugins/laravel4/README.md, oh-my-zsh/plugins/laravel4/laravel4.plugin.zsh, oh-my-zsh/plugins/laravel5/README.md, oh-my-zsh/plugins/laravel5/laravel5.plugin.zsh, oh-my-zsh/plugins/last-working-dir/README.md, oh-my-zsh/plugins/last-working-dir/last-working-dir.plugin.zsh, oh-my-zsh/plugins/lein/README.md, oh-my-zsh/plugins/lein/_lein, oh-my-zsh/plugins/lighthouse/README.md, oh-my-zsh/plugins/lighthouse/lighthouse.plugin.zsh, oh-my-zsh/plugins/lol/README.md, oh-my-zsh/plugins/lol/lol.plugin.zsh, oh-my-zsh/plugins/lpass/README.md, oh-my-zsh/plugins/lpass/_lpass, oh-my-zsh/plugins/lxd/README.md, oh-my-zsh/plugins/lxd/lxd.plugin.zsh, oh-my-zsh/plugins/macos/README.md, oh-my-zsh/plugins/macos/_security, oh-my-zsh/plugins/macos/macos.plugin.zsh, oh-my-zsh/plugins/macos/music, oh-my-zsh/plugins/macos/spotify, oh-my-zsh/plugins/macports/README.md, oh-my-zsh/plugins/macports/_port, oh-my-zsh/plugins/macports/macports.plugin.zsh, oh-my-zsh/plugins/magic-enter/README.md, oh-my-zsh/plugins/magic-enter/magic-enter.plugin.zsh, oh-my-zsh/plugins/man/README.md, oh-my-zsh/plugins/man/man.plugin.zsh, oh-my-zsh/plugins/marked2/README.md, oh-my-zsh/plugins/marked2/marked2.plugin.zsh, oh-my-zsh/plugins/mercurial/README.md, oh-my-zsh/plugins/mercurial/mercurial.plugin.zsh, oh-my-zsh/plugins/meteor/README.md, oh-my-zsh/plugins/meteor/_meteor, oh-my-zsh/plugins/meteor/meteor.plugin.zsh, oh-my-zsh/plugins/microk8s/README.md, oh-my-zsh/plugins/microk8s/microk8s.plugin.zsh, oh-my-zsh/plugins/minikube/README.md, oh-my-zsh/plugins/minikube/minikube.plugin.zsh, oh-my-zsh/plugins/mix-fast/README.md, oh-my-zsh/plugins/mix-fast/mix-fast.plugin.zsh, oh-my-zsh/plugins/mix/README.md, oh-my-zsh/plugins/mix/_mix, oh-my-zsh/plugins/mongocli/README.md, oh-my-zsh/plugins/mongocli/mongocli.plugin.zsh, oh-my-zsh/plugins/mosh/README.md, oh-my-zsh/plugins/mosh/mosh.plugin.zsh, oh-my-zsh/plugins/multipass/README.md, oh-my-zsh/plugins/multipass/_multipass, oh-my-zsh/plugins/multipass/multipass.plugin.zsh, oh-my-zsh/plugins/mvn/README.md, oh-my-zsh/plugins/mvn/mvn.plugin.zsh, oh-my-zsh/plugins/mysql-macports/README.md, oh-my-zsh/plugins/mysql-macports/mysql-macports.plugin.zsh, oh-my-zsh/plugins/n98-magerun/README.md, oh-my-zsh/plugins/n98-magerun/n98-magerun.plugin.zsh, oh-my-zsh/plugins/nanoc/README.md, oh-my-zsh/plugins/nanoc/_nanoc, oh-my-zsh/plugins/nanoc/nanoc.plugin.zsh, oh-my-zsh/plugins/ng/README.md, oh-my-zsh/plugins/ng/_ng, oh-my-zsh/plugins/nmap/README.md, oh-my-zsh/plugins/nmap/nmap.plugin.zsh, oh-my-zsh/plugins/node/README.md, oh-my-zsh/plugins/node/node.plugin.zsh, oh-my-zsh/plugins/nomad/README.md, oh-my-zsh/plugins/nomad/_nomad, oh-my-zsh/plugins/npm/README.md, oh-my-zsh/plugins/npm/npm.plugin.zsh, oh-my-zsh/plugins/npx/README.md, oh-my-zsh/plugins/npx/npx.plugin.zsh, oh-my-zsh/plugins/nvm/README.md, oh-my-zsh/plugins/nvm/_nvm, oh-my-zsh/plugins/nvm/nvm.plugin.zsh, oh-my-zsh/plugins/oc/README.md, oh-my-zsh/plugins/oc/oc.plugin.zsh, oh-my-zsh/plugins/octozen/README.md, oh-my-zsh/plugins/octozen/octozen.plugin.zsh, oh-my-zsh/plugins/operator-sdk/README.md, oh-my-zsh/plugins/operator-sdk/operator-sdk.plugin.zsh, oh-my-zsh/plugins/osx/README.md, oh-my-zsh/plugins/osx/osx.plugin.zsh, oh-my-zsh/plugins/otp/README.md, oh-my-zsh/plugins/otp/otp.plugin.zsh, oh-my-zsh/plugins/pass/README.md, oh-my-zsh/plugins/pass/_pass, oh-my-zsh/plugins/paver/README.md, oh-my-zsh/plugins/paver/paver.plugin.zsh, oh-my-zsh/plugins/pep8/README.md, oh-my-zsh/plugins/pep8/_pep8, oh-my-zsh/plugins/per-directory-history/README.md, oh-my-zsh/plugins/per-directory-history/per-directory-history.plugin.zsh, oh-my-zsh/plugins/per-directory-history/per-directory-history.zsh, oh-my-zsh/plugins/percol/README.md, oh-my-zsh/plugins/percol/percol.plugin.zsh, oh-my-zsh/plugins/perl/README.md, oh-my-zsh/plugins/perl/perl.plugin.zsh, oh-my-zsh/plugins/perms/README.md, oh-my-zsh/plugins/perms/perms.plugin.zsh, oh-my-zsh/plugins/phing/README.md, oh-my-zsh/plugins/phing/phing.plugin.zsh, oh-my-zsh/plugins/pip/README.md, oh-my-zsh/plugins/pip/_pip, oh-my-zsh/plugins/pip/pip.plugin.zsh, oh-my-zsh/plugins/pipenv/README.md, oh-my-zsh/plugins/pipenv/pipenv.plugin.zsh, oh-my-zsh/plugins/pj/README.md, oh-my-zsh/plugins/pj/pj.plugin.zsh, oh-my-zsh/plugins/please/README.md, oh-my-zsh/plugins/please/please.plugin.zsh, oh-my-zsh/plugins/pm2/README.md, oh-my-zsh/plugins/pm2/_pm2, oh-my-zsh/plugins/pm2/pm2.plugin.zsh, oh-my-zsh/plugins/pod/README.md, oh-my-zsh/plugins/pod/_pod, oh-my-zsh/plugins/poetry/README.md, oh-my-zsh/plugins/poetry/poetry.plugin.zsh, oh-my-zsh/plugins/postgres/README.md, oh-my-zsh/plugins/postgres/postgres.plugin.zsh, oh-my-zsh/plugins/pow/README.md, oh-my-zsh/plugins/pow/pow.plugin.zsh, oh-my-zsh/plugins/powder/README.md, oh-my-zsh/plugins/powder/_powder, oh-my-zsh/plugins/powify/README.md, oh-my-zsh/plugins/powify/_powify, oh-my-zsh/plugins/profiles/README.md, oh-my-zsh/plugins/profiles/profiles.plugin.zsh, oh-my-zsh/plugins/pyenv/README.md, oh-my-zsh/plugins/pyenv/pyenv.plugin.zsh, oh-my-zsh/plugins/pylint/README.md, oh-my-zsh/plugins/pylint/_pylint, oh-my-zsh/plugins/pylint/pylint.plugin.zsh, oh-my-zsh/plugins/python/README.md, oh-my-zsh/plugins/python/python.plugin.zsh, oh-my-zsh/plugins/rails/README.md, oh-my-zsh/plugins/rails/_rails, oh-my-zsh/plugins/rails/rails.plugin.zsh, oh-my-zsh/plugins/rake-fast/README.md, oh-my-zsh/plugins/rake-fast/rake-fast.plugin.zsh, oh-my-zsh/plugins/rake/README.md, oh-my-zsh/plugins/rake/rake.plugin.zsh, oh-my-zsh/plugins/rand-quote/README.md, oh-my-zsh/plugins/rand-quote/rand-quote.plugin.zsh, oh-my-zsh/plugins/rbenv/README.md, oh-my-zsh/plugins/rbenv/rbenv.plugin.zsh, oh-my-zsh/plugins/rbfu/README.md, oh-my-zsh/plugins/rbfu/rbfu.plugin.zsh, oh-my-zsh/plugins/rbw/README.md, oh-my-zsh/plugins/rbw/rbw.plugin.zsh, oh-my-zsh/plugins/react-native/README.md, oh-my-zsh/plugins/react-native/_react-native, oh-my-zsh/plugins/react-native/react-native.plugin.zsh, oh-my-zsh/plugins/rebar/README.md, oh-my-zsh/plugins/rebar/_rebar, oh-my-zsh/plugins/redis-cli/README.md, oh-my-zsh/plugins/redis-cli/_redis-cli, oh-my-zsh/plugins/repo/README.md, oh-my-zsh/plugins/repo/_repo, oh-my-zsh/plugins/repo/repo.plugin.zsh, oh-my-zsh/plugins/ripgrep/README.md, oh-my-zsh/plugins/ripgrep/_ripgrep, oh-my-zsh/plugins/ros/README.md, oh-my-zsh/plugins/ros/_ros, oh-my-zsh/plugins/rsync/README.md, oh-my-zsh/plugins/rsync/rsync.plugin.zsh, oh-my-zsh/plugins/ruby/README.md, oh-my-zsh/plugins/ruby/ruby.plugin.zsh, oh-my-zsh/plugins/rust/README.md, oh-my-zsh/plugins/rust/_rustc, oh-my-zsh/plugins/rust/rust.plugin.zsh, oh-my-zsh/plugins/rustup/README.md, oh-my-zsh/plugins/rustup/rustup.plugin.zsh, oh-my-zsh/plugins/rvm/README.md, oh-my-zsh/plugins/rvm/rvm.plugin.zsh, oh-my-zsh/plugins/safe-paste/README.md, oh-my-zsh/plugins/safe-paste/safe-paste.plugin.zsh, oh-my-zsh/plugins/salt/README.md, oh-my-zsh/plugins/salt/_salt, oh-my-zsh/plugins/samtools/README.md, oh-my-zsh/plugins/samtools/_samtools, oh-my-zsh/plugins/sbt/README.md, oh-my-zsh/plugins/sbt/_sbt, oh-my-zsh/plugins/sbt/sbt.plugin.zsh, oh-my-zsh/plugins/scala/README.md, oh-my-zsh/plugins/scala/_scala, oh-my-zsh/plugins/scd/README.md, oh-my-zsh/plugins/scd/_scd, oh-my-zsh/plugins/scd/scd, oh-my-zsh/plugins/scd/scd.plugin.zsh, oh-my-zsh/plugins/screen/README.md, oh-my-zsh/plugins/screen/screen.plugin.zsh, oh-my-zsh/plugins/scw/README.md, oh-my-zsh/plugins/scw/_scw, oh-my-zsh/plugins/sdk/README.md, oh-my-zsh/plugins/sdk/sdk.plugin.zsh, oh-my-zsh/plugins/sfdx/README.md, oh-my-zsh/plugins/sfdx/_sfdx, oh-my-zsh/plugins/sfffe/README.md, oh-my-zsh/plugins/sfffe/sfffe.plugin.zsh, oh-my-zsh/plugins/shell-proxy/.editorconfig, oh-my-zsh/plugins/shell-proxy/README.md, oh-my-zsh/plugins/shell-proxy/proxy.py, oh-my-zsh/plugins/shell-proxy/shell-proxy.plugin.zsh, oh-my-zsh/plugins/shell-proxy/ssh-agent.py, oh-my-zsh/plugins/shell-proxy/ssh-proxy.py, oh-my-zsh/plugins/shrink-path/README.md, oh-my-zsh/plugins/shrink-path/shrink-path.plugin.zsh, oh-my-zsh/plugins/singlechar/README.md, oh-my-zsh/plugins/singlechar/singlechar.plugin.zsh, oh-my-zsh/plugins/spring/README.md, oh-my-zsh/plugins/spring/_spring, oh-my-zsh/plugins/sprunge/README.md, oh-my-zsh/plugins/sprunge/sprunge.plugin.zsh, oh-my-zsh/plugins/ssh-agent/README.md, oh-my-zsh/plugins/ssh-agent/ssh-agent.plugin.zsh, oh-my-zsh/plugins/stack/README.md, oh-my-zsh/plugins/stack/stack.plugin.zsh, oh-my-zsh/plugins/sublime-merge/README.md, oh-my-zsh/plugins/sublime-merge/sublime-merge.plugin.zsh, oh-my-zsh/plugins/sublime/README.md, oh-my-zsh/plugins/sublime/sublime.plugin.zsh, oh-my-zsh/plugins/sudo/README.md, oh-my-zsh/plugins/sudo/sudo.plugin.zsh, oh-my-zsh/plugins/supervisor/README.md, oh-my-zsh/plugins/supervisor/_supervisorctl, oh-my-zsh/plugins/supervisor/_supervisord, oh-my-zsh/plugins/supervisor/supervisor.plugin.zsh, oh-my-zsh/plugins/suse/README.md, oh-my-zsh/plugins/suse/suse.plugin.zsh, oh-my-zsh/plugins/svcat/README.md, oh-my-zsh/plugins/svcat/svcat.plugin.zsh, oh-my-zsh/plugins/svn-fast-info/README.md, oh-my-zsh/plugins/svn-fast-info/svn-fast-info.plugin.zsh, oh-my-zsh/plugins/svn/README.md, oh-my-zsh/plugins/svn/svn.plugin.zsh, oh-my-zsh/plugins/swiftpm/README.md, oh-my-zsh/plugins/swiftpm/_swift, oh-my-zsh/plugins/swiftpm/swiftpm.plugin.zsh, oh-my-zsh/plugins/symfony/README.md, oh-my-zsh/plugins/symfony/symfony.plugin.zsh, oh-my-zsh/plugins/symfony2/README.md, oh-my-zsh/plugins/symfony2/symfony2.plugin.zsh, oh-my-zsh/plugins/systemadmin/README.md, oh-my-zsh/plugins/systemadmin/systemadmin.plugin.zsh, oh-my-zsh/plugins/systemd/README.md, oh-my-zsh/plugins/systemd/systemd.plugin.zsh, oh-my-zsh/plugins/taskwarrior/README.md, oh-my-zsh/plugins/taskwarrior/_task, oh-my-zsh/plugins/taskwarrior/taskwarrior.plugin.zsh, oh-my-zsh/plugins/term_tab/README, oh-my-zsh/plugins/term_tab/term_tab.plugin.zsh, oh-my-zsh/plugins/terminitor/README.md, oh-my-zsh/plugins/terminitor/_terminitor, oh-my-zsh/plugins/terraform/README.md, oh-my-zsh/plugins/terraform/_terraform, oh-my-zsh/plugins/terraform/terraform.plugin.zsh, oh-my-zsh/plugins/textastic/README.md, oh-my-zsh/plugins/textastic/textastic.plugin.zsh, oh-my-zsh/plugins/textmate/README.md, oh-my-zsh/plugins/textmate/textmate.plugin.zsh, oh-my-zsh/plugins/thefuck/README.md, oh-my-zsh/plugins/thefuck/thefuck.plugin.zsh, oh-my-zsh/plugins/themes/README.md, oh-my-zsh/plugins/themes/themes.plugin.zsh, oh-my-zsh/plugins/thor/README.md, oh-my-zsh/plugins/thor/_thor, oh-my-zsh/plugins/tig/README.md, oh-my-zsh/plugins/tig/tig.plugin.zsh, oh-my-zsh/plugins/timer/README.md, oh-my-zsh/plugins/timer/timer.plugin.zsh, oh-my-zsh/plugins/tmux-cssh/README.md, oh-my-zsh/plugins/tmux-cssh/_tmux-cssh, oh-my-zsh/plugins/tmux/README.md, oh-my-zsh/plugins/tmux/tmux.extra.conf, oh-my-zsh/plugins/tmux/tmux.only.conf, oh-my-zsh/plugins/tmux/tmux.plugin.zsh, oh-my-zsh/plugins/tmuxinator/README.md, oh-my-zsh/plugins/tmuxinator/_tmuxinator, oh-my-zsh/plugins/tmuxinator/tmuxinator.plugin.zsh, oh-my-zsh/plugins/toolbox/README.md, oh-my-zsh/plugins/toolbox/kubectx.plugin.zsh, oh-my-zsh/plugins/torrent/README.md, oh-my-zsh/plugins/torrent/torrent.plugin.zsh, oh-my-zsh/plugins/transfer/README.md, oh-my-zsh/plugins/transfer/transfer.plugin.zsh, oh-my-zsh/plugins/tugboat/README.md, oh-my-zsh/plugins/tugboat/_tugboat, oh-my-zsh/plugins/ubuntu/README.md, oh-my-zsh/plugins/ubuntu/ubuntu.plugin.zsh, oh-my-zsh/plugins/ufw/README.md, oh-my-zsh/plugins/ufw/_ufw, oh-my-zsh/plugins/universalarchive/README.md, oh-my-zsh/plugins/universalarchive/_universalarchive, oh-my-zsh/plugins/universalarchive/universalarchive.plugin.zsh, oh-my-zsh/plugins/urltools/README.md, oh-my-zsh/plugins/urltools/urltools.plugin.zsh, oh-my-zsh/plugins/vagrant-prompt/README.md, oh-my-zsh/plugins/vagrant-prompt/vagrant-prompt.plugin.zsh, oh-my-zsh/plugins/vagrant/README.md, oh-my-zsh/plugins/vagrant/_vagrant, oh-my-zsh/plugins/vagrant/vagrant.plugin.zsh, oh-my-zsh/plugins/vault/README.md, oh-my-zsh/plugins/vault/_vault, oh-my-zsh/plugins/vi-mode/README.md, oh-my-zsh/plugins/vi-mode/vi-mode.plugin.zsh, oh-my-zsh/plugins/vim-interaction/README.md, oh-my-zsh/plugins/vim-interaction/vim-interaction.plugin.zsh, oh-my-zsh/plugins/virtualenv/README.md, oh-my-zsh/plugins/virtualenv/virtualenv.plugin.zsh, oh-my-zsh/plugins/virtualenvwrapper/README.md, oh-my-zsh/plugins/virtualenvwrapper/virtualenvwrapper.plugin.zsh, oh-my-zsh/plugins/volta/README.md, oh-my-zsh/plugins/volta/volta.plugin.zsh, oh-my-zsh/plugins/vscode/README.md, oh-my-zsh/plugins/vscode/vscode.plugin.zsh, oh-my-zsh/plugins/vundle/README.md, oh-my-zsh/plugins/vundle/vundle.plugin.zsh, oh-my-zsh/plugins/wakeonlan/README.md, oh-my-zsh/plugins/wakeonlan/_wake, oh-my-zsh/plugins/wakeonlan/wakeonlan.plugin.zsh, oh-my-zsh/plugins/wd/LICENSE, oh-my-zsh/plugins/wd/README.md, oh-my-zsh/plugins/wd/_wd.sh, oh-my-zsh/plugins/wd/wd.plugin.zsh, oh-my-zsh/plugins/wd/wd.sh, oh-my-zsh/plugins/web-search/README.md, oh-my-zsh/plugins/web-search/web-search.plugin.zsh, oh-my-zsh/plugins/wp-cli/README.md, oh-my-zsh/plugins/wp-cli/wp-cli.plugin.zsh, oh-my-zsh/plugins/xcode/README.md, oh-my-zsh/plugins/xcode/_xcselv, oh-my-zsh/plugins/xcode/xcode.plugin.zsh, oh-my-zsh/plugins/yarn/README.md, oh-my-zsh/plugins/yarn/_yarn, oh-my-zsh/plugins/yarn/yarn.plugin.zsh, oh-my-zsh/plugins/yii/README.md, oh-my-zsh/plugins/yii/yii.plugin.zsh, oh-my-zsh/plugins/yii2/README.md, oh-my-zsh/plugins/yii2/yii2.plugin.zsh, oh-my-zsh/plugins/yum/README.md, oh-my-zsh/plugins/yum/yum.plugin.zsh, oh-my-zsh/plugins/z/Makefile, oh-my-zsh/plugins/z/README, oh-my-zsh/plugins/z/README.md, oh-my-zsh/plugins/z/z.1, oh-my-zsh/plugins/z/z.plugin.zsh, oh-my-zsh/plugins/z/z.sh, oh-my-zsh/plugins/zbell/README.md, oh-my-zsh/plugins/zbell/zbell.plugin.zsh, oh-my-zsh/plugins/zeus/README.md, oh-my-zsh/plugins/zeus/_zeus, oh-my-zsh/plugins/zeus/zeus.plugin.zsh, oh-my-zsh/plugins/zoxide/README.md, oh-my-zsh/plugins/zoxide/zoxide.plugin.zsh, oh-my-zsh/plugins/zsh-interactive-cd/README.md, oh-my-zsh/plugins/zsh-interactive-cd/zsh-interactive-cd.plugin.zsh, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-aliases.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-cd.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-env.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-functions.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-history.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-kill.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-list.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-options.conf, oh-my-zsh/plugins/zsh-navigation-tools/.config/znt/n-panelize.conf, oh-my-zsh/plugins/zsh-navigation-tools/LICENSE, oh-my-zsh/plugins/zsh-navigation-tools/Makefile, oh-my-zsh/plugins/zsh-navigation-tools/NEWS, oh-my-zsh/plugins/zsh-navigation-tools/README.md, oh-my-zsh/plugins/zsh-navigation-tools/_n-kill, oh-my-zsh/plugins/zsh-navigation-tools/doc/generate_single_file, oh-my-zsh/plugins/zsh-navigation-tools/doc/img/n-history2.png, oh-my-zsh/plugins/zsh-navigation-tools/doc/install.sh, oh-my-zsh/plugins/zsh-navigation-tools/doc/n-preview, oh-my-zsh/plugins/zsh-navigation-tools/doc/znt-tmux.zsh, oh-my-zsh/plugins/zsh-navigation-tools/n-aliases, oh-my-zsh/plugins/zsh-navigation-tools/n-cd, oh-my-zsh/plugins/zsh-navigation-tools/n-env, oh-my-zsh/plugins/zsh-navigation-tools/n-functions, oh-my-zsh/plugins/zsh-navigation-tools/n-help, oh-my-zsh/plugins/zsh-navigation-tools/n-history, oh-my-zsh/plugins/zsh-navigation-tools/n-kill, oh-my-zsh/plugins/zsh-navigation-tools/n-list, oh-my-zsh/plugins/zsh-navigation-tools/n-list-draw, oh-my-zsh/plugins/zsh-navigation-tools/n-list-input, oh-my-zsh/plugins/zsh-navigation-tools/n-options, oh-my-zsh/plugins/zsh-navigation-tools/n-panelize, oh-my-zsh/plugins/zsh-navigation-tools/znt-cd-widget, oh-my-zsh/plugins/zsh-navigation-tools/znt-history-widget, oh-my-zsh/plugins/zsh-navigation-tools/znt-kill-widget, oh-my-zsh/plugins/zsh-navigation-tools/znt-usetty-wrapper, oh-my-zsh/plugins/zsh-navigation-tools/zsh-navigation-tools.plugin.zsh, oh-my-zsh/plugins/zsh-syntax-highlighting, oh-my-zsh/templates/zshrc.zsh-template, oh-my-zsh/tools/changelog.sh, oh-my-zsh/tools/check_for_upgrade.sh, oh-my-zsh/tools/install.sh, oh-my-zsh/tools/require_tool.sh, oh-my-zsh/tools/theme_chooser.sh, oh-my-zsh/tools/uninstall.sh, oh-my-zsh/tools/upgrade.sh, setup.sh)

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[bbfce81a35...](https://github.com/sourcegraph/sourcegraph/commit/bbfce81a35562d84386862e854ef6b35b555a92a)
#### Friday 2023-05-12 17:11:53 by Juliana Peña

web/app: remove hover on navbar items to stop focus from being moved (#51739)

The dropdown menu items in the global navbar (Search and, in App,
Feedback) move focus when you hover over them. This is bizarre, ugly,
and most likely a [WCAG
violation](https://www.w3.org/TR/WCAG21/#focus-order). I spent some time
yesterday and the root cause is that the [Reach menu button we use does
not support hover at all](https://github.com/reach/reach-ui/issues/278)
and we're hacking it by [sending a mousedown event when you hover over
the
button](https://sourcegraph.com/github.com/sourcegraph/sourcegraph/-/blob/client/web/src/nav/NavBar/NavDropdown.tsx?L58).

There are two options I can think of to mitigate this bug:
1. Get rid of hover events and only open the dropdowns on click. This is
the easiest option, but obviously removes the ease of accessing the menu
for mouse users.
2. Rewrite the dropdown nav items to use a custom menu instead of Reach.
This is more expensive because we have to reimplement lots of a11y stuff
here, but we can have more fine-grained control of different UI flows
for mouse hover vs mouse click vs keyboard users.

I went with the first option following @almeidapaulooliveira's
[feedback](https://sourcegraph.slack.com/archives/C0HMGV90V/p1683735888755969?thread_ts=1683734992.157499&cid=C0HMGV90V).

The following changes were applied to `NavDropdown`:

- Removed all hover and touch events; now only a click will open the
menu.
- Removed the split button; now clicking anywhere on the button will
always open the menu.
- Made the mobile home item into a "generic" home item and always
visible when present.
- Made the home item optional (since the Feedback menu item in the
desktop app doesn't have a home item/route).
- Added customizable a11y names; in the past, the only dropdown was the
Search one, but in App we now have Feedback; the a11y labels were still
saying "Search" before this change.

Additionally, the following changes were applied for polish:

- The double-focus ring on the back/forward buttons in the Tauri app has
been fixed
- Styling changes made to simplify code

## Test plan

The global navbar has extensive visual and behavior test coverage.

---
## [thanhtunguet/react-native-reanimated](https://github.com/thanhtunguet/react-native-reanimated)@[0e96f1cd6e...](https://github.com/thanhtunguet/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Friday 2023-05-12 17:16:47 by Tomasz Żelawski

Remove plugin dev files from npm package (#4433)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Currently development files from `plugin/` are included in npm package.
This PR removes them from it.

b4:
<img width="253" alt="Screenshot 2023-05-08 at 14 39 29"
src="https://user-images.githubusercontent.com/40713406/236829343-1865480f-99d0-4843-adb2-f658db2acce0.png">
after:
<img width="238" alt="Screenshot 2023-05-08 at 14 39 51"
src="https://user-images.githubusercontent.com/40713406/236829379-7c31b6b4-27e1-493c-8be0-6254edbd0c4c.png">

Since [README is always
included](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#files)
I renamed plugin's dev README and removed `README` from being included
in `package.json`.


## Test plan

I recommend using this powerful oneliner: 
`./createNPMPackage.sh && mkdir tarball-new && mv
react-native-reanimated-3.1.0.tgz tarball-new && tarball-new && tar -xf
react-native-reanimated-3.1.0.tgz && ..`
to see the contents of the new package.

Also run _some_ Example App to see if Reanimated plugin from the tarball
is actually working.

---
_Note_: Testing this PR took me longer than it should.

For some reason with current configuration of Example App and running it
on Android (I didn't check iOS) it's surprisingly difficult to use
reanimated from either tarball or unpacked tarball directory. I had to
make a new app and then include Example's source code there.

While it's not that troublesome I think we should have a more
streamlined approach for using custom reanimated package location for
tests with our Examples.

---------

Co-authored-by: Tomek Zawadzki <tomasz.zawadzki@swmansion.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[edabb9be67...](https://github.com/Paxilmaniac/Skyrat-tg/commit/edabb9be679c65f176532670b339d9adc859e664)
#### Friday 2023-05-12 17:37:20 by SkyratBot

[MIRROR] Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[199aa000d3...](https://github.com/moocowswag/FeatureInflation13/commit/199aa000d3f46ee4386a65079992e4b9d0f2537d)
#### Friday 2023-05-12 17:44:08 by Rhials

Demotes Psyker Pirates to Bounty Hunter Duty (#75031)

This PR demotes the Psyker-gang from a pirate team to a fugitive hunting
team. For more information on Psyker pirates, please refer to #71650.

Stuff this also does in the process:
- Gives fugitive hunters their own subfolder in the fugitives antagonist
folder, moves some of their stuff into hunter-specific files rather than
interlacing it with the rest of the fugitive code.
- Moves the hunter backstories to defines, to make reading things easier
while I made this change.
- Exhaustively moves everything related to psykers from being
pirate-oriented to hunter-oriented (typepaths, locations where stuff is
defined, etc. There should be nothing left behind related to psykers in
anything pirate related). (Tell me if I missed anything somehow).

They still get their ship (they even get their own custom
psyker-friendly prisoner capsule). They still have a bunch of lethally
chambered firearms. They're the same gunrunning nutcases they were
before, just as bounty hunters.

To assist with basic tasks such as "getting to the station" or "figuring
out who the fuck we're supposed to be kidnapping", the psykers have
"acquired" a Seer to assist them. They can _try_ to coordinate the
psykers and lead them through situations where their impairments put
them at too great a disadvantage. If you're one of the psykers, make
sure to keep this guy alive at all costs!

Why are they called Shikaris instead of hunters? Mariam-Webster says
it's a Hindi word for some kind of hunter/tracker, and it sounded like
something a bunch of space-junkies would call themselves because they
think it sounds cool.

They now also come with a slightly different motivation, now that they
can't directly threaten the crew for money. Psyker hunters now arrive
tasked with a dirty kidnapping job, payment rendered in GORE.
## Why It's Good For The Game

Psykers aren't up to the challenge of being pirates. They're bogged down
by a number of fundamental issues that render them unable to do anything
expected of pirates. As it currently stands, they present about as much
threat as you would expect from three blind junkies with guns.

Removing them wholesale would be kind of lame. They can function as a
bunch of chaotic-neutral gun-toting space-maniacs, but for the purposes
of gameplay, keeping them as pirates would be a waste of their talents.

Moving them to a lower-stakes role not only moves them to a niche they
are more capable of filling, but gives players a more lax environment to
get a grip on playing psyker without being overwhelmed.

Giving them a seeing-eye role should bring a more unique dynamic to how
psykers are played (that is, some semblance of organization rather than
blind flailing), and should help get over the mechanical hurdles of
being a psyker until better solutions can be made. It shouldn't be too
big of an impact on balance considering the psyker gang only has three
spawns, while most hunter packs have 4+.

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[1674f25725...](https://github.com/moocowswag/FeatureInflation13/commit/1674f25725c25e15769b031553b42144f526f841)
#### Friday 2023-05-12 17:44:08 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Pyrtle93/frameworks_base-1](https://github.com/Pyrtle93/frameworks_base-1)@[34998c9449...](https://github.com/Pyrtle93/frameworks_base-1/commit/34998c94496c8f0964f64af27c9427a719dab768)
#### Friday 2023-05-12 18:59:13 by Kuba Wojciechowski

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
## [datacommonsorg/website](https://github.com/datacommonsorg/website)@[60d93d54cc...](https://github.com/datacommonsorg/website/commit/60d93d54cc21bc04c0f3e1c3435a76e3e74fe808)
#### Friday 2023-05-12 19:51:54 by Jehangir Amjad

[NL Interface] Embeddings update (#2642)

In this PR, we do the following:

1. Make the build_embeddings_v2.py be the default way to generate
embeddings.
2. Updates the latest embeddings (after running the process in (1)).
3. Due to (1) and (2), increased the number of query -> sentences
matched number (from 20 to 40).
4. Updates the nl server tests (need reviewers to check carefully)
5. Update the integration tests (will need a careful look)
6. Linked is the embeddings index differ script output (using top 3
only):

https://drive.google.com/file/d/1-6A-xXcRYj50poglis_7rc1P3aqxYf3R/view?usp=sharing


Based on (6), most of the changes look Ok. We looked at some individual
cases to figure out if the differences are actually impacting. Only one
case below (in bold) was found to actually be different than what's on
autopush right now.

24: How many male civilians are there in Queens? => this is the same on
autopush and after the changes in this PR (ignoring "Queens" and the
stop words makes the results the same.)

38: What is the median age of American Indian or Alaska Native females
in the United States? => same as above (no impact).

43: age in california => this is different but since we'll soon be
removing some of the age SVs by breakdowns, it should be Ok.

44: agricultural output across california => same as above (no impact
due to place and stop word removal)

63: count of earthquakes per year => same on autopush so no impact. This
is because earthquake events are handled separately.

100: housing price trend comparison across US states => same as above
(no impact) after place and stop word removal.

**101: housing trend comparison across US states** => this is different
(autopush uses housing units but new embeddings lead to number of
households but that seems Ok but arguably autopush is also bad because
it goes to a correlation plot which is not the right thing to do here
anyway)

---
## [lube/evals](https://github.com/lube/evals)@[170dfd886c...](https://github.com/lube/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Friday 2023-05-12 20:02:39 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [GFXTI/ProfessionalGeneration](https://github.com/GFXTI/ProfessionalGeneration)@[c5ae46e25d...](https://github.com/GFXTI/ProfessionalGeneration/commit/c5ae46e25dbd8f1f5b8fddbfc679566eca5b30e0)
#### Friday 2023-05-12 20:39:23 by GFXTI

debugging this gonna be a pain in the ass especially since i dont fuck with OOP most the time

---
## [MI439-CLO/android_frameworks_base](https://github.com/MI439-CLO/android_frameworks_base)@[6e34b27726...](https://github.com/MI439-CLO/android_frameworks_base/commit/6e34b277261352c86603e0db54bd44790d2ffd3f)
#### Friday 2023-05-12 20:47:15 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Jprimero15 <jprimero15@aospa.co>

---
## [FreetoZ/cmss13](https://github.com/FreetoZ/cmss13)@[0c35ec75e7...](https://github.com/FreetoZ/cmss13/commit/0c35ec75e7ff5202767260473e84823085472412)
#### Friday 2023-05-12 21:23:26 by Logan

PFC rack sprite change (#3264)

# About the pull request
This PR changes the PFC rack sprite a tiny bit, by replacing the old PFC
kits, with weapon cases.

Why am I making this PR you might ask? Is it because my sugar induced
OCD made me notice something so small and infinitesimal that the kits in
the vendor are outdated and must be changed at once?

No. It is because these vendors when I see them, completely and utterly
ruin my RP and immersion when I see them, I walk out of the chow hall,
belly full of stale food bars with my RP fulfilled, and then I see them,
those fucking little bursts of color that are the old PFCs kits, they
shouldn't be there, _"they shouldn't even exist"_ I tell myself, but its
too late, by the time I come back to my senses, I've already killed
2/3rds of the RO line in my 3rd Vancleve style M2C rampage, after this
rampage I realized that if I, a near 7 year vet of CM can be so easily
triggered by this, what must the PVTs be feeling when they see those
little bursts of outdated color, do they feel hope when they see them in
the dullness of color that is the vendor, only to have their hope turn
into hopeless despair as they scroll hopelessly through the UI looking
for those kits, and when they can't find they either breakdown complete
on the spot, crying and sobbing in the corner till the SEA finds them,
or they suffer a total mental break, and wander the halls of the Almayer
naked with a M41 in their hand, only to appear at briefing to gun down
the CO.

With this change, we can at last save RP and immersion by removing the
PFC kits sprites with weapon case spites.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Sprite Consistency good, 
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.
Old: https://i.gyazo.com/9f1ec938a1ebf9995f353cede374f7b9.png
New: https://i.gyazo.com/4836db37aaa5b8fc4f8a80c8e6531540.png
</details>


# Changelog
:cl: Tisx


imageadd: Added weapon case sprites to PFC vendors 
imagedel: Removed old PFC kit sprites from PFC vendors 

/:cl:

Co-authored-by: Logan <tisx16@gmail.com>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[8af0048ba4...](https://github.com/Buildstarted/linksfordevs/commit/8af0048ba47730d599c6b607832f3243943f937f)
#### Friday 2023-05-12 22:06:43 by Ben Dornis

Updating: 5/12/2023 9:00:00 PM

 1. Added: Type-safe tensors · sebinsua
    (https://sebinsua.com/type-safe-tensors)
 2. Added: I have a new Junior Developer and it kinda sucks - Michael Salim | Senior Full Stack Freelancer and Startup Founder
    (https://michaelsalim.co.uk/blog/i-have-a-new-junior-developer/)
 3. Added: Being Original
    (https://www.vincentntang.com/being-original/)
 4. Added: The kind of thinking computer science enables
    (https://lambdaland.org/posts/2023-05-11_thinking_cs/)
 5. Added: Infrastructure from mining makes sense for scientific computing
    (https://www.noahlebovic.com/infra-from-mining/)
 6. Added: How to Understand Abstract Art
    (http://andreivajnaii.blogspot.com/2023/05/how-to-understand-abstract-art.html)
 7. Added: A Simple System for Measuring Flaky Tests in a Large CI/CD Pipeline
    (https://davidgomes.com/measuring-flaky-tests-large-ci-cd-pipeline/)
 8. Added: Cloudflare is slow and Cloudflare cant do much about it
    (https://hiranyey.dev/posts/cloudflare/)
 9. Added: Relation between Writing and Thinking
    (https://ccomkhj.github.io/WriteAndThink/)
10. Added: #AudioEye Is Suing Me
    (https://adrianroselli.com/2023/05/audioeye-is-suing-me.html)
11. Added: Learning Homebrew Game Boy Game Development in Assembly
    (https://blakesmith.me/2023/05/11/learning-homebrew-game-boy-game-development-in-assembly.html)
12. Added: Should You Automate Your Online Business? - Sarah M. Chappell
    (https://sarahmchappell.com/should-you-automate-your-online-business/)
13. Added: Experimenting with multi-factor encryption
    (https://notes.volution.ro/v1/2023/05/remarks/e175b2ef/)
14. Added: Longevity Biotech Landscape — Ada Nguyen
    (https://www.adanguyenx.com/longevity)
15. Added: Bing Preview Release Notes: Images in Chat Answers, and More
    (https://blogs.bing.com/search/may_2023/Bing-Preview-Release-Notes-Images-in-Chat-Answers,-Export,-and-More)
16. Added: Learn Contravariant in 5 minutes
    (https://jship.github.io/posts/2023-05-11-learn-contravariant-in-five-minutes/)
17. Added: Metaphor thinking
    (https://douglasorr.github.io/2023-03-deep-metaphors/article.html)
18. Added: Postgresql tricks | Lanre Adelowo
    (https://lanre.wtf/blog/2023/05/11/postgres-tricks)
19. Added: The Dark Side of Passkeys: Critical Notes on FIDO2 Passwordless Authentication
    (https://www.jbspeakr.cc/fido-passkeys/)
20. Added: TIL: A use case for UUIDv5
    (https://www.alexghr.me/blog/til-generating-stable-uuids/)
21. Added: Lessons From Billions of Breached Records • Troy Hunt • GOTO 2022
    (https://youtu.be/VM6Zs_7OKrQ?list=PLEx5khR4g7PIEgcDlsEP5veliuyKgnpbt)

Generation took: 00:06:31.0506170
 Maintenance update - cleaning up homepage and feed

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[36baa9e623...](https://github.com/PlagueVonKarma/kep-hack/commit/36baa9e623f36d5171201a8fb69759d31d71774b)
#### Friday 2023-05-12 23:08:44 by Llinos Evans

Boy/Girl option

This adds the boy/girl selection from later generations, using the pret tutorial and a spriteset from Pokemon Anniversary Red. I made some alterations, namely inserting the option later into the speech to be less clunky, and having the Nidorino become a Nidorina if you pick the feminine option.

I decided to make the third name option Seren, a common Welsh name for girls. It means "star", which is really cute! But...most people will probably say it's a Panel de Pon reference, which is cool too.

---

