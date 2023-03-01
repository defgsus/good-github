## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-28](docs/good-messages/2023/2023-02-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,279,179 were push events containing 3,501,804 commit messages that amount to 284,856,463 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [Mister-moon1/cmss13](https://github.com/Mister-moon1/cmss13)@[b53c9f0531...](https://github.com/Mister-moon1/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Tuesday 2023-02-28 00:48:51 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

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

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

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
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [refnode/linuxkit-linuxkit](https://github.com/refnode/linuxkit-linuxkit)@[860934d5d9...](https://github.com/refnode/linuxkit-linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Tuesday 2023-02-28 00:55:22 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[fc1e2e5e26...](https://github.com/insertnamehere123/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Tuesday 2023-02-28 00:57:46 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [SonGorLick/pcsx2](https://github.com/SonGorLick/pcsx2)@[87abacc632...](https://github.com/SonGorLick/pcsx2/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Tuesday 2023-02-28 01:25:16 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [xamarin/java.interop](https://github.com/xamarin/java.interop)@[77800dda83...](https://github.com/xamarin/java.interop/commit/77800dda83c2db4d90b501c00069abc9880caaeb)
#### Tuesday 2023-02-28 02:18:05 by Jonathan Pryor

[Java.Interop.Tools.Expressions] Add Java.Interop.Tools.Expressions (#1046)

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
assemblies to disk, which is a feature that never made it to .NET Core,
and is still lacking as of .NET 7 (xamarin/java.interop#616)?

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

When running in-tree, e.g. AzDO pipeline execution, when
`--jvm PATH` isn't specified, `jnimarshalmethod-gen`
will attempt to read the path in `bin/Build*/JdkInfo.props`
a'la `TestJVM` (002dea4a).  This allows an in-place update in
`core-tests.yaml` which does:

	dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp -o bin/TestDebug-net7.0

~~ Using `jnimarshalmethod-gen` output ~~

What does `jnimarshalmethod-gen` *do*?

	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll.orig > beg.il
	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll      > end.il
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

	# do this *before* running above `dotnet jnimarshalmethod-gen.dll` command…
	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 103 ms - Java.Interop.Export-Tests.dll (net7.0)

Then after running the above `dotnet jnimarshalmethod-gen.dll` command,
re-run the tests:

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
	# which currently fails :-(

Re-enable most of `Java.Interop.Export-Tests.dll` for .NET 7;
see 41ba3485, which disabled those tests.

To verify the generated IL, use the [dotnet-ilverify][0] tool:

	dotnet tool install --global dotnet-ilverify

Usage of which is "weird":

	$HOME/.dotnet/tools/ilverify bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[52bded7096...](https://github.com/treckstar/yolo-octo-hipster/commit/52bded70961712c01503dcffa91b097b647c8cbf)
#### Tuesday 2023-02-28 02:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [hustcer/nushell](https://github.com/hustcer/nushell)@[378a3ae05f...](https://github.com/hustcer/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Tuesday 2023-02-28 02:43:12 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[81c1229373...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Tuesday 2023-02-28 02:47:51 by Captain277

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
## [ca1e/UACME](https://github.com/ca1e/UACME)@[c65f9215c1...](https://github.com/ca1e/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Tuesday 2023-02-28 03:12:22 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [Gfry1234/alx-system_engineering-devops](https://github.com/Gfry1234/alx-system_engineering-devops)@[459fa7f5fe...](https://github.com/Gfry1234/alx-system_engineering-devops/commit/459fa7f5fe25299ee46346885b7b4278507bde92)
#### Tuesday 2023-02-28 03:53:25 by Gfry1234

This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

Your script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used
You can find a [log file here].

Example:

$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[e5652d962c...](https://github.com/clintjedwards/gofer/commit/e5652d962c238d710a334bd2a978a30eb3057145)
#### Tuesday 2023-02-28 04:20:00 by Clint J Edwards

refactor: Refactor the config package

Previously the configuration for the app was home grown
it used many different config libraries to create a hierarchy
of configuration.

This worked well, but there was a lot of hacks to make up for little
places where the many libraries did not fit perfectly(namely,
the hcl parser code was kinda shit and we had struct tags for
every library)

To fix this and make the configuration code much simplier I swapped
the config package to use https://github.com/knadh/koanf which
greatly simplifies a lot of hoemgrown code. HCL time.Duration parsing
works right out of the box where previously there was a lot of code
to make it work.

The tradeoff is that envs now need to be separated by double underscores
in order to be understood properly. Which can be a confusing interaction
but the maintainabiliy boost is probably worth writing a bit of
extra documentation.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[f0b7813d48...](https://github.com/Paxilmaniac/Skyrat-tg/commit/f0b7813d489b64d627e1b1d3009d1e6a05768043)
#### Tuesday 2023-02-28 04:22:05 by SkyratBot

[MIRROR] Don't create abandoned airlocks with walls underneath them. [MDB IGNORE] (#19568)

* Don't create abandoned airlocks with walls underneath them. (#73656)

## About The Pull Request
Fixes #71504

#70237 attempted to remove this and did in some cases, however the case
where the abandoned airlock is able to find an adjacent wall turf to
copy the type of still fails to delete the airlock.
This fixes that.

Also in my testing, the times where it _failed_ to find a nearby wall
turf to copy and spawned a default wall would leave the mapping helper
visible in the round. Oops!

## Why It's Good For The Game

Mapping helpers should always delete themselves when finished.
The airlocks with walls under them are funny once and annoying the rest
of the time. As of that older PR, this continuing to happen is regarded
as a bug.
Also apparently it might be required anyway for Wallening.

## Changelog

:cl:
fix: Maintenance tunnels should no longer sometimes contain airlocks
with walls underneath them.
/:cl:

* Don't create abandoned airlocks with walls underneath them.

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [xenomacabre/VilesMods](https://github.com/xenomacabre/VilesMods)@[9068914ce1...](https://github.com/xenomacabre/VilesMods/commit/9068914ce1430b5025f6a5ac59b33d4a534e9900)
#### Tuesday 2023-02-28 04:37:41 by VileHeathen

The Fish and Fuel Update

The Fish and Fuel Update

This is a two-part update which overhauls fishing, and adds “stuffed” firewood to the game. It also overhauls fueled lighting.

Note: These changes affect several of my mods, so it's best to update them all. And the changes may not be everyone's cup of tea, so I saved the previous version on a separate Github branch. This is in alpha, so the previous branch is more stable (yet still in testing).

Part I: The Fish:
Overhauls fish. Fishing still works the same way, but there is a wider variety of fish with better textures
There are also big-game fish, which are rare and yield a lot of meat. A couple even yield exotic leather.
Many fish are biome and climate-specific

Hypnosquid		Medium
Saberfish		Big Game
Redfin Tuna		Large
Snackerel		Tiny
Cuda			Small
Ice Flounder	Medium
Eeel			Small
Alligar		Large
Breadmouth 	Medium
Killer Catfish	Big Game
Death Sturgeon	Big Game
Sterling Perch	Tiny
Pinstripe Bass	Small

Part II: The Fuel (and lighting)
Firewood is now stuffed, meaning its burn time is related to the species of wood. Hardwoods tend to burn longer, so softwoods are often best used as kindling. Oak is king.

NEW BUILDINGS
Seasoning Rack - Can take many days to process, so plan accordingly.
Chopping Block - Sort of an upgrade of the log-splitting spot. All firewood chopping is moved here from the woodcutting bench.

NEW FUELS:
Rushlights - A cheap fast-burning light sources using grass and tallow/pitch/oil
Candles - Burns longer than rushlights
Pitch – extracted from pine and spruce
Fish Oil – from fish of course
Plant Wax (WIP) – extracted from certain seeds
Turpentine – made from pitch
Tallow – ok not new, but has more uses
Riven Boards – previously 'firewood', these are crude split planks for building and fuel

NEW LIGHTING:
Tree Torch – single use torch that destroys itself when it burns out
Rushlight Holder - also has a slot for a candle.
Fire Basket
Lamppost (oil-burning)
Lantern Sconce (oil-burning)
Candle Sconce
Candelabra (replaces original candle)
Standing torch – similar to the vanilla one
Cresset – Like the Olympics torch. Replaces bowl lamp.

Part III: Other fixes and changes
HARDCORE RENOVATIONS:
Fixed bar counters so they don't instantly build
NEW: Added two new doors: Ornate Door, which is attractive and durable, and the Barn door, which uses the rustic texture, and the rustic door gets a new texture.
Lowered drystone wall HP
Increase Flax Carpet cleanliness and lowered cost
HELL-BENT FOR LEATHER TANNING:
Fixed hides not rotting
Adjusted exotic leather color
MATERIALS SCIENCE:
Fixed missing ammonia recipe
Fixed broken Aermet recipe
Ores now have colors in the scanner
METALLURGY:
Fixed missing Russian translation
NEW: Added a new scenario start: The Guildmasters (Medieval)
Fixed broken coke kiln recipe
VILE'sTEAKS:
This isn't much of a mod, just some personal adjustments I've added for myself. Entirely optional.
Adds new pawn badges and retextures some of the old ones. WIP
Experimental changes to Realistic Darkness to make the moderate mode slightly darker. WIP
Pawns are more likely to spawn gay, bisexual and asexual to be more realistic to life.

---
## [shaojiewang/pytorch](https://github.com/shaojiewang/pytorch)@[d09cd15216...](https://github.com/shaojiewang/pytorch/commit/d09cd152161626381cae7780bbd2c44eedeb33d7)
#### Tuesday 2023-02-28 05:56:24 by Taylor Robie

[Profiler] Defer recording startup python events (take 2) (#91684)

This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks @dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/91684
Approved by: https://github.com/chaekit

---
## [xsm2/jak-project](https://github.com/xsm2/jak-project)@[c249dbc437...](https://github.com/xsm2/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Tuesday 2023-02-28 07:14:14 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[97f52bd40d...](https://github.com/odoo-dev/odoo/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Tuesday 2023-02-28 07:14:28 by Arnold Moyaux

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

Part-of: odoo/odoo#109640

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[d21740b475...](https://github.com/MemedHams/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Tuesday 2023-02-28 08:28:02 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [iewiewiew/spring-boot](https://github.com/iewiewiew/spring-boot)@[732d891287...](https://github.com/iewiewiew/spring-boot/commit/732d89128701a46d252c336fb168da59d5127808)
#### Tuesday 2023-02-28 08:44:47 by wmh

[TOC]

# 参考资料
[Markdown官方教程](https://markdown.com.cn/)

# 1、Markdown 标题语法
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

# 2、Markdown 段落语法
I really like using Markdown.

I think I'll use it to format all of my documents from now on.

# 3、Markdown 换行语法
This is the first line.
And this is the second line.

# 4、Markdown 强调语法
## 粗体（Bold）
I just love **bold text**.
I just love __bold text__.
Love**is**bold

## 斜体（Italic）
Italicized text is the *cat's meow*.
Italicized text is the _cat's meow_.
A*cat*meow

## 粗体（Bold）和斜体（Italic）
This text is ***really important***.
This text is ___really important___.
This text is __*really important*__.
This text is **_really important_**.
This is really***very***important text.

# 5、Markdown 引用语法
要创建块引用，请在段落前添加一个 > 符号
> Dorothy followed her through many of the beautiful rooms in her castle.

多个段落的块引用
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

嵌套块引用
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

带有其它元素的块引用
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

# 6、Markdown 列表语法
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

# 7、Markdown 代码语法
At the command prompt, type `nano`.
``Use `code` in your Markdown file.``

# 8、Markdown 分隔线语法
***

---

_________________

# 9、Markdown 链接语法
这是一个链接 [Markdown语法](https://markdown.com.cn)。
这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。
<https://markdown.com.cn>
<fake@example.com>
I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](#code).

# 10、Markdown 图片语法
![这是图片](/assets/img/philly-magic-garden.jpg "Magic Gardens")
[![沙漠中的岩石图片](/assets/img/shiprock.jpg "Shiprock")](https://markdown.com.cn)

# 11、Markdown 转义字符语法
\* Without the backslash, this would be a bullet in an unordered list.
http://images.google.com/images?num=30&amp;q=larry+bird
&copy;

# 12、Markdown 内嵌 HTML 标签
This **word** is bold. This <em>word</em> is italic.

This is a regular paragraph.

<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>

This is another regular paragraph.

# 13、Markdown 表格
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

对齐
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

# 14、Markdown 围栏代码块
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

# 15、Markdown 脚注
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.

Indent paragraphs to include them in the footnote.

`{ my code }`

Add as many paragraphs as you like.

# 16、Markdown 标题编号
### My Great Heading {#custom-id}
[Heading IDs](#heading-ids)

# 17、Markdown 定义列表
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.

# 18、Markdown 删除线
~~世界是平坦的。~~ 我们现在知道世界是圆的。

# 19、Markdown 任务列表语法
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

# 20、Markdown 使用 Emoji 表情
去露营了！ :tent: 很快回来。

真好笑！ :joy:

# 21、Markdown 自动网址链接
自动将URL转换为链接
http://www.example.com

禁用自动URL链接
`http://www.example.com`

---
## [ychin/vim](https://github.com/ychin/vim)@[ff5b3e389f...](https://github.com/ychin/vim/commit/ff5b3e389f44e65b980547c01d958eedad8c38c3)
#### Tuesday 2023-02-28 09:06:24 by Yee Cheng Chin

Support Python 3 stable ABI to allow mixed version interoperatbility

Vim currently supports embedding Python for use with plugins, and the
"dynamic" linking option allows the user to specify a locally installed
version of Python by setting `pythonthreedll`. However, one caveat is
that the Python 3 libs are not binary compatible across minor versions,
and mixing versions can potentially be dangerous (e.g. let's say Vim was
linked against the Python 3.10 SDK, but the user sets `pythonthreedll`
to a 3.11 lib). Usually, nothing bad happens, but in theory this could
lead to crashes, memory corruption, and other unpredictable behaviors.
It's also difficult for the user to tell something is wrong because Vim
has no way of reporting what Python 3 version Vim was linked with.

For Vim installed via a package manager, this usually isn't an issue
because all the dependencies would already be figured out. For prebuilt
Vim binaries like MacVim (my motivation for working on this), AppImage,
and Win32 installer this could potentially be an issue as usually a
single binary is distributed. This is more tricky when a new Python
version is released, as there's a chicken-and-egg issue with deciding
what Python version to build against and hard to keep in sync when a new
Python version just drops and we have a mix of users of different Python
versions, and a user just blindly upgrading to a new Python could lead to
bad interactions with Vim.

Python 3 does have a solution for this problem: stable ABI / limited API
(see https://docs.python.org/3/c-api/stable.html). The C SDK limits the
API to a set of functions that are promised to be stable across
versions. This pull request adds an ifdef config that allows us to turn
it on when building Vim. Vim binaries built with this option should be
safe to freely link with any Python 3 libraies without having the
constraint of having to use the same minor version.

Note: Python 2 has no such concept and this doesn't change how Python 2
integration works (not that there is going to be a new version of Python
2 that would cause compatibility issues in the future anyway).

---

Technical details:
======

The stable ABI can be accessed when we compile with the Python 3 limited
API (by defining `Py_LIMITED_API`). The Python 3 code (in `if_python3.c`
and `if_py_both.h`) would now handle this and switch to limited API
mode. Without it set, Vim will still use the full API as before so this
is an opt-in change.

The main difference is that `PyType_Object` is now an opaque struct that
we can't directly create "static types" out of, and we have to create
type objects as "heap types" instead. This is because the struct is not
stable and changes from version to version (e.g. 3.8 added a
`tp_vectorcall` field to it). I had to change all the types to be
allocated on the heap instead with just a pointer to them.

Other functions are also simply missing in limited API, or they are
introduced too late (e.g. `PyUnicode_AsUTF8AndSize` in 3.10) to it that
we need some other ways to do the same thing, so I had to abstract a few
things into macros, and sometimes re-implement functions like
`PyObject_NEW`.

One caveat is that in limited API, `OutputType` (used for replacing
`sys.stdout`) no longer inherits from `PyStdPrinter_Type` which I don't
think has any real issue other than minor differences in how they
convert to a string and missing a couple functions like `mode()` and
`fileno()`.

Also fixed an existing bug where `tp_basicsize` was set incorrectly for
`BufferObject`, `TabListObject, `WinListObject`.

Technically, there could be a small performance drop, there is a little
more indirection with accessing type objects, and some APIs like
`PyUnicode_AsUTF8AndSize` are missing, but in practice I didn't see any
difference, and any well-written Python plugin should try to avoid
excessing callbacks to the `vim` module in Python anyway.

I only tested limited API mode down to Python 3.7, which seemes to
compile and work fine. I haven't tried earlier Python versions.

WIP:
======

I marked this as WIP because there are a few things that I want to
finish up, but wanted to gather some feedbacks on this PR first.

- Add way to set `Py_LIMITED_API`. Probably a configure.ac option.
- Add `has()` / `:version` indicator that a Python build has been built
  with stable ABI. I'm not sure if `:version` really need to be changed,
  but I'm imagining `+python3/dyn-stable`.
- Add documentation to explain this, and also how to use `has()` to
  query.
- Add CI coverage to exercise this.
- Test out popular Vim plugins written in Python (see below, I would
  welcome some suggestions) to make sure they still work.
- *Maybe*: Add a `v:python3_version`? This can help the user tell what
  version of Python Vim was built against. Useful esp for non-stable-ABI
  mode.
- *Maybe*: In the old non-stable-ABI mode, throw a warning when loading a
  Python 3 DLL that's a different version from the one Vim expects? I
  may punt on this.

---

I only tested on macOS, down to Python 3.7, with both static and dynamic
linking. If other people want to try this on Windows and Linux that
wouldl be appreciated. I ran a couple Python plugins and they seemed to
work fine (e.g. Ultisnips), but I personally don't use any plugins that
use Python so I may not be running into much edge cases.

Note: If you want to test this, just pull the PR and build. You can comment out the `#define
Py_LIMITED_API 0x03080000` line on the top of if_python3.c to get back
the full API behavior. It should pass all tests and run Python plugins
just like before. One way to know you are running in limited mode is to
run `:py3 print(sys.stdout)` which looks a little different.

---
## [Bastixxinc/Sharkjack-Scripts](https://github.com/Bastixxinc/Sharkjack-Scripts)@[124f9ff111...](https://github.com/Bastixxinc/Sharkjack-Scripts/commit/124f9ff111124453886b99951914fa1fa5107444)
#### Tuesday 2023-02-28 10:37:47 by Bastixxinc

Create Router-Ravager 25

Das Script beinhaltet 25 Angriffe, die auf einem lokalen Netzwerk durchgeführt werden können. Diese Angriffe reichen von Port-Scanning über Denial-of-Service-Angriffe bis hin zu Social-Engineering-Angriffen und Router-Exploits. Die Angriffe sind in separate Blöcke unterteilt. Wenn alle Angriffe ausgeführt wurden und mindestens ein Angriff erfolgreich war, wird versucht die Firewall zu deaktivieren.

Farbcodes:

    LED BLAU: Aktuell wird ein Angriff ausgeführt..
    LED GRÜN: Zeigt an, dass der Angriff erfolgreich war.
    LED ROT: Zeigt an, dass der Angriff nicht erfolgreich war.
    LED PINK: Es wird versucht die Firewall zu deaktivieren.
    LED DAUERHAFT GRÜN: Firewall wurde deaktiviert und der Angriff beendet.
    LED ROT-GRÜN BLINKEND: Die Firewall konnte nicht deaktiviert werden.
    LED ROT BLINKEND: Es ist ein Fehler aufgetreten.

Schritt-für-Schritt-Anleitung:

    Laden Sie das Script auf einen Sharkjack.
    Schließen Sie den Sharkjack an einen Router im lokalen Netzwerk an.
    Warten Sie, bis der Sharkjack das Script automatisch ausführt.
    Beobachten Sie die LEDs am Sharkjack, um zu sehen, ob die Angriffe erfolgreich waren oder nicht.
    Wenn die LED grün leuchtet, war der Angriff erfolgreich. Wenn die LED rot leuchtet, war der Angriff nicht erfolgreich.

Ich freue mich über Bewertungen und information auf mögliche Fehler.

DISCLAMER:

Dieses Script enthält eine Reihe von Angriffen, die illegal und moralisch verwerflich sind. Die Verwendung dieses Scripts ohne Zustimmung des Netzwerkbesitzers ist illegal und kann schwerwiegende Konsequenzen haben. Jegliche Verwendung dieses Scripts erfolgt auf eigene Gefahr.

Bitte beachten Sie, dass einige der Angriffe in diesem Script nicht mehr funktionieren könnten oder dass es möglicherweise erforderlich ist, sie an die jeweiligen Umgebungen anzupassen. Es wird empfohlen, dieses Script nicht ohne eine gründliche Kenntnis der Funktionsweise der einzelnen Angriffe zu verwenden.

ICH ÜBERNEHME KEINE HAFTUNG FÜR DIE ILLEGALE ANWENDUNG DIESES SCRIPTS

---
## [ReloadedOS/frameworks_base](https://github.com/ReloadedOS/frameworks_base)@[442921f3af...](https://github.com/ReloadedOS/frameworks_base/commit/442921f3af3aaa104429577f0f6d2452ace2de4e)
#### Tuesday 2023-02-28 11:15:14 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[1cedb92bd9...](https://github.com/KingDragoness/ProjectHypatios/commit/1cedb92bd9eef4a35bc70456316d0a79e3624175)
#### Tuesday 2023-02-28 12:30:35 by KingDragoness

Hypatios 1.4.4 b7 (Wired Server)
DONE (Feb 28)
• Reorganized folder and added LeanTween asset
• Introduced new character: Tetraroid
o Character that appear in WIRED servers
o Char portrait
• New game mechanic: WIRED Server
o A special level when entered cannot go out, once completed, the player will die and go back to the 1st level.
o Mainly for trivia and progression.
• Heaven server: places where simulated reconstructed deceased people are.
o This server features simulated people that thought they’re in the heaven.
o Boss trigger
o Boss: Ophanim
 Circular angels with eyes
o Rewards lifetaker weapon
o Trivia heaven when completed.
o Shows a 5-character passcode in the air to indicate the weapon vault.
o Briefcase with killer pill shows up after defeating Ophanim.
• Perk bug
• Ophanim Boss
o Floating in air, random patrol position
o Weak point in the eyes
o Laser focus shooting stance
o Particle effect when locking
o Death animation
 Corpse ophanim (destroy self)
• No clip camera copy properties
• “setperk” command to set perks
o Temporary perk, resets when died.
• Modular script: ModularLaserWeapon.cs
o Raycast based laser
o Requires line renderer
o Also, an optional spark object
• Changes to the health system
o If the player took damage while healing, the healing process will be undone.
o This design changes make sure to prevent “potion spamming” and forces player to drink potion at strategic times.
• FOV command to set FOV
• “weapon ammo” command to add ammo to player’s ammo
• Help for “FOV” and “weapon ammo”
• Introduced new character: Emperor
o For the endgame/ending
• Lifetaker [Exotic]: Hold and aim at enemy target. Deals 20 damage per shot while gaining 4 HP for the player. Exotic gun.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[414135da52...](https://github.com/TaleStation/TaleStation/commit/414135da52ca6962366569d2fd62280b8d34aa7a)
#### Tuesday 2023-02-28 12:33:34 by TaleStationBot

[MIRROR] [MDB IGNORE] Brings the monkey back down (body horror edition/addition.) (#4701)

Original PR: https://github.com/tgstation/tgstation/pull/73325
-----

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[170fa49b92...](https://github.com/git-for-windows/git/commit/170fa49b924a23f4398a20199b4b11bad408a2b1)
#### Tuesday 2023-02-28 12:48:56 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [seydar/ideal_grid](https://github.com/seydar/ideal_grid)@[de11621303...](https://github.com/seydar/ideal_grid/commit/de11621303f26f16dfc331d8a497e14f7fce1677)
#### Tuesday 2023-02-28 13:13:59 by Ari Brown

fucking finally figured out the stupid bug. point reduction works. bug was because i was passing in duplicate points, so values were getting wonky

---
## [marcellerusu/coil-lang](https://github.com/marcellerusu/coil-lang)@[678f16c935...](https://github.com/marcellerusu/coil-lang/commit/678f16c93572b5a75d60c549ab486a6a80c11fae)
#### Tuesday 2023-02-28 14:20:23 by MarcelRusu

unbounded ranges

we don't have exclusive unbounded  ranges because it overlaps with the spread operator.

This is because the spread operator syntax is very loose to allow it for all the uses javascript allows for.

We could clean this up as there aren't too many cases, I believe its just for function arguments its not being implemented properly.

Maybe even just for function call parsing, since it currently is a simple ~Until[:close_p parse_expr :args].

So yea we could clean that up.. or we could take a note from rust and use .. for exclusive, and ..= for inclusive.

Honestly its very tempting to go for the rust syntax approach because I think .. vs ... is very confusing. I have to remember a saying my old coworker would say is "the last dot pushed out the last element". This is coming from the ruby tradition.

I think this may be a case where we want to borrow from somewhere else.

Its kind of funny how much this language resembles rust given how different the goals are.

On the note of syntax changes.

The object literal syntax is inconsistent with map syntax.

I'm a bit torn on this because with the record syntax doesn't have something similar to {a} which means {a: a}.

Its tough to make an argument for extending the record syntax for this case because while {a: 10} is clear that "a:" means that a is a keyword. Meaning its shorthand for {:a => 10}, {a} is not clear.

But one thing that should be changed for object literal syntax is {[key_expr]: value} instead of {key_expr => value}.

I like that currently object literals are very familiar to current js people, but the arrow syntax is more general & is consistent with the Record syntax.

Things to think about. I'm not 100% sure what the right path is.

I'm feeling strange about this language, each time I make significant progress in it I can't help this overwhelming feeling that its still not enough.

Maybe that feeling keeps me going to work on it, but its frustrating that I can't just accept some satisfaction for what I've done so far.

It also makes it fairly hard to demo this language because while I think there's value here, people don't seem to want to make the leap unless I prove that it is as is ready to replace _your language/framework_. Its not, it may never be, but why is that necessary for it to be a worthwhile & noteworthy project?

Anyways, though this commit is a half broken commit with a compiler that has horrible error messages, I'm quite proud of what I've made.

---
## [marcellerusu/coil-lang](https://github.com/marcellerusu/coil-lang)@[ed4e50e0e9...](https://github.com/marcellerusu/coil-lang/commit/ed4e50e0e95e70d82e44d4b35e2895cbea61b5f9)
#### Tuesday 2023-02-28 14:20:23 by MarcelRusu

start to implement OrderedCollection for Range

its not clear the best approach here. I think going fully lazy for take & is nice idea but currently there isn't a unified theme for lazy collections.

I think its something that contains an "Underscore", but I'm still not sold on that.

I like underscore a lot, but it needs a better name.

Or maybe not, its a confusing name, but any other name I can come up with is even more confusing.

At least its easy to look up & has little meaning, so if it gets used in ways different than say a "Transform" would be, idk.

Its not clear, but "Transform" is far too general of a name.

To describe it as clear as I can, it is a data structure which stores functions & arguments. These functions & arguments get applied when you invoke the "Underscore". This makes it feel like a function definition in a way.

Like a (pure, statement-less) function is a series of functions & arguments stored together, and when you call the function it reduces the series of function, argument pairings.

_ is implemented in coil functions which are composed of js functions which are composed of other js functions & c++ native operations which are composed of assembly instructions.

This is one of those things, even though I understand how its implemented, it still confuses me at a fundamental level.

There's always some mystery, I wish more developers would admit that.

I constantly question my design choices, and honestly its only gotten more confusing the more I learn.

I think that's a sign I'm growing.

Less sure about any specific set of design goals.

There are things that I find good that stick around for a while maybe many years but honestly its all up for debate. All of it.

I think of languages like go & elm which reject language-level abstraction. And in real world seem to be one of the better systems for building real, complex ideas.

On the other hand, scala, haskell, rust, even c++ seem to tend to extremely overly complex systems.

I can think of a few reasons why this might to be true

1 - solving program design at the language level is fundamentally impossible.

2 - expressive languages allow for personal freedom which is often let people get carried away.

3 - these languages have overly invasive type systems which encourage pre-maturely over-architected solutions due to the need to fullfil all type errors. I heard a good story from eric normand I believe it was who said described the fundamental difference between a clojure developer & a haskell developer is that clojure developers will give you an opt-out "unsafe" api for unfinished features, where haskell will just give you an incomplete yet type safe API. The example he was talking about was a CURL wrapper lib, and the haskell library didn't have the types for a certain option so it wasn't implemented. This is of course not a fundamental limitation of the language, they have notions of maps & other loosely typed collections. The problem is that it is unidiomatic to provide unsafe/loosely typed arguments.

The other issue with expressive type systems is they tend to be really hard to please, and when you do please them the type errors are cryptic and there is no such thing as a "type-level" breakpoint/debugger.

Where as a counter example, say I'm using a highly dynamic & expressive API in javascript. I can see what line it broke, get a stack trace & have the option to add a "debugger" statement. On top of that, the amount of information available at runtime lets API developers generate quite good error messages (I remember react being surprisingly pleasant). Now this is not always the case, but I think the option to display & manipulate the error messages for you API is much better than having a cryptic type error.

These are all just speaking of the current limitations.

These problems could get solved, but still makes me wonder.

For now I still think coil is worthwhile & it really _feels_ like a language, which makes me feel quite good.

There's a lot to do before its ready for use though and that really bothers me, but I'm not at all excited to work on compiler error messages right now so I won't give it much thought at all. I'll continue doing as I've been doing & just work on what ever is the most interesting at the given moment.

There is no need to _finish_ anything, because that is impossible, there is no target audience for this project, there is no requirements for what determines this to be fruitful other than if it is fun for me to work on. And it is

---
## [KermityOwen/Trash-Muncher-Webapp](https://github.com/KermityOwen/Trash-Muncher-Webapp)@[c65363093c...](https://github.com/KermityOwen/Trash-Muncher-Webapp/commit/c65363093cb2a2a2e2e32d16088016ac2f8dcb7e)
#### Tuesday 2023-02-28 14:23:18 by Owen Lee

scheduler monlkey-paytch

fucking bullshit threading shit tahat took wayyy too long fml

---
## [LoneAce01/IPT2-Group3](https://github.com/LoneAce01/IPT2-Group3)@[8f2a110437...](https://github.com/LoneAce01/IPT2-Group3/commit/8f2a110437921a9a35e6e3cc4014b9b1946da6cb)
#### Tuesday 2023-02-28 15:06:41 by Cmgdcmgd

Channel

May code na ng breakfast ideas and lunch ideas part pero need pa i edit (Lunch ideas) ni Erika and dagdag yung dinner ideas part. Thank you!

---
## [nightflyza/Ubilling](https://github.com/nightflyza/Ubilling)@[fb81c7f41c...](https://github.com/nightflyza/Ubilling/commit/fb81c7f41c129e73e9b87ea4c3ebd90f633f41f2)
#### Tuesday 2023-02-28 15:07:58 by l1ght13aby

fuck you array_merge

using array + array preserves keys

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[e190d1178c...](https://github.com/seanpdoyle/turbo/commit/e190d1178c3de688b552b46e42646e518a05fa03)
#### Tuesday 2023-02-28 16:07:28 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [Spookerton/Baystation12](https://github.com/Spookerton/Baystation12)@[e6362376cb...](https://github.com/Spookerton/Baystation12/commit/e6362376cb2bc6cf95004b921aa1f4bc5ff5ccb5)
#### Tuesday 2023-02-28 16:12:19 by gy1ta23

rifles!!!1


fixes descs


lathemags


oops i forgot a mag


holy shit hitting / is not that hard


Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>

---
## [sphilipse/kibana](https://github.com/sphilipse/kibana)@[43fa5174f8...](https://github.com/sphilipse/kibana/commit/43fa5174f813ce7999dbc65b71cbb9ba0168fb1d)
#### Tuesday 2023-02-28 16:31:41 by Clint Andrew Hall

[kibana] Thank you for everything, Spencer! 🧔🏻‍♂️ (#150759)

## Summary

> _Inspired by @kertal, and extracted from his PR
https://github.com/elastic/kibana/pull/150660, specifically
@thomasneirynck's
[proposal](https://github.com/elastic/kibana/pull/150660/files#r1101795511)._
>
> _Holding for 24 hours, for our friends in later time zones._

Several of us felt a dev-only easter egg-- where, if you're lucky,
@spalger joins you as you test your latest feature-- would be a fun
tribute as he leaves us for new and exciting opportunities.

Elasticians, feel free to send your love to @spalger in the channel of
your choice, of course, but we'd appreciate your review of this pull
request. ❤️


![image](https://user-images.githubusercontent.com/1178348/217867285-b23dcf1f-1a4a-45fd-b828-f6b24215fef2.png)

---------

Co-authored-by: spalger <spencer@elastic.co>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[494d4d9c32...](https://github.com/mrakgr/The-Spiral-Language/commit/494d4d9c3246890928ae0ac296d949b59b16db22)
#### Tuesday 2023-02-28 16:32:02 by Marko Grdinić

"1:55pm. Done with breakfast. Time for a bit of chill and then I will start dealing with the Web API tutorial.

2:25pm. Let me go back to Teddy's course.

Damn, I am tired. It is very difficult to get back to sleep once you get up in the middle of the night.

```cs
public decimal GetPokemonRating(Pokemon pokemon) => pokemon.Reviews.Average(x => (decimal)x.Rating);
```

I think this is what was giving me trouble. Let me fix it.

2:35pm.

```cs
public decimal GetPokemonRating(IQueryable<Pokemon> pokemon) => pokemon.SelectMany(x => x.Reviews.Select(x => (decimal)x.Rating)).Average();
```

I am not sure whether this will compile to valid SQL, but let me give it a try.

What did Jasper say about ModelState? I forgot.

```
        [HttpGet("{id}")]
        [ProducesResponseType(200, Type = typeof(Pokemon))]
        public IActionResult GetPokemon(int id)
```

Instead of returning this, I should return a typed `IActionResult`.

...Hmmm, it does not have a type.

2:55pm.

```cs
        [HttpGet("exists/{id}")]
        public ActionResult<bool> PokemonExists(int id)
```

Wow, I can't believe that I just had to do a single case and the autocomplete suggested a refactoring for the rest. Do I have Copilot on or something?

```cs
        public decimal GetPokemonRating(int id)
        {
            var x = ctx.Pokemons.Where(x => id == x.Id).SelectMany(x => x.Reviews.Select(x => (decimal)x.Rating));
            var n = x.Count();
            return n > 0 ? x.Sum() / n : 0;
        }
```

I do not like this implementation. But let me give it a try.

3:35pm.

```cs
        public decimal GetPokemonRating(int id)
        {
            var reviews = ctx.Pokemons.Where(x => id == x.Id).Select(x => x.Reviews.Select(x => (decimal) x.Rating)).First();
            try { return reviews.Average(); } catch { return 0; }
        }
```

I keep rewriting this thing trying to find the optimal form. It should be done like this.

3:45pm. Let's stop messing around. Let me watch Teddy's tutorial again.

https://youtu.be/K4WuxwkXrIY?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0

Teddy explains the model state here.

3:55pm. https://youtu.be/bSvYErXVRtQ?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0
ASP.NET Core Web API - 7. GET & Read Methods [PART 2]

I really don't have much patience today. Let me just skim the rest. I get all of this.

https://youtu.be/bSvYErXVRtQ?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0&t=819

This is the kind of work you'd need to pay me to do.

4pm. I do not feel like watching the rest. I do not need anymore than this. I get the basics of it. I am just too tired right now to mess with it.

How about those http and networking courses.

https://www.youtube.com/watch?v=qiQR5rTSshw
Computer Networking Course

> It will prepare you to configure, manage and troubleshoot computer networks.

https://youtu.be/qiQR5rTSshw?t=55

...I am already bored by this. Let me just give it a few minutes and then I'll check out the http course.

...Forget it.

https://youtu.be/iYM2zFP3Zn0
HTTP Crash Course & Exploration

I already watched this once back in 2020. This is more along the lines of what I'd want.

https://youtu.be/2JYT5f2isg4
Full HTTP Networking Course – Fetch and REST APIs in JavaScript

This is the one I linked to earlier.

> At the end we'll build a web crawled in JS from scratch.

This could be interesting.

4:10pm. I am thinking. The course is a bit interesting, but I am not going to be doing the exercises. I think I'll watch it for an hour and then leave it aside.

I'll make use of Teddy's project as a reference. I do not want to write more C# for my personal projects. Instead since F# has the migration tools, I'll give them a try. Alternatively, I'll write just the database segments in a separate C# project. Either way is fine for me.

...In the C# project, all I really need are the models and the context class. Everything else should really be done in F#.

4:20pm. https://youtu.be/2JYT5f2isg4?t=425

This isn't too bad, but yeah...it is time to start.

https://www.youtube.com/playlist?list=PLUOequmGnXxOgmSDWU7Tl6iQTsOtyjtwU
ASP.NET Core 2.2 & 3 REST API Tutorial

I am looking at this, and he goes through it in significant detail, a lot more than Teddy.

https://youtu.be/2JYT5f2isg4?t=512

This course is more interactive than I thought.

4:35pm. Nevermind that JS course. Let me watch the crash course for a bit.

https://www.youtube.com/playlist?list=PLillGF-RfqbYeckUaD1z6nviTp31GLTH8
Programming & Web Development Crash Courses

4:40pm. https://youtu.be/iYM2zFP3Zn0?t=595

Let me take a short break.

5pm. Let me resume.

5:05pm. https://youtu.be/iYM2zFP3Zn0?t=790
HTTP Crash Course & Exploration

Let me stop here. This is something I need to watch, but not right now.

I will crash at this rate. I am much more strained than I would usually be at this time.

I am tired!

Finishing off the EF Core videos was about how much I had in me. Plus I started an hour earlier than usual, so it is no wonder that I am so tired.

Right now I am thinking how I should resume the video that I started 10 days ago. I am going to recommend the CSS course and Jasper Kent's EF videos. Then I will dive right into the front end.

I am at my limit as far tutorials are concerned.

https://www.youtube.com/playlist?list=PLUOequmGnXxOgmSDWU7Tl6iQTsOtyjtwU
ASP.NET Core 2.2 & 3 REST API Tutorial

In this playlist there is knowledge I'll need on how to keep user state and how to log him in and such, but I do not need that right now. I'll leave that for when it comes to that. Tomorrow, I am going to get that basic HTTP course out of the way and start coding the frontend.

I was really missing knowledge of how to do the frontend and the acess the database.

Not going to get a job without those two. I've been right to apply, and apply honestly.

I can be mad at being rejected, but I need to be honest with how much of the stated requirements I actually meet.

I mean, if a job requires React and SQL, and similar database knowledge, I can't complain about being rejected for jobs that I applied to a month ago. If I have all the skills, and not getting calls, then I can bluff about my exp, or even try freelancing.

It is only now that I am really ready to start my first project. It should be fun.

I'll have to look at that Elmish.Bridge thing, as I want the server to be stateful for games.

I have all the pieces in my mind, I just need to bring them forth into code. I'll start that tomorrow, documenting every step of the way as I go along. In video as well!"

---
## [ivti09/Red-Dusk](https://github.com/ivti09/Red-Dusk)@[6074dbac00...](https://github.com/ivti09/Red-Dusk/commit/6074dbac0041db146de6d0f916d2e9485d64ad2c)
#### Tuesday 2023-02-28 16:52:54 by Durangq

We thought that storms were caused by petty gods

why the fuck is balancing this stupid war so hard

---
## [ASKnetCommunity/LEAD](https://github.com/ASKnetCommunity/LEAD)@[cde04bc0a0...](https://github.com/ASKnetCommunity/LEAD/commit/cde04bc0a0ceab8521e5e419e1e3519abd4a44bb)
#### Tuesday 2023-02-28 17:33:40 by Dawa Edina Hillary

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
## [zerbina/nimskull](https://github.com/zerbina/nimskull)@[c4250cc115...](https://github.com/zerbina/nimskull/commit/c4250cc11536bf6c8922bbd192d2ec39142d46d9)
#### Tuesday 2023-02-28 17:35:44 by Saem Ghani

Parser: drop direction `reports` dependencies

This removes direct dependency on `reports`, but an indirect one still
exists via `msgs`. It's pretty trivial indirection at the moment, but
after dropping direct reports dependencies the API can be changed more
drastically.

A number of changes were required in order to make this possible, here
is an overview:

- smaller parser public API & simpler implementation
- added `parse` compiler command, for devs
- parser error message improvements
- fixes to `astrepr` logic and output
- lots of style clean-ups

Details
=======

Slimmer `parser` Public API
---------------------------

Previously the parser had many public procedures (eg: `isOperator`,
`getTok`, `skipComment`, etc) that would allow fine grained control for
other modules.

There are many issues with this:
- there are no consumers of this API
- lots of public API surface to test
- the API itself was bad, it conflated lexing and parsing

The public API surface for the parser has been reduced significantly,
now consisting of:
- `openParser`
- `parseTopLevelStmt`
- `parseAll`
- `closeParser`
- `parseString`

That's it, which frankly reads far more sensibly.

Simplified `parser` Implementation
----------------------------------

- removed `InternalReport`, `reports_parser`, and `reports_enum` imports
- introduced diagnostics for the parser, akin to the lexer, `ParseDiag`
- `ParseDiag` favours data over strings
- `ParsedNode` now has its own kind enum, mostly a subset of
   `TNodeKind`, but entirely compatible

Consolidated a pattern within the parser, where a node was created with
the current token's information, and then the token was immediately
consumed via `getTok` to advance the `lexer`. This is captured in the
newly introduced `newNodeConsumingTok`.

Long-term, itemizing these traversal/consumption patterns will make the
parser logic not only more regular, but also highlight oddities in the
grammar as the implementation will be convoluted.

Parsing/Diagnostics Performance
-------------------------------

`ParsedNode` uses a lightweight `ParsedToken`

Introduce `ParsedToken`, a smaller data type, storing the least amount
of data required from `lexer.Token` for `ParsedNode`. This not only
saves memory, but the runtime performance impact on my machine is
roughly 33% faster full compiler testament run for all targets

- before change: 3+ minutes
- after change:  2+ minutes

Added specialized diagnostic/report kinds for:
- empty accent quote when ident expected
- msg for asm statements without a string literal
These reduces the amount of string data carried around in the compiler.

Improved Custom Numeric Literal Handling
----------------------------------------

- the `lexer` still does silly things for lexing these
- it just does less work and produces better data
- fewer string operations and hacks are required by the `parser`

Parser Diagnostic/Reporting - Invalid Indentation
-------------------------------------------------

- now has correct source line information
- tracks instantiation and submission location
- has the appropriate severity
- improved phrasing for indent error from possible missed `=` character
- adjusted tests for the above

Parser Diagnostic/Reporting - Malformed Call Syntax
---------------------------------------------------

- `parser` detects malformed calls and sets better line info
- net-net the user will have a better chance to find the issues

Parser Diagnostic/Reporting - Misc
----------------------------------

- token rendering call out keywords via prefix, eg: `keyword template`
- inconsistent spacing style check shows the problematic source

Removed unused report kinds:
- `rparIdentOrKwdExpected`
- `rparRotineExpected`
- `rparPragmaAlreadyPresent`

Parse Compiler Command
----------------------

`parse` command:
- added `parse` command, which outputs the parsed ast for a file
- usage: `nim parse foo.nim`
- super useful for diffing parser output changes
- heavily leverages `astrepr`

`astrepr` module:
- `astrepr.treeRepr` now works for `ParsedNode`, was previously broken
- AST trasversal is now exhaustive and breakages less likely to pass CI

`astrepr` output improvements, mainly for `ParsedNode`:
- `astrepr` now shortens ParsedNodeKind enum
- output now includes line and column information
- comments no longer result in excessive new line output
- fixed many formatting issues for `ParsedNode` output
- improved `astrepr`'s output for custom numeric literals

Canonical Filenames Performance Issue
-------------------------------------

Also discovered a performance issue with canonical filenames option and
the `nimdebugstacktrace` option. Removed some of the pain, but canonical
file paths result in significant performance issues due to filesystem
IO. I've fixed part of it and filed an issue:
https://github.com/nim-works/nimskull/issues/546

Other Improvements
------------------

- introduced `debugutils.setFrame` template for frame msg hints
- above `setFrame` avoids the canonical path performance hit
- removed circular dependency between `ast` and `options` module
- document unused parser reports and other outliers
- move `isImportedException` to `ast/types`, whice drops `front/options`
  cyclic depencdency from `ast/ast_query`
- fixed docs in nimlexbase, also easier to understand
- `ast.toPNode` now handles `nil` input
- `syntaxes.parseFile` returns `ParsedNode`, allows avoiding unnecessary
  conversions in future use cases where only `ParsedNode` is required

Special Mentions
----------------

Thanks, clyybber and zerbina for the reviews!

Misc
----
- remove blank space characters from otherwise empty lines
- remove awful code style of `0 < foo.len`
- fixed a number of typos in comments
- adjusted a few tests to ensure they pass

---
## [dcunited001/.emacs.guix](https://github.com/dcunited001/.emacs.guix)@[4dd655779c...](https://github.com/dcunited001/.emacs.guix/commit/4dd655779c2f841461b42947ab309b76502265b1)
#### Tuesday 2023-02-28 17:43:00 by David Conner

"trying to get preamble for non-added document"

* I've set up LSP at one point... but no, i've never seen that error before

* have you ever seen this error before?

YOUR MEDIAN INCOME OVER THE PAST 8 YEARS IS LESS THAN $4,000. THE ADDERAL AND
PSYCHIATRIST APPOINTMENTS REQUIRE OVER HALF YOUR GODDAMN ANNUAL INCOME BECAUSE
THE DEA SUCKS ASS.

YOU HAVE $3.00 IN YOUR BANK ACCOUNT AND WILL NOW SPEND THE NEXT TWO WEEKS IN A
BRAIN FOG BARELY SCRAPING ENOUGH MONEY TOGETHER TO GET MEDICATION, ALL SO YOU
CAN START WORKING IN A DIFFERENT DIRECTION OR ON A DIFFERENT PROJECT ALTOGETHER,
NEVER ONCE ABLE TO MAINTAIN MOMENTUM FOR LONG ENOUGH TO FUCKING GET A JOB WHERE
YOU'LL BE BABIED WITH $30.00 COPAYS FOR EVERY GODDAMN THING, NEVER CARING
WHETHER THE GENERIC ADDERALL XR HAS 25% L-AMPHETAMINE OR GODDAMN NEAR 95%
L-AMPHETAMINE. I SWEAR TO GOD THE BRAND-NAME SHIT IS CLEAN D-AMPHETAMINE BECAUSE
THE GENERIC ADDERAL IS NOTHING BUT SIDE-EFFECTS

**GARBAGE**

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[97f567fdc7...](https://github.com/Sealed101/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Tuesday 2023-02-28 18:07:18 by MMMiracles

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
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[27c35bfa0b...](https://github.com/Sealed101/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Tuesday 2023-02-28 18:07:18 by MrMelbert

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
## [eggheadfixers/jubilant-funicular](https://github.com/eggheadfixers/jubilant-funicular)@[c3f4e01496...](https://github.com/eggheadfixers/jubilant-funicular/commit/c3f4e01496571196b55780af97a7bec90cddb837)
#### Tuesday 2023-02-28 18:37:46 by eggheadfixers

Update README.md

A WiFi technician is a skilled professional who specializes in the installation, maintenance, and troubleshooting of wireless network systems. These systems include routers, access points, and other devices that enable users to connect to the internet wirelessly. As technology continues to advance, the role of a WiFi technician has become increasingly important in modern society.

WiFi has revolutionized the way we live, work, and communicate. The internet has become an essential part of our daily lives, and WiFi technology has made it possible to access the internet from almost anywhere. This has made it easier for people to stay connected with their friends, family, and colleagues, as well as access information and entertainment.

One of the main benefits of WiFi technology is its convenience. Unlike traditional wired networks, WiFi enables users to connect to the internet without the need for physical cables. This makes it possible to access the internet from multiple devices, such as smartphones, tablets, laptops, and desktop computers, without the need for additional hardware.

However, despite the convenience of WiFi technology, there are some common issues that can occur. These include slow internet speeds, poor signal strength, interference from other electronic devices, and security concerns. A WiFi technician is trained to address these issues and ensure that the wireless network is functioning optimally.

In addition to troubleshooting issues, a WiFi technician can also provide valuable advice on how to optimize the wireless network to achieve the best performance. This may include recommendations on where to place routers and access points, as well as advice on how to secure the network to prevent unauthorized access.

Overall, WiFi technology has significantly eased our lives by providing easy access to the internet from almost anywhere. And with the help of a skilled WiFi technician, users can ensure that their wireless network is functioning optimally and addressing any issues that arise.

---
## [ZzAve/teambalance](https://github.com/ZzAve/teambalance)@[be41a19967...](https://github.com/ZzAve/teambalance/commit/be41a199672f42698acd0e60d1d135ce589d480b)
#### Tuesday 2023-02-28 20:22:05 by Julius van Dis

Upgrade to MUI 5 (#227)

* clean covid-19

* Add themeprovider to app

* Add MUI 5 dependencies

- included @mui/x-date-pickers (as replacement for @material-ui/pickers)
- included emotion for typesafe css

* Remove MUI 4 dependencies, and fix breaking component changes

Follows: https://mui.com/material-ui/migration/v5-component-changes/

Noteworthy:
- Fixes in createStyles and withStyles
- Deprecated `<Hidden>` component (mostly move to:
 ```<Typography variant={"button"} sx={{ display: { sm: "block", xs: "none" } }}>
  Terug naar de veiligheid</Typography>```
- App is wrapped in <StyledEngineProvider injectFirst> to support JSS (prepare for migration to emotion
- Shit ton of renames from @material-ui/* to @mui/*
- Verwijderen van AttendeeStyledButton, en fallback op normale Button. 'uncertain' is mapped naar 'warning', en die kleur is aangepast in de palette van de theme.

* Apply webpack optimisations to reduce build times (dev: 30s to 10s, prod 60s to 10s)

* Replace JSS with emotion

* Remove @mui/styles

* Upgrade notistack to v2

* Pin dependencies

* Fix latest mui things

---
## [Cabbasca/Trouser-Streak](https://github.com/Cabbasca/Trouser-Streak)@[f5a16ec3b5...](https://github.com/Cabbasca/Trouser-Streak/commit/f5a16ec3b5a4ad85ebb7e6ff4962f2e5ac11a53a)
#### Tuesday 2023-02-28 20:22:48 by etianl

0.3.8 Many big updates, SHULKER BUTTONS back!

0.3.8
-**General**
-FULLAUTO options for Boom+, ExplosionAura, and HandOfGod now have a tick delay for reduced lag.
-ExplosionAura explosions now also have a tick delay when you are moving for less lag
-AirStrike+, Voider, and ExplosionAura now turns off when you leave the game and voider also when you die.
-AirStrike+ now rains cats which are invulnerable to damage.
-AirStrike+ Can now rain CatsAndDogs as an option.
-**ShulkerDoop!**
-Made ShulkerDupe work more like the original, using buttons in the shulkerbox screen rather than options in the meteor menu. Still uses Allah-Hack dupe code, credits to them for that.
-STILL ONLY WORKS IN SERVERS 1.19 and BELOW, VANILLA, FABRIC, OR FORGE.
-**NewerNewChunks updates**
-Improved the "IgnoreFlowBelow0" option to show a newchunk as well if flow is above AND below Y0 not just if above Y0.
-Added AdvancedMode to NewerNewChunks, which highlights chunks that have flow only below Y0. If there is nothing but these you are updating old chunks to the new build limits and the FlowIsBelowY0 coloured chunks are OLD. If they are mixed with newchunks the FlowIsBelowY0 coloured chunks are NEW.
-**Voider updates**
-Renamed to Voider+.
-Voider now grabs a location on activation to void around, instead of keeping it centered around your position. Just ensure that area stays loaded.
-Added a "VoiderBot3x3" option to run voider nine times over to void it's full range three by three times.
-Added a "TP forward" option which can teleport you forward and run Voider again clearing a strip out of the world.
-**HandofGod updates**
-Added "NukeAroundPlayer" option so you can now turn off the default /fill around your player.
-"NukeAroundPlayer" /filling is now based on a tick delay, rather than based on pressing directionals like it was before
-Added "VoiderAura" option. It /fills a single layer from top to bottom in a loop based on the ranges from your character you set. Credits to AllahHack for the idea from the voider module.
-Added "MagicEraser" option. It deletes a single layer up to 90 blocks in radius at a set distance from your character. Press directional keys to delete world.
-Added "Roofer" option so you can automatically make an obisidian roof as you're deleting the world.

---
## [hibou-io/odoo](https://github.com/hibou-io/odoo)@[639cfc76ba...](https://github.com/hibou-io/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Tuesday 2023-02-28 20:29:08 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Retinalogic/LianaLovesMe](https://github.com/Retinalogic/LianaLovesMe)@[b01fc177f0...](https://github.com/Retinalogic/LianaLovesMe/commit/b01fc177f02734bc3024a299f9bd43bfe0eed3c2)
#### Tuesday 2023-02-28 20:48:58 by PowerPC

Surprise Liana!

[Intro]
doorbell Yea? bang Surprise Liana!

[Verse 1: Hurt2TheCore]
It's time for me to act like a Liana
Some people don't believe that I can turn Romanian
Romanian, it's just a simple way of being fucked up
Fuck Liana family for a bunch of dough like a drug bust
Bustas with no nuts wanna give me shit real quick
Quit beggin' trick 'fore I shoot you in yo face bitch
Bitch ass Lianas like to high cap like they from the hood
Hood pimpin' Lianas like to shoot them pistols with no love
Lovelessly you get this, when I smoke a Liana

---
## [5XD-AVD/Hoger-bewustzijn](https://github.com/5XD-AVD/Hoger-bewustzijn)@[11809593b1...](https://github.com/5XD-AVD/Hoger-bewustzijn/commit/11809593b1d4459f327bac54b008a38196441b4d)
#### Tuesday 2023-02-28 21:46:39 by Arjen van Diepen

Hoger bewustzijn

De wereld veranderen door te creëren!

Waarheid is de basis om te kunnen creëren. Iedereen wil vrijheid, geluk, liefde, gezondheid, maar veel mensen negeren de waarheid om dit te bereiken. 
Deze waarheid ligt in onszelf en de omgeving om ons heen. 
We geloven vaak dingen of gaan liever in leugens mee om aardig gevonden te worden of om bij een groep te horen. 
We doen dit uit gemakzucht of om een ander de schuld te geven. 
Van deze principes maken vooral ook religies in onze samenleving veelvuldig gebruik.

Om bewust te kunnen creëren "moeten" we eerst weten waar we mee te maken hebben. 
Dat zijn namelijk occulte groeperingen. 
Occult betekent niks meer of minder dan verborgen.
Deze groeperingen hebben occulte kennis verborgen gehouden door eerdere samenlevingen te manipuleren en om te vormen naar de huidige.
De kennis waar het hier vooral om gaat is die van de natuurwet, hoe het bewustzijn werkt en de onzichtbare spirituele wetten, die de gevolgen van menselijk gedrag beheersen. 

Hoe kunnen we de waarheid zo goed mogelijk benaderen om de natuurwet toe te passen?

Wie bepaalt de natuurwet?
Natuurlijke wetten zijn gelijk aan waarheid. Het is iets wat aanwezig is in de natuur en waarop de mens geen invloed heeft.

Wat bepaalt de natuurwet?
De waarheid wordt bepaald door de natuur en is niet door de mens te bepalen.

Waar is de natuurwet?
De waarheid is in de natuur aanwezig, het is er voor altijd en dit zal de mens zo goed mogelijk moeten benaderen, om in harmonie met de natuur te kunnen leven.

Wanneer is de natuurwet van toepassing?
De waarheid is dit moment en wat er altijd geweest is, maar ook in de toekomst zal zijn.

Conclusie waarheid is absoluut en voor altijd.

Waarom is de natuurwet aanwezig in de mens(heid)?
De mens is één met de natuur. Deze waarheid is te vinden in onze genen, de plattegrond in de mens. Deze worden gevormd, voor dat we een foetus worden. Deze zijn dus voor altijd aanwezig en kunnen we niet (meer) veranderen. Men probeert dit wel (chemisch) te doen en tot op zekere hoogte zal dit de connectie met onze natuur verstoren. Dit zal echter niets veranderen aan de waarheid, die was, is en zal zijn.

Hoe is de natuurwet aanwezig in de natuur?
Dit wordt vertaald door mRNA naar ons DNA. Dit is de antenne van ons mensen, naar het hogere bewustzijn.


Conclusie: de waarheid blijft altijd hetzelfde!
Waarheid blijft objectief, wat betekent dat het niet gebaseerd is op perceptie van mensen.
De waarheid wankelt niet, buigt of verandert niet. Het maakt niet uit of iemand het gelooft, weet, ziet, en of iemand het wil zien. Het verandert niet en zal nooit meer veranderen. Het verleden en nu blijft hetzelfde.

Waarheid of perceptie 
Als de mensen waarheid horen hebben de mensen de meest ongelofelijke rare opmerkingen. Zoals dat is jouw of mijn waarheid of het in verband brengen met God, of iets anders dat volkomen irrelevant is.
Als iemand zijn bril afzet kan de waarheid er anders uit zien maar blijft hetzelfde.
Perceptie is niet gelijk aan realiteit of waarheid!

Geloof of waarheid
We geloven al snel wat we "moeten" denken, dit komt door de informatie die de hele dag op ons afkomt. De telefoon, tv, radio, school, borden langs de weg, regels etc… 
We geloven dit en denken niet eens meer na en volgen dit gewoon op. 

Ego
Dit kan al worden gezien als een aanval op het menselijk ego, namelijk hoe groter ego men heeft hoe meer dat hun perceptie belangrijk en accuraat is voor hen. 

Daar komen principes bij om de waarheid te vinden. 
Hierin spelen proteïnes een belangrijke rol. 
Deze proteïnes kunnen beïnvloed worden door chemicaliën, trauma maar vooral door: waar wij in geloven. 

Chemicaliën 
Alles wat onze hersenen en genen beïnvloed zoals drugs, voeding, wat we op ons huid smeren en wat we in ademen etc. beïnvloeden de toegang tot en de verwerking van de informatie, die in ons DNA is opgeslagen.

Trauma
We worden van jongs af aan beïnvloed door trauma, als we te dicht bij een vijver komen kan dat al voor een trauma zorgen. 

Waar we in geloven 
Is hierbij het belangrijkste. Iedereen kan zwemmen vanaf de geboorte dat zit in onze genen. Vanaf dat we kunnen lopen worden we bij water weggehouden omdat onze ouders geprogrammeerd zijn dat we kunnen verdrinken. Deze angst wordt met incidenten uitvergroot door media, onder - wijs etc… 

Als we geloven dat een trauma echt is, zal dit gedeelte van de informatie in ons DNA niet meer gelezen worden, doordat de proteïne dat gedeelte van onze genen niet meer wil lezen.   
Groeien we op in de omgeving van dit trauma zullen de mensen in deze omgeving daar ook in gaan geloven. 
Hierdoor zetten we sloten op veel mentale kooien voor onszelf. 

Kunnen we deze ontgrendelen door de waarheid te accepteren?

Je kan onwetend iets doen en hopen dat het goed afloopt of je kan eerst op onderzoek uitgaan om uiteindelijk een staat van weten te bereiken. Hiervoor heb je kennis nodig van de natuurlijke wetten. 
Mensen, die onwetend volgen, ontbreekt het aan die kennis. Deze mensen hebben moedwillig al de informatie, vaak enkel uit gemakzucht, genegeerd.
Maar als je onwetend van een hoge klif springt of valt dan zijn er evengoed gevolgen.
Hoe dan ook, aan de natuurwet ontkom je niet. 

Daarom is bewustzijn iets van weten en onwetendheid.
Hierin zit volgens de natuurwetten geen verschil in. 
De waarheid is ieder zijn eigen verantwoordelijkheid

Willen we creëren gaan we weer terug naar de natuurlijke wetten en hoe het werkt.
De principes zitten ook in de natuur en gaan we zo dicht mogelijk benaderen.
Daarbij zijn de principes absoluut en voor altijd en te meten aan de waarheid! 
Het is aan ons mensen om daarnaar te leven. 

In jouw werkelijkheid kun je eraan denken om de schadelijke chemicaliën te vermijden en trauma's op te lossen maar het belangrijkste is, niet meer te geloven, maar de waarheid zo dicht mogelijk zien te benaderen met de principes uit de natuurlijke wetten.

Waarom zijn de principes aanwezig in de natuur?
Deze principes worden voor onze proteïnes verborgen of gelezen in onze genen (de plattegrond). Deze zijn wel voor altijd aanwezig en kunnen we niet (meer) veranderen (behalve misschien chemisch). We zullen ze alleen weer moeten leren te lezen zonder vervuiling en/of verstoring. 

Als we willen dat onze proteïnes de genen weer compleet kunnen lezen, betekent dat we de waarheid compleet lezen, hetgeen weer vertaald wordt door ons mRNA naar ons DNA. Hiermee herstellen we de antenne naar ons bewustzijn.

Hoe kunnen we onze principes aanpassen aan de waarheid?
Als je deze verandering wilt creëren is actie vereist! Het belangrijkste is de waarheid te vinden of te zien om te creëren. 
Onze huidige werkelijkheid is op vals geloof gebaseerd, op een illusie.

Sommige mensen zeggen dat verandering gebeurt in het hart of hoofd, wat zeker waar is. maar uiteindelijk gebeurt er pas echt iets met lef en actie! 

Principes zijn vaak aangeleerd op een vals geloof zoals religie, overheid, media, onder - wijs, familiaire omstandigheden etc. Bijvoorbeeld, je mag niet stelen volgens de natuurlijke wet.
Veranderen we de natuurlijke wet in religie mogen we biechten, bij de overheid moet een rechter hierover beslissen, volgens de media moet het eerst bewezen worden en op school kan men zomaar je stift afpakken als je deze ongeoorloofd gebruikt, in een familie wegkijken om gezeik te voor komen. 

Maar volgens de natuurwet maakt de draai, die eraan wordt gegeven, niets uit. Er is altijd schade aan de omgeving en de balans dient hersteld te worden. Door jezelf of door de omgeving. Het creëren van een onbalans, heeft altijd direct gevolgen in jezelf en in je omgeving. Het is hierdoor dat we in een maatschappij zitten, die zichzelf vernietigt.

Daarom is het belangrijk om de principes uit de natuur te volgen en geen misdaden te begaan, die vaak uit angst of mind control plaatsvinden, zoals:
Diefstal, aanranding of verkrachting, moord, liegen (waarheid achterhouden), geweld of dwang toepassen.

Maar wat is nu de waarheid als je kijkt naar deze, door ons allemaal als misdaad bestempelde handelingen?

Diefstal
Spreekt voor zich. We weten allemaal dat stelen verkeerd is.
Maar, veel mensen zullen zeggen dat ze belasting zien als iets goeds, terwijl, als er een andere criminele organisatie geld vraagt voor bescherming, ze dit wel als fout zien. Angst om het zelf op te lossen of het geloof in de overheid, die in feite dezelfde natuurlijke wet overtreedt.

Aanranding of verkrachting
Als iemand tegen zijn zin in gevaccineerd wordt, is dat feitelijk ook verkrachting. 
Angst om buiten de groep te staan of het geloof in je ego, veranderen niets aan het feit dat je lichaam, tegen je wil, binnengedrongen wordt.

Moord
Als je iemand doodt om een moord of meerdere moorden te voorkomen, kunnen ze je nog altijd opsluiten voor moord.
Hierdoor is er angst om jezelf te verdedigen en het geloof dat doden ten alle tijden moord is, terwijl de omstandigheden enorm van belang zijn om te kunnen bepalen of iets wel of niet het juiste is om te doen.

Liegen (waarheid achterhouden)
Als je liegt of waarheid achterhoudt, ontneem je een ander het recht om de waarheid te ontdekken over iets of iemand.
Angst, om niet geaccepteerd te worden of het geloof dat jouw ego belangrijker is veranderen daar ook hier weer niets aan.

Geweld of dwang
Ook hier zullen we zeggen: "Spreekt voor zich", maar als iemand anders je begint te slaan, of te dwingen mag je jezelf verdedigen.
Angst jezelf te verdedigen of te laten dwingen, het geloof in de overheid, die dezelfde middelen gebruikt, gaat nog altijd in tegen deze natuurlijke wet en zal, hoe dan ook een verstoring in de balans veroorzaken.

Het gevolg van het negeren van de natuurlijke wetten en accepteren en vaak zelfs verdedigen en goedpraten van de gepleegde misdaden, is meer trauma of angst.
Trauma komt voort uit angst zorgt ervoor dat je bepaalde dingen niet meer gaat zien dus ontwikkeling van jezelf tegen houdt.
Door het geloof in iets of iemand, dat puur mind control is, ga je principes relativeren.
Wat uiteindelijk je proteïnes aanpast, zodat je genen (plattegrond) niet meer volledig te lezen zijn. 

Als we de waarheid weten, kunnen we die kennis omzetten in actie.

1.	Erken, om te beginnen, dat er een probleem is.
Vervolgens kun je de op angst gebaseerde ontkenning aanpakken en overwinnen. Ontkenning zal het probleem alleen maar groter maken (denk aan slavernij).

2.	Erken dat symptomen slechts gevolgen zijn van onderliggende oorzaken. 
In plaats van symptomen te behandelen, kun je beter een nauwkeurige diagnose stellen (= bij wijze van kennis) van de oorzaak van het probleem. Daarbij kom je tot inzicht in welke oorzaak bepaalde symptomen hun oorsprong vinden.

3.	Door middel van de verkregen kennis dien je de actie ondernemen, die nodig is om de oorzaak, die tot het probleem heeft geleid, te corrigeren.

Als we weten hoe dat we denken om de waarheid te zien, kunnen we creëren.
Hierbij is de hersenstructuur, gedrag, gezondheid en inzicht in de 3 basis structuren van het menselijk brein cruciaal.

Het R-complex (reptiel brein) 
Dit is het laagste bewuste deel van de hersenen, dat alleen reageert op stimulus. Vecht of vlucht modus wordt dit ook wel genoemd en omschrijft mooi wat we de hele dag "moeten" denken (basis overleving functies). Symbolische het mannelijke deel.

Het limbische systeem (zoogdier brein)
Dit is het midden brein bij narcisten, psychopaten functioneert dit deel van de hersenen niet goed. Dit gedeelte wordt verdoofd door de proteïne. Hier zijn de chronische aandoeningen, trauma, geboortestoornis etc… van belang. Symbolische het vrouwelijke deel.

De Ne cortex (menselijk brein)
Het bewustzijn het nieuwste deel van de hersenen, waar elektrochemische activiteit plaatsvind die ons mens maken. Met hogere denkfuncties zoals, logica, intuïtie, creativiteit, etc…

Toekomst
Aangezien de waarheid in het nu en verleden ligt, kan je de toekomst wel veranderen. 
De term waarheid kan altijd worden gebruikt of naar verwezen worden.
Als je het vermogen krijgt om waar te nemen wat nu, en is gebeurd noemt men bewustzijn. 
Nu heeft men het vermogen om patronen te herkennen en betekenis te geven. 
Hoe meer het bewustzijn is ontwikkeld, hoe meer men de waarheid ziet. 
Wat weer invloed heeft op je omgeving (de Cloud).

De belangrijkste eigenschappen die je nodig hebt om te creëren uit de waarheid zijn tijd en waar geef je aandacht aan.

We geloven op dit moment:
Bij de geboorte een naam en nummer in een systeem te schrijven die we koppelen aan de gregoriaanse kalender.

Dit is een kalender, die alleen is bedoeld voor fysiek bewijs.
Van verjaardagen, feestdagen maar ook planning van onderwijs, recht, loon, carrière, nieuws, huwelijk, kinderen etc…  
De vernauwing van ons bewustzijn vind hier al plaats.
We stellen niet eens vragen over andere zaken, we zijn alleen bezig met deze planning. 

Spiritualiteit is uit de samenleving!

Oftewel deze kalender is ons dogma dat we zelf hebben gecreëerd of is opgedrongen.
Hier worden de proteïne al aangepast dat we onze genen niet meer volledig lezen.
Maar dat ze met deze kalender ons bewustzijn, lichaam en denken controleren.

Bijvoorbeeld: 
De Maya's noemde deze kalender de Haab, deze gebruikte men alleen voor de boekhouding van de staat. 
Tzolkin kalender gebruikte men als persoonlijke kalender en duurt 260 dagen, namelijk 13 bedoelingen om te creëren en 20 aspecten om te kunnen creëren. 
Astrologisch 12 tekens per jaar maar ook weer verschillende tekens per dag. Etc…. 
Oude culturen keken ook naar de invloeden van buiten ons bewustzijn. 

Waar keken ze naar? 

Onze hersenen is het gereedschap om te denken, waardoor men letterlijk ruimte, krijgt om tijd te zien, die met deze kalender, gebruikt wordt om ons met fysiek bewijs dingen aan te leren.

Als men iets waarneemt waar geen fysiek bewijs van is, neem je het onbewust waar en zal je het niet (kunnen) of verkeerd toepassen. 
Ego is gecreëerd door programmering of trauma hoe dat je jezelf ziet of wilt zien.
Deze kalender is gegijzeld het patroon is te zien en wordt ook getoond aan ons.
Zolang we die volgen lopen we in een fuik die voor ons bepaald wordt.
Met andere woorden de proteïne heeft zich al aangepast om je genen niet meer in zijn geheel te lezen.

Geen verschil met een computer of robot. 

Als je dit los kan laten en alles overlaat aan je bewustzijn, ga je (out of your mind) voorbij je denken, of te wel over naar je intuïtie (je ziel, hart). 
Hierbij verlies je alle stress en zal je angst verdwijnen! 

Dan kan je uit komen in staat van alles weten (je genen kunnen weer volledig gelezen worden) op het gebied waar je de tijd en aandacht aan besteed.

Bewustzijn zit altijd vast aan:
Tijd (in het nu)
Plaats (waar je bent intern en extern)
Waar je naar kijkt
Hoe je het ziet

Vrije wil is de keuze waar je naar wilt kijken.
Bewustzijn is niet alleen wij mensen maar ook alles om ons heen (de cloud).

Dan komt er taal bij. 
We worden meteen naar school gestuurd om spelling te leren. Spelling oftewel toverspreuken (spel van spelling).

Als je een persoon neerzet met daar een lampje boven dan krijg je een idee.
Als je dit plaatje voor je ziet gaat er veel meer actie vanuit als het woord idee op papier.
Dit wordt waargenomen door je intuïtie (genen) aangezien we vaak beelden zien als we moe zijn na een dag hard werken, zijn we dit gaan zien als entertainment.

We denken in taal die ons op het verkeerde been zet. Als we in symbolen gaan denken en met elkaar communiceren, zou het veel makkelijker zijn.
Als men maanden bezig kan zijn om ons een presentatie te geven van 1,5 uur in vorm van een film of ander programma. 
Hoeveel symbolen krijgen we dan wel gepresenteerd in deze tijd. Hetzelfde geldt voor een lesprogramma etc...

Onze ouders kopiëren wat hun ze is aangeleerd. 
Op school leren we kopiëren wat anderen ons vertellen. 
Hetzelfde geldt voor het voortgezet onderwijs, waar we ons mogen ontplooien in onze gekopieerde werkelijkheid. 
Mochten we dan een carrière hebben met onze ambitie, leven we in de toekomst voor erkenning. 

Informatie is vaak geen waarheid, alleen bevestiging wat je al denkt te weten. 
We zijn zo op zoek naar informatie maar daarmee lopen we ook in een fuik die voor ons bepaald wordt.

Als we vrij willen zijn zullen we onze genen volledig gaan leren lezen met waarheid. 
Hier staat de G onder ander voor bij het freemason symbool 

Aangezien we aangeleerd worden om de 2 eerste hersenhelften apart te ontwikkelen wat symbolische in amusement terug komt als de bijl, gespleten kokosnoot, another brick in the wall (Pink Floyd), een hart van steen, medusa (media), etc… weten we nu wat het ego inhoud namelijk een blokkade tussen deze hersenhelften het mannelijke en vrouwelijke deel. Vaak is een van deze 2 sterker ontwikkeld door trauma (vrouwelijk) of ego (mannelijk). 

Als we gaan begrijpen dat onze programmering alleen bedoeld is om ons van de echte kennis weg te houden, gaan we begrijpen dat we niks geleerd hebben over het leven. 
Alleen maar om een systeem in stand houden voor een paar mensen die de echte kennis bij ons weghouden om ons te besturen als slaven.

Willen we ons ontwikkelen is het trivium belangrijk hulpmiddel.

Basis principes van het trivium:

Wie, wat, waar en wanneer bepaalt de definitie van het probleem.
Dat kan zijn spelling, invoer of kennis!

Waarom bepaalt de definitie van het probleem.
Dat kan door logica, begrippen of verwerking!

Hoe is het probleem ontstaan, bepaalt de definitie.
Dat kan door retoriek, spreken, uitvoer, wijsheid!

Gebruik altijd deze volgorde!

Hiermee leren we niet meer wat we moeten denken maar hoe dat we gaan denken.
Willen we gezamenlijk creëren zullen we een hoger bewustzijn "moeten" bereiken.

Je kan niet iets veranderen wat gecreëerd is, je kan wel iets nieuws creëren.



Gebaseerd op het werk van Bruce Lipton, Ian Xel Lungold, Max Igan en Mark Passio.
Met dank aan Eric zegt het.

https://t.me/freedom5xd
Link telegram kanaal

5XD

Arjen van Diepen

---
## [endofhome/kirill](https://github.com/endofhome/kirill)@[b0de200f78...](https://github.com/endofhome/kirill/commit/b0de200f7866c39dab06e2d69f8a54aceca5cd99)
#### Tuesday 2023-02-28 21:59:40 by Tom Barnsbury

Spike - Connect AudioOutput to button on listen page.

This commit contains a lot of changes!

Firstly, what was known as `AudioOutput` is now `Power`. The metaphor has changed slightly. That's because I want to write tests against a 'component', which I'm defining as the marriage of some HTML and some JavaScript. I renamed the class to `Power` so I could give the name `AudioOutput` to the component. Looking at it now, I think I quite like the `Power` metaphor. At the moment the component only includes a 'power on button', so that seems to fit well.

The tests for the component are much more complicated than the tests for the class we had previously. However, you can see how the class tests have evolved - the remnants are still visible in the test named 'AudioOutput can be powered on', which has the same assertions but now operates at the level of interactions with HTML elements. I'm using Jest's "jsdom" environment to allow me to interact with the HTML, this is enabled by a comment at the top of the test file.

I also had to write a script that parses the erb file. There's a JavaScript function `compileErb` which I can use in my JavaScript tests. This function relies on a bash script I wrote (`render_erb.sh`) which takes a template as a string, some variables as a string and then uses Ruby to render the result. You don't really need to understand how this works, but I can explain more if you want to understand it better.

There's entry point to the JavaScript app is a file called `app.js` which at this point in time only `requires` and executes the AudioOutput component script. It uses common.js modules, so I'm using Parcel.js to produce a JavaScript file which the browser can run. Commonly, a single JavaScript file will be included on all of the pages of the website, so I've decided not to test for the presence of it - I'm happy to rely on the fact that we'll ensure the app.js bundle is always present on our pages.
I've added another step to the `build` script which produces the JavaScript bundle after all of the tests have passed.

In the `listen.erb` page the JavaScript bundle is added to the page via a <script> tag.
The AudioOutput erb file is also added to the page.

I replaced the test against the server for the button with a test that proves that the component HTML is present. The button is now tested in the JavaScript component tests, so I don't need to test for it twice. All that matters at the server level is that the component is included on the page.

I don't love this design. Actually, there are a number of things I don't like about it, especially the way the files are organised. We might move some of them around. However, I think this design follows a modular approach, the TDD has aided the design of the production code and I believe it's made it quite difficult to break accidentally. I'd be interested to know what ways you're able to break the application without making one of these tests fail 😁

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[fae321e4ab...](https://github.com/Buildstarted/linksfordevs/commit/fae321e4ab395d3f319c954dd2e701b3400dad04)
#### Tuesday 2023-02-28 22:08:16 by Ben Dornis

Updating: 2/28/2023 10:00:00 PM

 1. Added: I Will Fucking Dropkick You If You Use That Spreadsheet — Ludicity
    (https://ludic.mataroa.blog/blog/i-will-fucking-dropkick-you-if-you-use-that-spreadsheet/)
 2. Added: axo blog - Thanks For Breaking cargo-dist! (I Rewrote It)
    (https://blog.axo.dev/2023/02/cargo-dist-rewrite)
 3. Added: How to develop un-analyzable PL
    (https://www.l3r8y.ru/2023/02/27/how-to-develop-un-analyzable-pl)
 4. Added: SiriGPT: A More Conversational Voice-Assistant
    (https://shivam.sh/2023/siri-gpt)
 5. Added: Rayan Saleh — The myth of the valuable generalist
    (https://www.rayan.ooo/2023/01/31/The-myth-of-the-valuable-generalist.html)
 6. Added: One Book, Many Readings
    (https://samizdat.co/cyoa/)
 7. Added: LattePanda V1 - my experience with a Raspberry Pi alternative
    (https://ounapuu.ee/posts/2023/02/28/lattepanda-v1/)
 8. Added: Investing Fundamentals: Probabilities (Free Tool)
    (https://blog.kerryjones.net/posts/investing-fundamentals/weighted-averages/)
 9. Added: Pagi on the App Store
    (https://lucas.love/blog/pagi-app-store)
10. Added: My favourite Ruby on Rails engines
    (https://blog.rstankov.com/top-8-ruby-on-rails-engines/)
11. Added: Business Law Research Paper Example - Brawnywriters
    (https://brawnywriter.com/business-law-research-paper-example/)
12. Added: Building Like the Yankees
    (https://shermanonsoftware.com/2023/02/27/building-like-the-yankees/)
13. Added: Matrix rain effect
    (https://www.maartenhus.nl/blog/matrix-rain-effect/)
14. Added: A Story from the Great Beyond: The Disabled Ghosts of Earth
    (https://florianbeijers.xyz/a-story-from-the-great-beyond-the-disabled-ghosts-of-earth)
15. Added: Writing Shouldn’t Be Hard
    (https://om.co/2023/02/27/writing-shouldnt-be-hard/)

Generation took: 00:08:06.2390629
 Maintenance update - cleaning up homepage and feed

---
## [dekreet/Kech-Support](https://github.com/dekreet/Kech-Support)@[f43c2dfa3e...](https://github.com/dekreet/Kech-Support/commit/f43c2dfa3e394f25a3b5d18e1272334d53fc9d67)
#### Tuesday 2023-02-28 22:32:52 by Davey Smit

Play some music to greet the visitor! :^)

When a visitor clicks fucking ANYWHERE, the mouse click is followed immediately by a 3 minute and 9 second, 32kb/s FL Keys MIDI render of Smash Mouth - All Stars (this is categorically the single most evil shit I've ever done as a programmer)

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[2b76197397...](https://github.com/GoldenAlpharex/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Tuesday 2023-02-28 23:00:24 by Jacquerel

Makes Lesser Form into one ability & unit tests it (#73572)

## About The Pull Request

Fixes #73491
Every time I have used this ability lately it's been fucked. 
It would vanish from my actions at arbitrary moments, and also sometimes
transform me into a horrible monkey-man thing instead of a monkey. This
is a shame because being able to become a monkey can be pretty fun, even
if it makes you very vulnerable to being butchered.

Refactoring it into being one action instead of two actions which add
and remove each other fixes the part where the action just disappears.
It reliably sticks between transformations now, regardless of whether or
not they were voluntary.

I also noticed that when I was turning into a monkey it wasn't dropping
the changeling "fake clothes" outfit pieces I had on as a human, leading
to a really fucked up looking monkey. I fixed this by adding `force =
TRUE` in the drop to ground proc in the check for if the equipment you
have is still valid after your species changes. I don't _think_ this has
any side effects but I never do and then someone finds some.
For good measure I also made all of the changeling equipment abilities
which don't work if you are a monkey detect if you become a monkey and
retract themselves.

I also noticed that for a long time Last Resort has been trying and
failing to give you Lesser Form (well, Human Form rather) as a Headcrab,
so I fixed that and now you actually get the ability.

Finally I did a _little_ bit of housekeeping in general on the
changeling actions, mostly balloon alerts. I think these definitely need
more attention than I gave them though. I left a lot of the `to_chat`s
in place because many of them give information you want to be a little
sticky, or refer back to in order to double check what you just did.

I also added a unit test which flips back and forth a few times to
ensure the ability still works.
This required adding an "instant" flag to the monkeyize/humanize procs
to skip the timers, and idenitified a couple of weird issues.
First point: Humanising a monkey would remove the monkey mutation and
then call humanise again, which would not skip itself because it still
regarded you as being a monkey. I changed the order of operations here
slightly so that it will early return.
Second point: Calling `domutcheck` on `human/consistent` would runtime
because we skip the bit which sets up any mutations in their DNA. This
is a part of changeling transformation, so I just made it return
instantly.

## Why It's Good For The Game

You can use this ability again without getting stuck permanently as a
monkey, or it just deleting itself from your list of abilities for no
reason.
Turning into a monkey with fake outfit pieces on won't turn you into an
abomination.

## Changelog

:cl:
refactor: Changeling's Lesser Form is now one ability instead of two
which keep swapping, which should consistently turn you back and forth
without deleting itself from your action bar.
fix: Hatching from an egg left by a Last Resort headcrab should
correctly grant you Lesser Form in addition to your other abilities.
fix: Turning into a monkey while using the Changeling space suit won't
leave you as a monkey with a weird inflated head.
qol: Using lesser form as a monkey with only one stored DNA profile will
skip asking which profile you want and will simply transform you
immediately into the only option.
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [ArcaneBow7258/CSE528_FPS](https://github.com/ArcaneBow7258/CSE528_FPS)@[ac456356b1...](https://github.com/ArcaneBow7258/CSE528_FPS/commit/ac456356b100ea5ad2799135ba892609d26474fc)
#### Tuesday 2023-02-28 23:13:53 by Alvin Tran

Holy shit I hate VFX

So i kept crashing but i udpated to better unity version and it fixed haha

Reimported all vfx assets
Refactored abiltiy code
Added Poison Cloud Ability

---
## [DataDog/dd-trace-rb](https://github.com/DataDog/dd-trace-rb)@[eeabe537a2...](https://github.com/DataDog/dd-trace-rb/commit/eeabe537a29191ea3aeb3086c9aa8b91c958c0f3)
#### Tuesday 2023-02-28 23:24:07 by Ivo Anjo

Second step of making some sample values optional: make StackRecorder configurable

In the previous commit the `sample_values` struct was introduced, which
abstracted how values are passed to libdatadog away from everywhere
else in the profiler, and centralized this into the `StackRecorder`.

In this commit, I reimplemented the `record_sample` function to,
instead of using a hardcoded position for every value type, rely
on two extra indirections:
* `state->position_for`
* `state->enabled_values_count`

By default (e.g. when all profile types are enabled), this new
strategy behaves exactly as before.

The interesting thing happens when some profile types are disabled
(via the constructor). When profile types are disabled,
the two indirections above are reconfigured: `enabled_values_count`
becomes less than `ALL_VALUE_TYPES_COUNT`, and `position_for` is
updated to account for this as well.

In pratice, the `position_for` array is treated as if it was a
hashmap -- the key is a given profile type, and the value is the
position that libdatadog is expected it to be written to.

Thus, converting a `sample_values` to an array for libdatadog
is as simple as

```c
  metric_values[position_for[CPU_TIME_VALUE_ID]]      = values.cpu_time_ns;
  metric_values[position_for[CPU_SAMPLES_VALUE_ID]]   = values.cpu_samples;
  metric_values[position_for[WALL_TIME_VALUE_ID]]     = values.wall_time_ns;
  metric_values[position_for[ALLOC_SAMPLES_VALUE_ID]] = values.alloc_samples;
```

The trick here, is that when certain profile_types are disabled
their `position_for` is changed, so they are put at the end of the
`metric_values` array.

For instance, when we disable both `CPU_TIME_VALUE` and
`ALLOC_SAMPLES_VALUE` the `position_for` "hashmap" will look something
like

```ruby
{
  CPU_SAMPLES_VALUE_ID: 0,
  WALL_TIME_VALUE_ID: 1,
  CPU_TIME_VALUE_ID: 2,
  ALLOC_SAMPLES_VALUE_ID: 3,
}
```

And thus, given

```ruby
{ 'cpu-time' => 123, 'cpu-samples' => 456, 'wall-time' => 789, 'alloc-samples' => 4242 }
```

We will produce a `metrics_values` array with

```
+-----+-----+-----+------+
| 456 | 789 | 123 | 4242 |
+-----+-----+-----+------+
```

...but we'll tell libdatadog to only use the first 2 positions of
the array, which contain the values for the enabled profile types!

To be honest, this was more boilerplate than I wanted, but I'm happy
that most of the complexity lies in `_native_initialize` around the
creation of `position_for` and the values list for libdatadog, and
everywhere else still looks kinda sane.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[31eabb62f1...](https://github.com/shiptest-ss13/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Tuesday 2023-02-28 23:41:44 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [memfault/memfault-docs](https://github.com/memfault/memfault-docs)@[645a9005c0...](https://github.com/memfault/memfault-docs/commit/645a9005c000cf8919f297125374e27bc7eda0d4)
#### Tuesday 2023-02-28 23:47:19 by Noah Pendleton

Add PAT to prettier action

Use a Personal Access Token instead of the built-in
`secrets.GITHUB_TOKEN`. This is very annoying, but pushes from the
`secrets.GITHUB_TOKEN` _do not_ trigger a workflow run:

https://github.com/orgs/community/discussions/25702#discussioncomment-3248819

I assume some weird way to avoid eternally-looping workflows?

Which results in PR's never getting the updated status if the prettier
action pushes a commit, and the PR never satifies the merge requirement.

Anyway, using a PAT works around the problem 🤷 . Update the action
version too since I'm in here.

You can see it in "action" (😅) here:

https://github.com/memfault/memfault-docs/pull/414

NB: I never noticed this because I am obsessive about squash-rebase if
prettier detects any changes.

---

