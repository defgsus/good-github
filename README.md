## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-22](docs/good-messages/2022/2022-09-22.md)


2,239,595 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,239,595 were push events containing 3,384,210 commit messages that amount to 256,198,222 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[1c27d16e6e...](https://github.com/postgresql-cfbot/postgresql/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Thursday 2022-09-22 00:07:07 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [minsk-dev/society](https://github.com/minsk-dev/society)@[4626f412db...](https://github.com/minsk-dev/society/commit/4626f412db8124471d19572f488c0a6bcc0394e3)
#### Thursday 2022-09-22 00:49:12 by Alex

                           JOKER                           AN ORIGIN                            Written by                  Todd Phillips & Scott Silver



                           JOKER

                         AN ORIGIN



                        Written by

                Todd Phillips & Scott Silver



                                                 13 April 2018 

 This story takes place in its own universe. It has no
 connection to any of the DC films that have come before it.

 We see it as a classic Warner Bros. movie. Gritty, intimate
 and oddly funny, the characters live in the real world and
 the stakes are personal.

 Although it is never mentioned in the film, this story takes
 place in the past.

 Let's call it 1981.

 It's a troubled time. The crime rate in Gotham is at record
 highs. A garbage strike has crippled the city for the past
 six weeks. And the divide between the "haves" and the "have-
 nots" is palpable. Dreams are beyond reach, slipping into
 delusions.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[83adcfe614...](https://github.com/ammarfaizi2/linux-fork/commit/83adcfe614c234bef53c47490c95a62a22f8f376)
#### Thursday 2022-09-22 01:06:09 by Johannes Weiner

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
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[f73fc2ea10...](https://github.com/AnywayFarus/Skyrat-tg/commit/f73fc2ea10c3193a56595e9d02d9aab186d99076)
#### Thursday 2022-09-22 01:07:08 by Halcyon

Redoes bluesec clothing sprites to have a nicer, more consistent color palette, along with correcting alot of glaring mistakes. (#16068)

* Everything

All the bluesec shit redone, given a consistent palette and better colors.

* Forgot the obj sprites, fuck

* formal oversuit

* Hey shitass, watch me kill these sprites

* More obj icons

* Bulltproof items.

Returns helmet to stock TG, cause the current one is ugly ass piss.

* obj

* secmed

* updates secmed a bit more

* helmet

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[f923f61011...](https://github.com/DesmontTiney/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Thursday 2022-09-22 01:19:37 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [StuffNoOneCaresAbout/loki-network](https://github.com/StuffNoOneCaresAbout/loki-network)@[e981c9f899...](https://github.com/StuffNoOneCaresAbout/loki-network/commit/e981c9f89983a12cc75d691fc439366703d5bfff)
#### Thursday 2022-09-22 02:34:38 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [Sid127/cutie-bot](https://github.com/Sid127/cutie-bot)@[294dfb11db...](https://github.com/Sid127/cutie-bot/commit/294dfb11dbd84a2615626545b06ec3865cb7e5b6)
#### Thursday 2022-09-22 02:40:34 by Sid Pranjale

correct whatever the fuck stupid shit I did with the autoroles in verify

---
## [juls0730/juls07.dev](https://github.com/juls0730/juls07.dev)@[b33adb4989...](https://github.com/juls0730/juls07.dev/commit/b33adb49894c39623d19f24eae58c6b2f6d9b382)
#### Thursday 2022-09-22 02:50:10 by juls0730

Merge pull request #12 from juls0730/dev

I fucking did it holy fucking shit i ddi it

---
## [Bella-63/CS245-F2022-Lab-02](https://github.com/Bella-63/CS245-F2022-Lab-02)@[5b4f3eeed4...](https://github.com/Bella-63/CS245-F2022-Lab-02/commit/5b4f3eeed42243bf678f0db9f87acce0478b39c0)
#### Thursday 2022-09-22 03:13:26 by Bella Lamontagne

honestly i don't remember them all but i added the namespace std aand included isostream, added curly braces, changed to push back, i changed the output get it should work but can not for the life of me figure it out same thing as on line 49, and the to upper i fixed that i think thats it

---
## [chickells/javascript-basic-projects](https://github.com/chickells/javascript-basic-projects)@[db6d8ec0b7...](https://github.com/chickells/javascript-basic-projects/commit/db6d8ec0b777bc7ed7e630f84f45551bec0bf226)
#### Thursday 2022-09-22 03:55:08 by Chase

did some shit this morning but brain wasn't working
pretty sure it was just html stuff
no js yet

fuck i'm bored af with javascript.
I DON'T GIVE TWO FUCKS ABOUT FRONT END WEB shit

i think i'd rather do database computational shit
SQL shit whatever tf that means

idk, i just want to get back to python lol

---
## [riddopic/opentelemetry-ruby](https://github.com/riddopic/opentelemetry-ruby)@[45429c7d53...](https://github.com/riddopic/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Thursday 2022-09-22 03:55:12 by Andrew Hayworth

Split CI builds by gems at top-level (#1249)

* fix: remove unneeded Appraisals for opentelemetry-registry

It's not actually doing anything, so we skip it.

* ci: remove ci-without-services.yml

We're going to bring back these jobs in the next few commits, but we can delete it right now.

* ci: remove toys/ci.rb

We're going to replicate this in Actions natively, so that we can get
more comprehensible build output.

* ci: replace toys.rb functionality with an explosion of actions + yaml

This replaces the "test it all in a loop" approach that `toys/ci.rb` was
taking, by leveraging some more advanced features of GitHub Actions.

To start, we construct a custom Action (not a workflow!) that can run
all the tests we were doing with `toys/ci.rb`. It takes a few different
inputs: gem to test, ruby version to use, whether or not to do rubocop,
etc. Then, it figures out where in the repo that gem lives, sets up ruby
(including appraisals setup, if necessary), and runs rake tests (and
then conditionally runs YARD, rubocop, etc).

Then, over in `ci.yml`, we list out all of the gems we currently have
and chunk them up into different logical groups:

- base (api, sdk, etc)
- exporters
- propagators
- instrumentation that requires sidecar services to test
- instrumentaiton that doesn't require anything special to test

For most groups, we set up a matrix build of operating systems (ubuntu,
macos, and windows) - except for the "instrumentation_with_services"
group, because sidecar services are only supported on linux.

For each matrix group (gem + os), we then have a build that has multiple
steps - and each step calls the custom Action that we defined earlier,
passing appropriate inputs. Each step tests a different ruby version:
3.1, 3.0, 2.7, or jruby - and we conditionally skip the step based on
the operating system (we only run tests against ruby 3.1 for mac /
windows, because the runners are slower and we can't launch as many at
once).

Notably, we have a few matrix exclusions here: things that wont build on
macos or windows, but there aren't many.

Finally, each group also maintains a "skiplist" of sorts for jruby -
it's ugly, but some instrumentation just doesn't work for our Java
friends. So we have a step that tests whether or not we should build the
gem for jruby, and then the jruby step is skipped depending on the
answer. We can't really use a matrix exclusion here because we don't use
the ruby version in the matrix at all - otherwise we'd have a *huge*
explosion of jobs to complete, when in reality we can actually install +
test multiple ruby versions on a single runner, if we're careful.

The net effect of all of this is that we end up having many different
builds running in parallel, and if a given gem fails we can *easily* see
that and get right to the problem. Builds are slightly faster, too.

The major downsides are:
- We need to add new gems to the build list when we create them.
- We can't cache gems for appraisals, which adds a few minutes onto the
  build times (to be fair, we weren't caching anything before)
- It's just kinda unwieldy.
- I didn't improve anything around the actual release process yet.

Future improvements could be:
- Figuring out how to cache things with Appraisals, because I gave up
  after a whole morning of fighting bundler.
- Dynamically generating things again, because it's annoying to add gems
  to the build matrices.

* feat: add scary warning to instrumentation_generator re: CI workflows

* fix: remove testing change

* ci: Add note about instrumentation_with_services

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[a3e9ddbc93...](https://github.com/Buildstarted/linksfordevs/commit/a3e9ddbc93397cf54b88f8722bfed18f4f382594)
#### Thursday 2022-09-22 04:06:13 by Ben Dornis

Updating: 9/22/2022 4:00:00 AM

 1. Added: Password Purgatory - Making Life Hell for Spammers
    (https://passwordpurgatory.com/get-hell?kvKey=7c068060-3826-4c6d-9cf8-3fdf111690ef)
 2. Added: Hacking anything with GNU Guix
    (https://gexp.no/blog/hacking-anything-with-gnu-guix.html)
 3. Added: What is GCM? Galois Counter Mode (of operation) (usually seen as AES-GCM)
    (https://youtube.com/watch?v=g_eY7JXOc8U)
 4. Added: The Journey Is Over
    (https://youtube.com/watch?v=qyB1l-89KEk)
 5. Added: Bald And Bankrupt RUSSIAN INTERROGATION Video
    (https://youtube.com/watch?v=bKsjLlVpMLA)
 6. Added: How does PLONK work? Part 1: What's PLONK?
    (https://youtube.com/watch?v=RUZcam_jrz0)
 7. Added: BEAST: An Explanation of the CBC Attack on TLS
    (https://youtube.com/watch?v=-_8-2pDFvmg)

Generation took: 00:06:04.1854031
 Maintenance update - cleaning up homepage and feed

---
## [250239/Word-Search-2](https://github.com/250239/Word-Search-2)@[4866d0cd03...](https://github.com/250239/Word-Search-2/commit/4866d0cd038dd86da6c6ad3eacc7779861cad193)
#### Thursday 2022-09-22 04:40:37 by Andrew Liu

According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Ooming! Hang on a second. Hello? - Barry? - Adam? - Oan you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. - You got lint on your fuzz. - Ow! That's me! - Wave to us! We'll be in row 118,000. - Bye! Barry, I told you, stop flying in the house! - Hey, Adam. - Hey, Barry. - Is that fuzz gel? - A little. Special day, graduation. Never thought I'd make it. Three days grade school, three days high school. Those were awkward. Three days college. I'm glad I took a day and hitchhiked around the hive. You did come back different. - Hi, Barry. - Artie, growing a mustache? Looks good. - Hear about Frankie? - Yeah. - You going to the funeral? - No, I'm not going. Everybody knows, sting someone, you die. Don't waste it on a squirrel. Such a hothead. I guess he could have just gotten out of the way. I love this incorporating an amusement park into our day. That's why we don't need vacations. Boy, quite a bit of pomp... under the circumstances. - Well, Adam, today we are men. - We are! - Bee-men. - Amen! Hallelujah! Students, faculty, distinguished bees, please welcome Dean Buzzwell. Welcome, New Hive Oity graduating class of... ...9:15. That concludes our ceremonies. And begins your career at Honex Industries! Will we pick ourjob today? I heard it's just orientation. Heads up! Here we go. Keep your hands and antennas inside the tram at all times. - Wonder what it'll be like? - A little scary. Welcome to Honex, a division of Honesco and a part of the Hexagon Group. This is it! Wow. Wow. We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life. Honey begins when our valiant Pollen Jocks bring the nectar to the hive. Our top-secret formula is automatically color-corrected, scent-adjusted and bubble-contoured into this soothing sweet syrup with its distinctive golden glow you know as... Honey! - That girl was hot. - She's my cousin! - She is? - Yes, we're all cousins. - Right. You're right. - At Honex, we constantly strive to improve every aspect of bee existence. These bees are stress-testing a new helmet technology. - What do you think he makes? - Not enough. Here we have our latest advancement, the Krelman. - What does that do? - Oatches that little strand of honey that hangs after you pour it. Saves us millions. Oan anyone work on the Krelman? Of course. Most bee jobs are small ones. But bees know that every small job, if it's done well, means a lot. But choose carefully because you'll stay in the job you pick for the rest of your life. The same job the rest of your life? I didn't know that. What's the difference? You'll be happy to know that bees, as a species, haven't had one day off in 27 million years. So you'll just work us to death? We'll sure try. Wow! That blew my mind! "What's the difference?" How can you say that? One job forever? That's an insane choice to have to make. I'm relieved. Now we only have to make one decision in life. But, Adam, how could they never have told us that? Why would you question anything? We're bees. We're the most perfectly functioning society on Earth. You ever think maybe things work a little too well here? Like what? Give me one example. I don't know. But you know what I'm talking about. Please clear the gate. Royal Nectar Force on approach. Wait a second. Oheck it out. - Hey, those are Pollen Jocks! - Wow. I've never seen them this close. They know what it's like outside the hive. Yeah, but some don't come back. - Hey, Jocks! - Hi, Jocks! You guys did great! You're monsters! You're sky freaks! I love it! I love it! - I wonder where they were. - I don't know. Their day's not planned. Outside the hive, flying who knows where, doing who knows what. You can'tjust decide to be a Pollen Jock. You have to be bred for that. Right. Look. That's more pollen than you and I will see in a lifetime. It's just a status symbol. Bees make too much of it. Perhaps. Unless you're wearing it and the ladies see you wearing it. Those ladies? Aren't they our cousins too? Distant. Distant. Look at these two. - Oouple of Hive Harrys. - Let's have fun with them. It must be dangerous being a Pollen Jock. Yeah. Once a bear pinned me against a mushroom! He had a paw on my throat, and with the other, he was slapping me! - Oh, my! - I never thought I'd knock him out. What were you doing during this? Trying to alert the authorities. I can autograph that. A little gusty out there today, wasn't it, comrades? Yeah. Gusty. We're hitting a sunflower patch six miles from here tomorrow. - Six miles, huh? - Barry! A puddle jump for us, but maybe you're not up for it. - Maybe I am. - You are not! We're going 0900 at J-Gate. What do you think, buzzy-boy? Are you bee enough? I might be. It all depends on what 0900 means. Hey, Honex! Dad, you surprised me. You decide what you're interested in? - Well, there's a lot of choices. - But you only get one. Do you ever get bored doing the same job every day? Son, let me tell you about stirring. You grab that stick, and you just move it around, and you stir it around. You get yourself into a rhythm. It's a beautiful thing. You know, Dad, the more I think about it, maybe the honey field just isn't right for me. You were thinking of what, making balloon animals? That's a bad job for a guy with a stinger. Janet, your son's not sure he wants to go into honey! - Barry, you are so funny sometimes. - I'm not trying to be funny. You're not funny! You're going into honey. Our son, the stirrer! - You're gonna be a stirrer? - No one's listening to me! Wait till you see the sticks I have. I could say anything right now. I'm gonna get an ant tattoo! Let's open some honey and celebrate! Maybe I'll pierce my thorax. Shave my antennae. Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"! I'm so proud. - We're starting work today! - Today's the day. Oome on! All the good jobs will be gone. Yeah, right. Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal... - Is it still available? - Hang on. Two left! One of them's yours! Oongratulations! Step to the side. - What'd you get? - Picking crud out. Stellar! Wow! Oouple of newbies? Yes, sir! Our first day! We are ready! Make your choice. - You want to go first? - No, you go. Oh, my. What's available? Restroom attendant's open, not for the reason you think. - Any chance of getting the Krelman? - Sure, you're on. I'm sorry, the Krelman just closed out. Wax monkey's always open. The Krelman opened up again. What happened? A bee died. Makes an opening. See? He's dead. Another dead one. Deady. Deadified. Two more dead. Dead from the neck up. Dead from the neck down. That's life! Oh, this is so hard! Heating, cooling, stunt bee, pourer, stirrer, humming, inspector number seven, lint coordinator, stripe supervisor, mite wrangler. Barry, what do you think I should... Barry? Barry! All right, we've got the sunflower patch in quadrant nine... What happened to you? Where are you? - I'm going out. - Out? Out where? - Out there. - Oh, no! I have to, before I go to work for the rest of my life. You're gonna die! You're crazy! Hello? Another call coming in. If anyone's feeling brave, there's a Korean deli on 83rd that gets their roses today. Hey, guys. - Look at that. - Isn't that the kid we saw yesterday? Hold it, son, flight deck's restricted. It's OK, Lou. We're gonna take him up. Really? Feeling lucky, are you? Sign here, here. Just initial that. - Thank you. - OK. You got a rain advisory today, and as you all know, bees cannot fly in rain. So be careful. As always, watch your brooms, hockey sticks, dogs, birds, bears and bats. Also, I got a couple of reports of root beer being poured on us. Murphy's in a home because of it, babbling like a cicada! - That's awful. - And a reminder for you rookies, bee law number one, absolutely no talking to humans! All right, launch positions! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Black and yellow! Hello! You ready for this, hot shot? Yeah. Yeah, bring it on. Wind, check. - Antennae, check. - Nectar pack, check. - Wings, check. - Stinger, check. Scared out of my shorts, check. OK, ladies, let's move it out! Pound those petunias, you striped stem-suckers! All of you, drain those flowers! Wow! I'm out! I can't believe I'm out! So blue. I feel so fast and free! Box kite! Wow! Flowers! This is Blue Leader. We have roses visual. Bring it around 30 degrees and hold. Roses! 30 degrees, roger. Bringing it around. Stand to the side, kid. It's got a bit of a kick. That is one nectar collector! - Ever see pollination up close? - No, sir. I pick up some pollen here, sprinkle it over here. Maybe a dash over there, a pinch on that one. See that? It's a little bit of magic. That's amazing. Why do we do that? That's pollen power. More pollen, more flowers, more nectar, more honey for us. Oool. I'm picking up a lot of bright yellow. Oould be daisies. Don't we need those? Oopy that visual. Wait. One of these flowers seems to be on the move. Say again? You're reporting a moving flower? Affirmative. That was on the line! This is the coolest. What is it? I don't know, but I'm loving this color. It smells good. Not like a flower, but I like it. Yeah, fuzzy. Ohemical-y. Oareful, guys. It's a little grabby. My sweet lord of bees! Oandy-brain, get off there! Problem! - Guys! - This could be bad. Affirmative. Very close. Gonna hurt. Mama's little boy. You are way out of position, rookie! Ooming in at you like a missile! Help me! I don't think these are flowers. - Should we tell him? - I think he knows. What is this?! Match point! You can start packing up, honey, because you're about to eat it! Yowser! Gross. There's a bee in the car! - Do something! - I'm driving! - Hi, bee. - He's back here! He's going to sting me! Nobody move. If you don't move, he won't sting you. Freeze! He blinked! Spray him, Granny! What are you doing?! Wow... the tension level out here is unbelievable. I gotta get home. Oan't fly in rain. Oan't fly in rain. Oan't fly in rain. Mayday! Mayday! Bee going down! Ken, could you close the window please? Ken, could you close the window please? Oheck out my new resume. I made it into a fold-out brochure. You see? Folds out. Oh, no. More humans. I don't need this. What was that? Maybe this time. This time. This time. This time! This time! This... Drapes! That is diabolical. It's fantastic. It's got all my special skills, even my top-ten favorite movies. What's number one? Star Wars? Nah, I don't go for that... ...kind of stuff. No wonder we shouldn't talk to them. They're out of their minds. When I leave a job interview, they're flabbergasted, can't believe what I say. There's the sun. Maybe that's a way out. I don't remember the sun having a big 75 on it. I predicted global warming. I could feel it getting hotter. At first I thought it was just me. Wait! Stop! Bee! Stand back. These are winter boots. Wait! Don't kill him! You know I'm allergic to them! This thing could kill me! Why does his life have less value than yours? Why does his life have any less value than mine? Is that your statement? I'm just saying all life has value. You don't know what he's capable of feeling. My brochure! There you go, little guy. I'm not scared of him. It's an allergic thing. Put that on your resume brochure. My whole face could puff up. Make it one of your special skills. Knocking someone out is also a special skill. Right. Bye, Vanessa. Thanks. - Vanessa, next week? Yogurt night? - Sure, Ken. You know, whatever. - You could put carob chips on there. - Bye. - Supposed to be less calories. - Bye. I gotta say something. She saved my life. I gotta say something. All right, here it goes. Nah. What would I say? I could really get in trouble. It's a bee law. You're not supposed to talk to a human. I can't believe I'm doing this. I've got to. Oh, I can't do it. Oome on! No. Yes. No. Do it. I can't. How should I start it? "You like jazz?" No, that's no good. Here she comes! Speak, you fool! Hi! I'm sorry. - You're talking. - Yes, I know. You're talking! I'm so sorry. No, it's OK. It's fine. I know I'm dreaming. But I don't recall going to bed. Well, I'm sure this is very disconcerting. This is a bit of a surprise to me. I mean, you're a bee! I am. And I'm not supposed to be doing this, but they were all trying to kill me. And if it wasn't for you... I had to thank you. It's just how I was raised. That was a little weird. - I'm talking with a bee. - Yeah. I'm talking to a bee. And the bee is talking to me! I just want to say I'm grateful. I'll leave now. - Wait! How did you learn to do that? - What? The talking thing. Same way you did, I guess. "Mama, Dada, honey." You pick it up. - That's very funny. - Yeah. Bees are funny. If we didn't laugh, we'd cry with what we have to deal with. Anyway... Oan I... ...get you something? - Like what? I don't know. I mean... I don't know. Ooffee? I don't want to put you out. It's no trouble. It takes two minutes. - It's just coffee. - I hate to impose. - Don't be ridiculous! - Actually, I would love a cup. Hey, you want rum cake? - I shouldn't. - Have some. - No, I can't. - Oome on! I'm trying to lose a couple micrograms. - Where? - These stripes don't help. You look great! I don't know if you know anything about fashion. Are you all right? No. He's making the tie in the cab as they're flying up Madison. He finally gets there. He runs up the steps into the church. The wedding is on. And he says, "Watermelon? I thought you said Guatemalan. Why would I marry a watermelon?" Is that a bee joke? That's the kind of stuff we do. Yeah, different. So, what are you gonna do, Barry? About work? I don't know. I want to do my part for the hive, but I can't do it the way they want. I know how you feel. - You do? - Sure. My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist. - Really? - My only interest is flowers. Our new queen was just elected with that same campaign slogan. Anyway, if you look... There's my hive right there. See it? You're in Sheep Meadow! Yes! I'm right off the Turtle Pond! No way! I know that area. I lost a toe ring there once. - Why do girls put rings on their toes? - Why not? - It's like putting a hat on your knee. - Maybe I'll try that. - You all right, ma'am? - Oh, yeah. Fine. Just having two cups of coffee! Anyway, this has been great. Thanks for the coffee. Yeah, it's no trouble. Sorry I couldn't finish it. If I did, I'd be up the rest of my life. Are you...? Oan I take a piece of this with me? Sure! Here, have a crumb. - Thanks! - Yeah. All right. Well, then... I guess I'll see you around. Or not. OK, Barry. And thank you so much again... for before. Oh, that? That was nothing. Well, not nothing, but... Anyway... This can't possibly work. He's all set to go. We may as well try it. OK, Dave, pull the chute. - Sounds amazing. - It was amazing! It was the scariest, happiest moment of my life. Humans! I can't believe you were with humans! Giant, scary humans! What were they like? Huge and crazy. They talk crazy. They eat crazy giant things. They drive crazy. - Do they try and kill you, like on TV? - Some of them. But some of them don't. - How'd you get back? - Poodle. You did it, and I'm glad. You saw whatever you wanted to see. You had your "experience." Now you can pick out yourjob and be normal. - Well... - Well? Well, I met someone. You did? Was she Bee-ish? - A wasp?! Your parents will kill you! - No, no, no, not a wasp. - Spider? - I'm not attracted to spiders. I know it's the hottest thing, with the eight legs and all. I can't get by that face. So who is she? She's... human. No, no. That's a bee law. You wouldn't break a bee law. - Her name's Vanessa. - Oh, boy. She's so nice. And she's a florist! Oh, no! You're dating a human florist! We're not dating. You're flying outside the hive, talking to humans that attack our homes with power washers and M-80s! One-eighth a stick of dynamite! She saved my life! And she understands me. This is over! Eat this. This is not over! What was that? - They call it a crumb. - It was so stingin' stripey! And that's not what they eat. That's what falls off what they eat! - You know what a Oinnabon is? - No. It's bread and cinnamon and frosting. They heat it up... Sit down! ...really hot! - Listen to me! We are not them! We're us. There's us and there's them! Yes, but who can deny the heart that is yearning? There's no yearning. Stop yearning. Listen to me! You have got to start thinking bee, my friend. Thinking bee! - Thinking bee. - Thinking bee. Thinking bee! Thinking bee! Thinking bee! Thinking bee! There he is. He's in the pool. You know what your problem is, Barry? I gotta start thinking bee? How much longer will this go on? It's been three days! Why aren't you working? I've got a lot of big life decisions to think about. What life? You have no life! You have no job. You're barely a bee! Would it kill you to make a little honey? Barry, come out. Your father's talking to you. Martin, would you talk to him? Barry, I'm talking to you! You coming? Got everything? All set! Go ahead. I'll catch up. Don't be too long. Watch this! Vanessa! - We're still here. - I told you not to yell at him. He doesn't respond to yelling! - Then why yell at me? - Because you don't listen! I'm not listening to this. Sorry, I've gotta go. - Where are you going? - I'm meeting a friend. A girl? Is this why you can't decide? Bye. I just hope she's Bee-ish. They have a huge parade of flowers every year in Pasadena? To be in the Tournament of Roses, that's every florist's dream! Up on a float, surrounded by flowers, crowds cheering. A tournament. Do the roses compete in athletic events? No. All right, I've got one. How come you don't fly everywhere? It's exhausting. Why don't you run everywhere? It's faster. Yeah, OK, I see, I see. All right, your turn. TiVo. You can just freeze live TV? That's insane! You don't have that? We have Hivo, but it's a disease. It's a horrible, horrible disease. Oh, my. Dumb bees! You must want to sting all those jerks. We try not to sting. It's usually fatal for us. So you have to watch your temper. Very carefully. You kick a wall, take a walk, write an angry letter and throw it out. Work through it like any emotion: Anger, jealousy, lust. Oh, my goodness! Are you OK? Yeah. - What is wrong with you?! - It's a bug. He's not bothering anybody. Get out of here, you creep! What was that? A Pic 'N' Save circular? Yeah, it was. How did you know? It felt like about 10 pages. Seventy-five is pretty much our limit. You've really got that down to a science. - I lost a cousin to Italian Vogue. - I'll bet. What in the name of Mighty Hercules is this? How did this get here? Oute Bee, Golden Blossom, Ray Liotta Private Select? - Is he that actor? - I never heard of him. - Why is this here? - For people. We eat it. You don't have enough food of your own? - Well, yes. - How do you get it? - Bees make it. - I know who makes it! And it's hard to make it! There's heating, cooling, stirring. You need a whole Krelman thing! - It's organic. - It's our-ganic! It's just honey, Barry. Just what?! Bees don't know about this! This is stealing! A lot of stealing! You've taken our homes, schools, hospitals! This is all we have! And it's on sale?! I'm getting to the bottom of this. I'm getting to the bottom of all of this! Hey, Hector. - You almost done? - Almost. He is here. I sense it. Well, I guess I'll go home now and just leave this nice honey out, with no one around. You're busted, box boy! I knew I heard something. So you can talk! I can talk. And now you'll start talking! Where you getting the sweet stuff? Who's your supplier? I don't understand. I thought we were friends. The last thing we want to do is upset bees! You're too late! It's ours now! You, sir, have crossed the wrong sword! You, sir, will be lunch for my iguana, Ignacio! Where is the honey coming from? Tell me where! Honey Farms! It comes from Honey Farms! Orazy person! What horrible thing has happened here? These faces, they never knew what hit them. And now they're on the road to nowhere! Just keep still. What? You're not dead? Do I look dead? They will wipe anything that moves. Where you headed? To Honey Farms. I am onto something huge here. I'm going to Alaska. Moose blood, crazy stuff. Blows your head off! I'm going to Tacoma. - And you? - He really is dead. All right. Uh-oh! - What is that?! - Oh, no! - A wiper! Triple blade! - Triple blade? Jump on! It's your only chance, bee! Why does everything have to be so doggone clean?! How much do you people need to see?! Open your eyes! Stick your head out the window! From NPR News in Washington, I'm Oarl Kasell. But don't kill no more bugs! - Bee! - Moose blood guy!! - You hear something? - Like what? Like tiny screaming. Turn off the radio. Whassup, bee boy? Hey, Blood. Just a row of honey jars, as far as the eye could see. Wow! I assume wherever this truck goes is where they're getting it. I mean, that honey's ours. - Bees hang tight. - We're all jammed in. It's a close community. Not us, man. We on our own. Every mosquito on his own. - What if you get in trouble? - You a mosquito, you in trouble. Nobody likes us. They just smack. See a mosquito, smack, smack! At least you're out in the world. You must meet girls. Mosquito girls try to trade up, get with a moth, dragonfly. Mosquito girl don't want no mosquito. You got to be kidding me! Mooseblood's about to leave the building! So long, bee! - Hey, guys! - Mooseblood! I knew I'd catch y'all down here. Did you bring your crazy straw? We throw it in jars, slap a label on it, and it's pretty much pure profit. What is this place? A bee's got a brain the size of a pinhead. They are pinheads! Pinhead. - Oheck out the new smoker. - Oh, sweet. That's the one you want. The Thomas 3000! Smoker? Ninety puffs a minute, semi-automatic. Twice the nicotine, all the tar. A couple breaths of this knocks them right out. They make the honey, and we make the money. "They make the honey, and we make the money"? Oh, my! What's going on? Are you OK? Yeah. It doesn't last too long. Do you know you're in a fake hive with fake walls? Our queen was moved here. We had no choice. This is your queen? That's a man in women's clothes! That's a drag queen! What is this? Oh, no! There's hundreds of them! Bee honey. Our honey is being brazenly stolen on a massive scale! This is worse than anything bears have done! I intend to do something. Oh, Barry, stop. Who told you humans are taking our honey? That's a rumor. Do these look like rumors? That's a conspiracy theory. These are obviously doctored photos. How did you get mixed up in this? He's been talking to humans. - What? - Talking to humans?! He has a human girlfriend. And they make out! Make out? Barry! We do not. - You wish you could. - Whose side are you on? The bees! I dated a cricket once in San Antonio. Those crazy legs kept me up all night. Barry, this is what you want to do with your life? I want to do it for all our lives. Nobody works harder than bees! Dad, I remember you coming home so overworked your hands were still stirring. You couldn't stop. I remember that. What right do they have to our honey? We live on two cups a year. They put it in lip balm for no reason whatsoever! Even if it's true, what can one bee do? Sting them where it really hurts. In the face! The eye! - That would hurt. - No. Up the nose? That's a killer. There's only one place you can

---
## [Xtended-Devices/kernel_oneplus_sm8150](https://github.com/Xtended-Devices/kernel_oneplus_sm8150)@[2c66467b1a...](https://github.com/Xtended-Devices/kernel_oneplus_sm8150/commit/2c66467b1a9b4bbfa818f79b3d69b4f761c2e072)
#### Thursday 2022-09-22 05:41:21 by alk3pInjection

drm: Handle dim for udfps

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

---
## [bitnine-oss/agensgraph](https://github.com/bitnine-oss/agensgraph)@[b6002a796d...](https://github.com/bitnine-oss/agensgraph/commit/b6002a796dc0bfe721db5eaa54ba9d24fd9fd416)
#### Thursday 2022-09-22 06:27:51 by David Rowley

Add Result Cache executor node

Here we add a new executor node type named "Result Cache".  The planner
can include this node type in the plan to have the executor cache the
results from the inner side of parameterized nested loop joins.  This
allows caching of tuples for sets of parameters so that in the event that
the node sees the same parameter values again, it can just return the
cached tuples instead of rescanning the inner side of the join all over
again.  Internally, result cache uses a hash table in order to quickly
find tuples that have been previously cached.

For certain data sets, this can significantly improve the performance of
joins.  The best cases for using this new node type are for join problems
where a large portion of the tuples from the inner side of the join have
no join partner on the outer side of the join.  In such cases, hash join
would have to hash values that are never looked up, thus bloating the hash
table and possibly causing it to multi-batch.  Merge joins would have to
skip over all of the unmatched rows.  If we use a nested loop join with a
result cache, then we only cache tuples that have at least one join
partner on the outer side of the join.  The benefits of using a
parameterized nested loop with a result cache increase when there are
fewer distinct values being looked up and the number of lookups of each
value is large.  Also, hash probes to lookup the cache can be much faster
than the hash probe in a hash join as it's common that the result cache's
hash table is much smaller than the hash join's due to result cache only
caching useful tuples rather than all tuples from the inner side of the
join.  This variation in hash probe performance is more significant when
the hash join's hash table no longer fits into the CPU's L3 cache, but the
result cache's hash table does.  The apparent "random" access of hash
buckets with each hash probe can cause a poor L3 cache hit ratio for large
hash tables.  Smaller hash tables generally perform better.

The hash table used for the cache limits itself to not exceeding work_mem
* hash_mem_multiplier in size.  We maintain a dlist of keys for this cache
and when we're adding new tuples and realize we've exceeded the memory
budget, we evict cache entries starting with the least recently used ones
until we have enough memory to add the new tuples to the cache.

For parameterized nested loop joins, we now consider using one of these
result cache nodes in between the nested loop node and its inner node.  We
determine when this might be useful based on cost, which is primarily
driven off of what the expected cache hit ratio will be.  Estimating the
cache hit ratio relies on having good distinct estimates on the nested
loop's parameters.

For now, the planner will only consider using a result cache for
parameterized nested loop joins.  This works for both normal joins and
also for LATERAL type joins to subqueries.  It is possible to use this new
node for other uses in the future.  For example, to cache results from
correlated subqueries.  However, that's not done here due to some
difficulties obtaining a distinct estimation on the outer plan to
calculate the estimated cache hit ratio.  Currently we plan the inner plan
before planning the outer plan so there is no good way to know if a result
cache would be useful or not since we can't estimate the number of times
the subplan will be called until the outer plan is generated.

The functionality being added here is newly introducing a dependency on
the return value of estimate_num_groups() during the join search.
Previously, during the join search, we only ever needed to perform
selectivity estimations.  With this commit, we need to use
estimate_num_groups() in order to estimate what the hit ratio on the
result cache will be.   In simple terms, if we expect 10 distinct values
and we expect 1000 outer rows, then we'll estimate the hit ratio to be
99%.  Since cache hits are very cheap compared to scanning the underlying
nodes on the inner side of the nested loop join, then this will
significantly reduce the planner's cost for the join.   However, it's
fairly easy to see here that things will go bad when estimate_num_groups()
incorrectly returns a value that's significantly lower than the actual
number of distinct values.  If this happens then that may cause us to make
use of a nested loop join with a result cache instead of some other join
type, such as a merge or hash join.  Our distinct estimations have been
known to be a source of trouble in the past, so the extra reliance on them
here could cause the planner to choose slower plans than it did previous
to having this feature.  Distinct estimations are also fairly hard to
estimate accurately when several tables have been joined already or when a
WHERE clause filters out a set of values that are correlated to the
expressions we're estimating the number of distinct value for.

For now, the costing we perform during query planning for result caches
does put quite a bit of faith in the distinct estimations being accurate.
When these are accurate then we should generally see faster execution
times for plans containing a result cache.  However, in the real world, we
may find that we need to either change the costings to put less trust in
the distinct estimations being accurate or perhaps even disable this
feature by default.  There's always an element of risk when we teach the
query planner to do new tricks that it decides to use that new trick at
the wrong time and causes a regression.  Users may opt to get the old
behavior by turning the feature off using the enable_resultcache GUC.
Currently, this is enabled by default.  It remains to be seen if we'll
maintain that setting for the release.

Additionally, the name "Result Cache" is the best name I could think of
for this new node at the time I started writing the patch.  Nobody seems
to strongly dislike the name. A few people did suggest other names but no
other name seemed to dominate in the brief discussion that there was about
names. Let's allow the beta period to see if the current name pleases
enough people.  If there's some consensus on a better name, then we can
change it before the release.  Please see the 2nd discussion link below
for the discussion on the "Result Cache" name.

Author: David Rowley
Reviewed-by: Andy Fan, Justin Pryzby, Zhihong Yu
Tested-By: Konstantin Knizhnik
Discussion: https://postgr.es/m/CAApHDvrPcQyQdWERGYWx8J%2B2DLUNgXu%2BfOSbQ1UscxrunyXyrQ%40mail.gmail.com
Discussion: https://postgr.es/m/CAApHDvq=yQXr5kqhRviT2RhNKwToaWr9JAN5t+5_PzhuRJ3wvg@mail.gmail.com

---
## [sillsdev/chorus](https://github.com/sillsdev/chorus)@[7d1b3e3ff1...](https://github.com/sillsdev/chorus/commit/7d1b3e3ff1263a48741f82babe3a1215aa0331aa)
#### Thursday 2022-09-22 07:16:19 by josephmyers

.hgrc points to chorusmerge on Linux (bugfix) (#297)

LibChorus now also runs its suite on .NET6. The bug was preventing LfMerge from a successful S/R in LanguageForge. There is another issue (in LfMerge) that is already fixed there. With these two fixes, LfMerge successfully uses the .NET6 version of ChorusMerge to resolve merge issues. Below are the cleaned-up commits:


* Adding .NET6 target to LibChorus.Tests.csproj

This is an effort to reproduce the chorusmerge script failure on .NET6. The script may be being called by LfMerge, but something about the ChorusMerge executable has changed between Framework and .NET6. It could be a pathing issue. I noticed that when I mangled the executable name in the hgrc, the "hg merge" command failed silently, as it does in production. Now, I seem to remember verifying chorusmerge wasn't even being launched in the lfmerge container. However, with the changes in ExecutionEnvironment, we don't use chorusmerge in the first place, which would be a great improvement if it's possible. Sending this to the other computer, since this one's WSL is hosed.

* Seeing what happens when the hgrc always points to ChorusMerge.exe over the script. Based on the comment, it would appear chorusmerge was only necessary for Mono. It would be really nice to be able to eliminate that extra piece from the equation, but it's near impossible to test without pushing packages to Nuget. Also not clear is why the hgrc is even using the chorusmerge script, when that set lies in IsMono code. Is Platform.IsMono true when on .NET6?

* Registering 1252 encoding.

This is required on .NET6 to prevent an exception.

* Re-introducing the chorusmerge setting in hgrc

However, instead of triggering off of Platform.IsMono, we trigger off of Platform.IsLinux. It's not Mono that makes the script required, at least apparently. hg isn't able to launch the .exe directly on Linux. Someone with more Linux experience may be able to configure it to do so, but for the current effort I'm re-integrating the chorusmerge script.

* chorusmerge test script uses dotnet

Got the test failure I was expecting. The test chorusmerge is being called. This is different from how I remember production behaving. I wasn't able to verify chorusmerge is being called in the production environment. But there could've been something else going on.

* Going back to Platform.IsLinux

With .IsMono, the test, according to the output statements, is failing like the production environment. So that's a good step

* Trying to get ChorusMerge.exe to exec

dotnet run is not working, which is what's in the production code

* Fixing a test based on the recent Platform.IsMono -> .IsLinux change

It's certainly possible this actually specific to Mono, but I think it in fact applies to Linux as a whole, and the previous was a slight oversight. We'll see what the build server thinks.

---
## [Poyo2007/Bad-Engine](https://github.com/Poyo2007/Bad-Engine)@[44993f7b90...](https://github.com/Poyo2007/Bad-Engine/commit/44993f7b9093173c04bb1732f489eaded01c2d2a)
#### Thursday 2022-09-22 07:46:13 by Poyo2007

WHY AM I SO DUMB IVE BEEN STRUGGLING ALL DAY WITH THIS I HATE MYSELF OH MY GOD

---
## [kmeixner247/ft_containers](https://github.com/kmeixner247/ft_containers)@[b225675990...](https://github.com/kmeixner247/ft_containers/commit/b22567599044c70b510a498f3c57ba05d7af35d8)
#### Thursday 2022-09-22 09:52:13 by Konstantin Meixner

forgot to initialize capacity in default constructor which broke LITERALLY FUCKING EVERYTHING OH MY GOD THIS TOOK ME SO MUCH TIME

---
## [WhatHappenedTo2nd/ft_transcendence](https://github.com/WhatHappenedTo2nd/ft_transcendence)@[14276067f5...](https://github.com/WhatHappenedTo2nd/ft_transcendence/commit/14276067f574a211ed683fa68833e1e7816e94e2)
#### Thursday 2022-09-22 10:07:24 by inyang

conflicting backend package-lock.json file fuck you

---
## [bderya/42Exam_rank-2](https://github.com/bderya/42Exam_rank-2)@[f2ee10f1c3...](https://github.com/bderya/42Exam_rank-2/commit/f2ee10f1c3950e0080d6b8aa1c7fc766cd70a0c7)
#### Thursday 2022-09-22 10:33:23 by bderya

Update tab.c

i. changed your code because itswrong fuck you abdel i hope you will accept

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Thursday 2022-09-22 10:39:52 by Xavier Morel

[IMP] *: owlify password meter and convert change password to real wizard

The changes in `auth_password_policy` are largely the owlification of
the password meter widget:

- modernize the password policy module and convert it to an
  odoo-module (note: now exports a pseudo-abstract class which is
  really a policy, for the sake of somewhat sensibly typing
  `recommendations`)
- replace the implementation of the Meter and PasswordField widgets by
  owl versions

The changes to web and base stem from taking a look at converting the
ChangePassword wizard, and finding that it would be a pain in the ass
but also... unnecessary? It seems to have been done as a wizard
completely in javascript despite being backend-only for legacy
reasons: apparently one of the very old web clients (v5 or v6
probably) implemented it as a "native action" which was directly part
of the client's UI, and so it had to be implemented entirely in the
client.

Over time it was moved back into the regular UI (and moved around
quite a bit), hooked as a client action to maintain access to the
existing UI / dialog.

But since it's been an action opened via a button for years it can
just... be a normal wizard, with password fields, which
auth_password_policy can then set the widget of.

So did that:

- removed the old unnecessary JS, and its dedicated endpoint (which is
  *not* used by portal, portal has its own endpoint)
- used check_identity for the "old password check"
- split out `change_password` with an internal bit so we can have a
  safer (and logged) "set user password" without needing to provide
  the old password, which is now used for the bulk password change
  wizard as well
- added a small wizard which just takes a new password (and
  confirmation), for safety a given change password wizard is only
  accessible to their creator (also the wizard is restricted to
  employees though technically it would probably be fine for portal
  users as well)

Rather than extensive messy rewrite / monkeypatching (the original
wizard was 57 LOC, though also 22 LOC of template, the auth_policy
hooking / patching was 33, plus 8 lines of CSS),
`auth_password_policy` just sets the widget of the `new_password`
field in the new wizard, much as it did the bulk wizard.

Also improve the "hide meter if field is empty" feature by leveraging
`:placeholder-shown`. This requires setting a placeholder, and while
empty works fine in firefox, it doesn't work in chrome. So the
placeholder needs to be a single space. Still, seems better than
updating a fake attribute or manipulating a class for the sake of
trivial styling.

Notes on unlink + transient vacuum

Although the wizard object is only created when actually calling
`change_password`, and is deleted on success, it is possible for the
user to get an error and fail to continue (it should be unlikely
without overrides since the passwords are checked while creating /
saving but...).

While in that case the `new_password` in the database is not the
user's own, it could be their *future* password, or give evidence as
to their password-creation scheme, or some other signal useful to
attack that front of the user's life and behavior. As such, quickly
removing leftovers from the database (by setting a very low transient
lifetime) seems like a good idea.

This is compounded by the `check_identity` having a grace period of 10
minutes. 0.1 is 6 minutes, but because the cron runs every 10 the user
effectively has 6~10 minutes between the moment they create an
incorrect / incomplete version of the wizard and the moment where it
is destroyed if they just leave it.

closes odoo/odoo#99458

Signed-off-by: Xavier Morel (xmo) <xmo@odoo.com>

---
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[7fed801135...](https://github.com/justinpryzby/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Thursday 2022-09-22 11:05:37 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [phytec/linux-phytec-mainline](https://github.com/phytec/linux-phytec-mainline)@[adee8f3082...](https://github.com/phytec/linux-phytec-mainline/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2022-09-22 11:57:28 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [neildavis/mame2003-plus-libretro](https://github.com/neildavis/mame2003-plus-libretro)@[fecf11dfbd...](https://github.com/neildavis/mame2003-plus-libretro/commit/fecf11dfbdf77f24dc20531d5bc489c5ec9fb80f)
#### Thursday 2022-09-22 12:31:58 by Kyland K

Killer Instinct 1 and 2 Cheats Update! (#1325)

Note: Being that this the initial addition of massively updated KI1 and KI2 Cheats, please do not expect all Cheats to fully function as advertised! Some of the Cheats may be subject to change in future Updates!

Killer Instinct 1 and 2 Cheats Update!
Killer Instinct 1: Attack and Movement Speed Manipulation via Updated Cheats (cheat.dat)!

Selection of 12 different speeds and 21 different sizes, including Defaults.  You can choose to move as slow as molasses, or as fast as a Jedi!  Fight as a metaphorical watching paint dry sloth, or as frenetic as a one inch punch from Bruce Lee!  You can also be as small as a mouse or as large as a Kaiju!

Dozens of other Cheats added for both Killer Instinct 1 and 2, including Automated Ultra Combos and Humiliations and No Mercy Finishers!

Personal thanks to Mahoneyt944 and Abystus for their incredible efforts and insight in this little project I personally wanted to implement to help better lower spec platforms!

retroarch/system/mame2003-xtreme/cheat.dat

retroarch/system/mame2003-plus/cheat.dat

If using 2003 Plus, you must delete the .rzip, before the new cheat.dat will take effect!

R2 to open MAME Menu on 2003 Xtreme; L3 or Core Options to do the same for 2003 Plus.

Select Cheats, Apply, Resume Game, Rinse and Repeat, Enjoy the Performance/Speed Boost!

---
## [HutchyBean/Fedoraware-crack](https://github.com/HutchyBean/Fedoraware-crack)@[50a54973e7...](https://github.com/HutchyBean/Fedoraware-crack/commit/50a54973e76ff2315320cab53235f3a91da053c8)
#### Thursday 2022-09-22 14:04:12 by Baan

Merge pull request #693 from Radeon0078/patch-1

fuck you this is better kys 130 fov sucks balls

---
## [fcsonline/factorial-dotfiles](https://github.com/fcsonline/factorial-dotfiles)@[277b8a2c09...](https://github.com/fcsonline/factorial-dotfiles/commit/277b8a2c0904e13000f5a6ea713bd92d2f32fb48)
#### Thursday 2022-09-22 14:55:49 by Pau Ramon Revilla

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
## [jorbian/holbertonschool-low_level_programming](https://github.com/jorbian/holbertonschool-low_level_programming)@[68162f1d74...](https://github.com/jorbian/holbertonschool-low_level_programming/commit/68162f1d741c7f9c55dfa855a415bf8963cd90ec)
#### Thursday 2022-09-22 15:21:42 by jorbian

Again, just back to the checker saying "It's wrong because fuck you."

---
## [OmniSharp/omnisharp-roslyn](https://github.com/OmniSharp/omnisharp-roslyn)@[efeafeca33...](https://github.com/OmniSharp/omnisharp-roslyn/commit/efeafeca33abe1d19659ed8c7ebab1d7c3481188)
#### Thursday 2022-09-22 17:22:56 by Fredric Silberberg

Host dependency cleanup

Today, we delete a a few dlls in the cake packaging scripts, to remove DLLs that should come from the runtime we're loaded with, rather than the dlls we built with. This is fine for packaging, but is annoying when doing local tests by just rebuilding the relevant driver, because you have to remember to go into the output directly and delete them every time. I addressed this by removing the dlls in msbuild itself:

* System.Configuration.ConfigurationManager: this was a transitive dependency through Microsoft.CodeAnalysis.Features -> Microsoft.CodeAnalysis.Elfie. We don't need Elfie or its dependencies, so I made all references to these layers explicit and turned off flowing of transitive dependencies. This does cause a slight issue: one of those transitive dependencies is System.Text.Json 6.0, while OmniSharp.MSBuild transitively references 5.0. To ensure the appropriate binding redirects are still generated, I added an explicit reference to System.Text.Json, but we are not using that reference for anything else.
* Nuget.*.dll: these are real dependencies that we should not ship in .NET 6+. I added a target to remove that version from the list of files to be copied.

---
## [andercard0/duckstation](https://github.com/andercard0/duckstation)@[ae2241f718...](https://github.com/andercard0/duckstation/commit/ae2241f7186428f63101409f901899345a1fda87)
#### Thursday 2022-09-22 18:18:25 by Anderson 0 Cardoso

Update chtDb to the latest

Following games were updated in the Database:

- Spyro 2 - Ripto's Rage
- Medal Of Honor
- Digimon World 3
- Megaman Legends 2
- Star Ocean - The Second Story
- Disney Presents Tigger's Honey Hunt
- Spyro X Sparx - Tondemo Tours
- Resident Evil 1
- Grand Theft Auto
- Castlevania Symphony Of The Night
- Megaman X
- Dino Crisis
- Valkyrie Profile
- MediEvil 2
- Crash Bandicoot - Warped

---
## [ExactExampl/kernel_motorola_payton](https://github.com/ExactExampl/kernel_motorola_payton)@[2bc2fbcd3b...](https://github.com/ExactExampl/kernel_motorola_payton/commit/2bc2fbcd3b1a0d8810c7607ff36665c911052df0)
#### Thursday 2022-09-22 18:22:52 by Christian Brauner

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
## [icaro105/react](https://github.com/icaro105/react)@[b6978bc38f...](https://github.com/icaro105/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2022-09-22 18:27:55 by Andrew Clark

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
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[893cb76636...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/893cb766366cb97def1d8c87266ee64c36e1ee5a)
#### Thursday 2022-09-22 18:34:55 by Nickay

HOLY FUCKING SHIT HOW MANY FUCKING TIME WILL I HAVE TO GO BACK AND FIX THIS SHIT

---
## [renansouzzzz/free-programming-books](https://github.com/renansouzzzz/free-programming-books)@[5fd70502a0...](https://github.com/renansouzzzz/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Thursday 2022-09-22 18:48:14 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [eskoONE/duckstation](https://github.com/eskoONE/duckstation)@[f9212363d3...](https://github.com/eskoONE/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Thursday 2022-09-22 18:54:50 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [IntelligentTech1993/Ultimate-Facebook-Clone-SocialNetwork](https://github.com/IntelligentTech1993/Ultimate-Facebook-Clone-SocialNetwork)@[de34770879...](https://github.com/IntelligentTech1993/Ultimate-Facebook-Clone-SocialNetwork/commit/de34770879ba4f22dc388592bac08ca715513051)
#### Thursday 2022-09-22 19:13:15 by تكنولوجيا الحلول التقنية الاستشارية المستقبلية المتكاملة Integrated Future Technology Consulting Technology Solutions

Ultimate Facebook Clone Social Network Platform

Frontend
High Performance & High Level Cache System: The #1 thing that must be available on any social network website, The Speed ! Speed up your website with our Cache system, enable it and the website can handle more than 1 Million user!
Wonder (New Feature): With our new feature, user can wonder posts, photos, videos.
RTL Support: WoWonder also supports right to left languages.
Social Login: With WoWonder you can login via most famous social media websites like (Facebook â€“ Twitter â€“ Google+ â€“ LinkedIn â€“ Vk â€“ Instagram).
Easy & Nice Looking URL: Users, Pages, Group all in one tiny URL !
User Last Seen: Displays userâ€™s last seen/online status.
Profile visit Notification: Receive notification from users who visited your profile.
Friends & Follow System: WoWonder Supports friends system like Facebook, follow system like twitter.
Home/News Feed: Displays Posts, Photos, Files, Videos, and Maps posted by friends/followed people, Also story filters, follow/friends suggestions, and user activities list.
User Timeline: Displays user?s profile with Posts, Photos, Videos posted and shared by user.
Pages: User can create unlimited pages and invite his friends to like the pages.
Groups: User can create unlimited groups and invite/add his friends to his joined groups.
Games: User can play unlimited flash games.
Social Videos Support: User can easily share videos from the biggest videos sharing websites like Youtube, Dailymotion, Vine, Vimeo, Facebook videos & Soundcloud music
Photo Album: User can create unlimited photo albums with nice looking style.
Cover Picture: Dynamic Cover for users.
Profile Picture: Dynamic profile picture for users.
User Privacy: Control who can message you, post on your timeline, follow you, confirm follow requests or not, last seen, etc.
User Profile Info: Displays userâ€™s profile information (birthday, website, gender, social media, about, last seen, etc).
Notifications: Receive notification from users (likes, dislikes, comments, wonders, shares .. etc)
#Hashtags: Displays trending and related topics shared by users.
@Mentions: Use @username to tag people in a status or messages.
Post Publisher: Status, Sound cloud, YouTube, Vine, Google Maps, Videos, Files, Photos and emoticons.
Delete & Edit Posts: User can delete and edit his own posts.
Save Posts: User can save posts to view them later.
User Events: User can share their events like feelings/travailing/watching/playing/listening.
Recent Search: What ever the user was looking for, all will be saved into recent searches with the ability to clear them.
Post Privacy: User can choose the post privacy (Only me, Everyone.. etc)
Likes: Like or unlike a post. View list of people who like this.
Dislike: Dislike a post. View list of people who dislike this.
Comments & Replies: Comment on a post, Reply to a comment, View all post comments.
Search: Search for people, #Hashtags with our filtered search system.
Reports: Report posts to be checked by administrators.
Live Chat: Real-time live chat system, (online, offline) status.
Messages: Send and receive private messages & share files from other Users.
API: retrieve user data, user posts, search for users via API.
Activities: Displays userâ€™s latest activities (likes, shares,comments, wonders)
Multi Languages: 4 Languages (Arabic, English, Russian, Turkish) with the ability to add unlimited languages.
Verified Profiles/Pages.
Fully responsive for all devices, browsers.
Password recovery by email.
Online user counter on admin & home page.
Comment auto detector
Emoticons.
and many more.

---
## [edsantiago/libpod](https://github.com/edsantiago/libpod)@[5c914a94a9...](https://github.com/edsantiago/libpod/commit/5c914a94a916c4e90c06c819c5d53b0fafe947ba)
#### Thursday 2022-09-22 19:27:20 by Ed Santiago

Proof of concept: nightly dependency treadmill

As discussed in f2f: this is the cleanest, simplest mechanism
I can think of to auto-test the Big Three dependencies: simply
run go mod edit immediately after git checkout, then run the
entire CI test suite.

If this approach works, we can set up a new CIRRUS_CRON=treadmill
job. I'm expecting it not to work, because Murphy, but want to
see what the unexpected gotchas are.

This differs significantly from the buildah treadmill, in that
buildah is almost impossible to re-vendor without manual intervention.
(In practice, so are these, but let's dream of a world in which
this will run and pass every night). (I want a pony too).

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [Bang-Coder/I-don-t-know-what-the-f-k-i-am-doing](https://github.com/Bang-Coder/I-don-t-know-what-the-f-k-i-am-doing)@[7424538375...](https://github.com/Bang-Coder/I-don-t-know-what-the-f-k-i-am-doing/commit/7424538375530cde60af72ac28c887a78200891b)
#### Thursday 2022-09-22 19:29:13 by Bang-Coder

Rename Go fuck your self to Go fuck your self.html

---
## [ianstormtaylor/superstruct](https://github.com/ianstormtaylor/superstruct)@[d9fc2ff0a7...](https://github.com/ianstormtaylor/superstruct/commit/d9fc2ff0a7af71ad7f1bc0aa10eb61806b75d9cc)
#### Thursday 2022-09-22 19:29:58 by Elliot Winkler

Support Node 14 (again) (#1112)

It appears that between 0.16.0 and 0.16.1, the minimum version of Node required
to use this package changed, from 14.x to 16.x. This was not explicit but seems
to have been caused by a couple of factors.

But first, what changed. If you look at `src/error.ts` in 0.16.0 you will see
[this line][1]:

```
return (cached ??= [failure, ...failures()])
```

In the [published version of this file in 0.16.0][2] this gets transpiled to:

```
return (_cached = cached) != null ? _cached : cached = [failure, ...failures()];
```

In 0.16.1, the [original line is unchanged][3], but in the [published
version][4] it is transpiled to:

```
return cached ??= [failure, ...failures()];
```

The `??=` syntax is not supported by Node 14, hence, developers are forced to
upgrade to at least Node 16 if they want to use v0.16.1 or greater.

After looking at the diff between these two versions and running some
experiments, I believe that there are two reasons why this line shows up
differently in these two published versions.

1. Different Node versions were used to build and publish these versions. It
appears that Node 14 was used for the former whereas Node 16 was used for the
latter. This assertion is supported by the fact that in the [Rollup
configuration][5], `@babel/preset-env` is configured with `node: true`, which
instructs Babel to [use the current version of Node as a target][6]. So if the
current Node version changes, so does the Babel config.
2. Between 0.16.0 and 0.16.1, [`browserslist` was updated from 4.20.3, to
4.21.4][7] (you will probably need to expand `yarn.lock`; if so, Cmd-F for
"browserslist"). In `browserslist` 4.21.0, [IE 11 was removed from the default
set of browsers][8] (which is being used in this case, since no explicit list is
provided). According to caniuse, [IE 11 does not support the `??=` syntax][9],
so its removal means that Babel doesn't need to transpile this syntax any
longer.

To address this problem, this PR:

* changes the Rollup configuration mentioned above to use `node: "14.0"` instead
of `node: true`, so that Node 14 is always used to compute the transpilation
rules regardless of the version of Node used locally to build and publish the
package
* updates the CI workflow to ensure that Node 14 is being tested (along with 16
and 18)
* adds Node >= 14 to the `engines` field to communicate that it is supported

---

One thing you may wonder is why this change is needed at all. Node 16 is the
current LTS, so shouldn't that be enough? True, but Node 14 hasn't hit
end-of-life yet, and many people are still using it, including my company. We
think this package is really great, but it would be even better if we didn't
have to have a workaround for our libraries that we still want to keep on Node
14.

Thanks for considering :)

[1]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.0/src/error.ts#L44
[2]: https://unpkg.com/superstruct@0.16.0/lib/index.cjs
[3]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.1/src/error.ts#L44
[4]: https://unpkg.com/superstruct@0.16.1/lib/index.cjs.js
[5]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.4/config/rollup.js#L26
[6]: https://babel.dev/docs/en/options#targetsnode
[7]: https://github.com/ianstormtaylor/superstruct/compare/v0.16.0...v0.16.1?diff=unified#diff-51e4f558fae534656963876761c95b83b6ef5da5103c4adef6768219ed76c2deL99
[8]: https://github.com/browserslist/browserslist/blob/main/CHANGELOG.md#421
[9]: https://caniuse.com/?search=%3F%3F%3D

---
## [dootMaster/zulip-mobile](https://github.com/dootMaster/zulip-mobile)@[0af1d1133c...](https://github.com/dootMaster/zulip-mobile/commit/0af1d1133c50f38057877eba063f837f82b961bd)
#### Thursday 2022-09-22 21:47:19 by Chris Bobbe

UnicodeEmoji [nfc]: Reduce to just what we use; cut out r-n-vector-icons

Emojis aren't icons, so even from its name, it's not clear that
react-native-vector-icons is best suited to render them, even if it
has turned out to be convenient for a subset of emoji (Unicode
emoji).

Like avatars, emojis are a mode of freeform user expression (think
of the "thank you" emoji). Icons, on the other hand, are a palette
of UI elements that UI designers use to convey UI meaning and make
the UI more approachable. ("Ah, a star icon, I bet that'll take me
to starred messages if I press it.")

The createIconSet function from r-n-vector-icons is designed to give
us such a palette of UI elements: we're to call it once, at module
top-level, and and it'll give us a React component that can render
any one of a static menu of icons. We've co-opted that into "a
static menu of Unicode emoji," but that's worked fine so far.

But, with #2956, we don't want a static menu, we want a menu that's
defined by the server. That's a breaking point for continuing to use
createIconSet here. We'd have to handle these constraints:
  - We can't call createIconSet at module top-level anymore, since
    we don't have the server data at that time.
  - We'd have to call it before it's time to render a Unicode emoji.
…And that seems like too much trouble to keep around something that
isn't designed for this use case anyway.

So, as a first step, in this commit, take part of createIconSet's
returned component [1] -- just enough to preserve current behavior
-- and define it in a separate file. It's pretty small, so, go ahead
and convert to a function component while we're at it. After this,
it'll be an easy switch to consume data from Redux, with
useSelector.

[1] node_modules/react-native-vector-icons/lib/create-icon-set.js

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d34fa4c642...](https://github.com/tgstation/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Thursday 2022-09-22 22:34:12 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---

