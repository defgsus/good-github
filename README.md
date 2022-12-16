## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-15](docs/good-messages/2022/2022-12-15.md)


2,180,036 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,180,036 were push events containing 3,277,219 commit messages that amount to 265,349,851 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [CurlySparkle/ARC9-GSR](https://github.com/CurlySparkle/ARC9-GSR)@[328b88e54b...](https://github.com/CurlySparkle/ARC9-GSR/commit/328b88e54b437e3cbf64eee221fa5fbc99609554)
#### Thursday 2022-12-15 02:18:15 by May Lian

Massive shitstorm on the G3

This is such a pain in the ass to work with

---
## [IgnGrillo/TimerBattler](https://github.com/IgnGrillo/TimerBattler)@[cbe31e71d1...](https://github.com/IgnGrillo/TimerBattler/commit/cbe31e71d130b535f80c698813248288488022aa)
#### Thursday 2022-12-15 02:18:19 by IgnGrillo

Update MousePresenter, adding three new test to check if there are any Hovering events needed to be called.

My God, I am sorry for my sins with all my heart. In choosing to do wrong, and failing to do good, I have sinned against you whom I should love above all things. I firmly intend, with your help to do penance, to sin no more,and avoid whatever leads me to sin. Our savior Jesus Christ suffered and died for us. In his name, my God, have mercy.

---
## [vdavalon01/cockroach](https://github.com/vdavalon01/cockroach)@[a30fb1438a...](https://github.com/vdavalon01/cockroach/commit/a30fb1438a6f1f99ebf2a27695e89d4b4e51cf8f)
#### Thursday 2022-12-15 05:42:20 by craig[bot]

Merge #93153 #93325 #93354 #93545 #93557 #93563 #93618

93153: rttanalysis: don't count leasing the database desc r=andreimatei a=andreimatei

A bunch of rtt-analysis tests were counting a request for leasing the database descriptor. This is not interesting. This patch makes the test framework lease it first through a "USE" statement.

The number of KV requests required for leasing is currently mis-counted. We count 1, but in reality it's 4. A different patch will correct the miscounting that, at which point that would be too significant for the tests.

Release note: None
Epic: None

93325: multitenant: retain range splits after TRUNCATE for secondary tenants r=knz a=ecwall

Fixes #69499
Fixes #82944

Existing split points are preserved after a TRUNCATE statement is executed by a secondary tenant.

Release note: None

93354: tracing: disallow children of sterile span with different Tracer r=andreimatei a=andreimatei

Before this patch, creating a "child" of a sterile span with a different Tracer than the one used to create the sterile span was tolerated - on the argument that sterile spans don't actually get children (the would-be child span is created as a root), so the arguments for not allowing a children to be created with different tracers don't apply. At the same time, creating a child of a noop span with a different Tracer than the noop span's Tracer was documented to not be allowed. In practice, it was, because the code was confused [1].

This patch disallows creating children of sterile spans with a different tracer, for consistency with all the other spans. The patch also makes it a panic for the children of noop spans to be created with a different Tracer.

This is all meant as a cleanup / code simplification.

[1] WithParent(sp) meant to treat sterile spans differently than noop spans but it was using sp.IsSterile(), which returns true for both. As such, it was unintentionally returning an empty parent option. startSpanGeneric() meant to check the tracer of parent noop spans, but it was failing to actually do so because it was going through the opts.Parent.empty().

Release note: None
Epic: None

93545: sql: make SHOW RANGES FOR TABLE include all indexes r=ajwerner a=knz

Informs #80906.
Fixes #93546.
Fixes #82995.

Release note (backward-incompatible change): `SHOW RANGES FOR TABLE`
now includes rows for all indexes that support the table. Prior to
this change, `SHOW RANGES FOR TABLE foo` was an alias for `SHOW RANGES
FOR INDEX foo@primary`. This was causing confusion, as it would miss
data for secondary indexes. It is still possible to filter to just the
primary index using `SHOW RANGES FOR INDEX foo@primary`.

The statement output now also includes the index name.

93557: syntheticprivilegecache: scan all privileges at startup  r=ajwerner a=ajwerner

#### syntheticprivilegecache: move caching logic out of sql
This is a pure refactor to move the logic for caching synthetic privileges
from the sql package. This will make it easier to add features later.

#### syntheticprivilegecache: scan all privileges at startup 


Fixes https://github.com/cockroachdb/cockroach/issues/93182

This commit attempts to alleviate the pain caused by synthetic virtual table
privileges introduced in 22.2. We need to fetch privileges for virtual tables
to determine whether the user has access. This is done lazily. However, when a
user attempts to read a virtual table like pg_class or run SHOW TABLES it will
force the privileges to be determined for each virtual table (of which there
are 290 at the time of writing). This sequential process can be somewhat slow
in a single region cluster and will be very slow in an MR cluster.

This patch attempts to somewhat alleviate this pain by scanning the table
eagerly during server startup.

Release note (performance improvement): In 22.2 we introduced privileges on
virtual tables (system catalogs like pg_catalog, information_schema, and
crdb_internal). A problem with this new feature is that we now must fetch those
privileges into a cache before we can use those tables or determine their
visibility in other system catalogs. This process used to occur on-demand, when
the privilege was needed. Now we'll fetch these privileges eagerly during
startup to mitigate the latency when accessing pg_catalog right after the
server boots up.

93563: pgwire: handle decoding Geometry/Geography in binary r=rafiss a=otan

Resolves #81066
Resolves #93352

Release note (bug fix): Previously, CockroachDB would error when receiving Geometry/Geography using binary parameters. This is now resolved.

93618: cli,cliccl: move some mt commands to cliccl r=ajwerner a=ajwerner

Part of #91714

Epic: none

Release note: None

Co-authored-by: Andrei Matei <andreimatei1@gmail.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>
Co-authored-by: Andrew Werner <awerner32@gmail.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a9fda932e2...](https://github.com/tgstation/tgstation/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Thursday 2022-12-15 05:48:22 by Tim

Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u 
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.


![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[b476bce004...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/b476bce004f741ccd2fd69526292b5cd1fa4d4c9)
#### Thursday 2022-12-15 06:45:07 by SkyratBot

[MIRROR] Fishing-themed Escape Shuttle [MDB IGNORE] (#18113)

* Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

* Fishing-themed Escape Shuttle

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[81ca11b95a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/81ca11b95a59d5cf0eb0a066454b2903f4859503)
#### Thursday 2022-12-15 06:50:56 by SkyratBot

[MIRROR] Basic Mob Carp: Retaliate Element [MDB IGNORE] (#18030)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---
## [GoatersBro/HEXAPAWN_BOT](https://github.com/GoatersBro/HEXAPAWN_BOT)@[c1912257cb...](https://github.com/GoatersBro/HEXAPAWN_BOT/commit/c1912257cbbf03c3b1b814255c7e5fbfd4f6db5c)
#### Thursday 2022-12-15 07:26:15 by GoatersBro

Things are getting weird

Holy shit its a miracle that this code works

---
## [HR0N/wms](https://github.com/HR0N/wms)@[8bd616a05d...](https://github.com/HR0N/wms/commit/8bd616a05d09a1342db0f877be438d760f28c61d)
#### Thursday 2022-12-15 08:30:59 by HR0N

love github token update <3; just kidding... FUCK YOU!..

---
## [warmchang/procps](https://github.com/warmchang/procps)@[9773c56add...](https://github.com/warmchang/procps/commit/9773c56add6446d418c0677f306c8771356f0c01)
#### Thursday 2022-12-15 08:42:41 by Jim Warner

top: refactored for correct multi-byte string handling

When this project first began implementing translation
support nearly 6 years ago, we overcame many 'gettext'
obstacles and limitations.  And, of course, there were
not any actual translations at the time so our testing
was quite limited plus, in many cases, only simulated.

None of that, however, can justify or excuse the total
lack of attention to top's approach to NLS, especially
since some actual translations have existed for years.

When the issue referenced below was raised, I suffered
immediate feelings of anxiety, doubt and pending doom.
This was mostly because top strives to avoid line wrap
at all costs and that did not bode well for multi-byte
translated strings, using several bytes per character.

I was also concerned over possible performance impact,
assuming it was even possible to properly handle utf8.

But, after wrestling with the problem for several days
those initial feelings have now been replaced by guilt
over any trouble I initially caused those translators.

One can only imagine how frustrating it must have been
after the translation effort to then see top display a
misaligned column header and fields management page or
truncated screens like those of help or color mapping.
------------------------------------------------------

Ok, with that off my chest let's review these changes,
now that top properly handles UTF8 multi-byte strings.

. Performance - virtually all of this newly added cost
for multi-byte support is incurred during interactions
with the user. So, performance is not really an issue.

The one occasion when performance is impacted is found
during 'summary_show()' processing, due to an addition
of one new call to 'utf8_delta()' in 'show_special()'.

. Extra Wide Characters - I have not yet and may never
figure out a way to support languages like zh_CN where
the characters can be wider than most other languages.

. Translated User Name - at some future point we could
implement translation of user names. But as the author
of the issue acknowledged such names are non-standard.
Thus task display still incurs no new multi-byte costs
beyond those already incurred in that escape.c module.

For raising the issue I extend my sincerest thanks to:
Göran Uddeborg

Reference(s):
https://gitlab.com/procps-ng/procps/issues/68

Signed-off-by: Jim Warner <james.warner@comcast.net>

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[7f1e80ca3d...](https://github.com/Nanu308/cmss13/commit/7f1e80ca3dd4800f54b5ff4dc3663dd1f804c28c)
#### Thursday 2022-12-15 08:48:21 by carlarctg

MIDIs are now either 'Meme' or 'Atmospheric', players can toggle each option (#1939)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Updated savefile number from 19 to 20. Meme and atmospheric preferences
are enabled by default.

Admin sounds now need a selection between 'Meme' or 'Atmospheric' type.
Ideally, this would let players decide if they want to listen to hijack
or first drop songs without needing to listen to GOOD HITS or whatnot.

I am uncertain about the savefile bit of code. I don't fully understand
it.

As stated I don't care about GBP, so if the tags are teechnicallly
incorrect go ahead and change them or whatever.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.

As it says. Lots of people hate the memes and just want to listen to the
cool atmosphere. This is of course dependant on staff selecting the
right option, which is sometimes up to opinion, but I fully trust staff
will be able to handle this subjective affair correctly.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
refactor: Updated savefile number from 18 to 19. Meme and atmospheric
preferences are enabled by default.
admin: Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [EyeDeck/Advent-of-Code](https://github.com/EyeDeck/Advent-of-Code)@[e5b9670214...](https://github.com/EyeDeck/Advent-of-Code/commit/e5b96702146b501bc460777da337f4019193e0f5)
#### Thursday 2022-12-15 08:49:25 by EyeDeck

Solve 2022 day 15

00:36:19 (2020) / 03:29:19 (5401)
Whew boy, that was a tough one. This code barely even works.

My part 1 solution was just awful, I don't want to talk about it.

Part 2 was a little better (though still god-awfully slow and memory hungry), I made a list of line segments for each diamond the on x axis, de-overlapped the line segments, and recorded the coordinate of every 1-wide gap. I then repeated the same thing on the y-axis, and when one of those coordinates overlapped one of the x-axis ones, that one is our answer.

---
## [Dan1ss1mo/Cataclysm-DDA](https://github.com/Dan1ss1mo/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/Dan1ss1mo/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Thursday 2022-12-15 09:14:09 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [tpetric7/yuzaR-Blog](https://github.com/tpetric7/yuzaR-Blog)@[0e2122af7d...](https://github.com/tpetric7/yuzaR-Blog/commit/0e2122af7da4238743281d2d5102c2e703d3cb60)
#### Thursday 2022-12-15 09:21:04 by yuryzablotski

new post fix: stupidely, I needed to add two last Rmd scripts to QR post, because for whatever reasen, it needed them in there ... starts to get annoying actually, that it does not just fucking work!

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Thursday 2022-12-15 09:42:56 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [avar/git](https://github.com/avar/git)@[a8b1ccd9b7...](https://github.com/avar/git/commit/a8b1ccd9b7fe69fc5d329f6820244ee644c10887)
#### Thursday 2022-12-15 10:49:21 by Ævar Arnfjörð Bjarmason

[TODO t0450] submodule: make it a built-in, remove git-submodule.sh

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

It would be better to use run_command() here directly to avoid copying
"args" and "env" copying, but let's use run_command_v_opt_cd_env()
instead to optimize for subsequent diff size. By using our own "struct
strvec args" we can push to "&args", not a "&cp.args". Eventually
we'll stop invoking "submodule--helper" as a sub-process, and avoid
the churn of converting all of "&cp.args" to "&args".

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[eac0dcc3a9...](https://github.com/rHermes/adventofcode/commit/eac0dcc3a90544b2496ddf1f16a85b6b407dc76a)
#### Thursday 2022-12-15 10:54:49 by Teodor Spæren

2022 Day 15

FUUUUUUUUUUUUUUUUUCCCCCCCCCCCCCKKKKKKKKKKKKKKKKKKKKKKK

I decided that I would sleep in today, to try to get back on my feet
sleep wise. I thought to myself: "I'm not going to get on the
leaderboard anyway". I guess I should have known better than to jinks
myself like that, but nothing to do about it now.

My real times where:

Part one: 00:09:19 (Rank 58)
Part two: 00:09:19 (Rank 19)
Total:    00:18:39

I even had a stupid mistake on part one, where I didn't change the y
from 10 to 2000000, and so that cost me 60 seconds.

This one really hurts. But I guess I should just take it with me that I
would have placed on at least one task this year.

So talking about the task itself. When I opened it up, I was a bit
surprised to see that this was very similar to an earlier years task. I
cannot find it right now, but that one was quite hard. I quite quickly
figured out the ruleset and focused only on the row that we are
interested in. I just added all places that where closer to the senors
than the beacon on that row to the set.

I made one silly mistake, which as noted above, was to forget changing
the row from 10 to 2000000 which cost me 60 seconds. I realized it
almost immediately and so was able to fix it and just wait to be able to
enter the input.

For part two, I very quickly decided to go for using z3 to solve it,
seeing as it really was just a matter of solving a couple of equations.
I had to google how to use z3 in python again, and it took a little
time, but it worked almost straight away, after i had figured out how to
do abs. I really love z3 for these kinds of tasks, it's almost like a
cheat code to be honest.

I don't really know how I would have done this without it, but I guess
that will be a fun task to try to figure out.

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 15   05:12:15  12374      0   05:21:36   7458      0

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[0747099063...](https://github.com/Pickle-Coding/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Thursday 2022-12-15 12:24:24 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[bf582cb833...](https://github.com/Pickle-Coding/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Thursday 2022-12-15 12:24:24 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[bbb956d2a6...](https://github.com/Pickle-Coding/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Thursday 2022-12-15 12:24:24 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[c1f0141967...](https://github.com/Pickle-Coding/tgstation/commit/c1f01419671ad084a6c048ec7900d008de53bfe2)
#### Thursday 2022-12-15 12:24:24 by LemonInTheDark

Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

---
## [AlexanderPaulStevens/alexanderpaulstevens.github.io](https://github.com/AlexanderPaulStevens/alexanderpaulstevens.github.io)@[c86743a578...](https://github.com/AlexanderPaulStevens/alexanderpaulstevens.github.io/commit/c86743a578c68aee82fe6139580e8ea63ada99a0)
#### Thursday 2022-12-15 13:08:09 by Alexander Paul Stevens

Delete --- layout: page title: About me subtitle: Why you'd want to go on a date with me ---  My name is Inigo Montoya. I have the following qualities:  - I rock a great mustache - I'm extremely loyal to my family  What else do you need?  ### My story  To be honest, I'm having some trouble remembering right now, so why don't you just watch [my movie](https:/en.wikipedia.org/wiki directory

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[df4ed1bfdc...](https://github.com/NetBSD/pkgsrc/commit/df4ed1bfdca92b3f36d1f7d04a0d4bceb27058b5)
#### Thursday 2022-12-15 13:48:19 by nia

mgba: Update to 0.10.0. Split the Qt interface into a separate package.

Since the Qt interface has noticable performance problems on NetBSD,
this saves some significant bloat in the main package by only building
the CLI interface by default.

Also modify the default settings to provide a best "out of box"
experience on NetBSD and SunOS, and remove the MESSAGE file indicating
to change the settings.

0.10.0: (2022-10-11)
Features:
 - Preliminary Lua scripting support
 - Presets for Game Boy palettes
 - Add Super Game Boy palettes for original Game Boy games
 - Tool for converting scanned pictures of e-Reader cards to raw dotcode data
 - Options for muting when inactive, minimized, or for different players in multiplayer
 - Cheat code support in homebrew ports
 - Acclerometer and gyro support for controllers on PC
 - Support for combo "Super Game Boy Color" SGB + GBC ROM hacks
 - Improved support for HuC-3 mapper, including RTC
 - Support for 64 kiB SRAM saves used in some bootlegs
 - Discord Rich Presence now supports time elapsed
 - Additional scaling shaders
 - Support for GameShark Advance SP (.gsv) save file importing
 - Support for multiple saves per game using .sa2, .sa3, etc.
 - Support for GBX format Game Boy ROMs
 - New unlicensed GB mappers: NT (newer type), Sachen (MMC1, MMC2)
Emulation fixes:
 - ARM7: Fix unsigned multiply timing
 - GB: Copy logo from ROM if not running the BIOS intro (fixes mgba.io/i/2378)
 - GB: Fix HALT breaking M-cycle alignment (fixes mgba.io/i/250)
 - GB Audio: Fix channel 1/2 reseting edge cases (fixes mgba.io/i/1925)
 - GB Audio: Properly apply per-model audio differences
 - GB Audio: Revamp channel rendering
 - GB Audio: Fix APU re-enable timing glitch
 - GB I/O: Fix writing to WAVE RAM behavior (fixes mgba.io/i/1334)
 - GB MBC: Fix edge case with Pocket Cam register accesses (fixes mgba.io/i/2557)
 - GB Memory: Add cursory cartridge open bus emulation (fixes mgba.io/i/2032)
 - GB Serialize: Fix loading MBC1 states that affect bank 0 (fixes mgba.io/i/2402)
 - GB SIO: Fix bidirectional transfer starting (fixes mgba.io/i/2290)
 - GB Video: Draw SGB border pieces that overlap GB graphics (fixes mgba.io/i/1339)
 - GBA: Improve timing when not booting from BIOS
 - GBA: Fix expected entry point for multiboot ELFs (fixes mgba.io/i/2450)
 - GBA: Fix booting multiboot ROMs with no JOY entrypoint
 - GBA: Fix 1 MiB ROM mirroring to only mirror 4 times
 - GBA Audio: Adjust PSG sampling rate with SOUNDBIAS
 - GBA Audio: Sample FIFOs at SOUNDBIAS-set frequency
 - GBA BIOS: Work around IRQ handling hiccup in Mario & Luigi (fixes mgba.io/i/1059)
 - GBA BIOS: Initial HLE timing estimation of UnLz77 functions (fixes mgba.io/i/2141)
 - GBA DMA: Fix DMA source direction bits being cleared (fixes mgba.io/i/2410)
 - GBA I/O: Redo internal key input, enabling edge-based key IRQs
 - GBA I/O: Disable open bus behavior on invalid register 06A
 - GBA Memory: Fix misaligned 32-bit I/O loads (fixes mgba.io/i/2307)
 - GBA Video: Fix OpenGL rendering on M1 Macs
 - GBA Video: Ignore horizontally off-screen sprite timing (fixes mgba.io/i/2391)
 - GBA Video: Fix Hblank timing (fixes mgba.io/i/2131, mgba.io/i/2310)
 - GBA Video: Fix rare crash in modes 3-5
 - GBA Video: Fix sprites with mid-frame palette changes in GL (fixes mgba.io/i/2476)
 - GBA Video: Fix OBJ tile wrapping with 2D char mapping (fixes mgba.io/i/2443)
 - GBA Video: Fix horizontal lines in GL when charbase is changed (fixes mgba.io/i/1631)
 - GBA Video: Fix sprite layer priority updating in GL
Other fixes:
 - ARM: Disassemble Thumb mov pseudo-instruction properly
 - ARM: Disassemble ARM asr/lsr #32 properly
 - ARM: Disassemble ARM movs properly
 - Core: Don't attempt to restore rewind diffs past start of rewind
 - Core: Fix the runloop resuming after a game has crashed (fixes mgba.io/i/2451)
 - Core: Fix crash if library can't be opened
 - Debugger: Fix crash with extremely long CLI strings
 - Debugger: Fix multiple conditional watchpoints at the same address
 - FFmpeg: Fix crash when encoding audio with some containers
 - FFmpeg: Fix GIF recording (fixes mgba.io/i/2393)
 - GB: Fix temporary saves
 - GB: Fix replacing the ROM crashing when accessing ROM base
 - GB: Don't try to map a 0-byte SRAM (fixes mgba.io/i/2668)
 - GB, GBA: Save writeback-pending masked saves on unload (fixes mgba.io/i/2396)
 - mGUI: Fix FPS counter after closing menu
 - Qt: Fix some hangs when using the debugger console
 - Qt: Fix crash when clicking past last tile in viewer
 - Qt: Fix preloading for ROM replacing
 - Qt: Fix screen not displaying on Wayland (fixes mgba.io/i/2190)
 - Qt: Fix crash when selecting 256-color sprite in sprite view
 - Qt: Fix coloration of swatches on styles with distinct frame backgrounds
 - VFS: Failed file mapping should return NULL on POSIX
Misc:
 - Core: Suspend runloop when a core crashes
 - Core: Add wallclock offset RTC type
 - Debugger: Save and restore CLI history
 - Debugger: GDB now works while the game is paused
 - Debugger: Add command to load external symbol file (fixes mgba.io/i/2480)
 - FFmpeg: Support dynamic audio sample rate
 - GB: Support CGB0 boot ROM loading
 - GB Audio: Increase sample rate
 - GB MBC: Filter out MBC errors when cartridge is yanked (fixes mgba.io/i/2488)
 - GB MBC: Partially implement TAMA5 RTC
 - GB Video: Add default SGB border
 - GBA: Automatically skip BIOS if ROM has invalid logo
 - GBA: Refine multiboot detection (fixes mgba.io/i/2192)
 - GBA Cheats: Implement "never" type codes (closes mgba.io/i/915)
 - GBA DMA: Enhanced logging (closes mgba.io/i/2454)
 - GBA Memory: Implement adjustable EWRAM waitstates (closes mgba.io/i/1276)
 - GBA Savedata: Store RTC data in savegames (closes mgba.io/i/240)
 - GBA Video: Implement layer placement for OpenGL renderer (fixes mgba.io/i/1962)
 - GBA Video: Fix highlighting for sprites with mid-frame palette changes
 - mGUI: Add margin to right-aligned menu text (fixes mgba.io/i/871)
 - mGUI: Autosave less frequently when fast-forwarding
 - Qt: Rearrange menus some
 - Qt: Clean up cheats dialog
 - Qt: Only set default controller bindings if loading fails (fixes mgba.io/i/799)
 - Qt: Save converter now supports importing GameShark Advance saves
 - Qt: Save positions of multiplayer windows (closes mgba.io/i/2128)
 - Qt: Add optional frame counter to OSD (closes mgba.io/i/1728)
 - Qt: Add optional emulation-related information on reset (closes mgba.io/i/1780)
 - Qt: Add QOpenGLWidget cross-thread codepath for macOS (fixes mgba.io/i/1754)
 - Qt: Enable -b for Boot BIOS menu option (fixes mgba.io/i/2074)
 - Qt: Add tile range selection to tile viewer (closes mgba.io/i/2455)
 - Qt: Show warning if XQ audio is toggled while loaded (fixes mgba.io/i/2295)
 - Qt: Add e-Card passing to the command line (closes mgba.io/i/2474)
 - Qt: Boot both a multiboot image and ROM with CLI args (closes mgba.io/i/1941)
 - Qt: Improve cheat parsing (fixes mgba.io/i/2297)
 - Qt: Change lossless setting to use WavPack audio
 - Qt: Use FFmpeg to convert additional camera formats, if available
 - Qt: Resume crashed game when loading a save state
 - Qt: Include cheats in bug report
 - SDL: Support exposing an axis directly as the gyro value (closes mgba.io/i/2531)
 - VFS: Early return NULL if attempting to map 0 bytes from a file

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[a753229ee2...](https://github.com/Striders13/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Thursday 2022-12-15 14:08:16 by GoldenAlpharex

Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.


<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.


![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @MrMelbert about it and he gave me the go-ahead, as can be seen
here:


![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[35b5ac0c4e...](https://github.com/Striders13/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Thursday 2022-12-15 14:08:16 by Fikou

Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Metastruct/garrysmod-chatsounds](https://github.com/Metastruct/garrysmod-chatsounds)@[b57b3d8d45...](https://github.com/Metastruct/garrysmod-chatsounds/commit/b57b3d8d45f8dd4c014640f92eced35d940d4a36)
#### Thursday 2022-12-15 15:35:37 by Ayane

My name is Skyler White yo (#428)

* My name is Walter Hartwell White.

I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a Virtual Youtuber empire for over a year now and using me as his recruiter. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my Live2D knowledge to recruit talents, which he would then hire using his connections in the Japanese utaite world. Connections that he made through his career with Niconico. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small indie channel could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Motoaki Yagoo Tanigo, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Yagoo threatened my family. I didn't know where to turn. Eventually, Hank and Yagoo had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Yagoo flatly refused to give him, and things escalated. Yagoo was able to arrange, uh I guess I guess you call it a hit on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over 77,000. Upon recovery, Hank was bent on revenge, working with a man named Riku Tazumi , he plotted to kill Yagoo, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Cover Corp, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my vtubing activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

---
## [ZeevSheli/Level-Design](https://github.com/ZeevSheli/Level-Design)@[4a25733c11...](https://github.com/ZeevSheli/Level-Design/commit/4a25733c1151fd099ebe21de0afa303c9a268ca5)
#### Thursday 2022-12-15 17:15:57 by Sarah Norén

fuck this shit i am out

I did so much, you don't even know how strenuous this was, I'd be here until Jenny found my body in the morning if Arthur wasn't here. nooooo

---
## [JCCPort/PETsysUtils](https://github.com/JCCPort/PETsysUtils)@[f4a322999c...](https://github.com/JCCPort/PETsysUtils/commit/f4a322999c98f3b8d23a249ad2616c03d43051ca)
#### Thursday 2022-12-15 17:24:09 by petsys

Merge branch 'master' of github.com:JCCPort/PETsysUtils
I can merge what I want fuck you

---
## [ItsRqtl/ipy-library](https://github.com/ItsRqtl/ipy-library)@[e527a7d034...](https://github.com/ItsRqtl/ipy-library/commit/e527a7d034f93781d2739a380a1c87c089fdf572)
#### Thursday 2022-12-15 17:59:51 by EdVraz

feat(channel): Add new overwrite helper methods (#1173)

* fix: edge case

* refactor: move import

* guys I don't recommend coding when you're sick

* do stuff

* omg what the fuck did i code yesterday

* fix: simplify code

* feat: add another helper method

* Update channel.py

---
## [GNOME/glib](https://github.com/GNOME/glib)@[b8e1ecdd6b...](https://github.com/GNOME/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Thursday 2022-12-15 19:23:10 by Michael Catanzaro

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
## [GoatersBro/HEXAPAWN_BOT](https://github.com/GoatersBro/HEXAPAWN_BOT)@[9271632094...](https://github.com/GoatersBro/HEXAPAWN_BOT/commit/9271632094b6488f49f6b682041cd0d53e19be3e)
#### Thursday 2022-12-15 19:37:43 by GoatersBro

HOLY SHIT

Why are there so many different probabilities in moving a god damn pawn

---
## [Nilstrieb/rust](https://github.com/Nilstrieb/rust)@[aa3a689b8c...](https://github.com/Nilstrieb/rust/commit/aa3a689b8ce64bc697c74074bffd2f77e3a07b77)
#### Thursday 2022-12-15 19:56:19 by Nilstrieb

Rip it out

My type ascription
Oh rip it out
Ah
If you think we live too much then
You can sacrifice diagnostics
Don't mix your garbage
Into my syntax
So many weird hacks keep diagnostics alive
Yet I don't even step outside
So many bad diagnostics keep tyasc alive
Yet tyasc doesn't even bother to survive!

---
## [CDRDecky/sunset-wasteland](https://github.com/CDRDecky/sunset-wasteland)@[f7f7ae2cfc...](https://github.com/CDRDecky/sunset-wasteland/commit/f7f7ae2cfc1c91d2df5bfdbd7895e7ab2c6eb4d3)
#### Thursday 2022-12-15 20:13:34 by Colovorat

Fixes cable merging, changes merging code just a little bit (#60997)

Makes stack code support merging two different stacks with the same mats, but different mats_per_unit numbers by implementing averages.

It's in an attempt to support the stupid efficiency shit that protolathes do. It's not great, but it ought to work alright for now. Kinda a bandaid
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[84b1612201...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/84b161220115e3243272299b3f8f3cb29d484709)
#### Thursday 2022-12-15 20:19:38 by SkyratBot

[MIRROR] Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. [MDB IGNORE] (#18019)

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.

![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup.

* update modular

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [AmazingAmpharos/core](https://github.com/AmazingAmpharos/core)@[fbd7918899...](https://github.com/AmazingAmpharos/core/commit/fbd7918899749fa7a6d71227ef598cbd1cd248a2)
#### Thursday 2022-12-15 20:39:45 by AmazingAmpharos

OoTR Compliance: Spirit Temple

This should fully update the logic to match what OoTR has for Spirit Temple, given the constraints of this (notably hard assuming you can buy sticks and nuts and that a Bomb Bag automatically lets you acquire Bombchus from the Market; it's considerably more complex if you can't). Some of it is really not intuitive, but honestly, this is way less dense than I expected given what Spirit Temple is. I overhyped it, sorry.

---
## [julien/dotfiles](https://github.com/julien/dotfiles)@[87a0b41017...](https://github.com/julien/dotfiles/commit/87a0b410179309c64269435ac7109dedf4b1b6f0)
#### Thursday 2022-12-15 21:58:48 by Julien Castelain

Update zsh settings

I don't actually care about this right now.

Since I want to keep my configuration files as "minimal" (I hate that
word) as possible, I'm removing this and I think it's a shame that we
need "Ad Blockers" to make the web a "safe" space.

---
## [steadmon/git](https://github.com/steadmon/git)@[f1c903debd...](https://github.com/steadmon/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Thursday 2022-12-15 22:03:03 by Ævar Arnfjörð Bjarmason

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
## [raspbian-packages/git](https://github.com/raspbian-packages/git)@[b4a60325fc...](https://github.com/raspbian-packages/git/commit/b4a60325fc8e95dcb1d037ba17ab1d2643f763f3)
#### Thursday 2022-12-15 22:07:49 by Johannes Schindelin

protect_ntfs: turn on NTFS protection by default

Back in the DOS days, in the FAT file system, file names always
consisted of a base name of length 8 plus a file extension of length 3.
Shorter file names were simply padded with spaces to the full 8.3
format.

Later, the FAT file system was taught to support _also_ longer names,
with an 8.3 "short name" as primary file name. While at it, the same
facility allowed formerly illegal file names, such as `.git` (empty base
names were not allowed), which would have the "short name" `git~1`
associated with it.

For backwards-compatibility, NTFS supports alternative 8.3 short
filenames, too, even if starting with Windows Vista, they are only
generated on the system drive by default.

We addressed the problem that the `.git/` directory can _also_ be
accessed via `git~1/` (when short names are enabled) in 2b4c6efc821
(read-cache: optionally disallow NTFS .git variants, 2014-12-16), i.e.
since Git v1.9.5, by introducing the config setting `core.protectNTFS`
and enabling it by default on Windows.

In the meantime, Windows 10 introduced the "Windows Subsystem for Linux"
(short: WSL), i.e. a way to run Linux applications/distributions in a
thinly-isolated subsystem on Windows (giving rise to many a "2016 is the
Year of Linux on the Desktop" jokes). WSL is getting increasingly
popular, also due to the painless way Linux application can operate
directly ("natively") on files on Windows' file system: the Windows
drives are mounted automatically (e.g. `C:` as `/mnt/c/`).

Taken together, this means that we now have to enable the safe-guards of
Git v1.9.5 also in WSL: it is possible to access a `.git` directory
inside `/mnt/c/` via the 8.3 name `git~1` (unless short name generation
was disabled manually). Since regular Linux distributions run in WSL,
this means we have to enable `core.protectNTFS` at least on Linux, too.

To enable Services for Macintosh in Windows NT to store so-called
resource forks, NTFS introduced "Alternate Data Streams". Essentially,
these constitute additional metadata that are connected to (and copied
with) their associated files, and they are accessed via pseudo file
names of the form `filename:<stream-name>:<stream-type>`.

In a recent patch, we extended `core.protectNTFS` to also protect
against accesses via NTFS Alternate Data Streams, e.g. to prevent
contents of the `.git/` directory to be "tracked" via yet another
alternative file name.

While it is not possible (at least by default) to access files via NTFS
Alternate Data Streams from within WSL, the defaults on macOS when
mounting network shares via SMB _do_ allow accessing files and
directories in that way. Therefore, we need to enable `core.protectNTFS`
on macOS by default, too, and really, on any Operating System that can
mount network shares via SMB/CIFS.

A couple of approaches were considered for fixing this:

1. We could perform a dynamic NTFS check similar to the `core.symlinks`
   check in `init`/`clone`: instead of trying to create a symbolic link
   in the `.git/` directory, we could create a test file and try to
   access `.git/config` via 8.3 name and/or Alternate Data Stream.

2. We could simply "flip the switch" on `core.protectNTFS`, to make it
   "on by default".

The obvious downside of 1. is that it won't protect worktrees that were
clone with a vulnerable Git version already. We considered patching code
paths that check out files to check whether we're running on an NTFS
system dynamically and persist the result in the repository-local config
setting `core.protectNTFS`, but in the end decided that this solution
would be too fragile, and too involved.

The obvious downside of 2. is that everybody will have to "suffer" the
performance penalty incurred from calling `is_ntfs_dotgit()` on every
path, even in setups where.

After the recent work to accelerate `is_ntfs_dotgit()` in most cases,
it looks as if the time spent on validating ten million random
file names increases only negligibly (less than 20ms, well within the
standard deviation of ~50ms). Therefore the benefits outweigh the cost.

Another downside of this is that paths that might have been acceptable
previously now will be forbidden. Realistically, though, this is an
improvement because public Git hosters already would reject any `git
push` that contains such file names.

Note: There might be a similar problem mounting HFS+ on Linux. However,
this scenario has been considered unlikely and in light of the cost (in
the aforementioned benchmark, `core.protectHFS = true` increased the
time from ~440ms to ~610ms), it was decided _not_ to touch the default
of `core.protectHFS`.

This change addresses CVE-2019-1353.

Reported-by: Nicolas Joly <Nicolas.Joly@microsoft.com>
Helped-by: Garima Singh <garima.singh@microsoft.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
(cherry picked from commit 9102f958ee5254b10c0be72672aa3305bf4f4704)
Signed-off-by: Jonathan Nieder <jrnieder@gmail.com>

Gbp-Pq: Name 0016-protect_ntfs-turn-on-NTFS-protection-by-default.diff

---
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[70bcd3b6fb...](https://github.com/spartanbobby/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Thursday 2022-12-15 23:19:06 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Safariminer/3bune](https://github.com/Safariminer/3bune)@[899bdf4d21...](https://github.com/Safariminer/3bune/commit/899bdf4d217d1ce247bc802c6a5667e0d709f4d1)
#### Thursday 2022-12-15 23:35:50 by Safariminer

REWROTE THE ENTIRETY OF TOTOZ GOD DAMNIT CHRIST

I REWROTE THE ENTIRETY OF TOTOZ RENDERING FUCK ME IT WAS SO STUPID

---
## [HotFixDeveloper/liberty-win](https://github.com/HotFixDeveloper/liberty-win)@[1c97b2497f...](https://github.com/HotFixDeveloper/liberty-win/commit/1c97b2497fda507dd9b3e8bfc601d73a751b7c49)
#### Thursday 2022-12-15 23:40:10 by hackuna

Minimum Viable Product

Roskomnadzor, go fuck yourself!

---
## [SandroMartens/chess-openings](https://github.com/SandroMartens/chess-openings)@[9f7632e84e...](https://github.com/SandroMartens/chess-openings/commit/9f7632e84ebf35b79b8d3c08af9b95943cc54e59)
#### Thursday 2022-12-15 23:44:32 by Alexandru Duca

Scandinavian Defense: Portuguese Gambit

- Removed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. f3 Bf5` named `Scandinavian Defense: Portuguese Variation, Portuguese Gambit`.
- Renamed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` from `Scandinavian Defense: Portuguese Variation` to `Scandinavian Defense: Portuguese Gambit`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` named `Scandinavian Defense: Portuguese Gambit, Banker Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` named `Scandinavian Defense: Portuguese Gambit, Classical Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` named `Scandinavian Defense: Portuguese Gambit, Correspondence Refutation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` named `Scandinavian Defense: Portuguese Gambit, Elbow Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` named `Scandinavian Defense: Portuguese Gambit, Jadoul Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` named `Scandinavian Defense: Portuguese Gambit, Lusophobe Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` named `Scandinavian Defense: Portuguese Gambit, Melbourne Shuffle Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` named `Scandinavian Defense: Portuguese Gambit, Wuss Variation`.

This line `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` in the Scandinavian Defense has many different names across chess literature. Selby Anderson released the book [Center Counter Defense: The Portuguese Variation](https://www.amazon.com/Center-Counter-Defense-Portuguese-Variation/dp/1886846103) in the year 1997 and, apparently, named it `Portuguese Variation`. In his book [Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943), [David Smerdon](https://en.wikipedia.org/wiki/David_Smerdon) called this line `Portuguese Complex`, but he noted that it was also called `Portuguese Opening` as well as `Jadoul Variation` [Section 1]. It's called `Portuguese Gambit` in Wikipedia's [list of chess gambits](https://en.wikipedia.org/wiki/List_of_chess_gambits#Scandinavian_Defense) and `Portuguese Variation` as well as `Jadoul Variation` in Wikipedia's article on the [Scandinavian Defense](https://en.wikipedia.org/wiki/Scandinavian_Defense#2...Nf6). (Unfortunately, I was unable to check the sources Wikipedia provides because I couldn't find the referenced books.)

Since Selby Anderson's book predates all other sources, there is an argument to name this line `Portuguese Variation`. However, Black delays taking back the pawn on d5 twice (first time with `2... Nf6` and second time with `3... Bg4`). This gives White the opportunity to secure the extra pawn with e.g. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4 Bg6 6. c4`. Additionally, Selby Anderson may not have been aware of the dubious nature of this variation ([Stockfish gives White +0.8](https://lichess.org/7CAhQOCs)). Furthermore, David Smerdon repeatedly refers to this line as a gambit despite calling it `Portuguese Complex`. Because of this, I argue that this line should be called the `Portuguese Gambit`.

[Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943) is currently the most extensive book on the `Portuguese Gambit`. It categorizes all major responses from White after `1. e4 d5 2. exd5 Nf6 3. d4 Bg4`. Smerdon also offers creative names for all variations covered by his theory. Here are the variations sorted by chapter:
1. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` is called `The Banker`. (White "banks" the extra pawn with the immediate `5. c4`.)
2. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` is called `The Jadoul`. (Named after [Michel Jadoul](https://de.wikipedia.org/wiki/Michel_Jadoul) who is one of the earliest exponents of the Portuguese Gambit [Introduction, Inspirational Game #1].)
3. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` is called `The Melbourne Shuffle`. (Played by many australian IMs from Melbourne [Chapter 3]. It is named after a [rave dance](https://en.wikipedia.org/wiki/Melbourne_shuffle) which originated in Melbourne.)
4. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` is called `The Correspondence Refutation`. (A line against the `Portuguese Gambit` successfully employed the correspondence community [Chapter 4].)
5. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` is called `The Wuss`. (Apparently, `4. Be2` is a wimpy move and only a [wuss](https://www.merriam-webster.com/dictionary/wuss) would play it.)
6. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` is called `The Lusophobe`. (According to Wikipedia, [Lusophobia](https://en.wikipedia.org/wiki/Lusophobia) is irrational hostility, racism or hatred towards Portugal, the Portuguese people or the Portuguese language and culture. David Smerdon is making a joke by referring to the line `4. Bb5+ Nbd7 5. Be2` as "Anti-Portuguese" or "effective against the Portuguese Gambit".)
7. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` is called `The Elbow`. (Given the effectivness of the line `4. Bb5+ Nbd7 5. Be2`, occasionally playing `4... c6` may discourage players from studying it while preparing against you. Playing `4... c6` is a metaphor for hitting your well prepared opponent with your elbow [Chapter 7].)
8. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` is called `The Classical`. (Refers to the fact that the move `4. Nf3` is principled [Chapter 8].)

---
## [xDroidOSS-Pixel/platform_frameworks_base](https://github.com/xDroidOSS-Pixel/platform_frameworks_base)@[cd3746acc9...](https://github.com/xDroidOSS-Pixel/platform_frameworks_base/commit/cd3746acc94d432acf0734abe4df3e522e330464)
#### Thursday 2022-12-15 23:49:41 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

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

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---

