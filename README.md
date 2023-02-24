## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-23](docs/good-messages/2023/2023-02-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,294,728 were push events containing 3,526,953 commit messages that amount to 269,010,357 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [jonpryor/java.interop](https://github.com/jonpryor/java.interop)@[6247614522...](https://github.com/jonpryor/java.interop/commit/6247614522c6886b473ff44fdce99e75d7189819)
#### Thursday 2023-02-23 00:31:03 by Jonathan Pryor

[Java.Interop.Tools.Expressions] Add Java.Interop.Tools.Expressions

Fixes: https://github.com/xamarin/java.interop/issues/616

Context: https://github.com/xamarin/java.interop/issues/14
Context: ff4053cb1e966ebec1c16f97211b9ded936f2707
Context: da5d1b8103bb90f156b93ebac9caa16cfc85764e
Context: 4787e0179b349ab5ee0d0dd03d08b694acea4971
Context: 41ba34856ab119ea6e22ab103320180143fdf03d

Remember `jnimarshalmethod-gen` (176240d2)?  And it's crazy idea to
use the `System.Linq.Expressions`-based custom marshaling
infrastructure (ff4053cb, da5d1b81) to generate JNI marshal methods
at build/packaging time.  And how we had to back burner it because
it depended upon `System.Reflection.Emit` being able to write
assemblies to disk, which is a feature that never made it to
.NET Core, and is still lacking as of .NET 7?

Add `src/Java.Interop.Tools.Expressions`, which contains code which
uses Mono.Cecil to compile `Expression<T>` expressions to IL.

Then update `jnimarshalmethod-gen` to use it!

~~ Usage ~~

	% dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp \
	  --jvm /Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home/lib/jli/libjli.dylib \
	  -o _x \
	  -L bin/TestDebug-net7.0 \
	  -L /usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0

First param is assembly to process; `Java.Interop.Export-Tests.dll`
is handy because that's what the `run-test-jnimarshal` target in
`Makefile` processed.

  * `-v -v` is *really* verbose output

  * `--keeptemp` is keep temporary files, in this case
    `_x/Java.Interop.Export-Tests.dll.cecil`.

  * `--jvm PATH` is the path to the JVM library to load+use.

  * `-o DIR` is where to place output files; this will create
    `_x/Java.Interop.Export-Tests.dll`.

  * `-L DIR` adds `DIR` to library resolution paths; this adds
    `bin/TestDebug/net7.0` (dependencies of
    `Java.Interop.Export-Tests.dll`) and
    `Microsoft.NETCore.App/7.0.0-rc.1.22422.12` (net7 libs).

By default the directories containing input assemblies and the
directory containing `System.Private.CoreLib.dll` are part of the
default `-L` list.

When running in-tree, e.g. AzDO pipeline execution, `--jvm PATH`
will attempt to read the path in `bin/Build*/JdkInfo.props`
a'la `TestJVM` (002dea4a).  This allows an in-place update in
`core-tests.yaml` which does:

	dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp -o bin/TestDebug-net7.0

~~ Using `jnimarshalmethod-gen` output ~~

What does `jnimarshalmethod-gen` *do*?

	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll > beg.il
	% ikdasm _x/Java.Interop.Export-Tests.dll > end.il
	% git diff --no-index beg.il end.il
	# https://gist.github.com/jonpryor/b8233444f2e51043732bea922f6afc81

is a ~1KB diff which shows, paraphrasing greatly:

	public partial class ExportTest {
	    partial class '__<$>_jni_marshal_methods' {
	        static IntPtr funcIJavaObject (IntPtr jnienv, IntPtr this) => …
	        // …
	        [JniAddNativeMethodRegistration]
	        static void __RegisterNativeMembers (JniNativeMethodRegistrationArguments args) => …
	    }
	}
	internal delegate long _JniMarshal_PP_L (IntPtr jnienv, IntPtr self);
	// …

wherein `ExportTest._<$>_jni_marshal_methods` and the `_JniMarshal*`
delegate types are added to the assembly.

This also unblocks the desire stated in 4787e017:

> For `Java.Base`, @jonpryor wants to support the custom marshaling
> infrastructure introduced in 77a6bf86.  This would allow types to
> participate in JNI marshal method ("connector method") generation
> *at runtime*, allowing specialization based on the current set of
> types and assemblies.

What can we do with this `jnimarshalmethod-gen` output?  Use it!

First, make sure the tests work:

	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 103 ms - Java.Interop.Export-Tests.dll (net7.0)

Then update/replace the unit test assembly with
`jnimarshalmethod-gen` output:

	% \cp _x/Java.Interop.Export-Tests.dll bin/TestDebug-net7.0
	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Total tests: 17
	     Passed: 17

`core-tests.yaml` has been updated to do this.

~~ One-Off Tests ~~

One-off tests: ensure that the generated assembly can be decompiled:

	% ikdasm  bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll
	% monodis bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll

	% ikdasm  _x/Java.Interop.Export-Tests.dll
	% monodis _x/Java.Interop.Export-Tests.dll
	# which currently fails :-()

Re-enable most of `Java.Interop.Export-Tests.dll` for .NET 7;
see 41ba3485, which disabled those tests.

To verify the generated IL, use the [dotnet-ilverify][0] tool:

	dotnet tool install --global dotnet-ilverify

Usage of which is "weird":

	$HOME/.dotnet/tools/ilverify _x/Java.Interop.Export-Tests.dll \
	  --tokens --system-module System.Private.CoreLib \
	  -r 'bin/TestDebug-net7.0/*.dll' \
	  -r '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0/*.dll'
	All Classes and Methods in /Volumes/Xamarin-Work/src/xamarin/Java.Interop/_x/Java.Interop.Export-Tests.dll Verified.
	# no errors!

where:

  * `--tokens`: Include metadata tokens in error messages.
  * `--system-module NAME`: set the "System module name".  Defaults
    to `mscorlib`, which is wrong for .NET 5+, so this must be set to
    `System.Private.CoreLib` (no `.dll` suffix!).
  * `-r FILE-GLOB`: Where to resolve assembly references for the
    input assembly.  Fortunately file globs are supported…

~~ Removing `System.Private.CoreLib` ~~

`System.Private.CoreLib.dll` is *private*; it's not part of the
public assembly surface area, so you can't use
`csc -r:System.Private.CoreLib …` and expect it to work.  This makes
things interesting because *at runtime* everything "important" is in
`System.Private.CoreLib.dll`, like `System.Object`.

Specifically, if we do the "obvious" thing and do:

	newTypeDefinition.BaseType = assemblyDefinition.MainModule
	    .ImportReference (typeof (object));

you're gonna have a bad type, because the resulting IL for
`newTypeDefinition` will have a base class of
`[System.Private.CoreLib]System.Object`, which isn't usable.

Fix this by:

 1. Writing the assembly to a `Stream`.
 2. Reading the `Stream` from (1)
 3. Fixing all member references and assembly references so that
    `System.Private.CoreLib` is not referenced.

If `jnimarshalmethod-gen.dll --keeptemp` is used, then a `.cecil`
file is created with the contents of (1).

Additionally, and unexpectedly -- [jbevain/cecil#895][1] -- Mono.Cecil
adds a reference to the assembly being modified.  Remove the declaring
assembly from `AssemblyReferences`.

[0]: https://www.nuget.org/packages/dotnet-ilverify
[1]: https://github.com/jbevain/cecil/issues/895

---
## [LordPapalus/Citadel-Station-13-RP](https://github.com/LordPapalus/Citadel-Station-13-RP)@[81c1229373...](https://github.com/LordPapalus/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Thursday 2023-02-23 00:32:21 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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

:cl:
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [OpenAngelArena/oaa](https://github.com/OpenAngelArena/oaa)@[56395dd4f5...](https://github.com/OpenAngelArena/oaa/commit/56395dd4f523b90cd0b5d64857ad877e80da2343)
#### Thursday 2023-02-23 01:27:01 by Darko V

Modifiers February Update (#3464)

* Hybrid modifier attack damage stacks are now based on spell cooldown.
* Blood Magic modifier: hopefully fixed not having mana when respawning after losing this modifier.
* Brute modifier: Damage per hp reduced from 0.08 to 0.05
* Chaos modifier: Added Drunkard modifier to the pool of modifiers. Drunkard: 10% chance to do 3x critical damage on each attack and spell damage instance. 10% chance to avoid any damage. Has a random chance to miss a spell and moves randomly when idle.
* Cursed Attack modifier no longer has a miss chance.
* Cursed Attack modifier now provides a 50% chance to deal 350 pure damage.
* Cursed Attack modifier now also reduced attack damage by 125.
* Chaos modifier: Disabled Explosive Death and Guardian's Weakness after 20 min.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[c58cbb4dfb...](https://github.com/lizardqueenlexi/orbstation/commit/c58cbb4dfb42e0d9d6198c3ad581dc5a4d2f8f48)
#### Thursday 2023-02-23 01:40:23 by John Willard

Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID


https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov


![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.


https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Mu-L/graphql-engine](https://github.com/Mu-L/graphql-engine)@[6e574f1bbe...](https://github.com/Mu-L/graphql-engine/commit/6e574f1bbe521e561a8116bf167a6be1060bc8d4)
#### Thursday 2023-02-23 02:19:31 by Antoine Leblanc

harmonize network manager handling

## Description

### I want to speak to the `Manager`

Oh boy. This PR is both fairly straightforward and overreaching, so let's break it down.

For most network access, we need a [`HTTP.Manager`](https://hackage.haskell.org/package/http-client-0.1.0.0/docs/Network-HTTP-Client-Manager.html). It is created only once, at the top level, when starting the engine, and is then threaded through the application to wherever we need to make a network call. As of main, the way we do this is not standardized: most of the GraphQL execution code passes it "manually" as a function argument throughout the code. We also have a custom monad constraint, `HasHttpManagerM`, that describes a monad's ability to provide a manager. And, finally, several parts of the code store the manager in some kind of argument structure, such as `RunT`'s `RunCtx`.

This PR's first goal is to harmonize all of this: we always create the manager at the root, and we already have it when we do our very first `runReaderT`. Wouldn't it make sense for the rest of the code to not manually pass it anywhere, to not store it anywhere, but to always rely on the current monad providing it? This is, in short, what this PR does: it implements a constraint on the base monads, so that they provide the manager, and removes most explicit passing from the code.

### First come, first served

One way this PR goes a tiny bit further than "just" doing the aforementioned harmonization is that it starts the process of implementing the "Services oriented architecture" roughly outlined in this [draft document](https://docs.google.com/document/d/1FAigqrST0juU1WcT4HIxJxe1iEBwTuBZodTaeUvsKqQ/edit?usp=sharing). Instead of using the existing `HasHTTPManagerM`, this PR revamps it into the `ProvidesNetwork` service.

The idea is, again, that we should make all "external" dependencies of the engine, all things that the core of the engine doesn't care about, a "service". This allows us to define clear APIs for features, to choose different implementations based on which version of the engine we're running, harmonizes our many scattered monadic constraints... Which is why this service is called "Network": we can refine it, moving forward, to be the constraint that defines how all network communication is to operate, instead of relying on disparate classes constraint or hardcoded decisions. A comment in the code clarifies this intent.

### Side-effects? In my Haskell?

This PR also unavoidably touches some other aspects of the codebase. One such example: it introduces `Hasura.App.AppContext`, named after `HasuraPro.Context.AppContext`: a name for the reader structure at the base level. It also transforms `Handler` from a type alias to a newtype, as `Handler` is where we actually enforce HTTP limits; but without `Handler` being a distinct type, any code path could simply do a `runExceptT $ runReader` and forget to enforce them.

(As a rule of thumb, i am starting to consider any straggling `runReaderT` or `runExceptT` as a code smell: we should not stack / unstack monads haphazardly, and every layer should be an opaque `newtype` with a corresponding run function.)

## Further work

In several places, i have left TODOs when i have encountered things that suggest that we should do further unrelated cleanups. I'll write down the follow-up steps, either in the aforementioned document or on slack. But, in short, at a glance, in approximate order, we could:

- delete `ExecutionCtx` as it is only a subset of `ServerCtx`, and remove one more `runReaderT` call
- delete `ServerConfigCtx` as it is only a subset of `ServerCtx`, and remove it from `RunCtx`
- remove `ServerCtx` from `HandlerCtx`, and make it part of `AppContext`, or even make it the `AppContext` altogether (since, at least for the OSS version, `AppContext` is there again only a subset)
- remove `CacheBuildParams` and `CacheBuild` altogether, as they're just a distinct stack that is a `ReaderT` on top of `IO` that contains, you guessed it, the same thing as `ServerCtx`
- move `RunT` out of `RQL.Types` and rename it, since after the previous cleanups **it only contains `UserInfo`**; it could be bundled with the authentication service, made a small implementation detail in `Hasura.Server.Auth`
-  rename `PGMetadaStorageT` to something a bit more accurate, such as `App`, and enforce its IO base

This would significantly simply our complex stack. From there, or in parallel, we can start moving existing dependencies as Services. For the purpose of supporting read replicas entitlement, we could move `MonadResolveSource` to a `SourceResolver` service, as attempted in #7653, and transform `UserAuthenticationM` into a `Authentication` service.

PR-URL: https://github.com/hasura/graphql-engine-mono/pull/7736
GitOrigin-RevId: 68cce710eb9e7d752bda1ba0c49541d24df8209f

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[7d27d8508c...](https://github.com/realforest2001/forest-cm13/commit/7d27d8508ce0723dbbcf1dfad9810a3092a71f61)
#### Thursday 2023-02-23 03:08:46 by TotalEpicness

Fixes invincible base crusher (#2682)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes an oversight that allowed base crusher to have half it's intended
shield cooldown
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.
runs
Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Never intended on the first place and led to crusher being busted as
fuck as it is currently.

This was never intended and was a mess up on my part. It fell through
from the painfully long development that Charger had as months went by
between testing sessions and TMs, along with my inexperience with larger
projects and bad note taking at the time.

Maintainers are also supposed to filter stuff like this but after like a
billion code reviews Charger had, I can see how it got through on their
end as well.

Nevertheless this dies here. 

funny contrib moment
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
it runs
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

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

:cl: Totalepicness
balance: Fixes base crusher having half it's intended cooldown for the
shield ability
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Epicness <coolguyethanw@gmail.com>

---
## [camobiwon/Voidway-Bot](https://github.com/camobiwon/Voidway-Bot)@[cff6be8055...](https://github.com/camobiwon/Voidway-Bot/commit/cff6be805568e25040e176af5c0c1a250fcce3fb)
#### Thursday 2023-02-23 04:44:04 by extraes

Unknown key in thread update: applied_tags - this should be reported to library developers
holy fucking shit thanks D#+

---
## [HongyiRen2009/Civilization](https://github.com/HongyiRen2009/Civilization)@[1d8df98397...](https://github.com/HongyiRen2009/Civilization/commit/1d8df98397c74652aa74d3f14618ab2efc6dc3aa)
#### Thursday 2023-02-23 05:34:22 by alexey

simplify tutorial popup text
The need for the Constitution grew out of problems with the Articles of Confederation, which established a “firm league of friendship” between the States, and vested most power in a Congress of the Confederation. This power was, however, extremely limited—the central government conducted diplomacy and made war, set weights and measures, and was the final arbiter of disputes between the States. Crucially, it could not raise any funds itself, and was entirely dependent on the States themselves for the money necessary to operate. Each State sent a delegation of between two and seven members to the Congress, and they voted as a bloc with each State getting one vote. But any decision of consequence required a unanimous vote, which led to a government that was paralyzed and ineffectual.A movement to reform the Articles began, and invitations to attend a convention in Philadelphia to discuss changes to the Articles were sent to the State legislatures in 1787. In May of that year, delegates from 12 of the 13 States (Rhode Island sent no representatives) convened in Philadelphia to begin the work of redesigning government. The delegates to the Constitutional Convention quickly began work on drafting a new Constitution for the United States.The Constitutional ConventionA chief aim of the Constitution as drafted by the Convention was to create a government with enough power to act on a national level, but without so much power that fundamental rights would be at risk. One way that this was accomplished was to separate the power of government into three branches, and then to include checks and balances on those powers to assure that no one branch of government gained supremacy. This concern arose largely out of the experience that the delegates had with the King of England and his powerful Parliament. The powers of each branch are enumerated in the Constitution, with powers not assigned to them reserved to the States.Much of the debate, which was conducted in secret to ensure that delegates spoke their minds, focused on the form that the new legislature would take. Two plans competed to become the new government: the Virginia Plan, which apportioned representation based on the population of each State, and the New Jersey plan, which gave each State an equal vote in Congress. The Virginia Plan was supported by the larger States, and the New Jersey plan preferred by the smaller. In the end, they settled on the Great Compromise (sometimes called the Connecticut Compromise), in which the House of Representatives would represent the people as apportioned by population; the Senate would represent the States apportioned equally; and the President would be elected by the Electoral College. The plan also called for an independent judiciary.The founders also took pains to establish the relationship between the States. States are required to give “full faith and credit” to the laws, records, contracts, and judicial proceedings of the other States, although Congress may regulate the manner in which the States share records, and define the scope of this clause. States are barred from discriminating against citizens of other States in any way, and cannot enact tariffs against one another. States must also extradite those accused of crimes to other States for trial.The founders also specified a process by which the Constitution may be amended, and since its ratification, the Constitution has been amended 27 times. In order to prevent arbitrary changes, the process for making amendments is quite onerous. An amendment may be proposed by a two-thirds vote of both Houses of Congress, or, if two-thirds of the States request one, by a convention called for that purpose. The amendment must then be ratified by three-fourths of the State legislatures, or three-fourths of conventions called in each State for ratification. In modern times, amendments have traditionally specified a time frame in which this must be accomplished, usually a period of several years. Additionally, the Constitution specifies that no amendment can deny a State equal representation in the Senate without that State’s consent.With the details and language of the Constitution decided, the Convention got down to the work of actually setting the Constitution to paper. It is written in the hand of a delegate from Pennsylvania, Gouverneur Morris, whose job allowed him some reign over the actual punctuation of a few clauses in the Constitution. He is also credited with the famous preamble, quoted at the top of this page. On September 17, 1787, 39 of the 55 delegates signed the new document, with many of those who refused to sign objecting to the lack of a bill of rights. At least one delegate refused to sign because the Constitution codified and protected slavery and the slave trade.RatificationThe process set out in the Constitution for its ratification provided for much popular debate in the States. The Constitution would take effect once it had been ratified by nine of the thirteen State legislatures; unanimity was not required. During the debate over the Constitution, two factions emerged: the Federalists, who supported adoption, and the Anti-Federalists, who opposed it.James Madison, Alexander Hamilton, and John Jay set out an eloquent defense of the new Constitution in what came to be called the Federalist Papers. Published anonymously in the newspapers The Independent Journal and The New York Packet under the name Publius between October 1787 and August 1788, the 85 articles that comprise the Federalist Papers remain to this day an invaluable resource for understanding some of the framers’ intentions for the Constitution. The most famous of the articles are No. 10, which warns of the dangers of factions and advocates a large republic, and No. 51, which explains the structure of the Constitution, its checks and balances, and how it protects the rights of the people.The States proceeded to begin ratification, with some debating more intensely than others. Delaware was the first State to ratify, on December 7, 1787. After New Hampshire became the ninth State to ratify, on June 22, 1788, the Confederation Congress established March 9, 1789 as the date to begin operating under the Constitution. By this time, all the States except North Carolina and Rhode Island had ratified—the Ocean State was the last to ratify on May 29, 1790.The Bill of RightsOne of the principal points of contention between the Federalists and Anti-Federalists was the lack of an enumeration of basic civil rights in the Constitution. Many Federalists argued, as in Federalist No. 84, that the people surrendered no rights in adopting the Constitution. In several States, however, the ratification debate in some States hinged on the adoption of a bill of rights. The solution was known as the Massachusetts Compromise, in which four States ratified the Constitution but at the same time sent recommendations for amendments to the Congress.James Madison introduced 12 amendments to the First Congress in 1789. Ten of these would go on to become what we now consider to be the Bill of Rights. One was never passed, while another dealing with Congressional salaries was not ratified until 1992, when it became the 27th Amendment. Based on the Virginia Declaration of Rights, the English Bill of Rights, the writings of the Enlightenment, and the rights defined in the Magna Carta, the Bill of Rights contains rights that many today consider to be fundamental to America.The First Amendment provides that Congress make no law respecting an establishment of religion or prohibiting its free exercise. It protects freedom of speech, the press, assembly, and the right to petition the Government for a redress of grievances.The Second Amendment gives citizens the right to bear arms.The Third Amendment prohibits the government from quartering troops in private homes, a major grievance during the American Revolution.The Fourth Amendment protects citizens from unreasonable search and seizure. The government may not conduct any searches without a warrant, and such warrants must be issued by a judge and based on probable cause.The Fifth Amendment provides that citizens not be subject to criminal prosecution and punishment without due process. Citizens may not be tried on the same set of facts twice and are protected from self-incrimination (the right to remain silent). The amendment also establishes the power of eminent domain, ensuring that private property is not seized for public use without just compensation.The Sixth Amendment assures the right to a speedy trial by a jury of one’s peers, to be informed of the crimes with which one is charged, and to confront the witnesses brought forward by the government. The amendment also provides the accused the right to compel testimony from witnesses, as well as the right to legal representation.The Seventh Amendment provides that civil cases preserve the right to trial by jury.The Eighth Amendment prohibits excessive bail, excessive fines, and cruel and unusual punishments.The Ninth Amendment states that the list of rights enumerated in the Constitution is not exhaustive, and that the people retain all rights not enumerated.The Tenth Amendment assigns all powers not delegated to the United States

---
## [dyrone/git](https://github.com/dyrone/git)@[f1c903debd...](https://github.com/dyrone/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Thursday 2023-02-23 06:29:14 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[91f06a97d3...](https://github.com/Gofawful5/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Thursday 2023-02-23 07:05:19 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[d95ca04819...](https://github.com/Gofawful5/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Thursday 2023-02-23 07:05:19 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [Crandel/melpa](https://github.com/Crandel/melpa)@[4872ef038d...](https://github.com/Crandel/melpa/commit/4872ef038dbbf67008bfa7951574ee372d6ff68d)
#### Thursday 2023-02-23 08:01:56 by Jonas Bernoulli

Distribute all back-ends with the emacsql package

There are two reasons for this.

- Going forward, packages that use `emacsql' and SQLite should use
  the best back-end that can be used with the Emacs instance in use,
  either `emacsql-sqlite-builtin`, `emacsql-sqlite-module`, or as a
  last resort `emacsql-sqlite'.

  That means that if we didn't bundle the back-end libraries with
  `emacsql' itself, these packages would have to depend on all three
  back-end packages in addition to `emacsql' itself.  (Alternatively
  they could not depend on any of the back-end packages, and instead
  make the user install the appropriate back-end, when they try to
  use the package.  That's a bad user experience and there likely
  would be bugs, making it even more painful.)

- EmacSQL is now distributed on NonGNU Elpa as well.  While we at
  Melpa encourages the creation of separate packages for optional
  extensions (which are not useful to all users, or which have
  additional dependencies) the Emacs maintainers prefer everything to
  be distribute as one package, even if that means that `defvar' and
  `declare-function' declarations are necessary to keep the compiler
  happy.

  I still think our way is usually better, but since three of the
  back-end libraries have to be distributed with the main package
  anyway, we might as well give in here and bundle the other three
  as well.

For the time being, we have to continue to *also* distribute the
back-end libraries as separate packages.

Several third-party packages depend on the existing `emacsql' and
`emacsql-sqlite' packages.  These packages should be updated to only
depend on `emacsql', but the latest released versions of these
packages will continue to depend on `emacsql-sqlite' as well.  If we
removed the recipe for that, that would remove the latest release of
that package from Melpa, not just the snapshot version.

This is the current roadmap:

0. Include all back-ends in `emacsql'.
1. Update dependant packages to only depend on `emacsql'.
2. Make changes to `emacsql', which are enabled by the former two
   steps, and which are blocking the creation of a new `emacsql'
   release.  (These changes are related to the addition of the
   additional SQLite back-ends.  So this is a bit of a chicken and
   egg problem, and this commit (0) is the first step to break out
   of that.)
3. Create an `emacsql' release.
4. Wait for new releases of all dependant packages.
5. Change the separate back-end packages to warn the user, asking
   them to remove all of these packages.
6. After waiting some more, remove the separate back-end packages.

While a back-end is installed as part of `emacsql' and as a separate
package, it is undefined which version is loaded, but until step (5)
the two versions should be the same, so it doesn't matter.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Thursday 2023-02-23 08:45:35 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [Eagletanker/coolstation](https://github.com/Eagletanker/coolstation)@[e424304790...](https://github.com/Eagletanker/coolstation/commit/e424304790a06573bfefbaa832c73a61f25ed6e1)
#### Thursday 2023-02-23 09:06:38 by bobskunk

PIZZA PASTA PUT IT IN A BOX

SHIT MY ASS AND FUCK IT LIKE A FOX

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ab4328144d...](https://github.com/treckstar/yolo-octo-hipster/commit/ab4328144d73c65f5128d5796a034aea1ca65c5f)
#### Thursday 2023-02-23 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [MalleeFoul/Homebrew-Zrythm-reqs](https://github.com/MalleeFoul/Homebrew-Zrythm-reqs)@[fcd0369488...](https://github.com/MalleeFoul/Homebrew-Zrythm-reqs/commit/fcd036948899eb25dfb08c16b8b0a3183209d1e9)
#### Thursday 2023-02-23 09:35:08 by MalleeFoul

	modified:   About.md
No fucking way, holy shit, I actually made a formula for libaudec? Holy fucking bingle!

---
## [SawshaDev/quark](https://github.com/SawshaDev/quark)@[edcb909382...](https://github.com/SawshaDev/quark/commit/edcb909382f8aa9eefc676e7db150c89d6a1107b)
#### Thursday 2023-02-23 10:48:05 by SawshaDev

Fuck you enoki, im committing unstable changes now

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[c7a33d5ff9...](https://github.com/harryob/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Thursday 2023-02-23 12:54:11 by riot

PMC and Whiteout stuff (#1966)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

As a preword, I came up with every change in this PR and coded them in
the span of 10 hours, so some things may be iffy.

PMCs and Whiteout may be good, but they're a bit outdated, this
modernizes multiple loadout aspects, enables antag vendors for
admin-spawn, and does some balance changes to certain
portions(specifically chem ERT).

Individual changes, numbered, will go over each in why its good, may
have forgotten one or two things.

1. Buffs whiteout flamer with blue flame damage, belt-linked magharn,
and pyro underbarrel extinguisher
2. Adds a synthetic repair kit(medkit), with synth repair tools, gives
it to whiteout.
3. Adds breaching charges and swaps crowbars to tactical in whiteout
loadouts
4. Gives whiteout PMC sniper goggles(thermals)
5. Gives whiteout medic the required gear to actually repair a downed
member of the team, and just a lot of synth heals.
6. Gives whiteout leader a pyro extinguisher.
7. Gives whiteout weapons default attachments.
8. Adds an 'advanced' mini-flamer with the same stats as UPP integrated
UBF, gives it to NSG23 and random m41/2 attachie.
9. Gives detainer PMCs a version of the corporate m41A MK2(goon gun),
with attachies and adv flamer to replace flamethrower.
10. Swaps chem PMC TL P90(name is too long) with an M41/2
11. Gives normal PMC ERT roles a webbing vest with meds and
miniextinguisher
12. Gives PMC Surgeon the essentials required to act as a medic, swaps
NSG with M39/2, gives them a normal but unique look.
13. Whiteout and PMC SG powerpacks have 30k power by default, instead of
10k.
14. Gives PMC guns more options for random attachments, and gives m41/2
its intended collapsible stock
15. Gives PMC engi m39/2 instead of P90
16. Removes flamer from potential PMC loadouts.
17. Gives PMCs better CQC skill.
18. Gives PMC TLs autoinjector pouches(which gives chem TL a second
pouch in the first place)
19. Detainer PMCs now have tac-sechuds, PMC TLs have sensorhuds.
20. **Enables antag vendor for PMC roles.** (Look at file changes for
the specific things, too long for pr desc)

# Explain why it's good for the game

Modernization and some needed loadout/balance changes(IMO).
Per number:

1. Whiteout flamer did worse damage than napalm, and was incredibly easy
to lose.
2. More heals for each member of the whiteout team, allows more
self-sufficiency.
3. Breach charges for tacticool breaches, crowbar doubles as a melee
weapon in case the player doesn't know about synth punch
4. Whiteout didn't have proper NVG, thermals allows them to do
tacticooler breaches by lining up people wth breach charge.
5. Whiteout medic didn't have a lot of heals at all, and didn't have a
defib, so they weren't much of a medic.
6. To extinguish the flames and lead charges, works like pyro
underbarrel extinguisher, but handheld.
7. Default tacticool attachment, already made whiteout subtypes for
HEAP, why not give them good attachies with them too.
8. Mini-flamer sucks, gives a better version for NSG and m41/2, same
stats as the already existing UPP integrated UBF.
9. Detainers had flamers which sucked, gives them corpo m41s which
aren't as good as /2s, but have adv UBF for flames.
10. P90 sucks, having default m41/2 fits with other leader type, also
gives them a better gun than their underlings.
11. Medkit but in a webbing, its my personal combat webbing load when I
play so its good.
12. PMC Surgeon was horrifically undergeared, they didn't even have a
medhud, gives them basic gear similar to PMC med but with a beret to
tell them apart.
13. ERTs don't have spare batteries to get usually, more staying power
in fights.
14. More options for attachies to further make PMC weapons better, also
gives m41/2 the m41 collapsible stock because it needed it.
15. P90 sucks, support roles getting the m39/2 is cool.
16. Flamer sucks to get as PMC, and adv. UBF as a potential m41/2
attachie makes a full-sized flamer useless too.
17. PMCs could fireman carry, and multi-strip, but did it horrifically
slow, gives them MP level CQC(master for spec, expert for TL)
18. TL getting extra meds is neat, also chem TL had an empty pocket slot
and no meds, thats bad.
19. Sechud-thing for PMC detainers is useful(stops flashbang trolling
for one), giving PMC TL a sensorhud to watch their team's status is also
good.
20. Makes doing event bases for PMCs much easier, too long to post the
specific changes here but look at files for them.


# Testing Photographs and Procedure

I forgot to take screenshots but it all works. 👍 
I spawned myself as every changed role and tested every individual
change extensively.

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

:cl:
add: PMCs are now able to use antag vendors.
balance: Multiple loadout and skill changes to PMCs and Whiteout
balance: Buffs whiteout flame damage to blue flame damage.
fix: PMC Investigator Lead now appropriately spawns with a medical pouch
in their pocket, instead of nothing.
fix: Maximum skill preset now appropriately also has BE and intel skill,
at maximum of course.
fix: PMC Smartgunner now appropriately a VP78 to go along with their
VP78 magazines
fix: Whiteout now appropriately have night vision.
fix: M41A/2 now appropriately comes equipped with a collapsible stock.
spellcheck: PMC smartgun drum now has a seperate description and name
from base SG to match its different appearance.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [DuckHunt-discord/DHV4](https://github.com/DuckHunt-discord/DHV4)@[99ccc167b1...](https://github.com/DuckHunt-discord/DHV4/commit/99ccc167b14b85ccd5b5453122410ae5e592400b)
#### Thursday 2023-02-23 14:17:10 by Arthur

Let saysounds be videos to fix discord stupid mobile apps that can play stupid audio files smh. Imaging wasting time on making @silent messages but not having a proper AUDIO PLAYER in a CHAT APP for YEARS AND YEARS.

Thanks ffmpeg for the funny bulk convert. I wouldn't have done it without you and some very ugly python scripting.

In [9]: for file in pathlib.Path("./").glob("*.mp3"):
   ...:     pre = file.stem
   ...:     os.system(f"""ffmpeg -loop 1 -i image.png -i "{pre}.mp3" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -shortest -movflags +faststart "{pre}
   ...: .mp4" && rm "{pre}.mp3" """)

---
## [fleetdm/fleet](https://github.com/fleetdm/fleet)@[6091556b7a...](https://github.com/fleetdm/fleet/commit/6091556b7a6f69f92b7bbb590b5a3068c3a4558d)
#### Thursday 2023-02-23 14:18:55 by Mike McNeil

Fix build (#10018)

mikermcneil
  3 minutes ago
@Kathy Satterlee
 I think https://github.com/fleetdm/fleet/pull/9881 broke the build
4 replies

 .
mikermcneil
  2 minutes ago
https://github.com/fleetdm/fleet/pull/9979#issuecomment-1440604277


Zay Hanlon
  1 minute ago
Oops. That was my approval/merge on Kathy's change


Zay Hanlon
  1 minute ago
How do I fix?


mikermcneil
  < 1 minute ago
@Zay Hanlon
All good. I think we should make it so that PRs can't be merged until
they pass the CI checks. It's annoying but would prevent things like
this, which are expensive and involve multiple folks' time.
@Zach Wasserman
 
@Luke Heath
I'm going to turn on the branch protection that prevents merging when
automated CI checks are failing.
@Kathy Satterlee
 I'll follow up with a fix now.
@Jarod Reyes
 Feel free to go ahead and merge your PR in the meantime.


Zay Hanlon
:spiral_calendar_pad: [11 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091760162369?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Sorry :disappointed:


mikermcneil
[10 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091789685699?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
All good, inevitable


Zach Wasserman
[9 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091841779269?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
FWIW turning that on will really slow down my dev process at times.


Zach Wasserman
[8 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091942206439?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
eg. if I make one tiny change on a PR that I already know passes all the
tests then I'll have to wait 15 mins for the whole CI to run before I
can merge.


mikermcneil
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091967828479?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
it was an indentation issue:
https://github.com/fleetdm/fleet/pull/10018/files#diff-68623aac08ce48b5c1275a38ea9f42a8a730a9c2e04ab1946174cdc67f4ce686R8
:ty:
1



Luke Heath
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092006055779?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Is it possible to conditionally enable the required CI checks?


Zach Wasserman
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092018873739?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Maybe you can just turn on a limited set of checks that we know go
really fast and have a high true-positive rate?


Luke Heath
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092062859149?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
That's a good idea. FWIW we'll be removing e2e test runs in CI later
this week, which will reduce the CI run time by ~25 minutes.


mikermcneil
[< 1 minute
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092432337109?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
This is not the first time this has happened and I'd like to put an end
to the emergency remediation that takes a chunk of the day's focus away
from multiple people each time it occurs. If it causes a drain on our
ability to move quickly, let's def change it back. If it's worth the
friction (like the PR approval restriction), then we can keep it.
I'm running into the problem of being able to select the "test-website"
job from [this
list](https://github.com/fleetdm/fleet/settings/branch_protection_rules/18283834),
likely because it is already conditional:
image.png

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a487eaeb9c...](https://github.com/treckstar/yolo-octo-hipster/commit/a487eaeb9cd5205719873dd1845775f2890df417)
#### Thursday 2023-02-23 14:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [valnar012/Spooder](https://github.com/valnar012/Spooder)@[8120f971b9...](https://github.com/valnar012/Spooder/commit/8120f971b9184608e6000724c300ccbbfba34526)
#### Thursday 2023-02-23 14:26:11 by GreySole

0.3.8 Update

This beast of an update makes a lot of deep changes that I really think should be made to make Spooder more organized and user friendly. Some dependencies have changed as well as folder structures. It’ll probably work if you copy/paste the repo over what you have, but you might as well backup your settings and plugins and restore them in a clean installation.

Regardless, use `npm install` to get the new dependencies!

Init
- Gets network interfaces and recommends 192.168.x.x

OBS
- Added callOBS() global function to make obs websocket calls outside of the module (events)
Web UI
- Prints actual network info to access instead of stored info

- Ngrok integration: Put in your API key in the config tab to have your tunnels and eventsubs all set when starting up. If you want to run Spooder without using this, call `npm run safe`. Recommended for developing where Spooder will get restarted a lot.

- Refresh eventsubs: Deletes all eventsubs and resubscribes with the current callback url. Ngrok will do this automatically. You can do this manually in the EventSub tab.

- Added OBS data to Events tab for OBS commands

- Backup/Restore fix: When importing backups, check/create backup directory

- Config: Like Events, the object structure is built into the UI and will auto fix/upgrade your files.
Customize your Spooder in the Config tab :3

Mod UI

- Mod UI themes are now part of the themes.json file so any themes made will be immortalized.
- New authentication method makes it easier to log in securely. Instead of making an auth token with Twitch, mods now enter their Twitch username and their own password (doesn’t have to be the account’s password, but it can). Finally, mods call ‘!mod verify’ in the Spooder user’s chat to ensure it’s them. Passwords are encrypted and stored in mod.json.
Plugins
- Plugins have been made more “solid”. Information from its package.json is now used for the Web UI. So you get a proper, capitalized name with version numbers and author name.

- Wait for the sample plugin to update, because there’s a lot of good changes in the osc bundle.
- Connect messages now carry info about the overlay/utility. Such as:
-- which version of Spooder it was made for (I want to make auto-updates for the osc-bundle sometime)
-- The plugin’s internal name (can access the plugin’s proper name by accessing activePlugins[pluginname]._name)
-- Any error messages from plugins will also be transmitted so you can see in the Web UI’s OSC Monitor. Gives you a chance to catch it on the fly rather than while testing. Error logs are also stored separately so they won’t shift out of the OSC messages.
Spooder
- Added theme file for saved Mod UI Themes, Custom Spooder, and Web UI Themes (For a later update)
- Added spamguard to mod commands. Call ‘!mod spamguard’ to automatically timeout users spamming commands. Timeouts are specific to Spooder, so there aren’t any role exceptions…unless you would want that. Let me know.
- Chat module switched to tmi.js. I feel it’s better maintained and stable. There are some ways twitch-js formed message objects that are easier to develop with (like emotes), so it builds the tmi object to be more like twitch-js.
- Added OBS commands: setinputmute, switchscenes, and sceneitemenabled. More to come.
- Global functions: You can use these functions in plugins
-- restartChat(message:string): Restarts the chat. You can add a message to say after finishing restart.
-- chatisFirstMessage(message:obj): Returns true or false whether the message is the user’s first message to your channel
-- chatIsReturningChatter(message:obs): Returns true or false whether the message is from a returning chatter.
-- chatIsMod(message:obj): Returns true or false whether the user who sent this message is a moderator.
-- chatIsSubscriber(message:obj): Returns true or false whether the user who sent this message is a subscriber.
-- chatIsBroadcaster(message:obj): Returns true or false whether the user who sent this message is the broadcaster
-- getChatters(type:string): Returns an array of usernames for a specific type. Available types are: mod, vip, all
-- blacklistUser(viewername:string, duration:number (millis): Locks a user from using chat commands for the duration.
-- lockEvent(moduser:string, modCommand:string, target:string): Locks an event from use in chat. moduser is to tell which mod called the command. modCommand is either “lock” or “unlock” and it adapts to booleans and integers. Target is which event to lock.
- Async response commands: To allow API calls within responses like with getChatters()
- OBS event handlers: Control OBS with chat commands, channel point redeems, or OSC
- Mod event handlers: Call mod commands through events. Though chat commands are already built in and there’s not many use cases for redeems. This is still handy to hook an OSC message to a mod command.
- Event timeouts use setTimeout and command durations are now parsed as float: This way you have more precision for timed UDP commands.

There’s probably more features and fixes I don’t know off the top of my head, but this is quite a list as it is lol. I hope this all works well for you, if not, please create an issue here or ask for help on the Discord Server. Happy weaving! /╲/\( º^ ω ^º )/\╱\

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[a2295b2b04...](https://github.com/ss220-space/tgstation/commit/a2295b2b049ba3c77186ffb0eaacb507c001cdc8)
#### Thursday 2023-02-23 14:26:32 by LemonInTheDark

Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode. 
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible. 
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[97f567fdc7...](https://github.com/ss220-space/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Thursday 2023-02-23 14:44:10 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[27c35bfa0b...](https://github.com/ss220-space/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Thursday 2023-02-23 14:44:10 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [uweigand/wasmtime](https://github.com/uweigand/wasmtime)@[1efee4abdf...](https://github.com/uweigand/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Thursday 2023-02-23 15:20:21 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [FR0Z3/PD2-Real-Weapon-Names](https://github.com/FR0Z3/PD2-Real-Weapon-Names)@[e652745307...](https://github.com/FR0Z3/PD2-Real-Weapon-Names/commit/e65274530788ae2bf3836cc1137ff25b561a463e)
#### Thursday 2023-02-23 15:28:20 by PoorPockets McNewHold

French localization update.

THE TRANSLATION STILL GOT THINGS TO BE TRANSLATED/ LA TRADUCTION A ENCORE DES CHOSES À TRADUIRE

Here's a more updated version of the French translation, Due to myself now only playing on the VR version, and due to the BLT support being extremely glitchy according to me in VR, I don't use that mod anymore. 
Here are some points I want to address:
-I've fixed my typo with "Cannon" which is written with one N instead.
-As stated, I don't use that mod anymore, so I've might make some typo's that make the localization crash the game, before pushing it, I'll suggest to test it before. (If you remember, This already happened with my work on this mod)
-Decided to translate "Model" by the actual word in French which is "Modèle" beside the word is often used as the actual NAME of the weapon/attachment. If you aren't alright with this decision, feel free to delete those modified ones, If I'm not mistaking, I've only made that modification to those strings.
-I've tried to arrange the order of the strings in the same of the actual English localization, might be useless, but isn't for the next translators.
-I'm still not sure if "Boite de culasse" is the right translation for the receiver, Doesn't have any weapons at home, or any other users at the shooting range talking about any "receivers", "reçeuveur"(The word I've first thought it was supposed to be translated) or "boite de culasse". Didn't find much documentation on the internet to actually proof being the right translation, so feel free to not accept it.
-I've made some research for only a few weapons/attachments, so I might call a handguard as a grip and vice-versa, If someone wants to continue to translate this, I really suggest him/her/pancake make research than me.
-By moving some words orders (Because in french, we don't say "a FLYING banana" but "une banane VOLANTE", We need to arrange some words orders when translating from English), I've decided to move Carbine/carabine (Why do you not use the "correct" name ? I mean, it's a french name...Pff, stupid Americans) in the first position to for example, as a "MLGX23 Carbine Barrel" to precise what type of barrel it is, Translating in French as "Canon de Carabine MLGX23", which literally translate to "Carbine barrel type MLGX23", If needed, Simply move "Carabine" as where your "Carbine" was previously in the original English string, also, maybe remove the uppercase letter if needed for it, determine it was a "noun"/"type of weapon" instead of a random word.

---
## [AlphaKeks/gokz.rs](https://github.com/AlphaKeks/gokz.rs)@[e8260f6cb7...](https://github.com/AlphaKeks/gokz.rs/commit/e8260f6cb765d0277be107572d5f1da7b8db400e)
#### Thursday 2023-02-23 15:30:28 by AlphaKeks

0.13.0

- added `Tier` enum
- changed a lot of unsigned ints to signed ones because apparrently the
  API likes to return stupid values
- changed `map_name` on `Map` to an Option because fuck you that's why

---
## [apollographql/router](https://github.com/apollographql/router)@[cfb421a564...](https://github.com/apollographql/router/commit/cfb421a5646de4ae5d5634415c86336d70c6fb90)
#### Thursday 2023-02-23 15:41:16 by Bryn Cooke

Fixes #2123 (#2162)

Issue was introduced with #2116 but no release had this in.

Move operations would insert data in the config due to the delete magic
value always getting added. Now we check before adding such values.

We may need to move to fluvio-jolt longer term.

<!--
First, 🌠 thank you 🌠 for considering a contribution to Apollo!

Some of this information is also included in the /CONTRIBUTING.md file
at the
root of this repository.  We suggest you read it!

  https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md

Here are some important details to keep in mind:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* 📖 Contribution guidelines
Follow https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
associated issues! Documentation in the docs/ directory should be
updated
        as necessary.  Finally, a /CHANGELOG.md entry should be added.

We hope you will find this to be a positive experience! Contribution can
be
intimidating and we hope to alleviate that pain as much as possible.
Without
following these guidelines, you may be missing context that can help you
succeed
with your contribution, which is why we encourage discussion first.
Ultimately,
there is no guarantee that we will be able to merge your pull-request,
but by
following these guidelines we can try to avoid disappointment.

-->

Co-authored-by: bryn <bryn@apollographql.com>

---
## [KhidagrimR/UpThemBeats](https://github.com/KhidagrimR/UpThemBeats)@[36ebd24223...](https://github.com/KhidagrimR/UpThemBeats/commit/36ebd2422305f9a9d3167dd9f5fec33472c50833)
#### Thursday 2023-02-23 15:45:42 by Zorskel

Fixed the goddamn post fucking sonuvabitch process

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[2415006fbe...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/2415006fbe18d48ceae171c2421f2b73b28f4c1c)
#### Thursday 2023-02-23 17:04:28 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccNixDrivenBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [kittywhiskers/dash](https://github.com/kittywhiskers/dash)@[aec7441ac2...](https://github.com/kittywhiskers/dash/commit/aec7441ac2863b4d92c5032e98e8b2691262a912)
#### Thursday 2023-02-23 17:23:23 by Wladimir J. van der Laan

Merge #15277: contrib: Enable building in Guix containers

751549b52a9a4cd27389d807ae67f02bbb39cd7f contrib: guix: Additional clarifications re: substitutes (Carl Dong)
cd3e947f50db7cfe05c05b368c25742193729a62 contrib: guix: Various improvements. (Carl Dong)
8dff3e48a9e03299468ed3b342642f01f70da9db contrib: guix: Clarify SOURCE_DATE_EPOCH. (Carl Dong)
3e80ec3ea9691c7c89173de922a113e643fe976b contrib: Add deterministic Guix builds. (Carl Dong)

Pull request description:

  ~~**This post is kept updated as this project progresses. Use this [latest update link](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718) to see what's new.**~~

  Please read the `README.md`.

  -----

  ### Guix Introduction

  This PR enables building bitcoin in Guix containers. [Guix](https://www.gnu.org/software/guix/manual/en/html_node/Features.html) is a transactional package manager much like Nix, but unlike Nix, it has more of a focus on [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) and [reproducibility](https://www.gnu.org/software/guix/blog/tags/reproducible-builds/) which are attractive for security-sensitive projects like bitcoin.

  ### Guix Build Walkthrough

  Please read the `README.md`.

  [Old instructions no. 4](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718)

  [Old instructions no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-493827011)

  [Old instructions no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old instructions no. 1</summary>
  In this PR, we define a Guix [manifest](https://www.gnu.org/software/guix/manual/en/html_node/Invoking-guix-package.html#profile_002dmanifest) in `contrib/guix/manifest.scm`, which declares what packages we want in our environment.

  We can then invoke
  ```
  guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```
  To have Guix:
  1. Build an environment containing the packages we defined in our `contrib/guix/manifest.scm` manifest from the Guix bootstrap binaries (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) for more details).
  2. Start a container with that environment that has no network access, and no access to the host's filesystem except to the `pwd` that it was started in.
  3. Drop you into a shell in that container.

  > Note: if you don't want to wait hours for Guix to build the entire world from scratch, you can eliminate the `--no-substitutes` option to have Guix download from available binary sources. Note that this convenience doesn't necessarily compromise your security, as you can check that a package was built correctly after the fact using `guix build --check <packagename>`

  Therefore, we can perform a build of bitcoin much like in Gitian by invoking the following:

  ```
  make -C depends -j"$(nproc)" download && \
      cat contrib/guix/build.sh | guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```

  We don't include `make -C depends -j"$(nproc)" download` inside `contrib/guix/build.sh` because `contrib/guix/build.sh` is run inside the container, which has no network access (which is a good thing).
  </details>

  ### Rationale

  I believe that this represents a substantial improvement for the "supply chain security" of bitcoin because:

  1. We no longer have to rely on Ubuntu for our build environment for our releases ([oh the horror](https://github.com/bitcoin/bitcoin/blob/72bd4ab867e3be0d8410403d9641c08288d343e3/contrib/gitian-descriptors/gitian-linux.yml#L10)), because Guix builds everything about the container, we can perform this on almost any Linux distro/system.
  2. It is now much easier to determine what trusted binaries are in our supply chain, and even make a nice visualization! (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html)).
  3. There is active effort among Guix folks to minimize the number of trusted binaries even further. OriansJ's [stage0](https://github.com/oriansj/stage0), and janneke's [Mes](https://www.gnu.org/software/mes/) all aim to achieve [reduced binary boostrap](http://joyofsource.com/reduced-binary-seed-bootstrap.html) for Guix. In fact, I believe if OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler).

  ### Steps to Completion

  - [x] Successfully build bitcoin inside the Guix environment
  - [x] Make `check-symbols` pass
  - [x] Do the above but without nasty hacks
  - [x] Solve some of the more innocuous hacks
  - [ ] Make it cross-compile (HELP WANTED HERE)
    - [x] Linux
      - [x] x86_64-linux-gnu
      - [x] i686-linux-gnu
      - [x] aarch64-linux-gnu
      - [x] arm-linux-gnueabihf
      - [x] riscv64-linux-gnu
    - [ ] OS X
      - [ ] x86_64-apple-darwin14
    - [ ] Windows
      - [ ] x86_64-w64-mingw32
  - [ ] Maybe make importer for depends syntax
  - [ ] Document build process for future releases
  - [ ] Extra: Pin the revision of Guix that we build with with Guix [inferiors](https://www.gnu.org/software/guix/manual/en/html_node/Inferiors.html)

  ### Help Wanted

  [Old content no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-483318210)

  [Old content no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old content no. 1</summary>
  As of now, the command described above to perform a build of bitcoin a lot like Gitian works, but fails at the `check-symbols` stage. This is because a few dynamic libraries are linked in that shouldn't be.

  Here's what `ldd src/bitcoind` looks like when built in a Guix container:
  ```
  	linux-vdso.so.1 (0x00007ffcc2d90000)
  	libdl.so.2 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libdl.so.2 (0x00007fb7eda09000)
  	librt.so.1 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/librt.so.1 (0x00007fb7ed9ff000)
  	libstdc++.so.6 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libstdc++.so.6 (0x00007fb7ed87c000)
  	libpthread.so.0 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libpthread.so.0 (0x00007fb7ed85b000)
  	libm.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libm.so.6 (0x00007fb7ed6da000)
  	libgcc_s.so.1 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libgcc_s.so.1 (0x00007fb7ed6bf000)
  	libc.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libc.so.6 (0x00007fb7ed506000)
  	/gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fb7ee3a0000)
  ```

  And here's what it looks in one of our releases:
  ```
  	linux-vdso.so.1 (0x00007ffff52cd000)
  	libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f87726b4000)
  	librt.so.1 => /usr/lib/librt.so.1 (0x00007f87726aa000)
  	libm.so.6 => /usr/lib/libm.so.6 (0x00007f8772525000)
  	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f877250b000)
  	libc.so.6 => /usr/lib/libc.so.6 (0x00007f8772347000)
  	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8773392000)
  ```

  ~~I suspect it is because my script does not apply the gitian-input patches [described in the release process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#fetch-and-create-inputs-first-time-or-when-dependency-versions-change) but there is no description as to how these patches are applied.~~ It might also be something else entirely.

  Edit: It is something else. It appears that the gitian inputs are only used by [`gitian-win-signer.yml`](https://github.com/bitcoin/bitcoin/blob/d6e700e40f861ddd6743f4d13f0d6f6bc19093c2/contrib/gitian-descriptors/gitian-win-signer.yml#L14)
  </details>

  ### How to Help

  1. Install Guix on your distro either [from source](https://www.gnu.org/software/guix/manual/en/html_node/Requirements.html) or perform a [binary installation](https://www.gnu.org/software/guix/manual/en/html_node/Binary-Installation.html#Binary-Installation)
  2. Try out my branch and the command described above!

ACKs for top commit:
  MarcoFalke:
    Thanks for the replies. ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f
  laanwj:
    ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f

Tree-SHA512: 50e6ab58c6bda9a67125b6271daf7eff0ca57d0efa8941ed3cd951e5bf78b31552fc5e537b1e1bcf2d3cc918c63adf19d685aa117a0f851024dc67e697890a8d

---
## [Kazakazara/tgstation](https://github.com/Kazakazara/tgstation)@[66b7310039...](https://github.com/Kazakazara/tgstation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Thursday 2023-02-23 18:06:47 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[aaa4821373...](https://github.com/mrakgr/The-Spiral-Language/commit/aaa4821373c261f5d428e2cb0582db141af23aaf)
#### Thursday 2023-02-23 18:19:03 by Marko Grdinić

"9:15am. I woke up early and lounged in bed, but I slept soundly tonight. I am much more rested that I was yesterday.

9:20am. https://boards.4channel.org/a/thread/249303252/one-punch-man-chapter-180-translated-is-here

Let me read this and then I will resume the React course. Any emails?

9:35am. A bit on the issue I opened in Feliz. OPM.

9:50am. Let me start.

https://youtu.be/bMknfKXIFA8?t=7265

I was here last time.

Let me start up the project.

https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing

I am going to have to get used to googling CSS properties. Yesterday I tried playing with HTML tags. If I put something like `qwe` which can't possibly be built in as the attribute name, that actually isn't an error. It just get interpreted as an inline element. That explains what those 'special' Youtube tags were.

Ok, I refreshed my memory of the React project.

Since I was doing the HTML course in React from the start I have a good basis to continue from.

https://youtu.be/bMknfKXIFA8?t=7237

Oh, is the goal to make something like this.

Actually, let me chill just a bit more. I feel distracted.

10:25am. Let me start for real here.

Let me implement this thing on the screen. I could do it better than the guy himself.

11:15am. Now I am getting bogged down in some flexbox issue.

11:25am. I figured it out. It turns out that just setting the max width on an image without also setting the min width can be a bad idea! By default min-width is auto which causes issue when I narrow the viewport. I found it really weird how the text on the right side would overflow the title. I get it now.

https://developer.mozilla.org/en-US/docs/Web/CSS/flex

Hmmm, what is this?

12pm. https://stackoverflow.com/questions/8543859/css-vertical-alignment-text-inside-li

I get autistically stuck on some issue sometimes, and this is one of those cases.

https://youtu.be/bMknfKXIFA8?t=7237

You know what? Fuck this. Let me just watch the course. I can't get a satisfactory solution. The flexbox one causes the discs to disappear.

Let me just place the logo.

12:15pm. Gah, I can't figure out how to change the color. Or how to set the Z indexes succinctly...

11:20am. I figured it out, but the solution is not good enough. Let me just watch the video.

https://youtu.be/bMknfKXIFA8?t=8147
> At least at this time, when I was researching, I could not find a good way to realign these.

Yeah. I spent a lot of time on this today as well.

https://youtu.be/bMknfKXIFA8?t=8256

Ah, I see. It didn't occur to me at all to add it as a background image.

```
.main {
    position: relative;
    display: flex;
    flex-direction: column;
    background-color: hsl(0, 0%, 25%);
    padding: 1em 2em;
    min-height: 30em;

    background-image: url("./assets/react-logo.svg");
    background-repeat: no-repeat;
    background-position: calc(100% + 15em) center;
    background-size: 30em;
    background-blend-mode: luminosity;
}
```

Oh, I figured out how to add this stupid thing!

Like so.

1pm. https://youtu.be/bMknfKXIFA8?t=8656

Let me pause here. It is time for breakfast.

I just got word from the Valora guy. He sent me some links. Maybe with his recommendation, I'll actually get an interview opportunity.

1:45pm. Done with breakfast and chores. Let me just read the two chapter of Destiny Unchain and then I will apply to Valora.

Let's take it easy.

2:40pm. Let me resume. It is time to apply to Valora.

https://en.valora.career/job/zurich/software-engineer-fullstack/29368/45005687568

It is this thing here.

2:55pm. I applied. I also checked and programmer salaries in Swis are quite strong, about 7x of what they are in Croatia.

Anyway, that is that. I should at least not get my resume thrown straight into the trash in this place.

Now, instead of resuming the React course here, let me follow up on that Feliz issue. First let me try out the template.

https://github.com/dotnet/fsharp/issues/

Opened issue 14792.

3:10pm. Now let me resume the React course.

https://youtu.be/bMknfKXIFA8?t=9065
> If you are already feeling very confident in styling in React, I will give you permission to skip the next few screencasts.

I guess I'll be skimming the following sections.

3:45pm. Resolved that apostorphe error. It will be fixed in the upcoming version of Ionide, and it has already been fixed VS 17.5. I upgraded and tested it myself and see that it works.

https://youtu.be/bMknfKXIFA8?t=11643

Oh so that is how the props work on the JS side.

4pm. https://youtu.be/bMknfKXIFA8?t=12724

I am just skimming this stuff as it is super obvious. This is pretty much how Blazor components work. With CSS and HTML components on the other hand I needed to do some memorization and playing around in order to get used to how they work.

I should be able to finish the tutorial a lot sooner than I thought. Let me just continue skipping it.

4:15pm. https://youtu.be/bMknfKXIFA8?t=17108

I'll want to focus on this for a bit.

https://youtu.be/bMknfKXIFA8?t=17658

Oh, you can do the grid template like this.

https://youtu.be/bMknfKXIFA8?t=17677

I am not familiar with this CSS.

https://youtu.be/bMknfKXIFA8?t=17773

Oh this CSS property would have been good for the search bar. Instead I've been padding it.

4:30pm. https://www.terluinwebdesign.nl/en/css/flexible-padding-for-buttons/

Let me pause a bit, I need to learn about flexible marking and padding.

https://developer.mozilla.org/en-US/docs/Web/CSS/::before

Ah, I see. I could use this for the list item attributes.

4:40pm. Oh, right. I need to thank the guy for refering me.

4:55pm. I see now that I got his surname wrong and forgot to note his department despite him suggesting it to do so.

I am such a fool. My clumsiness will be the end of me.

Instead of being flexible about it, I just decided to do it. Assuming this causes the Valora application to fail, this is the reason why I'll be failing interviews in the future.

Forget it, let me just resume the course.

https://youtu.be/bMknfKXIFA8?t=18742

Hmmmm....

This key thing. I do not think that in the Feliz library I have that. Should I be setting that? I'll look into it in the future, nevermind it for now...

https://youtu.be/bMknfKXIFA8?t=19129

Let me pause here and I will look at the attribute. It is not goot to put things off.

https://reactjs.org/docs/lists-and-keys.html

Ok, this is easy. It does about what you'd expect.

I do not need to worry about this.

5:35pm. https://youtu.be/bMknfKXIFA8?t=19958

In the end it will turn out that CSS was harder than React.

https://youtu.be/bMknfKXIFA8?t=20994

Any reason why this is so?

https://youtu.be/bMknfKXIFA8?t=21180
> If you were to run two state setter functions back to back. The way react handles it, maybe or may not run one of them before the other. I see.

Ok, I get it. It seems that just grabbing the regular value might cause sync issues due to batching.

5:40pm. https://developer.mozilla.org/en-US/docs/Web/CSS/:root

<html> is the root element it turns out.

I could set it like this.

https://youtu.be/bMknfKXIFA8?t=21683

These things are super simple, I do not feel like doing them even though I've felt like doing the HTML/CSS lessons.

5:50pm. Let me just keep going forward. I am past the halfway mark. I'll aim to finish the course soon, so I can start work on my own things. In addition to that, I want to further study backend development and the way ASP.NET firmware works. Not to mention, refresh my memory of HTTP requests, and set up a REST API. Everyone seems to be asking for that so I should put it on my resume somewhere.

5:55pm. Took a short break. Focus me. Let me just go at it for 10m more. This time of the day is really just about time for me to finish.

6:10pm. https://youtu.be/bMknfKXIFA8?t=25450

I skipping ahead really strongly. I am 7h in already. But this stuff is really piece of cake programming.

Right now, I've realized I've forgotten how to do nested Elmish components...wait, I think I see it, nevermind. I'll figure it out right away when the time comes to practice. Let me go forward even more.

...Lunch time.

6:40pm. Done with lunch. Let me just watch a bit more of the course and then I will be done.

6:45pm. https://youtu.be/bMknfKXIFA8?t=25778
> You probably don't need derived state.

https://youtu.be/bMknfKXIFA8?t=26050

I am guessing he'll use partial application.

https://youtu.be/bMknfKXIFA8?t=26188

Sigh, I was in the right direction, but his solution is more complicated than what I had in mind.

https://youtu.be/bMknfKXIFA8?t=26361

Imperative programmer trying do functional one. He should have just used a map.

https://youtu.be/bMknfKXIFA8?t=26471

Rather than using a reactive variable that has an array, it might have been better to instead have an array of reactive variables.

https://youtu.be/bMknfKXIFA8?t=26660

Now he is doing it properly.

7:05pm. https://youtu.be/bMknfKXIFA8?t=27616

I am too tired to go on anymore. 7:40h out of 11:55h into it. I've been going through it at fast forward today, that is why I managed to cover 5.5 hours in one sitting. Tomorrow, I will completely clear how React works on move on to the next thing.

To think, it is this simple.

What I have to do next is really set my sights on mastering backend frameworks like ASP.NET. After I understand those, I will have zero trouble handling any kind of pro work in the future.

7:10pm. Tomorrow. I just have to pay my dues tomorrow and I am done scrambling for how to do web frontend work.

I am going to make it happen. I'll get the skills and I will get the money. If not Valora, it will be something else. I need to be determined to do whatever is needed. I have the choice of a niche, in which case I will pick .NET. I do not need many of them. I just need one that is well paid, and I will be set.

I won't give up. I'll continue to push forward.

But for now let me chill. I've been putting off Machimaho, and it is time for some fun. Let's hope I can sleep well tonight."

---
## [benkallman/artmetareal](https://github.com/benkallman/artmetareal)@[4d64d9ff9e...](https://github.com/benkallman/artmetareal/commit/4d64d9ff9ec919d636e8cf9554b13c0fce806838)
#### Thursday 2023-02-23 18:20:27 by a person

Update About.svelte

rewrite this code and content to sound more profesional and have a more impactful display,      <h2>Class located in Madison Wisconsin, with classes also offered online. Taught by Benjamin Kallman.</h2>
  <p class="title">Drawing and Painting. <br>Brush, pen, or digital. Guided classes either structured by students interest or standard class to find the students interest.</p>
  <p>Instructor: Benjamin Kallman<br>
Ben is an artist based in the midwest with a Bachelor’s degree in Fine Arts from The School of
the Art Institute of Chicago. He has been painting for 25 years.</p>
Introducing an exceptional opportunity to take Drawing and Painting classes taught by the talented Benjamin Kallman. Our classes are conveniently located in Madison, Wisconsin and also offered online for those who prefer a more flexible learning experience.

Our classes cater to a diverse range of interests, whether you prefer to work with brush, pen, or digital tools. We offer guided classes that are either structured by the student's interests or a standard class to help students discover their artistic passions.

Benjamin Kallman is an accomplished artist with a Bachelor's degree in Fine Arts from The School of the Art Institute of Chicago. He has been practicing painting for over 25 years and is excited to share his wealth of experience and knowledge with his students.

Join us today and unleash your artistic potential with the guidance of Benjamin Kallman.




Regenerate response

---
## [Johannes2262/cmss13](https://github.com/Johannes2262/cmss13)@[5f78464e25...](https://github.com/Johannes2262/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Thursday 2023-02-23 18:32:46 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
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

:cl:
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [hertera1/argilla](https://github.com/hertera1/argilla)@[4c5f51377e...](https://github.com/hertera1/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Thursday 2023-02-23 18:47:27 by Tom Aarsen

Use `rich` for logging, tracebacks, printing, progressbars (#2350)

Closes #1843

Hello!

## Pull Request overview
* Use [`rich`](https://github.com/Textualize/rich) for logging,
tracebacks, printing and progressbars.
* Add `rich` as a dependency.
* Remove `loguru` as a dependency and remove all mentions of it in the
codebase.
* Simplify logging configuration according to the logging documentation.
* Update logging tests.

## Before & After
[`rich`](https://github.com/Textualize/rich) is a large Python library
for very colorful formatting in the terminal. Most importantly (in my
opinion), it improves the readability of logs and tracebacks. Let's go
over some before-and-afters:
<details><summary>Printing, Logging & Progressbars</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219089678-e57906d3-568d-480e-88a4-9240397f5229.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219089826-646d57a6-7e5b-426f-9ab1-d6d6317ec885.png)

Note that for the logs, the repeated information on the left side is
removed. Beyond that, the file location from which the log originates is
moved to the right side. Beyond that, the progressbar has been updated,
ahd the URL in the printed output has been highlighted automatically.

</details>

<details><summary>Tracebacks</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219090868-42cfe128-fd98-47ec-9d38-6f6f52a21373.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219090903-86f1fe11-d509-440d-8a6a-2833c344707b.png)

---

### Before:

![image](https://user-images.githubusercontent.com/37621491/219091343-96bae874-a673-4281-80c5-caebb67e348e.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219091193-d4cb1f64-11a7-4783-a9b2-0aec1abb8eb7.png)

---

### Before

![image](https://user-images.githubusercontent.com/37621491/219091791-aa8969a1-e0c1-4708-a23d-38d22c2406f2.png)

### After

![image](https://user-images.githubusercontent.com/37621491/219091878-e24c1f6b-83fa-4fed-9705-ede522faee82.png)

</details>

## Notes
Note that there are some changes in the logging configuration. Most of
all, it has been simplified according to the note from
[here](https://docs.python.org/3/library/logging.html#logging.Logger.propagate).
In my changes, I only attach our handler to the root logger and let
propagation take care of the rest.

Beyond that, I've set `rich` to 13.0.1 as newer versions experience a
StopIteration error like discussed
[here](https://github.com/Textualize/rich/issues/2800#issuecomment-1428764064).

I've replaced `tqdm` with `rich` Progressbar when logging. However, I've
kept the `tqdm` progressbar for the [Weak
Labeling](https://github.com/argilla-io/argilla/blob/develop/src/argilla/labeling/text_classification/weak_labels.py)
for now.

One difference between the old situation and now is that all of the logs
are displayed during `pytest` under "live log call" (so, including
expected errors), while earlier only warnings were shown.

## What to review?
Please do the following when reviewing:
1. Ensuring that `rich` is correctly set to be installed whenever
someone installs `argilla`. I always set my dependencies explicitly in
setup.py like
[here](https://github.com/nltk/nltk/blob/develop/setup.py#L115) or
[here](https://github.com/huggingface/setfit/blob/78851287535305ef32f789c7a87004628172b5b6/setup.py#L47-L48),
but the one for `argilla` is
[empty](https://github.com/argilla-io/argilla/blob/develop/setup.py),
and `pyproject.toml` is used instead. I'd like for someone to look this
over.
2. Fetch this branch and run some arbitrary code. Load some data, log
some data, crash some programs, and get an idea of the changes.
Especially changes to loggers and tracebacks can be a bit personal, so
I'd like to get people on board with this. Otherwise we can scrap it or
find a compromise. After all, this is also a design PR.
3. Please have a look at my discussion points below.

## Discussion
`rich` is quite configurable, so there's some changes that we can make
still.
1. The `RichHandler` logging handler can be modified to e.g. include
rich tracebacks in their logs as discussed
[here](https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions).
Are we interested in this?
2. The `rich` traceback handler can be set up to include local variables
in its traceback:
<details><summary>Click to see a rich traceback with local
variables</summary>


![image](https://user-images.githubusercontent.com/37621491/219096029-796b57ee-2f1b-485f-af35-c3effd44200b.png)
    </details>
Are we interested in this? I think this is a bit overkill in my opinion.
3. We can suppress frames from certain Python modules to exclude them
from the rich tracebacks. Are we interested in this?
4. The default rich traceback shows a maximum of 100 frames, which is a
*lot*. Are we interested in reducing this to only show the first and
last X?
5. The progress bar doesn't automatically stretch to fill the full
available width, while `tqdm` does. If we want, we can set `expand=True`
and it'll also expand to the entire width. Are we interested in this?
6. The progress "bar" does not need to be a bar, we can also use e.g. a
spinner animation. See some more info
[here](https://rich.readthedocs.io/en/latest/progress.html#columns). Are
we interested in this?

---

**Type of change**

- [x] Refactor (change restructuring the codebase without changing
functionality)

**How Has This Been Tested**

I've updated the tests according to my changes.

**Checklist**

- [x] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [x] follows the style guidelines of this project
- [x] I did a self-review of my code
- [x] I added comments to my code
- [ ] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works

- Tom Aarsen

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[6ebdfdc73f...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/6ebdfdc73f233d94bcc6c4a2f72d902af868583f)
#### Thursday 2023-02-23 18:49:49 by SkyratBot

[MIRROR] Makes Shake() proc work [MDB IGNORE] (#19424)

* Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

* Makes Shake() proc work

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [wisdark/UACME](https://github.com/wisdark/UACME)@[c65f9215c1...](https://github.com/wisdark/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Thursday 2023-02-23 20:42:48 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[296ca23aa1...](https://github.com/Floofies/tgstation/commit/296ca23aa1d8531fba291eb9b802b7282fee657b)
#### Thursday 2023-02-23 20:50:02 by Jacquerel

Most actions cannot be used while incapacitated (#73513)

## About The Pull Request

Fixes #39775
The `TRAIT_INCAPACITATED` trait is intended to block you from acting but
does not inherently block actions. Actions only check for "conscious",
"has available hands", "immobile", or "lying down".
Most actions still _can't_ be used while incapacitated. This is because
most actions are spells, most spells have invocations, and you can't
talk while you are incapacitated. This is silly.

I have resolved this by adding a new flag which blocks actions while
incapacitated. This is somewhat redundant with "conscious" because most
sources of that also make you incapacitated but not _always_, you might
want the specificity.

I have tried to be discerning about where this flag is applied, it is
not in all cases (for instance you can still swallow implanted pills
while incapacitated and such), but it's not only possible but I can't
really avoid implementing this without it being a balance change in
_some_ cases,

Actions this effects are things such as:
Xenomorph Tail Sweep, Lesser Magic Missile (cult constucts), Heretic
Shadow Cloak, the Smoke spell in general, Conjuring (but not firing)
Infinite Guns, Mime spells

Times when these actions will no longer be available but were previously
are such times as when the mob is:
Stamina Crit, Stunned, Paralysis, and Time Stopped.

## Why It's Good For The Game

The incapacitated trait is applied by effects which should block acting
but still permits several actions which logically would be prevented.
This fortunately hasn't come up too often due to the high ratio of
actions with invocations, but it feels bad to stun someone and then have
them still able to perform an action they logically wouldn't be able to
take while stunned.
This is especially egregious in the case of Time Stop (the only way to
stun a lot of the mobs effected by this) but that's a rare pick on a
rare antagonist and would also rarely be used on these mobs, so a bit of
an edge case.

## Changelog

:cl:
fix: Many spell-like abilities which could be stunned, paralysed, or
frozen in time now cannot be.
/:cl:

---
## [rajahfox/aliaison](https://github.com/rajahfox/aliaison)@[66d2f280df...](https://github.com/rajahfox/aliaison/commit/66d2f280dfa059222a4ad8ce46bde3422aeee2c3)
#### Thursday 2023-02-23 21:09:07 by rajahfox

deign

Each text of any substantial length, regardless of genre, invariably contains a genomic sequence. From the Holy Bible to the Egyptian Book of the Dead, to the corpus of text messages we send back and forth every day, to the very words we utter over the course of a lifetime, we, each of us, speaks life.

This trifle, deign, itemizes the abbreviations for the four nucleotides of deoxyribonucleic acid (DNA). Those four chemicals, Thymine, Guanine, Adenine and Cytosine, are abbreviated by the letters, T, G, A and C. It may also be augmented to produce a messenger RNA (mRNA) sequence by replacing the T for Thymine with U for Uracil.

deign extracts the four letters from a body of text, effectually transubstantiating the word from word to flesh.

The sequence of nucleotides, once extracted from a text, can be entered into a genome database such as the National Library of Medicine's Basic Local Alignment Search Tool (BLAST), the DNA Database of Japan (DDBJ), or the European Bioinformatics Institute (EBI), to name a few.

These databases compare the genetic sequence queries entered against a litany of genetic sequences gleaned from flora and fauna found on our planet. deign makes it possible to compare and examine the DNA or RNA sequences a text shares with a living organism. And, properly altered, one may also view the building-block aminos contained within a text by grouping the DNA or RNA codons by threes and converting them to their corresponding proteins with a dictionary-key mechanism. I will upload this dynamo soon.

So what? What is the point of this, you may ask? Well, I don't have a straightforward answer for that yet. In essence, I simply don't know enough about the scientific and medical worlds to know if this application is worth it's weight and wait (I've been sitting on this idea for damn near nine years.

I do have one anecdotal example in which I transubstantiated the Papyrus of Ani and found edible organisms of such significant but cohesive variety that I was able to create a nice recipe, a ceviche, to be exact.

Lofty though my intentions may be, I believe we can learn more than what is offered at face value in our shared cultural affinity for text. This union of Science, Technology, Engineering and logical Mathematics (STEM) with the Liberal and Language Arts, I believe, bears potential. How much is up to you, me and anyone who deigns to get down to the basics.

This tableau reliance restores a nation's laughter—edifies, teeming, a lingual legend.

---
## [VinsCool/furnace](https://github.com/VinsCool/furnace)@[717f7802a0...](https://github.com/VinsCool/furnace/commit/717f7802a060b15abb47f06bccbab1d8951f9f33)
#### Thursday 2023-02-23 21:54:13 by VinsCool

pokey: there was yet another attempt.
- the delta freq thing is painful, ABSOLUTE pitch will be necessary, I'm afraid :v
- fixed a bunch of 16-bit related bugs, the order is reverted to hardware for channels that will output sound, sorry tiledarrow, it just works that way.
- pretty much everything seems to work and is close enough to RMT, except not really, tuning is commiting suicide with the poor delta being unable to do its thing as I was hoping for it.
- I'm probably wasting my time with this but whatever, if that can somehow work, I'm cool with that...

---
## [VinsCool/furnace](https://github.com/VinsCool/furnace)@[f6eae14069...](https://github.com/VinsCool/furnace/commit/f6eae140690557cabeab3fe4e117e3c020e99d7c)
#### Thursday 2023-02-23 21:54:13 by VinsCool

pokey: oh god please no this is just cursed
- this is slightly better, I guess, honestly this is terrible unless I can get the absolute pitch reference!

---
## [cortex-command-community/Cortex-Command-Community-Project-Source](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source)@[b390e7c13f...](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source/commit/b390e7c13ff0d662f35c1732096ee7a9086a210d)
#### Thursday 2023-02-23 22:05:34 by MaximDude

Static linking hell AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Link to a bunch of bullshit libs to resolve missing symbols and rebuild Luabind and RakNet without iterator debugging crap and remove iterator debugging crap macro in RTE to compile this piece of shit with SDL static linked in debug on x86 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[1fe9efd00a...](https://github.com/Jolly-66/dragon-station/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Thursday 2023-02-23 22:18:58 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[ae08395328...](https://github.com/SmoSmoSmoSmok/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Thursday 2023-02-23 23:50:24 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---

