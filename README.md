## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-19](docs/good-messages/2022/2022-07-19.md)


1,855,913 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,855,913 were push events containing 2,791,302 commit messages that amount to 206,758,983 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tigerRyi/SecondHand](https://github.com/tigerRyi/SecondHand)@[1828111c3e...](https://github.com/tigerRyi/SecondHand/commit/1828111c3e23a2fb450ac0730da6b98625b4f953)
#### Tuesday 2022-07-19 00:08:23 by Jesse0x

I'm so sorry to hear that u want to give up... Here, I'll fix for you... But I really don't want to see u give up, cuz your logic and math and other are much better than me.. For real, during the ap practice, I could see it clearly. I could see one more important thing, which is you are careful... It is a very important thing to have. And I don't have that, the only thing u need is experience, SO I REALLY DON'T WANT TO SEE U GIVE UP ... (PS: if I want to encurage him, I shouldn't help him fix this right? an moral issue forever XD)

---
## [mafemergency/Paradise](https://github.com/mafemergency/Paradise)@[6082c95eb3...](https://github.com/mafemergency/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Tuesday 2022-07-19 00:35:23 by LightFire53

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
## [coreyja/battlesnake-rs](https://github.com/coreyja/battlesnake-rs)@[1d5dff768c...](https://github.com/coreyja/battlesnake-rs/commit/1d5dff768c7ba623fa0e3e6b1ac17aa5a6fcf893)
#### Tuesday 2022-07-19 00:52:44 by Corey Alexander

Merge branch 'main' into ca/main/scorable

* main:
  Allow sherlock to be used for early eliminations
  Try without the circleci cache
  Mess up the public interface for minimax to have things return the depth we got to better. Need to fold that into the Result type I think.
  Restructure the benchmark a bit, starting to see patterns with the fixture files
  Oh shit, no wonder the benchmarks looked like the start of game metrics :facepalm:
  Report a different span name for when we don't have an exploration thread
  Add a new benchmark function for Hobbs. Its a later game arcade maze map

# Conflicts:
#	battlesnake-minimax/src/paranoid/eval.rs

---
## [Urban-Coalition/ArcCW_UC_Common](https://github.com/Urban-Coalition/ArcCW_UC_Common)@[3e699a0338...](https://github.com/Urban-Coalition/ArcCW_UC_Common/commit/3e699a03387741c916a0324e6575c59bf9207327)
#### Tuesday 2022-07-19 03:22:36 by Fesiug

Usable version of the UBGL

reminds me how much ArcCW's UBGLs FUCKING SUCK AND BLOW AND SHIT AND FUCKING SUCKC OMPLET E FUCKING ASS FUCK

---
## [lranjbar/assisted-service](https://github.com/lranjbar/assisted-service)@[564650feca...](https://github.com/lranjbar/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Tuesday 2022-07-19 03:42:19 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition (#4072)

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [MbrllaHacks/Website](https://github.com/MbrllaHacks/Website)@[98fbe637bf...](https://github.com/MbrllaHacks/Website/commit/98fbe637bf61489f2f5b1236fe9b74e01f998077)
#### Tuesday 2022-07-19 04:23:01 by Hiten1708

In the Name and by the power of Our Lord Jesus Christ, + may you be snatched away and driven from the Church of God and from the souls made to the image and likeness of God and redeemed by the Precious Blood of the Divine Lamb.

---
## [MenacingManatee/Yogstation-2](https://github.com/MenacingManatee/Yogstation-2)@[c3e823d052...](https://github.com/MenacingManatee/Yogstation-2/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Tuesday 2022-07-19 06:46:29 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---
## [MenacingManatee/Yogstation-2](https://github.com/MenacingManatee/Yogstation-2)@[8b77243ce9...](https://github.com/MenacingManatee/Yogstation-2/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Tuesday 2022-07-19 06:46:29 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [niftynei/lightning](https://github.com/niftynei/lightning)@[c0cd87fbfe...](https://github.com/niftynei/lightning/commit/c0cd87fbfe6e87c7c67b94b9da5897fe69eb5416)
#### Tuesday 2022-07-19 07:35:10 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [kavishinsa/realestatehub](https://github.com/kavishinsa/realestatehub)@[35a9a559cd...](https://github.com/kavishinsa/realestatehub/commit/35a9a559cd6220d6a5c5a1d2648a83b3a9050490)
#### Tuesday 2022-07-19 07:53:28 by kavishinsa

Sobha Highland Hosur Road Bengaluru


Sobha Highland is a new launch residential project that offers premium 2, 3 & 4 BHK apartments designed with modern amenities and facilities by Sobha Limited. The project well located at Hosur Road, Bangalore.
Where discussion starts with innovation as needed and wraps up on the way of thinking. A genuine nature-wrapped objective where you can go for a stroll in the recreation time along the tree-adjusted roads, and taste your espresso while partaking in the new inhale of air. Partake in your quiet mornings and brilliant nights in the wonderfully created homes.
At Sobha Highland Hosur Road, The smart life is prepared to welcome you from where you can work, appreciate, party, and live without limit. A day-to-day existence that is combined with brilliant homes, shrewd elements, and savvies you. The delighted minutes that are included in the books of recollections can now be made here with friends and family.
Amazing homes have the ideal sceneries thus as this undertaking. The perspectives on outlandish scenes, cutting-edge clubhouse, and perfectly thought Courtyards and Activity Terraces are some of the numerous extra benefits.

At Sobha Highland Bangalore, These exquisite habitations are similarly smart as they are furnished with brilliant living elements that offer application-based administrations for the local area. The administrations like e-notice board and booking the executives for clubhouse facilities can be appreciated here.

Click here to know more : https://www.sobhalimited.in/bangalore/sobha-highland-hosur/

---
## [TDKorn/insta-tweet](https://github.com/TDKorn/insta-tweet)@[9c0920cf80...](https://github.com/TDKorn/insta-tweet/commit/9c0920cf806b195d1cf8a0cbc3c4c4f9e8b3f9d8)
#### Tuesday 2022-07-19 08:17:37 by TDKorn

merge db-and-profiles

Squashed commit of the following:
commit ff4819d52a1b1bd77914870e11ffe5b5ada57eea
Author: TDKorn <96394652+TDKorn@users.noreply.github.com>
Date:   Tue Jul 19 03:02:24 2022 -0400

    Add docstrings from `sphinx` branch

    and maybe a lil extra from here 😩😎

    Squashed commit of the following:
    commit 64aa0ed09437977feaad419a5a27b661813b90ce
    Author: TDKorn <96394652+TDKorn@users.noreply.github.com>
    Date: Sun Jul 17 21:47:56 2022 -0400

    Update instatweet.py

    commit 2e86bcf9ff1d262f9ac43ca54689f338de32bee3
    Author: TDKorn <96394652+TDKorn@users.noreply.github.com>
    Date: Fri Jul 15 14:21:19 2022 -0400

    Update InstaPost/InstaUser

    commit 2cb3f8691bfddf9792d5990f7546c865b476a20d
    Author: TDKorn <96394652+TDKorn@users.noreply.github.com>
    Date: Thu Jul 14 01:27:19 2022 -0400

    Fix more docstrings

    Update instaclient.py

    Update profile.py

    commit 91ce8af731e08dae9bde43dd726df3de325534d8
    Author: TDKorn <96394652+TDKorn@users.noreply.github.com>
    Date: Wed Jul 13 00:28:14 2022 -0400

    Docstring Fixes Jul 12 i ve had enough

commit 3b25ce30cf7480f9e1cb5d657d4175d8fb3eacbd
Author: TDKorn <96394652+TDKorn@users.noreply.github.com>
Date:   Tue Jul 19 01:22:05 2022 -0400

    Add `DOWNLOAD_DIR`  to `InstaClient` and more `InstaPost` properties

    Main Changes
     * `InstaClient.DOWNLOAD_DIR` is where IG posts will be downloaded to now, rather than nowhere in particular
        - When `InstaClient` downloads a post, it still sets the `filepath` attribute on the `InstaPost`

     * `InstaPost` has new properties
        - `filetype`: returns the filetype of the post (video/photo --> 'mp4'/'jpg')
        - `filename`: returns the default basename for the file (`id` + `filetype`)
        - `is_downloaded`: returns if the post has been downloaded yet; checks `filepath` attribute to see if a file exists

    ---

    General Issue
    * I'm struggling to decide if I want the InstaClient/Post to be functional as standalone classes or not

    * Take this commit itself as an example:
        - Felt illogical to "calculate" the download path within the `InstaClient`, considering the filename is an intrinsic property of an `InstaPost`
        - Making the `filepath` a property of InstaPost, rather an than attribute, would require a property setter
            > The filepath is used to determine if the post was downloaded successfully, ie. the `is_downloaded` property
            > So if passing a custom filepath to `InstaClient.download_post()`, it needs to be overriden on the `InstaPost` too
        - Feels excessive to doo all this for something that will NEVER happen WITHIN the package?
            > Like it'd only be a problem if the classes aren't used as intended (but do I really have an intention?? no... im not the InstaClient police or something... so...?)
        - Instead I kept it as an attribute, added `filename` to help construct almost all of the filepath, but still... it feels wrong to make it harder to customize

    * Note that this commit replaced commit ea1918b7431d05379331409a8db40392f60d8491
        - In that commit, there's an option to specify a download directory and override the InstaClient one
        - But what if you want a custom file name? How much customization ability am I supposed to provide? Like UGHHHHHHHHHHHHHHH 🤮🤮🤮🤮
        - god knew I'd be too powerful if I didn't have crippling ADHD paralysis 😞✊

---
## [xhevfx/postgres](https://github.com/xhevfx/postgres)@[c40ba5f318...](https://github.com/xhevfx/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Tuesday 2022-07-19 08:48:24 by Tom Lane

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[2853619772...](https://github.com/Buildstarted/linksfordevs/commit/2853619772747c833c46653cb8060a19f5027a61)
#### Tuesday 2022-07-19 09:05:09 by Ben Dornis

Updating: 7/19/2022 9:00:00 AM

 1. Added: My Poor Experience With Azure (or why I'm sticking with AWS)
    (https://new.pythonforengineers.com/blog/my-poor-experience-with-azure-or-why-im-sticking-with-aws/)
 2. Added: Python Hidden Hacks You Probably Don’t Know About
    (https://rubikscode.net/2022/07/19/python-hidden-hacks-you-probably-dont-know-about/)
 3. Added: Base64 Encode and Decode in C# - Code Maze
    (https://code-maze.com/base64-encode-decode-csharp/)
 4. Added: elmah.io launches two GitHub Actions in the GitHub Marketplace
    (https://blog.elmah.io/elmah-io-launches-two-github-actions-in-the-github-marketplace/)

Generation took: 00:05:00.3883393

---
## [tschwinge/gcc](https://github.com/tschwinge/gcc)@[5493ee7145...](https://github.com/tschwinge/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Tuesday 2022-07-19 09:28:39 by Alexandre Oliva

i386 testsuite: cope with --enable-default-pie

Running the testsuite on a toolchain build with --enable-default-pie
had some unexpected fails.  Adjust the tests to tolerate the effects
of this configuration option on x86_64-linux-gnu and i686-linux-gnu.

The cet-sjlj* tests get offsets before the base symbol name with PIC
or PIE.  A single pattern covering both alternatives somehow triggered
two matches rather than the single expected match, thus my narrowing
the '.*' to not skip line breaks, but that was not enough.  Still
puzzled, I separated the patterns into nonpic and !nonpic, and we get
the expected matchcounts this way.

Tests for -mfentry require an mfentry effective target, which excludes
32-bit x86 with PIC or PIE enabled, that's why the patterns that
accept the PIC sym@RELOC annotations only cover x86_64.  mvc7 is
getting regexps extended to cover PIC reloc annotatios and all of the
named variants, and tightened to avoid unexpected '.' matches.

The pr24414 test stores in an unadorned named variable in an old-style
asm statement, to check that such asm statements get an implicit
memory clobber.  Rewriting the asm into a GCC extended asm with the
variable as an output would remove the regression it checks against.
Problem is, the literal reference to the variable is not PIC, so it's
rejected by the elf64 linker with an error, and flagged with a warning
by the elf32 one.  We could presumably make the variable references
PIC-friendly with #ifdefs, but I doubt that's worth the trouble.  I'm
just arranging for the test to be skipped if PIC or PIE are enabled by
default.


for  gcc/testsuite/ChangeLog

	* gcc.target/i386/cet-sjlj-6a.c: Cope with --enable-default-pie.
	* gcc.target/i386/cet-sjlj-6b.c: Likewise.
	* gcc.target/i386/fentryname3.c: Likewise.
	* gcc.target/i386/mvc7.c: Likewise.
	* gcc.target/i386/pr24414.c: Likewise.
	* gcc.target/i386/pr93492-3.c: Likewise.
	* gcc.target/i386/pr93492-5.c: Likewise.
	* gcc.target/i386/pr98482-1.c: Likewise.

---
## [SofiWesson/CyberSlimeEndlessRunner](https://github.com/SofiWesson/CyberSlimeEndlessRunner)@[a4edfd44ab...](https://github.com/SofiWesson/CyberSlimeEndlessRunner/commit/a4edfd44ab2db1cf339d28b46593153ee4726828)
#### Tuesday 2022-07-19 09:53:47 by MayKovacs

Implemented Timer to Main Scene

I don't know why I've been such a stupid idiot making the timer. It literally took me like 10 minutes at home and I couldn't get it working for like several days on my last project and said "screw it" and make a hacky workaround that would probably make a programmer hunt me down and brutally murder me if they ever saw it. It's a god damn timer, why the hell was it so hard?

---
## [scrtlabs/SecretNetwork](https://github.com/scrtlabs/SecretNetwork)@[a8ffddebfe...](https://github.com/scrtlabs/SecretNetwork/commit/a8ffddebfe95cb7bad51eb0ecdcdcd7108319d1c)
#### Tuesday 2022-07-19 09:58:00 by Cashmaney

Setting up gitpod username with proper permissions on github

Also, fuck you wavy lines logo

---
## [richardcase/cluster-api-provider-aws](https://github.com/richardcase/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/richardcase/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Tuesday 2022-07-19 10:19:37 by Claudia Beresford

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
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[36fa73136e...](https://github.com/payday-restoration/restoration-mod/commit/36fa73136e99a2ee01878e459b648f0d55507393)
#### Tuesday 2022-07-19 10:52:17 by SonicSoapyBoi

RAGE! OH MY FUCKING GOD! I HATE WHEN THIS HAPPENS AAAAAAAAAAAAAA

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b181cf6353...](https://github.com/mrakgr/The-Spiral-Language/commit/b181cf6353cd33bc2231044d624917cf3bb1d3ec)
#### Tuesday 2022-07-19 11:00:30 by Marko Grdinić

"5:50am. Yesterday I went to bed at 9pm after watching Dave talk for almost 3h. I did not get enough sleep and I was just so tired that I did not feel like playing BG2. I am not sure how fast I fell asleep, but I do feel a lot more rested than I was yesterday. I am a bit groggy right now, but not fatigued in the way I was yesterday. Any mail? A bunch of them.

2 accept, 1 reject. Plus the GI HR drone is pestering me to grab a slot. Ignore that. Now what is my tally?

> That is 3 accepts so far, out of 9 companies that I've applied to. Not bad.
> I got 2 rejects, but only one is by a HR bot like now. The other one is because I was not a good fit for the Haskell guys.

Adding what I have now from yesterday based on the quotes, that puts me at 5 accepts, 3 rejects. Even if I get a reject at that last company, this is a good enough signal that I have a >50% hit rate with my current resume. There is no need to improve on it further, that is what I am sure.

It is interesting that I got a reject from that streaming media engineer position. Maybe they are looking for somebody whose resume is less of a generalist? Maybe they already filled it? Who can know. If I was applying to places such as those, I'd probably fill the job descriptions with video compression and streaming stuff. If I did that, I probably would have gotten through the first stage. But I do not resent this reject particularly, media streaming and compression is not my field. I don't have an interest in it. If I was really interested in it, I'd be studying the subject now instead of revisiting webdev.

More than just the hit rate, the accepts and rejects are sensible now.

6:05am. Whether I get a job or not with the current batch does not matter, with this resume I'll be sure to get plenty of interviewing experience which will serve me well in cracking the game. If you have a <10% hit rate, every single interview is precious and you can't afford to loose it easily, but with a high hit rate, job offers are literally everywhere. I sure would not want to have something like a 1% hit rate. Those guys would need to accept literally anything and as a consequence have zero room to negotiate a high salary. I am in a strong position here.

I am going to ignore the current crop of applications until I am ready. It is fine if they run out. I can just apply again to different places.

6:10am. Now...what do I want to do right now. I want to start my studies.

I think I can gain something from this experience. I can internalize the correct attitude to use big frameworks like ASP.NET to which I am alergic to.

6:15am. In 2020 I feel like my learning attempt on ASP.NET crashed and burned, instead I really benefited from studying Rx and Hopac instead. This is because they really get to the crux of what concurrent programming is really about. They solve some pressing issues and give me capabilities that I did not have before. They greatly deepened my concurrency capabilities.

If I try to approach ASP.NET with the same attitude of wanting to grasp deep capability, of course I am bound to be disappointed.

But now I am mature enough to understand something. Imagine I was donig a cloud app. I certainly would not rail against the limits and stress due to not understanding how data is sent through the data centers. That sort of thing is not my responsibility.

The same goes with ASP.NET.

Those app tutorials that I saw yesterday were actually pretty shallow. The way to use big frameworks like these is to not worry about their design too much and just place your hooks where they need to be. If need be, I can use Rx or Hopac alongside them if I need greater capability.

I can easily manage this sort of goal.

So let me clear it.

6:25am. Let me just finish chilling. After that.

https://www.youtube.com/results?search_query=scalable+application

https://www.youtube.com/playlist?list=PLm556dMNleHc1MWN5BX9B2XkwkNE2Djiu
Computer Networking: A Top-Down Approach

Let's forget ASP.NET for today.

https://www.youtube.com/watch?v=a2rcgzludDU
How to Scale an Application? | System Design

https://youtu.be/a2rcgzludDU?t=182

This is actually fairly interesting. It is a good intro why you need backups and logs.

https://youtu.be/a2rcgzludDU?t=205

Here he mentions autorestarts. Spiral's lang server sometimes goes down for uknown reasons. It might be good to implement something for when that happens. I'll keep the word in mind.

https://youtu.be/a2rcgzludDU?t=362

I never knew what Redis was, but based on this, I guess it is a cache. I thought it might have been a database, but it seems I was wrong.

https://youtu.be/a2rcgzludDU?t=380

This is an interesting story. If I ever do a non-toy web app, I'll be keeping all of this in mind.

https://youtu.be/a2rcgzludDU?t=458

Database splitting. So that is a thing.

6:50am. Read the Kaiji chapter. Let me go for one more video.

https://www.youtube.com/playlist?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI
Web Development

This is a course from 7 years ago. I won't go for it right now, I am not interested in becoming a full time webdev.

https://www.youtube.com/watch?v=yPF94QiI2qk
How I scaled a website to 10 million users (web-servers & databases, high load, and performance)

https://youtu.be/6pjGuuGsqxE
Architecting Large Scale Systems | Creating Scalable Web Application Architecture

Let me watch these in order and then I'll be done with this. I'll move on to ASP.NET after that.

https://youtu.be/yPF94QiI2qk?t=158
> You generally want the user to stay on a single server.

He did mention at the start that he did not do it correctly and I see why. It is actually a natural urge to try to keep user state, but it would make things a lot more difficult. ZeroMQ explicitly does not do this.

If I had to do it, I'd have the frontend transmit all the necessary data so the backend can remain stateless. In fact offloading as much processing as possible to the user and keeping the backend simple would be a great way to keep down the costs.

Even so, saying this is making me realize that I am missing some foundational knowledge such as how the connections are encrypted and such.

https://youtu.be/yPF94QiI2qk?t=484

So far what he is talking about is similar to how it was in the previous video. I should note that all this seems like an incredible pain to do compared to using the cloud. I can see why webdevs have such high salaries. Programming wise, it is not too strenuous, but it does require a lot of management.

https://youtu.be/yPF94QiI2qk?t=607

He is talking about making slave servers that only do reads.

https://youtu.be/yPF94QiI2qk?t=651
> You take the user id, mod it by 10, and depending on that send it to one of the 10 database servers.

Yeah, this is one way of doing it!

https://youtu.be/yPF94QiI2qk?t=690

Towards the end he summarizes it.

7:20am. Right now I am reading the comments.

> This is one of TechLead's best videos imo. I've done a bunch of server setups and full stack development and half of the stuff he mentioned never occured to me, like splitting users between databases based on a master user table. That being said I still think a load balancer is a good idea as it ultimately saves you time. Also Firebase or AWS is really a huge time saver, even if it does cost a bit more. For me personally the hours I spend trying to get all the configs and scripts right on a linux server and complaining all the dependencies from source with all the correct configs ends up taking so much extra time that the the price I spend on FIrebase or AWS is worth it. That being said if you want to go the configure it yourself route, this video is a treasure trove of really good ideas.

It is decided, if I want webdev jobs, I'll just learn how to do it with AWS. The troublesome part of it is scaling anyway, and who wants to manage his own servers? It is not like they are my own brains.

https://youtu.be/6pjGuuGsqxE
Architecting Large Scale Systems | Creating Scalable Web Application Architecture

Let me also watch this.

https://youtu.be/NMuL6xOY1Ro?t=41
> (Runs his hand through his hair) For those of you who are new to this channel, I wanted to briefly introduce myself. I am an ex-Google tech lead...which is amazing! Absolutely magnificent! (Sips drink) So good! It is something to keep in mind as you are watching my videos, why should you listen to me, where is my authority coming from, why do you need to respect me? Simple. I am the tech lead.

> And that is something that you couldn't say about anybody else that you know.

Kek. This was pretty funny.

The video was a bit interesting as it assumes that it more beneficial to carve out ownership than to get the job done in a timely manner. Honestly, I'd be more interested in just getting it done and moving on to the next thing rather than becoming a maintainer. Is job safety really that important when the jobs pay so well that you can retire after a few years of work? Probably not. A programmer should be trying to shake things up. Those 50k lines of crap SQL he talked about might be 50k lines of job safety, but work is not worth it unless you are an entrepreneur.

7:40am. https://youtu.be/6pjGuuGsqxE
Architecting Large Scale Systems | Creating Scalable Web Application Architecture

Let me get started on this.

https://youtu.be/6pjGuuGsqxE?t=558

He talks about event sourcing. It seems to be a pattern where you keep the message trail and this allows you to arrive on the latest state in an immutable fashion.

https://youtu.be/6pjGuuGsqxE?t=608

Nevermind this. I can't listen to 30m of it. I am done with these kinds of tutorials.

https://youtu.be/YkGHxOg9d3M
System design interview: Scale to 1 million users

Let me just go for this. I want to see if it has some insights. The previous video was pretty useless.

7:50am. This video seems to be on point. So far the best one was the one I watched yesterday which gave me some good insight.

8:05am. Let me take a short break here.

8:15am. Let me resume. I think it is a way forward that I am taking interest in these issues to begin with.

https://youtu.be/YkGHxOg9d3M?t=321

If I was applying to a senior webdev position, this would be difficult for me. I don't know what the tradeoffs between different databases are.

https://youtu.be/YkGHxOg9d3M?t=449

He mentions having different videos where he talks about these systems at a high level. I am not going to go for them as I am not aiming for webdev positions, but this first video will be useful to me.

To really internalize that kind of material, hands on exp would be needed anyway. Plus, I'd go for cloud jobs in that area even if I was aiming for them, so I do not need as much expertise in this like a standalone dev would.

https://youtu.be/YkGHxOg9d3M?t=466

Here he mentions practice.

8:35am. https://youtu.be/YkGHxOg9d3M?t=796
> Web socket that could stream video back to the user.

I honestly have no idea whow video streaming works. Well, you'd still use messages, but otherwise split the video into chunks of them. So I guess it would not be too big of a deal.

https://youtu.be/YkGHxOg9d3M?t=950
> It can be really easy to lock yourself into a single instance where horizontal scaling is challenging.

I've had to design Spiral v2 so it can be used as a service. The old version design would not have worked.

8:45am. https://youtu.be/YkGHxOg9d3M?t=1094

Load balancing the databases. That might be an option. I'd need to think about how database replication works.

https://youtu.be/YkGHxOg9d3M?t=1216

At this stage he is talking about stateless servers.

It seems that load balancing the databases is to increase their durability, while for the servers it is to increase the overall system capacity to handle users.

https://youtu.be/YkGHxOg9d3M?t=1271
> And this is really something that, modern application stacks like Kubernetes give us. It is the ability to easily scale up and scale down as needed, but your server application logic has to be stateless. So we can offload that state to databases and the database system down here.

> So now we can scale our server stack to infinity.

8:50am. https://youtu.be/YkGHxOg9d3M?t=1375

He mentions that CDNs are extremely expensive. He mentions that I need a fallback as CDNs even from Google Cloud or AWS can fail.

https://youtu.be/qjsuOUXxD64?list=PLAWxBXefx3-nXeXrv9yX8cKn57Spf3VTr
System design interview: Database Scaling

I won't watch this, it is not important right now. I'll definitely keep it in mind.

John Codes is really good though. That System Design interview was the best of the bunch. If I had to recommend a single video out of the bunch I'd pick it. It is quite thorough.

9:05am. At this point in the day, usually I'd not have even started, but now I've already put in 3h. Not bad.

9:10am. A short break is in order here.

I am thinking what to do next and am leaning towards finally giving ASP.NET a try. Frontend, backend, database. I'll do an app that has all 3 elements After I do I'll have basic webdev knowledge. Once I break the ice on that, I'd be able to make really rapid progress thanks to my existing foundation in concurrency.

Ohhhh...I forgot!

https://www.youtube.com/playlist?list=PLm556dMNleHc1MWN5BX9B2XkwkNE2Djiu
Computer Networking: A Top-Down Approach

I meant to also watch some of this first before I got started on ASP.NET.

9:15am. Ok, let me get this course out of the way. I am in the mood for it. It is not like I'd gain anything specific for doing the ASP.NET app, I am just trying to spend time in least useless way until I get access to AWS.

9:20am. Before I dive in, let me note down the video times.

13+16+19+14+10+6+12+25+18+10+19+8+17+21+9+14+12+17+24+11+14+12+15+23+6+1+16+15+22+30+21+11+12+7+20+11+18+14+14+5+11+9+28+17+13+12+5+6+7+15+11+14=730

This comes up to 12h.

9:25am. You know what, since I do not feel like watching lectures for the next 12h, and want to do programming as slight as it is instead, I am going to do the ASP.NET app. It won't take me long, after I am done, I'll spread the above course over a few days.

https://youtu.be/74sEFYBBRAY?list=PLm556dMNleHc1MWN5BX9B2XkwkNE2Djiu
1.1 Introduction (reposted) - What is the Internet

Let me just finish the intro at least, that won't cost me much.

https://www.youtube.com/results?search_query=asp.net

Oh, compared to when I looked at it last, this search has new things on it. For one, it has a course for .NET 6. Good thing I installed VS 2022.

https://youtu.be/hZ1DASYd9rk
Learn ASP.NET Core MVC (.NET 6) - Full Course

It is 3h, which is just the right amount of time that I want to spend on this. Let me take a short break. It will be a bit of watching, a bit of doing, and by the end of it, I'll know how to do webapps. I already know how to scale them, so I just need to deal with the more fundamental parts.

Things like load balancing and distributing I already know from my foray into ZeroMQ. The ZeroMQ docs are a really good intro to concurrency.

10am. Let me resume. I'll follow this one as it goes along.

https://youtu.be/hZ1DASYd9rk?t=62

Courses like these won't make you good at programming, but they are useful for getting you started and familiarized with a new field. They can get you to the point where you can continue exploring on your own.

https://youtu.be/hZ1DASYd9rk?t=126
> And lastly we will deploy our application to Azure.

10:05am. I thought I got rid of all of them, but it seems that I have SQL Server 2019.

I really have a ton of them. What is SSMS?

https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16

650mb. Well it is a pittance in this day and age. It will be done before I know it.

My desktop PC is really not suitable to be a database server though. At most I can use it to learn.

https://youtu.be/hZ1DASYd9rk?t=400
> Also .NET Core was built with the cloud in mind.

10:20am. Right now I've started reading HN comments dumping on Azure. Forget that. Let me get back to the course.

https://youtu.be/hZ1DASYd9rk?t=801

An interface is quite similar to a record of functions. I might consider putting them into Spiral at some point, but I do not need them right now. If I did them, I'd need to implement them for all 3 backends. If I had to put them in I'd probably get rid of the older 2.

https://youtu.be/hZ1DASYd9rk?t=909

I'll go with the F# version personally, though no doubt the lecturer will pick C#. It is fine. This should be just a bit of an extra challenge that I'll welcome.

https://youtu.be/hZ1DASYd9rk?t=1006

The version I have of .NET Core 6 is out of preview, so I do not have the auth option here.

```fs
module Program =
    let exitCode = 0

    [<EntryPoint>]
    let main args =
        let builder = WebApplication.CreateBuilder(args)

        builder
            .Services
            .AddControllersWithViews()
            .AddRazorRuntimeCompilation()

        builder.Services.AddRazorPages()

        let app = builder.Build()

        if not (builder.Environment.IsDevelopment()) then
            app.UseExceptionHandler("/Home/Error")
            app.UseHsts() |> ignore // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.

        app.UseHttpsRedirection()

        app.UseStaticFiles()
        app.UseRouting()
        app.UseAuthorization()

        app.MapControllerRoute(name = "default", pattern = "{controller=Home}/{action=Index}/{id?}")

        app.MapRazorPages()

        app.Run()

        exitCode
```

I remember studying this years ago. Back then I found it really confusing how it would hit all these static calls. Compared to the JS tutorial from yesterday this is more awkward. But let me just push on with it.

10:50am.

```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:7012
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5012
```

This is clear enough. What is the other IP for?

https://youtu.be/hZ1DASYd9rk?t=1273

```
    "iisExpress": {
      "applicationUrl": "http://localhost:3683",
      "sslPort": 44304
    }
```

I wonder why it is ignoring the port in the application URL and using the ssl port instead? Also what is the difference between the two? Also since it did not open a console window, how do I shut it down?

I am a bit into this tutorial. I find it easier to digest than the MS docs of yore.

I feel more driven than last time since I have the overall software architecture in mind. Since I've started at 6am, I think I won't do it till 6pm today and close earlier instead. Yesterday I was just so tired going late, getting up early and then making a trip to the bank that it readjusted my whole schedule back by 4 hours.

11am. https://youtu.be/hZ1DASYd9rk?t=1477

Let me pause here. It is time for breakfast.

11:30am. Done with the eating part of breakfast. Let me read Mitsuha 80k and then I'll resume.

12pm. Let me resume.

https://teletype.in/@kati_lilian/SJA8KwjjN
Yuri made me human

I'll leave this interview for later.

Ugh, I really feel like closing for the day. I've been at it for 6h already, but let me put in a bit more. So far, I like this course. It is thorough and well structured. It is just what I'd want for the sake of learning ASP.NET.

12:15pm. https://youtu.be/hZ1DASYd9rk?t=1843

Shit, I am really stressed out right now.

Let me try another 10m, after that I'll close for the day if I feel like it and play some BG2.

12:30pm. https://youtu.be/hZ1DASYd9rk?t=2413

This part is a bit smart. I didn't realize that Views and Controllers share names.

https://youtu.be/hZ1DASYd9rk?t=2525

Hmmm, I see. So it using reflection to get the names of the methods as well the parent class and using that for views. I didn't realize this a year ago. So I am making progress.

12:50pm. https://youtu.be/hZ1DASYd9rk?t=2942

Let me stop here. I am at my limit. Getting at 6am does not mean the 6pm rule suddenly holds. I can't study 12h a day.

In hindshight, I should have just watched the video by John Codes on scaling, and then move to this ASP.NET course. Had I done that I would have finished it by now.

But I've meet the 5h of work a day rule, so by stopping here it is not like I am going against my own ethos. Tomorrow, I will complete the course and the toy app. After that I'll either go for the networking course or study ASP.NET using a different venue. By the time I am done with that, hopefully the card will have gotten here."

---
## [BrackeysBot/DSharpPlus](https://github.com/BrackeysBot/DSharpPlus)@[8380b5b2de...](https://github.com/BrackeysBot/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Tuesday 2022-07-19 12:11:57 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [StarbloomSS13/StarbloomSS13](https://github.com/StarbloomSS13/StarbloomSS13)@[635f518d04...](https://github.com/StarbloomSS13/StarbloomSS13/commit/635f518d04a30c4c9f977c0570d480f8d44e56d1)
#### Tuesday 2022-07-19 12:16:42 by notfrying1pans

web edit fuck yoooou

i swear to fucking god if this resets line endings or some shit im gonna scream

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[5522769378...](https://github.com/cockroachdb/cockroach/commit/5522769378eea814c85e4d22b839c6ff81f6f744)
#### Tuesday 2022-07-19 13:38:34 by craig[bot]

Merge #76776 #76793 #76835 #76901

76776: scpb,scdecomp,scbuild: remodel elements, use decomposition r=postamar a=postamar

This change adresses some shortcomings of the declarative schema
changer that would have compromised its ability to evolve gracefully in
its current form. Basically these are:
  1. the builder generating targets based off a hybrid descriptor-and-
     element scheme, and
  2. an awkward handling of back-references which precludes doing much
     more than DROP statements correctly.

This change therefore consists of, respectively:
  1. rewriting the builder to hide descriptors from the `scbuildstmt`
     package, instead exposing sets of elements, and
  2. reworking the element model definition by getting rid of
     back-reference elements entirely.

In support of (1) this commit introduces a new `scdecomp` package which,
given a descriptor, will walk a visitor function over all its
constituent elements. This itself is made quite simple by (2) which
largely removes the need to look up referenced descriptors outside of
some mild edge-cases.

This `scdecomp` package is used by the backing structs of the
`scbuildstmt` dependency interfaces to collect a "state-of-the-world"
snapshot of elements upon which the schema change target elements are
layered. This approach lends itself well to caching as the descriptors
remain immutable in the builder.

The rewrite of most of `elements.proto` in support of (2) implies a slew
of cascading changes:
 - the attributes in `screl` need to be adjusted,
 - the lifecyles of the elements in `opgen` have to be adjusted,
 - the dependency rules and no-op rules need to be adjusted,
 - in turn, new operations need to be defined in `scop`, and,
 - in turn, these operations need to be implemented in `scmutationexec`.

Elements are now responsible for updating any back-references that
correspond to their forward references, which effectively pushed that
complexity into these reference update ops in `scmutationexec`. These
have to operate on a best-effort basis, because there are no longer
back-reference elements with dependency rules to enforce convenient
assumptions about the context of their adding or removal. This is
arguably not a bad thing per-se: this new paradigm is "fail hard, fail
fast" which surfaces bugs a lot more quickly than a badly-written
dependency rule would.

The rules themselves fall into cleaner patterns. This commit provides some
tools to express the most common of these. This commit also unifies the
`deprules` and `scopt` packages into a commit `rules` package with full
data-driven test coverage.

Other changes in this commit are peripheral in nature:
  - Working on this change surfaced some deficiencies in the
    cross-referenced descriptor validation logic: we checked that the
    referenced descriptor exists but not that it's not dropped. This
    commit fixes this.
  - The expression validation logic in `schemaexpr` quite reasonably
    used to assume that columns can be found in descriptors;
    unfortunately the builder needs to be able to use this for columns
    which only exist as elements. This commit refactors the entry points
    into this validation logic as a result.
  - Quality-of-life improvements like adding a testing knob used to
    panic TestRollback with an error with a full stack trace when the
    rollback fails.
  - Because back-references don't exist as elements anymore, they also
    don't exist as targets, so we now have schema changer jobs linked to
    descriptors for which there are zero targets. This commit addresses this
    by simply allowing it. This is necessary to lock descriptors to
    prevent any concurrent schema changes which would affect them.

Release note: None


76793: storage: introduce guaranteed durability functionality r=jbowens a=sumeerbhola

This is the CockroachDB plumbing for Pebble's
IterOptions.OnlyReadGuaranteedDurable. It is for use in
the raftLogTruncator https://github.com/cockroachdb/cockroach/pull/76215.

Since most of the exported interfaces in the storage
package use a Reader, we support this via a
DurabilityRequirement parameter on Engine.NewReadOnly,
and not via an iterator option.

There is also a RegisterFlushCompletedCallback method
on Engine which will be used to poll certain durable
state in the raftLogTruncator.

Other than the trivial plumbing, this required some
refactoring of the Reader.MVCCGet* code for Pebble
and pebbleReadOnly. Even though it is deprecated and
primarily/only used in tests, we don't want to have
the durability semantics diverge.

Release note: None

76835: ttljob: add controls to pause TTL jobs r=rafiss a=otan

See individual commits for details.

76901: colexecspan: de-templatize span assembler and use span.Splitter r=RaduBerinde a=RaduBerinde

#### colexecspan: de-templatize span assembler

The span assembler code is generated only to inline a piece of code
that has two variants. This change converts it to non-generated code
and simply forks the code paths above the batch loop.

Release note: None

#### colexecspan: use span.Splitter

The span assembler duplicates some of the logic in `span.Splitter`.
Now that the latter is a separate type, we can use it instead.

Release note: None


Co-authored-by: Marius Posta <marius@cockroachlabs.com>
Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>

---
## [Hurricos/realtek-poe](https://github.com/Hurricos/realtek-poe)@[88cb11bd6c...](https://github.com/Hurricos/realtek-poe/commit/88cb11bd6c6a3fdd69dff2638aeeac7d1d936258)
#### Tuesday 2022-07-19 16:44:02 by Alexandru Gagniuc

realtek-poe: Fix memory leak in poe_reply_consume()

When thinking "embedded", it's a good idea to stay the fuck away from
malloc(). Falling out of scope is a free garbage collector. Port
config and state arrays followed this advice, but for some reason, the
command queue did not.

No worries, free() is used in poe_reply_consume(). No problemo! Crisis
averted! Did you spot the several failure modes which return before
the free() call. In these modes, a malloc()d command is taken off the
queue, and not free()d. The pointer falls out of scope and memory lost.
Quod Erat Demonstratum.

To fix this, free() the command before hitting any exit paths.

Signed-off-by: Alexandru Gagniuc <mr.nuke.me@gmail.com>

---
## [Wahid7852/kernel_xiaomi_mt6785-bal](https://github.com/Wahid7852/kernel_xiaomi_mt6785-bal)@[54923e297f...](https://github.com/Wahid7852/kernel_xiaomi_mt6785-bal/commit/54923e297f245b422c521b948f2c195b44f1c839)
#### Tuesday 2022-07-19 16:48:59 by Peter Zijlstra

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
## [Drmarru/Drmarru](https://github.com/Drmarru/Drmarru)@[a8682c4cef...](https://github.com/Drmarru/Drmarru/commit/a8682c4cefb8459adfc1d832def09250f4766547)
#### Tuesday 2022-07-19 16:58:49 by Drmarru

thank you very much

How about the program I developed?
It is free for all to use. So the hack is meaningless. I would be happy if you could create a new era from it. My first program is pragmasolidity. From there, I built econosystem matic, etc. Recently, Ubuntu and fullter daemon are well known to everyone.
I am Japanese. I respect America. It runs this world. I respect and appreciate it.
That's why I'm working hard to make everyone happy. I receive zero compensation.
That's why I work elsewhere. I will do anything. Sometimes I work at construction sites. Why work elsewhere when you have a sponsor? That's right, I don't get any income from this program.
You are earning from the program I created.
Life is like that.
I'm going to work with a Japanese company to make the best game in the world.
Using blockchain.
Enjoy!

Translated with www.DeepL.com/Translator (free version)

---
## [noahshaw11/couchdb](https://github.com/noahshaw11/couchdb)@[77f34a1bbc...](https://github.com/noahshaw11/couchdb/commit/77f34a1bbc7c76aefa59777da21e2e76e79f7ec8)
#### Tuesday 2022-07-19 17:14:06 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 23 as the embedded Erlang version in packages. We
  avoid Erlang 24 for now because Clouseau is not currently compatible.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

This is a cherry-pick of 9b6454b with the following modifications:

- Drop the MINIMUM_ERLANG_VERSION to 20
- Drop the packaging ERLANG_VERSION to 23
- Add the weatherreport-test as a build step
- Add ARM and POWER back into the matrix using a new buildx-based
  multi-architecture container image.

---
## [el-ang/GeoID](https://github.com/el-ang/GeoID)@[ef8bacffe9...](https://github.com/el-ang/GeoID/commit/ef8bacffe928902112d8387725a6b3068da46e3b)
#### Tuesday 2022-07-19 18:09:39 by el-ang

:package: Backing Up package-lock.json

The worst mistake in my life :man_facepalming:

---
## [epage/clap](https://github.com/epage/clap)@[d43f1dbf6f...](https://github.com/epage/clap/commit/d43f1dbf6f1f7865dccfece0e1605a12efb76670)
#### Tuesday 2022-07-19 19:05:24 by Ed Page

docs: Move everything to docs.rs

A couple of things happened when preparing to release 3.0
- We needed derive documentation
  - I had liked how serde handled theres
  - I had bad experiences finding things in structopt's documentation
- The examples were broken and we needed tests
- The examples seemed to follow a pattern of having tutorial content and
  cookbook content
- We had been getting bug reports from people looking at master and
  thinking they were looking at what is currently released
- We had gotten feedback to keep down the number of places that
  documentation was located

From this, we went with a mix of docs.rs and github
- We kept the number of content locations at 2 rather than 3 by not
  having an external site like serde
- We rewrote the examples into explicit tutorials and cookbooks to align
  with the 4 styles of documentation
- We could test our examples by running `console` code blocks with
  trycmd
- Documentation was versioned and the README pointed to the last release

This had downsides
- The tutorials didn't have the code inlined
- Users still had a hard time finding and navigating between the
  different forms of documentation
- In practice, we were less likely to cross-link between the different
  types of documentation

Moving to docs.rs would offer a lot of benefits, even if it is only
designed for Rust-reference documentation and isn't good for Rust derive
reference documentation, tutorials, cookbooks, etc.  The big problem was
keeping the examples tested to keep maintenance costs down.  Maybe its
just me but its easy to overlook
- You can pull documentation from a file using `#[doc = "path"]`
- Repeated doc attributes get concatenated rather than first or last
  writer winning

Remember these when specifically thinking about Rust documentation made
me realize that we could get everything into docs.rs.

When doing this
- Tutorial code got brought in as was one of the aims
- We needed to split the lib documentation and the README to have all of
  the linking work.  This allowed us to specialize them according to
  their rule (user vs contributor)
- We needed to avoid users getting caught up in making a decision
  between Derive and Builder APIs so we put the focus on the derive API
  with links to the FAQ to help users decide when to use one or the
  other.
- Improved cross-referencing between different parts of the
  documentation
- Limited inline comments were added to example code
  - Introductory example code intentionally does not have teaching
    comments in it as its meant to give a flavor or sense of things and
    not meant to teach on its own.

This is a first attempt.  There will be a lot of room for further
improvement.  Current know downsides:
- Content source is more split up for the tutorials

This hopefully addresses #3189

---
## [nodejs/package-maintenance](https://github.com/nodejs/package-maintenance)@[e4c00154f5...](https://github.com/nodejs/package-maintenance/commit/e4c00154f5072c95c4b10e1d2082f517e73ee681)
#### Tuesday 2022-07-19 19:06:05 by Ayush Anand

Add @Ayushsunny as a member (#532)

Hello,
I'm Ayush Anand, I'm wanting to be a member so I can work with all of the interesting stuff to gain more experience. I'm available to work on any part of this org like documentation, community engagement, and package building. I'd also like to help give any input in any areas that I have experience in according to my GitHub profile.
Thank you all for your amazing work!

---
## [hipe/tmx](https://github.com/hipe/tmx)@[9318b078f3...](https://github.com/hipe/tmx/commit/9318b078f3971969f974948ab6d126f68a38972a)
#### Tuesday 2022-07-19 20:15:05 by Mark Meves

feat(kiss:cap-server): Integrate "routing" (urls) ((1757))

Discussion: we don't know how far we are going to be able to carry the
vaporware dream of "app flow"; but one essential feature it seemed to
hurt most from was a proper formalization of "routes" (as they call it
in rails).

Also it felt like the biggest "sore thumb" of this as a web app (just
from a look-and-feel standpoint) that we had only one endpoint and a bunch
of GET parameters on every request (most importantly the `action`).

Implementing our bespoke version of "routing" was fun and rewarding,
but also shook things up pretty deeply because of how significant an
architecture change it was.

For reference, these were (more or less) the endpoints we tested visually:

@endpoint('/capability/{EID}/notes/add/')
@endpoint('/capability/{EID}/edit/')
@endpoint('/capability/{EID}/notes/add/', http_method='POST')
@endpoint('/capability/{EID}/edit/', http_method='POST')
@endpoint('/capability/{EID}/')
@endpoint('/')
@endpoint('/', GET_params={'index_style':'tree'})
@endpoint('/test/UI/')
@endpoint('/ping/')

(times)
  07-05 12:15  (from Hyperion) begin integrating routing omg
        20:30  (from SWP) re-arch is heavy around commands and signatures
  07-06 16:52  (from Shinola) ok figured out that our spec isn't that bad
  07-12 07:41  (from Hyperion) we got a form submit working The New Way.
                we just have to finish all the other refactoring
                around url construction
  07-13 14:16  (from Hyperion, home) please let's finish routing
        15:47  (break to go downtown)
        17:51  (from SWW) bash is so annoying to write scripts for
  07-14 19:11  (from SWP) gotta piece together runnable webserver again lol
        20:54  progress was ok. but we need to deal with routes for assets like stylesheets
  07-15 16:48  amazing - served
  07-16 08:15  (from Hyperion) oh noes now that urls have gotten deep,
               assets are loading weird
        08:24  (fixed. was easy. had to introduce absolute urls)
  07-19 11:36  after hours and days and years
        11:37  (from Hyperion) after piecemeal sub-hours after several
               days, maybe we have the story working
        15:48  smoke test & begin assemble commit

---
## [newstools/2022-daily-dispatch](https://github.com/newstools/2022-daily-dispatch)@[43ee455c02...](https://github.com/newstools/2022-daily-dispatch/commit/43ee455c02e2b6d58b7fae184756ae815e4c0cec)
#### Tuesday 2022-07-19 20:35:05 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2022-07-19-life-in-jail-for-man-who-murdered-his-girlfriend-thokozile-kubheka-after-repeated-threats/]

---
## [PivotingMom/mvpproj_frontend](https://github.com/PivotingMom/mvpproj_frontend)@[2e23cc21f7...](https://github.com/PivotingMom/mvpproj_frontend/commit/2e23cc21f7e5624214dba1d720348aceef665a61)
#### Tuesday 2022-07-19 21:53:05 by Pivotingmum

becoming a programmer was never part of the plan, it is a dream bore out of pain, rejection, poverty, a  desire to live life on my terms, and to be a source of hope and inspiration, I'm grateful for this dream

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[4f9df17cb1...](https://github.com/Paxilmaniac/Skyrat-tg/commit/4f9df17cb150bd073914527bce381b583cf83657)
#### Tuesday 2022-07-19 22:39:19 by magatsuchi

[FIXED MIRROR] Tsu's Brand Spanking New Storage: or, How I Learned to Refactor For Skyrat (#14868)

* Tsu's Brand Spanking New Storage: or, How I Learned To Pass Github Copilot As My Own Code

* Delete storage.dm

* yippee

* shit

* holy shit i am stupid

* more fixes

* fuck

* woops

---
## [triyon333/StarbloomSS13](https://github.com/triyon333/StarbloomSS13)@[cbd7626cb7...](https://github.com/triyon333/StarbloomSS13/commit/cbd7626cb7b189f1aa19ae007a5dcc253757601d)
#### Tuesday 2022-07-19 23:06:35 by RegJackson

Readds buckshot to the autolathe

I used the shotgun. You know why? Cause the shot gun doesn't miss, and unlike the shitty hybrid taser it stops a criminal in their tracks in two hits. Bang, bang, and they're fucking done. I use four shots just to make damn sure. Because, once again, I'm not there to coddle a buncha criminal scum sucking faggots, I'm there to 1) Survive the fucking round. 2) Guard the armory. So you can absolutely get fucked. If I get unbanned, which I won't, you can guarantee I will continue to use the shotgun to apprehend criminals. Because it's quick, clean and effective as fuck. Why in the seven hells would I fuck around with the disabler shots, which take half a clip just to bring someone down, or with the tazer bolts which are slow as balls, impossible to aim and do about next to jack shit, fuck all. The shotgun is the superior law enforcement weapon. Because it stops crime. And it stops crime by reducing the number of criminals roaming the fucking halls.

---
## [DunniDee/Project-R](https://github.com/DunniDee/Project-R)@[c0ae7f5186...](https://github.com/DunniDee/Project-R/commit/c0ae7f5186f02f0538109693a911f40d872f5c9b)
#### Tuesday 2022-07-19 23:53:16 by Dunstan

Motor and UI Changes

Fuck you fraser ive neuterd your shit

---

