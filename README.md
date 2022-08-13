## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-12](docs/good-messages/2022/2022-08-12.md)


1,957,572 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,957,572 were push events containing 2,874,941 commit messages that amount to 206,517,946 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [checkraisefold/Foundation-19](https://github.com/checkraisefold/Foundation-19)@[e4613632cc...](https://github.com/checkraisefold/Foundation-19/commit/e4613632cc5b9ab4363d8c768752d74623e9112b)
#### Friday 2022-08-12 00:08:05 by Grey

Remove ERT Code that makes it so you can't call the shuttle for 30 minutes (#639)

* gets rid of old dumb code

* Revert "gets rid of old dumb code"

This reverts commit a816ca0c26964781b8a0bdf2d1af4858bc76964d.

* simpler implementation (i was strongarmed)

* removes the datum

* fuck your predicates they're not used anywhere

* Revert "fuck your predicates they're not used anywhere"

This reverts commit eefa96c718892a74936efff85b96edbef4382c0a.

* Revert "Revert "fuck your predicates they're not used anywhere""

This reverts commit 6ad00652eda432e76c4cf1a6edf0ff0ee4bcafa8.

* THIS TIME WE ACTUALLY REMOVE THE DME RIGHT

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[2002678591...](https://github.com/ammarfaizi2/linux-fork/commit/2002678591f643adea8bfa62a65080fcd3ddc225)
#### Friday 2022-08-12 00:26:14 by Johannes Weiner

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
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[1ab6eb1716...](https://github.com/srsbsns5/GAN-GDDS1/commit/1ab6eb17160a1f130584d76c075528029c513592)
#### Friday 2022-08-12 00:54:19 by schmidtheimer

Minor changes to hitboxes to and item pickup

Balls hanging low while I pop a bottle off a yacht
Chain swanging, cling-clang and it cost a lot
Bitch, I'm always after guala, yeah, and you are not
Bad-ass B, keep on going 'til you hit the spot
Woah, I'm a big bag hunter with the bow
She got a big bad dumper, drop it low
Mama called me and she happy with the growth
Never ever fold for a thottie, that's an oath (Yeah, ayy)

[Verse 1: Rich Brian & bbno$]
Just popped her kidney, I bought a million
Options of the stock and I stopped doin' the green
Man, I rock arenas, bringin' the peace, I'm bumpin' that Pac
In the car, pretendin' I got all the eyes on me
Got a bad baby and she's independent
Too many people older than me that's seekin' attention
When they warned me 'bout the goofies, man, I shoulda listened
And the smell of the money My Strangest Addiction, uh
She tip for dick, I let her lick
I had to dip, I'm off a fifth, am I rich now?
I bought a whip, I paint it pink
It drive itself, the fuck you think? Yeah, I'm rich now
[Pre-Chorus: bbno$]
Ayy, lil' mama, yeah, you heard about me
I'ma pop you like a pea, yeah, edamame
Yeah, feel so hot like I'm chillin' on the beach
Yeah, baby in the sun like the Teletubbies (Woo)

[Chorus: bbno$]
Balls hanging low while I pop a bottle off a yacht
Chain swanging, cling-clang and it cost a lot
Bitch, I'm always after guala, yeah, and you are not
Bad-ass B, keep on going 'til you hit the spot
Woah, I'm a big bag hunter with the bow
She got a big bad dumper, drop it low
Mama called me and she happy with the growth
Never ever fold for a thottie, that's an oath

[Verse 2: Rich Brian & bbno$]
I've been in the club and takin' shots
If you got your mask off in the photo, you getting cropped
Hoppin' out the function, the CVS is like a block away
Bought a moisturizer, my ice cold, it's drying my face
Don't need that VVS, my ice is fake, your life is fake
I choose to do it for my pocket's sake
You basing your opinions on what the major says
I renovate, the bad energy I erase, uh
Yeah, I don't really ever wanna talk, talk, talk, talk
Only really ever want the top, top, top, top
Guess I'm goin' back to the sock, sock, sock, sock
Least this money never really stop, stop, stop, stop

---
## [Blaineworld/fancy-python-slides](https://github.com/Blaineworld/fancy-python-slides)@[0cd234dd8d...](https://github.com/Blaineworld/fancy-python-slides/commit/0cd234dd8d753410ee50adb5b764ed80da809997)
#### Friday 2022-08-12 01:23:33 by Blaineworld

working configuration system

I think it's pretty decent. I wrote this while listening to Splatoon music. I'm going to go do other real life stuff like dog-walking now. How is this relevant to the actual commit? That's the cool part: it isn't! lmao. sorry the splatoon music has me in a silly mood

---
## [scp-cs/scp-cs-wiki](https://github.com/scp-cs/scp-cs-wiki)@[51900dc196...](https://github.com/scp-cs/scp-cs-wiki/commit/51900dc196aa67e8d9fae133c5511cdaf2ab4f0d)
#### Friday 2022-08-12 01:29:00 by HEG1

Stab me in my toaster if I'm mistaken, but all of this is obsolete and useless

It's been a while sice I check on the bugs. Seems like the big update resolved a fair number of them. Also the last fix of info module turned out to be doing abolutely nothing. Yet the classic rating module had still a decent problem. I'm happy we finally managed to make rating/info module to fully function and look good, too. There's still a decent number of small little unclean bugs, but to be honest, none is worth the time nor the massive fucking headache.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[893cb76636...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/893cb766366cb97def1d8c87266ee64c36e1ee5a)
#### Friday 2022-08-12 01:50:09 by Nickay

HOLY FUCKING SHIT HOW MANY FUCKING TIME WILL I HAVE TO GO BACK AND FIX THIS SHIT

---
## [anrui2032-OpenSource/android_kernel_oppo_msm8939](https://github.com/anrui2032-OpenSource/android_kernel_oppo_msm8939)@[f755689e15...](https://github.com/anrui2032-OpenSource/android_kernel_oppo_msm8939/commit/f755689e152c181550b821d9e994d43a0d44fa87)
#### Friday 2022-08-12 02:22:14 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [sortofasian/d3](https://github.com/sortofasian/d3)@[971ebd3bbc...](https://github.com/sortofasian/d3/commit/971ebd3bbce3d3c0ddeb4916cd48aa28670e98ae)
#### Friday 2022-08-12 03:41:07 by sortofasian

HOLY FUCKING SHIT IT'S TOP LEVEL AWAIT + TYPESCRIPT + NODEMON + DEBUG ALL WORKING TOGETHER

---
## [ALarsonPi/goalsApp](https://github.com/ALarsonPi/goalsApp)@[20afe49907...](https://github.com/ALarsonPi/goalsApp/commit/20afe4990799eff15200b6dae49d7b786fba8646)
#### Friday 2022-08-12 04:58:49 by Alec Larson

Note to self - probably would be good if I don't code super late at night. So with these changes, I allowed for a goal to have a subgoal, fixed routing and updated the goalscreen UI accordingly. Also figured out that custom scroll view and sliver list would be the best way to display all this as they're super fast, don't take up much memory, and lazy loading. Yeah, routing was the main part of these updates. Also, it would definately be good to note that Android has some major display discrepancies with how IOS is showing up (especially with the carousel). So I'll want to get those fixed. Each day I work on this app, I figure out just how much bigger of an app it really is...lol. So it is with scope creep

---
## [SimonCalleLaverde/project-x-2022-next-js](https://github.com/SimonCalleLaverde/project-x-2022-next-js)@[5bbf14801c...](https://github.com/SimonCalleLaverde/project-x-2022-next-js/commit/5bbf14801c76a16762ea42160b7cc3adbec21139)
#### Friday 2022-08-12 04:58:52 by Simon Calle Laverde

My Cat Ñeña (My Only Son & Best Friend) Left Me This Week. AUG 07, 2022.

-- Travelled to my parent's place this week for 3 days without my Mac.

- Will commit some random small file title changes I had done on Friday August 05, 2022. 6 days ago. When the night after my cat died, during the early-morning/dawn of 07.
- Will commit before continuing as per the next commit/&-todo-list I had already written on the 05, shown below.
- Uploading a picture of my cat to "/public". Might do something or inspire to do something after.

----------------------------------
Creating "pages/index.js" & "components/ProjectCard.js" Files' Structure. Fetching From GraphCMS.

- Creating "components/ProjectCard.js". ...
- Printing/Passing data/props from "projects" within Hygraph, in/into "pages/index.js"/"<ProjectCard/>". ...

-- Continued revising old "Portfolio V3 2022 NextJS" to get to what I had done:
º Homepage as it was there (but now with this fetched content already too).
º Base styles structure as I had already.
º Fonts (from my "Portfolio 2021" (in Jekyll) or from my "Portfolio V3 2022 NextJS").
----------------------------------

---
## [MaxMood96/platform_bionic](https://github.com/MaxMood96/platform_bionic)@[1f462dec34...](https://github.com/MaxMood96/platform_bionic/commit/1f462dec34a5358c3e63d6a8e986a82248338aed)
#### Friday 2022-08-12 05:13:21 by Elliott Hughes

Add %b and %B support to the scanf/wscanf and strto*/wcsto* families.

Coming to C23 via WG14 N2630.

This one is a little interesting, because it actually changes existing
behavior. Previously "0b101" would be parsed as "0", "b", "101" by these
functions. I'm led to believe that glibc plans to actually have separate
versions of these functions for C23 and pre-C23, so callers can have the
behavior they (implicitly) specify by virtue of which -std= they compile
with. Android has never really done anything like that, and I'm pretty
sure app developers have more than enough to worry about with API levels
without having to deal with the cartesian product of API level and C
standard.

Therefore, my plan A is "if you're running on Android >= U, you get C23
behavior". My plan B in the (I think unlikely) event that that actually
causes trouble for anyone is "if you're _targeting_ Android >= U, you
get C23 behavior". I don't think we'd actually want to have two versions
of each of these functions under any circumstances --- that seems by far
the most confusing option.

Test: treehugger
Change-Id: I0bbb30315d3fabd306905ad1484361f5d8745935

---
## [jasonm23/melpa](https://github.com/jasonm23/melpa)@[570bde6b4b...](https://github.com/jasonm23/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Friday 2022-08-12 05:43:23 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[dd76836f98...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/dd76836f9851e61571d759eed25480134b91df96)
#### Friday 2022-08-12 06:18:12 by ODRI-the-human

yoooo

3d guy. the textures are fucked but i can't work out how to fix it and i'm going insane. also knockback is inexplicably fucked on two enemies so yeah i'm gonna become the joker

---
## [argrath/NetHack](https://github.com/argrath/NetHack)@[8a549b0a60...](https://github.com/argrath/NetHack/commit/8a549b0a602fdb13d13fa83bb2f6b1d1a1a257cf)
#### Friday 2022-08-12 06:21:43 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

---
## [BSCPGROUPHOLDINGSLLC/RELATIVES](https://github.com/BSCPGROUPHOLDINGSLLC/RELATIVES)@[0d9991a9d0...](https://github.com/BSCPGROUPHOLDINGSLLC/RELATIVES/commit/0d9991a9d0db8982ec230405adbe545301a75f0b)
#### Friday 2022-08-12 06:31:23 by 1212-5858

$$$$$ FOR INSPECTION BY THE RESPECTIVE FACTIONS

PART I.
Discuss “Digital Responsibility” and ethics.  

PART II.
Explain the standards for workplace engagement online, preventative measures for hacking, and codes of conduct.  

PART III.

What further rules should be in place?

Solomon, David M. “Corporate Governance.” Code of Business Conduct and Ethics, Goldman Sachs, https://www.goldmansachs.com/investor-relations/corporate-governance/. 


To cultivate a diverse workforce, we must draw on the largest possible pool of potential team members. We seek to attract
and retain a diverse network of people from across the globe who bring with them a wide range of backgrounds, cultures,
perspectives and experiences. 


As noted throughout, it’s the responsibility of every individual at the firm to escalate potential legal, regulatory, and ethical
breaches, including violations of this Code as well as our core values and our Business Principles. This includes any
instances of retaliation. The firm strictly prohibits retaliation against anyone who in good faith reports a possible
violation, no matter who the report involves.
Paperwork Reduction Act of 1995''

 To further the goals of the Paperwork Reduction Act to have Federal 
 agencies become more responsible and publicly accountable for reducing 
      the burden of Federal paperwork on the public, and for other 
              purposes. <<NOTE: May 22, 1995 -  [S. 244]>> 

    Be it enacted by the Senate and House of Representatives of the 
United States of America in Congress <<NOTE: Paperwork Reduction Act of 
1995. Information resources management.>> assembled,

SECTION 1. <<NOTE: 44 USC 101 note.>> SHORT TITLE.

    This Act may be cited as the ``Paperwork Reduction Act of 1995''.

SEC. 2. COORDINATION OF FEDERAL INFORMATION POLICY.

    Chapter 35 of title 44, United States Code, is amended to read as 
follows:

        ``CHAPTER 35--COORDINATION OF FEDERAL INFORMATION POLICY

``Sec.
``3501. Purposes.
``3502. Definitions.
``3503. Office of Information and Regulatory Affairs.
``3504. Authority and functions of Director.
``3505. Assignment of tasks and deadlines.
``3506. Federal agency responsibilities.
``3507. Public information collection activities; submission to 
           Director; approval and delegation.
``3508. Determination of necessity for information; hearing.
``3509. Designation of central collection agency.
``3510. Cooperation of agencies in making information available.
``3511. Establishment and operation of Government Information Locator 
           Service.
``3512. Public protection.
``3513. Director review of agency activities; reporting; agency 
           response.
``3514. Responsiveness to Congress.
``3515. Administrative powers.
``3516. Rules and regulations.
``3517. Consultation with other agencies and the public.
``3518. Effect on existing laws and regulations.
``3519. Access to information.
``3520. Authorization of appropriations.

``Sec. 3501. Purposes

    ``The purposes of this chapter are to--
            ``(1) minimize the paperwork burden for individuals, small 
        businesses, educational and nonprofit institutions, Federal 
        contractors, State, local and tribal governments, and other 
        persons resulting from the collection of information by or for 
        the Federal Government;
            ``(2) ensure the greatest possible public benefit from and 
        maximize the utility of information created, collected, main

[[Page 109 STAT. 164]]

        tained, used, shared and disseminated by or for the Federal 
        Government;
            ``(3) coordinate, integrate, and to the extent practicable 
        and appropriate, make uniform Federal information resources 
        management policies and practices as a means to improve the 
        productivity, efficiency, and effectiveness of Government 
        programs, including the reduction of information collection 
        burdens on the public and the improvement of service delivery to 
        the public;
            ``(4) improve the quality and use of Federal information to 
        strengthen decisionmaking, accountability, and openness in 
        Government and society;
            ``(5) minimize the cost to the Federal Government of the 
        creation, collection, maintenance, use, dissemination, and 
        disposition of information;
            ``(6) strengthen the partnership between the Federal 
        Government and State, local, and tribal governments by 
        minimizing the burden and maximizing the utility of information 
        created, collected, maintained, used, disseminated, and retained 
        by or for the Federal Government;
            ``(7) provide for the dissemination of public information on 
        a timely basis, on equitable terms, and in a manner that 
        promotes the utility of the information to the public and makes 
        effective use of information technology;
            ``(8) ensure that the creation, collection, maintenance, 
        use, dissemination, and disposition of information by or for the 
        Federal Government is consistent with applicable laws, including 
        laws relating to--
                    ``(A) privacy and confidentiality, including section 
                552a of title 5;
                    ``(B) security of information, including the 
                Computer Security Act of 1987 (Public Law 100-235); and
                    ``(C) access to information, including section 552 
                of title 5;
            ``(9) ensure the integrity, quality, and utility of the 
        Federal statistical system;
            ``(10) ensure that information technology is acquired, used, 
        and managed to improve performance of agency missions, including 
        the reduction of information collection burdens on the public; 
        and
            ``(11) improve the responsibility and accountability of the 
        Office of Management and Budget and all other Federal agencies 
        to Congress and to the public for implementing the information 
        collection review process, information resources management, and 
        related policies and guidelines established under this chapter.
		
		
		Sergey Aleynikov, a 40-year-old former Goldman Sachs programmer, was found guilty on Friday by a federal jury in Manhattan of stealing proprietary source code from the bank’s high-frequency trading platform. 
		He was convicted on two counts theft of trade secrets and transportation of stolen property and faces up to 10 years in prison.
	

During the two-week trial, Judge Denise L. Cote closed the courtroom to the public several times to protect Goldman’s proprietary source code. Yet several details emerged about the firm’s high-frequency trading business, including that the unit accounted for about $300 million in revenue last year, less than 1 percent of Goldman’s total revenue of $45 billion.

On the evening of July 3, 2009, six agents from the Federal Bureau of Investigation met Mr. Aleynikov as he landed at Newark International airport and arrested him.

Mr. Aleynikov remains free on bail but because he holds dual United States and Russian citizenship, the judge placed him under home confinement and electronic monitoring until his sentencing, which is set for March 18.

A version of this article appears in print on Dec. 11, 2010, Section B, Page 1 of the New York edition with the headline: Wall St. Programmer Guilty of Code Theft.

 United States Attorney Southern District of New York 
 
 Manhattan U.S. Attorney PREET BHARARA said: "Protecting the proprietary information of America’s companies is critically important. Today’s sentence sends a clear message that professionals like Sergey Aleynikov who abuse their positions of trust to steal confidential business information from their employers will be prosecuted and punished."

Under USC 18.225.each person:

'...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main
https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed
https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker


FOR INVASION OF PRIVACY AS WELL WAS UNCONSENTED AS ANNEXED "CEASE AND DESIST" NYSCEF 153974/2020

THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER THE AUSPICE OF THE OCC.TREAS.GOV AS OF JUNE 29TH, 2022



AUGUST 8TH, 2022

To whom this may concern,

    THE INFORMATION CONTAINED HEREIN IS CLEARLY THE OBJECCT OF ATTRACTION BY AND BETWEEN SEVERAL DEPARTMENT OF THE USDOJ WHO ARE IN FACT INVESTIGATING THE INDIVIDUALS AND PRINCIPLES OF THOSE ENTITIES WHO ARE RESPONSIBLE FOR A LAUNDRY LIST AS ENTITIES AND PERSONS WHO LED THEMSELVES INTO A COMBINE OF VIOLATIONS UNDER THE USC CODE, TAX CODE, AND HAVE ALSO ANNEXED AND FILED THEIR VIOLATION UNDER THE SECURITIES AND EXCHANGE ACT.


THE ZUCKERS AND THEIR ENTERPRISES, have avoided prosecution ,in fact prior to August 4th, 2022.
 - but thank you for checking in, DOCKET 309, nyscef 153974/2020, and in a high-fashion.

STATE FARM LIFE INSURANCE COMPANY

UNDER THE SCOPE OF THE PLAINTIFF, LITERALLY.
- subjugated AND AT THE COMPROMISE OF CIK FILER 93715, WHEREBY DIRECTORS FILED THEIR USC TITLE 18.215 PAYMENTS VOTED ON, KNOWN AND RECEIVED AS DIRECTORS OF CRD MEMBER 43036, AND ALSO " STATE FARM LIFE INSURANCE COMPANY " AND UNDER TICKERS OF FAMILY 4: STFGX.



https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

^ THAT REFERENCE.     IS THE REFERENCE OF GREATEST VALUE, COVERS THE SCOPE OF CONVERSATIONS
- USC TITLE 18.1952 VIOLATIONS, AND IN BOLD ***** BELOW, ET. AL.
 
*****

[ USC Title 18.225, USC Title 18.215, USC Title 18.21, USC Title 18.2 ]

Each person as Participants in NYSCEF matter 153974/2020
   

    '...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker
   

*****


THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER 
	
		THE AUSPICE OF THE *@OCC.TREAS.GOV AS OF JUNE 29TH, 2022
		
 *** see also. Random $9000 audit by PWC for filer 93715, 
				to file their KNOWN problems then by CIK filer 93715 and into CIK filer 1516523.'
				## STILL HOLDS THOSE PAPERS.. CAN'T TERMINATE UNTIL THE TAXES ARE " PAID IN FULL "
				## ALL SIX-PROPERTIES, AND A LETTER FROM ANY FEDERAL REGULATOR WOULD BE WHAT IS A "CALL" 
				## FROM THE ISSUER OF ALL THAT MONEY IN ONE PAGE, AND IMPOSES THE SAME LEVERAGE STAKES AT ANY CUSTODIAN.
    
 /S/ BO DINCER.	).
 
	MAC. 646-256-3609
	TMO. 917-378-3467

📫 https://github.com/BSCPGROUPHOLDINGSLLC/2021-DUCKER-ZUCKER/pull/1


CIK FILER 93715 ITNO CIK FILER 1516523
# MAKESMALLBIGGER
^ 1 REFERENCE <br>
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf


$$$$$ leb@fbi.gov

https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

UNDER THE SCOPE OF THE PLAINTIFF, LITERALLY.
- subjugated the decision(s) of STATE FARM LIFE INSURANCE BY IMPEDING A TIMELY RELEASE OF INFORMATION FILED IN NYSCEF 153974/2020
- AND AT THE COMPROMISE OF CIK FILER 93715.
^ WHEREBY DIRECTORS FILED THEIR USC TITLE 18.215 PAYMENTS VOTED ON, KNOWN AND RECEIVED AS DIRECTORS OF CRD MEMBER 43036, 
^ AND ALSO " STATE FARM LIFE INSURANCE COMPANY " AND UNDER TICKERS OF FAMILY 4: STFGX LOST THE GREATER OF 10% IN A SINGLE TRADING SESSION.




https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

^ THAT REFERENCE.     IS THE REFERENCE OF GREATEST VALUE, COVERS THE SCOPE OF CONVERSATIONS
- USC TITLE 18.1952 VIOLATIONS, AND IN BOLD ***** BELOW, ET. AL.
 
*****

[ USC Title 18.225, USC Title 18.215, USC Title 18.21, USC Title 18.2 ]

Each person as Participants in NYSCEF matter 153974/2020
   

    '...imprisoned for a term of not less than 10 years and which may be life."

# FEDERAL FILE FINDERS
^	UNDER THE PAPERWORK REDUCTION ACT OF 1995

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/find/MSGFILES

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/find/VIDEOTAPED-DISTRIBUTED

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/main

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/2020-11-20-FILER0000093715

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/REQUEST-TO-BAR

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/Assessments


### $9000.00 AUDIT WAS A "SURPRISE DISCOUNT" BY CHANCE PROVES THAT ' PWC ' KNEW ' SOMETHING WAS GOING ON '

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker
   

*****


THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER 
	
		THE AUSPICE OF THE *@OCC.TREAS.GOV AS OF JUNE 29TH, 2022
		
 *** see also. Random $9000 audit by PWC for filer 93715, 
				to file their KNOWN problems then by CIK filer 93715 and into CIK filer 1516523.'
				## STILL HOLDS THOSE PAPERS.. CAN'T TERMINATE UNTIL THE TAXES ARE " PAID IN FULL "
				## ALL SIX-PROPERTIES, AND A LETTER FROM ANY FEDERAL REGULATOR WOULD BE WHAT IS A "CALL" 
				## FROM THE ISSUER OF ALL THAT MONEY IN ONE PAGE, AND IMPOSES THE SAME LEVERAGE STAKES AT ANY CUSTODIAN.
    
 /S/ BO DINCER.	).
 
	MAC. 646-256-3609
	TMO. 917-378-3467
The Financial Information eXchange (FIX) is an information and data protocol 
mailbox BSCPGROUPHOLDINGSLLC/2021-DUCKER-ZUCKER#1


CIK FILER 93715 ITNO CIK FILER 1516523
# MAKESMALLBIGGER
^ 1 REFERENCE <br>
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf


i am unfamiliar with any internet based spy tools, other than mobi-stealth, which was helpful in the past. other than that one, i don’t know about any other spy tools other than what is used by the federal government.

 In fact, SPAM only contains six ingredients! And the brand's website lists them all. They are: pork with ham meat added (that counts as one), salt, water, potato starch, sugar, and sodium nitrite.

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[851a158844...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/851a15884469627393f2eef7bf5f46746d81875a)
#### Friday 2022-08-12 06:33:54 by ODRI-the-human

stupid

ok im dumb and figured out the reason knockback was fucked 1 minute after comitting the last one (i'd been stuck on it for an hour or so last night). still no textures on the guy, but at least he has no materials because unity is designed to be as unintuitive as possible/i'm stupid.

---
## [faye-yap/FightingGameStuff](https://github.com/faye-yap/FightingGameStuff)@[1f3f69ef5e...](https://github.com/faye-yap/FightingGameStuff/commit/1f3f69ef5e95a5d783b18bf8328cd48a60c5aff7)
#### Friday 2022-08-12 06:57:00 by invertedplant

Knight updates

patch notes:
Knight:
2B taking 14 frames to come out and having 20 frames lagtime seems excessive for something that has very little motion... consider cutting it in half (current frame data fairly similar to 2s)
forward s: animate projectile to "start" on its active frame (9) or frame 0 (currently: frame 0)? projectile collider should be default ENABLED, right? when redoing the projectile data, noticed by default collider was DISABLED
jB: way too few active frames for such a large slash?
5A: also feels kinda laggy, potential to be faster
5S: different frame data from suggested, comes out on frame 16 instead, lingers for a while (dynamic hitbox sizing), still has 25 frames of recovery after move ends
3B: maybe it should have a longer recovery time to match the GDD description of "strong move, invincible while leaping, long recovery"

- check "transitions" for down-forward B, crouching B, jA, neutral A/B.
- crouch move startups look clunky on the knight
- don't we need "jumping" and/or "gotgrabbed" animations / states? there is a jumping sprite but it doesn't look used

---
## [BSCPGROUPHOLDINGSLLC/RELATIVES](https://github.com/BSCPGROUPHOLDINGSLLC/RELATIVES)@[c1d53b7c1f...](https://github.com/BSCPGROUPHOLDINGSLLC/RELATIVES/commit/c1d53b7c1f62e7195f95994729d14aeff6ae5843)
#### Friday 2022-08-12 07:44:11 by 1212-5858

$$$$$$ Nexus of Zuckers


> https://s3.amazonaws.com/handshake.production/attachments/documents/000/832/183/original/2021_PBS_PP_VES_Marketing_Flyer_vGeneral_Handshake.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2HSNSGACXF6KKT2H%2F20220712%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220712T193929Z&X-Amz-Expires=10&X-Amz-SignedHeaders=host&X-Amz-Signature=3e2d9fe10da3e1ee8396cefab33824544bad2983a5c3a8d08d012c2fdef9e42b 

<https://s3.amazonaws.com/handshake.production/attachments/documents/000/832/183/original/2021_PBS_PP_VES_Marketing_Flyer_vGeneral_Handshake.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2HSNSGACXF6KKT2H%2F20220712%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220712T193929Z&X-Amz-Expires=10&X-Amz-SignedHeaders=host&X-Amz-Signature=3e2d9fe10da3e1ee8396cefab33824544bad2983a5c3a8d08d012c2fdef9e42b>

2020.06.22 REQUEST TO APPEAR BY PLAINTIFF - 
AT-WILL AS-NEEDED PROCEEDINGS ARE A VIOLATION OF MY CIVIL RIGHTS, 
THE CONSITITUTION AND RIGHTS TO A FAIR TRIAL 
WHICH WAS GROSSLY OBSTRUCTED AND KNOWN BY ALL COUNSELORS SGO2107@COLUMBIA.EDU, ET. AL

LEAD TO THE DEMISE OF CIK FILER 93715, DAMAGES NOT COVERED AS FILED WITH SECURITIES & EXCHANGE COMMISSION
- INFORMATION THAT WAS IMPEDED, OBSTRUCTED, AND GROSSLY CONTINUES TO BE RELEASED TO LAW ENFORCEMENT
- HENCE, I PARTNERED WITH MY BUDDIES FROM 2012 AGAIN - AM KNOWN, WILFULLY.
- HENCE, I AM NOT AFRAID OF THE ZUCKERS, OR THEIR COUNSELORS (ABSENT OF BEING OBSTRUCTED ANY FURTHER)
*** THANK YOU.

<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=qhjjPjzuwUgwWnZcfiIluA==>

ALL UNDER TITLE 18

TITLE 18, § 1962 - Prohibited activities
	(a) It shall be unlawful for any person who has received any income derived, directly or indirectly, from a pattern of racketeering activity or through collection of an unlawful debt in which such person has participated as a principal within the meaning of section 2, title 18, United States Code, to use or invest, directly or indirectly, any part of such income, or the proceeds of such income, in acquisition of any interest in, or the establishment or operation of, any enterprise which is engaged in, or the activities of which affect, interstate or foreign commerce. A purchase of securities on the open market for purposes of investment, and without the intention of controlling or participating in the control of the issuer, or of assisting another to do so, shall not be unlawful under this subsection if the securities of the issuer held by the purchaser, the members of his immediate family, and his or their accomplices in any pattern or racketeering activity or the collection of an unlawful debt after such purchase do not amount in the aggregate to one percent of the outstanding securities of any one class, and do not confer, either in law or in fact, the power to elect one or more directors of the issuer.
	(b) It shall be unlawful for any person through a pattern of racketeering activity or through collection of an unlawful debt to acquire or maintain, directly or indirectly, any interest in or control of any enterprise which is engaged in, or the activities of which affect, interstate or foreign commerce.
	(c) It shall be unlawful for any person employed by or associated with any enterprise engaged in, or the activities of which affect, interstate or foreign commerce, to conduct or participate, directly or indirectly, in the conduct of such enterprise's affairs through a pattern of racketeering activity or collection of unlawful debt.
	(d) It shall be unlawful for any person to conspire to violate any of the provisions of subsection (a), (b), or (c) of this section.

TITLE 18, § 1963
	(a) Whoever violates any provision of section 1962 of this chapter shall be fined under this title or imprisoned not more than 20 years (or for life if the violation is based on a racketeering activity for which the maximum penalty includes life imprisonment), or both, and shall forfeit to the United States, irrespective of any provision of State law- (1) any interest the person has acquired or maintained in violation of section 1962; (2) any- (A) interest in; (B) security of; (C) claim against; or (D) property or contractual right of any kind affording a source of influence over; any enterprise which the person has established, operated, controlled, conducted, or participated in the conduct of, in violation of section 1962; and (3) any property constituting, or derived from, any proceeds which the person obtained, directly or indirectly, from racketeering activity or unlawful debt collection in violation of section 1962. The court, in imposing sentence on such person shall order, in addition to any other sentence imposed pursuant to this section, that the person forfeit to the United States all property described in this subsection. In lieu of a fine otherwise authorized by this section, a defendant who derives profits or other proceeds from an offense may be fined not more than twice the gross profits or other proceeds. (b) Property subject to criminal forfeiture under this section includes- (1) real property, including things growing on, affixed to, and found in land; and (2) tangible and intangible personal property, including rights, privileges, interests, claims, and securities.

ALL UNDER TITLE 18
	§ 2 - Principals
		(a) Whoever commits an offense against the United States or aids, abets, counsels, commands, induces or procures its commission, is punishable as a principal.
		(b) Whoever willfully causes an act to be done which if directly performed by him or another would be an offense against the United States, is punishable as a principal.
	§ 3 - Accessory after the fact
		Whoever, knowing that an offense against the United States has been committed, receives, relieves, comforts or assists the offender in order to hinder or prevent his apprehension, trial or punishment, is an accessory after the fact. Except as otherwise expressly provided by any Act of Congress, an accessory after the fact shall be imprisoned not more than one-half the maximum term of imprisonment or (notwithstanding section 3571) fined not more than one-half the maximum fine prescribed for the punishment of the principal, or both; or if the principal is punishable by life imprisonment or death, the accessory shall be imprisoned not more than 15 years.
	§4. Misprision of felony
		Whoever, having knowledge of the actual commission of a felony cognizable by a court of the United States, conceals and does not as soon as possible make known the same to some judge or other person in civil or military authority under the United States, shall be fined under this title or imprisoned not more than three years, or both.	
	§6. Department and agency defined
		As used in this title:
		-The term "department" means one of the executive departments enumerated in section 1 of Title 5, unless the context shows that such term was intended to describe the executive, legislative, or judicial branches of the government.
		-The term "agency" includes any department, independent establishment, commission, administration, authority, board or bureau of the United States or any corporation in which the United States has a proprietary interest, unless the context shows that such term was intended to be used in a more limited sense.

---
## [FranzBusch/swift-protobuf](https://github.com/FranzBusch/swift-protobuf)@[a6b087bde3...](https://github.com/FranzBusch/swift-protobuf/commit/a6b087bde33f8196b44b19eec7f9333e25837148)
#### Friday 2022-08-12 09:29:19 by FranzBusch

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ad0879c1e0...](https://github.com/mrakgr/The-Spiral-Language/commit/ad0879c1e067d624f38358ca796a227a6b98b69c)
#### Friday 2022-08-12 10:14:05 by Marko Grdinić

"9:35am. Let me do my slacking and I will do some writing.

10am. There was a big dump of Magical Trans on Dex today. Also, I saw a thread about Stable Diffusion on /g/.

https://stability.ai/blog/stable-diffusion-announcement

> Stability AI and our collaborators are proud to announce the first stage of release of Stable Diffusion to researchers via this form, the model weights are hosted by our friends at Hugging Face once you get access. The code is available here and the model card here. We are working together towards a public release soon.

> Stable Diffusion runs on under 10 GB of VRAM on consumer GPUs, generating images at 512x512 pixels in a few seconds.

I actually need more than this. 1k images at least. If I can't run it on my own rig, that will finally be an excuse to try out the cloud.

> The model was trained on our 4,000 A100 Ezra-1 AI ultracluster over the last month as the first of a series of models exploring this and other approaches.

Yikes.

The images look quite good. It is as I said, for a popular task like image generation, OpenAI has zero moat. They should have actually been open instead of messing with content moderation.

It is ironic, if they could have had a monopoly in this, they'd have made a ton of money, but because of all the competition they'll make nada. All their content moderation will do is annoy people.

10:20am. Right now I am doing some research into Pathfinder Archery builds. Let me just deal with that guilty pleasure and I will start writing. Oh right. Any mail?

> Paperspace Launches Free Tier IPU Cloud

I got this in the promotions tab. I might want to check this out.

10:40am. https://www.reddit.com/r/Pathfinder_Kingmaker/comments/o8wtg8/good_archer_builds_that_dont_have_pets/
> Magus(Eldritch Archer) 2/Rogue(Scoundrel) 8/Eldritch Knight 10

Forget this. I am going crazy to spend so much effort studying this as if it actually matters.

Let me see if I can get some writing done.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and feel that in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

(Heaven's Key, Perimeter of a floating city)

I dive into the game again, and take in the sights of the city of gold. Taking only a passing glance at the railing, I turn around and go into the city proper. As fun as that experience was, I do not want to spend my entire day diving off the edge. Gawking like a tourist as a I stroll around, I get a stock of the place. Near the frontier where I was the density of buildings was low, so amongst the houses as if to spur business a lively entertainment sector was built. I could see circus tents, restaurants, stages as well as casinos. There seemed to be a lot of people enoying themselves, though I wouldn't say it was packed. I found the city plan somewhat peculiar. There were roads for example, but no cars, and I could only see people using their own legs as far as I looked. The regular houses made sense, but other entertainment related facilities seemed to be build in the middle of roads and at intersections. Overall, it felt like the city itself was molded based off some template, and then patched up to fit a need by the people actually living here.

By the looks of it

$$$

Damn, what is that word for the edge of a territory. I saw it used in the Kingmaker game, but it slipped from my memory.

11am. Oh I have a good idea. Right now it just occured to me to wonder why Euclid would not just get scammed out of his entire stack on the very first transaction.

Let me change the rules. A transation that would kill the user would be rejected by the system.

11:10am. Also idea comes to me just now. In the initial scene there should be (fake) job advertizements around the place, paying exorbiant monthly sums. This is to further the impression of the life chips being cheap. Plentiful jobs everywhere that pay 3k and more a month for doing things like waitering, restaurants that have items costing in the 10-100 chip range. Rides and venues whose entry is also in the two digit range.

Those job boards are really important, it would take a huge sceptic to assume they are all fake initially.

11:10am. I was going to go for cash games in the casinos initially, but I'll make the most popular format SNG tourneys. Having something like 1/2 blinds would be too expensive for the initial small stacks, and cash games encourage nitty play, especially in the situation where one's life is on the line like in Heaven's Key. I think Pokerstars HU tables got banned due to the pros only wanting to play fish. Fundamentally it is the venue's responsibility to encourage action.

11:20am. When the user is too low on chips to pay full entry fee, he can still enter, but the stack will be correspondingly shorter.

11:20am. A solo artist can scam a person, but to get a properly stable and large scam, you need a group effort. Group efforts can really make a story believable and take it to the next level.

Ah, crap. I forgot the watermelon again.

Let me have a short break here.

11:55am. Done with the short break. Mhhhh, I might as well have proper breakfast.

I am still thinking about it. Initially, the scene that drove me was Euclid getting cleaned out by a cute female guide, but given the background information that I've established yesterday, her role should not be to scam him directly, but to induce him to spend. I wanted it to be a scene of betrayal, but given the kind of group effort this con should be, my thinking does not make sense.

I have to think about the motivation of the people there. I generally don't think about that in regular life, since it would make no difference either to what I have to do.

But I've gotten burned due to this in the programming interviews.

Like for example, I was really surprised that the HR drones are actually gauging interest. From my own perpective, most of the place I'd apply to would chuck my resume, so there is zero reason to show interest in a company before I get an offer as it would be a waste of time. The Neurolabs guy did try a trick to see whether I can remember the stuff on my resume.

Basically all these mental games that they play are insightful. On a personal level, they might not have anything to do with gauing a candidate's job performance, but at a wide scale, they do act as a selection mechanism. I mean they did weed me out by making me realize I do not want a job. My attitude was pretty bad, I wouldn't want to hire myself either, but that is mostly because I am confused at what I should be focusing on.

For HR recruiters it never occured to me to wonder how they themselves are measured. Are they really gauged based on the hires' job performance? I find that difficult to believe. To get a job, I am simply lacking too much, if Heaven's Key and Hatred do not give me any benefits I'll have to give up on writing and will have to tackle the job market again. I'll have to get an insight on what the recruiters are looking for, what the companies are looking for, and get over my nervousness. If I can adjust both my understanding and attitude, getting jobs in the 100-200k range would not be too hard.

Life is long and all that, forget this for now.

12:10pm. You know what, let me skip the morning session. I somehow wasted most of it already. I'll have breakfast and check out that Graphcore free cloud offering. I just want to see whether those IPUs could be programmed directly. That would have some value to me.

It is really difficult for me to try to stitch a scene I had in mind together so I need to rethink it. Rather than forcing the issue, it would be best to just adjust the foundations of the story and let it flow naturally from there.

I do not really need a plot point where he gets scammed by a particular person. I can swap them for the many friendly and smilling faces that are part of a group."

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[e12f2a3433...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/e12f2a34332e1d737f11d0e946db03de27c52439)
#### Friday 2022-08-12 13:30:49 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [ambasada-ludozerska/Rebirth-Of-The-Night](https://github.com/ambasada-ludozerska/Rebirth-Of-The-Night)@[52caa606ac...](https://github.com/ambasada-ludozerska/Rebirth-Of-The-Night/commit/52caa606ac67d67e1f6ebda880e612e7c0d20d00)
#### Friday 2022-08-12 15:43:43 by Foreck1

Bunch o'stuff

Added Tapestry blocks: red, green, cyan, and purple. One-way craft with wool.
Swapped Zanite with Gravitite
Gravitite is now mostly equivalent to silver in stats
Gravitite ore is now sturdy level
Zanite is now part of the gem tier in stats
Zanite ore is now refined level
Zanite now has an ingot form for all equipment
Zanite now counts towards gem advancements
Nerfed Ptera health to half
Tweaked rain droplets on screen effect
Doubled resolution of water drop and fire particles
Added new painting to go along cyan tapestry
Textures tweaked/added for diamond ingot, exorite ingot, ruby ingot, sapphire ingot, zanite ingot
Fixed missing texture particles for giant clovers
Moved Bloodied demon eye recipe from crafting table to runic table to make it more obvious
Nerfed extra drops from clay in rivers to be twice as rare

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5070d98856...](https://github.com/mrakgr/The-Spiral-Language/commit/5070d98856d74e1d741907ee75bfe0904cda6d70)
#### Friday 2022-08-12 16:03:25 by Marko Grdinić

"12:25pm. https://github.com/graphcore/tutorials/tree/master/tutorials/poplar

Hmmm...

https://www.graphcore.ai/ipus-in-the-cloud

Also, it seems that Graphcore has plenty of cloud providers.

https://github.com/graphcore/tutorials/tree/master/tutorials/poplar/tut1_variables

> Before starting this tutorial, take time to familiarise yourself with the IPU's architecture by reading the IPU Programmer's Guide. You can learn more about the Poplar programming model in the corresponding section of our documentation: Poplar and PopLibs User Guide: Poplar programming model.

12:35pm. https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/

This is a step forward. I had no idea Graphcore had a programming guide.

https://github.com/graphcore/examples/tree/master/reinforcement_learning/rl_policy_model/tensorflow1

There is even some RL stuff. This is from 3 weeks ago.

1pm. Done with brekafast.

https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/programming_tools.html

Programming this sure seems like a pain in the ass.

https://github.com/graphcore/examples/tree/master/reinforcement_learning/rl_policy_model/tensorflow1

Let me check out the stuff here and then I am done. No way do I feel like messing with this. I have better things to do that chuck another 6 months of my life to researching something. I really hate this world for not giving me a proper path.

1:05pm. My will to program right now is the weakest it has ever been. I didn't think the AI revolution would be like this. Simple models trained on huge machines, and no place for me to come in.

Take DALLE. Something like DALLE I would have liked to do myself, but just how possibly could I have? Take the quote from before...

> The model was trained on our 4,000 A100 Ezra-1 AI ultracluster over the last month as the first of a series of models exploring this and other approaches.

Yeah, sure, I could have done it if I had an ultracluster, but where would I get one? And even if I was rich, just who is going to toss endless amounts of money at something that has no return.

1:10pm. I do not get it. I failed at trading and at AI. In both cases my trading and my programming skills are completely useless to me. Will I just die without ever making use of the skills I've painstakingly cultivated? Just what is the point of this game, to watch somebody else cause the Singularity?

My effort was unrewarded, and my desire unsatisfied.

Outside it, I can only look at the field of ML with resentment as it move on without me.

1:15pm. In such a state no wonder Heaven's Key changed. From the first time for the bottom of my heart I wished that the Lord of Nightmares existed so that I might get a chance to fulfil my purpose.

What is the point of the self improvement loop being the purpose of life, if you can't enter it? Everything is chaotic in this world and my vision is shrouded in darkness.

1:25pm. I guess this kind of mindset explains why religions get made. My mindset is kind of unique since not many people earnestly pursue the Singularity. Having realized my limits and approaching doom, of course I'd earnestly wish for a God that would allow me to grasp the Singularity without the rush of the arms race that I can't ever win.

1:30pm. It might sound like whining, but this is the dominant emotion coursing through me.

I do not have infinite willpower like the Inspired do. If you locked me up in solitary confinement I'd break at some point, while the Inspired would be able to easily withstand the passage of any amount of time. I need something to sweeten the pot. Just having the hardware is not enough.

1:35pm. Let me step away from the screen. It is inevitable that the story will be intervowen with my own feelings and thoughts about the future.

I'll take a nap and think about the scene a bit more. I thought of another lie.

I'll have the guide lie that the amount of people coming into the city is a lot rarer than it actually is to further drop Euclid's guard. Also I am not going to put in transaction restrictions, that was just a brain fart. I forgot that the life chips are physical things that can be manifested and handed over. It is not some status window that shows up.

1:40pm. Yeah, compared to last year I've changed, but I didn't notice how until now. I now no longer care about either the Singularity or the self improvement loop because they are not something that is under my control. What I care about is the Lord of Nightmares, and his justice.

The 2014 arcs were definitely about the self improvement loop. The 2022 ones aren't. They will be dedicated to the God that does not exist yet.

1:45pm. https://youtu.be/k_jR7DfN67c
Fundamentals of the IPU and Poplar®

This was out there for almost 2 years now, but I missed it. How could that happen? I must have been blind.

https://youtu.be/k_jR7DfN67c?t=343

Make no mistake, this is hard to use. Making custom graphs in C++? Pure spew.

I could probably make great gains for these chips using Spiral. But so what? What gain would that get me?

https://youtu.be/VYqR57ApTUU
Evaluating Batch Sizes for IPUs

Let me watch this for just a bit.

1:55pm. No forget this. Forget Graphcore unless some algorithm comes out to entice me back to RL. I want hardware that has some proper message passing between chips. I need flexibility. Just what are these shitty toy kernels? Who cares about DL.

5:05pm. I took a bath and was in bed this whole time thinking.

My will to become a writer is not entirely solid. I am still wandering between different choices unsure of which path to take, searching for a sign. But I did get a sign in the last 9 months. Regardless of my intention, I was studying art, and then DALLE came out and obliviated that. I honestly didn't care too much about that, but...

Imagine if I was a pro concept artist. That would have made me scared about my future.

It will be like that. Art is going to get progressively taken over by AI, and while now I can only write, in the future I will be able to be my own studio.

Just writing is low tech now, but in the future it will be at the forefront of everything.

Right now, I am just too negative to see reality properly. It feels like I keep getting rejected left and right, but those are just my personal feelings.

I might be feeling negative that I am not participating in the wave directly, but what is wrong about simply taking advantage of existing technology. Wasn't that in a way my whole plan all along, to find something good and make use of it?

Imagine if I could right now write and have NN agents illustrate, create music and animate the work. Would I be wondering whether I should be getting crap-tier programming work just for money?

I would be retarded if I did. And yet that is the future.

Right now it takes 4,000 A100 GPUs, but in the future I should get the capability to train it myself. Baby steps.

Let me watch a video on stable diffusion. I played games all my life, but never bemoaned my ability to make them. AI should go the same way. It will be my role to use what exists.

https://youtu.be/dWYsRVy-hFM
STABLE DIFFUSION vs DALLE 2? (I Entered my DALLE2 Prompts in Stable Diffusion) - Comparison Part 1.

https://youtu.be/dWYsRVy-hFM?t=46

Disgustingly good. How many weeks would it take me to do something like this in Blender?

https://youtu.be/dWYsRVy-hFM?t=165

These dragons are crazy good. There is no point in drawing by hand anymore, the only real question is how to get more precise control over these systems.

I'll definitely be able to use this, since they said that machines with 10gb VRAM would work. I mean, my own PC does not have enough, but I'll make good use of the cloud in that case until I can upgrade my rig.

I wasn't wrong to take cloud seriously. I should be able to rent a card with 16-40gb without a problem. But most likely there will be a site where I will be able to use it for cheap.

https://youtu.be/dWYsRVy-hFM?t=175

These chara portraits are good. Hell, they are better than the Kingmaker ones.

https://youtu.be/dWYsRVy-hFM?t=179

Ok, this one not so much. The eyes are non-symmetric.

https://youtu.be/dWYsRVy-hFM?t=211

The face could use some work, but otherwise these are excellent.

https://youtu.be/dWYsRVy-hFM?t=218

The charas are eldrich abominations, but this would be useful for backgrounds.

https://youtu.be/dWYsRVy-hFM?t=244

Wicked. This is a great dark fantasy illustration.

5:25pm. https://youtu.be/EqTLkt-Ycwo
Stable Diffusion: Launch Presentation of Beta + Tutorial for Stable Diffusion + Current Results

The reason to be excited about Stable Diffusion is because most likely, I'll be able to get access to this before I get past the DALLE waiting list. And it will be free to boot instead of requiring me 0.1-0.2$ per image.

https://youtu.be/EqTLkt-Ycwo?t=367
> The code will be released as MIT, the weights will be released as Apache license

Ok, forget this for now. I had enough of it for one day. Let me rest here. I've already started reading Magical Trans.

I am going to build up my will. I can't really fail at writing. What would be failing in it mean, anyway? Less than 1,000/month? Less than 100/month? Anything is fine for me. I've already gotten to 5/month with Spiral. I just need to go forward.

It is true that my 2014 work is not good enough. A proper story requires a consistent vision which thanks to the intro chapters has been established. This time I'll be able to make a proper try. The 2014 work has been very exploratory.

Right now I am just sad. But once I taste success I will make a connection with the world.

Isn't this vision of mine something that I've taken 35 years to cultivate? Anyone can write, but a 10 year old or a 20 year old me could not do it. As I keep living I will only get stronger.

I was fine to just play games as a kid. And it is fine, to just make use of what is out there.

I needed an out and here it is. Honoring the Lord of Nightmares and putting the dot on the current period of machine learning is what I should aim for.

5:40pm. I should aim for it. Not to become a writer, but to become my own studio. That is true path of an artist.

5:45pm. Who wants to work for other people? I will instantiate my vision of the future and sustain myself through that. I can always make something up, and the ML wave will ensure that it never gets boring.

...

While I was in bed I had time to think about the scene. Basically right now, I do not have the mental state to do much banter. Akamatsu is really good at friendly banter and bad at philosophy while I am the complete opposite.

It is true that I've sort been aiming for a betrayal kind of scene, I'll keep that kind of sentiment, but change the overall theme of the sequence. I won't put too much focus on the guide herself. The focus will always be on inside Euclid's own mind. There is a moral lesson behind this story and I have a message to tell.

It is a powerful thing. It is not just going to vanish just like that.

Only I can do it, so I might as well do it.

5:55pm. Yeah, it is going to get some pep work for me to properly get into it. I am not a real artist just yet. Once I post the thing and see the reactions, maybe that will awaken something in me? I need to work towards finishing chapter 4. Once that is done, I will be able to post in online for the first time.

6pm. Right now, it is time for fun. I am going to keep resting during the day and ranting until I get into the right mindset.

This is how I went through the programming journey. This is how I will tackle the writing challenge. With grit and perseverance. There are always reasons to do and not do something. I will find the right ones to motivate myself."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[50f9557acb...](https://github.com/treckstar/yolo-octo-hipster/commit/50f9557acb11095118319226c768b9532834f56b)
#### Friday 2022-08-12 16:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [noamco23-meet/Individual-Project](https://github.com/noamco23-meet/Individual-Project)@[526eac8b94...](https://github.com/noamco23-meet/Individual-Project/commit/526eac8b94efc99232db76299dc54f95b992d5a6)
#### Friday 2022-08-12 16:51:08 by Noam Cohen-Ofir

added error messages

why am i updating this after the summer?
i dont know
still mad that you guys didn't use this website for the cs money. people wanted to transfer their money between users didn't they!! (rhetorical question without a question mark)
the answer is yes the people wanted transfers and my website delivered and alas,,,, sexism in the workplace (that was a joke)
hope you guys see this but also like sorry
i had a great summer thank you so much for everything <3

---
## [eun0115/android_kernel_samsung_universal7904](https://github.com/eun0115/android_kernel_samsung_universal7904)@[b354d065ec...](https://github.com/eun0115/android_kernel_samsung_universal7904/commit/b354d065eca922ce2219b4b29e0b85653f86ca67)
#### Friday 2022-08-12 17:42:13 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [capnganj/fxhash-MagicMushrooms](https://github.com/capnganj/fxhash-MagicMushrooms)@[ff143311ec...](https://github.com/capnganj/fxhash-MagicMushrooms/commit/ff143311ec2c24919fc9adc06d0df2139968169f)
#### Friday 2022-08-12 18:43:42 by Benjamin Howes

second step :mushroom:

:laughing: omg you goddamn know it is the 90s again my grungy stoner babies.  This is going to work :mushroom: :doughnut:

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[5b6010d722...](https://github.com/silicons/Citadel-Station-13-RP/commit/5b6010d722f24734b362064ee9e12ce521aa078e)
#### Friday 2022-08-12 20:57:14 by lectronyx

Closed Eyes (#4303)

* Closed Eyes

Adds the "Closed Eyes" marking from Vorestation, because Sergal Eyes suck ass and in this house we bully cheeses

* unfucked sprite

apparently i just needed to give -head

* Fixed newline error

Apparently, ending on a line with content is bad.

---
## [git/git](https://github.com/git/git)@[5beca49a0b...](https://github.com/git/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Friday 2022-08-12 21:08:36 by Ævar Arnfjörð Bjarmason

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
## [Danntime/Navetas](https://github.com/Danntime/Navetas)@[280000f215...](https://github.com/Danntime/Navetas/commit/280000f215ba3a01781e25b6729d16ffe38548d6)
#### Friday 2022-08-12 21:21:17 by Danntime

TextBoxes/tuto

I put so much time doing this seriously
these are fucking textboxes damn
anyway they are good to go now its midnight i am literally coding in the middle of a wheat field

---
## [John-Dang/lobotomy-corp13](https://github.com/John-Dang/lobotomy-corp13)@[f968fffb12...](https://github.com/John-Dang/lobotomy-corp13/commit/f968fffb12c5283b0dd5b9224a8691f1facf70ef)
#### Friday 2022-08-12 21:27:15 by Zachary Goldman

no access airlocks

asteroid shuttle no longer has airlocks that require ID access

removing underwater basket recipes and death angel mushrooms

removing one mushroom type and a basket weaving recipe and object

death nettle gone

removed death nettle and its products

rainbow weed removed

removed the funny king of weed plants

removed a couple replicapods

the pods themselves aren't removed entirely but you can't mutate them from cabbages now

reishe no longer grow as weed or seed available

its in da code but you can't really access it without a manual spawn

jupiter cups removed

removed the jupiter cup mushroom

poppy no longer has libital in it

the poppy should be safe for growth and use now

poison berries removed

bad berries gone

world peas gone

no more world peace because the city is sad and violent

spaceman's trumpet gone + trumpet cake

Removed the funny flower and its super cake

corpse flower gone

no more stinky miasma flower

omega weed gone

head made it illegal

lifeweed no longer has omnizine

white weed should be no abuse now

coffee robusta gone

no more coffee robusta

killer tomato not accessible

players should not be able to grow it, even though it still exists as a simplemob

star cactus made safe no more helbital

its now safe to grow no more funny healing chem

sugarcane no longer mutates into bamboo

so it should be inaccessible

ambrosia seeds inaccessible + dank pizza no longer heals

dank pizza ain't accessible anyways but this should help plus ambrosia no longer an issue ingame

kudzu not accessible by players

it still exists in code but can't be randomly grown as weeds or accessed

fraxinella nutriment line removed

nothin special here

glowcap teslium removed

shouldn't make sentient creatures now

green grapes no longer have airui in them

should be safe last plant change

left 4 zed gone from biogenerator

its gooone

strange seeds + monkey cubes removed from biogen

no funny monkey memes

little carpet change

just made a couple airlocks have little airlock bottoms on them

changed a few announcements to manager

my immersion

---
## [llvm/llvm-project](https://github.com/llvm/llvm-project)@[e17cae076c...](https://github.com/llvm/llvm-project/commit/e17cae076c4727b99017927c3e8746db5bec6db7)
#### Friday 2022-08-12 22:13:58 by Walter Erquinigo

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
## [VaelophisNyx/Yogstation](https://github.com/VaelophisNyx/Yogstation)@[9813e53f3f...](https://github.com/VaelophisNyx/Yogstation/commit/9813e53f3fa719cc23c32a89d1bf96d8b76be299)
#### Friday 2022-08-12 22:20:47 by 00ze-cyclone

remove one space (#14472)

I think it might fix everything, if it does then holy shit I want HC

---
## [lewcc/Paradise](https://github.com/lewcc/Paradise)@[fd5580307e...](https://github.com/lewcc/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Friday 2022-08-12 22:32:46 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [JuliaPackaging/BinaryBuilderBase.jl](https://github.com/JuliaPackaging/BinaryBuilderBase.jl)@[047eb6f9a8...](https://github.com/JuliaPackaging/BinaryBuilderBase.jl/commit/047eb6f9a8e71a7d3d00bf91f7915cfed87083c7)
#### Friday 2022-08-12 22:52:14 by Keno Fischer

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
## [noreenko/RWoM](https://github.com/noreenko/RWoM)@[bc6c0ffd17...](https://github.com/noreenko/RWoM/commit/bc6c0ffd17f558adff1415ef80408b309c434157)
#### Friday 2022-08-12 23:19:24 by TorannD

v2.5.8.0 update

New:
 o Advanced Classes
  - Unique type of custom class that can be added (or removed) onto existing classes
  - Share the same pawn level and displays on the same might/magic tabs with base class, and other advanced classes
  - Advanced classes share the same xml definition as normal classes, but are identified using the <isAdvancedClass> tag
  - See the Possessed class for an example
  - Other options for advanced classes include:
	* Restrict the advanced class to require a base class first using <requiresBaseClass> (true/false)
	* Allow the advanced class to be added as a trait during pawn generation with <canSpawnWithClass> (true/false)
	* Create advanced class "chains" by removing a pre-requisite trait with <removeRequiredTrait> (true/false)
	* Specify one or more valid pre-requisite traits using <requiredTraits> (TraitDef list)
	* Prevent pawns with certain traits from becoming the advanced class using <disallowedTraits> (TraitDef list)

 o Chained abilities
  - TMAbilityDef options that allow temporary abilities to be added and removed to create ability chains
  - See Possessed Control Spirit Storm for an example
  - Options include:
	* Specify a chained ability <chainedAbility> (TMAbilityDef)
	* Manually set a duration for the temporary ability <chainedAbilityExpiresAfterTicks> (integer > 0, -1 for "do not use")
	* Link the chained ability to be removed when the main ability cooldown expires <chainedAbilityExpiresAfterCooldown> (true/false)
	* Remove the ability after use; can be applied to any ability <removeAbilityAfterUse> (true/false)
	* Remove a list of abilities after use to clear or reset an ability chain <abilitiesRemovedWhenUsed> (TMAbilityDef list)

 o New Class: Possessor - an invisible, wandering spirit able to possess the bodies of the dead or living using spirit energy
  - Perishes when spirit energy fully depletes
  - Uses spirit energy to fuel their abilities
  - Able to possess other bodies and augments the abilities of the occupied body
  - Able to possess a corpse with all skills, talents, and memories of the dead pawn, but spirit energy will gradually deplete and must be replenished
  - Able to possess animals and assert control over their actions; the spirit has limited influence while in the body of an animal and spirit energy gradually depletes
  - Able to possess living pawns; much lower spirit energy loss than other options, but the host pawn will have conflicting thoughts - this can be offset if the spirit and the host pawn share the same outlook on life (backstory preferences, traits, gender, ideo, etc)
  - Shard of spirit extraction is used to remove a spirit from a pawn; the spirit may exit the body of an animal at any time
  - The possessor may naturally gain spirit energy while doing common, meditative tasks and can forcefully gain spirit energy using an ability or inflicting melee damage
  - A pawn occupied by a possessor will no longer be able to heal naturally; wounds can only be healed by external items, abilities, or spells, or when the possessed pawn gains spirit energy (by any means)

 o New Autocast options:
  - <onlyAppliesToCaster> (true/false) - forces the condition check against the caster instead of the target, when different
  - <targetNoFaction> (true/false) - target pawn is only selected if the faction is null (wild pawns)

Tweaks:
 o Summoned creatures will respond more aggressively when summoned near enemies
 o Magic Wardrobe automatically sets swapped equipment as forced/locked
 o Changed Brand graphics to be less error prone

Bug fixes:
 o Polymorphed or shapeshifted animals will take drafted orders again
 o Taunted targets will no longer attempt to attack a deceased taunter
 o Fixed a bug where AI would not use abilities if autocasting was disabled
 o Winter's Reign and Snap Freeze correctly assign damage attribution
 o Cure Disease can be cast while wearing a shield belt
 o Defense pylon will only spam invalid location message once instead of infinitely

---
## [BootlegBow/KirieStation](https://github.com/BootlegBow/KirieStation)@[8a977645a0...](https://github.com/BootlegBow/KirieStation/commit/8a977645a0f4c6e1560405bc0acaa317f643a7e0)
#### Friday 2022-08-12 23:35:58 by projectkepler-RU

Blue helmets resprites (#777)

* gsdkfsldka

* blue helmet babey

* more reskin

* aaa

* blue helmete

* blue beret too :)

* the blue helmets :3

* I hate how hard my fucking life is

* now you have both :)

---

