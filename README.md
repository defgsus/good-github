## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-18](docs/good-messages/2023/2023-05-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,118,327 were push events containing 3,517,819 commit messages that amount to 242,141,186 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 61 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[303cfa3bbb...](https://github.com/tgstation/tgstation/commit/303cfa3bbb2199b24df17e87864d92e038a32dca)
#### Thursday 2023-05-18 00:20:09 by GoldenAlpharex

Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable (#75489)

## About The Pull Request
I have been debugging this stupid macro for the past nearly five hours,
to finally figure out why it was breaking. If you had something like `a
|| 0` in what you called the macro with, it would somehow manage to
break the cache. This makes it far more foolproof, and will ensure that
it doesn't break here anymore, because debugging this has to be one of
the biggest pains in my ass I've ever had.

## Why It's Good For The Game
So shit like this

![image](https://github.com/tgstation/tgstation/assets/58045821/455122b0-34eb-4ec0-92dd-2775c1f0f878)

Doesn't end up breaking your CI (or even worse, the game in prod), in
places unrelated. At least now it shouldn't be overwriting values in the
cache.

It shouldn't have to do verification that you're doing the right thing,
that should be left on the person using the macro because it was meant
to be faster than a proc call, adding too much verification overhead
kind of just loses some of that speed.

## Changelog

:cl: GoldenAlpharex
fix: Makes checks for the station z level more robust against coders
doing less intuitive stuff, thus protecting it from breaking in weirdly
difficult and seemingly unrelated places (I'm looking at you, nuke
cinematic unit test).
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[835952ccf4...](https://github.com/effigy-se/effigy-se/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Thursday 2023-05-18 00:24:21 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...


![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11


![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

---
## [SethLafuente/tgstation](https://github.com/SethLafuente/tgstation)@[bc22fefe3b...](https://github.com/SethLafuente/tgstation/commit/bc22fefe3b1de4d882dd87a5492344672230736d)
#### Thursday 2023-05-18 00:25:37 by Helg2

Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

---
## [SethLafuente/tgstation](https://github.com/SethLafuente/tgstation)@[2845c985fa...](https://github.com/SethLafuente/tgstation/commit/2845c985fab04b0de1f7615799a260527af30822)
#### Thursday 2023-05-18 00:25:37 by Rhials

Adds a revolutionary conversion stinger (#75002)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds an antagonist gain stinger for Revolutionaries, created with
inspiration from the obsessed/traitor conversion sounds.


https://user-images.githubusercontent.com/28870487/235028674-170a4f9e-a873-4938-a700-536f005e539f.mp4

Raw audio:


https://cdn.discordapp.com/attachments/440978216484732934/1101964419203862548/revolutionary_tide.ogg

_A distant, hypnotic whistling. The heavy footfalls and clamoring voices
of an approaching crowd. The unstoppable revolutionary tide breaks its
waves upon an unsuspecting station._

I wanted to try and make something that felt like it fit in with the
other antagonist stingers we already have. Let me know what you think!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gives a bit more flavor, and helps set the mood for the upcoming
bloodbath.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

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
sound: Revolutionaries now have their own stinger that plays upon
becoming that antagonist.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [chromium/chromium](https://github.com/chromium/chromium)@[5af88dafc9...](https://github.com/chromium/chromium/commit/5af88dafc9ee01bdfc76c82c14533e9705a0acb2)
#### Thursday 2023-05-18 00:27:41 by Andres Calderon Jaramillo

OOP-VD: Kill utility process when all decoders in it die.

A renderer process can create a media::mojom::VideoDecoder during start
up in order to query the supported video decode acceleration
configurations. With OOP-VD, this causes the creation of a utility video
decoder process. Before this CL, this process would stay alive even
after the renderer process tore down the connection to it. That means
that there would always be one utility video decoder process per
renderer process that behaves as above. In practice, this has dire
memory pressure consequences since each utility process consumes some
memory even if it isn't doing any work.

The reason the video decoder process stays alive is that the only thing
that happens in this process when a StableVideoDecoder is disconnected
is that a mojo::Receiver<StableVideoDecoder> is removed from a
mojo::UniqueReceiverSet. As long as the StableVideoDecoderFactory and
StableVideoDecoderFactoryProcess connections stay alive, the process
stays alive. The StableVideoDecoderFactory is maintained by the browser
for each RenderProcessHostImpl. The browser process doesn't know when
all the StableVideoDecoder connections have ended, so it doesn't know
when to destroy the StableVideoDecoderFactory connection.

This CL adds code that destroys the StableVideoDecoderFactory connection
once all the StableVideoDecoders created with it have died. The approach
is to add a StableVideoDecoderTracker interface with no methods. The
browser process sends a mojo::PendingRemote<StableVideoDecoderTracker>
at the moment of calling
StableVideoDecoderFactory::CreateStableVideoDecoder(). When the created
StableVideoDecoder dies, the StableVideoDecoderTracker connection also
dies. The browser process can handle this disconnection and destroy the
StableVideoDecoderFactory when all StableVideoDecoderTracker connections
die.

>>> Q&As about this approach:

- Why not just handle a disconnection of the
  mojo::Remote<StableVideoDecoder>?

  The browser does not own a mojo::Remote<StableVideoDecoder>. The
  browser only acts as a broker to establish a StableVideoDecoder
  connection, but it sends the mojo::PendingRemote<StableVideoDecoder>
  to the GPU process where it's bound to a
  mojo::Remote<StableVideoDecoder>. The GPU process can't control the
  state of the StableVideoDecoderFactory connection, so we can't use a
  StableVideoDecoder disconnection event in that process for our needs.

- Ok, so why not handle a disconnection of the
  mojo::Receiver<StableVideoDecoder> then?

  This was actually my initial approach. We already have code that
  handles the disconnection of the
  mojo::Receiver<StableVideoDecoderFactory> in the utility process [1];
  when that happens, we disconnect the
  mojo::Receiver<StableVideoDecoderFactoryProcess> [2] which should
  cause the utility process to die. This handles things like a renderer
  process dying. I had extended this to also handle a disconnection of
  each mojo::Receiver<StableVideoDecoder>: when there were no more
  connected mojo::Receiver<StableVideoDecoder>s we could destroy the
  StableVideoDecoderFactoryProcess connection. This was mostly fine but
  there was a timing problem. To illustrate, consider the following
  sequence of events under this hypothetical implementation:

  1) A renderer process requests one mojo connection to do hardware
     video decoding. Suppose this is the only video decoding connection
     (e.g., there's only one video playing).

  2) To satisfy this, the browser process starts a video decoder utility
     process to host a StableVideoDecoderFactory. It establishes a
     StableVideoDecoder connection using the
     mojo::Remote<StableVideoDecoderFactory>.

  3) The renderer process terminates its connection.

  4) The termination of the first connection causes the
     StableVideoDecoder connection to die. Because it's the only one so
     far, the video decoder process gets destroyed.

  5) The renderer process starts a new connection. (3) and (5) may
     happen if the renderer process wants to start playing another
     video.

  6) Suppose the browser process hasn't gotten notified of the video
     decoder process termination from (4). That means that it thinks the
     mojo::Remote<StableVideoDecoderFactory> from (2) is still connected
     so it re-uses it to establish the StableVideoDecoder connection we
     need for (5).

  In reality, since the StableVideoDecoderFactory connection from (2)
  has already died, the "established" StableVideoDecoder connection in
  (6) is bogus, so it can't be used for video decoding. Ultimately, this
  will cause the renderer to fallback to software decoding.

  Therefore, it's not good enough to monitor the
  mojo::Receiver<StableVideoDecoder> as the race condition described
  above may become problematic in practice.

  With the solution implemented in this CL, we don't need to worry about
  this scenario since the browser process will know exactly when the
  StableVideoDecoderFactory connection dies due to all the
  StableVideoDecoders having died.

>>> Versioning considerations:

It proved difficult to make this CL work smoothly with an older version
of the StableVideoDecoderFactory interface. However, that's not much of
a problem in practice. The only scenario where version skew can occur is
with LaCrOS. OOP-VD for LaCrOS was enabled by default starting in M114,
but I have landed CL:4532897 that disables it back in M114. OOP-VD for
LaCrOS is still enabled by default on ToT. Therefore, in practice, end
users should always use OOP-VD with the changes introduced in this CL
(both for the client and the service). That's unless they run a weird
setup of, e.g., a newer lacros-chrome canary/dev with an older
ash-chrome canary/dev. Instead of trying to handle this version skew
which would have added more complexity for little benefit, I've added a
RequireVersion() in this CL. Here are the worst-case scenarios with
OOP-VD enabled (which is the case for LaCrOS on ToT):

- lacros-chrome with this CL + ash-chrome without this CL:

  The StableVideoDecoderFactory connection should die almost immediately
  due to the RequireVersion(). This should cause all hardware video
  decode requests to fallback to software.

  As M115 progresses, this should become a very rare scenario.

- lacros-chrome without this CL + ash-chrome with this CL:

  The StableVideoDecoderTracker connection is optional. In this
  scenario, ash-chrome should receive a null
  mojo::PendingRemote<StableVideoDecoderTracker> which is fine, but
  things will just behave as before this CL: hardware video decoding can
  still be done, but the "leak" of video decoder processes will be
  there.

  As M115 progresses, this should also become a very rare scenario.

[1] https://source.chromium.org/chromium/chromium/src/+/main:media/mojo/services/stable_video_decoder_factory_service.cc;l=182;drc=dfc607e946e8862d54aa06d7c63e5b617e88f56f
[2] https://source.chromium.org/chromium/chromium/src/+/main:media/mojo/services/stable_video_decoder_factory_process_service.cc;l=48-50;drc=a1abb372f2784fb1264e8fc4815255f410e1a2be

Bug: 1444970, b:195769334
Test: on brya, crosvideo.appspot.com on lacros-chrome while monitoring the task manager
Test: unit tests
Change-Id: I07ce73348fafd209802c82884550804478f2dfa9
Reviewed-on: https://chromium-review.googlesource.com/c/chromium/src/+/4538864
Reviewed-by: Dale Curtis <dalecurtis@chromium.org>
Reviewed-by: Alex Moshchuk <alexmos@chromium.org>
Reviewed-by: Alex Gough <ajgo@chromium.org>
Reviewed-by: Pilar Molina Lopez <pmolinalopez@chromium.org>
Commit-Queue: Andres Calderon Jaramillo <andrescj@chromium.org>
Cr-Commit-Position: refs/heads/main@{#1145724}

---
## [momentum-mod/website](https://github.com/momentum-mod/website)@[364535d202...](https://github.com/momentum-mod/website/commit/364535d202ae90353a1b407a6992de24964929b6)
#### Thursday 2023-05-18 00:30:19 by tsa96

refactor(front): Remove SmartTableService

What the fuck even was this lmao? Bunch of random mocks in our actual services? Hell yeah!

---
## [sjp38/linux](https://github.com/sjp38/linux)@[9a402bdc8f...](https://github.com/sjp38/linux/commit/9a402bdc8f90c6dec7c541d516fcbb5ab9407039)
#### Thursday 2023-05-18 00:52:10 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead. 
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[856955c45a...](https://github.com/Superlagg/coyote-bayou/commit/856955c45acda58a4ebab15a67ce4d6e96280e4a)
#### Thursday 2023-05-18 01:20:15 by Tk420634

Redlick & Garland City Take 2

Fuck you to, strong dmm

---
## [Beinsezii/ompl](https://github.com/Beinsezii/ompl)@[f06aebd42b...](https://github.com/Beinsezii/ompl/commit/f06aebd42b9daa4ea955e5678cfcfc73f0098b83)
#### Thursday 2023-05-18 01:37:41 by Beinsezii

SYMPAL Rest of the fucking owl

Should be completely up-to-spec with the rodio backend now.

Tested with PipeWire mp3+ogg+flac.

Hypothetically nothing stopping it from working on other audio formats.
Everything is still upcast to 32-bit right now which
is memory intensive though...

Plus it also still maxes a thread. I could insert a nano-second sleep
in there to help but I'm not sure that'd be desireable on anything
but the most potato of computers. If you're on a RasPi you're probably
not using this player anyways. Would it even compile on ARM..?

Windows untested as of writing this. Not sure if using pulse-alsa or
native alsa will be any different from pipewire-alsa either. The only
issue I can see is no F32 support somewhere.

While it's technically possible to write generic code for handling
any->any sample format, donig so *sanely* is TBD.

Also bonus points if some format I've never used has planar stereo
instead of interleaved causing a
"Help my audio is stuttery/crackly/mono" bug report in the near future.

Additionally, right now I always just play the first track.
Honestly I'm content to leave it as multi-track music files arent really
a thing, and IDK who in their mind is playing video clips in a music
player. Rodio probably does the same thing I'd imagine.
Who knows, might get proven wrong again...

Uhhh what else..?

I love you.

---
## [TalkingCactus/coyote-bayou](https://github.com/TalkingCactus/coyote-bayou)@[6fd64b92ca...](https://github.com/TalkingCactus/coyote-bayou/commit/6fd64b92ca4cc80357d8d78c8efc1c6d8196204f)
#### Thursday 2023-05-18 01:43:41 by Tk420634

Updating the Mansion a bit

Preparing my brain for making a non euclidian dungeon, because I fucking hate everything.

---
## [BasapuramBasavaraju/JAVA-FULLSTACK-](https://github.com/BasapuramBasavaraju/JAVA-FULLSTACK-)@[38889fa994...](https://github.com/BasapuramBasavaraju/JAVA-FULLSTACK-/commit/38889fa994ce32cefca014e90e65f1445d4dad56)
#### Thursday 2023-05-18 02:01:30 by BasapuramBasavaraju

Create Three Idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line. 

Input Format: 

Input consists of 4 integers. 

The first integer corresponds to x1 . 

The second integer corresponds to y1. 

The third and fourth integers correspond to x2 and y2 respectively. 

Output Format: 

Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]

Sample Input:

 2

 4

 10

 15

Sample Output:

Binoy's house is located at (6.0,9.5)

---
## [FeenieRU/Shiptest](https://github.com/FeenieRU/Shiptest)@[7df4885117...](https://github.com/FeenieRU/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Thursday 2023-05-18 02:04:48 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [BasapuramBasavaraju/JAVA-FULLSTACK-](https://github.com/BasapuramBasavaraju/JAVA-FULLSTACK-)@[566733b565...](https://github.com/BasapuramBasavaraju/JAVA-FULLSTACK-/commit/566733b565c7f623fcb775fbc5e1b3ed505ff222)
#### Thursday 2023-05-18 02:06:37 by BasapuramBasavaraju

Create Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

Input & Output Format:

Input consists of 4 integers.

First value consists of x1.

Second value consists of y1.

Third value consists of x2.

Fourth value consists of y2.

Output consists of two float values.

Sample Input
2

4

10

15

Sample Output

6.0
9.5

---
## [iguessthislldo/OpenDDS](https://github.com/iguessthislldo/OpenDDS)@[8029f5acbc...](https://github.com/iguessthislldo/OpenDDS/commit/8029f5acbcf34349f860474d8a1fc67524fa4fa1)
#### Thursday 2023-05-18 02:12:45 by Fred Hornsey

Generate News in Sphinx From Fragments

The current way of generating the news for releases mostly consists of
generating a spreadsheet of PRs, editing that, and creating the new
entries from that manually. More info on that process
[here](https://opendds.readthedocs.io/en/master/internal/release.html#update-files-in-the-repo-as-needed)
and [here](https://github.com/OpenDDS/OpenDDS/blob/f511b1f1582664ab7f49b3b012b968e684928aa2/tools/scripts/release_notes/README.md).
News entries can be directly committed in the PR where the change is
taking place, but doing that risks merge conflicts.

Overall this process is somewhat messy and limiting:

- Deciding what's newsworthy, what exactly to write, and reviewing the
  news is done all at once right before the release, sometimes months
  after the work was done. This makes it harder to remember what's
  newsworthy, what specific things needs to be pointed out to users, and
  what PRs should go together for single news item. This also means it
  takes more time to prepare the release and there's less time to spot
  and correct mistakes in the news or improve it.
- Most of the time the news item is left as just the title of PR. In the
  best case these might not need to be tweaked much or at all for
  changes that require little explanation. However this is certainly
  inadequate for explaining larger changes, for example like for [the
  XTypes fixes from PR4078](
  https://github.com/OpenDDS/OpenDDS/blob/f511b1f1582664ab7f49b3b012b968e684928aa2/NEWS.md?plain=1#L49).
  It'd be very awkward to write that much in a spreadsheet.
- It's hard to link to documentation. This is better than it was before
  with the PDF devguide, when it was impossible, but this could still be
  improved on more. Linking would give more context to users and could
  immediately give them details on use a new feature.
- Contributors outside the OpenDDS maintainers basically have no direct
  input on what the news says for changes they contribute. Honestly I'm
  not sure if any have wanted to, but they couldn't if they did.

The solution in this PR is committing the news of changes of a PR as a
file in that PR. At release these fragments of the news are
brought together automatically. There are still a few kinks to iron out,
but even if those are mostly unresolved I think this system will improve
the quaility of the news.

The system is inspired by [Python's blurb
tool](https://pypi.org/project/blurb/) and to a lesser extent tools like
[towncrier](https://towncrier.readthedocs.io/en/stable/index.html).
These tools are not bad, but they have some serious drawbacks. blurb is
specifically tailored for CPython development. For example, it's
oriented by GitHub issues, where as many of the changes we make are not
prompted by a GitHub issue. towncrier really expects the project to be a
Python project and has some quirks for some of use cases I was looking
for. Specifically needing multiple identical files for to attribute a
news item to multiple PRs and needing multiple files for a PR to have
different kinds of changes. Also both rely on the files having a
specific name, which seems unnecessary to me.

The following is the basics of adding a news fragment and how the news
is generated in this system:

Create a rst file in `docs/news.d/`. This is a news fragment. It can be
named anything as long as it doesn't have an leading underscore and is a
rst file, but it should be somewhat descriptive. Naming it the same as
the branch the change is on might be good idea. The change must be a rst
list. It has to have some rst-directive-like metadata around it. A
minimal file looks like this:

``` rst
.. news-prs: 5000
.. news-push: Additions
- This is an addition we made.
.. news-pop
```

Additional PRs are added by appending them to end of the `news-prs`
line. Additional `news-push`s and `news-pop`s can be used to add list
items to other sections, like fixes, or to create nested sections for
groups of changes like like "XTypes" or "RTPS". All sections will be
merged together in the final result. These sections and items are sorted
first by a quality called rank, then by the PR numbers in reverse order
(basically chronological). The rank is changed by `.. news-rand:
RANK_NUMBER`. It can be used to headline an important change or set of
changes,

See `docs/news.d/_example.rst` for a longer example. I also have added a
recreation of the 3.24.0 news as fragments as a test and a full example
of what this would look like.

Before release a preview of the news entry will always be available in
the built version of `docs/news.rst`. The means news added in an PR can
be previewed in the PR. During a release the fragments are permanently
committed to that file and the fragment files in `docs/news.d` are
removed.

Here are the two main issues I see with this system right now:

- To do a PR with a news fragment in one commit, you basically have to
  know what the PR number is going to be before hand. Otherwise another
  commit is needed to add the PR number. The PR number could technically
  be manually added after the PR is merged, but I would consider that
  poor practice. One solution could be a placeholder in `news-pr`
  statement that an action automatically replaces with the PR number
  after the PR is merged.
- How does this relate/integrate with `NEWS.md` and the GitHub release
  notes? I'm honestly a little stumped by this and unlike the other
  issue this needs to be figured out before this can be merged.
  - Something like pandoc could be used to convert the rst, but it would
    still need some manual intervention based on tests I did with the
    3.24.0 news.
  - The markdown version could just be a summarized version of the news,
    mostly consisting of highlights. This could be manually done or done
    with pandoc with human intervention. Also this summery could be what
    goes out in a prerelease announcement on social media.
  - The `NEWS.md` file could be also be done away with to simplify
    things. If that's the case, shuold news.rst live in the root
    directory and be called `NEWS.rst`? Is that going to case problems to
    try to include it in Shpinx?
  - The GitHub release notes could just link to `news.rst`, but I feel
    like they probably should at least have a summery.

Besides that there are some more things I needs to do, specifically:

- Document either in the documentation guidlines or dev guidelines how
  to add to the news.
- Improve release entries, it needs the release date and output could be
  tweaked.
- Maybe add two smaller examples just for "Additions" and "Fixes"
  without comments that are eaiser to use as templates.
- Before merge, remove 3.24.0 fragments, add any newer releases, and add
  any news fragments for a pending release.

---
## [ConsumingChaos/rules_rust](https://github.com/ConsumingChaos/rules_rust)@[80f0eb488a...](https://github.com/ConsumingChaos/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Thursday 2023-05-18 03:28:43 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [felipec/git](https://github.com/felipec/git)@[f1c903debd...](https://github.com/felipec/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Thursday 2023-05-18 03:38:50 by Ævar Arnfjörð Bjarmason

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
## [felipec/git](https://github.com/felipec/git)@[b01e1c7ef0...](https://github.com/felipec/git/commit/b01e1c7ef0f8c7cd05190898ec6acffe638ccfcf)
#### Thursday 2023-05-18 03:38:50 by Jeff King

ref-filter: fix parsing of signatures without blank lines

When ref-filter is asked to show %(content:subject), etc, we end up in
find_subpos() to parse out the three major parts: the subject, the body,
and the signature (if any).

When searching for the blank line between the subject and body, if we
don't find anything, we try to treat the whole message as the subject,
with no body. But our idea of "the whole message" needs to take into
account the signature, too. Since 9f75ce3d8f (ref-filter: handle CRLF at
end-of-line more gracefully, 2020-10-29), the code instead goes all the
way to the end of the buffer, which produces confusing output.

Here's an example. If we have a tag message like this:

  this is the subject
  -----BEGIN SSH SIGNATURE-----
  ...some stuff...
  -----END SSH SIGNATURE-----

then the current parser will put the start of the body at the end of the
whole buffer. This produces two buggy outcomes:

  - since the subject length is computed as (body - subject), showing
    %(contents:subject) will print both the subject and the signature,
    rather than just the single line

  - since the body length is computed as (sig - body), and the body now
    starts _after_ the signature, we end up with a negative length!
    Fortunately we never access out-of-bounds memory, because the
    negative length is fed to xmemdupz(), which casts it to a size_t,
    and xmalloc() bails trying to allocate an absurdly large value.

    In theory it would be possible for somebody making a malicious tag
    to wrap it around to a more reasonable value, but it would require a
    tag on the order of 2^63 bytes. And even if they did, all they get
    is an out of bounds string read. So the security implications are
    probably not interesting.

We can fix both by correctly putting the start of the body at the same
index as the start of the signature (effectively making the body empty).

Note that this is a real issue with signatures generated with gpg.format
set to "ssh", which would look like the example above. In the new tests
here I use a hard-coded tag message, for a few reasons:

  - regardless of what the ssh-signing code produces now or in the
    future, we should be testing this particular case

  - skipping the actual signature makes the tests simpler to write (and
    allows them to run on more systems)

  - t6300 has helpers for working with gpg signatures; for the purposes
    of this bug, "BEGIN PGP" is just as good a demonstration, and this
    simplifies the tests

Curiously, the same issue doesn't happen with real gpg signatures (and
there are even existing tests in t6300 with cover this). Those have a
blank line between the header and the content, like:

  this is the subject
  -----BEGIN PGP SIGNATURE-----

  ...some stuff...
  -----END PGP SIGNATURE-----

Because we search for the subject/body separator line with a strstr(),
we find the blank line in the signature, even though it's outside of
what we'd consider the body. But that puts us unto a separate code path,
which realizes that we're now in the signature and adjusts the line back
to "sigstart". So this patch is basically just making the "no line found
at all" case match that. And note that "sigstart" is always defined (if
there is no signature, it points to the end of the buffer as you'd
expect).

Reported-by: Martin Englund <martin@englund.nu>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[d188513e9e...](https://github.com/Superlagg/coyote-bayou/commit/d188513e9e6871ce027e9b9d5c65c3318a0d0b3f)
#### Thursday 2023-05-18 03:45:14 by Jess

Merge pull request #2066 from jinxynii/master

stop cheesing my fucking dungeon you god damn LOSERS

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[2068ea9ab5...](https://github.com/MrMelbert/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Thursday 2023-05-18 03:49:07 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [BasicallyWiz/CallOfMinecraftWeb](https://github.com/BasicallyWiz/CallOfMinecraftWeb)@[62a10a4813...](https://github.com/BasicallyWiz/CallOfMinecraftWeb/commit/62a10a481355b7b10d5e1732d88498ebb009694d)
#### Thursday 2023-05-18 04:19:31 by BasicallyWiz

LETS GET THIS PARTY STARTED IN HERE
The page actually resembles how I think it'll look by the end?!?

After going through idea after Idea, I finally found an Idea that would be unique and cool. An interactive map of rail routes and shit.
So I made that, and put it up on my local environment to realize that it sucked. I don't know if I am just really bad at making train routes, or if that's just simply not the way to go, but I instead just did my classic thing:

Minimal UI, with an image in the background, sort of resembling the drawing I've made just now.

---
## [tjeznach/linux](https://github.com/tjeznach/linux)@[1bba82fe1a...](https://github.com/tjeznach/linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Thursday 2023-05-18 04:50:33 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [oshanoshu/evals](https://github.com/oshanoshu/evals)@[170dfd886c...](https://github.com/oshanoshu/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Thursday 2023-05-18 04:52:39 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [oshanoshu/evals](https://github.com/oshanoshu/evals)@[b93700ab49...](https://github.com/oshanoshu/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Thursday 2023-05-18 04:52:39 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [oshanoshu/evals](https://github.com/oshanoshu/evals)@[8e276ea460...](https://github.com/oshanoshu/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Thursday 2023-05-18 04:52:39 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [oshanoshu/evals](https://github.com/oshanoshu/evals)@[2ffd4b57de...](https://github.com/oshanoshu/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Thursday 2023-05-18 04:52:39 by Andrew Kondrich

add more logging (#964)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [ederekun/x-ft_kernel_oneplus_msm8998](https://github.com/ederekun/x-ft_kernel_oneplus_msm8998)@[4abad43a46...](https://github.com/ederekun/x-ft_kernel_oneplus_msm8998/commit/4abad43a469df80b26144bd5081a6ed0e70fe5f9)
#### Thursday 2023-05-18 04:53:48 by Peter Zijlstra

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
## [elliskdowns/hello-world](https://github.com/elliskdowns/hello-world)@[fa45131f10...](https://github.com/elliskdowns/hello-world/commit/fa45131f10b8d5a28e75919991ebf2db5b235fb7)
#### Thursday 2023-05-18 04:59:47 by elliskdowns

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7c9dd17b76...](https://github.com/treckstar/yolo-octo-hipster/commit/7c9dd17b766cd4d8a66f3d63aa7a8326da64aac4)
#### Thursday 2023-05-18 05:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[16e4f3c492...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/16e4f3c492cd18e74c975051c4fcd9da5e59fb80)
#### Thursday 2023-05-18 05:45:00 by SkyratBot

Tcomms Soundloop Comes From One Source And Is Less Awful [MDB IGNORE] (#20713)

* Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Tcomms Soundloop Comes From One Source And Is Less Awful

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[178b6fc96c...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/178b6fc96cef11619565d802750cad9e6c34b12a)
#### Thursday 2023-05-18 05:45:00 by SkyratBot

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles [MDB IGNORE] (#20711)

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ce894aaea3...](https://github.com/mrakgr/The-Spiral-Language/commit/ce894aaea31be0a6dded001dd2b6075bcd41fa05)
#### Thursday 2023-05-18 06:21:48 by Marko Grdinić

"8:05pm. If nobody is interested in posting on RR, I'll just ditch that part and make a compiler for VN without any specific site posting functionality.

On the plus side, today I got another recruiter on LinkedIn. That makes six ever since I fixed my resume.

If Youtubing can only get me so far, I'll get a job as I intended.

8:15pm. Oh yes, I am considering completely kicking voice-overs out. I can just play music while I record myself programming. How about that?

That would also speed up my programming workflow significantly.

https://www.youtube.com/results?search_query=comfyui

ComfyUI is fairly popular. That anon did good.

https://github.com/comfyanonymous/ComfyUI

Has a lot of stars.

Sigh...

It truly is hard to make something popular.

https://youtu.be/ifaGND2MYjU
【Chill Lofi】🌈 Freedom and happiness under the blue sky, enjoying sunshine and music 🌈

This playlist is pretty good.

8:35pm. I need to simplify my life.

Does Youtube matter that much?

Programming is what matters. I should just do what I feel like, and right now I don't feel like doing voice overs anymore.

It is not like there is some rule, that I have to keep doing the same thing every time.

https://news.ycombinator.com/item?id=35965483

///

> Standalone executables. You can now create standalone executables with bun build.
> bun build --compile ./foo.ts

> This lets you distribute your app as a single executable file, without requiring users to install Bun.

> ./foo

This is big! Part of Go's popularity is due to how easy it is to produce self-contained executables.

And it seems to support amd64 and arm according too: https://twitter.com/jarredsumner/status/1657964313888575489

///

8:50pm. Fuck, I should have spent lunacy on 9 1x extractions. It seems the probabilities aren't cumulative.

I am such an idiot.

And now I am pissed at the game. I had 1270 lunacy and could have waited till tomorrow, to get another 100, but Sinclair's 3 star N corp id expires tomorrow and I am not sure whether I'd have time for it. The risk didn't pay off. For all I know had I waited for that extra 100 lunacy I'd get tomorrow and then decarolled, I might have gotten him. Forget it.

I'll give up on him.

https://mobofdeer.wordpress.com/kenja-no-deshi/

Kendeshi got licensed, I guess that is why translations stopped.

https://old.reddit.com/r/ExperiencedDevs/comments/13hwa4k/what_are_some_good_youtube_channels_for/
https://www.youtube.com/@SebastianLague/videos

This guy is a beast.

11:35pm. https://mobofdeer.wordpress.com/golden-experience-1/

> If you’re feeling ill, you can go to a VR clinic. Your VR equipment can perform scans to give your attending physician real-time updates on your health. You can even have a physical examination, then get any prescribed medications sent to your home that day. If it’s something serious that can’t be resolved during a standard office visit, unfortunately you’d still have to go to an actual medical facility in person. However, there are no doctors there. You lie on a bed assigned by the medical technologist, then medical robots treat you. Of course, you’re actually being treated by a qualified physician via VR.

This is actually an interesting use of VR.

5/17/2023

8:05am. I am up. Let me see if I got any replies. I got autistic in that one thread, so we'll see...

https://www.reddit.com/r/royalroad/comments/13j3big/how_to_post_a_chapter_with_images_on_royal_road/
https://www.royalroad.com/forums/thread/129094
https://www.royalroad.com/forums/thread/129095
How to post a chapter with images on Royal Road

Wow, absolutely zero interest.

I guess I'll treat the project as an experience booster.

8:10am. Well, having something where I can store my prompts and dailogues will have value.

Let me go for another few months of this and then I'll start contracting. If necessary I'll look for remote jobs in Croatia at the worst.

https://www.youtube.com/watch?v=cC6HFd1zcbo&t=1042s
Did I Pick The Right Database???

> Please don't use Mongo, unless you have a very specific reason.

Let me watch this from the start.

https://youtu.be/cC6HFd1zcbo?t=1400

This is pretty insightful.

I do not feel like programming right now, I'll get to it later.

https://youtu.be/cC6HFd1zcbo?t=2351
> The reason Firebase succeeded is because backend was too hard. And it was. Backend was way too hard.
> We fixed that.

10:20am. Let me start programming. I'll skip having a bath today.

I went to bed late last night, and now I am tired again. Shit.

It is like when I was working on Spiral all over again.

God, I just wished I could find a project that gave me smooth rewards along the way.

Hoping you get rewarded at the end is hell isn't it?

Just a few more months of this and then I quit NEETing.

The stock market is recovering.

10:30am. I wasted 2.5 hours at least this morning being stressed out over nothing.

My mentality is negative today.

I really wish I could make money. Because money is what I need to get the computational resources needed to work on AI. The fact that I cannot fulfil this purpose is incredibly painful for me.

Money, just what ability do I need to earn it?

Maybe I should ask Bing that?

Tomorrow.

Let me check out the video from yesterday on context menu. The other guy showed how to style them.

https://youtu.be/imfuOrVO9kg
Custom Right Click with Context Menu in React

I think it was that.

https://youtu.be/imfuOrVO9kg?t=175

I'll watch him at 2x.

Should I use style components. Just what kind of styling does React Flow use.

What should I use for menu buttons that meshes with it.

I should familiarize myself with styling libraries.

https://youtu.be/imfuOrVO9kg?t=399

Mhhh...what the hell is this?

https://reactflow.dev/docs/guides/theming/#using-third-party-libraries

> You can use any library you want for styling your flows. Check out the styled-components or tailwind examples for some inspiration.

Should I check these out?

https://reactflow.dev/docs/examples/styling/styled-components/

Interesting.

...Is this some kind of site. I thought I went through all of the docs, but it seems I haven't.

11:05am. Had to take a break, let me resume.

I guess in the end, the best way to get money is to do what people'd be willing to pay you directly to do.

So I should want a job. With a job, I'd have motivation to work and improve.

That is how I should be treating them.

Find a job that would let me develop myself.

Forget making money of any of my projects.

As for these Youtube videos, they'll have to be my legacy.

I'll use them as leverage in the job search.

Selling software is really difficult.

I wish I had an army of AIs to promote my work. That would be the way to succeed.

Right now, I know that even if I make the project, it wouldn't amount to much more than a wet fart.

Rather than sell things to the public, I need to sell things to the higher ups.

I guess that is the way the world works.

I just don't have the power to do everything by myself.

In an ideal world, I'd just put out something on the marketplace and it would win on its own merits, but that is not how things work at all.

If you have a good idea, you need to ram it down people's throats.

https://youtu.be/imfuOrVO9kg?t=483

Let me get back to the video.

11:10am. It is really amazing, how this pain of working in isolation is starting to make me want a job.

Having view, likes and followers is like a slap in my face.

I want dollars!

11:10am. Ah, fuck it. Let me go take a bath.

12:05pm. I am thinking.

Sometimes you simply need time to think about what you are doing and why you are doing things.

My feelings change from day to day.

Heaven's Key, and now Youtubing were both long shots.

What my primary goal should be with this project is to prove that I am a webdev.

I am still not one.

I should have fucking skipped leduc and have gone straight into this.

Just why am I so stupid?

Just what do I think I am doing with my moves?

At last pre-2022 there was a sense to them, even if the world I predicted did not come.

Right now...

I could have skipped Fable and gained a lot more. Right now, all those Fable vids were a complete waste of time.

https://old.reddit.com/r/ExperiencedDevs/comments/13jmfck/everyone_is_talking_about_how_chatgpt_has/
> Regex, ChatGPT is the regex god

12:35pm. I can't do it. I'll take a break today. To study styling.

Or maybe I'll make a commit to program unimpeded by screecasting needs and go over it twice.

1:10pm. Sigh, I am just reading posts on ExperiencedDevs right now.

This is what I am missing. I need to want that job. I need to cultivate the mindset.

1:15pm. https://youtu.be/imfuOrVO9kg?t=604

Let me do some studying.

I am going to step back a while form screencasting to properly learn styling. I need a more open mind.

https://youtu.be/imfuOrVO9kg?t=820

I need to watch this in full. I can afford 10m.

But I am really not paying attention right now.

https://www.youtube.com/watch?v=imfuOrVO9kg

People are going thank you, thank you here, but look at his Patreon and he has 2 subscribers.

https://styled-components.com/

> This Button variable here is now a React component that you can use like any other React component! This unusual backtick syntax is a new JavaScript feature called a tagged template literal.
> You know how you can call functions with parenthesis? (myFunc()) Well, now you can also call functions with backticks! (learn more about tagged template literals)

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates

Hmmm, interesting.

https://styled-components.com/docs/tooling#typescript-plugin

I've looked at whether SC is compatible with Vite and TS and there are a lot of problems.

Nevermind this meme library.

I don't see the point of inlining CSS into a JS file.

https://styled-components.com/

This seems to be what its all about.

So maybe I could look into bootstrap or...

https://youtu.be/FSCSdAlLsYM?list=PLC3y8-rFHvwgu-G08-7ovbN9EyhF_cltM
React Styled Components - 1 - Introduction

Let me just watch this, and then I'll look a video for getting it to run with Vite.

https://youtu.be/FSCSdAlLsYM?list=PLC3y8-rFHvwgu-G08-7ovbN9EyhF_cltM&t=56

Maybe I could need this, as CSS classes get loaded in a side effecting manner.

1:40pm. Nevermind, I'll skip syled components. I don't need the installation troubles.

https://youtu.be/8Fvn4as79OA
Rating The Most Popular React UI Frameworks

https://youtu.be/8Fvn4as79OA?t=49

Inline css.

https://youtu.be/8Fvn4as79OA?t=124

I wonder if there is a type for CSS style objects?

There should be. I'd be surprised if there wasn't.

https://youtu.be/8Fvn4as79OA?t=202

You can make a css that applies only to a single component.

That would be good. I want to know how that works.

Also I want to be able to select between the styles.

https://youtu.be/8Fvn4as79OA?t=266

Ok, think me, think. Turn on that brain.

https://youtu.be/8Fvn4as79OA?t=345

He says SC 'was' one of the most popular react frameworks for styling.

https://youtu.be/8Fvn4as79OA?t=490

What I really want it something to help me import the styles locally. I guess those would be css modules?

https://youtu.be/8Fvn4as79OA?t=495
> Now with Next.js version 13, it is not even working.

He is talking about it.

https://youtu.be/8Fvn4as79OA?t=543

Should I use one of the component libraries. I am not sure I want to style personally.

https://youtu.be/8Fvn4as79OA?t=604

I think Vite can optimize this.

https://youtu.be/8Fvn4as79OA?t=754

Why don't I use MUI?

I'll watch a similar video to this by Theo.

https://youtu.be/8Fvn4as79OA?t=1024

Tailwind has prebuilt components.

> I think Chakra UI, Mantine, and Mui are perfect solutions for full-stack devs, who do not like to write CSS :)

One of the comments.

> Also downside of css-in-js like Styled Components is the additional runtime size and cost, which is why many are moving away, especially now with the (new) rise of SSR

https://youtu.be/hdGsFpZ0J2E
Should You Use Tailwind CSS?

https://youtu.be/CQuTF-bkOgc?t=257

Theo is pretty informative when he talks about what he knows. This is better than that other video.

https://youtu.be/CQuTF-bkOgc?t=330
> The reason why people kept going to bootstraps is a combination of CSS being hard to write, CSS being hard to pick up, and developers being lazy.

https://youtu.be/CQuTF-bkOgc?t=506
> I'd argue this is our job as front end developers.

He is talking about component libraries.

https://youtu.be/CQuTF-bkOgc?t=644
> Those problems are pretty damn common in MUI land.

https://youtu.be/CQuTF-bkOgc?t=685
> There is very little need except for a backend leaning developer that's trying to ignore the frontend as much as possible to use something like MUI.

https://youtu.be/CQuTF-bkOgc?t=910

Menu & Transition, that seems like something I'd want.

https://youtu.be/CQuTF-bkOgc?t=946

You know what, fuck all this. I am giong to go with a component library. Focus is important. I am backend leaning.

https://youtu.be/CQuTF-bkOgc?t=962
> Unstyled.

This video is really good and informative. GG Theo.

https://youtu.be/CQuTF-bkOgc?t=969

Oh this is cool. I was wondering where these were, and how to build them in HTML.

https://youtu.be/CQuTF-bkOgc?t=1263
> Let's talk about Styled Components

https://youtu.be/CQuTF-bkOgc?t=1450
> INLINE STYLES ARE ACTUALLY GOOD

Was I lied to this whole time?

https://youtu.be/CQuTF-bkOgc?t=1510
> I couldn't give less of a shit about what this looks like as a developer.

https://youtu.be/CQuTF-bkOgc?t=1827
> The architecture of you application is based on MUI and how it decides to break things up.

https://youtu.be/CQuTF-bkOgc?t=1995
> Vanilla Extract that do a way better job at that.

A lot of people in the comments are praising ChakraUI.

https://youtu.be/CQuTF-bkOgc?t=872

Ok, fuck it. I'll go with his recommendations.

I guess I'll try DaisyUI with some of the things on the left.

https://daisyui.com/

https://daisyui.com/docs/install/

Do I need something special for Tailwind.

https://tailwindcss.com/docs/installation

> Installing Tailwind CSS as a PostCSS plugin is the most seamless way to integrate it with build tools like webpack, Rollup, Vite, and Parcel.

https://tailwindcss.com/docs/guides/vite

3:20pm. Honestly, I thought that Tailwing would just be a css library, but is seems there is more to it.

https://tailwindcss.com/docs/installation

https://daisyui.com/docs/install/

Oh, it has a bunch of example. I clicked on the React Vite one and it opened a sandbox.

3:35pm. Holy shit, I have an ant infestation in my room. They are coming out in full force.

3:45pm. https://daisyui.com/components/carousel/

The carousel confuses me. Is it not working correctly?

4:50pm. I am back. The ants chased me out. Ugh, this is going to be a pain in the ass to deal with from here on out.

My mother fulminated the room, and says we'll have to do it tomorrow as well.

https://daisyui.com/components/checkbox/

I've been checking out these components. Let me just watch brief tailwing tutorial.

https://youtu.be/bxmDnn7lrnk?list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw
Tailwind CSS Tutorial #1 - Intro & Setup

I want to understand what are all those plugins.

You know, maybe it would be worth watching a couple of these. I should definitely start by installing tailwind.

https://youtu.be/bxmDnn7lrnk?list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw&t=492

https://www.freecodecamp.org/news/how-to-install-tailwindcss-in-react/

Why don't these instructions work for me?

Ah, maybe the file postfixes for the config files need to be `.ts`?

https://larainfo.com/blogs/install-setup-vite-react-typescript-tailwind-css-3

Sigh, this is just the same as what I did. Did I miss something? Why isn't it working for me.

5:45pm. I have no choice, let me try it on an isolated project.

That's webdev for you I guess.

5:50pm. It might be working I guess. I have no idea why it is not working in React Flow.

Forget this. I am under too much pressure lately.

I'll take playing with Tailwind at a more leisurely pace.

Let me just go into the tutorial briefly, forget React.

https://www.jetbrains.com/help/rider/Tailwind_CSS.html

> Make sure the CSS and Tailwind CSS bundled plugins are enabled in the Installed tab of the Settings | Plugins page as described in Managing plugins.

6pm. Great, now Rider supports Tailwind.

6:10pm. Rider isn't completing Tailwind classes.

https://www.jetbrains.com/help/rider/Tailwind_CSS.html#ws_css_tailwind_complete_classes

> Configure a Node.js interpreter in your project as described in Configuring a local Node.js interpreter, or in Using Node.js on Windows Subsystem for Linux, or in Configuring remote Node.js interpreters.

Wait, maybe I need to configure this?

...I already had it configed.

https://youtrack.jetbrains.com/issue/WEB-54065/Tailwind-v3-CSS-autocomplete-not-working-in-Webstorm-2021.3-Vue.js-3-project#focus=Comments-27-6704364.0-0

It seems that this plugin constantly keeps breaking.

> I clicked on the "Manage Scopes...", I added the scope to the node_modules where the tailwindcss is:

Wait. Maybe it isn't working because I've installed it as a dev dependency.

...No, it is right there. That can't be it.

6:30pm. Let me try it on a vanilla project.

6:35pm. No, it still doesn't work. But the VS Code extension works perfectly.

I guess I'll be switching from Rider back to VS Code for my TS projects.

https://vitejs.dev/guide/features.html#css-modules

> Any CSS file ending with .module.css is considered a CSS modules file. Importing such a file will return the corresponding module object:

So Css can have modules.

> Importing .css files will inject its content to the page via a <style> tag with HMR support. You can also retrieve the processed CSS as a string as the module's default export.

I do not really understand what the scoping for css imports is.

https://github.com/css-modules/css-modules

Wait, can I combine the css modules with tailwind?

8:25pm. Ok, I've played enough.

That super weird error on the Helix project was because for a stupid reason I had converted the .css file to UTF-16 previously. For some reason Rider was complaining so I did it to shut it up, but it really backfired on me.

Otherwise it is not hard at all to set up. Neither is DaisyUI.

The VS Code plugin is a bit wonky in that those @apply and @tailwind statements give warnings, but otherwise the intellisense is perfect.

It even works in .tsx files!

It is ironic given that I couldn't find a plugin for regular CSS that works with those.

I spent a lot of time going through the past Rider issues, but it seems the Tailwind plugin is in a permanent state of brokeness.

God I am so tired.

5/18/2023

8:05am. I went to bed early, and slept deeply. I even got up once and fell back asleep.

8:15am. Let me start for the day."

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[bbfce81a35...](https://github.com/sourcegraph/sourcegraph/commit/bbfce81a35562d84386862e854ef6b35b555a92a)
#### Thursday 2023-05-18 06:33:47 by Juliana Peña

web/app: remove hover on navbar items to stop focus from being moved (#51739)

The dropdown menu items in the global navbar (Search and, in App,
Feedback) move focus when you hover over them. This is bizarre, ugly,
and most likely a [WCAG
violation](https://www.w3.org/TR/WCAG21/#focus-order). I spent some time
yesterday and the root cause is that the [Reach menu button we use does
not support hover at all](https://github.com/reach/reach-ui/issues/278)
and we're hacking it by [sending a mousedown event when you hover over
the
button](https://sourcegraph.com/github.com/sourcegraph/sourcegraph/-/blob/client/web/src/nav/NavBar/NavDropdown.tsx?L58).

There are two options I can think of to mitigate this bug:
1. Get rid of hover events and only open the dropdowns on click. This is
the easiest option, but obviously removes the ease of accessing the menu
for mouse users.
2. Rewrite the dropdown nav items to use a custom menu instead of Reach.
This is more expensive because we have to reimplement lots of a11y stuff
here, but we can have more fine-grained control of different UI flows
for mouse hover vs mouse click vs keyboard users.

I went with the first option following @almeidapaulooliveira's
[feedback](https://sourcegraph.slack.com/archives/C0HMGV90V/p1683735888755969?thread_ts=1683734992.157499&cid=C0HMGV90V).

The following changes were applied to `NavDropdown`:

- Removed all hover and touch events; now only a click will open the
menu.
- Removed the split button; now clicking anywhere on the button will
always open the menu.
- Made the mobile home item into a "generic" home item and always
visible when present.
- Made the home item optional (since the Feedback menu item in the
desktop app doesn't have a home item/route).
- Added customizable a11y names; in the past, the only dropdown was the
Search one, but in App we now have Feedback; the a11y labels were still
saying "Search" before this change.

Additionally, the following changes were applied for polish:

- The double-focus ring on the back/forward buttons in the Tauri app has
been fixed
- Styling changes made to simplify code

## Test plan

The global navbar has extensive visual and behavior test coverage.

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[527fb7b003...](https://github.com/Rex9001/Rex-station-/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Thursday 2023-05-18 08:21:39 by DrTuxedo

ELEVATOR MUSIC: True Elevator Experience (#75388)

## About The Pull Request
Adds elevator music into the game that is played by an elevator panel.


https://github.com/tgstation/tgstation/assets/42353186/1a801604-3990-46ae-a96a-b3766b102d62

It's done by using loop sound, with a Kevin MacLeod "Local Forecast -
Elevator" (UNDER CC ATTRIBUTIONS 4.0, and we anyway used some other
Kevin MacLeod music) chopped into 8 small pieces.
The elevator panel has a variable which allows playing music but can be
changed in the map editor if you don't want it to play at certain
places.

(It also doesn't ignore walls, this means you can't hear the music
through wall or when elevator is closed)
## Why It's Good For The Game
Gives elevators more flavour and love, especially when people mostly
prefer stairs to those "laggy crushing machines."
Because of this people might instead hop into an elevator just to hear
meme elevator music, which is relaxing and might create comedic
situations (although elevators don't move that fast)
## Changelog
:cl: DrDiasyl aka DrTuxedo
sound: Nanotrasen have started installing music players in the elevators
to boost workers' morale.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Offroaders123/MCA-Buffer](https://github.com/Offroaders123/MCA-Buffer)@[abf007832b...](https://github.com/Offroaders123/MCA-Buffer/commit/abf007832b716522cc0890fa45c8793112cb14b7)
#### Thursday 2023-05-18 08:25:56 by Offroaders123

Parsing Rework

Took the things I brought over from MCRegionJS, and refactored them to more strongly work with the Java format specifically. Things are a bit more tidy now in that regard.

It does seem like Java regions are the easiest to parse, which is fortunate! It's actually not too bad to iterate over all of the file to get specific chunks and things like that.

Went back to the wiki's docs about the file format to get familiar with it's specifics again.

https://minecraft.fandom.com/wiki/Region_file_format

Part of the rework was that I mainly noticed that since the body of the chunk data is just plain NBT, I can pass that directly into NBTify itself, and have it deal with the compression formats! I wish LCE was structured this way, because that seems to work really well in conjunction with building on top of each section of the file format. By that, I mean that you can read some parts at a time specifically, without having to do the other steps first. You can get the file size and compression format before you have to decompress the actual content, things like that. In LCE chunks, some parts of the compression stages depend on you to have decompressed 'x' stages before you are able to read the header at that point. So, each part of the header is saved in a different section of the compression stage, meaning you have to do each part one by one, rather than being able to query that format information before having to decode the whole content of the chunk.

Have started trying listening to ASMR while coding, and wow it is a great experience. Especially with headphones. I've listened to it before, sometimes to help with sleep. For coding though, it feels like it really helps keep my attention on the project at hand. It is making me sleepy though, but that's a good thing, since I usually tend to stay up coding all night on the weekends, haha.

---
## [seailz/discord-api-docs](https://github.com/seailz/discord-api-docs)@[dd3f05a170...](https://github.com/seailz/discord-api-docs/commit/dd3f05a1709add398bac3a68af3cc27287f67038)
#### Thursday 2023-05-18 08:44:18 by Jerry Jiang

Document Silent Messages. (#5910)

Hey folks!

This is actually my 2022 hackweek project which I got to finish to
completion. :)

During a message send request, if you include the new
`SUPPRESS_NOTIFICATIONS` flag it will not broadcast any push/desktop
notifications but will still increment the relevant mention counters.

The intention is that you can get someone's attention but not feel like
you could be distracting them. Like when you DM someone at 5am. I'm sure some
bots can leverage this as well to avoid noise or something.

Also this should work for the webhook send request as well.

[Add a picture of the UI here]

If you're looking to leverage this as a non-bot, you can write `@silent`
as the _very first_ thing in a message. Make sure your client is
up-to-date btw. Autocomplete a-la `@everyone` is not planned. Eventually we may
put this in an "actual UI", for now this is where it lives. :)

Also sorry to all the users on Discord named silent who may have some
textual conflict now. Forgive me!

---
## [rust-lang/miri](https://github.com/rust-lang/miri)@[70dbca76ce...](https://github.com/rust-lang/miri/commit/70dbca76ce312c938f88d93c4685c13d370bef3a)
#### Thursday 2023-05-18 09:05:38 by Nilstrieb

Rollup merge of #111607 - jyn514:clubby-reviews, r=clubby789

Add clubby789 to the bootstrap review rotation

r? `````@clubby789````` - thank you for volunteering!

I have been meaning for a very long time now to write up how to do reviews, but I haven't gotten around to it yet :( here is a short summary:

1. If you're not sure what the changes does or if it's ok, always feel free to ping someone else on the team, especially in the first few weeks. You can use `r? bootstrap` to get triagebot to assign someone else.
2. Bootstrap unfortunately has very few tests. Things that touch CLI or toml parsing should likely have a test in `src/bootstrap/config/tests.rs`; things that touch "core" build logic should have a test in `builder/tests.rs`, anything else kinda just slips in :( see https://github.com/rust-lang/rust/issues/102563 for ideas on how to improve the situation here.
3. "Major" changes should be documented in `src/bootstrap/CHANGELOG.md`. "Major" is up to you, but if it breaks a config option or otherwise is likely to break *someone's* build, it's probably major. If it breaks nearly *everyone*'s build, it should also update `VERSION` in `lib.rs`; this should be very rare. Please also ping me or Mark-Simulacrum for major changes (I might set up a triagebot ping for this so you don't have to remember).
4. Once you've approved the PR, tell bors it's ok - you've been contributing for a while so you know how bors works, but here's a cheatsheet just in case: https://bors.rust-lang.org

Documentation about how to use bootstrap lives at https://rustc-dev-guide.rust-lang.org/building/bootstrapping.html; internal docs live in `src/bootstrap/README.md`. The latter unfortunately is not very complete.

---
## [Speengard/Damnatio](https://github.com/Speengard/Damnatio)@[6ff97dcf1b...](https://github.com/Speengard/Damnatio/commit/6ff97dcf1bcc7a419f7694d7567db3c8a988a31d)
#### Thursday 2023-05-18 09:22:36 by Salvatore De Luca

The Legend of Zelda (ゼルダの伝説 Zeruda no densetsu?) è una serie di videogiochi action-adventure in ambientazione high fantasy, creata da Shigeru Miyamoto e Takashi Tezuka nel 1986 per il Nintendo Entertainment System.

La serie divenne subito una delle più importanti della storia videoludica, arrivando a vendere complessivamente quasi 110 milioni di copie in tutto il mondo e producendo un grande numero di seguiti, comparsi su molte delle console dell'azienda di Kyoto: Nintendo Entertainment System, Super Nintendo Entertainment System, Nintendo 64, Nintendo Game Boy, Nintendo GameCube, Nintendo Wii, Nintendo DS, Nintendo 3DS, Nintendo Wii U e Nintendo Switch.

Sin dal suo debutto con il primo The Legend of Zelda, la serie è considerata una delle più acclamate della storia videoludica e la maggior parte dei titoli che la compongono sono riconosciuti dalla critica come grandi capolavori, primi fra tutti The Legend of Zelda: Ocarina of Time, The Legend of Zelda: A Link to the Past, The Legend of Zelda: The Wind Waker, The Legend of Zelda: Majora's Mask, The Legend of Zelda: Twilight Princess, The Legend of Zelda: Skyward Sword ,The Legend of Zelda: Breath of the Wild e The Legenz of Zelda: Tears of the Kingdom.

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[0e96f1cd6e...](https://github.com/software-mansion/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Thursday 2023-05-18 09:57:07 by Tomasz Żelawski

Remove plugin dev files from npm package (#4433)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Currently development files from `plugin/` are included in npm package.
This PR removes them from it.

b4:
<img width="253" alt="Screenshot 2023-05-08 at 14 39 29"
src="https://user-images.githubusercontent.com/40713406/236829343-1865480f-99d0-4843-adb2-f658db2acce0.png">
after:
<img width="238" alt="Screenshot 2023-05-08 at 14 39 51"
src="https://user-images.githubusercontent.com/40713406/236829379-7c31b6b4-27e1-493c-8be0-6254edbd0c4c.png">

Since [README is always
included](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#files)
I renamed plugin's dev README and removed `README` from being included
in `package.json`.


## Test plan

I recommend using this powerful oneliner: 
`./createNPMPackage.sh && mkdir tarball-new && mv
react-native-reanimated-3.1.0.tgz tarball-new && tarball-new && tar -xf
react-native-reanimated-3.1.0.tgz && ..`
to see the contents of the new package.

Also run _some_ Example App to see if Reanimated plugin from the tarball
is actually working.

---
_Note_: Testing this PR took me longer than it should.

For some reason with current configuration of Example App and running it
on Android (I didn't check iOS) it's surprisingly difficult to use
reanimated from either tarball or unpacked tarball directory. I had to
make a new app and then include Example's source code there.

While it's not that troublesome I think we should have a more
streamlined approach for using custom reanimated package location for
tests with our Examples.

---------

Co-authored-by: Tomek Zawadzki <tomasz.zawadzki@swmansion.com>

---
## [BlueMoon-Labs/SERP-BlueMoon-Station-13](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13)@[3ecc9f859d...](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13/commit/3ecc9f859dfc0f870500d717e382d52662667996)
#### Thursday 2023-05-18 11:12:44 by SkyratBot

[MIRROR] Allows Export of your Preferences JSON File [MDB IGNORE] (#20894)

* Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:

![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.

![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

* Allows Export of your Preferences JSON File

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Bashshesh/ass5](https://github.com/Bashshesh/ass5)@[c53634fdd9...](https://github.com/Bashshesh/ass5/commit/c53634fdd90cff25966b1e42b389f8c752a71334)
#### Thursday 2023-05-18 11:49:52 by Bashshesh

It's cool to live, but I sometimes think that living, in general, existing and that people generally overestimate life is strange, isn't it? People found a way out in this, not to think about it, life is short to think about it, no one wants to think, but I want to, what is the meaning of existence in this whole world, who can tell me the answer? God? Family? Job? Money?

---
## [dj-34/Skyrat-220](https://github.com/dj-34/Skyrat-220)@[21363d07a5...](https://github.com/dj-34/Skyrat-220/commit/21363d07a5eec9fbce5be2f17cd1693319906d61)
#### Thursday 2023-05-18 11:53:54 by SkyratBot

[MIRROR] De-holes holy arrows [MDB IGNORE] (#20985)

* De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

* De-holes holy arrows

---------

Co-authored-by: Thunder12345 <Thunder12345@users.noreply.github.com>

---
## [Omarley7/DTaaS-Bachelor-new-GUI](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI)@[4106db0ebe...](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI/commit/4106db0ebe75c9b45d3144ccdda8036160888285)
#### Thursday 2023-05-18 13:38:03 by Mathias Brændgaard

Add unit tests for Store/AppAccess and Store/UserAccess (#63)

* Add unit tests for Store/AppAccess and Store/UserAccess

* Honestly bullshit codeclimate error.
Would be overly complicated to fix. Even this solution is stupid.
And also updated envUtil to use the same hook, act, assert approach.

* Bullshit løsning

---------

Co-authored-by: Omar <omarg@live.dk>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[52eb909f42...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/52eb909f423900340814843d3223a7f3205add35)
#### Thursday 2023-05-18 13:42:05 by Tom

Makes Hell Microwaves Not Use Power (#67413) (#21210)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

Co-authored-by: san7890 <the@san7890.com>

---
## [chilli-axe/mpc-autofill](https://github.com/chilli-axe/mpc-autofill)@[fe779f5516...](https://github.com/chilli-axe/mpc-autofill/commit/fe779f5516389dd23c5d5ef8d8a05c99271f62b0)
#### Thursday 2023-05-18 13:52:12 by Nicholas de Paola

god fucking dammit

bad ugly not good solution to the race condition on page load,
but it works perfectly so w/e

i'm delaying each query until the backend URL to query is specified

the (imo) correct solution here is to correctly invalidate tags
in the presence of a race condition. seems like there's a PR to do
that here: https://github.com/reduxjs/redux-toolkit/pull/3116
but no movement on it for the last few months

related issue: https://github.com/reduxjs/redux-toolkit/issues/3386

---
## [agebhar1/awesome-docker](https://github.com/agebhar1/awesome-docker)@[3164d6df94...](https://github.com/agebhar1/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Thursday 2023-05-18 14:35:01 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [miguse/terminal](https://github.com/miguse/terminal)@[6ad8cd0a63...](https://github.com/miguse/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Thursday 2023-05-18 15:21:22 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [jnutt367/psalms](https://github.com/jnutt367/psalms)@[a7a2ba9598...](https://github.com/jnutt367/psalms/commit/a7a2ba9598ff25fbb577089ac6766fc4a0532d62)
#### Thursday 2023-05-18 17:22:40 by Jason Nutt (He/Him) Christian Developer/Creator

Update index.js

For the director of music. Of David. A psalm.
1 I waited patiently for the Lord;
    he turned to me and heard my cry.
2 He lifted me out of the slimy pit,
    out of the mud and mire;
he set my feet on a rock
    and gave me a firm place to stand.
3 He put a new song in my mouth,
    a hymn of praise to our God.
Many will see and fear the Lord
    and put their trust in him.

4 Blessed is the one
    who trusts in the Lord,
who does not look to the proud,
    to those who turn aside to false gods.[b]
5 Many, Lord my God,
    are the wonders you have done,
    the things you planned for us.
None can compare with you;
    were I to speak and tell of your deeds,
    they would be too many to declare.

6 Sacrifice and offering you did not desire—
    but my ears you have opened[c]—
    burnt offerings and sin offerings[d] you did not require.
7 Then I said, “Here I am, I have come—
    it is written about me in the scroll.[e]
8 I desire to do your will, my God;
    your law is within my heart.”

9 I proclaim your saving acts in the great assembly;
    I do not seal my lips, Lord,
    as you know.
10 I do not hide your righteousness in my heart;
    I speak of your faithfulness and your saving help.
I do not conceal your love and your faithfulness
    from the great assembly.

11 Do not withhold your mercy from me, Lord;
    may your love and faithfulness always protect me.
12 For troubles without number surround me;
    my sins have overtaken me, and I cannot see.
They are more than the hairs of my head,
    and my heart fails within me.
13 Be pleased to save me, Lord;
    come quickly, Lord, to help me.

14 May all who want to take my life
    be put to shame and confusion;
may all who desire my ruin
    be turned back in disgrace.
15 May those who say to me, “Aha! Aha!”
    be appalled at their own shame.
16 But may all who seek you
    rejoice and be glad in you;
may those who long for your saving help always say,
    “The Lord is great!”

17 But as for me, I am poor and needy;
    may the Lord think of me.
You are my help and my deliverer;
    you are my God, do not delay.

---
## [Lyroy/dustbowl-blues](https://github.com/Lyroy/dustbowl-blues)@[9bcf5d42f2...](https://github.com/Lyroy/dustbowl-blues/commit/9bcf5d42f2da5ab8757867ee8f6b539c43b785e0)
#### Thursday 2023-05-18 17:46:19 by Lyroy

Merge pull request #8 from lpeapnni/OMFG-PASS-THE-FUCKING-TESTS

PASS THE FUCKING CI TESTS YOU STUPID PIECE OF SHIT

---
## [peff/git](https://github.com/peff/git)@[fd312e7c15...](https://github.com/peff/git/commit/fd312e7c15c02f62509bb586593e8826c50ce4d6)
#### Thursday 2023-05-18 18:30:29 by Jeff King

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
## [emu1729/evals](https://github.com/emu1729/evals)@[ab5f7b2a89...](https://github.com/emu1729/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Thursday 2023-05-18 20:02:04 by oscar-king

Counting bigrams in sentences (#302)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [emu1729/evals](https://github.com/emu1729/evals)@[b170a21cf3...](https://github.com/emu1729/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Thursday 2023-05-18 20:02:04 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [emu1729/evals](https://github.com/emu1729/evals)@[b5da073c21...](https://github.com/emu1729/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Thursday 2023-05-18 20:02:04 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [GitGaming-Paradise/GitGaming-Paradise.github.io](https://github.com/GitGaming-Paradise/GitGaming-Paradise.github.io)@[a4d64656d7...](https://github.com/GitGaming-Paradise/GitGaming-Paradise.github.io/commit/a4d64656d74485523d8b8ee9854f2759876eddee)
#### Thursday 2023-05-18 20:16:07 by _enderculk8

Added a story

One summer day in the park, I was having a delightful picnic with my good friend Orville. And I said to him, I said “Orville, I-I have a story” And he said to me “What’s the significance of the story?” I said to him “Orville, not every story has to have significance, ya know? Sometimes uhh, sometimes a story is just a story. You try to read into every little thing and find meaning in everything anyone says, you’ll just drive yourself crazy. Had a friend do it once, wasn’t pretty, we talked about it for years. And not only that, you’ll likely end up believe something you shouldn’t believe or thinking something you shouldn’t think o-o-or assuming something you shouldn’t assume, ya know? Sometimes I said a story is just a story, so just be quiet for one second here life and eat your sandwich, okay? Of course, it was only then I realized i made sandwiches and poor Orville was having such difficulty eating it! Elephants have those clumsy hands, ya know? Actually, I suppose that’s the problem, they don’t have hands at all, they’re all feet. I couldn’t imagine someone asking me to eat a sandwich with my feet. Now, if I recall correctly there was a bakery nearby, I said to him “Orville, let me go get you some rye bread.” Now, I’m unsure elephants enjoy rye bread, but, I assure you that Orville does. Now this was on a Tuesday which was good because rye bread was always fresh on Tuesday. They made sourdough on Monday and threw it out Wednesday. or rather they sold it at a discount for people who wanting to feed the ducks and then probably at the end of the day they threw it all out. I do remember a man who would being his son to the bakery every Wednesday, and go feed the ducks. He would buy all of the sourdough bread, of course, you know, you’re not supposed to feed the ducks sourdough bread at all. It swells up in their stomach and they all die, at least that’s what I’ve heard. Ya know I never saw any ducks die myself but I did notice a substantial decrease in duck population over the course of a few years. I just never thought to stop the man and tell him he was killing the ducks by feeding them sourdough bread. And if you want my opinion on the matter if you wanna feed ducks or birds or any kind for that matter, especially buy seed. I mean, when you think about it, breads of any sort don’t occur in nature, they don’t grow on trees or spring up from bushes! I don’t think birds know what to do with bread. What was I saying? Oh oh yes yes. So I bought Orville some rye bread. What a fine day it was.

---
## [openai/evals](https://github.com/openai/evals)@[8f8632ec55...](https://github.com/openai/evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Thursday 2023-05-18 20:17:15 by Oshan Upreti

Nepali song singer recognition (#892)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Nepali Song Singer

### Eval description

It tests the ability to understand Nepali language from given English
Transliteration phrase which is provided by user as a song title, and
checks the singer/band of the song. This eval has the accuracy of zero.
And, I still created this eval PR because I get the wrong answers every
time I ask, and I don't think that should be the case. It might not be
something that needs to be done immediately, but in a near future you
would expect your AI to answer it correctly.

### What makes this a useful eval?

If it can do for any English songs in the database, it should be able to
do for other languages as well. This is just a pattern I found it in my
mother tongue, but there might be different other languages where this
is happening as well, and it can be other things as well not just the
song title recognition.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Sayad Timro Bato Ma"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Timi Lai Dekhera"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Aaja maan udhera bhagchha"}],
"ideal": "Udit Narayan"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Kaha Hola Ghar Bara"}], "ideal":
"Karma"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Khaseka Tara"}], "ideal":
"Albatross"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[33484c8341...](https://github.com/openai/evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Thursday 2023-05-18 20:18:27 by emu1729

Added AIME eval (#293)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
AIME-Evaluation

### Eval description

This eval evaluates GPT on some selected AIME (American Invitational
Mathematics Examination) problems. This is a selective and prestigious
mathematical examination for high schoolers. All questions are selected
from the 2001 and 2002 AIME I and II examinations.

### What makes this a useful eval?

This evaluation combines math and logical evaluation and is designed to
be quite challenging. The model must first understand the math question
asked and then perform the math equations needed to come up with a
reasonable solution.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

Our eval was designed to include both math and logical reasoning and is
quite challenging. This is a level above the AMC10 examination.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Find the sum of all positive
two-digit integers that are divisible by each of their
digits."}],"ideal":"630"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A fair die is rolled four
times. The probability that each of the final three rolls is at least as
large as the roll preceding it may be expressed in the form m\/n, where
m and n are relatively prime positive integers. Find m +
n"}],"ideal":"079"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A sphere is inscribed in the
tetrahedron whose vertices are A = (6, 0, 0), B = (0, 4, 0), C = (0, 0,
2), and D = (0, 0, 0).The radius of the sphere is m \/ n, where m and n
are relatively prime positive integers. Find m + n."}],"ideal":"005"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A mail carrier delivers mail
to the nineteen houses on the east side of Elm Street. The carrier
notices that no two adjacent houses ever get mail on the same day, but
that there are never more than two houses in a row that get no mail on
the same day. How many different patterns of mail delivery are
possible?"}],"ideal":"351"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"The numbers 1, 2, 3, 4, 5, 6,
7, and 8 are randomly written on the faces of a regular octahedron so
that each face contains a different number. The probability that no two
consecutive numbers, where 8 and 1 are considered to be consecutive, are
written on faces that share an edge is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"085"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Let N be the largest positive
integer with the following property: reading from left to right, each
pair of consecutive digits of N forms a perfect square. What are the
leftmost three digits of N?"}],"ideal":"816"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each of the 2001 students at a
high school studies either Spanish or French, and some study both. The
number who study Spanish is between 80 percent and 85 percent of the
school population, and the number who study French is between 30 percent
and 40 percent. Let m be the smallest number of students who could study
both languages, and let M be the largest number of students who could
study both languages. Find M-m."}],"ideal":"298"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A set of positive numbers has
the 'triangle-property' if it has three distinct elements that are the
lengths of the sides of a triangle whose area is positive. Consider sets
{4, 5, 6, ..., n} of consecutive positive integers, all of whose
ten-element subsets have the triangle property. What is the largest
possible value of n?"}],"ideal":"253"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each unit square of a 3-by-3
unit-square grid is to be colored either blue or red. For each square,
either color is equally likely to be used. The probability of obtaining
a grid that does not have a 2-by-2 red square is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"929"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Given that x and y are both
integers between 100 and 999, inclusive; y is the number formed by
reversing the digits of x; and z=|x-y|. How many distinct values of z
are possible?"}],"ideal":"009"}

  ```
</details>

---------

Co-authored-by: Emily Mu <emilymu@30-10-85.wireless.csail.mit.edu>
Co-authored-by: Emily Mu <emilymu@30-10-24.wireless.csail.mit.edu>

---
## [Bokkiewokkie/Shiptest](https://github.com/Bokkiewokkie/Shiptest)@[b5dc4835a6...](https://github.com/Bokkiewokkie/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Thursday 2023-05-18 21:22:18 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[bad4c9168c...](https://github.com/Jolly-66/dragon-station/commit/bad4c9168c3ccf04effadc09b3d1b1a817fbfbf6)
#### Thursday 2023-05-18 21:47:30 by SkyratBot

[MIRROR] Mafia rebalance and backend refactor [MDB IGNORE] (#20631)

* Mafia rebalance and backend refactor (#74640)

## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

* Mafia rebalance and backend refactor

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [ProditorMagnus/Ageless-for-1-14](https://github.com/ProditorMagnus/Ageless-for-1-14)@[2167581ad6...](https://github.com/ProditorMagnus/Ageless-for-1-14/commit/2167581ad6a64efd5c1b562d2b201e8c4900a12d)
#### Thursday 2023-05-18 22:00:24 by ReynBolt

changelog - update EFM changes

Added changes :


EFM - Dalefolk
Minor Pricement and XP adjustments at most.
AMLA XP that are lower than 100 adjusted to 120 so they can gain +strikes upgrades even if inteligent trait.
(except wilderman)

- Beacon Price to 34g (-6g)
- Conduit Price to 60g (+10g)

- Botanist arcane/cold ressistance to 20% (+10%) , price to 26g (-4g)

- Mountainer cold ressistance to 10% (+10%)

- Delver cold ressistance increase to 20% (+10%) , price to 26g (-2g)
- Foreman cold ressistance to 20% (+10%)

- Raven cold ressistance to 20% , now has +feeding
- Mynah cold ressistance to 20% , now has +feeding , accuracy +5% on their melee

- Rocketer XP from 40 to 38
- Bombardier XP from 85 to 70 , price to 26g (-3g)
- Battery price to 50g (+8g)

Not sure how to evaluate Shifter without proper testing, then for later.


EFM - Darklanders
AMLA XP that are lower than 100 adjusted to 120
(Beastskull intentionally requires 1 AMLA to then gain strikes becuase of powerful berserker)
(Serpent won't as well because why it has to deal high damages? it gained lv2 massive damage buff to not get murdered by lv1 serkers)

- Beastskull price to 37g (-3g)

- Catamaran price to 22g (-2g)

- Wasp price to 26g (-3g)
- Stalker XP from 90 to 75 , price to 25g (-4g)
- Whisper price to 48g (+9g)

- ALL jaguar riders and level up fire ressist to 10% (cheetah 20% instead)

- Wrath price to 37g (-3g)
- Vengeance price to 57g (+7g)
- Judgement price to 75g (+15g)

- Guerrila sword damage increase to 7-4 , ranged damage increase to 11-1 , price to 26g (-2g)
- Militia Impact ressistance to 10% , price to 26g (-2g)
- Guard price to 53g (+13g)

- Serpent cold ressistance to 10%


EFM - Freemen
If you question me, nobody will tell they love this faction lol
AMLA XP that are lower than 100 adjusted to 120
(Roc needs one AMLA because 18-3 is already insane base value)

- Aristocrat XP from 50 to 42
- Amir XP from 100 to 80 , price to 28g (-2g)
- Caliph price to 55g (+25g)
- Vizier XP from 100 to 80
- Sultan price to 57g (+11g)

- Howler XP from 100 to 90 , price to 32g (+2g)
- Screecher price to 54g (+9g)

- Mufti XP from 90 to 85 , price to 33g (-2g)
- Mullah price to 57g (+12g)

- Great Roc price to 53g (+3g)
Freemen recruits lv2 rocs in standard version of eras... too risky to adjust pricement.

- Ensnarer price to 28g (-1g)
- Guardsman price to 23g (-2g)
- Goun price to 47g (+9g)

- Wanderer price to 14g (-1g)
- Dervish XP from 90 to 75
Being 70% sand defense and better ressists than swift-foot can be problematic, reason I did not reprice lower.
- Immortal price to 54g (+11g)
- Nomad melee damage increase to 7-4 , price to 28g (-2g)
They enjoy of great mobility, but their melee was underperforming.
- Sheik now has 50% flat defense, price to 52g (+8g)
Unit was bit underpowered in both levels


EFM - Highlanders
Minor buffs because they have negative ressists which in certain cases is a problem.
Solution in here is decreasing a bit XP's to lv3 and some units having +10% res to one physic element.
AMLA XP that are lower than 100 adjusted to 120 
(Elephants needs one AMLA because in offensive 15-4 for a lv3 is insane!)
(Hippos as well, because of insane bulks)

- Warrior XP from 80 to 74 , price to 23g (-1g)
- Chief Impact ressistance to -10% (+10%) , price to 50g (+10g)

- Oliephant price to 52g (+7g)

- Hippopotamus price to 40g (-4g)

- Hunter XP from 40 to 37
- Prowler XP from 80 to 74 , price to 23g (-3g)
- Manhunter pierce ressistance to -10% (+10%) , price to 50g (+8g)

- Lion Adept XP from 100 to 85 , price to 33g (-2g)
- Lion Master price to 57g (+12g)
- Lion Renegade XP from 100 to 85 , price to 33g (-2g)
- Lion Maverick price to 55g (+10g)

- Strider XP from 70 to 65 , price to 25g (-1g)
- Wind Walker pierce ressistance to -10% (+10%) , price to 48g (+13g)

- Shaman XP from 100 to 85 , price to 31g (-3g)
- Warlock XP from 100 to 85
- Spirit Welder price to 57g (+7g)


EFM - Imperialists
Few XP and pricement adjustments

- MAX LEVEL AMLA XP values from 100 to 120 (115 for lv2 slingers)
This is sometimes a problem, requirimg AMLA to get strikes which is not of help.

- Ballista XP from 50 to 46
- Bolter price to 33g (-2g)

- Avalanche price to 62g (+17g) , AMLA XP from 100 to 120
- Tank price to 57g (+12g) , AMLA XP from 100 to 120

- Hoplite arcane ressistance to 15% (-5%)
- Phalanx arcane ressistance to 15% (-5%) price to 55g (+13g)
- Shock Troop all physical ressist to 10% (-10%) , XP from 100 to 90 , price to 37g (+1g)
Charge is very powerful... it needs to be considered in unit design...
- Gargantaur blade/pierce ressist to 10% (-10%) , price to 62g (+17g) , AMLA XP from 100 to 120
- Stalwart price to 30g (-2g)
- Praetorion price to 55g (+15g)

- Velite XP from 70 to 63 , fire ressist to 10%
- Equite fire ressist to 15% , price to 43g (+3g)

- Slinger XP from 39 to 36
- Flinger AMLA XP from 80 to 115 
- Spiker AMLA XP from 80 to 115

- Centurion XP from 100 to 84 , price to 34g (-6g)
- Primus XP from 140 to 115 , price to 57g (+7g)
- Legatus all Physical ressists to 15% (+5%) , price to 80g (+15g)


EFM - Pygmies

- MAX LEVEL AMLA XP values from 100 to 120 (115 for max Lv2)
This is sometimes a problem, requirimg AMLA to get strikes which is not of help.

- Knat from 28 to 27
- Fly XP from 44 to 41
- Mudfoot price to 20g (-9g)
- Stinger price to 22g (-5g)

- Piper XP from 50 to 45
- Charmer melee damage increase to 4-3

- Puma XP from 42 to 38
- Lynx price to 28g (-2g)
- Saber Cat price to 48g (+8g)

- Spider Rider XP from 50 to 44
- Great Spider price to 34g (-4g)
- Web Spitter price to 36g (-4g)

- Grand Cocodrile price to 27g (-2g)

- Wyrd price to 33g (+3g)
- Lizard Eye price to 55g (+5g)
- Sorceress price to 57g (+12g)

- Lizard price to 6g (+1g)


EFM - Sea States

- Lv3 AMLA XP's from 100 to 120

- Concoctionist fire/cold res to 10% , arcane res to 30% , price to 27g (-1g)
- Doctor regenerates worsened to self-heal(4) , price to 28g (-4g)

- Turtle XP from 78 to 75
- Snapper price to 44g (+5g)

- Composite Bowman XP from 44 to 42
- Veteran Bowman price to 29g (-4g)
- Elite Bowman price to 55g (+13g)
These lv3 archers are really insane units lol...

- Sagiharii XP from 96 to 85 , price to 32g (-5g)
- Clibbanarii price to 57g (+12g)

- Liegeman price to 52g (+14g)

- Paddle warship XP from 100 to 85 , price to 32g (-8g)
- Paddle Frigate price to 54g (-6g)

- Guild Officer XP from 90 to 80 , price to 32g (-3g)
- Merchant Lord price to 57g (+7g)
- Retainer price to 27g (-1g)
- House Guard price to 52g (+12g)

- Raider price to 30g (-2g)
- Cataphract price to 57g (+14g)


EFM - Whites

- Lv3 AMLA XP's adjusted to 120

- Keeper XP from 40 to 38
- Huntress XP from 80 to 75 , price to 30g (-3g)
- Bow Lady price to 53g (+7g)
- Storm Lady price to 62g (+17g)
- Storm Queen price to 93g (+33g)

- Raider flat defense increase to 40%
Unit has lv1 damages at both ranges, needs this buff.

- Heat Guard price to 32g (+2g)
- Soul Guard price to 52g (+12g)

- Terror Strider price to 36g (+6g)

- Guardian flat defense increase to 40% , village defense to 65% , XP from 74 to 70 , price to 23g (-1g)
- Sentinal flat defense increase to 40% , village defense to 65% , price to 52g (+17g)
- Vigilange flat defense increase to 40% , village defense to 65%

- Housecarl XP from 80 to 74 , price to 26g (-2g)
- Thane price to 50g (+10g)
- Bard XP from 84 to 78
- Balladier price to 50g (+10g)

---
## [git/git](https://github.com/git/git)@[eb1c42da8e...](https://github.com/git/git/commit/eb1c42da8e21cc2a8dacd21023a179b788858887)
#### Thursday 2023-05-18 22:31:17 by Jeff King

t/lib-httpd: make CGIPassAuth support conditional

Commit 988aad99b4 (t5563: add tests for basic and anoymous HTTP access,
2023-02-27) added tests that require Apache to support the CGIPassAuth
directive, which was added in Apache 2.4.13. This is fairly old (~8
years), but recent enough that we still encounter it in the wild (e.g.,
RHEL/CentOS 7, which is not EOL until June 2024).

We can live with skipping the new tests on such a platform. But
unfortunately, since the directive is used unconditionally in our
apache.conf, it means the web server fails to start entirely, and we
cannot run other HTTP tests at all (e.g., the basic ones in t5551).

We can fix that by making the config conditional, and only triggering it
for t5563. That solves the problem for t5551 (which then ignores the
directive entirely). For t5563, we'd see apache complain in start_httpd;
with the default setting of GIT_TEST_HTTPD, we'd then skip the whole
script.

But that leaves one small problem: people may set GIT_TEST_HTTPD=1
explicitly, which instructs the tests to fail (rather than skip) when we
can't start the webserver (to avoid accidentally missing some tests).

This could be worked around by having the user manually set
GIT_SKIP_TESTS on a platform with an older Apache. But we can be a bit
friendlier by doing the version check ourselves and setting an
appropriate prereq. We'll use the (lack of) prereq to then skip the rest
of t5563. In theory we could use the prereq to skip individual tests, but
in practice this whole script depends on it.

Reported-by: Todd Zullinger <tmz@pobox.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[505143ca11...](https://github.com/git-for-windows/git/commit/505143ca1161b093e5b2711a48d5e796e0a1a43c)
#### Thursday 2023-05-18 22:33:12 by Johannes Schindelin

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
## [jenbroatch/LSC540](https://github.com/jenbroatch/LSC540)@[69684e1c96...](https://github.com/jenbroatch/LSC540/commit/69684e1c9649fc597c54f7b87def16e8b7b4bd46)
#### Thursday 2023-05-18 23:08:10 by jenbroatch

Add files via upload

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.
This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relevant information about the patient.

Attribute Information

1) id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not
*Note: "Unknown" in smoking_status means that the information is unavailable for this patient


https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

---

