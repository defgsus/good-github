## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-27](docs/good-messages/2021/2021-12-27.md)


1,508,937 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,508,937 were push events containing 2,056,633 commit messages that amount to 146,659,422 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [jperkin/hubris](https://github.com/jperkin/hubris)@[8e0b13b865...](https://github.com/jperkin/hubris/commit/8e0b13b86564fc7316428943dfe5fde88bb60ef4)
#### Monday 2021-12-27 00:14:39 by Cliff L. Biffle

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
## [DragonTrance/tgstation](https://github.com/DragonTrance/tgstation)@[b2ba847c22...](https://github.com/DragonTrance/tgstation/commit/b2ba847c223dcbdc49c85a46156d5dbc28dbe5bd)
#### Monday 2021-12-27 00:26:33 by LemonInTheDark

Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

---
## [p2sr/SourceAutoRecord](https://github.com/p2sr/SourceAutoRecord)@[155c8e21c8...](https://github.com/p2sr/SourceAutoRecord/commit/155c8e21c8eedf0e9288651996ef104d70da6622)
#### Monday 2021-12-27 00:44:03 by mlugg

fix: fix crashing issues on Windows

From the bottom of my heart: fuck you, Microsoft. Why in the everloving
*fuck* does stringifying a filepath just throw an undocumented
system_error if the string contains certain Unicode characters?

---
## [ProfessorPopoff/mojave-sun-16](https://github.com/ProfessorPopoff/mojave-sun-16)@[5dc263ea2d...](https://github.com/ProfessorPopoff/mojave-sun-16/commit/5dc263ea2de53f573fcd35fe927e21f2cc1ee1d8)
#### Monday 2021-12-27 00:53:11 by ms-mirror-bot

[MIRROR] Nerfs the shit out of the felinid tail grab mood buff. (#1494)

* Nerfs the shit out of the felinid tail grab mood buff (#62768)

Mood controls your movespeed. Making Felinids objectively the best mood management race provided your ~~metagame buddy~~friend pulls your tail once every two minutes is insane, even as a meme.

A +5 mood buff was ridiculously good. This is better than the antag mood buff which is 4, equal to the cult buff for sacrificing which is 5, better than tripping balls, better than playing an arcade game and winning, better than the upgraded hug, equal with the best hug, and frankly one of the easiest best mood buffs you can get. And stacks with all the other ones.

* Nerfs the shit out of the felinid tail grab mood buff.

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [ProfessorPopoff/mojave-sun-16](https://github.com/ProfessorPopoff/mojave-sun-16)@[220a6ccaea...](https://github.com/ProfessorPopoff/mojave-sun-16/commit/220a6ccaeaa27e90224cff4f17e174bda00d101b)
#### Monday 2021-12-27 00:53:11 by ms-mirror-bot

[MIRROR] Nerfs the shit out of the negative sprayed with water mood event for Felinids (#1493)

* Nerfs the shit out of the negative sprayed with water mood event for Felinids (#62769)

Mood controls your movespeed. Making Felinids get their movespeed tanked because someone tried to fire extinguisher them is insane. Movespeed is the most important factor in SS13 when it comes to just about everything, it's how we punish people for damage after all.

A -5 mood is insanely punishing. It is equivalent to getting smitten by the gods, worse than a terrible noogie, worse than being bald, worse than literally throwing up all over yourself, worse than losing your family heirloom, and worse than having your eye stabbed out. This sucks for how easy it is to inflict on someone, especially considering the most common method of inflicting this is trying to fire extinguisher someone who's lit themselves on fire.

🆑
balance: Nerfs the felinid water spray moodlet
/🆑

* Nerfs the shit out of the negative sprayed with water mood event for Felinids

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [LuanVSO/terminal](https://github.com/LuanVSO/terminal)@[f2ebb21bd1...](https://github.com/LuanVSO/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Monday 2021-12-27 01:10:44 by Mike Griese

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
## [LuanVSO/terminal](https://github.com/LuanVSO/terminal)@[442432ea15...](https://github.com/LuanVSO/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Monday 2021-12-27 01:10:44 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [Guidesu/Skyrat-tg](https://github.com/Guidesu/Skyrat-tg)@[8e6590c600...](https://github.com/Guidesu/Skyrat-tg/commit/8e6590c6004266ab0fc01aacfc30c5dadca99226)
#### Monday 2021-12-27 01:34:16 by SkyratBot

[MIRROR] Add Ethereal lungs to the limbgrower [MDB IGNORE] (#9634)

* Add Etheral lungs to the limbgrower (#62469)

Saturday morning, calm shift.
I spend most of my time staring at CANARY waiting for an atmos alarm to pop up while I sit at the foyer hearing what random craziness Poly is spewing and wondering about the previous and more interesting shifts.
When suddenly, an atmos alarm pops up at the Incinerator.
"Fucks sake, I bet the other atmos are torching the place again..."
I rush there expecting to fix a fire, but instead I find the start of something great...

The madman kidnapped an Ethereal to use as an organic Hydrogen farm, nothing I haven't seen before but... my hands start shaking, a spark of brilliance and potential in my eyes as I mumbled the words:
"I always hear that organic things are healthier... so what if we throw the Electrolyzer away and instead, print Etheral lungs in the limbgrower and implant them on monkeys..."
To our sadness, Ethereal lungs weren't added to the Ethereal disk design, this fixes that!

* Add Ethereal lungs to the limbgrower

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [Guidesu/Skyrat-tg](https://github.com/Guidesu/Skyrat-tg)@[de4647c320...](https://github.com/Guidesu/Skyrat-tg/commit/de4647c320640766b64df2ecbfa69b4df8decb66)
#### Monday 2021-12-27 01:34:16 by SkyratBot

[MIRROR] Replaces Batform with Vampire houses [MDB IGNORE] (#9636)

* Replaces Batform with Vampire houses (#62516)

Permissions for species change

image
About The Pull Request

Goodbye batform

Hello, new preference called vampire status. Outcast vampires act just like normal, Inoculated vampires join their department under a unified "vampire house name" everyone shares.

image

image

image
Why It's Good For The Game

I've heard people complain about batform for years now, if vampires aren't gone by next halloween we can at least enjoy making them far less griefy (ruining a lot of the fun of halloween as just a dumb grief holiday) and more roleplay oriented. I don't even know why vampires got a griefy spell when they already have their main mechanic encourage randomly attacking people and stealing their blood to stay alive
Changelog

cl
del: Batform is gone!
add: ...Replaced by vampire houses as a preference. Join your department as a vampire ménage!
/cl

* Replaces Batform with Vampire houses

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [zergclan/guava](https://github.com/zergclan/guava)@[e015172847...](https://github.com/zergclan/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Monday 2021-12-27 02:20:49 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [nfagerlund/advent-of-code-2021](https://github.com/nfagerlund/advent-of-code-2021)@[392802b388...](https://github.com/nfagerlund/advent-of-code-2021/commit/392802b3881ebacb7c9ab66c6e35e50e16baa700)
#### Monday 2021-12-27 02:30:07 by Nick Fagerlund

HELL YEAH.

The hell of it is, I remember thinking of this on the train, and then I forgot it.

---
## [eliotbaez/libcobalt](https://github.com/eliotbaez/libcobalt)@[4a7db37269...](https://github.com/eliotbaez/libcobalt/commit/4a7db372696ffbbfbb573b73ec5cc79c9672d9b2)
#### Monday 2021-12-27 05:08:57 by Eliot Baez

Write function CMakeLists.txt files

Believe me when I tell you that this was a major pain in the behind. In
about a day I forced myself to understand, to the necessary extent, how
CMakeLists.txt and CMake as a whole work. Some stupid mistakes, like
forgetting to add include directories, slowed down my workflow
considerably. This is what happens when I have a 68 line Makefile that
I'm trying to convert into a CMakeLists.txt collection. It is not
pretty.

In other news, the rationale for this commit: moving toward a more
cross-platform build process. Makefiles had proven to be very difficult
to port to Windows on their own. Hopefully the time and frustration that
I have spent writing the CMakeLists.txt files will pay off.

---
## [auchtopus/CPSC_434_Final_Project](https://github.com/auchtopus/CPSC_434_Final_Project)@[2b6d99d5a6...](https://github.com/auchtopus/CPSC_434_Final_Project/commit/2b6d99d5a64fbbbf7275ab37562ac0848ea9748b)
#### Monday 2021-12-27 06:24:04 by Anthony Jiang

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
## [jujumumu/unnamed-game-prototype](https://github.com/jujumumu/unnamed-game-prototype)@[79ad0794ac...](https://github.com/jujumumu/unnamed-game-prototype/commit/79ad0794acfe46511066dba2cb35dd65ac26fdef)
#### Monday 2021-12-27 07:03:01 by Justin

some chunk queues work better

took me 1 whole day some shit just works better. like generate_queue. NOT THAT STABLE MAYBE who fucking knows fuck this hsit fuck u

---
## [KyleMagocs/flashyKawaii](https://github.com/KyleMagocs/flashyKawaii)@[dc00b32d97...](https://github.com/KyleMagocs/flashyKawaii/commit/dc00b32d97771bb7205a275dc85fd3e0e50e0dc9)
#### Monday 2021-12-27 07:20:09 by Kyle Magocs

yeah honestly the fade wheel kinda sucks.  oh well.

---
## [rookiejava/maui](https://github.com/rookiejava/maui)@[ac6befcbee...](https://github.com/rookiejava/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Monday 2021-12-27 07:36:15 by Jonathan Peppers

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
## [aarrbba123/tgstation](https://github.com/aarrbba123/tgstation)@[9c57fca97d...](https://github.com/aarrbba123/tgstation/commit/9c57fca97dfe6b6cae78b4b702ead513daedef01)
#### Monday 2021-12-27 08:19:25 by LemonInTheDark

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
## [mokulus/tgstation](https://github.com/mokulus/tgstation)@[bfa1542009...](https://github.com/mokulus/tgstation/commit/bfa1542009aa7fecbe0e50aef9561b49a4874448)
#### Monday 2021-12-27 09:27:05 by Cimika/Lessie/KathyRyals

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
## [Bawhoppen/-tg-station](https://github.com/Bawhoppen/-tg-station)@[4610f700eb...](https://github.com/Bawhoppen/-tg-station/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Monday 2021-12-27 09:39:07 by LemonInTheDark

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
## [kiara101/kiara-](https://github.com/kiara101/kiara-)@[4d5c9c72ea...](https://github.com/kiara101/kiara-/commit/4d5c9c72ea58309bc1975df5b72c303371b1377c)
#### Monday 2021-12-27 10:15:23 by kiara101

5 Common Winter Style Mistakes to Avoid

It’s high time now to avoid common winter-style mistakes that we usually commit unknowingly. Winter is a beautiful season to enjoy, but at the same time, the style mistakes cannot be enjoyed. While fair-weather fashionistas may lament the end of summer, any man who actually appreciates clothing anticipates the arrival of winter.

Get amazing outfit ideas at https://classicpolos.com/

---
## [qidaye/incubator-doris](https://github.com/qidaye/incubator-doris)@[ef2ea1806e...](https://github.com/qidaye/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Monday 2021-12-27 10:59:00 by HB

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
## [newstools/2021-the-daily-mavericks](https://github.com/newstools/2021-the-daily-mavericks)@[f35fb9ceea...](https://github.com/newstools/2021-the-daily-mavericks/commit/f35fb9ceead46b6be535b1b0f0c8e5825ea909fd)
#### Monday 2021-12-27 13:40:36 by Billy Einkamerer

Created Text For URL [www.dailymaverick.co.za/article/2021-12-27-my-friend-arch-was-a-guiding-light-a-brother-and-a-spiritual-leader-the-youth-should-emulate-graca-machel/]

---
## [newstools/2021-daily-dispatch](https://github.com/newstools/2021-daily-dispatch)@[e163fd3954...](https://github.com/newstools/2021-daily-dispatch/commit/e163fd39544f8a88281d79be0a97b8f9ebfa6a44)
#### Monday 2021-12-27 13:46:42 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2021-12-27-i-mourn-the-loss-of-a-brother-my-loyal-friend-and-my-spiritual-leader-graa-machel/]

---
## [arkaslittlemind/Competitive-Programming](https://github.com/arkaslittlemind/Competitive-Programming)@[5a7b5328d8...](https://github.com/arkaslittlemind/Competitive-Programming/commit/5a7b5328d8e3fbd78192f18af15dbddf22afc844)
#### Monday 2021-12-27 14:23:09 by Arkadipta Mojumder

Create 148A. Insomnia Cure.cpp

«One dragon. Two dragon. Three dragon», — the princess was counting. She had trouble falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?

---
## [arkaslittlemind/Competitive-Programming](https://github.com/arkaslittlemind/Competitive-Programming)@[f1bb77ab87...](https://github.com/arkaslittlemind/Competitive-Programming/commit/f1bb77ab87f031007d85192cfe219428c4a76f67)
#### Monday 2021-12-27 14:30:30 by Arkadipta Mojumder

Create 248A. Cupboards.cpp

One foggy Stockholm morning, Karlsson decided to snack on some jam in his friend Lillebror Svantenson's house. Fortunately for Karlsson, there wasn't anybody in his friend's house. Karlsson was not going to be hungry any longer, so he decided to get some food in the house.

Karlsson's gaze immediately fell on n wooden cupboards, standing in the kitchen. He immediately realized that these cupboards have hidden jam stocks. Karlsson began to fly greedily around the kitchen, opening and closing the cupboards' doors, grab and empty all the jars of jam that he could find.

And now all jars of jam are empty, Karlsson has had enough and does not want to leave traces of his stay, so as not to let down his friend. Each of the cupboards has two doors: the left one and the right one. Karlsson remembers that when he rushed to the kitchen, all the cupboards' left doors were in the same position (open or closed), similarly, all the cupboards' right doors were in the same position (open or closed). Karlsson wants the doors to meet this condition as well by the time the family returns. Karlsson does not remember the position of all the left doors, also, he cannot remember the position of all the right doors. Therefore, it does not matter to him in what position will be all left or right doors. It is important to leave all the left doors in the same position, and all the right doors in the same position. For example, all the left doors may be closed, and all the right ones may be open.

Karlsson needs one second to open or close a door of a cupboard. He understands that he has very little time before the family returns, so he wants to know the minimum number of seconds t, in which he is able to bring all the cupboard doors in the required position.

Your task is to write a program that will determine the required number of seconds t.

---
## [Did-hub/hello-world](https://github.com/Did-hub/hello-world)@[8cec696cac...](https://github.com/Did-hub/hello-world/commit/8cec696cac2ca2fb308d09c794c8ff5de06e5f65)
#### Monday 2021-12-27 14:59:36 by Did-hub

Update README.md

But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure

---
## [Sala/adventofcode](https://github.com/Sala/adventofcode)@[bc4e989319...](https://github.com/Sala/adventofcode/commit/bc4e98931942c08ed62451e29a007b4aec058da7)
#### Monday 2021-12-27 16:39:55 by sala

For the last three days, things got complicated as I had to travel and visit family for Christmas.

on the 23rd I'll be honest, I have just done it manually using notepad++ and a calculator. after that I've built the graphic part, so I can test it more. it's not perfect, it doesn't cover all cases, but you can get a good result.

24th of December was a real challenge. my first try was an awful brute force and only late in the night I realised that  I should use a genetic algorithm. surprisingly the implementation was really easy to finish. waiting for the result and fine-tuning the search was interesting.

25th was straight forward, but once again I had some "family business" and I could not finish as quick as I wanted.

This year was really nice. Next year in december I'll be a 5 months old father... so we'll see what I can do.

---
## [newstools/2021-national-daily-nigeria](https://github.com/newstools/2021-national-daily-nigeria)@[ddc83331ce...](https://github.com/newstools/2021-national-daily-nigeria/commit/ddc83331cebbb8daad67fb881c1730eed33f8ae9)
#### Monday 2021-12-27 18:48:17 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/yahoo-boy-on-the-run-after-hacking-his-girlfriend-to-death-on-christmas-eve-in-edo-video/]

---
## [basijijo/helena](https://github.com/basijijo/helena)@[a0b9ce039f...](https://github.com/basijijo/helena/commit/a0b9ce039fdf027e3c7f4532d36b247fb9cab879)
#### Monday 2021-12-27 18:51:55 by basijijo

const fs = require('fs') const Asena = require('../events'); const {MessageType, Mimetype } = require('@adiwajshing/baileys'); const FilterDb = require('./sql/filters'); const Config = require('../config') const jid = Config.DISBGM != false ? Config.DISBGM.split(',') : []; const Language = require('../language'); const Lang = Language.getString('filters');  if (Config.WORKTYPE == 'private') {  Asena.addCommand({pattern: 'filter ?(.*)', fromMe: true, desc: Lang.FILTER_DESC, dontAddCommandList: true}, (async (message, match) => {     match = match[1].match(/[\'\"\“](.*?)[\'\"\“]/gsm);      if (match === null) {         filtreler = await FilterDb.getFilter(message.jid);         if (filtreler === false) {             await message.client.sendMessage(message.jid,Lang.NO_FILTER,MessageType.text)         } else {             var mesaj = Lang.FILTERS + '\n';             filtreler.map((filter) => mesaj += '```' + filter.dataValues.pattern + '```\n');             await message.client.sendMessage(message.jid,mesaj,MessageType.text);         }     } else {         if (match.length < 2) {             return await message.client.sendMessage(message.jid,Lang.NEED_REPLY + ' ```.filter "sa" "as"',MessageType.text);         }         await FilterDb.setFilter(message.jid, match[0].replace(/['"“]+/g, ''), match[1].replace(/['"“]+/g, '').replace(/[#]+/g, '\n'), match[0][0] === "'" ? true : false);         await message.client.sendMessage(message.jid,Lang.FILTERED.format(match[0].replace(/['"]+/g, '')),MessageType.text);     } })); Asena.addCommand({pattern: 'stop ?(.*)', fromMe: true, desc: Lang.STOP_DESC, dontAddCommandList: true}, (async (message, match) => {     match = match[1].match(/[\'\"\“](.*?)[\'\"\“]/gsm);     if (match === null) {         return await message.client.sendMessage(message.jid,Lang.NEED_REPLY + '\n*Example:* ```.stop "hello"```',MessageType.text)     }      del = await FilterDb.deleteFilter(message.jid, match[0].replace(/['"“]+/g, ''));          if (!del) {         await message.client.sendMessage(message.jid,Lang.ALREADY_NO_FILTER, MessageType.text)     } else {         await message.client.sendMessage(message.jid,Lang.DELETED, MessageType.text)     } })); Asena.addCommand({on: 'text', fromMe: false}, (async (message, match) => {     if (message.jid.includes(Config.YAK)) {              return;         }      var filtreler = await FilterDb.getFilter(message.jid);     if (!filtreler) return;      filtreler.map(         async (filter) => {             pattern = new RegExp(filter.dataValues.regex ? filter.dataValues.pattern : ('\\b(' + filter.dataValues.pattern + ')\\b'), 'gm');             if (pattern.test(message.message)) {                 await message.client.sendMessage(message.jid,filter.dataValues.text, MessageType.text, {quoted: message.data});             }         }     ); })); } else if (Config.WORKTYPE == 'public') {  Asena.addCommand({pattern: 'filter ?(.*)', fromMe: true, desc: Lang.FILTER_DESC, dontAddCommandList: true}, (async (message, match) => {     match = match[1].match(/[\'\"\“](.*?)[\'\"\“]/gsm);      if (match === null) {         filtreler = await FilterDb.getFilter(message.jid);         if (filtreler === false) {             await message.client.sendMessage(message.jid,Lang.NO_FILTER,MessageType.text)         } else {             var mesaj = Lang.FILTERS + '\n';             filtreler.map((filter) => mesaj += '```' + filter.dataValues.pattern + '```\n');             await message.client.sendMessage(message.jid,mesaj,MessageType.text);         }     } else {         if (match.length < 2) {             return await message.client.sendMessage(message.jid,Lang.NEED_REPLY + ' ```.filter "sa" "as"',MessageType.text);         }         await FilterDb.setFilter(message.jid, match[0].replace(/['"“]+/g, ''), match[1].replace(/['"“]+/g, '').replace(/[#]+/g, '\n'), match[0][0] === "'" ? true : false);         await message.client.sendMessage(message.jid,Lang.FILTERED.format(match[0].replace(/['"]+/g, '')),MessageType.text);     } })); Asena.addCommand({pattern: 'stop ?(.*)', fromMe: true, desc: Lang.STOP_DESC, dontAddCommandList: true}, (async (message, match) => {     match = match[1].match(/[\'\"\“](.*?)[\'\"\“]/gsm);     if (match === null) {         return await message.client.sendMessage(message.jid,Lang.NEED_REPLY + '\n*Example:* ```.stop "hello"```',MessageType.text)     }      del = await FilterDb.deleteFilter(message.jid, match[0].replace(/['"“]+/g, ''));          if (!del) {         await message.client.sendMessage(message.jid,Lang.ALREADY_NO_FILTER, MessageType.text)     } else {         await message.client.sendMessage(message.jid,Lang.DELETED, MessageType.text)     } })); Asena.addCommand({on: 'text', fromMe: false}, (async (message, match) => {     if (message.jid.includes(Config.YAK)) {              return;         }          if(Config.BGMFILTER){         let banned = jid.find( Jid => Jid === message.jid);         if(banned !== undefined) return         if (!!message.mention && message.mention[0] == '919645628728@s.whatsapp.net') { await message.client.sendMessage(message.jid, fs.readFileSync('./sourav/music.mp3'), MessageType.audio, { mimetype: Mimetype.mp4Audio, quoted : message.data, ptt: true})         }         if (!!message.mention && message.mention[0] == Config.AFNN) { await message.client.sendMessage(message.jid, fs.readFileSync('./sourav/music.mp3'), MessageType.audio, { mimetype: Mimetype.mp4Audio, quoted : message.data, ptt: true})         } const array = ['Ayin','Ayinu','Bgm','Bot','Bye','Good night','Hello','Hi','Neymar','Pm','Sed','alive','assist','ban','bgm','bot','converting','fake','fork','fuck','music','myre','njan','number','oombi','poda','raganork','remove','reply','sed','subscribe','Basil'] array.map( async (a) =>  let pattern = new RegExp(`\\b${a}\\b`, 'g'); if(pattern.test(message.message)){        await message.client.sendMessage(message.jid, fs.readFileSync('./sourav/' + a + '.mp3'), MessageType.audio, { mimetype: Mimetype.mp4Audio, quoted: message.data, ptt: true}) } });     }      var filtreler = await FilterDb.getFilter(message.jid);     if (!filtreler) return;      filtreler.map(         async (filter) => {             pattern = new RegExp(filter.dataValues.regex ? filter.dataValues.pattern : ('\\b(' + filter.dataValues.pattern + ')\\b'), 'gm');             if (pattern.test(message.message)) {                 await message.client.sendMessage(message.jid,filter.dataValues.text, MessageType.text, {quoted: message.data});             }         }     ); })); Asena.addCommand({on: 'text', fromMe: false}, (async (message, match) => {     if (message.jid.includes(Config.YAK)) {              return;         }          if(Config.AUTOSTICKER){         let banned = jid.find( Jid => Jid === message.jid);         if(banned !== undefined) return const array = ['Akshan','Anthass','Ayin','Aysheri','Ayye','Ayyo','Bgm','Bye','Da','Ded','Ee','Eee','Enth','Entha','Enthada','Girls','Good morning','Good night','Hello','Hi','Hy','Kurippe','Kurumb','Line','Logan','Love','Mm','Monu','Msd','Nope','Ok','Pattumo','Pm','Poda','Poli','Pova','Raganork','Save','Sed','Shoo','Smile','Sourav','Sunny','Udayipp','Vaa','Vannu','Vijay','Wait','ban','bot','broken','bye','chattho','cheyyatte','cute','edit','engane und','etha','fear','filter','gn','help','ithokke enth','ivan','left','mention','myre','naanam','nadakkatte','number','paavam','padikk','para','photo','please','poda','power','poyi','remove','sed','seth','setth','sho','sticker','support','tag','umma','update','vibe','work','yo','ys'] array.map( async (a) => { let pattern = new RegExp(`\\b${a}\\b`, 'g'); if(pattern.test(message.message)){    await message.client.sendMessage(message.jid, fs.readFileSync('./souravkl11/' + a + '.webp'), MessageType.sticker, { mimetype: Mimetype.webp, quoted: message.data, ptt: false}) } }); }  var filtreler = await FilterDb.getFilter(message.jid); if (!filtreler) return;  })); }

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[45e40a3f08...](https://github.com/mrakgr/The-Spiral-Language/commit/45e40a3f088e4d8d63da69275c47c6b623665a5c)
#### Monday 2021-12-27 19:15:19 by Marko Grdinić

"11:15pm. Let me chill for a while. Then I'll do the painting. To be honest, the shot looks more amateurish than in my vague imagination. But that does not matter - this is just an exercise to see how well I can trace things. I wnat to make something appealing.

12:45pm. Done with breakfast and chores. Let me finish what I am reading and then I will start. Finally it is time to do some painting.

Enough of the endless tutorials. I can't stand them anymore. I should take it nice and easy.

1:10pm. Just one more chapter of Circle Zero and I will start. I was so bored with it yesterday, but now that I am fresher I find it more fun.

1:15pm. Let me start.

How long has it been since I last did anything Clip Studio. I have been really itching to do 2d art. First of all, how do I import an image?

1:25pm. Easy enough. Ok, let me do the outlines.

1:35pm. Hmmm, no. Here I am trying to do lineart, when I really should be masking things out. I need to separate the layers into two parts. The bottom part is clearly a sofa while the upper part is the space with the stars.

Instead, I am putting in the black line over where I think the sofa should be and in the process going over the cushions. I want to try a painterly approach where I put dark some blue and black on the top and red on the bottom and then follow things up from there. That is the way to do this.

Masks are one of the most important tools for a digital 2d artist and here is where I need to make use of them.

Let me take a short break here.

1:50pm. Let me resume. First order of business is to refresh my memory of CSP.

Ok, I refreshed my memory of selection layers. Let me get the lasso.

FFFFFFFFFFFFFFFFFFFFFuck. Why did it apply the polylines?

I messed up the selection. Art is suffering.

2:30pm. It is beter to do the selections directly without using the polylines.

I am so slow right now. But I should keep going. At some point I am going to speed up. Right now I am trying to plan things out. Let me do the cushions

3:15pm. Done with the first cushion. I need to persevere. I'll reserve judgement until the painting is complete. So far it reminds me of those bleached 16-bit old game images. It might turn out that painting is too difficult for somebody at my current level. In that case I'll try a cell shaded style. But until then, let me push forward. Let me do cushion 2.

4:15pm. I am thinking. No, it is not going well. It looks too flat, and I know why. The large flat area in the cushions. The parts that I actually did are decent, but if continue on this course the end result will be amaterish.

I know why. I understand exactly why.

I can't really immitate the workflow from the Ctrl + Paint guy. The colors are giving me a lot of trouble.

I do not think I really understand the painterly process after all. Why did work for me however is that black and white sketch of a can that I did months ago when I first got the tablet.

So I am thinking why not immitate that? But compared to that time, I know how to use masks and gradient maps. So I can do coloring just fine. Ok, let me copy this, since I want to reuse the masks, but I'll do the process from the ground up. I'll ditch the markers, and go back to the real pencil.

Right now the process is wrong. Rather than doing broad strokes, and erasing, I am being very careful to do the highlights and it is to my detribment. For the kind of effort I am putting in, I am not getting the payoff that I want.

This time, how about I start with the space? In addition to that...

Let me open a new file so I can actually try out the gradient maps without anything interfering.

4:45pm. Hmmm, how confusing. Why do gradient maps not work inside a folder?

https://youtu.be/r1iC9PuGh6I
[Clip Studio] How to Use Gradient Map

Ah, whatever. Let me watch this. Maybe that will give me an answer.

5pm. https://www.reddit.com/r/ClipStudio/comments/c9bbgc/is_there_a_way_to_stop_gradient_map_from/

This does not work for me, let me play with it more.

...I have no idea what is going on. Clipping to the layer below does not work. Putting it in a folder does not work.

I have no idea, it only works when it is in the outermost level.

Let me do more research.

> Set the folder's blending mode to "normal" (instead of the default blending mode, "through")

This guy got it the opposite. The default is normal and to make the grad maps work, I need to set it to through.

Still, what would happen if I had nested folders.

Then it stops working. It seems that folders being through causes them to have dynamic scope. It does not prevent the grad map from affecting the outside. Ah, what the hell?

Why is this so difficult?

https://youtu.be/ALgSJiXm4SY
How to Use GRADIENT MAPS and LAYER MASKS to color

This vid got me into them in the first place.

Let me watch it again. There is no way around it. I am going to have to concern myself with this.

5:15pm. No, she never use a folder or clipping to the layer below.

https://www.youtube.com/watch?v=EbOibnMoEPE
How I use the gradient map feature in Clipstudio Paint

Let me watch this.

Let me just ask on the Reddit sub.

https://www.reddit.com/r/ClipStudio/comments/rpr63s/how_to_make_gradient_maps_work_with_layer_clipping/

Now let me get back to the video.

https://youtu.be/EbOibnMoEPE?t=375

Huh, it seems to be working fine for him.

5:45pm. I still haven't figured this out. Damn.

6:10pm. Had to take a break. This gave me time to think about the issue. I think this issue has something to do with transparency and how CSP works.

6:25pm. I figured it out. I guess if I want transparency, I'll have to use masks for that.

This is unfortunate as it will make reflections more difficult.

CSP's grad maps are crappy.

I think I understand why this is going on. It is outright mapping the colors and ignoring transparency. It should be possible for it to do what I want, but it does not seem that feature is here.

Ok, if it is just transparency I can get that through masks. No problem.

6:50pm. Had to leave for lunch.

Let me do some more.

7:05pm. It is really annoying to keep having to change brush sizes constantly in CSP.

7:40pm. Success. When you zoom out, you can barely tell the difference between my own cushion and the others in the picture. Gradient maps rock.

I made the right choice. I am actually quite enjoying myself now. But let me stop here. I am going to do the rest of the picture tomorrow hopefully. I feel like I caught my stride.

I need to establish the process. Trying to do the painting directly is too much for my meager skills, just taking care of the tones and gradient mapping that make the process a lot easier.

And this technique is not weak at all, it looks quite appealing. I think that in general appealing images have segments with uniform color schemes.

For example, the sky is wisps of dark blue with black, the couch is various shades of red, and the stars are white white a yellow outline. This is a fairly workable way of thinking about color. Think of an overall scheme for a particular segment and then work within it.

Gradient maps mesh extremely well with that way of doing things. The technique works because colors in the real world are highly patterned and not arbitrary.

I like this, I really like this. I got a lot of use out of color ramps when messing with procedural textures, and they exactly the same thing as gradient maps.

7:55pm. Tomorrow, I am going to work on customizing my tool palete. I have all sorts of crap set to my hotkeys and it is making using the tools that I want a lot harder. I need a soft and hard marker (for selections), a soft airbrush, the blur tool, and not much else. Selection and curve tools I can leave out. Erasers I can immitate by using C with any of the existing brushes. This switches them to lowering the alpha. When I originally set the shortcuts I did not know that.

I think I'll also ditch opacity for density. I'll have to think about that.

8:10pm. Let me close here. Tomorrow, I'll be able to enjoy myself. No more tutorial hell, just art. I am going to reach my goals eventually."

---
## [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)@[92e6094449...](https://github.com/FreeCAD/FreeCAD/commit/92e6094449275e89e6ffd7a74c32e3ce3c62c1e6)
#### Monday 2021-12-27 20:03:57 by Abdullah Tahiri

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
## [Neternels/android_kernel_xiaomi_mojito](https://github.com/Neternels/android_kernel_xiaomi_mojito)@[19b5a417b8...](https://github.com/Neternels/android_kernel_xiaomi_mojito/commit/19b5a417b8c50382b94520b279db352288813dc3)
#### Monday 2021-12-27 20:15:41 by Cyber Knight

drivers/misc: debloat ximi changes

FUCK YOU XIMI WHO NEEDS CRAP LIKE mi_opensource.c AND FFS JUST REMOVE INCOMPLETE FUNCTIONS WHY EVEN COMMENT THEM!!!

Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [Neternels/android_kernel_xiaomi_mojito](https://github.com/Neternels/android_kernel_xiaomi_mojito)@[b7acfde5e9...](https://github.com/Neternels/android_kernel_xiaomi_mojito/commit/b7acfde5e912518f7f02f91e097c40c96f643e8e)
#### Monday 2021-12-27 20:16:10 by Cyber Knight

drivers/misc: debloat ximi changes

FUCK YOU XIMI WHO NEEDS CRAP LIKE mi_opensource.c AND FFS JUST REMOVE INCOMPLETE FUNCTIONS WHY EVEN COMMENT THEM OUT!!!

Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [spacestation13/dm-playground-linux](https://github.com/spacestation13/dm-playground-linux)@[e7ea78ea0f...](https://github.com/spacestation13/dm-playground-linux/commit/e7ea78ea0f37f2385e76a311c9bb07b6e3d7766d)
#### Monday 2021-12-27 20:47:29 by alexkar598

- Changes the patches as some of them have gone upstream.
- Disable busybox syslog as the kernel does not have syslog compiled in
- Disabled urandom scripts as fuck you that's why. It slows down the boot process and we can live without entropy.
- Moves the controller on dev console and sets it to respawn

---
## [pmmp/PocketMine-MP](https://github.com/pmmp/PocketMine-MP)@[d9c70cb176...](https://github.com/pmmp/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Monday 2021-12-27 21:54:39 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [BredPitch/PortCARL_RC3_21](https://github.com/BredPitch/PortCARL_RC3_21)@[26e528ed40...](https://github.com/BredPitch/PortCARL_RC3_21/commit/26e528ed40dd5cf03a9a83593b14e736480bc9cd)
#### Monday 2021-12-27 22:18:56 by derPUPE

die grafik zum ANSI Art Meisterwerk 

he legenday Acid Trip ANSIart as Adventure Scroller

Details: https://www.deviantart.com/radman1/art/blocktronics-ACiD-trip-ANS-version-405799573

The Source of the incredible ANSI was created by 22 artists from 6 different countries. At 3,266 lines long, this is far and away the longest ANSI scroller ever created.

First place winner of the ANSI/ASCII competition at Demosplash 2013, held at Carnegie Mellon University, October 4-5, 2013. The ANSI received the honor of a perfect score from the Demosplash audience.

This ANSI will be published as part of an upcoming ACiD tribute artpack by Blocktronics, named "Blocktronics: ACiD Trip", slated to be released on 11.12.13 (November 12, 2013).

Full credits: accessdenies, avg, cyonx, Deeply Disturbed, delicious, enzO, filth, H7, misfit, mattmatthew, ober, RaD Man, retribution, ReV, smoke, sonic, spear, The Creep Fever, the text exorcist, ungennant, whazzit, zerovision.

Additional trivia:

This ANSI was created using a collaborative ANSI editor called PabloDraw. Essentially a chatroom with an interactive ANSI/ASCII canvas that anyone can edit.
Two (2) PabloDraw servers were necessary to create this ANSI due to accommodate a current limitation of 2048 lines on the Windows version of PabloDraw.
It takes roughly 2 minutes to scroll this ANSI at full speed in PabloDraw. At 722KB, it would take roughly 6 & 1/2 minutes to display at 14,400 bps. (source: calctool.org)
Imagine 131 computer monitors stacked on top of each other. If this ANSI were to be broken up into separate 80x25 chunks, the standard resolution during the dialup BBS era, this ANSI would fill 131 CRT displays.
4 different artists came out of long term retirement to contribute to this ANSI, including Sonic, who had not drawn ANSI since a time when TheDraw was the editor of choice.
Scroler-Video https://www.youtube.com/watch?v=6zpUb3mUExA

---
## [keyy123/Node](https://github.com/keyy123/Node)@[0a25dbe026...](https://github.com/keyy123/Node/commit/0a25dbe026ece7b7d6a9466703b52f7fb844c422)
#### Monday 2021-12-27 22:52:59 by keyy123

I just used async await to make the Mongoose commands more developer friendly. I tThrough this experience     experience of addressing my weakpoints in Mongoose and MongoDB. I really think I should go back into my 3rd project nad upd    project to update the back-end using mongoose and mongodb. I have some cool features to add. HopIt'll be a fun experifun      time!

---
## [newstools/2021-the-times](https://github.com/newstools/2021-the-times)@[95512d89b8...](https://github.com/newstools/2021-the-times/commit/95512d89b8cc48cba9465868e088d80f25d78ebf)
#### Monday 2021-12-27 23:08:12 by Billy Einkamerer

Created Text For URL [www.timeslive.co.za/news/south-africa/2021-12-27-i-mourn-the-loss-of-a-brother-my-loyal-friend-and-my-spiritual-leader-graa-machel/]

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[b59ef639d4...](https://github.com/tdauth/wowr/commit/b59ef639d41b6de1c336f052aad241713570e432)
#### Monday 2021-12-27 23:37:52 by barade

1.9.3

- Increase number of respawn groups to fix missing respawns of creep bosses.
- Add The Burning Legion and Bosses to the player stats multiboard.
- Show level of Evolution in player stats.
- Show player stats multiboard from start but minimized.
- Rename AI players to AI.
- Increase gold of housings to 100 000.
- Add lost units and technologies to player stats.
- Fix tooltip of Improved Lumber Harvesting for Furbolgs.
- Hide Blood Elf Cage model on death.
- Increase number of farms and workers for Naga and Furbolg AI.
- Add quest log entries Hidden Bases and Hero Journey.
- Add Mountain Giant to tavern.
- Kil'Jaeden, Tichondrius, Eredar Warlock and Keeper of Frostmourne cost food now.
- Rename Ogrimmar to Orgrimmar for several heroes.
- Furbolg Tribal Center, Green Dragon Roost, Pig Farm and Dragon Roost require ground-pathable to be built now.
- Dragon Roost for Orcs costs 200 gold now.
- Fel Peon cost as much gold as regular Peons now.
- Keep Tier 2 XP bonus on repick and for second hero.
- Add many missing heroes to hero equivalents in the gameplay constants.
- Only show VIP welcome message if VIPs are enabled.
- Remove votes for leaving players from the votings in the beginning of the game.
- Add Goblin Laboratory and Black Market to many more start locations to make the game more fair.
- Add entry by the Ocean to Sunstrider Isle.
- Add black borders on the Ocean to Outland.
- Add quest log entry for the stats multiboard.
- Reduce quest log entries to Special Race Building.
- Reduce costs of Improved Power Generator.
- Add ability Drop all Items to Backpack.
- Add research Improved Mount which increases the movement speed of your mount.
- Add research levels to the tooltips of different researches with 100 levels.
- Fix icon of Unique - Legion´s Hate.
- Rename quest log entry "New Features" to "Reforged Version" and move it down.
- Fix icon of Engineering - Adept.
- Reduce collision size of Souls.
- Give Archimonde bonus hero Bash of Eredar Warlock.
- Add Neutral Shop which can built by Neutral Citizens and sells Orbs.
- Add names of VIPs to the VIP room.
- Reduce stock initial delay for Neutral Citizens to 0.
- Fix Orgrimmar name in floating text.

---
## [fowles/advent-of-code-2015](https://github.com/fowles/advent-of-code-2015)@[326d3d094f...](https://github.com/fowles/advent-of-code-2015/commit/326d3d094fb4071fc5a272ad06cefd0534d19915)
#### Monday 2021-12-27 23:40:12 by Matt Kulukundis

Day 12 part 1

reg​ex parsers for JSON will ins​tantly transport a programmer's consciousness into a world of ceaseless screaming, he comes, the pestilent slithy regex-infection wil​l devour your HT​ML parser, application and existence for all time like Visual Basic only worse he comes he comes do not fi​ght he com̡e̶s, ̕h̵i​s un̨ho͞ly radiańcé destro҉ying all enli̍̈́̂̈́ghtenment, HTML tags lea͠ki̧n͘g fr̶ǫm ̡yo​͟ur eye͢s̸ ̛l̕ik͏e liq​uid pain, the song of re̸gular exp​ression parsing will exti​nguish the voices of mor​tal man from the sp​here I can see it can you see ̲͚̖͔̙î̩́t̲͎̩̱͔́̋̀ it is beautiful t​he final snuffing of the lie​s of Man ALL IS LOŚ͖̩͇̗̪̏̈́T ALL I​S LOST the pon̷y he comes he c̶̮omes he comes the ich​or permeates all MY FACE MY FACE ᵒh god no NO NOO̼O​O NΘ stop the an​*̶͑̾̾​̅ͫ͏̙̤g͇̫͛͆̾ͫ̑͆l͖͉̗̩̳̟̍ͫͥͨe̠̅s ͎a̧͈͖r̽̾̈́͒͑e n​ot rè̑ͧ̌aͨl̘̝̙̃ͤ͂̾̆ ZA̡͊͠͝LGΌ ISͮ̂҉̯͈͕̹̘̱ TO͇̹̺ͅƝ̴ȳ̳ TH̘Ë͖́̉ ͠P̯͍̭O̚​N̐Y̡ H̸̡̪̯ͨ͊̽̅̾̎Ȩ̬̩̾͛ͪ̈́̀́͘ ̶̧̨̱̹̭̯ͧ̾ͬC̷̙̲̝͖ͭ̏ͥͮ͟Oͮ͏̮̪̝͍M̲̖͊̒ͪͩͬ̚̚͜Ȇ̴̟̟͙̞ͩ͌͝S̨̥̫͎̭ͯ̿̔̀ͅ

---
## [low-batt/mpv](https://github.com/low-batt/mpv)@[e2c24adebe...](https://github.com/low-batt/mpv/commit/e2c24adebede2d269b0fa2df3f1a05a44343e8c0)
#### Monday 2021-12-27 23:48:47 by Dudemanguy

wayland: unset hidden state in frame callback

More wayland weirdness. So previously, flipping a hidden state from true
to false was done in vo_wayland_wait_frame. In theory, this would be
after you get the frame callback and all those events so there's no
problem. However since the function also does a bunch of
flushing/dispatching/etc. to the default display queue so a lot of
unknown things can happen before we actually set the hidden variable
back to false. For example if a single image was paused and left on
another virtual desktop long enough (~5 minutes) while also not having
focus, switching back to that desktop could render it a black frame.

This edge case was supposed to be handled by the surface being activated
again in the toplevel event but apparently that doesn't always work. The
fix is to just delete all of that junk and set wl->hidden = false in the
frame callback. What's actually happening is kind of a mystery honestly.
Probably the compositor drops the buffers after a while as an
optimization (sensible) and forces a repaint if you switch back to the
virtual desktop. Somehow wl->hidden not being set to false would not
properly trigger a repaint (likely because it also sends a toplevel
event which does stuff) thus you just get a black window. If you just
make sure to set hidden in the frame callback, it appears like all of
these problems and edge cases are solved. Since this event must happen
first, that makes sense. That simplifies a lot of stuff and fixes some
subtle bugs at the same time so just go with this approach.

---

