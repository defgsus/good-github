## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-12](docs/good-messages/2022/2022-06-12.md)


1,550,895 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,550,895 were push events containing 2,175,619 commit messages that amount to 110,702,607 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [DarkKnight2019/crawl](https://github.com/DarkKnight2019/crawl)@[1352289c90...](https://github.com/DarkKnight2019/crawl/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Sunday 2022-06-12 00:47:18 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [Contrabang/Paradise](https://github.com/Contrabang/Paradise)@[6082c95eb3...](https://github.com/Contrabang/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Sunday 2022-06-12 01:03:17 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [Minecraft-Eternal/MC-Eternal-1.12](https://github.com/Minecraft-Eternal/MC-Eternal-1.12)@[e82e5dd2c1...](https://github.com/Minecraft-Eternal/MC-Eternal-1.12/commit/e82e5dd2c181c84bfabd1e624f81112cb1a69642)
#### Sunday 2022-06-12 01:14:05 by anabsolutesloth

"Smol" quest changes

update Scarecrow quest in Intro to reflect changes in Undead Rising
Add rewards to F&A quests (and do 1 text tweak)
redo the entire AE2 questline because yes
nerf the funny botania quest money (1M money is too much and you get a creative tablet for god's sake)
fix typo in NA Ritual of the Forest quest
fix NA book quest being happy with any patchouli book
redo Twilight Forest questline and add some sekret speeciel rewards C:
change RFTools Builder Shape Card dependencies (fortune now depends on regular)
fix all 3 EIO cap bank quests detecting any tier of cap bank (ignore damage funny)
remove alloy task dependencies from conduit quests because they were too confusing
mmmm nuclearcraft tutorial link but good

uh that should be it i think

---
## [doamatto/doamatto.xyz](https://github.com/doamatto/doamatto.xyz)@[4d02d842ef...](https://github.com/doamatto/doamatto.xyz/commit/4d02d842ef1bf351af7a8081c1ed8396d6970e3e)
#### Sunday 2022-06-12 01:25:25 by Matt Ronchetto

remote post (see commit mesg. desc)

TL;DR: This was a terrible piece that shouldn't have gone up. It may return after significant revisions, but it was just a generally not great post.

---

I enjoy writing these posts, but sometimes I feel the urge to write even if it's a topic no one cares about or I'm writing absolute non-sense. This post about TLD reputability isn't *inaccurate*, it's just poorly constructed. What I want to do moving forward is craft posts of a quality that would rival that of a thesis while being readable by a junior high student. It allows that nice balance between accessibility with new people being able to understand more complex concepts, as well as give me that tiny "yeah, I'm teaching people stuff!"

In short, this post is going to be taken down for the foreseeable future and remain (clearly) visible in commit history. I may revise this post and release it again in the future, but this is the best course of the time being.

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[cd294e9040...](https://github.com/Zonespace27/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Sunday 2022-06-12 01:30:24 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[245ec35dae...](https://github.com/Zonespace27/tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Sunday 2022-06-12 01:30:24 by LemonInTheDark

Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

---
## [Mooshimi/tgstation](https://github.com/Mooshimi/tgstation)@[95ffcd4e19...](https://github.com/Mooshimi/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Sunday 2022-06-12 01:45:26 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [stich4life08/python-turtle-and-other-stuff](https://github.com/stich4life08/python-turtle-and-other-stuff)@[33995f2258...](https://github.com/stich4life08/python-turtle-and-other-stuff/commit/33995f22589668f3a3fcf06129e4735667f3f795)
#### Sunday 2022-06-12 02:20:30 by stich4life08

added more questions (can i make this in html)

I can't get no sleep
I can't get no sleep
I used to worry, thought I was going mad in a hurry
Gettin' stressed, makin' excess mess in darkness
No electricity, something's all over me, greasy
Insomnia, please release me and let me dream
Of makin' mad love to my girl on the heath
Tearin' off tights with my teeth

---
## [Ruby-Dragon/activate-linux](https://github.com/Ruby-Dragon/activate-linux)@[6012d283ca...](https://github.com/Ruby-Dragon/activate-linux/commit/6012d283caeb096b9667ce759f0eeb92c0e99005)
#### Sunday 2022-06-12 03:45:04 by Reperak

Fix rgba_color_string returning default

Shame on me for not testing before submitting #65, and shame on the people who reviewed #65 for trusting my stupid ass.

Fixes #99

---
## [EmoGarbage404/space-station-14](https://github.com/EmoGarbage404/space-station-14)@[949fbd0194...](https://github.com/EmoGarbage404/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Sunday 2022-06-12 04:54:48 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2194053f29...](https://github.com/treckstar/yolo-octo-hipster/commit/2194053f29dc0e67d12cb5d7e8e0442a4b2b365d)
#### Sunday 2022-06-12 05:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [a4lg/binutils-gdb](https://github.com/a4lg/binutils-gdb)@[80c0a3bf1b...](https://github.com/a4lg/binutils-gdb/commit/80c0a3bf1b949403521d186fc04ed9052ea1d7d4)
#### Sunday 2022-06-12 06:36:52 by Andrew Burgess

gdb/testsuite: remove definition of true/false from gdb_compiler_info

Since pretty much forever the get_compiler_info function has included
these lines:

    # Most compilers will evaluate comparisons and other boolean
    # operations to 0 or 1.
    uplevel \#0 { set true 1 }
    uplevel \#0 { set false 0 }

These define global variables true (to 1) and false (to 0).

It seems odd to me that these globals are defined in
get_compiler_info, I guess maybe the original thinking was that if a
compiler had different true/false values then we would detect it there
and define true/false differently.

I don't think we should be bundling this logic into get_compiler_info,
it seems weird to me that in order to use $true/$false a user needs to
first call get_compiler_info.

It would be better I think if each test script that wants these
variables just defined them itself, if in the future we did need
different true/false values based on compiler version then we'd just
do:

  if { [test_compiler_info "some_pattern"] } {
    # Defined true/false one way...
  } else {
    # Defined true/false another way...
  }

But given the current true/false definitions have been in place since
at least 1999, I suspect this will not be needed any time soon.

Given that the definitions of true/false are so simple, right now my
suggestion is just to define them in each test script that wants
them (there's not that many).  If we ever did need more complex logic
then we can always add a function in gdb.exp that sets up these
globals, but that seems overkill for now.

There should be no change in what is tested after this commit.

---
## [AlexKollar/Cryptex](https://github.com/AlexKollar/Cryptex)@[b99e4911a2...](https://github.com/AlexKollar/Cryptex/commit/b99e4911a267e0efbe8bee82f318f3a38ccc74b4)
#### Sunday 2022-06-12 07:15:13 by Blue Cosmo

fuck your git merge bullshit ass lookin l...jopsjd

---
## [Zeldazackman/Core-Station](https://github.com/Zeldazackman/Core-Station)@[38724d4d4c...](https://github.com/Zeldazackman/Core-Station/commit/38724d4d4c140fb4bfc92444ba3e5dd182ca7df9)
#### Sunday 2022-06-12 11:44:51 by VerySoft

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
## [liwei330249526/cockroach](https://github.com/liwei330249526/cockroach)@[13a65d3682...](https://github.com/liwei330249526/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Sunday 2022-06-12 13:15:03 by Andrei Matei

util/tracing: fix crash in StreamClientInterceptor

Before this patch, our client-side tracing interceptor for streaming rpc
calls was exposed to gRPC bugs being currently fixed in
github.com/grpc/grpc-go/pull/5323. This had to do with calls to
clientStream.Context() panicking with an NPE under certain races with
RPCs failing. We've recently gotten two crashes seemingly because of
this. It's unclear why this hasn't shown up before, as nothing seems new
(either on our side or on the grpc side). In 22.2 we do use more
streaming RPCs than before (for example for span configs), so maybe that
does it.

This patch eliminates the problem by eliminating the
problematic call into ClientStream.Context(). The background is that
our interceptors needs to watch for ctx cancelation and consider the RPC
done at that point. But, there was no reason for that call; we can more
simply use the RPC caller's ctx for the purposes of figuring out if the
caller cancels the RPC. In fact, calling ClientStream.Context() is bad
for other reasons, beyond exposing us to the bug:
1) ClientStream.Context() pins the RPC attempt to a lower-level
connection, and inhibits gRPC's ability to sometimes transparently
retry failed calls. In fact, there's a comment on ClientStream.Context()
that tells you not to call it before using the stream through other
methods like Recv(), which imply that the RPC is already "pinned" and
transparent retries are no longer possible anyway. We were breaking
this.
2) One of the grpc-go maintainers suggested that, due to the bugs
reference above, this call could actually sometimes give us "the
wrong context", although how wrong exactly is not clear to me (i.e.
could we have gotten a ctx that doesn't inherit from the caller's ctx?
Or a ctx that's canceled independently from the caller?)

This patch also removes a paranoid catch-all finalizer in the
interceptor that assured that the RPC client span is always eventually
closed (at a random GC time), regardless of what the caller does - i.e.
even if the caller forgets about interacting with the response stream or
canceling the ctx.  This kind of paranoia is not needed. The code in
question was copied from grpc-opentracing[1], which quoted a
StackOverflow answer[2] about whether or not a client is allowed to
simply walk away from a streaming call. As a result of conversations
triggered by this patch [3], that SO answer was updated to reflect the fact
that it is not, in fact, OK for a client to do so, as it will leak gRPC
resources. The client's contract is specified in [4] (although arguably
that place is not the easiest to find by a casual gRPC user). In any
case, this patch gets rid of the finalizer. This could in theory result
in leaked spans if our own code is buggy in the way that the paranoia
prevented, but all our TestServers check that spans don't leak like that
so we are pretty protected. FWIW, a newer re-implementation of the
OpenTracing interceptor[4] doesn't have the finalizer (although it also
doesn't listen for ctx cancellation, so I think it's buggy), and neither
does the equivalent OpenTelemetry interceptor[6].

Fixes #80689

[1] https://github.com/grpc-ecosystem/grpc-opentracing/blob/8e809c8a86450a29b90dcc9efbf062d0fe6d9746/go/otgrpc/client.go#L174
[2] https://stackoverflow.com/questions/42915337/are-you-required-to-call-recv-until-you-get-io-eof-when-interacting-with-grpc-cl
[3] https://github.com/grpc/grpc-go/issues/5324
[4] https://pkg.go.dev/google.golang.org/grpc#ClientConn.NewStream
[5] https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing/client_interceptors.go#L37-L52
[6] https://github.com/open-telemetry/opentelemetry-go-contrib/blame/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go#L193

Release note: A rare crash indicating a nil-pointer deference in
google.golang.org/grpc/internal/transport.(*Stream).Context(...)
was fixed.

---
## [SlothScript/SlothScript.github.io](https://github.com/SlothScript/SlothScript.github.io)@[8a0295baae...](https://github.com/SlothScript/SlothScript.github.io/commit/8a0295baaeaf8a89c681faaefc81dbf0fc085a34)
#### Sunday 2022-06-12 14:15:53 by SlothScript

Create NatchHack.js

Yeah this simple mod allows you to cheat in Cookies, Heavenly Chips, and sugar lumps.

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[acca4b2756...](https://github.com/mbs-octoml/mbs-tvm/commit/acca4b275689a36e22bda68ce7a26ca01a4227bc)
#### Sunday 2022-06-12 14:54:12 by Mark Shields

** Collage v2 sketch ***

- Polish compiler_function_utils for splitting out
- Mark functions as extern.
- Get rid of relay.ext.cutlass
- kExternalSymbol:String ----> kExtern:Bool
- Host glitch if PlanDevices run before CollagePartition
- Fix unit test
- Make load_static_library first class python func
- Get CUTLASS going on graph executor as well as vm
- Include export_library in estimate_seconds
- Rollback DSOLibrary changes.
- Add StaticLibraryNode and switch CUTLASS to use it
  This avoids the crazy serialize/deserialize/load hackery, which I'll now remove.
- Get running again
- CUTLASS picks up all options from 'cutlass' external codegen target.
- Revert false starts with cutlass handling
- Get CUTLASS going with program-at-a-time tuning and compilation instead of
  function at a time.
- Save DSOLibraries by contents rather than by reference.
- futzing with libraries
- revert unnecessary cutlass changes
- starting unit test for dsolibrary save
- Prepare scalar changes for PR.
- Eager candidate cost measurement.
- More conv2d_cudnn.cuda training records.
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
## [Manukineko/Jabba](https://github.com/Manukineko/Jabba)@[2557960bc0...](https://github.com/Manukineko/Jabba/commit/2557960bc0380b7bc54056c3befc931e0d88d258)
#### Sunday 2022-06-12 14:57:02 by Manuel Utsunomiya Bonisoli

[WIP] Reworking Feedback & Jabba Container

Successful tests to change the way an element is added to a JabbaContainer
Successful tests to rework the feedback system based on how I did it for BibFortuna.
Feedback effect are now stored in the global space (took inspiration from how Juju doesn't it for Input) but I should be able to contain them into the new __feedbackPlayer constructor, I guess.
BibFortuna is now a full part of Jabba and not an extention anymore (was a pain in the ass to maintain)
add an enum to define the type of element.

All of those changes are WIP and not usable yet.

---
## [DoctorSquishy/MonkeStation](https://github.com/DoctorSquishy/MonkeStation)@[ada837ddc0...](https://github.com/DoctorSquishy/MonkeStation/commit/ada837ddc0840bb3a6dd1631d8c752a71853366c)
#### Sunday 2022-06-12 14:58:32 by BluBerry016

Exploration PP - Reworks Outpost Nuke Announcement (#450)

* Fuck you, die

* Update nuke_ruin.dm

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[5741b807be...](https://github.com/newstools/2022-new-york-post/commit/5741b807bec1c3b50653711135008f3caf8458df)
#### Sunday 2022-06-12 16:27:34 by Billy Einkamerer

Created Text For URL [nypost.com/2022/06/12/woman-stunned-after-boyfriend-refuses-to-pay-for-half-her-flight/]

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[2e7a0716b2...](https://github.com/newstools/2022-new-york-post/commit/2e7a0716b210b7e69e7c7a2ed4643d76a6ea9911)
#### Sunday 2022-06-12 16:27:37 by Billy Einkamerer

Created Text For URL [nypost.com/2022/06/11/woman-blasts-boyfriend-as-cheating-b-d-after-he-disappears/]

---
## [TrickumEnterprises/TrickumEnterprises](https://github.com/TrickumEnterprises/TrickumEnterprises)@[d29442d1cf...](https://github.com/TrickumEnterprises/TrickumEnterprises/commit/d29442d1cf4f72791eb8b31e893c9e6cdc13d132)
#### Sunday 2022-06-12 17:44:50 by Benny Trickum, C.E.O. Trickum Enterprises L.L.C

changes

changes are something we all go through as we learn and our belief system is affected by the affects of what we learn.  These are the most powerful of learning opportunities.   So we must in these moment re-evaluate everything and fix what is not correct then before its a problem later.  So through out my time here you will see things change as I learn new things and I hope to do my best to make known what is different whether it is in skill, philosophical, or simply stupidity; I want to do my best to keep it direct for my family and the future and I would love for others to do the same.  That said I would also encourage others to try better to simplify explanations rather then there efforts.  You can never put enough work in that does not better you but we don't try hard enough at the things that better others.  Many things I have read about here on github and in the beginning I understood basically nothing of what people were trying to show each other and that's not to say that I understand much of it now.  I think or my hope as that everyone could take a little more time to be more thorough in explaining what there page is about and is required to perform the task that they have committed.  This in turn should cut many problems down in all fields and create more individuals who understand better and create more solutions.  This is where many knowledgeable, lack wisdom.  They are not the same.  Knowledge is only good to the individual that has it if they lack wisdom.  Without the wisdom the knowledge can not be properly shared with others because wisdom is only found with love.  Without love you can not have wisdom and without those your knowledge is for nothing but you.  <cite>When wisdom enters into your heart and knowledge becomes pleasant to your soul:  Discretion will preserve you, and knowledge will keep you...</cite><u>Prov. 2:10-11.</u>  NOTE:  I would encourage people to read exactly what wisdom will protect you from, I think that a lot of you will find this quite interesting...

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[0dc169fead...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/0dc169fead53c079bd7ba2539d65ba936abddbf0)
#### Sunday 2022-06-12 18:23:18 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [PhoenixAceVFX/Fedoraware](https://github.com/PhoenixAceVFX/Fedoraware)@[5a23d95aca...](https://github.com/PhoenixAceVFX/Fedoraware/commit/5a23d95aca96005b454a9a9b75ba2ac9ae603c83)
#### Sunday 2022-06-12 18:26:57 by Johnathon Walnut

Merge pull request #380 from femboy-boop/patch-2

fuck you baan

---
## [thistleknot/Python-Stock](https://github.com/thistleknot/Python-Stock)@[2c8c915b36...](https://github.com/thistleknot/Python-Stock/commit/2c8c915b362e0ce278f9379851017831840d4f6d)
#### Sunday 2022-06-12 18:37:34 by Turning out data tricks since 2006!

v5

added a slew of features

I'm thinking of not exporting a xlsx until after the tail end of the visual graph. It's a very expensive [computationally] operation to export to xlsx and I've found a new way to "pickle" the data (idk why the name, but it means to serialize the data into a binary format) and I can use that method to pass it to the "analysis" portion of code and "unpack" it there fairly quickly meaning you can focus on the inferences while it's still exporting.

I want to expand the analysis from 2 years to 3-5 years. This won't affect any of the calculations, it will make an export of the data to excel much larger though. A filter will still be in place to only select those that have at least 2 years of data, but this is for preparation for my next step.

I want to add "seasonal index" calculations for the sectors. I default to quarterly because I like the nice round quarter numbers (i.e. 63 trading days) and most businesses seem to plan around that. I could do a monthly, but it would be a bastardized month (21 trading days != the same length). Or I could try weekly index's (but that would be noisy), as 52 weeks in a year is nice and smooth, but quarterly seems to be the nice midway point between those choices.

This way when you look at a stock and consider buying it, you can see how the historical performance of the sector has been and make a quick call if there will be a seasonal downturn (I notice energy sector dips in the summer and rise in the winter)

I've also added a 252 day seasonal forecast (excessive, but if I reduce the data to quarterly and then forecast out, it chops off any data after the last full quarter, by choosing 252 it focuses on the past 2 years of data, which is why I want to extend the analysis to 5 years because it will be more accurate). (2 years might be just fine)

I also want to calculate quality metrics and give an estimate about how accurate the forecast is.

As I've been doing since yesterday,, I will upload the report to google drive as a pdf so you can see visually all this stuff I'm talking about (without the code)

---
## [torvalds/linux](https://github.com/torvalds/linux)@[846bb97e13...](https://github.com/torvalds/linux/commit/846bb97e131d7938847963cca00657c995b1fce1)
#### Sunday 2022-06-12 18:41:07 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [JozsefKutas/scipy](https://github.com/JozsefKutas/scipy)@[c73e088350...](https://github.com/JozsefKutas/scipy/commit/c73e0883501a21cfaf7220a8118a6155857b5829)
#### Sunday 2022-06-12 19:04:06 by Tyler Reddy

MAINT: add `SCIPY_USE_PROPACK` env variable (#16361)

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [Bm0n/Paradise](https://github.com/Bm0n/Paradise)@[ab7a358506...](https://github.com/Bm0n/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Sunday 2022-06-12 21:39:25 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f6003ddc2b...](https://github.com/mrakgr/The-Spiral-Language/commit/f6003ddc2b8f60d2371b12cfe9d9905fdf3bc3ad)
#### Sunday 2022-06-12 22:23:45 by Marko Grdinić

"10:45am. Remember the days when I would go to bed late at past 1am, wake up past the start of the morning session and skip it and then put in some overtime later in the day. It seems I am back to my old habbit.

10:50am. But that is fine. It is not normal to keep overworking myself like I have for the past 8 months. Let me chill a bit. Sengoku Komachi as well as 2 Satanophany chapters are out. After that I'll read a chapter of Legendary Mechanic. So far I am at 202 with that.

I've done some thinking how I am going to handle the floating city problem. I am going to start off by placing a bunch of boxes on a flat flying cylinder. I'll try to make it so that the boxes outside the center of the territory are smaller, but will try to randomize it. That should give me a hint as to how I should deal with perspective.

As for the buildings themselves, I'll want to turn the boxes into something real.

I'll look at references for inspiration, but I am thinking that it is finally time to make use of Houdini. It has powerful functionality for urban procedural modeling that I've yet to try, and it is a good time to exploit that option. Otherwise, what was the point in putting all that effort in studying it?

11am. The earth was not too hard, but I want to go further.

https://www.youtube.com/watch?v=pZFYQuARAAA
Advanced Planet in Blender 2.9 Cycler Render

Right, before I get started on that, I want to take a look at this video. Maybe I'll want to go for volumetric clouds and angle the shot differently from what I have now.

11am. Well, let me chill.

11:45am. https://www.lightnovelpub.com/novel/the-legendary-mechanic-novel-10062255/245-chapter-204

Let me pause here. It is time to start. Let me watch the above tutorial.

Actually, before I do that, let me try putting the render from yesterday into the NN.

11:55am. I like the result with the great wave style more than I thought I would. After I am done I am going to properly investigate the styles. I am going to make some changes and clean up the scripts so as to make it easier to use. Right now I am renaming the files by hand and running PNGQuant after that.

Let me post them on Twitter.

https://twitter.com/Ghostlike

Should be good. I might as well put them in the /wip/ thread as well, but it is quite a burden to be posting in two places, especially if I am doing descriptions. Let me just copy paste them.

12:05pm. Done. Let me start the tutorial. I am interested in how he would do the clouds.

https://youtu.be/pZFYQuARAAA?t=196

It is annoying that he flat subdiv's a cube and then made it spherical. Seriously you guys, the settings in the UV and Ico sphere are there for a reason, and you get UVs for free.

https://youtu.be/pZFYQuARAAA?t=566
> Sea's a bit metallic.

I didn't think about that, but it does not matter.

12:20pm. https://youtu.be/pZFYQuARAAA?t=607
> The sea's not uniform in its roughness.

I didn't think of this either.

https://youtu.be/pZFYQuARAAA?t=1024

Hmmm, he scales the density by the distance from the pivot.

12:55pm. Had to take a short break. Let me watch for another 10m and then I will have breakfast.

1:05pm. He is talking about clouds here.

https://youtu.be/pZFYQuARAAA?t=2075
> There are a few routes to improve them: you either use subsurface...

Let me have breakfast here. I'll finish this after than and get started with playing with the buildings.

2pm. https://www.lightnovelpub.com/novel/the-legendary-mechanic-novel-10062255/245-chapter-209

Let me finish the battle and then I will resume.

2:10pm. https://youtu.be/pZFYQuARAAA?t=2075

Let me resume from here. I need to focus. Mentally I've already started relaxing, which is not good. Art is a lot of work. I need to finish the cover properly.

Style transfer made me elated, since just on its own, it cut my workload in half while increasing the quality. But rather than be satisfied with my current level, I should work my way towards one day getting a system like DALLE.

https://www.youtube.com/results?search_query=blender+subsurface

You know what, since he is talking about it, let me study subsurf just a bit.

https://youtu.be/stQAYNAKfTA?t=88
Easy Introduction to Subsurface - Blender & Maya!

I am going to have to play around with this and figure out what it does, but for now let me just watch the tutorial.

https://youtu.be/stQAYNAKfTA?t=518

This looks pretty cool. I had no idea Eevee could do it.

2:30pm. Let me get back to the tutorial.

https://youtu.be/pZFYQuARAAA?t=2186

I can't believe he turned on the adaptive subdiv and displacement here. That will make playing with shaders take forever.

No forget it. Samuel Krug is a very boring presenter, and he is just fooling around while I watch the screen change without much commentary. It does not feel like he is going at it with a clear intent.

If I continue watching this, it will sap my will to do the work that I should be doing.

Today really gives me flashbacks to the programming era. I've become engrossing in reading LNs and my will do work had slackened. To boot, I've started watching tutorials I have no interest in. Forget that

2:55pm. Had to help my father repair the trash can.

Let me resume.

I hate days like this. It is almost 3pm, but I've barely even started on the work for the day. That tutorial, plus getting up at 10:40 really cost me a lot. I am going to put in some overtime.

3pm. Let's say I have 7 more hours in the day to work no art instead of 3. I do not want to stress myself to rush.

This is not a 9-5 job so I should just work as long as I feel like it.

Let write what I want to write.

Right now I am at earth in space picture, and I am struck just how beautiful the painted image looks. While the 3d version feels somewhat generic, the styled transfered version is 5/5. At this point I am having a hard time imagining that dding the floating city would improve things. Right now it has just the right balance. If I put this as the first image in the story, it would definitely have an impact on the reader and entice him to read a couple of chapters.

3:10pm. Sigh, I know that I am on the right track when I have to stop myself from admiring my own work.

Focus me. Opem Blender 3.2.

I'll make a copy of the scene, since this one is set up just right.

3:30pm. Sigh, why can't geometry nodes work on the first try? It is not working for some reason. It hasn't put down even a single point.

...Ah, I forgot to plug in the damn mesh!

4:50pm. I hate Blender's scattering. It crashed my system just now. At any rate, the composition I have in mind is unworkable.

5:15pm. I've set it to render.

5:55pm. I've gone to take a break and when I came back it was done. It looks quite good. Since it was a part of the atmophere, the blur effect got applied to it automatically.

6pm. Sigh, I really adore this image. I really love it. I do not think it is particularly better than the previous version, but those golden lights will play a thematic role, so they should be there.

What I imagine originally was this image viewed from above the city, but that kind of composition would be nonsensical. If I really wanted something like that...

https://youtu.be/pZFYQuARAAA?t=2

The composition here just from beyond the atmosphere is much better. I can imagine having a city in the distance here. In my own image they could only be tiny bright lights in the distance.

6:10pm. At any rate, let me post this.

7:05pm. Done with lunch. A conclussion like this should have been obvious. I think I've made this mistake once before, but I forgot what the circumstances were.

Now...

7:10pm. I really feel like closing for the day, but let me do some work on the script. Let me first make it so that it is possible to load two files as content images and process them.

7:10pm. Hmmm, I've confirmed that it loads both files.

7:40pm. I am thinking about it.

```py
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    for i, data in enumerate(dataset):
        # if i == 0:
        #     model.data_dependent_initialize(data)
        #     model.parallelize()
        #     if opt.eval:
        #         model.eval()
        if i >= opt.num_test:  # only apply our model to opt.num_test images.
            break
        model.set_input(data)  # unpack data from data loader
        model.test()           # run inference
        visuals = model.get_current_visuals()  # get image results
        img_path = model.get_image_paths()     # get image paths
        if i % 5 == 0:  # save images to an HTML file
            print('processing (%04d)-th image... %s' % (i, img_path))
        save_images(webpage, visuals, img_path, width=opt.display_winsize)
    # webpage.save()  # save the HTML
```

I am confused about various things. Is this dataset really supposed to be used like this, within a for loop. For styles it might be better to use a double loop. Right now it groups them pairwise.

Just why is it loading it all in a single dataset instead of two separate ones?

https://pytorch.org/docs/stable/data.html#dataset-types

It says iterable and that is what the above is. So I guess it is fine.

7:45pm. Hmmm, maybe it is like this because this code was meant for loading text image pairs. Then it would make sense to load the dataset in tuples. It is not the case that it is loading the first style for both images. It does pair them up.

```py
        if self.opt.serial_batches:   # make sure index is within then range
            index_B = index % self.B_size
        else:   # randomize the index for domain B to avoid fixed pairs.
            index_B = random.randint(0, self.B_size - 1)
```

Huh really, it randomizes them.

```py
    def __len__(self):
        """Return the total number of images in the dataset.

        As we have two datasets with potentially different number of images,
        we take a maximum of
        """
        return max(self.A_size, self.B_size)
```

Right, the way it works now is on purpose. Rather than going over all the styles, it will go over all the datapoints in A, and either pick randomly from B or wrap around.

https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/tree/master/data

This code was taken from CycleGAN. I am thinking about implementing a more proper dataset when it occured to me that I should do a google search. Let me see if I can find a dataset that does what I want.

https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/data/aligned_dataset.py

Maybe this is what I want. Let me copy paste it.

8:05pm. Ah, fuck it. Let me implement it on my own.

```py
    def __len__(self):
        """Return the total number of images in the dataset."""
        return self.A_size * self.B_size
```

Let me do it like this.

```py
    def __getitem__(self, index):
        """Return a data point and its metadata information.

        Parameters:
            index (int)      -- a random integer for data indexing

        Returns a dictionary that contains A, B, A_paths and B_paths
            A (tensor)       -- an image in the input domain
            B (tensor)       -- its corresponding image in the target domain
            A_paths (str)    -- image paths
            B_paths (str)    -- image paths
        """
        A_path = self.A_paths[index // self.B_size]
        B_path = self.B_paths[index % self.B_size ]
        A_img = Image.open(A_path).convert('RGB')
        B_img = Image.open(B_path).convert('RGB')

        # Apply image transformation
        # For FastCUT mode, if in finetuning phase (learning rate is decaying),
        # do not perform resize-crop data augmentation of CycleGAN.
#        print('current_epoch', self.current_epoch)
        is_finetuning = self.opt.isTrain and self.current_epoch > self.opt.n_epochs
        modified_opt = util.copyconf(self.opt, load_size=self.opt.crop_size if is_finetuning else self.opt.load_size)
        transform = get_transform(modified_opt)
        A = transform(A_img)
        B = transform(B_img)

        return {'A': A, 'B': B, 'A_paths': A_path, 'B_paths': B_path}
```

Now I should get crossing behavior between content and style images.

8:10pm. Now let me just output the names properly in the results dir as well as get rid of the images subdir. The stupid thing outputs a large amount of directories.

```py
    def forward(self):
        """Run forward pass; called by both functions <optimize_parameters> and <test>."""

        self.real_A_feat = self.netAE(self.real_A, self.real_B)  # G_A(A)
        # self.real_B_feat = self.netAE(self.real_B, self.real_A)  # G_A(A)
        # self.fake_A = self.netDec_A(self.real_B_feat)
        self.fake_B = self.netDec_A(self.real_A_feat)
```

Great job keeping that intermediate in memory between runs.

https://www.oreilly.com/library/view/python-standard-library/0596000960/ch13s03.html

```py
def save_images(image, name, label, path, aspect_ratio=1.0):
    """Save images to the disk."""

    im = util.tensor2im(image)
    image_name = '%s (%s).png' % (name, label)
    save_path = os.path.join(path, image_name)
    util.save_image(im, save_path, aspect_ratio=aspect_ratio)
```

Let me do it like so.

```py
    def __init__(self, opt):
        BaseModel.__init__(self, opt)

        self.model_names = ['AE','Dec_A', 'Dec_B']

        # define networks (both generator and discriminator)

        vgg = net.vgg
        vgg = nn.Sequential(*list(vgg.children())[:31])
        self.netAE = net.ADAIN_Encoder(vgg, self.gpu_ids)
        self.netDec_B = net.Decoder(self.gpu_ids)

    def forward(self,input):
        AtoB = self.opt.direction == 'AtoB'
        real_A = input['A' if AtoB else 'B'].to(self.device)
        real_B = input['B' if AtoB else 'A'].to(self.device)
        return self.netDec_A(self.netAE(real_A, real_B))
```

I am the great simplifier.

Now the intermediates will not longer be uselessly held in memory.

It works now. Do I have anything for compressing png images?

9:05pm. https://pngquant.org/

Let me see if I can invoke this from the command line.

9:25pm.

```py
    print("Compressing...")
    os.system(f"pngquant --force --skip-if-larger --ext .png {web_dir}/*.png")
    print("Done.")
```

I got pgquant, put it directly into the directory and just hit this command. This causes it to quantize the image into 256 colors. I'd never have thought this was what it is doing. I can't tell the difference at all.

9:30pm. This really took a while. At any rate,

9:35pm. You know what? Why not. let me copy all the styles into dataB and see where it gets me.

10:05pm. https://github.com/cs-chan/ArtGAN/blob/master/WikiArt%20Dataset/README.md

This dataset is 25gb, but it might be worth getting.

```py
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    for i, data in enumerate(dataset):
        path = save_path(data, results_dir)
        if not os.path.exists(path):
            image = model.forward(data)           # run inference
            save_images(image, path)
            os.system(f"pngquant --force --skip-if-larger --ext .png \"{path}\"")
        else:
            print(f"Skipping {path}.")
    print("Done.")
```

I've set it up like this. Now I won't need to suffer from overwritting old styles.

10:40pm. Am checking out some styles on the deep dream generator site. The hill cloud is quite nice.

10:45pm. Colorful leaves.

11:25pm. The deep dream generator is no good. I was really lucky to get CAST. It is really a furtuitous encounter. I got exactly what I needed at the right time.

11:35pm. Let me post djeeta dark on /wip/ and then I will call it a day.

///

Here is a dark version to contrast the previous one. It has a murky, suppressed look, like the world is shrouded in fog. The net really understands lighting well, you wouldn't get this just by toning down the values globally.

I did some work on the scripts and now they are easier to use. I have a bunch of images that look great, but I'd get people calling me schizo autist if I started dumping so I'll hold back.

///

///

This one has good contrast and a vibrant palette. It is well balanced. I am not sure if I should strive for balance or if I'll go with an intense look.

I am not really happy with how drawings comes out on this image, the one I posted was the only one worth showcasing.

I think that I'll grab the 25gb wiki art dataset tomorrow and try a much wider selection of styles. I'll also get started on the next scene. I'll try out Houdini's urban modeling capabilities for the first time.

///

I'll also post jugsaw.

12:15pm. https://twitter.com/Ghostlike/status/1536019692414017538

I ended up posting a bunch on Twitter. It seems it allows multiple images per tweet.

I really put in overtime today. I definitely made up for my late start. Unfortunately, I also missed my chance to take a bath. Right now I am too tired for it."

---
## [damerell/crawl](https://github.com/damerell/crawl)@[a78a01fbda...](https://github.com/damerell/crawl/commit/a78a01fbda24ec21f42f2d91b77876e0e320e988)
#### Sunday 2022-06-12 22:35:39 by Floodkiller

Remove old malmutate

We all hate it so we're taking a leaf out of Gooncrawl's book.

Partially remove monster Malmutate

Removes Malmutate from nequxecs and cacodemons, the two most common
malmutaters (thanks to the overuse of demons throughout Extended and
summoners).

Nequoxecs get Paralyze, to match their 'mind flayer' theme. This should be
a threat at lower levels, but easily resisted by late-game characters (a
single pip of MR reduces success rate to 35%, two pips to 10%, etc.).

Cacodemons get Entropic Weave, to synergize with their digging and adding
to their 'disrupt the player from bigger threats' toolset.

This should reduce Malmutate enough to test to see if it needs to be
changed/removed from orbs of fire/shining eyes (as well as if Mnoleg needs
malmutate on hit removed).

(cherry picked from commit 15298a4ded55fc89561f5a8eb9934c3134e019ac)

Change Malmutate spell effect

From mutating the player to deteriorating all the players stats by
1+(1d4, average of 2 rolls). This will only affect Orbs of Fire as they
are the only monster left that has the Malmutate spell and I'm too lazy
to change the name in the source code for everything. This only affects
the spell version of Malmutate, not any other version that may exist
(i.e. Mnoleg melee, spell miscasts, etc).

Also left a note for myself to look into at some point.

(cherry picked from commit a2afb6c259e3b450e53f4dd65fb524583356f8c3)

Tone done new Malmutate

Waaaaaay too rough, oops

(cherry picked from commit 0d295a6d73b7014d2814741962ae627de7b1b361)

Give shining eyes Polymorph instead of Malmutate

Fits the theme of slimes and form changing while getting rid of the
Malmutate devil. Also upped the spellpower per HD of Polymorph for
monster casting, which hopefully shouldn't matter as only shining eyes
can cast it normally. Might need to tweak down the modifier a bit if it
is too extreme, but wanted to make sure they were still a threat.

(cherry picked from commit 3c9b759b45d4f420ddbd22d0fa63e83be52bfce9)

---

