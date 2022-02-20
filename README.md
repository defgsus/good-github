## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-19](docs/good-messages/2022/2022-02-19.md)


1,349,731 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,349,731 were push events containing 2,050,210 commit messages that amount to 125,924,012 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [mudlord/WTFggerat](https://github.com/mudlord/WTFggerat)@[df9660d71f...](https://github.com/mudlord/WTFggerat/commit/df9660d71f1aec466853249eb65de3d0aee5497e)
#### Saturday 2022-02-19 00:19:03 by mudlord

This is a massive fucking hack.

Due to the bullshit in the libretro mupen core, spurious buffer swaps corrupt
dear-imgui. So now to compensate for the fucking shit API, we have to weave UI
code to buffer swap cleanly at the same rate, until a better means of working
with the core is done, or another core is done entirely that behaves with how
the fuck I wanna do this. Spent all morning debugging to find this shit.

Render to textures/image buffer handles FFS instead of wanting to swap willy
nilly!

---
## [AntsyBoi/Time-n-Date](https://github.com/AntsyBoi/Time-n-Date)@[bfb71d14b4...](https://github.com/AntsyBoi/Time-n-Date/commit/bfb71d14b4e4d54c66cf1e303f2cfca4c11b58fe)
#### Saturday 2022-02-19 00:27:51 by AntsyBoi

Final commit (at least for awhile, read the note)

Made the main app not require p5 and only depend on JS on the front end

From the file
> I loved working on this project.
> I originally started working on it as an experiment to test
> something out in processingJS when I was learning it on Khan
> Academy (man that was a mistake, KhanAcademy is amazing for a 
> lot but not learning how to code), this funny enough was also
> first introductiont to fucntions. Then this project took 5
> years of my life (2017-2022) working on it off and on just 
> trying to perfect it, and I finally think it's time for me
> to be done with it. I might occasionally update it with
> dependency updates but other than that I want to work on
> other things. And with the 100th commit on GitHub for this
> project I want to finally have this project sail off into 
> the sunset, I loved every second of working on this project
> and I hope other people get that same amount of joy working
> on their projects. I know this project is stupid but I love
> it. It taught me so much and I want to now use that somewhere
> else. I love you Time&Date, and I hope that this project won't
> just fade into a free code void somewhere. Maybe someone will
> find it in 5 years from now and read this note. This note is
> getting me emotional just writing it but I hope this marks
> the next era of my coding passion and won't be the end.

---
## [Mu-L/cockroach](https://github.com/Mu-L/cockroach)@[255c1fb027...](https://github.com/Mu-L/cockroach/commit/255c1fb02708f99fef62b0af719af5e0984d9de3)
#### Saturday 2022-02-19 00:52:27 by craig[bot]

Merge #71542 #73319 #74077 #76401 #76748

71542: backupccl: Support RESTORE SYSTEM USERS from a backup r=gh-casper a=gh-casper

Support a new variant of RESTORE that recreates system users that don't exist in current cluster from a backup that contains system.users and also grant roles for these users. Example invocation: RESTORE SYSTEM USERS FROM 'nodelocal://foo/1';

Similar with full cluster restore, we firstly restore a temp system database which contains system.users and system.role_members into the restoring cluster and insert users and roles into the current system table from the temp system table.

Fixes: #45358

Release note (sql change): A special flavor of RESTORE, RESTORE SYSTEM USERS FROM ..., is added to support restoring system users from a backup. When executed, the statement recreates those users which are in a backup of system.users but do not currently exist (ignoring those who do) and re-grant roles for users if the backup contains system.role_members.

73319: jobs: Execute scheduled jobs on a single node in the cluster. r=miretskiy a=miretskiy

Execute scheduled jobs daemon on a single node -- namely, the lease
holder for meta1 range lease holder.

Prior to this change, scheduling daemon was running on each node,
polling scheduled jobs table periodically with a `FOR UPDATE` clause.
Unfortunately, job planning phase (namely, the backup planning phase) could
take significant amount of time.  In such situation, the entirety
of the scheduled jobs table would be locked, resulting in inability
to introspect the state of schedules (or jobs) via `SHOW SCHEDULES` or similar
statements.

Furthermore, dropping `FOR UPDATE` clause by itself is not ideal because
that would lead to expensive backup planning being executed on almost every
node, with all but 1 node making progress.

The single node mode is disabled by default, but can be enabled
via a `jobs.scheduler.single_node_scheduler.enabled` setting.

Release Notes: scheduled jobs scheduler now runs on a single node by default
in order to reduce contention on scheduled jobs table.

74077: kvserver: lease transfer in JOINT configuration r=shralex a=shralex

Previously:
1. Removing a leaseholder was not allowed.
2. A VOTER_INCOMING node wasn't able to accept the lease.

Because of (1), users needed to transfer the lease before removing
the leaseholder. Because of (2), when relocating a range from the
leaseholder A to a new node B, there was no possibility to transfer
the lease to B before it was fully added as VOTER. Adding it as a
voter, however, could degrade fault tolerance. For example, if A
and B are in region R1, C in region R2 and D in R3, and we had
(A, C, D), and now adding B to the cluster to replace A results in
the intermediate configuration (A, B, C, D) the failure of R1 would
make the cluster unavailable since no quorum can be established.
Since B can't be added before A is removed, the system would
transfer the lease out to C, remove A and add B, and then transfer
the lease again to B. This resulted a temporary migration of leases
out of their preferred region, imbalance of lease count and degraded
performance.

The PR fixes this, by (1) allowing removing the leaseholder, and
transferring the lease right before we exit the JOINT config. And (2),
allowing a VOTER_INCOMING to accept the lease.

Release note (performance improvement): Fixes a limitation which meant 
that, upon adding a new node to the cluster, lease counts among existing
nodes could diverge until the new node was fully upreplicated.

Here are a few experiments that demonstrate the benefit of the feature.
1. 
> roachprod create local -n 4 // if not already created and staged
> roachprod put local cockroach
> roachprod start local:1-3 --racks=3 // add 3 servers in 3 different racks
> cockroach workload init kv --splits=10000
> roachprod start local:4 --racks=3 // add a 4th server in one of the racks

Without the change (master):
<img width="978" alt="Screen Shot 2022-02-09 at 8 35 35 AM" src="https://user-images.githubusercontent.com/6037719/153458966-609dbb7e-ca3d-4db6-9cfb-adc228f2bdf2.png">

With the change:
<img width="986" alt="Screen Shot 2022-02-08 at 8 46 41 PM" src="https://user-images.githubusercontent.com/6037719/153459366-2d4e2def-37cf-405b-b601-8be57419ae02.png">

We can see that without the patch the number of leases on server 0 (black line) goes all the way to 0 before it goes back up and that the number of leases in other racks goes up, both undesirable. With the patch both things are no longer happening.

2. Same as 1, but with a leaseholder preference of rack 0:

ALTER RANGE default CONFIGURE ZONE USING lease_preferences='[[+rack=0]]';

Without the change (master):
<img width="966" alt="Screen Shot 2022-02-09 at 10 45 27 PM" src="https://user-images.githubusercontent.com/6037719/153460753-bce048f0-f6da-4e21-afdc-317620c035b2.png">

With the change:
<img width="983" alt="leaseholder preferences - with change" src="https://user-images.githubusercontent.com/6037719/153460780-55795866-cf47-404d-b77a-45d9e011f972.png">

We can see that without the change the number of leaseholders in racks 1 and 2 together (not in preferred region) grows from 300 to 1000, then goes back to 40. With the fix it doesn’t grow at all.






76401: pgwire: add server.max_connections public cluster setting r=rafiss a=ecwall

This setting specifies a maximum number of connections that a server can have open at any given time.
<0 - Connections are unlimited (existing behavior)
=0 - Connections are disabled
>0 - Connections are limited
If a new non-superuser connection would exceed this limit, the same error message is
returned as postgres: "sorry, too many connections" with the 53300 error code
that corresponds to "too many connections".

Release note (ops change): An off-by-default server.max_connections cluster
setting has been added to limit the maximum number of connections to a server.

76748: sql: add missing specs to plan diagrams r=rharding6373 a=rharding6373

This change allows missing specs (e.g., RestoreDataSpec and
SplitAndScatterSpec) to be shown in plan diagrams. Before this change a
plan involving these types would result in an error generating the
diagrams. Also added a test to make sure future specs implement the
`diagramCellType` interface, which is required to generate diagrams.

Release note: None


Co-authored-by: Casper <casper@cockroachlabs.com>
Co-authored-by: Yevgeniy Miretskiy <yevgeniy@cockroachlabs.com>
Co-authored-by: shralex <shralex@gmail.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>

---
## [mrsanjaychouhan/FestMan-Data-Challenge-Mobile-Subscribers-Challenge-Sanjay-Chouhan](https://github.com/mrsanjaychouhan/FestMan-Data-Challenge-Mobile-Subscribers-Challenge-Sanjay-Chouhan)@[d53c672a2b...](https://github.com/mrsanjaychouhan/FestMan-Data-Challenge-Mobile-Subscribers-Challenge-Sanjay-Chouhan/commit/d53c672a2b1134df909ede0e1d9f64f4e4cd34f7)
#### Saturday 2022-02-19 03:27:24 by Sanjay Chouhan

Add files via upload

Hi! This is my submission to the Mobile subscribers churning data challenge of FestMan™ Learning Hub.
This is my first challenge and I'm waiting for some reviews!
The challenge was quite interesting since it had lot of Metrics.
Here are some insights: 
Lost Customer in Last month -1869
Total customer - 7043
Female customer – 3488
Male Customers – 3555

Average Charges paid by per user -  
monthly – 64.76
Totally – 2283.30

Open Tickets
A-Admin - 3632
A-Tech – 2955

Customer Count & Ratio (Top and Bottom)  

By Type of service - Top: Fiber optical (3096, 44%) | Bottom: No Internet (1526, 21.67)  
By Type of subscription – Top: Music Time (4835, 16%) | Bottom: Online Security (2019, 6.67%) 
By Contract – Top: Month to Month (3875,55%) | Bottom: One Year (1473, 20%)
By Tenure – Top:  less than one year (1317, 19%) : Bottom 3 Years (787, 11%)
By Dependents – Top: No (4933, 70%) | Bottom: Yes (2110,30%)
By Partner – Top: No (3641, 51.7%) | Bottom: Yes (3402, 48.3%)  
By Payment Method – Top: Electronic (2365, 33%) | Bottom: Credit Card (1522, 21%)

---
## [Gui-iago/FNF-BedrockEngine](https://github.com/Gui-iago/FNF-BedrockEngine)@[0cc9543893...](https://github.com/Gui-iago/FNF-BedrockEngine/commit/0cc954389300d6d990f8f317ef6a7594e1fa28cc)
#### Saturday 2022-02-19 03:35:02 by HiroMizuki

All Star - Smash Mouth (Lyrics)

Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead
Well the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
It's a cool place and they say it gets colder
You're bundled up now, wait 'til you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how about yours?
That's the way I like it and I'll never get bored
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
All that glitters is gold
Only shooting stars break the mold
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show, on get paid
And all that glitters is gold
Only shooting stars
Somebody once asked could I spare some change for gas?
I need to get myself away from this place
I said, "Yup" what a concept
I could use a little fuel myself
And we could all use a little change
Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go (go!)
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
And all that glitters is gold
Only shooting stars break the mold

---
## [chef/chef](https://github.com/chef/chef)@[9c615241b5...](https://github.com/chef/chef/commit/9c615241b52a3947549bc17ab85e256dc47be7ab)
#### Saturday 2022-02-19 05:17:30 by Lamont Granquist

Disable knife gem install in kitchen tests

This causes horrible issues.

We are installing knife in a TK virt and can't really build it and
install it as a test (hacking up appbundler to do this would largely
invalidate the test since we wouldn't be testing customer behavior)
and as such it needs to be installed from rubygems.  That means
installing knife-17, which pulls down chef-17 which currently has
a dep on diff-lcs 1.3.x which conflicts with 1.5.x which throws
the errors around the binstubs conflicting (which may or may not be
a rubygems bug, I investigated that a bit and couldn't determine
why that is happening since the 3rd line has the magic rubygems
comment).  We can't just use "--force" as an option since that'll
ignore deps and stuff as well which is precisely the kinds of things
that we're trying to catch.  So for now this test is more pain
that it is worth.

Signed-off-by: Lamont Granquist <lamont@scriptkiddie.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2209c36036...](https://github.com/tgstation/tgstation/commit/2209c36036c5c0c303443fd4a6304da9384e5107)
#### Saturday 2022-02-19 05:28:22 by san7890

Fixes Weird Area Definition on DeltaStation (#64986)

So, there I was. Pondering the blobbosity of Auxiliary Base Construction. Deciphering and unclothing the issue in my mind in order to better comphrehend it. I was there for a few moments, until this ugly beast of a fucking area definition caught my eye:

Hideous. Repugnant. I was relishing the thought of dissecting Auxiliary Base Construction into fifteen million more areas (it _will_ lessen obtusities) when that scraggletooth of an utterly mortifying error forced me into a visceral rage: the likes of which have never been experienced on this planet Earth.

---
## [KrishnakantShedge/kernel_realme_RMX1851](https://github.com/KrishnakantShedge/kernel_realme_RMX1851)@[7d4b021e02...](https://github.com/KrishnakantShedge/kernel_realme_RMX1851/commit/7d4b021e0290eb3804b106070fe410eab9ba73a0)
#### Saturday 2022-02-19 07:10:43 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dakkshesh <dakkshesh5@gmail.com>

---
## [CamillieFu/chirpy](https://github.com/CamillieFu/chirpy)@[83d4ea0272...](https://github.com/CamillieFu/chirpy/commit/83d4ea02728614206c6b5aa9eb000ccadeafd527)
#### Saturday 2022-02-19 07:28:49 by Steven Vasquez

Merge pull request #60 from CamillieFu/removed-socials-fa

removed the shit fucking FA icons for the moment

---
## [Stonie4twnty0/Stonie4twnty0](https://github.com/Stonie4twnty0/Stonie4twnty0)@[d558ec5855...](https://github.com/Stonie4twnty0/Stonie4twnty0/commit/d558ec58556427573407fa0cf210aa9a8c065b98)
#### Saturday 2022-02-19 08:18:37 by Stonie4twnty0

Update README.md I need help my x  put a package in my phone or Gmail or wifi because I broke up with her for using neth around my daughter she has stolen from us and normal I would let these things pass but she's in my phone my parents phone and she is in my daughter's I've spent a lot of money replacing these phone moving carriers and she's still there she removes or apps and my dad misses doctors appointments and he can't miss these he has melanoma dementia and Parkinson she's in our bank accounts and now she put a restraining order on me lied and never served me and she won across the board and now I have classes and there's not enough time for this shit I barely get to c my daughter now im gonna c even less I can't prove she's doing it so I'm stuck I'm close to saying fuck it and put hands on her this is my last resort coming here don't even know if I'm doing this right please someone help me

---
## [jacksonchumbler/crawl](https://github.com/jacksonchumbler/crawl)@[9e681642b6...](https://github.com/jacksonchumbler/crawl/commit/9e681642b6851451cbfcbc7a92e7de4b97106055)
#### Saturday 2022-02-19 08:52:57 by Nicholas Feinberg

Tweak Mlioglotl

Make him demonic holiness to better match player expectations (re
vulnerability to holy word), and make his Lugonu abilities priestly
rather than magical.

---
## [BoHBranch/BoH-Bay](https://github.com/BoHBranch/BoH-Bay)@[0ee0c4a0c5...](https://github.com/BoHBranch/BoH-Bay/commit/0ee0c4a0c578c11009fe53f09e944a4dac429b3e)
#### Saturday 2022-02-19 08:55:24 by Carl?

Merge pull request #1245 from anconfuzedrock/penfix

Makes it so retractable pens can't fuck you over

---
## [mijiturka/stupid-movie-oracle](https://github.com/mijiturka/stupid-movie-oracle)@[53f5f63885...](https://github.com/mijiturka/stupid-movie-oracle/commit/53f5f63885a02cc658f954db503014e319f96f64)
#### Saturday 2022-02-19 10:48:38 by Rumyana

Build and configure pyenv with ansible

I kinda hate ansible already

As I wait and wait for it I am filling the time by
reading a blogpost in favour of how useful it is,
because you can use it to install Docker.

I am not joking: https://nickjanetakis.com/blog/docker-and-ansible-solve-2-different-problems-and-they-can-be-used-together

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[b1ace967a2...](https://github.com/ianjoneill/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Saturday 2022-02-19 10:50:37 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [avar/git](https://github.com/avar/git)@[b89dc5f70b...](https://github.com/avar/git/commit/b89dc5f70b607240fa9b583fb882725f87141af7)
#### Saturday 2022-02-19 10:53:58 by Ævar Arnfjörð Bjarmason

usage API: use C99 macros for {usage,usagef,die,error,warning,die}*()

Change the "usage" family of functions to be defined in terms of C99
variadic macros, as we've optionally done with the BUG() macro and
BUG_fl() function since d8193743e08 (usage.c: add BUG() function,
2017-05-12), and unconditionally since 765dc168882 (git-compat-util:
always enable variadic macros, 2021-01-28).

This would have been possible before having a hard dependency on C99,
but as the dual implementations of C99 and pre-C99 macros and
functions adjusted in preceding commits show, doing so would have been
rather painful.

By having these be macros we'll now log meaningful "file" and "line"
entries in trace2 events. Before this we'd log "usage.c" in all of
them, and the line would be the relevant locations in that file.

To do this we need to not only introduce X_fl() functions for
{die,error,warning,die}{,_errno}(), but also change all the callers of
the set_*() and get_() functions in usage.h to take "file" and "line"
arguments.

Neither the built-in {die,error,warning,die}{,_errno}() nor anyone
else does anything useful with these "file" and "line" arguments for
now, but it means we can define all our macros and functions
consistently.

It also opens the door for a follow-up change where these functions
could optionally emit the file name and line number, e.g. for
DEVELOPER=1 builds, or depending on configuration.

It might be a good change to remove the "fmt" key from the "error"
events as a follow-up change. As these few examples from running the
test suite show it's sometimes redundant (same as the "msg"), rather
useless (just a "%s"), or something we could now mostly aggregate by
file/line instead of the normalized printf format:

      1 file":"builtin/gc.c","line":1391,"msg":"'bogus' is not a valid task","fmt":"'%s' is not a valid task"}
      1 file":"builtin/for-each-ref.c","line":89,"msg":"format: %(then) atom used more than once","fmt":"%s"}
      1 file":"builtin/fast-import.c","line":411,"msg":"Garbage after mark: N :202 :302x","fmt":"Garbage after mark: %s"}

"Mostly" here assumes that it would be OK if the aggregation changed
between git versions, which may be what all users of trace2 want. The
change that introduced the "fmt" code was ee4512ed481 (trace2: create
new combined trace facility, 2019-02-22), and the documentation change
was e544221d97a (trace2: Documentation/technical/api-trace2.txt,
2019-02-22).

Both are rather vague on what problem "fmt" solved exactly, aside from
the obvious one of it being impossible to do meaningful aggregations
due to the "file" and "line" being the same everywhere, which isn't
the case now.

In any case, let's leave "fmt" be for now, the above summary was given
in case it's interesting to remove it in the future, e.g. to save
space in trace2 payloads.

The change here in git_die_config() is the bare minimum needed to get
it working, but better would be a change[1] to correctly report the
caller file and line numbers. Let's leave that for later, it can be
done later.

1. https://lore.kernel.org/git/patch-4.4-e0e6427cbd3-20211206T165221Z-avarab@gmail.com/#t

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[b1c6291dba...](https://github.com/avar/git/commit/b1c6291dba1d1b53901d9e35bb2a9716c0ae8de9)
#### Saturday 2022-02-19 10:53:58 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[b1f17d9f8f...](https://github.com/avar/git/commit/b1f17d9f8fdb1f9a3280ac12ad4ed0f2f24277de)
#### Saturday 2022-02-19 10:53:58 by Ævar Arnfjörð Bjarmason

usage API: make the "{usage,fatal,error,warning,BUG}: " translatable

In preceding commits the vreportf() function was made static, so we
know it's only being called with a limited set of fixed prefixes. Pass
an enum indicating the kind of usage message we're emitting instead,
which means that we can fold the BUG_vfl_common() functionality
directly into it.

Since we've now got one place were we're emitting these usage messages
we can make them translatable.

We need to be careful with this function to not malloc() anything, as
a failure in say a use of strbuf_vaddf() would call xmalloc(), which
would in turn call die(), but here we're using static strings, either
from libintl or not.

I was on the fence about making the "BUG: " message translatable, but
let's do it for consistency. Someone who doesn't speak a word of
English may not know what "BUG" means, but if it's translated they
might have an easier time knowing that they have to report a bug
upstream. Since we'll always emit the line number it's unlikely that
we're going to be confused by such a report.

As we've moved the BUG_vfl_common() code into vsnprintf() we can do
away with one of the two checks for buffer sizes added in
116d1fa6c69 (vreportf(): avoid relying on stdio buffering, 2019-10-30)
and ac4896f007a (fmt_with_err: add a comment that truncation is OK,
2018-05-18).

I.e. we're being overly paranoid if we define the fixed-size "prefix"
and "msg" buffers, are OK with the former being truncated, and then
effectively check if our 256-byte buffer is larger than our 4096-byte
buffer. I wondered about adding a:

    assert(sizeof(prefix) < sizeof(msg)); /* overly paranoid much? */

But I think that would be overdoing it. Anyone modifying this function
will keep these two buffer sizes in mind, so let's just remove one of
the checks instead.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [mosra/magnum](https://github.com/mosra/magnum)@[30c1a2b8f8...](https://github.com/mosra/magnum/commit/30c1a2b8f8c6a2e12ae7ac8414c096ad96e2dfab)
#### Saturday 2022-02-19 11:24:00 by Vladimír Vondruš

GL: drop a silly <tuple> from state tracker internals.

Using a tuple was very useful, helpful and exciting as I had to make an
explicit comment about what element is what, and then having to remember
the order in all places that accessed the tuple.

Using a struct however is rather boring as the fields are just named
there, I don't need any complex std::get<4>() and extra comments
explaining what is where and it's just not so adventurous anymore. The
build time of a non-deprecated MagnumGL library also dropped from 5.9
seconds to 5.85. SAD!

---
## [Jetof20/Astroids](https://github.com/Jetof20/Astroids)@[cdd12168f5...](https://github.com/Jetof20/Astroids/commit/cdd12168f560ae9641e73aacdd64cf01ffa5be3e)
#### Saturday 2022-02-19 14:26:53 by Jetof20

Lek 3 Bullet Fucking Works. Javaserviceloader go fuck yourself.

---
## [teamYOMI/EXMCore](https://github.com/teamYOMI/EXMCore)@[c194273eca...](https://github.com/teamYOMI/EXMCore/commit/c194273eca0563aadb07450f32ebc9c305b32c03)
#### Saturday 2022-02-19 15:10:16 by TetraTheta

[WIP] 22.02.20
I still don't understand why I cannot set UserData as id in DeathTracker/Whitelist. Fuck you ORMLite.

---
## [Sirspam/Greetings](https://github.com/Sirspam/Greetings)@[07a65b9b0e...](https://github.com/Sirspam/Greetings/commit/07a65b9b0ec56ef2be607edf3a55a0143be2d67c)
#### Saturday 2022-02-19 15:26:16 by Sirspam

Awaited GetUserInfo Task

I didn't know it was a task 😢
Clearly all Kryptec's fault
Fuck you Kryptec.

---
## [tdauth/wowr](https://github.com/tdauth/wowr)@[cc4970c0cf...](https://github.com/tdauth/wowr/commit/cc4970c0cf28f57a4345b2543f6e25010e32fcbe)
#### Saturday 2022-02-19 15:38:16 by barade

1.9.9

- Save XP of hero 2 in every savecode.
- Replace bugged Frost Armor ability of Crown of the Lich King by Item Attack Frost Bonus.
- Fix soundset of bonus hero Medivh.
- Give bonus hero Malfurion Invisibility and Summon Mount abilities.
- Remove ability Spell Immunity from bonus hero Wizard. Otherwise, it would take too many slots.
- Add missing learn tooltips to ability Summon Sea Elemental of bonus hero Admiral Proudmoore.
- Try to revive Illidan immediately before changing his ownership to avoid a bug while he is being revived.
- Make items in backpack always droppable to fix the drop bug with Illidan's Ring of the Dark Legion.
- Increase the produced food of Hideouts and all upgraded versions from 25 to 55.
- Add ability Invisibility to bonus hero Anasterian Sunstrider.
- Fix ability Storm Bolt in the description of bonus hero Rexxar.
- Turtle Shell and Frostmourne use fixed defense and attack type values now to avoid bugs.
- Remove Neutral Citizen Female from Goblin Laboratories to get the Reveal slot back.
- Add new Murloc Sorcerer boss on new island with many creeps.
- Add Gnomish Submarines.
- Replace Taunt of hero Mountain Giant with Hurl Boulder.

---
## [YumeMichi/kernel_oneplus_sm8250](https://github.com/YumeMichi/kernel_oneplus_sm8250)@[152257aa48...](https://github.com/YumeMichi/kernel_oneplus_sm8250/commit/152257aa48837d11a73bafb8a8313b631116d234)
#### Saturday 2022-02-19 16:12:41 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [mwatts/bonsaidb](https://github.com/mwatts/bonsaidb)@[b2086b60e1...](https://github.com/mwatts/bonsaidb/commit/b2086b60e1b795b5734f3dcd4d9dae2e78ffb0e5)
#### Saturday 2022-02-19 16:20:09 by Jonathan Johnson

Add lz4 compression support

Closes #185

This is a first pass at compression support. I believe that ultimately
we'll want to support both zstd and lz4, but right now feature flags are
really annoying to implement. When we can implement namespaced features
(#178), we should revisit adding multiple compression backends and
options. lz4-flex has a faster unsafe option that can be enabled
optionally, but I've kept disabled in the spirit of BonsaiDb's "safe"
defaults.

From my research, zstd will be preferred when storage is at a premium,
but lz4 *should* be faster in general. I want to write a good benchmark
suite, because I believe the relative performance will potentially be
hardware dependent, and users should be able to gauge what works best
for them.

---
## [ian-from-dover/ip](https://github.com/ian-from-dover/ip)@[e26741a8e2...](https://github.com/ian-from-dover/ip/commit/e26741a8e298ec19d554f4cc2d89ac74b6cbbbdf)
#### Saturday 2022-02-19 17:37:18 by ian-from-dover

Polish GUI, add stickers, add welc, exit msgs

GUI was copied from the tutorial and was not optimised for Lily's
personality.

Having a GUI which suits the theme of the app and the tone of the
character makes the experience more immersive.

Let's,
* select colours which reflect the duolingo colour scheme
* choose a similar font to that reflected in duolingo's style guide
* reference classmates's scripts for fxml inspiration
* separate dialogbox classes
* add stickers to convey emotions
* add welcome and exit messages
* add pauses between Lily responding to the user giving a more
  humanlike chatting experience

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[031c0866ed...](https://github.com/retlaw34/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Saturday 2022-02-19 18:22:18 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [narsxi/narsxi-funny-website](https://github.com/narsxi/narsxi-funny-website)@[877b0ec667...](https://github.com/narsxi/narsxi-funny-website/commit/877b0ec6671b14ad4776223047ee897e2afda894)
#### Saturday 2022-02-19 19:26:24 by Liam

Updated to V4783498723498723498732

i hate my life

---
## [PixelExperience-Lemonadep/kernel_oneplus_sm8350](https://github.com/PixelExperience-Lemonadep/kernel_oneplus_sm8350)@[15670c31d7...](https://github.com/PixelExperience-Lemonadep/kernel_oneplus_sm8350/commit/15670c31d706b399a4be144818be4df497128631)
#### Saturday 2022-02-19 20:43:14 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: chandu078 <chandudyavanapelli03@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7267257d41...](https://github.com/mrakgr/The-Spiral-Language/commit/7267257d418b86d9cee03bfb2dbbaaf610f9b636)
#### Saturday 2022-02-19 20:57:29 by Marko Grdinić

"11:50am. I got up late for once. In fact, given that I've been going to bed at 1-2am it was a miracle that I've been getting up as early as I did in the past two weeks. I am going to drop Fallout New Vegas. Like Skyrim, most of my time in the game is spent searching containers for random crap I can sell. This is such a boring way to play despite being optimal. I am just wasting my time with this lukewarm game. I should not have started the Old World Blues addon. Maybe I will go back to reading, the game itself is certainly not in any way challenging.

Well, I should not be too rough in, it was fun for a while. It reminds me of how Pathfinder was fun at the start, but then I figured out the strats and started dominating and it got boring.

https://www.sidefx.com/learn/collections/banana-project/

Let me watch the the first in this series. I do not feel like going for breakfast right away.

12pm. Games have lost their luster for me. I want the kinds of games I dream about that would allow me to draw power from them into the real world. These games as they are now are just parasites on my time.

https://youtu.be/sv8dVzr-xNI?t=74

Despite being a beginner course, I've already learned something new. I hadn't know how to import images or the composite view.

https://youtu.be/sv8dVzr-xNI?t=297

Yeah, this is one example of why Houdini's learning curve is so extreme. In Blender you'd just paste the image onto a plane and move it around, but here there are special menu items for everything.

I'd honestly give Houdini a low score as a language in terms of design. It gets the node based workflow right. That is true. But it gets quite a lot of other things wrong.

It is not really meeting my needs.

After I finish the pool scene I'll go back to Blender.

12:30pm. https://youtu.be/UOMY2jrsCsg?t=185

I suppose this is a decent tut of Houdini's modeling, but if it were me I'd start with a 5 sided tube and then bend it. Then I'd scale the select edge loops down.

https://youtu.be/8dVRDMwcD-I?t=81

I was wondering how creases would work with subdiv. I guess I have my answer.

1:05pm. https://www.sidefx.com/tutorials/banana-project-part-02/?collection=77

Done with part 1. This part is the one I am really interested in.

Maybe I am being too rough on Houdini. i am starting to sense that I am finally on the verge of actually getting good at it.

https://vimeo.com/ondemand/houdinifxfundamentals

The stuff here is quite expensive. Imagine paying 360$ for all of this. Being a poorfag is suffering though. It is one thing to not want to buy it and quite another to not be able to afford it in the first place.

1:10pm. I can only hold contempt towards deep learning for not allowing me to break out. No, it is one thing to fail, but it did not even give me particular insights into AI. In terms of what it would allow me to turn into a story, I not any better off than I was in 2015. Just what is Spiral?

Will I get a chance to take advantage of it? Will I make Heaven's Key and watch it fall into obscurity too?

I want to make money with sheer power rather than appeal to the public. I want my path to give me insight into the nature of reality.

Doing art will only give me insight into art itself. These illusions will not get me closer to reality.

But, if the path I want to pursue relies on resource acquisition, then my odds are not good. Big organizations definitely have the advantage in the race towards the Singularity and the winner will get all.

1:15pm. All those advantages could be reversed if I could get an AI chip and then infer a better learning algorithm. If I could do that, it would be possible to plunder the online gaming scene for further resources.

Will I be capable of getting it? I am pretty slow here in learning art. Maybe my potential audience simply won't like my work.

If I fail due to lack of skill and ability so be it. For all I know somebody that could cover the ground faster than me could be more successful.

I am completely serious about this, so putting my life and existence on the line is something I am prepared for.

1:20pm. Houdini I have to go through. It is like Haskell of 3d software. No way can I avoid mastering it to some degree.

That scene will get finished and afterwards I'll decide how I want to do further work. Whether it be Blender or Houdini I'll be able to make either of them work.

1:55pm. Let me do the chores. Since I have to clear the wall of overgrowth, that will take me an extra hour each day for the next week. It is a chore, but I'll get it done.

2:30pm. It is raining lightly so I've decided to skip the wall clearing. Let me chill just a bit and then I will start the tuts.

2:35pm. Let me start.

3pm. https://youtu.be/sQbJQ8CMHjk?t=565

I've paused here so I can try cutting seams into a tube by hand and it is messed up.

3:05pm. Hmmm, ok I got something done. But is overlapping. Let me go back to the video. I should figure it out.

3:25pm. i think I sort of get it. I just managed to cut up the box properly.

With Houdini I am constantly moving between admiration and conternation at its design. This thing where I rotate the pins? Brilliant.

The part where I can't box select the pins and have to click on them one by one? Shit.

https://youtu.be/sQbJQ8CMHjk?t=1220

So this is how you can export into .obj. This tutorial is really helpful.

https://youtu.be/sQbJQ8CMHjk?t=1253
> Now we can start in an external application to paint this. Keep in mind that if you want to pain on more than one texture set, You have to assign first dummy materials to this object. But this is a process I want to show in another tutorial series when I show how to work with UDIMs and different texture sets.

https://youtu.be/N2_zFlLymX0?t=286

This is my first time seeing texture painting done. I am not sure, but I think Blender should have an inbuilt tool for this.

https://www.youtube.com/channel/UCS-qRcJcG5qyHl7uRa6nZ1Q

Pixeltrain has some interesting stuff. There is a CoffeCup tutorial that goes into UDIMs whatever those are.

4pm. Ok, let me go for the last tutorial.

https://youtu.be/TWdWvf_c9Uc?list=PLp90cx0wSyKbu7V7P_S53W1XzSfYkQwNQ
02_03 Banana - Shading & Rendering in Houdini FX

https://youtu.be/TWdWvf_c9Uc?list=PLp90cx0wSyKbu7V7P_S53W1XzSfYkQwNQ&t=161

Hmmm, normal vs bump. Which is better?

> A bump map can be thought of as an older normal map. Bump maps were used before normal maps became a thing. Bump maps are less advanced than normal maps because they can only show the height values of a texture, whereas normal maps can show angle as well—which allows them to show detail more realistically.

https://www.cgdirector.com/normal-vs-displacement-vs-bump-maps/

///

* When to Use Bump Maps

Don’t use bump maps. Just use normal maps.

From a technical point of view, bump maps aren’t as large file size-wise compared to normal maps, so if you’re really, really, really tight on the VRAM, you could potentially downgrade to bump maps to save you a couple of MBs.

But that’s a very niche reason. 99% of people don’t need to worry about that.

So yeah, just use normal maps. They’re better in pretty much every way.

///

This article really answered my question. There are some image examples and the normal maps look a lot better.

https://youtu.be/TWdWvf_c9Uc?list=PLp90cx0wSyKbu7V7P_S53W1XzSfYkQwNQ&t=379

Damn, these are a lot of gotchas. Couldn't I set it up like in Blender?

https://youtu.be/TWdWvf_c9Uc?list=PLp90cx0wSyKbu7V7P_S53W1XzSfYkQwNQ&t=402

Let me pause here. I want to try cutting up a sphere.

4:30pm. Hmm, cutting it in half does help things. I mean, you can't really unwrap it without that.

4:45pm. I am playing around with nodes. Houdini has a lot of stuff that would otherwise require addons in Blender most likely. But I've only briefly touched on UVs in Blender.

Nevermind this for now.

Let me finish the video.

4:45pm. Done.

4:50pm. https://www.youtube.com/playlist?list=PLp90cx0wSyKZujXP4ssMcYS1Rmalh9pFt
Learn Houdini VFX with Helge Maus / pixeltrain

I am thinking what to do next.

4:55pm. https://www.sidefx.com/tutorials/toothbush-project-part-01/?collection=77

There are toothbrush tutorials here. How about I go through them as well?

I do not have the patience for all of them. Just the UV and texturing stuff.

https://youtu.be/bClfXfPIajE?t=450

He talks about baking here for a bit. I think that UVs can be as complicated or as easy as I want them to be.

https://youtu.be/bClfXfPIajE?t=563

I didn't expect he would turn a toothbrush into a volume.

5:30pm. I am messing with trying to unwrap a sphere so it matched the polar projection. No, putting the seams in the right places does not give the same result.

Working with pins is extremely annoying because a lot of the time I miss my click. Also there are the usual issues with selection and snapping to grid does not work on the edges of the UV map for some reason. Things like this drive me crazy. Also turning the distortion on and off does not work until I switch back and forth between nodes. Super annoying.

https://youtu.be/bClfXfPIajE?t=836

This is awkward. Couldn't he have subdivided it more? Or remeshed it?

The quad remesher is an external SOP that requires a license. So that explains why he went all the way to volumes.

5:40pm. https://youtu.be/HMJ7EMUV2jk
Toothbrush - 06 Quick Introduction to the Houdini FX Grooming system

Let me just watch this for a bit. Houdini does everything, so I should not be surprised that it can do hair, but I am.

https://youtu.be/HMJ7EMUV2jk?t=54
> Shelf tool seem to be an indicator of your professional experience.

It goes without saying that I never use them.

https://youtu.be/Wy9yJs6Wghg?list=PLp90cx0wSyKadoPBBcMQCSwtTAMBtXPIM
Toothbrush - 10 Baking Maps in Substance Painter

Let me skip the rest of the bristle generating tutorial. Let me watch these texturing related tutorials.

Actually, no.

https://youtu.be/YFXdTfdrT4Y
Introduction to Houdini 16: Simple Procedural UVs

Let me watch more focused tutorials on UVs.

I want to get this out of the way so I can get to work on slapping textures down tomorrow.

https://youtu.be/vBKg8tkHFIE
[TUT] Easy UV Unwrapping in Houdini

Actually, let me go for this one as it is more recent.

6:25pm. It drives me insane how I can't click on a node, press F1 and get help exactly for that node.

6:40pm. Am playing around with UV nodes a lot of them do not even have documentation.

Let me go back to the tutorial.

7pm. Had to leave for lunch.

7:20pm. https://youtu.be/vBKg8tkHFIE?t=1352
> So what are UDIMs?

Finally the mystery will be revealed.

https://youtu.be/vBKg8tkHFIE?t=1539

This is not a bad idea! With this you could get a lot more coverage for any particular island.

7:30pm. https://www.youtube.com/playlist?list=PLyH0C6d0_ZdRc5s4CjM3wp82NyGYy-Qt0
Houdini for Right-Brained People

A lot stuff here. Nothing really catches my interest though.

Ok, I think I get UVs.

7:50pm. Working with the UV Flatten tool is incredibly annoying in Houdini. For some reason the clicking on it is not good enough, it has to be below and I have to click twice every time to make the tool appear. There is also no selection.

But with this experience I should be able to triangulate it with Blender.

Align vertices to U or V keeps assigning wrong edges for some stupid reason. It is maddening.

7:55pm. https://youtu.be/YFXdTfdrT4Y

Let me watch this as well.

8:10pm. https://youtu.be/YFXdTfdrT4Y?t=521

This mentions covers pelt. I played around with it, but it gave me bad results.

...It seems he did not elaborate on it for long or for what it is useful for.

8:20pm. https://youtu.be/YFXdTfdrT4Y?t=817

I am at my limit. Let me stop this here. Tomorrow I'll finish watching this (or maybe even skip it) and move on to texturing my scene.

8:25pm. There really isn't that much to this. I just have to go in there and do it.

There are a bunch of automated methods, but my options are quite limited.

Ultimately it does not matter too much what kind of UVs I get in the end. Most of the time in the real world, I'd just get the UVs and pain the model directly. Where it matters is placing existing textures down, but I can tackle that without too much toruble.

8:30pm. Right now, I am looking at how UVs respond to transforms. They don't adapt really, they end up assuming the shape is the same which leads to stretching.

This is actually a big problem, at least for things like the stalks. Just how am I going to do those automatically?

It is great that I made them from curves, but I better hope the UV project from toroidal works. Otherwise I'll have to paint each stalk individually. Well, no, I'll do a little thing with the facing shader like in Belnder and a regular color so I won't really have to put much effort into the flowers.

8:50pm. Hrrmmmm...No it won't be hard at all. For most of the objects in the scene a flat coat of paint + noise at the shader level will suffice.

The stalk will be the only troublesome thing to unwrap, but it will be very simple regardless, and anyway, it too will have a flat coat, so that does not even matter. Only the ground itself and the pool need some kind of floor texture.

8:55pm. The material node can assign a different material to each primitive.

Yeah, the question of how much I need to concern myself with UVs is a question of what kind of resolution I am giving my poly models. If I model things right, I can get away with giving the right primitives a flat color.

The situation I am in is really highly convenient. For things like games you do need to paint the body to give the different objects a color, but at the level of detail I am using at the modeling level that becomes unecessary.

9:25pm. Ah, I give up. I really wish I could go over the grid with a scultping smooth brush. It does not matter in the least. I should stop obsessing over it.

Tomorrow the plan should be clear - I need to go over the scene and give each object a flat color. After that comes the micro detail using the noise patterns.

UVs I will only need for things that I intend to texture using downloaded textures.

Actually let me try one thing. I want to see if I can get the smooth node to work better.

9:40pm. No, no I can't I simply lack the tools to do it.

Cutting seams is one thing, but it is clearly doing the wrong thing when it comes to unwrapping a sphere. For the sphere it should unwrap it and then relax the edges so that they are the same size. Sculpting tools in Blender can do it, but I simply have no options when it comes to doing that in Houdini.

9:50pm. The auto UVs are pretty decent under the assumption that I am painting them myself. They are absolutely awful for somethling like a sphere though

9:55pm. Let me close here. Tomorrow I am going to paint the whole scene. After that I am going to refine it using noise. I do not need to do all fo this, but since it is my first somewhat complex scene, I want to do a good job of it.

I think that given a couple of days of tutorials, and a couple of days of working on the scene should be enough to finish it. So about a week. After that I can move to sculpting Luna, studying height maps or whatever else."

---
## [ColdCalzone/Bread-Bread-Breadvolution-Extra-Toasty](https://github.com/ColdCalzone/Bread-Bread-Breadvolution-Extra-Toasty)@[1eaab99ca2...](https://github.com/ColdCalzone/Bread-Bread-Breadvolution-Extra-Toasty/commit/1eaab99ca278c1a6af579e1fae406a3971cd28f1)
#### Saturday 2022-02-19 20:57:41 by ColdCalzone

Made mobile-friendliness changes to the game

GOD I HOPE THE TOUCH DETECTION IN GAME.GD JUST WORKS. GOD FUCK GOD PLEASE GOD PLEASE GOD.

---
## [mpapka/helloworld](https://github.com/mpapka/helloworld)@[f5c575cde4...](https://github.com/mpapka/helloworld/commit/f5c575cde42aa03ece48a41823473331bd3cef64)
#### Saturday 2022-02-19 21:21:37 by Michael E. Papka

Bharat Kale
  01/04/2022(5.0) Completed the implementation to visualize each molecule thumbnail as SVG rather than an image. This made thumbnails very clear after zoom-in. Also finished highlighting selected substructures during zoom operations. 
  01/06/2022(4.0) Started working on making the chemistry vis work accessable via vis server. Using nginx+gunicorn+django
  01/07/2022(5.0) Fixed the problem of not being able to access the chemistry vis stuff from vis server. Having gunicorn in between nginix and django did the trick. Started working on writing part. 
  01/11/2022(4.0) Implemented first version of expand operation. Completed the background part and was able to have all the expand results availble for the d3 code and visulized them in a seprate div. Need to work on proper transition to present the results to user.
  01/12/2022(6.0) Completed the expand operation transitions. Continuing on wrting part.
  01/14/2022(5.0) Continued on wrting - literature on graph visualization. Spent some time of ddiLab website (setup for adding custom publication types and added my masters thesis project page). 
  01/18/2022(2.5) Review of papers on Zoom interaction (focus+context) in InfoVis.
  01/19/2022(3.0) Summarized few papers on focus+context interaction and collected more papers on tree and graph vis techniques.
  01/20/2022(5.5) Updated the interactions in the scaffold graph to highlight direct connections on hover and show the results of upper and lower operations of selected compound propagated across all visible levels on click. started working on independently sorting levels.
  01/21/2022(6.0) Completed sorting with 3 stages (Unsorted - as data comes in, Ascending by attribute value, Descending by attribute value). Bug fixes to make interaction behaviour consistent when the view is zoomed into or not.
  01/22/2022(1.0) Tests on the vis with various scenarios to identify bugs and inconsistencies
  01/23/2022(4.0) More bug fixes from previous testing- especially with combination of zoom, sort, and any graph operation.
  01/24/2022(5.0) Attended lab meeting. Updates to the vis server on plick. Worked on fixing the performance lag during zoom operations.
  01/25/2022(5.0) Worked on writing about the chemical graph visualization and supported interactions. Fixed the bug found during the demo(@ last lab meeting).
  01/26/2022(6.0) Meeting with Dr. Papka and Dr. Sun. Started drafting content for VIS paper. Reading more related papers. Continued with preparing the video demo.
  01/27/2022(5.0) Worked on the layout and high level contents of each section in the paper. Spend some time on preparing material on teaching D3.
  01/28/2022(3.0) Discussion on improvements and new features to the scaffolg graph vis, user study creation. Read case studies from collected interdisciplinary vis papers.
  01/30/2022(2.0) Preapred slides for the weekly meeting. Worked on identifying and drafting contributions for the vis paper.
  01/31/2022(5.0) Attended lab meeting. Worked on writing for the vis paper.
  02/01/2022(5.0) Continued on reading and looking into user studies on interdisciplinary work. Worked on lab stuff - changing UPS batteries in the lab.
  02/02/2022(5.0) Attended meeting with Dr. Papka and Dr. Sun. Spent more time on the paper writing for the chemistry vis work.
  02/04/2022(5.0) Added high level points in each section showing the flow of the paper. Will work on expanding each section. Helped Tim (Chem Dept.) to fix running py script on hopcroft.
  02/05/2022(5.0) Read all the material shared by Austin to understand what is querying of large chemical databases mean and how do various works use the results of queries for their analysis.
  02/06/2022(3.0) Helped Tim with debugging issues related to nexus package on hopcroft. Prepared and sent questions to Austin, on querying other databases, to discuss during meeting on 02/07.
  02/07/2022(5.0) Meeting with Austin. Started working on incorporating database querying as first step to expand the graph and then fall back to SGUser when necessary. Looking into GraphQL+Neo4j with django
  02/08/2022(5.0) Prepared a list of actionable items from the recording of the meeting with Austin. Started working on encoding other attributes on nodes.
  02/09/2022(5.0) Helping Tim, debugging slurm issues on Hopcroft. Completed encoding "synthetic accesibility score" attribute on the nodes in chemical vis. Created accounts on Hartley, for the new students.
  02/10/2022(5.0) Worked on the vis paper - introduction section and motivation for the work. Started looking into adding interactions for sorting based on selected attribute. 
  02/13/2022(5.0) Completed the introduction section for the vis paper. Also worked on adding database queries as the first step, before using the transformer model.
Wesley Kwiecinski
  01/05/2022(2.5) Worked with Justin on dynamically drawing lines, decided to switch up approach and statically draw lines using the output csv files (Computer broke down after this so I was not able to work for the rest of the week)
  01/10/2022(2.0) Working with Justin, made line drawing in separate script using csv coordinate files, successful implementation
  01/12/2022(1.5) Added colors to lines in line draw script to indicate direction to and from the CS building, added script to pedestrian detection, unforseen issue found and will look into next time
  01/13/2022(1.5) Fixed the line drawing script and made minor adjustments to pedestriant detection, reran to make sure there were no issues
  01/18/2022(0.5) Discussed current implementation of drawing trajectories with Justin, waiting for response from Dr. Bharti to proceed.
  01/21/2022(2.0) Meeting with Dr. Bharti to discuss current problems with pedestrian detection, worked with Justin to discuss implementation for hourly image outputs for trajectories, created github repo for code, updated readme
  01/22/2022(2.0) Worked on implementing hourly plot_lines script with Justin
  01/23/2022(1.0) Fixed bugs in hourly line plot script
  01/24/2022(2.0) ddilab meeting, discussed ways to fix pedestrian detection issues w/ Justin
  01/26/2022(2.0) Worked with Justin to test various max score thresholds for pedestrian detection. Ran thresholds of .45, .55, .58, .6, .65, and .8.
  01/27/2022(1.0) Worked with Justin, tested various other changes, like area of bounding boxes. Noticed that re-identification issues often occur when people move offscreen. Also we figured that the low detection threshold for the object detection may be causing more issues on top of that.
  01/28/2022(2.0) Checked the results of the new threshold for object detection that Justin ran, adjusted the area bounding box in pedestrian detection to count smaller images of people, started work on a check edge function. Current plans are to check when a person goes off screen and to check the distance between people to hopefully solve re-id problem
  01/29/2022(1.0) Discussing re-id issue fixes with Justin, reimplementing check proximity function
  01/30/2022(2.0) More testing and theorycrafting, unsuccessful, found bad data examples for meeting with dr bharti, Unsure how to proceed so waiting for meeting, (W/ Justin)
  01/31/2022(1.0) ddilab meeting
  02/04/2022(3.0) Sage team meeting, updating github repo with sources and other information, printing logs to pinpoint re-id errors
  02/05/2022(2.0) Removing unnecessary data from logs, collecting more logs for Dr. Bharti, analyzing where code is going wrong (w/ Justin)
  02/06/2022(1.0) Brainstorming changing to fix re-id, added user input to run specific days via cl args
  02/07/2022(2.0) Ddilab meeting, fixing small bugs in pedestrian detection script (fixing file paths), meeting w/ Dr Bharti about logs
  02/09/2022(1.0) Meeting prep, meeting w/ new Sage members
  02/11/2022(2.0) Reviewed pedestrian detection code w/ Dr. Bharti, Justin, tried making adjustments to script to fix same-id issue
  02/12/2022(2.0) Documenting w/ Justin, fixing same ID in 1 frame issue
  02/13/2022(1.5) Working with Justin to adjust values, add y limit for re-id, started implementing check_proximity with max_score
  02/14/2022(2.0) Ddilab meeting, working with Justin to implement distance checks, popping old data in frame queue -> less re-id problems so far
  02/15/2022(1.0) Justin and I went through the new and old data to compare, found a large bug with the current script in the process
Justin Derus
  01/05/2022(2.5) Tried dynamically drawing trajectories - bad idea, got csv data into a script using Import csv
  01/10/2022(1.5) Created rough draft of trajectory images to see hotspots
  01/14/2022(2.0) Updating pedestrian code to find trajectories - running new scripts for optimal data
  01/16/2022(3.0) Reviewed opencv functions to see if there was a more efficient way of dealing with trajectory calculations, used opencv to add some quality of life things to our scripts (legends, colors, etc). 

All submissions from 12/17 to 1/17 are from over winter break, and were about improving upon pedestrian detection code and its sub programs.
  01/18/2022(0.5) Got 2 ways to find the trajectories, shared results with Dr. Bharti and waiting for his response
  01/21/2022(2.5) Met with Dr. Bharti and Wesley to discuss current issues, wrote up psuedocode to find hourly trajectories, set up a GitHub repo 
  01/22/2022(2.0) Worked on new plot lines script with Wesley 
  01/24/2022(3.0) Finishing up hourly trajectory script with Wesley, ddiLab weekly meeting
  01/26/2022(1.75) Ran tests to narrow down the re-id problem - still needs more testing with object detection and box areas
  01/27/2022(1.25) Testing new thresholds to try and fix the re-id problems
  01/29/2022(1.0) Finished up testing the new threshold ideas we had for the re-id problem, unsuccessful - starting new approach next week
  01/30/2022(3.0) Testing and theory crafting with Wesley to find solutions to re-id problems, need to meet with Dr. Bharti to discuss the problems further - will happen Tuesday.
  01/31/2022(1.0) ddiLab meeting
  02/04/2022(3.0) ddiLab sage team meeting, updating github repo, creating data logs to find re-id problem
  02/05/2022(2.0) Organized image_label_xmls directory on hartley, altered logs with wesley
  02/06/2022(2.0) Checked and updated logs for meeting with Dr Bharti this week. Updated script to work off command line arguments
  02/07/2022(2.0) ddiLab meeting, updates on script for use of command line arguments, met with Dr Bharti and Wesley - another meeting scheduled for tomorrow - set up sage meeting to discuss our code with newcomers and give them any helpful websites
  02/09/2022(1.5) AoT meeting with new members, getting topics for meeting prepped and finding useful material, getting new people set up on hartley and github, reviewing code for Friday meeting with Dr. Bharti and Wesley.
  02/11/2022(2.0) Met with Dr. Bharti and Wesley to go over logic of re-id functions, commented functions to make the logic more clear, looking in depth at re-id functions with Wesley trying to fix the re-id error where 2 people have the same ID.
  02/12/2022(3.0) Updating comments to make code more readable and easier to understand, same id in frame fixed, fixed layering of bounding boxes and person id
  02/13/2022(1.5) Testing fixed double id's with new parameters and functions to see if it resolves the deeper re-id issue
  02/14/2022(2.0) ddiLab meeting, progress with re-id with Wesley - popped old data in frame queue which fixed certain cases of re-id errors
  02/15/2022(1.0) Comparing old data with new, found plateau problem with ids due to new additions to code
Julia Finegan
  01/19/2022(1.0) watched some python tutorials, and have a very good handle on all of the basics now :)
  01/20/2022(1.2) Looked at videos and articles about arrayOfThings, waggle, and sage continuum. Also learned more python. 
  01/24/2022(1.0) More python practice
  01/25/2022(1.0) Python tutorials
  01/26/2022(1.0) Pandas
  01/27/2022(2.0) Pandas and numpy 
  01/28/2022(2.0) Numpy and pytorch tutorials 
  01/29/2022(2.5) Pytorch and deep learning
  01/31/2022(2.5) Machine learning and convolutional neural networks
  02/01/2022(3.0) YOLO, and compiling readings/tutorials
  02/02/2022(2.0) YOLO, submitting info for ddi lab, and reading articles comparing different object detection methods. Along with many tangents related to them
  02/06/2022(1.0) Watched video from meeting 
  02/09/2022(3.0) Met with Wesley and Justin. Worked on setting EDU node
  02/10/2022(1.4) Edu node setup
  02/13/2022(2.5) Worked on SageEDU node
  02/14/2022(1.0) SageEDU and Hartley setup
Francisco Lozano
  01/19/2022(1.0) Learned Python and completed my ddiLab site content
  01/20/2022(1.0) Learned and practice python
  01/21/2022(2.0) Learned and Practiced Python
  01/22/2022(2.0) Learned and Practiced Python
  01/23/2022(2.0) Practiced and Learned Python
  01/24/2022(1.0) Practiced and Learned Python
  01/27/2022(1.0) Learned and practiced python
  01/28/2022(2.0) learned and practiced python
  01/29/2022(2.0) learned and practice python
  01/30/2022(2.0) learned and practiced python
  01/31/2022(1.0) practiced and learned python
  02/01/2022(1.0) Learned and Practiced Python
  02/02/2022(1.0) Learned and Practiced Python
  02/03/2022(1.0) Learned and Practiced Python. Also looked at WSL
  02/04/2022(2.0) Learned and Practiced Python. Also looked at the AOT meeting recording
  02/05/2022(2.0) Learned and Practiced Python
  02/06/2022(2.0) Saw the aot_sage meeting recording and learned/practiced python
  02/09/2022(4.0) Set up the jetson nano
  02/11/2022(1.0) played around with the EDU node
  02/12/2022(2.0) played with the EDU node
  02/14/2022(1.0) I build a better setup for the Jetson nano since it was getting in the way in my desk
  02/15/2022(2.0) Connected the camera to the EDU node and played with the sample programs in the git repo
Emily Brown
  01/18/2022(2.0) Completed shareable versions of Spotify.ipynb and Audio_Visualizer.ipynb for Colab, began testing and troubleshooting Data_Explorer.ipynb on Colab
  01/19/2022(2.0) Finished adjusting Data_Explorer.ipynb for Colab, met with Brenda to discuss plans
  01/20/2022(2.0) Made adjustments to Spotify.ipynb as discussed with Brenda, cleaned up Data_Explorer.ipynb and shared with Brenda
  01/21/2022(2.0) Set up branch in SageAudio repo for Colab notebooks, started testing and troubleshooting Genres_Intro.ipynb and Genres_Full.ipynb
  01/26/2022(0.5) Met with Brenda to discuss current progress with the students and future updates
  01/27/2022(2.0) Finished two more notebooks (genres_intro.ipynb and genres_full.ipynb) for Google Colab, shared with Brenda and pushed to github
  01/28/2022(2.5) Explored and experimented with Google Colab's Github integration
  01/29/2022(1.0) Designed and tested hypothetical workflow for using Github with Google Colab
Joseph Lenz
  01/11/2022(3.0) Continued using Python tutorials
  01/17/2022(3.0) Learning Python using tutorials
  01/19/2022(1.0) Continued with Python Tutorial
  01/20/2022(3.0) Continued tutorial, started to practice simple projects
  01/23/2022(1.0) Continued with Python tutorials
  01/24/2022(1.0) Continued with python tutorials
  01/25/2022(3.0) Continued with Python tutorials, began practicing with smaller projects and such
  01/26/2022(1.5) Continued working with smaller projects, look at using tkinter and django
  01/29/2022(3.5) Read up on assorted Python subjects, worked on smaller projects for practice
  02/01/2022(4.0) Installed and learned about wsl and set it up with vsc. Also, researched different web servers such as apache
  02/02/2022(2.5) Begin researching apache specifically, and learning how to set it up on linux
  02/03/2022(2.5) Continued working with apache, watched and read about different configs for the web server
  02/04/2022(1.0) AOT Sage meeting
Ivan Popov
  01/21/2022(2.0) Studied python using this video: https://www.youtube.com/watch?v=XKHEtdqhLK8
  01/22/2022(2.0) Continued studying and learning python
  01/23/2022(3.0) Spent 2 hours studying python, and 1 hour reviewing what I learned over the week
  01/24/2022(1.0) Studied Python 
  01/25/2022(1.0) Studied Python
  01/26/2022(2.0) Studied Python, met with Dr Papka, looked into machine learning and other python programs
  01/27/2022(1.0) Studied Python
  01/28/2022(1.0) Studied Python
  01/29/2022(1.0) Studied Python 
  01/30/2022(1.0) Studied Python 
  02/04/2022(2.0) Met with the team and talked about the different projects.
Looked at introductory material for Linux system administration 
  02/05/2022(3.0) Continued working with Python.
Watched https://www.youtube.com/watch?v=qAMWG86sEm8
Reviewed material from previous UNIX course (330) taken at NIU
  02/06/2022(3.0) Used the day to continue working with Python
  02/09/2022(2.0) Met with AoT team, introductory meeting about basic functions of the team and how to get started. Met with Dr Papka, spoke about the initial steps to take regarding the website. Researched a bit about web servers 

  02/12/2022(5.0) Reviewed and learned Linux commands to brush up on them

Resources:
https://www.youtube.com/watch?v=ZtqBQ68cfJc - linux commands
https://www.freecodecamp.org/news/the-linux-commands-handbook/ - handbook 
  02/13/2022(3.0) Studied basic web server concepts. Looked at to work with html and create a website. watched nginx and apache tutorials 

Resources:
https://www.youtube.com/watch?v=9J1nJOivdyw - web server concepts
https://www.youtube.com/watch?v=NQP89ish9t8 - basic website stuff
Jacob Fitzenreider
  01/20/2022(4.0) Went through Python tutorials on Codecademy to brush up on my Python skills
  01/22/2022(3.5) Went through Python tutorials/brushed up on Python skills
  01/24/2022(2.0) Read about audio processing, and potential audio libraries to work with in Python
  01/27/2022(4.0) Continued Python Learning with Codecademy tutorials/class
  01/29/2022(4.0) More Python brush-up with Codecademy tutorials and course. 
Hal Brynteson
  01/21/2022(2.5) Research/installation of unity with the webXR plug-in
  01/24/2022(4.0) Lab meeting, more webXR and Unity, working on pipeline tutorial (for Hopcroft), documenting the Houdini situation (.geo files vs. v-ray proxies)
  01/25/2022(1.0) Snow/Vive maintenance, looking into plug-ins for adding VR capabilities to our pipeline (for both Maya and Houdini)
  01/26/2022(2.0) Hopcroft pipeline tutorial, ParaView section complete
  01/31/2022(3.5) Lab meeting, Hopcroft tutorial, digging into some blender tools for adding VR to the pipeline 
  02/02/2022(4.0) Call with maya-paraview channel team to discuss where we're at and our next steps, also pulling together a resource list of where we want to concentrate our efforts 
  02/04/2022(2.0) Following up on some potentially useful tools for expanding the pipeline capabilities (Blender, Unreal, Unity)
  02/09/2022(4.0) Call with vis channel, getting Houdini set up with licenses, looking into instancing for Houdini to render on Cooley
  02/11/2022(2.0) Working with Ina on the ParaView OpenVR plug-in and running remote on Cooley
Nestor Alvarez-Popoca
  01/24/2022(1.0) Weekly meeting
  01/28/2022(9.0) - Worked on creating a workflow between 3D CAD models and Unity for potential VR/AR projects.
- Developing VR application for 3D CAD models.
- Documented work done.
  01/31/2022(1.0) Ddilab Weekly meeting
  02/05/2022(7.5) Reviewed the process of importing and converting a dataset from Paraview into a vrmesh and then manipulated it in Maya.
  02/09/2022(1.5) Meet with Joe, Ina, Hal, Thom, Silvio and Victor. We discussed the Paraview-Maya Pipeline and brainstormed ideas for making it better.
Ina Murphy
  01/28/2022(10.0) Reading and researching about Vray materials, rendering, lighting for Maya. Test rendering Star data still images. Preparing more Before /After star data renderings (smoothing). Rendered a few more images before and after.
  02/04/2022(10.0) documentation for maya, vray pipeline, looking for ways to modify 3d vrmesh without losing RGB data, reading and documenting on vray rendering. Test rendering with different vray settings
  02/11/2022(10.0) Vray clipper, test rendering with vray clipper, vr paraview testing at the lab, meeting ddilab, meeting maya-paraview team.

---
## [christianheinrichs/rbc](https://github.com/christianheinrichs/rbc)@[018c6cb506...](https://github.com/christianheinrichs/rbc/commit/018c6cb5069d9ba4cf10f19c411cde256ad0bc72)
#### Saturday 2022-02-19 21:23:04 by Christian Heinrichs

- Add ‘Heroine’s Quest: The Herald of Ragnarok’
- Add ‘SuperTux’
- Add ‘The Mystery of the Druids’
- Add ‘Through the Woods’
- Add TODO file
- Make variable names more descriptive
- Blood Omen: Legacy of Kain - Add missing registry key check
- Call of Cthulhu: Dark Corners of the Earth - Delete device files
- Diablo (Classic): Registry key support
- Diablo: Hellfire - Registry key support
- Painkiller: Add third registry registry key, add missing registry key check
- S.T.A.L.K.E.R. Чистое Небо: Fix directory path name, add registry key support
- The Longest Journey: Backup registry key
- Wiedźmin: Move section down to ensure alphabetical order
- Make file existence check more strict by using wildcards
- Add licensing information
- Add .err and .out files to exclusion list

---
## [JulianUO/UOAscension-SphereX](https://github.com/JulianUO/UOAscension-SphereX)@[82e1dc29a0...](https://github.com/JulianUO/UOAscension-SphereX/commit/82e1dc29a07a3273b97a255f0c8214ac3a6614a8)
#### Saturday 2022-02-19 21:30:10 by drk84

Fixed: Reagents consumed on magical skill abortion (issue #605). (#638)

-Fixed: RegenHits, RegenMana, RegenStam and RegenFood are not saved when their value is 1.
-Added: @SpellEffectTick and @EffectTick triggers, they are fired when a spell memory has one or more charges(more2) and the spellflag_tick
 ON=@SpellEffectTick / ON=@EffectTick
 Default Object: The object that is going to be affected.
 Src: The object that is going to be affected.
 ARGN1: Spell Id
 ARGN2: Spell Level
 ARGO: The spell memory.(Argo.link holds the caster UID)
 local.charges (R/W) = How many charges are left on the spell memory, this will be automatically decreased by 1 at the end of the method execution. Default value is 1.
 local.delay (R/W) = How many seconds until the next spell effect tick. Default value is 5 seconds.
 local.effect (R/W) = The effect value of the spell, harmful or beneficial (if SPELLFLAG_HEAL is enabled).
 local.damagetype (R/W) = The damage type of the spell, if you are making a custom spell you must set a value otherwise the spell will not cause damage.
 return 1: Destroy the spell memory and block the spell execution.
 return 0: If the spell has the flag SPELLFLAG_SCRIPTED blocks the spell execution

 These triggers fires on the following spells and any custom spells with the SPELLFLAG_TICK:
  Poison: You can now change the damage and damage type by changing the local.effect and local.damage value in these triggers.
  Strangle and Pain Spike: You can now change the damage and damage type in these triggers.
  Regeneration: A Sphere custom spell, you can change the healing value by changing the local.effect value.
  Hallucination: A Sphere custom spell, you can change the duration of the hangover by using local.charges and local.delay.
  Alchool: Unlike in real life, you can change the duration of the hangover by using local.charges and local.delay.
  Custom Spells: Simply add SPELLFLAG_TICK to the spell spellflags. By default every spell memory starts with one charge.
   Spells with SPELLFLAG_HARM and local.damagetype set will cause damage every local.delay seconds.
   Spells with SPELLFLAG_HEAL will heal hitpoints every local.delay seconds.
   Remember that is not mandatory to use  SPELLFLAG_SCRIPTED to make a custom spell, you can just use a spell id higher than 1055, usually i choose 2000.
 It's recommended to update the spells scripts file and sphere defs file, alternatively just add the following line, in the spellflag section in defs.scp/sphere_defs.scp:
  spellflag_tick      080000000  // A spell is going to tick and causing an effect.
 And add SPELLFLAG_TICK to the following spells: Poison, Strangle, Pain Spike, Regeneration, Hallucination.
-Updated SphereCrypt.ini

---
## [IIvec/Stockfish](https://github.com/IIvec/Stockfish)@[cb9c2594fc...](https://github.com/IIvec/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Saturday 2022-02-19 21:37:45 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [cannnAvar/TheyMadeMe](https://github.com/cannnAvar/TheyMadeMe)@[3910854b08...](https://github.com/cannnAvar/TheyMadeMe/commit/3910854b0846b233612abb27bcfef032e84404d4)
#### Saturday 2022-02-19 23:53:36 by can bartu avar

fuck you alll mother fuckers I fuck the code I don't know What to to FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK

---

