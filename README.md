## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-13](docs/good-messages/2022/2022-01-13.md)


1,646,287 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,646,287 were push events containing 2,681,522 commit messages that amount to 203,628,813 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 23 messages:


## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[e9652d465a...](https://github.com/willior/Action_RPG_1/commit/e9652d465ac380afc8317f3e077decdda870aa95)
#### Thursday 2022-01-13 00:09:11 by willior

refactored formula display in pause menu

previously, the Formula Elements which populated the "Alchemy" section were made up of several different nodes, which were all configured and added as children separately. i've consolidated the different elements so that only one node needs to be instanced. the different elements are:
1. the Button
2. the "item", which displays information based off of FormulaData and formula_reference (ie. the spell's current level, and its cost)
3. the XP bar
all 3 were instanced into a single node "MenuFormula" which is instanced and configured per formula when the Pause Screen is opened.
next i should figure out how to sort the Formula screen. it looks like i can comfortably fit 10 formula items on screen at once (2 columns of 5 formulas). i was thinking that the maximum number of formulas a Player could carry would be 8 or 10, so this should work out.
other than that i've been tuning the Pause Screen even more. working with menus seems endlessly time-consuming. they need to be set up so specifically to work, and once they are set up, it becomes almost impossible to alter parameters and attain a desirable outcome. i realize that the only way i'll get better at this is to continue practicing, but menu programming isn't fun nor rewarding so it's frustrating.
the first pause screen just displayed text strings of the names of the stats and their values, and that took forever to figure out, so i guess i should be at least a little bit happy with where the pause screen has gone. but the code is very spaghetti-like and it's frustrating to work with. anyways, i'll likely end up re-doing the pause screen/menu from scratch at some point.
the next thing i should figure out is how to automatically sort the Formula list into something desirable. so if you have 5 formulas or less, it would display as it does now. but if you have more than 5, we shift the first column over to the left, and start adding the 6th and additional formulas to the second column. i'll see if i can get a preliminary start on getting that done now.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a2fa7799f3...](https://github.com/tgstation/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Thursday 2022-01-13 00:10:24 by Jeremiah

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
## [SpookyTheFox/Skyrat-tg](https://github.com/SpookyTheFox/Skyrat-tg)@[90a7aaff28...](https://github.com/SpookyTheFox/Skyrat-tg/commit/90a7aaff286b5bde4e93b9cb8e4675f3e9be5893)
#### Thursday 2022-01-13 01:54:20 by SkyratBot

[MIRROR] Reduces the move delay buffer to 1 tick, fixes "Flash stepping" (Is that what the kids are calling it?) [MDB IGNORE] (#10013)

* Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

* Reduces the move delay buffer to 1 tick, fixes "Flash stepping" (Is that what the kids are calling it?)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ArunParambath/Quality-mindset](https://github.com/ArunParambath/Quality-mindset)@[e156bd2b56...](https://github.com/ArunParambath/Quality-mindset/commit/e156bd2b56d6d2f0fd4277c748c307bbe3d315e3)
#### Thursday 2022-01-13 02:57:55 by Arun p

Delete Quality Mindset.txt

Quality Mindset.
_________________

Quality is a mindset that impacts everyone. It is more than a process or programme to be implemented by workers
 on an assembly line.  It impacts every decision we make, and isn't just limited to the workplace—it impacts us 
at home, work and school.It is the difference between being "good enough" and the best you can be.Quality is an 
age-old concept. Aspiring for the best has been a dominant impulse of humanbeings across civilizations. That is
why we have meticulously built great bath of Indus Valley Civilization or pyramids of Egypt. All the seven monumental 
wonders of the world or hundreds of heritage sites across the world are living examples of human desire for greatest
level of perfection.In modern context, quality has been defined by scholars and practitioners in various ways.Reeves 
and Bednar (1994) define quality as “… value, conformance to specifications,conformance to requirements, fitness for
 use, loss avoidance, and meeting and/or exceeding customers’ expectations.” 

The four pillars required to have a quality mindset
> Vision
> Empathy
> Commitment
> Adaptability

Vision - According to Stephen Covey Vision is the portable version of Covey's "The 7 Effects of Highly Effective People".
This book is full of inspirational and humorous quotes. There's no instructions, no how-tos and no formulas for success.
Instead you will find thought-provoking ideas , workable solutions , insight , and humor from some of the world's most 
influential and inspiring people. Even if you don't want to read the original book, the "Vision" book will encourage you
 to learn valuable lessons of life. 

Empathy - Empathy is the ability to emotionally understand what other people feel, see things from their point of view, and
imagine yourself in their place. Essentially, it is putting yourself in someone else's position and feeling what they must
be feeling.When you see another person suffering, you might be able to instantly envision yourself in the other person's   
place and feel sympathy for what they are going through.While people are generally pretty well-attuned to their own feelings
and emotions, getting into someone else's head can be a bit more difficult. The ability to feel empathy allows people to "walk
a mile in another's shoes," so to speak. It permits people to understand the emotions that others are feeling.For many, seeing
another person in pain and responding with indifference or even outright hostility seems utterly incomprehensible. But the fact
 that some people do respond in such a way clearly demonstrates that empathy is not necessarily a universal response to the
 suffering of others.

Commitment - Making a commitment involves dedicating yourself to something, like a person or a cause. Before you make a commitment,
think carefully. A commitment obligates you to do something.Some commitments are large, like marriage. When you take a job, you're
making a commitment to show up and do the job well, and your employer makes a commitment to pay you. There are smaller commitments 
too. If you said you'd meet a friend at six, that's a commitment — show up or your friend will be mad. You also can speak of commitment
as a quality. Staying after school for a study group shows your commitment to good grades.

Adaptability - Adaptability (Latin: adaptō "fit to, adjust") is a feature of a system or of a process. This word has been put to use 
as a specialised term in different disciplines and in business operations. Word definitions of adaptability as a specialised term differ
little from dictionary definitions. According to Andresen and Gronau[1] adaptability in the field of organizational management can in 
general be seen as an ability to change something or oneself to fit to occurring changes. In ecology, adaptability has been described 
as the ability to cope with unexpected disturbances in the environment.

---
## [alisonfel/wiredtiger](https://github.com/alisonfel/wiredtiger)@[24d35561e3...](https://github.com/alisonfel/wiredtiger/commit/24d35561e328e6568992bcafa18a560d56688185)
#### Thursday 2022-01-13 03:31:37 by Keith Bostic

WT-5521 Cache stuck during format initial load, configured with library checkpoints (#5233)

* If reconciliation requires multiple blocks and checkpoint is running we'll eventually fail.
It's possible this is a big page that will take a lot of writes, avoid wasted work.

* Quit doing so much work in format's read-scan, it's not that useful any more and we're have already
verified the load.

* Configuring WiredTiger library checkpoints is done separately, rather than as part of the
original database open because format tests small caches and you can get into cache stuck
trouble during bulk load. Imagine a single thread doing lots of inserts and creating huge
leaf pages. Those pages can't be evicted when there are checkpoints running in the tree and
the cache gets stuck. That workload is unlikely enough the library can't handle it, and we
configure it away here.

---
## [tombomba/tombomba.github.io](https://github.com/tombomba/tombomba.github.io)@[77665cba07...](https://github.com/tombomba/tombomba.github.io/commit/77665cba07f23869201fbe1d29641df5360dde1b)
#### Thursday 2022-01-13 03:34:18 by Tom Bomba

name change fuckin hell this editor can be a pain in the goddamn ass

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[947c6998ca...](https://github.com/i3roly/glibc_ddwrt/commit/947c6998ca7f353bdbdb50d42f7e5dbd3e7da4e1)
#### Thursday 2022-01-13 04:42:31 by gagan sidhu

4.14.261/v48119.MT_WIFI5.1.0.0+UI tweaks+softether. "why work when you can autotune?" - randy marsh

- the wifi driver has been updated to 5.1.0.0. the performance is noticeably better.
  thanks to @paldier for catching an error i thought i had checked.

- i've added lib/gconv for the big builds (2640/3040) and also set the environment
  variable GCONV_PATH for the 867/878/882 builds to /usr/local/lib/gconv

- consequently, big builds now have a recent (but not latest, since static
  sodium is causing a headache) version of softether, and i have also added
  it to the lootbag.

- i've added the 'SGI' suffix to the wireless client's 'mode', and also
  STBC if that is reported.

- also, i've fixed the situation where the terminal loses its previous title
  after sshing into the router, which left a 'root@DD-WRT ~' after logging out.
  the title of the originating shell is now restored.

- less important: updated util-linux to 2.37.2 and glib, for no
  particular reason.

an update on the randy marsh contract negotiations: he is driving a hard
bargain and, given we are a company that does nothing, these demands are
difficult to meet. at the risk of disappointing our fans, we recommend
viewing the current stalemate as irreconcilable.

we maintain our interest in marsh's proposal of using autotune to
operate under the guise of doing absolutely nothing and praise him
for boldly challenging the very definition of uselessness that
penetrates to the core of what it is to be a redskin, however we must
be pragmatic.

and OFC, redskin fans: G F Y

        -the MFin 'skins

* Shelly's room, evening. Randy knocks on her door *

Randy
        Shelly, that's enough time on your phone.

Shelly
        Leave me alone, Dad! Stop nagging me all the time!

Randy
        You know we're all cutting down on phone time.

Shelly
        [sits up]

        Don't limit me! You don't even understand me!

Randy
        [sees a poster of himself as <'famous' "musician">,
        his secret identity]

        Yeah. I don't understand you at all. A lot you know.

        [walks away saddened]

        *   The Marsh garage    *

*  Randy is adding more stacks of cash to those already  *
*    hidden behind the poster. A door opens and Randy    *
*            quickly seals it up.                        *

* He gets to his workbench just as Stan closes the door. *

Stan
        Uh hey Dad. I need to talk to you.

Randy
        Oh really? A-About... about what?

Stan
        Dad, is it possible for someone to be one way on
        the outside but totally different on the inside?

        [Randy sighs deeply and stands up to walk]

        I mean, can someone identify as one sex but be
        something else but still have it be nothing about sex?

Randy
        Yes. Yes, Stan. I am <'famous' "musician">.

Stan
        ...What?

Randy
        It started off so simple. There's a guy at work. Hanson.
        He would use the bathroom and just blow the thing up, you know?
        Not only that, but he was in there all the time! I finally got
        fed up and pretended to be a woman.
        I called myself <'famous' "musician">. Have you ever been in a
        woman's bathroom, Stan? It's all clean and there's enough stalls
        for everyone. It was so freeing. I started singing while I was
        in there, and then I- started writing things down.

Stan
        Well you said you knew a guy at work who was
        <'famous' "musician">'s uncle.

Randy
        Yah, that's my cover.

Stan
        The chick that wrote the theme song to the new
        <shitty recession stimulus-funded book and movie series>, is you?

Randy
        Yeah.

        [turns around and faces Stan]

        The record company messed it all up. It was supposed to go:

            "<shitty recession stimulus-funded book and movie series>,
            yah yah yah, yah yah yah! <shitty recession stimulus-funded
            book and movie series>."

        But they just- do what they want with my songs.

Stan
        Wha-wait, <'famous' "musician"> sounds like a girl.

Randy
        Autotune. Wanna see how I do it?

        [moments later, a music program pops up.
        Twelve tracks are shown at lower left]

        I come up with all my best stuff in the bathroom at work.

        I use this program to import the recordings I make on my phone.

        [plays the highlighted track]

            "Yeah yeah, feeling good on a Wednesday. Sparklinnnnn'
            thoughts. Givin' me the hope to go ohhhn"

            [farts and poop noises]

            "Oh! Whoa. What I need now is a little bit of shelter."

Stan
        Dad, <'famous' "musician">'s music is actually really good.

Randy
        Thanks.

        But it gets even better when I add the drum loops.

        [replays the same track with drum loops added]

        Then with the computer I can actually quantize everything.

        [brings up the quantizer and chooses his settings]

        Backup instruments.

        [scale, beats, bass, tambourine, guitars, strings]

        And then finally I use the Autotune.

        ["Auto-Tuner v10." He chooses his settings there, and
        the song is transformed. The same track is now enhanced
        with <no name shitty "musician">'s voice and no trace of Randy]

            "Sparklin' thoughts, feelin' good on a Wednesday.
            Givine me the hope, givin' givin' me the hope to go ohhhn.
            What I need is a little bit of shelter."

        [this is all too much for Stan to take in, and he passes out.]

        [Randy notices]

        Stan?

---
## [ppp-project/ppp](https://github.com/ppp-project/ppp)@[81ad945630...](https://github.com/ppp-project/ppp/commit/81ad945630120cc1c27c8bb00503be42b76ff202)
#### Thursday 2022-01-13 06:38:06 by Jaco Kroon

Expand byte count statistics to 64 bits (#298)

* Add Gigawords to radius packets where applicable.

IMPORTANT NOTE:  The ioctl() only supports 32-bit counters.  In order t
obtain 64-bit counters, these are now pulled in from sysfs (it's assumed
to be mounted on /sys which I'm assuming is standard).

It is unknown whether sysfs will be available everywhere, as such, keep
the ioctl() method in place, but attempt to detect wrap-overs.

If the sysfs mechanism fails, fail back to the ioctl().

Given maximum data rates, the intervals between calling this needs to be
such that no more than 4GB (2^32) bytes are sent or received in any
given interval.  Mostly important for radius plugin where data
accounting may be in effect.

Towards this, a timer interval on 25 seconds is set to force a ioctl()
poll irrespective of the rate of stats update calls.  This may be
important for especially radius that needs to provide interim-update
intervals, if the interim updates is too long and the counters could
wrap-over twice in a single interval.  At 25 seconds we should detect
all wraps up to an effective data rate of 1.37Gbps, which for my
purposes is adequate.

Possible downsides, 4 files are opened, read and closed every time
statistics is requested.  This results in 12 system calls every single
time statistics is required, compared to 1 for the ioctl.  Efficiency is
unknown, but as a rule of thumb fewer system calls are better, this is
however not a critical path in my opinion, so should not be a problem.
If required I can run a few benchmarks using gettimeofday() to measure
actual impact.

Signed-off-by: Jaco Kroon <jaco@uls.co.za>

* Use netlink if possible to obtain 64-bit stats.

This uses two system calls per round.

This should be preferred where available.  It seems the RTM_GETSTATS was
only added from 2016 some point (4.7.0 as per pali), which is in my
opinion old, but given experience with certain embedded systems does
need to be supported.

Signed-off-by: Jaco Kroon <jaco@uls.co.za>

Co-authored-by: Jaco Kroon <jaco@iewc.co.za>

---
## [jdcampolargo/content](https://github.com/jdcampolargo/content)@[546c0de66a...](https://github.com/jdcampolargo/content/commit/546c0de66a519812a8415c34b2ab50b6a12d3cb7)
#### Thursday 2022-01-13 07:01:48 by jdcampolargo

Possible edits

Here are some, others are edited into the edited essay. 

Edits
nation state --> nation-state
million person --> million-person
in land --> inland
by ocean -> by the ocean
And there are many pieces of Indonesia that are --> any pieces of Indonesia
for the purposes of forming contracts or adjudicating --> to form contracts or adjudicate
datacenter --> data center (maybe better?)
An enclave is a state that is fully landlocked --> An enclave is a fully landlocked state
That’s because during the rise of the modern Westphalian nation state --> That’s because, during the rise of the modern Westphalian nation-state
territory --> the territory
gain right --> gain the right
cloud first --> cloud-first
everyone need --> everyone needs
founding a company, or --> founding a company or
From today’s perspective this --> From today’s perspective, this
zero-to-one attempt actually works --> zero-to-one attempt works  
So you can actually sell --> So you can sell
would transitions --> would transition
You join a network state, and remain a citizen.You join a network state and remain a citizen.
but it has a number of important implications --> but it has several important implications.
51% democracy --> 51% democracy, 
In this sense the --> In this sense, the
when we we actively seek founders --> when  we actively seek founders
communist dictatorship --> by a communist dictatorship
tech billionare --> tech billionaire
found a billion dollar --> found a billion-dollar
the the distance between ->  the distance between
It’s true that Russia’s borders have --> Russia’s borders have indeed
distance-griven --> distance-driven
physical invisiblity --> physical invisibility
open source projects --> open-source projects
delete "actually" in most places 
real-time regulator --> real-time regulator
afffiliate revenue --> affiliate revenue
many mechanism to --> many mechanisms to
temporarily embarassed --> temporarily embarrassed
idiosyncracy --> idiosyncrasy


Edited Essay:

The Network State
A proposition is not a nation, though it can become one. Here we describe a peaceful, reproducible process for turning an online community premised on a proposition into a physical state with a virtual capital: a network state, the sequel to the nation-state.
A network state is a social network with a recognized founder, an integrated cryptocurrency, a definite purpose, a sense of national consciousness, and a plan to crowdfund territory. The state formation process begins with a founding influencer, who organizes the online community that eventually buys land in the physical world. Crucially, that land is not necessarily contiguous. In fact, by default, it’s distributed all over the world.
To understand what a network state looks like, and how it differs from a traditional nation-state, take a look at Figure \ref{fig:the-network-state-dashboard}. As this dashboard shows, a network state is composed of network nodes, each of which represents a group of digital netizens who have chosen to live together in the physical world.

The dashboard also demonstrates a key property of the network state: quantified growth. The series of snapshots in Figures \ref{fig:ns1}-\ref{fig:ns1m} shows how the network state formation process can begin with a single founding influencer and scale to a million-person physical community. The Network State founder’s task is as simple (and as difficult) as recruiting a community online that is capable of crowdfunding and coliving inland around the world.







Essentially, just like a tech company or a social network, the network state provides a smooth path from a single person with a computer and no other resources to a million-person global network. The difference is that a network state is more ambitious. It’s meant to start on the internet and become a peer to sovereign countries, just like Bitcoin started on the internet and became a peer to sovereign currencies.
Something of that scale has many facets. We can variously think of the network state as an archipelago of interconnected enclaves, a country you can start from your computer, a group defined by geodesic over geographic distance, a city-state in the cloud, a territory one can acquire but not conquer, a union of sovereign collectives, a band that defends cloud before land, a community aligned around cryptographic consensus, a state that recruits like a startup, a body based on math above science, a list of citizen journalists, a culture of crypto creators, a civilization that values digital civility, an organization of optimalists, an asymptotically automated administration, a ROC-based realtime regulator, a citizenry centered on single sign-on, a polity that prizes choice alongside voice, a 100% democracy instead of a mere 51% democracy, a society funded by subscription and seignorage, and a nation built from the internet rather than disrupted by it.
Whew! That’s quite a list. Each of these brief definitions illuminates a different aspect of the network state. Let’s go through each of them in turn.
An Archipelago of Interconnected Enclaves
Why might the distributed, discontiguous state shown in Figure \ref{fig:the-network-state-dashboard} even be workable? As motivation, start by looking at the nation states of Southeast Asia on a map (Figure \ref{fig:southeast-asia}).

Several of these countries are clusters of islands separated by the ocean. The obvious mapping of one island per entity doesn’t apply. The boundaries aren’t even close to clean convex sets. And many pieces of Indonesia are closer to, say, Malaysia than to other pieces of Indonesia.
Still, on top of this messy geography people have nevertheless superimposed the conceptual abstraction of nation-states. The people within the geographic boundaries of a nation-state as delimited on a map are subject to the same laws. If they are citizens, they may have logins on the same government services. And to form contracts or adjudicate disputes, this jurisdictional proximity takes precedence over mere geographical proximity.
That is, whether two people are citizens of the same abstract nation-state is often more material than whether two people are just physically close to one another. A given Indonesian may be physically closer to a given Malaysian than to another Indonesian 100 miles away, but the Indonesian state binds the two Indonesians together through a common set of laws, a common currency, a common school system, a common military, a common flag, and so on. The abstract - might we say the virtual? - dominates the concrete, the physical.
What if we extended this concept? What if those islands were separated not by the ocean, but by the internet — and scattered all around the world? That’s a glimpse of what a network state looks like. Contemporary precedents include coworking communities, crypto meetups, and the offices of large tech companies like Google: globally distributed, networked real estate gated by the common login of a corporate account.

One difference[fn:1] is that while Google’s real estate is mainly restricted to office and data center space, a network state’s footprint includes community-owned residential and commercial real estate. Each piece around the world is connected to a community with its center on the internet, forming an archipelago of interconnected enclaves.
That word - enclave - is worth underlining. An enclave is a fully landlocked state, surrounded by other states on all sides without access to the ocean. The key observation is that the internet increases the value of networked enclaves, of globally distributed pieces of territory that aren’t physically contiguous.
Why? When you visualize a map of the nation-states of the world, you realize that individual enclaves aren’t very common anymore. That’s because, during the rise of the modern Westphalian nation-state, enclaves became far less viable. Once cartography advanced to the point that maps were widely distributed and the territory became legible, once it became technologically feasible to first define something as abstract[fn:9] as a national border and then to enforce it, the people within an enclave found themselves at a disadvantage. They needed to gain the right of passage from the enclosing state to trade or travel to other locales. Over time, it became easier for enclaves to simply merge with their enclosing state, rather than be cut off from the world.
Note that an entity like Portugal with access to the ocean is not considered an enclave, even if it appears otherwise enclosed. Why? Because the ocean was the first peer-to-peer network. The modern nation-state of Portugal can send ships to Portuguese-speaking regions like Brazil or Macau without going overland through the modern nation-state of Spain. Spain cannot prevent Portugal from doing so as interdicting ocean travel is much harder than interdicting overland travel. So in a sense, Portugal was networked to other territories by the ocean.
What the internet does is put a port (in the digital sense) on every device, so it can connect to each other just as the ports (in the oceanic sense) of every maritime power connected its territories together. That port-to-port connection opens the door for the network state, increasing the value of an archipelago of interconnected enclaves.
A Country You Can Start From Your Computer
The Improbability of Starting a Currency
In 2008, if you’d walked into the office of a conventional investor and said that you wanted to found a new currency from your computer, you’d have gotten stares and guffaws.
What are you going to do, petition the IMF? The World Bank? Oh, and your imaginary internet money is going to be decentralized, and deflationary, huh? You do know that Paul Krugman proved that deflation could never work, that it’d cause liquidity traps, and even if your crazy scheme did it’d be shut down by the government immediately. Take a look at an Econ 101 textbook, and get out of my office.
Of course, Satoshi Nakamoto managed to create Bitcoin without any investment at all[fn:8]. But this is roughly the reaction you’d get today if you expressed a serious interest in starting a new country. And in fairness, while of course new countries have been started at various points in history, there have also been many half-baked attempts. So rational skepticism is warranted.
A Path for Founders, and a Path for Citizens
With that in mind, let’s suspend disbelief and start from first principles. An important feature of the modern era is that you can boot up a tech company, an online community, or even a cryptocurrency from a laptop. Can we generalize this process of founding beyond companies, communities, and currencies to cities and even countries?
A key concept is to start cloud-first, land last - but not land never. That is, start by founding a community online and then work on materializing it in the physical world by crowdfunding territory.
Note that not everyone needs be a founder of a network state. If we think about the current world, anyone can choose to become a founder of a company, community, or currency at any time, thereby taking on the immense stress and risk of trying to build something from scratch. Alternatively, they can choose to remain a “citizen” and be gainfully employed by a founder — or by a vehicle that a founder once created, whether that be a tech founder like Larry Page or a founding father like George Washington.
The network state model is similar. There is a path for founders of network states and a path for citizens. Anyone can switch between these paths at any time, just like you can (a) go from being a Google employee to taking on the insanity of founding a company or (b) transition from founding a company to selling to Google, hanging up the cleats for a time, and enjoying the easy life as an employee.
In other words, between any two moments in time, all four of the following transitions are possible:
Citizen to Founder. You begin gathering an online community, write up a founding document, create a cryptocurrency, and declare your intent to found a network state. From today’s perspective, this seems quixotic. But think again about Satoshi Nakamoto’s plan to start a new currency in 2009, and how utopian it seemed at the time. If the process of instantiating the first network state meets with success, if this zero-to-one attempt works, it will eventually become a template: anyone can start a country from their computer, beginning by building a following.
Founder to Citizen. You may not want to remain a founder forever. Heavy lies the crown! As we will see, unlike modern nation-states, but like historical ones, network states are built for full or partial M&A. So you can sell some or all of a network state to another network state, much as a large REIT might sell some of its properties to another REIT. A sale of this kind would transition the logins of all your citizens to a new system. Or you can shut it down, ideally with some notice, such that your citizens/users have time to switch citizenship over to another network state.
Citizen to Citizen. You join a network state and remain a citizen. Or you acquire dual citizenship, or N-th citizenship, in another network state - usually by buying and holding a sufficient amount of that network state’s coin, as well as satisfying other requirements like participation and civility. Different network states may have different reciprocity provisions, just like nation-states and social networks do[fn:2]. For example, a US passport allows you to enter some countries, but not others. And Quora allows you to login with Facebook or Google, but not vice versa. Similarly, citizenship in one network state may give partial access to another network state.
Founder to Founder. You continue running the network state you founded, or you sell or shut it down and start a new one. Perhaps the first such state is focused on quantified self, while the second is on life extension. Just like Evan Williams created Blogger, then Twitter, then Medium - all iterations on a theme, each informed by the previous one - it may be possible for a suitably talented administrator to do the Plymouth Colony, then Boston, then Massachusetts all within one lifetime. It’s analogous to an ambitious politician starting as mayor of a city, then governor of a state, and then becoming president of a country. But think of this as the v1, v2, and v3 of communities rather than companies. In this context, the history of mid-1800s American communes is highly relevant.


This takes much of the strain off the question of “who will lead a network state”? It’s like asking the question of who will be the CEO of a tech company. It could be you. You have the right to try taking on that immense responsibility if you want, when you want, should you want - or to politely demur, as is your wont.
An Abundance of Leaders, Not an Absence Of Them
The concept of empowering anyone to transition back and forth from network state founder to citizen as they see fit might seem obvious, but it has several important implications.
Among other things, it offers a pragmatic alternative to the three leading ideological positions of the day - Woke Capital (NYT), Communist Capital (CCP), and Crypto Capital (BTC) - as the network state is neither bureaucratic oligarchy nor communist autocracy nor crypto-anarchy.
100% Democracy, not 51% Democracy. First, when anyone can become a network state founder or switch citizenships, that’s not an argument against democracy, it’s an argument for more of it. It’s about more individual input, more consensual government, and more international inclusiveness. Put another way, it’s a case for 100% democracy, rather than a mere 51% democracy. Because in the 100% democracy of a network state, all the citizens in a jurisdiction have freely chosen the founder by signing a social smart contract upon entry. By contrast, in the status quo of a 51% democracy, we see the barest possible level of democratic assent, and a corresponding grudging reluctance by 49% to bend to coercion by the other 51%. In this sense, the network state is an alternative to the bureaucratic oligarchy imposed by NYT in the name of democracy.
Legitimate Leadership, not Communist Dictatorship. Second, when anyone can become a network state founder but must attract citizens, that’s not an argument against competent leadership. It’s an argument for legitimate leadership, leadership that citizens have freely chosen, much as they freely work for a CEO or vote for a president. It’s leadership without dictatorship: anyone can declare themselves a leader of a network state, and see whether they can build a following, just like they can declare themselves founder of a tech company and see whether they can build a product valuable enough to fund employees. The alternative is the non-consensuality of imposed direction by a communist dictatorship, the CCP model, where China’s international cities and greatest entrepreneurs are being crushed in the name of making China great on the international stage.
Crypto-Civilization, not Crypto-Anarchy. Third, when we actively seek founders, rather than reject them on principle, that’s not an argument against decentralization, it’s an argument for crypto-civilization over crypto-anarchy. It’s a recognition that Satoshi was a leader, Washington was a leader, Gandhi was a leader, Lee Kuan Yew was a leader, and Herzl was a leader. And that a stably decentralized world requires an abundance of leaders, not an absence of them, lest a highly organized centralized empire overwhelm a group of disorganized crypto-anarchists that reject the very concept of leadership.
Thus, at least conceptually, the network state embraces democracy, leadership, and decentralization while avoiding the failure modes of oligarchy, dictatorship, and anarchy. There are no royal titles either; there’s no hereditary monarchy, no newspaper nepotists, PRC princelings, or corporate feudalists at the head of things. A leader earns their way to the top, generating enough value for their digital citizens - or seeing them leave for another network state given the ease of exit. And a key to it all is that fluidity of transition: a network state is a country you can start from your computer, so anyone can go from citizen to founder.
96% of the World Can’t Become President, But 100% Can Found A Network State.
The idea that anyone can become a founder of a network state is a vision of global equality of opportunity. It is the modern version of Jefferson’s natural aristocracy. And it’s an improvement over America’s legitimating myth that “anyone can become president of the United States”, which isn’t really true, as only ~4% of the world is American and only a subset of those satisfy the age, birth, and residency requirements to become president.
So long as the US still rules the world, this means that most of the people the US rules cannot themselves rise to rule the US. In fact, once we realize that there have been only 46 US presidents (all of whom are American), but that there are thousands of billionaires (most of whom are now not American, we realize that it is /much more realistic/[fn:5] to become a tech billionaire than to become US president.

Similarly, now that Satoshi made it possible to start a new digital currency, it is much easier to found a new cryptocurrency than to become head of the Federal Reserve. The American establishment would never have picked Vitalik Buterin over Jerome Powell, but the young Canadian is on key dimensions a far more accomplished macroeconomist than the American sexagenarian. Buterin founded an economy, while Powell simply inherited one.
So, instead of the false hope of getting elected US president, a role available only to 46 people in history, or the even more difficult path of becoming Fed Chair, an opportunity for only 16 appointees, one can much more realistically found a billion-dollar company or coin from one’s computer.
By extending this concept, we allow anyone in the world with an internet connection (which will soon be everyone) to become not just a tech founder, or a protocol founder, but a network state founder. Whether the next Washington is Brazilian, Indian, Nigerian, or Eastern European, this mechanism lets them rise to global leadership. It permits a positive-sum avenue for the politically ambitious. But, again, it also allows anyone who doesn’t desire the stress of leadership or just doesn’t desire it at this point, to simply remain a citizen and pick from their available nation and network state jurisdictions.
A Group Defined By Geodesic Over Geographic Distance
Snapchat lies on a straight line with the dissolution of the nation-state. Why? Because people are sharing intimate moments with others 3000 miles away, while they often don’t know the names of the people next door in their anonymous urban apartment complex.
This undermines the underlying assumption of the Westphalian nation-state: namely, that people who live near each other will share the same values and therefore agree upon laws, such that the geographically-premised mechanism of the nation-state is the right entity to govern them. Instead, what we find is that people share values with people who are close to them in their social network…not in their physical vicinity. We cannot be a good neighbor if we do not even know the neighbors.
#
We can quantify this with a little math. First, take a look at the definitions for the great circle distance and the geodesic distance.

The great circle distance is the distance between two points on the surface of the earth. It’s the distance as the crow flies. You can do a modified version of this based on practical travel constraints, but to a first approximation, this is how far apart people are in the physical world.

The geodesic distance, by contrast, is a completely different metric. It’s the number of degrees of separation between two nodes in a social network along the shortest path.
Importantly, the geodesic distance is just as valid a mathematical metric as the great-circle distance. That means one can generate distance matrices, and hence maps, via techniques like multidimensional scaling. In fact, there are entire conferences devoted to cloud cartography, in which research groups present maps of online social networks - mapping not nation-states but states of mind.

Why is the geodesic distance important? Because the network state is enabled in nontrivial part by the fact that we are transitioning from a primarily great-circle-driven world to a graph-geodesic-driven world. And that means the fundamental division is less the visible geographic borders of the nation-state than the invisible geodesic borders of the social network. This in turn means that we need to reconceptualize the state as a primarily digital entity, a network state.

Think about the difference between Russia vs Ethereum. Russia was a geographical entity that switched its ideology in 1991, from communism to nationalism. The geography was primary, the ideology was secondary. Conversely, Ethereum is an ideological entity whose primary existence is in a network. The Ethereum community holds meetups in places like Cancun or Shenzhen, but the physical materialization is evanescent while the digital community is persistent.
Or think about the fact that Russia’s borders are (mostly) fixed, while Ethereum’s borders are highly fluid. Russia’s borders have indeed changed since 1991; its predecessor state, the USSR, extended farther out into Eastern Europe and Central Asia. But the Russian people have been near the Baltics, the Turks, the Eastern Europeans, and so on for quite a long time. Geopolitics doesn’t vary that much; Russia’s “competitors” for citizens have mostly stayed the same.
By contrast, the Ethereum-to-XYZ exchange rate does vary quite a bit, for different values of XYZ. Solana is a new digital currency that has popped up on Ethereum’s boundary and taken a good chunk of “citizens” from it, just as Ethereum itself rose in BTC terms since its inception.
This is similar to how early Facebook arose out of nowhere and took many “citizens” from Gmail before Google “closed the borders”. Of course, unlike territorial disputes, competitions over digital citizens are not strictly zero-sum. For at least a while, the space of cryptocurrency and internet users will keep expanding; even after that point, a rival still needs to build better services to attract a competitor’s digital citizens.
It is the geodesic distance that enables fluid switching between network states[fn:6]. The great-circle-distance-driven physical world requires individuals to move around the map to enter new territory, while the geodesic-distance-driven digital world just requires a user to hit a new key. This becomes more obvious when you have a VR headset on; hit a button and you are transported between worlds. Another button, another world.
And this applies not just to individuals, but to whole groups, to entire networks, which are expensive to move in the physical world but much easier to relocate near another network in digital space. Just do an Oauth-style integration and voila, your citizens can cross the border into another network state.
Legacy nation-states cannot do this. They cannot just move around the map at will. As we noted, the Russian state is mostly stuck with its neighbors like Japan and Turkey in a way that individual Russians, or the Telegram and Ethereum networks (both founded by people of Russian descent), are not.
We can term this concept digital dynamic geography after a term Patri Friedman introduced. He used it in the context of seasteading, to argue for homes like cruise ships that could dock and undock in congenial states at will, but it’s arguably easier to accomplish first in the digital world. For a group organized by geodesic distance, collective digital exit is as easy as pressing a key.
A Territory One Can Acquire but Not Conquer
Once we visualize a network state as a combination of (a) a digital social network with an integrated cryptocurrency and (b) a physical network of distributed enclaves, we realize that it is much easier to acquire than to conquer.
Easy to Acquire
First, why is it easy to acquire? For the digital portion of a network state, when the founder sells it to an acquirer, it’s like selling Instagram to Facebook. The digital logins of the two services are integrated and citizens in each network state now have access to the other’s apps and physical territory. This is a modern analog to the Louisiana Purchase or the purchase of Alaska. It’s also feasible to sell not the entire network, but simply a subnetwork - perhaps all those in a defined geographical location, or all those who have expressed a collective interest in changing citizenship. This is similar to Singapore becoming independent from Malaysia. Finally, it is also feasible to spin off a subnetwork into its own network, like the UK exiting from the EU.

If we visualize the physical portion of a network state as like a network of Google offices, a string of restaurant chains, or the real estate footprint of a REIT, we see how we can handle the physical component of network state M&A as well. In the simplest version, after one network state consummates the acquisition of the other, all citizens from one network state can enter the territory of the other. The smart locks just get a software update and now open all the doors and gates. The branding changes too, to be consistent with the new unified entity, much like a large hotel chain putting up new signage when it acquires a small one. Various kinds of reciprocity relationships with other network states and third parties may need to be renegotiated, just like many corporate contracts have change-of-control provisions, but this is straightforward so long as it is anticipated.

In theory, all of this can be done with current technical and legal infrastructure. It’s just like one multinational acquiring the digital, physical, and human resources of another, except it extends to people’s residences rather than simply their offices, and except that the acquired people become not just remote employees of the combined entity but digital citizens - though they can always leave for any new network state that admits them.
Over time, however, the technological infrastructure for each network state should live on a blockchain rather than a melange of paper contracts and cloud services. The reason is that a blockchain gives citizen accounts and balances, allows the recording of all real estate transactions, the maintenance of all citizen records, and the management of private keys in a globally consistent way across legacy nation-state jurisdictions. The problem of post-acquisition integration then reduces to porting over the records from one chain to another.
In summary, this is a way to extend the corporate concept of change-of-control to polities. It’s a recipe for nonviolent competition between countries, where peace treaties between would-be rebels and current incumbents are turned into M&A deals.
Hard to Conquer
The network state reduces violence on another dimension: thanks to their geographical decentralization and physical invisibility, network states are hard to conquer.
Network States are Geographically Decentralized
First, geographical decentralization. If you look at a map of France that includes its islands in the South Pacific, you realize that it’s difficult to nuke or attack the whole thing at once. It’s too globally distributed. So the geographical distribution of the network state itself is a deterrent to physical force. Just like cryptocurrency, decentralization deters violence.

Put another way, invading a network state is like invading every Bitcoin mine or Ethereum node in the world at once. Are you going to be able to get right-of-way for your troops from every surrounding territory? Won’t the collateral damage piss off the neighbors? And how will you even locate all the nodes in the first place? Because the list isn’t public.
Network States are Physically Invisible
This brings us to the second way that network states deter violence: physical invisibility. It’s a bit more subtle. Right now, you can see the physical border between France & Germany on a map. But you can’t visualize the border between Twitter & Facebook. That is, which people are on the “border” of Twitter and Facebook, in the sense that they have accounts on both sites?
This might seem like a trivial concept but isn’t. The Twitter and Facebook networks are each bigger than France or Germany - combined. However, social network membership is invisible to all but the network operators. There’s no public list of all Facebook and Twitter members. Only Facebook can generate a map like this.

The invisibility of network membership has immense implications. You couldn’t have nationalism itself without maps of physical space. For example, think about 54° 40’ or Fight, which made a literal reference to latitude. You couldn’t have that kind of border dispute without being able to visualize a border. People had to see the map to be able to fight over it.
So, because citizenship in a network state is invisible to a satellite, at least without the consent of the network state operator, these imagined communities are invisible countries. It’s the return of secret societies, at scale, as secret states. Network states thus reduce violence by encrypting the map itself; you can’t hit what you can’t see.
This is particularly interesting when it comes to the threat of invasions, and the use of nuclear weapons. If a network state of ten million people was spread around the globe, with a partially private user list (like Twitter and Facebook) and a physically decentralized footprint (like Bitcoin miners and Google offices), it’d be difficult to nuke it, or invade it, even if you could find it. You’d impose a lot of collateral damage on the people nearby in unaffiliated network states, you’d spend a lot of money, and the remaining 90-95% of citizens of the network state would likely seek some form of retaliation.
That’s not to say that network states are invulnerable. The types of attacks that could hit the entirety of a rival network state would be a cyberattack of some kind on their blockchain backbone, or perhaps a drone swarm (or perhaps SEAL team) that could be coordinated around the world given the GPS coordinates of every citizen.
But that’s a different battlefield than the one today’s militaries are prepared for. Special forces and cyber notwithstanding, they are still for the most part organized around tanks, planes, and aircraft carriers. But if the map goes dark, the network state itself becomes invisible, the nuclear weapons and invasions of the 20th century are less applicable, and cyberwar and drone strikes become fundamental, then the cloud becomes the primary theater of war - not air, sea, or land.
A Community Aligned Around Cryptographic Consensus
Today’s nation-states are typically either internally disaligned, like the US, or forcibly internally aligned, like China. In the first case, the citizens are arguably free but strongly disagree. In the second case, the citizens are in key respects less free, and thus do not openly disagree.

The ideal is a third way, to build a community that is consensually internally aligned, where the citizens have made a free choice to agree, and have working mechanisms to come to consensus in the event they disagree[fn:7].
That last bit is the hard part. In the US, polarization (or decentralization) has been increasing since the mid-century peak centralization and was accelerated by social media. The establishment attempted a counter-decentralization to try to censor and deplatform people from social media, but this is unsystematic and, after an initial surge, halfhearted. It’s an amateurish retrofit of speech and thought controls upon a previously free society, and it increasingly seems like it’s not going to stick, particularly with the emergence of semi-decentralized platforms like Substack, fully decentralized tools like Bitcoin, and censorship-resistant web3 tools like Mirror, IPFS, and the like. America’s model is no consensus and constant dissent.
In China, unification (or centralization) has arguably been increasing since mid-century, when there was the nadir of the Chinese Civil War when many of the most talented Chinese people sought their fortunes abroad, and when the most successful ethnically Chinese states were the islands outside mainland China: Hong Kong, Taiwan, and Singapore. Over the last several decades, like an ultra-aggressive sheepdog, the Chinese government has ensured that any burgeoning dissent is stifled, whether that be Tiananmen Square, the Great Firewall, Falun Gong, Bo Xilai, the Hong Kong National Security Law, the Xinjiang crackdown, US-supported democracy activists, Chinese tech founders, or Bitcoin miners. China’s model is to attain consensus by suppressing dissent.
What’s the better model? A combination of old-fashioned ideas like trust and communication, plus newer ideas like the cryptographic consensus that the blockchain permits.
After all, we should recognize that an Israeli and a Palestinian, a Chinese person and a Japanese person, a Democrat and a Republican, all agree on the state of the Bitcoin blockchain. Regardless of their political views, or geography, people agree on how much Bitcoin someone has globally. This is an incredible triumph because a trillion dollars is the kind of thing people will fight over. For wealth on the scale of a trillion dollars, people will invade countries, forge histories, do crazy things. Indeed, a “mere” million dollars is the kind of thing people will fight over. Yet there’s essentially no dispute on who owns what BTC.
The same consensus algorithms that can get people to agree on what Bitcoin someone had at what time can be extended to get people to agree on what digital property somebody had at what time. That’s stocks and bonds, but also things like art and video game items, and the digital keys to real-world homes and vehicles.
Finally, and less obviously, these consensus algorithms can be extended not simply to recording property, but to arbitrary kinds of timestamped information. What device recorded this temperature in Kansas on this date? What hospital uploaded this medical record to the blockchain at this time? What was the price of this house that was sold in this area? What crime was reported by this victim or this police officer in this area?
All of these feeds of data did not exist two decades ago. They mostly do exist today but in corporate silos. The next step is to put them on-chain and integrate them into what we call the ledger of record, which is a global feed of cryptographically timestamped, undeletable history.
If you think about how people use Twitter, they use it as a reference to prove that something happened, that someone said something at a given time. Twitter is in this sense a timestamped feed of events, one where we trust Twitter to tell us what happened. But this is imperfect for many reasons, not least of which that Twitter deplatforms many people, and has been hacked in ways that allow impersonation of users.
If a Twitter-style feed was on-chain, no one can man-in-the-middle attack or deplatform the users. They could steal the keys, but that would mean stealing property too. So it becomes harder to falsify history. The feed of what happened becomes harder to corrupt. And this is the transition from centralized truth, from the corporate “truth” of the American press and the official “truth” of the Chinese state to decentralized cryptographic truth, on-chain truth, truth you can verify for yourself.
This kind of truth is already used by crypto oracles like Chainlink to manage feeds of information that are the input to smart contracts handling billions of dollars. While price feeds may seem like a highly specific area to begin, they are ideal from one vantage point: if you can corrupt even one byte, you can hack a lot of money. So if you can create a defensible, hack-proof history there, you can extend it to protect many other kinds of history.
This is how we get to a community aligned around cryptographic consensus.
A Citizenry Centered On Single Sign-On
In many ways, we can think of modern citizenship as being defined by access to a single sign-on service like Singpass, as opposed to physical proximity to another person per se.

As we’ve mentioned, the backbone of the network state is likely a blockchain, whether that be permissionless, permissioned, or some variant thereof. Why? Because it can be used to replace the following services of a legacy nation-state.
Identity card: Your private keys give your user account and login to the digital services of the network state. It all starts here, with the new single sign-on for citizens. Like ENS’s satoshi.eth, you’d have an official name like yourname.countrychain.
The Social Contract: The metaphorical social contract becomes a literal social smart contract that you sign every time you want to re-up your subscription to the network state. There are explicit contract terms, multiple-choice questions to ensure that you understand those contract terms, reviews of the contract terms by other competing network states, and so on.
Passport: Your private keys, the network state’s foreign relations, and the technological state of chain interoperability determine what other network states you can access.
Voting: Every vote, shareholder vote, poll, or survey is done via digital signature using your private keys. Sophisticated kinds of privacy-preserving votes can be done with this infrastructure.
Governance: Should you be elected or appointed to office, your private keys determine your permission level, in terms of what budget you have as governor of a subgraph of the network state, or what actions you can take towards untoward citizens, such as deplatforming for 10 days after a first warning.
Crime and Punishment: On this topic, different network states will make different decisions here, but unlike the lawless deplatforming of today’s social media platforms, digital punishments could be more humane and acceptable than physical punishments so long as there are clear and pre-agreed rules that all members of the network state abide by at the time of joining.
Driver’s License, Pilot’s License: Your private keys determine which smart vehicles you can operate, either in person (eg a Tesla) or remotely (eg a drone).
Security Clearance: Your private keys determine whether you have Top Secret clearance, and in general whether you have permission to view any given document, enter a facility, or interact with any digital object.
Postal Service: Your private keys give encrypted p2p and group messaging. Note that the Postal Service was in the US Constitution!
Fund Recovery and Lawful Intercept: This is a controversial area, and different network states will make different decisions here. But if the network state founder has admin keys, it may be able to do lawful intercept of some messages or reversal of fund transfers after a pre-agreed social process, which proceeds on-chain and thus more transparently than the status quo of star chambers and civil forfeitures.
Why even mention this? Because it’s an open question as to how to deal with crime in a network state. The fact that the United States and other governments have abused their police powers and are likely beyond reform does not mean that the complete absence of lawful authority is the right answer; that path leads to crypto-anarchy and criminal gangs. The right answer is a new network state where you can choose to trust it and revoke that trust and exit to a new network state should it abuse it.
Here’s another way to think about it: as a user of a crypto exchange, you want complete privacy. But as the CEO of a crypto exchange, you want complete analytics on every user. Why? Because some users are genuinely seeking to harm or defraud other users, you may need tools like Sift Science to determine who they are, and to ban them from the platform.
Defensive Border Walls: So long as your chain is sufficiently sovereign resistant, no other entity besides the network state itself can penetrate the cryptography protecting your citizens’ messages and possessions.
Name Change: Seemingly trivial, but less so in the pseudonymous economy. Your private keys let you do this as well.
Signatures and Notarization: Your private keys allow digital signatures and, via multisig, notarization of others’ signatures.
Community Trust: A web-of-trust network of on-chain endorsements serves as a computable measure of community trust, like a higher stakes form of friending or following.
Corporate Law: Most corporate law can go on-chain. See this post mirrortables for details: balajis.com/mirrortables.
Dispute Resolution: Smart contracts give more predictable dispute resolution.
Land Registry: Cadestration and land registries can be put on-chain. Even more interestingly, any land use permits can be put on-chain, as can community ownership of land through a REIT, in a sort of neo-Georgist configuration.
Crowdfunding for public goods: All of this can be organized on-chain, potentially with traditional crowdfunding and possibly with commemorative NFTs where the largest bidders get their names on a digital plaque.
Currency: The internal currency or currencies of the network state are of course on-chain, as are any bonds or other securities it issues to finance its operations.
Taxes: these turn into (a) subscription fees paid on-chain and (b) Bitcoin-checked inflation of the network state’s native currency. The subscription concept is intuitive; it’s the annual payment for being a member of the network state. The inflation component is less obvious. Isn’t the whole point to get away from inflation? The idea here is that this “inflation” is highly visible, and more like a fundraising round where new shares are issued and closely scrutinized than the current hijinks the Federal Reserve prints trillions of dollars and then hides the scoreboard. In the event, any network state tries to inflate its currency too much, the citizens cash out to Bitcoin, which thus acts as a kind of pro-freedom global government.
Birth, Marriage, and Death Certificates: All of these go on-chain too. Everything that the city is asserting is true as an oracle.
Property Rights: user balances for all assets where the network state mediates disputes go on the network state’s blockchain. Notably, BTC is not included in that list, as Bitcoin stands above the network state on its blockchain as a check on every state.
This gives you a sense of where city coins can go. They eventually become city-state coins and network state coins.
A Society Funded by Subscription and Seignorage
Just to preface this section: to be clear, the network state starts as a non-sovereign entity, an imaginary construct, a LARP. Each netizen of the network state, and each network node, is expected to comply with the laws of its surrounding host state for the indefinite future.
But suspend disbelief and assume we can wave a magic wand. Assume we can eventually gain a degree of legal sovereignty for the network state by collective bargaining with a host state, perhaps by paying them a fee or otherwise working with them.
For example, a set of network nodes in the vicinity of Tuvalu might do a deal with Tuvalu similar to the purchase of the .tv domain. They might pay the Tuvalese (say) $X million annually for the privilege of being considered a Tuvalu special economic zone and setting their revenue policy.
What could that revenue policy look like?
In context, current nation-states are based on (a) coercive revenue collection, (b) financial surveillance, (c) bond-fueled debt, and (d) hidden inflation. The network state is set up to be financially solvent and ethically strong from the beginning by avoiding each of these pitfalls.
Subscription > Coercion
The primary source of revenue for a network state is subscriptions[fn:10]. Each netizen pays for the citizenship-as-a-service single sign-on.
If they do not renew their subscription, their single sign-on is turned off, and they end up being unable to enter buildings or log in. This is enough incentive for them to remain compliant with the terms of the social smart contract they signed upon entering. The blockchain handles the various details of nonviolent contract enforcement.
Importantly, as the cost of coercion rises, these types of subscriptions will end up being more profitable than traditional means of coercive revenue collection.
Why? Because if an illegitimate state like Venezuela tries to implement something like civil forfeiture on a national scale, if they tried to do Lenin’s Hanging Order in the age of Bitcoin, they will need to ensure that each act of seizure must pay for itself. That is, they need to deanonymize each ‘kulak’, geolocate them, ensure they have jurisdiction, send in the SWAT team, successfully execute the wrench attack, collect the Bitcoin, and then repeat this over and over again in many places while managing the PR fallout.
The key concept is that each such act by a Venezuela-style gangster state must generate more Bitcoin than it costs. It is not obvious that this will be the case as physical attacks are far less reproducible than the practice of simply hitting a key and printing money. And they are also less profitable than the new proposed practice of simply rendering a valuable enough citizenship service that people will consensually renew their subscription.
Privacy > Surveillance
There’s a second reason why subscriptions will be preferred over the current mechanism of invasive data collection and financial surveillance: namely, privacy.
You don’t need to fill out endless numbers of forms to pay Dropbox. You certainly don’t need to spend hours giving them a snapshot of your entire corporate and/or personal financial picture to pay them a percentage of your income, thereby risking your privacy further should Dropbox get hacked. You just pay Dropbox a flat monthly fee for services rendered and cancel it if you don’t like it.
Compare this to the state of affairs for states. Major government agencies are routinely hacked to an unbelievable degree. The OPM Hack, the Texas state hack, and the Solarwinds hack are just a few that have been publicly reported. If it has not already happened, it will likely soon occur that your personal financial information is sprayed over the internet by a hack of an incompetent government agency. The cloud may burst, with all this information raining down upon the internet. Add to this the surveillance state that one cannot opt-out of, and the potential for abuse becomes clear.
So the network state starts with an alternative principle: minimal necessary data collection. Governments should not collect what they cannot secure. The subscription state protects financial privacy relative to the existing system.
Sovereign Equity > Sovereign Debt
While subscriptions are expected to be the main source of funds, another mechanism network states can use to raise capital is seignorage. Specifically, much like a company issues new stock, the network state issues new units of its digital asset on its main blockchain.
Unlike the current process of secretive and random inflation, this is more akin to the highly ritualized ceremony around stock issuance that occurs when a company raises a new funding round. In such a ritual, the exact number of new shares is specified to the unit, the exact purchasers are known, the terms of those shares are detailed, the new liquidation waterfall is updated, and so on. If these terms are not agreeable to the purchasers of equity, then they walk, and the round is not completed.
Compare this to the current practice of lawlessly printing trillions, watching M2 ramp, then complaining that it doesn’t measure anything, thereby acknowledging that there are zero dashboards to monitor the flow of trillions into the economy. Or the practice of encouraging many entities to buy “debt” in the form of negative interest rate yielding US bonds, even as it becomes obvious that the long-term strategy is to monetize the debt by printing so much money that the bonds become worthless.
Bitcoin > Inflation
The third governor of the network state’s financial solvency is Bitcoin. This works in several ways.
First, because the Bitcoin blockchain is so difficult to interfere with, we can think of it as a form of property that even the world’s most powerful legacy states can’t stop. In this sense, Bitcoin is a global government that checks all other states, networks, and nation-states alike.
So, any investor who doesn’t like a network state’s seignorage practices can cash out to BTC, which cannot be issued by any network state. Any citizen can do the same. This is similar to how an investor who doesn’t like a company’s practices can cash out to USD.
Moreover, each network state itself holds Bitcoin as a strategic reserve, which cannot be seized by any other state. Having funds on-chain also allows a network state to demonstrate proof-of-reserve.
Of course, a network state will hold more than Bitcoin, just as traditional states held more than just gold. Each network state decides what digital assets are held in its portfolio, and which are approved for its medium of exchange, unit of account, and store of value.
Summary and FAQ
As you can see, we’ve put some thought into how to make the network state feasible. The concept has been defined to address many of the immediate questions - and emotional interjections - that arise when you discuss the concept of starting a new country.
What is a network state, anyway?. We defined the network state as a social network with a recognized founder, an integrated cryptocurrency, a definite purpose, a sense of national consciousness, and a plan to crowdfund territory. It’s a country you can start from your computer. There is a path for founders, and a path for citizens, as anyone can declare themselves founder or citizen of a network state at any time, and also switch between these roles.
How should we think about nation-states? The root word of nation is related to the word natality, which refers to birth. That is, a nation is considered to be an ethnic group with common culture, inheritance, language, traditions, etc. The state by contrast is the government. So in the classic nation-state, an ethnic group like the Japanese (the nation) names leaders (the state) to manage disputes, collective defense, and the like. The Jewish community by contrast was for a long time a nation without a territory or a formal state, until the establishment of Israel. And today we have multiethnic nation-states like Singapore, Luxembourg, and the USA, which generalize the concept beyond the historical ethnostate, and where the state becomes more primary. In the latter case, the defining principle is a proposition, rather than a nation, but this is a retrofit on what was previously an ethnostate. A major issue today is that the internet is accelerating the decay of the Western nation-state by making long-distance bonds over networks more salient than geographical ties between neighbors.
Why is a network now a better basis for a state than a nation? If we’re going to build a proposition nation, we should be honest about it and recruit based on that proposition from the beginning. Many Western countries today demonstrate the level of dissatisfaction that occurs on both sides when what was arguably implicitly an ethnostate is converted to a proposition nation with less than 100% assent. By instead starting with a group of people defined by geodesic rather than over geographic distance, we have a base population that is close together in an ideological sense and thereby much more likely to agree on what the state should do. By also articulating the proposition explicitly, we have a defined purpose, an objective that we are quantitatively optimizing as a society of optimalists. All recruiting is then for that purpose.
Why don’t you just reform existing institutions? We want to be able to start new countries for the same reason people want a clean sheet of paper, an empty text buffer, a bare piece of land, or a fresh cap table. It’s a clean start without legacy baggage. Think of the network state as a way to build replacements to reform-resistant legacy institutions that can’t be easily disrupted by tech companies, open-source projects, or crypto protocols. If those replacements succeed, then our exit enhances voice. That is, if we are successful in what we’re doing, that gives ammo for people to reform existing institutions, much as many practices were pioneered in America and imported back to the old world.
Why do you consider this an ethical imperative? Suppose you’re interested in improving longevity and thereby life expectancy. It takes 12 years and billions of dollars to get a drug through the FDA. And it might be faster and cheaper to start a new country than to reform such a sclerotic bureaucracy. This is the concept behind building a ROC-based real-time regulator, a regulator that quantifies approval decisions like a binary classifier and tries to minimize type I and II errors.
How will you get land, if it’s all spoken for?. The short version is that we crowdfund discontiguous territory around the world and network it together into an archipelago of interconnected enclaves. A network state can thus be visualized in a dashboard, and you can watch it grow over time.
Why is this not cosplaying like all the other failed micronations?. The key difference is that we start by building functional communities online. We aren’t just starting with a patch of territory, we’re starting with the network as the equivalent of the nation, and then building a state in the cloud before it materializes on the land. As for the LARPing part, (a) we just LARPed cryptocurrency to a trillion and (b) all countries start as imagined countries. For example, Herzl wrote Der Judenstaadt in the 1890s, five decades before the formation of Israel.
You do know we’ll invade you if you do it, and we’ll also denounce you if you have any defense plan?. As noted above, the network state has a nonviolent defense in depth. It’s a city-state with its capital in the cloud, and its territory is globally decentralized so it can’t easily be invaded. It might even be a secret state, with an encrypted membership list and set of network nodes, so it can’t even be easily found. It can however be bought and sold, with the consent of a sufficient number of coinholders, so it is a territory one can acquire but not conquer.
What about humanities and culture, techbro?!? Glad you asked so politely. Of course, when we think of France, we don’t think of the French Stock Exchange. We think of the Louvre and the Eiffel Tower, we think of the Mona Lisa and baguettes, we think of their art, culture, and food. So too will every network state need its artists, writers, bards, and chefs. In the modern era, we’ll think of these as crypto creators, who own their art and audience via private keys, unlike mere internet influencers. These crypto creators help attract new citizens to each network state and define its culture and value proposition. Phrased humorously, you can fund the Eiffel Tower with affiliate revenue from citizen referrals. This gives a sustainable business model for the arts.
How do you think about legitimacy and consent? The network state is a 100% democracy rather than a mere 51% democracy. That means that every netizen signs a social smart contract upon entering the digital (and eventually physical) environment, kind of like Envoy. They then periodically re-evaluate the terms at the time of subscription renewal or reject them to leave for a new network state.
What about loyalty if everyone is switching all the time?. There are many mechanisms to rebuild loyalty based on conscious, affirmative consent. For example, at the time of signing the social smart contract, incentives may be offered for longer-term contracts and coinholding periods. Attractive cultures may also serve as network effects that keep people from leaving a network state at the drop of a hat. There is always a balance; the point is to amplify the possibility of choice, not to build a mercenary society. But there will be several possible solutions here, so different network states will do this differently.
How does the network state resolve significant disputes? First off, part of the goal is to build a civilization that values digital civility. So many disputes are really about disrespect rather than substantive differences. But with respect to substantive issues, one way of thinking about the network state is as a union of sovereign collectives. Each sufficiently large network node has a CEO that folds into the CEO of the overall network state, which owns a stake in that node. If that CEO so chooses, they can spin out their network node into their own network state, or detach and join another network state. The signage of network state 1 goes down, and network state 2 goes up. This is a new mechanism for dynamic geography.
How does a network state come to consensus?. The network state is based on the ledger of record, which is a feed of cryptographically signed events. The metadata on these events can be validated (such as proof-of-who, proof-of-when, and proof-of-what via hash), and in this sense what is true is now based on math even more than “science”. This ledger of record turns every information source into an oracle or an advocate. The former is a dispassionate stream of data, the latter is an interpretation on top of it. Just as every citizen posts on social media today, every citizen will be considered a citizen journalist tomorrow. Some will raw report information via oracles that gets recorded in that network state’s ledger of record, while most others will provide commentary. Everything will be signed with their digital signature, and there will be a web of trust and many interlocking levels of automated rating and peer review. A key concept is prioritizing truly independent replication over “peer review” or mere retweeting. The goal is a community aligned around cryptographic consensus.
That wraps up our high-level overview of the network state and the initial FAQ. As a next step, you can make proposed edits to this PDF, fix typos, and add comments at github.com/1729/content/issues. We’d appreciate it if you did this!
Footnotes
[fn:1] Another difference is that the people of the network state wouldn’t have a single employer like Google. There would be as many different sources of income as there were network state citizens.
[fn:2] Think of interoperability between network state citizenship status as being a complex, fruitful ground for innovation -f much like interoperability between blockchains, and based on many of the same concepts given that citizenship is partially predicated on coin possession.
[fn:4] Yes, you may not use Facebook.com today. But you probably used it in the past, or use it solely as a login mechanism, or use Instagram, WhatsApp, Oculus, or one of Meta’s other properties. The point should be clear; feel free to substitute Google here as well should you choose.
[fn:5] This observation inverts the concept of the “temporarily embarrassed millionaire”; it is, in fact, much easier to become a millionaire or even a billionaire, than it is to become a president. The opposite phenomenon of someone who believes that change is best sought through the legacy political system is best characterized as a temporarily embarrassed politician.
[fn:6] This is different from, but complementary to, the fluidity of transitioning from citizen to founder, and back.
[fn:7] Or to exit if they truly cannot agree. While this is much more salient in the network state environment, it’s still a last resort.
[fn:8] To our best knowledge, of course. But as the saying goes, two men can keep a secret if one man is dead. Given the idiosyncrasy of the project and the consistency of the voice, I find it unlikely that Satoshi was venture-backed or a team.
[fn:9] Some national borders are more like natural borders, in the sense that they track geographical, religious, or linguistic differences. For example, the nation-state of the UK and that of France are divided by the English Channel, a geographical delimiter. The UK also includes Northern Ireland, which roughly maps to the religious boundary of Protestant vs Catholic. The internal divisions of the UK into England, Wales, and Scotland map to historical linguistic boundaries. Finally, the UK itself is responsible for much more artificial boundaries that map to neither geography, religion, nor language, such as the vertical and horizontal colonial lines that divide up Africa. This is a classic example of “Seeing Like a State”, because those lines are clean on a map but cut right through historical ethnic and linguistic groups, resulting in weak states that don’t reflect one historical people at the time of state formation. Of course, over time, these social constructs can start influencing language and genetics; for example, it’s usually easier to marry someone within your nation-state than outside it. Still, this is a good example of an artificial national boundary.
[fn:10] See the Sovereign Individual, David Sacks’ tweet, and Lakoff’s concept of subscription fees as the price one pays for being a citizen - though the latter may balk at taking the concept seriously rather than merely rhetorically!

---
## [criteo-cookbooks/choregraphie](https://github.com/criteo-cookbooks/choregraphie)@[176834de72...](https://github.com/criteo-cookbooks/choregraphie/commit/176834de720dda6846515d6ba342d40ed0880e33)
#### Thursday 2022-01-13 08:43:20 by Grégoire Seux

Adapt to changes from ruby 2.7+

Starting with ruby 2.7, usage of Proc.new without a body is discouraged
(warning and then error).
This patch makes sure we are ready for this.

This part of the choregraphie code is a bit arcane for non-initiated and
I had trouble myself understanding the full picture 5 years after
writing it so here is my understanding.

Rationale:
- most people writing choregraphies are not heavy ruby users, quite
  often not even experienced chef users. They consider ruby/chef to be
  some kinf of magic
- specifically rules of bindings (what kind of definitions can be called
  within a block, depending of where it was defined) are not very clear.
  Usage of choregraphie dsl within chef dsl does not make any of this
  clearer
- a reasonable expectation as a user is to be able to call methods from
  within choregraphie (in the core block or in a before/after block)
  that were defined anywhere in the same file
- another reasonable expectation is to be able to call the same
  methods/variables inside and outside choregraphie block

Lines touched by this patch are doing exactly this: they store the
context in which choregraphie object was initialized and refer any
missing reference (method) to this context.

Fixes #62.

Change-Id: I5f4f9c8ba1dcf67e0e1bae1ba3fa17d29cea385a

---
## [NimBlemations/BROMINATOR](https://github.com/NimBlemations/BROMINATOR)@[de625cfef9...](https://github.com/NimBlemations/BROMINATOR/commit/de625cfef9faab6d7f760891e84f69190de6aca4)
#### Thursday 2022-01-13 09:13:07 by NimBlemations

Oh my god rotation

Damn how does this stupid rotation and perspective work, it looks so easy to copy.

---
## [bossbuwi/existence](https://github.com/bossbuwi/existence)@[e4902ef561...](https://github.com/bossbuwi/existence/commit/e4902ef5619ee524c751618039e44f66f4ebf73e)
#### Thursday 2022-01-13 09:38:21 by micmanan

Release 0.1-alpha_20220113

It's been a while since my last commit. I've been busy not just with work but also with this pandemic thing going on.  Everybody's getting sick. I myself felt a bit sickly a few days back but thankfully my COVID test turned out to be negative.
Anyway, this commit marks the completion of the basic CRUD for the sonata backend. All significant CRUD processes have been finished although not all models have them. Most only have read and / or create methods. But the main model, the event, has all methods except for delete. After this commit, I will be moving on to the report generation.
Some bits of the frontend also have changes in them that are included on this commit. However, those are still far from working but I still want to commit them in case something bad happens to my local data. I could still delete them later if I want to right?

---
## [michaelsoliman-com/knowledge](https://github.com/michaelsoliman-com/knowledge)@[1a8afcccc6...](https://github.com/michaelsoliman-com/knowledge/commit/1a8afcccc6124b9505282abfb9b0f2c28cf7946d)
#### Thursday 2022-01-13 13:44:06 by Nikita Voloboev

SUMMARY animals books startups ngrok cloud-computing gcp aws-lambda cloudflare-workers serverless-computing build-systems computer-graphics computer-vision image-processing compression formal-verification kafka arweave blockchain cardano ethereum near solana databases postgresql redis design-inspiration design figma-plugins logos user-experience devops temporal terraform distributed-systems drugs investing learning environment rules front-end minecraft arduino recipes knowledge-graphs latex happiness life success xcode macOS datasets ml-libraries pytorch machine-learning ml-models reinforcement-learning calculus fractals satisfiability-modulo-theories math statistics acting music-production decentralization graphql http iot microservices networking nginx tcp tls nlp containers docker kubernetes emulators ios linux operating-systems wiki-workflow nix quantum-computing privacy c-libraries clojure-libraries clojure qt crystal flutter elixir-libraries elm fsharp go-libraries go idris java-libraries js-libraries nextjs react-components vue julia-libraries kotlin-libraries lisp ocaml-libraries ocaml php programming-languages django python-libraries python ruby rust-libraries rust scala swift-libraries typescript-libraries typescript zig constraint-programming embedded-systems jupyter-notebooks git psychology solving-problems robots cryptography security social-networks emacs elasticsearch tools netherlands russia cinematography video virtual-reality browsers deno nestjs nodejs web-accessibility web consultancies interviews remote-work

---
## [tstelfox/ft_containers](https://github.com/tstelfox/ft_containers)@[d13087eefc...](https://github.com/tstelfox/ft_containers/commit/d13087eefcbb09acfacc6a21b4a5367e21220a6a)
#### Thursday 2022-01-13 15:47:28 by Turlough Mullan

Instead of starting erase(), which looks like a pain in the ass, I'm gonna do the other oeprations like lower_bound and shit

---
## [owid/owid-static](https://github.com/owid/owid-static)@[b956eaaad6...](https://github.com/owid/owid-static/commit/b956eaaad6337d3c1fd262cfee39e84b75fdc959)
#### Thursday 2022-01-13 16:02:50 by owidbot

Deploy 2022-01-13T15:55:37.980Z
Updating chart number-of-homicide-deaths
Updating chart suicide-vs-homicide-rate
Updating chart suicide-vs-violent-deaths
Updating chart drowning-death-rate-vs-gdp-per-capita
Updating chart road-death-rate-vs-gdp-per-capita
Updating chart malnutrition-death-rate-vs-gdp-per-capita
Updating chart diarrheal-death-rates-vs-sanitation
Updating chart depression-daly-rates-by-age
Updating chart dalys-depression-age-std-rate
Updating chart disability-adjusted-life-years-major-depressive-disorders-age-std-rate

Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[9189850768...](https://github.com/LumberKing/Tianxia/commit/91898507681bb73206ba426ed942b9c96c7229d2)
#### Thursday 2022-01-13 16:39:21 by Silversweeper

Balance/optimization/polishing (part 7 of ???) + Fujiwara improvements (3 of ???):

Bloodlines:
- Added a bloodline for Imperial Family agnates (intentionally not powerful).

CBs:
- Fixed some incorrect tooltips regarding what would be obtainable from certain CBs.

Events:
- Blocked yet another possible case of sacrilege related to the Chrysanthemum Throne being usurped outside the Imperial Family.

Laws:
- Cleaned up irrelevant crown_laws.txt file.

Minor titles:
- Updated availability triggers for some minor titles that should be restricted based on government.

Nicknames:
- Added a couple of new nicknames.
- Removed the "the Unknown Master" nickname; he's got a better one now!

scripted_effects/etc.:
- Overhauled War of Honor Honor requirement.
- Fixed references to an incorrect dynasty ID in Chinese Imperial naming logic and conditions.

Traits:
- The Disinherited trait is now visible. Unsure why vanilla had it hidden...

Decisions:
- The WotRS decision to become Japanese Feudal is no longer available for characters that immediately will become ineligible.
- WotRS members looking for a mentor will now be less likely to pick a terrible warrior.
- WotRS members looking for a student will now be less likely to approach a terrible warrior.
- Improved some potential/from_potential blocks for WotRS stuff.

Events:
- Split WotRS events into several files.
- Added new WotRS mission to become Japanese Feudal for eligible characters.
- The WotRS will now give you one -- and only one -- opportunity to prove yourself the Very Best (like no one ever was!).
- Fixed an issue with the LNY logic.
- Fixed several WotRS logic issues.
- WotRS members showing off to a prospective mentor will now be more likely to do well if they have a higher PCS than the prospective mentor.
- Improved WotRS event logic in various places.
- WotRS students of mentors that neglect their training will now spend more time proving themselves.
- WotRS students that decide not to bother with their mentors' lessons will now spend more time proving themselves.
- Fixed a couple of missing flags for the Treasure Fleet
- Restructured WotRS The Very Best challenge logic.
- Changed the likelihood of various WotRS travel events.
- Improved WotRS The Very Best travel event logic.
- The Very Best will now get a nickname if they do not already have a "super cool" nickname.
- Abandoning the quest to become the Very Best or leaving the WotRS will now result in the event chain ending as soon as reasonable.
- Several WotRS events/decisions will no longer look for members of *any* society when they should look for WotRS members.
- Reworked the WotRS sake drinking contest to be shorter and better.
- Replaced the WotRS poetry contest event chain with an event chain to write a poem, which should not be particularly likely to freeze the game.
- Warriors of the Rising Sun are no longer particularly likely to become Paranoid by virtue of simply being Warriors of the Rising Sun long enough.
- Replaced old WotRS strategy discussion event with an event chain giving a chance to improve martial education trait tier, copied from the Hwarang.
- Added an event chain for WotRS members giving a chance to improve PCS, copied from the Hwarang.
- WotRS members that aren't being chaste/celibate should now lose those traits.
- Assorted WotRS events that have a possibility of adding/removing a trait should now alert the player if this happens.
- Improved triggers and pre-triggers for some WotRS stuff.
- Decreased Hwarang PCS improvement chance event chain likelihood a bit.
- Factions trying to install a new Tenno should no longer go "Let's give him Japan and Yamashiro while the old Tenno keeps everything else, including vassals and the Chrysanthemum Throne, and becomes independent!"

History:
- More Fujiwaras.
- More title history adjustments related to the above.
- Abe no Nakamaro is no longer used as an unnecessary placeholder in Annam in 767. The bureaucrats responsible for that mistake have been sacked.
- Tashibana no Toshitsuna (Fujiwara no Yorimichi's son) is now scripted as disinherited, seeing as he really shouldn't be inheriting from his biological father...

Interface:
- Might have fixed the charframe bug.
- The WotRS commander trait should now show up properly.

Localization:
- Fixed some instances of the game being "literally unplayable".
- Improved WotRS localization.
- You no longer think that lots of things should be written in second person.

---
## [ryancflam/findseed](https://github.com/ryancflam/findseed)@[1b018f3a96...](https://github.com/ryancflam/findseed/commit/1b018f3a961b7bfcd10ad0b2a818e512b0728b61)
#### Thursday 2022-01-13 18:50:05 by Ryan

github webhooks test #33 WHY ARE YOU SUCH A PAIN IN THE ASS GOD PERPENDICULAR LINES INTERSECTING AT A FLAMING ASSHOLE

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5f98fb9865...](https://github.com/mrakgr/The-Spiral-Language/commit/5f98fb986562385e7c6a3dbc7fe9785c35d2cb07)
#### Thursday 2022-01-13 18:58:35 by Marko Grdinić

"11:40am. I am up. Let me read a few chapters of the stuff I am following and then I'll do the usual: breakfast, chores. After that I'll get to doing those bug reports. Let me just set the nightly to download.

...There is the 3.0.1 released today. And there is the 3.1.0 Alpha. I'll give Alpha a try. Now let me read the Satanophany raw.

11:55am. https://code.blender.org/2021/10/blender-3-x-roadmap/

> Asset browsing and managing is one of the big new 3.0 features. Work on this area in Blender will continue for a while. The expectation is that good asset tools in Blender will help configuring efficient workflows; for expert artists in productions and beginners alike. Part of the Asset and UI project is to publish (a series of) Blender Bundles; relatively large downloads (1+ GB) with presets, primitives and asset libraries.

Oh, they intend to publish large bundles.

> The Geometry Nodes of 2.9x are a big success, and can be seen as proof of concept for ‘everything nodes’ in Blender. Next on the planning is to introduce solvers as nodes, add point-based nodes (particles) and nodes for physics simulations.

1:20pm. Let me do the chores here and then I will start.

1:50pm. Done with chores. I am already in 3.1. I see that it has spline length.

The old version has it as well!

No doubt this is what I should be using for length. Damn you got me good Blender.

I see that 3.1 has more geo nodes as well.

1:55pm. Ok, the issue where the instances are distributed incorrectly on the nuts curve has been fixed. No need to report that. The surve length I'll have to test, but most likely I am simply using the wrong node. I should have been using the spline length instead.

https://docs.blender.org/manual/en/dev/modeling/geometry_nodes/curve/spline_length.html

I'll have to test this.

2) Corrupted data in dimensions.
3) Scale from individual origins.

Let me try immitating the example here. I want to see if scale from individual origins works. I'll also have to test whether boolean parenting works.

Scaling from individual origins still fails.

Tested the spline length. It is the node that I need.

The dimensions seem fine, though I will have to test it on a more elaborate example.

2:40pm. Damn it, I think I fucked up. I was testing the cube example on the 3.0 version.

Let me try it on the fence example.

2:20pm. I see that the dimensions are still corrupted.

https://wiki.blender.org/wiki/Process/Bug_Reports

Let me finally watch this and I will make my report.

2:30pm. I am trying out scaling from individual origins on the path, and I figured out why it is not working. Because for curves every control point is an individual origin. With the Bezier curve, that ends up scaling the handles. So it is not that nothing is happening, what is happing is just not what I expected.

3:25pm. I am still messing with this. I am not sure what I want to report exactly.

I have some greater insight into the problem now. I see that ripping the edges without selecting the axis of orthogonality wrecks the normals. Without normals the rotation cannot be calculated correctly.

Let me take a break.

3:45pm. Let me resume.

First of all, that bug where there are gaps is not a bug. Rather it is merely rounding the amount of points to the nearest that will fit. It is sensible behavior.

That having said, there is definitely something wrong with rip edge.

Also I really need to learn what curve handle types mean.

Also no matter how I look at it, it is absolutely bizzare that rotation does not affect tilt.

https://youtu.be/Cjv54YRi5Hk

This is an old tutorial, but I suppose it will do.

https://docs.blender.org/manual/en/dev/modeling/curves/structure.html#handle-types

Actually, let me just read the docs.

///

Automatic (yellow handles)
This handle has a completely automatic length and direction which is set by Blender to ensure the smoothest result. These handles convert to Aligned handles when moved.

Vector (green handles)
Both parts of a handle always point to the previous handle or the next handle which allows you to create curves or sections thereof made of straight lines or with sharp corners. Vector handles convert to Free handles when moved.

///

I see.

https://blender.stackexchange.com/questions/35771/why-does-a-bezier-curve-twist-when-rotated

> If I create a bezier curve and rotate it in edit mode it does not accordingly rotate the tilt of the handles which creates an undesirable twisting along the curve.

4:40pm. I am still thinking about it. But I see where I went wrong in my thinking. Let me review and gather my thoughts.

1) Curve length node.
2) Corrupted data in dimensions.
3) Scale from individual origins.
4) Nuts curve bug.

For the first one, the problem was that I should have been using the spline length node.
The second one manifests when I make instances on a curve using gemotry nodes. While in 3.0 I got crap data, in 3.1 that gets set to 0, perhaps as a temporary measure. Changing it does not have any effect. No need to repoty it.
For the third one, it did not work because for a curve the individual origins are the control points. It just ends up scaling their handles. This is questionable behavior for a poly spline, but whatever. Now I at least understand it.
The fourth one was outright fixed in 3.1.

What I've been doing now is playing with curve and seeing how they are affected by rotation. It is strange.

I thought it was a bug that rotating a curve did not affect its tilt, but that is not the full story.

This problem only happens when the curve is not cyclical. When it is, the tilt gets calculated correctly. It also get calced better when when the curve has more than just a single point. Its real tilt depends on the overall curvature and having more information allow the program to infer it. I do not understand the exact way it is done at the moment, but my initial assumption was wrong. This is all due to my inexperience.

Furthermore I understand some other pertinent facts. There is a big difference between resampling a curve and having curves on points. In the later case, it determines the rotation by interpolating between nearby points. In the ther it actually generates new points on the curve. I have a square made of curves and in the interpolated case, they all end up pointing towards the center. But if I resample the curve first, I get a fence pointing in the proper direction around the perimeter.

5pm. So in the end, the local problem I ran into is a design consequence of the overall algorithm and I did not understand that.

5:10pm. I see. If the object does not have a face, the vetex normals are calculated based on the object's origin.

5:20pm. Now I am playing with ripping. The reason why I am getting strange results when changing any of the rip options is because doing that actually cancels the effect of the rip. I thought it had something to do with the tilt, but it did not.

So in the end, everything works as it should, the problem was in my own understanding.

Rip can be a bit weird. Sometimes it does not rip all the edges, but instead just a few of them. Maybe it would make sense in broader considerations given that it should be possible to rip multiple edges at the same time. At any rate, I just have to apply it a few times to be sure.

Now...

I think I should just report that using any of the rip options merges the ripped face back together.

5:30pm. I opened a report.

5:35pm. Ok, now that I've gone through this gauntlet and understand curves better, let me gather my thoughts.

I should also note, that when changing handle types, it is necessary to hit Shift + N in order to recalc them. That is also another thing I learned. Because I did not do that, when I previously fiddled with changing handle types I never got any difference between them.

6:30pm. Had to leave for lunch.

6:35pm. Id rather just call it a day here, but I should do some more.

Let me take a break here. Figuring out these curve issues took most of my energy.

Let me read Rebuild World.

Actually, I should open an issue for scaling paths and poly splines. Let me do it now.

Done.

Now let me read Rebuild World. After that I will resume. I need to think what is next. Momentum is important when programming and doing art, and coming to an understand of the issues that plagued me yesterday made me relax. If I did anything now, it would be like starting an entirely new thing. I feel like I've accomplished what I set out to do for the day.

7pm. As far as shonen manga go Rebuild World is up there. I'd give it high marks in all aspects.

7:25pm. ...

7:35pm. I do not feel like it. I finished lunch, had some time to think about what I nwat to do next and now I just want to stop for the day. Maybe I'll use this chance to go to bed earlier for once.

I honestly, can't be bothered to start work on the fence, and the texturing and whatever. I should just deal with that tomorrow.

The exercise of doing this should teach me quite a bit. After I do the pool, and paint it from a few angles, I'll get back into sculpting. I'll want to improve the base mesh a bit, specifically the arms and hands. After that I'll retopo it, and derive Luna's mesh from it. I'll want her to have a slightly taller torse and longer face, since her form is an adult one. The base mesh I have here is a bit too young, it might serve as her teen form instead. Since she is an action heroine, I need to give her her own look rather than use the base mesh as is.

7:45pm. All this will take some work. Tracking down the assets or painting and creating them on my own is something I should get used to.

Sigh, let's hope I do not get distracted with Blender related issues like today and yesterday anymore. I want to do art instead of just fiddling around.

7:50pm. Enough, let me close here. I'll figure out how to do the pool water tomorrow. I think it should be a transmissive material, but it ends up being too reflective if a do that. Despite all my learning I still don't understand how to do it. The way it is now is just glass. But increasing the roughness does not make sense to me. Alpha? My intuition is telling me not to use that either. So what is the answer?

I'll have to find out. During the initial courses I was just immitating what the instructor was doing, but now I am going to be making my own design decisions. It is by doing this that the material will really sink in. A few months of this will completely transform my art abilities. I've gone through the initial stage which is the hardest. In the intermediate stage is where the big gains will happen that will lead to people mistaking me for a pro."

---
## [i0Z3R0/Skribblio-Spam-Bot](https://github.com/i0Z3R0/Skribblio-Spam-Bot)@[b79907055e...](https://github.com/i0Z3R0/Skribblio-Spam-Bot/commit/b79907055ef76b23c36d6918600039c6a9cd4ee2)
#### Thursday 2022-01-13 19:31:19 by i0Z3R0

HOLY SHIT I FOUND THE ISSUE WITH NOT LEAVING WHEN KICKED IM AN IDIOT AAA

---
## [rijswijkschehc/takaro](https://github.com/rijswijkschehc/takaro)@[17429afdc7...](https://github.com/rijswijkschehc/takaro/commit/17429afdc70af48abceb8823c6b19c70d55fbcd1)
#### Thursday 2022-01-13 20:27:17 by Joost van Rijn

Sorry not sorry, this is an aweful commit… including the commit message

So we refactored a lot on the admin controller side, DRY’ed some shit.
Too much has happened, and I’m very much not proud of this. It’s a hail
Mary that everything keeps working in production and I pinkyswear I’ll
never ever do anything like this again…

Not without decent fucking test coverage anyway.

Much love <3 (And I actually am sorry)

---
## [diptikkat/bmlproduction.](https://github.com/diptikkat/bmlproduction.)@[398e26d8eb...](https://github.com/diptikkat/bmlproduction./commit/398e26d8eb2ac0b00a04ce5f31067390a79a9d50)
#### Thursday 2022-01-13 20:46:06 by diptikkat

Add files via upload

BML PRODUCTION has successfully provided technology and logistics planning solutions for renowned clients. With our in-house production and creative departments, set design and fabrication, AV warehouse, and strong support staff, BML PRODUCTION can tackle any project challenge, anywhere. Experience the difference with BML PRODUCTION.
With literally thousands of events in our portfolio, we have handled every type of corporate event imaginable. Events range from small group meetings with a single microphone and speakers to stadium-sized conferences with multiple projection screens and concert sound systems. If you're looking for an AV partner for your next corporate event, join the hundreds of satisfied businesses and meeting planners who cite BML Production as the best in the industry.

what we do
AWARDS – The Corporate Events team hosts gala dinners awards ceremonies and industry parties for 50 to 1500+ people. We provide a bespoke event design service and deliver state-of-the-art performance that meets your unique business objectives.

CORPORATE EVENTS: Our conference management includes end-to-end services, from conception to execution. Every step of the way, our team is by your side to manage the logistical details and provide expert advice to help you achieve your immediate goal and easily plan your next conference.
EXHIBITIONS - If you choose BML Production as your exhibition stand designer and want to make it stand out. As the main focal point of your event stage, waterproof structures, booths, pagodas, peak booths, custom booths, backdrops, booth design, photo booths and other finishing fabrications bring together essential elements of the event, such as lighting, sound, scenery and visual effects. to make an impact. your audience
FASHION SHOWS: When you are asked to plan a fashion show, the most important thing that comes to mind is the selection of the venue, the style of the stage, the judges and the style of the audience seats, the audio, the video, the lighting and the stage crew. BML Production works with show producers to coordinate events with a wide range of services including staging, rigging, concert sound, digital broadcasts, video projection and smart lighting.
LIVE CONCERTS - After Covid, we are virtually connecting artists and their fans on a virtual platform where they can listen and enjoy their singers, comedians, actors, etc. preferred from home, because health safety is now a big concern. We have digitized most of our event services. Contact us now to attend live worship services.
MEDICAL CONFERENCES - As organizers of corporate conferences and seminars, we recognize the critical factors that must be incorporated into the event. We take proper precautions, including a spacious, level space, safe seating, installation of high-end projection screens with high-end melodic structures, and a decent atmosphere for a formal gathering.
VIRTUAL CONFERENCES For over a decade, BML Production has provided customized virtual meeting and hybrid event solutions for our national and international clients. As the event landscape has changed, we've accelerated our discovery and design process and redoubled our capabilities to ensure our ideas and results meet the demands of our client's vision
PRODUCT INTRODUCTION Finding a suitable location can take time. Proximity is important because the location must be easily accessible to the target audience. The released product should also have some impact. Technical and space planning details should be covered. An online room directory like BML Production can support the selection and organization of rooms.

THEMED DECORATION - Our exclusive services ensure you are surrounded by magic and sparkle on your memorable day by aligning locations by color, period or even style. We will help you create any theme you have imagined.
ENTERTAINMENT-Specialized in musical entertainment services, planning, conceptualization of the general idea, management of scenic facilities, lights, sound, music, DJ, singer, band, international artists, Indian belly dance, musical show, LED video walls, LED bars, bartenders, supply complete theme decoration, floral decoration, etc. as required.

---
## [alxpettit/SimpleCreate-bin](https://github.com/alxpettit/SimpleCreate-bin)@[e4b065e473...](https://github.com/alxpettit/SimpleCreate-bin/commit/e4b065e473cedb99b291469a37c1fedb65a99671)
#### Thursday 2022-01-13 20:47:55 by Alexandria

actually, you know what? Fuck you. neither of them git the modpack

---
## [LittleHuman1/README.md](https://github.com/LittleHuman1/README.md)@[5062c2aec3...](https://github.com/LittleHuman1/README.md/commit/5062c2aec38677014e1ad894e213085045262ef3)
#### Thursday 2022-01-13 21:00:20 by LittleHuman1

README.md

Semantic Versioning 1.0.0-beta
In the world of software management there exists a dread place called “dependency hell.” The bigger your system grows and the more packages you integrate into your software, the more likely you are to find yourself, one day, in this pit of despair.

In systems with many dependencies, releasing new package versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a package without having to release new versions of every dependent package). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your project forward.

As a solution to this problem, I propose a simple set of rules and requirements that dictate how version numbers are assigned and incremented. For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.

I call this system “Semantic Versioning.” Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.

Semantic Versioning Specification (SemVer)
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it should be precise and comprehensive.

A normal version number MUST take the form X.Y.Z where X, Y, and Z are integers. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically by increments of one. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.

When a major version number is incremented, the minor version and patch version MUST be reset to zero. When a minor version number is incremented, the patch version MUST be reset to zero. For instance: 1.1.3 -> 2.0.0 and 2.1.7 -> 2.2.0.

A pre-release version number MAY be denoted by appending an arbitrary string immediately following the patch version and a decimal point. The string MUST be comprised of only alphanumerics plus dash [0-9A-Za-z-] and MUST begin with an alpha character [A-Za-z]. Pre-release versions satisfy but have a lower precedence than the associated normal version. Precedence SHOULD be determined by lexicographic ASCII sort order. For instance: 1.0.0.alpha1 < 1.0.0.beta1 < 1.0.0.beta2 < 1.0.0.rc1 < 1.0.0.

Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications must be released as a new version.

Major version zero (0.y.z) is for initial development. Anything may change at any time. The public API should not be considered stable.

Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.

Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes.

Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY include minor and patch level changes.

Tagging Specification (SemVerTag)
This sub-specification SHOULD be used if you use a version control system (Git, Mercurial, SVN, etc) to store your code. Using this system allows automated tools to inspect your package and determine SemVer compliance and released versions.

When tagging releases in a version control system, the tag for a version MUST be “vX.Y.Z” e.g. “v3.1.0”.

The first revision that introduces SemVer compliance SHOULD be tagged “semver”. This allows pre-existing projects to assume compliance at any arbitrary point and for automated tools to discover this fact.

Why Use Semantic Versioning?
This is not a new or revolutionary idea. In fact, you probably do something close to this already. The problem is that “close” isn’t good enough. Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By giving a name and clear definition to the above ideas, it becomes easy to communicate your intentions to the users of your software. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.

A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a library called “Firetruck.” It requires a Semantically Versioned package named “Ladder.” At the time that Firetruck is created, Ladder is at version 3.1.0. Since Firetruck uses some functionality that was first introduced in 3.1.0, you can safely specify the Ladder dependency as greater than or equal to 3.1.0 but less than 4.0.0. Now, when Ladder version 3.1.1 and 3.2.0 become available, you can release them to your package management system and know that they will be compatible with existing dependent software.

As a responsible developer you will, of course, want to verify that any package upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let Semantic Versioning provide you with a sane way to release and upgrade packages without having to roll new versions of dependent packages, saving you time and hassle.

If all of this sounds desirable, all you need to do to start using Semantic Versioning is to declare that you are doing so and then follow the rules. Link to this website from your README so others know the rules and can benefit from them.

FAQ
How do I know when to release 1.0.0?
If your software is being used in production, it should probably already be 1.0.0. If you have a stable API on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.

Doesn’t this discourage rapid development and fast iteration?
Major version zero is all about rapid development. If you’re changing the API every day you should either still be in version 0.x.x or on a separate development branch working on the next major version.

If even the tiniest backwards incompatible changes to the public API require a major version bump, won’t I end up at version 42.0.0 very rapidly?
This is a question of responsible development and foresight. Incompatible changes should not be introduced lightly to software that has a lot of dependent code. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.

Documenting the entire public API is too much work!
It is your responsibility as a professional developer to properly document software that is intended for use by others. Managing software complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your software, or what methods are safe to call. In the long run, Semantic Versioning, and the insistence on a well defined public API can keep everyone and everything running smoothly.

What do I do if I accidentally release a backwards incompatible change as a minor version?
As soon as you realize that you’ve broken the Semantic Versioning spec, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Remember, it is unacceptable to modify versioned releases, even under this circumstance. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.

What should I do if I update my own dependencies without changing the public API?
That would be considered compatible since it does not affect the public API. Software that explicitly depends on the same dependencies as your package should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to fix a bug or introduce new functionality. I would usually expect additional code for the latter instance, in which case it’s obviously a minor level increment.

About
The Semantic Versioning specification is authored by Tom Preston-Werner, inventor of Gravatars and cofounder of GitHub.

If you’d like to leave feedback, please open an issue on GitHub.

License
Creative Commons ― CC BY 3.0 http://creativecommons.org/licenses/by/3.0/

---

