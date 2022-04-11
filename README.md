## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-10](docs/good-messages/2022/2022-04-10.md)


1,626,560 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,626,560 were push events containing 2,486,908 commit messages that amount to 132,720,264 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b1a793f840...](https://github.com/tgstation/tgstation/commit/b1a793f840d90131f88eabc0450e2b2b2157123e)
#### Sunday 2022-04-10 00:02:44 by Tim

Refactor and improve antimagic to be more robust (#64124)

This refactors the antimagic component to use and have bitflags, documentation, defines, code comments, named arguments, and renames variable names for clarity. 

- /obj/effect/proc_holder/spell/aoe_turf/conjure/creature/cult is not used anywhere and has been removed
- /obj/effect/proc_holder/spell/targeted/turf_teleport/blink/cult is not used anywhere and has been removed

- New sound effects are played when magic is blocked. Depending on the type of magic being used it will be either:

- Equipping antimagic now properly updates the magic buttons
- Any magic being blocked or restricting casting now displays a message
- MAGIC_RESISTANCE_MIND now properly blocks telepathy effects
- Removes blood splatter when fireball is blocked
- Magic projectiles for staff of locker no longer spawn lockers when blocked by antimagic
- Fire breath is no longer blocked by antimagic
- Spellcards are now blocked by antimagic

Any antimagic on a mob blocks that magic type from being casted. (certain spells such as mime abilities completely ignore antimagic)

- Foilhats prevent someone from casting mind magic (telepathy, mindswap, etc.)
- Bibles, ritual Totems, nullrods, holymelons, and TRAIT_HOLY prevent someone from casting unholy magic (cult spells, etc.)
- Nullrods, ritual totem, and holymelons prevent someone from casting wizard magic (fireball, magic missile, etc.)
- Immorality talismans, berserker suits, and TRAIT_ANTIMAGIC prevents all types of magic (except stuff like mime abilities)
- Touch of Madness and Mindswap is now blocked with MAGIC_RESISTANCE and MAGIC_RESISTANCE_MIND
- Voice of god is now blocked with MAGIC_RESISTANCE_HOLY and MAGIC_RESISTANCE_MIND

---
## [robertnsu/Terminal](https://github.com/robertnsu/Terminal)@[f2ebb21bd1...](https://github.com/robertnsu/Terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Sunday 2022-04-10 00:02:45 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [jogerj/place-atlas](https://github.com/jogerj/place-atlas)@[84c10997d5...](https://github.com/jogerj/place-atlas/commit/84c10997d59c3eabea7e30d51ace76b3e511510e)
#### Sunday 2022-04-10 00:03:10 by Johnyknowhow

Various duplicate removals and description edits

Removed duplicates from various artworks south of the northwest Turkish flag, edited a few descriptions to combine information/increase clarity/make it more understandable to outsiders

RIT logo
(-)twua6s - duplicate, short desc
(e)twu980 - remaining, merged into, combined descriptions

small chilean flag:
(-)txdqoq - duplicate, no desc
(-)txd2js - duplicate, outdated desc
(-)tx8o7v - duplicate, joke desc
(-)txa6ya - duplicate, troll desc
txffm2 - remaining entry

belgian flag Tintin
(e)000056 refined shape, updated title and description

canadian flag
(-)txapxq - dupe, simple entry
(-)twx0nb - dupe, doesn't mention canada, only the battle for it
(-)twp9xq - dupe, good description but twmbw6 seems better (my opinion)
(e)twmbw6 - remaining entry; good description, changed subreddit to /r/placecanada

eldenring potfriend
(-)twrfvo - dupe, good description but lacking context
(e)txysr4 - remaining entry; merged description in and added objective explanation of *what* potfriend is, edited for brevity

large chile flag/art area
(-)txaka4 - dupe, super short desc
(-)txbdl6 - dupe, not descriptive about the art
twn3qv - remaining entry, perfect description

---
## [SCScbc-Projects2022/WeathCon-project-one](https://github.com/SCScbc-Projects2022/WeathCon-project-one)@[a102b1d899...](https://github.com/SCScbc-Projects2022/WeathCon-project-one/commit/a102b1d8999f86610d550eae22e1fca82e5cfcfa)
#### Sunday 2022-04-10 00:12:02 by TOVTC

I did it. I finally got it. It took me four hours.

thank you Erik for your solution from one week ago that turned out to be the same solution that saved my code just now god this is a demon project

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[cd2bd18cf8...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Sunday 2022-04-10 01:20:20 by SkyratBot

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
## [battlecatsultimate/BCU_java_util_common](https://github.com/battlecatsultimate/BCU_java_util_common)@[f89d080b36...](https://github.com/battlecatsultimate/BCU_java_util_common/commit/f89d080b367a5cf738b70386c7e89e0ec58c83a5)
#### Sunday 2022-04-10 01:38:44 by しき中村

Fix Surge Curse bug(?)

This code sucks but it works but I hate it anyways

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[351afe260b...](https://github.com/JohnFulpWillard/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Sunday 2022-04-10 01:44:13 by san7890

Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!) (#65899)

* Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!)

Hey there,

I implore you look at this photograph right here:

Ugly stupid base broken dumb /obj instead of the actual sprite fucking garbage idiotic purple-white square damn it i hate it so much fuck fuck fuck fuck let's fix it before the fire under my seat gets worse argh

Anyways, I checked with Kapu and did a bit of testing, and I managed to figure out a way to get the best of both the mapping world and the in-game world. Don't believe me? Check these out:

* addressses review

things still work

* kills female moth chests

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[5c1e69aa44...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/5c1e69aa448e6e28738b4643a54bb104ee032555)
#### Sunday 2022-04-10 02:06:59 by SkyratBot

[MIRROR] Fixes borg wallmounting [MDB IGNORE] (#12046)

* fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

* Fixes borg wallmounting

Co-authored-by: 小月猫 <alina.r.starkova@gmail.com>

---
## [Dreaming381/Kinemation-Skinning-Prototype](https://github.com/Dreaming381/Kinemation-Skinning-Prototype)@[abd70f7fde...](https://github.com/Dreaming381/Kinemation-Skinning-Prototype/commit/abd70f7fde3d4392e2ee8213f08af036c1e30f87)
#### Sunday 2022-04-10 03:25:50 by Tyler

Refactor and Fix Shadows

Shadows were broken. Turns out that the chunk bounds can't be 1e9f but instead need to be real values. Fortunately we can calculate real and practical values while exclusively touching meta chunks. This also meant less hacks to LatiosHybridRendererSystem. But while diagnosing the issue I ended up rearranging the entire system anyways. Porting changes might be a little more painful now, but it will be much easier to work with for the next big refactor.

Also, culling stats are actually broken as they use the wrong input system. So I'm not even going to try and use that and maybe provide my own stats system instead.

---
## [iradukud/Codewars](https://github.com/iradukud/Codewars)@[c249ea61a3...](https://github.com/iradukud/Codewars/commit/c249ea61a355ab565ada16e58e7dd485c70215bd)
#### Sunday 2022-04-10 03:39:46 by David Iradukunda

Simple_Fun#1-Seats_in_Theater

Task
Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.

The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.

Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

---
## [SteelSlayer/Paradise](https://github.com/SteelSlayer/Paradise)@[6082c95eb3...](https://github.com/SteelSlayer/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Sunday 2022-04-10 03:57:07 by LightFire53

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
## [akarle/dotfiles](https://github.com/akarle/dotfiles)@[8206649651...](https://github.com/akarle/dotfiles/commit/8206649651aed66a1f87abbb04f0ecd2a54e1de4)
#### Sunday 2022-04-10 04:12:17 by Alex Karle

theme: Turn on the lights (drop NO_COLOR)

Well, I gave it a good run. I tried forcing monochrome output in most of
my apps. And while it was certainly an interesting experience of
blending everything into "pure text", I found myself maybe the tiniest
bit less effecient in finding things in output / on the screen and it
was hard to justify when pairing with teammates.

That said, going back to regular colors has also been sometimes
overwhelming, which is interesting. So many bright lights! Maybe I'll
tone down the colorscheme.

There was something really cool about "the only color you see is now
more visible". Like I used a subtle pink for syntax errors and it was
reallllly clear when my code was borked.

In the wise words of my friend Cal: "I feel like humans evolved to see
color for a reason, see color, so why not use that to our advantage?"

---
## [MehrabAgh/LastBreath](https://github.com/MehrabAgh/LastBreath)@[b64fec5e40...](https://github.com/MehrabAgh/LastBreath/commit/b64fec5e4047c4e15f01eb68a018b8e309b64959)
#### Sunday 2022-04-10 05:02:41 by Mohammad9760

Snow VFX

couldnt upload the vfx texture pack cuz my network sucks shit bitch

---
## [Lunarequest/servers-config](https://github.com/Lunarequest/servers-config)@[a0b200b80a...](https://github.com/Lunarequest/servers-config/commit/a0b200b80a9a5ebf72ab6df8f1e6ec4cc90cacf8)
#### Sunday 2022-04-10 05:47:48 by Luna D. Dragon

god damn that hardneding bull broke my server. I hate this

---
## [uShifty/qb-core](https://github.com/uShifty/qb-core)@[9d83a952c2...](https://github.com/uShifty/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Sunday 2022-04-10 06:09:58 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [erikarn/wtf-os](https://github.com/erikarn/wtf-os)@[42ced9be6a...](https://github.com/erikarn/wtf-os/commit/42ced9be6aecfed4a67d1e079c2db71d18c2dd53)
#### Sunday 2022-04-10 06:13:18 by Adrian Chadd

[stm32] [arm] update the syscall code to be a little .. better?

* drop the arg count to r0..r3 for now.  It may be interesting to
  support r4, r5 as syscall arguments and we can always add them
  back later on.
* .. because they were working by magic, not by intent.  The
  syscall code I wrote was pushing arg5, arg6 onto the stack and just
  magically had their values in r4, r5.
* .. BUT those values need to be pushed into the /kernel stack/
  before we call into the C syscall handler.

Note that the arm_m4_syscall_handler routine is getting r0..r3 from
the original exception saved state, and r8 is magically persisting
across that jump.  I .. dislike that a lot and I'm sure (a) it's wrong,
and (b) it's going to bite me.  I reckon I'm going to have to save
the original return address in the task struct or the kernel stack,
not in r8.

So, this works for now.  If I want more than 4 args then yes
I'll have to write some hacky C inline assembly stubs that will
assemble r0..r3 and then r4, r5 as syscall arguments and then
shovel them into the SVC call in the right way.  However, I still
think how r8 is being used needs to be fixed.

(This has been a fun journey figuring out the depths of the SVC
handling hacks needed for ARM!)

---
## [PestoVerde322/tgstation](https://github.com/PestoVerde322/tgstation)@[0e904f7032...](https://github.com/PestoVerde322/tgstation/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Sunday 2022-04-10 08:38:46 by LemonInTheDark

[MDB IGNORE] Moves non floor turfs off /floor. You can put lattices on lavaland edition (#65504)


About The Pull Request

Alternative to #65354

Ok so like, there was a lot of not floor types on /floor. They didn't actually want any of their parent type's functionality, except maybe reacting to breaking (which was easy to move down) and some other minor stuff.
Part of what we don't want them to have is "plateable" logic.
I should not be able to put floor tiles on the snow and be fine. It's dumb.

Instead, I've moved all non floor types down to a new type, called /misc.

It holds very little logic. Mostly allowing pipes and wires and preventing blob stuff.
It also supports lattice based construction, which is one of the major changes here. I think it makes more sense, and it fixes an assumption in shuttle code that assumed you couldn't place "a new tile" by just hitting some snow with a floor tile.
Oh and lattices don't smooth with asteroid tiles anymore, this looks nicer I think.

Moving on to commits, and minor changes

Changes clf3 to try and burn any turfs it's exposed to, instead of just floors
Moves break_tile down to the turf definition, alongside burn_tile
If you're in basic buildmode and click on anything that's not handled in a targeted way, you just build plating
FUNCTION CHANGE: you can't use cult pylons to convert misc tiles over anymore
Generalizes building floors on top of something into two helper procs on /turf/open, reducing copypasta
Adds a new turf flag, IS_SOLID, that describes if a turf is tangible or not.
Uses this alongside a carpet and open check to replace plating and floor checks in carpet code. This does mean that non iron tiles can be carpeted, but I think that's fine

Moves the /floor update_icon -> update_visuals call to /open
This change is horrificly old, dating back to 8e112f6 but that commit describes nothing about why it was done. Choosing to believe it was a newfriend mistake. Uncomfortable nuking it though, because of just how old it is. Moving down instead

Create a buildable "misc" type off open, moves /dirt onto it
Basically, we want a type we can use to make something support
construction, since that can be a messy bit of logic. Also enough
structure to set things up sanely.

I'm planning on moving most misc turfs onto it, if only because
constructing on a dirt tile with rods should be possible, and the same
applies to most things

Murders captain planet, disentangles /turf/open/floor/grass/snow/basalt

Adds a diggable component that applies the behavior of "digging"
something out from a turf.

Uses it to free the above pain typepath into something a bit more
sensible

The typepaths that aren't actually used by floor tiles are moved onto
/misc

The others are given names that better describe them, and kept in
fancy_floor

Oh and snowshoes don't work on basalt anymore, sorry

Snowed over platings now actually have broken/burned icon states, fixing black holes to nowhere

Misc turfs no longer smooth as floors, so lattices will ignore them

Placing a lattice will no longer scrape the tile it's on

Ok this is a really old one.
I believe this logic is a holdover from kor's baseturf pr
(97990c9)
It used to be that turfs didn't have a concept of "beneath" and instead
just decided what should be under them by induction. This logic of "if
it's being latticed scapeaway to space" made sense then, but has since
been somewhat distorted

We do want to scape away on lattice spawn sometimes, mostly when we're
being destroyed, but not always. We especially don't want to scape away
if someone is just placing a rod, that's dumb.

Adds a path updating script for this change

I've done my best to find all the errors this repathing will pull out, but I may have missed some. I'm sorry.
Why It's Good For The Game

Very old code made better, more consistent turfs for lavaland and icebox, better visuals, minor fix to snowed plating, demon banishment in lattice placement, fixes the icebox mining shuttle not being repairable
Changelog

cl
add: Rather then being tileable with just floor tiles, lavaland turfs, asteroid and snow (among other things) now support lattice -> floor tile construction
fix: Because of the above, you can now properly fix the icebox mining shuttle
refactor: Non floor turfs are no longer typed as floor. This may break things, please yell at me if it does
/cl

---
## [fdiedler/EasyAdminBundle](https://github.com/fdiedler/EasyAdminBundle)@[f3a4b13382...](https://github.com/fdiedler/EasyAdminBundle/commit/f3a4b13382f6d96f85b0b1d8dfe329f40a39d32c)
#### Sunday 2022-04-10 08:57:36 by Javier Eguiluz

minor #5139 Disable UX-Turbo (Lustmored)

This PR was merged into the 4.x branch.

Discussion
----------

Disable UX-Turbo

In all my projects with EasyAdmin I am sharing Stimulus controllers between EasyAdmin and frontend (I need them sometimes and it's just simpler). Since enabling Turbo on some projects I need to overwrite EasyAdmin layout just to disable it.

Currently EA is very unfriendly towards Turbo - there are JavaScripts in body, DOMContentLoaded listeners and so on. Refactoring everything to be turbo-compatible would be titanic effort with little benefit (it's not really needed in CRUD dashboards in my opinion), while adding this single attribute will make life easier for probably more consumers than just myself :)

Commits
-------

735b2397 Disable UX-Turbo

---
## [SingingSpock/Skyrat-tg](https://github.com/SingingSpock/Skyrat-tg)@[b995fbe31b...](https://github.com/SingingSpock/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Sunday 2022-04-10 09:04:13 by Zonespace

Contractor Expansion 2 (#12311)

* weh!

* fuck you linter

* very important

* Update modular_skyrat/modules/contractor/code/datums/midround/event.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Update modular_skyrat/modules/contractor/code/datums/midround/outfit.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* requested changes

* also this

* requested + cleanup

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [fajar3109/kernel_xiaomi_ginkgo](https://github.com/fajar3109/kernel_xiaomi_ginkgo)@[a8c692d951...](https://github.com/fajar3109/kernel_xiaomi_ginkgo/commit/a8c692d9511c2f20e05fc294a3292474a2803855)
#### Sunday 2022-04-10 09:34:59 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [linuxppc/linux](https://github.com/linuxppc/linux)@[53a05ad9f2...](https://github.com/linuxppc/linux/commit/53a05ad9f21d858d24f76d12b3e990405f2036d1)
#### Sunday 2022-04-10 12:32:17 by David Hildenbrand

mm: optimize do_wp_page() for exclusive pages in the swapcache

Patch series "mm: COW fixes part 1: fix the COW security issue for THP and swap", v3.

This series attempts to optimize and streamline the COW logic for ordinary
anon pages and THP anon pages, fixing two remaining instances of
CVE-2020-29374 in do_swap_page() and do_huge_pmd_wp_page(): information
can leak from a parent process to a child process via anonymous pages
shared during fork().

This issue, including other related COW issues, has been summarized in [2]:

 "1. Observing Memory Modifications of Private Pages From A Child Process

  Long story short: process-private memory might not be as private as you
  think once you fork(): successive modifications of private memory
  regions in the parent process can still be observed by the child
  process, for example, by smart use of vmsplice()+munmap().

  The core problem is that pinning pages readable in a child process, such
  as done via the vmsplice system call, can result in a child process
  observing memory modifications done in the parent process the child is
  not supposed to observe. [1] contains an excellent summary and [2]
  contains further details. This issue was assigned CVE-2020-29374 [9].

  For this to trigger, it's required to use a fork() without subsequent
  exec(), for example, as used under Android zygote. Without further
  details about an application that forks less-privileged child processes,
  one cannot really say what's actually affected and what's not -- see the
  details section the end of this mail for a short sshd/openssh analysis.

  While commit 17839856fd58 ("gup: document and work around "COW can break
  either way" issue") fixed this issue and resulted in other problems
  (e.g., ptrace on pmem), commit 09854ba94c6a ("mm: do_wp_page()
  simplification") re-introduced part of the problem unfortunately.

  The original reproducer can be modified quite easily to use THP [3] and
  make the issue appear again on upstream kernels. I modified it to use
  hugetlb [4] and it triggers as well. The problem is certainly less
  severe with hugetlb than with THP; it merely highlights that we still
  have plenty of open holes we should be closing/fixing.

  Regarding vmsplice(), the only known workaround is to disallow the
  vmsplice() system call ... or disable THP and hugetlb. But who knows
  what else is affected (RDMA? O_DIRECT?) to achieve the same goal -- in
  the end, it's a more generic issue"

This security issue was first reported by Jann Horn on 27 May 2020 and it
currently affects anonymous pages during swapin, anonymous THP and hugetlb.
This series tackles anonymous pages during swapin and anonymous THP:

 - do_swap_page() for handling COW on PTEs during swapin directly

 - do_huge_pmd_wp_page() for handling COW on PMD-mapped THP during write
   faults

With this series, we'll apply the same COW logic we have in do_wp_page()
to all swappable anon pages: don't reuse (map writable) the page in
case there are additional references (page_count() != 1). All users of
reuse_swap_page() are remove, and consequently reuse_swap_page() is
removed.

In general, we're struggling with the following COW-related issues:

(1) "missed COW": we miss to copy on write and reuse the page (map it
    writable) although we must copy because there are pending references
    from another process to this page. The result is a security issue.

(2) "wrong COW": we copy on write although we wouldn't have to and
    shouldn't: if there are valid GUP references, they will become out
    of sync with the pages mapped into the page table. We fail to detect
    that such a page can be reused safely, especially if never more than
    a single process mapped the page. The result is an intra process
    memory corruption.

(3) "unnecessary COW": we copy on write although we wouldn't have to:
    performance degradation and temporary increases swap+memory
    consumption can be the result.

While this series fixes (1) for swappable anon pages, it tries to reduce
reported cases of (3) first as good and easy as possible to limit the
impact when streamlining.  The individual patches try to describe in
which cases we will run into (3).

This series certainly makes (2) worse for THP, because a THP will now
get PTE-mapped on write faults if there are additional references, even
if there was only ever a single process involved: once PTE-mapped, we'll
copy each and every subpage and won't reuse any subpage as long as the
underlying compound page wasn't split.

I'm working on an approach to fix (2) and improve (3): PageAnonExclusive
to mark anon pages that are exclusive to a single process, allow GUP
pins only on such exclusive pages, and allow turning exclusive pages
shared (clearing PageAnonExclusive) only if there are no GUP pins.  Anon
pages with PageAnonExclusive set never have to be copied during write
faults, but eventually during fork() if they cannot be turned shared.
The improved reuse logic in this series will essentially also be the
logic to reset PageAnonExclusive.  This work will certainly take a
while, but I'm planning on sharing details before having code fully
ready.

#1-#5 can be applied independently of the rest. #6-#9 are mostly only
cleanups related to reuse_swap_page().

Notes:
* For now, I'll leave hugetlb code untouched: "unnecessary COW" might
  easily break existing setups because hugetlb pages are a scarce resource
  and we could just end up having to crash the application when we run out
  of hugetlb pages. We have to be very careful and the security aspect with
  hugetlb is most certainly less relevant than for unprivileged anon pages.
* Instead of lru_add_drain() we might actually just drain the lru_add list
  or even just remove the single page of interest from the lru_add list.
  This would require a new helper function, and could be added if the
  conditional lru_add_drain() turn out to be a problem.
* I extended the test case already included in [1] to also test for the
  newly found do_swap_page() case. I'll send that out separately once/if
  this part was merged.

[1] https://lkml.kernel.org/r/20211217113049.23850-1-david@redhat.com
[2] https://lore.kernel.org/r/3ae33b08-d9ef-f846-56fb-645e3b9b4c66@redhat.com

This patch (of 9):

Liang Zhang reported [1] that the current COW logic in do_wp_page() is
sub-optimal when it comes to swap+read fault+write fault of anonymous
pages that have a single user, visible via a performance degradation in
the redis benchmark.  Something similar was previously reported [2] by
Nadav with a simple reproducer.

After we put an anon page into the swapcache and unmapped it from a single
process, that process might read that page again and refault it read-only.
If that process then writes to that page, the process is actually the
exclusive user of the page, however, the COW logic in do_co_page() won't
be able to reuse it due to the additional reference from the swapcache.

Let's optimize for pages that have been added to the swapcache but only
have an exclusive user.  Try removing the swapcache reference if there is
hope that we're the exclusive user.

We will fail removing the swapcache reference in two scenarios:
(1) There are additional swap entries referencing the page: copying
    instead of reusing is the right thing to do.
(2) The page is under writeback: theoretically we might be able to reuse
    in some cases, however, we cannot remove the additional reference
    and will have to copy.

Note that we'll only try removing the page from the swapcache when it's
highly likely that we'll be the exclusive owner after removing the page
from the swapache.  As we're about to map that page writable and redirty
it, that should not affect reclaim but is rather the right thing to do.

Further, we might have additional references from the LRU pagevecs, which
will force us to copy instead of being able to reuse.  We'll try handling
such references for some scenarios next.  Concurrent writeback cannot be
handled easily and we'll always have to copy.

While at it, remove the superfluous page_mapcount() check: it's
implicitly covered by the page_count() for ordinary anon pages.

[1] https://lkml.kernel.org/r/20220113140318.11117-1-zhangliang5@huawei.com
[2] https://lkml.kernel.org/r/0480D692-D9B2-429A-9A88-9BBA1331AC3A@gmail.com

Link: https://lkml.kernel.org/r/20220131162940.210846-2-david@redhat.com
Signed-off-by: David Hildenbrand <david@redhat.com>
Reported-by: Liang Zhang <zhangliang5@huawei.com>
Reported-by: Nadav Amit <nadav.amit@gmail.com>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Cc: Hugh Dickins <hughd@google.com>
Cc: David Rientjes <rientjes@google.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Jason Gunthorpe <jgg@nvidia.com>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Mike Rapoport <rppt@linux.ibm.com>
Cc: Yang Shi <shy828301@gmail.com>
Cc: Kirill A. Shutemov <kirill.shutemov@linux.intel.com>
Cc: Jann Horn <jannh@google.com>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Roman Gushchin <roman.gushchin@linux.dev>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Don Dutile <ddutile@redhat.com>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Jan Kara <jack@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [projects-nexus/android_kernel_xiaomi_gauguin](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin)@[f2c05578b3...](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin/commit/f2c05578b3b4aec7117845f6a70e325eacf99885)
#### Sunday 2022-04-10 12:50:17 by Wang Han

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
## [Lovebird-Frungy/Yogstation](https://github.com/Lovebird-Frungy/Yogstation)@[c75c75d899...](https://github.com/Lovebird-Frungy/Yogstation/commit/c75c75d899e32f2bebcf0e48797c18ce00812989)
#### Sunday 2022-04-10 13:46:03 by UselessTheremin

fixes light pink pylons giving no warning for lightgeistification (ruined poor phillip's round very sad) (#12907)

* Update _structures.dm

* Update _structures.dm

* Update _structures.dm

* Update _structures.dm

* honestly fuck you

* Update colossus.dm

* Update colossus.dm

* Update colossus.dm

* Update colossus.dm

---
## [raziel100/duckstation](https://github.com/raziel100/duckstation)@[f9212363d3...](https://github.com/raziel100/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Sunday 2022-04-10 14:44:43 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [FlyingBBQ/dwm](https://github.com/FlyingBBQ/dwm)@[67d76bdc68...](https://github.com/FlyingBBQ/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-04-10 15:17:01 by Chris Down

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
## [hawkw/mycelium](https://github.com/hawkw/mycelium)@[2bfe554046...](https://github.com/hawkw/mycelium/commit/2bfe5540460b18c3de399179297c4439a803dbcb)
#### Sunday 2022-04-10 16:02:59 by Eliza Weisman

fix(x86_64): unfuck interrupt stack frames (#148)

It turns out that the reason we've been seeing extremely spooky behavior
in interrupt handlers, especially when trying to disassemble at `[rip]`,
is because LOL ELIZA FUCKED UP THE REGISTERS LOL LMAO.

When an interrupt occurs, a number of registers are pushed to the stack
frame for the interrupt handler. This includes the instruction pointer,
stack pointer, and the code and stack segment selectors. We defined a
`Registers` struct that consists of named fields for these registers, in
the correct order. However, because I'm a **loser fucking idiot**, the
current x86_64 ISRs were accidentally taking an `&mut Registers` rather
than a `Registers`. This meant we were interpreting the first 64 bits of
the registers (which I believe was the zero-padded 16-bit `ss` stack
segment selector) as a *pointer*, and reading the "register" values from
`[ss]`. This results in garbage.

And, when we tried to use `yaxpeax` to disassemble `[rip]`...`[rip +10]`
in the oops handler, we followed the "`rip`" from the location
pointed to by the stack segment selector, which was usually not pointing
at anything good. Thus, disassembly would always fault.

This branch fixes the ISR prototypes to take the registers by value, and
puts back `yaxpeax` disassembly.

Signed-off-by: Eliza Weisman <eliza@elizs.website>

---
## [Abdykadyrrov/gameoflife](https://github.com/Abdykadyrrov/gameoflife)@[42321ee1cb...](https://github.com/Abdykadyrrov/gameoflife/commit/42321ee1cb68784a1c172775bc0193aa1edc8286)
#### Sunday 2022-04-10 16:50:57 by Abdykadyrrov

nnxn

This game is based on the game of life. It shows how humanity multiplies. 
The blue cells are male individuals, and the pink ones are female, respectively.

In the game, 4 cells of random color are randomly created, then the program reads the cells and stops when it finds blue cells, after which the program reads the cells located in the neighboring blue cells for the presence of pink cells. When the blue and pink cells touch, 4 more random-colored cells are generated in neighboring cells, and the old cells die. The game continues as long as the cells remain, let's say, without their pair, thereby ending the kind of life.

---
## [merenlab/anvio.org](https://github.com/merenlab/anvio.org)@[1d2a69daa3...](https://github.com/merenlab/anvio.org/commit/1d2a69daa391be2ff61b9cca15a527a1a6af5685)
#### Sunday 2022-04-10 16:58:45 by A. Murat Eren

going back to 3.7 due to STUPID SH*T FC*K REASONS

There is no conda package for Bowtie2 compatible with Python 3.10,
so basically we have to go all the way back to Python 3.7. This is
ridiculous and frustrating. The year made it all the way to 2022
but we are stuck in middle ages.

---
## [anhaeyeong/GameGraphicProgramming_2018102117_HaeyoungAn](https://github.com/anhaeyeong/GameGraphicProgramming_2018102117_HaeyoungAn)@[946e34e7d1...](https://github.com/anhaeyeong/GameGraphicProgramming_2018102117_HaeyoungAn/commit/946e34e7d10f6526ca10785641a0a97920e39169)
#### Sunday 2022-04-10 19:36:38 by anhaeyeong

[ASS01]

fuck ggp fuck you fuck man fucking tomboy

---
## [the-unidentified-anomalous-baguette/DOOMnt](https://github.com/the-unidentified-anomalous-baguette/DOOMnt)@[a456782c5f...](https://github.com/the-unidentified-anomalous-baguette/DOOMnt/commit/a456782c5f3859b999fa75ec3fbcb4086fa28a9e)
#### Sunday 2022-04-10 20:00:10 by the-unidentified-anomalous-baguette

lotsa half finished shite

Do you hear the flibbity jibbity jibber jabber
With an, "Oh my God, I've got to get out of here or I'll have another
Word to sell, another story to tell
Another time piece ringing the bell"
Do you hear the clock stop when you reach the end?
No, you know it must be never ending, comprehend if you can
But when you try to pretend to understand
You resemble a fool although you're only a man
So give it up and smile

---
## [MacBlaze1/tgstation](https://github.com/MacBlaze1/tgstation)@[54403a1ca0...](https://github.com/MacBlaze1/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Sunday 2022-04-10 20:06:28 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [Zeioth/wofi-calc](https://github.com/Zeioth/wofi-calc)@[ae2552c96a...](https://github.com/Zeioth/wofi-calc/commit/ae2552c96a3eddcc8a98da157d230159510dcae6)
#### Sunday 2022-04-10 20:15:46 by Zeioth

From now on the main branch is master to avoid conflicts between AUR and GitHub.

This shit made me lose two hours of my day.
Fuck Microsoft and fuck every single of
their fucking executives.

---
## [Physolia/julia](https://github.com/Physolia/julia)@[62e0729dbc...](https://github.com/Physolia/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Sunday 2022-04-10 20:45:09 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [akitum/surge](https://github.com/akitum/surge)@[e6f4ffaef9...](https://github.com/akitum/surge/commit/e6f4ffaef9d6f3222749fcf0d86a37063130a36e)
#### Sunday 2022-04-10 20:49:46 by Paul

Doubleclick Renamed Modulators without annoying bug (#6024)

Doubleclick renames a modulator. Cool

But this kinda sucks if you click into a modulator and then click to arm
quickly and misfire a double click

So if you have *just* selected a modulator the double click doesn't work.

Only after that

Closes #5774

---
## [SagaraBattousai/falcie](https://github.com/SagaraBattousai/falcie)@[03bbebeb73...](https://github.com/SagaraBattousai/falcie/commit/03bbebeb73542dfed3e47aa9124b14bb378ddda6)
#### Sunday 2022-04-10 20:53:21 by James Calo

Code cleaned up, Forget all that C/C++ stuff, I have been thinking about it all day and literally cannot stop thinking about it!!!!! I need to just chill out and stick with GO. Once I have a working system I can then be pedantic but at the moment I have no time and this is seriously not that important, I just hate not haveing full controll and hate garbage collection and no pointer aritmentic #NoXORLists :'(

---
## [Avensen/Stockfish](https://github.com/Avensen/Stockfish)@[cb9c2594fc...](https://github.com/Avensen/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Sunday 2022-04-10 21:59:29 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [j4james/terminal](https://github.com/j4james/terminal)@[855e1360c0...](https://github.com/j4james/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Sunday 2022-04-10 22:01:07 by Mike Griese

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

---
## [DartIkari/HyperGoo-Station-13](https://github.com/DartIkari/HyperGoo-Station-13)@[5d96c13de2...](https://github.com/DartIkari/HyperGoo-Station-13/commit/5d96c13de288fd1d735a392ceffd991d7ecc17f2)
#### Sunday 2022-04-10 22:14:44 by sarcoph

holy fucking shit i am so tired of refactoring

to do list:
- ensure all useBackends use context instead of props
- ensure all uis that need it get their `{ act, data, config }` from useBackend(context)
- fix the rest of the bugs

i do not have the energy for this.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b73fd3f835...](https://github.com/mrakgr/The-Spiral-Language/commit/b73fd3f8359d0d8e1eb3557c8ff978a94f2970fe)
#### Sunday 2022-04-10 22:25:00 by Marko Grdinić

"11:05pm. I am up. Let me read the Satanophany chap and I will get started. I could have gotten up earlier, but I've decided to lounge in bed instead. Today I'll deal with the desk.

11:20am. Let me start.

11:25am. Touched up on of the sides. Some of the wear damage that I did was simply too rough so I smoothed out the edges a bit.

Now let me do the wood pattern on the sides.

11:45am. Fuck!

Painter is fine for painting, but even though it has the nodes, making the wood patterns that I want is impossible! Goddamit.

Like yesterday, I am struggling so much today with just these simple things. This would be so much easier in Designer. So why don't I do it there?

Nevermind the cost for all these programs which is 50$ a month. I'll just get it when I can afford it. So what if I end up shelling out 2k per year for all the software packages.

11:50am. I'll consider this a lesson. From now I'll work on patterns in Designer. Painter is not suitable for it.

I'll have to go to that tutorial and focus on it.

12:30pm. Sigh, what the hell, why can't I update the resource?

It won't do it automatically. I need to drag the sbsar file by hand. The resource updates will only allow me to update after that. Lame.

Where is the hot reloading?

https://youtu.be/Zh6MxVW-VSk
Using the Resource Updater in Substance Painter

Let me watch this.

https://youtu.be/Zh6MxVW-VSk?t=346

This is pretty interesting. You can actually update the individual brush strokes.

1:25pm. Done with the desk. I did not even watch the video in full yet, I'll do that after the break.

2:20pm. Done with breakfast. Let me catch up with Bai Ji's adventure and then I'll do the chores. After that I'll think of what comes next.

3:05pm. Done catching up with Blood Princess.

4pm. Let me resume. I overdid it with the break, but now I can finally get rolling again.

Let me complain about something. I want to get started with the music studies, but I can't just yet.

Yesterday I had some good tunes in my head, but music memory being what it is, it faded from my memory and I can't recall how it goes today. Since it is music I can't really reason it out either. I am just left with a feeling of being unable to recall a memory. I hate this. Had I music skills I would have been able to write some of it down to help me recall.

4:05pm. Now the desk. I wanted to merge some of the texture sets in order to lessen the memory burden.

While Painter can reproject when the UVs change, since the layers are associated to texture sets, I am not sure I'll be able to change those. If I did, I'd probably lose all the work that I did so far.

I should have gone with the UDIM workflow. If I did, I'd have a single texture set for the whole object, just with different tiles. I am going to have to study that for me next prop.

Now, let me finish those resource updates videos from earlier. Then I'll post a screenshot or two in the /3/ thread.

https://youtu.be/Zh6MxVW-VSk?t=645

He has his own shelf and as a result the updater looks at the files where they are on the hard drive to see if they are out of date. When I just add the resources to the folder that does not happen.

Ok, now what about the other video?

https://youtu.be/bgquP-teXd0
5 things you didn’t know about in Substance Painter

It was this one.

https://youtu.be/bgquP-teXd0?t=16

The first time is how to add a custom shelf. Exactly what I've been wondering about!

https://youtu.be/bgquP-teXd0?t=64

Hmmm, this would be a good way of doing it.

4:30pm. https://cgpersia.com/2022/03/blendermarket-bundle-1-mar-2022-183250.html

Found it. Here is the UV Packmaster for Blender.

Still...how do I deal with texel densities and stuff like that...

I guess I'll just eyeball the checker texture. It is not biggie.

4:40pm. I browsed CG Persia's two years of Blender entries. The only plugin that caught my eye was Scatter, but I do not need it right now. It is not like Blender will support volume on the level of Clarisse anyway. I am not going to bother going in this direction.

UV Packmaster on the other hand will be a pure gain with no downsides over Blender's inbuilt capabilities. I'll make use of it for the next prop, but the way I have done things currently with every object being its own texture set would get any benefit from it.

To review the desk, I made a huge mistake using separate texture sets.

I need to figure out the UDIM workflow for all the next assignment.

But, even though it is inefficient, there is no reason to be ashamed of what I've done here.

I might want to make heavier use of Designer in the future though as drawing things with the brush leads to huge file sizes for some reason. It is not as huge as last time due to me not baking positional maps, but it is still 220mb which is ridiculuos. Probably because I've been using different random seeds for each stamp.

...Still, if I assume that it stores every stamp individually, storing an extra random value for the seed should not be too much of a burden.

So I won't worry about it.

5:50pm. Nevermind the desk for now. I'll import it into the scene and set it up later.

Right now, let me get started on some things I wanted to do for a while. I want to watch the chair tutorial by Blender Guru. I am interested in the workflow he took. After that, I am also interested in going through the procedural texturing course by Shrimp. I downloaded it a while ago.

After that I'll want to look into MaterialX in Designer. I am interested in how it would work. Textures have poor scaling, and on future hardware, I think I'd want to do all my texturing procedurally.

https://vimeo.com/349801935
Houdini 4D

What are 4d models. Let me start with this. Then I'll go into the chair vids.

6:20pm. https://www.youtube.com/watch?v=Hf2esGA7vCc&list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR

Let me watch some of this. Obviously it is really long so I'll be skimming it.

https://youtu.be/Hf2esGA7vCc?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=210

I remember him talking about finding branded props and the blueprints for them in the previous video. I completely forgot about that until he reminded me just now.

https://youtu.be/VNjZ0UDnv9Y
How to Fix Pen Pressure in Substance Painter

https://youtu.be/uzPWpoOqIRg
Easy Switching to Blender from Other 3D Software

Right now I am watching this. Let me just follow my interests. Who is going to start work on an another prop right now.

5m is enough. Let me go back to the chair vid.

6:55pm. https://www.youtube.com/results?search_query=blender+udim

https://youtu.be/Z3PwX1K9KDY
Udims in Blender to Substance Painter and Back Again

This video is very much in my interest.

I'll watch it later.

https://youtu.be/AP5CTAKckBI?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=687

Loop cuts are just bad. He should be using creases here.

7:05pm. I am not a fan of subsurf workflows. Not that I've done them much, but I think they'd be hard to deal with. If I had to do that back thing, I use bevels instead.

https://youtu.be/7xASHmUs7sU?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=193

I hadn't known about Ctrl + Alt + Q.

I'll have to remember this. It split the main view into the main + 3 orthogonal ones.

It is little things like this that I learn while watching the vids at random.

https://youtu.be/7xASHmUs7sU?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=291

I had no idea bout the even mode either.

7:20pm. I just figured out what poke faces does. It triangulates them, except it works well for Ngons instead of reating a huge mess.

7:30pm. No, I was wrong. Watching the video made me interested in how I would model the backrest.

7:35pm. I was wrong about the subdivision modifier. I should be in fact using it to do beveling. Subdivision essentially turns regular poly modeling into quasi curve modeling which is good.

I tried making the backrest by beveling the corners and that cause a huge issue with the main faces being ngons. It is fine if you intend to leave them flat, but if you put a loop cut in the middle and then try dragging that, they'll stop being planar.

Instead to make the backrest, you put two loop cuts down the middle, bevel those to get some extra geometry near the edges (this would not make them ngons), and then put a subdiv modifier.

This gives you nice beveled corners.

Then if you want to curve the backrest you just turn on proportional editing and drag it along the x axis. Piece of cake.

I did run into issue with bevels when working on the desk. Had I been trying to make a subdiv workflow work, I might have an easier time.

It would have resulted in more geometry, but who cares about that.

7:55pm. Had to leave for lunch.

I keep thinking about that desk piece which gave me so much trouble. There is definitely a case for taking a subsurf approach to that and not have to worry about mesh shearing and whatnot afterwards.

Let me leave that aside. I want to watch more of the chair tutorial.

https://youtu.be/7xASHmUs7sU?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=452

Holy shit! It is possible to move in the opposite direction!

I've tried this in the past and could not figure out how.

> You know, I've been using Blender for what? 15 years? And I've discovered it (two hours ago.)

8:15pm. As expected the Decimate modifier has a planar option. I can use that to get rid of planar polygons.

8:20pm. Creases in Blender do not work the same way as in Houdini. In Blender they are straight 0-1.

If I start with a cube, and put a crease on one of the faces I can use subdivide to make a half sphere.

I playing with that because I have some issue with the Decimate modifier. I can't see the small angle, but the modifier can and without the crease the planar quads won't be planar enough in the place I want to remove them.

8:25pm. No, there isn't much difference either way. If I put in 0 or even something like 0.01 or 0.03 it does not decimate the flat top of that sphere properly. You need something like 0.1 to get good results.

I've never had good results with the decimate modifier before, but on semi-hard surfaces this plan works really well. I am impressed. On the backrest it cuts the number of faces in half without any loss in visual quality. It does introduce ngons, but who care about those.

To me, this makes the subsurf workflow a lot more effective. I'll consider it instead of the bevel one.

Oh yes. there is an option to delimit merging by UV seams. If I turn that on, I won't have to worry about decimation messing up UVs.

And there is an option for UVs to do their unwrapping after applying the mods.

I see, I see...

Surprisingly, I gained a lot from the chair tutorial.

Let me get back to it.

9:45pm. https://youtu.be/KzA5fOIq8Qw?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=276

I didn't know that Shift + E allow you to modify the edge creases.

https://youtu.be/KzA5fOIq8Qw?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=333

He says he does not use creases because he needs edge loops to give geometry for the bevel. Reasonable. Still it would be good to have creases for those edge faces.

https://youtu.be/KzA5fOIq8Qw?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=360

Instead of doing them separately, he really should just put one down the middle and then bevel it. That would make sure they are equal distance from both corner edges.

https://youtu.be/KzA5fOIq8Qw?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=735

> Instead of holding Alt, somebody in the comments said you can press C once and it turns that on or off.

Useful to know.

https://youtu.be/XeBUfMKKZDo?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR
> Now that we've finished the modeling, the real fun can be begin - UV unwrapping! Some people get excited by lighting, rendering and other people will get excited about UV unwrapping. And those people areee - psychopaths!

Kek.

The delivery of this joke was so good.

10:25pm. Yeah, I've been using the wrong thing - subdiv modifiers perfectly preserve the UV seams while bevels wreck them. I've been using the wrong thing for bevels the entire time.

10:30pm. As expected Decimate respects edge seams. Perfect.

10:45pm. https://youtu.be/zJ_AoS7wojk?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR
Blender Beginner Modeling Chair Tutorial - Part 8: Texture Mapping

Since I am into it so much, I might as well watch it all the way to the end.

https://youtu.be/zJ_AoS7wojk?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=171

How is he selecting it so fast? Is there some trick to get it to select the shortest path? Maybe he use just selecting edge loops. I am not sure.

https://youtu.be/zJ_AoS7wojk?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=282

Yeah, selecting by sharp edges occured to me.

https://youtu.be/zJ_AoS7wojk?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=369

Oh, the designer chair site tells me exactly what material are used on the chair.

https://youtu.be/zJ_AoS7wojk?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=670

Agh, why didn't I think of this.

...Probably because for the problems I had, it would't have helped me.

11:25pm. https://youtu.be/W1px5mPdN4s?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR
Blender Beginner Modeling Chair Tutorial - Part 9: Finale!

Time for the final part. I am a bit confused as I clearly remmeber his render having wear on the texture rather than being a flat one off texture.

I was really curious how he would do that in Blender, and I am guessing the answer is that he wouldn't.

https://youtu.be/W1px5mPdN4s?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=1306

Actually, I had no idea that you could just append collections like this.

Also I had no idea that you can deduplicate objects by linking object data.

11:55pm. Ok, good. I am done for the day.

Watching these tutorials gives me a lot more motivation to do the rest of the props. I want to try out the new workflow. Had I known what I had learned today, I'd have used the subdiv workflow for the desk as it would have been far easier than the bevel one.

Even though I knew what subdiv was, I didn't really get it.

That is what my lack of experience gets me. Just what did I spend the last six and a half months doing? I have no idea.

It feels so easy now. I am watching that guy work and thinking - I can do the same thing.

It really was worth watching despite being a beginner series as I learned some good tricks.

I have a good feelings about this.

Tomorrow, I will study up on UDIM workflows and then get started on the rest of the props. There are a couple of them in the room. By the time I am done I should have build up my modeling and texturing foundation.

12:15pm. I couldn't get that limbo scene done, so something simple like this will have take its place.

The difficulty will ramp up quickly after that. It really won't be long until I start working on whole cities.

It is not as big of deal as it seems. Making a big building is not that much harder than making a desk. It might even be easier.

It all depends on how distant something is from the camera and the amount of detail I want to put in. A building for example is just a bunch of boxes stacked on top of each other. Add some scattering tricks and I can get a lot of variation for cheap.

This is why I got excited for Houdini's scattering capabilities and later Clarisse.

I made a mistake not thinking more deeply about subdiv as a way of working, but that has been fixed today. Experience builds on itself, today for example I only thought of planar decimation because I learned what planar ngons were in Houdini. I thought the modifier might have it and it did.

I will keep going like this.

3/5 - I will reach this general art level in the next few months."

---
## [beefpatty8888/furry-broccoli](https://github.com/beefpatty8888/furry-broccoli)@[a8f91e367c...](https://github.com/beefpatty8888/furry-broccoli/commit/a8f91e367c8eada4e6fb5a1dbda6d755ce4655a8)
#### Sunday 2022-04-10 22:57:34 by jack

Some corrections on typos and formatting to correct the links.
Whoops. "git rebase" to rewrite history in 3..2..1. Oh no, my
conscience got in the way! Darn morality, darn ethics. They get
in the way of doing evil stuff like rewriting history.

---

