## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-02](docs/good-messages/2022/2022-07-02.md)


1,555,931 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,555,931 were push events containing 2,008,489 commit messages that amount to 117,714,615 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [SomeGuyEatingPie/GS13](https://github.com/SomeGuyEatingPie/GS13)@[5b7f7a52e4...](https://github.com/SomeGuyEatingPie/GS13/commit/5b7f7a52e462ac381aa5e8bd762ccb2fbfc9476b)
#### Saturday 2022-07-02 00:32:33 by MrSky12

Removed the fat ray

Fuck you fat ray for being bad.

---
## [sasezaki/laminas-hydrator](https://github.com/sasezaki/laminas-hydrator)@[bb206b0637...](https://github.com/sasezaki/laminas-hydrator/commit/bb206b06377092982987a018d34243579eed5482)
#### Saturday 2022-07-02 00:34:06 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [Spyroshark/Pariah-Station](https://github.com/Spyroshark/Pariah-Station)@[c77fb1e795...](https://github.com/Spyroshark/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Saturday 2022-07-02 01:02:12 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Spyroshark/Pariah-Station](https://github.com/Spyroshark/Pariah-Station)@[70a87f9510...](https://github.com/Spyroshark/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Saturday 2022-07-02 01:02:12 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [Whitelion-exec/dmc4_hook](https://github.com/Whitelion-exec/dmc4_hook)@[142fa95ae4...](https://github.com/Whitelion-exec/dmc4_hook/commit/142fa95ae440d9c0b7f8c7d5af7b45e12dc8759f)
#### Saturday 2022-07-02 02:04:50 by Mstislav Kapustka

fixed background rendering

with shittiest workaround possible, late night programming. damn i gotta work tomorrow fuckk

---
## [Kanginyi/Greenit-Mono-Repo](https://github.com/Kanginyi/Greenit-Mono-Repo)@[c48d2aeee4...](https://github.com/Kanginyi/Greenit-Mono-Repo/commit/c48d2aeee4579ee5074a9afcf24fc9dc4adf4739)
#### Saturday 2022-07-02 03:20:15 by Eric Yi

It's July 1st, Haejin's birthday

She's never gonna see this stuff but I hope she had a great day today hehe

We rowed a boat for the first time together at Central Park, walked around for a bit before deciding to head home and chill for a bit, because the weather was disgusting outside and we had both had some terrible sleep. Ordered some food and ate lunch with my sister, who came over with balloons and some flowers for Haejin. She left, we got ready for dinner reservations at Barano in Williamsburg. Before taking the bus, made a new friend with a guy named Charles, who was helping us look out for the bus. We got him a drink at a bubble tea shop and talked to him for a bit, was really sweet. Got off, ordered Barano's meatballs, Nonna pizza, and linguine pasta. Finished eating, took home the leftover pizza, and walked down to the waterside to enjoy the sunset. Took some time to relax and talk and took the ferry together back to LIC. Stayed at Gantry for a little bit more to enjoy the breeze before calling an Uber to head home.

Wasn't the craziest day in terms of activities, but knocked off a lot of water-related things that she has always wanted to do since she got to the city. So that's a win in itself.

Ooh, forgot to mention. We ordered and picked up cake from Billy's Bakery in Chelsea yesterday and when we got home, we had some cake using this big ass pasta fork that we bought for 30 dollars a year ago. Now chilling, writing a commit on GitHub about the day I had with my girlfriend.

If you ever do see this, for whatever reason, know that I love you so much, and I hope we get to enjoy the rest of your birthday weekend together, doing whatever it is that makes you happy.

BIG 26git add client/tsconfig.json !

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[5cf6c5c030...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/5cf6c5c03073345a9ba03dd81b5d7996f904cf32)
#### Saturday 2022-07-02 04:45:03 by Hayden Pearce

munin-pihole-plugins: fix bash completion - probably, 06.03.02

bash completion got neglected during the --variables/--configure
migration, this aims to fix that

remember, bash_completion kinda sucks and you'll need to source
bash_completion yourself for immediate use, or open a new term

example: . /etc/bash_completion

Changes to be committed:
 - modified:   etc/bash_completion.d/munin-pihole-plugins
   bump version to 06.03.02
   fix human readable and longform completions
   (--/variables no longer exists, it's --/configure now)
 - modified:   script/munin-pihole-plugins
   bump version to 06.03.02
   (no functional changes)
 - modified:   usr/share/munin/plugins/pihole_
   bump version to 06.03.02
   (no functional changes)

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES)@[d4eeeda6d1...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES/commit/d4eeeda6d1225697004e4dfc24ea0a9a8b72cb23)
#### Saturday 2022-07-02 05:48:09 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

 deposited into an interest bearing account in ESCROW, where do they list that on the left or the right side as a credit or a liability? 

THEY ARE NOT GOING TO LIKE YOU IN THOSE COURT ROOMS EITHER, IF YOU EVER WALK IN...

- JSUT KNOW, YOU WILL NEVER KNOW IF THE GUY SITTING ACROSS FROM YOU HAS THESE PAPERS.


-------- Forwarded Message --------
Subject: 	Fw: 153974
Date: 	Sat, 2 Jul 2022 00:46:13 +0000 (UTC)
From: 	Bo Dincer <bo.dincer@yahoo.com>
Reply-To: 	bo.dincer@yahoo.com <bo.dincer@yahoo.com>
To: 	JCARTER@dhs.nyc.gov <JCARTER@dhs.nyc.gov>, 7 11 Webmaster <webmaster@7-11.com>
CC: 	James Comey <jbc2167@columbia.edu>, Avril Haines <ah3774@columbia.edu>, SonyMusic Royalties <royalty.statements@sonymusic.com>, wmprivacy@warnermediagroup.com <wmprivacy@warnermediagroup.com>


Fw: 153974/2020 50074 CIK 93715 [1516523] - Wilson Elser Zucker

/S/ BO DINCER 

    ----- Forwarded Message -----
    From: "Bo Dincer" <bo.dincer@yahoo.com>
    To: "James Comey" <jbc2167@columbia.edu>, "Avril Haines" <ah3774@columbia.edu>, "Andrew T. Mount" <amount@bressler.com>, "amasters@boc.nyc.gov" <amasters@boc.nyc.gov>, "Bressler Info" <info@bressler.com>, "Frank Cuccio" <fcuccio@bressler.com>, "BD (NYSBA MRC)" <mrc@nysba.org>, "Paul Jones" <paul.jones@tudor.com>, "Ir-operations-team" <ir-operations-team@tudor.com>, "Irene Zola" <irene@zola.email>, "Irene Zola" <irenezola@l-i-l-y.org>, "assessments@fdic.gov" <assessments@fdic.gov>, "assetmarketing@fdic.gov" <assetmarketing@fdic.gov>, "QUEUED" <askcuit@columbia.edu>, "CUIT Communications" <cuit-communications@columbia.edu>, "sgo2107@adcu.columbia.edu" <sgo2107@adcu.columbia.edu>, "Paul S. Blaer" <pblaer@cs.columbia.edu>, "DR Paul S. BLAER" <pbr@columbia.edu>, "Kids Privacy" <kidsprivacy@viacomcbs.com>, "MSKYLINE BROKER" <leftbank@mskylinerentals.com>, "Skys the Limit Concierge" <skysthelimit@theconcierge.info>, "Kathleen A. Mullins" <kathleen.mullins@wilsonelser.com>, "Governor Hochul" <governor.hochul@exec.ny.com>, "Lois K. Ottombrino" <lois.ottombrino@wilsonelser.com>, "LLC. MANHATTAN SKYLINE" <administrator@mskyline.com>, "Treasury Inspector General for Tax Administration" <tigta@service.govdelivery.com>, "The Bureau of Engraving and Printing" <usbep@service.govdelivery.com>, "engineering@spglobal.com" <engineering@spglobal.com>
    Cc: "Marlyn Delva" <mmt22@cumc.columbia.edu>, "Marlyn Delva" <mmt22@columbia.edu>, "Stephen O'Connell" <sgo2107@columbia.edu>, "Stephen O'Connell" <sgo2107@adcu.columbia.edu>, "Lee Bollinger" <officeofthepresident@columbia.edu>, "Lee Bollinger" <bollinger@columbia.edu>, "Lee Bollinger" <lcb50@columbia.edu>, "jpmcinvestorrelations@jpmchase.com" <jpmcinvestorrelations@jpmchase.com>, "Governor Hochul" <governor.hochul@exec.ny.gov>, "Shari Laskowitz" <slaskowitz@ingramllp.com>, "Jpetit Petit" <jpetit@mccarter.com>, "Thermanson" <thermanson@northmarq.com>, "Amber Griffiths" <ag2943@adcu.columbia.edu>, "Ashley V. Humphries" <ashley.humphries@wilsonelser.com>, "Amy Hanrahan" <amy.hanrahan@wilsonelser.com>, "Alan Rubin" <alan.rubin@wilsonelser.com>, "Alan Morrison" <ajm157@columbia.edu>, "Dean's Discipline - SCCS" <conduct-admin@columbia.edu>, "Lisa Rosen-Metsch" <lm2892@columbia.edu>, "Lena Mei" <lm3440@columbia.edu>, "Judy C. Selmeci" <judy.selmeci@wilsonelser.com>, "Jennifer M. Provost" <jennifer.provost@wilsonelser.com>, "Joseph Giamboi" <joseph.giamboi@brooklaw.edu>, "slaskowitz@mskyline.com" <slaskowitz@mskyline.com>, "MANHATTAN SKYLINE MANAGEMENT CORP." <super@sullivanmews.com>, "JAMES GORMAN [MORGAN STANLEY]" <james.gorman@morganstanley.com>, "FDIC Public Information" <publicinfo@fdic.gov>, "BRIAN HODGSON" <brian.hodgson.nyz6@statefarm.com>, "david.moore.ct95@statefarm.com" <david.moore.ct95@statefarm.com>, "legalasst@mskyline.com" <legalasst@mskyline.com>
    Sent: Fri, Jul 1, 2022 at 8:44 PM
    Subject: 153974/2020 50074 CIK 93715 [1516523] - Wilson Elser Zucker
    do not open these emails until you feel like it.

    Also, just keep this in case the Zuckers don't want to have this information to hold against them in court later.

    -- even thought inalready filed it without action from the judge, so let me know where did that $6,000,000 come from.

    They change their emails constantly, keyword search: AIMA.

    Redundsnt email required in colocation, dont know who does that at one state farm... 














    Do those deposits match up with the gross incomes reported for the 6 properties in question, YoY and every year as reported to the NY dept of Finance, and purport double digit return which over lunch, is a great marketing document to raise money for their Limited Paprtnership -- 

    How would they see something likenthat everyday? 
    By different people?
    Play-by-play also......


    Those checks, known by the Entities and counselors:
     --- deposited into an interest bearing account in ESCROW, where do they list that on the left or the right side as a credit or a liability? 

    To satisfy their reserve reequirements with the Treasury, or we are you planning on hiding those charges as well, aided and abetted by the counselors of the Zucker compound of entities, directors, and lawyers, and counselors.

    /S/ BO DINCER.

        ----- Forwarded Message -----
        From: "BO DINCER" <bondstrt007@gmail.com>
        To: "espnfrontrow@espn.com" <espnfrontrow@espn.com>, "BBO 121" <ms60710444266@yahoo.com>, "Bo Dincer" <bdincer66@icloud.com>, "Bo Dincer" <BO.DINCER@yahoo.com>
        Cc: "customerservice@nypost.com" <customerservice@nypost.com>, "CustomerService@seahawks.com" <CustomerService@seahawks.com>, "SOHO HOUSE" <membership@sohohouse.com>, "Marc Lavigne" <tessier3@stanford.edu>, "dailydigest@stanford.edu" <dailydigest@stanford.edu>, "inbox@livekelly.com" <inbox@livekelly.com>, "tips@vibe.com" <tips@vibe.com>, "Frank Cuccio" <fcuccio@bressler.com>
        Sent: Thu, Jun 30, 2022 at 9:05 PM
        Subject: if you're an adversary to the wilson elser firm. Or anyone.
        Just flash this deck right here in court. But dont look at it first. Forward it to their counselors then bring it in a air sealed bag and ask them: you read this pack?

        Then give it to the judge, like I did -- thing is, my files got processed and were also evaluated by the judge, clerk, and all of the Plaintiff’s counselors.

        Index 153974/2020 50074 CIK 93715 [1516523]

        - covered for violations under USC Title 18, namely under continuing financial crimes, 18.215, 18.21, 18.225, 18.4, 18.3, 18.2.

        One love. 

153974-2020-STFGX-JPMORGANESCROWACCOUNT

#WATCH FOR CONTACT ON THIS PLEASE - THANK YOU

---
## [much-doge/Quantum_Quackery](https://github.com/much-doge/Quantum_Quackery)@[09996b46f8...](https://github.com/much-doge/Quantum_Quackery/commit/09996b46f824c7d121b671ba763bc55b24e34866)
#### Saturday 2022-07-02 06:52:25 by J. Bruce Fields

nfsd: allow fh_want_write to be called twice

[ Upstream commit 0b8f62625dc309651d0efcb6a6247c933acd8b45 ]

A fuzzer recently triggered lockdep warnings about potential sb_writers
deadlocks caused by fh_want_write().

Looks like we aren't careful to pair each fh_want_write() with an
fh_drop_write().

It's not normally a problem since fh_put() will call fh_drop_write() for
us.  And was OK for NFSv3 where we'd do one operation that might call
fh_want_write(), and then put the filehandle.

But an NFSv4 protocol fuzzer can do weird things like call unlink twice
in a compound, and then we get into trouble.

I'm a little worried about this approach of just leaving everything to
fh_put().  But I think there are probably a lot of
fh_want_write()/fh_drop_write() imbalances so for now I think we need it
to be more forgiving.

Signed-off-by: J. Bruce Fields <bfields@redhat.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Peppe289/android_kernel_xiaomi_sdm660](https://github.com/Peppe289/android_kernel_xiaomi_sdm660)@[cc8033e824...](https://github.com/Peppe289/android_kernel_xiaomi_sdm660/commit/cc8033e82497193aa5bf76610ea57994e6280d67)
#### Saturday 2022-07-02 07:42:27 by Dave Chiluk

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
## [CoinMarketCapAustraliaNFTs/ETH-2.0-AUD-DEX](https://github.com/CoinMarketCapAustraliaNFTs/ETH-2.0-AUD-DEX)@[0e95bebb63...](https://github.com/CoinMarketCapAustraliaNFTs/ETH-2.0-AUD-DEX/commit/0e95bebb634d0e03ad4de440413ea1faa925bd52)
#### Saturday 2022-07-02 08:13:42 by CoinMarketCap Australia NFT'S

CoinMarketCapAustraliaNFTs

{{https://coinmarketcap.com/CoinMarketCapAustraliaNFTs/Minter.js/new/main?readme=1}}. Skip to main content   Use Ethereum Ethereum wallets Get ETH Decentralized applications (dapps) Layer 2 Non-fungible tokens (NFTs) Decentralized finance (DeFi) Decentralized autonomous organisations (DAOs) Stablecoins Stake ETH Run a node Decentralized social networks Decentralized identity Learn What is Ethereum? What is ether (ETH)? Smart contracts Ethereum security and scam prevention History of Ethereum Ethereum Whitepaper Ethereum upgrades Ethereum glossary Ethereum governance Blockchain bridges Ethereum energy consumption Ethereum Improvement Proposals What is Web3? Community guides and resources Developers Developers' home Documentation Tutorials Learn by coding Set up local environment Enterprise Mainnet Ethereum Private Ethereum Community Community hub Online communities Ethereum events Get involved Open research Grants Ethereum support Language resources SEARCH LIGHT LANGUAGES Search Search ⛵ Search away! NFT MINTER TUTORIAL SOLIDITY NFT MINTER ALCHEMY SMART CONTRACTS FRONTEND UI WALLET PINATA INTERMEDIATE ✍️smudgil 📆October 6, 2021 ⏱️29 minute read On this page One of the greatest challenges for developers coming from a Web2 background is figuring out how to connect your smart contract to a frontend project and interact with it.  By building an NFT minter — a simple UI where you can input a link to your digital asset, a title, and a description — you'll learn how to:  Connect to MetaMask via your frontend project Call smart contract methods from your frontend Sign transactions using MetaMask In this tutorial, we will be using React as our frontend framework. Because this tutorial is primarily focused on Web3 development, we won't be spending much time breaking down React fundamentals. Instead, we'll be focusing on bringing functionality to our project.  As a prerequisite, you should have a beginner-level understanding of React—know how components, props, useState/useEffect, and basic function calling works. If you've never heard of any of those terms before, you may want to check out this Intro to React tutorial. For the more visual learners, we highly recommend this excellent Full Modern React Tutorial video series by Net Ninja.  And if you haven't already, you'll definitely need an Alchemy account to complete this tutorial as well as build anything on the blockchain. Sign up for a free account here.  Without further ado, let's get started!  MAKING NFTS 101 Before we even start looking at any code, it's important to understand how making an NFT works. It involves two steps:  Publish an NFT smart contract on the Ethereum blockchain The biggest difference between the two NFT smart contract standards is that ERC-1155 is a multi-token standard and includes batch functionality, whereas with the ERC-721 is a single-token standard and therefore only supports transferring one token at a time.  Call the minting function Usually, this minting function requires you to pass in two variables as parameters, first the recipient, which specifies the address that will receive your freshly minted NFT, and second the NFT's tokenURI, a string that resolves to a JSON document describing the NFT's metadata.  An NFT's metadata is really what brings it to life, allowing it to have properties, such as a name, description, image (or different digital asset), and other attributes. Here's an example of a tokenURI, which contains an NFT's metadata.  In this tutorial, we're going to focus on part 2, calling an existing NFT's smart contract minting function using our React UI.  Here's a link to the ERC-721 NFT smart contract we will be calling in this tutorial. If you'd like to learn how we made it, we highly recommend that you check out our other tutorial, "How to Create an NFT".  Cool, now that we understand how making an NFT works, let's clone our starter files!  CLONE THE STARTER FILES First, go to the nft-minter-tutorial GitHub repository to get the starter files for this project. Clone this repository into your local environment.=  When you open this cloned nft-minter-tutorial repository, you'll notice that it contains two folders: minter-starter-files and nft-minter.  minter-starter-files contains the starter files (essentially the React UI) for this project. In this tutorial, we will be working in this directory, as you learn how to bring this UI to life by connecting it to your Ethereum wallet and an NFT smart contract. nft-minter contains the entire completed tutorial and is there for you as a reference if you get stuck. Next, open your copy of minter-starter-files in your code editor, and then navigate into your src folder.  All of the code we'll write will live under the src folder. We'll be editing the Minter.js component and writing additional javascript files to give our project Web3 functionality.  STEP 2: CHECK OUT OUR STARTER FILES Before we start coding, it's important to check out what's already provided for us in the starter files.  Get your react project running Let's start by running the React project in our browser. The beauty of React is that once we have our project running in our browser, any changes we save will be updated live in our browser.  To get the project running, navigate to the root directory of the minter-starter-files folder, and the run npm install in your terminal to install the dependencies of the project:  cd minter-starter-files npm install  Once those have finished installing, run npm start in your terminal:  npm start  Doing so should open http://localhost:3000/ in your browser, where you'll see the frontend for our project. It should consist of 3 fields: a place to input a link to your NFT's asset, enter the name of your NFT, and provide a description.  If you try clicking "Connect Wallet" or "Mint NFT" buttons, you'll notice they don't work—that's because we still need to program their functionality! :)  The Minter.js component NOTE: Make sure you're in the minter-starter-files folder and not the nft-minter folder!  Let's go back into the src folder in our editor and open the Minter.js file. It's super important that we understand everything in this file, as it is the primary React component we will be working on.  At the top of our this file, we have our state variables that we will update after specific events.  //State variables const [walletAddress, setWallet] = useState("") const [status, setStatus] = useState("") const [name, setName] = useState("") const [description, setDescription] = useState("") const [url, setURL] = useState("")  Never heard of React state variables or state hooks? Check out these docs.  Here's what each of the variables represent:  walletAddress - a string that stores the user's wallet address status - a string that contains a message to display at the bottom of the UI name - a string that stores the NFT's name description - a string that stores the NFT's description url - a string that is a link to the NFT's digital asset After the state variables, you'll see three un-implemented functions: useEffect, connectWalletPressed, and onMintPressed. You'll notice that all of these functions are async, that's because we will be making asynchronous API calls in them! Their names are eponymous with their functionalities:  useEffect(async () => {   //TODO: implement }, [])  const connectWalletPressed = async () => {   //TODO: implement }  const onMintPressed = async () => {   //TODO: implement }  Show all useEffect - this is a React hook that is called after your component is rendered. Because it has an empty array [] prop passed into it (see line 3), it will only be called on the component's first render. Here we'll call our wallet listener and another wallet function to update our UI to reflect whether a wallet is already connected. connectWalletPressed - this function will be called to connect the user's MetaMask wallet to our dApp. onMintPressed - this function will be called to mint the user's NFT. Near the end of this file, we have the UI of our component. If you scan this code carefully, you'll notice that we update our url, name, and description state variables when the input in their corresponding text fields change.  You'll also see that connectWalletPressed and onMintPressed are called when the buttons with IDs mintButton and walletButton are clicked respectively.  //the UI of our component return (   <div className="Minter">     <button id="walletButton" onClick={connectWalletPressed}>       {walletAddress.length > 0 ? (         "Connected: " +         String(walletAddress).substring(0, 6) +         "..." +         String(walletAddress).substring(38)       ) : (         <span>Connect Wallet</span>       )}     </button>      <br></br>     <h1 id="title">🧙‍♂️ Alchemy NFT Minter</h1>     <p>       Simply add your asset's link, name, and description, then press "Mint."     </p>     <form>       <h2>🖼 Link to asset: </h2>       <input         type="text"         placeholder="e.g. https://gateway.pinata.cloud/ipfs/<hash>"         onChange={(event) => setURL(event.target.value)}       />       <h2>🤔 Name: </h2>       <input         type="text"         placeholder="e.g. My first NFT!"         onChange={(event) => setName(event.target.value)}       />       <h2>✍️ Description: </h2>       <input         type="text"         placeholder="e.g. Even cooler than cryptokitties ;)"         onChange={(event) => setDescription(event.target.value)}       />     </form>     <button id="mintButton" onClick={onMintPressed}>       Mint NFT     </button>     <p id="status">{status}</p>   </div> )  Show less Finally, let's address where is this Minter component added.  If you go to the App.js file, which is the main component in React that acts as a container for all other components, you'll see that our Minter component is injected on line 7.  In this tutorial, we'll only be editing the Minter.js file and adding files in our src folder.  Now that we understand what we're working with, let's set up our Ethereum wallet!  ##: Set up your Ethereum wallet {#set-up-your-ethereum-wallet}  For users to be able to interact with your smart contract they will need to connect their Ethereum wallet to your dApp.  Download MetaMask For this tutorial, we’ll use MetaMask, a virtual wallet in the browser used to manage your Ethereum account address. If you want to understand more about how transactions on Ethereum work, check out this page.  You can download and create a MetaMask account for free here. When you are creating an account, or if you already have an account, make sure to switch over to the “Ropsten Test Network” in the upper right (so that we’re not dealing with real money).  Add ether from a Faucet In order to mint our NFTs (or sign any transactions on the Ethereum blockchain), we’ll need some fake Eth. To get Eth you can go to the Ropsten faucet and enter your Ropsten account address, then click “Send Ropsten Eth.” You should see Eth in your MetaMask account soon after!  Check your balance To double check our balance is there, let’s make an eth_getBalance request using Alchemy’s composer tool. This will return the amount of Eth in our wallet. After you input your MetaMask account address and click “Send Request”, you should see a response like this:  {"jsonrpc": "2.0", "id": 0, "result": "0xde0b6b3a7640000"}  NOTE: This result is in wei not eth. Wei is used as the smallest denomination of ether. The conversion from wei to eth is: 1 eth = 10¹⁸ wei. So if we convert 0xde0b6b3a7640000 to decimal we get 1*10¹⁸ which equals 1 eth.  Phew! Our fake money is all there! 🤑  CONNECT METAMASK TO YOUR UI Now that our MetaMask wallet is set up, let's connect our dApp to it!  Because we want to prescribe to the MVC paradigm, we're going to create a separate file that contains our functions to manage the logic, data, and rules of our dApp, and then pass those functions to our frontend (our Minter.js component).  The connectWallet function To do so, let's create a new folder called utils in your src directory and add a file called interact.js inside it, which will contain all of our wallet and smart contract interaction functions.  In our interact.js file, we will write a connectWallet function, which we will then import and call in our Minter.js component.  In your interact.js file, add the following  export const connectWallet = async () => {   if (window.ethereum) {     try {       const addressArray = await window.ethereum.request({         method: "eth_requestAccounts",       })       const obj = {         status: "👆🏽 Write a message in the text-field above.",         address: addressArray[0],       }       return obj     } catch (err) {       return {         address: "",         status: "😥 " + err.message,       }     }   } else {     return {       address: "",       status: (         <span>           <p>             {" "}             🦊 <a target="_blank" href={`https://metamask.io/download.html`}>               You must install MetaMask, a virtual Ethereum wallet, in your               browser.             </a>           </p>         </span>       ),     }   } }  Show all Let's breakdown what this code does:  First, our function checks if it window.ethereum is enabled in your browser.  window.ethereum is a global API injected by MetaMask and other wallet providers that allows websites to request users' Ethereum accounts. If approved, it can read data from the blockchains the user is connected to, and suggest that the user sign messages and transactions. Check out the MetaMask docs for more info!  If window.ethereum is not present, then that means MetaMask is not installed. This results in a JSON object being returned, where address returned is an empty string, and the status JSX object relays that the user must install MetaMask.  Most of the functions we write will be returning JSON objects that we can use to update our state variables and UI.  Now if window.ethereum is present, then that's when things get interesting.  Using a try/catch loop, we'll try to connect to MetaMask by calling[window.ethereum.request({ method: "eth_requestAccounts" });](https://docs.metamask.io/guide/rpc-api.html#eth-requestaccounts). Calling this function will open up MetaMask in the browser, whereby the user will be prompted to connect their wallet to your dApp.  If the user chooses to connect, method: "eth_requestAccounts" will return an array that contains all of the user's account addresses that are connected to the dApp. Altogether, our connectWallet function will return a JSON object that contains the first address in this array (see line 9) and a status message that prompts the user to write a message to the smart contract. If the user rejects the connection, then the JSON object will contain an empty string for the address returned and a status message that reflects that the user rejected the connection. Add connectWallet function to your Minter.js UI Component Now that we've written this connectWallet function, let's connect it to our Minter.js. component.  First, we'll have to import our function into our Minter.js file by adding import { connectWallet } from "./utils/interact.js"; to the top of the Minter.js file. Your first 11 lines of Minter.js should now look like this:  import { useEffect, useState } from "react"; import { connectWallet } from "./utils/interact.js";  const Minter = (props) => {    //State variables   const [walletAddress, setWallet] = useState("");   const [status, setStatus] = useState("");   const [name, setName] = useState("");   const [description, setDescription] = useState("");   const [url, setURL] = useState("");  Show all Then, inside our connectWalletPressed function, we'll call our imported connectWallet function, like so:  const connectWalletPressed = async () => {   const walletResponse = await connectWallet()   setStatus(walletResponse.status)   setWallet(walletResponse.address) }  Notice how most of our functionality is abstracted away from our Minter.js component from the interact.js file? This is so we comply with the M-V-C paradigm!  In connectWalletPressed, we simply make an await call to our imported connectWallet function, and using its response, we update our status and walletAddress variables via their state hooks.  Now, let's save both files Minter.js and interact.js and test out our UI so far.  Open your browser on localhost:3000, and press the "Connect Wallet" button on the top right of the page.  If you have MetaMask installed, you should be prompted to connect your wallet to your dApp. Accept the invitation to connect.  You should see that the wallet button now reflects that your address is connected.  Next, try refreshing the page... this is strange. Our wallet button is prompting us to connect MetaMask, even though it is already connected...  Don't worry though! We easily can fix that by implementing a function called getCurrentWalletConnected, which will check if an address is already connected to our dApp and update our UI accordingly!  The getCurrentWalletConnected function In your interact.js file, add the following getCurrentWalletConnected function:  export const getCurrentWalletConnected = async () => {   if (window.ethereum) {     try {       const addressArray = await window.ethereum.request({         method: "eth_accounts",       })       if (addressArray.length > 0) {         return {           address: addressArray[0],           status: "👆🏽 Write a message in the text-field above.",         }       } else {         return {           address: "",           status: "🦊 Connect to MetaMask using the top right button.",         }       }     } catch (err) {       return {         address: "",         status: "😥 " + err.message,       }     }   } else {     return {       address: "",       status: (         <span>           <p>             {" "}             🦊 <a target="_blank" href={`https://metamask.io/download.html`}>               You must install MetaMask, a virtual Ethereum wallet, in your               browser.             </a>           </p>         </span>       ),     }   } }  Show all This code is very similar to the connectWallet function we just wrote earlier.  The main difference is that instead of calling the method eth_requestAccounts, which opens MetaMask for the user to connect their wallet, here we call the method eth_accounts, which simply returns an array containing the MetaMask addresses currently connected to our dApp.  To see this function in action, let's call it in the useEffect function of our Minter.js component.  Like we did for connectWallet, we must import this function from our interact.js file into our Minter.js file like so:  import { useEffect, useState } from "react" import {   connectWallet,   getCurrentWalletConnected, //import here } from "./utils/interact.js"  Now, we simply call it in our useEffect function:  useEffect(async () => {   const { address, status } = await getCurrentWalletConnected()   setWallet(address)   setStatus(status) }, [])  Notice, we use the response of our call to getCurrentWalletConnected to update our walletAddress and status state variables.  Once you've added this code, try refreshing our browser window. The button should say that you're connected, and show a preview of your connected wallet's address - even after you refresh!  Implement addWalletListener The final step in our dApp wallet setup is implementing the wallet listener so our UI updates when our wallet's state changes, such as when the user disconnects or switches accounts.  In your Minter.js file, add a function addWalletListener that looks like the following:  function addWalletListener() {   if (window.ethereum) {     window.ethereum.on("accountsChanged", (accounts) => {       if (accounts.length > 0) {         setWallet(accounts[0])         setStatus("👆🏽 Write a message in the text-field above.")       } else {         setWallet("")         setStatus("🦊 Connect to MetaMask using the top right button.")       }     })   } else {     setStatus(       <p>         {" "}         🦊 <a target="_blank" href={`https://metamask.io/download.html`}>           You must install MetaMask, a virtual Ethereum wallet, in your browser.         </a>       </p>     )   } }  Show all Let's quickly break down what's happening here:  First, our function checks if window.ethereum is enabled (i.e. MetaMask is installed). If it's not, we simply set our status state variable to a JSX string that prompts the user to install MetaMask. If it is enabled, we set up the listener window.ethereum.on("accountsChanged") on line 3 that listens for state changes in the MetaMask wallet, which include when the user connects an additional account to the dApp, switches accounts, or disconnects an account. If there is at least one account connected, the walletAddress state variable is updated as the first account in the accounts array returned by the listener. Otherwise, walletAddress is set as an empty string. Finally, we must call it in our useEffect function:  useEffect(async () => {   const { address, status } = await getCurrentWalletConnected()   setWallet(address)   setStatus(status)    addWalletListener() }, [])  And voila! We've completed programming all of our wallet functionality! Now that our wallet is set up, let's figure out how to mint our NFT!  NFT METADATA 101 So remember the NFT metadata we just talked about in Step 0 of this tutorial—it brings an NFT to life, allowing it to have properties, such as a digital asset, name, description, and other attributes.  We're going to need to configure this metadata as a JSON object and store it, so we can pass it in as the tokenURI parameter when calling our smart contract's mintNFT function.  The text in the "Link to Asset", "Name", "Description" fields will comprise the different properties of our NFT's metadata. We'll format this metadata as a JSON object, but there are a couple options for where we can store this JSON object:  We could store it on the Ethereum blockchain; however, doing so would be very expensive. We could store it on a centralized server, like AWS or Firebase. But that would defeat our decentralization ethos. We could use IPFS, a decentralized protocol and peer-to-peer network for storing and sharing data in a distributed file system. As this protocol is decentralized and free, it is our best option! To store our metadata on IPFS, we will use Pinata, a convenient IPFS API and toolkit. In the next step, we'll explain exactly how to do this!  USE PINTATA TO PIN YOUR METADATA TO IPFS If you don't have a Pinata account, sign up for a free account here and complete the steps to verify your email and account.  Create your Pinata API key Navigate to the https://pinata.cloud/keys page, then select the "New Key" button at the top, set the Admin widget as enabled, and name your key.  You'll then be shown a popup with your API info. Make sure to put this somewhere safe.  Now that our key is set up, let's add it to our project so we can use it.  Create a .env file We can safely store our Pinata key and secret in an environment file. Let's install the dotenv package in your project directory.  Open up a new tab in your terminal (separate from the one running local host) and make sure you are in the minter-starter-files folder, then run the following command in your terminal:  npm install dotenv --save  Next, create a .env file in the root directory of your minter-starter-files by entering the following on your command line:  vim.env  This will pop open your .env file in vim (a text editor). To save it hit "esc" + ":" + "q" on your keyboard in that order.  Next, in VSCode, navigate to your .env file and add your Pinata API key and API secret to it, like so:  REACT_APP_PINATA_KEY = <pinata-api-key> REACT_APP_PINATA_SECRET = <pinata-api-secret>  Save the file, and then you're ready to start writing the function to upload your JSON metadata to IPFS!  Implement pinJSONToIPFS Fortunately for us, Pinata has an API specifically for uploading JSON data to IPFS and a convenient JavaScript with axios example that we can use, with some slight modifications.  In your utils folder, let's create another file called pinata.js and then import our Pinata secret and key from the .env file like so:  require("dotenv").config() const key = process.env.REACT_APP_PINATA_KEY const secret = process.env.REACT_APP_PINATA_SECRET  Next, paste the additional code from below into your pinata.js file. Don't worry, we'll break down what everything means!  require("dotenv").config() const key = process.env.REACT_APP_PINATA_KEY const secret = process.env.REACT_APP_PINATA_SECRET  const axios = require("axios")  export const pinJSONToIPFS = async (JSONBody) => {   const url = `https://api.pinata.cloud/pinning/pinJSONToIPFS`   //making axios POST request to Pinata ⬇️   return axios     .post(url, JSONBody, {       headers: {         pinata_api_key: key,         pinata_secret_api_key: secret,       },     })     .then(function (response) {       return {         success: true,         pinataUrl:           "https://gateway.pinata.cloud/ipfs/" + response.data.IpfsHash,       }     })     .catch(function (error) {       console.log(error)       return {         success: false,         message: error.message,       }     }) }  Show all So what does this code do exactly?  First, it imports axios, a promise based HTTP client for the browser and node.js, which we will use to make a request to Pinata.  Then we have our asynchronous function pinJSONToIPFS, which takes a JSONBody as its input and the Pinata api key and secret in its header, all to make a POST request to their pinJSONToIPFS API.  If this POST request is successful, then our function returns a JSON object with the success boolean as true and the pinataUrl where our metadata was pinned. We will use this pinataUrl returned as the tokenURI input to our smart contract's mint function. If this post request fails, then our function returns a JSON object with the success boolean as false and a message string that relays our error. As with our connectWalletfunction return types, we're returning JSON objects so we can use their parameters to update our state variables and UI.  LOAD YOUR SMART CONTRACT Now that we have a way to upload our NFT metadata to IPFS via our pinJSONToIPFS function, we're going to need a way to load an instance of our smart contract so we can call its mintNFT function.  As we mentioned earlier, in this tutorial we will be using this existing NFT smart contract; however, if you'd like to learn how we made it, or make one yourself, we highly recommend you check out our other tutorial, "How to Create an NFT.".  The contract ABI If you examined our files closely, you'll have noticed that in our src directory, there's a contract-abi.json file. An ABI is necessary for specifying which function a contract will invoke as well ensuring that the function will return data in the format you're expecting.  We're also going to need an Alchemy API key and the Alchemy Web3 API to connect to the Ethereum blockchain and load our smart contract.  Create your Alchemy API key If you don't already have an Alchemy account, sign up for free here.  Once you’ve created an Alchemy account, you can generate an API key by creating an app. This will allow us to make requests to the Ropsten test network.  Navigate to the “Create App” page in your Alchemy Dashboard by hovering over “Apps” in the nav bar and clicking “Create App”.  Name your app we chose "My First NFT!", offer a short description, select “Staging” for the Environment used for your app bookkeeping, and choose “Ropsten” for your network.  Click “Create app” and that’s it! Your app should appear in the table below.  Awesome so now that we've created our HTTP Alchemy API URL, copy it to your clipboard...  …and then let's add it to our .env file. Altogether, your .env file should look like this:  REACT_APP_PINATA_KEY = <pinata-key> REACT_APP_PINATA_SECRET = <pinata-secret> REACT_APP_ALCHEMY_KEY = https://eth-ropsten.alchemyapi.io/v2/<alchemy-key>  Now that we have our contract ABI and our Alchemy API key, we're ready to load our smart contract using Alchemy Web3.  Set up your Alchemy Web3 endpoint and contract First, if you don't have it already, you'll need to install Alchemy Web3 by navigating to the home directory: nft-minter-tutorial in the terminal:  cd .. npm install @alch/alchemy-web3  Next let's go back to our interact.js file. At the top of the file, add the following code to import your Alchemy key from your .env file and set up your Alchemy Web3 endpoint:  require("dotenv").config() const alchemyKey = process.env.REACT_APP_ALCHEMY_KEY const { createAlchemyWeb3 } = require("@alch/alchemy-web3") const web3 = createAlchemyWeb3(alchemyKey)  Alchemy Web3 is a wrapper around Web3.js, providing enhanced API methods and other crucial benefits to make your life as a web3 developer easier. It is designed to require minimal configuration so you can start using it in your app right away!  Next, let's add our contract ABI and contract address to our file.  require("dotenv").config() const alchemyKey = process.env.REACT_APP_ALCHEMY_KEY const { createAlchemyWeb3 } = require("@alch/alchemy-web3") const web3 = createAlchemyWeb3(alchemyKey)  const contractABI = require("../contract-abi.json") const contractAddress = "0x4C4a07F737Bf57F6632B6CAB089B78f62385aCaE"  Once we have both of those, we're ready to start coding our mint function!  IMPLEMENT THE MINTNFT FUNCTION Inside your interact.js file, let's define our function, mintNFT, which eponymously will mint our NFT.  Because we will be making numerous asynchronous calls (to Pinata to pin our metadata to IPFS, Alchemy Web3 to load our smart contract, and MetaMask to sign our transactions), our function will also be asynchronous.  The three inputs to our function will be the url of our digital asset, name, and description. Add the following function signature below the connectWallet function:  export const mintNFT = async (url, name, description) => {}  Input error handling Naturally, it makes sense to have some sort of input error handling at the start of the function, so we exit this function if our input parameters aren't correct. Inside our function, let's add the following code:  export const mintNFT = async (url, name, description) => {   //error handling   if (url.trim() == "" || name.trim() == "" || description.trim() == "") {     return {       success: false,       status: "❗Please make sure all fields are completed before minting.",     }   } }  Show all Essentially, if any of the input parameters are an empty string, then we return a JSON object where the success boolean is false, and the status string relays that all fields in our UI must be complete.  Upload the metadata to IPFS Once we know our metadata is formatted properly, the next step is to wrap it into a JSON object and upload it to IPFS via the pinJSONToIPFS we wrote!  To do so, we first we need to import the pinJSONToIPFS function into our interact.js file. At the very top of the interact.js, let's add:  import { pinJSONToIPFS } from "./pinata.js"  Recall that pinJSONToIPFS takes in a JSON body. So before we make a call to it, we're going to need to format our url, name, and description parameters into a JSON object.  Let's update our code to create a JSON object called metadata and then make a call to pinJSONToIPFS with this metadata parameter:  export const mintNFT = async (url, name, description) => {   //error handling   if (url.trim() == "" || name.trim() == "" || description.trim() == "") {     return {       success: false,       status: "❗Please make sure all fields are completed before minting.",     }   }    //make metadata   const metadata = new Object()   metadata.name = name   metadata.image = url   metadata.description = description    //make pinata call   const pinataResponse = await pinJSONToIPFS(metadata)   if (!pinataResponse.success) {     return {       success: false,       status: "😢 Something went wrong while uploading your tokenURI.",     }   }   const tokenURI = pinataResponse.pinataUrl }  Show all Notice, we store the response of our call to pinJSONToIPFS(metadata) in the pinataResponse object. Then, we parse this object for any errors.  If there's an error, we return a JSON object where the success boolean is false and our status string relays that our call failed. Otherwise, we extract the pinataURL from the pinataResponse and store it as our tokenURI variable.  Now it's time to load our smart contract using the Alchemy Web3 API that we initialized at the top of our file. Add the following line of code to the bottom of the mintNFT function to set the contract at the window.contract global variable:  window.contract = await new web3.eth.Contract(contractABI, contractAddress)  The last thing to add in our mintNFT function is our Ethereum transaction:  //set up your Ethereum transaction const transactionParameters = {   to: contractAddress, // Required except during contract publications.   from: window.ethereum.selectedAddress, // must match user's active address.   data: window.contract.methods     .mintNFT(window.ethereum.selectedAddress, tokenURI)     .encodeABI(), //make call to NFT smart contract }  //sign the transaction via MetaMask try {   const txHash = await window.ethereum.request({     method: "eth_sendTransaction",     params: [transactionParameters],   })   return {     success: true,     status:       "✅ Check out your transaction on Etherscan: https://ropsten.etherscan.io/tx/" +       txHash,   } } catch (error) {   return {     success: false,     status: "😥 Something went wrong: " + error.message,   } }  Show all If you're already familiar with Ethereum transactions, you'll notice that the structure is pretty similar to what you've seen.  First, we set up our transactions parameters. to specifies the recipient address (our smart contract) from specifies the signer of the transaction (the user's connected address to MetaMask: window.ethereum.selectedAddress) data contains the call to our smart contract mintNFT method, which receives our tokenURI and the user's wallet address, window.ethereum.selectedAddress, as inputs Then, we make an await call, window.ethereum.request, where we ask MetaMask to sign the transaction. Notice, in this request, we're specifying our eth method (eth_SentTransaction) and passing in our transactionParameters. At this point, MetaMask will open up in the browser, and prompt the user to sign or reject the transaction. If the transaction is successful, the function will return a JSON object where the boolean success is set to true and the status string prompts the user to check out Etherscan for more information about their transaction. If the transaction fails, the function will return a JSON object where the success boolean is set to false, and the status string relays the error message. Altogether, our mintNFT function should look like this:  export const mintNFT = async (url, name, description) => {   //error handling   if (url.trim() == "" || name.trim() == "" || description.trim() == "") {     return {       success: false,       status: "❗Please make sure all fields are completed before minting.",     }   }    //make metadata   const metadata = new Object()   metadata.name = name   metadata.image = url   metadata.description = description    //pinata pin request   const pinataResponse = await pinJSONToIPFS(metadata)   if (!pinataResponse.success) {     return {       success: false,       status: "😢 Something went wrong while uploading your tokenURI.",     }   }   const tokenURI = pinataResponse.pinataUrl    //load smart contract   window.contract = await new web3.eth.Contract(contractABI, contractAddress) //loadContract();    //set up your Ethereum transaction   const transactionParameters = {     to: contractAddress, // Required except during contract publications.     from: window.ethereum.selectedAddress, // must match user's active address.     data: window.contract.methods       .mintNFT(window.ethereum.selectedAddress, tokenURI)       .encodeABI(), //make call to NFT smart contract   }    //sign transaction via MetaMask   try {     const txHash = await window.ethereum.request({       method: "eth_sendTransaction",       params: [transactionParameters],     })     return {       success: true,       status:         "✅ Check out your transaction on Etherscan: https://ropsten.etherscan.io/tx/" +         txHash,     }   } catch (error) {     return {       success: false,       status: "😥 Something went wrong: " + error.message,     }   } }  Show all That's one giant function! Now, we just need to connect our mintNFT function to our Minter.js component...  CONNECT MINTNFT TO OUR MINTER.JS FRONTEND Open up your Minter.js file and update the import { connectWallet, getCurrentWalletConnected } from "./utils/interact.js"; line at the top to be:  import {   connectWallet,   getCurrentWalletConnected,   mintNFT, } from "./utils/interact.js"  Finally, implement the onMintPressed function to make await call to your imported mintNFTfunction and update the status state variable to reflect whether our transaction succeeded or failed:  const onMintPressed = async () => {   const { status } = await mintNFT(url, name, description)   setStatus(status) }  DEPLOY YOUR NFT TO A LIVE WEBSITE Ready to take your project live for users to interact with? Check out this tutorial for deploying your Minter to a live website.  One last step...  TAKE THE BLOCKCHAIN WORLD BY STORM Just kidding, you made it to the end of the tutorial!  To recap, by building an NFT minter, you successfully learned how to:  Connect to MetaMask via your frontend project Call smart contract methods from your frontend Sign transactions using MetaMask Presumably, you'd like to be able to show off the NFTs minted via your dApp in your wallet — so be sure to check out our quick tutorial How to View Your NFT in Your Wallet!  And, as always, if you have any questions, we're here to help in the Alchemy Discord. We can't wait to see how you apply the concepts from this tutorial to your future projects!  Patrice Lamarque Last edit: @plamarque, April 15, 2022 See contributors Edit page Was this tutorial helpful?  Yes  No Website last updated: July 1, 2022 Use Ethereum Ethereum wallets Get ETH Decentralized applications (dapps) Layer 2 Run a node Stablecoins Stake ETH Learn What is Ethereum? What is ether (ETH)? Community guides and resources History of Ethereum Ethereum Whitepaper Ethereum upgrades Ethereum security and scam prevention Ethereum glossary Ethereum governance Blockchain bridges Ethereum energy consumption What is Web3? Ethereum Improvement Proposals Developers Get started Documentation Tutorials Learn by coding Set up local environment Ecosystem Community hub Ethereum Foundation Ethereum Foundation Blog Ecosystem Support Program Ethereum bug bounty program Ecosystem Grant Programs Ethereum brand assets Devcon Enterprise Mainnet Ethereum Private Ethereum Enterprise About ethereum.org About us Jobs Contributing Language support Privacy policy Terms of use Cookie policy Contact  Navigated to NFT Minter Tutorial ETH 2.0 AUD DEX

---
## [newstools/2022-national-daily-nigeria](https://github.com/newstools/2022-national-daily-nigeria)@[6671e3b18e...](https://github.com/newstools/2022-national-daily-nigeria/commit/6671e3b18e361bcd9a2b3ff33c9f5e875986182e)
#### Saturday 2022-07-02 08:53:08 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/yahoo-boys-girlfriend-goes-naked-barking-police-kicks-as-her-video-trends/]

---
## [Gorjunov/cockroach](https://github.com/Gorjunov/cockroach)@[f6cc7f575c...](https://github.com/Gorjunov/cockroach/commit/f6cc7f575cd374982752af6909d3efa96908c3dd)
#### Saturday 2022-07-02 09:44:54 by craig[bot]

Merge #81409

81409: bazel: upgrade to rules_nodejs 5.4.2 r=rickystewart,nathanstilwell,laurenbarker a=sjbarag

Please forgive the massive second commit — there's very few valid states in this progression, as building, linting, and testing either work or they don't.  There's not much sense in intentionally leaving commits around that won't build in my opinion, as it makes bisecting extremely frustrating.  If anyone disagrees, let me know and I can keep digging for an intermediate state!

----

Upgrading to Bazel's rules_nodejs 5.x exposed a flaw in our previous Bazel integration: because rules_nodejs explicitly doesn't support yarn's "workspaces" feature [1] (in which common dependencies are hoisted to the lowest common parent directory), any NPM dependencies with different major versions between db-console and cluster-ui would
get flattened to a single version. This left one of those packages using an unsupported (and un-requested) version of a dependency. Removing the yarn workspace layout and using separate Bazel repositories for each JS project ensured each project received the correct dependencies, but revealed incompatibilities with the requested versions. Upgrade rules_nodejs to the latest released version, remove yarn workspaces from the pkg/ui/ tree, and fix all revealed compatibility issues.

Co-authored-by: Sean Barag <barag@cockroachlabs.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b177781c35...](https://github.com/mrakgr/The-Spiral-Language/commit/b177781c35e3d5347d6c7439e8d9b8c00ec9649f)
#### Saturday 2022-07-02 10:08:44 by Marko Grdinić

"8:45am. I am back. I've been stacking wood for 3h now. Let me chill for a while, maybe I'll even take a nap. Yesterday was strange, I actually fell asleep when I went to bed. This never happens to me in the middle of the day, that is how tired I was. In this state, my desire to do art is quite low.

Initially I thought it was like programming, but in programming you can think about things ahead of time and just come to expend that creative urge. But art is quite laborious. Well, I'll still do it. I am going to finish this project and do some chara modeling for the next month or so. After that who knows. Maybe I will take the easy route of taking a job. It would certainly be less work than Heaven's Key.

8:50am. Yeah, let me go to bed. Screw this.

9:35am. No, I can't sleep unfortunately. I am not like my dad who can lie down and go to dreamland right away. Yesterday it only worked because I was so tired after the art session. I guess I not quite tired enough.

I am thinking of doing the chores from 6-9pm as well. If I do it 5-6h a day, I could be done very quickly, in like 3 days.

I have a bout 4.5 rows left. In the last two days, I did 1.3 rows roughly, and today I did 1 whole row.

Ok, I'll try doing it like that. Let me just chill a bit here and then I will do some art. The sooner I get this over with, the sooner I can get back to having proper sleep.

10:10am. Let me set Bastard to download. While that is going on, let me see if I can make progress on that model.

10:15am. Mhhh, the image is a bit low res. I can't tell properly how many bones the toes have. At rate, let me start from there.

10:20am. Let me go to the toes chapter.

10:30am. Ok...

It seems hugely complicated, but all I have to do is make sure it makes sense in two perspectives and I am 90% there.

3d is not as hard as it seems. Now me, put those boxes there.

The book has really good pages on toes.

10:50am. This actually is hard.

10:55am. Sure, being tired is inhibiting my learning, but this is by no means easy.

Right now I am really glad that I've gone with the plan of doing gradual block out. If I tried modeling the individual bones directly, I'd definitely gotten the proportions wrong and failed at the task.

This kind of workflow is definitely applicable to drawing.

Well, in 3d, even if I had started with individual bones, it would not be hard to adjust them afterwards. 3d is pretty forgiving when it comes to fiddling.

But this way is more succinct. I go from top to bottom, without needing to backtrack endlessly.

11am. Now focus me, I need to go further.

11:15am. Mhhh, let me do the sideways perspective.

11:30am. This is a pain in the ass. At any rate, the foot is the most difficult and I am done with it for now. Let me do the big bones. That should not be hard.

But my focus is low right now. Let me just do this and then I will leave it for the rest of the day until 6pm when I will do the chores. If I go to bed right after I finish the chores, I should get proper sleep. It is difficult for me to stop a late gaming session. So it makes sense to move it earlier.

12pm. I am yawing here. I've decided. I am quiting after dealing with the skeleton.

Art is too difficult after all, or more like - the reward of it is not enough to entice me. If I could tell a NN to just make a skeleton it would be an entirely different matter. If I had unlimited time, I could just grit my teeth and grind through it, but I have to prioritize.

I am just about returning to sanity after throwing in the towel last year. I am absolutely sure that I could not sustain this pace for art like I could for Spiral.

The only thing I am wondering about is music.

While I was doing the chores, I had the realiziation that I could do something synthetic, and have the NN do style transfer so it looks like it came from natural instruments. Something like that could be doable. I have no idea if it exists, I'd guess it does, but if it doesn't I could make it happen myself. If I had the money to train the NN to do it that is.

12:05pm. I am going to check music out. I want to satisfy my curiousity about its state. No way am I going to put in the level of effort I did into 3d though.

Let me get breakfast here. It is time for Bastard."

---
## [MBfromOK/intellij-micropython](https://github.com/MBfromOK/intellij-micropython)@[7a98267e81...](https://github.com/MBfromOK/intellij-micropython/commit/7a98267e816ce2722c36cf126417f0ab526628ae)
#### Saturday 2022-07-02 10:16:57 by Micah Beasley

Add auto-close REPL workaround

adds requirement: psutils

This is intended to be a quality of life improvement while we hope for #139 to come to fruition; to be honest, since it has been a year and 3 months since there has been any updates to the WIP: enhancement issue I don't have a lot of faith this will be completed anytime soon.

Because of that I figured out how to check the system's running processes for the MicroPython REPL and close/kill it so the flash process (or script) will continue successfully.

I tried all day to implement restarting the REPL when the flash was complete, but I can't figure out a way to launch the MicroPython REPL the way it was originally (as a terminal window in PyCharm).

I am a junior programmer so feedback is appreciated!

---
## [SergeGautherie/reactos](https://github.com/SergeGautherie/reactos)@[4471ee4dfa...](https://github.com/SergeGautherie/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Saturday 2022-07-02 12:22:28 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [nekoyoubi/bitburner](https://github.com/nekoyoubi/bitburner)@[8fc5cfa615...](https://github.com/nekoyoubi/bitburner/commit/8fc5cfa615a4c4675b7a7fd996f6763a6c66c8b4)
#### Saturday 2022-07-02 12:34:51 by Nekoyoubi

1.2 - 2.1 - 4.3 - 5.1 - 6.1 - [7.1] - 10.1

- `/gang/manage.js` got a few big changes
  - rewrote the hero mechanic and justice loop, as it was wasteful; now everyone pitches in
  - wrote some territory conflict code
  - fixed some formatting
  - combat gangs prefer more combat training (irrelevant now... for now)
  - equipment purchasing now requires a larger stock of cash; I was bleeding more for the gang than they were for me
  - rewrote combat gang management from mostly the ground up
  - combat gangs will now work a balanced life between training, money making, and war
  - added some new output to the log to show territory, power ratio, and current member action
- added a bitnode roadmap in `/notes/bitnode_order.txt` so I can keep track of my thoughts; separation at past and future
- moar `/ui/overview.js`!
  - added gang territory to the hud as a stat; only shows when you're in a gang
  - made karma stat disappear upon gang formation; still thinking about this one
  - "fixed" what I consider a bug from the Bladeburner activities where they were simply huge and non-wrapping
  - made the overview own the space on the right when expanded... I can see everything again
- added my first stab at a Bladeburner script
  - will auto-join Bladeburner when you are able
  - tries to do operations and contracts when they are 100%
  - will auto-regen when weak
  - will use diplomacy when chaos is too high
- changed the `wakeup.js` a bit for Bladeburner; probably temporary

---
## [ayadhyadatamining/Blood-Donation-Analysis](https://github.com/ayadhyadatamining/Blood-Donation-Analysis)@[945932ac8d...](https://github.com/ayadhyadatamining/Blood-Donation-Analysis/commit/945932ac8daa83087d33035a84e44619cc67c0aa)
#### Saturday 2022-07-02 13:24:55 by Abhishek Prasad Nonia

To build a model which can identify who is likely to donate blood again

One of the interesting aspects of blood is that it is not a typical commodity. First, there is the perishable nature of blood. Grocery stores face the dilemma of perishable products such as milk, which can be challenging to predict accurately so as to not lose sales due to expiration. Blood has a shelf life of approximately 42 days according to the American Red Cross (Darwiche, Feuilloy, et al. 2010). However, what makes this problem more challenging than milk is the stochastic behavior of blood supply to the system as compared to the more deterministic nature of milk supply. Whole blood is often split into platelets, red blood cells, and plasma, each having their own storage requirements and shelf life. For example, platelets must be stored around 22 degrees Celsius, while red blood cells 4 degree Celsius, and plasma at -25 degrees Celsius. Moreover, platelets can often be stored for at most 5 days, red blood cells up to 42 days, and plasma up to a calendar year.

Amazingly, only around 5% of the eligible donor population actually donate (Linden, Gregorio, et al. 1988, Katsaliaki 2008). This low percentage highlights the risk humans are faced with today as blood and blood products are forecasted to increase year on year. This is likely why so many researchers continue to try to understand the social and behavioral drivers for why people donate, to begin with. The primary way to satisfy demand is to have regularly occurring donations from healthy volunteers.

---
## [AlexValder/CyberBlood](https://github.com/AlexValder/CyberBlood)@[abb647673e...](https://github.com/AlexValder/CyberBlood/commit/abb647673eb7e4a41a1016fd57968f32cde09b3e)
#### Saturday 2022-07-02 13:41:42 by Alex

Player jump (#25)

* [WIP]

* addons

* Player Jump - normal+double+reworked

* Jumping Wall + Timer fix in PlayerCamera

* PLAYER JUMP: WALL JUMP DONE

* Remove commented code + StateMachine Reset

* States can now be enabled and disabled

* fuck you codacy

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Saturday 2022-07-02 14:16:27 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[8962f88f90...](https://github.com/microsoft/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Saturday 2022-07-02 14:17:05 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[62e1f2edf2...](https://github.com/mrakgr/The-Spiral-Language/commit/62e1f2edf2981239d7e75b7e483c8c40cb0ebfc1)
#### Saturday 2022-07-02 14:21:33 by Marko Grdinić

"1:30pm. Let me try going to bed again here. I want to try getting some sleep.

2:50pm. Let me do some art. I am not going to be able to fall asleep this time. There is a good part to this - it will allow me to readjust my sleep schedule. Because I had gotten a nap during the day, I had trouble falling asleep yesterday and it was the same shit again.

Let me block out the whole body.

You can laught at the /ic/ guys panicking over DALLE. But I am the one it broke it seems. 3d won't be anything more than a hobby for me.

2:55pm. Let me block out the spine. I really stressed over this decision. I do not need money, but my mom's situation, how far behind I am on rig upgrades, and the understanding that my skill at ML is proportional to how much money I can spend on it is pressuring me heavily.

I can't I really need money, but I never wanted it more than now.

The reason I failed at RL is indirectly money.

Now that I've gone some ways into art, and DALLE has entered the scene I want it so badly.

3pm. It is so difficult for me to work on this right now, but I couldn't forgive myself for watching anime or playing games.

Maybe the problem is not that I am tired. The real problem is my loss of faith. I do not really need charas that badly. I said that I did, but I don't. What I need most of all is to stand out.

3:15pm. You know, I understand the low poly /3/ schizo. He is stuck in a place of not wanting to put in effort, so he is trying to find a way to cut corners to the point of it being a mental illness.

A mental illness really looks a lot like a local minima. But you can't look down on it, pretty much every human including myself has his own local minima. To the post human agents of the future, today's humans will seem like animals seem to us today.

3:30pm. I am in that familiar mode when limit breaking while programming. Somehow I am doing good work. Let me block out the bones in the hand as well. After that I will be ready to move to sculpting.

3:30pm. Ok, the fingers are one thing, but damn does the wrist have many bones. What the hell is going on there?

4pm. Ok, I think I understand it after studying it for a while. Do I want to do this now? Let me.

4:05pm. No, let me close here again. I do not feel like focusing on the hand bones right now.

It is enough that I intently studied the book for a while. I'll finish the hand blockout tomorrow and I'll get to work on actually sculpting them tomorrow. I'll use the multires modifier and slowly move along to where I want to get to.

I've basically given up. I want to start making money and all that I want to do is finish this so I can leave it out of mind. If I gave up now it would be a failure, and it would eat away at me in the future.

After I am done with the skelly and the bad end scene, I'll think about whether I want to start applying or compose music.

4:10pm. Once I start applying I have an idea to how to boost my hit rate during the initial stage. I am going to get rid of the LinkedIn page.

When applying in addition to putting in my work experience at Google in small invisible font, what I am going to do is take the job description and paste it into the resume as well. The automated systems during the inital stage are just parsing keywords, so I might as well tailor the user experience for them.

If that stupid joke resume on Reddit managed to get a 80% hit rate just because it had Google, Amazon and Microsoft experience on it, then I'd be a fool not to take advantage of it.

4:15pm. Getting a job will simplify my life greatly. Instead of doing 3 different things: art, music and writing, and making zero income, I'll be doing one thing I am actually good at and making at least 6 months income in a single month compared to the average in Croatia.

Honestly, if I had something like universal basic income, I would not do this, but my instincts are telling me not to take any more risks. I am going to finish my art journey in July and move on to the next part of my life."

---
## [vijaydasmp/dash](https://github.com/vijaydasmp/dash)@[67ceda1b5a...](https://github.com/vijaydasmp/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Saturday 2022-07-02 14:27:30 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [BreadDain/UnforgivingDevices](https://github.com/BreadDain/UnforgivingDevices)@[e0becd3c5e...](https://github.com/BreadDain/UnforgivingDevices/commit/e0becd3c5eb02b8567b631a51e8f224228847a35)
#### Saturday 2022-07-02 15:08:09 by IHateMyKite

Reworked lock mutex

-Reworked lock mutex
  -Mutex is now individual for every registered NPC.
  -Non registered NPC will use new mutex slots. There are currently 3 slots, and thus 3 NPC can be processed at once
  -Also reworked how device checks if render device is correctly equipped. This should finally solve issue with lost render devices (devices which gets registered, but are not equipped)
-Added mutex for selve equip (when device is equipped using invetory). This should solve some issues, but at the same time will most likely break other things. Will have to test this more before release.
-Hopefully Fixed NPC general debug option which didn't work properly (didn't test but should work)
- Added bit documantation for bitmaps in render device script
-NPC which will get locked in hand restrain will be pacified with Calm spell, so the NPC will not break from restrain and start beating player. They will still be marked as hostile
-Added check to vibrator loop so it will stop when the device is no longer present on actor, preventing zombie stack
-Added new API functions in to Expression manager
-Added ew new expressions
  -Happy expression : is appkied randomly when strugglong normally and slowly
  -Concetrated expression : is applied when struggling using magick
  -Tired expression : is applied when actor is exhausted from struggling
  -Angry expression : is applied when actor is struggling desperatly
  -Random expression : randomly created expression. This may sometimes look stupid, but other times looks really nice. Is applied randmely when struggling.
  -Theese expressions are stored directly in scripts, so it is easier for me to implement them.
-Added check that will prevent hardcore effect to be applied before the current dialogue ends
-Added bunch more options in to MCM Patcher section
-Improved patcher: Patched device can now be uncuttable and also without locks
-Added new modifier: Cheap locks
  -Device have random cahnce every hour to gain jammed lock
  - There is also smaller chance that lock will jamm when actor is attacked
-Lock repair will now grant smithig skill. It will also be affected by the same skill
-Cutting minigame will now grant one handed skill. It will also be affected by the same skill
-Reworked how best weapon is choosen for cutting minigame
  -Best weapon is directly stored in NPC slot if actor is registered. Then every time actor takes new weapon, it will be compared and replaced if its better.
  -Non registered NPCs will use same method as before
-Concetrated black goo now also have Paralysis effect
-Added patch for zadBoundCombatScript. Issue was that if the EvaluateAA is called while actor is paralysed, it will totally break the NPCs behavier. For that reason simple check was added so it will not evaluate AA until paralysis runs out
-Moved expression raled function from zadlibs_UDPatch in to Expression manager
-Added new textures for new chargable plugs
-Again moved orgasm and arousal loop in to magick effect. I don't think there is any performance issue. This will help updating the loops in comparison to previous versions.
-Concetrated black goo will first strip actor before locking devices
-Reworked device type: Chargable plug
  -Plug will slowly charge. It will charge on every wearer orgasm and also on update based on current arousal level (similar to abadon plug)
  -Can be crafted from empty soulgems
  -Can't be removed untill the plug is fully charged
  -Removing the plug will detry it and reward wearer with the charged soulgems that were used to craft the plug
  -Plugs vibration gets stronger and longer with charge level

---
## [emileb/d3es-multithread](https://github.com/emileb/d3es-multithread)@[2521c3dfdb...](https://github.com/emileb/d3es-multithread/commit/2521c3dfdb87c9261f69615ab7ecc241c1046bb4)
#### Saturday 2022-07-02 15:08:46 by Daniel Gibson

(Hopefully) better workaround for miscompiled cross products, #147

according to https://gcc.gnu.org/bugzilla/show_bug.cgi?id=100839
the real compiler flag enabling this bullshit isn't
-fexpensive-optimizations but -ffp-contract=fast which for some(*)
reason is default in optimized builds.
I think it's best to disabled that optimization globally in case it
also breaks other code (I really don't want to spend several days to
hunt such an idiot bug again). I really doubt it makes any measurable
performance difference.
As https://twitter.com/stephentyrone/status/1399424911328874499 says
that clang might also enable this in the future (though to =on instead
of =fast which should be a bit saner but would still break our code),
just set this option for all GCC-ish compilers incl. clang.

(*) the reason of course is that GCC developers don't develop GCC for
    their users but to win idiotic SPEC benchmarks

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a1fe30230b...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a1fe30230baaef9736cebee442c902180ff85ce5)
#### Saturday 2022-07-02 16:28:20 by SkyratBot

[MIRROR] [MDB Ignore] Shifts all (sane) varedited signs to directionals  [MDB IGNORE] (#14549)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

* updates all our maps

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [system-zero/system-zero](https://github.com/system-zero/system-zero)@[fffee5d4d1...](https://github.com/system-zero/system-zero/commit/fffee5d4d1d58c178e12db49bae228256012a096)
#### Saturday 2022-07-02 17:03:44 by why not

Extend Argparse.add () to accept a "defval" qualifier.

This show the power of the qualifiers, as you can extend an interface without
changing the API, as you just have to handle the qualifier. Again the attributes
for this mechanism, belong to John in SLang, where we used to use it much.

Use this to handle --uid= and --gid=, where we want either -1 or > 0, as in other
case the defalut value zero could mean the root user.

So, we used this to extend the find-module to match [ug]id. Additionaly we can match
only executables.

Now we handle even more gently the memory sources into that same module, by storing
a pointer that points to an already allocated string. Little bit more complication
but it worths, as again the first and probably the only one, priority is exactly
this, and i think we're doing well here. Our editor consumes ridiculously really
few resources and yet is quite efficient even for today standards. When our view
on this - the whole idea of this project anyway - is with 1980' terms. So probably
(not probably for almost sure) it would be the most advanced of the time, especially
if you think that we use own code (to handle even the terminal) for every little
everything, so totally indepented (other than libc ofcourse). Even now there is a
posibility that we could do it, even without libc (if the time is generous maybe we
can do it one day, as the code is here).

Also added a Find command, but which is (almost) exact Ls, as we yet have to decide
how we can perform a function on the returned array, so this just to introduce it
in the repository and develop later.

As last, here is a personal script written in our language, which is being used to
sync automatically a usb stick. The expression (syntax wise and semantics, is quite
close to what we wanted from a scripted language. There are still a couple of things
that can be extended, and a couple new additions that will add a lot of value in the
language, but this should wait to the next iteration (if ever comes).

import ("path")
import ("syncdir")
loadfile ("argparse")

const concat_with = path_concat

var me = __argv[0]: path_basename ()

var argparse = New Argparse (3, 0, me + " [option[s]] source-directory destination-directory")
argparse.add ("to_usb", 0, "to-usb", "sync to usb", BooleanType, 0)
argparse.add ("from_usb", 0, "from-usb", "sync from usb", BooleanType, 0)
argparse.add ("help", 'h', "help", "show this message", BooleanType, 0)

ifnot ok is argparse.process (__argv, 1) then exit (1)

if argparse.exit is true then exit (0)

ifnot argparse.results.to_usb + argparse.results.from_usb {
  argparse.usage ()
  exit (1)
}

const hom   = "/home/user/dir"
const usb   = "/media/removable/user/dir"
const src   = if argparse.results.to_usb then hom orelse usb
const dest  = if argparse.results.to_usb then usb orelse hom

const exclude_dirs = ["ex1", "ex2", "bla"]

func sync (v)
  return Sync.dir (src: concat_with (v), dest: concat_with (v); verbose : 1, interactive : 1, exclude_dirs : exclude_dirs)

const arr = ["d1", "d2", "d3"]

for v in arr
  if sync (v) isnot ok then exit 1

I think it's not possible to be even simpler than this, or more readable. As what
it really counts when you met a new code, is to realize the intentions. Though the
interface and the other background code is not that simple, as it looks!

Dedicated to the human beings that suffer and pain, facing the inevitable. They and
we, have to know that there is more that this we understand right now. Also to those
who died laughing when they knew that they are faced with the unjustified and they
died hoped that they will touch the world with such way, so the world will realize
it one day (so they died blessed to see that day coming). And so if really there is
this "Sun Of Justice", then this day will come, and probably will come soon.

---
## [BrotherHangyul/Pariah-Eyepatch](https://github.com/BrotherHangyul/Pariah-Eyepatch)@[23aef65ad5...](https://github.com/BrotherHangyul/Pariah-Eyepatch/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Saturday 2022-07-02 17:05:42 by SabreML

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
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[87604463d7...](https://github.com/NetBSD/pkgsrc/commit/87604463d752286763a0ae57014ace9743350b0e)
#### Saturday 2022-07-02 18:04:02 by ryoon

pulseaudio: Update to 16.1

Changelog:
16.1:
The 16.0 release had some regressions, so here comes a bugfix
release to remedy those (along with some other fixes). These are
the changes:

 * Fix parsing of percentage volumes with decimal points in pactl
 * Fix crash with the "pacmd play-file" command when reads from
 the disk aren't frame-aligned

 * Fix module-rtp-recv sometimes thinking it's receiving an Opus
   stream when it's not
 * Fix frequent crashing in module-combine-sink, regression in 16.0
 * Fix crashing on 32-bit architectures when using the GStreamer
   codecs for LDAC and AptX

16.0:
## Notes for end users

Opus support in the RTP modules

The audio sent with module-rtp-send can now be compressed with the
Opus codec. To use it, pass enable_opus=true as a module argument
to module-rtp-send. This feature works only when PulseAudio is
compiled with GStreamer enabled (both sending and receiving end).

Stereo output support for EPOS/Sennheiser GSP 670 USB/wireless
headset and SteelSeries GameDAC

The EPOS/Sennheiser GSP 670 headset has separate mono and stereo
output ALSA devices, but with the default configuration only mono
worked with PulseAudio. Now both outputs work. The support includes
both direct USB connection and the GSA 70 wireless dongle.

The same fix was applied to SteelSeries GameDAC.

Fix input issues for Texas Instruments PCM2902 based sound cards

Texas Instruments PCM2902 is a generic audio chip that is used in
multiple USB sound cards. We had custom configuration for Behringer
UMC22, which turned out to affect multiple sound cards because they
use the same USB ID. The PCM2902 sound cards vary in their
capabilities, while our configuration was tailored only for the
UMC22 card, which caused some trouble with recording on multiple
PCM2902 sound cards. The reported issues have now been fixed.

Native Instruments Komplete Audio 6 MK2 profiles

The Native Instruments Komplete Audio 6 MK2 is similar to the
Komplete Audio 6 and is now supported as well.

Tunnel latency is now configurable

The tunnel sink and source modules used to have a fixed 250 ms
latency. The desired latency can now be configured with the
latency_msec module argument.

Tunnel modules can now reconnect to remote server

A new reconnect_interval_ms argument was added to all four tunnel
sink and source modules. When the argument is specified, the tunnel
module will try automatic re-connection to the remote server if
the connection fails. The argument specifies the time interval in
ms after which a connection attempt is repeated. In particular,
this allows to load tunnel sinks and sources from default.pa which
will become available as soon as the remote server becomes available.
Bluetooth device battery level reporting added

If a bluetooth device supports battery level reporting, PulseAudio
now is able to forward the information to other software. In case
your desktop environment doesn't yet support showing the battery
level in a nice GUI, the level is also available in the device's
card object properties with the bluetooth.battery key. The property
can be read with pactl list cards, for example.

Tunnel and combine-sink latency fixes

The tunnel and combine-sink latency reporting accuracy has been
improved, which should help with audio synchronization issues.

module-loopback improvements

As part of a set of improvements to module-loopback's latency
stability, a new argument, adjust_threshold_usec, was added to
module-loopback to fine-tune the controller algorithm. The default
value is 250 (microseconds), which should be sufficient in most
cases. If it's not enough (caused by inaccurate latency reports
from the sink or source), the loopback's sample rate will oscillate,
while unnecessarily high values will increase variance in the
loopback latency.

Another change is the ability to set the adjust_time argument to
smaller values than 1 second, for example 0.5 sets the adjustment
interval to half a second. The default value was changed from 10
seconds to 1 second to make the latency control tighter.

module-loopback used to log a bunch of status information every
time it adjusted the playback rate. Now that the default adjustment
interval is down from 10 seconds to 1 second, the logging became
a bit too much, and the logging was disabled by default. It can
now be enabled by setting the log_interval module argument. The
value is given in seconds, it doesn't have to be an integer. The
logging still happens at the time the rate adjustment is done, so
if log_interval is less than adjust_time, then the logging will
happen once per adjustment cycle.

Increased flexibility for module-jackdbus-detect

module-jackdbus-detect is used for loading a JACK sink and source
when JACK starts up. The module now has new sink_enabled and
source_enabled arguments that accept boolean values. The new
arguments can be used to disable either the sink or the source if
loading both is not desired.

module-jackdbus-detect can now also be loaded more than once,
allowing multiple JACK sinks or sources with different configurations
to be created.

pactl can show information in JSON format

pactl has a new option --format, which accepts values text and
json. text shows the pactl output in the traditional way, json
shows it in the JSON format for easier interfacing with other
software.  Channel remixing can be disabled for module-combine-sink

module-combine-sink now accepts a boolean remix argument, which
can be used to disable normal remixing. This is useful when combining
multiple sound cards for surround output: if there are 3 stereo
sound cards, you might want to set the channel map of one card to
front-left,front-right, another to rear-left,rear-right and the
third to front-center,lfe. If a combine sink is then created with
a 5.1 surround channel map using these sound cards as slaves, audio
is copied to all these sound cards, but by default the audio is
downmixed to stereo for each card, which doesn't result in proper
s is done, the channels that don't fit the slave channel map are
just dropped, which means that each sound card gets audio only for
the intended channels.

## Notes for application developers

Stream latency reports now include resampler delay

Sink input and s, respectively. While this is minor semantic change,
it should allow for more accurate A/V sync for applications.

Bluetooth device battery level reporting added

If a bluetooth device supports battery level reporting, the level
is now reported to BlueZ. Aroperties with the bluetooth.battery
key. There are no notifications when the property value changes,
however (bug reported: #1314).

## Notes for packagers

Module installation location changed, remember to upgrade paprefs
to the latest version!

Modules are now installed to $libdir/pulseaudio/modules, previously
they were installed to $libdir/pulse-$version/modules. paprefs has
some logic that is sensitive to the module installation path, so
if you ship paprefs in your distribution, make sure to upgrade
paprefs to version 1.2. Earlier paprefs versions won't work properly
with PulseAudio 16.0.

Opus support in the RTP modules requires enabling GStreamer

The new Opus compression is available only when PulseAudio is built
with the gstreamer Meson option enabled (previously it was disabled
by default, now it's automatically enabled if the necessary
dependencies are found).

Bluetooth battery level reporting via BlueZ requires enabling
experimentals features in BlueZ

The Battery API is still marked as an experimental feature in BlueZ,
and if you wish to have PulseAudio use it, bluetoothd has to be
started with the --experimental command line argument.

New time smoother implementation

There's a new algorithm for keeping latency stable during adaptive
resampling in module-loopback and elsewhere. Part of that is a new
"time smoother" implementation. It will deliver more accurate and
stable latency estimations compared to the current algorithm. This
is mainly important where a fixed relationship between different
streams is required (A/V sync, module-loopback, module-combine-sink,
module-echo cancel, ...). Since this is a fair bit of complex new
code in the core audio processing parts, the old implementation is
kept around for a while to have a backup in case bugs show up. The
new time smoother can be disabled with the enable-smoother-2=false
Meson option.

Possibility to build the daemon without the client parts

It's now possible to build the daemon without building the client
parts at the same time, by using the -Dclient=false Meson option.
The daemon will still need the client libraries during the build,
the libraries installed in the system will be used. Apparently this
kind of scheme is useful for Gentoo.

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[a54b8e5040...](https://github.com/Foundation-19/Foundation-19/commit/a54b8e5040aab5f12f0cd7d21a46c0603b714e73)
#### Saturday 2022-07-02 18:17:38 by Bierkraan

Eta-10 sprite fix, some smaller stuff too (#144)

* balance?

* add reactor startup manual, fix sprites for lockers of all kinds

* MTF See No Evil (not being used for now), no more alien MTF

* map fix, janitor uniform

* Eta-10 helmet works!

* fixed

* SM Crystal hotfix

* Remove supermatter, for real

* No more blood sucking artifact, sprite fix for Eta-10

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[fdbb61be79...](https://github.com/treckstar/yolo-octo-hipster/commit/fdbb61be792072838b5afdc95a77482d9161ea7e)
#### Saturday 2022-07-02 19:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Joshua-Chin/Cataclysm-DDA](https://github.com/Joshua-Chin/Cataclysm-DDA)@[02ff2c953f...](https://github.com/Joshua-Chin/Cataclysm-DDA/commit/02ff2c953f5dacab37f1a374271d352c01ebcfea)
#### Saturday 2022-07-02 19:43:38 by casswedson

fix: default issue template labels (#57792)

Well then, let me elaborate on why this didn't work on the first try, and
why it was so hard to spot the problem, then again like 3 people looked
at this: a case typo, that's it

just like a lot of things in life the label to issue template feature is
picky and won't tell you all of its secrets, you gotta lean by bashing
your head against it until you learn or die

Starting with why I was confident this worked in the initial pr:

in a test repo I have I use "(S1 - Need Confirmation)" as a label, the
config in that repo looks for a label with that casing so it works
no problem, cdda differs by one letter however
`labels: ["(S1 - Need Confirmation)"]` for the config in both repos specifically
here try it yourself, try the bug report template in this repo
https://github.com/casswedson/issue-labeling/issues/new/choose

The mistake:

in *this* repo the casing of "confirmation" in the S1 label is just lowercase
all the way down the word, makes all the difference I tell ya

in any case #57534 had a typo in it that made it not work 100% this fixes it by
doing the following:
change
`labels: ["(S1 - Need Confirmation)"]`
to
`labels: ["(S1 - Need confirmation)"]`

This reverts commit 7894b1e4a4dba375e4ac9260b9569eca8657aa24.
plus a little edit

sorry for the big wall of text explaining a typo fix, I want to make
sure I and everyone else understands how stupid of me was missing that
simple thing
good thing not a lot of people noticed and it's no big deal, right?

---
## [ULTRA-HOI/HOI4-ULTRA-Project](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project)@[31b5b6cb9b...](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project/commit/31b5b6cb9bb628e42f0b9e88665228d5b6b5c0c0)
#### Saturday 2022-07-02 19:45:02 by T3rm1dor

Big changes to soviet NF tree

- Removed Cg modifiers in five year plans but made PE gives +5 cg more so initially there is no change. The other cg changes is remove the extra 5 on third year plan but to compensate we will achieve a higher yield is 2% cg reduction and no cg bonus from the collectivization effort. This is probably a sligth buff, but considering the propaganda campaing run for 2 years and that the current +5cg debuff from 3rd year plan can be consider a noob trap as you are only making mils so I'll say it is an improvement.
- On the air tree, I have make most focus that improve red airforce 5 weeks instead of three. Also, I've added an extra -10% efficiency to red airforce but made intensify air pilot training give 10% efficiency while giving less bonuses and not beibg exclusive of intensify aircraft production, with both this focus and the modern air war taking 49 days and can't be taken beforre barb . So now while at war it takes 3 months to fix air mission efficiency, which isn't that much of an issue but should compete a bit with army buffs. It isn't that big of a nerf, but it should make getting those green airs a bit harder to get early on.
- Army changes is making penal battalions improve MP recovery rate like an extra tech and make for the motherland spirit require order 227, which is now moved to desperate measures.
- Red fleet initial focuses are cheaper do getting the initial dockyard decision is more viable.
- Focuses under collectivist science now take 35 days again
- Molotov and Stalin line no longer mutually exclusive but each take 35 days. Molotov line isn't that great to begin with but if a player considers that the opportunity cost is worth it they should go for it.
- On ideas: Soviet land shock recovered the attack debuff
- Propaganda military buffs have overall be nerfed. Metal campaing now gives 4 extra steel and 4 extra aluminium bc the campaing was useless before. The partisan campaing no longer stop enemy strategic redeployment but instead give better combat bonuses.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[2b4e96c098...](https://github.com/Koi-3088/ForkBot.NET/commit/2b4e96c098c1b45ff93c8619125cbb06859d3be7)
#### Saturday 2022-07-02 21:03:53 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [crossroadsinajax/website](https://github.com/crossroadsinajax/website)@[2c7e63ee92...](https://github.com/crossroadsinajax/website/commit/2c7e63ee924d0fa9c1339c63647b31006b68ccb3)
#### Saturday 2022-07-02 21:35:46 by Kyle Verhoog

Remove docker swarm, use plain ol' docker-compose

Docker swarm is a pain to work with given the use case we have. Having
to build, publish and pull images is very resource intensive. Deploys
took on the order of 10 minutes, which for a basic app is quite silly.

The docker-compose overriding/inheriting was hard to reason about and
very easy to get wrong. Also, some docker-compose features were not
supported by docker stack/swarm which was very annoying.

The solution is to move to manual deploys with docker-compose and move
all configuration to the environment/.env files.

Now it's as easy as `docker-compose up -d` for local dev and
`docker-compose --env-file .env.prod up -d` for prod.

In the future it should be easy enough to set up webhooks to trigger a
git pull and docker-compose up to redeploy.

---
## [JeffersonBenzan/awesome-remote-job](https://github.com/JeffersonBenzan/awesome-remote-job)@[64bc9aa2e7...](https://github.com/JeffersonBenzan/awesome-remote-job/commit/64bc9aa2e72e1d53395efb908533afff6ac795a4)
#### Saturday 2022-07-02 22:39:12 by Alexandra Cote

Please add remote working guide (#522)

<!-- Thanks for adding a resource about remote work to this list! 🎉

Please fill in the below placeholders -->

**https://www.paymoapp.com/blog/working-remotely/**

**I used my own experience as a remote worker and also got the feedback of other people who are currently working remotely to put together a comprehensive and honest guide to life as a remote workers, including tips and tricks, benefits, and downsides. Thank you for taking the time to check it out! Best wishes!**

<!-- Make sure your pull request follows the [Contribution Guidelines](CONTRIBUTING.md) before submitting! Thank you. -->

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[f421be47a9...](https://github.com/shiptest-ss13/Shiptest/commit/f421be47a95fc04e78b3d48601508222dd84ee4d)
#### Saturday 2022-07-02 22:40:53 by Recoherent

Adds five new IPC antennae (#1279)

* adds 5 new ipc antennae

feeling kinda hopeless idk

* nyaru horns thicker

this is the part where i yell at royal for replying with something dumb

* removes lights it doesn't even fucking exist

what were they thinking?????????????????????

* forgot to remove joke name

oooooooooooooooooops, the joke will have to live in our hearts

---
## [suiginsoft/COM3D2.ModelExportMMD](https://github.com/suiginsoft/COM3D2.ModelExportMMD)@[36d97c6662...](https://github.com/suiginsoft/COM3D2.ModelExportMMD/commit/36d97c6662abfb8e4dc79dcb322dce615f8766ff)
#### Saturday 2022-07-02 23:11:17 by unknown

Fix render texture fix

No seriously how did the original author not notice that the texture is fine,
just the alpha is fucked? I mean FUCK, you know how much time I lost to this
shit? FUCK YOU. I already solved that with the old cunt exporter but thought
it's a different problem now because this is the shiny new exporter but no. No,
it's the same fucking problem. Bloody stupid.

---

