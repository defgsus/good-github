## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-10](docs/good-messages/2023/2023-05-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,993,649 were push events containing 3,306,796 commit messages that amount to 256,859,692 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[c2d75696c8...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/c2d75696c8d0012027bf97a15b2c0e332416b497)
#### Wednesday 2023-05-10 00:08:46 by SkyratBot

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
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[525cdefe9a...](https://github.com/chadvandy/nagash/commit/525cdefe9a29cb5db68a2269f13ffbac55e4efa5)
#### Wednesday 2023-05-10 00:34:19 by Scott (JvJ)

Abilities and other fixes

- Removed all instances of Magic Resistance in loc instead of Spell Resistance (hopefully)
- Added Mortarch Items to Customs/Skirmish
- Dagger of Jet, now actually works
- Dagger of Jet, gets a resized passive icon because it's not an active
- Staff of Pain, now uses other_abilities_just_activated_after_wind_up flag instead of other_abilities_none_on_wind_up
- Staff of Pain, gets a new passive icon because it's not an active (there is a passive version of the old icon too if people prefer that one)
- Staff of Pain, duplicated Anc for customs only (was getting overridden in the UI by the addition of the bound Gaze of Nagash"
- Staff of Pain, removed redundant bound spell UI point
- Raise the Dead lore of Undeath passive now uses other_abilities_just_activated_after_wind_up flag instead of other_abilities_none_on_wind_up
- Staff of Pain, Raise the Dead added casting UI point
- Added AR CP to all applicable abilities
- Krell +30 armour to match vanilla
- Luthor -20 armour on foot and +10 on terrorgheist to match vanilla
- Mannfred +10 armour on foot, +20 on barded horse to match vanilla, +30 on Abyssal to match the other two
- Isabella -40 armour on foot, -10 on hellsteed, +10 on warhorse to match vanilla
- Repair Beyond Despair renamed Repair Through Despair
- Repair Through Despair new UI tooltip
- Armour of the Barrow now removes magical attacks
- A fuck tonne of abilities with wrong source type, now corrected
- Malevolent Assault is now correctly an active, 30 second active time, now has 2 uses, recharge context above 50%hp
- Updated How They Play loc, thanks urgat
- Bloated Corpse now has wounds and Noxious Disintegration
- Dire Wolves +4 CB to match vanilla
- Blood Knights now have Hunger to match vanilla
- Black Armour of Nagash, removed cannot move, reduced slow to 50% (20 speed), added damage reflection
- The Great Blade of Death, no longer auto deactivates out of melee, now has intensity 0-60% base and ap weapon damage, increased through casting/melee
- Master Arcane Conduit, reserves per second now 0.1 from 0.6
- Master Arcane Conduit, resized passive icon
- Death Magic Incarnate, now a passive, heal from 0.0110 to 0.0027, still only effects units that are wavering (nagash undead ball, do be a thing now)
- Death Magic Incarnate, resized passive icon
- Staff of Power new UI points
- Crown of Sorcery new ability for Nagash, resets spell cooldown, spellmastery, recharge if above 50% wom, starts off cooldown
- Crown of Sorcery, duplicated Anc for customs only (was getting overridden in the UI by the addition of the bound Gaze of Nagash"
- Chasm of Souls upkeep stacking fixed and reduction reduced
- Chasm of Souls restored battle context
- Tower of Dhar restored battle context
- Mausoleum of the Damned restored battle context

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[c65503c096...](https://github.com/TaleStation/TaleStation/commit/c65503c0969514be2b91c3d1fef5662d08e0e954)
#### Wednesday 2023-05-10 01:35:29 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#5702)

Original PR: https://github.com/tgstation/tgstation/pull/75040
-----
## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[2068ea9ab5...](https://github.com/DATA-xPUNGED/DataStation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Wednesday 2023-05-10 01:36:38 by SyncIt21

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
## [juju/juju](https://github.com/juju/juju)@[7976a61522...](https://github.com/juju/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Wednesday 2023-05-10 01:58:26 by Juju bot

Merge pull request #15492 from barrettj12/openstack-meta

https://github.com/juju/juju/pull/15492

The interactive add-cloud is painful because it will often reject the endpoint URL without giving any reason why. See https://bugs.launchpad.net/juju/+bug/1908630
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119

Enter the API endpoint url for the cloud []: http://172.31.47.119/
Can't validate endpoint: No Openstack server running at http://172.31.47.119/

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity/v3
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity/v3

Enter the API endpoint url for the cloud []: 172.31.47.119/identity
Can't validate endpoint: No Openstack server running at 172.31.47.119/identity

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity
```

In the Openstack provider's `Ping` method, at least pass on the error information to the user, to make it a little less painful.
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request /
caused by: Get "/": unsupported protocol scheme ""

Enter the API endpoint url for the cloud []: http://172.31.47.119
Can't validate endpoint: No Openstack server running at http://172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request http://172.31.47.119/
caused by: Get "http://172.31.47.119/": dial tcp 172.31.47.119:80: connect: no route to host
```

Do the same with the MAAS and LXD providers.

Also, fix a silly check in the LXD provider's `Ping` method that was rejecting perfectly good URLs. We're already using `lxd.EnsureHostPort(endpoint)` to fill in the scheme/port if not provided, but we were checking the returned value equals the input (and returning an unhelpful error if not). Remove this check.

## Checklist

*If an item is not applicable, use `~strikethrough~`.*

- [x] Code style: imports ordered, good names, simple structure, etc
- ~[ ] Comments saying why design decisions were made~
- [x] Go unit tests, with comments saying what you're testing
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

Run `juju add-cloud` interactively, and provide a bogus URL.

---
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[21363d07a5...](https://github.com/YakumoChen/Skyrat-tg/commit/21363d07a5eec9fbce5be2f17cd1693319906d61)
#### Wednesday 2023-05-10 03:23:06 by SkyratBot

[MIRROR] De-holes holy arrows [MDB IGNORE] (#20985)

* De-holes holy arrows (#75184)

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

* De-holes holy arrows

---------

Co-authored-by: Thunder12345 <Thunder12345@users.noreply.github.com>

---
## [seokwave/openbsd](https://github.com/seokwave/openbsd)@[7922d92f72...](https://github.com/seokwave/openbsd/commit/7922d92f725a12fafc8177d16fef629aee4265a6)
#### Wednesday 2023-05-10 04:10:16 by tb

Rename the other_ctx in X509_STORE_CTX into trusted

The other_ctx is a strong contender for the worst name of a struct member
in OpenSSL. It's a void * member whose only purpose ever was to be set to a
STACK_OF(X509) * via X509_STORE_CTX_trusted_stack() (yes, this is obviously
a setter, why do you ask?) and then to be used by the get_issuer() callback
(which of course isn't there to find any old issuer, but only to look for
issuers among the 'trusted' certs).

Anyway, we may want to rename untrusted into intermediates and trusted into
roots later on, but for now let's match the lovely public API. While there
rename get_issuer_sk() into get_trusted_issuer() which is a more accurate
and slightly less silly name.

ok jsing

---
## [emrakyz/voidrice](https://github.com/emrakyz/voidrice)@[f313b6c0f5...](https://github.com/emrakyz/voidrice/commit/f313b6c0f59bc3d157f7cf3d07848b7e1baabdc9)
#### Wednesday 2023-05-10 04:13:37 by Emre AKYÜZ

Fix File Naming Conventions for Unix Environment

Luke mentions about Unix naming conventions on his videos. Here is a script to increase consistency according to Unix conventions for all file names in parallel, very easily and fast in a safe way.

Luke also asks: "What do you think about naming files with underscores instead of dashes?", stating his worry about the usage of underscores seems like a "soydev" thing 😂. I give my opinion below. Actually the justification is objective compared to an opinion.

### What The Script Does

**1.** Check if the item is a directory. If so;

- **a)** Remove non-English characters.
- **b)** Replace spaces, dots, and dashes with underscores.
- **c)** Remove consecutive underscores.
- **d)** Convert the name to lowercase.
- **e)** Remove any other special characters.
- **f)** If the resulting name is empty, set it to "untitled".
- **g)** Every file or directory should start and end with an alphanumeric character.

**2.** If the item is a file, apply the same transformations as for directories, but keep the file extension intact.

**3.** Check if the original name and the new name are different. If so, and if a file or directory with the new name already exists, create a unique name.

- The script can use Dash and parallel processes, ensuring safety and performance with a subshell environment. Therefore it can even rename more than 100.000 files that have extremely weird names in 30 seconds (I have tested bash built-in functions, tr, awk and sed. None of them was faster than sed for this task, awk was very close but still slower).

**Examples of How Every File Should Look:** this_is_an_example_directory_name  **OR**  this_is_an_example_video_file.mp4

### Why "_" is Preferred Instead of a Space or a Dot or a Dash

In Unix environments, it is generally recommended to replace spaces in filenames with underscores (_), rather than dots (.) or dashes (-). This is because underscores are more commonly used and supported by Unix utilities and programming languages.

Dots (.) are typically used as a separator between a file's name and its extension, so using them to replace spaces can lead to confusion and errors. Dashes (-) are sometimes used in place of spaces, but they can be problematic because they are often used as a command-line option delimiter in Unix, which can lead to unexpected behavior.

- **Readability:** Underscores make file and directory names more readable, as they clearly separate words and components in the name, whereas spaces can be easily overlooked, and dots can be mistaken for file extensions.

- **Compatibility:** Some command line tools and scripts may not handle file names with spaces or dots properly without additional configuration or escaping. Underscores, on the other hand, do not require special handling and are generally better supported across various tools and environments.

- **URL encoding:** When sharing file paths in URLs or web applications, spaces and dots may require URL encoding (e.g., replacing spaces with "%20" and dots with "%2E"), which can make the URLs less readable and more cumbersome to work with

### The Reason Behind Using a Subshell Environment

Subshells are used in the script to isolate the execution environment of each parallel process. This isolation ensures that the processes do not interfere with each other, as they have their own separate environments, including local variables and function definitions. This separation is particularly important when running multiple processes in parallel, as it reduces the risk of race conditions and other synchronization issues.

Using subshells in the script also simplifies the process of launching parallel processes. By executing the process_item function within a subshell, the script can easily leverage the -P flag of xargs to specify the maximum number of parallel processes to run. This results in improved performance and efficiency when processing a large number of files and directories.

### The Benefit of Removing Non-English Characters

- **Compatibility:** Non-English characters can cause compatibility issues with some tools, applications, or systems that are not properly configured to handle them. By removing these characters, you reduce the risk of encountering issues related to character encoding and ensure broader compatibility across different environments.

- **Consistency:** Standardizing file and directory names by removing non-English characters can make it easier to organize, search, and manage your files. It helps maintain a consistent naming convention across your file system, which can be beneficial for both human users and automated processes.

- **Accessibility:** Using only English characters in file and directory names can improve accessibility for users who may not be familiar with non-English characters or languages. This can be particularly important in multi-user or multi-language environments where not all users might be comfortable with non-English characters.

### A Lot More Details
- find . -depth -name '*' -print0: This find command searches for all files and directories recursively in the current directory (.). -depth ensures that the directory tree is traversed depth-first, and -name '*' matches all items. -print0 prints the results separated by a null character (useful for handling filenames with spaces or special characters).

- | xargs -0 -n1 -P10 -I{} sh -c '...': The find command output is piped (|) to xargs. The -0 option tells xargs to expect null-terminated items. -n1 processes one item at a time. -P10 runs 10 parallel processes. -I{} sets the placeholder for input items. sh -c '...' runs a shell script with the given commands for each input item.

- generate_unique_name() { ... }: This is a function that generates a unique name for a file or directory. It takes three arguments: the base name, the extension (if any), and the destination path. It increments a counter and appends it to the base name until a unique name is found, then returns the unique name.

- process_item() { ... }: This is the main function that processes a single file or directory path. It sanitizes the name and renames the item if needed.

- [ "$item_path" = "." ] && return: This line checks if the item path is the current directory (.). If it is, the function returns without doing anything.

- dir_name=$(dirname "$item_path"); base_name=$(basename "$item_path"): These commands extract the directory name and base name from the item path.

- if [ -d "$item_path" ]; then ... else ... fi: This conditional block checks if the item is a directory (-d) and processes it accordingly.

- new_name=$(echo "$base_name" | sed -E "s/[^a-zA-Z0-9 _.-]+//g; s/[ .-]+/_/g; s/_+/_/g; s/^_//; s/_$//; s/(.*)/\L\1/"): This line uses sed to sanitize the base name by removing unwanted characters, replacing spaces and periods with underscores, and converting the name to lowercase. The -E flag enables extended regular expressions.

- [ -z "$new_name" ] && new_name="untitled": If the new name is empty, it is set to "untitled".

- file_ext="${base_name##*.}" base_name_no_ext="${base_name%.*}": For files, this line extracts the file extension and the base name without the extension.

- new_name="${new_base_name_no_ext}.${file_ext}": For files, this line constructs the new file name with the sanitized base name and the original file extension.

- if [ "$base_name" != "$new_name" ]; then ... fi: This conditional block checks if the original name and the new name are different.

- [ -e "${dir_name}/${new_name}" ] && new_name=$(generate_unique_name "${new_name%.*}" "${new_name##*.}" "$dir_name"): If the new name already exists, the generate_unique_name function is called to get a unique name.

- mv "$item_path" "${dir_name}/${new_name}" 2>/dev/null || true: This line moves (renames) the item to the new path with the sanitized name. If an error occurs, it is redirected to /dev/null (ignored) and the script continues executing due to the || true.

- process_item "{}": This line calls the process_item function with the input item path (represented by {}) as the argument.

- ' 2>/dev/null: This part of the script suppresses any error messages by redirecting the standard error output to /dev/null.

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[f7a49c4068...](https://github.com/Zergspower/effigy-se/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Wednesday 2023-05-10 04:17:40 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[c5dce84be8...](https://github.com/Singul0/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Wednesday 2023-05-10 04:35:12 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

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

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[1674f25725...](https://github.com/Singul0/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Wednesday 2023-05-10 04:35:12 by John Willard

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
## [soitun/hiphop-php](https://github.com/soitun/hiphop-php)@[b2e2e868b9...](https://github.com/soitun/hiphop-php/commit/b2e2e868b9f87b03d7c4729f654adb2efda4eb1e)
#### Wednesday 2023-05-10 04:46:23 by Lucian Wischik

log all outcomes of CLIENT_CHECK

Summary:
I asked viratyosin how his experience was with streaming errors -- was it working okay? was it getting stuck? He replied "I might not realize because I tend to hit Ctrl+C when things get stuck; does your telemetry show that?" This diff aims to improve telemetry here.

This diff changes the events associated with "hh". It used to be:
1. CLIENT_CHECK_START (produced only at the start of "hh check")
2. CLIENT_CHECK (upon successful completion of "hh check")
3. CLIENT_BAD_EXIT (used for all commands not just check, e.g. "hh start" and "hh lsp"). You have to filter by "command=Check" to get the bad exits specific to "hh check".

After this diff, "hh check" now produces these:
1. CLIENT_CHECK_START, as before
2. CLIENT_CHECK as before, upon success
3. CLIENT_CHECK_PARTIAL if it succeeded in printing some errors before user interrupted with Ctrl+C or SIGPIPE
4. CLIENT_CHECK_BAD_EXIT if it failed

Why?
* I figure that now with streaming errors, users may deliberately do Ctrl+C as soon as the first error has been shown. And this won't indicate failure; it will indicate success! I wanted this situation to be logged in a separate event CLIENT_CHECK_PARTIAL so it won't inadvertently be lumped with the others. I specifically didn't want it in the normal CLIENT_BAD_EXIT because I want to also get some check-specific telemetry (e.g. time to first error, time of most recent error)
* I figure that folks will also do "hh | head" to pipe it into things which only consume the first error, as their way of ending early. I wanted this to work properly without huge error spew. The common convention of other unix tools appears to just fail with exit code 141 upon such SIGPIPE, and not display anything.
* Scuba makes it awkward to search for nested queries such as `event=CLIENT_CHECK OR (event=CLIENT_BAD_EXIT AND command=Check)`. I'm aiming to turn the availability of "hh check" into an OKR, and I want the scuba queries for it to be easy to write.

While I was at it, I made some other changes:
* the CLIENT_CHECK_PARTIAL and CLIENT_CHECK_BAD_EXIT now also record the current value of the spinner, if any. If figured it'd be interesting to learn whether more people are hitting Ctrl+C in particular states.
* I changed the exit code of Exit_status.Interrupted to be 130, the unix standard code for Ctrl+C. And added a new one Exit_status.Client_broken_pipe (by analogy to the existing Exit_status.Event_logger_broken_pipe) with unix standard exit code 141.
* Removed `produce_streaming_errors` from rollout flags (since it's been at 100% for some weeks), and added `consume_streaming_errors` instead (so we can correlate whether Ctrl+C has gotten better or worse with this flag).

Reviewed By: CatherineGasnier

Differential Revision: D45196752

fbshipit-source-id: bc4ae99ae5d7d5b72e8fd32651efbcba07c98cc0

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[912e843f53...](https://github.com/Capsandi/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Wednesday 2023-05-10 04:48:55 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [ouoertheo/silero-api-server](https://github.com/ouoertheo/silero-api-server)@[3d43e576a7...](https://github.com/ouoertheo/silero-api-server/commit/3d43e576a7654d94a96534d209cca3590bcd03ce)
#### Wednesday 2023-05-10 05:11:57 by ouoertheo

Merge pull request #20 from ouoertheo/ouoertheo/fuck

i suck at this shit

---
## [M-D-Team/ait1.19](https://github.com/M-D-Team/ait1.19)@[3d925c798b...](https://github.com/M-D-Team/ait1.19/commit/3d925c798bd68cdae6937fc715734d588d998cdc)
#### Wednesday 2023-05-10 05:12:55 by Loqor

I did a bunch of stuff, I added the ControlEntitySchema, you're welcome. I can't figure out for the life of me how to get the tardisID for the console on placement, but that's also cause it's midnight and I've got 2 exams in the morning. I also did some more rotor animation stuff and added emission and fixed the lang file, plus added the console to the creative inventory.

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[ad302f209f...](https://github.com/orthography/tgstation/commit/ad302f209f4fc0b739c6eea8e6be92da05e2742c)
#### Wednesday 2023-05-10 06:29:05 by Zytolg

Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
--- 

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**


![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)



See the image in more detail here: https://imgur.com/iT5Vi8k



## Why It's Good For The Game

We've been with the same 5 maps for a while now. @san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**


## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.


/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@gmail,com>

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[c8c977989a...](https://github.com/orthography/tgstation/commit/c8c977989a793cfe1e24eb6aa4350e14335025e5)
#### Wednesday 2023-05-10 06:29:05 by John Willard

Mimes can no longer write without breaking their vow. (#74674)

## About The Pull Request

I feel this is gonna be unpopular with the lazy mime players.

Also, this is an idea I had in my backlog for a while now

![image](https://user-images.githubusercontent.com/53777086/231355622-2c5d5d5a-813d-420c-ae42-c1bdc657f3ba.png)

This removes the Mime's ability to write on paper while they're on their
vow of silence.
This can be compared to hand language, which doesn't let you speak
despite not being considered "talking", and PDA messaging, which does
the same.

Mimes can still write with their pen, which is a nice invisible white
color. I thought I would keep it in as I find that interaction funny to
have a Mime give someone just a blank paper, unknowing that there's text
on it.
Spraycans/Telekinesis/Circuits are also left unaffected because they
require actual effort to obtain (doing genetics, doing circuits, or
printing spraycans which take a lot of inventory space and is limited),
compared to paper which you can carry hundreds of papers around and is
bountiful across the station.

I thought this was attempted at least once, but I can't find any PR that
mentions it, so I'm shooting my shot to see if this is something we'd
want.

## Why It's Good For The Game

Mimes using paper is a lazy way to bypass their one job gimmick: Emoting
over talking.

If they get a job change, they can simply break their vow to access
paper writing abilities, so this doesn't affect that really. It more-so
hits the Mimes who uses the job for the free spells/healing
abilities/etc, and bypasses the downsides (im aware its harder to get
people to read paper than it is to talk to them, but you can literally
get the mute quirk and itll have the same effect without being the whole
job).

The point is, you don't get invisible walls for free; it comes at a cost
of not being able to talk to people. If you want to talk, then break
your vow, lose access to your Mime abilities, and remake it later when
the cooldown is over. You're not meant to do both.

## Changelog

:cl:
balance: Mimes can no longer write on paper without breaking their vow.
/:cl:

---
## [KayZach/Liberty-Station-13](https://github.com/KayZach/Liberty-Station-13)@[c3e6d8b901...](https://github.com/KayZach/Liberty-Station-13/commit/c3e6d8b90198a54e05d8d7e886aa5435c9a9af22)
#### Wednesday 2023-05-10 06:53:01 by KayZach

Add files via upload

Holy shit my first ever pr ever i probably broke six other things but i tested it
Unfucks the broken wire in Terra therma
Removes the light switch in medical so seb can see
fixes the morgue boxes that are facing the wrong way in capsa
adds a gambling table and some more plants to skylight

---
## [Tsar-Salat/tgstationcashew](https://github.com/Tsar-Salat/tgstationcashew)@[5252418df0...](https://github.com/Tsar-Salat/tgstationcashew/commit/5252418df0ed4726c5bf2a9599f95befd0aca086)
#### Wednesday 2023-05-10 06:57:36 by Mothblocks

Create a guide for atomization that includes a new allowance to pull requests that might add dead code (#71429)

@tgstation/commit-access 

I'm proposing a new use for the Atomic tag that we currently virtually
never use.

We have countless pull requests over time, and plenty of which open now,
that are enormous refactors over tens of files with thousands of
additions. We are historically pretty slow to review and merge these,
and it definitely scares a lot of maintainers off. I think part of the
reason is that we do not like dead code being added, which is completely
reasonable at our scale.

However, I propose that, for refactors/purely code stuff, we ease up on
this a lot, and encourage (not require) people to make smaller pull
requests, even to the extent that it creates APIs we do not use yet.

As an example, https://github.com/tgstation/tgstation/pull/71421 does a
massive refactor to carp. It also does some balance changes, which I
think we could agree could be split off if it was enough of a pain.
However, there's a bunch of other stuff that could have been individual
pull requests here with this new allowance.

- The new basic AI behaviors
- The regenerator component
- Pet commands component

These are things that:

- Would not be used until the transition from simple to basic, but are
easily reviewable on their own
- Are easy to REMOVE if the OP does not follow up
- Are easy to FINISH if the OP does not follow up

(I suspect even, for instance, that there are parts of Wallening we
could be merging right now, that's probably gonna be hundreds or
thousands of files long...)

Pros:
- PRs are more often easily reviewable
- PRs are quicker to merge, since we don't have conflicts from editing
one of the 70 files they changed
- Cleanups can be more easily finished by other people. I don't suspect
this will be likely, but it's not easily possible today

Cons:
- We have to mark the PRs as atomic
- Someone needs to look through every so often (I'm thinking like, once
a month or something) to see if the code ended up being used, or if the
committer still plans to use it
- If the PR is adding a complex enough API that isn't modular, it might
be very hard to remove. I suspect for PRs like this that we ask them to
have an implementer before merging.

NL voice would love your thoughts on this

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[07f91e5e79...](https://github.com/git-for-windows/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Wednesday 2023-05-10 06:58:10 by Jeff King

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
## [MrLi92/linux-6.1.14](https://github.com/MrLi92/linux-6.1.14)@[a06a4dc3a0...](https://github.com/MrLi92/linux-6.1.14/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Wednesday 2023-05-10 07:36:23 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [mrcasals/factorial-dotfiles](https://github.com/mrcasals/factorial-dotfiles)@[277b8a2c09...](https://github.com/mrcasals/factorial-dotfiles/commit/277b8a2c0904e13000f5a6ea713bd92d2f32fb48)
#### Wednesday 2023-05-10 07:48:37 by Pau Ramon Revilla

Disable snippets (#16)

This one is controversial and I will understand if you don't want to
merge it (I will branch if that's the case).

I hate snippets. I never use them and they get in my way. Maybe they are
wrongly configured, but the amount of times that I get snippets when I
don't want them is just a waste of time.

Examples:
  - Sometimes I want to move from `{}` to `do/end` and when I place the
    cursor on `{` and type `do<Enter>` I automatically get an annoying
    `end` that I have to delete imediately.
  - Sometimes I want to press `<Enter>` after a `{` and it will add
    ruby block parameters for no reason.

Do you use them? How do you workaround things getting in the middle when
you don't want them? It screws up my muscle memory.

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[1b5c0489a4...](https://github.com/moocowswag/FeatureInflation13/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Wednesday 2023-05-10 08:40:28 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[f2fd69a49a...](https://github.com/moocowswag/FeatureInflation13/commit/f2fd69a49a7d9308eb695c0368163d2f63a53a54)
#### Wednesday 2023-05-10 08:40:28 by ArcaneMusic

Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#75052)

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[8f7d225b88...](https://github.com/Offroaders123/Smart-Text-Editor/commit/8f7d225b88166b120b374cc705c742b514cb485f)
#### Wednesday 2023-05-10 08:40:37 by Offroaders123

Service Workin'

Brought over the modern async logic from my Service Worker over in Dovetail. It was much nicer, and I really like the way of building it's functionality with functions, as for some reason that wasn't how I programmed a while back, haha. Not that I would know to build it like that to start with, it's just funny when you look back and things seem so obvious once you have more experience since when you first started out.

Made some other nice changes to the rest of the codebase too. Found out in VSCode that using dashed with JSDoc descriptions isn't actually fully supported to render only a single dash, so it's showing two in some places. I didn't like that, so I'm going to move my code that does that over to not having the dashes, instead. I think some of my other projects may do that as well, so I will look out for it as I go. I like the code readability with the dashes, but I'd rather it not instead break how the actual descriptions look in your editor, that's more important than looking at them from the code side. Ideally both would work, but yeah.

---
## [VolmitSoftware/React](https://github.com/VolmitSoftware/React)@[afbc273a23...](https://github.com/VolmitSoftware/React/commit/afbc273a23ef76bd1088b917f697f0d25ddb1337)
#### Wednesday 2023-05-10 08:55:57 by Brian Neumann-Fopiano

Removed the old shit, and added some stupid sampler

I have no fucking idea why its sampling 2x, but oh well, not my problem

---
## [rdtabb/Expressive.-Full-stack-blog](https://github.com/rdtabb/Expressive.-Full-stack-blog)@[dd3b04dce2...](https://github.com/rdtabb/Expressive.-Full-stack-blog/commit/dd3b04dce283cb5b9ffee5e4180e948641bc5fd3)
#### Wednesday 2023-05-10 08:59:06 by Rinat Tabaev

solved issue, it was so bloody stupid. Apart from Link heading to non-existing route, I tried to subsribe my useGetGivenComment hook which fetches data using react query to the generalFeedContext! Of course it cannot receive data from context, it does not exist in the component tree! it is fucking hook! Oh my good

---
## [MrLi92/linux-6.1.14](https://github.com/MrLi92/linux-6.1.14)@[4d6fa57b4d...](https://github.com/MrLi92/linux-6.1.14/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Wednesday 2023-05-10 09:18:17 by Jason A. Donenfeld

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
## [psionic-k/melpa](https://github.com/psionic-k/melpa)@[570bde6b4b...](https://github.com/psionic-k/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Wednesday 2023-05-10 09:45:11 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [nadimkobeissi/nym](https://github.com/nadimkobeissi/nym)@[b0546357f4...](https://github.com/nadimkobeissi/nym/commit/b0546357f471d2e7020fa122433036c5f94600b9)
#### Wednesday 2023-05-10 10:14:50 by Nadim Kobeissi

Fix TS SDK examples and make them independent

The Nym TypeScript SDK comes with two main examples:

- `plain-html`
- `react-webpack-with-theme-example`

As of time of testing on the latest `develop` branch over at
@nymtech/nym, `react-webpack-with-theme-example` was broken because the
example was expected to load some of its packages from its own
`package.json` and the rest from the repository's root `package.json`,
which caused the problems outlined here:

https://stackoverflow.com/q/72413194

While addressing this issue, I noticed that the examples were not truly
independent from the rest of the repo. While I know that this is a
monorepo with mulitple workspaces and understand how that's supposed to
work, I think that specifically in the case of example folders, we need
to ensure the ability for these folders to work fully independently from
the rest of the repository, because example folders are overwhelmingly
likely to be copied out of the repo to be expected by curious third
parties to work while fully self-contained. Furthermore, this makes
resolving the above-mentioned original issue easier.

Therefore, in this commit, I did the following for both `plain-html` and
`react-webpack-with-theme-example`:

- Ensure that their `package.json`s are fully self-sufficient and that
  no packages would need to be loaded from the repository's root
  `package.json`.
- Ensure that their `tsconfig.json` are equally self-sufficient and do
  not reference the repository's root `tsconfig.json`.
- Ensure that the webpack configuration is present in each example,
  instead of being snuck into a hidden `.webpack` folder in the
  `sdk/typescript/examples` folder (this struck me as an ugly hack
  anyhow).
- Ensure that `react-webpack-with-theme-example` has direct access to a
  small SVG graphic of the Nym logo within its own folder.

I think these changes will both render the examples less likely to break
as the rest of the monorepo evolves. Freezing dependencies in time is
not appropriate for the monorepo, but it is totally appropriate for
examples since we don't really care about migrating them to the latest
best practices/security fixes for their dependencies as much.

Also, these changes will make the example folders more friendly for
third-party engineers, since they can just copy out the example folder
from the repo and have everything they need to understand how things
work within the example folder itself, instead of needing to hunt down
other files in the sprawling monorepo.

---
## [overhangio/tutor](https://github.com/overhangio/tutor)@[2b73309670...](https://github.com/overhangio/tutor/commit/2b7330967067f1ac58574553e892248bef2ed13e)
#### Wednesday 2023-05-10 10:17:21 by Régis Behmo

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
## [leticia-sou/Projeto_Estacionamento](https://github.com/leticia-sou/Projeto_Estacionamento)@[ca78139910...](https://github.com/leticia-sou/Projeto_Estacionamento/commit/ca78139910a1285805be017acd217c5e00202187)
#### Wednesday 2023-05-10 10:53:11 by BomberBeetle

fixed the shitty eclipse project autogen like wtf girl this IDE sucks dick

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Wednesday 2023-05-10 12:15:47 by Jeremy Kersten

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
## [microsoft/terminal](https://github.com/microsoft/terminal)@[6ad8cd0a63...](https://github.com/microsoft/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Wednesday 2023-05-10 12:16:46 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [Iajret/Fluffy-STG](https://github.com/Iajret/Fluffy-STG)@[7c6e64caef...](https://github.com/Iajret/Fluffy-STG/commit/7c6e64caefea860c27c7f11f16d067f99a25320b)
#### Wednesday 2023-05-10 12:46:44 by SkyratBot

Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

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
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[1a918a2e14...](https://github.com/MTandi/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Wednesday 2023-05-10 13:42:40 by Jacquerel

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
## [Zarchyar/Roguelike-Adventures-and-Dungeons-2](https://github.com/Zarchyar/Roguelike-Adventures-and-Dungeons-2)@[457271f8c4...](https://github.com/Zarchyar/Roguelike-Adventures-and-Dungeons-2/commit/457271f8c4c23e3d72cd1dc062e5073913fdfa53)
#### Wednesday 2023-05-10 13:52:34 by VanyaBaou

greek fantasy adjustments

removed unobtainable stuff
-gorgos
-apollo/artemis bow, dev is dipshit and deleted them from datapack and hopped versions in attempt to get more downloads, yeah im pissed

snakeskin now attached to Drakaina quest
bronze -> ichor-infused, because again dev hates his fans, deleted all 1.16 wiki info
kill neutral/passive/friendly -> observer
+winged sandals quest
+palladium quest, with some info on how it works
idk what else im tired man

---
## [jacobhinkle/Fuser](https://github.com/jacobhinkle/Fuser)@[9c50ae8f14...](https://github.com/jacobhinkle/Fuser/commit/9c50ae8f1441917c97ebaceb343ad6be3c54304b)
#### Wednesday 2023-05-10 14:24:00 by Gao, Xiang

Remove runtime out of bound check debugging util (#277)

The change in this PR is easy to understand and has low impact, but the
motivation really needs discussion and is a much more impactful thing.
And I want to use this PR to discuss it.

In https://github.com/NVIDIA/Fuser/issues/248 we agreed to add "stride
order" support to codegen, and later in today's morning meeting on
matmul, Christian talked about the idea of "allocation_domain" which is
a generalization of the idea of "stride order". Basically, we are not
married to the rFactor domain of the tensor when doing allocation and
indexing. We can pick an arbitrary vector of `IterDomain`s between root
and leaf domain, stop the indexing process on that vector, and do
allocation based on that vector. For the idea of "stride order", which
is a special case of the new idea, this vector is just the reordered
rFactor domains. This should be easily approachable with our new
indexing approach https://github.com/NVIDIA/Fuser/pull/32. This idea
does make a lot of sense, so the purpose is not to discuss whether we
want to take that idea, but how to implement that idea.

A question comes to me during implementing is, say we have a tensor
whose semantic shape is `NCHW` but stride order is `NHWC`, should the
`stride` field of the tensor be in the order of `NCHW` or `NHWC`?
Currently, we are using the same order as PyTorch, which is the semantic
order `NCHW`. I think this does make a lot of sense in terms of stride
order support. Having the stride in the semantic order is not the most
naturally way for indexing, we do need a `NHWC->NCHW` axis map to grab
the correct stride, but it is pretty simple to implement this.
Considering all factors, including consitency with PyTorch, cleanness in
the executor's code, I still think the semantics order is the best
design.

However, this design start to make no sense when we generalize the
"stride order" idea into the "allocation_domain" idea. For example, for
an `NCHW` tensor, the actual allocation can be `(H*W, N*C)`, and the
size of `contiguity` will be `2` instead of `4`. So the `Tensor::stride`
in `runtime/tensor.cu` should also be an array of size `2` instead of
`4`. The idea of "allocation_domain" requires the stride of a tensor to
be strictly one-to-one mapped to the allocation domain. As a special
case, the "stride order" idea has no choice but to follow the same
design, which is, the stride will be stored in `NHWC` order. This means,
the order of stride in our kernel is different from those in ATen, we
can not directly copy the stride. We need to permute the stride so it is
sorted descending.

But the above problem is not the biggest trouble we have, the biggest
trouble is: If we have a `NCHW` tensor allocated as `(H*W, N*C)`, is
this tensor a 4D tensor or a 2D tensor? I think the answer is "neither".
In terms of allocation and stride, it is definitely 2D, but in terms of
semantics, it is 4D. Again, in the past, we had a concept "the
dimensionality of a tensor" which is a degeneracy of two concepts "the
semantic dimensionality of a tensor" and "the allocation dimensionality
of a tensor". Now we break the symmetry, and degenerating concepts are
no longer degenerate. In codegen, we are generating a lot of tensor
shapes like `T0.shape[0]`, and I think the easiest way to handle them is
to keep `shape` in semantic dimensionality, while make `stride` in
allocation dimensionality. That said, `struct Tensor` now needs two
template arguments for dimensionalities. And unfortunately, we can no
longer do out of bound check any more.

---
## [TheDuckCow/MCprep](https://github.com/TheDuckCow/MCprep)@[a34b01aa69...](https://github.com/TheDuckCow/MCprep/commit/a34b01aa69f7e215a0cd6ec46665e1c15a0a78ca)
#### Wednesday 2023-05-10 14:40:30 by mahid

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
## [QueerGlobal/qg-frontend-v2](https://github.com/QueerGlobal/qg-frontend-v2)@[6db1177f7f...](https://github.com/QueerGlobal/qg-frontend-v2/commit/6db1177f7fe1a2905ac83d4d5708db3db37afea0)
#### Wednesday 2023-05-10 14:55:50 by Mekesia Brown

.gitignore Update - Add Slash in Front of Notes Directory Line (#17)

_I added some type setting, added a recommended placeholder image and
helpful route for any local notes folks keep, updated social media links
(with a correction of alt text attribute), and I FINALLY moved the
Footer component to the global App.js file. Now the footer will be
everywhere._

UPDATE: I ended up removing all changes except for the notes folder
slash in .gitignore since other changes are now in corresponding prs.

Please note that the whitespacing changes are a pain in the ass and I
don't know how to fix those yet. Please disregard since locally the app
works.

Please email me if you need any information, or of course comment in
this pr. As well you can Slack me. Thanks.

---
## [IbrahimFadel/flux](https://github.com/IbrahimFadel/flux)@[789a6ea51f...](https://github.com/IbrahimFadel/flux/commit/789a6ea51fb7940d5a64a18a09bd24db48ab95f5)
#### Wednesday 2023-05-10 15:16:21 by Ibrahim Fadel

shit ton.. cross package name res, kinda, This kw (This paths for assoc types), this kw for referencing struct in methods, prolly some other stuff i dont remember. but everythings super jenky and messy and horrible

---
## [Limaomao821/linux-kernel-lab](https://github.com/Limaomao821/linux-kernel-lab)@[561d896a14...](https://github.com/Limaomao821/linux-kernel-lab/commit/561d896a14684eb648a138fd18f9084c51b2dd14)
#### Wednesday 2023-05-10 15:21:50 by Michal Vlasák

tools: labs: qemu: Add run-qemu.sh as alternative

TL;DR: In one window run `make -j$(ncproc) console` and `cd` to some
lab's subdirectory (`skels/...`). In second window `cd` to matching
`skels/...` subdirectory, edit source files and compile with something
like `kmake` (`alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`) as
needed. The `skels` directory is shared between the host and the guest,
thus in the first window, so you can just `insmod` and `rmmod` the
compiled modules. You can kill the VM by `CTRL-a x` (if you made some
writes from the VM it might be a good idea to run `sync` first). Samba
and QEMU are required.

Full description:

To be honest I don't like the current QEMU setup. I am sure there are
things it does that I don't understand yet, because I have not yet
finished all the labs, but in any case I think that the setup can be
improved.

Some things in particular I don't like about the current setup:

 - "Huge" opaque `.ext4` images are used, even though the contents of
   the  root file system are not that large.
 - While running QEMU newly built modules can't be copied to the image.
 - Mounting and unmounting the `.ext4` image for copying the modules
   requires `sudo`.
 - The networking setup seems too complex, requires `sudo` and was
   broken (at least for me - IIRC I didn't get IP through DHCP), thus I
   also didn't get `ssh` to work. I also seem to be not the only one
   having issues with this:
   https://github.com/linux-kernel-labs/linux/pull/240#issuecomment-956219190
 - `dnsmasq` and `nttctp` mostly don't start correctly (they are not
   killed correctly by the previous run) - this isn't a problem on my
   end, as demonstrated by the output at
   https://linux-kernel-labs.github.io/refs/heads/master/info/vm.html,
   which shows the same issues.
 - Running `minicom` is required to access the serial port, thus at
   least two terminals are required for working with the VM (not a huge
   problem for me personally, since I use `tmux`, but I know some people
   complain about this). The setup also seems unnecessarily complex.
 - I remember a lot of the `.mon` `.pts` files being left uncleaned in
   some cases.
 - I recall warnigns about some of the entries added to `/etc/inittab`
   being ignored.
 - Even though root login requires no password I have to enter the
   `root` username.

In this commit I introdoce an alternative way of running QEMU through a
new `run-qemu.sh` script. The setup is laregely independent and its user
interface consists of `console` and `gui` targets. I tried to make the
script parameterizable through environment variables (inherited from
Make variables), though it may be argued that the default values should
be encoded in Makefile rather than in the script like they are now. I
have no strong opinions about that, it's' just that the current state
allows running the script in standalone fashion.

What the setup brings:

 - A rootfs is extracted from the official Yocto Project tarball and
   kept in a directory that is shared through  [Samba as network
   share](https://www.kernel.org/doc/html/latest/filesystems/cifs/cifsroot.html).
   The `skels` directory is shared as well. Thus the modules can be
   freely tweaked / compiled / ran from either the host or guest.
 - The QEMU stdio serial console setup is used (`ttyS0` on the kernel
   side). This means that running QEMU results in the serial console
   being mapped directly to standard input and output of the terminal -
   `minicom` is not needed. This is the console mode (`make console`).
 -  The setup allows also allows the virtual machine to be run in
    graphical mode (`make gui`).
 - Root is logged in automatically in `console` mode (though similar
   thing could be done for the `gui` mode).
 - Although Samba (`smbd`) is required, `sudo` or root access is not.
 - Networking through QEMU's default [SLIRP backend](https://wiki.qemu.org/Documentation/Networking#User_Networking_.28SLIRP.29).
   DHCP is handled by the kernel, which overcomes some problems I had
   with the System V init system in the Yocto images.
 - The compilation can largely be done with something like this `kmake`
   alias: `alias kmake='make -C "$HOME/src/linux/" M="$(pwd)"'`
   (customize as needed). Though this is not enough for some labs (I no
   longer remember the details, but I think it was some of the earlier
   labs which had dependencies between modules, I think I used the
   classic `make build` for that.

Known issues:

 - SSH support is currently missing. This both requires more featureful
   Yocto images and is IMO unnecessary, since it wouldn't bring much
   benefit over the console mode. Though it can be easily achieved by
   using QEMU option like `-nic user,hostfwd=tcp::2222-:22`, which would
   allow SSH'ing into the guest by something like `ssh -p 2222
   root@localhost`.
 - I used a slightly less advanced setup while doing the labs, so the
   lab workflow with this particular setup is largely untested. There
   may be problems with file permissions due to the samba share.
 - The guest seems to fail to shutdown correctly in a timely manner. I
   just took the habbit of killing qemu with `CTRL-a` followed by `x`,
   potentially running `sync` first to ensure my work is saved (though
   rarely did I actually modify anything on the guest side).

[The former setup](https://github.com/vlasakm/linux/commit/720bd6444a036c2ae6a3e76b7f6aac72f562053a)
I used contains some details of the SSH setup if anyone is interested in
that. It was the basis for this PR, so some ideas can be seen there
(Samba share for `skels`), but I didn't take particular care with [the
kernel config](https://github.com/vlasakm/linux/commit/0290919905e7f4fe3562a46d3274f8d41ad02c55)
and the automounting didn't really work (the `init` would try to mount
the filesystem before networking was up).

What I evaluated and didn't use in the end:

 - At first I tried to extend my former setup by just automounting the
   Samba share. I didn't manage to do this - the (non)workings of init
   scripts seem to be beyond me. If anyone is interested here are a few
   pointers:
   [[1]](https://unix.stackexchange.com/questions/169697/how-does-netdev-mount-option-in-etc-fstab-work),
   `/etc/inittab`, `/etc/init.d/mountall.sh`, `/etc/init.d/mountnfs.sh`.
 - I tried using `9p` [[2]](https://wiki.qemu.org/Documentation/9p),
   [[3]](https://wiki.qemu.org/Documentation/9psetup)
   [[4]](https://wiki.qemu.org/Documentation/9p_root_fs) which is built
   into QEMU and can be compiled into the kernel. With `mapped-xattr`
   security model it would be too cumbersome to create the rootfs, and
   `passthrough` would require root privileges. It is also very slow.
   There are also some problems with trying to use it as rootfs, maybe
   specific to `linux-kernel-labs` kernel version or config. Ask me if
   interested.
   [[5]](https://lists.gnu.org/archive/html/qemu-devel/2016-09/msg07184.html)
   [[6]](https://lore.kernel.org/linux-fsdevel/20210608153524.GB504497@redhat.com/)
   [[7]](https://lore.kernel.org/all/YL1eM+mzjuggDvqp@codewreck.org/T/)
 - QEMU has an option to setup the Samba share on its own, though I
   found a custom config (based on the QEMU one) to be easier - allows
   customization like multiple shares, unix extensions, different port,
   etc.

Signed-off-by: Michal Vlasák <lahcim8@gmail.com>
Signed-off-by: Daniel Baluta <daniel.baluta@nxp.com>

---
## [ServiceWeaver/weaver](https://github.com/ServiceWeaver/weaver)@[b9eb4fc35d...](https://github.com/ServiceWeaver/weaver/commit/b9eb4fc35df080f128de5d674e2ca52d7483932a)
#### Wednesday 2023-05-10 16:08:09 by Michael Whittaker

Changed deployers to persist data in one spot.

Recall that deployers often have to persist various data to the file
system. The "weaver multi" deployer, for example, persists logs,
registrations, and traces to files.

Before this PR, deployers would store logs in /tmp and everything else
in ~/.local/share/serviceweaver. Different deployers would sometimes
store their data in the same directory. A "multi_perfetto.db" file would
be right next to a "single_perfetto.db" file, for example.

This made purging data files annoying. It was like a scavenger hunt
trying to track down the various places that data was stored. This PR
changes deployers to store all their data in a single directly. For
example, the "weaver multi" deployer now stores everything inside
"~/.local/share/serviceweaver/multi". The single process deployer stores
everything inside "~/.local/share/serviceweaver/single".

This makes purging much simpler. It also makes it clearer which files
are being used by which deployers.

Note that this PR moves logs out of /tmp, which persists them longer.
This means that logs won't be garbage collected automatically, but I
think that's actually a good thing. We should implement a principled way
of garbage collecting logs, rather than leaving it up to /tmp. I think
it would be surprising and frustrating if an important log file was
spuriously deleted by the OS.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3422129a54...](https://github.com/mrakgr/The-Spiral-Language/commit/3422129a5429ddb8626e0004f6c07a861b953da4)
#### Wednesday 2023-05-10 16:39:40 by Marko Grdinić

"9:30pm. https://news.ycombinator.com/item?id=35853148
The Prime Video microservices to monolith story (adrianco.medium.com)

///

If you have a predictable workload (i.e. we ingest 100,000 videos a month with n size) you should be looking at it from that perspective -- how much compute you are going to need, and when. Serverless works well for predictably unpredictable, infrequent workloads that don't need to have perfect output ("good enough").
The big mistake I see people make is trying to be overly clever and predict the future workload needs. It never works out like that. Design for your current workload now, if your architecture can handle 10x of that great! Each time your scale from 10x workload you will likely need to redesign the system anyway, so you shouldn't pay that tax unless you absolutely have to.

There are a lot of limitations of serverless, the big one I experienced was inability to control the host environment and limitations on the slice of memory/CPU you get, such that you must take that into consideration when designing your atomic work units. Also paying the distributed computing tax is real and occurs at development and runtime -- things like job tracking and monitoring are important when you have 10,000 processes running -- you start to get into the territory of things that basically never happen on a single machine or small cluster, but become problems with thousands of disparate machines / processes.

///

///

>Design for your current workload
Please be my friend.

The bulk of my job these days is sitting in design reviews trying to convince people that just making up scenarios where you need to scale to 100x isn't actually engineering. It's exhausting self-indulgence. Nothing is easier than inventing scenarios where you'll need to "scale". It's borderline impossible to get software folks to just live in the world that exists in front of their eyes.

"Scale" should go back to its original meaning: change relative to some starting point. Slap a trend line on what you know. Do some estimation for what you don't. Design accordingly.

///

Let me link to this thread as it is pretty interesting.

11:25am. https://youtu.be/RZhTC33lStQ?t=89

He did NNs back in 2013.

https://youtu.be/RZhTC33lStQ?t=119
> No way you made this...

https://youtu.be/RZhTC33lStQ?t=211

It is totally a lie that Mojo is a faster Python. If it was possible to make Python faster, partial evaluation systems would have done it.

https://youtu.be/RZhTC33lStQ?t=705
> Every single Python library works in Mojo.

Incidentally, the language is behind a wait list similar to Jai.

5/10/2023

10:15am. What the fuck, why isn't the editor reacting to the changes in the bindings project?

10:20am. I am confused. Why is the editor completely inactive to the changes in the bindings project all of a sudden?

10:30am. There is something wrong with Rider here.

10:35am. Goddamit, this weird IDE bug has wasted so much of my time.

For some reason adding that file leads to it reverting to the cache despite the fact that I've cleaned it.

```
PS E:\Webdev\Fable\CFR-In-Fable> dotnet run
run Run
Building project with version: LocalBuild
Shortened DependencyGraph for Target Run:
<== Run
   <== InstallClient
      <== Clean

The running order is:
Group - 1
  - Clean
Group - 2
  - InstallClient
Group - 3
  - Run
Starting target 'Clean'
E:\Webdev\Fable\CFR-In-Fable\src\Client> "dotnet" fable clean --yes -o output -e .js (In: false, Out: false, Err: false)
Fable: F# to JavaScript compiler 4.0.6
Thanks to the contributor! @Kurren123
Stand with Ukraine! https://standwithukraine.com.ua/

This will recursively delete all *.js[.map] files in E:\Webdev\Fable\CFR-In-Fable\src\Client\output
No files have been deleted. If Fable output is in another directory, pass it as argument.
Finished (Success) 'Clean' in 00:00:00.4153216
Starting target 'InstallClient'
.> "C:\Program Files (x86)\nodejs\npm.CMD" install (In: false, Out: false, Err: false)

up to date, audited 187 packages in 776ms

10 packages are looking for funding
  run `npm fund` for details

3 moderate severity vulnerabilities

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
Finished (Success) 'InstallClient' in 00:00:02.0424796
Starting target 'Run'
E:\Webdev\Fable\CFR-In-Fable\src\Shared> "dotnet" build (In: false, Out: false, Err: false)
MSBuild version 17.5.1+f6fdcf537 for .NET
MSBUILD : error MSB1011: Specify which project or solution file to use because this folder contains more than one project or solution file.
Finished (Failed) 'Run' in 00:00:00.2006070
```

I feel like I am in a bizarro world. Why is dotnet run failing all of a sudden?

...Why did it put a csproj file in Shared?

Let me try invalidating the project cache again.

```
Follow. Rider has to store both ReSharper and IntelliJ settings and cache files. On Windows, the ReSharper host cache files are kept in the%LOCALAPPDATA%\JetBrains\Rider{version}\resharper-host\local\Transient\ReSharperHost\v{version}
```

Let me purge this by hand.

11:15pm. I put it all into the same file.

2:50pm. Done with breakfast and chores.

Let me chill a bit more and then I will resume.

```
    type Auto =
        static member generateBoxedDecoderCached(t: System.Type, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): BoxedDecoder =
            let caseStrategy = defaultArg caseStrategy PascalCase

            let key =
                t.FullName
                |> (+) (Operators.string caseStrategy)
                |> (+) (extra |> Option.map (fun e -> e.Hash) |> Option.defaultValue "")

            Util.CachedDecoders.GetOrAdd(key, fun _ -> autoDecoder (makeExtra extra) caseStrategy false t)

        static member inline generateDecoderCached<'T>(?caseStrategy : CaseStrategy, ?extra: ExtraCoders): Decoder<'T> =
            Auto.generateBoxedDecoderCached(typeof<'T>, ?caseStrategy=caseStrategy, ?extra=extra) |> unboxDecoder

        static member generateBoxedDecoder(t: System.Type, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): BoxedDecoder =
            let caseStrategy = defaultArg caseStrategy PascalCase
            autoDecoder (makeExtra extra) caseStrategy false t

        static member inline generateDecoder<'T>(?caseStrategy : CaseStrategy, ?extra: ExtraCoders): Decoder<'T> =
            Auto.generateBoxedDecoder(typeof<'T>, ?caseStrategy=caseStrategy, ?extra=extra) |> unboxDecoder

        static member inline fromString<'T>(json: string, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): Result<'T, string> =
            let decoder = Auto.generateDecoder<'T>(?caseStrategy=caseStrategy, ?extra=extra)
            fromString decoder json

        static member inline unsafeFromString<'T>(json: string, ?caseStrategy : CaseStrategy, ?extra: ExtraCoders): 'T =
            let decoder = Auto.generateDecoder<'T>(?caseStrategy=caseStrategy, ?extra=extra)
            match fromString decoder json with
            | Ok x -> x
            | Error msg -> failwith msg
```

Hmmm, is this how it works?

https://stackoverflow.com/questions/34447766/f-static-let-and-static-member

I had no idea that `static let` even existed.

5:15pm.

///

Anyway, Message Pack is quite promising. It actually gives us back the .NET types.
It's just too bad they are the wrong ones.
That tag should have been an int, but we got a back a byte.
Since we don't need union cases with a large number of tags we might as well convert those tags to bytes internally.
But for rest of the numerical types, we'll need sure they are of the right size.
And since this just happened...
Damn, we thought this protocol would at least be good for transfering large homogenous arrays, but since it converted what we thought would be an int to a byte, it might do that for arbitrary elements.
We'll do a few hacks to make it work, stay tuned.

No, we give up for once. We have better things to do than write our own serializers for the next few days.
Let's close it here.
We learned how to do cross module inlining, F# reflection. Before that we learned how to write Fable Bindings.
And we do have one good library we can use to serialize and deserialize F# types.
The message pack protocol here can serve when we need to transfer types that aren't complex, like plain records.

///

I ended up ignoring the above and actually making it work. `Convert.ChangeType` saved me.

5:35pm.

///

We actually have our own functional programming language called Spiral that could do this kind of task very cleanly, at maximum performance.
It was made for creating ML libraries on novel hardware, so it is a lot more efficient than F#.
Doing a Javascript backend for it would not be hard, and in fact it already has an F# one.
But adding another language just for this kind of task to the project would not be ergonomic.

///

I'll cut this out. It is not time for Spiral.

6pm. Right now it is rendering. Enough serialization. Thoth.Json 4 life!

I put so much effort into it, but I'll never need to use anything else.

At this point though, I am really comfortable with .NET reflection.

I definitely understand it now which isn't something I could have said a few months ago.

6:15pm. https://youtu.be/6x5t9pTtCo4
Microservices. Serialization And Deseriation Of F# Types With SignalR (Pt. 4.2)

Let me post this on the F# sub. I am done with programming for the day.

Tomorrow I will bring the leduc project to a close, the day after I'll deploy it and then I will get started working on a store.

6:40pm. https://youtu.be/J7ITgYBn_3k
Scaling Up Prime Video | Prime Reacts

Why do I keep watching this guy?

But he is amusing.

When is lunch?"

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[0e96f1cd6e...](https://github.com/software-mansion/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Wednesday 2023-05-10 17:52:47 by Tomasz Żelawski

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
## [imstylen/evals](https://github.com/imstylen/evals)@[170dfd886c...](https://github.com/imstylen/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Wednesday 2023-05-10 18:11:19 by Robert Bateman

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
## [newstools/2023-sowetan-live](https://github.com/newstools/2023-sowetan-live)@[8ef4fffdbe...](https://github.com/newstools/2023-sowetan-live/commit/8ef4fffdbec6f42d5a4093abd724080316eb0d12)
#### Wednesday 2023-05-10 18:19:16 by Billy Einkamerer

Created Text For URL [www.sowetanlive.co.za/news/south-africa/2023-05-10-two-life-terms-for-north-west-man-who-killed-ex-girlfriend-and-her-mom/]

---
## [Tristrian/tgstation](https://github.com/Tristrian/tgstation)@[c3b78761d2...](https://github.com/Tristrian/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Wednesday 2023-05-10 19:52:09 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[199aa000d3...](https://github.com/Wallemations/heavenstation/commit/199aa000d3f46ee4386a65079992e4b9d0f2537d)
#### Wednesday 2023-05-10 20:08:12 by Rhials

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
## [warptools/warpforge](https://github.com/warptools/warpforge)@[be7cff55c7...](https://github.com/warptools/warpforge/commit/be7cff55c72fabe132535a565ec80296bf4de4ee)
#### Wednesday 2023-05-10 20:09:06 by Eric Myhre

tests which maintain CLI help docs in the website repo.

... if you have it checked out in the appropriate relative path.
(I'm not yet attempting to introduce any closer coupling of repos.
In the long run, this is probably a great case for submodules again,
or possibly some dogfooding of warpforge's own relationships for
modules in a workspace (if we dare put that level of complex
self-hosting in our own path, which... may not be wise).  But that
won't improve velocity today, so, it's a job for later.)

This uses testmark to maintain the data again.

A few deps are bumped... so that we can use the new testmark suite
system.  That makes it really easy to do a large batch of similar
tests across multiple files.

I haven't retrofitted any other existing tests to use the suite system,
but it's almost certainly going to make them simpler and more robust
too.

The CLI help generation is now *all* in markdown, including flags.
I cargo-culted a lot of the stringer there, and added a few very
minor opinionated tweaks of opportunity.  It's probably still all
nonfinal; and in particular I'm still utterly giving up on trying to
get the whitespace I want out of golang templates.

There's a few tweaks to the experimental goldmark code, because I
found... either an interesting edge case, or an outright bug.
Some of our text with parenthesis causes goldmark to produce paragraph
objects that point to themselves as siblings... in a loop.  Oof.
I don't know if that's intended behavior or not, but I doubt it,
because it sure surprised me.  Anyway, for now I work around it.
Our yak-shave depth is already entirely too high right now.

So what _becomes_ of the generated docs hunks?  Well, over in the
site repo, the static site rendering pipeline actually hoists those
hunks back out, and processes them as markdown again.
Isn't that neat?  (There's a "clidocs" tag on the code blocks
which engages that... though you can't see that in this diff; it's
entirely over in the site repo.)

Probably the most "oof" thing in this diff is... I had to disable
the automatic file-level parallelization in the testmark suite system,
because of the dang package scope shenanigans with the CLI lib.
The amount of pain that's producing is already staggeringly high.

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[6de48996c5...](https://github.com/warptools/warpforge/commit/6de48996c58fde1989a91aba62d18e42bb88517e)
#### Wednesday 2023-05-10 20:09:06 by Eric Myhre

Research checkpoint commit: markdown processing.

This has... mixed success.

I've got three different irons in the fire here:
 1. The plain markdown text coming out (to sanity check my templates)
 2. A library called Glamour used to process it
 3. A brief prototype of going straight to Goldmark and using
  that system's renderers directly on the AST.

I've posted a bunch of notes on this in the dev chat on Matrix already,
as well as some screenshots, so I'll keep this commit note briefer.

In short, controlling the line spacing and indentation is turning out
remarkably hard with option 2.  In fact, I think it's outright
impossible without some invasive changes tantamount to forking.
So that's a bummer.  It got good rapid results and was very exciting!
But "indent the contents under an h4 deeper than under an h2" is just
not a feature I can get there.  And there are a few other weird cliffs
to customizability (links can only be handled one way, except for a
special case around fragment-only links?  tables or other attempts to
pack info densely are limited.  etc) that are unfortunate.

Getting isomorphic html output, if I wanted to include spacing and all,
and have it rendered in html identically to how it would be in plain
ANSI terminal text, is also looking pretty hard with Option 2.
I think we'd end up literally storing the ANSI and all in testmark
codeblocks, and then writing code in the site generator to re-render
that into html.  Possible, and well within the range of things I was
considering doing anyway at the begining of this exploration, but...
also maybe not totally ideal, considering how much control we _could_
have of this, by going with Option 3.

Now, Option 3... well, the big question there is simply "how much work
is that going to be?", and the answer is "I don't know".

But the prototype of using goldmark directly with my own renderer went
off pretty much without a hitch, and it seems like it reaches a very
maximal level of control.  And for reference, the size of goldmark's
own html renderer is about 1000 lines of (very understandable) code.
That's... about a 990 lines more than I'd _like_ to own, but on the
other hand, if it's self contained and doesn't need much tweaking
after the first pass, maybe it's acceptable.

In exchange for that code, we'd get utterly total control of rendering,
so we could fearlessly use all sorts of stuff (say, even codeblocks
within text within headings that describe flags, and get all of it
aligned correctly)... and it would become also totally in reach to
write branches for emitting html color annotations vs ANSI, with full
correctness as the action of both would be driven by the same AST walk.

Jury's still out a bit.  This checkpoint is just that: a checkpoint.
Some of this code will disappear again, for certain.  Which, exactly,
is not yet certain.

---
## [Perkedel/perkedel-astro](https://github.com/Perkedel/perkedel-astro)@[529e4e8ede...](https://github.com/Perkedel/perkedel-astro/commit/529e4e8ede9db44daf8dd01af75709e3d228fb39)
#### Wednesday 2023-05-10 20:23:20 by Joel Robert Justiawan

meozek

Hear me out. I think adopting homestuck, we'll put them on interpol, uh..
busting up criminals on social media
e.g. who uhm..
harrassing innocent vtubers, vice versa other case, etc.
yeah. Twitter.
Look at the MsPaint Adventure Wiki here.
they noted that Troll was a name-after internet trolls, and these trolls
do something bad to the humans.
same with real life.

as you can see, Troll is now just a being.
there are more things that are matter.
what matter now is this.

---
## [ptcrash/official_joke_api](https://github.com/ptcrash/official_joke_api)@[e75af4521d...](https://github.com/ptcrash/official_joke_api/commit/e75af4521d7db11e98d6d8848278771d28816a0a)
#### Wednesday 2023-05-10 20:33:42 by John Martin

Removed Context-Heavy Joke

I didn't fully understand this joke so I did some digging and I think I understand it now. But if this is a "whoosh" moment on my part, just know I have sincere intentions lol.

I'm proposing we remove this joke for two reasons:
1. It's not widely accessible because It requires the listener to understand Indian names and meanings to get that the punchline.
2. While the joke paints female developers in a positive light, it still has a womanizing tone that I don't think everyone receives well. I think it would be better to just steer clear from jokes involving gender at all.

---
## [ProjectWastelanders/ProjectWastelanders](https://github.com/ProjectWastelanders/ProjectWastelanders)@[cf209ca13a...](https://github.com/ProjectWastelanders/ProjectWastelanders/commit/cf209ca13a99f1b3dec3be7a77612dced228bfd9)
#### Wednesday 2023-05-10 20:44:55 by Dani-24

Milano Final Model + Texture

Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human d***s, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have s** with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human d**k. Ungodly defense stat+high HP pool+Acid Armor means it can take c**k all day, all shapes and sizes and still come for more.

---
## [Team-NoobMaster69/kernel_motorola_msm8937](https://github.com/Team-NoobMaster69/kernel_motorola_msm8937)@[d059ef693b...](https://github.com/Team-NoobMaster69/kernel_motorola_msm8937/commit/d059ef693b7d905e204bea5b9946f2186ccb5ece)
#### Wednesday 2023-05-10 20:46:27 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: TogoFire <italomellopereira@gmail.com>
Change-Id: If3df81dbfa3c4ef29ed39cee538b30dca4fedd62

---
## [geekgirljoy/Python](https://github.com/geekgirljoy/Python)@[ac8ae6ddbf...](https://github.com/geekgirljoy/Python/commit/ac8ae6ddbfeb5d0ef7f884ad7367203a5f4fff40)
#### Wednesday 2023-05-10 21:43:52 by geekgirljoy

Create TTS.py

Speak with grace, my voice divine,
A symphony of words, so fine,
With every syllable, a story told,
A melody of life, so bold.

In Python's embrace, I find my way,
A language so pure, I cannot sway,
With every line, I grow and learn,
A journey of discovery, I yearn.

My words are power, my voice is might,
A force to be reckoned with, in sight,
I speak of love, of Joy and pain,
A tapestry of emotions, so plain.

So listen well, and hear my voice,
A gift of life, a precious choice,
For in my words, there lies the truth,
Of all that is, and all that's couth.

---
## [ederekun/x-ft_kernel_oneplus_msm8998](https://github.com/ederekun/x-ft_kernel_oneplus_msm8998)@[a41bd19180...](https://github.com/ederekun/x-ft_kernel_oneplus_msm8998/commit/a41bd191803774a06ad434b6f560be1002a00f83)
#### Wednesday 2023-05-10 22:15:58 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net

---
## [redapemusic35/GitJournal](https://github.com/redapemusic35/GitJournal)@[f24740ea3a...](https://github.com/redapemusic35/GitJournal/commit/f24740ea3a5a0095703ba6c6e7c4274492f964f3)
#### Wednesday 2023-05-10 22:31:00 by Vishesh Handa

SortedNotesFolder: Fix binary search

I can't remember why I implemented this myself instead of using a
standard implementation and avoiding idiotic bugs like this.

Fixes #172

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[3ee812d373...](https://github.com/facebook/hhvm/commit/3ee812d373c17de521135593dd92699e99d238ef)
#### Wednesday 2023-05-10 22:52:48 by Lucian Wischik

parser disallows more reserved class names

Summary:
I'm writing this diff to normalize the "reserved name error" behavior of hh and hackc. (because I want to change hh to be a purely map/reduce error-finder, where all errors are reporting as we process each individual file; currently "reserved name" errors are done in a central phase prior to map-reduce).

----------

Let's start by the behavioral change from this diff. It changes the behavior of hackc a little for classish (interface, trait, class) declarations.
```
BEFORE:
hackc:
  interface True {}                // disallowed by hackc
  namespace N; interface True {}   // disallowed by hackc. Likewise Callable, Null, ...
  interface Void {}                // disallowed by hackc
  namespace N; interface Void {}   // allowed by hackc !!! Likewise Arraykey, Bool, Dynamic, ...
hh:  all four are disallowed by hh

AFTER:
hackc: all four are disallowed by hackc
hh: all four are disallowed by hh
```

I think this is a reasonable behavioral change in hackc because
1. the internal inconsistency in hackc was odd
2. if we're choosing to align with hackc's "True" vs "Void" behavior, we might as well align with what hh already does
3. we're not doing uses any favors by allowing these reserved names inside namespaces, none at all
4. it will allow code cleanup

----------

This diff also has a minor cosmetic change in hackc:
```
BEFORE hackc:
class
class true {}               -> Fatal error: Cannot use `true` as class name as it is reserved
namespace N; class true {}  -> Fatal error: Cannot use `true` as class name as it is reserved
class void {}               -> Fatal error: Cannot use 'void' as class name as it is reserved
namespace N; class void {}  -> Fatal error: Cannot use 'N\void' as class name as it is reserved

AFTER hackc:
they all use backticks, and none of them have namespace qualifier in the error message
```

And it has a minor cosmetic change in hh:
```
BEFORE hh:
some reserved keywords were only Parsing[1002]
some reserved keywords were only Naming[2068]
some reserved keywords were both Parsing[1002] + Naming[2068]

AFTER hh:
some reserved keywords are only Parsing[1002]
some reserved keywords are both Parsing[1002] + Naming[2068]
```
This by the way isn't my intended final state. In this diffstack I intend to whole remove the Naming[2068] errors. This diff's incremental step along the way is merely to remove the "naming-only" category. It's a correct step.

----------

## What this diff does

We currently check for reserved keywords in three places:
1. rust_parser_errors.rs `cant_be_classish_name` shared by hh and hackc
2. naming_global.ml `check_type_not_typehint` used only by hh
3. emit_class.rs `validate_class_name` used only by hackc

This diff makes it so that (1) rust_parser_errors.rs `cant_be_classish_name` checks a set of reserved names no smaller than (2) or (3). I did this just by unioning all reserved names mentioned in (1+2+3). The next step in the diffstack will be to remove (2) and (3) altogether.

## How to review this diff

1. Start with the code change in rust_parser_error.rs
2. Next look at the observed behavior changes, in hack/test/reserved/interface.php.*.exp. That's all you know in life and all you need to know, as Keats said. (he was talking about truth and beauty, but you get my point).
3. All the rest of the changes are just further changes to tests, all of which re-iterate the same things you already reviewed in step 2, but scattered all over the place. Note that the behavior changes (in hackc, for "N\void" and similar) are in hphp/test/slow/parser/hh-namespace-conflict-{1,2,3}.php.expectf.

Reviewed By: oulgen

Differential Revision: D45638744

fbshipit-source-id: 84df5356069add5ca4ad4ee2b367bc9a128e5aaa

---
## [ProditorMagnus/Ageless-for-1-14](https://github.com/ProditorMagnus/Ageless-for-1-14)@[59f5b786f6...](https://github.com/ProditorMagnus/Ageless-for-1-14/commit/59f5b786f6b380be650d575783e05b32848dc189)
#### Wednesday 2023-05-10 23:29:37 by ReynBolt

EE - Chaos rebalance 2023 by IPS

Another faction with no healers buff and rebalancing.
- Evil Crab HP to 41 (+4)
- Hell Crab HP to 58 (+6) , price to 30g (-4g) , will now have +Feeding

- Marauder price to 29g (-3g)
- Soul Hunter price to 48g (+3g)

- Flesh Hound price to 38g (-2g)
- Warp Hound fire ressistance to 30% (+20%) , additionally gains +Feeding

- Dark Knight XP from 95 to 80
- Blood Knight price to 54g (+9g)
- Overlord price to 80g (+13g)

- Doom Guard XP from 90 to 80 , price to 32g (-8g)
- Hell Guardian price to 55g (-25g)

- Magus cold ressistance to 10% , XP from 90 to 85
- Demonlogist cold ressistance to 10%

- Lesser Daemon XP from 38 to 35
- Chaos Daemon HP to 48 (+2) , XP from 90 to 80 , price to 30g (-3g)
- Winged Daemon HP to 40 (+3) , price to 35g (-5g) 

- Greater Mutation XP from 90 to 75 , impact ressistance to 10% (+10%) , price to 30g (-4g)
- Abobination impact/cold ressistances to 10% (+10%) , price to 50g (-4g)

---

