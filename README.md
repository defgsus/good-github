## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-26](docs/good-messages/2022/2022-08-26.md)


1,981,822 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,981,822 were push events containing 2,970,219 commit messages that amount to 224,127,043 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [silnith-org/pgp-keys-filler](https://github.com/silnith-org/pgp-keys-filler)@[d87ff0fcbc...](https://github.com/silnith-org/pgp-keys-filler/commit/d87ff0fcbc0992d889aa52c945af2953cdbf03f1)
#### Friday 2022-08-26 00:08:09 by silnith

Use "legacy" naming style for JDKs.

Because it's fucking accurate.  Fuck you, Oracle.

---
## [xdroid-oss/xd_frameworks_base](https://github.com/xdroid-oss/xd_frameworks_base)@[d5ec384141...](https://github.com/xdroid-oss/xd_frameworks_base/commit/d5ec384141a71179ae2cc8940206a03d88451df1)
#### Friday 2022-08-26 00:10:12 by Joey Huab

core: Refactor Pixel features

* Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

* Remove P21 experience system feature check

---
## [TheRakeshPurohit/react](https://github.com/TheRakeshPurohit/react)@[b6978bc38f...](https://github.com/TheRakeshPurohit/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2022-08-26 00:49:44 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [karelianpie/coordinape](https://github.com/karelianpie/coordinape)@[2a76043a17...](https://github.com/karelianpie/coordinape/commit/2a76043a17dd06ac4e47e8d2434b5ef9113fe19c)
#### Friday 2022-08-26 01:19:39 by topocount

bugfix: enable FormTokenField to have an empty input (#1277)

One of the major considerations during the FormTokenField (and downstream) refactor was allowing for empty string inputs. This enables for much cleaner UX, since users aren't typing "around" a zero
and in my opinion, makes us look like we know what we're doing as devs. There are other hacks that could make the UX better than the incumbent, but why not just make it behave correctly and be done with it?

Co-authored-by: crabsinger <83605543+crabsinger@users.noreply.github.com>
Co-authored-by: zashton <17747090+zashton@users.noreply.github.com>

---
## [scala/docs.scala-lang](https://github.com/scala/docs.scala-lang)@[8cb441957d...](https://github.com/scala/docs.scala-lang/commit/8cb441957d96d6de21a7e3ed38d8156df4a20883)
#### Friday 2022-08-26 01:30:24 by Martijn Hoekstra

Remove joke

When you're trying to understand something, jokes are never funny

---
## [dm1940k/RMarkdown-Web-Testing](https://github.com/dm1940k/RMarkdown-Web-Testing)@[254c11b715...](https://github.com/dm1940k/RMarkdown-Web-Testing/commit/254c11b71538e03849879549b1658d1c739da0a0)
#### Friday 2022-08-26 05:04:51 by dm1940k

Adjusted html so backing is always the right height (hopefully), and made charsheet text a little smaller to better suit small screens. Seem to have fucked up the hover highlight in the process of tinkering with a dropdown sub menu, and can't figure out git pulls and shit this late at night.

---
## [jtigues/Ironmon-Tracker](https://github.com/jtigues/Ironmon-Tracker)@[761fe4b0f1...](https://github.com/jtigues/Ironmon-Tracker/commit/761fe4b0f171d6fca47aa72e196aa42680da7279)
#### Friday 2022-08-26 05:13:06 by Zac Elsik

Some randomized moves still showed "1" power

This correctly captures all weird power but actually no-power moves:
Guillotine (12)
Horn Drill (32)
SonicBoom (49)
Low Kick (67)
Counter (68)
Seismic Toss (69)
Dragon Rage (82)
Fissure (90)
Night Shade (101)
Bide (117)
Psywave (149)
Super Fang (162)
Flail (175)
Reversal (179)
Return (216)
Present (217)
Frustration (218)
Magnitude (222)
Hidden Power (237)
Mirror Coat (243)
Endeavor (283)
Sheer Cold (329)

---
## [MyceliaStargaze/Numerical-Analysis](https://github.com/MyceliaStargaze/Numerical-Analysis)@[b6277490b3...](https://github.com/MyceliaStargaze/Numerical-Analysis/commit/b6277490b37edb0fe16a650e90ce72d5d5be2e05)
#### Friday 2022-08-26 05:16:51 by Mycelia Stargaze

Create 16 –– Computing integrals using recursion and using Simpson's rule 

it's like those little yellow fellas huh, but for math. shoutout to Francois sensei for being a dope as fuck teacher and crushing my ego to dust with Real Analysis. some dude talked about proving the number line a couple days ago and i has a full blown panic flashback. thank god i didnt become alcoholic and overdose on painkillers back then and stuck to smonking dat donk everyday instead. good times

---
## [ahamlinman/xt](https://github.com/ahamlinman/xt)@[0f52796f40...](https://github.com/ahamlinman/xt/commit/0f52796f4051d7ba6dd2b3db8d0d35844fb997a9)
#### Friday 2022-08-26 05:40:22 by Alex Hamlin

Raise SIGPIPE manually on broken pipe errors

I'm a big fan of how Go handles SIGPIPE errors: if the error happens on
stdout or stderr, die with SIGPIPE to work like a typical command line
utility; otherwise, ignore the signal to avoid dying on closed network
connections.

When I went to study how this was implemented, I assumed that the Go
runtime had some special way to link a received SIGPIPE to a write on a
particular file descriptor (which in retrospect seems a bit ridiculous).
In reality, the runtime basically ignores SIGPIPE (at least as long as
no C code installs a handler for it), and when the os.File.Write method
encounters an EPIPE it calls into a special runtime method that fiddles
with the necessary handler settings and manually raises SIGPIPE.

Honestly, it never even crossed my mind that xt could raise its own
signals, even though in theory it's something I know Unix programs are
capable of. I think this is a much cleaner way to achieve the goal of
looking like a "normal" Unix utility without maintaining and (if I'm
being honest, not actually) testing separate Unix and non-Unix error
handling paths.

---
## [dcaballe/llvm-project](https://github.com/dcaballe/llvm-project)@[e17cae076c...](https://github.com/dcaballe/llvm-project/commit/e17cae076c4727b99017927c3e8746db5bec6db7)
#### Friday 2022-08-26 06:15:40 by Walter Erquinigo

[trace][intel pt] Fix per-psb packet decoding

The per-PSB packet decoding logic was wrong because it was assuming that pt_insn_get_sync_offset was being udpated after every PSB. Silly me, that is not true. It returns the offset of the PSB packet after invoking pt_insn_sync_forward regardless of how many PSBs are visited later. Instead, I'm now following the approach described in https://github.com/intel/libipt/blob/master/doc/howto_libipt.md#parallel-decode for parallel decoding, which is basically what we need.

A nasty error that happened because of this is that when we had two PSBs (A and B), the following was happening

1. PSB A was processed all the way up to the end of the trace, which includes PSB B.
2. PSB B was then processed until the end of the trace.

The instructions emitted by step 2. were also emitted as part of step 1. so our trace had duplicated chunks. This problem becomes worse when you many PSBs.

As part of making sure this diff is correct, I added some other features that are very useful.

- Added a "synchronization point" event to the TraceCursor, so we can inspect when PSBs are emitted.
- Removed the single-thread decoder. Now the per-cpu decoder and single-thread decoder use the same code paths.
- Use the query decoder to fetch PSBs and timestamps. It turns out that the pt_insn_sync_forward of the instruction decoder can move past several PSBs (this means that we could skip some TSCs). On the other hand, the pt_query_sync_forward method doesn't skip PSBs, so we can get more accurate sync events and timing information.
- Turned LibiptDecoder into PSBBlockDecoder, which decodes single PSB blocks. It is the fundamental processing unit for decoding.
- Added many comments, asserts and improved error handling for clarity.
- Improved DecodeSystemWideTraceForThread so that a TSC is emitted always before a cpu change event. This was a bug that was annoying me before.
- SplitTraceInContinuousExecutions and FindLowestTSCInTrace are now using the query decoder, which can identify precisely each PSB along with their TSCs.
- Added an "only-events" option to the trace dumper to inspect only events.

I did extensive testing and I think we should have an in-house testing CI. The LLVM buildbots are not capable of supporting testing post-mortem traces of hundreds of megabytes. I'll leave that for later, but at least for now the current tests were able to catch most of the issues I encountered when doing this task.

A sample output of a program that I was single stepping is the following. You can see that only one PSB is emitted even though stepping happened!

```
thread #1: tid = 3578223
    0: (event) trace synchronization point [offset = 0x0xef0]
  a.out`main + 20 at main.cpp:29:20
    1: 0x0000000000402479    leaq   -0x1210(%rbp), %rax
    2: (event) software disabled tracing
    3: 0x0000000000402480    movq   %rax, %rdi
    4: (event) software disabled tracing
    5: (event) software disabled tracing
    6: 0x0000000000402483    callq  0x403bd4                  ; std::vector<int, std::allocator<int>>::vector at stl_vector.h:391:7
    7: (event) software disabled tracing
  a.out`std::vector<int, std::allocator<int>>::vector() at stl_vector.h:391:7
    8: 0x0000000000403bd4    pushq  %rbp
    9: (event) software disabled tracing
    10: 0x0000000000403bd5    movq   %rsp, %rbp
    11: (event) software disabled tracing
```

This is another trace of a long program with a few PSBs.
```
(lldb) thread trace dump instructions -E -f                                                                                                         thread #1: tid = 3603082
    0: (event) trace synchronization point [offset = 0x0x80]
    47417: (event) software disabled tracing
    129231: (event) trace synchronization point [offset = 0x0x800]
    146747: (event) software disabled tracing
    246076: (event) software disabled tracing
    259068: (event) trace synchronization point [offset = 0x0xf78]
    259276: (event) software disabled tracing
    259278: (event) software disabled tracing
    no more data
```

Differential Revision: https://reviews.llvm.org/D131630

---
## [dfr/podman](https://github.com/dfr/podman)@[09ef6fc66c...](https://github.com/dfr/podman/commit/09ef6fc66cac44dec94c29cd7a1a53f70831446d)
#### Friday 2022-08-26 07:01:39 by Ed Santiago

podman generate kube - add actual tests

This exposed a nasty bug in our system-test setup: Ubuntu (runc)
was writing a scratch containers.conf file, and setting CONTAINERS_CONF
to point to it. This was well-intentionedly introduced in #10199 as
part of our long sad history of not testing runc. What I did not
understand at that time is that CONTAINERS_CONF is **dangerous**:
it does not mean "I will read standard containers.conf and then
override", it means "I will **IGNORE** standard containers.conf
and use only the settings in this file"! So on Ubuntu we were
losing all the default settings: capabilities, sysctls, all.

Yes, this is documented in containers.conf(5) but it is such
a huge violation of POLA that I need to repeat it.

In #14972, as yet another attempt to fix our runc crisis, I
introduced a new runc-override mechanism: create a custom
/etc/containers/containers.conf when OCI_RUNTIME=runc.
Unlike the CONTAINERS_CONF envariable, the /etc file
actually means what you think it means: "read the default
file first, then override with the /etc file contents".
I.e., we get the desired defaults. But I didn't remember
this helpers.bash workaround, so our runc testing has
actually been flawed: we have not been testing with
the system containers.conf. This commit removes the
no-longer-needed and never-actually-wanted workaround,
and by virtue of testing the cap-drops in kube generate,
we add a regression test to make sure this never happens
again.

It's a little scary that we haven't been testing capabilities.

Also scary: this PR requires python, for converting yaml to json.
I think that should be safe: python3 'import yaml' and 'json'
works fine on a RHEL8.7 VM from 1minutetip.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[ed3a05f111...](https://github.com/Bcadren/crawl/commit/ed3a05f11175cc29afafb1c089b66559ee42ebe5)
#### Friday 2022-08-26 07:23:27 by Lucien

Additions to ebering's curse rework. More specificity on which races have bones for the "bones ache" message. Chance of rot restored, with much higher rot amounts (Necro miscast rot was soo low), now it's Severity/3 + random2(Severity) instead of just 1-3. This might be a little too high, we'll see with testing. Chance of a summoned elemental restored. (Reaper, Rot Elemental, Pain Elemental, Shadow) [Reaper == Death Elemental, Shadow == Weak Darkness elemental]. Reaper guaranteed at highest severity unless it's against a low level player (killed a greater mummy in an early ossuary or something), player step down to forced lesser elemental or Shadow at lv. 21 and 12 respectively. Pain elementals never come for those immune to pain. Suspect stat rot (1-5 points) is probably still the worst death curse. Commit also explicitly changes Shadows from Undead to Elemental (kinda think mainline should follow and move to non-living, matches flavour).

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[04a409949d...](https://github.com/Bcadren/crawl/commit/04a409949dd54ffb817bb6a766406d10f00e2e74)
#### Friday 2022-08-26 08:25:48 by Edgar A. Bering IV

Decouple Zot trap effects from miscasts and revise

The Zot trap effect code was very old, wedged into the miscast system
for convenient access to certain things the old miscast class handled.

The effect list was long and had a highly variable impact and threat
level.

This commit re-implements zot trap effects directly in traps.cc with a
much pruned list. The new table of effects is below, with 2/3rds of the
weight spent on "evil magic" and 1/3rd on "hostile summoning" as loose
categories.

Evil magic (total weight 16):
- lose 1 + r2a(5,2) stats (weight 4)
- 7000 + r2a(13000,2) contam (weight 4)
- 2 - 5 turn paralysis (weight 1)
- mp drain to 0 wt (weight 2)
- petrification wt (weight 1)
- random2(20) turns of magic vulnerability (weight 4)

Summoning (total weight 8):
- word of recall 2 - 4 foes (weight 3)
- durably summoned greater demon (weight 3)
- malign gateway (weight 1)
- twister (weight 1)

These effects will need further tuning (and possible re-weighting).

BcadrenCrawl: Paralysis replaced with sleep, since Paralysis is
mostly removed and petrification was already used.

---
## [ringods/pulumi-hugo](https://github.com/ringods/pulumi-hugo)@[57060a7a96...](https://github.com/ringods/pulumi-hugo/commit/57060a7a96837ce68cf5593c2b37a8daf488a01a)
#### Friday 2022-08-26 08:43:50 by Joe Duffy

Improve download discoverability (#1811)

* Improve download discoverability

We know users have trouble simply downloading Pulumi. This used to be
very easy, but over time, as we optimized the Getting Started flows, it
got pushed further and further away from the core user experience.

I don't know about you, but the first thing I care about when I'm
trying out a new open source tool is downloading it!

This change aims to do two things:

1. Make downloading a more prominent CTA.

2. Improve the download page so it's less noisy and more focused.

This entails:

* Adding a DOWNLOAD secondary CTA on the homepage.

* Summarizing the recommended download options at the top of the
  download page, very clearly, and without any preamble. This
  hopefully tells you instantly what you wanted for the 80% case.

* I exerted some artistic freedom which I'd love feedback on. The
  recommended options were our Official Brew Tap for macOS, curl
  command for Linux, and MSI Installer for Windows. Peers to those
  are simple download links for the binaries, as that's the simplest
  possible thing, which today is actually the hardest thing to find.
  Notably for Windows, I thought of using Chocolatey or Winget, but
  I don't perceive that either is "the default" for Windows users.
  Winget is the future but it isn't supported pre-Win11, which I have
  to assume most users aren't on yet. MSI has been around since the
  dinosaurs, so it seems like the safest choice to promote.

* Moving the list of download options for each operating system
  underneath a collapsable accordion list, which is collapsed by
  default, and clearly labeling it as "Other"; as in, if the heading
  didn't work for you, here are some other options.

* A few other wordsmithing tweaks to make the page a little more
  streamlined and to flow better.

This is absolutely NOT the final destination for any of this,
however, I am hopeful it will be a simple incremental improvement
that moves the needle on key metrics. We'll watch it in the weeks
to come and course correct as needed -- as well as continuing to
think about ways we can improve all of this overall!

One note: This depends on a new secondary hero button style that
isn't yet merged in the upstream Hugo component library. Assuming
I did that correctly (a big if!) I'll need to rev the go.mod file
after it merges. See: https://github.com/pulumi/theme/pull/159.

* Apply suggestions from code review

Co-authored-by: susan evans <susan.ra.evans@gmail.com>

* Fix up some styling

* Update themes/default/layouts/index.html

Co-authored-by: susan evans <susan.ra.evans@gmail.com>

* Use new theme/style

Co-authored-by: susan evans <susan.ra.evans@gmail.com>
Co-authored-by: zchase <zachary@pulumi.com>

---
## [opal/opal](https://github.com/opal/opal)@[d83d7400f4...](https://github.com/opal/opal/commit/d83d7400f49f8e255de9e10cf3fc277d195ef85b)
#### Friday 2022-08-26 08:44:13 by hmdne

Optimize $eqeq and $eqeqeq calls.

```
 Comparison of the Asciidoctor (a real-life Opal application) compile and run:
                  Compile time: 5.999 -> 5.987 (change: -0.19%)
                      Run time: 0.271 -> 0.268 (change: -1.11%)
                   Bundle size: 4784558 -> 4766408 (change: -0.38%)
          Minified bundle size: 1027822 -> 1015882 (change: -1.16%)
            Mangled & minified: 716587 -> 702347 (change: -1.99%)
```

Similarly to how we optimize $rb_lt and friends to create a shortpath
for those, let's optimize $eqeq,$eqeqeq as well. This certainly brings
an incompatibility if we monkey patch those methods for Number/String,
but with the previous commit we made it reliable to return `nil` from
== and === which is in my opinion much more important.

---
## [queercpu/script](https://github.com/queercpu/script)@[50e919b71a...](https://github.com/queercpu/script/commit/50e919b71a42a49d793fbe9b8999e42c7dd10e9f)
#### Friday 2022-08-26 09:04:25 by home.cpu

i played a game with ep3 script. i went over everything i had... and I forced myself to say what is essential, what is neccessary.. i said... what is it about? and i just wrote all these sentences what its about.. example.. its bout a girl struggling with her faith. its about being in love with viva and wanting her badly. its about getting in trouble. its about balbla... i wrote a ton down until i got ideas.. then i simplified the story... by cutting out everything not necessary.. rebuilt on paper with the cold warm hot stickers... once i established a bunch of clear blocks / chapters... i built a new ESSENCECHRISTI file... and created new blocks... i went thru all files and yanked any text that fit into the new box collection. I dont know how many chapter/blocks total... i will check now... but i just finished doing a cleanup pass on it. the guts still need cleaning but its gettign clearer now how I can finish this

---
## [Lulalaby/MikuSharp](https://github.com/Lulalaby/MikuSharp)@[094ef83009...](https://github.com/Lulalaby/MikuSharp/commit/094ef8300945bc9d67476f8dad2c529e370b169d)
#### Friday 2022-08-26 10:15:24 by Lala Sabathil

Slash Rewrite

Moderation: invite management
- Allow mods to enable or disable invites in case of raids
Update readme with new instructions how to use miku
clean up attributes and convert to ac attr
Remove prefix stuff
Bump MikuSharp to 4.0.0
Convert to file-scoped namespace
Remove Actions from dm
Cleanup derpy weeb
remove outdated jokes
switch nsfw stuff back to cnext and use mention prefix
Pull out database name to config
Minimize http client bullshit
Add backup sql data
remove breaking chars from playlists
Add news channel add
Bump package, switch to release
Upgrade timespan of 25 sec to 30 bcs of interactions
clean uppppp :airplane:
Add playlist autocomplete
Add json ignore to db conn string
rename autocompleteprovider class to *providers
Simplify get opts
make bilibili and nicovideo great again
Fix queue database operations
move console write to logger log<level>
kill info messages
Reimplement top.gg
add submodule nnn
add spotify & apple music support
Add translator project

Co-Authored-By: BloodDragooner <33168706+blooddragooner@users.noreply.github.com>
Co-Authored-By: Mira <mira@aitsys.dev>
Co-Authored-By: Nyuw~ <nyuw@aitsys.dev>

---
## [avar/git](https://github.com/avar/git)@[5beca49a0b...](https://github.com/avar/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Friday 2022-08-26 10:15:29 by Ævar Arnfjörð Bjarmason

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
## [myzael/HOI4-ULTRA-Project](https://github.com/myzael/HOI4-ULTRA-Project)@[31b5b6cb9b...](https://github.com/myzael/HOI4-ULTRA-Project/commit/31b5b6cb9bb628e42f0b9e88665228d5b6b5c0c0)
#### Friday 2022-08-26 10:24:17 by T3rm1dor

Big changes to soviet NF tree

- Removed Cg modifiers in five year plans but made PE gives +5 cg more so initially there is no change. The other cg changes is remove the extra 5 on third year plan but to compensate we will achieve a higher yield is 2% cg reduction and no cg bonus from the collectivization effort. This is probably a sligth buff, but considering the propaganda campaing run for 2 years and that the current +5cg debuff from 3rd year plan can be consider a noob trap as you are only making mils so I'll say it is an improvement.
- On the air tree, I have make most focus that improve red airforce 5 weeks instead of three. Also, I've added an extra -10% efficiency to red airforce but made intensify air pilot training give 10% efficiency while giving less bonuses and not beibg exclusive of intensify aircraft production, with both this focus and the modern air war taking 49 days and can't be taken beforre barb . So now while at war it takes 3 months to fix air mission efficiency, which isn't that much of an issue but should compete a bit with army buffs. It isn't that big of a nerf, but it should make getting those green airs a bit harder to get early on.
- Army changes is making penal battalions improve MP recovery rate like an extra tech and make for the motherland spirit require order 227, which is now moved to desperate measures.
- Red fleet initial focuses are cheaper do getting the initial dockyard decision is more viable.
- Focuses under collectivist science now take 35 days again
- Molotov and Stalin line no longer mutually exclusive but each take 35 days. Molotov line isn't that great to begin with but if a player considers that the opportunity cost is worth it they should go for it.
- On ideas: Soviet land shock recovered the attack debuff
- Propaganda military buffs have overall be nerfed. Metal campaing now gives 4 extra steel and 4 extra aluminium bc the campaing was useless before. The partisan campaing no longer stop enemy strategic redeployment but instead give better combat bonuses.

---
## [rporres/sretoolbox](https://github.com/rporres/sretoolbox)@[5fd9aa9104...](https://github.com/rporres/sretoolbox/commit/5fd9aa91044a2c710befb8225f18eb406e3598a4)
#### Friday 2022-08-26 10:30:28 by Rafa Porres Molina

Content-Type based equality for version 2 images

The Docker Image Manifest V 2, Schema 2 spec states that header should
be used to determine the kind of image that it is returned, a
multi-architecture image (aka "fat" image) that returns a manifest list
or a simple image (returns a manifest). The OCI spec is not as clear but
it also mentions the header as the way to distinguish images since
`mediaType` is not mandatory.

This patch adds support for comparations via the `Content-Type` header
for both Docker and OCI images.

Tests have been added for all the equality cases. Manifests have been
taken from real-life examples when available or from the spec examples.
A new dependency (`requests-mock`) has been added as it wasn't possible
to mock `requests.get` directly using MagicMock as it is a default in
the `_request_get` method signature. Anyway, writing tests using
`requests-mock` has proven to be a very pleasant experience.

`Pipenv.lock has been regenerated due to the addition of the new
dependency.

Signed-off-by: Rafa Porres Molina <rporresm@redhat.com>

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[468ac2c008...](https://github.com/majestrate/loki-network/commit/468ac2c0082aa67f1a641acd6f2217397012c677)
#### Friday 2022-08-26 11:51:02 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [Prajyot-Parab/cluster-api-provider-aws](https://github.com/Prajyot-Parab/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/Prajyot-Parab/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Friday 2022-08-26 12:05:34 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [codemascot/php-src](https://github.com/codemascot/php-src)@[128768a450...](https://github.com/codemascot/php-src/commit/128768a4503c8bc5c6ccf564061f9dc8b307f57f)
#### Friday 2022-08-26 12:37:53 by Alex Dowad

Adjust number of error markers emitted for truncated UTF-8 code units

In 04e59c916f, I amended the UTF-8 conversion code, so that when given
invalid input, it would emit a number of errors markers harmonizing
with the WHATWG's specification of the standard UTF-8 decoding
algorithm. (Which, gentle reader of commit logs, you can find online
at https://encoding.spec.whatwg.org/#utf-8-decoder.) However, the code
in 04e59c916f was faulty in the case that a truncated UTF-8 code unit
starts with 0xF1.

Then, in dc1ba61d09, when making a small refactoring to a different
part of the UTF-8 conversion code, I inexplicably broke part of the
working code, causing the same fault which was already present with
truncated UTF-8 code units starting with 0xF1 to also occur with
0xF2 and 0xF3 as well. I don't remember what inane thoughts I was
thinking when I pulled off this feat of utter mental confusion.

None of these cases were covered by unit tests, by the way.

Thankfully, my trusty fuzzer picked up on this when testing the
new implementation of mb_parse_str (since the legacy UTF-8
conversion filter did not suffer from the same problem, and I was
fuzzing to find any differences in behavior between the old and
new implementations).

Fortuitously, the fuzzer also picked up another issue which was
present in 04e59c916f. I was emitting only one error marker for
truncated code units starting with 0xE0 or 0xED, in cases where
the WHATWG standard indicates two should be emitted. Examples
are 0xE0 0x9F <END OF STRING> or 0xED 0xA0 <END OF STRING>.

Code units starting with 0xE0-0xED should have 3 bytes. If the
first byte is 0xE0, the second MUST be 0xA0 or greater. (Otherwise,
the codepoint could have fit in a two-byte code unit.) And if the
first byte is 0xED, the second MUST be 0x9F or less. According to
the WHATWG algorithm, step 4, if the second byte is outside the
legal range, then the decoder should emit an error... AND
reprocess the out-of-range byte. The reprocessing will then
cause another error. That's why the decoder should indicate two
errors and not one.

---
## [loot/oblivion](https://github.com/loot/oblivion)@[2ec24072b1...](https://github.com/loot/oblivion/commit/2ec24072b19a4a5f48818aaf72bc0522b9bfc741)
#### Friday 2022-08-26 13:45:51 by MacSplody

Remove message

 - Compared in xEdit against any vampire mods I could find.
 - No direct conflicts, would have to be tested in game to confirm.
 - Vampire Revolution, Unholy Darkness, Vampire Hunting, Blood is Everything.
 - Dahyka's Vanilla Spells and Vampirism Improved, StarX Vanilla Vampires Revised.
 - Nekhanimals Awesome Vampire Mod, LTD-Vampire Overhaul, Scorns Vampirism.
 - Lithians Nature Of The Beast Mod Beta, Terran Vampires.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[9dafc33c14...](https://github.com/pytorch/pytorch/commit/9dafc33c14156de4580a57bba868ae623a0cd44c)
#### Friday 2022-08-26 15:13:58 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`. 

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading). 

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.


### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)
  
  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)
  
  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>



[ghstack-poisoned]

---
## [factorialco/factorial-dotfiles](https://github.com/factorialco/factorial-dotfiles)@[277b8a2c09...](https://github.com/factorialco/factorial-dotfiles/commit/277b8a2c0904e13000f5a6ea713bd92d2f32fb48)
#### Friday 2022-08-26 15:27:49 by Pau Ramon Revilla

Disable snippets (#16)

This one is controversial and I will understand if you don't want to
merge it (I will branch if that's the case).

I hate snippets. I never use them and they get in my way. Maybe they are
wrongly configured, but the amount of times that I get snippets when I
don't want them is just a waste of time.

Examples:
  - Sometimes I want to move from `{}` to `do/end` and when I place the
    cursor on `{` and type `do<Enter>` I automatically get an annoying
    `end` that I have to delete imediately.
  - Sometimes I want to press `<Enter>` after a `{` and it will add
    ruby block parameters for no reason.

Do you use them? How do you workaround things getting in the middle when
you don't want them? It screws up my muscle memory.

---
## [ng-rgb/DIPs](https://github.com/ng-rgb/DIPs)@[821a3ce8b8...](https://github.com/ng-rgb/DIPs/commit/821a3ce8b8b2153867f020a658f7eec7f8ad5e9d)
#### Friday 2022-08-26 15:32:55 by N.G

Create DIP-23.md

---
DIP: DIP-23
Title: CRYPTOMURALS - Street art hunting
Status: Draft
Themes: Social, Art & Beauty, Community Involvement, Public Goods.
Tags: Software, Communications, Others.
Authors: 0xnats@proton.me j.caraballose@gmail.com cryptomurals@gmail.com manu@doingud.com sanchit@doingud.com 
Resources Required: Development of the street art hunt platform by DoinGud, Production of 3 murals in Bogotá by ELAR,GAVILÁN & TONRA, Graffiti tour guides for 4 days, operations support. 
Discussion: [Cryptomurals - street art hunt](https://forum.devcon.org/t/cryptomurals-street-art-hunt/1040/8)
---

-----Summary of Proposal-----
__Street art as public good - Devcon 6 Graffiti Tour__

-----Abstract-----
__Exclusive graffiti tour for Devcon6 attendees including a digital experience as a “Street Art Hunting” that rewards them with a memorial NFT of Devcon 6 promoting muralism heritage as a public good.__

-----Motivation & Rationale-----
__Bogotá is well known worldwide for its street art, at Cryptomurals we (A group of muralist & Ethereum enthusiasts) believe in street art as a public good, we want to keep the record of the layers of murals that has been painted on the same wall to stock them on the Ethereum blockchain and make it accessible to anyone as a public good.__

__Cryptomurals aims to be a public gallery in the form of an archive that allows anyone to see the history of the best spots & murals worldwide, we call it “The wallchain”, this will be a collaborative process to keep it updated thanks to our international network of street art festivals & high quality muralists.__

__We propose an exclusive experience for Devcon attendees to discover best murals in downtown with graffiti guides that will guide them to unlock the Devcon6 memorial NFT for free.__

-----Implementation-----
__This will be the first Cryptomurals hunt experience thanks to a partnership with DoinGud(https://doingud.com/) and the support of EthColombia(https://www.instagram.com/eth_colombia/) community. __
__Attendees will be invited to create a unique ID linked to their Eth wallets and use the Street art hunt platform during the Graffiti tour. They will be able to unlock the 3 murals that will populate the Colombian map puzzle.__

__Shortly: 3 murals + 3 geolocated spots + 3 artists = 1 Cryptomurals = Free Devcon 6 memorial NFT.__

__Timeline:__
__August: Start the production if the murals in bogotá & creation of the NFT__
__September: Strat the development of the platform with DoinGud__
__October: Implementation of the graffitti tour & street art hunt during Devcon 6.__

__This will be a free NFT that we create in two stages:__

__1st STAGE - PRODUCTION:__
__- We are producing the first 3 cryptomurals within the graffiti tour path thanks to the support of the EthColombia Community to preserve it on the Ethereum blockchain as a cultural heritage to create the first layer of “the Wallchain”.__

__- Develop the Street art hunting platform with the DoinGud team.__

__2nd STAGE - IMPLEMENTATION:__

__- Promotion of the graffiti tour before and during Devcon.__
__- Get subscribers on a free guided graffiti tour during Devcon [& Devcon week if possible]__
__- Implement the Street art hunting platform for people to be able to complete the map with the 3 cryptomurals of the Colombian map.__
__- Airdrop 3000 NFTs to anyone who has collected the 3 pieces of the puzzle.__

__EXTRA STAGE: UNLOCKABLE CONTENT__
__- Allow unlockable content to be implemented like NFT ticketing for side events or swags for participants of the street art hunt__

-----Operational Requirements & Ownership-----

__1. Actions required to implement the proposal at Devcon__
__- Wall art digital design by our 3 Cryptomurals artists.__
__- Cryptomurals artists are painting the 3 murals in geolocalized spots.__
__- The 3 geolocated spots are integrated at the Graffiti Tour.__
__- Design the “street art hunt” user flow for the digital experience.__
__- Develop the “street art hunt” platform powered by DoinGud to complete the map and be eligible for the Devcon 6 memorial NFT airdrop.__
__- Design and production of: team identification swag and unlockable content for participants.__ 
__- Promotion of Street Art Hunting experience powered by Cryptomurals & Doingud as an official Devcon 6 community event.__
__- Subscription form by QR code & mailing list.__
__- Graffiti tours & street art hunt implementation on the 11th through 14th October.__
__- Possibility to implement the experience on Devcon Week from the 7th to 16th October.__

__2. Responsible for the proposal to be implemented effectively__

__Joanna from Cryptomurals, Manu & Sanchi from DoinGud__

__3. Other projects could this proposal be integrated with__
__The platform could join other proposals for:
__- Unlockable content for ticketing on side events like the closing party proposed by [Shrine House](https://forum.devcon.org/t/devcon-vi-bogota-colombia-closing-party-by-shrine-house/1169)__
__- Presence at the [Chiva chill zone](https://forum.devcon.org/t/dev-roots-an-opportunity-to-show-who-we-are/394/19) with visuals of the memorial NFT and a QR code for people to sign up to the graffiti tours__

-----Links & Additional Information-----

_Cryptomurals was born at the EthGlobal Web3Jam Hackathon on November 2021 and it got on the finalist, you can check our showcase here:  (https://showcase.ethglobal.com/web3jam/cryptomurals)__

__We've already secured a partnership with DoinGud(https://doingud.com/), which will allow us to implement this Proof of Concept and develop this further among other Eth community events__

---
## [wincent/command-t](https://github.com/wincent/command-t)@[148e54a6c1...](https://github.com/wincent/command-t/commit/148e54a6c1941beaaf940ff703dc2bff511b6def)
#### Friday 2022-08-26 16:40:49 by Greg Hurrell

feat: continue adding to Lua port

Yeah, this is a horrible mixed-bag commit. Just showing that we can
compile multiple translation units in a single invocation (may want to
refactor the Makefile to do that a little more traditionally, to be
honest; compile each source individually, then link... but then again,
this is simple and the project is tiny so speed is not a concern).

---
## [howieyoo/oiio](https://github.com/howieyoo/oiio)@[069f079eb5...](https://github.com/howieyoo/oiio/commit/069f079eb5dc0f6ef23b1d2afec8c6abd8ec2ebb)
#### Friday 2022-08-26 16:51:48 by Larry Gritz

Rename src/dds.imageio/squish/simd.h -> squish-simd.h (#3424)

This tiny change is a quality-of-life fix for me, addressing the fact
that there are two different simd.h files in our code base. I never
would have done that on purpose, but one of them is part of the
imported "squish" source code that we use for dds encoding.

For years I've been frustrated that reflexively typing `CMD-P simd.h`
in the editor has a 50/50 chance of pulling in this file, when in fact
there is literally a 100% chance of my wanting
src/include/OpenImageIO/simd.h.

So finally put my editing brain out of its misery by renaming the file
that I never want to edit.

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Friday 2022-08-26 17:16:40 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [Logg-y/the-frozen-north](https://github.com/Logg-y/the-frozen-north)@[40c8b30834...](https://github.com/Logg-y/the-frozen-north/commit/40c8b3083478ec7119904a9670946d07e60ed8df)
#### Friday 2022-08-26 17:41:24 by Logg-y

Beholder and formians, plus misc fixes

Added a new task and bounty given by the Seer in Lith My'athar. You might want to be quite high level (11 or 12) for this one, though.
Increased beholder bite damage from 2d4 to 2d6.
Increased beholder Strength from 11 to 14.
If you are below level 11, the Seer now comments that trying to stop the Valsharess might be harder until you are more experienced. She doesn't stop you trying, though.
Added dialogue to the Seer to turn in the Hive Mother quest.
Mischa now uses Remove Disease on nearby diseased friendlies when out of combat. She's a very helpful soul and will do her best to cure all those in need.
Added an escape lever to Layenne's Tomb so it is no longer possible to get stuck if someone else opened the locked door and you logged out inside.
Fixed Ferdinand's two tasks not appearing in the quest log after logging out and back in.
Fix towards ferrymasters scamming money and not putting passengers on their boat.
Adjusted the Mummy of the Damned - it's now behind a door at the other end of the Warrens. The old door still offers a faster way out once it's dead, though.

---
## [sweatylobster/musings](https://github.com/sweatylobster/musings)@[1b1efaea9d...](https://github.com/sweatylobster/musings/commit/1b1efaea9dd08fd5f445549af32577cba481b9ba)
#### Friday 2022-08-26 18:42:36 by Max de Hoyos

MGSV thoughts, Language and Scent, the new orientation of the project

MGSV thoughts need organization. The gz.md file can be used for
analyzing the use of particular dates for Extra Ops in Ground Zeroes.
The mgsv.md file has to do with Biblical and Oedipal motifs of
Venom Snake as a king/ruler. I'd like to add thoughts on fathering,
like the way that Venom Snake tells Miller "See? Kid's a natural."

Language and Scent is a reading of Baudelaire.
I think it's somewhere in between phenomenology and semiotics.
The only poem I'm drawing from at the moment is IV. CORRESPONDANCES.
I obviously have more to research.
It was inspired while reading Chapter 2 of Eco's Kant and the
Platypus, but can't seem to remember what. I'll determine this later.

This essay is going to play a role in a project that's been brewing in
my mind for a few months.
I'm concerned with the ontology of AI -- what sort of thing can it be?
Many popular conceptions of AI don't appreciate that it is merely
statistical, merely algorithmic. Deep learning also uses algorithms to
shape the output of neural networks whose structures can be entirely described by
mathematics. In other words, the being of an AI seems to be
arithmetical, and therefore, purely representational. Even the term
quantum computer seems to be cheating a bit. Is the output of a quantum
computer traceable in the same way as that typical computer is?

In any case, I started by saying that AI doesn't have a Kantian imagination.
Because there is no manifold of intuition or sense impressions that a machine
can be aware of, this problem must be overcome by selecting labeled data.
Even unsupervised learning organizes the data along certain axes.
In the famous iris dataset, the length and width of the sepal and petal
are distinguished, for example. Can we say that the machine really
understands these components spatially, or geometrically?
A machine would not be limited to a three-dimensional understanding,
whereas we have a prejudice to limit our ratios to two-term ratios.
It takes creativity to graph two-argument functions, for example.
We can see this in VPD charts. But back to the question of whether the
machine understands measurements geometrically, and whether this is of
fundamental importance to its
We experience space in a non-measured way.
We are often wrong about the lengths of objects in the units of
extension that we've used our whole lives. The intuition of space has no
particular alliance to the arithmetical mode of being. The arithmetical
is merely applicable.
I think the Dedekind essay will necessarily tackle this question,
of whether the geometrical precedes the arithmetical, or vice-versa, in
the form of where the notion of continuity is to be found: in arithmetic
or in geometry. I simply can't make sense of which is prior, or stage a
discussion to determine which must, by the argument, be 'prior' -- and
with respect to inaugurated 'continuity' -- a term which has no exegetic
meaning for me yet.

So AI seems to be a purely arithmetical.
Every sense impression which a human has must have aa
corresponding machinic representation. Monitors must display pixels,
refresh at certain rates...
schemas are not inborn, or latent, but learned. Fast.ai's creator,
Jeremy Howard, in Practical Deep Learning for Coders, showcases a paper
in which a deep learning model shows the features which it has learned
to recognize. This reminded me of schemas, and I think it's worth asking
the question whether this is a fair comparison, and in what way they
differ. For schemas like 'four' and 'dog' (is this a schema?)
So I'm going to have to critically investigate Kantian schemas, and see
whether AI feature-engineering, or a deep-learning model's ability to
detect features on its own, is in any way comparable to the notion of
Kantian schemas. I'll also have to investigate the literature on Kantian
schemas, and see what shortcomings the definition has. I think I recall
some dissatisfactions with its provisional character, but idk.

Is this something that the mind can be? Certainly, the
mind can't be any of machines it produces it produces in the real world,
though the mathematical nature of the AI is identical with some
fundamental part of man. I have to critically read both Dedekind's
"Theory of Numbers", where he introduces the notion of continuity,
and Husserl's "Origin of Geometry" for a future essay, to determine
something on this question.

---
## [ThakaRashard/film1](https://github.com/ThakaRashard/film1)@[43fc719b3d...](https://github.com/ThakaRashard/film1/commit/43fc719b3d5f172db3269df388a231750578f9c3)
#### Friday 2022-08-26 18:46:39 by ThakaRashard

  [UNKLE - Psyence Fiction (full album)](https://www.youtube.com/watch?v=ojYI5XUlMV0) [UNKLE - Psyence Fiction (full album)](https://www.youtube.com/watch?v=ojYI5XUlMV0)

  ## SUBURBAN_WIFEY_NiGHTMARE
  [KASHDOLL ROBBED IN LA!!!](https://www.youtube.com/watch?v=6s4slL3_jtI)
  # Dear_HAYAT
  ## Sartu_got_robbed
  <img src="https://raw.githubusercontent.com/ThakaRashard/bubblegumpop/gh-pages/sort/Screenshot%202022-08-01%202.30.18%20AM.png">

  [Please watch this video, you can feel her terror.](https://www.youtube.com/watch?v=6s4slL3_jtI) As we both know her parents were murdered during that 80s criminal ass regime in [Dire-Dawa](https://en.wikipedia.org/wiki/Dire_Dawa), earlier this week on the phone she left me inspired to look at the [RealEstate_iN_DiRE_DAWA](https://jiji.com.et/houses-apartments-for-sale). And I feel so helpless shes raped and sodomized to the point I often dont recognize her and Im going mad with lonelyness. As you know we are well known in Alpharetta, Hollywood and Venice's telepath communites as a fully telekinetic Tantric couple thats separated by prostitution. People in hollywood think because she is posted on the internet shes not kidnapped. I work for JPL still and I was taken away from my job because all my women got kidnapped. Including Muna, that derlic ass Cracker SEVER_MSK has ruined her, she is so fucking whitewashed and the children get no contact with me they have all caught so much BLACK_ENTERTAiNMENT_NETWORK_DiCK they dont look the same after all the molestation. Can you talk to DAnielle_Mushonga for us DPSS_iS_CLEARLY_HUMAN_TRAFFiCKiNG_WiTH_DFACS
  [Please watch this video, you can feel her terror.](https://www.youtube.com/watch?v=6s4slL3_jtI)
  <img src="https://images.genius.com/a41ee0150f3ce869e2b2546dc569e23c.1000x333x1.jpg">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/Libbd7BCBHE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
## [georgzoeller/stable-diffusion-webui](https://github.com/georgzoeller/stable-diffusion-webui)@[4f8dd02ccb...](https://github.com/georgzoeller/stable-diffusion-webui/commit/4f8dd02ccb69f5e457226531a82f54fa4dfe97ea)
#### Friday 2022-08-26 19:08:16 by Georg Zoeller

Adding .png metadata 

This may open the option to read data from images dragged into the tool later.  Activated with --save_metadata

Properties (example output from imagemagic 'identify -verbose' command:
    SD:cfg_scale: 7.5
    SD:GFPGAN: False
    SD:height: 512
    SD:normalize_prompt_weights: True
    SD:prompt: a beautiful matte painting of a cottage on a magical fantasy island, unreal engine, barometric projection, rectilinear
    SD:seed: 247624793
    SD:steps: 50
    SD:width: 512

---
## [danhhz/materialize](https://github.com/danhhz/materialize)@[305082a6a9...](https://github.com/danhhz/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Friday 2022-08-26 19:31:29 by Daniel Harrison

persist: commit state updates to durable storage incrementally

Before, there was pressure to keep the size of state down, because it
was rewritten entirely on each command application. In particular, this
created a tension in compaction tuning between being aggressive about
fewer batches (smaller state) and compacting small batches lazily
(smaller write amplification).

Writing state updates as incremental diffs means that size of a
Consensus writes for each command is independent of the total size of
state. We should be able leverage this to make the entire
`WriteHandle::compare_and_append_batch` latency constant w.r.t. the size
of state and thus independent of compaction. This lets us tune
compaction entirely for where we want to be in its more intrinsic
tradeoff between read, write, and space amplification.

(NB: This commit doesn't quite get us to constant latencies, there's
some elbow grease left. I've proven concretely that it can get down to
`O(log(num state batches))`, but that included some hacks that didn't
make this PR. This would be lovely followup work once we get a chance.)

As persist metadata changes over time, we make its versions (each
identified by a [SeqNo]) durable in two ways:
- `rollups`: Periodic copies of the entirety of [State], written to
  [Blob].
- `diffs`: Incremental [StateDiff]s, written to [Consensus]. The
following invariants are maintained at all times:
- A shard is initialized iff there is at least one version of it in
  Consensus.
- The first version of state is written to `SeqNo(1)`. Each successive
  state version is assigned its predecessor's SeqNo +1.
- `current`: The latest version of state. By definition, the largest
  SeqNo present in Consensus.
- As state changes over time, we keep a range of consecutive versions
  available. These are periodically `truncated` to prune old versions
  that are no longer necessary.
- `earliest`: The first version of state that it is possible to
  reconstruct.
  - Invariant: `earliest <= current.seqno_since()` (we don't garbage
    collect versions still being used by some reader).
  - Invariant: `earliest` is always the smallest Seqno present in
    Consensus.
    - This doesn't have to be true, but we select to enforce it.
    - Because the data stored at that smallest Seqno is an incremental
      diff, to make this invariant work, there needs to be a rollup at
      either `earliest-1` or `earliest`. We choose `earliest` because it
      seems to make the code easier to reason about in practice.
    - A consequence of the above is when we garbage collect old versions
      of state, we're only free to truncate ones that are `<` the latest
      rollup that is `<= current.seqno_since`.
- `live diffs`: The set of SeqNos present in Consensus at any given
  time.
- `live states`: The range of state versions that it is possible to
  reconstruct: `[earliest,current]`.
  - Because of earliest and current invariants above, the range of `live
    diffs` and `live states` are the same.
- The set of known rollups are tracked in the shard state itself.
  - For efficiency of common operations, the most recent rollup's Blob
    key is always denormalized in each StateDiff written to Consensus.
    (As described above, there is always a rollup at earliest, so we're
    guaranteed that there is always at least one live rollup.)
  - Invariant: The rollups in `current` exist in Blob.
    - A consequence is that, if a rollup in a state you believe is
      `current` doesn't exist, it's a guarantee that `current` has
      changed (or it's a bug).
  - Any rollup at a version `< earliest-1` is useless (we've lost the
    incremental diffs between it and the live states). GC is tasked with
    deleting these rollups from Blob before truncating diffs from
    Consensus. Thus, any rollup at a seqno < earliest can be considered
    "leaked" and deleted by the leaked blob detector.
  - Note that this means, while `current`'s rollups exist, it will be
    common for other live states to reference rollups that no longer
    exist.

---
## [Mindgibber/zig](https://github.com/Mindgibber/zig)@[a31b449b55...](https://github.com/Mindgibber/zig/commit/a31b449b55c32eba1cb61a48753a6fc98696c98f)
#### Friday 2022-08-26 22:09:41 by Andrew Kelley

make LLVM and Clang emit DWARF 4 instead of 5

This reverts 6d679eb2bcbe76e389c02e0bb4d4c4feb2847783 and additionally
changes the command line parameters passed to Clang to match.

Clang 14 defaults to DWARFv5 which is an interesting choice. v5 has been
out for 5 years and yet Valgrind does not support it, and apparently
neither does either GDB or LLD, I haven't determined which, but I wasn't
able to use GDB to debug my LLVM-emitted dwarf 5 zig code that was linked
with LLD.

A couple years ago when I was working on the self-hosted ELF linker, I
emitted DWARFv5 but then downgraded to v4 when I realized that third
party tools were stuck in the past. Years later, they still are.

Hopefully, Clang 14's bold move will inspire third party tools to get
their shit together, however, in the meantime, everything's broken, so
we're passing `-gdwarf-4` to clang and instructing LLVM to emit DWARFv4.

Note that Zig's std.debug code *does* support DWARFv5 already as of a
previous commit that I made today.

---

