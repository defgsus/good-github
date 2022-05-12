## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-11](docs/good-messages/2022/2022-05-11.md)


1,789,387 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,789,387 were push events containing 2,897,977 commit messages that amount to 198,115,763 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [stemnic/binutils-gdb](https://github.com/stemnic/binutils-gdb)@[cb2cd8cba8...](https://github.com/stemnic/binutils-gdb/commit/cb2cd8cba82a0a5480a147d95b16098ad74d33c6)
#### Wednesday 2022-05-11 00:00:09 by Pedro Alves

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
## [shobbs528/FinalProject_a3](https://github.com/shobbs528/FinalProject_a3)@[95bda50e70...](https://github.com/shobbs528/FinalProject_a3/commit/95bda50e70e6f127a320743f05666adca4861bcc)
#### Wednesday 2022-05-11 00:02:50 by Samwich422

omg fucking god something went right

kay, the headlights are good now.

---
## [CandleJaxx/Skyrat-tg](https://github.com/CandleJaxx/Skyrat-tg)@[52dbce8997...](https://github.com/CandleJaxx/Skyrat-tg/commit/52dbce8997f420c803197faf0aa38ee36c93246e)
#### Wednesday 2022-05-11 00:21:41 by SkyratBot

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
## [ProfessorPopoff/mojave-sun-13](https://github.com/ProfessorPopoff/mojave-sun-13)@[9fbcb32a6d...](https://github.com/ProfessorPopoff/mojave-sun-13/commit/9fbcb32a6d72113b5ac781a61c5a6e12a47ebf5f)
#### Wednesday 2022-05-11 01:22:31 by tralezab

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
## [GolfinhoVoador/tgstation](https://github.com/GolfinhoVoador/tgstation)@[27946f516d...](https://github.com/GolfinhoVoador/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Wednesday 2022-05-11 01:50:11 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [Talking-Chicken/TimHub](https://github.com/Talking-Chicken/TimHub)@[37b5216f82...](https://github.com/Talking-Chicken/TimHub/commit/37b5216f82e2e17fd645befb12a1844e705a76ce)
#### Wednesday 2022-05-11 02:54:31 by Max Seavey

fixed playtest note issues

- Tape timling not intractable
- Fridge gremlin has no portrait
- baby heads and bodega table text need to be flip flopped
- toothpastes might be good to be enlarged a bit
- mountimdew timling makes penne go to a weird location, still has placeholder portrait
- wisdom tooth needs final sprite?
- rug lady should not have physics, can’t be spoken to
- note for max: change church Tim painting origin point to be higher
- move confession log book closer to the booth so it looks like it just accidentally fell out
- Nero and Tim should be disabled in secret room
- change like spacing of case report submission
- hard to see everything — especially will — against pasta ground
- will needs to not have physical collider
- FADE TO BLACK IS TOO FAST AND CANT SEE ENDING DISLOGUE

---
## [ChirayuRai/CS2640_HANGMAN](https://github.com/ChirayuRai/CS2640_HANGMAN)@[435af08d35...](https://github.com/ChirayuRai/CS2640_HANGMAN/commit/435af08d35b1c34dcdac0d51d0c1be293d7391c0)
#### Wednesday 2022-05-11 04:08:30 by ChirayuRai

finally fucking done with this piece of shit god damn fucking bitch ass code fuck you fuck your mom i hate you

---
## [madfu/DotNetty](https://github.com/madfu/DotNetty)@[f8250adf7b...](https://github.com/madfu/DotNetty/commit/f8250adf7bc76b78b937abcaad355d82ff83a684)
#### Wednesday 2022-05-11 04:32:39 by madfu

amazing what a couple of small changes will do (and won't).

the goal for this commit was just to alter the code enough to get a set of DLLs
imported into Unity that didn't crash on import.  that has been accomplished, but
with a compromise: we might have to give up using DotNetty.Protobuf in this first
design.

the story behind the reasons is long, but the upshot is that the .Net build process
does not allow for the manipulation of dependencies of dependencies.  this is something
i take for granted coming out of Java, where through Maven you can suppress an old
version of a package in a dependency, so that only a newer one has precedence.

in .Net, the two competing packages just collide.  the solution according to Microsoft:

“To resolve incompatibilities, do one of the following:

* Retarget your project to a framework that is supported by the packages you want to use.

* Contact the author of the packages and work with them to add support for your chosen
framework. Each package listing page on nuget.org has a Contact Owners link for this purpose.”

so, if the author is Google and the package is Google.Protobuf, good luck getting them to
work with you...and i don't say this out of hand.  i went and read some of the comments.

so, as i see it i have two possible solutions:

1) clone the Google.Protobuf repo, make the changes, build it myself, and then figure out
how to pull it into DotNetty.Protobuf,

or

2) just do without DotNetty.Protobuf.

tonight, i'm choosing the latter, but who knows how i'll feel tomorrow.

on the Unity side, i'll proceed with all the DotNetty DLLs except DotNetty.Protobuf.
this is a more comprehensive set of DLLs than what wizard872 used, so hopefully they all work.

one thing to note is that there are a couple of projects that have done PRs and such to the
Google code with suggestions on how Google might improve the code for compatibility with
Unity.  will have to take a look at those.

now for the stuff that did work...

* Unity had multiple complaints about the import, but after adjusting the API Compatibility Level
to .Net 4.x, and the Scripting Backend to IL2CPP, most went away.  those that did not involved
upgrading dependencies.

* Google.Protobuf was upgraded to version 3.20.1 (which doesn't solve the ultimate problem).

* System.Diagnostics.DiagnosticSource was added to the DotNetty.Common package at version 5.0.0.

because we're on the newer version of NuGet, these changes were made in the .csproj files below.

	modified:   src/DotNetty.Codecs.Protobuf/DotNetty.Codecs.Protobuf.csproj
	modified:   src/DotNetty.Common/DotNetty.Common.csproj

* the last change was just adding a directory to coalesce the DLLs before bringing them into Unity.
i don't want to commit that to the repo, so .gitignore got a visit.

	modified:   .gitignore

that's it...END-OF-LINE...

---
## [macdice/postgres](https://github.com/macdice/postgres)@[c40ba5f318...](https://github.com/macdice/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Wednesday 2022-05-11 05:29:55 by Tom Lane

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a3c8013b45...](https://github.com/tgstation/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Wednesday 2022-05-11 06:49:17 by GoldenAlpharex

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
## [QueIvan/library-manager](https://github.com/QueIvan/library-manager)@[2d63379131...](https://github.com/QueIvan/library-manager/commit/2d63379131bea06f13d90d40aa133cde850969f5)
#### Wednesday 2022-05-11 10:12:37 by Jan Szewczyk

Merge pull request #11 from QueIvan/dev

Full blown refactor (FUCK YOU CEZIK)

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[fb5cf9102e...](https://github.com/Hekzder/mojave-sun-13/commit/fb5cf9102e3f942b3b47e985a4dc19d671932b3e)
#### Wednesday 2022-05-11 10:20:44 by LemonInTheDark

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
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[ba8e590fea...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/ba8e590fea897304bb5155f66965fd473a7c8c2f)
#### Wednesday 2022-05-11 10:55:50 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [BenjaminKing1337/fullstack_project-Sable](https://github.com/BenjaminKing1337/fullstack_project-Sable)@[685a7d2680...](https://github.com/BenjaminKing1337/fullstack_project-Sable/commit/685a7d268069731c01272a59ef77aa1b3386900e)
#### Wednesday 2022-05-11 11:14:52 by BenjaminKing1337

Want to learn the intricacies of coding?

WELL :D :D :D FUCK YOU :D :D :D

---
## [BenjaminKing1337/fullstack_project-Sable](https://github.com/BenjaminKing1337/fullstack_project-Sable)@[47e659d247...](https://github.com/BenjaminKing1337/fullstack_project-Sable/commit/47e659d2477d37ca1ff13184fb8cac1e2e2bcda4)
#### Wednesday 2022-05-11 11:19:57 by BenjaminKing1337

stupid ass fucking bullshit

shit stopped worked over night like FUCK

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ea4ef85825...](https://github.com/mrakgr/The-Spiral-Language/commit/ea4ef85825739fbdb9eb3fe78ecfc00a3d689dda)
#### Wednesday 2022-05-11 11:20:22 by Marko Grdinić

"10:10am. I am up. Let me chill and I will start. Let me check out the Moi thread. Actually, I'll do that after I finish chilling.

10:15am. First Frieren.

10:25am. Oh by the way, it really does make me happy that BTC finally started collapsing. I wasn't sure whether it would go for another bull run, but this should be enough to finally get the bear market started. That is how I feel. Watching the financial markets and speculating every once in a while is the closest to what I would call to me having a hobby.

10:50am. I am ready to start. But first, I have to do some chores around the house. I'll be back soon.

10:55am. Let me check out the Moi forum. I wonder what he will say about the intersection curves? My bet is that Rhino simply does them differently and gives surfaces instead.

///

Hi MRAKGR,

re:
> I've run into problems with booleans a few times today, and indeed, extending the cutter
> a bit did solve the issue.

Also what version of MoI are you using? There are some tune ups to booleans in the v5 beta.

I have not been able to test if those changes are significant for what you are running into
since you have not posted any model files.

> But if intersect just gives curves what use is it for booleans? For a boolean of two solids
> wouldn't you need an intersecting surface instead?

The booleans use the intersection curves to partition the 2 solids into different chunks of
connected faces and then those chunks are either combined with others or discarded
depending on what volume they are contained inside of.

- Michael

///

I get the feeling he really wants me to post those model files. I guess I could. Let me start with that.

11:10am. No, it is not replicating. Right now the boolean works properly for me. Lame.

11:20am. Let me start work on finishing the rig.

Focus me. Just make that hexagonal grid.

11:55am. Hmm, this pattern on the side is quite intricate. At first I thought it was just a copy of the one on the top, but it is not. Instead of being hexagonal dents, it actually extrudes upwards.

12:10pm. What is distance from edge in the move tool?

Right now I want to move a bunch of cirles and it is hell as it keeps snapping to points. How about I just turn off object snapping? Let me take a short break here.

12:30pm. Let me resume.

1:15pm. Let me stop here for breakfast. I am almost done with it. I am starting to get skeptical of whether I should be using the pen here as it is less accurate than a mouse and is putting strain on my hand. A pen is useful only when you want to make strokes, but if you are just placing points the benefit of that goes away. But it is good practice for using the pen so I might as well go for it."

---
## [olsamtech/Olsamtech](https://github.com/olsamtech/Olsamtech)@[7c6523e236...](https://github.com/olsamtech/Olsamtech/commit/7c6523e2367345f243307392e0f84351978d274b)
#### Wednesday 2022-05-11 12:13:47 by olsamtech

Update README.md

Hi,
I am Olsam, a computer science graduate, software developer, mobile application and game developer.
We are a team of freelancers (organization named Olsamtech). We have 3+ years of experience in this field.
We are the trusted partner for some of the world’s leading enterprises and businesses. We have helped bring ideas to life while building sustainable business practices across industries. 
We build highly affordable custom software for companies large and small by applying modern design principles, in conjunction with the latest in cloud, mobile, and desktop technologies, we create tailored solutions that connect co-workers with each other and companies with their customers, simplify and accelerate business processes, and lower costs.

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[de7e66b921...](https://github.com/canalplus/rx-player/commit/de7e66b921dc8c803cafd38b4d25bd1c9c82d777)
#### Wednesday 2022-05-11 13:35:57 by Paul Berberian

HTMLMediaElement's related error have now the initial message if it exists

I was very shamefully not aware that `MediaError`s as emitted by
HTMLMediaElement could have a `message` property describing the actual
problem.

For my defense, this was not always the case for MediaErrors (I found
some w3c and chrome links to prove it!).
Yet it apparently is since 2017, so my defense is still pretty weak.

Relying on those could definitely have saved us many hours of debugging
over the years, where we were trying to find which segment of which
type provoked a MEDIA_ERR_DECODE and why.

Anyway, I prefer not to think to much about it, here it is, and now it's
available: the corresponding error message will actually be the message
of the corresponding `RxPlayer`'s `MediaError`'s message (yes, both the
native browser error and the RxPlayer supplementary layer have the
exact same name, and no, it cannot be a source of confusion at all, why
would you say that?).

---
## [Amirirany3031/Amirirany3031](https://github.com/Amirirany3031/Amirirany3031)@[79bad1b6cd...](https://github.com/Amirirany3031/Amirirany3031/commit/79bad1b6cdf191a3246508fcd132a128ac7941ad)
#### Wednesday 2022-05-11 14:16:28 by Amirirany3031

Update README.md

I'm elite in the theory of general economic and political analyst elite public issues where experience has earned my ideas creative can a group with the idea of a new unraveling and solving the problems that the first idea about the secret of currencies sports CRYPTOCard  or FIFA token at the beginning if financially programming anyone can support the idea of value with the efficiency of early gave Ibn first idea that my name and my idea to the Dome's pool complete description with contact e-mail me  amirnaji3031@gmail.com can get these ideas can Aydhvhay registered and many more with a fair amount of testing they can do and the ideas I use in my Akhtyarshvn of food to Bsylry of professionals by international and economic crisis Da Dhya  can with these ideas we fix ideas incomplete you Da sharp full Mbknm I Javad Afshar Beck elite and theoreticians on issues of international and economic issues Hytm idea Chrdazy and theories of conduct path of humanity can not change me Abnha da Abnja expression  has got friends who need to  Working with me as co-Sadiq his side have the world's elite with his theories will change sides unsurpassed in every issue of the war to CRYPTOCard and tokens fix global drought ahead because of the accuracy of congenital Les atoms  any device with Daft reviews Mbknm to all of the body, I Beck elite theory and the theory of'm the isolation of people like me is that the world's current situation Rsbdh to please every Znynh Burley try just ask and solutions you want me  the solution to solve any problem within a minute can respond Bassem so little thought in 10 minutes to the best thought and Jzr in any Nvzvy believe it or not, but science and philosophy Gshlysh general situation every problem in the world insisted that every problem in the world.  My school gifted and elite several years I studied at university very well Thsyl Chrome but a lot of time ahead Hineman Mtavrs Meg first before you come in for work in the United Arab Emirates Post and plans had been made, and waiting for a reply was a few weeks  after the project name and the company name was registered Mtavrs I originally plan  Theft Shdsh My original plan had I not called me and Bdlbl failure to register Mtavrs called me the plan were robbed of UAE Arabic and Mtvrs, and Lee plans that Mtavrs against which nothing As for plans to pass many tests  in my mind there is surprisingly a sponsor or bought plans, economic and new CRYPTOCard or tokens to solve climate problems and all the problems that the world is important not Burley personal goal is to change the tactical economies in the world to prosperity  Mrvm the world and on all issues of implementation Bsylr resolve this, but apparently some do not see or know the problem

---
## [Ankitsoran/Malignant-comment-classifier](https://github.com/Ankitsoran/Malignant-comment-classifier)@[bb8194918d...](https://github.com/Ankitsoran/Malignant-comment-classifier/commit/bb8194918d4f7fd237c68d4a838c59cb37332e15)
#### Wednesday 2022-05-11 14:47:34 by Ankit soran

Update README.md

Due the penetration of the internet in all domains of life which has led to increase of people’s participation actively
and give remarks as an issue of communicating their concern/feedback/opinion in various online forums. Although
most of the times these comments are helpful for the creator toextemporize the substance that is being provided to
people, but sometimes these may be abusive and create hatred-feeling among the people. Thus as these are openly
available to the public which is being viewed from various sections of the society, people in different age groups,
different communities and different socio-economic background, it becomes the prime responsibility of the
content-creator ( the host) to filter out these comments in order to stop the spread of negativity or hatred within
people.
Lately there has been many cases in which the growing menace of hate and negativity has been witnessed in the
online platforms especially social media as such, many governments around the world has seen the rise of cases
related to cyber bullying that has led to spread of hatred and violence.
Since the democratization of substance creation following the dispatch of web-based media stages, every single
one of us has become content makers making and distributing our own substance, which thus has made a
framework where the nature of distributed substance cannot, at this point be controlled. The effect of the most
recent twenty years' innovation unrest is presently affecting organizations, political frameworks, family lives,
society, and individuals 
.
Detecting Toxic comments has been a great challenge for the all the scholars in the field of research and
development. This domain has drawn lot of interests not just because of the spread of hate but also people refraining
people from participating in online forums which diversely affects for all the creators/content-providers to provide
a relief to engage in a healthy public interaction which can be accessed by public without any hesitation.
There have been sure turns of developments in this area which includes couple of models served through API. But
the models still make errors and still fail to provide an accurate solution to the problem and may need more clarification and develpment in future

---
## [UnderscoreSquad/UnderscoreGame](https://github.com/UnderscoreSquad/UnderscoreGame)@[b4a4f2a14b...](https://github.com/UnderscoreSquad/UnderscoreGame/commit/b4a4f2a14b7e387bd7e5a48108256cd66f621d1e)
#### Wednesday 2022-05-11 15:41:43 by XENON

DSFSDFdsfg

HOLY FUCKING SHITTTT
SO MUCH CHANGED FILES BUT THEY ARENT
WHY
WHY

---
## [Dorsisdwarf/tgstation](https://github.com/Dorsisdwarf/tgstation)@[d411393e72...](https://github.com/Dorsisdwarf/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Wednesday 2022-05-11 15:51:51 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [Dorsisdwarf/tgstation](https://github.com/Dorsisdwarf/tgstation)@[4652d4bb63...](https://github.com/Dorsisdwarf/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Wednesday 2022-05-11 15:51:51 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [Dorsisdwarf/tgstation](https://github.com/Dorsisdwarf/tgstation)@[b86cf89125...](https://github.com/Dorsisdwarf/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Wednesday 2022-05-11 15:51:51 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [m-falkowski1/linux](https://github.com/m-falkowski1/linux)@[213d266ebf...](https://github.com/m-falkowski1/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Wednesday 2022-05-11 16:04:00 by Linus Torvalds

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
## [joast/newsboat](https://github.com/joast/newsboat)@[2dd8022096...](https://github.com/joast/newsboat/commit/2dd8022096590b6042948687dfc69d7b39198334)
#### Wednesday 2022-05-11 16:21:29 by Lysander Trischler

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
## [OpenAngelArena/oaa](https://github.com/OpenAngelArena/oaa)@[841368b6b0...](https://github.com/OpenAngelArena/oaa/commit/841368b6b064c700c6194d8e46d798e0d4494ed1)
#### Wednesday 2022-05-11 16:21:39 by Darko V

Modifiers changes (May 2022) (#3351)

* Cycled Out modifiers: Hyper Lifesteal, Blood Magic, Healer and Brute.
* Randomize button will no longer randomize the 'None' option.
* Buffed Timeless Relic modifier from 25% to 30%.
* Telescope modifier now also provides 400 bonus vision (day/night).
* Fixed Telescope modifier cast range bonus not stacking with other cast range bonuses.
* Fixed Creed of Omniscience and Telescope neutral items cast range bonuses not stacking with Octarine Core or Far Sight cast range bonuses.
* Random Draft number of banned heroes increased from 70 to 75.
1) Added Aghanim, Nimble and Sorcerer modifiers.
2) Updated tooltip for Wisdom modifier.
3) Bonus AoE/Radius modifier now ignores:
- Arc Warden Flux search radius
- Drow Ranger agility range penalty
- Monkey King Wukong's Command
- Phantom Assassin Blur
- Spectre Desolate
4) Bonus AoE/Radius now improves Sohei's Dash width.
5) Diarrhetic auto-poop-ward check-for-wards-radius increased from 200 to 300. This means auto-pooped wards will be farther from each other.
6) Explosive Death modifier will now proc on Tempest Doubles and heroes that are reincarnating.
7) Attack Range Switch modifier bonus attack range reduced from 600 to 500.
8) Attack Range Switch modifier bonus projectile speed increased from 900 to 1100.
9) Added Max Power modifier
10) Fixed tooltip for modifiers saying undefined when 'Random' option is selected.

---
## [jaaat4u/NikoKernel](https://github.com/jaaat4u/NikoKernel)@[73e600de91...](https://github.com/jaaat4u/NikoKernel/commit/73e600de911bf35a46f0ae117137faaad44bb3bc)
#### Wednesday 2022-05-11 16:35:55 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: Devang Chaudhary <devangsingh369@gmail.com>

---
## [FoxGamingYTCR/BATCH-FILE](https://github.com/FoxGamingYTCR/BATCH-FILE)@[0935cf0677...](https://github.com/FoxGamingYTCR/BATCH-FILE/commit/0935cf0677c5e64f9290786234ec28f92701918c)
#### Wednesday 2022-05-11 17:00:12 by FOX GAMINGYT

funny fake virus prank (flashing lights warning)

it is just a prank and it has a lot of flashing/changing colors so be aware of that... it is fun to use on friends though or make your parents/friends think you've been hacked!! XD

---
## [FlameArrow57/goon-flock](https://github.com/FlameArrow57/goon-flock)@[bdad398f9e...](https://github.com/FlameArrow57/goon-flock/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Wednesday 2022-05-11 17:20:43 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1393591c90...](https://github.com/mrakgr/The-Spiral-Language/commit/1393591c900d14163aa65cfbf599a1f79e4951dc)
#### Wednesday 2022-05-11 17:39:35 by Marko Grdinić

"2:20pm. I thought it would be chilling for longer...let me check out the Birdie Wing thread for just like 5m, and then I will resume.

Ah, fuck. It occured to me to wonder about this just now. It seems that the grate I did and unioned to the main shape is not hollow anymore.

Nevermind that. First let me post the model on the Moi forum and ask them how they would appoach the hole drilling problem.

2:25pm. I am trying to upload the rig, but I keep getting server errors. Nevermind this for now. I'll try posting it later. Right now, let me just redo that grate.

2:40pm. Focus me. Let me break out the pen.

2:50pm. This is ridiculous. Now the network is not acting properly for me.

Let me try uploading the grate error again.

3:15pm. Instead of doing art, I am trying to work around the error cause by nurbs based modeling. One operation would work, the other would mysteriously fail.

3:30pm. Right now I am taking a break to think about it.

4:25pm. Done with it. Holy shit. I newer thought this simple thing would take this long. Forget unioning the grate.

The reason it took so long is because when I modeled the grate I kept running into weird errors with the network node. I can only imagine it was out sync or something.

I am going to count this as a minus in favor of using Moi. Let me just make those screws and I will be done.

https://youtu.be/ewy1WUj-ggc
ZBrush Tutorial - Custom Navigation Middle Mouse Scroll

Let me just watch this.

I really hate using right click to navigate after all. It is really awkward to use the pen like that. I'd rather not use the pen buttons if I can't help it.

5:15pm. Ok, I've learned some important lessons. Next time I'll endeavor not to make things so complicated on myself.

Also I think I understand how the designer create the pattern on the grate. He probably went in and connected the edges menually. I was so damn stubborn with this.

I should not have aimed for founded edges, but chamfers instead. It was not worth it to spend all this time for that little thing. At any rate, I have the grate pattern down including screws.

Let me make the shapes pop just a tiny bit and add the remaining fillets and I will be done.

5:45pm. Finally done! Halleluyah.

This is all I'll need of the model. Let me post it in the wip thread. Then I'll export it and do a distortion check. I'll also check Rhino's quad remesher after that. After that comes texturing.

In hindsight for a semi complicated piece like that grate here which gave me so much trouble in network mode, I should have just subdiv modeled it and exported the control cage into Moi.

When Moi fails it is really surprising and leaves me wondering how to fix it.

5:55pm. Focus me. Let me just post it.

6:05pm. Oh, it managed to union the grate. I am impressed. I wonder why it failed the last time. It is not like I moved it or anything.

7:10pm. Done with lunch. The quad remesher really makes a mess of the grate even with 100k quads just for the big piece. What a waste of time. I won't bother with it again. I think I can safely uninstall Rhino, but I'll keep it around for the time being.

7:15pm. Damn it, let me get a screenshot of the mess.

...It really takes a while to finish.

7:25pm. Finally posted it.

Time to catch up with Fable and UQ Holder.

Tomorrow I will texture the rig. I really should post some of the recent work on Twitter."

---
## [TheRakeshPurohit/wireit](https://github.com/TheRakeshPurohit/wireit)@[c85c022769...](https://github.com/TheRakeshPurohit/wireit/commit/c85c02276975a1a86cbf509a7e9a353d5f0a19a8)
#### Wednesday 2022-05-11 18:10:08 by Alexander Marks

Error when trying to cache outside of package (#182)

It's currently not possible to locally cache an output file that isn't inside of the package directory. We check for this case when we delete and throw, but not when we cache. So if you are caching but have cleaning disabled, we would silently weirdly save the output file to a parent directory, and then not restore it.

Now this is an error.

Note we could in theory do this during analysis, but I'm not 100% confident in my ability to correctly detect this case given all of the possible magic glob syntax, so for now it's safer to just do it at runtime. (see https://github.com/google/wireit/issues/64).

Also note we could in theory support caching files outside of the package root, but we'd have to do something like a tarball for the local cache, instead of simply copying into `.wireit/<script>/cache/<hash>`. We should think carefully about whether we want to do that, though, so I'm not dealing with that for now.

Fixes https://github.com/google/wireit/issues/181

---
## [AndrejK1/Hollow-Knight-Saves](https://github.com/AndrejK1/Hollow-Knight-Saves)@[6ae478e100...](https://github.com/AndrejK1/Hollow-Knight-Saves/commit/6ae478e10036c5e8c8d4c0e97853da019baa15a7)
#### Wednesday 2022-05-11 18:15:32 by Andrew Kononenko

Main profile - 3rd pantheon completed! 111%
Haha poor Zote!!! Removed this shitty boy from it (and yes, first try = win)
(returned back anyway)

To remove Zote set this:
{
    "playerData": {
        ...
        "greyPrinceDefeats": 0,
        "greyPrinceDefeated": false,
        ...
    },
    ...
}

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[90b82cd5fb...](https://github.com/treckstar/yolo-octo-hipster/commit/90b82cd5fbd699bba5e02e39fc3126832c2561d3)
#### Wednesday 2022-05-11 19:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [n00by-common/nixos](https://github.com/n00by-common/nixos)@[c4400dafba...](https://github.com/n00by-common/nixos/commit/c4400dafbaa68034f07b716b584eb91e47d4ce9b)
#### Wednesday 2022-05-11 19:33:47 by Hannes Bredberg

Add MultiMC client secret

Fuck you Microsoft, I wanna use my mojang account for my ancient game.

---
## [bellegarde-c/android_kernel_gnumdk_sm8150](https://github.com/bellegarde-c/android_kernel_gnumdk_sm8150)@[323565fb91...](https://github.com/bellegarde-c/android_kernel_gnumdk_sm8150/commit/323565fb914eae95344ea2beb29dc0f043b72396)
#### Wednesday 2022-05-11 20:00:58 by Peter Zijlstra

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
## [jhnvz/graphiti](https://github.com/jhnvz/graphiti)@[5e7633a397...](https://github.com/jhnvz/graphiti/commit/5e7633a3974df6bacc8037656c13f89a9fde1cd5)
#### Wednesday 2022-05-11 20:05:58 by Lee Richmond

Support cursor-based pagination

We currently support a `page[offset]` parameter. This updates the
codebase to accept `before` and `after` cursors, applying the relevant
`offset` logic as appropriate.

When JSON:API we're render `meta: { cursor: <cursor> }` for each entity,
and when flat JSON/GraphQL we'll render `_cursor: <cursor>`. This is to
support GQL queries like

```graphql
employees {
  nodes {
		firstName
		_cursor
	}
}
```

We're not doing a full `edges` implementation because A) I just kinda
hate it and B) to value here is metadata about the relationship, mostly
for M2M relationships, which Graphiti doesn't support yet anyway.

The cursor is Base64 encoded JSON of `{offset: <offset>}`.

In addition, we accept `?fields[page_info]=has_next_page,etc` to render
the relevant `pageInfo` section. This uses the same code already used
to populate pagination links and cursors.

---
## [jocrl/cockroach](https://github.com/jocrl/cockroach)@[f4b394d527...](https://github.com/jocrl/cockroach/commit/f4b394d527e6c5132d06c1b24625e5288e6bf71f)
#### Wednesday 2022-05-11 20:17:13 by Josephine Lee

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
that we've to work.

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
## [canelhasmateus/nimskull](https://github.com/canelhasmateus/nimskull)@[f35b5bf2d4...](https://github.com/canelhasmateus/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Wednesday 2022-05-11 20:22:16 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[713b4903b2...](https://github.com/mrakgr/The-Spiral-Language/commit/713b4903b24c3c37b46ed25d4b656e19cbe8f89c)
#### Wednesday 2022-05-11 20:35:56 by Marko Grdinić

"https://medium.com/@katelyngadd/why-i-quit-googles-webassembly-team-and-how-it-made-me-sick-c50ef562ce1

///

Earlier in this post I made the absurd statement that WebAssembly gave me brain damage. Unfortunately, this is true. My two years at Google were spent perpetually stressed, acting as an unofficial producer, helping run meetings and document decisions while dealing with sometimes hostile colleagues. Thankfully other members of the team were working hard to manage these same issues, but it took a toll nonetheless. Over time I slowly lost my mid and short term memory, to the point that some days I couldn’t find my car in the garage or forgot entire conversations. I had to take very detailed notes. Eventually my physicians put me on forced medical leave, and they strongly encouraged me to quit; advice I later took, but not soon enough.

///

Oh lol. It is a good thing I've started slowing down as I've been experiencing some of this as well.

9:30pm. http://moi3d.com/2.0/docs/moi_command_reference11.htm#shortcutkeys

Finally found the shortcut for freeform. It is curve.

I am playing around with loft and just realized the difference between normal and loose. Network fails all the time, but had I used loft I'd have gotten exactly what I wanted without any issue.

Loft is to surfaces what freeform is to curves. Loose creates sufaces by using curves like control points.

On one hand I feel stupid for not realizing this earlier while working on the grate, on the other I feel elated for having gained such an useful tool! Having this will be soo useful in various situation. It is like gaining a superpower. In the future, with this I'll be able to fillet manually without any issue whereas previously I could do only projective cuts.

9:45pm. https://youtu.be/M4F6Q6h2-ao
Blender Tutorial | Lofting Shapes

Let me watch this for a bit and then I'll get back to UQ Holder."

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[a583c6964c...](https://github.com/sunamo/sunamo/commit/a583c6964c494904ba9cf2f395a270441ff0c478)
#### Wednesday 2022-05-11 21:08:38 by Radek Jancik

Well, yeah. At a certain point, you've got to be really honest with yourself. Like, 'Why am I doing this? What are my motivations?' Like, if you get into it because you want to be famous? Then you've got a long row to hoe. But if you really feel like it's a labour of love and it's something you're actually legitimately good at, then it's not that hard to keep plugging away. - Will Arnett

---
## [ccuser44/Adonis](https://github.com/ccuser44/Adonis)@[4928cc16a3...](https://github.com/ccuser44/Adonis/commit/4928cc16a3846384dc873ed8c33186f87ff2a856)
#### Wednesday 2022-05-11 21:38:15 by P3tray

Added settings.Messages, also did a lot more. (#757)

* Update Settings.lua

* We Had To Use Dark Magic To Make This Work

* these guys are flipped

* this is how we generate our shit.

* arrgghh... damn this thing for not working.

* Now we tell you your browser sucks in your native tongue.

* All hail the mighty ccuser44

* Update Loader.server.lua

Co-authored-by: Sceleratis <sceleratis@gmail.com>

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[fcab2aeda1...](https://github.com/Fargowilta/FargowiltasSouls/commit/fcab2aeda1174df4fe6f7465e27984fafe183f20)
#### Wednesday 2022-05-11 22:01:24 by terrynmuse

sprites
 squirrel coat of arms
 dread shell (shield also applies to lump, soul of siblings)
renamed heart of eternal and soul of siblings to heart/soul of master, fuck you master mode

---
## [magit/magit](https://github.com/magit/magit)@[ab801de538...](https://github.com/magit/magit/commit/ab801de53827a232b7806362fb08ca804f27c6d0)
#### Wednesday 2022-05-11 22:06:27 by Jonas Bernoulli

magit-section-context-menu: Support non-section branches

We use section keymaps to implement context-sensitive menus but
branches are not always represented using sections.  To support
such "painted branches" anyway use fake sections, which closely
mirror the commit section in which the click occurred.

This admittedly is ugly and somewhat risky, but seems to work well.
`magit-section-update-highlight' would break due to this hack, so
we avoid calling it.  If it turns out that things also break due
to this kludge, then we might have to revert.

---
## [Terminal-Wars/BattleTerminal](https://github.com/Terminal-Wars/BattleTerminal)@[5f531f2f94...](https://github.com/Terminal-Wars/BattleTerminal/commit/5f531f2f947d0de7b65ebb953b6d433ae9fdc218)
#### Wednesday 2022-05-11 22:13:34 by IoIxD

HAHA NOPE SUCK MY DIRTY ASSHOLE WE HAVE TO USE GTK OR MAKE OUR OWN SHIT

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[b8a001d721...](https://github.com/Buildstarted/linksfordevs/commit/b8a001d7218e82f1832fb508ecf25554c8274310)
#### Wednesday 2022-05-11 23:06:42 by Ben Dornis

Updating: 5/11/2022 11:00:00 PM

 1. Added: The direction I want to take this blog in
    (https://www.bramadams.dev/projects/home-base-blogging)
 2. Added: the miracle at the heart of the ordinary
    (https://riccardo.cefala.net/posts/the-miracle-at-the-heart-of-the-ordinary/)
 3. Added: So you want to run a virtual event
    (https://blog.lazerwalker.com/2022/05/10/virtual-events.html)
 4. Added: Stealing checks worth millions & pwning a bank
    (https://www.jhaddix.com/post/stealing-checks-worth-millions-pwning-a-bank)
 5. Added: Let's talk about this async
    (https://conradludgate.com/posts/async)
 6. Added: Changes after quitting social media for 1 year.
    (https://vaidik.bearblog.dev/quitting-instagram/)
 7. Added: Earn $200K by fuzzing for a weekend: Part 1
    (https://secret.club/2022/05/11/fuzzing-solana.html)
 8. Added: The productive ritual of listening to a single song
    (https://danganiev.me/blog/the-productive-ritual-of-listening-to-a-single-song/index.html)
 9. Added: Thanks red badge & lock screen banner, but it's time I tried to stay up to date all by myself
    (https://makun.mataroa.blog/blog/notifications/)
10. Added: Surfing the Gopherspace
    (https://charlieharrington.com/surfing-the-gopherspace/)
11. Added: The Death of Mystery is an Illusion
    (https://nathanieltravis.com/2022/05/11/the-death-of-mystery-is-an-illusion/)
12. Added: How to Twitter: The Martin Way
    (https://martinboss.com/how-to-twitter-martin-way/)
13. Added: VPS Showdown - May 2022 - DigitalOcean vs. Lightsail vs. Linode vs. UpCloud vs. Vultr by Josh Sherman
    (https://joshtronic.com/2022/05/01/vps-showdown-digitalocean-lightsail-linode-upcloud-vultr/)
14. Added: Microservices gets it WRONG defining Service Boundaries
    (https://codeopinion.com/microservices-gets-it-wrong-defining-service-boundaries/)
15. Added: How I learned to stop worrying and love the YAML | lbr.
    (https://leebriggs.co.uk/blog/2022/05/09/learning-to-love-yaml)
16. Added: How to make Ruby interpreter run program written in a natural language
    (https://dmitrytsepelev.dev/natural-language-programming-with-ruby)

Generation took: 00:06:30.5634205
 Maintenance update - cleaning up homepage and feed

---
## [kuroringo90/android_kernel_xiaomi_vayu](https://github.com/kuroringo90/android_kernel_xiaomi_vayu)@[e8cfa7c2a4...](https://github.com/kuroringo90/android_kernel_xiaomi_vayu/commit/e8cfa7c2a4963f7aa9324197bc6b374af8762241)
#### Wednesday 2022-05-11 23:11:25 by Wang Han

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
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[905a7e782f...](https://github.com/mbs-octoml/mbs-tvm/commit/905a7e782fb875416b915a455f11cad6d554b9a5)
#### Wednesday 2022-05-11 23:47:57 by Mark Shields

** Collage v2 sketch ***

- cleanup before rebase
- Use 'regular' target when build, not external codegen target
- Tuned for -libs=cudnn
- Tune before collage not during
- Bring over target changes
- Fix GetSpecName
- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---

