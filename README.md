## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-17](docs/good-messages/2022/2022-05-17.md)


1,795,065 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,795,065 were push events containing 2,908,000 commit messages that amount to 210,470,136 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[cd1b891d79...](https://github.com/OliOliOnsiPree/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Tuesday 2022-05-17 00:27:28 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [codelipenghui/incubator-pulsar](https://github.com/codelipenghui/incubator-pulsar)@[81cbc96005...](https://github.com/codelipenghui/incubator-pulsar/commit/81cbc960055c1480072308b776ce15ac055c237c)
#### Tuesday 2022-05-17 01:19:07 by feynmanlin

Fix hasMessageAvailable return true but can't read message (#10414)

### Motivation

I temporarily fixed this problem in PR https://github.com/apache/pulsar/pull/10190.
Now we have found a better way, this way can avoid the seek, then avoid trigger another reconnection.
Thank you @codelipenghui  to troubleshoot this issue with me all night.

We have added a lot of log and found that this issue is caused by some race condition problems. Here is the first reason:
https://github.com/apache/pulsar/blob/f2d72c9fc13a33df584ec1bd96a4c147774b858d/pulsar-client/src/main/java/org/apache/pulsar/client/impl/ConsumerImpl.java#L1808-L1818
Now we have an acknowledgmentsGroupingTracker to filter duplicate messages, and this Tracker will be cleaned up after seek.

However, it is possible that the connection is ready and Broker has pushed message, but `acknowledgmentsGroupingTracker.flushAndClean(); ` has not been executed yet. 

Finally hasMessageAvailableAsync returns true, but the message cannot be read because it is filtered by the acknowledgmentsGroupingTracker


### Modifications
clean the tracker when connection was open

### Verifying this change


(cherry picked from commit f69a03b28d29689eaf910e0b99994fa250adb213)

---
## [SylvainTran/speculative-futures-project-2](https://github.com/SylvainTran/speculative-futures-project-2)@[44acfcf44b...](https://github.com/SylvainTran/speculative-futures-project-2/commit/44acfcf44b3536fafed8187096c8420e73e2aeea)
#### Tuesday 2022-05-17 02:08:25 by SylvainTran

[KDM!] Added Website Companion Fake CBT E-Learning Web Interface with Unity Embeds Prototype

[KDM!] I wanted to experiment and create an alternative perspective for the project
using web technologies. In this prototype, I want to see if big constraints on the tooling can help create interesting creative solutions. Another point is that I know from previous research that a web companion site is useful/standard for CBT related applications and games, so why not strike two problems in one shot! Besides, Unity can always be integrated as a library (i.e., Unity as a Library) inside the same web page, which I think makes more sense performance-wise and is vastly more developer friendly given its powerful and safe C# language, 2D/3D editor and complete set of game tools, compared to any other solution such as Three.js/A-Frame/Phaser.js?

Anyways, the design question to answer is, "How can I use a web companion for this CBT Game?" implying the technical question of, "How do I integrate/embed Unity experiences in a webpage and make the whole thing feel harmonious and... united? To use the web + unity to make stories/experiences" is the attempt here. The result of this commit: I've done a basic "E-Learning System" layout using React.js which simulates stepping in other people's skin to live particular experiences, in the context of a Learning Pathway (in this case, CBT). I used language to make it sound serious in the software itself, which makes the whole thing somewhat feel "real" (that's definitely odd)? Using my own experiences doing Unity's learning pathway and millions of other online
courses like Udemy, SkillShare, Domestika, the current layout and website structure seemed like a satisfying and correct approach. I've also used my own portfolio website structure to subvert into this strange futuristic machinery that I almost immediately wanted to call "MentalRay". It seems easy to free-flow into selecting content items and contextualize them with the game's world. I've also added a few "user contributed stories" from a fictional "Frag.Net", where people just drag and drop / upload some of their life experiences using advanced 360/Real World Capture data that gets converted neatly into a playable Unity game. This will exist in the near future if trends with VR continue.  Remains to integrate Unity embeds in the proper sections now.

---
## [ThePainkiller/sojourn-station](https://github.com/ThePainkiller/sojourn-station)@[796aeaa98f...](https://github.com/ThePainkiller/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Tuesday 2022-05-17 02:13:29 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [libretro/mame2003-plus-libretro](https://github.com/libretro/mame2003-plus-libretro)@[fecf11dfbd...](https://github.com/libretro/mame2003-plus-libretro/commit/fecf11dfbdf77f24dc20531d5bc489c5ec9fb80f)
#### Tuesday 2022-05-17 03:12:53 by Kyland K

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
## [riggtravis/keybert](https://github.com/riggtravis/keybert)@[f51ddc8f3a...](https://github.com/riggtravis/keybert/commit/f51ddc8f3a2a7797b9260c1e7a37970081eb812a)
#### Tuesday 2022-05-17 04:07:37 by Travis W Rigg

feat: enforced good board geometry using FreeCAD

Parametric modeling is a wonderful thing and I'm unclear on why
KiCAD doesn't have it. Oh well, it is what is is. Using the
dimensions I obtained from the wonderful experience of performing
my parametric modeling adjustments, I finally had all of the
information I needed to get pricing for the PCBs as they are
currently designed. The results were not good. Currently,
[Aisler](https://aisler.community/t/pcb-design-rules/41) rates the
design as complex. This fails to meet the mission goal of Keybert
in a couple of ways.

Firstly, a complex PCB is an expensive PCB and an expensive PCB is
not beginner friendly. Secondly, a complex PCB is a harder to
understand and evaluate PCB and a harder to understand and evaluate
PCB is a PCB that doesn't help a biginner wrap their heads around
the sorts of decisions are present in the general world of custom
mechanical keyboards. Also, as an open source project, I feel a
certain degree of responsibility to make sure that this is as easy
to remix and remaster as possible. I look at the ecosystem left by
wootapoot and am so glad that the Let's Split was open sourced.
That board was a wonderful and excellent board, but the original
creator has seemingly vanished. I want when I stop being available
to support Keybert for Keybert to be able to venture out into the
world supported by many, just like the Let's Split lives on and
even has inspired things like the Lundquist and Let's Tango

chore: tidy up repository

Look at this place! Look at this mess! This isn't easy to understand or
explore! What are we even doing here!?

---
## [kylehaidar/odin-recipes](https://github.com/kylehaidar/odin-recipes)@[aa576ef62f...](https://github.com/kylehaidar/odin-recipes/commit/aa576ef62f23f3b608fa67ed7cc33d87e9809a11)
#### Tuesday 2022-05-17 04:44:07 by kylehaidar

Update README.md

Okay, so clearly I am not a good coder, but I tried to utilize everything I have been taught so far in order to complete this project, I added my favorite foods, and honestly, I dont care what anyone says, I am so happy with it, I feel like im making true progress and at this point this is more of a journal entry.
It feels good to like, idk, complete it you know, its so nice to have worked so hard on something, and for it to be completely done.
Anyway, back to the coding part, I utilized unordered and ordered lists in order to present the ingredients and the steps, I used some text things like making things bold and italiziced (fuck idk how to spell) and I used hyperlinks and normal links, overall, I geniunely had a great time doing this, i like this.

---
## [Faseehurrehman04/websites](https://github.com/Faseehurrehman04/websites)@[4f7458ec4f...](https://github.com/Faseehurrehman04/websites/commit/4f7458ec4f855cdb4d58cf40a47223609a8435e5)
#### Tuesday 2022-05-17 07:24:13 by Faseeh Ur Rehman

Why You Need Professional Website Development and SEO Services

If you’re reading this, you probably already know that SEO and website development are essential components of any good business strategy. But do you know how to find trustworthy SEO and website development services? How do you know when it’s time to switch from the little guy to the big guns?
 
If you don’t have a website
If you’re starting a business, you need a website. People search online before they commit to spending money on anything; if you don’t have a presence for your business, potential customers are likely to just move on. Without a website, you have no way of making an impression; without one, you have no way of reaching out to current or future clients. We make websites that are responsive — you don’t have to worry about visitors having trouble with your site from their phones or tablets. If that’s not enough, we can optimize your site for search engines so that people will find it when they search for relevant keywords. We make it easy for you — just tell us what kind of website makes sense for your business (e-commerce?
If you don’t have an online presence
An online presence is vital for any business, especially if you’re trying to reach a wider market. If you’re serious about increasing your sales, growing your customer base, and improving your reputation with new prospects who find you online — you need professional services that can help streamline processes like Social Media Management, Virtual Assistant Management, email marketing campaigns, and website design & development so you can focus on what matters most: getting new customers. For example, it takes time to keep up with Facebook posts and tweets, but an experienced social media manager can schedule posts in advance and manage several social accounts at once. It also takes time to draft emails for promotional campaigns or newsletters (and then send them out) but a virtual assistant can take care of that process for you too! The bottom line? Investing in professional services will save you time so you have more hours in your day to work on building relationships with existing customers or finding new ones!
How much does it cost?
When starting your business, it is important to ask yourself how much you are willing to spend. It might seem daunting to begin a new venture with such a large question lingering over your head. However, starting up isn’t as scary as it sounds when you break it down into manageable steps. After all, there are many different ways to save money on any given service or good. It is more of just doing the research needed in order to make sure that you aren’t spending too much money on things that can be done cheaply or for free. Business website cost vary depending on what kind of site you want, but generally speaking creating a great looking site will cost about $1000 for its creation and about $100 per month for hosting services.
Who is responsible for what?
Most companies have at least one person responsible for maintaining each of their company’s social media accounts. But who is in charge of overall content writing? If there is no dedicated writer, it’s up to people with other job descriptions to produce content when they have time or energy to do so. While one member of your team may be better than another at creating engaging content, it is ideal to have someone as your go-to person for all things blogging.
We make a website on WordPress for you
WordPress is a platform that powers millions of websites around the world. It’s easy to use, free, popular, powerful, and has one of best support communities online. WordPress comes with built-in SEO functionality, in addition to its more than 500+ plugins that provide additional functionality. No matter what your business or website needs are, you can find a plugin that meets those needs. If you can’t find it — then chances are you need professional website development help! That’s why Faseeh Ur Rehman offers professional website development services in addition to our content writing & platform services such as graphic design & eCommerce services.
We do SEO of your website
Websites built on WordPress, which is one of the most popular Content Management Systems (CMS) in existence, aren’t SEO-friendly out of the box. Without SEO-friendly web design, it’s impossible to bring high rankings in search engines like Google. If you want your website to be found by potential customers, then you need SEO. Faseeh Ur Rehman is a professional website development company that specializes in creating fully functional and user-friendly websites for every budget. Our company understands how powerful a great website can be for any business; don’t settle for anything less than a custom site built with WordPress from Faseeh Ur Rehman.
We write content for your website 
Getting traffic to your website is hard work. It’s even harder when you have a confusing website design or outdated content. Let our professional writing team help. Our writers can create compelling, easy-to-read content that attracts new visitors and keeps them coming back for more. And we don’t just write about your business or your product; we also research key topics that matter to your customers, which means even more targeted traffic. How? We’ve got some tricks up our sleeves — that’s what we do here at Faseeh Ur Rehman, after all! — but for starters, give us a call and ask about our premium service options for content writing. Our talented team will get you on track in no time!
We increase your WordPress website speed
Nothing is more frustrating to a user than waiting around for your WordPress website to load. These days, users don’t care if you have a million page views per month — they only care about how fast your site loads. Speed affects everything from bounce rates to conversion rates. You need a professional SEO-focused team with proven methods of increasing speed on WordPress sites in order to stay competitive in 2019 and beyond. Faseeh Ur Rehman has years of experience on all things related to WordPress websites — including custom development solutions, speed optimization, quality content creation and more!
We make an E-Commerce website for you
An E-Commerce website allows your business to create an online store where customers can purchase products or services. We build fully optimized e-commerce stores for businesses in a variety of industries. Whether you want to sell existing products through an existing business, or would like us to help you design and produce unique products specifically for sale online, we are happy to provide assistance. Additionally, if you already have an E-Commerce site but it isn’t attracting visitors, we can help with strategies that will drive more traffic to your website. So contact us today! We look forward to working with you!
About Faseeh Ur Rehman
 
Faseeh Ur Rehman is a Professional Website Development, SEO, And Content Writing Services Platform. Here we will provide you services of WordPress Website Development, SEO, Content Writing, And many more services.
Our Mission
We’re dedicated to providing you the best in Website Development, SEO, And Content Writing Services, with a focus on dependability and Best Website developer, SEO Expert, and Content Writer.
What We Do
•	Website Development On WordPress
•	Social Media Account Handling
•	E-Commerce Store On WordPress
•	SEO OF websites
•	Content Writing
•	Increase DA
•	Increase DR

---
## [williamcll/Skyrat-tg-cn](https://github.com/williamcll/Skyrat-tg-cn)@[f6ce903dea...](https://github.com/williamcll/Skyrat-tg-cn/commit/f6ce903deade160357e23b927d376851f0dbdd2c)
#### Tuesday 2022-05-17 09:33:34 by SkyratBot

[MIRROR] Makes glass floors override platings. Fixes glass floor openspace bug. [MDB IGNORE] (#13226)

* Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

* Makes glass floors override platings. Fixes glass floor openspace bug.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [mekstrem/metallb](https://github.com/mekstrem/metallb)@[bf9b2aee7d...](https://github.com/mekstrem/metallb/commit/bf9b2aee7dbafe4d63ed01601f2b5f9ec1cafb5b)
#### Tuesday 2022-05-17 09:57:59 by Rodrigo Campos

website: Fix style in 0.9.2 release notes

This commit fixes the style so the paragraph is not dedented and the
next item is not shown in the same line.

The first issue is "fixed" by just making it one paragraph, as no other
alternatives were found that worked correctly in hugo 0.57.0 (didn't
explored ugly hacks like manually indent, etc.).

The second issue (item in the wrong line) was reproduced locally with
hugo 0.57.0. It didn't happen with other newer hugo versions (tested
several >= 0.62.2 versions), however this patch is rendered correcly on
new and old hugo versions.

This patch was tested with hugo 0.57.0, as this was the only version I
found to render the site locally as similar as possible to the current
website. In particular, it renders the site with the horrible black
thing rendered when written like this[1], and properly includes the site
header logo (is not shown with newer hugo versions). However, some other
changes might be required if the production site is rendered using
another hugo version.

Fixes: #548

[1]: https://github.com/metallb/metallb/commit/2d0cbd89bd71298f55372c168365acec711dc3f2#diff-3c4a3af03bacf924a0523da3eb3ec9bdR18

---
## [ev-ev/tmnf-rpe](https://github.com/ev-ev/tmnf-rpe)@[7b52765d52...](https://github.com/ev-ev/tmnf-rpe/commit/7b52765d521fb0d13213f4521bcb9310ebe7f2fa)
#### Tuesday 2022-05-17 10:01:58 by Evgeny

read the fucking header. implemented lookupstring, literally the most braindead thing ever oml, 3 hours of my life gone

---
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[71cbca3021...](https://github.com/input-output-hk/ouroboros-network/commit/71cbca30215c827117425b8f082038b34a390109)
#### Tuesday 2022-05-17 10:21:14 by Nicholas Clarke

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
## [EdenKupe/anarchysf](https://github.com/EdenKupe/anarchysf)@[161e3f13bd...](https://github.com/EdenKupe/anarchysf/commit/161e3f13bd27d89521b5f0170b3ea4c9f7534a36)
#### Tuesday 2022-05-17 11:15:51 by Ben-Beck

Create 001150 Rachel Pollack.md

Pollack was the subject of a <a href="https://www.fifthestate.org/archive/380-spring-2009/rachel-pollack-willing-change-everything/">profile article</a> by Cara Hoffman, in _Fifth Estate_ #380. She notes that:

"Her work is often concerned with what is below the surface of everyday matters, what happens when the life of the mind and the concerns of the material world converge.

"This makes Pollack’s work not only transcendent, but often very funny. As in _Unquenchable Fire_, where God appears in the form of a chocolate chip cookie salesman on Seventh Avenue, and is then perceived to be out of touch with the experiences of mortals, and therefore insane."

---
## [force-push-kernel/stalker](https://github.com/force-push-kernel/stalker)@[b4c069a5b6...](https://github.com/force-push-kernel/stalker/commit/b4c069a5b64600298e190e395993e4f634fecd43)
#### Tuesday 2022-05-17 12:28:21 by Peter Zijlstra

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
Signed-off-by: Souljacker1 <sameerpyo39@gmail.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cbc9279eaa...](https://github.com/odoo-dev/odoo/commit/cbc9279eaa169e65aeb2dab6dd36e3ffab4e481e)
#### Tuesday 2022-05-17 12:35:11 by Odoo's Mergebot

[MERGE] im_livechat: introduce chatbot scripts

PURPOSE

This commit introduces a chatbot operator that works based on a user-defined
script with various steps.

SPECS

A im_livechat.chatbot.script can be defined on a livechat rule.
When a end-user reaches a website page that matches the rule, the chat window
opens and the script of the bot starts iterating through its steps.

The chatbot code is currently directly integrated with the existing livechat
Javascript code.
It defines extra conditions and layout elements to be able to automate the
conversation and register user answers.

AVAILABLE STEPS

A script is defined with several steps that can currently be one of the
following types:

"text"

A simple text step where the bot posts a message without expecting an answer
e.g: "Hello! I'm a friendly robot!"

"question_selection"

The bot will ask a question and suggest answers, the end-user will have to
click on the answer he chooses
e.g: "How can I help you?
  -> Create a Ticket
  -> Create a Lead
  -> Speak with a human"

"question_email"

That step will ask the end user's email address (and validate it)
The result is saved on the linked im_livechat.im_livechatchatbot.mail.message

"question_phone"

Same logic as the 'question_email' for a phone number
We don't validate the input this time as it's a complicated process
(requires country, ...)

"forward_operator"

Special type of step that will add a human operator to the conversation when
reached, which stops the script and allow the visitor to discuss with a
real person.

The operator will be chosen among the available operators on the
livechat.channel.

If there is no operator available, the script continues normally which allows
to automate an "answering machine" that will redirect the user in case no
operator is available.

e.g: "I'm sorry, no operator is available right now, please contact us by email
at 'info@company.com', we will try to respond as soon as possible!".
(Or even something more complex with multiple questions / paths).

"free_input_single"

Will ask the visitor for a single line of text.
This text is not saved anywhere else than in the conversation, but it's still
useful when combined with steps that create leads / tickets since those print
the whole conversation into the description.

"free_input_multi"

Same as "free_input_single" but lets the user input multiple lines of text.
The frontend implementation is made by waiting a few seconds (currently 10) for
either the next submitted message or the next character typed into the input.

This lets visitors explain their issue / question with multiple messages.
Which is very useful since new messages are sent every time you press "Enter".

"create_lead"

Special step_type that allows creating a crm.lead when reaching it.
Usually used in addition to 'question_email' and 'question_phone' to create
interesting leads.

LINKS

Task-2030386

closes odoo/odoo#84000

Related: odoo/enterprise#24894
Signed-off-by: Thibault Delavallee (tde) <tde@openerp.com>
Co-authored-by: Patrick Hoste <pko@odoo.com>
Co-authored-by: Aurélien Warnon <awa@odoo.com>

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[de7e66b921...](https://github.com/canalplus/rx-player/commit/de7e66b921dc8c803cafd38b4d25bd1c9c82d777)
#### Tuesday 2022-05-17 12:39:40 by Paul Berberian

HTMLMediaElement's related error have now the initial message if it exists

I was very shamefully not aware that `MediaError`s as emitted by
HTMLMediaElement could have a `message` property describing the actual
problem.

For my defense, this was not always the case for MediaErrors (I found
some w3c and chrome links to prove it!).
Yet it apparently is since 2017, so my defense is still pretty weak.

Relying on those could definitely have saved us many hours of debugging
over the years, where we were trying to find which segment of which
type provoked a MEDIA_ERR_DECODE and why.

Anyway, I prefer not to think to much about it, here it is, and now it's
available: the corresponding error message will actually be the message
of the corresponding `RxPlayer`'s `MediaError`'s message (yes, both the
native browser error and the RxPlayer supplementary layer have the
exact same name, and no, it cannot be a source of confusion at all, why
would you say that?).

---
## [SabreML/Pariah-Station](https://github.com/SabreML/Pariah-Station)@[23aef65ad5...](https://github.com/SabreML/Pariah-Station/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Tuesday 2022-05-17 13:00:25 by SabreML

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607) (#704)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [hulthe/linux](https://github.com/hulthe/linux)@[213d266ebf...](https://github.com/hulthe/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Tuesday 2022-05-17 13:25:47 by Linus Torvalds

gpiolib: acpi: use correct format characters

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

---
## [SuperSpaceEye/TheLifeEngineCpp](https://github.com/SuperSpaceEye/TheLifeEngineCpp)@[e9c77a4894...](https://github.com/SuperSpaceEye/TheLifeEngineCpp/commit/e9c77a489419cd2bd9f7fb28d6f2f58220f48822)
#### Tuesday 2022-05-17 16:44:51 by spaceeye

YES!!! FUCKING YES!!! IT IS WORKING! HELL YEAH!!!!

---
## [bautrey37/opentelemetry-ruby](https://github.com/bautrey37/opentelemetry-ruby)@[45429c7d53...](https://github.com/bautrey37/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Tuesday 2022-05-17 16:52:33 by Andrew Hayworth

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
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[65361947a3...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/65361947a3a69cc854185ba869b34398f8a53c49)
#### Tuesday 2022-05-17 17:06:33 by AmyBSOD

Dual-wielding guns

Due to the SLASH'EM design team not caring about game balance in the slightest, I have to change their stuff such that it becomes balanced... (also fuck you whoever states that slex is supposedly unbalanced, because it's not :-P)

---
## [rust-lang/rust-analyzer](https://github.com/rust-lang/rust-analyzer)@[1a5925dc84...](https://github.com/rust-lang/rust-analyzer/commit/1a5925dc84d0ef966023d6612147f93a0464174c)
#### Tuesday 2022-05-17 18:50:03 by bors

Auto merge of #12294 - listochkin:prettier, r=Veykril

Switch to Prettier for TypeScript Code formatting

## Summary of changes:

 1. Added [`.editorconfig` file](https://editorconfig.org) to dictate general hygienic stuff like character encoding, no trailing whitespace, new line symbols etc. for all files (e.g. Markdown). Install an editor plugin to get this rudimentary formatting assistance automatically. Prettier can read this file and, for example, use it for indentation style and size.
 2. Added a minimal prettier config file. All options are default except line width, which per [Veykril](https://github.com/Veykril) suggestion is set to 100 instead of 80, because [that's what `Rustfmt` uses](https://rust-lang.github.io/rustfmt/?version=v1.4.38&search=#max_width).
 3. Change `package.json` to use Prettier instead of `tsfmt` for code formatting.
 4. Performed initial formatting in a separate commit, per [bjorn3](https://github.com/bjorn3) suggestion added its hash to a `.git-blame-ignore-revs` file. For it to work you need to add a configuration to your git installation:
    ```Shell
    git config --global blame.ignoreRevsFile .git-blame-ignore-revs
    ```
 5. Finally, removed `typescript-formatter` from the list of dependencies.

----
What follows below is summary of the discussion we had on Zulip about the formatter switch:

## Background

For the context, there are three reasons why we went with `tsfmt` originally:
* stick to vscode default/built-in
* don't add extra deps to package.json.lock
* follow upstream (language server node I think still uses `tsfmt`)

And the meta reason here was that we didn't have anyone familiar with frontend, so went for the simplest option, at the expense of features and convenience.

Meanwhile, [**Prettier**](https://prettier.io) became a formatter project that JS community consolidated on a few years ago. It's similar to `go fmt` / `cargo fmt` in spirit: minimal to no configuration to promote general uniformity in the ecosystem. There are some options, that were needed early on to make sure the project gained momentum, but by no means it's a customizable formatter that is easy to adjust to reduce the number of changes for adoption.

## Overview of changes performed by Prettier

Some of the changes are acceptable. Prettier dictates a unified string quoting style, and as a result half of our imports at the top are changed. No one would mind that. Some one-line changes are due to string quotes, too, and although these a re numerous, the surrounding lines aren't changed, and git blame / GitLens will still show relevant context.

Some are toss ups. `trailingComma` option - set it to `none`, and get a bunch of meaningless changes in half of the code. set it to `all` and get a bunch of changes in the other half of the code. Same with using parentheses around single parameters in arrow functions: `x => x + 1` vs `(x) => x + 1`. Perrier forces one style or the other, but we use both in our code.

Like I said, the changes above are Ok - they take a single line, don't disrupt GitLens / git blame much. **The big one is line width**. Prettier wants you to choose one and stick to it. The default is 80 and it forces some reformatting to squish deeply nested code or long function type declarations. If I set it to 100-120, then Prettier finds other parts of code where a multi-line expression can be smashed into a single long line. The problem is that in both cases some of the lines that get changed are interesting, they contain somewhat non-trivial logic, and if I were to work on them in future I would love to see the commit annotations that tell me something relevant. Alas, we use some of that.

## Project impact

Though Prettier is a mainstream JS project it has no dependencies. We add another package so that it and ESLint work together nicely, and that's it.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2e4a92feb2...](https://github.com/mrakgr/The-Spiral-Language/commit/2e4a92feb25454366b59880f0a74ee7ead804839)
#### Tuesday 2022-05-17 18:56:41 by Marko Grdinić

"2:45pm. Let me resume.

https://youtu.be/PFLp_ekTdxw
[Speedpaint] Creating Manga Background From Photo.

This is 8m, let me watch it. Then I will check out some other things.

2:45pm. Nevermind it. Let me move on.

https://www.youtube.com/results?search_query=blender+manga
https://www.youtube.com/results?search_query=manga+shading

https://youtu.be/s5QZZJBuBbw
How To Shade Both In Anime/Manga & Realistic Drawings

Let me watch this. I need some shading tips.

3:05pm. https://youtu.be/s5QZZJBuBbw?t=646

Let me pause this here.

https://www.youtube.com/results?search_query=solo+leveling+art

I want to check out some of this. Though I do not expect much of it.

https://youtu.be/wZ7vRYTqPZI
Illustrator Reacts to Manga and Manhwa Art

https://youtu.be/wZ7vRYTqPZI?t=157

Yeah, it is very crisp and clean.

https://youtu.be/wZ7vRYTqPZI?t=243

This is something I've noticed a few minutes into the vid, just as he notes, rather than the flats being laid out, they'll instead lay out the gradients and then go for the shadows.

3:20pm. Ok, enough drawing tutorials.

https://youtu.be/PpZkFWQojmY
BEER - FREE & Open-Source NPR for Blender

Non photorealistic renderer.

Oh, righ, oh right. I keep forgetting to check out the Moi issue. I really hope I did not come across as sarcastic in the issue.

3:30pm.

///

Hi MRAKGR,

re:
> Considering the edges were so far away from the cutter, why were they a problem?

It has to do with the surface structure - for the areas with 4 coplanar faces each planar face has a kind of trapezoidal control point structure. That means that even though it is a planar surface it is a generic spline surface that happens to have all its control points in a plane.

That's a little different case than planar surfaces made by Construct > Planar which are able to use a specialized plane analytic surface that has some special case handling to get tighter accuracy on various operations like intersections.

It usually helps to have planar areas use the analytic plane surface and to have just one large plane instead of multiple coplanar fragments. That's a general cleanup step that is one of the first things I do with cases that are having difficulty.

I'm not entirely sure which step it is helping in this particular case, it would probably take a few days of work doing a deep analysis to determine that.

It's also possible to go about things in a little different way to avoid the overlapping. Like you can do a boolean with just these lines selected:

[AttachmentMRAKGR_bool1.jpg]

That will cut up the faces but won't be able to automatically separate it into different pieces but you can do that yourself using Edit > Separate, then Join together the pieces and use Construct > Planar to fill in the remaining pieces.

If the simplified planes didn't work then that would have been another way to do it.

///

Let me give what he suggested a try.

3:45pm. No, it is not working for me. Let me take a screenshot and I will ask again.

4:05pm. Let me get back on track. Ah, right maybe...

4:15pm. I figured out how to planar it, but the steps are long winded. For that reason, I am not sure if that it is the process I am expected to take.

Now let me go back to what I was watching.

https://youtu.be/PpZkFWQojmY
BEER - FREE & Open-Source NPR for Blender

Namely this. The stuff here looks good. It is true that I've studied texturing, but I've never really thought about the rendering process itself. I sort of went with the assumption of using ray tracing, but I knew that if went down that route I'd have to keep cramming details to prevent it from looking uncanny.

Rather than study texturing, maybe I should study rendering. It is just about time for this kind of thing.

https://youtu.be/PpZkFWQojmY?t=2

This scene is very nice.

Rather than me trying to learn how to draw like an expert, since I have a basis in 3d already, going in this direction might not be bad.

https://youtu.be/PpZkFWQojmY?t=39

Is the background on the webpage in BEER? If so it might be worth serious consideration.

https://youtu.be/PpZkFWQojmY?t=87

It is a renderer as one would expect.

https://youtu.be/PpZkFWQojmY?t=173

This is nice. Maybe I could like this. Remember how I used to mess with falloff nodes in V-Ray. That might have been a clue that I should look into NPR more seriously.

4:45pm. I am starting to hear thunder outside.

https://youtu.be/s5QZZJBuBbw?t=646

Since I started this, let me finish it.

https://www.youtube.com/playlist?list=PLdvpK-NAm6_c37muLyuil3OCCJpb9fjc9

Then I'll watch the freestyle vid on this playlist. Then I'll take a look at the Blender NPR stuff.

4:50pm. Let me move on. Nevermind this vid.

When it comes to freestyle edges, I am a bit unsure how they relate to the rest of the NPR shading.

4:45pm. https://youtu.be/l06RRz8w_4w?list=PLdvpK-NAm6_c37muLyuil3OCCJpb9fjc9
The basics of Freestyle for comics

Let me start with this.

https://youtu.be/dJcglkAEqN4
2008 - Freestyle Basics (updated for 2.83)

Here is an updated version. Let me watch it instead.

https://youtu.be/dJcglkAEqN4?t=110

Ah, I see. Freestyle is part of Eevee.

I am betting it would not work with Cycles. If I used Malt, I would not be able to use it with that either.

https://youtu.be/dJcglkAEqN4?t=367

He said he had a very basic setup, so why do the ceiling and floors have lights? Are they maybe emissive?

5:35pm. I am tired at this point.

https://www.youtube.com/playlist?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76

I should take a look at what this playlist has to offer.

https://youtu.be/vCxnbOCYELM?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76
Grease Pencil - Line Art Modifier in Blender 2.93 Alpha

Let me watch this.

At 71k views, this has a decent bit of interest.

https://youtu.be/vCxnbOCYELM?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=909

Ah wait, is this modifier for generating grease pencil curves from freestyle edges?

https://youtu.be/vCxnbOCYELM?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=1029
> It has more in common with a branch that NPR enthusiasts are familiar with called Lan PR.

6pm. https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76
Comic Shading using the Compositor in Blender

Let me watch this. After that I'll leave it aside and focus on NPR.

https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=27
> This image is created using basic shaders that are inside of Blender, Cycles and the compositor.

No toon shaders.

https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=211

It seems he is using Cycles because it can separate freestyle from all the other passes. I guess in March of 2019 Eevee did not have that capability yet.

https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=252

It seems Cycles does have Freestyle strangely enough.

https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=338

This is a bit too much for me to take in right now, but it is obvious to me now that if I continue going in this direction, I am definitely going to be learning about composition.

6:55pm. Had to leave for lunch. Let me finish the video and I will close for the day.

https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=1007

I've realized something - compositing is not that big of a deal. It is just like stacking layers in CSP and Substance Painter. Though since they are using a node based approach it is more like working in Substance Designer. I get that.

https://youtu.be/anIFTskTUKI?list=PLLS6dnaeZi7EsSeMMAVrjJKPuNqmYer76&t=1272

Yeah, this is pretty much how Designer works. Who knew it would be relevant to my experience in Blender?

7:20pm. https://youtu.be/_IVDwGsn4AQ
How to CELL SHADE | CLIP STUDIO PAINT

Let me watch this. Those creases can either be very hard or very easy. My current technique is very geared towards capturing realism. But I were doing cell shading I'd go for 3 tones. Let me take a look at how he does the shading here.

https://youtu.be/_IVDwGsn4AQ?t=337
> You want to get right in there and make sure everything is perfect.

I have absolutely have this tendency.

8:15pm. I am going to close here.

I had to go out and seek info.

8:20pm. Here is what I am going to do. I am going to have to in fact soup up the models and check out non-physical rendering, but that is a separate matter from me not being able to paint the bed.

It is not that I can't. It is just that using my current approach I'd need a hard ref and it would take me forever to go every little detail. If I wanted to go for that look, I'd be better off souping up the model and going deeper into 3d.

I need to try out a cell shading approach instead.

I am going to have to make it as simple as it can be. No messing with gradients and the blur tool like now. I should just reture that. Instead I should lay out the flats, and then use a few fill saturation layers and paint in their masks.

Look at how far Inio got with just the monochrome.

8:25pm. In order to make progress I should place some heavy restrictions on myself nad move forward that way.

It won't as good as the souped up models, or a proper painterly approach, but it will tell me exactly where I stand.

8:30pm. If I was a beginner, while I was watching the compositing tutorial, I would have faced another struggle, but today gives me a 'meh, I've been there' kind of feeling. Tomorrow, I am going to dive back into the fray.

For my next attempt, I am going to completely get rid of the mili pen, the blur tool, and opacity stacking. Instead I'll use lines as pseudo masks and let the paint bucket do the talking. No admiring the grainy texture. Forget that sort of thing. For shades and highlights I will either draw lines on a separate layer and fill them in, or use lassoed in masks.

8:35pm. The goal will be to go for a cheap, mostly flat look. Not something I'd put on the cover, but something that would be usable in a pinch. I need to develop a baseline style with which to benchmark future improvements.

I mean what is the problem. Laying down lines by tracing out the reference? Filling in the flats? Masking in some hades and highlights? This isn't something I need to lose sleep over. A painterly look over the whole scene, sure, that would be very hard to do quickly. But if I am expecting to be able to do that quickly, I am the fool here.

I am going to complete this cheap image next and then dive into painterly aspects of 3d.

8:40pm. I'll reach my goals one by one.

Today gave me a lot of confidence. Think about what Inio is doing? If he just starts things off by bringing in an image and levels out the midtones, just what is cleaning up? I thought this was some amazing achievement. And indeed painting a whole city from imagination would be 5/5 and even higher ability, but what he is doing is not that different from what I did with the couch. It takes skill to draw the lines the way he did, but I could do it with enough effort.

And indeed, why not do it? It is not like I need to be capable of building cities from the ground up when I can just have them be given to me. There is zero reason for me to feel a sense of inferity to those better than me. Just what is the point of being good at art if you are a fancy photoshop filter in the end?

8:50pm. This is why I am putting in effort into 3d. Even if I could win just tracing, what good would that be? I am going to acquire something tangible from all of this. And there is nothing more tangible than skill of working directly in 3d space.

I'll master 3d this year and leave the higher dimensions for the future.

8:55pm. Tomorrow even if it kills me, I am going to lay down the basic lines and the flats. I need to curb my creativity and work according to the process I've set out for myself. Once I have the lines and the flats, the 2 levels of shades and the single level of hightlights should come naturally."

---
## [bgamez23/rathena](https://github.com/bgamez23/rathena)@[d617d9f083...](https://github.com/bgamez23/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Tuesday 2022-05-17 19:31:20 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [Sir-Mora/goonstation](https://github.com/Sir-Mora/goonstation)@[bdad398f9e...](https://github.com/Sir-Mora/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Tuesday 2022-05-17 19:45:55 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a064b35b25...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Tuesday 2022-05-17 20:00:15 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [jocrl/cockroach](https://github.com/jocrl/cockroach)@[5791e22545...](https://github.com/jocrl/cockroach/commit/5791e225458d1669058484dca26b09dc29e265bd)
#### Tuesday 2022-05-17 20:01:16 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are less need with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [dolev146/orgchart-a](https://github.com/dolev146/orgchart-a)@[9e52383983...](https://github.com/dolev146/orgchart-a/commit/9e523839838a6a88ed992c9668db97638046050c)
#### Tuesday 2022-05-17 20:25:47 by dolev146

fuck you mother fucker bitch ben shel zona mizdayen

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[30100412e6...](https://github.com/Buildstarted/linksfordevs/commit/30100412e64d3c3c4ddb9a6bfdacea215156edf6)
#### Tuesday 2022-05-17 23:06:04 by Ben Dornis

Updating: 5/17/2022 10:00:00 PM

 1. Added: Thorsten Ball - Professional Programming: The First 10 Years
    (https://thorstenball.com/blog/2022/05/17/professional-programming-the-first-10-years/)
 2. Added: Zstandard Worked Example Part 1: Concepts
    (https://nigeltao.github.io/blog/2022/zstandard-part-1-concepts.html)
 3. Added: How to make video calls almost as good as face-to-face
    (https://www.benkuhn.net/vc/)
 4. Added: JSON is not a YAML subset
    (https://john-millikin.com/json-is-not-a-yaml-subset)
 5. Added: Mining a Dispensary
    (https://lerielab.wordpress.com/2022/04/16/mining-a-dispensary/)
 6. Added: macOS tips and tricks - saurabhs.org
    (https://saurabhs.org/macos-tips)
 7. Added: Calculating type sets is harder than you think
    (https://blog.merovius.de/posts/2022-05-16-calculating-type-sets/)
 8. Added: Florence: the Short Masterpiece that Goes Past a Love Story – doamatto
    (https://www.maatt.ch/blog/florence-a-short-masterpiece/)
 9. Added: Laurence Tratt: Static Integer Types
    (https://tratt.net/laurie/essays/entries/static_integer_types.html)
10. Added: A real life use-case for generics in Go: API for client-side pagination
    (https://vladimir.varank.in/notes/2022/05/a-real-life-use-case-for-generics-in-go-api-for-client-side-pagination/)
11. Added: My Thoughts About Fly.io (So Far) and Other New-ish Technology I'm Getting Into
    (https://blog.hartleybrody.com/thoughts-on-flyio/)
12. Added: Steps towards debugging and resolving Android bootloops
    (https://johannes.truschnigg.info/writing/2022-05_android_bootloop_debugging/)
13. Added: Learn C# with CSharpFritz - Get Started with ASP.NET Core MVC
    (https://www.youtube.com/watch?v=LnfZ23an4eA)
14. Added: Sync Obsidian Between Laptop and Android
    (https://nsirap.com/posts/050-sync-obsidian-between-laptop-and-android/)

Generation took: 00:05:52.3163279
 Maintenance update - cleaning up homepage and feed

---
## [elizagamedev/mujmap](https://github.com/elizagamedev/mujmap)@[b961b9032e...](https://github.com/elizagamedev/mujmap/commit/b961b9032e024c84044d8667ff8dbf47a45d70e6)
#### Tuesday 2022-05-17 23:16:46 by Eliza Velasquez

Add troubleshooting section with auth guide

Also adds more warnings to the "migration" section, as I am becoming
increasingly paranoid that someone might behave like me and recklessly
try to migrate without doing the proper precautions, destroying their
notmuch database they spent hours working on (which in my case was not
because of mujmap, but because I tried to switch protonmail IMAP
clients, which was a horrible idea to do without backing up that I
immediately regretted)

---

