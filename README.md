## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-28](docs/good-messages/2021/2021-12-28.md)


1,587,384 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,587,384 were push events containing 2,227,451 commit messages that amount to 153,371,971 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [Khanor-s-Mod-Projects/norwegian_focus_and_flavor](https://github.com/Khanor-s-Mod-Projects/norwegian_focus_and_flavor)@[68f100da31...](https://github.com/Khanor-s-Mod-Projects/norwegian_focus_and_flavor/commit/68f100da31351f7387bb9b1c55ac2c51bfe5ae90)
#### Tuesday 2021-12-28 00:05:50 by Khanor

Advisor, tooltip and flavor update

- Added three new characters with political advisor roles, so historical ones with AI logic and requirements for use can take the place of random generic ones given by the game at start.

- Tried to handle widespread character loss, especially advisor loss, on a civil war for Norway. Now should at least keep the two bread and butter Field Marshals/Army Chiefs and some focus given Corps Commanders in every case.

- Reworked many focus tooltips regarding political advisors, added in direct links to the advisors themselves in these cases before the reworked NaW tooltips with additional information. Now things are in line with vanilla HoI IV, very clean and nice, and comes with generally all relevant information.

- Improved graphics use and AI logic on other characters/advisors.

- New company idea IDs so they all follow the same scheme for IDs, with country tag first.

- Added 12 plausible Norwegian agent names from R56 to NaW too, and added 14 additional historical ones before those, inspired by cover names for (Norwegian) agents working for XU, Milorg and/or SOE during the Second World War.

- Shortened some focuses to give the player and AI Norway some breathing room to get things done: Coastal Defense Specialization 105 days --> 70 days, Modern Escort Ships 70 days --> 35 days, Mountaineers 70 days --> 35 days and District Investments 70 days --> 35 days.

- District Investments' bonus for dispersed industry can now also be used for excavation techs, so it's not completely wasted if deciding to go concentrated industry.

- Railway from Østlandet to Vestlandet ("Raumabanen") given to Norway through De norske Statsbaner focus now also level two like the minimum of all other Norwegian railways after the two railway focuses.

- Fixed bug where cascading effects could instantly remove Aftermath of the Great Depression, rather than in several steps as intended.

- Cleaned up commanders given by focuses potentially being given to both sides during civil wars. Tried to ensure they're now only given to one side if in a civil war (that side being the player/NOR-tag.)

- Focus file cleanup, more use of base, effect sorting, etc.

- Improved focus search filters to be even more accurate and helpful.

- Added four new unit name lists, Cavalry Regiment (starting list, also in use at the start), Jäger Division (unlocked by focus), Monarchist Infantry Division and Monarchist Mobile Division (both unlocked by focus, and ideology-dependent.)

- Some new name lists used by starting templates/units or units given through focuses. Cleaned up starting unit history files.

- Rebalanced National Collectivism and Socialist Collectivism. Now no pop growth, general building speed and ideology drift, but extra resources, production retention and infrastructure building instead. Should be less awkward if in faction with or a subject of other ideologies. The relevant focuses now give timed generic fascist-/communist drift ideas instead.

- Fixed event province targetting for Orkney, now uses the correct province rather than the R56 addition that doesn't exist in the base game.

- Removed double country leader entry on the event for who shall lead the monarchist coalition after the civil war.

- VP/city renaming event made better for one option.

- Added a touch of political power to each side in the Norwegian Monarchist Civil War to get them started, especially important now that a civil war dragging out will really cripple non-aligned/monarchist Norway's political power gain due to the new country leader added.

- Added a new VP/city to Vestlandet, Haugesund.

- Improved focus localisation and character localisation. Moved a VP to replace loc file, removed redundant/unused tooltip. Renamed the loc files themselves.

- Moved an airbase in Norrland to where it was supposed to be. Added supply nodes (supply node graphics) to some states that hadn't been given such yet.

- Better descriptor-file handling.

---
## [Bawhoppen/-tg-station](https://github.com/Bawhoppen/-tg-station)@[4610f700eb...](https://github.com/Bawhoppen/-tg-station/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Tuesday 2021-12-28 00:24:44 by LemonInTheDark

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

---
## [aarrbba123/tgstation](https://github.com/aarrbba123/tgstation)@[9c57fca97d...](https://github.com/aarrbba123/tgstation/commit/9c57fca97dfe6b6cae78b4b702ead513daedef01)
#### Tuesday 2021-12-28 00:33:57 by LemonInTheDark

Fixes random hell call-counts to Move (#63317)

Removes the parent call from mob/Login

Mothblocks pinged me with a profile of just a hellish amount of move calls
Way too many, like 200000
Started looking into it, got distracted by how expensive macros were
Turns out most of the cost of macros was in the nuke ops summon spawner

So I looked at why, only bit of it that was at all expensive was the login for the cyborgs
Tested on a local, huh that is slow yeah

Looked at the profiler, huh there's that move count again
So anyway, why is login so expensive

Spawned a few cyborgs in, dragged myself into them, nothing
Spawned myself in with sdql magic using the summon spawner, man it really is still there
I guess it has to do with move somehow, try and stick a breakpoint on it, get fucked by the debugger
I notice the hanging comes during the Login parent call

Try again, this time with good breakpoints.
We're trying to move, to (1,1,1), just like the reference says we will https://secure.byond.com/docs/ref/#/mob/proc/Login

But man, it just keeps happening, and we don't actually move
Step through the code, we've got that null loc check in atom/movable/Move

So the move to (1,1,1) isn't working

Here's the exact line from the reference
"If the mob has no location, place it near (1,1,1) if possible"
Keyword is near

Talked to lummox about this behavior, figured it was a bug

It turns out by near, they mean inside that tile's area
It'll keep trying to place you somewhere, in an attempt to effectively cover for shitty login systems, until you succeed in moving

That tile is space. There are 200,000 tiles with the same area as it
OH.

So anyway, we're not calling parent on mob/login anymore. We can do all the work it did that we care about ourselves (IE: Just the statobj set)
And this way we don't need to worry about 4 SECONDS OF OVERTIME WHENEVER SOME POOR FUCK MESSES UP SPAWN ORDER

So yeah, I'm a genius and not at all just malding at the existance of keybind macros, and hopefully another source of stutter bites the dust
Not actually sure how widespread this is, but even if it's just spawn becacons that's pretty banging

---
## [573462273/FreeCAD](https://github.com/573462273/FreeCAD)@[92e6094449...](https://github.com/573462273/FreeCAD/commit/92e6094449275e89e6ffd7a74c32e3ce3c62c1e6)
#### Tuesday 2021-12-28 00:45:02 by Abdullah Tahiri

Sketcher: EditModeCoinManager/DrawSkechHandler refactoring

======================================================

Creation of EditModeCoinManager class and helpers.

In a nutshell:
- EditModeCoinManager gets most of the content of struct EditData
- Drawing is partly outsourced to EditModeCoinManager
- EditModeCoinManager gets a nested Observer class to deal with parameters
- A struct DrawingParameters is created to store all parameters used for drawing
- EditModeCoinManager assume responsibility for determining the drawing size of the Axes
- Preselection detection responsibility is moved to EditModeCoinManager.
- Generation of constraint nodes and constraint drawing is moved to EditModeCoinManager.
- Constraint generation parameters are refactored into ConstraintParameters.
- Text rendering functions are moved to EditModeCoinManager.
- Move HDPI resolution responsibility from VPSketch to EditModeCoinManager
- Move responsibility to create the scenograph for edit mode to EditModeCoinManager
- Move full updateColor responsibility to EditModeCoinManager
- Allows for mapping N logical layers (LayerId of GeometryFacade) to M coin Layers (M<N). This
is convenient as, unless the representation must be different, there is no point in creating coin
layers (overhead).

Refactoring of geometry drawing:
- Determination of the curve values to draw are outsourced to OCC (SRP and remove code duplications).
- Refactor specific drawing of each geometry type into a single template method, based on classes of geometry.
- Drawing of geometry and constraints made agnostic of scale factors of BSpline weights so that a uniform treatment can be provided.

Refactoring of Overlay Layer:
- A new class EditModeInformationOverlayConverter is a full rewrite of the previous overlay routines.

ViewProviderSketch:
- Major cleanup due to migration of functionalities to EditModeCoinManager
- Reduce public api of ViewProviderSketch due to refactor of DrawSketchHandler
- Major addition of documentation
- ShortcutListener implementation using new ViewProvider Attorney
- Gets a parameter handling nested class to handle all parameters (observer)
- Move rubberband to smart pointer
- Refactor selection and preselection into nested classes
- Removal of SEL_PARAMS macro. This macro was making the code unreadable as it "captured" a local stringstream that appeared unused. Substituted by local private member functions.
- Remove EditData
- Improve documentation
- Refactor Preselection struct to remove magical numbers
- Refactor Selection mechanism to remove hacks

ViewProviderSketchDrawSketchHandlerAttorney:
- new Attorney to limit access to ViewProviderSketch and reduce its public interface
- In order to enforce a certain degree of encapsulation and promote a not too tight coupling, while still allowing well
defined collaboration, DrawSketchHandler accesses ViewProviderSketch via this Attorney class.
-DrawSketchHandler has the responsibility of drawing edit temporal curves and markers necessary to enable visual feedback
to the user, as well as the UI interaction during such edits. This is its exclusive responsibility under the Single
Responsibility Principle.
- A plethora of speciliased handlers derive from DrawSketchHandler for each specialised editing (see for example all the
handlers for creation of new geometry). These derived classes do * not * have direct access to the
ViewProviderSketchDrawSketchHandlerAttorney. This is intentional to keep coupling under control. However, generic
functionality requiring access to the Attorney can be implemented in DrawSketchHandler and used from its derived classes
by virtue of the inheritance. This promotes a concentrating the coupling in a single point (and code reuse).

EditModeCoinManager:
- Refactor of updateConstraintColor
- Multifield - new struct to identify a single element in a multifield field per layer
- Move geometry management to delegate class EditModeCoinGeometryManager
- Remove refactored code that was never used in the original ViewProviderSketch.

CommandSketcherBSpline:
- EditModeCoinManager automatically tracks parameter change and triggers the necessary redraw, rendering an explicit redraw obsolete and unnecessary.

Rebase on top of master:
- Commits added to master to ViewProviderSketch applied to EditModeCoinManager.
- Memory leaks - wmayer
- Constraint Diameter Symbol - OpenBrain
- Minor bugfix to display angle constraints - syres

Architecture Description
=======================

* Encapsulation and collaboration - restricting friendship - reducing public interface

Summary:
- DrawSketchHandler to ViewProviderSketch friendship regulated via attorney.
- ShortcutListener to ViewProviderSketch friendship regulated via attorney.
- EditModeCoinManager (new class) to ViewProviderSketch friendship regulated via attorney.
- ViewProviderSketch public interface is heavily reduced.

In further detail:
While access from ViewProviderSketch to other classes is regulated via their public interface, DrawSketchHandler, ShortcutListener and EditCoinManager (new class) access
to ViewProviderSketch non-public interface via attorneys. Previously, it was an unrestricted access (friend classes). Now this interface is restricted and regulated via attorneys.
This increases the encapsulation of ViewProviderSketch, reduces the coupling between classes and promotes an ordered growth. This I call the "collaboration interface".

At the same time, ViewProviderSketch substantially reduces its public interface. Access from Command draw handlers (deriving from DrawSketchHandler) is intended to be restricted to
the functionality exposed by DrawSketchHandler to its derived classes. However, this is still only partly enforced to keep the refactoring within limits. A further refactoring of
DrawSketchHandler and derivatives is for future discussion.

* Complexity and delegation

Summary:
- Complexity of coin node management is dealt with by delegation to helper classes and specialised objects.

In further detail:

ViewProviderSketch is halved in terms of code size. Higher level ViewProviderSketch functions remain

* Automatic update of parameters - Parameter observer nested classes

Summary:
- ViewProviderSketch and CoinManager get their own observer nested classes to monitor the parameters relevant to them and automatically update on change.

The split enables that each class deals only with parameters within their own responsibilities, effectively isolating the specifics and decoupling the implementations. It is
more convenient as there is no need to leave edit mode to update parameters. It is more compact as it leverages core code.

More information:
https://forum.freecadweb.org/viewtopic.php?p=553257#p553257

---
## [Glepooek/maui](https://github.com/Glepooek/maui)@[ac6befcbee...](https://github.com/Glepooek/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Tuesday 2021-12-28 01:10:36 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [SenseiTarzan/PocketMine-MP](https://github.com/SenseiTarzan/PocketMine-MP)@[d9c70cb176...](https://github.com/SenseiTarzan/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Tuesday 2021-12-28 01:29:59 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [Xirado/Bean](https://github.com/Xirado/Bean)@[3088daa8a3...](https://github.com/Xirado/Bean/commit/3088daa8a39b2d5bff5b26f3e9bd59af2e043b5f)
#### Tuesday 2021-12-28 01:38:06 by Marcel Korzonek

Add support for banning guilds (fuck you in particular)

---
## [oxidecomputer/hubris](https://github.com/oxidecomputer/hubris)@[8e0b13b865...](https://github.com/oxidecomputer/hubris/commit/8e0b13b86564fc7316428943dfe5fde88bb60ef4)
#### Tuesday 2021-12-28 02:14:47 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [lhx11187/mpv](https://github.com/lhx11187/mpv)@[f6c81047fa...](https://github.com/lhx11187/mpv/commit/f6c81047fa5a9199084fa92327c41c6d8a16b059)
#### Tuesday 2021-12-28 03:10:38 by wm4

player: do not fall back to a default track with explicit selections

Consider e.g. --aid=2 with a file that has only 1 track. Then it would
fall back to selecting track 1. Stop doing this. If no matching track is
found, this will not select any track now.

Note that the fingerprint stuff (track_layout_hash in the source)
prevents softens the impact of this change. Without the fingerprint,
playing a dual-audio file with the second track selected, and then a
single-audio file, would play the second file without audio. But the
fingerprint resets it due to differences in the track list.

Try to exhaustively document this and tricky interactions between the
other features. What a damn mess, I think it's simply cursed. Of course
it's still my fault.

See: #7608

---
## [zhengshiJ/incubator-doris](https://github.com/zhengshiJ/incubator-doris)@[ef2ea1806e...](https://github.com/zhengshiJ/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Tuesday 2021-12-28 03:25:37 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [SgtHunk/fulpstation-1](https://github.com/SgtHunk/fulpstation-1)@[c797bf79ea...](https://github.com/SgtHunk/fulpstation-1/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Tuesday 2021-12-28 05:35:14 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [SgtHunk/fulpstation-1](https://github.com/SgtHunk/fulpstation-1)@[b59f03e592...](https://github.com/SgtHunk/fulpstation-1/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Tuesday 2021-12-28 05:35:14 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [GetStream/stream-chat-react-native](https://github.com/GetStream/stream-chat-react-native)@[7ec18259c0...](https://github.com/GetStream/stream-chat-react-native/commit/7ec18259c0f6ac784edbe814c8d35114c7c70463)
#### Tuesday 2021-12-28 08:13:42 by Mads Røskar

test(MessageSimple): Pondering life, surprised at own hacks

In the list of "oh god, please let me remember to squash this commit so
nobody can witness the blasphemy of what I'm doing to get this to work
before I refactor it to something sensible", this commit is pretty high
up the list.

On the other hand... _hackerman_ 😎

---
## [reduce-algebra/reduce-algebra](https://github.com/reduce-algebra/reduce-algebra)@[640a5dcf60...](https://github.com/reduce-algebra/reduce-algebra/commit/640a5dcf609cb2609b8c7d3edd5265b503e812e5)
#### Tuesday 2021-12-28 09:07:34 by Arthur C. Norman

CSL. The main thing that this checkin provides is a function "zprintf"
defined in "log.h". This attempts to mimic regular C/C++ "std::printf" save
that all aorts of integer can be printed using "%d" or "%x". That means
that clumsy-looking use of PRTxPTR and friends becomes unnecessary. Furthermore
it prevents attempts to display a floating point value using an integer
directive or vice versa. Basically it maps a call of zprintf(format, args...)
onto use of std::cout << {stuff} where the stuff is made up from the plain
text in the format, IO manipulators to achieve the desired layout and the
arguments to be printed. This means that if you use the format specifier %s
it just passes the argument to "cout<<" so private overrides of that will be
honoured. As an extra trick, if you pass an value of type std::atomic<T> to
zprintf it displays the value obtained by using the .load() method of the
object. Finally, if you compile your code in C++20 mode (eg with g++ you
say "-std=gnu++20) the format will be checked for validity and for consistency
with the values being printed at compile time rather than run time.
An example will show why I view this as useful. Consider the statement
   zprintf("Value is %#X\n", some_intptr_t_variable);
then using regular printf one needs
   std::printf("Value is %#" PRIxPTR "\n", some_intptr_t_variable);
and I find the "PRIxPTR" clumsy. But with C++ iostream one may end up with
   std::cout << "Value is " << std::hex << std:uppercase
             << some_intptr_t_variable << std::dec << std::nouppercase
             << "\n";
which is amazingly verbose even if clear. Using "%X" rather than "%x" may be
unusual and make this look especially bad, as does my code restoring cout
to a tidy state after printing. But specification of widths and precision
are about as clumsy.
Well also anybody who picks up log.h and the code for zprintf will find that
they could add extra formatting options. I have a format "%a" for use with CSL
that displays addresses in segment/page/offset form.
The current version of log.h is about the first version I think is stable
enough to check-in. But at present zprintf has two bodies of code for
parsing format strings - one at compile time one for run-time. I hope I can
consolidate them into just one. There will also be limits to the testing
it has had so far, but log.cpp is intended to be the basis of code to
exercise it.


git-svn-id: https://svn.code.sf.net/p/reduce-algebra/code/trunk@6202 2bfe0521-f11c-4a00-b80e-6202646ff360

---
## [Orchian/tgstation](https://github.com/Orchian/tgstation)@[bfa1542009...](https://github.com/Orchian/tgstation/commit/bfa1542009aa7fecbe0e50aef9561b49a4874448)
#### Tuesday 2021-12-28 09:37:56 by Cimika/Lessie/KathyRyals

Felinids don't like getting sprayed with water. (#59506)

This PR is an ode to @Ryll-Ryll, who inspired me to try and find fun, silly things to PR to try and make people smile.
About The Pull Request

Felinids now get a SMALL and SHORT mood debuff when getting sprayed with water. The intent of this PR is not to provide content to grief felinid (flashback to the "Felinids hate water" pr), but rather to provide a funny interaction.

Bonus point (Suggested by Ninja) : Getting sprayed with water interrupts do_after. Felinid climbing on your table ? Pssshttt. Straight in the face.

PR with permission from @ninjanomnom
Why It's Good For The Game

Light-hearted fun and a bit of flavour to felinids.
Changelog

cl
add: Felinids don't like getting sprayed with water.
code: Adds a new status effect, incapacitated, which causes your do_afters to stop.
/cl

---
## [HahaKykrixSkidlol/Haha-Kykrix-Noob-Lol-I-skid-and-you-cant-do-anything](https://github.com/HahaKykrixSkidlol/Haha-Kykrix-Noob-Lol-I-skid-and-you-cant-do-anything)@[9e43b4dc98...](https://github.com/HahaKykrixSkidlol/Haha-Kykrix-Noob-Lol-I-skid-and-you-cant-do-anything/commit/9e43b4dc98bc4094fae6776e221e5265998dfeea)
#### Tuesday 2021-12-28 10:39:53 by HahaKykrixSkidlol

Uhh, i made this and def not stupid kykrix

haha get skidded noob, you fucking sucking ass bitch

---
## [someone5678/frameworks_base-tmp](https://github.com/someone5678/frameworks_base-tmp)@[1ba101f82e...](https://github.com/someone5678/frameworks_base-tmp/commit/1ba101f82eae4e54293428480fbcbfd1c58359c8)
#### Tuesday 2021-12-28 10:56:29 by Steve Howard

Improve accelerometer-based orientation sensing.

There were three main complains about orientation sensing:
* Switching to landscape when putting a device down on a table (or picking it up)
* Changing orientation due to road bumps or vehicle vibrations while in a car dock
* Switching to upside-down too easily

This change includes three primary enhancements.

First, we run the accelerometer output through a lowpass filter before considering its orientation.  This avoids glitches due to brief phone movement, particularly when the phone hits a table.  The filter uses a very low default time constant of 200ms to retain responsiveness (note the samping period is ~200ms, so the effect of this filtering is pretty mild).  At tilt angles beyond 45 degrees, however, we increase the time constant to 600ms, which helps greatly with avoiding glitches picking the phone up from a table.  It does introduce some sluggishness when rotating while the phone is tilted back, i.e. being used in one's lap.

It's also worth mentioning that the accelerometer output on Sapphire appears to be pre-lowpass-filtered with a time constant of around 500ms, making this less necessary on that device, but the added effect doesn't noticeably degrade user experience in my opinion.

Second, we check the magnitude of the raw accelerometer output.  If it deviates from the strength of gravity by more than one m/s^2, we distrust the data, since that implies the device is under external acceleration and the sensor data doesn't accurately reflect orientation.  This helps avoid glitches due to shocks and vibrations, as in the car dock scenario.  However, rather than ignore the data entirely, we filter it with a very high time constant (5 sec).  As a result, if the device is rotated while vibrating, even if we never pick up a clean sample, we will eventually detect the orientation switch.  Of course, with a sampling period of 200ms, we're prone to aliasing, but that seems like a highly unlikely corner case.

Third, we restrict transitions to upside-down orientation to a much narrower range, both in terms of orientation and tilt.  This should prevent upside-down mode from activating in most cases where it's not desired.

I also updated a lot of stale documentation, added a lot of documentation, and cleaned up a lot of the code, so as to make this (often subtle) code as transparent as possible.

---
## [lindorelie/Coursera-test](https://github.com/lindorelie/Coursera-test)@[55a878f049...](https://github.com/lindorelie/Coursera-test/commit/55a878f0499637b80ca0ddee55e4812a86d577e7)
#### Tuesday 2021-12-28 12:09:38 by lindorelie

TIMJ

I'm a cool person, I want to fun with every sad person cause I found my joy on this and I have friend to any person created by God. If I'm her son so we're brother and sister.

---
## [MrClogsworthYT/FNF-PsychEngine](https://github.com/MrClogsworthYT/FNF-PsychEngine)@[ac3c9ef92e...](https://github.com/MrClogsworthYT/FNF-PsychEngine/commit/ac3c9ef92ed1c32a2d5e1814e976a55fa89db74b)
#### Tuesday 2021-12-28 13:01:38 by ShadowMario

Merge pull request #704 from MeowcaTheoRange/patch-2

This was fucking hell I'm *so* sorry @ShadowMario

---
## [LDR-Siren/EmilyC-SamanthaPrater-EruzaArto](https://github.com/LDR-Siren/EmilyC-SamanthaPrater-EruzaArto)@[5f3530e828...](https://github.com/LDR-Siren/EmilyC-SamanthaPrater-EruzaArto/commit/5f3530e8286be167f3eaeebf5287b4f515cbe9dc)
#### Tuesday 2021-12-28 13:37:17 by LDR

Dec 26 2021 She claims I am an Art Thief

This made me laugh. So apparently I am an Art Thief. So the reason she thinks I am is because I used Free to use template to make the logo for the Dibney Cru. The non monetary support group made up of people that she has abused, harassed, stalked, and harmed in some fashion or another.  I made it through Canva, and it is a free to use stock image on Adobe Stock and Shutterstock. 

The next thing she claims is "Stolen" is the Clipart PNG of a set of fairy wings I used in my Secondlife Marketplace for a tattoo I made 6+ years ago. I actually have the fair use of those wings png and they are free to use clip art on a dozen or more PNG sites. Why? Because the artist offered them up for free. To drive this point home further, I gain no real world currency off said wings. None. The pittance I charge on the game website is less than 1 penny in real world currency. So I have gained nothing monetarily from them, and I have the fair use of them. 

I find it funny the person that just recently came out and admitted to stealing art is calling others out on it. If you want to see refer to 0 12 27 2021 0 file. It is all there.

---
## [david072/SourceAutoRecord](https://github.com/david072/SourceAutoRecord)@[155c8e21c8...](https://github.com/david072/SourceAutoRecord/commit/155c8e21c8eedf0e9288651996ef104d70da6622)
#### Tuesday 2021-12-28 14:45:09 by mlugg

fix: fix crashing issues on Windows

From the bottom of my heart: fuck you, Microsoft. Why in the everloving
*fuck* does stringifying a filepath just throw an undocumented
system_error if the string contains certain Unicode characters?

---
## [LinkBoi00-Development/android_kernel_xiaomi_cannon](https://github.com/LinkBoi00-Development/android_kernel_xiaomi_cannon)@[4509144d48...](https://github.com/LinkBoi00-Development/android_kernel_xiaomi_cannon/commit/4509144d48d139b60ea325e7676f5417798dea24)
#### Tuesday 2021-12-28 15:54:58 by Peter Zijlstra

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b6d6e88d62...](https://github.com/mrakgr/The-Spiral-Language/commit/b6d6e88d6292808c260f65596d33fc48f2374f8e)
#### Tuesday 2021-12-28 18:21:13 by Marko Grdinić

"10:55am. Let me chill a bit and then I will start. Maybe I'll skip the morning session.

https://readmanganato.com/manga-km988147/chapter-64

Masterful bait to get me to read it on the scanlators website. Okay, I'll go there.

> This account has been suspended.

Yeah, this is the problem I was afraid of. Scanlators come and go, while the mange piracy sites serve as backup and they all have the fake chapter. Now where am I going to get the real scans?

https://manhuascan.com/read-circle-zeros-otherworldly-hero-business-reboot-chapter-64.html

This one is real.

https://manhuascan.com/read-circle-zeros-otherworldly-hero-business-reboot-chapter-65.html

My god, they did it for two chapters is a row!

11:25am. I got lucky with 64, but I've checked 10 different sites and they are all fake.

11:30am. I guess I'll just skip chapter 65 and hope they don't do this again.

11:40am. I am happy right now. That I am able to enjoy myself like this is proof enough that I am moving in the right direction. I'll spend the morning like this and then properly get into it later.

11:55am. That was satisfying. Let me have breakfast.

1:05pm. I meant to read Hero King, but it seems I am 7 chapters behind rather than just 1. I'll leave it for later then. It is art time.

Let me start up CSP.

1:20pm. I am playing with pastels, but they don't feel right to me. I need to take this seriously.

First of all, how do I set up my own custom toolbox?

http://www.clipstudiotutorials.com/organizing-your-workspace

1:30pm. I do not feel like messing with toolbars. I am happy that I set up the shortcuts. Two rounds brushes, an airbrush and the blur tool is all that I need. Though, as a challenge, let me try making the second cushion with pastels. I want to give it a try.

...No, it is not working. The rough texture of these tools is making a mess. Let me use my trusty things.

2:25pm. Done with the second cushion. The soft airbrush is not that great. It is too easy to get careless with it and end up with things that look like crap. It is only useful on the very edges and even there it it doubtful. Regular soft brush (milli marker) + blur tool ends up looking neater.

2:30pm. You know what, let me kick the softbrush out of my arsenal entirely. I don't need it.

Focus me, I am getting lost in thoughts.

2:35pm. Let me mask out the third cushion. i feel a bit high from doing the second one. I need to focus. I need to get faster at this. I need to learn a worflow where I put in the paint and then later smooth out the edges. Right now I am doing it as I go along. It is fun, but it is also a drain on my time.

2:45pm. Yeah, it is really a bad idea to just blur things without care. It always results in a mess.

2:50pm. Damn, I was wrong to try doing the highlights without masks. Let me try the magic wand.

30pm. Yeah, it was a big mistake to try to do the highlights without placing the mask first.

I started feeling good, and then I started being sloppy. The masks are such an essential part of digital painting.

3:20pm. it really looks good, but...

3:25pm. The parts that I did look good, but most of the cushion looks too flat.

3:40pm. I did the third cushion. I've added some darker shades on the sides and it looks better as a result.

So far, I feel like I am doing things the wrong way around.

I've runto in problem where I needed to do things out of order like having to add those shades just now. I have to do it on a separate layer.

So far I've been super focusing, but I need to learn to go faster. Let me see if I can up my pace. Ultimately, this is not programming. Most of the real work has been done in 3d, and I am just practicing my painting here.

3:55pm. This time on the third cushion I made sure to start off with the not just the flats, but also the shades. This is not faithful to the picture, but it should make it easier in the future steps.

Hmmm...you know what, let me try doing the highlights on a separate layer instead of messing with the selections. The way I am working now is far too much of a hassle.

4pm. No I need the mask. The reason is this round brush I am using. it is very difficult to trace out the elaborate shapes the lighting is taking. I'd have to lower the size of the brush to very low and be careful in working around it. But adding a bunch of color and carving it out in the eraser mode is much easier. I can only do this with the mask.

4:05pm. This reminds me how I used to draw in school. It was such a pain in the ass to paint things in. I trace a out a part and then filled it in using quick strokes.

The way I am doing things now is a lot superior. The sculpting style of painting is great. I could only do this digitally.

4:25pm. The right side of the cushion is pretty bad. I tried to hurry things along and this is where it is getting me.

5:05pm. This is starting to get boring. It was fun to play with lighting at first, but now...

The countours of light have so much detail and takes such an insane amount of time. If I was cell shading I'd been long done by now.

Let me take a break. I need to think about it.

5:45pm. I am back. Let me wipe the monitor with alchohol while I think. I am quite tired of working on the cushions.

6pm. Let me do some more. It is not really going right even though the picture looks good. I find the process too difficult. The tiny creases and the way light interacts with the shape of cushion makes things hell.

I can't do this using broad strokes.

6:20pm. Let me set the hard brush (mono-fill marker) to key 3. I've been using 1 for both soft and hard and it is a pain. Maybe I should have a rough eraser keyed to 4 as well, but I'll hold off on that. Actually, the E key is close enough for my liking.

6:40pm. I am not painting, but I am not slacking by any means. I am reviewing my moves in my head. This latest part is giving me trouble so I am reasoning out where I am going wrong. I know where.

I feel that I've learned quite a bit today. It really is one thing to watch video and quite another to practice it yourself.

I've made various mistake today which thankfully did not make the picture worse, they just slowed me down greatly.

I didn't really come in with a concrete plan. It was like with sculpting where I knew what shape I wanted to get, but the path to get there was ambiguous. I just tried my best to hit my isolated goals. I had to really push my creativity to its limit.

7:05pm. Let me close here. Who is going to do this anymore today.

Based on today's experience, I've come up with a concrete plan for how to paint tomorrow. It is definitely painting. I thought that gradient maps might classify as drawing, but it is definitely not the case. The image would not look good if I did crosshatching for shading.

7:15pm. Once I improve my process, things will go more smoothly. I'll go over the changes I intend to introduce tomorrow.

Right now, let me rest."

---
## [hugovk/nose2](https://github.com/hugovk/nose2)@[17d8fc9dd4...](https://github.com/hugovk/nose2/commit/17d8fc9dd4b01c8896f7e5c30ec8fc83cd4f76d3)
#### Tuesday 2021-12-28 18:59:59 by Stephen Rosen

Add "prettyassert" plugin, enabled by default

Make `assert` failures pretty, like `nosetests -d`.

If you call `nose2 --pretty-assert` or turn it on in config,
print the relevant exception statement, the exception message if given,
and attempt to resolve all names to their values by inspecting the
locals and globals available at the time of the exception to print
those as well.

The implementation of `nosetests -d` was the primary inspiration/guiding
force for this. The py.test approach is far too laborious to be worth
trying in nose2, as it involves rewriting bytecode on the fly, and its
original author noted that "Windows was a pain". Plus, there are all
sorts of caveats given with that implementation and scenarios where
it's known to blow up with other plugins, so we'd want this
implementation as a fallback for those cases anyway.

This is not an exact reimplementation of the `nosetests -d` approach,
however. I've tried to make some modest improvements to the behavior,
aided in part by the fact that we don't have to support ancient python
versions.

---
## [ssmessia/AOC_2015](https://github.com/ssmessia/AOC_2015)@[2399d93530...](https://github.com/ssmessia/AOC_2015/commit/2399d93530f0cc475dcb9ca373fd3c36e95caf4b)
#### Tuesday 2021-12-28 19:10:02 by Steven M

Add files via upload

Advent of Code[About][Events][Shop][Settings][Log Out](anonymous user #1221400) 8*
      /*2015*/[Calendar][AoC++][Sponsors][Leaderboard][Stats]
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle answer was 254575.

--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle answer was 1038736.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

Your puzzle input was bgvyzdsv.

You can also [Share] this puzzle.

---
## [sosedoff/pgweb](https://github.com/sosedoff/pgweb)@[cc1666b16a...](https://github.com/sosedoff/pgweb/commit/cc1666b16aa43a5e7de548e813bb00578bd0abf3)
#### Tuesday 2021-12-28 19:13:14 by Matthieu Vachon

Removes (annoying) `alert` on column copy value

All other copy to clipboard action are `alert` free like copying a table name to the clipboard. I think it should be the same for copying a column value.

If you think some feedback is necessary, maybe we should see a small label showing up than closing shortly after. As a comparison, it appears GitHub, in the commit list view, does not shot any feedback anymore (is it a bug maybe? because remote url copy still shows a feedback, anyway :)).

P.S. My editor automatically removed some trailing white spaces, if you prefer, I can revert those.

---
## [ConsistencyPlus/ConsistencyPlus](https://github.com/ConsistencyPlus/ConsistencyPlus)@[15b8b1dea8...](https://github.com/ConsistencyPlus/ConsistencyPlus/commit/15b8b1dea8d0f7364468326f9821d80ab9b77418)
#### Tuesday 2021-12-28 20:22:13 by Siuol

This is not the number one champion sound.

In this commit I did the following:

Fixed the Cobbled Blackstone issue #92

Finally a reference people will understand. (Please don't victory royale this please don't please I beg of you absolutely do not make this the fortnite parody please don't please I just wanna do this in peace please this is just the haha funny blackstone fix please isn't that funny enough for you haha blackstone fix haha funny funny joke Siuol I think Siuol is quite funny without the victory royale please don't victory royale this.)

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

---
## [SamuliSalonen/StreamElementsTTS-Unity](https://github.com/SamuliSalonen/StreamElementsTTS-Unity)@[c0a06f1a63...](https://github.com/SamuliSalonen/StreamElementsTTS-Unity/commit/c0a06f1a63a61132b3cfd94606bc2d418c8c5035)
#### Tuesday 2021-12-28 20:51:56 by Irish John Games

You probably know about what was wrong with that fuckin shit, it was giving me shit about fuckin, fuckin what dya fuckin call it, fuckin awful shite fuckin shit altogether, the fuckin json, json the bastard, bastard wouldn't let me import the fuckin shit, the TwitchLib shit, Fuck

---
## [h2sm/Safe-Document-Management](https://github.com/h2sm/Safe-Document-Management)@[3f77578cd4...](https://github.com/h2sm/Safe-Document-Management/commit/3f77578cd49e9ac4aaaaff9761664356bca98de0)
#### Tuesday 2021-12-28 21:30:46 by Egor Fedorenko

i fucking hate this bullshit. i have no clue what the fuck i am doing. Yo what the fuckkkkkkkk

---
## [Fagyi/kernel_xiaomi_cepheus](https://github.com/Fagyi/kernel_xiaomi_cepheus)@[b3656de25c...](https://github.com/Fagyi/kernel_xiaomi_cepheus/commit/b3656de25c711333d7efb6a447ec4a17321846e1)
#### Tuesday 2021-12-28 21:57:26 by George Spelvin

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
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Zlatan Radovanovic <zlatan.radovanovic@fet.ba>

---
## [partomahsiavash/USERNAME](https://github.com/partomahsiavash/USERNAME)@[e964323cb9...](https://github.com/partomahsiavash/USERNAME/commit/e964323cb9c0e0997f3f7617984bd405f781d0da)
#### Tuesday 2021-12-28 22:35:36 by siavash partonia

Add files via upload

I am a servant of Siavash Protonia from Kurdistan province and a final year student of Master of Petroleum Engineering. My project is about a talking robot that first greets you and introduces itself and asks for your name.
In the next stage, your family and then your gender, which is male and female
After being the original of this program, it asks the age, which is the age return for this software, which if it is under 6 years old, does not allow to speak until it reaches 6, and if it is over 6 years old, it recognizes that a school Is he either a university student or is he at work?
Then, if he is a student, he is called by an empty name, and if he is a university student, he is called a gentleman by an empty name, and if he is old, he is called a gentleman by a surname.
And finally, it gives explanations to the user with age range and this software is being developed and more features will be added to it.
End

---
## [Urban-Coalition/ArcCW_UR](https://github.com/Urban-Coalition/ArcCW_UR)@[b46af5b722...](https://github.com/Urban-Coalition/ArcCW_UR/commit/b46af5b722a97e8489cf605e8a97d154d3442f89)
#### Tuesday 2021-12-28 22:46:54 by mewbird

added aks mesh

need to redo the lua from the ground up goddamnit fuck fucking shit

---
## [auchtopus/CPSC_434_Final_Project](https://github.com/auchtopus/CPSC_434_Final_Project)@[2b6d99d5a6...](https://github.com/auchtopus/CPSC_434_Final_Project/commit/2b6d99d5a64fbbbf7275ab37562ac0848ea9748b)
#### Tuesday 2021-12-28 23:25:07 by Anthony Jiang

It's all just so fucked

1. accept should be blocking; need to think of a way to implement that or develop a means of rationalizing making it not blocking.
- the issue is that a) if the syn comes in before the acceopt, this approach is okay
- if the syn comes in after the accept, we are in trouble because we need to set a state variable

However, the bigger problem is the semantics.

accept is supposed to
1. be blocking
2. return the newly created socket for listening on the 4-tuple.

our accept is a) nonblocking (will return immediately regardless of whether the underlying thread has actually accepted) and b) returns the original socket. This is because we create new TCPSocks in threads (because we did not think far enough to use selector/multiplexer) so we are stuck with TCP connections in individual threads. To implement this feature requires the implementation of a blocking accept; without a blocking accept, you will not necessarily be able to return the copleted socket. \

The "slack" -- delay for receiving a message is picked up by the server code, where we use an infinite loop and the write function that can safely return 0 if no bytes can be read.
We will effectively return 0 until the connection is fully accepted on the listensock//now mp connection 1

---

