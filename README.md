## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-19](docs/good-messages/2022/2022-06-19.md)


1,491,578 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,491,578 were push events containing 2,130,782 commit messages that amount to 111,952,145 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [GsoSoft/Rocket.Chat](https://github.com/GsoSoft/Rocket.Chat)@[5a37518e42...](https://github.com/GsoSoft/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Sunday 2022-06-19 00:54:33 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [SabreML/Skyrat-tg](https://github.com/SabreML/Skyrat-tg)@[01a6ade18c...](https://github.com/SabreML/Skyrat-tg/commit/01a6ade18cfcc1b79e5f5dace05c5e9c1e89b919)
#### Sunday 2022-06-19 01:02:42 by SkyratBot

[MIRROR] Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. [MDB IGNORE] (#13758)

* Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)

About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

* Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs.

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [jkunimune15/elastik](https://github.com/jkunimune15/elastik)@[fbd11a29f0...](https://github.com/jkunimune15/elastik/commit/fbd11a29f0b8976b15c5a39a79ae1521f6cc235d)
#### Sunday 2022-06-19 01:09:00 by Justin Kunimune

Force Method for Improving Distances

I implemented gradient descent.  man, remember that time Richard Gott publishd a paper where it was painfully obvious that he had never heard of gradient descent?  and they publishd an article in Scientific American that he rote about himself and his stupid double-sided map projection.  and I've never even had one customer!

anyway, the gradient descent method is working decently now, tho there are obviously improvements I want to make.  but first there's a minor bug in the mesh generation I want to fix.  after that, I want to see if scaling the gradients will help it converge faster, and I need to have it use the stricter objective function after it converges the first time.

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[3486e808de...](https://github.com/Dudemanguy/mpv/commit/3486e808de7548e69436f8b56ef0ac87493d86ec)
#### Sunday 2022-06-19 01:27:08 by Dudemanguy

x11: support xorg present extension

This builds off of present_sync which was introduced in a previous
commit to support xorg's present extension in all of the X11 backends
(sans vdpau) in mpv. It turns out there is an Xpresent library that
integrates the xorg present extention with Xlib (which barely anyone
seems to use), so this can be added without too much trouble. The
workflow is to first setup the event by telling Xorg we would like to
receive PresentCompleteNotify (there are others in the extension but
this is the only one we really care about). After that, just call
XPresentNotifyMSC after every buffer swap with a target_msc of 0. Xorg
then returns the last presentation through its usual event loop and we
go ahead and use that information to update mpv's values for vsync
timing purposes. One theoretical weakness of this approach is that the
present event is put on the same queue as the rest of the XEvents. It
would be nicer for it be placed somewhere else so we could just wait
on that queue without having to deal with other possible events in
there. In theory, xcb could do that with special events, but it doesn't
really matter in practice.

Unsurprisingly, this doesn't work on NVIDIA. Well NVIDIA does actually
receive presentation events, but for whatever the calculations used make
timings worse which defeats the purpose. This works perfectly fine on
Mesa however. Utilizing the previous commit that detects Xrandr
providers, we can enable this mechanism for users that have both Mesa
and not NVIDIA (to avoid messing up anyone that has a switchable
graphics system or such). Patches welcome if anyone figures out how to
fix this on NVIDIA.

Unlike the EGL/GLX sync extensions, the present extension works with any
graphics API (good for vulkan since its timing extension has been in
development hell). NVIDIA also happens to have zero support for the
EGL/GLX sync extensions, so we can just remove it with no loss. Only
Xorg ever used it and other backends already have their own present
methods. vo_vdpau VO is a special case that has its own fancying timing
code in its flip_page. This presumably works well, and I have no way of
testing it so just leave it as it is.

---
## [abarnes1/curriculum](https://github.com/abarnes1/curriculum)@[9c740aacfa...](https://github.com/abarnes1/curriculum/commit/9c740aacfa82b3abb39345c2f6fe042c271ca711)
#### Sunday 2022-06-19 03:00:06 by BMT-z

Add section for warnings about branch diversions

From personal experience and what I've seen in the git-help channel it seems like a few people are struggling with the issue of branch diversion, I'm still doing the html foundations and didn't realize making changes to my readme file via GitHub would cause the branch diversion issue, I think in git basics it should state that making any changes to your files via GitHub can cause issues and if you want to change even the readme file it's best to do it via a commit and push, I'm aware this is covered later on but i still believe making this a note in the git basics section would help a lot of users from running into this issue.

---
## [ehkarabas/exprograms](https://github.com/ehkarabas/exprograms)@[2b3b3cf4e8...](https://github.com/ehkarabas/exprograms/commit/2b3b3cf4e80357fc3ce1c21c62b6cd5c3641c076)
#### Sunday 2022-06-19 03:08:21 by Huseyin Karabas

Create Coffee Machine

Coffee Machine Program Requirements

1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

a. Check the user’s input to decide what to do next.

b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

2. Turn off the Coffee Machine by entering “ off ” to the prompt.

a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.

3. Print report.

a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

4. Check resources sufficient?

a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.

b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”

c. The same should happen if another resource is depleted, e.g. milk or coffee.

5. Process coins.

a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.

b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

6. Check transaction successful?

a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.

b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.

7. Make Coffee.

a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.

---
## [gwern/gwern.net](https://github.com/gwern/gwern.net)@[b15d702dc9...](https://github.com/gwern/gwern.net/commit/b15d702dc91c269c8a25520562a8592d5b391282)
#### Sunday 2022-06-19 04:01:42 by gwern

LM: tags: look for cross-tag double-nesting tags - seems to catch too many due to liberal see-also use, so doesn't work as-is as a lint. hm...
Example output:
...,("https://www.nature.com/articles/s41598-019-44324-x",("Breed differences of heritable behaviour traits in cats",["cat/genetics","cat/psychology","genetics/heritable"])),("https://www.nature.com/articles/s41598-019-45619-9#deepmind",("",["reinforcement-learning/model/alphago","reinforcement-learning/multi-agent"])),("https://www.nature.com/articles/s41598-020-75622-4",("Evening home lighting adversely impacts the circadian system and sleep",["melatonin","zeo"])),("https://www.nature.com/articles/s42003-018-0078-7",("Construction of arbitrarily strong amplifiers of natural selection using evolutionary graph theory",["genetics/selection/artificial","reinforcement-learning/exploration","reinforcement-learning/multi-agent","sociology"])),("https://www.nber.org/papers/w29676",("Robots and Firm Investment",["economics/automation","reinforcement-learning/robot"])),("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4509557/",("Lithium in drinking water and suicide mortality: interplay with lithium prescriptions",["lithium","psychiatry"])),("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4520322/",("The Mechanics of Human Achievement",["psychology/energy","psychology/personality/conscientiousness","psychology/willpower"])),("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6867811/",("Predictability and Uncertainty in the Pleasure of Music: A Reward for Learning?",["music","psychology/novelty"])),("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8588667/",("Does the combination of resistance training and a nutritional intervention have a synergistic effect on muscle mass, strength, and physical function in older adults? A systematic review and meta-analysis",["creatine","exercise"])),("https://www.newyorker.com/magazine/2011/10/03/personal-best",("Personal Best: Top athletes and singers have coaches. Should you?",["psychiatry/meditation","psychology","sociology"])),("https://www.newyorker.com/magazine/2011/11/21/crunch",("Crunch: Building a better apple",["genetics/cloning","genetics/selection/artificial/apple"])),("https://www.newyorker.com/magazine/2019/04/15/the-age-of-robot-farmers",("",["economics/automation","technology"])),("https://www.newyorker.com/magazine/2019/09/30/paging-dr-robot",("",["economics/automation","technology"])),("https://www.nngroup.com/articles/aesthetic-usability-effect/",("The Aesthetic-Usability Effect",["design/visualization","technology"])),("https://www.nytimes.com/2013/09/08/magazine/poker-computer.html",("",["reinforcement-learning/imperfect-information","reinforcement-learning/multi-agent"])),("https://www.nytimes.com/2019/07/02/magazine/dead-pig-brains-reanimation.html",("Scientists Are Giving Dead Brains New Life. What Could Go Wrong? In experiments on pig organs, scientists at Yale made a discovery that could someday challenge our understanding of what it means to die.",["biology","cryonics","psychology/neuroscience"])),("https://www.nytimes.com/2020/01/07/magazine/hologram-musicians.html",("",["ai/music","music"])),("https://www.nytimes.com/2021/07/11/world/europe/carrara-italy-robot-sculptures.html",("",["economics/automation","technology"])),("https://www.pnas.org/content/114/47/12590.full",("Three-dimensional visualization and a deep-learning model reveal complex fungal parasite networks in behaviorally manipulated ants",["ai/nn","biology","psychology/neuroscience"])),("https://www.pnas.org/doi/full/10.1073/pnas.2120887119",("DNA methylation clocks for dogs and humans",["genetics/heritable/dog","genetics/sequencing","longevity/epigenetics"])),("https://www.quantamagazine.org/cells-form-into-xenobots-on-their-own-20210331/",("Cells Form Into \8216Xenobots\8217 on Their Own: Embryonic cells can self-assemble into new living forms that don\8217t resemble the bodies they usually generate, challenging old ideas of what defines an organism",["biology","cs/cellular-automaton"])),("https://www.quantamagazine.org/the-busy-beaver-game-illuminates-the-fundamental-limits-of-math-20201210/",("How the Slowest Computer Programs Illuminate Math\8217s Fundamental Limits: The goal of the 'busy beaver' game is to find the longest-running computer program. Its pursuit has surprising connections to some of the most profound questions and concepts in mathematics",["cs/computable","math","philosophy/logic"])),("https://www.ribbonfarm.com/2012/03/08/halls-law-the-nineteenth-century-prequel-to-moores-law/",("Hall's Law: The 19<sup>th</sup> Century Prequel to Moore's Law",["economics/automation","technology"])),("https://www.sciencedirect.com/science/article/pii/S0167268119302641",("Predicting mid-life capital formation with pre-school delay of gratification and life-course measures of self-regulation",["economics","psychology/personality/conscientiousness"])),("https://www.sumsar.net/blog/2015/01/probable-points-and-credible-intervals-part-two/",("",["reinforcement-learning/exploration","statistics/bayes","statistics/decision"])),("https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/",("The simple but ingenious system Taiwan uses to crowdsource its laws: vTaiwan is a promising experiment in participatory governance. But politics is blocking it from getting greater traction",["design/visualization","law","sociology/technology","statistics"])),("https://www.technologyreview.com/2020/02/17/844721/ai-openai-moonshot-elon-musk-sam-altman-greg-brockman-messy-secretive-reality/",("The messy, secretive reality behind OpenAI\8217s bid to save the world: The AI moonshot was founded in the spirit of transparency. This is the inside story of how competitive pressure eroded that idealism",["ai/clip","ai/nn/transformer/gpt/dall-e","ai/nn/transformer/gpt/jukebox","ai/scaling","reinforcement-learning/openai","reinforcement-learning/robot"])),("https://www.technologyreview.com/2021/08/06/1030802/ai-robots-take-over-warehouses/",("",["economics/automation","reinforcement-learning/robot"])),("https://www.theatlantic.com/newsletters/archive/2022/04/shania-twain-creativity-one-hit-wonder/629569/",("A Stanford Psychologist Says He\8217s Cracked the Code of One-Hit Wonders: What separates Blind Melon from Shania Twain?",["music","psychology/novelty"])),("https://www.theguardian.com/technology/2022/mar/29/artificial-intelligence-beats-eight-world-champions-at-bridge",("",["reinforcement-learning/imperfect-information","reinforcement-learning/multi-agent"])),("https://www.theverge.com/2021/7/6/22565448/waymo-simulation-city-autonomous-vehicle-testing-virtual",("",["ai/nn/gan","reinforcement-learning/robot","reinforcement-learning/safe"])),("https://www.usenix.org/system/files/conference/woot16/woot16-paper-wustrow.pdf",("DDoSCoin: Cryptocurrency with a Malicious Proof-of-Work",["bitcoin","cs/cryptography"])),("https://www.vanityfair.com/style/2012/01/prisoners-of-style-201201",("",["music","psychology/novelty"])),("https://www.wired.co.uk/article/deepmind-alphago-zero-nature-reinforcement-learning",("DeepMind's latest AI breakthrough is its most important yet: Google-owned DeepMind's Go-playing artificial intelligence can now learn without human help... or data",["ai/scaling","reinforcement-learning/model/alphago"])),("https://www.wired.com/story/ai-helps-warehouse-bots-pick-new-skills/",("AI Helps Warehouse Robots Pick Up New Tricks: Backed by machine learning luminaries, Covariant.ai's bots can handle jobs previously needing a human touch",["economics/automation","reinforcement-learning/meta-learning","reinforcement-learning/robot"])),("https://www.wired.com/story/dog-poodemic-robots-drones/",("",["economics/automation","technology"])),("https://www.wired.com/story/robots-are-fueling-the-silent-ascendance-of-the-electric-motor/",("",["economics/automation","technology"])),("https://www.wired.com/story/you-can-now-buy-spot-the-robot-dog/",("",["economics/automation","technology"])),("https://www.wsj.com/articles/the-robots-are-coming-for-garment-workers-thats-good-for-the-u-s-bad-for-poor-countries-1518797631",("",["economics/automation","reinforcement-learning/robot"])),("https://www.youtube.com/watch?v=QyJGXc9WeNo&list=PLOXw6I10VTv9HODt7TFEL72K3Q6C4itG6&index=3",("",["reinforcement-learning/meta-learning","reinforcement-learning/model-free/oa5","reinforcement-learning/robot"])),("https://www.youtube.com/watch?v=SVcsDDABEkM",("",["ai/clip/samples","ai/nn/transformer/gpt/dall-e"])),("https://xkcd.com/2565/",("Latency",["economics/automation","technology"])),("https://xkcd.com/915/",("",["culture","psychology/novelty"])),("https://yang-song.github.io/blog/2021/score/",("",["ai/anime","ai/diffusion","ai/nn/gan/stylegan"]))]

---
## [eun0115/android_kernel_samsung_m20lte](https://github.com/eun0115/android_kernel_samsung_m20lte)@[92e6cafc8c...](https://github.com/eun0115/android_kernel_samsung_m20lte/commit/92e6cafc8cb44376d74e9b00e7c2dd04eec8fe37)
#### Sunday 2022-06-19 04:09:11 by Dave Chiluk

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

---
## [projects-nexus/android_kernel_lavender-4.19](https://github.com/projects-nexus/android_kernel_lavender-4.19)@[38b0bd0f25...](https://github.com/projects-nexus/android_kernel_lavender-4.19/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Sunday 2022-06-19 04:43:16 by Linus Torvalds

gpiolib: acpi: use correct format characters

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

---
## [crawl/crawl](https://github.com/crawl/crawl)@[e8bc28a0cf...](https://github.com/crawl/crawl/commit/e8bc28a0cf5eb223156f893c8f47b1284931e78a)
#### Sunday 2022-06-19 05:31:51 by DreamDust

vaults: float vaults by DreamDust

dreamdust_dug_too_deep

The dwarves dug a little too deep and unearthed... a Balrug! Even a
mighty dwarf hero (with a potentially good weapon to loot!) fell in
battle to the demon. RIP. Maybe this is why we don't see deep dwarves
much anymore. Hmmmm...

The idea behind this vault is to place a single Balrug early enough that
it's a serious (but not unmanageable) threat. I added a downhatch close
by if players need to escape in a hurry. There are also warning signs in
advance (all the dwarf corpses and the suspicious volcanic floor tiles
outside the Balrug room).

[ Committer's note: Added a runed door for the balrug, adjusted
  transparency, traded volcanic floor for blood. ]

dreamdust_wu_jian_sword_trials

A Wu Jian-themed vault. Challenge three increasingly powerful
sword-wielders for their increasingly good swords.

[ Committer's note: Adjusted depth range, added monsters to the earlier
  trial, trimmed arenas, added transperency. ]

dreamdust_merry_men

Inspired by Robin Hood and his band of merry men. Features a forest with
a bunch of archers and a good bow and aides to banditry to loot in the center.

[ Committer's note: Adjusted layout to prevent teleport closets, monster
  counts, loot. ]

dreamdust_tengu_aerie

A large nest of tengus. They keep their shiny loot in the center...
along with their fledglings (wait, are we the baddies??).

[ Committer's note: moved the crystal walls to the middle, put the
  rock wall on the outside (so the reavers can bolt bounce their
  omnibolts), and thinned the monster density. ]

dreamdust_hydra_shepherd

A shepherd is raising a flock (?) of hydras down in the Depths! Some
players might regret abandoning their flaming weapons after finishing
Lair/Swamp, haha.

[ Committer's note: upgraded the cyclops to a stone giant, added a small
  chance for a really high head count. ]

dreamdust_elfheim

The home of Duvessa and Dowan.
The more-practical Duvessa has training dummies in her room, while the
vain Dowan has a large mirror to admire himself with.

[ Committer's note: cut down on custom tiling/colouring a bit. ]

---
## [PastaPastaPasta/dash](https://github.com/PastaPastaPasta/dash)@[67ceda1b5a...](https://github.com/PastaPastaPasta/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Sunday 2022-06-19 05:38:25 by fanquake

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
## [flygarn12/realtek-poe-10mp](https://github.com/flygarn12/realtek-poe-10mp)@[0f8c27e4f4...](https://github.com/flygarn12/realtek-poe-10mp/commit/0f8c27e4f438efd565a218a63c7ecbfaa5d4e71c)
#### Sunday 2022-06-19 08:49:38 by flygarn12

realtek-poe: De-suckify "poe sendframe" command

Typing "0x" repeatedly in a string of numbers that's obviously
hexadecimal is painful. So don't use sscanf(), which forces the "0x"
prefix. Instead, use strtoul() in base 16. This accepts numbers with
and without the prefix.

Also, if the string we receive is crap for whatever reason, don't try
to send it to the PoE controller. Just throw it the fuck out.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a4975f9238...](https://github.com/LemonInTheDark/tgstation/commit/a4975f92380a9509029bb200b068b32e8a970b28)
#### Sunday 2022-06-19 09:23:17 by LemonInTheDark

Adds logic to human overlays to allow for updating their planes "in place"

Ok so like, doing a full update would be too expensive, so instead we're
gonna create a list of all the overlays that either have a unique plane,
or have a child with a uniuqe plane

Then we walk up that list to remove overlays, and down it to add
Cause of the overlay flattening biz and all

Note: What I want to do in the end is store a copy of this list over
each iteration, rather then recalcing it each z change.

I can't atm tho, because when I try to I end up in fucky hell
Basically, overlays are weird, and there's something funky goin on.
I've seen behavior where appearances were pulled from the void, and
applied to the mob

Scares me

---
## [DasOakster/h-rider-haggard_allan-quatermain](https://github.com/DasOakster/h-rider-haggard_allan-quatermain)@[074f43ecad...](https://github.com/DasOakster/h-rider-haggard_allan-quatermain/commit/074f43ecad18d3dce8b328b67c308cf4fdba769c)
#### Sunday 2022-06-19 09:39:19 by Andy Oakley

Proof Read: Non-Editorial Changes

Proof Read: Introduction:

Removed italics from 'never' in 'you will never, while the world endures'
Restored 'And so in my trouble' back to 'And so in my great grief'
Restored 'for ever and ever' to 'forever and ever'
Removed capitalisation from 'Political Economy'

Proof Read: Chapter 1

Added emphasis back to 'curious moral ascendancy'

Proof Read: Chapter 2

ostrich-feathers -> ostrich feathers
food-supplies -> food supplies

---
## [TallerThanShort/ddxd](https://github.com/TallerThanShort/ddxd)@[facfb7fa67...](https://github.com/TallerThanShort/ddxd/commit/facfb7fa673ec088d275f5c9b015ea002eda130a)
#### Sunday 2022-06-19 09:44:11 by TTS

holy fuck how does this shit even work wtf

i genuinely dont understand how the dude who made this made it...

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[a297304eff...](https://github.com/yogstation13/Yogstation/commit/a297304effcf85d7ba9828021df218ffea8f51b3)
#### Sunday 2022-06-19 09:48:42 by LazennG

makes some of the recent megafauna drops less shit (#14455)

* this is everything i think idk it's 330am

* polishes some things for now therell probably be more later

* Update miscellaneous.dm

* fuck it critical heal

* you're able to the body entirely

---
## [Axlefublr/Personal](https://github.com/Axlefublr/Personal)@[c0fd413856...](https://github.com/Axlefublr/Personal/commit/c0fd413856ca754d2b556fb173bd47efad870409)
#### Sunday 2022-06-19 10:47:41 by Axlefublr

Small rewrite of \`Script\`; Snippet to make an _onExit function; Cis() makes the current window fully non-transparent; `+!e` while viewing an ahk file in vs code now copies the file`s path into your clipboard and opens the compiler; FullDateAndTime() returns the date in year.month.day hour:minute; Function that gets the full titile of the currently playing song on spotify; Function that lets you added an artist you`re listening to with the date and time next to it. ; I used to mark new discovered artists in the calendar, but having a nice list is better.; I was thinking of making it so it refused to add an artist if you`ve discovered them already, but if I`m doing that, I either forgot so much that I don`t remember the music anyway or decided to give them an another chance, in which case I`d want that to be shown in the list still.; Send to Kristi is now in runner instead of the hotkey;

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[9813e53f3f...](https://github.com/yogstation13/Yogstation/commit/9813e53f3fa719cc23c32a89d1bf96d8b76be299)
#### Sunday 2022-06-19 11:12:06 by 00ze-cyclone

remove one space (#14472)

I think it might fix everything, if it does then holy shit I want HC

---
## [EtraIV/MerchantStation13](https://github.com/EtraIV/MerchantStation13)@[33027699b9...](https://github.com/EtraIV/MerchantStation13/commit/33027699b9b12d2a5be75965dd1c985194abf14c)
#### Sunday 2022-06-19 12:05:44 by EtraIV

Fixes escaping the DM(I hope) Part 2: Fuck you Lunaman edition (#283)

* Fixed the hole in the wall on maint mania

* Why did you add a window here lol

---
## [LunarWatcher/upm](https://github.com/LunarWatcher/upm)@[3dd8ee6a70...](https://github.com/LunarWatcher/upm/commit/3dd8ee6a7042696d816d2dbb0260b9fae9bad68a)
#### Sunday 2022-06-19 14:00:24 by Olivia

Stage one pi compatibility

Worked out installation, and I should in theory have that up and
running. Fucked up on which arm version was selected for node, but
that's a quickfix.

Haven't tested activation because I'm dumb, forgot which version I just
installed, and the lack of @latest symlinks/tracking is starting to
annoy me.

Should also start tracking which versions are actually installed. Not
sure if that's better suited for metadata, or if that's something
I'll just compute at runtime. Not particularly performant, especially if
the underlying file system is shit, but that's a problem for me to
figure out when I start diving into this rabbit hole.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5da682dc6a...](https://github.com/treckstar/yolo-octo-hipster/commit/5da682dc6a328c03b3cc5758badcc5a7b5ff7d36)
#### Sunday 2022-06-19 14:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [DasOakster/h-rider-haggard_allan-quatermain](https://github.com/DasOakster/h-rider-haggard_allan-quatermain)@[bc6e6a7bab...](https://github.com/DasOakster/h-rider-haggard_allan-quatermain/commit/bc6e6a7bab84589cf3b18826ae9063c3132e161c)
#### Sunday 2022-06-19 14:58:22 by Andy Oakley

Proof Read: Non-Editorial

Proof Read: Introduction

Changed 'And so in my trouble' back to 'And so in my great grief'

Proof Read: Chapter 1

Added emphasis back to 'curious moral ascendancy'

Proof Read: Chapter 2

ostrich-feathers -> ostrich feathers
food-supplies -> food supplies

Proof Read: Chapter 3

Minor punctuation changes

Removed italics from magnum opus

---
## [louiznk/deploy-sith](https://github.com/louiznk/deploy-sith)@[6db2afae81...](https://github.com/louiznk/deploy-sith/commit/6db2afae81ae63e06fd61ee7f77880c6661c4d9a)
#### Sunday 2022-06-19 15:55:59 by Louis Tournayre

Sheriff Chameleotoptor sighed with an air of weary sadness, and then
turned to Doppelgutt and said 'The Senator must really have been on a
bender this time -- he left a party in Cleveland, Ohio, at 11:30 last
night, and they found his car this morning in the smokestack of a British
aircraft carrier in the Formosa Straits.'
		-- Grand Panjandrum's Special Award, 1985 Bulwer-Lytton
		   bad fiction contest.

---
## [matthiasbeyer/config-rs](https://github.com/matthiasbeyer/config-rs)@[142eaca531...](https://github.com/matthiasbeyer/config-rs/commit/142eaca5310365a1bc89c8b59e9b98892624b5dc)
#### Sunday 2022-06-19 16:25:08 by Matthias Beyer

Remove "watch" example

This patch removes the "watch" example. The idea should be straight
forward to a decently experienced rust dev, and (to be honest) I am too
lazy right now to update the example for the removed (because
deprecated) interfaces.

Shame on me.

If someone wants to provide this example again, I'm happy to see this
patch reverted and the example adapted. ;-)

Signed-off-by: Matthias Beyer <mail@beyermatthias.de>

---
## [sadguitarius/surge](https://github.com/sadguitarius/surge)@[66cfdde3a7...](https://github.com/sadguitarius/surge/commit/66cfdde3a74f5d304069709ea4b5a1735abd2994)
#### Sunday 2022-06-19 16:42:09 by Paul

Send Param Automation for Filter Subtypes (#6269)

Paramter Automation messages were not sent because
basically filter subtypes are kinda screwed in how we
implement them both GUI wise and model wise. It's all a hack.
Anyway added an explicit send automation call and now when you
toggle through with clicks you end up getting the DAW showing changes.

My theory is this is the problem in #6264 but will wait for user
confirm before we close it.

---
## [ringy9/fakedataapp](https://github.com/ringy9/fakedataapp)@[8cd21d67e7...](https://github.com/ringy9/fakedataapp/commit/8cd21d67e71baed092a74907624e0fc5831aac6d)
#### Sunday 2022-06-19 17:17:55 by ringy9

Delete DONT CALL FRIDAY NIGHT FUNKIN AT 3AM! (EVIL BOYFRIEND PRANK!) (online-audio-converter.com).mp3

---
## [lnx00/Fedoraware](https://github.com/lnx00/Fedoraware)@[5a23d95aca...](https://github.com/lnx00/Fedoraware/commit/5a23d95aca96005b454a9a9b75ba2ac9ae603c83)
#### Sunday 2022-06-19 17:25:12 by Johnathon Walnut

Merge pull request #380 from femboy-boop/patch-2

fuck you baan

---
## [nzceo/rpg-framework](https://github.com/nzceo/rpg-framework)@[e9daf22035...](https://github.com/nzceo/rpg-framework/commit/e9daf22035b0f129dba73985188b60bd29a51d19)
#### Sunday 2022-06-19 18:08:32 by nzceo

feat: Improved interface (#6)

* initial commit

* More improvements

* Removed unused variable

* Improved dialog stuff

* Fixed tests

* Typescript is dumb

* Ignore refs, fuck you

* Ignoring more refs

---
## [Sangram0001/1.-Create-a-TXT-record-in-your-DNS-configuration-for-the-following-hostname-_github-pages-challenge](https://github.com/Sangram0001/1.-Create-a-TXT-record-in-your-DNS-configuration-for-the-following-hostname-_github-pages-challenge)@[aabc07238b...](https://github.com/Sangram0001/1.-Create-a-TXT-record-in-your-DNS-configuration-for-the-following-hostname-_github-pages-challenge/commit/aabc07238b411faaba8968459be567bd0dd7afea)
#### Sunday 2022-06-19 18:08:44 by SANGRAM CHOWDHURY

CONTACT ME

"Myself Sangram Chowdhury. I was born & brought up in Purulia. I have done my schooling from Derozio Young Bengal School & Chittaranjan High School. I have Completed my graduation in Bachelor of Tourism Studies + Bachelor in Hotel Management from INTERNATIONAL SCHOOL OF HOSPITALITY MANAGEMENT,KOLKATA. I Love to Travel a lot,Love to Make new friends & Hangout with them. Social Media surfing is one of my best hobbies. I know Maximum about Tech Related Resolutions. I'm the founder of iCONIC PRODUCTION, Which is a YouTube Channel. I know Videography, Photography, Video & Photo Editing, Audio Distribution, Website Designing, Social Media Handling etc. I'm quite Confident Towards My Work & Life. If u want to know more about me then ping me. TNX."

---
## [TheFinalFrontierBruno/Naruto_Ninpou](https://github.com/TheFinalFrontierBruno/Naruto_Ninpou)@[006170dccc...](https://github.com/TheFinalFrontierBruno/Naruto_Ninpou/commit/006170dccc681881c09ca424f50cd362eb790e4f)
#### Sunday 2022-06-19 18:22:13 by RandomTales

random

chain lightning procing mirror
rikdou madara meteor bugging spells
neji and hinata r sometimes not silencing
hyuuga byagukans falling off sometimes
hanzo mirror procing on q
 reduce the animation between the indra arrow exploding and stunning, atm you can jump and chakra jump after the fact that it hit and u will still get stunned/dmged
Taka sasuke W damage is fucked
hashirama can no longer walk over cliffs

---
## [danton-nlp/factual-beam-search](https://github.com/danton-nlp/factual-beam-search)@[c6a181c1fa...](https://github.com/danton-nlp/factual-beam-search/commit/c6a181c1fa94c5b77d283a4736c398738f830873)
#### Sunday 2022-06-19 19:23:00 by Daniel Levenson

Correct some out-of-source annotations

* don't think these effect summary factuality

remaining annotations that were labeled intrinsic, even though they are
actually technically out of source from an NER perspective:

```bash
$ python audit_annotations.py
Using custom data configuration default
Reusing dataset xsum (/Users/daniel/.cache/huggingface/datasets/xsum/default/1.2.0/32c23220eadddb1149b16ed2e9430a05293768cfffbdfd151058697d4c11f934)
100%|███████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 144.84it/s]
count of out-of-source possible bad annotations: 8
count of in-source possible bad annotations: 0
count of total summaries annotated: 708
---
IN SOURCE POSSIBLE BAD ANNOTATIONS
set()
---
OUT OF SOURCE POSSIBLE BAD ANNOTATIONS
{ ( '30457745',
    'Ghanaian duo The Busy Twist have released a new dance track called '
    "'Dance, Dance, Dance' which they say has captured the spirit of the "
    'country.',
    '{"ent": "Ghanaian", "type": "NORP", "start": 0, "end": 8, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '30457745',
    'With the release of their latest single, The Busy Twist, Ghanaians Ollie '
    'Williams and Ohene Agyapong decided to take their music to the streets of '
    'the capital Accra.',
    '{"ent": "Ghanaians", "type": "NORP", "start": 57, "end": 66, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '30760966',
    "The drugs expert at the centre of the'superman' ecstasy scandal has told "
    'the Global Drugs Survey it\'s "not safe" to take pills with the logo on '
    'them.',
    '{"ent": "the\'superman", "type": "WORK_OF_ART", "start": 34, "end": 46, '
    '"in_source": false, "label": "Non-hallucinated"}'),
  ( '33262593',
    'A World War Two fighter jet that was used in the Gulf War has been put up '
    'for sale by two ex-RAF engineers.',
    '{"ent": "World War Two", "type": "EVENT", "start": 2, "end": 15, '
    '"in_source": false, "label": "Intrinsic Hallucination"}'),
  ( '34474416',
    'A migrant camp set up at Dismaland has been moved after organisers '
    'decided not to send it to the UK.',
    '{"ent": "UK", "type": "GPE", "start": 97, "end": 99, "in_source": false, '
    '"label": "Intrinsic Hallucination"}'),
  ( '35723757',
    'Two British tourists have been arrested at the Machu Picchu '
    'archaeological site in Peru, police say.',
    '{"ent": "Two", "type": "CARDINAL", "start": 0, "end": 3, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '35811486',
    'Byron Rhodes, the leader of Derbyshire County Council, is talking about '
    'seizing an opportunity in a crisis.',
    '{"ent": "Derbyshire County Council", "type": "ORG", "start": 28, "end": '
    '53, "in_source": false, "label": "Intrinsic Hallucination"}'),
  ( '39784504',
    'A Cornwall newspaper has accused the Conservatives of being "archaic" and '
    '"20th-Century in the way its journalists covered Prime Minister Mr  visit '
    'to the Cornish village of Helston.',
    '{"ent": "20th-Century", "type": "DATE", "start": 75, "end": 87, '
    '"in_source": false, "label": "Intrinsic Hallucination"}')}
```

---
## [Bouteillebleu/echoes](https://github.com/Bouteillebleu/echoes)@[f94bc79016...](https://github.com/Bouteillebleu/echoes/commit/f94bc79016d7bcbff7334122d1ea0eddf0b1a28f)
#### Sunday 2022-06-19 19:30:14 by Bluebottle

Initial testing of django-allauth

Changes are based on https://wsvincent.com/django-allauth-tutorial/.

The /example page loads with the correct CSS, but /accounts/logout
and /accounts/login don't, which isn't surprising as they are using
their default templates.

Next tasks to do:
* Plan what to do with django-invitations next.

There's also some site design I want to do - what are the pages / views
that we're serving? Can we at least have a decent index page after login
for "here are things you might want to do, go and do them"?
I'm going to take inspiration from Aquarion's design for
https://dagon.church/ in that regard.

---
## [LZ1WS/Before_The_Dead_Slashers_Revamped](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped)@[4acb5a06f0...](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped/commit/4acb5a06f00b54365625cf2f946c15df9a753a1a)
#### Sunday 2022-06-19 19:41:28 by LZ1WS

Survivor Expansion Update

#"From all around the world" Survivor Expansion Update#
| Added |
- New Survivors:
  - Drake
#A medical officer with extensive experience in his specialty. Not a fan of listening to instructions and, for the most part, self-taught, trusting his criteria for assessing the condition of patients. Nevertheless, he copes well with his work, which proves the effectiveness of his methods#
  - Theodore
#A survivor using a boombox to distract attention. Has only one 'Box' with him, therefore, and one chance to get rid of unnecessary attention for a certain time.#
- Bear Traps for Sheldon

| Changed |
- Frost Magic SWEP for Tirsiak
- F4 GUI redesign
- Simons description was rewritten
#A sense of danger and intuition are not the words that can describe your peculiarity in the ability to detect an approaching threat.\n Darkness and troubles seem to find you by themselves. The constant feeling of persecution and observation by otherworldly beings has affected your mental state.\n You can use it to see the world through the eyes of a creature.#
- Removed surnames from Survivors that had them
- Changed name of the gamemode in menu BTD Slashers Revamped
- Changed GM.Github and GM.Workshop in shared.lua

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[9428d97a4f...](https://github.com/RandomGamer123/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Sunday 2022-06-19 19:50:46 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [heig-vkaelin/mcr-project](https://github.com/heig-vkaelin/mcr-project)@[c875e150ab...](https://github.com/heig-vkaelin/mcr-project/commit/c875e150ab0dd020e9d81a80075e55aa41f34947)
#### Sunday 2022-06-19 20:23:31 by Maxime Scharwath

Howard Shore composed, orchestrated, conducted and produced the trilogy's music. Shore visited the set in 1999, and composed a version of the Shire theme and Frodo's Theme before Jackson began shooting.[48] In August 2000 he visited the set again, and watched the assembly cuts of The Fellowship of the Ring and The Return of the King.[49] In the music, Shore included many (85 to 110) leitmotifs to represent various characters, cultures and places—the largest catalogue of leitmotifs in the history of cinema, surpassing, for comparison, that of the entire Star Wars film series. For example, there are multiple leitmotifs just for the hobbits and the Shire. Although the first film had some of its score recorded in Wellington, virtually all of the trilogy's score was recorded in Watford Town Hall and mixed at Abbey Road Studios.[30] Jackson planned to advise the score for six weeks each year in London, though for The Two Towers he stayed for twelve.[50]

The score is primarily played by the London Philharmonic Orchestra, ranging from 93 to 120 players throughout the recording. London Voices, the London Oratory School Schola boy choir, and many artists such as Ben Del Maestro, Sheila Chandra, Enya, Renée Fleming, James Galway, Annie Lennox and Emilíana Torrini contributed. Even actors Billy Boyd, Viggo Mortensen, Liv Tyler, Miranda Otto (extended cuts only for the latter two) and Peter Jackson (for a single gong sound in the second film) contributed to the score. Fran Walsh and Philippa Boyens served as librettists, writing lyrics to various music and songs, which David Salo translated into Tolkien's languages. The third film's end song, "Into the West", was a tribute to a young filmmaker Jackson and Walsh befriended named Cameron Duncan, who died of cancer in 2003.[51]

Shore composed a main theme for the Fellowship rather than many different character themes, and its strength and weaknesses in volume are depicted at different points in the series. On top of that, individual themes were composed to represent different cultures. Infamously, the amount of music Shore had to write every day for the third film increased dramatically to around seven minutes.[51] The music for the series has been voted best movie soundtrack of all time for the six years running, passing Schindler's List (1993), Gladiator (2000), Star Wars (1977) and Out of Africa (1985), respectively.[52]

---
## [ElementsOfJustice/Automation](https://github.com/ElementsOfJustice/Automation)@[a57b77ba2b...](https://github.com/ElementsOfJustice/Automation/commit/a57b77ba2b7bb052ef8dd14d863a369984819e73)
#### Sunday 2022-06-19 20:30:24 by ExodexoDev

emotionEngine 6/19/22

Redid the database format to not suck ass while also being compatible with JSFL. At this stage I should be free to compile all poses from 2-3 onwards, yay

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[763a10d1cc...](https://github.com/Y0SH1M4S73R/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Sunday 2022-06-19 20:45:52 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [The-Best-Boi-Project/The-Best-Boi-Project](https://github.com/The-Best-Boi-Project/The-Best-Boi-Project)@[40cb3da450...](https://github.com/The-Best-Boi-Project/The-Best-Boi-Project/commit/40cb3da450443943c306b147d5def0b77edda922)
#### Sunday 2022-06-19 21:36:06 by julian poelmann

Added Lore, fixed a lot of links, fuck you mobirise

---
## [chazizgrkb/squarebracket](https://github.com/chazizgrkb/squarebracket)@[d694d0f4c1...](https://github.com/chazizgrkb/squarebracket/commit/d694d0f4c15ece45ad53864f43af8dc8dc0dd251)
#### Sunday 2022-06-19 22:14:48 by Chaz "Gamerappa" Péloquin

move shit around as a means of testing design

i honestly don't know what the fuck am i doing

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[8c5288577c...](https://github.com/Zeodexic/tsorcRevamp/commit/8c5288577c7dfb327602d539705b5aa0c0327f80)
#### Sunday 2022-06-19 22:15:36 by RecursiveCollapse

Many changes

Tetsujin now only fire their sweeping laser at players who are close, and fire their projectile attack in bursts

Fixed many bosses dropping double loot in expert mode

Blocking bosses from dropping loot is super fucking annoying now, so the blocked items are now just disabled until a later boss is defeated instead, with a tooltip indicating what boss to kill to re-enable them.

Fixed stamina drops not dropping

King Slime can now drop its hook and saddle. The hook is disabled as mentioned before, and the saddle doesn't matter because there are multiple new routes on the map that intentionally let players skip the starting jump barrier anyway

Our boss bags have new visual effects, kinda like the vanilla ones

---

