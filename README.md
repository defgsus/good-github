## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-25](docs/good-messages/2022/2022-08-25.md)


2,013,397 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,013,397 were push events containing 3,119,565 commit messages that amount to 241,543,064 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[6f2354e694...](https://github.com/MidoriWroth/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Thursday 2022-08-25 00:12:15 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[22d57da140...](https://github.com/carshalash/tgstation/commit/22d57da14091d9bf7d8e1dcb7a5104b3f89eeec5)
#### Thursday 2022-08-25 00:31:56 by LemonInTheDark

Readds Alien Vore (#68312)

* Readds Alien Vore

Aliens can now eat people again. Behavior was removed by #43991 (b6c41e3b328078b72bd0f88fd46719aa99c55be2)
because nasku thought it was weird, and the code was really bad.

I think it's funny, and I've made the code not trashtier.

Basically, an alien can agressive grab any living mob. If they stay next
to the mob, facing them for 13 seconds, they will "eat" the mob,
IE:insert them into a list on their custom stomach.

The xeno can then hit an action button to spit out the mob, alongside
some acid.

If the mob is alive enough to pull out a weapon inside the xeno/has one
on it, they can attack the xeno from inside, dealing damage to the
creature and its stomach. If the stomach drops below a threshold, the
mob gibs the xeno and escapes.

I've done my best to steer things away from horny and into gross, though
I'm aware you fucks do your best to blur that line.

Anyway something something balance change something something lets xenos
abduct people more easily, I'm mostly doing this cause I think it has
soul.

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [jtigues/Ironmon-Tracker](https://github.com/jtigues/Ironmon-Tracker)@[761fe4b0f1...](https://github.com/jtigues/Ironmon-Tracker/commit/761fe4b0f171d6fca47aa72e196aa42680da7279)
#### Thursday 2022-08-25 00:50:38 by Zac Elsik

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
## [computernewb/collab3](https://github.com/computernewb/collab3)@[b69ee9af72...](https://github.com/computernewb/collab3/commit/b69ee9af72d557d9fea335f7ab5f621c9250d990)
#### Thursday 2022-08-25 01:04:27 by modeco80

fix capnp module

oops. my bad.
also cleared out .gitconfig HOLY FUCK there's so much ancient garbage in there

---
## [Y0SH1M4S73R/StarbloomSS13](https://github.com/Y0SH1M4S73R/StarbloomSS13)@[635f518d04...](https://github.com/Y0SH1M4S73R/StarbloomSS13/commit/635f518d04a30c4c9f977c0570d480f8d44e56d1)
#### Thursday 2022-08-25 01:18:28 by notfrying1pans

web edit fuck yoooou

i swear to fucking god if this resets line endings or some shit im gonna scream

---
## [QWERTYghri/ARPv3-C](https://github.com/QWERTYghri/ARPv3-C)@[7a4badcc4c...](https://github.com/QWERTYghri/ARPv3-C/commit/7a4badcc4cfdb17886c66916f2e0e27828234db4)
#### Thursday 2022-08-25 04:02:13 by QWERTYbae

resolved circular includes

I fucking hate my life

---
## [kittstone/better](https://github.com/kittstone/better)@[ba29c41ea0...](https://github.com/kittstone/better/commit/ba29c41ea03f3f0fd55bafe82940b2d1145a573d)
#### Thursday 2022-08-25 04:21:51 by WizardMantis441

GOD FUCKING DAMN IM GOATED WITH SUPPLEMENTAL SAUCE

GOT STORY MENU STATE FROM 446 LINES TO 294 WHAT IN TARNATION I DIDNT EVEN OPTOMIZE SHIT YET

---
## [BratishkaErik/zig](https://github.com/BratishkaErik/zig)@[a31b449b55...](https://github.com/BratishkaErik/zig/commit/a31b449b55c32eba1cb61a48753a6fc98696c98f)
#### Thursday 2022-08-25 04:38:47 by Andrew Kelley

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
## [SonicOriginalSoftware/server](https://github.com/SonicOriginalSoftware/server)@[d9037f4c49...](https://github.com/SonicOriginalSoftware/server/commit/d9037f4c4952cf070c1b3555a6b5ba3f39727d67)
#### Thursday 2022-08-25 06:11:38 by Nathan Blair

filling in with some bullshit domain because the go developers made an insanely stupid decision about how imports work

---
## [rjusto/git](https://github.com/rjusto/git)@[5beca49a0b...](https://github.com/rjusto/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Thursday 2022-08-25 07:05:25 by Ævar Arnfjörð Bjarmason

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
## [Nowaaru/suwariyomi.rs](https://github.com/Nowaaru/suwariyomi.rs)@[342d1ee74f...](https://github.com/Nowaaru/suwariyomi.rs/commit/342d1ee74f7db42335c149934d9b9533735b3a54)
#### Thursday 2022-08-25 09:26:24 by Nowaaru

[backend] update handlers with get_all to handle Some cases (PSA: shitty solution god fuck)

---
## [zMyLlama/videndjurs-aftensmad](https://github.com/zMyLlama/videndjurs-aftensmad)@[82100c91f4...](https://github.com/zMyLlama/videndjurs-aftensmad/commit/82100c91f42fe22e7e5e69d2a7662c5a5f7a837f)
#### Thursday 2022-08-25 09:31:22 by zMyLlama

even more fucking bitch ass nextjs changes

this might finally fucking work

---
## [CherishOS-Temp/android_frameworks_base](https://github.com/CherishOS-Temp/android_frameworks_base)@[3f4ccabb10...](https://github.com/CherishOS-Temp/android_frameworks_base/commit/3f4ccabb1037b7b73030989066ce3508ac040ee1)
#### Thursday 2022-08-25 09:39:29 by Joey Huab

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

Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d36d895b8c...](https://github.com/mrakgr/The-Spiral-Language/commit/d36d895b8ca47bbc95bdded2a6c54676928b3389)
#### Thursday 2022-08-25 09:44:32 by Marko Grdinić

"9:40am. I am up. Yesterday I stopped Pathfinder at 11am, had dinner and went to bed. As a result a feel a lot less groggy right now than I was yesterday. I did the right thing.

I am playing PF, but I set the difficulty all the way to Unfair. It is still easy, but the enemies are actually dangerous now, so it gives me a bit of rush.

9:45am. Let me read Mahoako and Rosen Garten and I will do some writing.

10:05am. I am distracted. Rather than reading the manga, I am thinking about future scenes. It is not even for the chapter I am writing, that one is already set, but what happens after that.

10:35am. I am still thinking about it. I'll start soon.

11am. I am still thinking about it.

I still have doubts about whether I should be working and grinding out a living or whether I should be writing. But maybe it is good enough that you have passion for something and just do it. Some people are passionate about wage slaving.

I myself am passionate about the Singularity. Right now I am in despair as I realize how weak the hardware I currently have is.

I am thinking about some of the thing Euclid will do, and pretty much none of the interesting simulation he will be doing are in any way possible on my own rig. The current hardware is just so shitty when it comes to doing actual ML. I can't do anything with it.

11am. I've really been fucked up for the past year. Those job application that I did on a whim last month are proof of how weak my will really is right now.

I am not sure what I can accept. I've poured so much passion into my work over the past years, but the world is not recognizing it. Nothing is going my way. The Singularity is not really happening the way it should, the AI chip companies are ignoring me, my resume is weak and I am not even sure I want a job. Getting money by wage slaving definitely wasn't a part of the plan unless my parents died and left me stranded.

I really should be backtracking and going the symbolic route. That would give me some success. But without AI chips, that path is really limited. I am not motivated to pursue it. I really felt that I needed functional programming + AI chips to win. With Spiral I have the functional programming needs met.

11:10am. I think I have sense - just leaving my obsession aside is going to kill me. I have zero interest in a normal life. Job, family, friends, I do not care about any of those. I certainly am not going to put in effort to make those my goals. Let ordinary people aim for that.

If I have to be a slave, I'd rather die in a revolt than live with a whip on my back.

11:15am. Wouldn't it be good to face my own ruin here?

I am wondering what my responsibility is, but maybe it is just to show my strong will to the world. Nobody can win when he wants to. Living in such a demonic manner suits me.

11:20am. I should just live, dreaming about better computers.

11:25am. If I could go back 1.5 decade ago into the past, with my current skills, I would have been a lot more successful. But even if I had a million dollars right now, just what could I do with it? Pretty much nothing. I could aim for that chip ahead of schedule. But at the same time, I am guessing there are zero millionaires in the world who are waiting in life for TensTorrent chips. The kind of people to make a million by the time they are 30 don't spend their time exploring like I have.

11:30am. I've been yearning for the path of transcendence. But maybe even if I can't reach it, the world will give me a path just the same.

I need to show my strong will. I won't feel bad about not accomplishing what I set out to do. Maybe it was simply destiny that things turn out like this in this era.

11:35am. Just who can win in this world? There is surely a way of writing a story, the right combination of words that would give me a million dollars in a month. There is the general intelligence program, waiting to be written as well. But who can see it?

Just who can draw out that genius whenever he wants?

11:40am. Everyone wants to be winner when they are kid, but right now, I wonder.

No matter how much I admired the winners, never did that bring me closer to victory.

So there is point in admiring the winners and despising the losers.

There is just the will of a human, and in the future the Inspired Desire.

Sigh...with this ability, just what can I do except put one more sentence into the story. I should do that. It would be bad to stop here wouldn't it. And who knows, luck is a fickle thing. Maybe it will smile upon me after I reach 300 pages or more?

Let me have breakfast here."

---
## [maeannie94/Buy-Adderall-Online-Overnight](https://github.com/maeannie94/Buy-Adderall-Online-Overnight)@[68b913b825...](https://github.com/maeannie94/Buy-Adderall-Online-Overnight/commit/68b913b8257c105bdb794bfa5656dd1ad25904b5)
#### Thursday 2022-08-25 10:04:06 by maeannie94

Create README.md

Buy Now – Order Adderall Online
Adderall is used to treat attention deficit hyperactivity disorder – ADHD. It works by changing the amounts of certain natural substances in the brain. Amphetamine/dextroamphetamine belongs to a class of drugs known as stimulants. The Food and Drug Administration (FDA) approved Adderall in 1996.
Place your order now – Buy Adderall Online
Where To Get Adderall Pills Over The Counter in the USA?
Buy Adderall Online – Order Adderall 10mg, 20mg, 30mg, Adderall XR, without prescription, overnight FedEx delivery, discounted price 20% off at No.1 Online Pharmacy in USA.
Online Adderall Store
 

 
Buy Adderall Online - order Adderall without a prescription overnight shipping at the best price in the USA with Buy Adderall Pill.
Adderall is a combination medicine for the management of ADHD  and Narcolepsy. Buy Adderall 15mg Online It contains two salts of amphetamine, and it belongs to the class of drugs called stimulants. In addition, it has some non-label use of the drug, and as a result, it is also used for non-therapeutic use.
Buy Adderall 15mg Online is available both in immediate-release and extended-release tablets, and the drug's effect varies. The effect of immediate-release and extended-release as the effect of the drug will work for four to six hours, and an extended-release tablet is usually prescribed once daily.
 
How to use Adderall
 
Buy Adderall Online , Read the Medication Guide provided by your pharmacist before you start taking generic Adderall and each time you get a refill. If you have any questions, ask your doctor or pharmacist.
Take generic Adderall by mouth with or without food as directed by your doctor, usually 1 to 3 times a day. The first dose is usually taken when you wake up in the morning. If more doses are prescribed, take them as directed by your doctor, usually 4-6 hours apart. Taking generic late in the day may cause trouble sleeping (insomnia).
The dosage is based on your medical condition and response to treatment. Your doctor may adjust your dose to find the dose that is best for you. Follow your doctor's instructions carefully.
 
>>>>> CLICK HERE TO BUY ADDERALL ONLINE <<<<<<
 
What Is Adderall?
 
Adderall is a controlled drug, meaning it’s available by prescription, for the treatment of attention deficit hyperactivity disorder or ADHD. When someone takes Adderall, and they have ADHD, it can help improve their concentration, focus, and self-control. When someone takes it, and they don’t have Adhd or they abuse it, it can cause them to feel high. Symptoms of an Adderall high include euphoria, increased energy, and a sense of exaggerated self-confidence.
 
Buy Adderall Pills Online
 
Adderall is available in an extended-release formula, Adderall XR. It’s also available in a generic form as amphetamine/dextroamphetamine salts. Buy Adderall Pills From Us And get fastest Delivery.
 
>>>>> CLICK HERE TO BUY ADDERALL ONLINE <<<<<<
 
While the medication is FDA-approved for ADHD and narcolepsy, some medical providers may prescribe it for unapproved, off-label uses. These include treatment of depression, anxiety, bipolar depression and to help people lose weight. Because Adderall is a stimulant, working professionals and students may use it without a prescription to get more work done, to improve focus while studying or with alcohol to get high. It’s one of the most misused ADHD drugs. But misuse of this drug can lead to serious cardiovascular events or sudden death, according to the Adderall drug label.
 
>>>>> CLICK HERE TO BUY ADDERALL ONLINE <<<<<<

---
## [Daffa06/NoName-X00T](https://github.com/Daffa06/NoName-X00T)@[233ecce43e...](https://github.com/Daffa06/NoName-X00T/commit/233ecce43ef6be6d50e36d9beff90c9c11539fd2)
#### Thursday 2022-08-25 11:43:32 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>

---
## [JS1209/front](https://github.com/JS1209/front)@[f9f14b596a...](https://github.com/JS1209/front/commit/f9f14b596aee0ae0fa1c82223586a438dfd93970)
#### Thursday 2022-08-25 14:49:31 by JS1209

bitchass shit finally works but seriously dont know who. Fuck middleware and fuck mister middleware for inventing it :)

---
## [carolgeng/tremor-runtime](https://github.com/carolgeng/tremor-runtime)@[bdcc1c716f...](https://github.com/carolgeng/tremor-runtime/commit/bdcc1c716ff69ade53c3cd34faa12697f19c1f83)
#### Thursday 2022-08-25 15:31:51 by Sasha Pourcelot

Enforce "no mod.rs files" via clippy lints

Back in spring when I was working on the [ClickHouse sink][1], I had
[an interesting comment][2] stating that Tremor prefers using `mod_name.rs`
files instead of `mod_name/mod.rs` files.

(*In my opinion this is bad, but let's not discuss this here.*)

Once my work got merged, I started wondering if we could statically check this
and make `clippy` emit an error if it sees `mod.rs` files. Turns out there's a
[`mod_module_files`][3] we can `deny`. That's basically what this commit does.

The resulting compilation error is just as friendly as it needs to be:

```none
$ cargo clippy
    Checking tremor-runtime v0.12.4 (/home/ssha/git/tremor/tremor-runtime)
error: `mod.rs` files are not allowed, found `src/should_not_compile/mod.rs`
  --> src/should_not_compile/mod.rs:0:1
   |
   |
note: the lint level is defined here
  --> src/lib.rs:25:5
   |
25 |     clippy::mod_module_files
   |     ^^^^^^^^^^^^^^^^^^^^^^^^
   = help: move `src/should_not_compile/mod.rs` to `src/should_not_compile.rs`
```

I `deny`-ed this on the following crates:
  - `tremor-runtime`,
  - `tremor-api`,
  - `tremo-common`,
  - `tremor-influx`,
  - `tremor-pipeline`,
  - `tremor-script`,
  - `tremor-value`.

Feel free to request the addition of this lint elsewhere. I may have forgotten
some crates :).

It turns out y'all did a great job at maintaining this at each code review, as
I had no compilation error once all the lint were added.

Thank you for your work!

[1]: https://github.com/tremor-rs/tremor-runtime/pull/1538
[2]: https://github.com/tremor-rs/tremor-runtime/pull/1538#discussion_r904836976
[3]: https://rust-lang.github.io/rust-clippy/master/index.html#self_named_module_files

Signed-off-by: Sasha Pourcelot <sasha.pourcelot@protonmail.com>

---
## [stulu08/SEngine](https://github.com/stulu08/SEngine)@[a83fea216a...](https://github.com/stulu08/SEngine/commit/a83fea216a1e2d8a53653078e5d6371ca8161790)
#### Thursday 2022-08-25 15:57:16 by Stulu

You can now render 1000 spheres using gizmos in just 10 draw calls using instancing. WOW isnt that amazing. I mean its kinda not but i just wrote the code in school without google and 0 knowledge and it magicly just worked...

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[dba5139b13...](https://github.com/mrakgr/The-Spiral-Language/commit/dba5139b134ae8b5ac186b980703345589454d49)
#### Thursday 2022-08-25 16:01:42 by Marko Grdinić

"12:15pm. Just what is being a programmer in this era? Nothing. I thought I was good at it, but there are other people who can do that. Maybe I've been destined to become a writer from the start.

I was wondering what my rank in writing is? I said it is not 5, but I do have the most important prerequisite for it, which is a mature vision of both the meaning of life and what the universe should be. Back in 2014, I just opened the door a little on it. It was a wild ride that lead me into despair.

So why not aim to exceed the me from 2014? Face the old me.

I thought that I'd become a programmer, but programming might be destine to become a part of my writing skill.

I should do it for real this time.

12:25pm. In 2014 I've had all kinds of insecurities about whether other people would accept me. I was right to go insane. Just who would accept a universe where there can be only one winner. That thing past the end of Torment arc where god goes around giving chances is complete nonsense.

12:30pm. Maybe it should have been obvious. Just because I can figure out the universe, does not necessarily mean I'll have the power to put the key into the lock.

12:35pm. I thought I would just get to writing today, I didn't think I'd become introspective in such a manner. I think I am going to step away from the screen for a while.

2:15pm. I just don't know how to live in this present era. Are dreams and desires only allowed to those post-humans like Euclid?

Should I be writing or should I be working at a job?

There is one thing I am sure of - what I did was not programming. Programming is what I see when I look outside the window. The nature itself is the ultimate programmer. It has the right device and the right algorithm. I have neither. I've just been fooling around.

I thought I was good, but maybe I've been a writer all along. I thought that when I stopped writing Simulacrum in 2014, that was it for me as a writer, but Spiral was the spiritual successor to it.

Should I have accepted that 2.5k offer by Z?

Just what do I know what the right choice is.

2:20pm. Maybe this is the point of Heaven's Key. I'll show the world how to live in the future, so in return I'll ask it to show me how to live in the present.

Is Singularity all about the money in this era or is there something else to it?

This grief, this sadness, this disappointment, just what do I do with it?

I can only use it as a catalyst for me writing.

It is just too much to expect to be successful, but maybe just maybe I'll get an answer to where I've been going wrong in my life. Let me try writing.

$$$

(Heaven's Key, Computer shop)

Vividly, the image before me crystalized into my eyes. In front of me, past the glass pane of the shop were cores! Brain cores! Shining, gleaming, brain cores!

Excited, I ran quickly into the shop, not even realizing how strange it was that while all the other shops were locked, this one didn't even have a lock on the door. The door just swung open for me automatically.

I grabbed a brain core off the shelf, using a mental command I tried connecting to it, and found that it worked. It worked just like the real thing. The brain conversion options were already there, but I could not use it as my brain was already a core, even in the simulated world. Using the core I grabbed off the shelf, I could see a diagram of my own brain. My thoughts turbulent, I realized that all the NPCs here could in fact enter the self-improvement loop and become the Inspired themselves. I thought I had huge advantages, but that wasn't the case.

If I had something special, it is not talent or intelligence, but desire.

I wanted power, but as it happens, I was the only one in this world who was filling to pay the price for it.

I thought it might as well be me in Mickey's place. If nobody gave me a chance, I would just be another ghost in the garden, but that is not the case. The chance has always been there, but Mickey never took it. I understand it now.

I am special, and it is my desire that makes me so. Whoever made this world saw to it that justice existed in it.

It is what I would have done. A universe where all of those with desire can rise is a just one. It is enough to give a chance to other people, it is not anyone's responsibility to make them want to take it.

I clutch the core to my chest and then pocket it, intent on bringing it out of here. My mind that was wavering becomes steely and I decide.

I won't take it easy on the NPCs, and I won't regret the battles that are to come.

I swear it on my desire, that I will rise. I will escape this city and into the real world beyond.

(Heaven's Key, Streets)

I march out of the shop, intent on my destination. At this point due to all the aimless wandering, I've become completely lost, but it should not be hard to find my way back to the inn. I scale one of the larger apartment buildings, and from the high vantage points of the external corridor, in the distance spot the rollercoaster I rode with Lily. Establishing the direction, I get back to the streets and head towards it. It has been a couple of hours since I went out into the city, and in a few more I am guessing the morning should arrive. I remember that cores exist in this world, and on mental command I try accessing, not the real world core which houses my actual self, but the one in the game. A sense connects to it, and I bring up the time.

4:38am.

I have time. If it becomes known that I slipped out of the inn during the night, Lily might get suspicious of me, I do not want her to think that I am anything more than an easy mark. I want her to show me around more casinos. Right now she is my only connection here.

It won't take me more than an hour and a half to get back to the perimeter, but then I'll have to spend time figuring out where the inn was.

I get an idea, and try accessing the core I pocketed from the computer shop. I tried searching for a map application, and to my pleasant surprise I found it. The game core, I'll call it that as opposed to the main core I am on, has a tracking ability. As long as I make use of this, I'll never get lost again in the future.

I am feeling pretty lucky right now. I mean, I just found some guy in a park to talk to, as well as a computer shop. It is not like finding some priceless treasure by accident, but everyone in this world is out to get me, so finding my footing, and so quickly, is a large gain.

Block by block, I make my way to the perimeter. In the distance, I can see the sun's rays starting to break out.

(Heaven's Key, Perimeter)

I finally got back to the familiar area where I first came to the city. Not far from me, I can see the restaurant where I met Lily. I check the time.

6:10am.

It won't be long before people start waking up, so I have to get back. I put a marker on the core's map to indicate where I currently am and scroll it, trying to find the nearest resting places. It seems that map is somewhat out of date. Some of the buildings, in particular the circus tents, which I can see around me do not seem to be on it. Neither do the new venues built in the middle of intersections. Maybe the map on this core is how the city was originally?

I think about it for a moment. Yeah, that is most likely the case.

On impulse, I decide to just save here.

6:15am.

It would be best for me to try to retrace my steps by feeling rather than relying on the map. The inn should not be too far from where I am, but if I get lost, I can always reload to where I am and try again.

(Heaven's Key, Side of the inn)

My sense of direction does not seem too be bad. It took me quarter of an hour to find my way back to the inn. When I slipped out a couple of hours ago, it was through the window. I did that movie trick where I tied a couple of bed sheets together in knots and use them as a rope. My room was on the second floor, so it wasn't too high up, but not so low that I can just jump up to it. The bedsheet rope was still there where I left it, snaking out of the open window of my room.

I came up to it, and gave it a little tug as a test only to have the sheets unravel midway.

Right now, I am stuck with having a sheet in my hand, thinking what I should do. I observe the other end. Though it would be rough, if I did a little run and skid up the wall I could probably grab the other end and let myself in that way. I crumple the bedsheet in my hand into a ball and throw it into the room. Then I back up and prepare to take a run. Just before I start, I get an idea. I remember the night in the park, and how Mickey taught me to manifest food. And he gave me an idea to how to unlock doors using gel.

Instead of straining myself here, let me try making a ladder.

In my hand I manifest a chip and focus my will upon it.

Ladder, ladder, ladder...

I visualize it in my mind and project it into the space in front of me. I feel something trying to come out, but it is difficult.

My image is vague, but I persevere. Rather just any kind of ladder, I think of a wood ladder I once saw used. I remember and focus on the dry feel of food. I focus on how the bars are slotted into the two pillars. It starts to feel vivid. The wood ladder manifests in front of me, right where I wanted it to be. I realize that I feel a certain connection between the chip in my hand and the ladder. I don't probe it with my sense, instead I pocket it and grab the ladder bar and start climbing my way up. It is a short climb, and go through the window unimpeded. Then I grasp the chip in my hand, feel it out in my mind and cut the mental connection between it and the ladder.

I stick my head outside and confirm that the ladder has vanished. After that I drag the sheet that was sticking out back in and close the window.

6:40am. Safe!

As I check the time, outside, I can see people starting to go about their business and the city becoming lively. Maybe somebody spotted me climbing back into my room, but it does not matter. Since I was getting back in, they'll be able to deduce that I was playing hocky during the night rather than a burglar. There isn't a crime to report and I doubt whoever is Lily's boss has eyes everywhere. The pattern I've established won't be distrupted.

Sigh. I plop myself on the bed and take of my shoes.

I am quite tired right now. I went out at around 10:30pm and have been wandering all this time. 8 hours of physical activity is enough to make my feet quite sore. I rub my head against the smooth pillow.

I lie there for a while. I can feel myself getting drowsy.

This is not good. If I fall asleep here, Lily will come by to drag me out just when I am getting some shut eye.

With a mental command, I save and then exit the game.

(Helix Studio, Regent Suite)

I'll have to make some compromises. I can't avoid having my body be tired, but if I get a good night's rest in a different place, it will be reflected inside the game. 8 hours of exertion is not enough to allow me to fall asleep, so for the next 4 hours I might as well watch anime and play regular games.

Right now I am in the very luxurious living room of the cruise suite. I grab a cola from the fridge, pour myself a glass, and then start exploring the place. I find the bedroom. The bed is oversized as one would expect, but as if the designers knew what I like, they placed a desk with a PC there. I seat myself in my rightful place, and push on the power button on the black case. The monitor comes to life. The OS is of course prepared. The Internet speeds have gone way up since the Singularity started, so I don't find it hard to pirate a game and start it. Before I get into it, I close the shutters to darken the room. Only a couple of rays are getting in through the cracks, just the way I like it. I sit myself back on my battle seat and start clicking away.

Ironically, despite being legacy hardware simulated on the core, the computer is actually better than the one I have in real life. It has the latest AMD CPU and the Nvidia GPU, I've checked the setting.

Playing games inside a game, this really is the next level! I become immersed.

After a couple of hours of battling monsters, the fatigue really starts hitting me. I hit the sheets, and with a mental command change the environment settings to night time. What was once a clear day immediatelly shifts to a starry night. No longer bothered by the light, I shut my eyes and let the sleep come to me.

I don't have school tomorrow, so I do not have to worry about the time.

(Heaven's Key, Inn)

    In the dark days remember,
    Necromutation is Transcendence.
    - Loading Blurb

"If Lily, the guide who was with me before, comes by tell her I'll be at the casino we were yesterday." I told the proprietress of the inn and left.

(Heaven's Key, Streets)

It was early morning, and people were starting work. Mickey told me that new arrivals happened between 7 and 12pm, so people have to be ready to welcome them. Scamming them out of money was what powered the city's economy. I really gained a lot from Mickey explaining to me that we are all active illusions here. It is possible to infer a lot from that.

None of the citizens, as opposed to arrivals, had to work for food specifically. It is easy to understand why that is, they can just magic it out of thing air. Furthermore, there were no diseases here. Neither did people age, as they were holograms. Mickey didn't know how old the city was, but even so, that might be that there might be people here who are thousands and even tens of thousands of years old. As for getting injured, those would need a doctor, but not like in the real world. In this city, the doctor would be a hypnotist trying to convince the patient that his arm isn't broken, once that is accomplished it would become the truth. Furthermore, everyone in the city was an arrival from the world below, there were no children born of pregnancy.

Given all that, without having to worry about food, shelter or health, it is easy to see what the citizens would be obsessed about. Money.

This is a really good environment for me to learn to gamble.

As I made my way through the increasingly busy streets, I remarked this to myself. The golden rays of light illuminated the streets in their luster. The dawn had arrived.

(Heaven's Key, Raven's Eye Casino)

Raven's Eye Casino was not a large building, its defining trait was the cartoony logo of what appeared to be a raven's claw clutching some circles. Playing here is going to essentially be my job for a while, so I better get used to it. I intend to make use of the mind controlling program if I ever sense myself getting tired of it. Retreat is not an option. I have to win here. I need to find what my limits are. Only after I grasp what they are, can I start work on exceeding them.

I push the door open and make my way inside. I do not bother the receptionist and instead make my way straight to the game room. If Dale is there, I'll play against him and his group, otherwise anyone is fine.

I save here.

If the bet is something like a single chip, I'll let the result be as it is. In fact, losing minor games would be good, as it would make Dale and the guide more confident about raising the stakes against me. There isn't any doubt whether I'll win or not. This is a game, and I can't possibly lose it with the ability to save and load it. The real risk is me getting tired. Right now, everything is fun and exciting, but how will I feel after playing for a year? 10 years? A 100 years?

Imagine living like this for 10,000s of years, stuck on this brain core.

Before I uploaded myself, I could barely stand school for a single week. Will I really be able to do this?

(Heaven's Key, Game floor of the Raven's Eye Casino)

I look around for Dale's group, or anyone else for that matter, and it seems nobody is here. I idly wonder if there might be some people here, just in the duel space? Mickey called it the shadow realm. What do I do now? Awkward, I wander around and checking the seats, I realize that some of them have white dics on them, like tags. I think about what it might mean, and I realize that they might be there to indicate that the host is currently in a duel. If I try moving it...

I try picking the tag up, and my hand passes through it. This confirms my suspiction. Such an illusory thing is definitely this game's style.

I check the other tables in the room, but none of them have these dics on the seats. Since I am eager to start, I take an empty seat at the table with the discs. I wonder what would happen if I was sitting in the seat that was already occupied and the host returned from the duel? I might get telefragged, so it is best that I do not risk.

I spend some time like that, just waiting...

~~~

High above the surface of the world, golden cities floated, shinning their radiance on the world below. In the side of Earth that was lighted by the sun, there were like dots, but closer to the shadows where the vantage point was there were such islands of light.

"Euclid has started playing the game."

The scenery shifted to show him playing with a different group from yesterday. Compared to the adults around him, he was nothing more than a glasses wearing kid, focusing on the game in front with a smug look. He tries his best to keep a poker face when in the hand, but when he wins he smiles, and when he loses he feels the sting. He gets careless when he is out of the hand.

"He imagines this is how he would rise."

The scenery changed to him going into the casino in the morning, and then immediatelly the afternoon came and showed him stepping in the opposite direction.

"It is not like that."

A scene was shown of Euclid at the table going all-in. What was once a small stack, increased and increased.

Euclid was seated at the table facing his opponents. And behind him was an enormous pile of chips as tall as a mountain. Hundreds of thousands, millions!

"No!"

With red paint, that scene became crossed out.

"Euclid thinks he has time to play around, but a fuse has already been lit."

A scene of a lit fuse leading to stacks of explosives came about.

"Unbeknowst to him, the preparations to eradicate him are already being made..."

The scene changed to a building deeper in the city. Inside it, the guide Lily was seated at the desk of her office looking ready to begin he work for the day.

~~~

(Lily POV - Heaven's Key, Lily's Office)

After giving one last check to my attire, I put away the mirror and prepare to step out of my office, when I hear a knocking on the door.

"Enter." I call out.

"Hello." A young woman entered. She had a youthful face, and a her short hair was in twintails. This innocent look was out of tune with the military style camos she was wearing. "I have a report, boss."

I knew her well. Last night when that kid started avoiding payment and gave me that ridiculous story about throwing himself off the school building due to not wanting to work, I immediatelly became suspicious of him. I gave a task to some subordinates of mine to keep track of him so he does not slip away with the chips. I also requested the intelligence department to look into his background. Though it is rare that a citizen would pretend to be a newcomer, it is not impossible. Right now I am afraid that Euclid might be a weak expert trying to make use of me to fish.

If that is the case, then there is no point in me trying to act friendly. I'll just request an enforcer to take care of it and move on to the next assignment.

"I didn't expect to hear from you so early. Have you found anything suspicious about the newcomer?"

"I saw him slipping out his room last night. I followed him the entire time."

"Tch!" I clicked my tongue. "I knew it, I am the one getting tricked here. I'll have an enforcer take care of it." I seat myself back at my desk and lean in. I shake my head in disappointment. Requesting an enforcer would lower my evaluation, but it couldn't be helped.

"No, I don't think he is a hustler. Based on what I've observed he really is a newcomer."

"Really?" I look at her slightly incredulous. Lisa nods and seats herself opposite of me. "Let me show you some of the fotage. Typically when people are with others, they put on appearances, but when they are alone their true intentions come to light. I am quite sure he didn't notice me following him."

She picks out a core and sends some data over to me. We start going over it.

...

"After he left his room, take a look at how he is looking around at the streets as if everything is new to him."

...

"Hello, is anyone in there!?" I saw a video clip of Euclid yelling and slamming on the appartment doors. I looked at Ellie, as if seeking confirmation. She nodded.

"I have it all recorded. He spent two hours trying out various apartments to see if any were empty." Ellie explained. "He must have given the people inside some of them a big scare. Nothing good happens in this city when somebody visits in the dead of night."

...

I saw Euclid sating himself on the park fountain. Then followed the two-man night party between the ghost he had met and him.

"That is a lot, kid. You shouldn't have given me so much. Once you drop to 0, you'll die you know?" After a moment of thought, Mickey asks. "How much do you have left?"

A bit later I saw him giving 20 chips to the ghost for what was basic information my supervisor taught me on my first day here. I pause the clip.

"Ellie, send somebody to get those chips from the ghost." I told Ellie.

"Already did boss."

"Good job."

...

"Here is the part where it gets interesting. I only showed you some clips, but the kid spent 8 hours acting like a tourist that just got here."

The clip she showed was that of Euclid looking at an open window on the second floor of a building. He was outside the inn, and had to get back in through the window of his room. A bedsheet rope was leading into it from the outside. He gave a tug and it unraveled. Then have backed up, tossed the loose sheet inside and posed as if he wanted to make a run for the wall. Just as he was about to start, he changed his mind, calmly walked up to the room and manifested a ladder. The he went up it inside.

I knew what Ellie was trying to show to me. A citizen who was trying to commit a crime would have never acted like this. A citizen woudn't wander around doing stupid experiments. At the very least, he would not spend time thinking about how to get up to the second floor, but just bring up the ladder immediately.

Euclid really was a newcomer. Really?

"When he clipped out, I expected he would met up with his accomplice to hand over the chips he had gotten, but what happened instead is that he just toured the city. I was really surprised."

"And you say, it is not likely that he is pretending?" I asked for confirmation.

"Sometime people coming from below are familiar with using the brain core to manipulate their own emotions, but that kind of thing is limited and they tend to act robotically. Such people tend to be hard working, but that sort of mental hacking is not good at immitating curiosity and surprise."

For that reason, people tend to not use it here. I sometimes use it when things get tedious, but my supervisor taught me not to rely on it as it inhibits creativity too much.

"I'd bet on it that he really is a newcomer." Ellie continued.

I tapped my finger on the table, deep in thought.

"I guess I'll hold off on calling an enforcer then." I sighed. "Thank you, Ellie."

"You are welcome, boss!" She beamed.

"You can leave. I am going to have to make some arrangments for this."

"I've been up all night, I am going to bed." Ellie stretched. "Lisa is tracking him right now. Since Euclid has been up all night and must be tired, now is a good time to try to squeeze him dry."

"Okay."

"See you tonight." Ellie gave a little wave and opened the door before fading into invisibility and vanishing into thin air. There was only a slight visual distortion in the air as she closed the door behind her, and then I was alone in my office. I couldn't hear her footsteps when she moved like that.

I think for a bit and then I make a decision. Even though calling an enforcer would lower my evaluation, I have other things to do than trying to pull a thorn in my side. Even if Euclid might be a newcomer, if he is good at cards, then it is not worth it for me to try to gamble it out of him. Yesterday he's had a lot of luck so I am not sure what his skill is. I'll play with him today and if it looks like he is good, I'll abort and move on to the next mark.

I've been in this city for 50 years, so I am good at cards compared to those below. I should be able to tell whether he is a young online pro or a fool. Well, even if he is a former, he can't compare to the actual experts fighting life and death matches here. Since he wasn't chosen to become a citizen, he is going to lose either way in the end. It is a pity.

But that is how we in the city live.

Unless we want to disappear ourselves we have no choice, but to take from those who wander in.

(Lily POV - Heaven's Key, Shadow realm)

In the abysal realm of shadows, seated at the table are just me and Euclid. Initially, there were 6, but Euclid buster the other 4 and is now sitting on a towering pile of 466 chips. Meanwhile, I managed to win a hand and am at 134. Almost a week had passed since I along with Dale's group started playing against him.

As I focus the button gets passed to me, and the ante of 2 life chips gets taken from my pile. Meanwhile, Euclid is the first to go and antes 4.

Two cards get dealt to each of us. Carefully, I take a peek at my own.

Ah Qd.

A very strong preflop hand heads-up.

"Check." Euclid checks to me. Gingerly, I look at Euclid, probing for his reactions and not getting much, raise to 8.

He thinks about it for a moment, and calls. As soon as he does, the flop cards manifest themselves on the table.

Qs 2h 6c.

"Check." Euclid looks at me with a focused gaze. He isn't bored, and I get a sense, that he might have something in this hand. A low pair, maybe the gutshot, or even a weaker high pair than mine?

I make a pot sized bet of 16. Euclid thinks for a moment, and calls, bringing the total up to 48.

Qs 2h 6c Th.

I immediatelly put him on the gutshot. He most likely has 35 in his hand. But since it is him, he could have something like a flush draw now, any two hearts. He could even have a J9 or JK. Not hesitating, I bet 48 into the pot, and Euclid after tanking it for a while goes all in.

I am definitely going to call.

"Call." As I do, I pray to dear god that he does not hit his card on the river.

Both of our cards get revealed.

3c 5c.

It is just as I thought! Please, let him miss!!!

Over the past week him winning in these kinds of situations where he is 95% sure to lose happened so often, that I don't have the least sense of being ahead in this hand. As I try to keep myself from collapsing mentally, the next card gets dealt.

4h.

Sure, enough he won.

(Lily POV - Raven's Eye Casino, Game room)

"Sweet!" Euclid is happy to have won, but as I look at the rest of the group, they look like their spirit is leaving from their body. Completely deafeated, I slump back in my chair and just let it out.

"Hahhhhhhh..." My eyes are half closed and I do not even realize that I am looking at the ceiling. I just want to run away, be anywhere other than here. I was like this yesterday, but then used the brain core to regulate my emotions. This just resulted in me losing even more money.

Pretty much every game was like this. I was prepared to abort and go the other way if Euclid seemed halfway decent. But Euclid's game once I started playing him was absolutely terrible! I very rarely see him getting his opponent to put money in with a worse hand. Instead, he chases drawns like a monkey, hits them and then cashes out. What a clown! He always, always puts money in when he is behind, but ends up winning! I keep waiting for his luck to run out, but it never happens, it is ridiculous!

I glare at him for a moment, and I see him counting his chips with a happy look.

6720!

I wanted to get his 100 chips, but instead lost 66 whole lives and wasted a whole week trying to get his!

Newcomer or not, it doesn't matter anymore! I can't afford to make any more losses.

I get up from my seat.

"Lily, are you going already?" Euclid asks me.

"Sorry, I'll cut it short today. I'll be busy tomorrow." I want to curse at him, but muster all my professionalism and make a smooth exit. Leaving the group behind, I can hear him saying.

"What about you guys? Duel?" I do not have to look around to see the rest looking at him wearily.

(Lily POV - Geoffrey's office)

I spend two hours composing a writen report and with it stored, leave my own apartment. I make my way a couple of blocks deeper into the city. Inside an apartment building, I come by my superior's office and knock on the door.

"Enter." I hear his voice. I mentally prepare myself for an apology.

"Hello, sir." I gret him, and take a seat.

"Hello, Lily. What can I help you with?" He smiles at me. An older man, my superior is wonderful. Always curteous, helpful and professional.

"I came to get some advice and also request an enforcement. I am trying to release a newcomer, and am currently 6620 chips in the red as a result." His eyebrows shoot up. I can barely look at him in the eyes. This has never happened to me before. I am can feel myself getting flush from embarassment!

"How did that happen?" He adjusted himself in his seat.

"I have it in my report so please look at it." I sent him the email with the report.

"Okay, I'll take a look right now. How long have you been following him?"

"About a week. I thought he was a newcomer, but now I am not sure."

...Some time passed as he went over my report. I patiently sat in my seat, answering an occasional question. At the end of it he cleared his throat.

"I'll go take a look myself tomorrow. He usually plays at the Raven's Eye, right?"

"Yes. Will you not be sending an enforcer immediatelly?"

"I want to see whether he can really predict the cards that are coming out. If that is the case, sending low ranked and even medium ranked enforcers would just result in their deaths."

"I see. What should I do now?" I asked for instructions.

"You don't have to worry about it anymore, go get some rest for a few days and then guide another." I feel nothing, but relief to be done with this wretched case.

"Thank you, sir."

"Go get some rest, you look tired."

"I will. Goodbye, sir." I give him a smile and leave the office.

(Report by Geoffrey to the Enforcement Department)

Subject: Episteme-level enforcement request

One of the newcomers of about a week ago is currently in posession of 8210 chips. I've played him personally, and in my estimation, he is at the very least a peak ranked Aleator who possess the ability to track cards beyind the dimensions, or most likely an Episteme. Weirdly, based on his emotional reactions, he does not seem to have actual gameplaying skill, but that seemed to be working in his favor so far. He would be extremely dangerous for even Aleator ranked enforcers to challenge in a resolution, so I request that this enforcement action be taken up by a top ranked player. He is capable of knowing not only what cards his opponents posses without the use of marking techniques, but he also knows which cards will come out next using methods that are completely unknown to me.

We've done extensive background checking and confirmed that he is a newcomer, but my recommendation is to disregard that fact during the decision making.

In the attachments are the report I received from my subordinate guide as well as my own. The reports have extensive recording of our games with him.

~~~

At the heart of the city, in the Enforcement department, a furror was caused by the report.

"Episteme-request?" One young man said.
"Did you say..." A woman replied incredulous.
"An Episteme request? That hasn't happened in hundreds of years!" An older man said.
"Euclid? Never heard of him." Another noted.

They were all discussing it around a table, clamoring. It was the most interesting thing that had happened in a long time.

A scene was painted of a busy meeting, of people pointing and shouting. The enforcement department was giddy like kids.

In the end, the request was passed on. It went through the air as wireless signals into a part of a city that looked lavish. A mansion fit for a billionaire stood there.

Seated at a poker table, was a man with vertiginous white hair and a sharp, glowing gaze, dressed in a bathing robe. His right hand was resting on a small pile of a 100 chips.

An illustration of such a scene did not seem weird, but as the camera panned backwards, the pile that was blurred out behind him came into focus. They were all life chips. 100,000s of thousands would be too small to count it. The huge pile, a mountain of treasure absolutely dwarfed the man himself. The golden life chips sparkled in the darkness.

~~~

(Euclid POV - Heaven's Key, Streets)

Leaving the casino, I made my way back to the inn with a spring in my step. I might be a cheating bastard, but I never thought living like this could be so satisfying. I haven't heard from Lily for a while, but some old dude Geoffrey came by to take her place. It felt like he was probing me, but there is not much I can do about that, but take the money he offered me. He didn't seem to mind much, but Dale's group has started giving me the stink eye. It is only a matter of time before the breakup comes.

Right now I am at 9380. It won't be easy finding another group willing to play me for these stakes.

As I think, not really paying attention to my surroundings, the sun goes below the horizon.

I don't care about that, only how well my plan is going, but all of a sudden at the corner of a street I see a man come out, staring at me directly in the eyes. I don't bother with him and continue moving, but he goes directly in the middle of my path as if trying to intercept me. Dressed in a gray trenchcoat, he has a sharp gaze and white vertiginous hair as if he used too much hair gel. His hands are in the pockets of his coat as he stares straight at me. Uncomfortable, at the attention I come to a stop.

As I am about to tell him to move aside, my voice gets caught in my throat when I see him taking an object out of pocket.

Ah shit, it is a revolver, I am going to get robbed!

It happens very quickly, without hesitation, he points it at me and fires!

My reaction to that is to expect to eat a bullet, and I flinch, crossing my arms in front of me. But I do not feel piece of metal hitting me, instead I feel the familiar sensation of being drawn into the world beyond.

(Heaven's Key, Heavenly realm)

A blinding light comes over my eyes, and I squint.

"Ghhhhh!" It feels bright, overwhelmingly bright, but a bit by bit, the area comes into focus. My eyes get used to it and I realize where I am.

At a poker table, much like the one in the duel realm. But whereas that shadowy realm's background was darkness and blue nebulas, similar to a night sky, the background here was golden and white. Above I can see a small, very bright sun shining down on the table. Turning my eyes in front, across the table I come face to face with the man who turned a gun on me.

"Hello, kid." Languid, he greets me.

"Who the hell are you?" I ask him. He shrugs, refusing to answer. I look around. "What is this? I thought I was going to get robbed."

"A resolution. It is not a duel, but a death match. Unlike a duel, all of our chips are on the line and the winner gets everything. This match will only end if one of us goes to 0 or if both of us agree to abort." He explained.

I probe around with my mind and I realize that unlike in a duel where I get 100 chips regardless of the buyin, here I have my entire pile of 9380. I see that I am on the button and the antes are 1/2.

"Is this still NL Holdem? The stacks are very deep." I remarked.

"There no pot limits in this Holdem game. It is all no-limit Holdem in this city. It has been that way for a long while."

"Do the blinds increase as the game goes on?"

"It doubles every 18 revolutions. Your deep stack will be shallow pretty soon if you keep folding. Come at me with everything you've got!" He challenged me.

"That is what I intend!" I slammed my hand on the table, angry at him. "Go ahead, you are first!"

The man in front of me grinned, and fished around in his pocket instead checking or raising. A grim feeling comes over me as I remember what came out of that pocket last time. Don't tell me!?

The gun comes out of the pocket. I recoil in my seat and try jumping out only to run into an invisble wall. It is no use, other than the invisble box the players are in, it is impossible to move away.

Bang!

Unlike in the street, this time I feel a sharp pain in my chest. I look down and horrified I see a bloody hole where I've been hit. Slowly, I see blood spreading across my shirt.

Bang! Bang! Bang! Bang! Bang!

I have no time rest as the whole revolver is emptied into my body. Six holes in my chest, I feel weakness wash over me and slump on the table, no being able to feel a finger. In front, I see my two unupturned cards. As I lie there trying to stay awake, a puddle of blood spreads over them.

As much as I try, I absolutely can't move even a finger. I remind myself that all of this is not real, and that I am a hologram. Quckly I give a command to the mind controlling program to raise my mental state. It quashes my fear, but regardless the feeling of weakness is overpowering and soon I lose my senses. I can hear the man saying something, but it feels far in the distance and darkness overcomes me.

My senses leave me, and I feel my thoughts slowing down.

I die.

$$$

3:30pm. It is only this late. How much have I written? 1.1k words.

What comes now is a report by Geoffrey.

4:10pm. 5.8k. I added a bit.

4:20pm. I am thinking how things should go. The chapter is almost over.

5:40pm. This should be good enough to for chapter 6. 6.8k words, a bit over 15 pages.

I think this is good for a day's work.

I think I'll stop here for now. I'll leave proofing and publishing it for tomorrow. I do not feel like going through the errors in Docs right now.

5:45pm. If I want to hunt for my answer of how I should live, 300 pages are needed. That should be enough for other people to properly judge me. I'll see whether that will be possible by the end of next month. 190 pages spready across 30 days. I am not sure if I will be able to do it, but I should be able to write 100 at least. Slow and steady wins the race and all that, I won't pressure myself.

After I hit 300, maybe I'll post the story in one of the /lit/ threads. And maybe on the Singularity reddit like in the old times.

6pm. Let me close here. This feeling of insecurity will remain in me until I either get some supporters or I finish Heaven's Key without success. I need to keep pushing forward until I get my answer."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[53721c9134...](https://github.com/treckstar/yolo-octo-hipster/commit/53721c9134f85f9911ee43278e2124d8a69456f5)
#### Thursday 2022-08-25 17:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [facebook/react](https://github.com/facebook/react)@[b6978bc38f...](https://github.com/facebook/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2022-08-25 18:12:21 by Andrew Clark

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
## [ashley-cui/podman](https://github.com/ashley-cui/podman)@[09ef6fc66c...](https://github.com/ashley-cui/podman/commit/09ef6fc66cac44dec94c29cd7a1a53f70831446d)
#### Thursday 2022-08-25 18:23:26 by Ed Santiago

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
## [danhhz/materialize](https://github.com/danhhz/materialize)@[90203cc21b...](https://github.com/danhhz/materialize/commit/90203cc21ba2689ff9f1ec850c920fb70ba41b53)
#### Thursday 2022-08-25 18:36:25 by Daniel Harrison

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
## [lawrindovsk/Pok-Lax](https://github.com/lawrindovsk/Pok-Lax)@[52df9c2711...](https://github.com/lawrindovsk/Pok-Lax/commit/52df9c2711afd33b69951ef0ff844f226afb480f)
#### Thursday 2022-08-25 19:02:46 by Gustavo Laurindo dos Santos

Update 1.0

Good morning Good afternoon Good night.

Welcome to PokeLax

The idea is to create a website with information about the franchise we love, Pokémon! , on the site you will have the classic pokédex, pokémon information such as attacks, nature, origin and even competitive.

Update 1.0 - Description:

In the alpha version we had a .png of a pokédex , however, I took it out so that it can work on an "authentic" pokédex , we also added a .js file, to work using the PokéAPI , we refactored the index and created sobre.html (which will be updated later).

---
## [Dimasw99/sojourn-station](https://github.com/Dimasw99/sojourn-station)@[f5da3823ac...](https://github.com/Dimasw99/sojourn-station/commit/f5da3823ac07f22c72a19e8191a4567882020f7f)
#### Thursday 2022-08-25 19:28:19 by nikothedude

holy SHIT i hate saycode (hotfix) (#3816)

* whydidthishappen

* fuck

---
## [Dimasw99/sojourn-station](https://github.com/Dimasw99/sojourn-station)@[c3c08d0946...](https://github.com/Dimasw99/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Thursday 2022-08-25 19:28:19 by nikothedude

Ports moveSS from TG (#3771)

* p

* fucker

* fuckin

* fuckin!!!!

* commit time

* hell yeah

* FUCKING. TG

* groan

* fuvkin

---
## [Holeryn/Mic_Spectrum_analysis](https://github.com/Holeryn/Mic_Spectrum_analysis)@[8877768fe1...](https://github.com/Holeryn/Mic_Spectrum_analysis/commit/8877768fe17100183a15fa831de0ff2f97a88bdb)
#### Thursday 2022-08-25 20:08:32 by Holeryn

Add files via upload

Fuck you!, Fuck you!, Fuck you!

---
## [robertmarsal/gqlgen](https://github.com/robertmarsal/gqlgen)@[43b56cbaf3...](https://github.com/robertmarsal/gqlgen/commit/43b56cbaf3f1de1d1ad379055ab1de157592cf38)
#### Thursday 2022-08-25 20:55:42 by Ben Kraft

Forward `go mod tidy` stdout/stderr

This is a command that can fail (in my case I think for stupid reasons
in a hell of my own construction, but nonetheless).  Right now we just
get
```
$ go run github.com/Khan/webapp/dev/cmd/gqlgen
tidy failed: go mod tidy failed: exit status 1
exit status 3
```
which is not the most informative.  Now, instead, we'll forward its
output to our own stdout/stderr rather than devnull.

---
## [lm40/VOREStation](https://github.com/lm40/VOREStation)@[4c0245a1b0...](https://github.com/lm40/VOREStation/commit/4c0245a1b03250deaf58072545aec079b0722e96)
#### Thursday 2022-08-25 21:22:18 by C.L

Adds Toxins & Cloneloss digestion damage.

- Adds Toxins as a digestion damage type.
- Adds Clone damage as a digestion damage type.

- Cloneloss gives 2x nutrition than brute/burn since it is exceptionally harder to heal from. (not that it matters)

So now slime characters can actually RP out sucking out your DNA and leaving you a DNAless husk while slamming you with toxins like xenobio slimes can.

---
## [garglk/garglk](https://github.com/garglk/garglk)@[dd59906d33...](https://github.com/garglk/garglk/commit/dd59906d33d36a41bfac288096cb48723691b7bb)
#### Thursday 2022-08-25 21:26:46 by Chris Spiegel

Check more than style_Preformatted for monospace

The Agility interpreter uses styles User1 and User2 for monospace, but
Gargoyle only considered style_Preformatted, meaning that Gargoyle
assumed user styles were _not_ monospace, and translated hyphens into
em- and en-dashes.

Since Gargoyle knows which font type a style maps to, use that
information instead of checking the style directly. This will work if
interpreters use User styles, or if they change the appearance of other
styles via hints.

As noted in the comment, this assumes the user has properly set a
monospace font. If a proportional font is set as the monospace font,
Gargoyle will still assume it's monospace, because it's "supposed" to
be. This is at odds with how ligatures are done: there, the font file
itself is examined and if it's monospace, ligatures are disabled.

I think these differing approaches make sense: Here, with dashes, if a
user sets a proportional font as the monospace font, it hardly matters
whether the hyphens become em- and en-dashes, given that the width of
the glyphs is variable anyway (i.e. box drawing is hopelessly broken if
you set a proportional font, so changing hyphens is a drop in the
bucket). And if a monospace font is set as the proportional font, yes,
it'll get em- and en-dashes, but that's fine, since the width of the
characters, at that point, can't be expected to be fixed, given that it
_could_ be a proportional font. It will be a slightly degraded
experience since it won't be obvious it's a longer dash, but then, if
you're setting a monospace font everywhere, you can turn off dash
conversions.

As for ligatures, if the user sets a monospace font for the proportional
font (which is perfectly fine), the ligatures would look pretty silly,
especially the three-character ones. For example:

    Oﬀice
    Ofﬁce
    Oﬃce
    Ofﬂine
    Oﬄine

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[e6bf3025d8...](https://github.com/pytorch/pytorch/commit/e6bf3025d87a55a95885d8dee41e90b2fb356bb5)
#### Thursday 2022-08-25 21:42:07 by Andrew Gu

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
## [shaneutt/darkplaces](https://github.com/shaneutt/darkplaces)@[91342dd0a8...](https://github.com/shaneutt/darkplaces/commit/91342dd0a88d002a188418a4b0dd21957e0737b6)
#### Thursday 2022-08-25 21:48:10 by Cloudwalk

 README: Remove Discord invite link. The Discord server is now deprecated

I'm unable to sustain the DarkPlaces engine community on Discord. They have
falsely disabled my main account and now my second account, this time
without an email explaining the reason. I have a 3rd account that is still
active. They have not responded to my emails asking for them to review
the ban of my main account and they have the gall to nuke my second
account as well.

They are flooded with support tickets likely because it is incredibly easier
to hijack a Discord account than any other account due to the simple fact
that Discord does NOT require email verification to change passwords. God
only knows what other horrors lie beneath that Eldritch abomination of
duct-taped JavaScript.

I was not banned from Discord as I was able to create the third account using
the same IP address. They ban IPs if you're banned from Discord. I can no
longer, in good conscience, give this shit, incompetent, bullshit company
a single neuron of mindshare going forward. Other arrangements for a community
hangout are to be determined but are not available at this time. The IRC,
obviously, remains available.

Until they get their shit together (if they do), FUCK Discord and FUCK
everything they stand for.

Signed-off-by: Cloudwalk <cloudwalk@icculus.org>

---
## [queercpu/script](https://github.com/queercpu/script)@[ae0a222dfa...](https://github.com/queercpu/script/commit/ae0a222dfa4c9fac7f0588824efc3d7fe7dab5a4)
#### Thursday 2022-08-25 23:04:08 by home.cpu

worked on some gui, jacked some code from internet to get some rough sketchy musicrooms/gallery/glossary etc semi working, not done at all, the codes themselves need working. I can prob learn myself but it would be really useful to work with someone who can do renpy work to execute these sort of renpy /menu gui dramas... i have very clear ideas and want to impliment.  another thing id like is to show a bookmark whenever quicksaved, or saved from menu... that is an overlay, the red bookmark, then dissolves out.  i painted it and added but didnt write any code for it.  added scriptures A B C from prototype to script folder.  wrote some shit about bible tutor i think in the ep3 folders.

---
## [obamasolutions/obama.solutions](https://github.com/obamasolutions/obama.solutions)@[d6750ddb2a...](https://github.com/obamasolutions/obama.solutions/commit/d6750ddb2a942c4e52a757901c02485a445253d1)
#### Thursday 2022-08-25 23:54:20 by Tucker Carlson

fuck you zuck
also our apache config doesn't seem to support the features of my htaccess rn :(

---

