## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-06](docs/good-messages/2022/2022-05-06.md)


1,720,794 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,720,794 were push events containing 2,732,179 commit messages that amount to 187,010,628 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [cinder1992/tgstation](https://github.com/cinder1992/tgstation)@[27946f516d...](https://github.com/cinder1992/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Friday 2022-05-06 00:25:30 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [BongoDongo2000/tgstation](https://github.com/BongoDongo2000/tgstation)@[cd1b891d79...](https://github.com/BongoDongo2000/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Friday 2022-05-06 00:40:25 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [ThePainkiller/Skyrat-tg](https://github.com/ThePainkiller/Skyrat-tg)@[e99b3624ef...](https://github.com/ThePainkiller/Skyrat-tg/commit/e99b3624ef3a041e76e3e8f34577effe07ca41d9)
#### Friday 2022-05-06 00:45:01 by SkyratBot

[MIRROR] Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. [MDB IGNORE] (#13029)

* Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug.

Co-authored-by: Vladin Heir <44104681+VladinXXV@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [anarazel/postgres](https://github.com/anarazel/postgres)@[c40ba5f318...](https://github.com/anarazel/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Friday 2022-05-06 01:43:27 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [LukeSandsor/GitFit-App](https://github.com/LukeSandsor/GitFit-App)@[581b91acff...](https://github.com/LukeSandsor/GitFit-App/commit/581b91acff84fb97f45824bbf79384b501b06dde)
#### Friday 2022-05-06 01:51:40 by Lucas Reyna

after painfully implementing contexts into the CalendarPage.js, I am happy to announce that the calendar will now load info on a specific day. The code looks kinda like garbage, but it works for now. I just hope that there won't be many slow downs when incorporating the backend. We'll have to see about caching, maybe.

---
## [have-no-clue-what-im-doing/Broderic_Blog](https://github.com/have-no-clue-what-im-doing/Broderic_Blog)@[adaea90db4...](https://github.com/have-no-clue-what-im-doing/Broderic_Blog/commit/adaea90db47556ce05762299d46b98a6db7d72cc)
#### Friday 2022-05-06 01:53:34 by purplepeoplehacker

it's really hard to get a stupid fav to work in hugo holy shit

---
## [Genso-Necromancer/The-Magician](https://github.com/Genso-Necromancer/The-Magician)@[e791f05a22...](https://github.com/Genso-Necromancer/The-Magician/commit/e791f05a227913a634d62d6592656bdf9e2f792f)
#### Friday 2022-05-06 02:44:23 by Genso-Necromancer

Mishaps and Miracles Update

=Ecological Bomb
DMG penalty now -34%
Single Target Blight now 2-4/3

=Crimson Court Set
Added very the basic functionality of the two dolls
Added the trinket art
This is still far from a final version, and it's not entirely the first draft either

=Magic Missile
Fixed the Dark Hakkero Curse having the wrong rule type and preventing the skill from working at the wrong times
Added an FX for when MM gains damage on kill. Will fine tweak it's positioning once a combat animation has been made.
Added an FX for when Magician reaches death's door and loses her power buffs

=Powerful Drug
Removed situational Healing reduction
Changed Healing rates to 2-2/2-3/3-3/3-4/4-4
Added Mishap and Miracle system
>There is a 24% chance for a Mishap or Miracle, you cannot get both, but you can get neither
>Mishaps always inflict +100% Random Target chance(Attack&Friendly)
>Miracles always add the value of the heal low roll onto what you did roll
>Miracle bonuses are doubled when critting
>There's a few unmentioned quirks of the skill, but they're all intentional and part of the fun
Added barks for when Magician get's a mishap on someone else, and different ones for when using it on herself
There is support for, but not yet written, bark reactions from Maid and Miko when a mishap is inflicted upon them

=Art
Added Camping Sprite!

---
## [ORCACommander/Tannhauser-Gate-Dev](https://github.com/ORCACommander/Tannhauser-Gate-Dev)@[c5f0ea76e0...](https://github.com/ORCACommander/Tannhauser-Gate-Dev/commit/c5f0ea76e0fa1d1236fe04a2edaf6d9c047fc7c8)
#### Friday 2022-05-06 02:54:57 by SkyratBot

[MIRROR] Vim mecha changes [MDB IGNORE] (#12981)

* Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>

---
## [Nexus003/device_xiaomi_sdm845-common](https://github.com/Nexus003/device_xiaomi_sdm845-common)@[1d39b80ad6...](https://github.com/Nexus003/device_xiaomi_sdm845-common/commit/1d39b80ad68251184b58888ba7fa5f879e57c255)
#### Friday 2022-05-06 03:43:10 by Dhruv Gera

rootdir: Spoof selinux state

Fuck you google and your cts

---
## [patevs/wireit](https://github.com/patevs/wireit)@[c85c022769...](https://github.com/patevs/wireit/commit/c85c02276975a1a86cbf509a7e9a353d5f0a19a8)
#### Friday 2022-05-06 07:08:48 by Alexander Marks

Error when trying to cache outside of package (#182)

It's currently not possible to locally cache an output file that isn't inside of the package directory. We check for this case when we delete and throw, but not when we cache. So if you are caching but have cleaning disabled, we would silently weirdly save the output file to a parent directory, and then not restore it.

Now this is an error.

Note we could in theory do this during analysis, but I'm not 100% confident in my ability to correctly detect this case given all of the possible magic glob syntax, so for now it's safer to just do it at runtime. (see https://github.com/google/wireit/issues/64).

Also note we could in theory support caching files outside of the package root, but we'd have to do something like a tarball for the local cache, instead of simply copying into `.wireit/<script>/cache/<hash>`. We should think carefully about whether we want to do that, though, so I'm not dealing with that for now.

Fixes https://github.com/google/wireit/issues/181

---
## [noemina/acts](https://github.com/noemina/acts)@[6e1fd31474...](https://github.com/noemina/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Friday 2022-05-06 07:28:28 by Stephen Nicholas Swatman

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
## [plctlab/corev-binutils-gdb](https://github.com/plctlab/corev-binutils-gdb)@[bbea680797...](https://github.com/plctlab/corev-binutils-gdb/commit/bbea68079781ac4c2fc941867ee9888585cafb77)
#### Friday 2022-05-06 07:45:38 by Andrew Burgess

gdb/python: improve the auto help text for gdb.Parameter

This commit attempts to improve the help text that is generated for
gdb.Parameter objects when the user fails to provide their own
documentation.

Documentation for a gdb.Parameter is currently pulled from two
sources: the class documentation string, and the set_doc/show_doc
class attributes.  Thus, a fully documented parameter might look like
this:

  class Param_All (gdb.Parameter):
     """This is the class documentation string."""

     show_doc = "Show the state of this parameter"
     set_doc = "Set the state of this parameter"

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_All, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_All ('param-all')

Then in GDB we see this:

  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

Which is fine.  But, if the user skips both of the documentation parts
like this:

  class Param_None (gdb.Parameter):

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_None, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_None ('param-none')

Now in GDB we see this:

  (gdb) help set param-none
  This command is not documented.
  This command is not documented.

That's not great, the duplicated text looks a bit weird.  If we drop
different parts we get different results.  Here's what we get if the
user drops the set_doc and show_doc attributes:

  (gdb) help set param-doc
  This command is not documented.
  This is the class documentation string.

That kind of sucks, we say it's undocumented, then proceed to print
the documentation.  Finally, if we drop the class documentation but
keep the set_doc and show_doc:

  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

That seems OK.

So, I think there's room for improvement.

With this patch, for the four cases above we now see this:

  # All values provided by the user, no change in this case:
  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

  # Nothing provided by the user, the first string is now different:
  (gdb) help set param-none
  Set the current value of 'param-none'.
  This command is not documented.

  # Only the class documentation is provided, the first string is
  # changed as in the previous case:
  (gdb) help set param-doc
  Set the current value of 'param-doc'.
  This is the class documentation string.

  # Only the set_doc and show_doc are provided, this case is unchanged
  # from before the patch:
  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

The one place where this change might be considered a negative is when
dealing with prefix commands.  If we create a prefix command but don't
supply the set_doc / show_doc strings, then this is what we saw before
my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- This command is not documented.
  ... snip ...

And after my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- Set the current value of 'print param-none'.
  ... snip ...

This seems slightly less helpful than before, but I don't think its
terrible.

Additionally, I've changed what we print when the get_show_string
method is not provided in Python.

Back when gdb.Parameter was first added to GDB, we didn't provide a
show function when registering the internal command object within
GDB.  As a result, GDB would make use of its "magic" mangling of the
show_doc string to create a sentence that would display the current
value (see deprecated_show_value_hack in cli/cli-setshow.c).

However, when we added support for the get_show_string method to
gdb.Parameter, there was an attempt to maintain backward compatibility
by displaying the show_doc string with the current value appended, see
get_show_value in py-param.c.  Unfortunately, this isn't anywhere
close to what deprecated_show_value_hack does, and the results are
pretty poor, for example, this is GDB before my patch:

  (gdb) show param-none
  This command is not documented. off

I think we can all agree that this is pretty bad.

After my patch, we how show this:

  (gdb) show param-none
  The current value of 'param-none' is "off".

Which at least is a real sentence, even if it's not very informative.

This patch does change the way that the Python API behaves slightly,
but only in the cases when the user has missed providing GDB with some
information.  In most cases I think the new behaviour is a lot better,
there's the one case (noted above) which is a bit iffy, but I think is
still OK.

I've updated the existing gdb.python/py-parameter.exp test to cover
the modified behaviour.

Finally, I've updated the documentation to (I hope) make it clearer
how the various bits of help text come together.

---
## [plctlab/corev-binutils-gdb](https://github.com/plctlab/corev-binutils-gdb)@[299953ca95...](https://github.com/plctlab/corev-binutils-gdb/commit/299953ca95cc5ac47e52236e2eeb44afc5369134)
#### Friday 2022-05-06 07:45:38 by Andrew Burgess

gdb/python: handle non utf-8 characters when source highlighting

This commit adds support for source files that contain non utf-8
characters when performing source styling using the Python pygments
package.  This does not change the behaviour of GDB when the GNU
Source Highlight library is used.

For the following problem description, assume that either GDB is built
without GNU Source Highlight support, of that this has been disabled
using 'maintenance set gnu-source-highlight enabled off'.

The initial problem reported was that a source file containing non
utf-8 characters would cause GDB to print a Python exception, and then
display the source without styling, e.g.:

  Python Exception <class 'UnicodeDecodeError'>: 'utf-8' codec can't decode byte 0xc0 in position 142: invalid start byte
  /* Source code here, without styling...  */

Further, as the user steps through different source files, each time
the problematic source file was evicted from the source cache, and
then later reloaded, the exception would be printed again.

Finally, this problem is only present when using Python 3, this issue
is not present for Python 2.

What makes this especially frustrating is that GDB can clearly print
the source file contents, they're right there...  If we disable
styling completely, or make use of the GNU Source Highlight library,
then everything is fine.  So why is there an error when we try to
apply styling using Python?

The problem is the use of PyString_FromString (which is an alias for
PyUnicode_FromString in Python 3), this function converts a C string
into a either a Unicode object (Py3) or a str object (Py2).  For
Python 2 there is no unicode encoding performed during this function
call, but for Python 3 the input is assumed to be a uft-8 encoding
string for the purpose of the conversion.  And here of course, is the
problem, if the source file contains non utf-8 characters, then it
should not be treated as utf-8, but that's what we do, and that's why
we get an error.

My first thought when looking at this was to spot when the
PyString_FromString call failed with a UnicodeDecodeError and silently
ignore the error.  This would mean that GDB would print the source
without styling, but would also avoid the annoying exception message.

However, I also make use of `pygmentize`, a command line wrapper
around the Python pygments module, which I use to apply syntax
highlighting in the output of `less`.  And this command line wrapper
is quite happy to syntax highlight my source file that contains non
utf-8 characters, so it feels like the problem should be solvable.

It turns out that inside the pygments module there is already support
for guessing the encoding of the incoming file content, if the
incoming content is not already a Unicode string.  This is what
happens for Python 2 where the incoming content is of `str` type.

We could try and make GDB smarter when it comes to converting C
strings into Python Unicode objects; this would probably require us to
just try a couple of different encoding schemes rather than just
giving up after utf-8.

However, I figure, why bother?  The pygments module already does this
for us, and the colorize API is not part of the documented external
API of GDB.  So, why not just change the colorize API, instead of the
content being a Unicode string (for Python 3), lets just make the
content be a bytes object.  The pygments module can then take
responsibility for guessing the encoding.

So, currently, the colorize API receives a unicode object, and returns
a unicode object.  I propose that the colorize API receive a bytes
object, and return a bytes object.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ce1bdb0205...](https://github.com/tgstation/tgstation/commit/ce1bdb0205e1428fccff7c81cb67cb3d0a68f1a3)
#### Friday 2022-05-06 07:47:53 by itseasytosee

Stops floating mobs from being affected by slowndown bulky_drag and human_carry (#66610)

Put simply, removes the slowdown from pulling bulky items as well and fireman carrying (and piggyback rides) while in zero gravity.

This also fixes some weirdness, like how slowdowns from aggressive grabs are negated in zero g, but because bulky_drag is NOT negated, you can still be slowdown in zero gravity if your target is laying down. or in a neck grab or higher because they are then automatically floored. Which makes zero consistant sense given the context.

Also, while testing this, I noticed that it was faster to drift while pulling a bulky object in space rather than fly with a jetpack because of the  slowdown and how drifting works, which also makes no god damn sense. This should fix that too.

Fixes the consistency errors mentioned above, also adds an interesting change of game state in zero gravity which seems fun. (see: faster to drag away downed friendlies during a space battle, or perhaps kidnap a downed enemy)

Fixes #62600 (aggressively grabbing a body in space makes you move faster than passively grabbing them)


You can now pull bulky things in zero gravity at full speed
The slowdown from neck grabs is now properly negated in zero gravity.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[2b34e1db66...](https://github.com/Buildstarted/linksfordevs/commit/2b34e1db664751e0dac3144618a1f71406c72995)
#### Friday 2022-05-06 08:05:38 by Ben Dornis

Updating: 5/6/2022 8:00:00 AM

 1. Added: Home - Moshe Karmel
    (https://moshekarmel.com/thoughts/decisions.html)
 2. Added: The Simple Joy of Learning to Play Piano
    (https://brianschrader.com/archive/the-simple-joy-of-learning-to-play-piano/)
 3. Added: Darlings of the self-hosted, open-source world
    (https://loganmarchione.com/2022/05/darlings-of-the-self-hosted-open-source-world/)
 4. Added: My PhD Research Workflow – Tony Zorman
    (https://tony-zorman.com/posts/phd-workflow/2022-05-01-my-phd-workflow.html)
 5. Added: A vision for Decentraland's next 5 years
    (https://maraoz.com/2022/05/04/decentraland-vision/)
 6. Added: How Musicians Could Profit From Copyleft
    (https://timdaub.github.io/2022/05/05/how-musicians-could-profit-from-copyleft/)
 7. Added: My Software Engineering Bootcamp Journey (Series three)
    (https://tekhthings.com/my-software-engineering-bootcamp-journey-series-three)
 8. Added: Hating On Oats
    (https://hatingonoats.com/blog/I%20Spent%20$1000%20Making%20an%20NFT%20Project%20And%20Unfortunately%20Learned%20Some%20Things)
 9. Added: Why Ballerina is a language
    (https://blog.jclark.com/2022/05/why-ballerina-is-language.html)
10. Added: Chief Innovation Officer- What are the prerequisites?
    (https://radoncnotes.com/2022/05/05/chief-innovation-officer-what-are-the-prerequisites/)
11. Added: Fixing the problem of too many tabs
    (https://carl.duevel.online/blog/desktop/)
12. Added: Syncthing: The data deduplication master
    (https://www.ctrl.blog/entry/syncthing-deduplication-master.html)

Generation took: 00:05:27.2682301
 Maintenance update - cleaning up homepage and feed

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[455a178927...](https://github.com/treckstar/yolo-octo-hipster/commit/455a178927dee79ddb1baf9002124a33b6bd511d)
#### Friday 2022-05-06 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [warmchang/libpod](https://github.com/warmchang/libpod)@[e74717f348...](https://github.com/warmchang/libpod/commit/e74717f348c2768b87cad7dd6997c42dc85fc50a)
#### Friday 2022-05-06 09:52:28 by Ed Santiago

Treadmill script: revamp

Major revamp: instead of stacking a vendor commit on top of
the treadmill changes, do it the other way around: vendor,
then apply treadmill diffs.

Reason: the build-all-new-commits test. Sigh. It fails in the
common case where our treadmill changes include a new struct
element in cmd/podman/images/build.go

Why this is good: well, superficially, it's more intuitive.

Why this is horrible: omg the rebasing games are a nightmare.
When the vendor commit is on top (HEAD), it's ultra-trivial
to drop it, rebase the treadmill changes on main, then add
a new vendor-buildah commit on top. As you can see from the
diffs in this PR, treadmill-as-HEAD introduces all sorts
of complex dance steps in which things can go catastrophically
wrong and you can lose all your treadmill patches. I try very
hard to prevent this, and to offer hints if there's a problem,
and heck in the worst case it's still git so it's still possible
to find lost commits... but it's still much riskier than the
old way.

Alternative I considered: using sed magic to disable the
build-all-new-commits test. So tempting... but that would
also disable the bloat check.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [MKLab-ITI/hugomklab](https://github.com/MKLab-ITI/hugomklab)@[3c6ca459d4...](https://github.com/MKLab-ITI/hugomklab/commit/3c6ca459d4c92830c0b31846c83ee4552a0243bc)
#### Friday 2022-05-06 10:07:11 by nikiserri

Create Publication “2022-05-06-water-quality-issues-can-we-detect-a-creeping-crisis-with-social-media-data”

---
## [der-lyse/newsboat](https://github.com/der-lyse/newsboat)@[2dd8022096...](https://github.com/der-lyse/newsboat/commit/2dd8022096590b6042948687dfc69d7b39198334)
#### Friday 2022-05-06 11:56:51 by Lysander Trischler

Remove trailing whitespace

Trailing whitespace is not harmful, but unnecessary and ugly in my
opinion. I configured my editor to highlight it, so I see it all the
time, which is a bit annoying. Let's get rid of it.

Actually regenerating the filter produces some slightly different code
with my installed version of cococpp (Coco/R Jan 02, 2012), so I just
kept the old code and removed the trailing spaces and tabulators.

`make fmt` now also removes trailing whitespace from all the text files.
Since not only source files but any text files might be subject to
introducing new trailing whitespace, CI will not skip that formatting
task anmyore for documentation-, translation-, contribution- and/or
snap-only changes. It's now unconditionally executed all the time.

'xargs -r' is not supported everywhere, so we need to use a loop
instead. That will guard against no files necessary to be rewritten.

---
## [MentalTorque/Federal-Spending](https://github.com/MentalTorque/Federal-Spending)@[5b744a3fc3...](https://github.com/MentalTorque/Federal-Spending/commit/5b744a3fc306d01697e5cba9d56dbdfbb3935bb6)
#### Friday 2022-05-06 13:45:12 by Nick Staich

Add files via upload

Worked on an initial model for the Federal Spending; it was an utter disaster.  I was thorough, but the model is simply not structured well wo get away from underfitting.  A very interesting experience.  As these assignments are part of my learning program, and I intend on using it to drive the $10M in revenue I produce annually, I find it interesting to see how these models can break, so to learn how to rectify it in the real world.  Not every model, very few in fact, will run optimally if at all on their first go around.  Part of learning data science is experimenting with the models to learn both how they optimize, and also how they fail.  Those failures will be the bedrock of future optimizations.

To rectify this model, I am hyptohesizing the following:

If I OHE the Geography feature, it'll create far more features to analyze across the model which we need considering how drastically underfit this model presently is.  This should improve the nuance of the model, allow for improved PCA, provide better clustering, and ultimately give improved accuracy to the model.

As I've been coding for 36 hours straight now, in order to have everything in to unlock the exam, I am having difficulty maintaining the rate.  I will try and get the revamped model in ASAP, but I am getting concerned that the relentless pursuit of perfection, especially in such a compressed period,  required with the submission of all of these assignments  is also going to adversely impact my performance on the incredibly rigorous exam, which I will have to commence in the next 18 hours if I am to finish by the submission deadline.  The class just learned that if you miss just half a point on the exam, it demotes you to some form of second class belt.  This setup is not very conducive to success in my opinion, considering the previous cadence disruptions of shifting dates, especially when enjoined to working 70 hours a week and raising a child.  It's a good thing I really want this.

Let's take a crack at this next model.

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[3544662bd8...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/3544662bd88c45db7ede933782b548873103a71b)
#### Friday 2022-05-06 13:47:42 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [Brellos/roundtablehold.github.io](https://github.com/Brellos/roundtablehold.github.io)@[07161f103d...](https://github.com/Brellos/roundtablehold.github.io/commit/07161f103d851b6b863d25c50950515adf1a007b)
#### Friday 2022-05-06 14:04:03 by Olivia

Landmarks Overhaul pt 1

- The Evergaols and Legacy Dungeons pages are completely gone. I removed the yaml and html files. Their progress will be lost.
- The Caves page has been completely redone to become a Landmarks page. The page has been renamed to Landmarks & Locations and the yaml is renamed to landmarks.yaml. The id is still caves so that progress from Caves, Catacombs, and Tunnels is preserved on this new page.
- Content from the two deleted pages has been moved to the Landmarks page. Their ids now follow new conventions to not clash with the existing Caves ids: "e1" - "e10" for evergaols, and "ld1" - "ld14" for legacy dungeons.
- The Location column and description for all preexisting items on the Landmarks page have been removed. It will be made obsolete by map links to every location, though these are not yet implemented.
- Every location in the game that generates a landmark on the in-game map now has an entry on the Landmarks page, dramatically extending the page. For the most part, these new entries don't have notes or other info that'd be good to add yet, but they do all have their correct icons, unless I made any mistakes. Landmarks follow the id convention "l1" - "l130". I think I got all of them, but there's 130 and no list in the game to compare against, so I welcome double and triple checkers.
- The Landmarks page is sorted by location as the Caves page was, with all other integrated items sorted into their places.
- Within region sections, I sorted the locations into consistent orders as best I could, but they will likely need reordering. My order within a region is Caves, Catacombs, Tunnels, Hero's Graves, Evergaols, Minor Erdtrees, Divine Towers, Puzzle Towers, Ruins, Shacks, Churches, Unique, and Legacy Dungeons. I enforced this order with commenting in every section.
- The original Caves page was missing two: Sellia Hideaway and Auriza Side Tomb. These have been added.
- I changed Fort Haight from a legacy dungeon to a simple landmark. Calling it a legacy dungeon seemed a pretty extreme stretch, especially when all other (sometimes bigger) Forts weren't.
- In other tweaks, I renamed rememberances.yaml to be spelled correctly, remembrances.yaml. The page title was spelled correctly, so the html name didn't change and any links should be preserved.
- I moved Incantations below Sorceries in the list of pages, just because it seemed silly that we have Incantations on top when Sorceries are always listed first in-game.
- Next up is linking the locations of all these new Landmarks.

---
## [cadadr/configuration](https://github.com/cadadr/configuration)@[77bab15c41...](https://github.com/cadadr/configuration/commit/77bab15c41520dfe52cedf944ade9982d782e741)
#### Friday 2022-05-06 14:08:07 by İ. Göktuğ Kayaalp

pcmanfm fucking yeeted bloody yeeted

SEPARATE YOUR DAMN STATE FROM YOUR CONFIG GODDAMIT

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[cfc90a53ef...](https://github.com/zx2c4/linux-rng/commit/cfc90a53ef3a040cdbcdcfc138b8c3a2648a2536)
#### Friday 2022-05-06 14:41:15 by Jason A. Donenfeld

random: remove entropy estimation

The last vestiges of entropy estimation aren't helping with anything,
and as far as I can tell, haven't helped with anything for the last 3
years. It also introduces a side channel attack.

Way back when, we wanted as much entropy to accumulate as soon as
possible, because /dev/random would block often. To a degree we also
cared about boot blocking, but input events were rarely useful at boot,
and block has had limited contributions for a long time (rotational
disks only, generally). But moreover, mostly all systems that don't have
storms of interrupts and don't have RDRAND wind up getting seeded at
boot from jitter entropy. (Recall that the jitter bootstrapping was
added in response to ext4 becoming more efficient and not generating
enough block activity.) This is so much the case that in my testing,
I've been _unable_ to successfully seed a system using any meaningful
contribution from block or input randomness. In every configuration I
try, something else bootstraps it there first.

Secondly, for the last several years, the crng only reseeds itself every
5 minutes, leaving a full 5 minutes to accumulate entropy. With the
interrupt handler generally contributing at least 1 bit per second, this
is mostly already taken care of. Everything else helps, of course, but 5
minutes is a long time, and the combination of many different inputs
nearly always gets 256 bits accumulated in a 5 minute span. It's simply
not that hard. Again, this is because we no longer have the goal of
accumulating lots of entropy really fast to keep /dev/random flowing; we
just need 256 bits every 5 minutes. And with even more recent changes,
we don't have any requirements for how much we "need" every interval, so
this doesn't matter at all post-initialization.

For that reason, there's really no good purpose of having input or block
randomness contribute _more_ than 1 bit per event. So this commit makes
the conservative choice of just doing that.

Actually though, the stronger motivation for this patch is that the
entropy estimation arguably makes everything worse, by leaking
information to attackers about the contents of the pool! The file
/proc/sys/kernel/random/entropy_avail is readable by the world (which
isn't going to change for compatibility reasons), which means by simple
inspection, it's easy to see how many bits of entropy are added per
event. Since the entropy estimation uses the time, and the time is one
of the inputs to the input pool, this enables a side channel to glean
some information about what's going into the pool. It's not a lot of
information, but it's not nothing either, and so it's not a stretch to
say that the amount of unknown data added to the pool is less than what
it would have been without entropy estimation.

There's some argument to be made that the leak doesn't matter, since an
attacker observing entropy_avail could also just read it repeatedly and
see when it changes. However, this still requires a trip through the
scheduler, which means the information is probably delayed by some
amount. In contrast, the number of entropy bits estimated represents
something about the past that an attacker can reliably obtain in the
future, without a scheduler delay obscuring that information.

So since entropy estimation isn't helping us with much any more, and
only really serves to hurt us through a tiny side channel, let's just
get rid of it and credit 1 bit per event, like all the other sources of
entropy.

One point of concern is that the entropy estimator would sometimes
credit 0 bits, so in that sense perhaps always going with 1 bit
overestimates, but on the other hand, most of these events were being
double counted anyway by add_interrupt_randomness() (addressed in a
follow-up commit), the reduction of larger events to 1 bit largely
cancels out the increase of 0-bit events to 1, and in practice, 0 bit
events seem somewhat uncommon.  It also isn't necessarily correlated to
anything real -- which is why we're making this commit in the first
place -- considering that jiffies is so course in resolution.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [prymakD/CodeWars](https://github.com/prymakD/CodeWars)@[f42dd61b9e...](https://github.com/prymakD/CodeWars/commit/f42dd61b9e71056ee67964dc8345c36a93146dbf)
#### Friday 2022-05-06 15:45:39 by Danila

Create smallest.cpp

Every Christmas the good old man can go to every house in the world and leave gifts for the children who have been good throughout the year, but this is only possible because of his magic gift bag. It would be impossible for Santa to carry all the presents in his bag, the volume and weight of them all makes this obviously unfeasible. What actually happens is that your bag is a kind of magical portal to your gift factory at the North Pole. Where the presents are stacked by their elves and Noel always takes the gift from the top of that pile when he accesses his magical bag.

Gifts have a numerical measure of the degree of fun they can provide children, and Santa is always concerned with the least fun gift he will deliver throughout the night because he does not want any child to feel bad about it. you receive. However, this can not be done in advance because throughout the night as the good old man takes gifts from the pile to deliver, others are still being made and placed on the pile. So the most he can know is the value of the least fun present on the stack up to that point.

Your task is, given the sequence of operations done on the stack of gifts, answer Santa's queries about the value of the least entertaining gift on the stack thus far.

The first line of the input contains an integer N (1 ≤ N ≤ 106) corresponding to the number of operations performed on the present stack. The operations can be of three types: "PUSH V" where V (1 ≤ V ≤ 109) is an integer representing the degree of fun of the present being placed on the stack; "POP" which represents that Santa Claus is taking a gift from the cell to deliver and "MIN" representing a Noel query to know the smallest gift value in the stack.

The output consists of a line containing an integer with the smallest present value in the stack for queries of type "MIN" or "EMPTY" for "MIN" and "POP" operations when the stack is empty.

---
## [prymakD/CodeWars](https://github.com/prymakD/CodeWars)@[5a1c202281...](https://github.com/prymakD/CodeWars/commit/5a1c20228157dd1e50e0c6108e56ddbf0cc3e749)
#### Friday 2022-05-06 15:45:39 by Danila

Bishops

Yesterday was Sam's birthday. The most interesting gift was definitely the chessboard. Sam quickly learned the rules of chess and defeated his father, all his friends, his little sister, and now no one wants to play with him any more.

So he decided to play with another birthday gift – a Book of Math Problems for Young Mathematicians. He opened the book somewhere in the middle and read the following problem: "How many knights can be placed on a chessboard without threatening each other?" After a while he realized that this was trivial and moved on to the next problem: "How many bishops can be placed on a chessboard without threatening each other?". Sam is in trouble here. He is not able to solve this problem and needs your help.

Sam's chessboard has size N x N. A bishop can move to any distance in any of the four diagonal directions. A bishop threatens another bishop if it can move to the other bishop's position. Your task is to compute the maximum number of bishops that can be placed on a chessboard in such a way that no two bishops threaten each other.

The input file consists of several lines. The line number i contains a single positive integer N representing the size of the i-th chessboard. [1 <= N <= 10^100]

The output file should contain the same number of lines as the input file. The i-th line should contain one number – the maximum number of bishops that can be placed on i-th chessboard without threatening each other.

---
## [ChickenProp/haskell-hedgehog](https://github.com/ChickenProp/haskell-hedgehog)@[6ff06b1d22...](https://github.com/ChickenProp/haskell-hedgehog/commit/6ff06b1d22317dc1131f4c8aadca0684e2d40c59)
#### Friday 2022-05-06 16:00:58 by Phil Hazelden

Use state to update a Command's input.

This allows you to write commands whose input changes when a previous
Command shrinks.

For example, suppose the state contains `someList :: [Bool]` and
you have a command whose input expects "index into `someList` pointing
at `True`". You can generate that index directly, but if an earlier
command shrinks, `someList` might change and your index now points at
`False`.

(This is contrived, but hopefully points at the sorts of more
complicated situations where it might be useful.)

With this you can instead generate a number between 0 and (the number of
`True` elements). Then use `mkInput` to turn that number into an index
into `someList`. This will still be valid as long as the number of
`True` elements doesn't shrink below the generated value.

You could also pass this number directly into `exec`. But then in `exec`
you'd need to get `someList` directly from the concrete model, which
might be complicated and/or slow.

I implemented this by adding a new `Command` constructor, `CommandA`
where A is for Advanced. I don't love this. I could have simply changed
the existing constructor, but that means every existing Command needs to
be updated. (It's a simple change, `commandMkInput = const Just` means
they work as before, but still a massive pain.) The downside of this
approach is implementation complexity, plus any user functions taking a
`Command` as input may need to be updated.

Other approaches we could take here:

1. We could pass the concrete state into `exec` along with the concrete
input. Then you wouldn't need to get `someList` from the model. But you
might still need to do complicated calculations in `exec` which could
make the failure output hard to follow.

     If we did this we'd have the same tradeoff between changing the
     existing constructor and adding a new one.

2. We could add a callback

    ```haskell
    MapMaybeInput
      (state Symbolic -> input Symbolic -> Maybe (input Symbolic)
    ```

    Each of these would be applied in turn to update the input.
    (`Require` would be equivalent to a `MapMaybeInput` that ignores
    state, and either returns the input unchanged or `Nothing`.)

    This would be compatible with existing commands, but functions
    accepting a `Command` or a `Callback` as input might still need
    changing.

    The downside is that the generated type and the input type might be
    completely different, but this forces them to be the same. You can
    hack around that but it's gonna be ugly.

---
## [Tavelar/OddJobs-Backend](https://github.com/Tavelar/OddJobs-Backend)@[becdfc69da...](https://github.com/Tavelar/OddJobs-Backend/commit/becdfc69da419887f03b357935e07abddc33ba7e)
#### Friday 2022-05-06 16:11:04 by Tavelar

tims beautiful work, god hes so amazing i hate him so much

---
## [WebAssembly/binaryen](https://github.com/WebAssembly/binaryen)@[d1bea49163...](https://github.com/WebAssembly/binaryen/commit/d1bea49163be364d6f8b277b35510555211374b5)
#### Friday 2022-05-06 16:26:58 by Alon Zakai

TrapsNeverHappen mode (#4059)

The goal of this mode is to remove obviously-unneeded code like

(drop
  (i32.load
    (local.get $x)))

In general we can't remove it, as the load might trap - we'd be removing
a side effect. This is fairly rare in general, but actually becomes quite
annoying with wasm GC code where such patterns are more common,
and we really need to remove them.

Historically the IgnoreImplicitTraps option was meant to help here. However,
in practice it did not quite work well enough for most production code, as
mentioned e.g. in #3934 . TrapsNeverHappen mode is an attempt to fix that,
based on feedback from @askeksa in that issue, and also I believe this
implements an idea that @fitzgen mentioned a while ago (sorry, I can't
remember where exactly...). So I'm hopeful this will be generally useful
and not just for GC.

The idea in TrapsNeverHappen mode is that traps are assumed to not
actually happen at runtime. That is, if there is a trap in the code, it will
not be reached, or if it is reached then it will not trap. For example, an
(unreachable) would be assumed to never be reached, which means
that the optimizer can remove it and any code that executes right before
it:

(if
  (..condition..)
  (block
    (..code that can be removed, if it does not branch out..)
    (..code that can be removed, if it does not branch out..)
    (..code that can be removed, if it does not branch out..)
    (unreachable)))

And something like a load from memory is assumed to not trap, etc.,
which in particular would let us remove that dropped load from earlier.

This mode should be usable in production builds with assertions
disabled, if traps are seen as failing assertions. That might not be true
of all release builds (maybe some use traps for other purposes), but
hopefully in some. That is, if traps are like assertions, then enabling
this new mode would be like disabling assertions in release builds
and living with the fact that if an assertion would have been hit then
that is "undefined behavior" and the optimizer might have removed
the trap or done something weird.

TrapsNeverHappen (TNH) is different from IgnoreImplicitTraps (IIT).
The old IIT mode would just ignore traps when computing effects.
That is a simple model, but a problem happens with a trap behind
a condition, like this:

if (x != 0) foo(1 / x);

We won't trap on integer division by zero here only because of the
guarding if. In IIT, we'd compute no side effects on 1 / x, and then
we might end up moving it around, depending on other code in
the area, and potentially out of the if - which would make it happen
unconditionally, which would break.

TNH avoids that problem because it does not simply ignore traps.
Instead, there is a new hasUnremovableSideEffects() method
that must be opted-in by passes. That checks if there are no side
effects, or if there are, if we can remove them - and we know we can
remove a trap if we are running under TrapsNeverHappen mode,
as the trap won't happen by assumption. A pass must only use that
method where it is safe, that is, where it would either remove the
side effect (in which case, no problem), or if not, that it at least does
not move it around (avoiding the above problem with IIT).

This PR does not implement all optimizations possible with
TNH, just a small initial set of things to get started. It is already
useful on wasm GC code, including being as good as IIT on removing
unnecessary casts in some cases, see the test suite updates here.
Also, a significant part of the 18% speedup measured in

#4052 (comment)

is due to my testing with this enabled, as otherwise the devirtualization
there leaves a lot of unneeded code.

---
## [JerkyTreats/tetris](https://github.com/JerkyTreats/tetris)@[29db147d22...](https://github.com/JerkyTreats/tetris/commit/29db147d2231162d5e811392eb70a19f0eafc3b2)
#### Friday 2022-05-06 16:35:06 by JerkyTreats

Fully working BoardManager (WIP: Requires Cleanup)

This adds a working, if still messy, BoardManager. The requirements for the game is to have multiple Tetris games playable, so we need a way to turn games off and on in a controlled manner.

However, I do not want to strongly tie the implementation of the game to the management system- I want to turn games on and off without knowing or caring about the games specifically.

This led me to design this feature around interfaces. An `interface` defines common functionality across varying objects.

I started with the GameManager - the thing that turns boards on and off. It interacts with objects implementing the interface `IGameController`. The contract defined by this interface is all related to the lifecycle of our minigame (in this case, the only game so far is `TetrisClassic`).

I created a `GameController` class that implements the interface, and have TetrisClass inheriting from GameController. The idea here is that the GameController defines the basic interaction between Manager/Controller, but if there are new game modes down the line that need more specific implementation, we can implement the interface directly.

As the GameManager deals with the lifecycle of a game, it has to deal with Initialization of each game. This means that it is going to be taking pure data of a game and converting that data into the playable game. This requirement means that I also have to have my serializable data objects implementing a `IGameControllerData`.

The Manager only has knowledge of the abstracted interface methods. The data for each game type can vary wildly, but we need to guarantee data that the manager will use during the Initialization process. Therefore I have converted the `TetrisClassicData` from a struct to a class, so that it can implement the IGameControllerData interface, so that the Manager has the data it needs to implement.

I am shocked this is working, to be honest. I more than once felt that I had architected my way into a corner, and that the implementation of the system is overly-complex. That might still be true, but I believe the complexity helps scale with the intended complexity of the requirements- A lifecycle manager for a game session that does not care what that game actually is- just that it started, it ended, and it provided the feedback required to make those decisions.

---
## [Project-Zephyrus/meteoric_kernel](https://github.com/Project-Zephyrus/meteoric_kernel)@[38b0bd0f25...](https://github.com/Project-Zephyrus/meteoric_kernel/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Friday 2022-05-06 17:06:53 by Linus Torvalds

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[afa5ac922c...](https://github.com/mrakgr/The-Spiral-Language/commit/afa5ac922c059a208ba66c41a45325d1fb59abae)
#### Friday 2022-05-06 18:05:56 by Marko Grdinić

"10:25am. Yesterday my stress level was so high I did not even feel like watching Estab Life. Instead I skipped dinner and went to bed. I slept somewhat rough.

10:40am. I need to try taking it lighter today. It is hard to believe how not art, but just setting that monitor up yesterday stressed me out.

10:55am. Let me start. What do I need to get out of the way? Let me figure out why the monitor's pivot is off.

11am. Why isn't the scroll wheel working for zoom?

Now it works for some reason. Clarisse being Clarisse.

11:20am. Set it up. It is actually hard to do proper render previews in Clarisse as its renderer is so slow. If it is just this room, it would be better to do it in Blender. But I am persistent about doing it my way.

11:25am. Think about the topology has been stressing me for who long. Last night I finally came the conclussion that doing that monitor using sculpting would have been doable. When I started this, I didn't think it would because sculpting brushes are so imprecise and would wreck everything. But now that I know about lattices and projections, my view has changed. You could take a sculpting approach assuming you do not go at it with brushes, but instead use deformers for the subtle things..

The attempt when I tried retopoing using shrinkwrap and failed I regret not succeeding. I should not have failed in that approach. Instead I should have used the shrinkwrap in a more nuanced manner, doing localized projectsions whenever I needed precision.

I should have cut up the original model I was attempting to trace over in order prevent it from projecting to inner parts by accident.

I should also have used subdiv levels smartly. I could have even applied it once to get a good level of detail.

Those were all common sense things I could have done, but did not due to mental fog. I picked subdiv to get those smooth curves and good edge work, but the real star was the lattice.

11:40am. Subdiv is really great for edge work though, but not so great for general shaping.

11:50am. Enough let me stop messing with basic shapes. It is time to get started on the rig.

At this point, given how much time I've spent on 3d, I am starting to think there is a very real possibility, that I should have just gone with 2d. I am going to finish it this month. I need a more simplified approach. This way of doing things where I take days and days to get a single prop out is not viable for me. I had a success when I did that couch, it might be worth taking that kind of approach.

But for now forget it. Let me just do the rig.

12:55pm. Let me stop here for the morning. I was depressed going into it, but I stuck through, and I quite like Moi as a result of that. I need to give it enough time to at least finish the room project. My plan was to lean on 3d much more heavily, but it has been hard.

1:05pm. Oh yeah. I meant to write that I was wrong about boolean cuts messing up the topology. As long as you cut into planar faces, it is impossible that booleans would make them non planar. I was simply wrong about that. My apologies to Blender Bros. I was not thinking straight when I said that booleans would break the topology by making faces non planar. I am not sure if that is what I wrote, but that is what I was thinking.

Maybe the rought style they are using is not bad after all. This is just goes to show how torn I am on how art should be done.

2:20pm. Done with breakfast and chores.

Let me chill a bit and then I will resume.

2:40pm. Let me resume. Let me get this thing done.

2:55pm. Sigh. Let me stop here for a while.

The thought that I should stop doing 3d and instead move to 2d has entered my mind and will not let go.

3pm. Yeah, I am exhausted.

Juggling Moi, Substance, Blender, Clarisse is too much for me.

I do not want to spend all this effort texturing. I do not want to spend all this effort thinking about toplogy.

Moi is really a great program, but I keep thinking how I would do it in Blender, and it would be easier to correct myself there.

I've been working with Blender for so long at this point, that its way of doing things feels the most natural to me. Instead of texturing in Substance I really want to just slap on some basic shaders and call it a day.

I imported the monitor in Clarisse, and I really hate waiting for the ray tracing renderer to give me something decent. I hate it!

3:10pm. I do not want to do this in Moi. Yes, the bevels were a huge pain in the ass when I started, but now I completely understand them so I do not mind their idiosyncracies so much.

For those shading issues Josh suggested various hacky solutions to, a simple inset would take care of it.

3:15pm. I guess what really demoralized me with Moi is that I got some proportions wrong. This is nothing unusual and it is in fact expected for my first try. But it would have been so much easier to correct myself in a polygon based program.

3:25pm. Let me take a break just for a while. Mentally, I am at my limit. The burden of trying to master all these aspects of 3d is too much. I know that to really get the results I want using this approach, I really need a cloning machine as the amount of work is simply too overbearing.

https://youtu.be/8bmM1227MyY
How to create MASSIVE CITIES in Clarisse

Let me watch this. It is only 5m. After that, I am going to make my last experiment before I start cutting out aspects of my workflow. I want to try making the rig in Zbrush. I need to give the sculpting approach a proper chance. I need to know whether I want it or Blender.

4:05pm. No, forget Zbrush. While I've sunk in a good week into washing various tutorials on it, right now I am trying it out and am struggling with navigation. I am really a long way from being able to use it proficiently. I could do the rig in it assuming I am willing to spend a month really getting proficient with it.

It seems all the experience with Moi, Zbrush and other programs is really destined to come back to me in Blender. I really don't want to be using anything except Blender. I do not want to the hassle of getting used to Blender's strange navigation. Literally, everything I want, I could do in Blender. I knew that from the start. So why am I saying I'll do this last experiment. well, I sure did it.

https://youtu.be/kz2o5Uxjr2M
toposolve - Enter Meshmachine

Remember those cylinders by Ian. This is on the same theme.

https://youtu.be/kz2o5Uxjr2M?t=88

I'll probably end up modeling like this.

https://www.youtube.com/c/masterxeon1001/search?query=%23topsolve

This guy posts videos, much like I do these journal entries aparently.

4:30pm. Enough of this. Let me make my resolve.

Let me take a short break, and I will give it a try in making the rig in Blender.

4:40pm. I am going to kick Moi and Zbrush out of the running. Although I was not considering it, the same goes for Rhino. Houdini is out as well.

Blender, Clarisse and Substnace Painter. I'll restrict myself to those 3 tools only.

I won't aim to do texturing like I have before because it is a huge drain on my time. Amd Clarrise will only be there for massive env scenes, so I can forget it for a bit.

4:45pm. Sigh. It is almost dissapointing how easily this is coming to me in Blender. I really can call myself proficient in it.

4:45pm. This is a good chance to pick up Boxcutter. The rig has 50 or so grate holes on the sides. I could make a cube, and array it, but instead why don't I take the chance to increase my knowledge of Blender yet again? First let me install it.

Let me also try updating Zen UV. Ah, nevermind. That is not like BlenderKit which will fetch the latest version from the web.

Since a new version of MESHmachine is out, I can update that at least.

https://youtu.be/O9DkIz5ctmg
Learn Boxcutter in Blender in Under 10 Minutes

Got it installed. Let me watch this.

5:05pm. I do a cut, then I undo, and then the thing crashes. Is this another situation like with the MESHMachine? Zen UV is instable as well. Just what the hell is going on with pirate sites these days?

5:15pm. Let me try getting an more up to day version.

Hmmm, maybe I could go into the hard sculpting thread and get that old link from there. Maybe that one will work. I find it suspicious how these pirates sites seem to be crash happy.

I really hate the aeblender site for throwing popus and strong arming me to beg them on discord.

5:20pm. But this plugin seems to be solid. It works right and does not crash Blender when I try to undo.

5:35pm. Enough wasting time. Let me just do those grates. In the time it took me to get Boxcutter I could have long finished it in plain Blender.

5:55pm. I made a huge mistake. I should uninstall Hardops, Boxcutter and all those plugins. It is one thing if I was a pro churning out these assets by the truckload, but the mental overhead of having to juggle all these plugins is considerable. I was just about getting comfortable with Hard ops. I wasn't at all prepared to learn a completely new way of working today.

6:45pm. I am getting fucked up here by the rig.

The main problem is that I am on the verge of demoralization over how long 3d is taking to do anything. I really wanted to go on this journey so I could make something cool. But what is happening now is the opposite of that. It feels like I am drowing in details and not making progress.

Regarding the current issues facing me, what I need to get accustomed to are doing insets. I have it in my mind how I need to break things down.

I saw Josh do this before, but I've never tried doing serious cutting and insetting before. If it were the usual me, I jump into studying how to do it and master it. In fact, the rig is the ideal piece to try out the techniques that I've seen.

But right now, the thoughts that are going through my mind is - 'Why won't this ever end? I should be so much faster with this. The rig is something that should have been done in an hour, and yet I seem to be losing the battle against it.'

Those kinds of thoughts. I am really thinking of changing my approach. I want to try some drawing of still lives. I didn't expect 3d to have this much overhead. I am really getting my ass kicked by the objects that should be the simplest to do in 3d.

Let me get a new version of Clip Studio.

7:35pm. I had to go bed for a bit.

I wasn't ready to do the rig today it seems. I know exactly which moves need to be taken, but having several different ways of doing it in one's head is no good unless one of them ends up dominant.

7:40pm. What is my main problem? I need to just make up my mind to get busy with learning hard ops and box cutter.

I have to get good at that. I need to dedicate time to going through the docs and examples for each. Forget the rig. Bring in the basic cube, and experiment with all the different options.

I got just a tad familiar with Hard Ops, but having to deal with Boxcutter as well overwhelmed me.

7:45pm. I must not throw away the good because of the bad. If I get good at modeling, it will become faster than 2d. Shitty 2d will be faster, but not ray traced stuff in Cycles or Clarisse.

I came this far already. I know so much about modeling. Am I really going to give up just because I do not want to take the time to immerse myself into the two tools that I have and would rather let panic wash over me?

Yeah, I want to learn drawing, but what is the point in changing my approach at this point because of some difficulties. After Heaven's Key comes Hell's Prototype. I am going to get by with 2d for that. I can't just rely on illustration skills even if I had them unless I want to be permantently stuck doing 2d games.

Don't say it is only a rig. Say that it is an accomplishment to attain it. Once I start comparing myself to others mentally, I will become lost.

I need to focus all of my thoughts on this single goal.

Every prop has its own challenge.

7:55pm. I am going to dedicate the next few days to getting the rig done. So what if it is snail slow. I am going to optimize the workflow for dealing with the two addons, complete it and move on. Then I will do the rest of room without issue. Nothing besides the rig will give me any more trouble.

After that, if I want to I will allow myself to move form 3d art to something else. Doing a single mastery challenge is enough. But until then I should not quit no matter how long it takes. Anybody can go the other way as soon as he encounters a bit of hardship. The winners persevere."

---
## [RGBKnights/andril](https://github.com/RGBKnights/andril)@[471227398f...](https://github.com/RGBKnights/andril/commit/471227398f3caff83b74e39e894978dca3f93378)
#### Friday 2022-05-06 18:15:52 by esteban sustacha

Added multiple packages

Added the following packages:

AOE Magic Spell
Action RPG VFX
Dreamscape Nature
Fantasy Village Pack
Filo Cable Simulator
Low Poly AnAnimated Animals
Low Poly Wild Animals
Polygon Farm
Spells Pack
Stylized Medieval War Pack
2000 Fantasy Icons

---
## [Chromosore/dotfiles](https://github.com/Chromosore/dotfiles)@[072b1ce282...](https://github.com/Chromosore/dotfiles/commit/072b1ce282051998e0887746ef8a4a7a7e227afc)
#### Friday 2022-05-06 18:37:11 by Chromosore

revert(nvim): Remove the `gd` and `GD` mappings

Quick remainder: the other day I though "Oh well how could I optimise my
tab-switching workflow in neovim?". And I thought: "Yes, I'll introduce
new mappings! Brilliant!". Except that... No.

I'm kind of fine with the `gd` mapping, but `GD`... Just no. I realised
quite quickly my mistake when I tried to go to the end of the file. And
I *hate* waiting (btw I should do something for ds and cs, but it's
quite hard).

I tried to live with `GG` instead of `G`, but it just doesn't work. `G`
already requires you to shift, so pressing it twice makes it a cost 4
mapping (yeah I just made up this cost thing while writing).

So, I announce loudly that no, `gd` and `GD` aren't the solution to my
tab-switching workflow, and also that everyone underestimates `G` (no,
seriously, I didn't thought it'd be such a big deal).

(This experiment with new mappings lead me to think that I could
absolutely redesign the mapping system in vim. There are some
conventions already like the c <=> C / d <=> D relationship, but I think
that I could expand on this, with for instance a 0 <=> $ relationship
that would also apply to files, like g0 <=> g$, or even to paragraphs,
like {0 <=> {$ instead of { <=> }.)

---
## [kuroringo90/android_kernel_xiaomi_sm8150](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150)@[e08c94a926...](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150/commit/e08c94a9267a34fd325882f9fdd4928ea0052bb4)
#### Friday 2022-05-06 18:45:18 by Wang Han

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
Signed-off-by: Jebaitedneko <Jebaitedneko@gmail.com>

---
## [german-one/terminal](https://github.com/german-one/terminal)@[855e1360c0...](https://github.com/german-one/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Friday 2022-05-06 18:58:57 by Mike Griese

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
## [raujimenez/tiktok-discord-bot](https://github.com/raujimenez/tiktok-discord-bot)@[b5f7cf1dbd...](https://github.com/raujimenez/tiktok-discord-bot/commit/b5f7cf1dbd9ff4ad437b83a03bc2dac9a8c4f7e5)
#### Friday 2022-05-06 19:46:42 by Raul Jimenez

fix(versioning): fuck you microsoft for changing your dependencies for playwright docker, also fixing fuck up from versioning for TikTokApi

---
## [zeripath/gitea](https://github.com/zeripath/gitea)@[3725fa28cc...](https://github.com/zeripath/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Friday 2022-05-06 19:48:14 by Gusted

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
## [JalenPacker/Java-Projects](https://github.com/JalenPacker/Java-Projects)@[dc4d5bd0eb...](https://github.com/JalenPacker/Java-Projects/commit/dc4d5bd0ebd34a61ea412e88d233bdacac175f55)
#### Friday 2022-05-06 19:58:06 by JalenPacker

Create JobAssigner Description

In the Netflix original titled "The Society", an Orwellian teen apocalypse-esque show, one of the episodes has a former exemplary high school student now a delegated survivalist voluntarily create a program that allocates various jobs at random to all the schools' completely unsupervised students with the intent to establish structure to their crumbling, despair-imminent town. I personally felt inclined to emulate the program myself based on the Java experience I gained during high school; at this point, the most advanced coding I knew were Array Lists and a bit of recursion. A couple of years later, 2022, I stumbled upon the same program and improved it using professional, preferred program techniques  with descriptive comments and optimizing Hash Maps, switch statement statements, and for-each loops. The project attached here is the optimized version in Java Eclipse.

---
## [BMerullo/simply-recipes-tutorial](https://github.com/BMerullo/simply-recipes-tutorial)@[3561f7a473...](https://github.com/BMerullo/simply-recipes-tutorial/commit/3561f7a473a49938581cdb8f38ecd260253d6212)
#### Friday 2022-05-06 20:02:41 by Bob Merullo

removed slugify(fuck you so much slugify) to try and fix routing error

---
## [Urgau/cargo](https://github.com/Urgau/cargo)@[6a4d98d232...](https://github.com/Urgau/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Friday 2022-05-06 20:43:16 by bors

Auto merge of #10472 - epage:add, r=ehuss

feat: Import cargo-add into cargo

### Motivation

The reasons I'm aware of are:
- Large interest, see #5586
- Make it easier to add a dependency when you don't care about the version (instead of having to find it or just using the major version if thats all you remember)
- Provide a guided experience, including
  - Catch or prevent errors earlier in the process
  - Bring the Manifest format documentation into the terminal via `cargo add --help`
  - Using `version` and `path` for `dependencies` but `path` only for `dev-dependencies` (see crate-ci/cargo-release#288 which led to killercup/cargo-edit#480)

### Drawbacks

1. This is another area of consideration for new RFCs, like rust-lang/rfcs#3143 (this PR supports it) or rust-lang/rfcs#2906 (implementing it will require updating `cargo-add`)

2. This is a high UX feature that will draw a lot of attention (ie Issue influx)

e.g.
- killercup/cargo-edit#521
- killercup/cargo-edit#126
- killercup/cargo-edit#217

We've tried to reduce the UX influx by focusing the scope to preserving semantic information (custom sort order, comments, etc) but being opinionated on syntax (style of strings, etc)

### Behavior

Help output
<details>

```console
$ cargo run -- add --help
cargo-add                                                                                                                                  [4/4594]
Add dependencies to a Cargo.toml manifest file

USAGE:
    cargo add [OPTIONS] <DEP>[`@<VERSION>]` ...
    cargo add [OPTIONS] --path <PATH> ...
    cargo add [OPTIONS] --git <URL> ...

ARGS:
    <DEP_ID>...    Reference to a package to add as a dependency

OPTIONS:
        --no-default-features     Disable the default features
        --default-features        Re-enable the default features
    -F, --features <FEATURES>     Space-separated list of features to add
        --optional                Mark the dependency as optional
    -v, --verbose                 Use verbose output (-vv very verbose/build.rs output)
        --no-optional             Mark the dependency as required
        --color <WHEN>            Coloring: auto, always, never
        --rename <NAME>           Rename the dependency
        --frozen                  Require Cargo.lock and cache are up to date
        --manifest-path <PATH>    Path to Cargo.toml
        --locked                  Require Cargo.lock is up to date
    -p, --package <SPEC>          Package to modify
        --offline                 Run without accessing the network
        --config <KEY=VALUE>      Override a configuration value (unstable)
    -q, --quiet                   Do not print cargo log messages
        --dry-run                 Don't actually write the manifest
    -Z <FLAG>                     Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for
                                  details
    -h, --help                    Print help information

SOURCE:
        --path <PATH>        Filesystem path to local crate to add
        --git <URI>          Git repository location
        --branch <BRANCH>    Git branch to download the crate from
        --tag <TAG>          Git tag to download the crate from
        --rev <REV>          Git reference to download the crate from
        --registry <NAME>    Package registry for this dependency

SECTION:
        --dev                Add as development dependency
        --build              Add as build dependency
        --target <TARGET>    Add as dependency to the given target platform

EXAMPLES:
  $ cargo add regex --build
  $ cargo add trycmd --dev
  $ cargo add --path ./crate/parser/
  $ cargo add serde serde_json -F serde/derive
```

</details>

Example commands
```rust
cargo add regex
cargo add regex serde
cargo add regex@1
cargo add regex@~1.0
cargo add --path ../dependency
```
For an exhaustive set of examples, see [tests](https://github.com/killercup/cargo-edit/blob/merge-add/crates/cargo-add/tests/testsuite/cargo_add.rs) and associated snapshots

Particular points
- Effectively there are two modes
  - Fill in any relevant field for one package
  - Add multiple packages, erroring for fields that are package-specific (`--rename`)
  - Note that `--git` and `--path` only accept multiple packages from that one source
- We infer if the `dependencies` table is sorted and preserve that sorting when adding a new dependency
- Adding a workspace dependency
  - dev-dependencies always use path
  - all other dependencies use version + path
- Behavior is idempotent, allowing you to run `cargo add serde serde_json -F serde/derive` safely if you already had a dependency on `serde` but without `serde_json`
- When a registry dependency's version req is unspecified, we'll first reuse the version req from another dependency section in the manifest.  If that doesn't exist, we'll use the latest version in the registry as the version req

### Additional decisions

Accepting the proposed `cargo-add` as-is assumes the acceptance of the following:
- Add the `-F` short-hand for `--features` to all relevant cargo commands
- Support ``@`` in pkgids in other commands where we accept `:`
- Add support for `<name>`@<version>`` in more commands, like `cargo yank` and `cargo install`

### Alternatives

- Use `:` instead of ``@`` for versions
- Flags like `--features`, `--optional`, `--no-default-features` would be position-sensitive, ie they would only apply to the crate immediate preceding them
  - This removes the dual-mode nature of the command and remove the need for the `+feature` syntax (`cargo add serde -F derive serde_json`)
  - There was concern over the rarity of position-sensitive flags in CLIs for adopting it here
- Support a `--sort` flag to sort the dependencies (existed previously)
  - To keep the scope small, we didn't want general manifest editing capabilities
- `--upgrade <POLICY>` flag to choose constraint (existed previously)
  - The flag was confusing as-is and we feel we should instead encourage people towards `^`
- `--allow-prerelease` so a `cargo add clap` can choose among pre-releases as well
  - We felt the pre-release story is too weak in cargo-generally atm for making it first class in `cargo-add`
- Offer `cargo add serde +derive serde_json` as a shorthand
- Infer path from a positional argument

### Prior Art

- *(Python)* [poetry add](https://python-poetry.org/docs/cli/#add)
  - `git+` is needed for inferring git dependencies, no separate  `--git` flags
  - git branch is specified via a URL fragment, instead of a `--branch`
- *(Javascript)* [yarn add](https://yarnpkg.com/cli/add)
  - `name@data` where data can be version, git (with fragment for branch), etc
  - `-E` / `--exact`, `-T` / `--tilde`, `-C` / `--caret` to control version requirement operator instead of `--upgrade <policy>` (also controlled through `defaultSemverRangePrefix` in config)
  - `--cached` for using the lock file (killercup/cargo-edit#41)
  - In addition to `--dev`, it has `--prefer-dev` which will only add the dependency if it doesn't already exist in `dependencies` as well as `dev-dependencies`
  - `--mode update-lockfile` will ensure the lock file gets updated as well
- *(Javascript)* [pnpm-add](https://pnpm.io/cli/add)
- *(Javascript)* npm doesn't have a native solution
  - Specify version with ``@<version>``
  - Also overloads `<name>[`@<version>]`` with path and repo
    - Supports a git host-specific protocol for shorthand, like `github:user/repo`
    - Uses fragment for git ref, seems to have some kind of special semver syntax for tags?
  - Only supports `--save-exact` / `-E` for operators outside of the default
- *(Go)* [go get](https://go.dev/ref/mod#go-get)
  - Specify version with ``@<version>``
  - Remove dependency with ``@none``
- *(Haskell)* stack doesn't seem to have a native solution
- *(Julia)* [pkg Add](https://docs.julialang.org/en/v1/stdlib/Pkg/)
- *(Ruby)* [bundle add](https://bundler.io/v2.2/man/bundle-add.1.html)
  - Uses `--version` / `-v` instead of `--vers` (we use `--vers` because of `--version` / `-V`)
  - `--source` instead of `path` (`path` correlates to manifest field)
  - Uses `--git` / `--branch` like `cargo-add`
- *(Dart)* [pub add](https://dart.dev/tools/pub/cmd/pub-add)
  - Uses `--git-url` instead of `--git`
  - Uses `--git-ref` instead of `--branch`, `--tag`, `--rev`

### Future Possibilities

- Update lock file accordingly
- Exploring the idea of a [`--local` flag](https://github.com/killercup/cargo-edit/issues/590)
- Take the MSRV into account when automatically creating version req (https://github.com/killercup/cargo-edit/issues/587)
- Integrate rustsec to report advisories on new dependencies (https://github.com/killercup/cargo-edit/issues/512)
- Integrate with licensing to report license, block add, etc (e.g. https://github.com/killercup/cargo-edit/issues/386)
- Pull version from lock file (https://github.com/killercup/cargo-edit/issues/41)
- Exploring if any vendoring integration would be beneficial (currently errors)
- Upstream `cargo-rm` (#10520), `cargo-upgrade` (#10498), and `cargo-set-version` (in that order of priority)
- Update crates.io with `cargo add` snippets in addition to or replacing the manifest snippets

For more, see https://github.com/killercup/cargo-edit/issues?q=is%3Aissue+is%3Aopen+label%3Acargo-add

### How should we test and review this PR?

This is intentionally broken up into several commits to help reviewing
1. Import of production code from cargo-edit's `merge-add` branch, with only changes made to let it compile (e.g. fixing up of `use` statements).
2. Import of test code / snapshots.  The only changes outside of the import were to add the `snapbox` dev-dependency and to `mod cargo_add` into the testsuite
3. This extends the work in #10425 so I could add back in the color highlighting I had to remove as part of switching `cargo-add` from direct termcolor calls to calling into `Shell`

Structure-wise, this is similar to other commands
- `bin` only defines a CLI and adapts it to an `AddOptions`
- `ops` contains a focused API with everything buried under it

The "op" contains a directory, instead of just a file, because of the amount of content.  Currently, all editing code is contained in there.  Most of this will be broken out and reused when other `cargo-edit` commands are added but holding off on that for now to separate out the editing API discussions from just getting the command in.

Within the github UI, I'd recommend looking at individual commits (and the `merge-add` branch if interested), skipping commit 2.  Commit 2 would be easier to browse locally.

`cargo-add` is mostly covered by end-to-end tests written using `snapbox`, including error cases.

There is additional cleanup that would ideally happen that was excluded intentionally from this PR to keep it better scoped, including
- Consolidating environment variables for end-to-end tests of `cargo`
- Pulling out the editing API, as previously mentioned
  - Where the editing API should live (`cargo::edit`?)
  - Any more specific naming of types to reduce clashes (e.g. `Dependency` or `Manifest` being fairly generic).
- Possibly sharing `SourceId` creation between `cargo install` and `cargo edit`
- Explore using `snapbox` in more of cargo's tests

Implementation justifications:
- `dunce` and `pathdiff` dependencies: needed for taking paths relative to the user and make them relative to the manifest being edited
- `indexmap` dependency (already a transitive dependency): Useful for preserving uniqueness while preserving order, like with feature values
- `snapbox` dev-dependency: Originally it was used to make it easy to update tests as the UX changed in prep for merging but it had the added benefit of making some UX bugs easier to notice so they got fixed.  Overall, I'd like to see it become the cargo-agnostic version of `cargo-test-support` so there is a larger impact when improvements are made
- `parse_feature` function: `CliFeatures` forces items through a `BTreeSet`, losing the users specified order which we wanted to preserve.

### Additional Information

See also [the internals thread](https://internals.rust-lang.org/t/feedback-on-cargo-add-before-its-merged/16024).

Fixes #5586

---
## [MineClone2/MineClone2](https://github.com/MineClone2/MineClone2)@[5f126c4686...](https://github.com/MineClone2/MineClone2/commit/5f126c468650577ea0baefb5d79b81835fe33579)
#### Friday 2022-05-06 21:01:35 by cora

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
## [GetComponents/Catflife](https://github.com/GetComponents/Catflife)@[0fa986c6d0...](https://github.com/GetComponents/Catflife/commit/0fa986c6d02db3f755d24f3061727dcabe3f3cdc)
#### Friday 2022-05-06 21:27:05 by Jan Pluschkell

Implemented Tims shit bitch fuck + UI render layer

---
## [sunset-wasteland/sunset-wasteland](https://github.com/sunset-wasteland/sunset-wasteland)@[28d5794423...](https://github.com/sunset-wasteland/sunset-wasteland/commit/28d57944238656c75d3283c37c7a5453ce10e640)
#### Friday 2022-05-06 23:35:19 by Shane Merrol

disables fermichem for synthtissue

Fuck fermichem, all my homies hate fermichem

Jokes aside, you need it for organ repair surgery, and it's a QoL change for FoA

---

