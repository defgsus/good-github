## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-10](docs/good-messages/2022/2022-05-10.md)


1,768,462 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,768,462 were push events containing 2,879,245 commit messages that amount to 215,158,956 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[27946f516d...](https://github.com/timothymtorres/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Tuesday 2022-05-10 00:18:17 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[cd1b891d79...](https://github.com/GoblinBackwards/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Tuesday 2022-05-10 00:30:59 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[fb5cf9102e...](https://github.com/EdwardNashton/mojave-sun-13/commit/fb5cf9102e3f942b3b47e985a4dc19d671932b3e)
#### Tuesday 2022-05-10 00:40:29 by LemonInTheDark

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
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[52dbce8997...](https://github.com/YakumoChen/Skyrat-tg/commit/52dbce8997f420c803197faf0aa38ee36c93246e)
#### Tuesday 2022-05-10 00:49:15 by SkyratBot

[MIRROR] Improper forced qdel cleanup,  some expanded del all verbs [MDB IGNORE] (#13384)

* Improper forced qdel cleanup,  some expanded del all verbs (#66595)

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

Co-authored-by: Seth Scherer <supernovaa41@ gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@ gmx.com>

* Improper forced qdel cleanup,  some expanded del all verbs

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Seth Scherer <supernovaa41@ gmx.com>

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[9fbcb32a6d...](https://github.com/Koshenko/mojave-sun-13/commit/9fbcb32a6d72113b5ac781a61c5a6e12a47ebf5f)
#### Tuesday 2022-05-10 00:49:45 by tralezab

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
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[98f32035d8...](https://github.com/Pickle-Coding/tgstation/commit/98f32035d8dbd6b925700e9934652d03739f024b)
#### Tuesday 2022-05-10 01:07:56 by LemonInTheDark

Parallax but better: Smooth movement cleanup (#66567)

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

---
## [PikrlRealForReal/fnf-scratch-stuffs](https://github.com/PikrlRealForReal/fnf-scratch-stuffs)@[a7a14c101c...](https://github.com/PikrlRealForReal/fnf-scratch-stuffs/commit/a7a14c101c29964eb5efdbf194a479a977675b08)
#### Tuesday 2022-05-10 01:08:58 by PikrlRealForReal

HOW THE FUCK DO I ADD FOLDERS GITHUB!!

i hate myself

---
## [Kapu1178/Pariah-Station](https://github.com/Kapu1178/Pariah-Station)@[95db2c6bfc...](https://github.com/Kapu1178/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Tuesday 2022-05-10 01:48:27 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [RealHeart/Grasscutter](https://github.com/RealHeart/Grasscutter)@[fbaeaee4b5...](https://github.com/RealHeart/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Tuesday 2022-05-10 05:10:48 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [Raines333/corporate-America-](https://github.com/Raines333/corporate-America-)@[10729aaa9e...](https://github.com/Raines333/corporate-America-/commit/10729aaa9ef55cf6eba124c003c1fbfecfbf3ab5)
#### Tuesday 2022-05-10 07:05:29 by Raines333

Create README.md

Mary420 is just a joke and clean humor. I do not suggest anyone to take anything to serious because we’re Corporate America, if you don’t like it fuck you

---
## [yuyang0/spacemacs](https://github.com/yuyang0/spacemacs)@[c595640a34...](https://github.com/yuyang0/spacemacs/commit/c595640a344b90965bd080420f7845af65526736)
#### Tuesday 2022-05-10 07:46:04 by Daniel Nicolai

In navigation layer, Bind J/K to scroll up/down in Info-mode

Spacemacs lacks a keybinding alternative to the most natural way of scrolling
Info pages (i.e. SPC) in vanilla emacs.
Anyway, this commit adds J/K to scroll most naturally through info pages.
Currently, in Info-mode, a keybinding for J is not defined while K is bound to
evil-lookup.

Issue #2828 already adresses the inconsistent experience, and in my opinion this
can and should be improved as navigating Info pages is a very crucial part of
using Emacs.

Personally I have bound J/K to scroll page up/down in buffers/pdf/djvu/doc-view,
which I inherited from using the zathura pdf reader, and I think this is a better
default than the default vim alternatives.

---
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[71cbca3021...](https://github.com/input-output-hk/ouroboros-network/commit/71cbca30215c827117425b8f082038b34a390109)
#### Tuesday 2022-05-10 08:12:36 by Nicholas Clarke

Integrate the Babbage ledger era.

- The BabbageEra is imported from cardano-ledger-babbage and added to
  `CardanoEras` etc.
- A new Babbage era is added to the Shelley codebase, and made an
  instance of `ShelleyBasedEra`. Note the slightly weird
  `TranslationContext` - we need to use the Alonzo translation context
  because of the assumption (in `ShelleyBasedEra`) that the translation
  context is equal to the `AdditionalGenesisConfig`. The latter is a
  diff from `Shelley`, whereas the former is a diff from the previous
  era.

  TODO We should drop this assumption and correct the relationship
  between these things.
- We introduce a new class, `SupportsTwoPhaseValidation`, to reuse code
  for dealing with 2-phase validation in Alonzo and subsequent eras.
- Add standard boilerplate patterns for the Babbage era (particularly in
  Ouroboros.Consensus.Cardano.Block).
- We add additional translation code to translate from Alonzo to
  Baggage. This is slightly more complex than usual, since it must also
  translate from TPraos to Praos. It's generally formulaic, however.
- New protocol versions are introduced supporting the Babbage era.
- `protocolInfoCardano` is expanded with configuration for
  Babbage/Praos. Again, this is largely straightforward.
- Block forging code for Praos is now uncommented, since there is a
  Praos era to work on.
- The block forging code for the TPraos eras is adjusted to add a "skip"
  at the end, for the Babbage era. Honestly, this is rather ugly, but
  it's the simplest approach right now.

---
## [wens/linux](https://github.com/wens/linux)@[366a0a194b...](https://github.com/wens/linux/commit/366a0a194b3b3e3e52bc7b7b1ac35b40a1187902)
#### Tuesday 2022-05-10 08:44:05 by Douglas Anderson

arm64: dts: qcom: sc7280: eDP for herobrine boards

Add eDP support to herobrine boards, splitting up amongst the
different files as makes sense. Rationale for the current split of
things:
* The eDP connector itself is on qcard. However, not all devices with
  a qcard will use an eDP panel. Some might use MIPI and, presumably,
  someone could build a device with qcard that had no display at all.
* The qcard provides a PWM for backlight that goes to the eDP
  connector. This PWM is also provided to the board and it's expected
  that it would be used as the backlight PWM even for herobrine
  devices with MIPI displays.
* It's currently assumed that all herobrine boards will have some sort
  of display, either MIPI or eDP (but not both).
* We will assume herobrine-rev1 has eDP. The schematics allow for a
  MIPI panel to be hooked up but, aside from some testing, nobody is
  doing this and most boards don't have all the parts stuffed for
  it. The two panels would also share a PWM for backlight, which is
  weird.
* herobrine-villager and herobrine-hoglin (crd) also have eDP.
* herobrine-hoglin (crd) has slightly different regulator setup for
  the backlight. It's expected that this is unique to this board. See
  comments in the dts file.
* There are some regulators that are defined in the qcard schematic
  but provided by the board like "vreg_edp_bl" and
  "vreg_edp_3p3". While we could put references to these regulators
  straight in the qcard.dtsi file, this would force someone using
  qcard that didn't provide those regulators to provide a dummy or do
  an ugly /delete-node/. Instead, we'll add references in
  herobrine.dtsi.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Abhinav Kumar <quic_abhinavk@quicinc.com>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Signed-off-by: Bjorn Andersson <bjorn.andersson@linaro.org>
Link: https://lore.kernel.org/r/20220426124053.v2.1.Iedd71976a78d53c301ce0134832de95a989c9195@changeid

---
## [AlexandrBasan/jekyll-theme-memoirs](https://github.com/AlexandrBasan/jekyll-theme-memoirs)@[2625de1387...](https://github.com/AlexandrBasan/jekyll-theme-memoirs/commit/2625de138764b8feb75e635010a146af954bce06)
#### Tuesday 2022-05-10 09:06:49 by Alexandr Basan

Update 2022-03-24-russian-warship-go-fuck-yourself.md

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[2f89b1f42a...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/2f89b1f42a89df88c42c5680e4c4e3ee4b505d4f)
#### Tuesday 2022-05-10 09:10:12 by umeshl@appynitty.com

Chnages done By Millionaire persone and its me peaceMinded aka umesh I will Definielty succssfull in trading in this year any how and i can buy my dream laptap is macbook m12 and create youtube channel and instagram account ameen god bless me thanku for support god and sorray for any mistake har har mahadev jai shree ram jai sai ram

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7a8bf2e017...](https://github.com/mrakgr/The-Spiral-Language/commit/7a8bf2e0175df6187ed41165ebb39c3dee552975)
#### Tuesday 2022-05-10 11:03:47 by Marko Grdinić

"10:10am. I am up. Last night I asked on the Moi forums how to do Zbrush style perspective cuts. Before I check out the solution, let me try it on my own. Maybe simply turning off object snapping would do the trick.

Nope. It ends up being drawn on the construction plane which is on the XY axis. I need the contruction plane to be perpendicular to the viewport instead.

https://moi3d.com/forum/messages.php?webtag=MOI&msg=10689.1

///

10689.2 In reply to 10689.1
Hi MRAKGR,

Try setting up a shortcut key to set the construction plane to the view direction of the 3D view:
http://moi3d.com/forum/index.php?webtag=MOI&msg=5759.17
or a different variant here:
http://moi3d.com/forum/index.php?webtag=MOI&msg=10112.11

Then when you trigger that you'll be able to draw on the view oriented construction plane.

To reset it back do a right click on View > CPlane.

- Michael

///

Let me take a look.

10:30am. Hmmm, the cut is sligtly off from where I drew it. I decided to ask about this.

10:35am. Let me chill a bit and I will start. I'll take a break from the Zbrush tutorial and work on the rig in Moi. Consider that a vacation from the tutorials.

11am. Let me start. I had my bit of fun.

First, let me erase the front part and I will redo it.

I simply have to do this. I have more than enough knowledge now. I need to get used to making art.

Now let me make the case 10-20% wider. I hadn't gotten the proportions that wrong, but 10% is just the kind of amount I would not be able to eyeball.

The pen, let me use the pen. After I deal with this, I'll properly set up the hotkeys.

12pm. Sigh, this sometimes happens. Remember when I tried Rhino and it was messing up the fillets. Right now Moi is outright refusing to boolean that sweep that I did. I am not sure what to do here. It would work if I make the profile bigger, but I set it just right.

12:25pm. I spent this entire time trying to figure out how to do that small seam. I did a sweep with the specified profile, but the boolean difference fails for me unless I make it big enough.

Let me make a screenshot and I will ask on the forums. After that I'll leave the issue aside to focus on the other parts. By all means, I could have just done with in Substance.

///

Hi MRAKGR, it's probably because your view is a perspective projection and the cuts are going to project in a straight direction along the construction plane normal.

If you want it to match better you might try setting the 3D view to a parallel projection instead of perspective. You can do that under Options > View > 3D view projection = "Parallel".

- Michael

///

Oh I see. I thought it was parallel already, but I guess I was wrong. I should have guessed it.

12:45pm. Yeah, changing it to parallel (orthogonal) view makes the cuts proper. Come to think of it, I get weird results even in Zbrush unless I switch to orthogonal.

https://moi3d.com/forum/discussion.php?webtag=MOI&msg=10689.5

Here is the thread I opened to ask about the small seam.

Unless I get an answer to this, that will be a point in favor of Zbrush. I am sure than just making the mesh dense enough and then going over it with some brush would have resoved the issue easily enough.

12:50pm. Now let me have breakfast here. Damn it, I hate it when I run into issue like these.

But yeah, I have run into these issues with booleans in the past. Maybe it is because of numerical inaccuracy, but I'd get these weird failures both in Moi and Rhino. I really need to factor these issues in when I decide what my main workflow will be.

Hmph, even an union fails.

https://wiki.mcneel.com/rhino/booleanfaq
> Boolean operations can be great time saving procedures for constructing objects in Rhino. But, for the beginner, they seem to often mysteriously fail, and it is difficult to understand why.

////

So, the first thing to keep in mind is that a solid understanding of how the component operations of Booleans work is necessary. When all else fails, you can get the job done with these commands: Intersect, Split, Delete, and Join. Try undoing a successful Boolean operation and redoing it manually using those commands. Get comfortable with the fact that this procedure will always get you where you want to go even if your Boolean attempts fail.

///

Hmmm, really?

> The other thing to check is your modeling tolerances (see Understanding Tolerances).

This is for Rhino. I'll check out how Moi handles this later. Let have breakfast here."

---
## [m-falkowski1/linux](https://github.com/m-falkowski1/linux)@[213d266ebf...](https://github.com/m-falkowski1/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Tuesday 2022-05-10 11:21:30 by Linus Torvalds

gpiolib: acpi: use correct format characters

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

---
## [FPTyel/Configs](https://github.com/FPTyel/Configs)@[6697285774...](https://github.com/FPTyel/Configs/commit/6697285774845fead000ab6847cff87e927a38b2)
#### Tuesday 2022-05-10 11:32:32 by FPTyel

Hell Mode update

1. Balance corrected for bosses: slightly buffed dmg for all bosses;
2. ColorCorrection fix: Now you'll see everything, better than nothing;
3. Level 6 + Level ???: Near the door, when you being pushed up to the ship, push works for humans and zombies;
4. Particle fix on level ???;
5. Added few particles of boss fight of his end on level ???
6. Music added for level ??? boss fight;
7. Lowered volume of creepy music for level ??? (to save your ears xd)
8. Extreme HP buff for boss fight for level ??? (6500 > 20000 hp). The reason is because of static hitbox.

---
## [ahjragaas/binutils-gdb](https://github.com/ahjragaas/binutils-gdb)@[cb2cd8cba8...](https://github.com/ahjragaas/binutils-gdb/commit/cb2cd8cba82a0a5480a147d95b16098ad74d33c6)
#### Tuesday 2022-05-10 13:20:13 by Pedro Alves

Fix "b f(std::string)", always use DMGL_VERBOSE

Currently, on any remotely modern GNU/Linux system,
gdb.cp/no-dmgl-verbose.exp fails like so:

  break 'f(std::string)'
  Function "f(std::string)" not defined.
  (gdb) FAIL: gdb.cp/no-dmgl-verbose.exp: gdb_breakpoint: set breakpoint at 'f(std::string)'
  break 'f(std::basic_string<char, std::char_traits<char>, std::allocator<char> >)'
  Function "f(std::basic_string<char, std::char_traits<char>, std::allocator<char> >)" not defined.
  (gdb) PASS: gdb.cp/no-dmgl-verbose.exp: DMGL_VERBOSE-demangled f(std::string) is not defined

This testcase was added back in 2011, here:

  [patch] Remove DMGL_VERBOSE
  https://sourceware.org/pipermail/gdb-patches/2011-June/083081.html

Back then, the testcase would pass cleanly.  It turns out that the
reason it fails today is that the testcase is exercising something in
GDB that only makes sense if the program is built for the pre-C++11
libstc++ ABI.  Back then the C++11 ABI didn't exist yet, but nowadays,
you need to compile with -D_GLIBCXX_USE_CXX11_ABI=0 to use the old
ABI.  See "Dual ABI" in the libstdc++ manual, at
<https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html>.

If we tweak the gdb.cp/no-dmgl-verbose.exp testcase to force the old
ABI with -D_GLIBCXX_USE_CXX11_ABI=0, then it passes cleanly.

So why is it that setting a breakpoint at "f(std::string)" fails with
modern ABI, but passes with old ABI?

This is where libiberty demangler's DMGL_VERBOSE option comes in.  The
Itanium ABI mangling scheme has a shorthand form for std::string (and
some other types).  See
<https://itanium-cxx-abi.github.io/cxx-abi/abi.html>:

  "In addition, the following catalog of abbreviations of the form "Sx" are used:

     <substitution> ::= St # ::std::
     <substitution> ::= Sa # ::std::allocator
     <substitution> ::= Sb # ::std::basic_string
     <substitution> ::= Ss # ::std::basic_string < char,
						   ::std::char_traits<char>,
						   ::std::allocator<char> >
     <substitution> ::= Si # ::std::basic_istream<char,  std::char_traits<char> >
     <substitution> ::= So # ::std::basic_ostream<char,  std::char_traits<char> >
     <substitution> ::= Sd # ::std::basic_iostream<char, std::char_traits<char> >
  "

When the libiberty demangler encounters such a abbreviation, by
default, it expands it to the user-friendly typedef "std::string",
"std::iostream", etc..  If OTOH DMGL_VERBOSE is specified, the
abbreviation is expanded to the underlying, non-typedefed fullname
"std::basic_string<char, std::char_traits<char>, std::allocator<char> >"
etc. as documented in the Itanium ABI, and pasted above.  You can see
the standard abbreviations/substitutions in
libiberty/cp-demangle.c:standard_subs.

Back before Jan's patch in 2011, there were parts of GDB that used
DMGL_VERBOSE, and others that did not, leading to mismatches.  The
solution back then was to stop using DMGL_VERBOSE throughout.

GDB has code in place to let users set a breakpoint at a function with
typedefs in its parameters, like "b f(uint32_t)".  Demangled function
names as they appear in the symbol tables almost (more on this is in a
bit) never have typedefs in them, so when processing "b f(uint32_t)"
GDB first replaces "uint32_t" for its underlying type, and then sets a
breakpoint on the resulting prototype, in this case "f(unsigned int)".

Now, if DMGL_VERBOSE is _not_ used, then the demangler demangles the
mangled name of a function such as "void f(std::string)" that was
mangled using the standard abbreviations mentioned above really as:

  "void f(std::string)".

For example, the mangled name of "void f(std::string)" if you compile
with old pre-C++11 ABI is "_Z1fSs".  That uses the abbreviation "Ss",
so if you demangle that without DMGL_VERBOSE, you get:

  $ echo "_Z1fSs" | c++filt --no-verbose
  f(std::string)

while with DMGL_VERBOSE you'd get:

  $ echo "_Z1fSs" | c++filt
  f(std::basic_string<char, std::char_traits<char>, std::allocator<char> >)

If, when the user sets a breakpoint at "f(std::string)", GDB would
replace the std::string typedef for its underlying type using the same
mechanism I mentioned for the "f(uint32_t)" example above, then GDB
would really try to set a breakpoint at "f(std::basic_string<char,
std::char_traits<char>, std::allocator<char> >)", and that would fail,
as the function symbol GDB knows about for that function, given no
DMGL_VERBOSE, is "f(std::string)".

For this reason, the code that expands typedefs in function parameter
names has an exception for std::string (and other standard
abbreviation types), such that "std::string" is never
typedef-expanded.

And here lies the problem when you try to do "b f(std::string)" with a
program compiled with the C++11 ABI.  In that case, std::string
expands to a different underlying type, like so:

  f(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

and this symbol naturally mangles differently, as:

  _Z1fNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

and then because this doesn't use the shorthand mangling abbreviation
for "std::string" anymore, it always demangles as:

  f(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

Now, when using the C++11 ABI, and you set a breakpoint at
"f(std::string)", GDB's typedefs-in-parameters expansion code hits the
exception for "std::string" and doesn't expand it, so the breakpoint
fails to be inserted, because the symbol that exists is really the

  f(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)

one, not "f(std::string)".

So to fix things for C++11 ABI, clearly we need to remove the
"std::string" exception from the typedef-in-parameters expansion
logic.  If we do just that, then "b f(std::string)" starts working
with the C++11 ABI.

However, if we do _just_ that, and nothing else, then we break
pre-C++11 ABI...

The solution is then to in addition switch GDB to always use
DMGL_VERBOSE.  If we do this, then pre-C++11 ABI symbols works the
same as C++11 ABI symbols overall -- the demangler expands the
standard abbreviation for "std::string" as "std::basic_string<char,
std::char_traits<char>, std::allocator<char> >" and letting GDB expand
the "std::string" typedef (etc.) too is no longer a problem.

To avoid getting in the situation where some parts of GDB use
DMGL_VERBOSE and others not, this patch adds wrappers around the
demangler's entry points that GDB uses, and makes those force
DMGL_VERBOSE.

The point of the gdb.cp/no-dmgl-verbose.exp testcase was to try to
ensure that DMGL_VERBOSE doesn't creep back in:

 gdb_test {break 'f(std::basic_string<char, std::char_traits<char>, std::allocator<char> >)'} \
	  {Function ".*" not defined\.} \
	  "DMGL_VERBOSE-demangled f(std::string) is not defined"

This obviously no longer makes sense to have, since we now depend on
DMGL_VERBOSE.  So the patch replaces gdb.cp/no-dmgl-verbose.exp with a
new gdb.cp/break-f-std-string.exp testcase whose purpose is to make
sure that setting a breakpoint at "f(std::string)" works.  It
exercises both pre-C++11 ABI and C++11 ABI.

Change-Id: Ib54fab4cf0fd307bfd55bf1dd5056830096a653b

---
## [HEELZacky/Strapontin](https://github.com/HEELZacky/Strapontin)@[be0f38f570...](https://github.com/HEELZacky/Strapontin/commit/be0f38f5702d19089fbece103852dcea1176f6bb)
#### Tuesday 2022-05-10 14:27:46 by HEELZacky

End of day commit

Might have left a custom event setting texts boxes to "fuck you and your family" do'nt take it personally, I was frustrated

---
## [nicholas-dougherty/natural-language-processing-exercises](https://github.com/nicholas-dougherty/natural-language-processing-exercises)@[11ae1b0ee4...](https://github.com/nicholas-dougherty/natural-language-processing-exercises/commit/11ae1b0ee4b5a0934f41a07a7b450473d82cefef)
#### Tuesday 2022-05-10 15:00:16 by Nicholas Dougherty

All I want in life is a little bit of love to take the pain away

---
## [Atemo/rathena](https://github.com/Atemo/rathena)@[d617d9f083...](https://github.com/Atemo/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Tuesday 2022-05-10 16:04:36 by Aleos

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
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[d6cbad1738...](https://github.com/Koi-3088/ForkBot.NET/commit/d6cbad17380392b08f7921a839b8b74f071383b2)
#### Tuesday 2022-05-10 17:02:43 by Koi

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
## [Miouyouyou/python-tests](https://github.com/Miouyouyou/python-tests)@[4c3b7e34ac...](https://github.com/Miouyouyou/python-tests/commit/4c3b7e34ac21c07cc0f5fe145283c56d624d283a)
#### Tuesday 2022-05-10 18:08:49 by Myy Miouyouyou

Not inspired

I forgot the fact that I still have no clear way
to detect if the UI can be run or not.

But the biggest issue is that I'm clearly not
inspired on this project.
I still have no clear idea where this is going,
even though there's a roadmap.

QT is sucking out the will I'd like to put on this
project, due to a FUCKING HORRENDOUS toolset.
The more I'm using it, the more I feel that QML is
just "that garbage that QT doesn't know what to do
with". This reminds that I'll have to make a converter
from Godot Engine, or whatever over UI maker that
makes a bit of sense in this era.

So yeah...

The best way to tackle this would be to have a UI
focused on presenting all the available docker images,
while also providing extended view and toolset for
installed images.
This can be done. However, then I'm still wondering
how to generalize this afterwards.
Hence the 'I feel I'm alone on this project that is
not mine'.

So, unless there's some real movement on the project,
this might be one of the last commit.

Signed-off-by: Myy Miouyouyou <myy@miouyouyou.fr>

---
## [raffclar/fulpstation](https://github.com/raffclar/fulpstation)@[c797bf79ea...](https://github.com/raffclar/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Tuesday 2022-05-10 18:24:14 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [raffclar/fulpstation](https://github.com/raffclar/fulpstation)@[b59f03e592...](https://github.com/raffclar/fulpstation/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Tuesday 2022-05-10 18:24:14 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e53e26bdd9...](https://github.com/mrakgr/The-Spiral-Language/commit/e53e26bdd9ab1e3263e1bace20314a9a0b491975)
#### Tuesday 2022-05-10 19:07:54 by Marko Grdinić

"2:45pm. Oh, I figured it out. I read something about Rhino not liking when objects are overlapping, so I had the idea to move the curve a little so its ends do not sit directly on the edges. I do not understand why this made it work, but I'll take it.

Let me post the resolution in the thread I opened.

3pm. Done. I am dwelling too much on this. Let me get this party started. Focus me, focus. Last time I got to this point, I lost my nerve. I need to do better this time around.

Got the power button. Let me do the other buttons. What is really important is that things go smoothly for me.

https://youtu.be/XqwMwTEsIcI?t=47

Let me take this chance to plug in these hotkeys. This is the ideal chance to do it.

4:25pm. Things are going well. I've finally hit my stride. Let me see if I can speed things up. I am ungodly slow as usual, but if I can get into the groove, I could put a dent into it.

6:05pm. Done with all the front ports. I'll aim to at least finish the front today so I can leave the easy stuff for tomorrow.

...Time for lunch.

6:20pm. Done with lunch.

6:25pm. I really want to call it a day, but let me do some more.

6:30pm. Let me do it. Just get the thing done.

6:40pm. https://moi3d.com/forum/lmessages.php?webtag=MOI&msg=8123.1
MoI keyboard shortcuts

I'll keep this thread in mind. Let me figure out where the show points is.

7:35pm. Now I've fallen into the trap of hasling myself with a certain edge.

8pm. Oh crap I thought I got it to work right, but I messed it up.

8:45pm. I am finally done with the front part. I think that boolean related issues cost me a few hours today. But I think I finally got my lesson - don't overlap them directly. This is not as easy as it seems, since apparently the whole program is designed to induce overlaps.

8:50pm. Tomorrow, I'll do the last pattern, which should not take me longer than half an hour and after that I'll be done modeling the rig. I'll be able to move to texturing. Right now I am 80% done.

Most of this time has been taken up by the small details.

I can do 95% of the volume in 5% of the time, but then get caught up in the hard stuff that nobody will even notice.

Yeah, this is not the way to really make illustrations fast. If I want to get good at this, I need to stop at blocking out the basic shape. If I want details, I should leave that for the texturing phase.

Hmmm, but yeah. This is not so bad. Boolean issues aside, I'll get used to working around them soon, Moi is a fun little program if you want to do hard surface modeling. Blender despite its complexity, is not better than it.

8:55pm. I'll aim to finish my 3d journey by the end of the month. In June, assuming I am satisfied with how much of the room I've done, I'll move to doing 2d.

I need to follow a process of iterative refinement. I need to get used to sketching in 2d, seeing what the weak points are and then using 3d to strengthen my art. I thought that it might be vible to focus solely on 3d, but it seems there is a reason I've yet to see anybody pursue such a path.

There is no way around it - I am going to have to get good all around at it.

9pm. Assuming I can meet decent quality standard, the most important thing after that is speed.

My sense is that it won't take me longer than six months to really get good at 2d. I've been afraid of testing myself, but my reason is telling me that people who get stuck at beg and int stages have some combination of laziness and stupidity holding them back. I am do not have the first flaw by any stretch surprisingly enough. And when I am stupid, it is due to external circumstance such as boredom, stress or fatigue.

9:05pm. Today's session would have been great if not for these weird boolean issues. But those frustrations aside, I've been in the zone the whole day. I should keep this up.

I can watching tutorials for years, but I'll never break beyond the intermediate stage if that is all that I do. It is when I know the tools, and really practice using them that I step on the path to expertise."

---
## [BenVillalobos/msbuild](https://github.com/BenVillalobos/msbuild)@[a572dc6b79...](https://github.com/BenVillalobos/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Tuesday 2022-05-10 19:25:58 by Forgind

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
## [FlameArrow57/goon-flock](https://github.com/FlameArrow57/goon-flock)@[bdad398f9e...](https://github.com/FlameArrow57/goon-flock/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Tuesday 2022-05-10 19:50:24 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [shobbs528/FinalProject_a3](https://github.com/shobbs528/FinalProject_a3)@[e137ef0a8f...](https://github.com/shobbs528/FinalProject_a3/commit/e137ef0a8f1168826d14be21ef05d22f640e27ec)
#### Tuesday 2022-05-10 20:43:19 by Samwich422

OKAY

OKAY. This code. right here. as it is. Allows for networking, and shows the ghost avatar of the other player moving. THIS RIGHT HERE. Counts. Not perfect. But fuck yes. I think we're almost at 70% for this stupid fucking project

---
## [NickLiffen/ghas-enablement](https://github.com/NickLiffen/ghas-enablement)@[c32bab9ba1...](https://github.com/NickLiffen/ghas-enablement/commit/c32bab9ba13c0d5e9d577b38e8c954fc9efa5916)
#### Tuesday 2022-05-10 21:00:59 by Dominique Thornton DJ

Features & Refactors (#64)

* chore: :wrench: Rename repos.json

This change is to allow repos.json & organizations.json to be added
to gitignore so that privacy can be maintained in private organizations.

* feat: :sparkles: Add missing java codeql file

Not sure if this was intentional, but a java codeql file doesn't exists.
This commit introduces the file

* chore: :arrow_up: Update deps

Update documentation. `Yarn add` expects a package. The equivalent of npm
install (install all deps)ya is `yarn install` or just `yarn`

See: https://classic.yarnpkg.com/lang/en/docs/cli/install/

* feat: :sparkles: Simplify destDir, user, add root

This commit attempts to simplify the determination of the destination
directory and username. It also introduces the root for user home to be
used in later feature.

* refactor: :recycle: command refactor

This commit is largely a refactor of the existing code. The point is to
simplify the commands required for windows/macos/linux. They largely
all use the same commands with slight variations, such as home
directory, and command arguments.

It is a larger commit than I'd like, but all three file changes do go
together.

globals.ts:
- Removes the need to create separate vars for windows vs
everything else. Determine the differences in globals and send 1 var.
- Determine OS here so we can set root to home path. No longer needed
in commitFile.ts

commands.ts:
- Squash windows/macOS/linux into a single command array.
- Introduce platform and root to differ commands/paths
- Remove unnecessary commands like mv as cp can accomplish this
- Make commands/arguments conditional
- Add helper function to convert linux paths to windows paths
  - This really helps with mkdir as Windows can natively create
    multi-leveled directory structures when correct paths are used: `\`

commitFile.ts:
- Moved existsSync, os and isCodespace to globals.ts
- Replaced mac/windowsCommands w/ genearlCommands
- Simplified gitCommands condition
- Added informs
- Added try catch to "for loop" of commands. I may just be missing it,
  but the If (stderr) block didn't seem to be activating. The app would
  die after stating the error.
- Whitelist function for known error responses like this folder alredy
  exists and can't delete a folder that doesn't exists.

The whitelist function feels hacky, so I welcome any thoughts on it.

* feat: :sparkles: ISSUE-61 PR comments

This commit contains the recommended changes from Nick.

1. globals consolidates all OS types to a common cwd under destdir
2. The commands.ts file consolidates all commands into a single list
3. Backticks are used in string block.

Also introduces user specified temp directory. It turns out I don't
have a ~/Desktop thanks to OneDrive.

ISSUE-61

---
## [cdcline/demo-website](https://github.com/cdcline/demo-website)@[a454ad4a5f...](https://github.com/cdcline/demo-website/commit/a454ad4a5f999c811d5c51744754175a5d3f4cbb)
#### Tuesday 2022-05-10 22:39:48 by Chris Cline

Cleanup footer and Page floating

The Page would grow to a max size, but was justified to the left.

This makes it awkward in large screens because it feels like a lot
of unused pixels they paid for.

So we'll float the page in the center of the background, which gives
a nice illusion of using more of the page than you actually are.

The Footer wasn't aligned correctly because the text was different
sizes and it's difficult to get a correct float with 3 items of
very different sizes.

So we hack in a right/left aligned style & do some fancy media
tags to handle the ugly layout at low widths

Definatly a hack for just this case but also looks good and this
is the demo so yeah, gonna go with it.

Also cleans up some bad spacing.

Also does minor cleanup
 * Fixes some invalid spacing

---
## [Odisurin/Civ13](https://github.com/Odisurin/Civ13)@[20b320a949...](https://github.com/Odisurin/Civ13/commit/20b320a949e6bd50e25ec505df3023405ce90dd6)
#### Tuesday 2022-05-10 22:59:31 by savethetreez

Adds missing conflicted icons

Fuck you again, Odisurin!

---

