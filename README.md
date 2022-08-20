## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-19](docs/good-messages/2022/2022-08-19.md)


1,899,082 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,899,082 were push events containing 2,900,821 commit messages that amount to 211,675,468 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[a7a0e33192...](https://github.com/Koshenko/mojave-sun-13/commit/a7a0e33192ad3fcac5ad64d441f24af6ec852054)
#### Friday 2022-08-19 01:06:12 by Hekzder

Mob overhaul for DT (#2117)

* Basic mobs

Title

* Start of simple robots

Title

* THE GREAT MOB SOUNDENING

TITLE

* Handies + ranged attack buffs

FASTER!!

* Protectrons, robobrains

* Death sounds and fixes some dumb shit

Title

* NEW ROACHES OMG!!!

WOW!

* Robo sounds

Title

* Mob projectile tweaks

I THINK WE'RE GOOD

* bitty

---
## [010blckswan420/reposteal](https://github.com/010blckswan420/reposteal)@[6e8f639303...](https://github.com/010blckswan420/reposteal/commit/6e8f63930366404f08805cc54c85c4c9d37eafd7)
#### Friday 2022-08-19 02:09:42 by theblckswan

sudo su && fuck you
Please enter the commit message for your changes. Lines starting
with '#' will be ignored, and an empty message aborts the commit.
On branch master
Your branch is up to date with 'slave/master'.
Changes to be committed:
	modified:   README.md

---
## [jiangxin/git](https://github.com/jiangxin/git)@[5beca49a0b...](https://github.com/jiangxin/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Friday 2022-08-19 02:37:07 by Ævar Arnfjörð Bjarmason

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[26a7d58281...](https://github.com/treckstar/yolo-octo-hipster/commit/26a7d58281d2f1e6df30c055bb41eba30a00b6da)
#### Friday 2022-08-19 03:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ht-vo/podman](https://github.com/ht-vo/podman)@[09ef6fc66c...](https://github.com/ht-vo/podman/commit/09ef6fc66cac44dec94c29cd7a1a53f70831446d)
#### Friday 2022-08-19 05:12:40 by Ed Santiago

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
## [rakheshjaghadish/Genocide-and-Crimes-Against-Humanity](https://github.com/rakheshjaghadish/Genocide-and-Crimes-Against-Humanity)@[e2e1e4a5ff...](https://github.com/rakheshjaghadish/Genocide-and-Crimes-Against-Humanity/commit/e2e1e4a5ff9c4813fa9e5060476fbbbbbde905e9)
#### Friday 2022-08-19 08:32:53 by rakheshjaghadish

Open Statement, Rakhesh Jaghadish L 19 8 2022


Open Statement, Rakhesh Jaghadish L, Public, Human Being

Generally, I don't hurt anyone with any intention. After my email on 16th January last, I am being deliberately harassed by powerful corrupt politicians in a psychological way. I was continuously monitored by them on Twitter for the past few months. The same day I sent the email, someone contacted my parents by phone. He asked, “is your son a doctor”. Then days passed and PM Modi spoke to the media after the email I sent him saying "somebody tried to tarnish India's image". Then on February 6th, 2022 my Novecore Music account was hacked. That is 19 days before the outbreak of war between Russia and Ukraine. That is 13 days before the Munich Security Conference. I received a new data breach notification on 6th Feb 2022. Then the planned war between Russia and Ukraine began on February 24. My tweets through Twitter changed the course of the planned war. Then on March 9th, I made a request via Twitter to Elon Musk to create an open source social networking medium like Twitter. I never imagined that he would announce the acquisition of Twitter on April 25th. Then days went by and every time I whistled in front of my house, my street only got blackout. I know who they are. But I remained silent. I also found myself being followed whenever I go out or go to college. I also found they hacking my device through my mobile using a mobile service van and I allowed it for analysis. I know it's illegal spying. 

My Accuse that they using my Aadhaar Digital ID in the wrong ways. This means they leaked my Phone Number to the RSS BJP Mobs. After they Leaked I Got Messages from the Foreign States (Philippines) and the Bihar Like States. Not only My Digital ID, those who all are against them and their Genocide.
There is no Safety and Privacy when it’s come to Digital ID.

They also cut off the electricity in my college exam room when I was going to take the exam. It seems that they think that their actions make to scare me. Every time I tweet against Genocide, every time I tag Elon Musk on Twitter, every time I tweet against vaccination, my street and house are cut off. Every time I tag International Criminal Court on Twitter my street and house have been cut off and continue to be cut off.

I usually don't go to any fuss. I am generally quiet. I can communicate internationally. I'm not who you think I am.
Human rights are equal for all. Whenever human rights are violated, humanity is depleted. Inhumane politicians continue to divide people in the name of religion and caste and incite hatred among people.

The government is run by the public people. People elect a person as a representative of the country through elections to protect the country and its people. But for the last 40 years, they have been doing nothing but corruption without doing any work to protect the people.
Persons elected by the people abandon the people and corrupt politicians collude with pharmaceutical companies to spread diseases, sell drugs and kill the public for greed profits.
Now, in the name of the coronavirus pandemic, Corrupt Politicians lured by greed money and power are now committing genocide against the World Peoples.
And also, they label Truth, Truthful Information, and The Real Pain of the Public Peoples as misinformation. That's what the unscientific media does. 
Without any scientific evidence, psychological warfare is being waged on a global scale by globalists using the Lockdown and the planned pandemic.
In the name of the pandemic, the personal agenda of globalists is being enforced by force and imposed on the general public.
In the name of Lockdown two innocent men named Jayaraj-Fenix from Tamil Nadu were Arrested for violating lockdown norms over the business hours of their shop. They were taken to the police station by police officers who are the slave of corrupt politicians. Brutally vandalized, dresses were removed and cops inserted metal objects into one of the arrested men's rectum and beaten to death and the police staged a drama to cover up the murder.
Who empowered the police officers to torture those or prisoners who are being taken for questioning, stripped naked, and tortured?
Clothing is a shield that gives dignity, a fortress, and protection. Stripping those brought in for interrogation is an act of inhumanity beyond measure. Whether those who are taken for trial or accused are guilty is decided in a court of law.

A police officer has the same dignity and human rights as the unaccused and the accused have the same dignity and human rights.
Human rights are natural in this world. It needs to be taught to present generations to create better future generations.
Government employees owe a debt of gratitude to the people as their salaries are paid out of people's tax money.
People do not need to be loyal to politicians or governments.

Politicians and governments must be loyal to the people.

Corrupt Politicians and Governments Rs. 2,063 Crore worth of statues of dead corrupt politicians. What did they do to the people? 
Instead of wasting that 2,063 Crore rupees on an idol, that money could have been spent on people who are suffering without medical help and without food.

There is more to say. - + No more to say.

Freedom is Equal for Everyone.

---
## [MemeHoovy/PE-tutorials](https://github.com/MemeHoovy/PE-tutorials)@[20f8d5167c...](https://github.com/MemeHoovy/PE-tutorials/commit/20f8d5167cb23910fd9fd5d6b0c491d78064345d)
#### Friday 2022-08-19 09:25:59 by Not_HaydenGaming

CUSTOM CUM TRANSITION 100% REAL

got that done in 15 minutes, cuz fuck you dave's revenge 3.5

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[277b3429f5...](https://github.com/Offroaders123/NBT-Parser/commit/277b3429f55faf0775bace3ecbacef18a2a09d5d)
#### Friday 2022-08-19 10:02:11 by Offroaders123

Tag Byte Type + Type Naming + GetTagByte

Lots of cool stuff! This is edging a bit closer to being API-like now :)

I keep reminding myself that I haven't even touched the writing half yet though, haha! These classes will makes things a lot easier though, the object structure actually feel like something maybe trustworthy at this point.

I can't wait to make something with this! I'm definitely going to add NBT editing as plain text to STE, that was one of my original use case ideas for this project. That also led me to work on NumText a bit some more a while back. Those changes haven't made it into stable yet, but a lot of my projects have moved forward, especially thanks to the more recent things I've looked into.

The biggest things in my JS dev world at the moment:
Web Components, ES6 Classes, ES Modules, Node (yes, I finally am getting used to that, haha), Promises / Async - Await, Compression Streams, TypedArrays (byte streams as a whole), Endianness (DEFINITELY deserves it's own category), and very recently, TypeScript! (.d.ts, and now full .ts)

These have been huge steps forward for me, and I really see how far it is pushing me forward from my projects just a short time ago. I look back at my practices before, and so many things have added together to make a big giant upgrade for my personal experience. I really like what can be done with all of these, and with how great learning these have been, I can't wait to eventually come back around to look at things like WebRTC. When I first looked into it, it was a bit over my head I think, and now that I understand the language structure a bit further, I have a bigger step up to wrap my head around it.

This library as a whole has been a great project for me, and it pretty much added a majority of those things I just listed to my experience catalog.

Well, thanks for vising my "blog", hope you like the writing XD

*Note: I also want to look into making my own page for my profile as an artist too, so like a landing page for album showcases and things like that. I have a lot of fun making artwork for my songs, and having an awesomely-styled website to go along with them sounds super cool to work on. Expect that eventually down the road too! Maybe Markdown would work best there :)

---
## [FranzBusch/swift-protobuf](https://github.com/FranzBusch/swift-protobuf)@[e47f7304c9...](https://github.com/FranzBusch/swift-protobuf/commit/e47f7304c909f2849648c790233cd4894a5477c5)
#### Friday 2022-08-19 10:33:55 by FranzBusch

Add SPM plugin

# Motivation
SPM is providing new capabilities for tools to expose themselves as plugins which allows them to generate build commands. This allows us to create a plugin for `SwiftProtobuf` which invokes the `protoc` compiler and generates the Swift code. Creating such a plugin is greatly wanted since it improves the usage of the `protoc-gen-swift` plugin dramatically. Fixes https://github.com/apple/swift-protobuf/issues/1207

# Modification
This PR adds a new SPM plugin which generates build commands for generating Swift files from proto files. Since users of the plugin might have complex setups, I introduced a new `swift-protobuf-config.json` file that adopters have to put into the root of their target which wants to use the new plugin. The format of this configuration file is quite simple:

```json
{
    "invocations": [
        {
            "protoFiles": [
                "Foo.proto"
            ],
            "visibility": "internal"
        }
    ]
}

```

It allows you to configure multiple invocations to the `protoc` compiler. For each invocation you have to pass the relative path from the target source to the proto file. Additionally, you have to decide which visibility the generated symbols should have. In my opinion, this configuration files gives us the most flexibility and more complex setups to be covered as well.

# Open topics

## Hosting of the protoc binary
Hosting of the protoc binary is the last open thing to figure out before we can release a plugin for `SwiftProtobuf`. From my point of view, there are three possible routes we can take:

1. Include the `artifactbundle` inside the `SwiftProtobuf` repository
2. Include the `artifactebundle` as an artifact on the GH releases in the protobuf repo
3. Extend the the artifact bundle manifest to allow inclusion of URLs. This would require a Swift evolution pitch most likely.

However, with all three of the above we would still need to release a new version of `SwiftProtobuf` with every new release of `protoc`.

# Future work

## Proto dependencies between modules
With the current shape of the PR one can already use dependencies between proto files inside a single target. However, it might be desirable to be able to build dependency chains of Swift targets where each target includes proto files which depend on protoc files from the dependencies of the Swift target. I punted this from the initial plugin because this requires a bit more work and thinking. Firstly, how would you even spell such an import? Secondly, the current way of doing `ProtoPathModuleMapping` files is not super ideal for this approach. It might make sense to introduce a proto option to set the Swift module name inside the proto files already.

# Result
We now have a SPM plugin that can generate Swift code from proto files. To use it, it provides a configuration file format to declare different invocations to the `protoc` compiler.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0bdc5d4204...](https://github.com/mrakgr/The-Spiral-Language/commit/0bdc5d4204c2cbc497928a50dc3f9058cd0398f3)
#### Friday 2022-08-19 10:59:32 by Marko Grdinić

"9:40am. I am up. I actually went to bed earlier than usual yesterday as I was so tired. I slept well. Let me chill a bit and then I will get started. I need to deal with my Patreon account. After that I'll proofread chapter 3 and post it.

10:20am. Ok, it is time to get started. I need to set up the Patreon.

https://www.patreon.com/Zogarth

On /wg/ somebody linked to this guy yesterday. He is literally making 28.5k/month off his Patreon. Indeed, having some chapters free on RR, and letting the Patreon subscribers have some in advance is a good business model.

10:25am. Er, before that, let me just take care of a medical need. A few days ago I stupidly scrapped the back of my heel and now is the time to remove the band-aid.

...Well, it looks horrid, but it is fine. The band-aid was not set that well, it was half covering the untouched part. The other part was exposed when I removed the band. It is fine.

At the very least, today I will finally be able to take a bath now that the wound has solidified. Enough about that.

Patreon.

10:45am. There are a bunch of links on the sidebar, so let me take a look at them.

10:50am. Nevermind those cookie cutter links. All I need to do is write one, leave one for the patrons, and I will get there.

Now I have two things to take care of. Profile photo and cover photo. What is the cover photo for? I can guess what the profile photo is, but the cover?

10:55am. I googled cover photo and I see it. I guess I could use the floating city illustration for the cover photo.

Now, I need a profile photo. I actually do not really want to use my own photo. I am thinking of doing a ghost. I could fire up Blender and use the cloth sim. Alternatively, I could take my AngelList photo and put it through style transfer.

...Let me go with the later.

https://www.patreon.com/Zogarth

No actually, take a look at this guy's page. I think that circle in the middle is the profile photo and the big thing at the top is the cover photo. Let me go with the ghost plan. I have a ghost as my avatar for the wordpress blog, but that is something I got off the net. I should make my own.

Let me fire up Blender. It should not take me too long to do this.

11:05am. Got the sphere, got the plane, let me run a cloth sim.

11:10am. What a pain in the ass, Blender crashed. During times like these I really wish I could draw. But no, I have to run a cloth sim! Maybe I try sculpting it.

11:20am. Now texture painting. Let me make the eyes and the mouth.

Hmmm, what the hell, where are my gloves? Hiding in plain sight I see.

11:25am. Ok, now. At this point I've forgotten some of how to use Blender. How do I activate the texture to paint on.

Things like these are why it takes forever for me to do anything.

https://blender.stackexchange.com/questions/29256/how-to-flood-fill-a-color-in-texture-paint

> You can use the recently added Fill brush:

11:45am. Damn it, how do I make the stroke go through. Blender is so shitty at this. There is an option for occlusion as well as that other thing.

11:50am. I am really regretting trying to do texture painting in Blender at this point. I am trying to smooth some colors and it has gone into an infinite loop it seems.

...Ah, for fuck's sake, I need to abort it. How much have I lost?

12:20pm. Ok, let me go with this. For something so simple, it sure took me a while. But that is the usual for me. The quality is not high, but the effort it takes to make is.

But still, being able to do at least this much is better than not being able to do anything at all. I have the option of doing at least an amateur cover.

12:25pm. I guess that takes care of the profile and the cover. But the cover is too tall. It should be something like 4 x 1, while mine is 3 x 2. I might have to cut some parts. But I do not see a preview, so I can't be sure how it looks just yet.

12:30pm. Let me just go through the checklist.

12:35pm. Hmmm, it seems it should be possible to post directly on Patreon.

12:40pm. Wait, why did Patreon eat what I wrote in the About page. What the hell?

Anyway, even though it is cut off, the image is not necessarily shrunk so it does not look too bad.

Let me write it here this time.

///

Hello, I am Ghostlike.

This is the Patreon for Simulacrum: Heaven's Key, hosted on Royal Road. More to be announced soon. Any support is highly appreciated and will allow me to keep updating the story.

Link: https://www.royalroad.com/fiction/57747/simulacrum-heavens-key

///

Can I make a lower tier. 10$/month is too much to start things off.

12:45pm. I am confused, how do I make a separate tier?

Nevermind it for now.

...Let me just launch the page and I will go have breakfast.

12:55pm. https://www.patreon.com/mrakgr

Ok, here it is. I haven't realized up to now that I really should be making my posts on Patreon. Maybe I'll move this journal there as well. I can offer the regular story for 3 and 5 just like the Zog guy, but let everything be accessible for 10/month along with this journal.

1pm. Let me stop here so I can have breakfast. I'll think of what comes next after that."

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[4e3aa92382...](https://github.com/ammarfaizi2/linux-block/commit/4e3aa9238277597c6c7624f302d81a7b568b6f2d)
#### Friday 2022-08-19 11:41:55 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[8c63096c01...](https://github.com/majestrate/loki-network/commit/8c63096c01d4ab41b053e65e85b99cfc5372b78e)
#### Friday 2022-08-19 12:54:34 by Jeff

by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea

---
## [ollieread/php-src](https://github.com/ollieread/php-src)@[128768a450...](https://github.com/ollieread/php-src/commit/128768a4503c8bc5c6ccf564061f9dc8b307f57f)
#### Friday 2022-08-19 14:07:05 by Alex Dowad

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[89b5745d36...](https://github.com/pytorch/pytorch/commit/89b5745d36310e279dd977f265e5ae14b14e8b7f)
#### Friday 2022-08-19 14:29:41 by Andrew Gu

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
## [kamaboko117/ft_containers](https://github.com/kamaboko117/ft_containers)@[3e5a7b9c2b...](https://github.com/kamaboko117/ft_containers/commit/3e5a7b9c2bca942787d90ea018eae5a9338d1f11)
#### Friday 2022-08-19 15:44:19 by Alexander SABOURET

fuck this shit this is fkn cringe i hate this fuck commit messages fuck this project

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3a972201cb...](https://github.com/mrakgr/The-Spiral-Language/commit/3a972201cb927f48716a4d7e61bed54be2b8da0c)
#### Friday 2022-08-19 15:50:02 by Marko Grdinić

"1:35pm. After I am done with breakfast, I'll take a bath. I am overdue on that and I can't work in this filth. Afterwards...Yeah, I'll post the next chapter on RR. Actually, before that I have to figure out how to make the tiers. The 3E one will just be for sneak peeks. Initially I'll only have the 5 and 10E ones. 5 for all the chapters, and 10 for that plus this journal.

After that I'll go into the grove of writing two chapters and posting one on RR.

2:15pm. Done with breakfast. Let me watch ep 2 of Kunoichi Tsubaki and then I am going to start. I need to figure out how to get a handle on the monthly tiers.  Actually before I start, I need to take that bath. Sigh. Well, after I deal with today I'll be able to just get back to the writing groove.

2:45pm. It is a fun anime. Bath time. I've been looking forward to this.

3:25pm. Phew, I got that shave. Nice, I am set once again.

Ok, let me check out my Patreon page. Can I add a 5E tier?

Yeah, I just have to click the Edit Tiers button.

Right now I have the 5E/month Aleator and 10E/month Episteme tiers. I'll add the Introspect 3E/month tier later.

3:30pm. Now it is time to publish another chapter. I also want to go over the first one for any errors.

Before that, are the new 40xx cards out. I want to check out their power consumption.

https://www.gpumag.com/nvidia-geforce-rtx-4000-series/

No, not really. I won't bother reading this.

https://semianalysis.substack.com/p/intel-cuts-fab-buildout-by-4b-to
> First Net Loss In Over 30 Years, Cutting Fab Buildouts, But “Committed To Growing The Dividend”

I've been thinking about this yesterday, but I think Intel deserves some kind of disapointment of the decade award. Intel had everything going for it to lead the way to a multicore revolution. Had it done so, we could have had 1,000 core chips today instead of waiting for AI startups to get to them. If the Singularity misses its 2045 target, it is Intel, not memristors, to whom the blame should be pointed at.

https://semianalysis.substack.com/p/cxl-deep-dive-future-of-composable

Right now I am reading this. Let me finish it and then I will publish the story.

> Datacenters have a massive memory problem. Core counts have grown rapidly since 2012, but the memory bandwidth per core and capacity has not increased commensurately.

3:50pm. Ok, let me go over chapter 1. Then I'll go over chapter 3.

> simulacrum_post_singularity_story

Let me see if I can change the page name to this.

https://www.patreon.com/simulacrum_post_singularity_story

It works.

3:55pm. Hmmm, let me go with that as my patreon page. It is long, but rememberable.

https://boards.4chan.org/h/thread/6801965
AI generated hentai

Not too bad. A post says they will release Stable Diffusion on Monday.

Let me get back to chapter 1.

4:15pm. I am not really focusing on it too intently, but chapter 1 seems fine.

4:35pm. I didn't find a single line to edit in chapter 3. I guess it is fine.

Ah, before that, let me edit the chapter numbers. How do other people label them?

Something like 'Chapter 1: The First Dream' and so on is fine.

4:50pm. Let me write the post-chapter autor note.

///

8/19/2022

Patreon: https://www.patreon.com/simulacrum_post_singularity_story

No benefits yet, but I'd appreciate any support you could give. The plan right now is to just write a lot to prove my willingness to do this, and once I have sufficient volume out, I'll start leaving some aside for Patrons.

All the arcs of Simulacrum are less stories for me and more like my aspiration, both to enter the self improvement loop and what the world I would create would be like. I am actually quite embarrassed that I've turned to writing instead of pursuing the Singularity through my programming, but the path of transcendence is a very hard slog in today's world. I'd end up homeless on the street if I pursued it any harder. The defining feature of any path is that it gives you a way of starting off and then gradually multiplying your advantage. It is how investors compound their investments over time, or salarymen get promotions at their company. The way I've imagined the path of transcendence in this age would go is that I'd make a weak AI agent, and the use of it would give me the resources that I'd need to make better agents, but even something like making an agent for a toy game like poker is quite hard. I mean, it is not that trivial - from a certain perspective Go is also trivial, but AlphaGo needed a cluster to be trained on, and poker is more complex than it. Still, I had a certain vision and a belief in how things should go so I pursued it. The AI agent should have given me resources, and on my own end, I had created a programming language that would make it easy to program the AI chips. Spiral is quite a good functional programming language, you can get it as a VS Code extension if you are interested. I am proud of it. Where I fell short is the making of an AI agent. Since they had the greatest potential, I made the mistake of focusing on NNs and deep RL.

I couldn't really avoid making such a mistake as I thought a language that can be used to easily make ML libraries on AI chips would be necessary, so I had to focus on that. But given how poor deep RL methods are, even making a weak poker agent turns out to be too hard on a single GPU. There is an alternative and more natural path to AI, where you start off with handwritten rules - the good, old-fashioned AI, then bring in evolutionary methods to optimize whatever handwritten rules you have. That would bring you to the weak level without much issue. After that it would be possible to bring in NNs on top of evolutionary methods. This would be a much stabler path of development and it is a pity I haven't taken it.

It would not be that easy to bring in NNs into the mix with today's hardware though. GPUs really shine when you have static datasets, but when you have simulators or games, and want to pass the inputs as they come, that is without batching, you run into huge efficiency issues. If I could get access to AI chips, I could resolve that. Since I have good PL skills owing to me working for 3 years on my own language, I really should be making all kinds of tooling for AI chips, but it is hard to get in touch with these companies or get access to their chips.

///

5:35pm. I am going to close here for the day. I'll leave proofing the chapter 4, and writing the note for it for tomorrow.

I want to officially give Intel the disappointment of the decade award.

5:40pm. Oh right, let me add an image to the album.

Simulacrum: Heaven's Key Illustrations: https://imgur.com/a/blBYUA2

I'll use it as a VN scene at some point. I've already posted it in plenty of styles on my Twitter.

Ah, right, let me post a link to Heaven's Key on my Tweeter.

https://twitter.com/Ghostlike

Done.

5:45pm. Yeah, this is good enough. I'll really close for the day here. Tomorrow I'll post chapter 4, and then get to work on adding more to chapter 5.

Time for lunch."

---
## [rive-app/rive-android](https://github.com/rive-app/rive-android)@[d20b028df1...](https://github.com/rive-app/rive-android/commit/d20b028df14fc71fc92c0b5e878e1185dfa56e5a)
#### Friday 2022-08-19 16:29:34 by mjtalbot

Fix a problem where we access deleted artboards and state machines

This fixes an issue around accessing data that has been deallocated.
https://2dimensions.slack.com/archives/CLLCU09T6/p1660763844645649

 Specifically, previous to this, running reset twice in a row, would crash the app, as we try to get a name of a deleted artboard instance.

Also moving artboards life cycle into the "dispose" path, as before, changing the selected artboard would dispose the old artboard (which trickles down to all the stateMachineInstances etc). Now, this will only get cleaned up once the renderer is disposed.

This is an attempt to address an issue you can run into when holding references to stateMachineInstances, in the instance where this is helpful, the stateMachine instance is simply used to grab the names of its inputs, so a ui could change the state machines input.

I *think* changing this lifecycle makes sense still, but of course this could start to have some unintended consequences, as the artboard instance referred to by the statemachine instance is no longer playing.

But in this case those old state machine instances were used to get "generic" information about the contents of the Rive object, not as concrete references to "state machine instances". I think this problem is a side effect of removing the non instanced version of artboards/state machines/animations as users now have no choice but to grab this information from instances.

perhaps a generic "hey whats in my rive file" function that offers a simple reference structure users can use will help with this though

wanna hear peoples thoughts.

- [ ] add a test to show the crash on double `reset()`

Diffs=
9036f5031 Fix a problem where we access deleted artboards and state machines

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[ae4bb92115...](https://github.com/payday-restoration/restoration-mod/commit/ae4bb921158dccebf8e60b7851a41b51a2bd736d)
#### Friday 2022-08-19 18:25:16 by Noep

stuff

- Lowered the deflection cap from 95% to 60%
-- You could never actually reach that level of deflection after Frenzy's nerf from 30/60% to 20/50%
-- Realistically speaking, this only slightly reduces effectiveness as getting to 60% deflection even before this change, assuming you have 30% from FJ + Die Hard, meant you'd have to be at 30% HP to get 60% deflection

- Oni Irezumi (Yakuza) raises the deflection cap by 20%, to a maximum of 80%
-- Again, assuming you have the 30% from FJ + Die Hard, you'd actually be downed at the point you'd get 80% deflection
--- You'll be tanky as fuck while downed tho :^)

---
## [coordinape/coordinape](https://github.com/coordinape/coordinape)@[2a76043a17...](https://github.com/coordinape/coordinape/commit/2a76043a17dd06ac4e47e8d2434b5ef9113fe19c)
#### Friday 2022-08-19 18:30:12 by topocount

bugfix: enable FormTokenField to have an empty input (#1277)

One of the major considerations during the FormTokenField (and downstream) refactor was allowing for empty string inputs. This enables for much cleaner UX, since users aren't typing "around" a zero
and in my opinion, makes us look like we know what we're doing as devs. There are other hacks that could make the UX better than the incumbent, but why not just make it behave correctly and be done with it?

Co-authored-by: crabsinger <83605543+crabsinger@users.noreply.github.com>
Co-authored-by: zashton <17747090+zashton@users.noreply.github.com>

---
## [delphix/linux-kernel-oracle](https://github.com/delphix/linux-kernel-oracle)@[9997f61537...](https://github.com/delphix/linux-kernel-oracle/commit/9997f615374a116e05bbad5b2fef49a28e6afdf0)
#### Friday 2022-08-19 19:19:10 by Linus Torvalds

gpiolib: acpi: use correct format characters

BugLink: https://bugs.launchpad.net/bugs/1973085

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kamal Mostafa <kamal@canonical.com>
Signed-off-by: Kleber Sacilotto de Souza <kleber.souza@canonical.com>

---
## [acramernc/babot](https://github.com/acramernc/babot)@[9026036e28...](https://github.com/acramernc/babot/commit/9026036e28192bd0653f0bb0eced4773dc841744)
#### Friday 2022-08-19 19:40:15 by KittenMoon

well well well, you have caught me here again and it is a day of typing to do again. it is 4 am so this start section will not be as long as the previous one but i feel i may be able to get this git commit message to be longer than the last one, if you are reading this then i am proud of you. So tomorrow in the am or sometime tomorrow i will do an in depth explination of either SAO or AoT, the one that will ge tthe explination is deterministic on wheather or not i finish AoT final season part 2 sub seciton a class I episode 13. Yes i did over exagerate the naming of the season but that is only because it is the "final season" which has been split into three parts, one in 2021, anotehr in 2022 and the last int 2023. so that is that but when i finish it then i will continue onto the next show which is something that i cant remember at the moment but if i look it up then i would be able to figure it out. SO when i watch my epsiodes, i do not skip through it like some "unnamed" person who i will not call out at all, defininately not some eye boy with a sack at all. ANyway i do have to infrom you that i iwll be in boone this weekend so there is a highter chance i will see hey buddy but that is like me saying there the chance goes from .1% to 1%, basically nothing but not 0 so whose to say, dont you hate it when your headphones just die when the good song is playing, silly headphoenes please dont do that. Well back to what i was saying with how i will be watching some shows this summer and after AoT it will be the fate movies which knowing me will likely get post poned as i will be in boone and when there i will want to watch something shortish on the laptop. I will use the boone pokemon weekend as an excuse to just watch things on my laptop as i will be in boone w/o the desktop :(. ඞ surprise mogus. be warned they can occur anytime. ok as i was saying there will be a time an place for the summer shows and as it is june first i normally wouldve watched my one movie today but i forgot and plus i will save it for a day i am not busy withh stufff which today was. alas i will have to make sure that i can do as well as summer shows 2020 in terms of amount watched which was 16 to 17 depending on how you count it with seasons of shows and movies and finishing one right as classes started (the weekend after). but that was still in technical summer. if i can do the 14 on my list i should be on par as some of the 14 are actually multiple seasons grouped together which would make the number go up higher and there is a set of 3 movies and in the 2020 group there were 2 movies counted in that. Another thing is that the start of SS 2020 was around now (june 1) and i started around now technically but there was some earlier just like there was some earlier in 2020 (soul eater, which isaac still hasnt finished). the time may be almost 5 am (4:54 to be exact) so i should be calling it for this part of the commit for today, but this commit will not be done until i finish 3 of my shows on the list (excluding fate movies), or in a week, whichever comes sooner as it could take a bit to watch all the shows as i get distracted or it could be soon as isaac is done watching SAO which means i will not have anything to distract me, unless i watch SAO, which if i finish all 14 shows i will reward myself with a season1 rewatch, but then again it isnt as fun to rewatch when dong it alone as i cant make comentary about what i enjoy and what is going on, oh well maybe the boi will be watching his drink of bleach show, which other than the pendulum arc wasnt the best as it was well c tier at most. The orb folding playlist is currently playing at this hour as we are expirencing real classic 2021 vibe time vibes witht he late times and golden age music vibe time vibes witht the bot -playing some classic orb folding songs. there are over 400 songs in the playlist and that do be pretty knifty. so the database update worked better than i thought it would as it went off (other than hank typos) without a problem. The database update allows for so many more things as we could easily do many things with it like the whomst command which i fixed here to require a user as opposed to it being an optional argument. which that was done on the second call of deploy commands which i thought didnt work but turns out that it just needs time to deploy the command update which it told me when i tried to run the command which led me to fixing move to as well with this commit. Well i shall be sleeping soon here for real this time but to you reading this it will seem like no time passed but for me it will be as if i had a sleep, maybe i will update you with soime stuff that occurs between now and well a few words from now. idk well see you on the flip side as hank sometimes says. So it has been a day now and i it is now the AM hourse of june 2. this means it is time to continue the commit message, and well now shows got watched due to me being distracted but i think i will be watching some soon. cookie dough is good and that is what i am eating right now as it is late and i dont want to wake anyone by doing stuff in the kitchen to cook the dough, alas it still tastes good. so i took a short break there, which you probably wouldnt have known if it werent for me telling, but it was because of COC as i was doing stuff on there. i used the Adam troops to steamroll something i really shouldnt have at my level. they had over 100k of each resouce which caused me to get full and now can research level 2 boney bois. So back to what the day was, as it started off with me planning on doing some AoT watching but i watched youtube because i found something on there to watch and then it was 6pm and dinner time and i got distracted and then now it is now. I will likely watch some AoT after i finish with the tasks for the day and hopefuly maybe finish the season, idk it has 8 eps left and calculating how long that is would be about 2-3 hours dependant on if i take a break or not to get foods. tomorrow will be the day i do the genshin story quests so i will not be able to watch AoT during the day hours as that is dedicated to genshin quests as there will be some LORE in there and it will be a good watch. I do still want to do a Man rants about AoT or SAO for far to long part to this but that may have to be over the weekend or after as weekend as i said before is a semi-busy time with being in boone. Typing this commit message is bringing back flashbacks to a hey buddys class and back to when i was in classes last semester and well that is when i did the last one so it would make sense that it would be what i am remembering.  hopefully i can use my detective skills to determine the accurate date of shanes birthday, if i find it before i send this commit then i will add it but it may be a year long endeavor to get the date. I have my suspicions that it may be on July 21 but that is just a hunch and i will have to do some day checking when the time gets closer, for now his birthday is on june 9 because that is 69 haha funny number. i may hide the fact that i will put it on 69 until it is june 8th and then on the 9th call a baba command in general to confuse everyone and then cause them to have to ask for the real shane bday and call his hand, this has given me a date that this commit will have to be after now as i have wrtitten all my plans here and if anyone were to parse this it may be shane so i cant go putting this on the github yet until probably after june 9th. good thing is baba has no urgent changes and we probably wont be focusing any updates to baba until well likely sometime later this month or when i do request it. i hope that by the time that this commit message is done it will be longer than the last and more content as in other than the SAO/AoT rant, just random thoughts spewing from my brain. hank has stated that he needs to find a new jet flying truck in stormworks which is one of the games that baba could be playing if i added it in this which i havent yet but i could if i remember tomorrow as i cant be bothered to do it now. Unlike the last one i am trying my best to limit spelling errors just for my sanity but any punctuation other than commas and periods are basically being forgotten. and capitalization of things that are not the first letter of a sentence is basically a no go too. hopefully we can convince hank to add dadbot back to the server but that is not going to happen sadly :(. THe way that i will likely explain the SAO storyline will probably be more clear than if you were to watch it as isaac was watching it which was more of a skip every scene of the show as if it were a stone skipping on a pond. but that is for another day. Today bob has 6 o's in his name and he has yet to say anything about it but it has been 1 per day and hoepfully he is just not going to notice until it hits the character limit. it is a many day strat but one day he will have all the os in the world, well now that means i cant post this commit until he notices for that would play my hand, well he doesnt do anything with the github so it "should" be fine to do it before but i will probably not take the chance yet, as he does know about me doing the commit messages as i have told him both times. so back on topic here with whatever i was talking about before, well today will mark nothing as it is only june 2 and as of baba there is no holidays on june second. i will lilkely find some more holidays to add to baba and also will instead of posting error.png as the image for when the holiday has no main image, i will just do the same text overlay thing as i did with the wednesdays until, hold on let me check something real quick. ok i am back and it is fixed for this commit as well, this is how things go around here orignially the last one was 3 file changes and it ended up being a massive update with many changes and this one will lilely be the same. i will also be doing some callback stuff for baba wednesday potentially here as i had a issue with image delay again but it might just be a one time thing so i may just push the wait timer a few 10ths of a second to a whole second longer and none will be the wiser, well anyway that is all for this days stuff as i am going to watch AOT now with some snacks, see you on the flip side, again.  SO the thing is there was no watching of AoT last night, who knows when i will get around to it but i was able to get to the interlude story quest and it was a great quest where we got basically a bunch of Xiao and yaksha lore and it gave character to all the yakshas that were the hero of the liyue region. Twas good and i hope that maybe someday down the line (copium) we get to play some of the yakshas as playable characters somehow idk how they would do it but it would be nice, yelan story quest will likely have to wait for a monday playthrough as i wont want to play it while in boone, but i may do it later tonight im sure you will know sooner than later as i will say if i did it when i do it or sometime around the time i played it. Well it has been a while hasnt it, so i went to boone and am back watched AOT already and started dressup darling. so the cliffhanger for AoT was good and i am excited for part 3 after we leaned about the rumbling and the titans are heading for the mainland which caused much strife to all of the main characters. but that is enough of AoT until the next time when i will do the long explanation. currently i am on dressup darling which has been a swell time as the show is reminding me of horimiya which was a very good show that i watched back earlier this year. But enough about anime lets explain why it has basically been over a week since the last time i was doing this writing of the git commit, well there is some leek wars stuff going on which the main three working on leeks are me jeremy and ryan as week have leeks that will kill the enemies. so far the leeking has been going swell and swimingly. the leek wars also have created 5 haikus that were in the database which means we have a massive amount of haikus  now and almost have reached the covited 500 haikus number which hopefully wont be horse related like the 400th one was (hank). leek wars has been taking a lot of my time as i am making bikus the leek be able kill all the enemies in the leek gardens. Today is pizza day so it is going to be time to eat the beepza. well i have been heavily distracted while watching the great and powerful Aleeksander do his fights vs the domingo ai leek.  but anyway i think that tomorrow and this weekend will be a bit of work as i will be busy in the evenings which will result in tired time so idk if i will work on leeks until monday but who is to say really as i will possibly work beforehand on leeks or i will just watch shows like i always do, similar to today. the good thing is that deino community day was confirmed as i accurately predicted back during go fest last weekend. the good thing is it is an 11-2 cd which means i can do the whole event at the park in cary without having distractions and after while at the place in the evning i can potentially do some catching if poeople do the dieno evolved form raids there. hopefully i get a hundo but i dont have high hopes. we are back because headphones are deadphones and now i can full focus writing the git commit message. well i have now wrote the code that allows for the haiku to do a custom one and it is working well, aslo added a code part that will sanitize the inputs for adams hopes and dreams to be improved much more and he will really like the command name and not go insane because of it. ඞ surprise mogus. hey i guess i can do the wordle again in here like i did last time, it is not because i want to pad out the characters with easy amounts of text no, it is because i can do it. :) Wordle 356 4/6  ⬛🟩⬛🟨⬛ 🟨🟩⬛⬛🟨 ⬛🟩🟨⬛🟨 🟩🟩🟩🟩🟩 there you have it, the wordle for  the day splendid isnt it. the word was annoying as it took way to long of random guesses to get but i got it in the end. ok enough words, time to go back to talking about leeks and then we will do a SAO rand as decided by baba with his coin flip, next time i do a long one of these when headphones are deadphones, probably on moday, we will get the AoT rand i promised as well, that will surely pad out the run time on this if it were a video but it isnt so whatever it will take YOU long to read my dude. So we start off on November 6 2022 which is this year but when the show initially released it was 10 years out so funny how time works, but back to the show. So SAO takes place in a VRMMORPG and well it uses a brain connecting thing which allows the users to view into the game, so at first the MC goes into the game and all is well, he meets some friends like Klein, and then his friend wanted to log out but couldnt. this led to them going to the main plaza where the game master kaiba was and he told them that if they die in the game they die in rreal life and to win was the only way out. this reulted in mass panic and at the end of episode 1 one month passed and 2000 people had died so far, So as the time went on they were stuck on floor one for a while but the people wanted to get out so some decided to form a party to slay the first boss and after losing a few people to it they succeeded and we meed the main female lead asuna.  kirito told her to join a guild as she is strong and should not be a solo player alone.  Later on kirito meets a group of people who he considers guilding with but when an accident and trap kill them all he thinks it is all his fault and decides to go it solo for more time as he doesnt want to put anyone else in danger. by now there had been at least 35 floors defeated and it was about 1 year into the story as it was around chrmbo 2023.  Now around the early 2024 times we get to where kirito meets the beast tamer character silica and basically this was one of the episodes where we meet a new character who will be in his group later on when they escape. Now it is march 6 2024 and they have gotten up to floor 56 defeated and there is a main ground called the knights of the blood who asuna has joined and is one of the top ranking members of. Kirito and asuna talk a bit after meeting again, rocky start, but then they get to a town where they witness a murder. normally as this is a game where this can happen that would be bad but not odd, but this was in a town which as a safe zone so it was way out of the ordianry. they then do investiagitng and by the end the end up witnessing another murder  Kirito and Asuna contemplate the events that had just occured and whilst doing so make some food, asuna makes a sandwitch for kitito and after some witty banter about food he accidently drops it and it shatters similar to how the other two died. this made kirito realize that the shattering of the people who were murdered wasnt them but their items and they teleported away at the moment which made it look like it was a murder, they then go to the grave site of the fallen comrad of the people who were thought to be dead and realized they were paid off to do this and wee meet the dark guild laughing coffin who are people who go around killing people in the game for fun.  SOme of the people seen here are more relivent in later storylines in future seasons so remember the guild, there were 3 memebers at the site, johnny black, PoH and XaXa, these three will be important later, so anyway they go back to town talk about stuff and then carry on with their adventures, Next episdes is another one where they MC meets another side character who will be part of his team outside of the world, basically same as the other story but she is a weaponsmith. So they then go and have to fight another boss same deal asuna wants kirito to join her guild, there is a wager that happens sometime but this part was a bit fuzzy for me. then they go to around do some more boss clearing and then by the end kirito asks for asuna to go with him on leave but they have to do a battle with the guild leader in order for it to be approved, otherwise kirito has to join the guild if he loses. so kirito duels with heathcliff the guild leader and whilst battling heath ends upo moving his shield at an unmatchable and impossible. kirito ends up losing and then gets forced to join the guild. They go to get him some clothes and when stopping to rest they are met with a member of blood oath who is confiming himself to be a member of laughing coffin and almost kills asuna but kirito is able to step in and ends up  killing him.  they then decided to have time alone together and get a house on the 22 floor which comes back into play later when they come back to this place. The two of them end up getting married and then actually take a temp leave from the guild.  they then encounter an ai of the game who they make their daughter. they get yui and have a bunch of fun in their house. things occur that are not super important to the story but it is fine, we learn that yui was made by the cardinal system of the game and it initially prevented her from interacting with people but she somehow was able but now the cardinal systam was trying to remove her, but kirito was able to save her data and keep it with him so they could recreate her when they leave the game eventually.  So time has passed and they are back to fighting bosses over time and they have reached the 75th floor boss and there is a big battle against it. The next episode is the final of this arc as the final battle was going on after the battle for floor 75. so kirito was sus of heath because oh how he had such high health and was surprisingly not exhausted. so kirito attacked him and what occured was a purple immortal object was there similar to back with yui which raised many questions amongst the players in the game. Thus it was revealed that heath was the game master kayaba who then confirmed it. some dialoge continues and we learn about what is going on kirito and asuna attempt to attack him resulting in them dying but main character syndrom kicks in and he is able to kill kayaba and they then realize they cleared the game, kayaba gives a monologue and they then are able to wake up from the game for the first time in 2+ years.  and that was SAO Aincrad Arc which was only the first of 5-7 arcs dependant on how you would classify it.  so time for at least the rest of this season.  starting after they get out of the game we meet kiritos sister and we learn about what happened over the past years whilst he was in the game and what was going on outside of the game. at the end we learn about asuna as they were at the bar of the main bar keep in the game, Agil. this surprises kirito. So kirito learns about the game ALfheim online which is where he will be going to next. kirito promises to get asuna back so he ends up going into the  game to try and save her. once he gets in he revives Yui and realizes he has some buffs from sao somehow. then near the end we meet some new characters leefa and her friend who are runing from salamanders, another group in this game.. so they do basic introduction stuff and not much goes on but we meet the main big bad oberon and we learn how they would be able to get up there,.  so they now are going to go on an adventure and decide to take shits when disconnecting so they dont get killed whilst in the neutral zone. but unbenonst to both of them is that each other is the others sibling. basically kirito is trying to get a bunch of allies to help him get to the top of the world tree. and they  do the stuff in this epsidoes and yada yada not much happens sister likes brother generi anime stuff .basically there was a faction war, he solved it and now he has friend to help him with thre world tree.  so basically he knows about asuna being at the top of the tree he tried to go up there, there is an invisible barrier and there is mutiple failed attemps which are not promising for his success.  his sister confesses but knows about asuna and is sad but so be it, next up is the final push and everyone helps with this and they get into the top of the world tree after yui opens it. kirito reunites with asuna and then oberon shows and causes a proble. kitito gains god mode and then is able to use kayabas powers to defeat oberon and cause him massive amounts of pain.  this results in kirito recieving the seed and he is able to create games similar to SAO with it that are based off it with the same underlying cardinal system,  basically now they are in the real world and we learn about what kitito does with the seed which is he makes it open source so anyone can create games based off it. this also means they add a version of  SAO to ALO which this time they decided that they would successfully beat it, and thusly that was all of season 1 of SAO.   so i did say i would do the AoT on monday but i think i may end up doing s2 of SAO and maybe Aliceization too as that is as long as s1+2 combined. there is also a movie but that will be short and easy to explain as all i need to do is explain the plot. the good thing is that s2 onward will be easier as i watched some of s2 recently and all of s3-a not underworld so that will be needing some info and research but it was a watch of 2021 but early. but that may be all i type tonight but that wouldnt be fun as albedos theme is going on and it is pretty great way of carefuly drowning out the fnv stuff, i will leave it as acronym but it was a true 76, 104 nauvis orbit moment and i just dont need to worry about it as i will likely be sleeping soon aka watching more dressup darling in bed. i am attempting to become woketh around 2-3 so i can eat lunch here then and not have to worry about dinner until a perhaps hopefully a sheetz run, i can potentially get ryan in as he wanted one and it would probably snowball into multiple people being there. so yeah today has been a day of leeks, anime and pizza, with a touch of nauvis orbit., well i hope your day was great i will see you on the flip side aka in a few seconds as it will be quick for you. Ok, it is now a new day here after i have watched a few more episodes of dressup darling, it has been really good so far. so we now are vibing with the music bot and it is giving some quality songs after i do my tactial song search for the spaghetti rat song and i make a list of many songs to push to the start of the list, twas very good. so mogus has done a crossover with fortnite so i will have now a delema if i want to obtain that or not but alas monday is the day of all the things i will be working on leekscript possibly if i find time but also anime would be fun to watch. in a bit (after all the chosen songs are completed), i will start to continue some more to the dressup darling episodes as i want to finish that by the end of the week. Sumemr shows 2022 is not going as fast as i want but it should pick up soon, hahaha sure. well i hope that i can get up to par with the amount of shows in 2020, but that would be a long shot. so i will probably do a fate movie three, where i watch one per night or i binge all 3 easily. so after watching dressup i can go to vivy or i can go to fate movies which i will decide in the moment. i also want to make a timeline feature for ol scheduly, with something similar to a calendar for checking future stuff, because why not, but that is not anytime soon. ok it is now time for me to explain why there is a frog that needs to be in our house at the moment. 🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸 ahh there was some nice frogs for you to enjoy. so it is time for me to rant about my shows list which i hope i can get done before going back to class, as i have 2 months to watch a bunch of shows but the thing is i only finished 3 shows since i got back which there was time i was busy and yeah, but that doesnt matter much. well if i dont keep getting distracted i would be able to watch all the shows i want so maybe when the vibe crew goes to non-woke times i will likely go and watch some episodes. the vibe playlist has some great songs on it from love live that is flintstones and other things involving hhgregg which are all quality songs that i will try and place at the start of the song everytime i see them when doing queue scouring. at the current moment isaac is starting fallout 4 which is the same day as when he finished fallout new vegas. thusly we will probably have some form of 76 104 nauvis orbit but that will probably not happen as it is only the start and isnt about NV. take a ride on the bungle bus you will enjoy it. bikus the leek is doing well and i hope that when i implement the quality leek stuff that i want to on monday then i will have to do that then. i also could use the wed/thurs pair time to do the leek stuff or watch a bunch of episodes. i do plan on having some form of watch time when the time comes, i will need to make sure not to get distracted when the time come but that will probably happen and what can i say but i told you so me. something about hank meeting a ghoul is what is going on in fallout right now as the person who was at the gate became a ghoul in 200 years.  after this song that plays finishes then i will have to go downstair and get some sort of dinenr as i am hungry and only ate the tacos around 4 when i was not at home. timelines of frogs invlove the frogs in the time of the frogs being timed to find where they are kept hostage for the time being. hopefully when i finish this git commit message we will be over 50k characters as right now we are only at 27k so if i am playing my cards right this will be the middle of the whole document. crab rave time!!! the haiku database is going well, as we are going to hit haiku 500 real soon, at the time of this recording we are at haiku 496 so we only need 4 more haikus to get the perfect 500 in the database. it would be extra great to have 500 be a good haiku and not some sort of horse repeating haiku as 400 was. it took us 3.5 months to make a total of 100 haikus which is a good HPS haikus per second rate, even though they are not made each second it is faster than other sets of 100 like 0 to 100 or 100 to 200, etc. but that is not to be worried about as i am estimating by the time that this update goes out to baba we will be well above 500 if we keep talking in the leek channel like we do as it causes many haikus when we do that. ooo grand escape, good song is now playing and it is a blast to listen too. i should tune my car reckonign playlist to be set to play grand escape tomorrow whilst i drive to the place i must go to at 3:30pm. ok i want to go get dinner still but i havent as i am currently listening to the quality songs that the music bot is playing which i do enjoy at the highest degree. we soon will get horse race, genshin themes and random chiptunes and it will not even be 2 yet, i hope that by 3am i will start up some episodes of dressup darling. that would be swimingly great and exceptionally splendid, indubitably quality watching of shows to watch. BEANS! So it has been a few days again, and in that time i finished dressup darling. it was a very good show to watch and i hope there is a second season because i want to see more of the content that is in this show. also tomorrow is supposed to be 109 feels like which will be pain and we have nauvis orbiting going on with NV so aaaaa but whatever. now onto something that may be pushed soon in this update, it will be the voice activity update. so in this we will have baba have the ability to track users voice activity and when they are in voice, there will be some things to make sure that the data isnt lost when baba crashes but this may require testing on production. this couldnt easily be done without the db update and i am glad it will be made as i hope it works out well. i think i can code it well, it shouldnt be too hard, the difficult part will be crash data prevention. so we may need to do a bunch of testing but whatever. that may get worked on around wed/thurs if i have watched enough episodes of vivy to be satisfied in doing a bit of programming for baba. and yes vivy is the next show i am watching as it seems like it will be a fun watch to see. idk what the major premise of it is but it was reccomended during one of the videos i watch with seasonal animes, it is many months old but i am sure it will be a fun and entertaining show to watch. speaking of watching stuff, tangentally i was able to get all but 2 of my friend-10 max ascention characters in genshin to have their lore explained and read/listened too. I have mona and ALBEDO left to do that with and i may do that later tonight after getting snacks or it will be tomorrow/wed as tomorrow will be the most painful day  of the year. i hope the thing i need to do gets cancelled tomorrow as heat is not enjoyable and it will feel OVER 100 in temp and i would not like to be outside at all when it is 80+ none the less but 100 is going to far. so i had a thought about rendering the bungle bus in the hey buddy renderer but i dont want to think about the logistics that would be needed to do that. so i will probably not do that at all as why would i cause myself pain when i could cause myself fun with coding baba :). also the weather update for baba will have to occur too, if i have time on wed/thurs and get the voice activity update working early then i will possibly work with baba to get some weather predicting and allowing baba to give you weather for any location as long as you provide it, also it will be restricted to USA. baba hurricane tracker will be easy as it will just use the one from NOAA but i hope that it is just a single link i can copy and send in chat and it will work correctly, i hope it doesnt involve web scraping but i may have to figure it out and im sure it wont be super horrendous, only a little bit but that will be as expected of anything with baba the multi-funtional random discord bot. oh and back to the voice activity thing, baba will also detect if a user is in voice on their birthday, i may do a crude date detection thing if user is already in channel, similar to how baba makes holiday channels, and if a user joins on birthday then baba will join and say happy birthday too. the only thing is should i check if user has already had baba say happy birthday or should it happen everytime, also i may put it on a one minute delay to allow the user to settle in, and void if user leaves within the minute (hank jumping in with mic problems). this is turning out to be more complex than i thought but it should work out. also i hope shane makes some good charts from the data i collect, but it will take some time to get working. also for getting baba to speak we could try playing audio clips generated by 15.ai of thing that i pre-provide the bot, including saying like happy birthday, etc. and a list of audio clips of each of the people in the servers' names. now we need shane to provide his birthday and this might just be the incentive. we could also have the voices be different and random, such as horse, tf2 characters, narrator, etc. it will be an excessive amount of audio files but why bother, it will be cool. to splice them we could either use a package for node or we could do the crude way of just playing them in order after each one stops, which may be more complex dependant on how discord's API works with detecting when an audio file finishes. oh no does this mean we will be needed to add ffmpeg to baba because i dont want to deal with that after jukebot and all his fun things, but it will not be as bad as i have it installed on here already, i think, either here or the laptop and if i have to do laptop gaming to get baba to work so be it. well that last part of the text was all actually relevant to baba so there is some use to reading all of this commit message, also i wonder if this is longer than the last one as the last one was some unknown length. also i think it is snack time perhaps, but that involves moving downstairs and oh boi do i not want to do that. especially if i have to deal with massive heat tomorrow and be outside for many hours on end without any breaks to go inside, i guess bathroom breaks may occur more often as i will have to use the 'bathroom' as i am drinking more water to keep away the heat from murking me on the morrow. ඞ surprise mogus. ok ok ok, time to get back to doing something that is important, reading genshin lore, i learned so much about the characters as i am learning about their lore and such. once i finish the genshin lore stuff, i will have to swap over to doing teapot suff as i have wanted to basically since before 2.6 and 2.6 was the 9 week update with no teapot editing ability so that is a hefty amount of time, this will also allow me to get the ruples for all the inazuma characters which i have been neglecting getting but i will eventually. so i will check off two things at once, which once that is done i will only have the recokoning left on my any day events part of the schedule other than the shows i am watching which currently i am between shows so nothing has been added as i dont normally add things until the day of. but if i am able to check 4 things off of this list by the end of the week it will be super great and i wont have them lingering over me like they have been for months now. i could work on the teapot stuff today but i may just call it an early night and use tomorrow to finish a bunch of things too whilst waiting to see if there is any cancelations due to heat (oh how i hope). i think the reason i am drained right now is just hunger and if i get english flavored muffins i will be able to regen my energy and stay awake to post 4am doing genshin or even starting the show i plan to watch, vivy. i ate snack, twas good, now i have energy again and will probably just move to bed and finish off the day there. so its been a bit, today now has become june 20th and we have finished vivy, very good show and i enjoyed it swimmingly. it has spoked the want for me to do another version of the recokoning. as right now i am listening to the final song of vivy. so i have also yet to do the genshin stuff i said i would do the following day but i think i will get to it tomorrow possibly or even tonight as it will be a long night of being awake and watching some dragon maid. i have started a bit of watching dragon maid and it is going to be one of those good entertaining shows which i find fun but not movingly great like vivy and horimiya. the shows that are single season which are 12-13 episodes are the ones to watch out for good stuff. so a brief summary of vivy is that at the start an ai from 2061 gets a helper ai from 100 years in the future sent back in time to help prevent a war between AIs and humans. this happens on a specific day that is significent and it will be explained later by me why. so the first episode goes into the two of them meeting and saving a person who wants to give AI's more rights as he is being targeted by an enemy faction known as TOAK. whilst battling them vivy saves a man who turns out to be important figure in toak in the future. after saving them vivy sees a future news paper where her friend dies and she tries to save the friend but the support AI stops vivy as they are not here to change the timeline. we now skip into the future where we vivy reconviens with matsumoto (support ai) after he shutdown for the years between in order to not cause any anomolies. this mission involves them saving a space station in which it kills many humans and is caused by one of the ai's that were controlling it. so they go onto the space station, and the head ai on the ship was not what matsumoto thought she was. this made vivy want to find out more and not just shut down the head AI. we then learn that TOAK has infultrated the space station and it is headed by the person who vivy saved back at the falling building. the members of toak brought an ai that is the sister of the head of the space station. they tried to impersonate her and cause the ship to fall down with them on it to send a message. vivy ended up saving the head of the station and they fought toak and the only casualties were the two ais, the head ai and the one toak brought. so then there was another time skip to many years later when there was another event they needed to fix due to the singularity project which they were working on. this one was stopping the ai only island from existing as it was a step up in ai rights. so they try and go to the island and meet up with another who wants to destroy the island too, which results in them making it to the island. they meet some friendly bots at the island but sadly they had to put the shutdown virus into it which resulted in the islands defense systems kicking in. at the same time toak trys to invade and vivy saves the same dude again and he sort of helps them take back the island. the island is actually the dude who they met initially's ai girlfriend who was going to become his wife but due to the sunrise incident (space station), things played out differently. this resulted in a chase sequence where they were able to shut down the island but the dude couldnt live without his ai wife. this caused vivy to have a catastrophic error which resulted in her being reset. many many years later a vivy (with no memories so we will refer to her as diva), sees a person who she thinks she knows so follows him but this results in her meeting with matsumoto again and he ended up trying to pretend they dont know each other but they chase each other around and mutually agree to work together to stop the next catastrophy. this one is the first documented ai killing themselves. so they spend this episode seperate but together working on the mission which resulted in matsumoto learning who was behind the catastrophy which was a support bot controling the girl ai who died. on the other end diva meets with the head of toak who now is in an ai body as he would be too old now. they do battle with each other and he just wants to know why she saved him as his former teacher was an ai who sacrifised himself to save others and he couldnt understand why. he was successful in getting a virus into diva which reset her alter ego back to vivy again. this occurs duing her final concert on the main stage. we then jump to a point in the future where she is now in a museum as she now has retired from singing and is a display that people can talk and view. this is where she meets osamu who she talks with over and over throughout the next many years. she also starts trying to write her own song as she wants to know what the heart means to people and her. we then learn that osamu is the person who created matsumoto the ai. then we cut to the day of the war and it still happens which results in them trying to find osamu to learn what they could do. they then go to toak which is where they meet the grand daughter of the toak leader she saved many times. whilst there they meet the sister ai who was brought on the sunrise and they learn of how she still serves her master. they then learn about what is going on in the world and how the ai are following orders from the archive and how any ai that hasnt connected to it is still safe. vivy connects with the archive to learn more and learns that the archive has known about what they have been doing for the past 100 years and still decide that this was the right path, but one part of the archive believes that vivys song she wrote on her own was enough to show that ais and humans could live together. and that ai tells vivy if she sings the song then they could stop the ai from destroying humanity. thus they go and try and take over the archives tower but while doing so almost everyone dies due to the ais getting the upperhand and they archive sends down all 1000+ sattelites to earth basically wiping most of humanity out. but osamu survives and this allows for him to send vivy's conciousness back to when they first met to go to toak immediately. in doing so it would cause him to die as he was saved by her but he was willing to risk his life to save humanity. vivy goes back in time which allows her to go to toak immediately and tell them about the plan of action to stop the sattelites from falling and the rogue ais. so they split up and vivy goes to the stage, while everyone else goes to the archive to stop it. vivy is able to sing her song and they are able to stop the sattelites in time except one which would destroy vivy but matsumoto is able to stop it in time which results in all rogue ais stopping function. in the epilogue matsumoto is all fine again and vivy is revived with no memories but she has her purpose to sing still. so that was the brief recap of vivy -fluorite eyes song-. basically if the show is something i really enjoy then expect a recap here, as long as the baba update hasnt gone out yet which it still hasnt as i am waiting a bit for people to forget about the voice activity update. speaking of that well it was implemented basically the day after i said i would and i did get it working 100% efficiently but then i brought it up and now it is opt in so ugh, but whatever it works and there is a new opt in command and opt out command. also it will technially opt you out immediatly but you will get a message until you run one of the commands and i cant be bothered to get that working anytime soon so that may just be how it is. but the good thing is that it works very well and i am glad that it does. i think that this update may be done soon but idk as i dont feel like dealing with the hastle this week maybe it will be sometime next week or after hank and adam go on summer camp which will be the most reasonable as in case baba breaks catestrophically then we dont need to cause hank pain whilst he is not home. still got the final song of vivy playing i think that this will be one of the first GG bois songs in a long whiles as i havent added to this since idk when but it has def been a while. oh and another thing that has happened since the last stuff that has happened here was that we had not one but two winning clan wars in COC which was good, i was mr 98% the first time but redeemed myself for the second war. we are about to have our third war tomorrow which will be knifty but after that i think we will take a break (as adam wants to). i have gotten 4 builders now which is gaming but alas. also the vibe playlist (scriblos to feed bikus too) has gotten the vivy song too which i may have had a part in making happen :). ░██████╗██╗░░░██╗░██████╗ ██╔════╝██║░░░██║██╔════╝ ╚█████╗░██║░░░██║╚█████╗░ ░╚═══██╗██║░░░██║░╚═══██╗ ██████╔╝╚██████╔╝██████╔╝ ╚═════╝░░╚═════╝░╚═════╝░ omega sus, this is rare but could happen anytime. oh in this week too we had a drum event in genshin which was really fun and we got some itto lore which is always appreated. back to vivy, so the matsumoto ai cube/bear was voiced by itto's va which is really cool as i like his va and he makes things funny and entertaining when talking. so i am hungry again and want to get waffle house but everyone is playing a game which means no waffle for me likely tonight :(. mayhaps around 2 am but that will be cutting it late in the night as i will be starved by then and have withered away probably. heyo again, it is I, and i have finished dragon maid season 1 but that is not why i am here, the real reason i have arrived is for the fact of that baba has buttons now. so haiku purity score will show only 5 items per page and if it gets more than that then buttons appear which allow for going between each page successfully. this was new thing i learned which means buttons could be used for other baba stuff as i have figured out how to parse the fact that only the user who sent the message can click the button. this could work for some other functions but idk what it could be used for yet if i add more then it will be included here. well today is sheetz night and pizza day too which is a double win. extra gaming will be done today which means fun. so i want to start some more dragon maid but i paused watching it due to so many YT stuffs but i finished that and now i could easily watch it later in the evning which may happen but i cant stay up that late as pokemon CD is tomorrow which means an early bed not to mention the double game tommorow which will mean a LONG day but hey baba wont be updated for a couple weeks as we are wating until post summer camp so that there will be no need to debug whilst hank is away. bikus is cool. so the next two days will be a hastle to deal with but once they are done i will have 2 days of good, and that will be alternating on and off for the next few bit of time until we hit the day SAO movie home relase which will be a good pattern. but the good thing that is better than last week at this time is that my friday was fully open which means that i was able to watch all my YT stuffs which will free up saturday and sunday evenings for dragon maid as if i play cards correctly i could do a 4 episodes per day system in which the next three days i do 4 per day, maybe more on sunday evening as that will lead to monday which is free and the night before i will be overly drained probably but who knows. hey at least the baba update is working well and it is done efficently so it will only get the data on call 1 to baba so it will just used the cached data when paging around. this will result in mismatched data if something is added while command is active but that will happen very rarely as i manually add the data and i would be the only one who is using the command when that could possibly happen as i am the one who commands. we are nearing the covited 50k characters i wanted for the commit update which means i will be able to do the baba update any time after that. that was the real reason i was saying baba should be updated post hank summer camp as i wasnt sure i would get to the character count when i wanted to. also it would mean i would have to omit the SAO s2+ introspectives and the AoT one as well which i will likely get to once i finish 2 more shows fully and probably before fate movies (i will get to them eventually). i have done well for this week as i finished 2 shows this week (technically, as vivy was started last week but it was only thursday last week which means i got through 2 shows in a 7 day period of the 16th - 23rd/24th. so after dragon maid is done, which i will likely next be here after that as i wont care too much to do any typing here over the weekend until potentially monday and i HOPE that i will be done with dragon maid by then but that is unlikely to happen fully. but we will see, and that is probably all for me here on the 24th of june, see when i see. heyo it is me mr boi boi back here on saturday after the long day of stuff, wasnt expecting to do any baba stuff but i got next birthday for wednesday command working so we now can get the next persons who has a birthday, their birthday to show. also baba has more buttons for the button update which was the solution to multiple events on same day when calling next event when it came to displaying them both like the legacy command system did. the old way was to pass both images at once but that wouldnt work with interactions as easily so now we just have a pagins system which allows for switching between frogs similar to how the haiku purity list works. there is no page numbers but oh well doesnt matter. also the code i wrote for haiku embeds works for this as i just pass the message i send in an array and it will generate it with the pages and it just works well. there may be some more buttons in the button update but at the moment i am unable to think of good ideas for them, maybe voting or something but idk how to get that to work. i will have to look throught the list of commands. 50k characters were just hit now so we can update baba anytime but that will be still done post july 4th and the summer camp week. that week will be likely high levels of show watching as most people will be away leaving me the ability to be at the computer or bed and watch many shows and maybe even the fate movies, ha funny joke. ok that was all, time to go watch my shows again but first get through YT stuff as i was busy all day and am now just getting time to do that. hey buddy, it is i here after the weekend of stuff popping in again on the 27th in the am to say no progress on dragon maid season 2 except for 2 episodes but i just ate a snack so i will probably stay up watching some episodes potentially soon. ok that is all for now. it is wednesday my dudes, no it is really June 28 and i finished the episodes of dragon maid now and the tuesday before the big rains start occuring amongst the north carolina areas. so dragon maid is done now and baba button update has been added a bit more too as well, we have now the paging system for wednesdays and all the other frog related commands that deal with holidays. oh and idk if this was mentioned all the way 50k characters ago but baba has now more friday varients for when the command is called on a non-friday day. they are funny also we brought back the how was your X doing funny command. so next up on the chopping block will be the show called sabikui bisco which is a show that i know not much about but it seems to be a good thing to watch and it might be fun. ok we have done 2 episodes of the show and now it is the 30th in the am and i will have to drive out to raleigh for picking up people. oh boy will it be a time to drive at this hour but alas it must be done. we shall take the fun road and it will make it the most easy to do. but then later we will be able to watch some more episodes of my show and also probably eat some form of dinner, i thought i would have to leave earlier than i did so i didnt eat yet as i was going to after but since it has been so long i guess i must eat snacks beforehand. ooph. oh how mind bending 5d chess with multiverse time travel is, thusly we must go and play that tomorrow potentially but unlikely as those who may play it wont be playing it when i get home around 10/11 tomorrow, alas it will be for the days i dont go outside. but at least there is a pattern to the outsides where it is 2 days out, 2 days in up until the 8th which is the day SAO movie is released which will be cool and i will likely watch it that evening. this meaning i should have no shows on the plate when that day occurs, so i must plan accordingly. i would be watching some of my episodes right now but i must leave at anytime and i dont want to leave mid episode and i know 100% sure that when i start an episode i will be summoned to leave on my adventure. finales for some of my other shows were this week so that frees up 45 mins for both wed and thurs for the next few months which is good and lets me watch more shows/YT videos. the kitten is making noise again and he needs to get some pets but he will be a special snowflake as he was playing with the cat door. still havent left yet and it is 1am :). i couldve watched many episodes and had dinner by now but i have yet to, alas we must keep wating. i will be taking the outer circle road for sure now as it is the most straight drive there without any odd paths. the issue here is that it will be one hour of time before i get back home and preferably want to get home before 3 so i can possibly eat something. alas i must continue to wait. ඞ, surprise mogus. i guess i could get cookout whilst out there as it is along the way and it would solve my hunger issues. that would be gaming to the extreme levels and it would allow me to not be hungry anymore. so about the AoT and SAO rants, they will return but i will likely do them during the week of summer camp so that i could wait until the absolute last moment possible. but that doesnt matter much as i will still do them for sure if not in this commit then the next one that will be published to baba in september. this is what i call a pro gamer commit message. long and im sure no one will read it but as the days go on it gets longer and longer until it becomes so long that it causes adam to go insane. the only person who i think will even skim any of this is SHANE, i put his name in caps there so that he will se it more likly and read the stuff before this, i see you reading this and you should know that there is some quality content in here you just have to read it ALL. ok enough about future people, back to now where i still havent left and basically i will just keep typing random stuff here until i am going to leave. see i need to limit my time to before 2 so that i am guarenteed to get some cook out as it closes at 3am, which is good for me at least, but why do i need to wait so long before leaving? idk man, i just want to go now so that i can eat dinner or something. hey we hit 55k characters now which is pretty cool but can we hit 100k? probably not without the AoT or SAO rants, might even need both. but who knows, as AoT is 4 seasons of stuff so that would be a lot to type and SAO has 3ish seasons but the 3rd is the same length as s1 and s2 combined so technically same amount of episodes as if it were 4 seasons. so both have the same season counts which means probably 40k+ characters in there total or each idk how to count that well. you can give spahgetti to a rat, incase you didnt know that. here frog 55555, that is the character count at the end of the last 5 in the 55555. you see i am running out of quality content to provide you and have resulted to listing the character count now multiple times within a 1000 characters, the old me wouldnt have done that, youve changed me, youve changed. Frog, ah a classic. so the baba progress bar is working well and we have gotten to 49% through the year which is very good but i hope to post the progress for 50% before daniel is able to post the twitter message in general. he has posted it at 40% and 45% so according to the pattern he should post at 50% as well which will happen any day now as we are .37% through 49% so soon we shall arive on the prophecised moment. why so late? idk because i said i would do the thing i would do at this hour but i thought it would be sometime around midnight or maybe even 11pm but not post 1:30, i think i will leave and head out at 1:50 even if not summoned and get food before hand. see i was going to have chicken for dinner once i got home but i cant make it before as it is a 30 min timer and once i get home would not be fun to do at this hour. plus i cant make it whilst waiting as if i get summoned i cant just pause the cooking easily. so i have decided to get cookout as i said before. daniel would be jealous of me as he lives for cookout so much and wants one closer to his house, which is why he likes the one in boone which is fairly close to where he lives there and he goes there frequently. it is me again, been a week or so, we are now on the eve of july 4th and it was an extra spicy hot outside day today where it was so hot i felt like death. but that isnt why i am here right now, no, i am here to talk about how we have had a takeover of the server by jeremy as hank and adam are gone and the server is now a concertina server, very excellent. ok now no knew baba stuff was added recently but i did finish about half of the next show i am watchign which is very good and i should be able to finish the rest within the next few days, famous last words. ok but anyway there may be frogs in the house somewhere as frogs are always in the house!! so the genshin livestream has occured and oh boi is it a hype to want the next update to come soon as we get kazoohoo as one of the 5 stars which means i will be getting him, there is also a new 4 star on that banner that i will get along with him as a bonus and if i dont then i will be sure to wish until i get him, and if i get a klee so be it i can get another character i dont have. lets just hope i dont get a dupe standard banner 5 star again, but knowing my past luck i will be likely to get one (that is if i get another 5 star). see i will want to save up my genshin ruples for the update after this, the one in august, as that is speculated to be 3.0 which means new characters in the masses as that will be a major update that has been a year and coming. also the thing is at the later half of that update, really close to the end that is, there will be the aniverary stuff as that falls in september which means more stuff there as well and hopefully more quality genshin character themes. but back to the next update, 2.8, so if i am to get kazoohoo before i get any copies of heizou then i will do a bit of wishing on klees banner so if i do happen to get another 5 star whilst trying for heizou it will be a new character so i can only be missing 3 characters, yae miko, yelan, and kuki shinobu (who may be obtained). see shinobu is a 4 star and will be in the pool of possible characters in the banner so if i am "unlucky" i will get her and then i will only not have 2 or 3 characters (klee dependant). see klee is the character that has been out the longest who i have yet to get which may change as i do want to have every character at some point and i say that i will try to get characters on their re-runs if possible (no other good characters on the current banner or no upcoming quality characters). but klee is the exception as she doesnt seem to have much use to me, but maybe i will get a copy of klee. so now 3.0 should be releasing on aug 23, which annoyingly is the day after classes start back up so it will be a pain as i do not want to deal with both classes and 3.0 at the same time but that is how it will have to be i guess, but hopefully since it is the start of the week, i will not have much going on in terms of HW so i will have plenty of time to do the probable archon quests that get released, and the probable story quests that do as well. because i know for sure that 3.1 will be when the release the archon as that is how they tend to do it as 1.1 was zhongli, 2.1 was baal, and 3.1 should be kusalani (i think). venti is the exception as he was in 1.0 but the whole prologue was released when the game released so it doesnt matter that much with him. but the good thing about 3.0 is there should be new content and exploration to do, not that we havent had new exploration at all as we have gotten chasm and enkanomiya recently which were a good change of pace. i also have to continue my 100% clearing run which will require a day or two of full genshin focus, as i got enkanomiya/chasm basically complete except for a few things, but now i have to do all of mondstadt, liyue and inazuma, and i want to preferably be done with this before 3.0 which means i have until classes begin again, which if i carve out a week to do this, i should reliably get it done, even if it is an hour a night leading up to that week, it should be done in less time that i think. but then again there is a lot of map to clear and i have gotten only a smallish chunk of mondstadt done. especially the puzzles that i have to do, those will be the hardest to make sure i have completed, but i think with some determination i should be able to get this done. ok now we move on to the 3.0 stuff. so in 3.0 i assume we will get 3 sections of sumeru as we got 3 islands of inazuma when it released and hopefully the subsequent updates after will release some more sections until we reach the usual 6 parts per region. also i wonder what the conflict/enemy fatui will be in sumeru because all i know about it is that there is a semi-new archon who was only put into power in the last 500 years after the previous one died in the archon war. but stepping back to 2.8 we have a semi-rerun of the golden apple archapelego event in which we can go to the islands again which i am looking forward too. another thing that we will be getting in the next update is a diluc skin which is the first 5 star rated skin as the previous skins for 5 stars were only rated 4 stars. this being that it comes with new voice lines and new idle animations so it will hopefully be not much more higher in the genshin ruple price but we will see when the update gets released in about a week. the good thing is that on the day of the update and the day after the update there is nothing going on for me in the outside realm so i will be able to stay up extra in order to do more genshin stuffs which will be pretty cool and it will be likely after this baba update comes out as well as hank/adam will be back around that weekend before the update. july 7th and we have now achieved another small addition to the baba haiku stuff in which we will now have the ability to view purity score list of dates, which previously impossible to do because it would be too long is now going to work as the list is now paged. this means we have it sorted by number of haikus, then purity if haiku count is the same, and if purity is same then it is sorted based on date in where the newest dates fall first in the list. oh so idk where i was in shows last time but i have gotten through all of sabuki bisco and also finished all of the finest assassin which well that was both done in the same day which was a good day for watching shows, i think the next show i will watch may be a fun one but idk what to pick exactly, im sure it will be picked before i return here and maybe done before then but i do have to be on the outside tomorrow as i did today let today was shorter than normal as it was a slow day. but on genshin note i have done all of the hangout events and now i am ready for the new update to release in under a week, also tomorrow is SAO movie release but lets hope it is up somewhere with easy access as soon as possible because i have been looking forward to this for over 9 months now and probably even more since it was announced back sometime last year. i havent gotten much new SAO since pre-bleach era, but i did get a good dose of it when isaac 'watched' it, more like skimmed through it. convient timing that my music is playing the SAO section right now but that is not now when whomst ever is reading this if they are reading this is reading this at the time they are reading this by reading it. bikus. ok time to figure out the next show to watch but that may be difficult as i want to pick a short and quick one so i can watch SAO, love is war and spy x family later next week or this week. but i do have good choices lined up which is pretty cool but that just means indecistion which is great. baba update is coming soon which means that this message will be coming to a close and mayhaps it will be this weekend or sometime next week, all depends on hanks mood, schedule and when i am able to be here to help debug the update. thusly it will be a waiting game and i wonder how many patch updates will be need to be in place after this one as it will have the voice detection update which hopefully goes off without any issues. i will have a bunch of changes that i will need to test on production when it goes live but that is for future me to deal with and he will have to take all the pain. oh and maybe there will be a SAO/AoT explain here soon if i get the want to do it today or tomorrow when just sitting in voice. oh speaking of voice the boi has joined voice which means perhaps i will join too, well i did and now i am watching a v…

---
## [The-Black-Screen/MonkeStation](https://github.com/The-Black-Screen/MonkeStation)@[31c9d411a7...](https://github.com/The-Black-Screen/MonkeStation/commit/31c9d411a7b9e4f6ad66b930d535e24e5555bd06)
#### Friday 2022-08-19 19:40:58 by nednaZ

Dynamic Adjustments Part 2 (#627)

* Dynamic Changes II

Changes the intercept message to be more flavorful.

Clamps the threat level to between 75% player pop and 200% player pop.

Logs increases to Dynamic threat budget.

Slightly reduces the weight of latejoin traitors. (From 7 to 4)

Increases the Weight (2 to 4), decreases the Cost (40 to 20) and decreases Minimum Players (35 to 30) of Revolution Latejoins.

Restores Heretics to Latejoin and Roundstart.

Heretics now have a lower number of sacrifice objectives. (From 2-6 to 1-3)

Heretics now have a chance to get a Steal objective.

Dynamic Abductors may no longer get spawned  in solo by mistake.

Midround Traitor chance reduced. (From 7 to 5)
Midround Traitor cap reduced. (From player_count / 10 to player_count / 15)

Midround Wizard weight increased (From 1 to 3)
Midround Wizards are now a HIGH_IMPACT_RULESET and will not repeat.

Midround Nuclear Operative Weight reduced. (From 5 to 4)

Blob Weight (4 to 3) and Cost (10 to 25) changed.

Xenomorph Cost increased (10 to 25)

Nightmare Cost increased (10 to 15)

Abductor Cost increased (10 to 15)

Space Pirates added to Dynamic.

Space Pirates have been given an update, with ship names and support for multiple types of pirates existing.

Revenant added to Dynamic.

Obsessed added to Dynamic.

Space Dragon early start changed to 40 minutes (From 50 minutes)

Roundstart Traitor cost increased (7 to 8)

Blood Brother Weight (4 to 2), Cost(15 to 13) and Scaling Cost(15 to 13) adjusted.

Changeling Weight(3 to 4) and Cost(15 to 17) adjusted.

Roundstart Wizard Weight(2 to 5) and Cost(40 to 30) adjusted.

Blood and Clock Cult Weight and Cost(30 to 25) adjusted.

Nuclear Operatives Weight(3 to 4) and Cost(50 to 25) adjusted.

* lone op

why didn't this commit

* Reverts max_traitors change

The maximum number of traitors is now player_count / 10 rather than 15

* Revolution Tweaks

Reduces the weight of latejoin revs from 4 to 2.

Increases the minimum number of required enemies from 2-0 to 5.

Changes the required enemies to be only security and the captain, AI and Cyborg are not counted.

The shuttle is no longer automatically called upon a Revolution victory.

There will be an announcement made after either 30% of the station is converted into revolutionaries OR if two heads of staff are killed.

* Pirate Fixes

Pirates now function as intended in Dynamic.

Pirates have a 25 player minimum to be called as antagonists.

Pirates have a minimum of 2 enemies before they can be called.

* Faster than opening VSC.

---
## [JuliaPackaging/BinaryBuilderBase.jl](https://github.com/JuliaPackaging/BinaryBuilderBase.jl)@[cf90fb4377...](https://github.com/JuliaPackaging/BinaryBuilderBase.jl/commit/cf90fb437738ecc8495b9ac150c7e8436f3110e2)
#### Friday 2022-08-19 20:29:18 by Keno Fischer

Add support for building sanitizer-enabled jlls

This adds support for automatically adding the appropriate `-fsanitize=`
flags when the platform includes a `sanitizer` tag. This is particularly
intended for msan, which requires that all .so's in the system are built
using it, but could be useful for other sanitizers also.

There's a couple annoyances. One is that we don't currently actually ship
the sanitizer runtime libraries in our rootfs. Thus, if we want to start
using this, we'd have to add a BuildDependency on LLVMCompilerRT_jll and
manually copy the runtime libraries into place. Not the end of the world,
but certainly a wart.

The other issue is that `platform_matches` (which is defined in Base) of
course currently ignores the `sanitizer` tag. In theory it is possible
to add a custom compare strategy, but since we're specifying the target
by triplet, we can't really add that. Easy enough to add manually here,
but does make me wonder whether the custom compare strategies in Base
actually fit the use case.

---
## [Misavius/Stock](https://github.com/Misavius/Stock)@[4c980b2238...](https://github.com/Misavius/Stock/commit/4c980b223877892aa448ae2e9ca10a98e14e8ae8)
#### Friday 2022-08-19 20:33:06 by Spencer

got the 2d classifiers works, make nn launch in new child process to actually fucking free the god-damn memory unlike that wretch tensorflow can do normally, added more models to the model_repository

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[497b91fb91...](https://github.com/Zeodexic/tsorcRevamp/commit/497b91fb91317eb98fbc819ec0645b15910d553d)
#### Friday 2022-08-19 21:10:37 by timhjersted

Phoenix Trio Revamp 1.0 + more

- The Phoenix bosses now have several new attack elements, some of which activate during a new 2nd phase at half health
-Corrupted Jellyfish renamed Obsidian Jellyfish and given wider spawn pool and HM stats, enabling potential interesting gameplay interactions with the map, (intentionally getting hit can give 30s of lava immunity), to go with the obsidian theme, they also have 999 defense requiring 5 or 10 hits to kill
-Created new banner placeholder sprite
-Added "Cracked Dragon Stone" which provides early HM access to On Fire! immunity, which will be useful during The Rage fight (can be crafted from Cobalt Bars or drops from Ancient Demon event as an expert drop)
-Bloodred Moss Clump now heals for 30HP, up from 20
-Ancient Demon now has a boss bag
-Ancient Demon and Oolicile Demon have better boss bag sprites
-Pwnhammer removed as a Wall of Flesh drop, WoF now drops Molten Pickaxe, which is also now used to craft Mjolnir
-Nerfed Corrupted Tooth healing, now has a 1/20 chance when attacking corrupted enemies, 1/10 chance for anything else
-Basilisk walkers and shifters as well as the Dworc family now has a chance to drop Bloodred Moss Clump
-Mutant Toads can now swim in water and have HM stats, plus 2s of Venom debuff in HM
-EoW and Golem damage stats bumped again slightly
-Cursed Dragon's Breath and Frozen Dragon's Breath now activate their most brutal debuffs after The Hunter and The Sorrow have been defeated
-Frozen Dragon's Breath adds 3s of Frostburn
-Enemy Black Fire kill sound changed
-Added Ice Spirit projectile which has a homing effect
-The Hunter's Miracle Sprouter/Vines emit more light for visibility
-Worm Food and Pwnhammer blocked via no drop/craft list

---
## [Claymore77/docs](https://github.com/Claymore77/docs)@[6897b8dbe7...](https://github.com/Claymore77/docs/commit/6897b8dbe79253b58a504f1f9424e5b3c7c769cb)
#### Friday 2022-08-19 21:15:17 by Claymore77

Master
(doc) Fix troubleshooting typos

<!--
BEFORE YOU CREATE A PULL REQUEST:

Ensure you have read over [CONTRIBUTING.md](./CONTRIBUTING.md). We provide VERY defined guidance (as such, we strongly adhere to it).

A summary of our expectations:
 - You are not submitting a pull request from your MASTER / MAIN branch.
 - YOUR GIT COMMIT MESSAGE FORMAT IS EXTREMELY IMPORTANT. We have a very defined expectation for this format and are sticklers about it. Really, READ the entire Contributing document. It will save you and us pain.
 - Do not reformat code, it makes it hard to see what has changed. Leave the formatting to us.

THANKS! We appreciate you reading the entire Contributing document and not just scanning through it.

Name your issue appropriately: give it a sentence that reads well enough for anyone seeing this in release notes to know what the issue is.

When writing out the pull request details please ensure you are writing it as
if you were explaining it to somebody else.
Even if you will be working on and resolving the issue yourself.
This helps others to understand the reasons for the pull request and for it to be searchable in future.

Please do not remove any of the headings.
If a heading is not applicable then enter N/A: Why it's not applicable

Make sure you have raised an issue for this pull request before continuing.

Please remove all comments before submitting.
-->

## Description Of Changes
<!-- Enter a description of the pull request changes -->

## Motivation and Context
<!-- Why is this change necessary and under what context is it being done -->

## Testing

* [ ] I have previewed these changes using the [Docker Container](https://github.com/chocolatey/docs/tree/master/.devcontainer) or another method before submitting this pull request.

## Change Types Made
<!-- Tick the boxes for the type of changes that have been made -->

* [ ] Minor documentation fix (typos etc.).
* [ ] Major documentation change (refactoring, reformatting or adding documentation to existing page).
* [ ] New documentation page added.
* [ ] The change I have made should have a video added, and I have raised an issue for this.
    * Issue #

## Change Checklist

* [ ] Requires a change to menu structure (top or left hand side)/
* [ ] Menu structure has been updated

## Related Issue
<!-- Make sure you have raised an issue for this pull request before continuing. -->

Fixes #

<!-- PLEASE REMOVE ALL COMMENTS BEFORE SUBMITTING -->

---
## [drisspg/pytorch](https://github.com/drisspg/pytorch)@[4c8cfb57aa...](https://github.com/drisspg/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Friday 2022-08-19 21:47:24 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [BlackMajor/CHOMPStation2](https://github.com/BlackMajor/CHOMPStation2)@[4704df506b...](https://github.com/BlackMajor/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Friday 2022-08-19 21:53:06 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [ThakaRashard/BUBBLEGUMPOP_QUXUBE](https://github.com/ThakaRashard/BUBBLEGUMPOP_QUXUBE)@[507b53740e...](https://github.com/ThakaRashard/BUBBLEGUMPOP_QUXUBE/commit/507b53740eebff63ff9bb575ecca58e2c36cc624)
#### Friday 2022-08-19 22:25:43 by ThakaRashard


[Abandon Ship (feat. Rampage the Last Boy Scout)](https://www.youtube.com/watch?v=pptLcLcRJz4)
[KRS-One - A Friend (Official Video)](https://www.youtube.com/watch?v=aj1Q7jDgrc4)
[H.I.P.H.O.P. · KRS-One I Got Next ℗ 1997 Zomba Recording LLC](https://youtu.be/MkWP0udk754)
[The Real Hip-Hop - Part II](https://youtu.be/ajwLy9BbFGA)
[KRS-One - MC's Act Like They Don't Know](https://www.youtube.com/watch?v=_J-h_8dwyiM)
[Lost Boyz - Lifestyles Of The Rich And Shameless](https://www.youtube.com/watch?v=0D-f01H6Kos)
[Beasts From The East · Lost Boyz Love, Peace & Nappiness ℗ 1997](https://www.youtube.com/watch?v=hJ5y0jKlLVc)
[Smif-N-Wessun - Sound Bwoy Bureill](https://www.youtube.com/watch?v=s5MogMGLWAA)
[Onyx - Last Dayz - All We Got Iz Us](https://www.youtube.com/watch?v=rlpxQ_moU9o)
[ONYX & Wu-Tang Clan - The Worst (Official Music Video)](https://www.youtube.com/watch?v=q1oa07Kw_RQ)
[Canibus, Heltah Skeltah & Ras Kass-Uni-4-orm (1997)](https://www.youtube.com/watch?v=JE2RAVLFknk)
[Redman - Creepin'](https://www.youtube.com/watch?v=HSc1BqDH9HI)
[Channel Live ft. KRS-One - Mad-Izm](https://www.youtube.com/watch?v=H3vs_lXebYc)
[Heltah Skeltah & OGC - Leflaur Leflah Eshkoshka](https://www.youtube.com/watch?v=i4sW3jJuVDg)
[Mad Lion - Take It Easy](https://www.youtube.com/watch?v=VSpNJrppImg)
[KRS-One - Step Into A World (Rapture's Delight)](https://www.youtube.com/watch?v=xbJxcFyaCpI)
[Common ft. Talib Kweli, Sadat X & DJ Hi-Tek - 1-9-9-9 (Official Video)](https://www.youtube.com/watch?v=dMIXAYBoGBM)
[Black Moon - Who Got Da Props](https://www.youtube.com/watch?v=58lZYDxHRV8)
[Black Moon - How Many MC's...](https://www.youtube.com/watch?v=_-eVgV4PzX8)
[Artifacts - Wrong Side Of Da Tracks](https://www.youtube.com/watch?v=GM92f-BUoow)
[Meyhem Lauren - 'Got The Fever' NYC Graffiti New York City](https://www.youtube.com/watch?v=gg5cJu1Zcws)
[KRS ONE - OUT FOR FAME (Rubens Video).wmv](https://www.youtube.com/watch?v=jhurGs6WBCw)
[Seen, Can2, Cope2 & Zebster - Wallstreet Graffiti Meeting](https://www.youtube.com/watch?v=vVr296bJj2E)
[Artifacts - Art of Graff](https://www.youtube.com/watch?v=Tn30EIvTKd4)
[Artifacts - Art Of Facts (Jam-A-Holics Remix)](https://www.youtube.com/watch?v=3F7xEjfPHjA)
[Artifacts - The Ultimate [Explicit]](https://www.youtube.com/watch?v=3WAq-n3qMpc)
[Artifacts - C'mon Wit Da Git Down (Official Video) [Explicit]](https://www.youtube.com/watch?v=XimyEvDJWzA)
[Digable Planets - 9th Wonder (Blackitolism)](https://www.youtube.com/watch?v=SyeI43BeR54)
[Special Ed - I Got It Made (Official Video)](https://www.youtube.com/watch?v=N_9GuiE5Fck)
[‘FX CREW’ (Graffiti Writers Crew) New York, 1998 [RARE full graff art VHS documentary archive]](https://www.youtube.com/watch?v=Jv7ECeiD1p4)

---
## [dmarra/UnityReflectionExample](https://github.com/dmarra/UnityReflectionExample)@[1f35bfa7e9...](https://github.com/dmarra/UnityReflectionExample/commit/1f35bfa7e9d89ec0e710cbcc188f90d707131026)
#### Friday 2022-08-19 23:13:52 by Dan Marra

chore: Reorganizes project layout

The project layout was very... flat. Most files for the project were just
slopped into `Assets`, without any subdivision. While this is a tiny demo
project, it bothered me that everything was just plopped into that one
space.

We now have materials _actually_ in the Materials folder! I also moved
textures to Textures, and moved all code to the Src folder.

The main scene is still in Assets. There are no plans for an additional
scene for this project, so there is really no need to make a separate
folder for it (can always be done later if we find the need).

One thing that is kind of hanging out is the "shittycamera" asset. If I
remember correctly, this was supposed to be a very basic model of a
camera to show where it is in the scene view. Upon loading this project
in a more modern version of unity, it seems this model is no longer
loading correctly. It could be the modern version, or it could be that
I made a mistake when adding it to the repo originally, which corrupted
it. This will be fixed in a followup commit.

---

