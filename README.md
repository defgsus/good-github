## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-21](docs/good-messages/2022/2022-10-21.md)


2,285,432 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,285,432 were push events containing 3,390,889 commit messages that amount to 253,759,378 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [elastic/ebpf](https://github.com/elastic/ebpf)@[abe597fffb...](https://github.com/elastic/ebpf/commit/abe597fffb2e7c0e39687db8ebf21f21c694a1af)
#### Friday 2022-10-21 00:07:08 by Rhys Rustad-Elliott

Implement variable-length ringbuf wire format (#159)

* Implement variable-length ringbuf wire format

This commit introduces variable-length fields into the ringbuf wire
format.

Over time, the number of fields in our wire format with a large
theoretical maximum size has grown (pathnames, argv, tty output, etc.).

Every field in the wire format is of a fixed-size. This simplifies
parsing of messages in userspace, but leads to huge memory waste as the
maximum possible buffer size needs to be allocated, even when it's not
used most of the time. For example, PATH_MAX on linux is 4096, but the
pathnames we pass up are going to be a fraction of that size 99% of the
time. Terminal output is an even bigger culprit for this sort of thing,
a 4 KiB buffer is allocated for each tty_write event, even if the data
being written to the tty is just one byte. For a high-frequency tty
write event, this can easily cause us to drop events.

This commit adds a few new structures present at the end of each event
struct that needs to use variable length fields. Fields that are always
of a fixed size (or variable length but so small as to be irrelevant
from a memory-usage perspective, e.g. task->comm) remain as they were
before, in a fixed-size part of the event. Variable length events are
packed into a flexible array member at the end of the event struct and
each are preceeded by a header describing the type of field and size.

An unfortunate necessity of this approach is that we cannot use the
ringbuffer reserve/commit API for events that have variable-length
fields, as we won't know the size of the event in advance. Instead, we
build each event with its variable-length fields in a percpu map, and
then output it using bpf_ringbuf_output. This should result in a small
performance hit as we're introducing an additional memory copy, but
should be made up for in massive memory usage improvements. An
alternative would have been to continue to use the reserve/commit API,
passing up each event in fixed-size chunks, but this would just shift
the extra copy to userspace, and introduce a bunch of complexity there
as we'd need to have reconstruction logic in the Ebpf events library. In
any case, there is no free lunch.

Logic and helpers for adding variable length parameters have been added
to Helpers.h and are fairly well documented. New events that need to use
variable-length fields should add a ebpf_varlen_fields_start struct as
their last member with a name of vl_fields. Variable-length fields can
then be added to the event. For example, in the case of a file delete
event:

        struct ebpf_file_delete_event *event = get_event_buffer();

        // ... Fill in fixed-length fields

        // Variable length fields
        ebpf_vl_fields__init(&event->vl_fields);
        struct ebpf_varlen_field *field;
        size_t size;

        // path
        ADD_VL_FIELD_OR_GOTO_EMIT(event, field, EBPF_VL_FIELD_PATH);
        size = ebpf_resolve_path_to_string(field->data, &p, task);
        ebpf_vl_field__set_size(&event->vl_fields, field, size);

    emit:
        bpf_ringbuf_output(&ringbuf, event, EVENT_SIZE(event), 0);

The emit label is required. The ADD_VL_FIELD_OR_GOTO_EMIT macro will
jump to it if there is no more space remaining in the event buffer
returned from get_event_buffer().

The use of variable-length fields also allows us to get rid of a bit of
cruft. In particular:

- No more PATH_MAX * 2 sized buffers in EbpfEventProto.h that waste
  space and leak an implementation detail of the BPF probes to userspace
- The memset reimplementation to deal with argv has been removed as we
  will now know size of argv in the variable-length parameter header,
  making zeroing out a fixed-size buffer unnecessary

This commit also bumps the ringbuffer size to 4 MiB so that it's larger
than the 2 MiB percpu event buffers.

* Add explanatory comment

* Correct ringbuffer size 64 MiB -> 4 MiB

Co-Authored-By: Michal Stanek <michal.stanek@elastic.co>

* Reduce per-cpu event buffer size to 256 KiB

This still provides 128 KiB of space, which is more than the theoretical
maximum sized event (an exec with maxed out argv), so we can save some
memory with no downside. This should be bumped if larger parameters are
added in the future that could result in an event > 128 KiB.

* Move variable length field utilities to Varlen.h

Co-Authored-By: Mattia Meleleo <mattia.meleleo@elastic.co>

* Fix not using get_event_buffer

Error from rebase

* Remove ADD_VL_PARAM_OR_GOTO_EMIT

Given the caps on argv and tty_out, the maximum theoretical possible
event size is currently ~40 KiB. Given 128 KiB of useable space in the
percpu event buffer, this means we will never run out of space and the
goto emit path will never be hit, making this logic unnecessary for the
time being. If in the future we need to read truly massive fields, this
can be revisited and potentially re-added.

* Error-check bpf_probe_read_kernel_str calls

Co-Authored-By: Michal Stanek <michal.stanek@elastic.co>

* Remove BUFFER_SIZE_HALF logic

Given the low caps on potentially large varlen params (argv, tty_out,
etc.), this bounding is unnecessary. It was back when we were reading
EVENT_BUFFER_SIZE_HALF as the maximum length of a new variable length
param, but doesn't do us anything now.

* Re-Add EVENT_BUFFER_SIZE_HALF bound

Mistake on my part, this is actually required to keep the verifier
happy. Re-add and document well.

Co-authored-by: Michal Stanek <michal.stanek@elastic.co>
Co-authored-by: Mattia Meleleo <mattia.meleleo@elastic.co>

---
## [RonaldKirk443/PriceScraper](https://github.com/RonaldKirk443/PriceScraper)@[d5ade8330d...](https://github.com/RonaldKirk443/PriceScraper/commit/d5ade8330da6bfdff4b7985ad71a59741175e20d)
#### Friday 2022-10-21 00:14:13 by RonaldKirk443

Updated tasks, fuck you Erfan

Thanks to Erfan I now have a couple extra tasks to do and some motivation to continue and finish this project.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e8be775da4...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e8be775da4892a20186105a69bdc8b0832fba1cb)
#### Friday 2022-10-21 00:37:48 by Paxilmaniac

Adds a collection of some kinda random greyscaled, recolorable clothes options (#16961)

* that's a few dmis

* a few sprite changes

* i hate making greyscale configs

* oh the misery

* 2:29 AM

* a few small things

* adds the stuff around more

* amazing work boss, this is why you're the best

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[a2577296e6...](https://github.com/TheBoondock/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Friday 2022-10-21 00:39:55 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[422accbe4e...](https://github.com/TheBoondock/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Friday 2022-10-21 00:39:55 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [daedela/FieryMudMaps](https://github.com/daedela/FieryMudMaps)@[7bd4d293e8...](https://github.com/daedela/FieryMudMaps/commit/7bd4d293e88c2e083b5ae919a714f43afcb89025)
#### Friday 2022-10-21 01:15:21 by daedela

Update The Cartographer.txt

Cartographer and his room and shop:
Ignore all the code stuff, I'm writing it here for quick and easy cut-and-paste and notes to remind myself what I'm doing.
I made a few tiny spelling/grammar/wording changes just to help it flow.  It's a great basic mob and room, well done!

Greater Mielikki Area Map: 

I LOVE this map!!!

1. I fixed some spelling errors, particularly "Mielikki".  Side note, Mielikki is a copywritten goddess from D&D, so we want to make sure we spell it correctly, AND ALSO refer to it as the Village of Mielikki or Town of Mielikki or something else to make it clear we're not talking about the goddess herself.
2. I removed Dheduu because that's supposed to be a hidden city, possibly on another plane of existence (it's coded for astral plane, so Kourrya clearly intended for it to be somewhere else).  I replaced them with the Rocky Tunnels, because it's helpful to know where you just died haha.
3. I added Rhell Forest and connected it to BFT and Twisted Forest.
4. The abbey is formally dedicated to St. George, so I like to call it "Abbey of St. George" where I can.
5. For new players, understanding Anduin is a city is generally helpful.
6. The proper name for the southern continent is South Caelia (whereas Mielikki is on North Caelia
7. I connected Gothra Desert to the Highlands (and fixed the spelling) because they actually do connect.

Farmlands:
I'm going to recolorize the farmlands map.  I think I'm going to make all the paths orange/brown/dark yellow and then all the actual fields green.  I'm going to leave indoor structures plain text.

1. I don't know how to indicate a door up or down...  That's got me stumped.  I like both + and # but I don't know what reads best
2. I replaced W with F so you can use F as a universal symbol
3. For points of interest, I aligned all the : on the same column so you can start all the text on the same column.
4. I changed the name of the abbey to match my preference about it's name
5. Kaaz's formal name is "The Temple of the Kaaz"
6. I think I want to leave the Hive off the list of mapped zones.  I would rather we make reference to the Frakati Reservation and perhaps note in that zone's map 


Kaaz:
The extra spaces between the east-west movement lines help SO MUCH.
1. Obviously, changed the name.
2. Changed the "an iron ring" to be a little less explicit
3. Thank you for not doing the lower level of the temple!
4. Added * to the rooms with the spheres because it might be cool to indicate there's something special there (again, newbie zone so low-hanging fruit is important)

Merchant:
1. I changed the name of the Abbey
2. Changed the C to X for a more universal symbol
3. Added directional arrows to zone boundaries

Abbey:
I'm gonna look at the Abbey and make some suggestions on how the level can be laid out.

---
## [hexagontruth/hexagontruth](https://github.com/hexagontruth/hexagontruth)@[4374ddaa18...](https://github.com/hexagontruth/hexagontruth/commit/4374ddaa185fb1ef84aa717b14fae98855de7d4b)
#### Friday 2022-10-21 02:03:55 by graham

Fall squash

Refactor with shader engine and style improvements

- Add whole-ass Player, Program, and various data/utility classes
- Use player/program structure developed for single-page shader apps
- Using background shader stack and logo shader
  - Feel the background CA could use color, but not sure how to add without changing aesthetic
- Was going to do a video shader taking background and video as input, but too janky
- Video files moved to seperate repo
- Add Express server stuff for serving static local media in dev
- Full-screen single-view tab with dynamic loading
  - Keeps sources in memory so they aren't reloaded
- Concerns about performance on various platforms
  - Works fine on all my shittiest computers, but reported problems from others
    - Particularly iOS/Safari WebKit
    - Fuck you Apple
  - Has not melted any of my devices or caused undue battery drain etc.
- Various style changes and added consistency across classes and content blocks
- Some changes to copy
- Idk probably a bunch of other stuff

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[7c9e26bb85...](https://github.com/Lamella-0587/Skyrat-tg/commit/7c9e26bb85a40ee3f5a570fe4f51df3c4f350ea5)
#### Friday 2022-10-21 02:14:52 by SkyratBot

[MIRROR] Fixes Some Incredulously Fucked Up Recycler Behavior [MDB IGNORE] (#17018)

* Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

* test one

Hey there!

Did you know that if you toss someone into a recycled emagger, that we delete _all_ of that mob's contents? You probably didn't because this shit is broken broken. Like, ow.

That's because we manually moved an item to nullspace, which caused a _slew_ of odd behavior in the Destroy chain for `obj/item` since it moves it to nullspace at a very specific point in time and makes all of it's assumptions on when you move the thing to nullspace. If it's in nullspace before you call qdel, you would shit out the ass with hanging references stuck on the mob (like `w_uniform` pointing to something in nullspace, like the image above).

All fixed now, though.

* I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

* i blanked

my guy hasn't moved for twenty minutes

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* wrong documentation

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Fixes Some Incredulously Fucked Up Recycler Behavior

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[8272749e8c...](https://github.com/justinpryzby/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Friday 2022-10-21 02:46:16 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [SimenB/apollo-server](https://github.com/SimenB/apollo-server)@[9e60e9f5a9...](https://github.com/SimenB/apollo-server/commit/9e60e9f5a90c2a4eb66e8bd761f3c09b80f169cd)
#### Friday 2022-10-21 03:27:28 by Trevor Scheer

Fix bad link to `graphql-js` source code (#7065)

Fixes #5812.

I think linking to a known spot in time is at least an improvement over
the current state.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [mamh-mixed/git-git](https://github.com/mamh-mixed/git-git)@[5beca49a0b...](https://github.com/mamh-mixed/git-git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Friday 2022-10-21 03:27:47 by Ævar Arnfjörð Bjarmason

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
## [NimBlemations/Vs-Joe-Stick](https://github.com/NimBlemations/Vs-Joe-Stick)@[4937f0be7b...](https://github.com/NimBlemations/Vs-Joe-Stick/commit/4937f0be7b6f66da56513c226ecff46acb0564e5)
#### Friday 2022-10-21 03:56:34 by NimBlemations

Fixed the fookin' optimization, but the songs won't play due to FUCKING HAXEFLIXEL ISSUES!!!

FUCK YOU HAXEFLIXEL!!!

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[48533d113c...](https://github.com/newstools/2022-express/commit/48533d113c2b432e2de2adad2bd5b305dbb56d5b)
#### Friday 2022-10-21 05:36:20 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1685672/megan-fox-boyfriend-machine-gun-kelly-blood-drinking-news-latest]

---
## [bra1n/townsquare](https://github.com/bra1n/townsquare)@[974bbb1a0f...](https://github.com/bra1n/townsquare/commit/974bbb1a0f35ab2a3333ba2a28955956e24fd900)
#### Friday 2022-10-21 07:45:10 by Dae Lorant

Updated night order for all roles

Updated night order for all roles to match the order at https://script.bloodontheclocktower.com/data/nightsheet.json

Some noticeable changes:
- Legion was moved much earlier in the order of demons (relevant if a another demon is made in a legion game, you can keep it around and kill it with legion before it kills on a subsequent night)
- Amnesiac was moved much later in night order (a more reasonable place for the most common type of amni abilities)
- Magician was given a night order for N1
- Pixie was given a night order for other nights

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[14c96d05b8...](https://github.com/Striders13/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Friday 2022-10-21 08:12:10 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[99b8d6b494...](https://github.com/Striders13/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Friday 2022-10-21 08:12:10 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [mamh-mixed/psf-black](https://github.com/mamh-mixed/psf-black)@[0019261abc...](https://github.com/mamh-mixed/psf-black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Friday 2022-10-21 09:00:16 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [Parsifal-M/opa](https://github.com/Parsifal-M/opa)@[965301f90e...](https://github.com/Parsifal-M/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Friday 2022-10-21 09:03:02 by Stephan Renatus

ast: support dotted heads (#4660)

This change allows rules to have string prefixes in their heads -- we've
come to call them "ref heads".

String prefixes means that where before, you had

    package a.b.c
    allow = true

you can now have

    package a
    b.c.allow = true

This allows for more concise policies, and different ways to structure
larger rule corpuses.

Backwards-compatibility:

- There are code paths that accept ast.Module structs that don't necessarily
  come from the parser -- so we're backfilling the rule's Head.Reference
  field from the Name when it's not present.
  This is exposed through (Head).Ref() which always returns a Ref.

  This also affects the `opa parse` "pretty" output:

  With x.rego as

    package x
    import future.keywords
    a.b.c.d if true
    e[x] if true

  we get

    $ opa parse x rego
    module
     package
      ref
       data
       "x"
     import
      ref
       future
       "keywords"

     rule
      head
       ref
        a
        "b"
        "c"
        "d"
       true
      body
       expr index=0
        true
     rule
      head
       ref
        e
        x
       true
      body
       expr index=0
        true

  Note that

    Name: e
    Key: x

  becomes

    Reference: e[x]

  in the output above (since that's how we're parsing it, back-compat edge cases aside)

- One special case for backcompat is `p[x] { ... }`:

    rule                    | ref   | key | value | name
    ------------------------+-------+-----+-------+-----
    p[x] { ... }            | p     | x   | nil   | "p"
    p contains x if { ... } | p     | x   | nil   | "p"
    p[x] if { ... }         | p[x]  | nil | true  | ""

  For interpreting a rule, we now have the following procedure:

  1. if it has a Key, it's a multi-value rule; and its Ref defines the set:

     Head{Key: x, Ref: p} ~> p is a set
     ^-- we'd get this from `p contains x if true`
         or `p[x] { true }` (back compat)

  2. if it has a Value, it's a single-value rule; its Ref may contain vars:

     Head{Ref: p.q.r[s], Value: 12} ~> body determines s, `p.q.r.[s]` is 12
     ^-- we'd get this from `p.q.r[s] = 12 { s := "whatever" }`

     Head{Key: x, Ref: p[x], Value: 3} ~> `p[x]` has value 3, `x` is determined
                                          by the rule body
     ^-- we'd get this from `p[x] = 3 if x := 2`
         or `p[x] = 3 { x := 2 }` (back compat)

     Here, the Key isn't used, it's present for backwards compatibility: for ref-
     less rule heads, `p[x] = 3` used to be a partial object: key x, value 3,
     name "p"

- The destinction between complete rules and partial object rules disappears.
  They're both single-value rules now.

- We're now outputting the refs of the rules completely in error messages, as
  it's hard to make sense of "rule r" when there's rule r in package a.b.c and
  rule b.c.r in package a.

Restrictions/next steps:

- Support for ref head rules in the REPL is pretty poor so far. Anything that
  works does so rather accidentally. You should be able to work with policies
  that contain ref heads, but you cannot interactively define them.
  
  This is because before, we'd looked at REPL input like

      p.foo.bar = true

  and noticed that it cannot be a rule, so it's got to be a query. This is no
  longer the case with ref heads.

- Currently vars in Refs are only allowed in the last position. This is expected
 to change in the future.

- Also, for multi-value rules, we can not have a var at all -- so the following
  isn't supported yet:

      p.q.r[s] contains t if { ... }

-----

Most of the work happens when the RuleTree is derived from the ModuleTree -- in
the RuleTree, it doesn't matter if a rule was `p` in `package a.b.c` or `b.c.p`
in `package a`.

As such, the planner and wasm compiler hasn't seen that many adaptations:

- We're putting rules into the ruletree _including_ the var parts, so

  p.q.a = 1
  p.q.[x] = 2 { x := "b" }

  end up in two different leaves:

  p
  `-> q
       `-> a = 1
       `-> [x] = 2`

- When planing a ref, we're checking if a rule tree node's children have
  var keys, and plan "one level higher" accordingly:

  Both sets of rules, p.q.a and p.q[x] will be planned into one function
  (same as before); and accordingly return an object {"a": 1, "b": 2}

- When we don't have vars in the last ref part, we'll end up planning
  the rules separately. This will have an effect on the IR.

  p.q = 1
  p.r = 2

  Before, these would have been one function; now, it's two. As a result,
  in Wasm, some "object insertion" conflicts can become "var assignment
  conflicts", but that's in line with the now-new view of "multi-value"
  and "single-value" rules, not partial {set/obj} vs complete.
* planner: only check ref.GroundPrefix() for optimizations

In a previous commit, we've only mapped

    p.q.r[7]

as p.q.r;  and as such, also need to lookup the ref

    p.q.r[__local0__]

via p.q.r

(I think. Full disclosure: there might be edge cases here that are unaccounted
for, but right now, I'm aiming for making the existing tests green...)


New compiler stage:

In the compiler, we're having a new early rewriting step to ensure that the
RuleTree's keys are comparible. They're ast.Value, but some of them cause us
grief:

- ast.Object cannot be compared structurally; so

      _, ok := map[ast.Value]bool{ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")}): true}[ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")})]

  `ok` will never be true here.

- ast.Ref is a slice type, not hashable, so adding that to the RuleTree would
  cause a runtime panic:

      p[y.z] { y := input }

  is now rewritten to

    p[__local0__] { y := input; __local0__ := y.z }

This required moving the InitLocalVarGen stage up the chain, but as it's still
below ResolveRefs, we should be OK.

As a consequence, we've had to adapt `oracle` to cope with that rewriting:

1. The compiler rewrites rule head refs early because the rule tree expects
   only simple vars, no refs, in rule head refs. So `p[x.y]` becomes
   `p[local] { local = x.y }`
2. The oracle circles in on the node it's finding the definition for based
   on source location, and the logic for doing that depends on unaltered
   modules.

So here, (2.) is relaxed: the logic for building the lookup node stack can
now cope with generated statements that have been appended to the rule bodies.


There is a peculiarity about ref rules and extents:

See the added tests: having a ref rule implies that we get an empty object
in the full extent:

    package p
    foo.bar if false

makes the extent of data.p: {"foo": {}}

This is somewhat odd, but also follows from the behaviour we have right now
with empty modules:

    package p.foo
    bar if false

this also gives data.p the extent {"foo": {}}.

This could be worked around by recording, in the rule tree, when a node was
added because it's an intermediary with no values, but only children.

Signed-off-by: Stephan Renatus <stephan.renatus@gmail.com>

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[2b87e1aff4...](https://github.com/newstools/2022-new-york-post/commit/2b87e1aff4fd1d533172e8443f83d7f7b6a6a15f)
#### Friday 2022-10-21 09:09:42 by Billy Einkamerer

Created Text For URL [nypost.com/2022/10/21/dear-abby-my-girlfriend-keeps-on-calling-me-her-dead-boyfriends-name/]

---
## [igorwulff/magento2](https://github.com/igorwulff/magento2)@[b6fbaeb89a...](https://github.com/igorwulff/magento2/commit/b6fbaeb89a5f14b195b6bb84546db895afcf7a1e)
#### Friday 2022-10-21 09:51:11 by Igor Wulff

Improve performance of DataObject magic calls and addData()

The magic calls from the DataObject are being called over a 100k when there is no block_cache available and depending on the page often thousands of times when all block_cache is available.

The small change for addData() is just included because its a tiny optimization and prevents a bug from happening. When a $value is an array the original call to setData would override the internal $_data array, this is not expected behavior and just setting it directly to $_data is faster anyway.

The other change is in the __call magic method and the _underscore function and the change is quite radical.
Since this method can be called so often, we want to prevent further function calls if possible. Functional calls are normally not that expensive, but will become more expensive if you use this extensively (thousands of even hundred of thousands extra calls):

These are my own benchmarks based on a local environment with opcache and with PROD mode. 

HOMEPAGE transaction
All cache enabled except for FPC (__call is called 975 times): 4.318307ms -> 1.469747ms
All cache enabled except for FPC + Block_html  (__call is called 100379 times): 385.36412ms -> 88.412914ms

PLP transaction:
All cache enabled except for FPC  (__call is called 4628 times): 19.625463ms -> 5.754514ms
All cache enabled except for FPC + Block_html (__call is called 112591 times): 404.84066ms -> 99.390374ms

Now this PR also skips some checks. It assumes if a $method call start with 'g' it will be for 'get' for example, this is done in my PR to get the most optimal performance result but might not be preferred. I also removed an index check with $args[1] for the setter since it isn't used anywhere, but might also be something we would want to change.

---
## [DoggyCraft/MyDog](https://github.com/DoggyCraft/MyDog)@[647bb492f3...](https://github.com/DoggyCraft/MyDog/commit/647bb492f310f38911598e672e4a4a9c0f30b8c0)
#### Friday 2022-10-21 10:25:36 by StrangeOne101

Pets no longer teleport on unload when sitting

# Changes
* Pets will no longer teleport to the player when they are sitting and the chunk they are in unloads.

# Reason for change
Randomly, all your pets will teleport to you when running in the nether - even if sitting. This happens when the previous chunk unloaded and so now all your lovely pets are now on fire, burning, dying, and may about to try swimming in lava. I've lost pets before to this, and I'm sick of roaming the nether without being able to leave my pets behind. This should fix that change.

Thanks for reading. :)

---
## [GNOME/glib](https://github.com/GNOME/glib)@[b8e1ecdd6b...](https://github.com/GNOME/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Friday 2022-10-21 12:45:36 by Michael Catanzaro

Automatically disable cast checks when building with optimization

Cast checks are slow. We seem to have some rough consensus that they are
important for debug builds, but not for release builds. Problem is, very
few apps define G_DISABLE_CAST_CHECKS for release builds. Worse, it's
undocumented, so there's no way apps could even be expected to know
about it.

We can get the right default is almost all situations by making this
depend on the __OPTIMIZE__ preprocessor definition. This is a GCC-specific
thing, although Clang supports it too. If the compiler does not define
__OPTIMIZE__, then this commit does no harm: you can still use
G_DISABLE_CAST_CHECKS as before. When checking __OPTIMIZE__, we are
supposed to ensure our code has the same behavior as it would if we do
not, which will be true except in case the check fails (which is
programmer error).

Downside: this will not automatically do the right thing with -Og,
because __OPTIMIZE__ is always defined to 1. We don't want to disable
cast checks automatically if using -O0 or -Og. There's no way to
automatically fix this, but we can create an escape hatch by allowing
you to define G_DISABLE_CAST_CHECKS=0 to force-enable cast checks. In
practice, I don't think this matters much because -Og kinda failed:
GCC's man page says it should be a superior debugging experience to -O0,
but it optimizes variables away so it's definitely not.

Another downside: this is bad if you really *do* want cast checks in
release builds. The same solution applies: define
G_DISABLE_CAST_CHECKS=0 and you'll get your cast checks.

---
## [nspcc-dev/neo-go](https://github.com/nspcc-dev/neo-go)@[b27e6918bd...](https://github.com/nspcc-dev/neo-go/commit/b27e6918bd969cc07f738ba96c7f246f44ede319)
#### Friday 2022-10-21 14:00:12 by Roman Khimov

Makefile: complicate version detection script

We've declared that we are using semantic versioning. We also want to use `git
describe` to make version strings for us because it's very convenient for
development builds (tagged versions are way simpler). The problem is that the
default `git describe` behavior is not semver compliant. If the most recent
tag is v0.99.2 then it'll generate something like '0.99.2-131-g8dc5b385',
which according to semver is a development version _before_ 0.99.2. While it's
obviously a version _after_ 0.99.2.

That's the one and only reason we have vX.Y.Z-pre tags in our repo. We set
them right after the release according to the release process and that gives
us some '0.99.3-pre-131-g8dc5b385' versions we're all used to. But these tags
are ugly as hell and they clutter up our repo over time.

So there is this idea that we can do patch version increment dynamically.
Making '0.99.2-131-g8dc5b385' be '0.99.3-pre-131-g8dc5b385' without any *-pre
tags. This patch implements this. It's ugly as hell as well, but at least
that's an ugliness somewhere inside our Makefile and not directly visible in
our tags. If we're to do this we can then greatly simplify our release process
(and even allow for CHANGELOG patches to be merged normally).

I know this can be done with awk in somewhat easier way, but no, I'm not into
awk, sorry.

---
## [repinger/leenux](https://github.com/repinger/leenux)@[d276507c2d...](https://github.com/repinger/leenux/commit/d276507c2d512b43245a31da200266311670a9fa)
#### Friday 2022-10-21 14:50:25 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [facebook/litho](https://github.com/facebook/litho)@[7a4babbc77...](https://github.com/facebook/litho/commit/7a4babbc77ae9be2f0fee55c96b30861e94e985c)
#### Friday 2022-10-21 16:20:39 by Fabio Carballo

Migrate two sample apps mount specs to mountable components

Summary:
As per request of apowolny, I attempted to migrate two of our mount specs to mountable components. Here goes my feedback:

**What was really easy:**
- It was really simple to get in into the concept/pattern of "MountableComponent" vs "SimpleMountable". The pattern is intuitive and simple enough with the methods to create content/mount/unmount.
- The pattern of passing a `null` `Style` into the mountables as we have in other examples felt nice.

**Things I felt more difficult:**
- It was hard to me to understand what to put as a result of the `Measure`.
  1. I looked up to other examples we had, and just attempted to use the `MeasureResult.withEqualDimensions` and see if it works (which it did). But honestly, maybe the naming is not super clear to me, or maybe it is not even the best way to do this and I just had luck.
- Making use of the `DynamicValue`:
   1. I believe there is still no documentation on this; I was able to do it because I still had an idea of the RFC and after some grepping. **However**, this API really feels like some dark magic, as we set the callbacks to the class type of the mountable (which we don't have any reference to). It works, but I think it is a pattern hard to "get into" and maybe even prone to some mistakes.
  2. I also couldn't use the syntatic sugar of `time.bindTo(0L, SimpleClockView::time)` and didn't really understand why. I feel clients of the API may get stuck here as I did.

Ideas:
- I wonder if we can infer the View/Drawable type (?)
- Could we potentially have a default `onMeasure` that just respects the width/height specs in a standard way? This would leave the override just for special cases.

Reviewed By: apowolny

Differential Revision: D40412675

fbshipit-source-id: 56d2d7d93f03082ab59b901f9c8740f000320914

---
## [maaaaaaaaaatt/Maaaaaaaaaatt.net](https://github.com/maaaaaaaaaatt/Maaaaaaaaaatt.net)@[292b042f24...](https://github.com/maaaaaaaaaatt/Maaaaaaaaaatt.net/commit/292b042f2466b13709013ce7fe97e85455242fee)
#### Friday 2022-10-21 16:37:41 by Matthew Flores

45: axing that old google doc CV, finally

remember when you got caught making edits in the middle of the night? yeah me too

---
## [asus-sdm660-devs/android_kernel_asus_sdm660](https://github.com/asus-sdm660-devs/android_kernel_asus_sdm660)@[68783b52a7...](https://github.com/asus-sdm660-devs/android_kernel_asus_sdm660/commit/68783b52a71b8df36e452078bd14d8208396a284)
#### Friday 2022-10-21 17:17:34 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [McFuzzykins/RPG2](https://github.com/McFuzzykins/RPG2)@[15d952e116...](https://github.com/McFuzzykins/RPG2/commit/15d952e1161d6814675208f7e28a6838cb67d324)
#### Friday 2022-10-21 17:47:59 by McFuzzykins

It Works

I am God's Nintendog that he remembered about

---
## [avar/git](https://github.com/avar/git)@[062d71cd52...](https://github.com/avar/git/commit/062d71cd525e74ed0bdebc20aa161713417d27c9)
#### Friday 2022-10-21 17:49:45 by Ævar Arnfjörð Bjarmason

submodule: make it a built-in, remove git-submodule.sh

Replace the "git-submodule.sh" script with a built-in
"builtin/submodule.c. For" now this new command is only a dumb
dispatcher that uses run-command.c to invoke "git submodule--helper",
just as "git-submodule.sh" used to do.

This is obviously not ideal, and we should eventually follow-up and
merge the "builtin/submodule--helper.c" code into
"builtin/submodule.c". Doing it this way makes it easy to review that
this new C implementation isn't doing anything more clever than the
old shellscript implementation.

This is a large win for performance, we're now more than 4x as fast as
before in terms of the fixed cost of invoking any "git submodule"
command[1]:

	$ git hyperfine -L rev HEAD~1,HEAD -s 'make CFLAGS=-O3' './git --exec-path=$PWD submodule foreach "echo \$name"'
	Benchmark 1: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1
	  Time (mean ± σ):      42.2 ms ±   0.4 ms    [User: 34.9 ms, System: 9.1 ms]
	  Range (min … max):    41.3 ms …  43.2 ms    70 runs

	Benchmark 2: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD
	  Time (mean ± σ):       9.7 ms ±   0.1 ms    [User: 7.6 ms, System: 2.2 ms]
	  Range (min … max):     9.5 ms …  10.3 ms    282 runs

	Summary
	  './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD' ran
	    4.33 ± 0.07 times faster than './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1'

We're taking pains here to faithfully reproduce existing
"git-submodule.sh" behavior related to "--" handling, even when that
behavior is stupid. We'll fix in subsequent commits, but let's first
faithfully reproduce it.

One exception is the change in the behavior of the exit code
stand-alone "-h" and "--" yield, see the altered tests. Returning 129
instead of 0 and 1 for "-h" and "--" respectively is a concession to
basic sanity.

The pattern of using "define BUILTIN_" macros here isn't needed for
now, but as we'll move code out of "builtin/submodule--helper.c" we'll
want to re-use these strings. See 8757b35d443 (commit-graph: define
common usage with a macro, 2021-08-23) and 1e91d3faf6c (reflog: move
"usage" variables and use macros, 2022-03-17) for prior art using this
pattern.

The "(argc < 2 || !strcmp(argv[1], "-h"))" path at the top of
cmd_submodule__helper() could now be a "(argc < 2)" if not for
t0012-help.sh (which invokes all built-ins manually with "-h"). Let's
leave it for now, eventually we'll consolidate the two.

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [eldarbr/silver-funicular](https://github.com/eldarbr/silver-funicular)@[c4b9454b17...](https://github.com/eldarbr/silver-funicular/commit/c4b9454b179567d03b046d3bd18989d004a928c0)
#### Friday 2022-10-21 18:10:18 by NailN03

Update lr_ladidie_3.3.cpp

Fuck my life, can't save that, girl
Don't tell me you could save that shit

---
## [reach-sh/reach-lang](https://github.com/reach-sh/reach-lang)@[369d4e327b...](https://github.com/reach-sh/reach-lang/commit/369d4e327bd8239529425b44102f6070d5808589)
#### Friday 2022-10-21 18:23:50 by William G Hatch

change isDataVariant test to use different length keys

Proving to myself and everybody that I was wrong and temporarily crazy when I wrote that I made a mistake in my implementation of this feature the first time.  I don't remember what I did that made me think there was a bug here.  But now I can rest assured in the knowledge of my own infallibility when writing code, and can view with skepticism any claims from myself or others that there is ever any problem with my code at any time for any reason.

---
## [DMMaster636/FNF-HD-Psych-Engine-Port-Source-Code](https://github.com/DMMaster636/FNF-HD-Psych-Engine-Port-Source-Code)@[fefc9fb14f...](https://github.com/DMMaster636/FNF-HD-Psych-Engine-Port-Source-Code/commit/fefc9fb14f3cacf373ed2b1bd5feb0ad08d1bb2f)
#### Friday 2022-10-21 18:35:01 by DMMaster636

animate doesn't like the HD stuff

first of all, i had to copy and manually type in 2 of the frames from stressed spooky cus it thought it was a copy of the anim from the normal one, even tho it's clearly not???
then it just kinda copied one anim instead of putting it together, even tho it was the same
so yeah
fuck you AA 22

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0513e7d6a1...](https://github.com/TaleStation/TaleStation/commit/0513e7d6a1d1d8d1d89030d919ed16c82317d3df)
#### Friday 2022-10-21 18:43:41 by TaleStationBot

[MIRROR] [MDB IGNORE] Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#2745)

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [STALKER-SS13/STALKER-13](https://github.com/STALKER-SS13/STALKER-13)@[1ad74ef093...](https://github.com/STALKER-SS13/STALKER-13/commit/1ad74ef0939fc81f96ea3e4485a0b82406a6d22e)
#### Friday 2022-10-21 19:14:27 by ProtivogaSpriter

FUCK YOU FUCK YOU

FUCK YOU!!!!

this literally comments out the entire renegades job file

---
## [STALKER-SS13/STALKER-13](https://github.com/STALKER-SS13/STALKER-13)@[fa6e6ee157...](https://github.com/STALKER-SS13/STALKER-13/commit/fa6e6ee1574cec2561d35f89969beaa595f11094)
#### Friday 2022-10-21 19:14:27 by emoats18

Merge pull request #214 from ProtivogaSpriter/srptotr

FUCK YOU FUCK YOU

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[06090b9269...](https://github.com/cockroachdb/cockroach/commit/06090b92696bfc4c84f457ac204c4bf17f780170)
#### Friday 2022-10-21 19:34:25 by craig[bot]

Merge #86603 #87166 #87535 #87870 #88078 #88111

86603: changefeedccl: redact user from confluent schema registry r=jayshrivastava a=jayshrivastava

This change redacts the confluent schema registry key
from the jobs table.

Fixes: https://github.com/cockroachdb/cockroach/issues/85902

Release justification: This change is important because
it prevents a user's secret key from being store in the DB.
The footprint of this change is small as it only touches
a specific changefeed option - confluent schema registry.

Release note (enterprise change): Previously, SHOW CHANGEFEED
JOBS would reveal confluent schema registry user information,
including a user's secret key. This change makes this info
redacted, meaning it will not be stored in CockroachDB
internal tables at all.

87166: kvserver: shorten `raft.process.handleready.latency` help text r=tbg a=erikgrinaker

We should get confirmation in #87112 that this size is below the limit before merging this.

---

AWS managed Prometheus rejects `raft.process.handleready.latency`
because the help text is too long. The text is currently 1123 bytes, so
the limit is suspected to be 1024 bytes. This patch reduces the size of
this help text to 938 bytes.

Resolves #87112.

Release justification: bug fixes and low-risk updates to new functionality

Release note (ops change): Reduced the length of the
`raft.process.handleready.latency` metric help text to avoid it being
rejected by certain Prometheus services.

87535: sql: support `#typeHints` greater than `#placeholders` for prepare stmt r=rafiss a=ZhouXing19

Previous, we only support pgwire prepare stmt with the number of typehints equal or smaller than the number of the placeholders in the query. E.g. the following usage are not supported:

```
Parse {"Name": "s2", "Query": "select $1", "ParameterOIDs":[1043, 1043, 1043]}
```
Where there is 1 placeholder in the query, but 3 type hints.

This commit is to allow mismatching #typeHints and #placeholders. The former can be larger than the latter now.

This feature is needed for [CRDB's support for Hasura GraphQL Engine](https://github.com/hasura/graphql-engine/issues/8839#issuecomment-1236691642).

Release justification: Low risk, high benefit changes to existing functionality

Release note: For pgwire-level prepare statements, add support for the case where the number of the type hints is greater than the number of placeholders in the given query.

87870: kvnemesis: reset op.Result r=erikgrinaker a=tbg

We found out (in #87814) after a wild goose chase that op.Result was not
reset, so unless operations were cognizant of this fact and
always fully repopulated the Result field, weird failures
could result from txn retries.

Reset the field.

Release note: None


88078: ui: update filter labels r=maryliag a=maryliag

Update filter label from "App" to "Application Name" and "Username" to "User Name" on SQL Activity and Insights pages.

Fixes #87960

<img width="467" alt="Screen Shot 2022-09-16 at 6 40 51 PM" src="https://user-images.githubusercontent.com/1017486/190827281-36a9c6df-3e16-4689-bcae-6649b1c2ff86.png">


Release note (ui change): Update filter labels from "App" to "Application Name" and from "Username" to "User Name" on SQL Activity and Insights pages.

88111: sql: fix `pg_get_viewdef` for materialized views r=rafiss a=knz

Fixes #88109.

Release note (bug fix): The function `pg_catalog.pg_get_viewdef` now works properly for materialized views.

Co-authored-by: Jayant Shrivastava <jayants@cockroachlabs.com>
Co-authored-by: Erik Grinaker <grinaker@cockroachlabs.com>
Co-authored-by: Jane Xing <zhouxing@uchicago.edu>
Co-authored-by: Tobias Grieger <tobias.b.grieger@gmail.com>
Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>

---
## [hashicorp/terraform-plugin-framework](https://github.com/hashicorp/terraform-plugin-framework)@[4dfa83cd64...](https://github.com/hashicorp/terraform-plugin-framework/commit/4dfa83cd64fcd29506dd2a950825cba18a28705a)
#### Friday 2022-10-21 20:11:07 by Brian Flad

types: Deprecate Null, Unknown, and Value fields

Reference: https://github.com/hashicorp/terraform-plugin-framework/issues/447

When the framework type system was originally being developed, the value types were introduced with exported fields which also served as the internal details of whether a value was null, unknown, or a known value of a friendlier Go type. It was known that there was the potential for issues, but the simplified developer experience seemed to outweigh the potential for developer issues. Fast forward a few months, this decision appears to have two consequences that the framework maintainers hear about across various forums.

One issue is that the value types directly expose their internal implementation details and support the three states of a Terraform type value: being null, unknown, or a known value. Only one state should ever be set, but provider developers can make a value that is any combination of those states. This makes the framework behavior potentially indeterminate from the provider developer perspective whether, for example, a null AND unknown value becomes null OR unknown as it works its way through the framework.

```go
type ThingResourceModel struct{
  Computed types.String `tfsdk:"computed"`
}

func (r ThingResource) Create(ctx context.Context, req resource.CreateResource, resp *resource.CreateResponse) {
  var data ThingResourceModel

  resp.Diagnostics.Append(req.Plan.Get(ctx, &data)...)

  tflog.Trace(ctx, "Data Values", map[string]any{
    // Unknown value: types.String{Null: false, Unknown: true, Value: ""}
    "computed": plan.Computed,
  })

  // Maybe some external API responses here, but showing hardcoded updates for
  // brevity. This will make the value invalid by enabling Null without
  // disabling Unknown.
  data.Computed.Null = true

  tflog.Trace(ctx, "Data Values", map[string]any{
    // Invalid value: types.String{Null: true, Unknown: true, Value: ""}
    "computed": data.Computed,
  })

  // The invalid value will be either null or unknown, depending on the
  // type implementation. If unknown, Terraform will error, since unknown
  // values are never allowed in state.
  resp.Diagnostics.Append(resp.State.Set(ctx, &data)...)
}
```

Another issue is that the default (zero-value) state for an "unset" value type turns into a known value, which is confusing since these values explicitly support being null. This causes Terraform errors which would surface to practitioners (especially when untested) that provider developers then have to troubleshoot the error message containing Terraform's type system details, potentially discover the reason why it is happening by looking at the framework type source code, then figure out a workable solution. It's not intuitive.

```go
type ThingResourceModel struct{
  // let's assume this is left unconfigured (null in config and plan)
  Optional types.String `tfsdk:"optional"`
}

func (r ThingResource) Create(ctx context.Context, req resource.CreateResource, resp *resource.CreateResponse) {
  // Providers can opt to use a single variable that is updated based on an
  // external response, however that logic can be more difficult sometimes,
  // so it can be easier to split them. Showing the split way to exemplify
  // the "unset" problem.
  var plan, state ThingResourceModel

  resp.Diagnostics.Append(req.Plan.Get(ctx, &plan)...)

  tflog.Trace(ctx, "Plan Values", map[string]any{
    // Null value: types.String{Null: true, Unknown: false, Value: ""}
    "optional": plan.Optional,
  })

  // Maybe some external API responses here, but intentionally not
  // doing any state.Optional setting, which might happen if the
  // external response for that data was null for example.

  tflog.Trace(ctx, "State Values", map[string]any{
    // Zero-value: types.String{Null: false, Unknown: false, Value: ""}
    "optional": state.Optional,
  })

  // The state zero-value will later cause Terraform to error, such as:
  // Error: Provider produced inconsistent result after apply
  // ... expected cty.NullVal(cty.String), got cty.StringVal("")
  // Since the plan value said it would be null.
  resp.Diagnostics.Append(resp.State.Set(ctx, &state)...)
}
```

This deprecation of the fields in preference of functions and methods aims to unexport the internal details and treat the value types as immutable once they are created. When provider developers switch over to the new model, any errant changes to the deprecated exported fields will have no effect. A future version will remove the exported fields entirely and switch the zero-value implementation of these values to being null, instead of a known zero-value of the underlying type.

Update CHANGELOG for #502

types: Note that valueState constants will be exported in the future so they can be used by external types

types: collection types

---
## [git/git](https://github.com/git/git)@[d3775de074...](https://github.com/git/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Friday 2022-10-21 21:19:57 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [peff/git](https://github.com/peff/git)@[28c19ba512...](https://github.com/peff/git/commit/28c19ba512d420504d8c33e7491849b1d0724d66)
#### Friday 2022-10-21 21:26:22 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[8dfbd39520...](https://github.com/peff/git/commit/8dfbd39520e582215e7eaa3eb0c163854a0844d1)
#### Friday 2022-10-21 21:26:22 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [shintaro-iwasaki/FBGEMM](https://github.com/shintaro-iwasaki/FBGEMM)@[5d4aabc498...](https://github.com/shintaro-iwasaki/FBGEMM/commit/5d4aabc4989f47dad3b1651bf9b3c8d1158685ff)
#### Friday 2022-10-21 22:26:46 by siwasaki

Enhance FBGEMM nightly CI with cuDNN fix (#1407)

Summary:
This PR updates FBGEMM nightly CI to make it more usable and maintainable by using GitHub Actions more effectively, with a cuDNN installation fix. I want to make them happen together so that the "fix" really fixes an issue.

## 1. Fix the cuDNN installation issue in FBGEMM nightly CI

We used `conda-forge` to install cuDNN, but this unintentionally added CUDA 10 dependency to the FBGEMM nightly package, breaking installation steps that rely on FBGEMM nightly.

To address this issue, we install cuDNN separately in the CI script so that it can coexist with CUDA 11.7, which is used by PyTorch-CUDA nightly.

## 2. Implement label-triggered wheel tests during a PR review

Previously, we needed to apply a hack to trigger wheel-related tests before merging the PR, which is neither comprehensive nor efficient.

To address this issue, this PR adds optional wheel-related tests.  Now a PR with a label such as `"test_wheel_nightly"`, `"test_wheel_prerelease"`, and `"test_wheel_release"` enables the corresponding wheel-related tests.  We don't need to modify YML files again, so we can easily run these tests.  Please trigger these tests for suspicious PRs that touch the installation logic.  Note that binaries won't be pushed to PYPI if this method is used.

## 3. Remove duplicated logic across YML files

Nightly/release/cpu/gpu wheel scripts shared most in common, but the logic were scattered across different files, which significantly lowered maintainability.

To address this issue, this PR collects all the wheel-related test logic into a single file (`build_wheel.yml`) and makes the callers (e.g., scheduled nightly trigger or per-PR tests using labels) pass flags to control the flow (e.g., per-PR tests do not push the wheel binary to PYPI).  No duplication improves maintainability.

<img width="1269" alt="Screen Shot 2022-10-21 at 9 58 56 AM" src="https://user-images.githubusercontent.com/15073003/197249555-bb00f3b1-9bc9-46f1-8fea-7874460723f6.png">

## 4. Support handy wheel-related tests on a local machine

Previously, the core wheel-related build/test logics were embedded into GitHub workflow files (`*.yml`) mixed with AWS-specific commands, so it was very tedious to test the nightly logic on a local machine, lowering the developer efficiency.

To address this issue, this PR extracts core scripts from GitHub workflow files and makes them standalone so that the developer can try wheel-build locally (i.e., without access to AWS machine). It uses conda to create a virtual software environment, so it should be handy enough in many cases though this is not as robust as a container-based solution.

```sh
# For example, check prerelease PyTorch (pytorch-test package) locally.
git clone https://github.com/pytorch/FBGEMM.git
cd FBGEMM
git submodule update --init --recursive
bash .github/scripts/build_wheel.bash -p 3.10 -c 11.7 -v -P pytorch-test -o fbgemm_gpu_test
bash .github/scripts/test_wheel.bash -p 3.10 -c 11.7 -v -P pytorch-test -w fbgemm_gpu/dist/fbgemm_gpu_test-2022.10.20-cp310-cp310-manylinux1_x86_64.whl
git clone https://github.com/pytorch/torchrec.git
cd torchrec
git submodule update --init --recursive
bash ../.github/scripts/test_torchrec.bash -o torchrec_nightly -p 3.10 -c 11.7 -v -P pytorch-test -w ../fbgemm_gpu/dist/fbgemm_gpu_test-2022.10.20-cp310-cp310-manylinux1_x86_64.whl
```

## 5. [Temporary] Add TorchRec integration test

TorchRec is one of our most important users, but we didn't test TorchRec integration in the nightly CI, so the changes in FBGEMM sometimes surprised the TorchRec developers.

To address this issue, though it is temporary, but this PR adds a TorchRec integration test before pushing a binary to PYPI so that we can make sure that FBGEMM works with TorchRec.  However, now broken TorchRec can break FBGEMM-nightly; we will investigate a more sustainable solution that makes everyone happy.

## 6. Better interface to manually trigger the CI

It looks nice. I love to operate the release management in an automated way as much as possible to reduce human errors at the very last minute. In the future, we can add more options if needed.

<img width="844" alt="Screen Shot 2022-10-21 at 5 53 03 AM" src="https://user-images.githubusercontent.com/15073003/197240190-e808df23-795a-451d-a7d9-ec1c43c68e92.png">

Pull Request resolved: https://github.com/pytorch/FBGEMM/pull/1407

Differential Revision: D40597700

Pulled By: shintaro-iwasaki

fbshipit-source-id: 150121661d58097164a589d506eeb842ee7ea905

---

