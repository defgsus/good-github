## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-12](docs/good-messages/2022/2022-09-12.md)


2,034,122 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,034,122 were push events containing 3,036,783 commit messages that amount to 228,459,180 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6a5fdbc319...](https://github.com/treckstar/yolo-octo-hipster/commit/6a5fdbc3198e978685a18d79ec2a841716078740)
#### Monday 2022-09-12 00:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [EmberReed/EmberLuna_OverlayCTRL](https://github.com/EmberReed/EmberLuna_OverlayCTRL)@[6d02138290...](https://github.com/EmberReed/EmberLuna_OverlayCTRL/commit/6d02138290de5259c4ba72d99e218ed22f1de2eb)
#### Monday 2022-09-12 01:29:42 by EmberReed

Seems stable, so i think we're gonna go with it. One or two weird bugs still lurking tho. Mostly tested. Holy fuck that was scary

---
## [nervere/vgstation13](https://github.com/nervere/vgstation13)@[496d3bb777...](https://github.com/nervere/vgstation13/commit/496d3bb777d9538dd05b57d9a042acffd6496741)
#### Monday 2022-09-12 02:22:01 by ValkyrieSkies

Med/Sci mapping changes on Metaclub, also Bridge lightswitch (#33197)

* Metaclub Science Improvements

* Feature creep

* Fixes the god awful bridge wallpipes

---
## [Trollenstine/RicoAskinPuleDoomClone](https://github.com/Trollenstine/RicoAskinPuleDoomClone)@[7b0339a78f...](https://github.com/Trollenstine/RicoAskinPuleDoomClone/commit/7b0339a78fb332dfc6421c5b46a0392450b99855)
#### Monday 2022-09-12 03:00:52 by Trollenstine

1:1 In the beginning God created the heaven and the earth. 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[00d7e1f375...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/00d7e1f375b7f6f55f71d77be8c7612a6a5d6030)
#### Monday 2022-09-12 03:18:15 by SkyratBot

[MIRROR] Rocking The Boat, er, Map Vote [MDB IGNORE] (#16083)

* Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

* Rocking The Boat, er, Map Vote

Co-authored-by: san7890 <the@san7890.com>

---
## [EvanWright565/first-Repo](https://github.com/EvanWright565/first-Repo)@[60382f45bf...](https://github.com/EvanWright565/first-Repo/commit/60382f45bfdf6e10f26e7032b9115c35a6926d60)
#### Monday 2022-09-12 03:27:30 by EvanWright565

Update homework 2

Learning styles response




My thoughts on the subject vary because personally I go through all the different types of learning each day, honestly the most important part of learning for me is that I can actually be interested and engaged with what we are learning. The one case that does resonate with me heavily is when I first started learning guitar, you see I have dyscalculia so numbers and math do not do very well with me and a way you can learn guitar songs and rhythm through tab which is a use of numbers and lines and dear god it was hell for me so as the years went on I dropped Tab completely and have done much much better using my ears using auditory learning

---
## [ankitm123/terraform-operator](https://github.com/ankitm123/terraform-operator)@[779030735a...](https://github.com/ankitm123/terraform-operator/commit/779030735afb66e6763fa218e3fdb0f2e18b9d28)
#### Monday 2022-09-12 03:37:57 by Isa Aguilar

New v1alpha2 apiVersion

Many changes in a new api version. Most of the changes are backwards compatible.

**Inroducing v1alpha2**

Changes have been introdced into v1alpha2 to give users even more granularity and options to configure
the workflow tasks (formerly known as runners). Each task container can now have defined container
options, such as labels, annotations, envs and envFrom, and more

Along with the changes to task options, each task is now a stand-alone container in a pod. This
simplifies setting up tasks since there is no sharing of pod configuration aside from the common items,
such as envs, volumes, volume mounts and a few others.

And of the biggest change is that tasks do not have their execution scripts built into the containers
anymore. Instead, tasks will pull their tasks from an http source, read them from a configmap, or
have them defined inline in the tfo resource spec. Why this change? Frankly, it was very hard to
modify the execution scripts becuase they had to be baked into containers. Changing a simple fix
in the task execution meant having to build new images to hunderds of different terraform versions.

I hope that the ability to get the execution script from a source would encourage users to make
changes easily and then contribute back if they feel their changes could benifit the community.

**Migration from v1alpha1**

This is not fun to say, but until v1alpha1 is fully deprecated and removed, a conversion webhook has
been introduced to migrate existing v1alpha1 resources to fit the into v1alpha2. The challenge of
api change was how guarantee parity to a greatest extent. Unfortunately, some features have been made. The
features may be added back as a plugin or a separate controller in the future.

**Conersion webhook**

The conversion webhook is both a blessing and a curse. The beauty of it means users can continue to
use v1alpha1 to create new resources. The ugly part is that is has a rather large operational
burden.

If a user's cluster has cert-manager installed, this really isn't that bad. Otherwise, operators will need
to create ssl certs to secure the webhook endpoints so that kubernetes could communicate with it. It's
probably not as bad as it sounds. I'll document some of the ways to do this.

**Removals**

One such feature that has been removed is exportRepo. This feature, though useful when terraform may be needed
to be run outside of tfo, was always run in the background. This meant it wasn't tracked as
a first-class citizen of the tfo project. A new project might be added to reintroduce this back into
the tfo ecosystem.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[ae03d12cbe...](https://github.com/san7890/bruhstation/commit/ae03d12cbe76d8bde20ebc8f0451fb5f36344189)
#### Monday 2022-09-12 04:15:10 by san7890

Fixes Bread Smite Causing Some Fucked Up Shit

Hey there,

So basically, when you had the bread smite done on you, you were _just_ added to the contents of the bread. Nothing more. That means that you could pick it up. You couldn't add it to your bag (it would always return back into your hand(?)), but it would create some weird oddities that was just cursed in general. Let's make it so you can't hold the container that you are contained within by giving you HANDS_BLOCKED.

---
## [roynatech2544/android_kernel_samsung_j2y18lte](https://github.com/roynatech2544/android_kernel_samsung_j2y18lte)@[75a802089d...](https://github.com/roynatech2544/android_kernel_samsung_j2y18lte/commit/75a802089d562e2a646273cdcddf2fcd0a610b5b)
#### Monday 2022-09-12 05:14:25 by Masahiro Yamada

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

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[7990d8bec1...](https://github.com/ammarfaizi2/linux-fork/commit/7990d8bec16eb092f508b9c5bbf8ce20799f7701)
#### Monday 2022-09-12 05:41:04 by Johannes Weiner

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Monday 2022-09-12 06:41:05 by Xavier Morel

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
## [Molly-12/Shopping-blog](https://github.com/Molly-12/Shopping-blog)@[634eae9e34...](https://github.com/Molly-12/Shopping-blog/commit/634eae9e346d4c2ff619a8db1eb84c943795e8b4)
#### Monday 2022-09-12 13:31:19 by Molly-12

Code for the blog

<!DOCTYPE html>
<html>
  <head>
    <style>
        body{
            background-color:azure;
        }
        h1{
            background-color:black;
            font-size:medium;
            font-weight:bold;
            font-family: 'Times New Roman', Times, serif;
            color:beige;
            font-size: 50px;
        }
        p{
            background-color:lavender;
            font-size:medium;
            font-weight:bold;
            font-family: 'Times New Roman', Times, serif;
            color:black

        }
        
        
        h2{
            
            background-color:black;
            font-size:medium;
            font-weight:bold;
            font-family: 'Times New Roman', Times, serif;
            color:beige;
            font-size: 50px;

        }
        h3{
            background-color:blueviolet;
            font-size:medium;
            font-weight:bold;
            font-family: 'Times New Roman', Times, serif;
            color:black
        }
        h4{
            background-color:black;
            font-size:medium;
            font-weight:bold;
            font-family: 'Times New Roman', Times, serif;
            color:beige;
            font-size: 25px;
        }
        ul li{
        
            font-size:medium;
            font-weight:bold;
            font-family: 'Times New Roman', Times, serif;
            color:yellowgreen;
            font-size: 25px;
        }

        
    </style>
    

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
    <center>
    <h1>Fashion Quest</h1>
  </head>
  <body>
   
   <a href="#contact"> <img src="C:\Users\Dell\OneDrive\Documents\ethnic-trends-2020-2.jpg"/></a>
   <p>Clothing in India is dependent upon the different ethnicities, geography, climate, and cultural traditions of the people of each region of India. Historically, male and female clothing has evolved from simple garments like kaupina, langota, achkan, lungi, sari, well as rituals and dance performances. In urban areas, western clothing is common and uniformly worn by people of all social levels. India also has a great diversity[1] in terms of weaves, fibers, colours, and material of clothing. Sometimes, color codes are followed in clothing based on the religion and ritual concerned. The clothing in India also encompasses the wide variety of Indian embroidery, prints, handwork, embellishment, styles of wearing clothes. A wide mix of Indian traditional clothing and western styles can be seen in India.</p>
    
    <h1>Perfect guide to your Indian wear!</h1>
    <img src="C:\Users\Dell\OneDrive\Documents\3_b22278d1-6ce5-45ad-b46c-616625930f03_1024x1024.webp"/>
    <p>You look beautiful the way you are. Everyone is unique in their own way. So.. Lets just cherish the beauty of every living being.</p>
    <p>Though there are many different styles of skirts and shirts/blouses in Indian fashion, the most popular and recognizable combination is probably the lehenga choli. Wearing the lehenga choli style involves pairing a lehenga (a long, often pattern or embroidered, flared skirt) with a choli (a blouse that is tightly fitted at the waist).  Typically this style of Indian clothing for women is worn for a wedding and special occasions. It is also commonly paired with a chunri shawl/wrap that is draped over the head, similar to a veil.</p>
    <img src="C:\Users\Dell\OneDrive\Documents\Sidharth-Malhotra.jpg"/>
    <p>A well dressed man is better than shirtless man. so.. Be a gentleman with a pinch of Indianess.</p>
    
    <h2> Beautiful dress for a Beautiful Lady</h2>
    <h2>Dressing for the Festivals</h2>
    <img src="C:\Users\Dell\OneDrive\Documents\kiara_advani_in_royal_blue_fancy_lehenga_choli.jpg"/>
    <p>Always be true to your own sense of style, if you don't you'll be uncomfortable the whole time and it will show. Remember, NYFW is about expressing yourself and taking in what the designers have chosen to express through their new lines. Also it's important to wear shoes you'll be comfortable in all day. Obviously you want to look good, but you'll be on your feet all day long, so be prepared.</p>
    </center>
    <h4>Related Content</h4>

    <header>
      <ul>
        <li>How to style a lehenga</li>
        <li>When Print Is Too Much</li>      
        <li>The Overalls Trend</li>
        <li>Fall's It Color: Blush</li>
        <li>the color of season is black</li>
      </ul>
    
    </header>
    <div id="contact">
      <p><strong>email</strong>: isa@fashionblog.com | <strong>phone</strong>: 917-555-1098 | <strong>address</strong>: 371 284th St, New York, NY, 10001</p>
    </div>
  </body>
</html>

---
## [gsteel/technical-steering-committee](https://github.com/gsteel/technical-steering-committee)@[546ca04712...](https://github.com/gsteel/technical-steering-committee/commit/546ca0471243fca55dfa64a02d4a97d1d3e9d0f7)
#### Monday 2022-09-12 13:50:28 by Michał Bundyra

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
## [benjaminhuth/acts](https://github.com/benjaminhuth/acts)@[6e1fd31474...](https://github.com/benjaminhuth/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Monday 2022-09-12 14:17:57 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [rdragan/tgstation](https://github.com/rdragan/tgstation)@[b4f19a7e0f...](https://github.com/rdragan/tgstation/commit/b4f19a7e0fc3802856ec4117eb71418287c51ac6)
#### Monday 2022-09-12 14:32:19 by John Willard

Greatly increases Pun Pun's abilities and strengths (using desk bells, cross stun immunity) (#68870)


About The Pull Request

Pun Pun has a new AI, with it they received the following:

    Instead of screeching/roaring/scratching/jumping/rolling, Pun Pun will instead sing/dance/bow/clear throat/sign.
    Pun Pun now rings desk bells instead of finding random shit to pick up, and doesn't intentionally seek out weapons.
    Pun Pun has a higher chance of giving people stuff in their hand, so the Bartender can give them a drink and let them go walking around.

Additionally:

    Pun Pun is now immune to being hardstunned by walking into them, giving them a little more bite for greytiders beating them up.
    Monkeys can now use desk bells.

Why It's Good For The Game

I like Pun Pun and when Monkey AIs were originally added, there was a note about giving them a unique AI. Since we're slowly turning the poor monkey into an actual Bartender assistant, I find it thematic that they would ring the bell and give out drinks in their hand, as if the Bartender taught them themselves.

For the hardstun immunity, I mostly did it because I find it annoying for a Bartender to have to carefully navigate around Pun Pun to not knock them over and make them drop an instrument (or anything else) in their hand, but it also works as a buff to people trying to kill them. Pun pun is a unique monkey so I don't believe they should be as easy to kill as any other.

Desk bell addition was necessary for Pun Pun to use it.
Changelog

cl
add: Pun Pun now gives stuff in their hand frequently and rings desk bells.
add: Pun Pun now has gentleman-like emotes, rather than screeching and roaring.
balance: Pun Pun no longer looks for weapons in their off time.
balance: Pun Pun is no longer vulnerable to stuns by being walked into.
qol: Monkeys can now use desk bells.
/cl

---
## [wfleming/advent-of-code](https://github.com/wfleming/advent-of-code)@[62bbcf3226...](https://github.com/wfleming/advent-of-code/commit/62bbcf3226256a5e2c4cfbe955ce133f2ad61781)
#### Monday 2022-09-12 15:55:34 by Will Fleming

2021 d19

This one drove me a bit crazy, but for dumb reasons.

I started by figuring out all the rotations, but initally rather than
just ending up with a list of final states I coded a series of rotations
building off each other, based on the first bit of output from
`rotations.rb`. Something like:

```
os = [self]
os = rotate_axis_90(:x)
os = os.last.rotate_axis_90(:x)
os = os.last.rotate_axis_90(:x)
...
os = os[8].rotate_axis_90(:y)
```

It looked ok so I moved on. That was a mistake I'll get back to.

Then for the core of the algorithm I started with a pretty naive
approach: for each pair of scanners (with a position-known scanner on
the left, position-unknown on the right), I iterated through every
orientation and looked for overlaps. That worked, but it was slow. But
it did at least allow me to answer part 1 for the example input in
reasonable time.

I got the squared-distances idea from the reddit solutions thread, and
that sped things up. I saw various approaches to how this affects the
cutoff, and I'm not certain what's 100% correct. I *think* my "/ 2"
approach is correct because if you have 6 overlapping distances that
implies up to 12 potential matching points (2 per distance). The same
point could belong to more than 1 of those pairs, so it could be less &
I could filter more on that, but in practice this seems good enough.

At that point I was basically just using the squared distances on a
filter before my previous fairly-inefficient implementation: if there
were 6 matching distances I then just iterated through *every* possible
pt/orientation again. I realized that was unecessary, and I only needed
to check all the pts from the overlapping sq distances.

At that point it was pretty fast and I was getting the correct answer on
the example input, but getting stuck after several iterations on my real
input. It would hit an iteration where it couldn't find any more matches
for remaining scanners. I banged my head on that for an embarrasingly
long time and went down a lot of false paths, and finally realized I had
a dumb bug in my rotation code. I had made a mistake transcribing all
the rotations, and was therefore actually doing the same rotation more
than once, and so I had a list of 24 items but there were dupes and only
18 distinct rotations. It took me way longer to find this than it should
have partially because I'd written a unit test, and *thought* I'd
checked `uniq.count` in the test, but... no, I'd just checked `.count`,
so my test was not testing what I thought. I guess I was just (un)lucky
with the example input, and the rotations I *had* included were
sufficient to match all the scanners.

I fixed that dumb bug by updating rotations.rb to derive the final
states and just code those, and then everything was fine and p2 was
trivial. Lessons learned: I knew the "rotations-on-rotations" code was a
bit brittle and tricky to write correctly, I should have paid more
attention to that thought and stopped myself earlier. Also I should have
checked my own assumptions more carefully about what I'd actually
written in the tests.

This runs both parts in 1.4s on my laptop, so I'm reasonably happy with
this.

---
## [gnoff/react](https://github.com/gnoff/react)@[b6978bc38f...](https://github.com/gnoff/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2022-09-12 16:16:06 by Andrew Clark

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
## [LewdDeveloper/lmaobox-scripting](https://github.com/LewdDeveloper/lmaobox-scripting)@[7ae8fd063f...](https://github.com/LewdDeveloper/lmaobox-scripting/commit/7ae8fd063f6231af7f05b6128ef856516e013967)
#### Monday 2022-09-12 17:43:01 by I fucking hate Rap

bla bla bla idc fuck you go write a renderer and menu library

---
## [YeOldeInn/agins-archive](https://github.com/YeOldeInn/agins-archive)@[7ef40f3cec...](https://github.com/YeOldeInn/agins-archive/commit/7ef40f3cec27d26f89d2d3b8705fa2366e1f79ac)
#### Monday 2022-09-12 18:22:04 by T. Joseph Carter

Migrating to new quest table (Unfinished)

This has been over a week in the making and I'm not finished with it
yet. Why commit it now? Because I almost fucked up. I deleted
quests.html. Fortunately it was open in my editor and I could just save
a new copy. The best backup in the world is to put your code on the
Internet.

So, there are 21 quests missing here. That's … less than half, but it's
still 40% of the quests needing to be converted to "markdown" format.

I say "markdown" because … none of these markdown files in the _quests
collection actually contain "markdown" content. The files are entirely
yaml front matter. Sure, a fair bit of it is written in Markdown, but
ideally the reqs would be reworked so they were done similarly to the
filenames. I just can't be arsed to do it—it's taken me long enough to
do them as they are right now!

Yes, I've been sick, which has had my stuffed up head feeling kind of
fuddled. Yes, I've had other things happening. But still, I need this
to get done.

Jekyll, the software that is builting the website on Github, has a
notion of "collections". If you know anything about Jekyll, the _posts
directory is a collection that's hardcoded to exist and defaults to
output: True. Others you have to define and output: False is the default
(which means they're not rendered into _site with the rest of your
output…)

I created _quests as an output: false collection. I can still access all
the front matter andd page content from another page (which is how you
get a blog's listing page made from individual posts), but on this site
the individual quest packs don't get their own pages. That's why the
content is blank. If anything the content should be the description of
the pack I guess, but I decided to make it part of the front matter too,
at least for the time being.

It's easy to change, but I doubt I will until I start doing a quests
page for YOI. I'm trying to change as little as possible on Agin's Inn
since it's supposed to be an archive. I'm just having to change a lot
more than I bargained for to make the content work everywhere.

Oh yeah, I buried the lede on that one pretty deep. If you're on
Windows, press ctrl-shift-on the github.io agins-archive page. Set the
page width to 900, then go to New Quests. Change the width to 899. Isn't
that freakin' cool? The entire table (the one I've been working on
anyway) changes from a really wide horizontal table to a list of tables
each containing one quest, vertically.

And yes, it sizes down! It works all the way down to 400px! Smaller than
400, it breaks. *sigh* Fixing that is low priority, but I can fix it. I
wouldn't bother except I think I know why it doesn't work at 400, and
I've made other things work all the way down to 320. If your device
doesn't have 320px width … um.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[553d0f46fe...](https://github.com/san7890/bruhstation/commit/553d0f46febe9d87ef52bf2f1e8219c972ac19cc)
#### Monday 2022-09-12 18:59:56 by san7890

we do a bit of component trolling

THIS TOOK ME TWO HOURS FUCK YOU

---
## [FreemindTrader/StockSharp](https://github.com/FreemindTrader/StockSharp)@[bfe46d1972...](https://github.com/FreemindTrader/StockSharp/commit/bfe46d1972f3d157d0bc881513b59f290558c3a2)
#### Monday 2022-09-12 19:09:25 by Freemind

I don't know WTF happened to the code. How come all those ecng shit will cause the software to fucked up. Please tell me........BTW, in the future, if I see those comments, I am drunk. Happy as always......Not really sure.....I think My happiness comes from Pearl, I love her....I guess which is no matter what....dont' really feel like she loves me alot....But...I still believe that and can feel it too...She should also love me tool

---
## [RedMisao/Cataclysm-DDA-Touhou-Mod](https://github.com/RedMisao/Cataclysm-DDA-Touhou-Mod)@[f3709eb626...](https://github.com/RedMisao/Cataclysm-DDA-Touhou-Mod/commit/f3709eb6266a2ea9506e8ccd4e3a5d0fbd088d7d)
#### Monday 2022-09-12 20:09:02 by KaenbyouA

0.9.3.14

- (Updated to 2022-09-09 experimental)

Spells:
- Aya: added a custom dash, Deadline day (movement speed buff), Draft blast (low dmg aoe that pushes items far away), Maple fan wind (deals low dmg and stuns an enemy for a duration), Maple fan tornado (improved aoe Maple fan wind), Wind sickle veiling (wind armor that reduces some physical attacks and deals cut dmg)
- Meiling: Mountain breaking cannon (charged punch with huge damage), Red energy release (low dmg punch that breaks terrain), Tiger energy release (aura that increases her melee damage)
- Reisen: Entanglement (swap positions with a targeted creature), Optimism (limb dmg balance, small heal and small pain recovery), Probability noise (dodge + dmg reduction + movement reduction effect cleanse), Uncertainty box (unsafe random aoe teleport)
- Remi: tweaked existing spells, added Vampiric aura, changed Scarlet shot for Demons' dinner fork (repeated aoe attack)
- Youmu: added Double wheel (summons a copy that slashes nearby enemies), Half-body (summons Myon to shoots enemies), Reflection slash (bullet-protecting barrier), Slash of the eternal future (random number of slashes, dmg scales with level), Slash of nether meditation (heavy, long sword attack)

Monsters:
- Added Agoniatites, Cleoniceras, Endoceras, Herpetotherium, Michelinoceras, Nochnitsa, Paracoroniceras, Parapuzosia, Taeniolabis, Viatkogorgon, including reproductive data and spawning

Misc changes:
- Youmu now uses her own martial arts, her CMBs were removed
- Rebalanced some professions skills
- Reduced Aya's, Utsuho's and Remi's movement speed
- Now all professions cost 4 points
- Added some magical materials for the auras
- Removed a bunch of starting locations, left only those with an outdoors start
- Removed the (arbitrary) loudness values for the Lunarian weapons

Fixes
- Some spells not working as intended
- Sakuya's knives being too fragile
- Remi's Gungnir being 30 meters long instead of 3
- Swimming monsters being slower than intended

---
## [aoleary/G4-Titan-Kernel](https://github.com/aoleary/G4-Titan-Kernel)@[dbf4f650a1...](https://github.com/aoleary/G4-Titan-Kernel/commit/dbf4f650a1472d973aee928d886333079f116e1a)
#### Monday 2022-09-12 20:45:18 by Petr Mladek

kthread: add kthread_create_worker*()

Kthread workers are currently created using the classic kthread API,
namely kthread_run().  kthread_worker_fn() is passed as the @threadfn
parameter.

This patch defines kthread_create_worker() and
kthread_create_worker_on_cpu() functions that hide implementation details.

They enforce using kthread_worker_fn() for the main thread.  But I doubt
that there are any plans to create any alternative.  In fact, I think that
we do not want any alternative main thread because it would be hard to
support consistency with the rest of the kthread worker API.

The naming and function of kthread_create_worker() is inspired by the
workqueues API like the rest of the kthread worker API.

The kthread_create_worker_on_cpu() variant is motivated by the original
kthread_create_on_cpu().  Note that we need to bind per-CPU kthread
workers already when they are created.  It makes the life easier.
kthread_bind() could not be used later for an already running worker.

This patch does _not_ convert existing kthread workers.  The kthread
worker API need more improvements first, e.g.  a function to destroy the
worker.

IMPORTANT:

kthread_create_worker_on_cpu() allows to use any format of the worker
name, in compare with kthread_create_on_cpu().  The good thing is that it
is more generic.  The bad thing is that most users will need to pass the
cpu number in two parameters, e.g.  kthread_create_worker_on_cpu(cpu,
"helper/%d", cpu).

To be honest, the main motivation was to avoid the need for an empty
va_list.  The only legal way was to create a helper function that would be
called with an empty list.  Other attempts caused compilation warnings or
even errors on different architectures.

There were also other alternatives, for example, using #define or
splitting __kthread_create_worker().  The used solution looked like the
least ugly.

Link: http://lkml.kernel.org/r/1470754545-17632-6-git-send-email-pmladek@suse.com
Signed-off-by: Petr Mladek <pmladek@suse.com>
Acked-by: Tejun Heo <tj@kernel.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Steven Rostedt <rostedt@goodmis.org>
Cc: "Paul E. McKenney" <paulmck@linux.vnet.ibm.com>
Cc: Josh Triplett <josh@joshtriplett.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: Jiri Kosina <jkosina@suse.cz>
Cc: Borislav Petkov <bp@suse.de>
Cc: Michal Hocko <mhocko@suse.cz>
Cc: Vlastimil Babka <vbabka@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[f11633bb13...](https://github.com/ammarfaizi2/linux-fork/commit/f11633bb13a73c9c8bd3bb0d17feff198db97f19)
#### Monday 2022-09-12 22:11:10 by Peter Xu

mm/x86: use SWP_TYPE_BITS in 3-level swap macros

Patch series "mm: Remember a/d bits for migration entries", v4.


Problem
=======

When migrating a page, right now we always mark the migrated page as old &
clean.

However that could lead to at least two problems:

  (1) We lost the real hot/cold information while we could have persisted.
      That information shouldn't change even if the backing page is changed
      after the migration,

  (2) There can be always extra overhead on the immediate next access to
      any migrated page, because hardware MMU needs cycles to set the young
      bit again for reads, and dirty bits for write, as long as the
      hardware MMU supports these bits.

Many of the recent upstream works showed that (2) is not something trivial
and actually very measurable.  In my test case, reading 1G chunk of memory
- jumping in page size intervals - could take 99ms just because of the
extra setting on the young bit on a generic x86_64 system, comparing to
4ms if young set.

This issue is originally reported by Andrea Arcangeli.

Solution
========

To solve this problem, this patchset tries to remember the young/dirty
bits in the migration entries and carry them over when recovering the
ptes.

We have the chance to do so because in many systems the swap offset is not
really fully used.  Migration entries use swp offset to store PFN only,
while the PFN is normally not as large as swp offset and normally smaller.
It means we do have some free bits in swp offset that we can use to store
things like A/D bits, and that's how this series tried to approach this
problem.

max_swapfile_size() is used here to detect per-arch offset length in swp
entries.  We'll automatically remember the A/D bits when we find that we
have enough swp offset field to keep both the PFN and the extra bits.

Since max_swapfile_size() can be slow, the last two patches cache the
results for it and also swap_migration_ad_supported as a whole.

Known Issues / TODOs
====================

We still haven't taught madvise() to recognize the new A/D bits in
migration entries, namely MADV_COLD/MADV_FREE.  E.g.  when MADV_COLD upon
a migration entry.  It's not clear yet on whether we should clear the A
bit, or we should just drop the entry directly.

We didn't teach idle page tracking on the new migration entries, because
it'll need larger rework on the tree on rmap pgtable walk.  However it
should make it already better because before this patchset page will be
old page after migration, so the series will fix potential false negative
of idle page tracking when pages were migrated before observing.

The other thing is migration A/D bits will not start to working for
private device swap entries.  The code is there for completeness but since
private device swap entries do not yet have fields to store A/D bits, even
if we'll persistent A/D across present pte switching to migration entry,
we'll lose it again when the migration entry converted to private device
swap entry.

Tests
=====

After the patchset applied, the immediate read access test [1] of above 1G
chunk after migration can shrink from 99ms to 4ms.  The test is done by
moving 1G pages from node 0->1->0 then read it in page size jumps.  The
test is with Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz.

Similar effect can also be measured when writting the memory the 1st time
after migration.

After applying the patchset, both initial immediate read/write after page
migrated will perform similarly like before migration happened.

Patch Layout
============

Patch 1-2:  Cleanups from either previous versions or on swapops.h macros.

Patch 3-4:  Prepare for the introduction of migration A/D bits

Patch 5:    The core patch to remember young/dirty bit in swap offsets.

Patch 6-7:  Cache relevant fields to make migration_entry_supports_ad() fast.

[1] https://github.com/xzpeter/clibs/blob/master/misc/swap-young.c


This patch (of 7):

Replace all the magic "5" with the macro.

Link: https://lkml.kernel.org/r/20220811161331.37055-1-peterx@redhat.com
Link: https://lkml.kernel.org/r/20220811161331.37055-2-peterx@redhat.com
Signed-off-by: Peter Xu <peterx@redhat.com>
Reviewed-by: David Hildenbrand <david@redhat.com>
Reviewed-by: Huang Ying <ying.huang@intel.com>
Cc: Hugh Dickins <hughd@google.com>
Cc: "Kirill A . Shutemov" <kirill@shutemov.name>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Andi Kleen <andi.kleen@intel.com>
Cc: Nadav Amit <nadav.amit@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Dave Hansen <dave.hansen@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [derfelot/android_kernel_sony_msm8998](https://github.com/derfelot/android_kernel_sony_msm8998)@[070a9b0538...](https://github.com/derfelot/android_kernel_sony_msm8998/commit/070a9b0538a1fb65aaad050bd8dcac9759158974)
#### Monday 2022-09-12 22:52:16 by Christian Brauner

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

