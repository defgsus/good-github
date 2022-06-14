## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-13](docs/good-messages/2022/2022-06-13.md)


1,698,560 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,698,560 were push events containing 2,675,477 commit messages that amount to 203,943,120 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[573344e3b4...](https://github.com/treckstar/yolo-octo-hipster/commit/573344e3b4116b71e21f544a975435fbd61025a3)
#### Monday 2022-06-13 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [DragonWolf1982/MODS](https://github.com/DragonWolf1982/MODS)@[4deddcc01c...](https://github.com/DragonWolf1982/MODS/commit/4deddcc01c4f6bb4e2b6f72afd4f68a18ed4cd4f)
#### Monday 2022-06-13 00:25:42 by DragonWolf1982

Add files via upload

This is a modlet that adds a bunch of different dye colors for 7 Days To Die.
In this lastest update I have added recipes for each dye color including the vanilla colors.
This modlet should work in any overhaul mod in SP and MP.
More is yet to come so stick around to see what is added as well as other projects.
If you have a color request you can contact either myself DragonWolf1982#8894 or Unforgiven774#2535 on Discord.
I couldn't have done it without the help of my friends Unforgiven774 and Khaine himself (creator of Darkness Falls overhaul mod). Thank you so much my friends.
I do hope you all enjoy this modlet.

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[3342ca320b...](https://github.com/crowlogic/arb4j/commit/3342ca320b4b27b04326041b051010474373969f)
#### Monday 2022-06-13 00:46:57 by Stephen Crowley

major fucking headache/splitting out just what i need from the refs,
fucking parser shits on itself and how the fuck else am i gonna get the
damn thing printed

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[95ffcd4e19...](https://github.com/timothymtorres/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Monday 2022-06-13 01:11:38 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [XanderAeon/kotohimegame](https://github.com/XanderAeon/kotohimegame)@[4f0484afa7...](https://github.com/XanderAeon/kotohimegame/commit/4f0484afa7736b522d87dd0235c16479feab9bb4)
#### Monday 2022-06-13 01:24:38 by Aeon

the project file got corrupted! god damn! my computer sucks! thanks git!

---
## [Slary1260/terminal](https://github.com/Slary1260/terminal)@[77215d9d77...](https://github.com/Slary1260/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Monday 2022-06-13 01:41:04 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [gl-prout/linux](https://github.com/gl-prout/linux)@[846bb97e13...](https://github.com/gl-prout/linux/commit/846bb97e131d7938847963cca00657c995b1fce1)
#### Monday 2022-06-13 01:46:22 by Jason A. Donenfeld

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
## [metalgearsloth/space-station-14](https://github.com/metalgearsloth/space-station-14)@[949fbd0194...](https://github.com/metalgearsloth/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Monday 2022-06-13 03:45:25 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [jordanlewis/cockroach](https://github.com/jordanlewis/cockroach)@[13a65d3682...](https://github.com/jordanlewis/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Monday 2022-06-13 05:00:05 by Andrei Matei

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
## [magdalenamae/plantr](https://github.com/magdalenamae/plantr)@[246b1fd141...](https://github.com/magdalenamae/plantr/commit/246b1fd1412b1c8f1db5cd5131d44ab215e0160e)
#### Monday 2022-06-13 06:14:54 by magdalena

Sorry for the last commit, that was a mistake.
Let me know what you think of the sign up frunction and ill incorperate it into the rest of the code later tonight.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[34bafc9f9f...](https://github.com/mrakgr/The-Spiral-Language/commit/34bafc9f9f2165fc690eabfb60fc0f250bf51abf)
#### Monday 2022-06-13 11:26:18 by Marko Grdinić

"9:50am. I am up. Let me chill for a bit and then I will start.

10:15am. https://www.lightnovelpub.com/novel/the-legendary-mechanic-novel-10062255/245-chapter-218

Let me finish this chapter and then I will start.

10:25am. 'Let me finish.' This is the worst thought ever. Now I want to continue reading more. But forget that. I wonder if I should stop posting in /wip/ and Twitter, it does not seem like I am getting any replies right now. Well, either way is fine. Maybe I'll just stick to posting a few variations of finished pieces on Twitter. The readers should come once I start Heaven's Key properly.

At any rate, let me try some of the styles I got. Also regarding the great wave, I'll lower the style strength to 0.8. I forgot about that actually.

I should get the wiki art dataset.

10:30am. Tsk, it is a 25gb direct download. Getting this would drain my internet budget. But let me just do it. Hope it does not break midway.

10:35am. Running style transfer while download is in progress is dangerous. I won't do it again. Forget it for now. It will only take an hour for the dataset to finish downloading.

While that is going on...

Yeah, I need to get started on the next scene. Cities, cities. I also want a scene from below.

Ok, first thing's first. How do I get rid of V-Ray. I'll upgrade Houdini after that.

10:50am. Got rid of V-Ray, but how do I upgrade Houdini. Wasn't there an option directly in the laucher. Why can't I find it?

It seems I need to login into my account in the browser first.

10:55am. Let me have breakfast early here. Right now my internet line is being used up, and I can't do anything until the downloads finish.

11:25am. Done with breakfast. And Houdini has finished updating. Nice.

The Wikiart download has less than 20m left.

Now what is my goal? I want to construct cities, so I should start with a block. After that I'll want to figure out how to model that scene of the earth from just above the atmosphere. Clouds will be trouble. Both Blender and Houdini can model them. Houdini is better. But even so that is only for individual clouds. I am not sure how I should approach the entire area below the atmosphere. I'll have to watch that video start to finish. But for now, let me just focus on modeling cities.

https://www.sidefx.com/learn/world-building/

'Copy pasting real life' This title really caught my attention. Let me take a look and then I'll watch the relevant city videos.

https://www.sidefx.com/tutorials/copy-pasting-real-life/
> Hey guys! In this 1-part-tutorial about terrains you will learn how to create terrain and heightfields from satellite data and then export this using the tools from SideF Labs to generate all different files for Unreal!

Hmmmmm...this strikes me as being really useful. If I end up not using this, I'll be making a big mistake.

OpenTopography.org.

11:40am. Wikiart finished downloading. Let me unpack it. This is the dataset the net was trained on, so I should get better results than random stuff I get from the net. It is really quite slow at unpacking.

The room on auxiliary HDD is rapidly getting consumed. I got it 7 years ago, and so far I've spend 1.8tb out of 3. I'll have to make another partition for that unused free segment.

11:45am. There was a CRC error in one of the rembrant files. Whatever.

1 out of thousands is not a big deal.

12pm. There were a bunch of errors in the zip file, but whatever. This is the disadvantage of getting a huge zip file. The authors should have split the thing up into several pieces.

Right now I am taking a look at the stuff in the file. A lot of it really looks like children's scribbles. In fact it is rare to find something good here.

12:10pm. Yeah, it is not that good. But that does not mean I won't get anything good once I pass them in as styles, so I should just go forward with it. It does not matter too much. All I need is a good variety of latent vectors.

Now me, focus on the Houdini tutorial.

12:15pm. Why is he doing all this? He got the heightfield earlier, is he just resizing it?

I am really falling asleep here, but I am 20m in, so I might as well stick it out for another 14m.

-$YMIN.

I should remember that way of transforming it.

12:35pm. I need a break. This thing has put me to sleep.

https://www.sidefx.com/tutorials/city-building-with-osm-data/

Let me do a little post in /wip/.

///

>I think that I'll grab the 25gb wiki art dataset tomorrow and try a much wider selection of styles.
I've downloaded and checked it out.

Most of the stuff in the dataset looks like crappy children's scribbles, and even the good stuff has a somewhat washed out palette. I haven't tried out style transfer with it though, maybe I'll get something good once I do that.

As I suspected, the standards of modern and old art are on completely different. It really is necessary to make full use of modern tools to get an edge in this field.

///

You know what, let me do that style transfer right now. I'll try it on couple of 100 different images. I've made a mistake trying to watch that random Houdini tutorial, it just ended up sapping my motivation. I need to get back on track.

12:55pm. The full dataset has like 81k files, it would be even more had the downloads not been busted. I've picked about 800. Let me give them a try on the vn cover. This will take a while.

1pm. This really hogs the resources. I regret not having a bigger GPU now.

1:05pm. Let me cancel it. I am satisfied. Let me watch this...

https://www.sidefx.com/tutorials/city-building-with-osm-data/

Now focus me. Do what you need to do. Master city building. With both cities and terrains, nothing will stand in my way.

https://vimeo.com/402297135

This looks really good. I'll be able to do a lot with this. I could model all of this by hand, but it would be really tedious. Literally nobody is going to care whether I rip some scene from the real world, or model it by myself. The way I did the VN cover, and the way I am going to do this is the smart way. An even more effective way of doing things would be to use phograps directly with style transfer, but that could get me sued, which is why I am using an intermediate step.

1:15pm. Let me take a short break here. This tutorial I am going to have to follow step by step. It does not matter if it takes me a few days. Cities are important. It is important that I get them down. Once I have them, they will be a powerful tool in my art arsenal.

A part of art is drawing lines on paper, sure. But when you gain the ability to do in 5m what would otherwise take hours and days, that represents a major advance in power. Beginners focus too much on meaningless grinding. While a pro would do what I am doing now.

The past 8 months were beginner learning for me, it was essentially just a tour of the art landscape. But what I will gain here is the ability to really leave my competition in the dust. This is a good opportunity. Since I've completed the mastery project, let me change the journal file. This one is literally 9.8mb long at this point. It has 188k lines accumulate of over a year of writing. It is time to retire it and start afresh. Right now I am in the 3/5 range as an artist. It will take me a few years, but I should set my sights to 4/5.

With the andvances in technology, it will even be possible to exceed the human limit and reach rank 6. I can only hope that my readers ends supporting me in this endeavor."

---
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[71cbca3021...](https://github.com/input-output-hk/ouroboros-network/commit/71cbca30215c827117425b8f082038b34a390109)
#### Monday 2022-06-13 11:35:38 by Nicholas Clarke

Integrate the Babbage ledger era.

- The BabbageEra is imported from cardano-ledger-babbage and added to
  `CardanoEras` etc.
- A new Babbage era is added to the Shelley codebase, and made an
  instance of `ShelleyBasedEra`. Note the slightly weird
  `TranslationContext` - we need to use the Alonzo translation context
  because of the assumption (in `ShelleyBasedEra`) that the translation
  context is equal to the `AdditionalGenesisConfig`. The latter is a
  diff from `Shelley`, whereas the former is a diff from the previous
  era.

  TODO We should drop this assumption and correct the relationship
  between these things.
- We introduce a new class, `SupportsTwoPhaseValidation`, to reuse code
  for dealing with 2-phase validation in Alonzo and subsequent eras.
- Add standard boilerplate patterns for the Babbage era (particularly in
  Ouroboros.Consensus.Cardano.Block).
- We add additional translation code to translate from Alonzo to
  Baggage. This is slightly more complex than usual, since it must also
  translate from TPraos to Praos. It's generally formulaic, however.
- New protocol versions are introduced supporting the Babbage era.
- `protocolInfoCardano` is expanded with configuration for
  Babbage/Praos. Again, this is largely straightforward.
- Block forging code for Praos is now uncommented, since there is a
  Praos era to work on.
- The block forging code for the TPraos eras is adjusted to add a "skip"
  at the end, for the Babbage era. Honestly, this is rather ugly, but
  it's the simplest approach right now.

---
## [replayio/devtools](https://github.com/replayio/devtools)@[aa62c1e8a1...](https://github.com/replayio/devtools/commit/aa62c1e8a1aac5cef19453014894023735f05df2)
#### Monday 2022-06-13 11:42:30 by Josh Morrow

Make Soft Focus the Default #7114

I've been saying for the past week that we basically already shipped
soft focus, but not technically. I'd like to clarify what I meant by
that, because it's confusing. Let's start from the beginning-ish.

I started [a
document](https://www.notion.so/replayio/Loading-Region-Problems-b8dc0d03c49840f8b504e967c7ea5778)
on April 26th describing an underlying cause for an entire family of
problems that I was seeing in the devtools UI. Around that same time, we
were also seeing a *lot* of crazy behavior with regions loading and
unloading (I'm gonna come back to this). The big takeaway from that
document was that we needed methods for focusing at slices more specific
than regions. We did a lot of work to support this.

- We added range parameters to backend endpoints, so that front-end
  requests could send the range they were interested in, rather than
  always addressing the entirety of all loaded regions
- We reworked how we run, monitor, and store the results of analyses
  generally
- We built two completely new backend endpoints for converting from
  times to TimeStampedPoints
- We built a thunk which observed the focus mode, and decided when it
  should attempt to reload some resources (starting with console
  messages, and then analyses) based on the newly chosen window and
  previous fetches

I'd like to pause at that last one. In many ways, that was the ultimate
goal at the time I wrote that document. It solves all "edge-piece" and
"overflow" problems, and while we can go even farther in the direction
of efficiency, I'm quite happy with the soundness of the foundation
we've laid, and soundness was the motivator for this project.

We shipped the first version of everything up above one week ago, and
sent it out with the newsletter. However, remember how I said that back
when I was first scoping this project we were having a lot of trouble
with loading and unloading regions? Well, one of the things that I
realized early on was that if we correctly handled edge-pieces, it no
longer mattered how big the edge pieces were. And if it does not matter
how big the edge pieces are, then there's no reason to forcibly unload
parts of the recording in order to exclude them. Back when unloading and
loading were causing massive headaches both for us and for users, this
seemed like a huge win, so I made it the final goal of Soft Focus - be
able to move your focus window around, without ever having to unload a
region.

My first shot at it was kind of wonky (you'll see just how wonky in a
second), and I didn't love it. And while we were busy getting everything
ready so we *could* turn this flag on, the rest of the team shipped
Turbo Replay, and all of a sudden, it did not matter that much if we
forcibly loaded or unloaded regions. It's still a nice performance win I
think, for users who are moving their focus window around a lot, and
more importantly, we corrected a ton of soundness problems on the way
here.

---

OK, so back to this change.

The final solution is probably best explained by this comment I wrote
earlier today to explain a type (if you've been deep in the weeds on
this stuff already a lot of this will sound familiar):

>  You might be wondering why there are multiple `begin`s and `end`s for
a single FocusRegion. Well, this is an artifact of the difference
between world-time, which is essentially continuous (and thus, linearly
interpolable), and execution time, which is both discrete (in the sense
that even though there may be many points "between" points 100 and 200,
there may not be any points that are valid for operations like Pausing)
and irregularly spaced (the recording might have many valid points
between the times 100-150ms, but no valid points between 150-500ms).
>
> It is very convenient to accept user input in the form of times. The
user can click somewhere on the timeline (which is really just a visual
interpretation of the continuous, evenly-spaced number line underlying
it), and we can try and use that to filter things down to that time.
>
> And that is where the trouble starts.
>
>  In order to accurately filter resources that are in memory, or to
specify a range to a backend endpoint which accepts ranges, we need to
bound our range by *points*, not just *times*. But the user did not give
us a point, they only gave us a time. So what should we do? Well, we try
to convert from our time to a point. However, because points are
discrete and unevenly spaced, this is not an exact translation, it
introduces a small amount of error (usually on the order of <100ms, but
occasionally more). Also, to be as precise in the conversion as possible
we need to hit a backend endpoint (getPointsBoundingTime), which is not
horribly expensive, but is significantly more expensive than a simple
lookup, for instance.
>
>  All of this causes problems, especially when the user is dragging
around a focus window. This is because:
>  1) The little errors start to add up. If you "snap" the continuous
values of
>  the timeline to the discrete values of the pointline, you introduce a
little bit of error. Then, maybe the user drags the line another pixel,
and you introduce another little error, and so on and so forth and, well
screens have many pixels so this can get out of hand quickly.
>  2) A difference of less than 100ms might not be super noticeable on
the timeline, but as the errors get larger (or if the recording is quite
short, for instance) it will start to be clear to the user that we are
not actually putting them at quite the time that they asked for. And,
well, we have very good reasons for doing that, but they are very hard
to explain (for instance, we might have to subject them to reading
something like this comment).
>  3) If we try and do an exact lookup every time the focus window
changes while selecting it, we will end up sending a *ton* of protocol
messages.
>
>  The solution I have come up with so far is that we store *two*
windows. One window is used for display. It is what we show on
timelines, and it is also what we use as the inputs to our time -> point
transformation *after* the user has chosen their focus window.
>
>  The other time is a proper TimeStampedPointRange, which we use to do
things like filter resources by point and interact with backend
endpoints which accept ranges.

With the above solution, we can ship Soft Focus (in the sense that there
does not need to be any forced unloading) without degrading the
experience of picking a focus window or having to expose the messiness
of the above to the user. Next, will be actually utilizing
`Session.getPointsBoundingTime` to be more specific in our mapping, but
even now, we are pretty darn specific most of the time, so I wanted to
get this in rather than waiting for that optimization piece to be done.

As for the changes this actually makes:

- Deletes the `Soft Focus` flag from experimental settings
- Changes `startTimeForFocusRegion` to `displayedStartForFocusRegion`
- Likewise for `endTimeForFocusRegion` to `displayedEndForFocusRegion`
- Displays the `displayed` time values when choosing a window, rather
  than the mapped-points' time values

That's it! Not a ton of changes, but building on a much larger set over
the past 6 weeks 🏗️

---
## [Blocksrey/Blocksrey](https://github.com/Blocksrey/Blocksrey)@[8c306b6755...](https://github.com/Blocksrey/Blocksrey/commit/8c306b675566b2a9730d71b9c298fd3354352dbb)
#### Monday 2022-06-13 12:10:47 by Jeff Skinner

gotta trick github's stupid fucking caching bullshit

---
## [ImFlynnn/android_kernel_realme_mt6785](https://github.com/ImFlynnn/android_kernel_realme_mt6785)@[469a006517...](https://github.com/ImFlynnn/android_kernel_realme_mt6785/commit/469a006517ad46a1bc141bf9e7356f97edeb8f0b)
#### Monday 2022-06-13 13:07:06 by Wang Han

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
Signed-off-by: officialputuid <officialputuid@hack.id>

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Monday 2022-06-13 13:08:47 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[e883348f8a...](https://github.com/dfinity/motoko/commit/e883348f8a35c0925d7363cc6b9488fdac261a29)
#### Monday 2022-06-13 14:17:54 by Gabor Greif

feat: introduce array-slice processing for compacting GC (#3231)

This PR introduces a modified marking (and visiting) technique for array fields, where `Array`s are GC-ed by considering their suffixes as slices, pushing these on the mark stack as bulk collections, and treating the fields in the prefix as individual objects being pushed onto the mark stack.

Following key changes are made:
- when visiting an `Array` in the dynamic heap we consult a new callback that can opt-out of the individual processing of some suffix of the array (by returning an index smaller than the array length)
- fields before this index will be processed as before by the first callback
- for the suffix the new callback is in charge to perform the bulk action
- in case of array marking, the new callback checks if the current slice is longer than some cutoff, and if so, it will push the array and the start of the suffix to the mark stack. (We abuse the tag entries as the start index for the suffix slice, so the cutoff must be numerically bigger than the biggest heap tag; this invariant is enforced)
- when pulling entries `(obj, tag)` from the mark stack a `tag >= TAG_ARRAY_SLICE_LOW_LIMIT` indicates that we have to deal with a suffix slice of an `Array`. The visitor will then again check the slice's length and do the subdivision again, as necessary.

This way of treating suffix-slices as pseudo-heapobjects originates from the suggestion of @ulan in a SGM (2022-05-30). It sidesteps the issue with layering violations, and restricts the handling of pseudo-tags to a very restricted portion of the collector source code, viz. the pushing of the range, and the visitor's case analysis on the tag, which now needs to  know about the suffix slices. Fortunately the visitor already accepts the heap tag as an argument (and doesn't extract it from the object; which would be unreliable due to threading), so the appearance of pseudo-tags is not a big deal.

The cutoff is currently chosen as 127, so for any `Array` at most 128 new entries are being placed on the mark stack.

The charm of this solution is that the same code is doing the marking pushing/popping and visiting as before, only that now it happens in an interleaved manner. The mark is already present on the array, so no reëntrancy can't occur, and eventually all its fields get processed.

-----

Below is an account of how field-by-field marking, pushing and visiting was done formerly (still in use for prefix portion of arrays), and an aborted attempt to a scheme as suggested by @osa1. I leave it for reference.

----------
See #2903. This reduces the marking stack traffic for GC-ed arrays substantially. Not applicable to copying GC!

## Status quo

Here is what happens to an array object's (single) field while `mark_fields`:
 - considered only when it is a skewed pointer and points into the dynamic heap (otherwise it is a _static object_ or a _magic_, no need to GC)
 - visitor callback is invoked:
   - `mark_object` will place a bit and push to the mark stack when not marked yet
     (when being pushed onto the mark stack the (unskewed) pointer and the heap tag are remembered)
   - the field address gets `thread()`-ed when the contained object is physically located at a less or equal address than the array itself
     (threading will put the field address into the object tag saving the tag into the word where the field address points to; the old object pointer is overwritten, but may live on in the mark stack)

## How bulk marking could work (ABANDONED)

When discovering a sequence of value fields that are laid out successively in memory and a count field in front, we can do a bunch of nice shortcuts. Below items sketch the how this could work. Invariant: there must be a tag field immediately before the length field.

- the bulk visitor callback gets called with a pointer to the length field
- it decides that it is worth doing a ranged marking and divides the bulk into a (small) prefix and a non-empty suffix `(pointer_to_length, start_index)`
- set all marks corresponding to (dynamic heap) objects in the suffix to avoid re-visiting (see [open issue](#Revisit-avoidance-is-more-complicated))
- push `(pointer_to_length, start_index)` onto the mark stack, using low bits in the pointer to differentiate from `(obj, tag)` pairs
- bulk visitor callback returns the prefix length, the fields in this area will be visited individually

When it comes to popping the mark stack and there is a field range on its top we want to be as transparent as possible, but also have to perform steps that had to be skipped (relative to the proceeding on individual fields)

 - identify that the ToS is a range `(pointer_to_length, start_index)`
 - obtain a pointer to the field indexed by `start_index`
 - increment `start_index` (still remains on the stack)
 - if  `start_index` is equal to the length, pop the entry
 - check that the field is a GC-able pointer
 - if so, extract the object and the heap tag corresponding to the field
 - otherwise pop again and return that
 - apply the threading to the field address (use the invariant to get the home object and apply the threading criterion)
 - return the object and the heap tag

## Open issues

There are some ugly wrinkles in this design, that need to be addressed somehow.

### Revisit avoidance is more complicated

An object is either unmarked, in the mark stack or is being (has been) visited. When pushing entire ranges, we cannot process individual objects and as such marking and threading may happen in unexpected ways.

#### Saving the marked bit

When eagerly marking the whole range of fields, we must not drop the info whether the individual mark is already set. This is because a mark means that either an object is in the mark stack or being/have-been visited. We have two possibilities:
- mark range eagerly on push, but remember previous marks (e.g. in the unused bit of the `Value` in the fields), or
- instead mark lazily on popping an object from the range, performing the threading anyway, but never returning already marked objects.

The latter option is in conflict with what #2903 suggests, and could potentially invalidate the idea of pushing ranges at all.

#### Intervening `thread()` call after range marking

After a range has been pushed and all dynamic objects marked, an individual field with an object also referenced by the range might become threaded. In this case the tag field of that object gets overwritten, but can be distinguished from regular tags. Such objects got individually pushed and already popped from the stack, and thus have been visited. So the field in the range must be threaded, but the pointed object must be skipped (not visited again).

### Layering violation

The fact that the `pop_mark_stack` needs to know about object layout and then how to do the threading is disgusting.
Maybe there should be a callback parameter that is invoked then a non-pointer (i.e. range) entry is encountered in ToS position.

### `pointer_to_dynamic_heap` needs the heap base

If `pop_mark_stack` is to check pointers for pointing into the dynamic heap, it needs to receive the heap base, but it currently doesn't. It is open if the caller has this piece of information. (It has, what a relief!)

### Special format of `usize` passed to `push_mark_stack` and `push_range_mark_stack`

Distinguishing by the lowest bit is hacky.

## Further improvement opportunities

I spotted below optimisation tricks while reading the code.

 - `pointer_to_dynamic_heap` unskews a lot, why not compare with a `heap_base` that is 1 less?
 - `mark_object` doesn't need to get the previous mark (`bool`), but compare the (64-bit) word the mark is in whether it changed
 - `mark_object` unskews. Would it be possible to do `set_bit` using the `raw_ptr`?
 - `field_value.get_ptr() <= obj` could be `field_value.raw_ptr() + 1 <= obj` and further `field_value.raw_ptr() < obj` saving us an addition
 - can the double storing of the heap tag (by `thread` and `push_mark_stack`) be consolidated?
   (we have 2 cases for whether `thread` happens and 2 cases whether the `push_mark_stack` happens)
 - can the dynamic heap pointer check be reduced to a shift and a comparison with `BITMAP_FORBIDDEN_PTR` (at least while marking, as it is not available in copying GC)?

---
## [phohtoo/sidetree](https://github.com/phohtoo/sidetree)@[c19a1ec7ec...](https://github.com/phohtoo/sidetree/commit/c19a1ec7eca4a5d9ff24989b1f37a6ac6eff40f7)
#### Monday 2022-06-13 17:18:38 by Henry Tsai

fix(ref-imp): fixed an integer precision bug in how transaction number is constructed

This was discovered in https://github.com/decentralized-identity/ion/issues/240

As a result, rewrote how transaction number is constructed to produce a smaller integer. Also took the opportunity to make the transaction number much more human-friendly also, the current transaction number format had been annoying me for a long time.

Specifically, the current transaction number is simply a large ugly looking number that doesn't make any sense to a human. It would be much easier to make sense of (thus debug), now that a transaction on index position 500 in block 777777 is 777777000500, as opposed to 3340526778581492. Notice the number is smaller AND easier to make sense of.

Also, due to this internal transaction number scheme change, both core and blockchain service will be required to be upgraded to the same build at the same time, a bit painful, but isn't worth more engineering time IMO to mitigate this inconvenience.

---
## [Unittellie/Remixed-Mappack-Github](https://github.com/Unittellie/Remixed-Mappack-Github)@[4caf492f94...](https://github.com/Unittellie/Remixed-Mappack-Github/commit/4caf492f945fcdece999ecfebd43ddfcfdbc9a0c)
#### Monday 2022-06-13 18:05:41 by Unittellie

Not Funny. Didn't Laugh

Not funny I didn't laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didn't even feel the slightest twitch. 0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brain power you must have put into that joke has the potential to power every house on Earth. Get a personality and learn how to make jokes, read a book. I'm not saying this to be funny I genuinely mean it on how this is just bottom barrel embarrassment at comedy. You've single handedly killed humor and every comedic act on the planet. I'm so disappointed that society has failed as a whole in being able to teach you how to be funny. Honestly if I put in all my power and time to try and make your joke funny it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it, and even then all that joke would get from people is a subtle scuff. You're lucky I still have the slightest of empathy for you after telling that joke otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again. We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure. Im disappointed, hurt, and outright offended that my precious time has been wasted in my brain understanding that joke. In the time that took I was planning on helping kids who have been orphaned, but because of that you've waisted my time explaining the obscene integrity of your terrible attempt at comedy. Now those kids are suffering without meals and there's nobody to blame but you. I hope you're happy with what you have done and I truly hope you can move on and learn from this piss poor attempt

---
## [pinklittleman/new](https://github.com/pinklittleman/new)@[78e92d8bbd...](https://github.com/pinklittleman/new/commit/78e92d8bbd05082587bc1bed938aa7ccfa5b8e4c)
#### Monday 2022-06-13 20:14:27 by theo

hell has open to swallow you whole so dont keep the devil waiting old friend

---
## [crash5band/MikuMikuWorld](https://github.com/crash5band/MikuMikuWorld)@[8c867ec8b1...](https://github.com/crash5band/MikuMikuWorld/commit/8c867ec8b1b127fae8f6fbf82af2c1aa1184f26c)
#### Monday 2022-06-13 20:32:28 by Crash5b

Fix importing .sus files with multiple time signatures

i hate my life

---
## [em3ndez/canvas-lms](https://github.com/em3ndez/canvas-lms)@[a403ea1af0...](https://github.com/em3ndez/canvas-lms/commit/a403ea1af0c5ccc59b803ba65962471f0c1074d5)
#### Monday 2022-06-13 20:35:02 by Evan Battaglia

Fix inconsistent plagiarism report permissions

Previously, due to permissions pecularities, if the plagiarism report
visibility was set to "never", teachers would not be able to view
plagiarism reports after their enrollments were "concluded" (due to them
not having the "manage_grades" permission then). This was inconsistent,
however, since the score would still show on speedgrader (but not the
submission page) but clicking it would error when trying to view the
report. Also, preventing them from seeing reports is especially
nonsensical since the teachers are usually the ones to set up the
assignment plagiarism report visibility which prevented them from
viewing them.

This commit makes the permissions for on the submissions page, and
actually viewing the report, nearly the same as that for using
speedgrader, although is difficult to get perfect. The permissions for
speedgrader are:
  - to use speed grader at all:
    manage_grades OR view_all_grades
  - additionally, the turnitin score is only shown if
    manage_grades OR (@context.concluded? && can_do(@context, @current_user, :read_as_admin))
    (see app/views/gradebooks/speed_grader.html.erb:235)

This commit brings the permissions for showing the score on the
submissions page, or viewing the report, to:
  - manage_grades OR view_all_grades

This means it's still possible for some cases for the score / report to
be visible from the submission page, but not from speed grader -- if:
  - the user can view_all_grades
  - the user cannot manage_grades (in the ticket this was just because
    the course/teacher enrollment was concluded)
  - the course is not concluded OR the user cannot read_as_admin

This seems like it should be very rare and I'm not sure it's worth
trying to tweak the permissions in speedgrader (which honestly I don't
understand well -- there may be some other reason for limiting what is
shown in speedgrader) or making the conditions for viewing the report as
complex as those in speedgrader. And, the risk is only that the score
will not show in speedgrader but will in the submission, not that there
will be any broken link.

fixes INTEROP-7312
flag=none

Test plan:
- setup to repro the original problem. Here is how I did this:
  - set up plagiarism platform in an assignment with report visibility
    "never" (students can never view reports). I used the
    lti_originality_report_example tool.
  - as a student, submit to the assignment
  - create an originality score/report for the submission. I used tok
    (Set up to get a token with the lti_2_token endpoint):
      tok web.canvas-lms2.docker/api/lti/assignments/469/submissions/1428/originality_report \
        originality_report[originality_score]=33 \
        originality_report[workflow_state]=scored \
        originality_report[originality_report_url]=http://example.com/123
  - make the course concluded
      course.update workflow_state: :completed
    that wil make all the enrollments also "completed".
- Make sure the original problem can now be repro'd: In this scenario
  (with the code before this commit), when viewed as a teacher, the
  submission page (e.g. courses/123/assignments/456/submissions/789,
  where 789 is the user id) should not show a plagiarism score;
  speedgrader will show a score, but when clicked, no report will be
  viewable.
  NOTE: it seems like I had to run "AdheresToPolicy::Cache.clear" and/or
  "Rails.cache.clear" for permissions to get updated when switching code
  for some reason.
- with this code checked out, make sure that:
  - the score shows up on speedgrader
  - clicking it works to show the report
  - the score shows up on the submission page and clicking it works to
    show the report
  - as a student, the score should NOT show up on the submission page

Change-Id: I6d527884205bb48de6dda98f9eac96939834f2f5
Reviewed-on: https://gerrit.instructure.com/c/canvas-lms/+/293531
Tested-by: Service Cloud Jenkins <svc.cloudjenkins@instructure.com>
Reviewed-by: Tucker Mcknight <tmcknight@instructure.com>
QA-Review: Xander Moffatt <xmoffatt@instructure.com>
Product-Review: Alexis Nast <alexis.nast@instructure.com>

---
## [jlherren/andeo-lunch](https://github.com/jlherren/andeo-lunch)@[09a0991c93...](https://github.com/jlherren/andeo-lunch/commit/09a0991c9377063f5f28a43c674ddc6d0bac98af)
#### Monday 2022-06-13 20:36:20 by Jean-Luc Herren

App: Reword help text for lunches

Lunches can in theory be used for breakfasts and dinners, but that is highly
unlikely to be the correct choice, because default-opt-ins are usually not
desired in these situations.

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[436132621c...](https://github.com/payday-restoration/restoration-mod/commit/436132621c713306cba351b474199cc75d3d60ad)
#### Monday 2022-06-13 21:26:32 by Noep

.30-06 stopping power

-Reduced the range but increased the minimum damage of the M1 Garand
--Also fuck you, Woody :)

---
## [jeffday/dayzserver](https://github.com/jeffday/dayzserver)@[8301c4594a...](https://github.com/jeffday/dayzserver/commit/8301c4594a7af05d0368785349dc18ccd20d7d7a)
#### Monday 2022-06-13 21:29:07 by Jeff Day

oh my fucking god. shoutout to Beelo for helping me realize i am an idiot

---
## [vries/gdb](https://github.com/vries/gdb)@[80c0a3bf1b...](https://github.com/vries/gdb/commit/80c0a3bf1b949403521d186fc04ed9052ea1d7d4)
#### Monday 2022-06-13 22:17:49 by Andrew Burgess

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
## [fajar3109/kernel_xiaomi_ginkgo](https://github.com/fajar3109/kernel_xiaomi_ginkgo)@[6f861103e7...](https://github.com/fajar3109/kernel_xiaomi_ginkgo/commit/6f861103e713482bb567c8e0a530f2e2d516f865)
#### Monday 2022-06-13 22:20:49 by George Spelvin

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
Signed-off-by: fajar <santuyz321@gmail.com>

---
## [furrybrackets/Lighthouse](https://github.com/furrybrackets/Lighthouse)@[81d5c6fbaf...](https://github.com/furrybrackets/Lighthouse/commit/81d5c6fbaf019faaf3f43ea5932150b349e3395c)
#### Monday 2022-06-13 23:50:09 by Peter Johnson

FUCK YES LETS GO NUMBERS FUCK YOU TORCHLIGHT.DEV PAYWALL BULLSHIT

---

