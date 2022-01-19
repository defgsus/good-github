## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-18](docs/good-messages/2022/2022-01-18.md)


1,721,533 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,721,533 were push events containing 2,665,768 commit messages that amount to 208,057,783 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[d005d76f0b...](https://github.com/Paxilmaniac/tgstation/commit/d005d76f0bd201060b6ee515678a4b6950d9f0eb)
#### Tuesday 2022-01-18 00:04:22 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[7bead07444...](https://github.com/StarStation13/StarStation13/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Tuesday 2022-01-18 00:19:45 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[413fd90502...](https://github.com/timothymtorres/tgstation/commit/413fd9050271829e2899b88a676995ae2517111c)
#### Tuesday 2022-01-18 00:47:15 by GoldenAlpharex

Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[b8af0d0a5c...](https://github.com/crawl/crawl/commit/b8af0d0a5c555d92b426b3ed22fa288e9ab0a9c8)
#### Tuesday 2022-01-18 01:05:07 by Nicholas Feinberg

Play with ranged weapon stats more

Following some thinking about ranged weapons, here's a new set of
ammoless stats. Philosophy:

- Slings are high-skill 1-handers. Hunting slings are vaguely like
  war axes, and fustibaluses are no longer ultra-rare but are now
  more like broad axes.
- Bows are high-skill 2-handers.
- Crossbows are lower-skill - it takes fairly little to get the hand
  crossbow or the arbalest to mindelay. The triple crossbow is still
  high-skill, but it's quite rare, so doesn't define the 'feel' of
  the class, much as you can't rely on finding a triple sword as a
  lbl user or an exec axe as an axe user. (Unless a gifting god gets
  involved.)

If we're going to keep all these item classes, it would be great to
have some more obvious and pronounced gimmicks. I suspect we'll end
up merging or removing some of these at some point, but that's a
larger project than I'm ready for right now.

TODO: make fustibali spawn at a higher rate - right now they're about
1/5th as common as I'd like.

---
## [nkruzan/ardu-configurator](https://github.com/nkruzan/ardu-configurator)@[7e0a444f79...](https://github.com/nkruzan/ardu-configurator/commit/7e0a444f79fa612bf2150be5c27bfb7f6666bc06)
#### Tuesday 2022-01-18 02:05:49 by Buzz

wip smartlinks test - can we get server-side node from mavagent to work?


more wip - 

tmp copied mav_v2.js direct from mavagent, as its known to work with smartlinks.js , also from mavagent.  todo delete the mav_v2 and use the one in js/mavsp/ foldrr
notes abut using -sdk version for developers


make new backend folder for Node-loaded local code.


allow jspack and 'long' module to both be used by the backend, if we want. 

yes, this is a differernet to the one in js/mavsp/local_modules/ which are currently tweaked for frontend use. sorry about the dupe, we should fix that at some point.
add mavlink parser as a proper local-node-module to the backend

.. with just tiny tweaks.
describe NW flavour on console at startup.

its easy to get the wrong one.
more dev notes


lightly hacked mavagent.js and its modules bing used as a pre-startup.js for ArduConfigurator.

// TERRIBLE HACK using mavagent.js almost in its entirety as a pre-startup.js for arduconfigurator.  
// surprisingly, it seems to kinda mostly work apart from the CLI interface.    we won't leave this here, but its interesting.
 - having this loaded its connecting to a SITL instance on tcp:localhost:5760 if u have one, and forwarding the packets to udp:localhost:14550, such as missionplanner etc.   its not yet routing any of this mavlink stream into the GUI, but its not crashing. 
remove most of  mavagent from pre-startup.js leaving mostly just smartlinks.js  AND get backend UDP routing through to frontend

frontend GUI is a bit borked when UDP right now, but its getting the data.
hex_parser changes are untested so hext parsing might be broken.?

prevents *really* early udp/tcp throwing error before window is opend.

---
## [newstools/2022-sunday-world](https://github.com/newstools/2022-sunday-world)@[5a04ec08cb...](https://github.com/newstools/2022-sunday-world/commit/5a04ec08cb239f54b88cb9d9678ffadf5457fadb)
#### Tuesday 2022-01-18 02:55:35 by Billy Einkamerer

Created Text For URL [sundayworld.co.za/news/family-ecstatic-as-11-year-old-girl-resurfaces-after-being-lured-by-boyfriend/]

---
## [JeremyGamer13/scratch-for-discord-jt](https://github.com/JeremyGamer13/scratch-for-discord-jt)@[6dc559c253...](https://github.com/JeremyGamer13/scratch-for-discord-jt/commit/6dc559c253ab6a9b09ed8ea6e9b61bd19edf933d)
#### Tuesday 2022-01-18 04:44:37 by JeremyGamer13

fuck you jose

why did you make streaming url only have one fucking status ffs

---
## [snickerbockers/calc-tutorial](https://github.com/snickerbockers/calc-tutorial)@[b2ac5a82d3...](https://github.com/snickerbockers/calc-tutorial/commit/b2ac5a82d3cff332e44a252dad393fc39d74b75c)
#### Tuesday 2022-01-18 07:26:02 by snickerbockers

ingenius fix for bug when subtracting negative numbers

the negative-operator reduction was eating up the subtraction too

so something like 4.5 - -0.5 would result in the 0.5 getting negated
twice because the subtraction is misinterpreted as another negative

this is proof that my life is cursed and nothing bad ever happens to me
because of my own actions or inability to learn.  @inolen literally never
has these problems because he's a spoiled rich kid whose daddy buys
everything for him.  unlike me who lives unemployed mooching off my parents and
has to resort to using the *lowest-end* version of m1 macbook air due to
my extreme poverty.

And not only that, but i ordered chik-fil-a from grub-hub and the driver
delivered *somebody else's* order before mine.  What a fucking karen.

---
## [Axwalmishra/Axwalmishra](https://github.com/Axwalmishra/Axwalmishra)@[d7c5019b84...](https://github.com/Axwalmishra/Axwalmishra/commit/d7c5019b8436e46f7a149d0677f45cbc4c8c0cc4)
#### Tuesday 2022-01-18 07:28:48 by Axwalmishra

Update birthday 

Happy birthday dear god bless you 🙌💝
Your all dream come true 😍💌💌💌
Enjoy your day and celebrite your birthday 🤗🤗👍🏻💌

---
## [starunity/dwm](https://github.com/starunity/dwm)@[67d76bdc68...](https://github.com/starunity/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-01-18 07:33:34 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [justinian/jsix](https://github.com/justinian/jsix)@[1d30322820...](https://github.com/justinian/jsix/commit/1d30322820ce22910e5cb21b259080874b47c207)
#### Tuesday 2022-01-18 07:35:47 by Justin C. Miller

[kernel] Pass objects not handles to syscall impls

This commit contains a couple large, interdependent changes:

- In preparation for capability checking, the _syscall_verify_*
  functions now load most handles passed in, and verify that they exist
  and are of the correct type. Lists and out-handles are not converted
  to objects.
- Also in preparation for capability checking, the internal
  representation of handles has changed. j6_handle_t is now 32 bits, and
  a new j6_cap_t (also 32 bits) is added. Handles of a process are now a
  util::map<j6_handle_t, handle> where handle is a new struct containing
  the id, capabilities, and object pointer.
- The kernel object definition DSL gained a few changes to support auto
  generating the handle -> object conversion in the _syscall_verify_*
  functions, mostly knowing the object type, and an optional "cname"
  attribute on objects where their names differ from C++ code.
  (Specifically vma/vm_area)
- Kernel object code and other code under kernel/objects is now in a new
  obj:: namespace, because fuck you <cstdlib> for putting "system" in
  the global namespace. Why even have that header then?
- Kernel object types constructed with the construct_handle helper now
  have a creation_caps static member to declare what capabilities a
  newly created object's handle should have.

---
## [The-Black-Screen/MonkeStation](https://github.com/The-Black-Screen/MonkeStation)@[040b7ff839...](https://github.com/The-Black-Screen/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Tuesday 2022-01-18 07:58:36 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [popeye92/Top10](https://github.com/popeye92/Top10)@[7400eb7a80...](https://github.com/popeye92/Top10/commit/7400eb7a8068179812f6ef96ee67bb492bed15e4)
#### Tuesday 2022-01-18 09:22:15 by Henry Hu

Create index.zh-tw.md

# OWASP Top 10 2021 介紹

歡迎來到最新版本的 OWASP Top 10! OWASP Top 10 2021 最新版本不只是設計
上不同，我們也提供了一頁式的圖形化說明讓你可以印出來，你可以從我們的網頁
上面直接下載。
Welcome to the latest installment of the OWASP Top 10! The OWASP Top 10
2021 is all-new, with a new graphic design and an available one-page
infographic you can print or obtain from our home page.

A huge thank you to everyone that contributed their time and data for
this iteration. Without you, this installment would not happen. **THANK
YOU**.

## What's changed in the Top 10 for 2021

There are three new categories, four categories with naming and scoping
changes, and some consolidation in the Top 10 for 2021.

<img src="./assets/image1.png" style="width:6.5in;height:1.78889in" alt="Mapping of the relationship between the Top 10 2017 and the new Top 10 2021" />

**A01:2021-Broken Access Control** moves up from the fifth position; 94%
of applications were tested for some form of broken access control. The
34 CWEs mapped to Broken Access Control had more occurrences in
applications than any other category.

**A02:2021-Cryptographic Failures** shifts up one position to #2,
previously known as *Sensitive Data Exposure,* which was broad symptom
rather than a root cause. The renewed focus here is on failures related
to cryptography which often leads to sensitive data exposure or system
compromise.

**A03:2021-Injection** slides down to the third position. 94% of the
applications were tested for some form of injection, and the 33 CWEs
mapped into this category have the second most occurrences in
applications. Cross-site Scripting is now part of this category in this
edition.

**A04:2021-Insecure Design** is a new category for 2021, with a focus on
risks related to design flaws. If we genuinely want to "move left" as an
industry, it calls for more use of threat modeling, secure design
patterns and principles, and reference architectures.

**A05:2021-Security Misconfiguration** moves up from #6 in the previous
edition; 90% of applications were tested for some form of
misconfiguration. With more shifts into highly configurable software,
it's not surprising to see this category move up. The former category
for XML External Entities (XXE) is now part of this category.

**A06:2021-Vulnerable and Outdated Components** was previously titled
*Using Components with Known Vulnerabilities* and is #2 in the industry
survey, but also had enough data to make the Top 10 via data analysis.
This category moves up from #9 in 2017 and is a known issue that we
struggle to test and assess risk. It is the only category not to have
any CVEs mapped to the included CWEs, so a default exploit and impact
weights of 5.0 are factored into their scores.

**A07:2021-Identification and Authentication Failures** was previously
*Broken Authentication* and is sliding down from the second position,
and now includes CWEs that are more related to identification failures.
This category is still an integral part of the Top 10, but the increased
availability of standardized frameworks seems to be helping.

**A08:2021-Software and Data Integrity Failures** is a new category for
2021, focusing on making assumptions related to software updates,
critical data, and CI/CD pipelines without verifying integrity. One of
the highest weighted impacts from CVE/CVSS data mapped to the 10 CWEs in
this category. Insecure Deserialization from 2017 is now a part of this
larger category.

**A09:2021-Security Logging and Monitoring Failures** was previously
*Insufficient Logging &* Monitoring and is added from the industry
survey (#3), moving up from #10 previously. This category is expanded to
include more types of failures, is challenging to test for, and isn't
well represented in the CVE/CVSS data. However, failures in this
category can directly impact visibility, incident alerting, and
forensics.

**A10:2021-Server-Side Request Forgery** is added from the industry
survey (#1). The data shows a relatively low incidence rate with above
average testing coverage, along with above-average ratings for Exploit
and Impact potential. This category represents the scenario where the
industry professionals are telling us this is important, even though
it's not illustrated in the data at this time.

## Methodology

This installment of the Top 10 is more data-driven than ever but not
blindly data-driven. We selected eight of the ten categories from
contributed data and two categories from an industry survey at a high
level. We do this for a fundamental reason, looking at the contributed
data is looking into the past. AppSec researchers take time to find new
vulnerabilities and new ways to test for them. It takes time to
integrate these tests into tools and processes. By the time we can
reliably test a weakness at scale, years have likely passed. To balance
that view, we use an industry survey to ask people on the front lines
what they see as essential weaknesses that the data may not show yet.

There are a few critical changes that we adopted to continue to mature
the Top 10.

### How the categories are structured

A few categories have changed from the previous installment of the OWASP
Top Ten. Here is a high-level summary of the category changes.

Previous data collection efforts were focused on a prescribed subset of
approximately 30 CWEs with a field asking for additional findings. We
learned that organizations would primarily focus on just those 30 CWEs
and rarely add additional CWEs that they saw. In this iteration, we
opened it up and just asked for data, with no restriction on CWEs. We
asked for the number of applications tested for a given year (starting
in 2017), and the number of applications with at least one instance of a
CWE found in testing. This format allows us to track how prevalent each
CWE is within the population of applications. We ignore frequency for
our purposes; while it may be necessary for other situations, it only
hides the actual prevalence in the application population. Whether an
application has four instances of a CWE or 4,000 instances is not part
of the calculation for the Top 10. We went from approximately 30 CWEs to
almost 400 CWEs to analyze in the dataset. We plan to do additional data
analysis as a supplement in the future. This significant increase in the
number of CWEs necessitates changes to how the categories are
structured.

We spent several months grouping and categorizing CWEs and could have
continued for additional months. We had to stop at some point. There are
both *root cause* and *symptom* types of CWEs, where *root cause* types
are like "Cryptographic Failure" and "Misconfiguration" contrasted to
*symptom* types like "Sensitive Data Exposure" and "Denial of Service."
We decided to focus on the root cause whenever possible as it's more
logical for providing identification and remediation guidance. Focusing
on the root cause over the symptom isn't a new concept; the Top Ten has
been a mix of *symptom* and *root cause*. CWEs are also a mix of
*symptom* and *root cause*; we are simply being more deliberate about it
and calling it out. There is an average of 19.6 CWEs per category in
this installment, with the lower bounds at 1 CWE for
*A10:2021-Server-Side Request Forgery (SSRF)* to 40 CWEs in
*A04:2021-Insecure Design*. This updated category structure offers
additional training benefits as companies can focus on CWEs that make
sense for a language/framework.

### How the data is used for selecting categories

In 2017, we selected categories by incidence rate to determine
likelihood, then ranked them by team discussion based on decades of
experience for Exploitability, Detectability (also likelihood), and
Technical Impact. For 2021, we want to use data for Exploitability and
Impact if possible.

We downloaded OWASP Dependency Check and extracted the CVSS Exploit, and
Impact scores grouped by related CWEs. It took a fair bit of research
and effort as all the CVEs have CVSSv2 scores, but there are flaws in
CVSSv2 that CVSSv3 should address. After a certain point in time, all
CVEs are assigned a CVSSv3 score as well. Additionally, the scoring
ranges and formulas were updated between CVSSv2 and CVSSv3.

In CVSSv2, both Exploit and Impact could be up to 10.0, but the formula
would knock them down to 60% for Exploit and 40% for Impact. In CVSSv3,
the theoretical max was limited to 6.0 for Exploit and 4.0 for Impact.
With the weighting considered, the Impact scoring shifted higher, almost
a point and a half on average in CVSSv3, and exploitability moved nearly
half a point lower on average.

There are 125k records of a CVE mapped to a CWE in the NVD data
extracted from OWASP Dependency Check, and there are 241 unique CWEs
mapped to a CVE. 62k CWE maps have a CVSSv3 score, which is
approximately half of the population in the data set.

For the Top Ten, we calculated average exploit and impact scores in the
following manner. We grouped all the CVEs with CVSS scores by CWE and
weighted both exploit and impact scored by the percentage of the
population that had CVSSv3 + the remaining population of CVSSv2 scores
to get an overall average. We mapped these averages to the CWEs in the
dataset to use as Exploit and Impact scoring for the other half of the
risk equation.

## Why not just pure statistical data?

The results in the data are primarily limited to what we can test for in
an automated fashion. Talk to a seasoned AppSec professional, and they
will tell you about stuff they find and trends they see that aren't yet
in the data. It takes time for people to develop testing methodologies
for certain vulnerability types and then more time for those tests to be
automated and run against a large population of applications. Everything
we find is looking back in the past and might be missing trends from the
last year, which are not present in the data.

Therefore, we only pick eight of ten categories from the data because
it's incomplete. The other two categories are from the industry survey.
It allows the practitioners on the front lines to vote for what they see
as the highest risks that might not be in the data (and may never be
expressed in data).

## Why incidence rate instead of frequency?

There are three primary sources of data. We identify them as
Human-assisted Tooling (HaT), Tool-assisted Human (TaH), and raw
Tooling.

Tooling and HaT are high-frequency finding generators. Tools will look
for specific vulnerabilities and tirelessly attempt to find every
instance of that vulnerability and will generate high finding counts for
some vulnerability types. Look at Cross-Site Scripting, which is
typically one of two flavors: it's either a more minor, isolated mistake
or a systemic issue. When it's a systemic issue, the finding counts can
be in the thousands for an application. This high frequency drowns out
most other vulnerabilities found in reports or data.

TaH, on the other hand, will find a broader range of vulnerability types
but at a much lower frequency due to time constraints. When humans test
an application and see something like Cross-Site Scripting, they will
typically find three or four instances and stop. They can determine a
systemic finding and write it up with a recommendation to fix on an
application-wide scale. There is no need (or time) to find every
instance.

Suppose we take these two distinct data sets and try to merge them on
frequency. In that case, the Tooling and HaT data will drown the more
accurate (but broad) TaH data and is a good part of why something like
Cross-Site Scripting has been so highly ranked in many lists when the
impact is generally low to moderate. It's because of the sheer volume of
findings. (Cross-Site Scripting is also reasonably easy to test for, so
there are many more tests for it as well).

In 2017, we introduced using incidence rate instead to take a fresh look
at the data and cleanly merge Tooling and HaT data with TaH data. The
incidence rate asks what percentage of the application population had at
least one instance of a vulnerability type. We don't care if it was
one-off or systemic. That's irrelevant for our purposes; we just need to
know how many applications had at least one instance, which helps
provide a clearer view of the testing is findings across multiple
testing types without drowning the data in high-frequency results.

## What is your data collection and analysis process?

We formalized the OWASP Top 10 data collection process at the Open
Security Summit in 2017. OWASP Top 10 leaders and the community spent
two days working out formalizing a transparent data collection process.
The 2021 edition is the second time we have used this methodology.

We publish a call for data through social media channels available to
us, both project and OWASP. On the [OWASP Project
page](https://owasp.org/www-project-top-ten/#div-data_2020), we list the
data elements and structure we are looking for and how to submit them.
In the [GitHub
project](https://github.com/OWASP/Top10/tree/master/2020/Data), we have
example files that serve as templates. We work with organizations as
needed to help figure out the structure and mapping to CWEs.

We get data from organizations that are testing vendors by trade, bug
bounty vendors, and organizations that contribute internal testing data.
Once we have the data, we load it together and run a fundamental
analysis of what CWEs map to risk categories. There is overlap between
some CWEs, and others are very closely related (ex. Cryptographic
vulnerabilities). Any decisions related to the raw data submitted are
documented and published to be open and transparent with how we
normalized the data.

We look at the eight categories with the highest incidence rates for
inclusion in the Top 10. We also look at the industry survey results to
see which ones may already be present in the data. The top two votes
that aren't already present in the data will be selected for the other
two places in the Top 10. Once all ten were selected, we applied
generalized factors for exploitability and impact; to help rank the Top
10 in order.

## Data Factors

There are data factors that are listed for each of the Top 10
Categories, here is what they mean:

-   *CWEs Mapped*: The number of CWEs mapped to a category by the Top 10
    team.

-   *Incidence Rate*: Incidence rate is the percentage of applications
    vulnerable to that CWE from the population tested by that org for
    that year.

-   (Testing) *Coverage*: The percentage of applications tested by all
    organizations for a given CWE.

-   *Weighted Exploit*: The Exploit sub-score from CVSSv2 and CVSSv3
    scores assigned to CVEs mapped to CWEs, normalized, and placed on a
    10pt scale.

-   *Weighted Impact*: The Impact sub-score from CVSSv2 and CVSSv3
    scores assigned to CVEs mapped to CWEs, normalized, and placed on a
    10pt scale.

-   *Total Occurrences*: Total number of applications found to have the
    CWEs mapped to a category.

-   *Total CVEs*: Total number of CVEs in the NVD DB that were mapped to
    the CWEs mapped to a category.

## Category Relationships from 2017

There has been a lot of talk about the overlap between the Top Ten
risks. By the definition of each (list of CWEs included), there really
isn't any overlap. However, conceptually, there can be overlap or
interactions based on the higher-level naming. Venn diagrams are many
times used to show overlap like this.

<img src="./assets/image2.png" style="width:4.31736in;height:3.71339in" alt="Diagram Description automatically generated" />

The Venn diagram above represents the interactions between the Top Ten
2017 risk categories. While doing so, a couple of essential points
became obvious:

1.  One could argue that Cross-Site Scripting ultimately belongs within
    Injection as it's essentially Content Injection. Looking at the 2021
    data, it became even more evident that XSS needed to move into
    Injection.

2.  The overlap is only in one direction. We will often classify a
    vulnerability by the end manifestation or "symptom," not the
    (potentially deep) root cause. For instance, "Sensitive Data
    Exposure" may have been the result of a "Security Misconfiguration";
    however, you won't see it in the other direction. As a result,
    arrows are drawn in the interaction zones to indicate which
    direction it occurs.

3.  Sometimes these diagrams are drawn with everything in *A06:2021
    Using Components with Known Vulnerabilities*. While some of these
    risk categories may be the root cause of third-party
    vulnerabilities, they are generally managed differently and with
    different responsibilities. The other types are typically
    representing first-party risks.

# Thank you to our data contributors

The following organizations (along with some anonymous donors) kindly
donated data for over 500,000 applications to make this the largest and
most comprehensive application security data set. Without you, this
would not be possible.

| | | | |
| :---: | :---: | :---: | :---: |
| AppSec Labs | GitLab | Micro Focus | Sqreen |
| Cobalt.io | HackerOne | PenTest-Tools | Veracode |
| Contrast Security | HCL Technologies | Probely | WhiteHat (NTT) |

---
## [nim-works/nimskull](https://github.com/nim-works/nimskull)@[f35b5bf2d4...](https://github.com/nim-works/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Tuesday 2022-01-18 09:38:26 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [Sverdfisk/github-slideshow](https://github.com/Sverdfisk/github-slideshow)@[86aa8820d6...](https://github.com/Sverdfisk/github-slideshow/commit/86aa8820d6b21a31db82c7b4d015b179f4c99e74)
#### Tuesday 2022-01-18 10:06:24 by Ken

Update 0000-01-02-Sverdfisk.md

What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.

---
## [Dark-Matter7232/kernel_x86_laptop](https://github.com/Dark-Matter7232/kernel_x86_laptop)@[eb376ff34c...](https://github.com/Dark-Matter7232/kernel_x86_laptop/commit/eb376ff34c225d8378c6720d4b044fe575079372)
#### Tuesday 2022-01-18 11:10:48 by Dave Chinner

xfs: reduce kvmalloc overhead for CIL shadow buffers

Oh, let me count the ways that the kvmalloc API sucks dog eggs.

The problem is when we are logging lots of large objects, we hit
kvmalloc really damn hard with costly order allocations, and
behaviour utterly sucks:

     - 49.73% xlog_cil_commit
	 - 31.62% kvmalloc_node
	    - 29.96% __kmalloc_node
	       - 29.38% kmalloc_large_node
		  - 29.33% __alloc_pages
		     - 24.33% __alloc_pages_slowpath.constprop.0
			- 18.35% __alloc_pages_direct_compact
			   - 17.39% try_to_compact_pages
			      - compact_zone_order
				 - 15.26% compact_zone
				      5.29% __pageblock_pfn_to_page
				      3.71% PageHuge
				    - 1.44% isolate_migratepages_block
					 0.71% set_pfnblock_flags_mask
				   1.11% get_pfnblock_flags_mask
			   - 0.81% get_page_from_freelist
			      - 0.59% _raw_spin_lock_irqsave
				 - do_raw_spin_lock
				      __pv_queued_spin_lock_slowpath
			- 3.24% try_to_free_pages
			   - 3.14% shrink_node
			      - 2.94% shrink_slab.constprop.0
				 - 0.89% super_cache_count
				    - 0.66% xfs_fs_nr_cached_objects
				       - 0.65% xfs_reclaim_inodes_count
					    0.55% xfs_perag_get_tag
				   0.58% kfree_rcu_shrink_count
			- 2.09% get_page_from_freelist
			   - 1.03% _raw_spin_lock_irqsave
			      - do_raw_spin_lock
				   __pv_queued_spin_lock_slowpath
		     - 4.88% get_page_from_freelist
			- 3.66% _raw_spin_lock_irqsave
			   - do_raw_spin_lock
				__pv_queued_spin_lock_slowpath
	    - 1.63% __vmalloc_node
	       - __vmalloc_node_range
		  - 1.10% __alloc_pages_bulk
		     - 0.93% __alloc_pages
			- 0.92% get_page_from_freelist
			   - 0.89% rmqueue_bulk
			      - 0.69% _raw_spin_lock
				 - do_raw_spin_lock
				      __pv_queued_spin_lock_slowpath
	   13.73% memcpy_erms
	 - 2.22% kvfree

On this workload, that's almost a dozen CPUs all trying to compact
and reclaim memory inside kvmalloc_node at the same time. Yet it is
regularly falling back to vmalloc despite all that compaction, page
and shrinker reclaim that direct reclaim is doing. Copying all the
metadata is taking far less CPU time than allocating the storage!

Direct reclaim should be considered extremely harmful.

This is a high frequency, high throughput, CPU usage and latency
sensitive allocation. We've got memory there, and we're using
kvmalloc to allow memory allocation to avoid doing lots of work to
try to do contiguous allocations.

Except it still does *lots of costly work* that is unnecessary.

Worse: the only way to avoid the slowpath page allocation trying to
do compaction on costly allocations is to turn off direct reclaim
(i.e. remove __GFP_RECLAIM_DIRECT from the gfp flags).

Unfortunately, the stupid kvmalloc API then says "oh, this isn't a
GFP_KERNEL allocation context, so you only get kmalloc!". This
cuts off the vmalloc fallback, and this leads to almost instant OOM
problems which ends up in filesystems deadlocks, shutdowns and/or
kernel crashes.

I want some basic kvmalloc behaviour:

- kmalloc for a contiguous range with fail fast semantics - no
  compaction direct reclaim if the allocation enters the slow path.
- run normal vmalloc (i.e. GFP_KERNEL) if kmalloc fails

The really, really stupid part about this is these kvmalloc() calls
are run under memalloc_nofs task context, so all the allocations are
always reduced to GFP_NOFS regardless of the fact that kvmalloc
requires GFP_KERNEL to be passed in. IOWs, we're already telling
kvmalloc to behave differently to the gfp flags we pass in, but it
still won't allow vmalloc to be run with anything other than
GFP_KERNEL.

So, this patch open codes the kvmalloc() in the commit path to have
the above described behaviour. The result is we more than halve the
CPU time spend doing kvmalloc() in this path and transaction commits
with 64kB objects in them more than doubles. i.e. we get ~5x
reduction in CPU usage per costly-sized kvmalloc() invocation and
the profile looks like this:

  - 37.60% xlog_cil_commit
	16.01% memcpy_erms
      - 8.45% __kmalloc
	 - 8.04% kmalloc_order_trace
	    - 8.03% kmalloc_order
	       - 7.93% alloc_pages
		  - 7.90% __alloc_pages
		     - 4.05% __alloc_pages_slowpath.constprop.0
			- 2.18% get_page_from_freelist
			- 1.77% wake_all_kswapds
....
				    - __wake_up_common_lock
				       - 0.94% _raw_spin_lock_irqsave
		     - 3.72% get_page_from_freelist
			- 2.43% _raw_spin_lock_irqsave
      - 5.72% vmalloc
	 - 5.72% __vmalloc_node_range
	    - 4.81% __get_vm_area_node.constprop.0
	       - 3.26% alloc_vmap_area
		  - 2.52% _raw_spin_lock
	       - 1.46% _raw_spin_lock
	      0.56% __alloc_pages_bulk
      - 4.66% kvfree
	 - 3.25% vfree
	    - __vfree
	       - 3.23% __vunmap
		  - 1.95% remove_vm_area
		     - 1.06% free_vmap_area_noflush
			- 0.82% _raw_spin_lock
		     - 0.68% _raw_spin_lock
		  - 0.92% _raw_spin_lock
	 - 1.40% kfree
	    - 1.36% __free_pages
	       - 1.35% __free_pages_ok
		  - 1.02% _raw_spin_lock_irqsave

It's worth noting that over 50% of the CPU time spent allocating
these shadow buffers is now spent on spinlocks. So the shadow buffer
allocation overhead is greatly reduced by getting rid of direct
reclaim from kmalloc, and could probably be made even less costly if
vmalloc() didn't use global spinlocks to protect it's structures.

Signed-off-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Allison Henderson <allison.henderson@oracle.com>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Dark-Matter7232 <kerneldeveloper7232@gmail.com>

---
## [damiennaylor1/rpggame](https://github.com/damiennaylor1/rpggame)@[feff4a8db5...](https://github.com/damiennaylor1/rpggame/commit/feff4a8db57d399284bd8e74ee950b10ab8bd6a7)
#### Tuesday 2022-01-18 11:13:56 by damiennaylor1

Update rpgGame.java

Crafting system done
(What's next?)
Add more quests
Add proper lore?
Revamp entire fucking crafting system it FUCKING SUCKS!!! IT CANT EVEN USE MULTIPLE ITEMS!!
Idea for revamp: compare against individual crafting recipes, then list possible crafts (like the checkers system but retarded cause I am!)
FUCK THIS GAME ITS GOING TO BE SCRAPPED WHEN I MAKE 2D GRAPHICS ANYWAYS WHY AM I STILL WORKING ON IT????? FUCK.
Can't even do the combat system I want this project sucks I suck java sucks FUCK
im going to bed its 5 am

---
## [drednoot/arsmori2.0](https://github.com/drednoot/arsmori2.0)@[2241dd043a...](https://github.com/drednoot/arsmori2.0/commit/2241dd043a415feb13f01727ed6296191d788b8c)
#### Tuesday 2022-01-18 11:57:33 by drednoot

Squashed commit of the following:

commit 6bd44252d14e9e71fa2929b576dacdeb0c501463
Author: drednoot <matveyerohin228@gmail.com>
Date:   Tue Jan 18 15:05:25 2022 +0400

    okay seems to be working now

    fuck this shit

commit 0b621e67aa4873fb5cc84fb44cb80a3ed1883304
Author: drednoot <matveyerohin228@gmail.com>
Date:   Tue Jan 18 15:03:19 2022 +0400

    Update .gitignore

    still doesn't work

commit ab86bf60a5c2c92d2e4d583ae6254d69fa7f690e
Author: drednoot <matveyerohin228@gmail.com>
Date:   Tue Jan 18 14:58:32 2022 +0400

    fuck gitignore

    doesn't work stupid shit

---
## [avar/git](https://github.com/avar/git)@[8f55456ce3...](https://github.com/avar/git/commit/8f55456ce39c720ed649734017850670b1b7f33b)
#### Tuesday 2022-01-18 12:27:02 by Ævar Arnfjörð Bjarmason

HP/UX build patch

From <20211002103740.791d7d24@pc09> (private E-Mail) from "H.Merijn
Brand" <linux@tux.freedom.nl> on Sat, Oct 2, 2021. His reply to
questions I had:

    On Wed, 6 Oct 2021 14:39:32 +0200, Ævar Arnfjörð Bjarmason
    <avarab@gmail.com> wrote:

    > Thanks, I managed to get it building with that!
    >
    > Can I add your Signed-off-by for munging/upstreaming these patches, it

    Yes, you can

    > just certifies that you're the copyright holder of them (required for
    > the git project), will make it clear that any testing/mistakes etc.
    > are mine. Will CC you on them if/when that's ready. Of course not all
    > of it's upstream-able, will need to add the relevant things to
    > config.mak.uname etc.
    >
    > Are the /pro/gnu /pro etc. paths something that's just on your system,
    > or typical/common enough of HP/UX to put it into config that'll be
    > used by others on that uname -s?

    No, /pro is Procura-specific (and thus all of my systems)
    It was just convenient enough to abuse it for gnu stuff too, as it
    thusly does not interfere with HP-UX releases

    HP-UX is with a dash, not with a slash

    > If so, are the paths to the GNU tools similarly "standard"? Hopefully

    No, they are not, not even when you happen to get them from the HP
    porting center. They move from /opt to /usr/local back-and-forth on a
    very inconsistent and unpredictable way

    > it can be built/tested mostly with the native toolchain, but the tests
    > e.g. rely on "diff -u" by default for comparison on failure, so
    > pointing just that diff usage to the GNU one would be handy.

    I've seen (and used) a 'g' prefix being rather common on HP-UX and
    AIX, so if you can find gdiff before you can find diff, you can be
    reasonably safe it is the GNU version, but don't pin me on that.

    If I want to build anything serious on AIX or HP-UX, the first thing
    I (re)build is GNU make

    Next to 'diff', note that 'cmp' is really ugly on older versions of AIX
    and HP-UX and ultimately incompatible

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [CommE2E/comm](https://github.com/CommE2E/comm)@[aa32b3e308...](https://github.com/CommE2E/comm/commit/aa32b3e30828f881fb436755fed3e0cd328aef1c)
#### Tuesday 2022-01-18 14:19:23 by Benjamin Schachter

[web] [15/n] add some base css utils

Summary:
This might be better to have as a conversation if there are strong opinions. I started grabbing functional utility classes that we need from https://github.com/basscss/basscss. The reason I didn't grab the library from NPM is:

- there isn't any documentation for grabbing the classes we need. (flex, text-align, etc.)
- there's a bunch of CSS we don't need and I didn't want to start configuring webpack with CSS purge.
- It's a really easy way for a developer at a glance to know which utility classes we have so they don't need to duplicate code.
- base's final release was a couple of years ago and there aren't plans to change it. They're just CSS classes.

(Note, I didn't add everything we need just yet because this is a rather large change to how we've been doing things and I want to know you're opinions)

base was the pre-cursor to tailwind and other CSS utility framework classes.

So, why not tailwind?
- I don't want to spend the time configuring it when most of what we need is in base.
- We have our own style guide that doesn't look like tailwind or match its spec.
- It's a bit more of a learning curve IMO.

So, why do it this way at all?

- I wanted to show y'all what I was thinking and how I've written larger CSS projects that don't use CSS-in-JS. We did this at https://rundexter.com about 5 years ago before CSS-in-JS took off. Their design style guide used basecss's defaults for the most part and overwrote what didn't fit. In general, I think this is a valid approach but isn't great. It makes understanding our CSS at glance possible in just the component and is highly composable. We end up getting a consistent system where 90% of repeated styles can be expressed in functional classes and mostly bespoke CSS modules are needed.

Alternative:
- Is to use a CSS-in-JS solution like styled or emotion. For the record, I'd use something like https://vanilla-extract.style, but flow. If you want to see this design system in action check out mirror: https://github.com/mirror-xyz/degen
- We'd have strict typing and auto complete.
- We'd just import components like `<Layout.Row align="center">Hello</Layout.Row>`, rather than repeating classes repetitively.
- It's super easy to find dead code we don't use with eslint, prune and flow.
- It comes at a perf cost. CSS-in-JS libs ship with a run time.
- We could possibly share components with native. But, also perf. I can't find it but someone at rainbow had a good tweet about using styled. I'm assuming they're using vanilla extract since the author of the library works on design systems at rainbow.
- Theming is super easy.

Just for the record I think both approaches are valid, I don't have a hard bias for either. Additionally, if anyone else has a different approach they'd want to take. From what I see it looks like the community has embraced CSS-in-JS. Tailwind is pretty incredible esp. with autocomplete support in vscode. Base doesn't have auto-complete but is still a great mental model to work with.

Test Plan: N/A

Reviewers: atul, ashoat

Reviewed By: atul, ashoat

Subscribers: ashoat, palys-swm, Adrian, atul, karol-bisztyga, boristopalov

Differential Revision: https://phabricator.ashoat.com/D2805

---
## [aws/aws-cdk](https://github.com/aws/aws-cdk)@[c071367def...](https://github.com/aws/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Tuesday 2022-01-18 14:21:40 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [ivan123-ru/ivan123s-website-new](https://github.com/ivan123-ru/ivan123s-website-new)@[9ee5943069...](https://github.com/ivan123-ru/ivan123s-website-new/commit/9ee5943069d301e42cb3294205f5dcdfe1eba2d9)
#### Tuesday 2022-01-18 14:35:16 by ivan123

Formatting changes and replacing unnecessary objects

God bless "Format Document" button.
Also, i was retarded enough to fuck up when i was working with padding object. FML.

---
## [chris-pie/BotlerIsland](https://github.com/chris-pie/BotlerIsland)@[d4d595f796...](https://github.com/chris-pie/BotlerIsland/commit/d4d595f796307a592c9c3968905a2e5cc66be7a7)
#### Tuesday 2022-01-18 14:44:50 by virtuNat

Tentative batch command and react fix update

- Note to self: test all of this shit soon because why the fuck does react roles keep breaking????

---
## [gh-developing/daariou_photography](https://github.com/gh-developing/daariou_photography)@[42b8024846...](https://github.com/gh-developing/daariou_photography/commit/42b80248463d7757eb47fb1456ff24da935c2669)
#### Tuesday 2022-01-18 16:01:10 by Hannes Lüthi

This shit made me rage fr dude it almost took 3 hours to get 3 checkboxes there that change SIZE! DUDE WTF...... ready to die now

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[f2ebb21bd1...](https://github.com/microsoft/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Tuesday 2022-01-18 16:11:40 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[442432ea15...](https://github.com/microsoft/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Tuesday 2022-01-18 16:11:40 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [Zonespace27/goonstation](https://github.com/Zonespace27/goonstation)@[213b1fb1c9...](https://github.com/Zonespace27/goonstation/commit/213b1fb1c936cb95eace5cc4faac16cddc174eac)
#### Tuesday 2022-01-18 16:17:19 by Nexusuxen

AI Skins (#7129)

* wip
skins added
support for different skins added
- battmode & apcmode overlays
- readjust stun/bsod icon states to use overlays
setSkin proc also includes input validation to ensure only valid icons
medal+reward "Now you're thinking with portals!" dwaine skin
FUCK NPC AI WHY DO THE MARTIANS AGGRO ON SPAWN ARGHGHH

* mostly final changes
adds clown skin
further refactors to ai core frame layering
ai core sprites are now separate from the screen
blank screen now used for when the ai is depowered
(cant remember all the details, its been a while)

* tweaks
some desc adjusts
undid weird indentation(s)
removed unnecessary/outdated comments
1 -> TRUE
adds clown ai kit to geoff honkington's stock
(honk)

---
## [apache/couchdb](https://github.com/apache/couchdb)@[400f2a4259...](https://github.com/apache/couchdb/commit/400f2a42597857107093da54dd69a4ce9bdd82dd)
#### Tuesday 2022-01-18 16:29:14 by Adam Kocoloski

Refactor build to dynamically generate test stages

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

* Defaults to Erlang 24.2 as the embedded Erlang version in packages.

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

---
## [Blevruz/tgstation](https://github.com/Blevruz/tgstation)@[a2fa7799f3...](https://github.com/Blevruz/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Tuesday 2022-01-18 17:45:20 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[c2c13dd553...](https://github.com/clamor-s/u-boot/commit/c2c13dd553c13cba671525e38de6f8c4a44681e3)
#### Tuesday 2022-01-18 17:55:03 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [rossbar/numpy](https://github.com/rossbar/numpy)@[f435a33a06...](https://github.com/rossbar/numpy/commit/f435a33a060721c309adfd09c19e4cea5c080bb9)
#### Tuesday 2022-01-18 18:50:31 by Sebastian Berg

BUG: Fix that reducelikes honour out always (and live int he future)

Reducelikes should have lived in the future where the `out` dtype
is correctly honoured always and used as one of the *inputs*.
However, when legacy fallback occurs, this leads to problems because
the legacy code path has 0-D fallbacks.

There are two probable solutions to this:
* Live with weird value-based stuff here even though it was never
  actually better especially for reducelikes.
  (enforce value-based promotion)
* Avoid value based promotion completely.

This does the second one, using a terrible hack by just mutating
the dimension of `out` to tell the resolvers that value-based logic
cannot be used.

Is that hack safe?  Yes, so long nobody has super-crazy custom type
resolvers (the only one I know is pyerfa and they are fine, PyGEOS
I think has no custom type resolver).
It also relies on the GIL of course, but...

The future? We need to ditch this value-based stuff, do annoying
acrobatics with dynamically created DType classes, or something similar
(so ditching seems best, it is topping my TODO list currently).

Testing this is tricky, running the test:
```
python runtests.py -t numpy/core/tests/test_ufunc.py::TestUfunc::test_reducelike_out_promotes
```
triggers it, but because reducelikes do not enforce value-based promotion
the failure can be "hidden" (which is why the test succeeds in a full test
run).

Closes gh-20739

---
## [jasonrobot/cornhole-scorecard](https://github.com/jasonrobot/cornhole-scorecard)@[95325dfed2...](https://github.com/jasonrobot/cornhole-scorecard/commit/95325dfed206d4b9cfbef8818e8ad4dd23e6e195)
#### Tuesday 2022-01-18 19:10:22 by Jason Howell

fuck css, just fuck it to hell and back im sick of this fuck

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1860c8ca8d...](https://github.com/mrakgr/The-Spiral-Language/commit/1860c8ca8de51fb785152935f8741b0a901fbfbb)
#### Tuesday 2022-01-18 19:12:44 by Marko Grdinić

"12:35am. https://www.reddit.com/r/Houdini/comments/s42jzz/made_a_city_generator_tool/

Stuff like this is what I am interested in.

https://youtu.be/GxKfKvYu7VU?t=38
Plant Growing animation | Houdini Full Tutorial

Check out these flowers.

https://youtu.be/GxKfKvYu7VU?t=167

This is my first time witnessing Houdini in action. This is it! This is the kind of workflow that I want for the environment. Not necesarily for characters, but for the world itself, that is how I would want to express it.

https://youtu.be/GxKfKvYu7VU?t=235

Not having a quality parameter for scene was one of the pain points for me in Blender.

https://youtu.be/GxKfKvYu7VU?t=330

Let me stop here. I can't start watching this right now. I'll leave it for tomorrow. Let me get dinner and then go to bed.

https://youtu.be/SYz3Pz0m2XM
Render Houdini Particles with Blender CyclesX via Geometry Nodes

Another thing I will leave for later. I'll probably end up using both Blender and Houdini the way things are going.

1/18/2022

11:15am. I am thinking that why don't I make it my goal to do the second scene in Houdini?

11:30am. Let me stop reading that retarded /ic/ thread on tracing 3d, and watch something useful.

https://youtu.be/GxKfKvYu7VU?t=38
Plant Growing animation | Houdini Full Tutorial

Let me watch this for a bit. I found this vid yesterday night and it inspired me. The way I want to do the world is different from how I want to do the characters and I want to do that as procedurally as possible. i have the urge to push my ability to automate, and I think that Houdini's difficulty will turn out to be overstated. It has a reputation for being the most difficult of 3d tools, but most people who try to pick it up do not have apex programming skills.

https://youtu.be/GxKfKvYu7VU?t=153

I feel a lot of affinity for this kind of workflow. It seems Houdini works by taking a trace of all the actions which allows him to reconstruct his work step by step.

https://youtu.be/GxKfKvYu7VU?t=443

Houdini has potential for having good tutorials. Simply walking through the nodes like this would be a lot easier than making a vid from how to do things from scratch in Blender.

11:50am. Watched 10m. Enough of that. Let me start going through the Houdini is not scary series.

https://www.youtube.com/playlist?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isn't Scary: Beginner Series

> When I started Houdini a few years back, a lot of the tutorials were too advanced and assumed a certain level of knowledge.

That is the impression I got when I read those docs yesterday. But my 3.5 months of knowledge in Blender is just right to get into it.

11:55am. I am going to choose this goal and pursue it. Maybe I'll end up doing everything by hand in Blender in the end, but for now while I am still learning I want to push myself as much as possible. 3d art is a whole new world for me and I want to explore it first. The best way to get to the higher level in programming is to master a better language, and so it will be in art.

https://youtu.be/Tsv8UGqDibc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=373

I wonder why instead of having these different modes, couldn't you navigate like in Blender? I'll leave that mystery for later. Ah, it is possible to move around using the space bar. Makes sense.

12:25pm. https://youtu.be/Tsv8UGqDibc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=794

Houdini's UI design is quite impressive. For this way of scaling, I'd already give it points over Blender.

12:35pm. https://youtu.be/2VFFb4s_RSM?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isn't Scary - Part 2: Objects

Time for the second vid. So far, Houdini is impressive. I like the way it has been designed. I can clearly see that Blender is stealing ideas from it, especially when it comes to geo nodes. And this makes it a lot easier for me to relate to what I am doing in Houdini. Wonderful. Things could not be better.

In 2022 I am going to enter and master this domain thoroughly. If I can do that, when work on Heaven's Key starts, it is going to have impressive art indeed. I've been wanting it to do it in 2d, but given the lengths I am going to, maybe I could find a way to make 3d work? It hasn't been done so far, but the path I am going down is not a regular one.

Why not make it in 3d? I do not have a good answer to that. I guess, when I get good at it I'll know why and whether.

Now let me start the donut tutorial.

12:50pm. https://youtu.be/2VFFb4s_RSM?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=146

The above video is from 2 years ago, and it seems the mountain node changed significantly. At any rate, the amplitude option is obvious enough, so all I had to do was lower it.

https://youtu.be/2VFFb4s_RSM?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=1461

I do not understand why changing the up options has no effect.

Hmmm, I think that...no, I've confirmed that you need to attribute create first for `pscale`. Then, does `up` exist as a vector of 1s and just get set to whatever the randomize attribute does. But in that case I should see some difference when adding.

Ah, no, I do. Where I do not see a difference is when multiplying. That means it is just 0s under the hood.

Ok, I see it.

2:05pm. Let me stop here, I am long overdue for breakfast. Blender got rid of attributes in favor of fields, but it is really hard to program without variable bindings.

https://youtu.be/F2rj31YXaCQ?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isn't Scary: Part 3 - Dynamics

Just had to finish the video. I'll resume from here after breakfast.

3:15pm. Done with breakfast and chores.

I've just noticed it, but the logo for Houdini is literally a spiral. Great minds think alike.

3:35pm. Done with the oranges. Let me resume.

Time for part 3.

3:55pm. https://youtu.be/F2rj31YXaCQ?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=572

I feel this streamlines what Blender is doing by a lot. Blender's design reminds me a lot of Cython in that a lot of stuff has been added haphazardly and there are limitation all over the place as a result. While Houdini has an overarching principle it is tapping into. It is a funtionaly pure, reactive language at its core.

https://youtu.be/F2rj31YXaCQ?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=743

This is it! I really like this. This is so much more convenient that having a bunch of global forces like in Blender.

4:50pm. https://www.youtube.com/watch?v=XZiDLTthieU&list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&index=4
Houdini Isn't Scary - Part 3 And a Bit: FAQ

It is quite late already. I've been quite into it so far.

Let me watch part 3.5.

5:15pm. I need a break, let me finish the video and I will have one.

https://youtu.be/Xz2hR9vl0GY?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isn't Scary - Part 4: Lights Camera Icing

Let me pause here. I need a break.

5:20pm. Phew, getting used to Houdini will take a while. I am just about used to Blender. I was on the verge of establishing my workflow as well, but instead I decided to explore more. So far, I really like it. But I'll want to do something real to get a sense for it. This will take me some time. But if I am happy with it, I'll stick with it for generating scenes.

5:40pm. Let me resume. I want to finish the first part of the series today.

5:55pm. https://youtu.be/Xz2hR9vl0GY?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=222

Oh, you can set the area light like this? This is nice.

6pm. I don't know why, but sprinkles are showing up as spheres instead of actual colored tubes in render. I'll leave this mystery for later.

6:10pm. Time for lunch.

6:25pm. Let me resume.

6:45pm. Houdini's principled shader has so many options compared to the Blender one it is insane. It would be very intimidating if I did not understand that most of them I do not need to concern myself with.

7:05pm. https://youtu.be/a6rR1iOZ0tQ?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W

Here is part 5. I am tired, but let me go through it.

https://youtu.be/a6rR1iOZ0tQ?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=306

I wonder if Matra uses the GPU automatically.

https://youtu.be/a6rR1iOZ0tQ?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=370

Remember the last chapter's One Punch Man page with the god? This scene with the flowers looks much like it minus the giant zombie in the background.

Mantra is so slow, it has almost been 5m and it is still rendering the donut.

7:45pm. https://youtu.be/NjtlYXRgqWc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isn't Scary Project - Part 1: Intermediate Objects

Let me stop here.

7:50pm. Houdini really has too much stuff in it. I wonder if it has a modeling mode like in Blender? I'll figure it out as I go along.

Towards the end of the last tutorial, it really bothered me how I had to move the objects around. Couldn't it have been possible to simply tune the depth of field itself instead?

7:55pm. I am too tired to watch anymore. Tutorials are fun at first, but get tedious towards the end. Still I have a bunch more left to do before I am done with the beginner's series. I should be able to clear it tomorrow. After that I'll get to work on modeling that football.

A big priority for me is how to immitate modeling in the way I am used to in Blender. From what I've heard, Blenderi s particularly good at that, but what it does is so basic that Houdini should be capable of it as well. I need to buckle down.

Despite how long I've been at it, I've only did 10% of the scene maybe. I could do it all in a few days had I decided to do it all by hand, but instead I am spending time trying to automate my process and it is taking me weeks. Well, let it take that long. I need these skills if I am going to do the kind of work it would take an entire team of traditional artists in the same amount of time. I need to express my desire through programming. I need to get better at this if I am going to have a future.

The poker plan failed, so I'll just have to make the money to pursue AI with my own two hands.

It is fine if it takes me a few weeks of constant study to go through all the Houdini learning materials. Just how much time did I waste learning how to program? Too much, and so it will be with art. If I can master 3d, I will have established my foundation."

---
## [luckyr13/arcode](https://github.com/luckyr13/arcode)@[96a654d29e...](https://github.com/luckyr13/arcode/commit/96a654d29e3db31e2fcc8d478738edf045c7dc6b)
#### Tuesday 2022-01-18 20:32:14 by technodromex

Update arweave wallet connector

At this point I really love what we have done here, amazing collaborations. Thanks God!

---
## [christopherlandry/crawl](https://github.com/christopherlandry/crawl)@[070a2a64fb...](https://github.com/christopherlandry/crawl/commit/070a2a64fb29b2c910b5e7a89e561f090fa03f63)
#### Tuesday 2022-01-18 21:38:18 by Kate

Allow demons and holies to be feared/berserked

As part of an effort to reduce the number of effects that are restricted
to natural monsters only, to increase some of the distinctions between
undead/demonic/nonliving holinesses, and to allow some more flavourful
interactions.

Lore-wise, demons and holies are supposed to be of similar stock aside from
their god alignment, so are grouped together here. They're also established
to be like living creatures in a number of ways - they're generally
intelligent, can be poisoned, and have souls, so it feels appropriate for
them to feel emotions in some way and be able to go berserk and be feared.
(Importantly this also allows the zealot's sword to send divine allies
berserk, for any TSO worshippers who happen to find it.)

---
## [ElpidioL/Go](https://github.com/ElpidioL/Go)@[eca79897c2...](https://github.com/ElpidioL/Go/commit/eca79897c29c47598de0f3399646195ebbbc84c5)
#### Tuesday 2022-01-18 21:42:04 by ElpidioL

0.1.3

A new weird feature connecting to League of Legends API to annoy my friends, its really bad designed rn, but I'm still thinking how to keep track of a lot of players, probably a DB later.
But for now it just annoys one of my friends whenever he starts a match.

---
## [SgtHunk/fulpstation-1](https://github.com/SgtHunk/fulpstation-1)@[2c26158a6e...](https://github.com/SgtHunk/fulpstation-1/commit/2c26158a6effcc7f90e61514dbc471ce66683539)
#### Tuesday 2022-01-18 21:59:06 by SgtHunk

fuck you john wilard

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Nobelium-XVIII/fulpstation](https://github.com/Nobelium-XVIII/fulpstation)@[c797bf79ea...](https://github.com/Nobelium-XVIII/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Tuesday 2022-01-18 22:23:37 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[6f4de45a22...](https://github.com/Buildstarted/linksfordevs/commit/6f4de45a22df2a6ad17a85ffb06368c30e884620)
#### Tuesday 2022-01-18 23:06:07 by Ben Dornis

Updating: 1/18/2022 11:00:00 PM

 1. Added: How to Ship Software Faster
    (https://joshghent.com/ship-faster/)
 2. Added: Wordle to yaml
    (https://katydecorah.com/code/wordle-to-yaml/)
 3. Added: High Modernism & Software Design
    (https://www.michaelbromley.co.uk/blog/high-modernism-software-design/)
 4. Added: Nomad Tips and Tricks
    (https://danielabaron.me/blog/nomad-tips-and-tricks/)
 5. Added: Load Testing at Scale and Lessons Learned
    (https://www.kevinlondon.com/2022/01/14/load-testing-guide)
 6. Added: The problem of de-synchronized metronomes
    (https://nicolo.dev/blog/metronomes-synchronization/)
 7. Added: The Internet Dream | Ramen Potential
    (https://ramenpotential.com/the-internet-dream)
 8. Added: FBI document shows what data can be obtained from encrypted messaging apps
    (https://therecord.media/fbi-document-shows-what-data-can-be-obtained-from-encrypted-messaging-apps/)
 9. Added: GitHub - YousefED/Matrix-CRDT: Use Matrix as a backend for local-first applications with the Matrix-CRDT Yjs provider.
    (https://github.com/YousefED/Matrix-CRDT)
10. Added: I Quit My Job and Took a Huge Pay Cut To Stop Using PowerPoint
    (https://www.sofuckingagile.com/blog/i-took-a-huge-pay-cut-so-i-could-get-away-from-powerpoint)
11. Added: How to use Org Mode and Hugo for a better scientific blogging – STRM
    (https://strm.sh/posts/org-mode-blogging/)
12. Added: The Horizon Problem for Faster than Light Travel
    (https://eriklentzphd.blogspot.com/2022/01/the-horizon-problem-for-faster-than.html)
13. Added: Computer Scientist Explains One Concept in 5 Levels of Difficulty | WIRED
    (https://www.youtube.com/watch?v=fOGdb1CTu5c)

Generation took: 00:05:54.9626613
 Maintenance update - cleaning up homepage and feed

---

