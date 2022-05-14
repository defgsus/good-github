## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-13](docs/good-messages/2022/2022-05-13.md)


1,760,914 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,760,914 were push events containing 2,831,343 commit messages that amount to 203,377,632 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [lingonberry1234/Citadel-Station-13-RP](https://github.com/lingonberry1234/Citadel-Station-13-RP)@[e88f63cd33...](https://github.com/lingonberry1234/Citadel-Station-13-RP/commit/e88f63cd33d7e9bd0322ddb33de4cd6a5fb15fa7)
#### Friday 2022-05-13 00:01:13 by silicons

refactors some gun things (#4036)

* wow

* wack

* fix

* fix

* fuck you

* i am declaring war on gun devs

* fix

* fix

Co-authored-by: fake_vm_user <fake_vm_user>

---
## [beneliezer/catseyexi](https://github.com/beneliezer/catseyexi)@[69b7bb4322...](https://github.com/beneliezer/catseyexi/commit/69b7bb43228902ad0fb0648d8ec9f4fabe0241a4)
#### Friday 2022-05-13 00:45:36 by NeuromancerXI

Fixes SQL Async Causes High CPU Load
Noticed very high CPU Load on an idle server instance. With the guidance
of zach2good, added a sleep condition to prevent the process from
running wild and eating CPU for breakfast, lunch, and dinner.

Co-authored-by: Zach Toogood <zrtoogood@gmail.com>

---
## [shobbs528/FinalProject_a3](https://github.com/shobbs528/FinalProject_a3)@[2bc0109088...](https://github.com/shobbs528/FinalProject_a3/commit/2bc0109088bbf68a1b9c0e6f7407b55c7314f550)
#### Friday 2022-05-13 00:49:35 by shobbs528

sound working and seemingly in 3D

Is it a bird? Is it a plane? No, it's a sound. But it's coming from somewhere! You know what they say about big sounds? They come from big sad people. That's me, I'm big sad. Oh yeah, I also turned down the volume on most of the sounds so your poor eardrums don't end up in San Francisco every time you play the game cause yeah tinnitus isn't that fun. Anyway, talk to you in a min. Also did you know that toasters toast toast? DO you know how to make a pool table laugh? Put the balls in the holes. Anyway, I'm pretty sure sound is okay now.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[a3c8013b45...](https://github.com/timothymtorres/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Friday 2022-05-13 01:17:02 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

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

---
## [Lastprismer/FargowiltasSouls](https://github.com/Lastprismer/FargowiltasSouls)@[fcab2aeda1...](https://github.com/Lastprismer/FargowiltasSouls/commit/fcab2aeda1174df4fe6f7465e27984fafe183f20)
#### Friday 2022-05-13 01:17:26 by terrynmuse

sprites
 squirrel coat of arms
 dread shell (shield also applies to lump, soul of siblings)
renamed heart of eternal and soul of siblings to heart/soul of master, fuck you master mode

---
## [tikimcfee/LookAtThat](https://github.com/tikimcfee/LookAtThat)@[1addf1d4dd...](https://github.com/tikimcfee/LookAtThat/commit/1addf1d4dd0c576cf9e219af6a5049bb6c9bc5e8)
#### Friday 2022-05-13 04:16:23 by Ivan Lugo

- SemanticInfoCategoryView is a thing
- GlobalSemantics are a thing too
- Cache by category, snapshot on view, gives random access to known info
-- TODO: Do the global part now. Maybe file selected + sub window?
-- Maybe just CategoryXMapArrays
-- RandomAccessCollection -> startIndex / endIndex / subscript(index)
-- Make a fake RAC by wrapper participant keys + maps

! ALSO HOLY SHIT IT WORKS ON THE IPAD OF COURSE IT DOES WHY DIDN'T I TRY THIS FIRST
! SERIOUSLY HOLY SHIT ALL OF A SUDDEN I HAVE A RIDICULOUS USE CASE!
! Lol I'm going to sit with the iPad on the side of the laptop, app open, receiving LSP commands, rendering them
! This is fun. This is just fun.

---
## [funnycorp/Forage](https://github.com/funnycorp/Forage)@[f1f6792c5c...](https://github.com/funnycorp/Forage/commit/f1f6792c5c5273a3d2d8d79e64c9ea704556905a)
#### Friday 2022-05-13 04:33:50 by CountBleck

Remove rotating background from pages

This honestly did not make anything look noticably better, and
it used unsupported features and ugly hacks to make it work.

---
## [adamqqqplay/dota2ai](https://github.com/adamqqqplay/dota2ai)@[0287c0dc90...](https://github.com/adamqqqplay/dota2ai/commit/0287c0dc90cd236fe5885a1520625d6d7e005e95)
#### Friday 2022-05-13 07:43:42 by Aaron Song

Update for 7.31c (#69)

Fix legion_commander;
Fix abaddon cast certain abilities on creep heroes;
Fix drow_ranger, clinkz, silencer auto-cast abilities cast whenever possible;
Prevent crystal_maiden from casting frostbite on antimage_counterspell;
Add doom_bringer auto-cast devour when devouring better creeps;
Fix jakiro doesn't cast liquid_fire, liquid_frost on buildings;
Decrease desire of lich casting frost_armour on creeps;
Fix abyssal_underlord casting pit_of_malice on non-teleporting enemeis;
Fix mirana casting moon_shadow on creep heroes;
Add necrolyte casting reapers_scythe on teleporting enemies;
Prevent slardar from casting corrosive_haze on affected units;
Decrease desire of undying casting decay on creeps;
Change brewmaster, viper ability level-up up to 7.31c;
Prevent nyx_assassin casting impale on magic immune targets;
Prevent venomancer casting venomous_gale on magic immune targets;
Decrease desire of warlock casting upheavel on creeps;
Fix typos in winter_wyvern source;
Change item build lists of some heroes;
Fix errors in slardar;
Prevent undying from casting decay on creep heroes;
Fix bounty_hunter uses track at ally lone_druid_bear;
Fix chen ability level up to 7.31c;
Fix enchantress_enchant neutral creep level limit to 7.31c;
Fix terrorblade uses reflection or sunder at creep heroes;
Forbid bane casting nightmare on transforming lone_druid;
Fix abyssal errors;

---
## [AJPfleger/acts](https://github.com/AJPfleger/acts)@[6e1fd31474...](https://github.com/AJPfleger/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Friday 2022-05-13 07:48:23 by Stephen Nicholas Swatman

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
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[8c36d9f9c7...](https://github.com/newstools/2022-new-york-post/commit/8c36d9f9c7ef7fea23af0af75de8df17162d6f05)
#### Friday 2022-05-13 07:51:06 by Billy Einkamerer

Created Text For URL [nypost.com/2022/05/12/im-an-overprotective-girlfriend-and-i-have-8-strict-rules-for-my-boyfriend/]

---
## [chrfoyer/Yes_SEP2](https://github.com/chrfoyer/Yes_SEP2)@[2a9753578c...](https://github.com/chrfoyer/Yes_SEP2/commit/2a9753578c39793541d422eb3848b50f01bf4794)
#### Friday 2022-05-13 08:48:57 by Raedrim

https://youtu.be/k2W9wA6J4sw

Cock and ball torture (CBT), occasionally known as penis torture, dick torture, or male genitorture/male genital torture, is a sexual activity involving the application of pain or constriction to the penis or testicles. This may involve directly painful activities, such as genital piercing, wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation, kneeing or kicking.[1] The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.[2]
Contents

---
## [et84121/rx-player](https://github.com/et84121/rx-player)@[0284938a2b...](https://github.com/et84121/rx-player/commit/0284938a2b76ce6abf36a01c00fa304d839b1bc7)
#### Friday 2022-05-13 09:50:44 by Paul Berberian

fix unknown active Period happening when switching rapidly between Representation

One of the application using the RxPlayer at Canal+ experienced
recently a new strange bug:
Some methods, like `getAvailableVideoBitrates`, would always return an
empty array, even when it is evident that there are multiple video
bitrates available.

After some quick checks, it turned out that multiple RxPlayer API were
in the same case and that this was due to the RxPlayer `API` module not
knowing which `Period` (subpart of the current content with its own
tracks and bitrates characteristics) was being played.

---

The `API` module relies on the `Stream` module's `ActivePeriodEmitter`
to know which `Period` is being played.

This last part (the `ActivePeriodEmitter`) knows which Period is the
"active Period" by exploiting a side-effect of the current `Stream`
behavior:

The "active Period" is the first chronological Period for which each type
of buffer ("audio", "video", "text") has a corresponding active
`RepresentationStream`.
Why this weird rule is used (instead of simpler solutions like relying
on the current position) is out of the scope of this message.

Anyway, turns out there was a pretty big bug in that
`ActivePeriodEmitter`:
If multiple `RepresentationStream` were created for a single buffer type
(audio, video, text) before other buffer types had their first one for
a given `Period`, it would be possible to never be able to emit this
`Period` as "active".

The source of the error seems to be due to a very evident logical error.
What was written as:
```js
if (A && B) {
  // Do thing
} else {
  // Do other thing
}
```
Should have been written:
```js
if (A && B) {
  // Do thing
} else if (!B) {
  // Do other thing
}
```
or more succintly (and simply):
```js
if (!A) {
  // Do other thing
} else if (B) {
  // Do thing
}
```

I like to talk about this type of error as "logical typos" because it
makes no sense when you read it, yet was most likely written with
well-thought logic in mind, it's just that the execution was poorly
done.

---

Now the biggest question is why are we seeing this more than 2-years-old
bug only now and not before?

I think it may be because we've been lucky (though I prefer to consider
us to be unlucky here, I generally prefer immediately-catched errors):

  1. Most contents have only one Period, and in those we usually will
     create synchronously a single `RepresentationStream` per type at
     the beginning.
     In this case, no error happens.

  2. Even for multi-Period contents, chances are that text and audio
     `RepresentationStream`, which generally are much less heavy and
     thus are pre-loaded faster, will be created before the video one,
     and we very rarely switch between audio or text Representations.

     Thus we rarely switch between audio or text `RepresentationStream`
     before the first video `RepresentationStream` is anounced and thus
     don't see any bug.

There might be other causes. I'm very surprised that we never either
catched this bug or seen some weird related behavior on multi-Period
contents due to this bug.

---
## [et84121/rx-player](https://github.com/et84121/rx-player)@[de7e66b921...](https://github.com/et84121/rx-player/commit/de7e66b921dc8c803cafd38b4d25bd1c9c82d777)
#### Friday 2022-05-13 09:52:28 by Paul Berberian

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a064b35b25...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Friday 2022-05-13 10:32:05 by SkyratBot

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[371199ad79...](https://github.com/mrakgr/The-Spiral-Language/commit/371199ad79a3f50eea5efd1fe60b063278d220b5)
#### Friday 2022-05-13 10:50:45 by Marko Grdinić

"9:55am. Let me read Kaiji and then I will get started with sculpting.

10:15am. Er, let me take a look at the Estab Life thread and then I'll get started. ...No thread. Nwm, let me get started then.

Also I hadn't gotten a reply to that Painter issue yet.

10:25am. Right now I am on vid 10/50 where I left off last time. It seem he is creating a stroke and projecting it all around the sphere. By creating a stroke, it seems he draw it as an outline on the canvas. I've been looking for a feature such as that for a while. Good that I found it.

10:35am. Damn it, the fact that I am starting to lean towards grinding 2d is sapping my will to study this course. I am the kind of guy who if he thinks he has to do something - he will do it. And that includes dropping whatever I am doing to pursue what I should.

Even thought it seems like I have been grinding arbitrary stuff, I've always believed in that the task at hand needed doing.

https://youtu.be/Ll5y29Nfw4k
028 Projection Master Overview

Just what is projection master. The guy doing the course did not explain what he is doing.

Hmmm, ok. Let me give it a try.

http://docs.pixologic.com/user-guide/3d-modeling/sculpting/projection-master/
> Projection Master is a unique feature of ZBrush that allows you to use all of the 2D and 2.5D brushes in sculpting, texturing, and otherwise working with your 3D model.

11:10am. This is so annoying. How do I get out of this stupid thing?

Also for me it only drew on a single side. Let me watch the video again. As well, how did he duplicate the stroke? By pressing S. No, he said S, but he actually pressed Shift + S. He also keeps saying that activating Projection master is G while it is really Shift + G.

What is shift + F? It is doing something, but I am not sure what.

11:25am. I have no idea what is going on anymore. Let me reload the file. I am really on the verge of dropping this course. Let me just finish this video at least.

11:35am. Right now, it works fine for me.

https://youtu.be/I1uZqeefd28
Architectural techniques with Sebastian Legrain using Projection Master - Part 4

This is 13 years old by now, but let me watch it. It seems that nothing is simple when it comes to 3d. It is just tutorials, tutorials, tutorials. Let me finish this and I will move on.

https://youtu.be/I1uZqeefd28?t=76

Yes, if it merely doing those ridges, I could have just used radial symmetry. Why is he bothering me with projection master?

One of the problems that I am having is that I do not understand how to properly dig in.

https://youtu.be/I1uZqeefd28?t=233

I am guessing that at this point they did not have the clip and trim curve brushes.

11:45am. He did not even use projection master.

https://youtu.be/49GN9RtoBkU?t=146

It is really lame how double sides would not work unless you also have the display option turned on.

https://youtu.be/49GN9RtoBkU?t=454

Hmmm, this might have been what was going on.

https://youtu.be/49GN9RtoBkU?t=804

It seems with ZApplink it is possible to set up a canvas in Photoshop and link it to Zbrush via Projection Master.

12:05pm. https://youtu.be/udHde70UZ6A
029 Hard Surface VDM Projection Master

Let me watch this since he will be using it for hard surface shapes.

12:15pm. Let me get back to the course.

12:20pm. Enough, I am done with this.

I do not want to deal with anymore of 3d's complexity.

If I had my mind on a brain core and was able to duplicate myself, I could parallelize the various workloads very neatly in 3d. But right now having to know all this stuff is really killing my pace. 3d is not viable as a 2d replacement. I am absolutely sure of that.

I just do not have the time to develop this path properly as a human.

I am going to sit down and start grinding 2d from here on out. if I need 3d, I'll be sure to bring it in. I can do the rest of the Zbrush course later whenever I feel like it.

12:25pm. Right now I am absoutely sure that nothing will stop me from getting to 3/5 in 3d as long as I put in the effort. But 2d is different. Plenty of people get stuck at the lower levels in it.

I get the sense that I should be able to do it, but I am going to have to make sure of that.

In school I was always bad at it, but I don't think I've ever had the sense of breaking the scene down into the constituent steps. I never even understood the purpose of sketching back then, so it is no wonder I was so poor at it.

Every time I did art back then, I had the image of what I wanted to do and just started mucking about to poor results. I just dove in without planning and got discouraged when it did not give me the results that I wanted.

I don't think I've ever improved despite years of art classes in school.

12:30pm. I am simply going to have to face this demon and hunt it down.

It is one thing to draw or paint from imagination, but I should get to a high level in copying what is in front of me. There is just no reason I should ever be weak at that as an artist.

12:35pm. I am going to make my first target the middle and back of the room. The monitor, the rig, the desk and the radiator are near the entrance at the back, but turning 90 degrees would give me the beds and the balcony door as well as the shelves and the boxes on top with the rig being partially to the side.

12:35pm. I am just so tired at this point.

Pumping out elaborate 3d scenes is beyond my ability unless I want to take a month per each. I might get faster if I persevere, but I'll never be able to overcome the strain of constant context switching between several different applications.

With Clip Studio Paint, I have a single tool that could do anything I'd need. Just that would speed things up significantly.

Right, remember months ago when I was studying Blender and it turned out some of the scenes that were very elaborate were just textures on various planes? I am going to have to investigate that kind of 2.5d workflow. I'll leave that for later, it is not like I need to get into that in particular right now. I know more than enough Blender to know how to immitate such a style already.

12:40pm. I want to get better.

Forget great things, I just need to get good at painting what is in front of me. If I can copy what I see, that will form the foundation for everything else.

Learning 3d was a great exercise in learning how to break things down into their primitives. That is what I need to focus on if I want to get good at 2d.

In school I was not aware of how a painting can be gradually refined. But now I definitely understand that.

It might turn out to be that I've been supressing myself too much with my timidity towards just drawing on a canvas.

12:45pm. If I really can't do it and am one of those retards who can't move beyond the /beg/ stage, I'll go back to programming and get a job. If I can't do art, then I'll have to resolve myself to become a wage slave."

---
## [abmakes/100-days-of-code](https://github.com/abmakes/100-days-of-code)@[282f6fa32a...](https://github.com/abmakes/100-days-of-code/commit/282f6fa32a880d4ed1019dda37671508a2baf347)
#### Friday 2022-05-13 10:55:40 by Adriaan Boshoff

<h3>#day3 - Finalized blog, learned some new CSS</h3>

<p>Today I finalized the blog setup & workflow to make it easy and managable. It is not optimized or super user friendly, but this is just a minimum viable product so I can focus on the other projects I want to work on. I might make some changes down the line, but for now it will work. I learned some new CSS techniques that I will need for upcoming projects including modifying range sliders and dark/light mode. Added the light and dark mode to my blog depending on your browser color preference.</p>

<p>I also picked up this monster of a VScode modification, go to Preferences > Keyboard Shortcuts and add the Alt+W shortcut to quickly wrap text in a tag:</p>

<pre>{
"key": "alt+w",
"command": "editor.emmet.action.wrapWithAbbreviation",
"when": "editorHasSelection && editorTextFocus"
}</pre>

<p>An emmet widow will open and you can enter the tag abdreviation eg. make aselection of some text > press Alt+W > write "p" and press Enter. Text will be wrapped in a paragraph tag. BOOM! MAGIC :)</p>

---
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[2bb10e0679...](https://github.com/lyz-code/blue-book/commit/2bb10e06798382d922b2bf84e04d8b116669d5e7)
#### Friday 2022-05-13 10:59:32 by Lyz

feat(sql#List all tables): List all tables using different databases

Mysql:

```sql
show tables;
```

Postgresql:

```sql
\dt
```

Sqlite:

```sql
.tables
```

feat(jwt): Introduce JWT

[JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) (JSON Web Token) is
a proposed Internet standard for creating data with optional signature and/or
optional encryption whose payload holds JSON that asserts some number of claims.
The tokens are signed either using a private secret or a public/private key.

feat(fastapi#Add endpoints only on testing environment): Add endpoints only on testing environment

Sometimes you want to have some API endpoints to populate the database for end
to end testing the frontend. If your `app` config has the `environment`
attribute, you could try to do:

```python
app = FastAPI()

@lru_cache()
def get_config() -> Config:
    """Configure the program settings."""
    # no cover: the dependency are injected in the tests
    log.info("Loading the config")
    return Config()  # pragma: no cover

if get_config().environment == "testing":

    @app.get("/seed", status_code=201)
    def seed_data(
        repo: Repository = Depends(get_repo),
        empty: bool = True,
        num_articles: int = 3,
        num_sources: int = 2,
    ) -> None:
        """Add seed data for the end to end tests.

        Args:
            repo: Repository to store the data.
        """
        services.seed(
            repo=repo, empty=empty, num_articles=num_articles, num_sources=num_sources
        )
        repo.close()
```

But the injection of the dependencies is only done inside the functions, so
`get_config().environment` will always be the default value. I ended up doing
that check inside the endpoint, which is not ideal.

```python

@app.get("/seed", status_code=201)
def seed_data(
    config: Config = Depends(get_config),
    repo: Repository = Depends(get_repo),
    empty: bool = True,
    num_articles: int = 3,
    num_sources: int = 2,
) -> None:
    """Add seed data for the end to end tests.

    Args:
        repo: Repository to store the data.
    """
    if config.environment != "testing":
        repo.close()
        raise HTTPException(status_code=404)
    ...
```

feat(food_management): Introduce my food management workflow

As humans diet is an important factor in our health, we need to eat daily around
three times a day, as such, each week we need to invest time into managing how
to get food in front of us. Tasks like thinking what do you want to eat, buying
the ingredients and cooking them make use a non negligible amount of time. Also
something to keep in mind, is that eating is one of the great pleasures in our
lives, so doing it poorly is a waste. The last part of the equation is that to
eat good you either need time or money.

This article explores my thoughts and findings on how to optimize the use of
time, money and mental load in food management while keeping the desired level
of quality to enjoy each meal, being healthy and following the principles of
ecology and sustainability. I'm no expert at all on either of these topics. I'm
learning and making my mind while writing these lines.

feat(grocy_management): Introduce my grocy management workflow

Buying stuff is an unpleasant activity that drains your energy and
time, it's the main perpetrator of the broken capitalist system, but sadly we
have to yield to survive.

This article explores my thoughts and findings on how to optimize the use of
time, money and mental load in grocy management to have enough stuff stored to
live, while following the principles of ecology and sustainability. I'm no
expert at all on either of these topics. I'm learning and making my mind while
writing these lines.

[grocy](https://grocy.info/) is a web-based self-hosted groceries & household
management solution for your home.

It is really [easy to deploy](grocy_deploy.md) if you know how to use
[Docker](https://en.wikipedia.org/wiki/Docker_%28software%29). The hard part
comes when you do the initial load, as you have to add all the:

* User attributes.
* Product locations.
* Product groups.
* Quantity conversions.
* Products.

feat(kag): Introduce King Arthur Gold

[King Arthur Gold](https://kag2d.com/en/), also known as KAG, is a free Medieval
Build n'Kill Multiplayer Game with Destructible Environments.

Construct freeform forts as a medieval Builder, fight in sword duels as a Knight
or snipe with your bow as an Archer. KAG blends the cooperative aspects of Lost
Vikings, mashes them with the full destructibility of Worms and the visual style
and action of Metal Slug, brought to you by the creators of Soldat.

feat(python_vlc): Introduce python's vlc library

[Python VLC](https://wiki.videolan.org/Python_bindings/) is a library to control
`vlc` from python.

There is not usable online documentation, you'll have to go through the
`help(<component>)` inside the python console.

feat(libreelec): Introduce LibreElec

LibreElec is the lightweight distribution to run Kodi

feat(sqlite3#Get a list of the tables): Get a list of the tables

```python
sql_query = """SELECT name FROM sqlite_master
  WHERE type='table';"""
cursor = sqliteConnection.cursor()
cursor.execute(sql_query)
print(cursor.fetchall())
```

feat(sudokus): Introduce the sudoku game

[Sudoku](https://en.wikipedia.org/wiki/Sudoku) is a logic-based,
combinatorial number-placement puzzle. In classic Sudoku, the objective is to
fill a 9 × 9 grid with digits so that each column, each row, and each of the
nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or
"regions") contain all of the digits from 1 to 9. The puzzle setter provides
a partially completed grid, which for a well-posed puzzle has a single
solution.

---
## [mochibms/oraja_difficulty_table](https://github.com/mochibms/oraja_difficulty_table)@[d628ced1d3...](https://github.com/mochibms/oraja_difficulty_table/commit/d628ced1d3fa443df9c5406991d2b03411546f2e)
#### Friday 2022-05-13 13:38:25 by mochibms

20220513更新

新規

0
Castor(BMS edit) [DP HYPER]
Cong＊Chu＊Jelly [DP 202THER]
deep blue sunrise (Another)
Once in my life [DP ANOTHER]
Scorpion Dance [DP Another]

1
ネコノテ・カリタガール [DP 202THER]

2
endemize [DP 202THER]

3
ホーリーサンバランド [ダブルサンバランド]

4
Acacia [DP INSANE]
Sayonara Stardust [DP another]

5
恋愛シンドローム [sub Black Another]

6
Castor(BMS edit) [DP ANOTHER]
Kalte [Blossom]
Take The Long Way Home [Heartbeat]

7
Sayonara Stardust[DP insane]
エトワール・エトワール [DP Another]
ネコノテ・カリタガール [DP ANOTHER]

9
Canon (blazing summer mix) [DP-sagINSANE]
エトワール・エトワール [DP Insane]
呼無のカミサマ [Dim Prequel]

10
Castor(BMS edit) [DP twins]
Caffeine Overdose Girl [DP MIYATHER]
温泉大作戦 [DP_Li†]

11
Cong＊Chu＊Jelly [DP-soijoy]
Poison AND÷OR Affection [LOVE 100%]
Sweet Little Chocolate [DP-soijoy]
スペクトラム (DP Another+)
桜花爛漫の墓標 [DP R.I.P]
じゃぱりぱー [きみはダブルがとくいなフレンズなんだね！]
タマモッチ -ダイエット-
現実をカットアップしてみた [DPINSA.NE+]

12
Castor(BMS edit) [DP INSANE]
RE:START [DP-soijoy]

13
Beyond [Comprehension]
NightTheater [DPYoitherAdjust]
Pandora [DP hututher]

---
## [Sergei-Udris/Star-Lord](https://github.com/Sergei-Udris/Star-Lord)@[a25354eec7...](https://github.com/Sergei-Udris/Star-Lord/commit/a25354eec7b435b6f5a5771a75f5b8af1102dfb2)
#### Friday 2022-05-13 14:03:34 by Star-Lord

i import and browse with adminer aligulac db
:Andy-Sandler the audience is eating it up, Bill
:Bill-Hader fuck you
:Andy love you,dude
:Hader auooh

---
## [QASETRYHMKPW/Grasscutter](https://github.com/QASETRYHMKPW/Grasscutter)@[fbaeaee4b5...](https://github.com/QASETRYHMKPW/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Friday 2022-05-13 14:09:20 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [MChecaH/ManiaCheck](https://github.com/MChecaH/ManiaCheck)@[c997b01a6a...](https://github.com/MChecaH/ManiaCheck/commit/c997b01a6a06151f272beb698af363d14c4d2d89)
#### Friday 2022-05-13 15:28:26 by MChecaH

Added the already built .dll for 'CheckLongNoteLength'

I can see many people not wanting to go through the hassle of learning how the fuck you build the plugins soooooooooo yeah.

---
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[e8d1d96981...](https://github.com/lyz-code/blue-book/commit/e8d1d9698100defacdca34df1585ebe05c256b85)
#### Friday 2022-05-13 15:44:02 by Lyz

feat(anki): Introduce Anki

[Anki](https://apps.ankiweb.net/) is a program which makes remembering things
easy. Because it's a lot more efficient than traditional study methods, you can
either greatly decrease your time spent studying, or greatly increase the amount
you learn.

Anyone who needs to remember things in their daily life can benefit from Anki.
Since it is content-agnostic and supports images, audio, videos and scientific
markup (via LaTeX), the possibilities are endless.

feat(anki#Interacting with python): Interacting with python

Although there are some python libraries:

* [genanki](https://github.com/kerrickstaley/genanki)
* [py-anki](https://pypi.org/project/py-anki/)

I think the best way is to use [AnkiConnect](https://foosoft.net/projects/anki-connect/)

The installation process is similar to other Anki plugins and can be accomplished in three steps:

* Open the *Install Add-on* dialog by selecting *Tools | Add-ons | Get
    Add-ons...* in Anki.
* Input `2055492159` into the text box labeled *Code* and press the *OK* button to
    proceed.
* Restart Anki when prompted to do so in order to complete the installation of
    Anki-Connect.

Anki must be kept running in the background in order for other applications to
be able to use Anki-Connect. You can verify that Anki-Connect is running at any
time by accessing `localhost:8765` in your browser. If the server is running, you
will see the message Anki-Connect displayed in your browser window.

feat(pytest#Enforce serial execution of related tests): Enforce serial execution of related tests

Implement a `serial` fixture with a session-scoped file `lock` fixture using the
`filelock` package. You can add this to your `conftest.py`:

```python
import contextlib
import os

import filelock

@pytest.fixture(scope='session')
def lock(tmp_path_factory):
    base_temp = tmp_path_factory.getbasetemp()
    lock_file = base_temp.parent / 'serial.lock'
    yield filelock.FileLock(lock_file=str(lock_file))
    with contextlib.suppress(OSError):
        os.remove(path=lock_file)

@pytest.fixture()
def serial(lock):
    with lock.acquire(poll_intervall=0.1):
        yield
```

Then inject the `serial` fixture in any test that requires serial execution. All
tests that use the serial fixture are executed serially while any tests that do
not use the fixture are executed in parallel.

feat(gettext): Introduce gettext

[Gettext](https://docs.python.org/3/library/gettext.html) is the defacto
universal solution for [internationalization](python_internationalization.md)
(I18N) and localization (L10N), offering a set of tools that provides
a framework to help other packages produce multi-lingual messages. It gives an
opinionated way of how programs should be written to support translated message
strings and a directory and file naming organisation for the messages that need
to be translated.

feat(python_internationalization): Introduce Python Internationalization

To make your code accessible to more people, you may want to support more than
one language. It's not as easy as it looks as it's not enough to translate it
but also it must look and feel local. The answer is internationalization.

Internationalization (numeronymed as i18n) can be defined as the design process
that ensures a program can be adapted to various languages and regions without
requiring engineering changes to the source code.

Common internationalization tasks include:

* Facilitating compliance with Unicode.
* Minimizing the use of concatenated strings.
* Accommodating support for double-byte languages (e.g. Japanese) and
    right-to-left languages (for example, Hebrew).
* Avoiding hard-coded text.
* Designing for independence from cultural conventions (e. g., date and time
    displays), limiting language, and character sets.

Localization (l10n) refers to the adaptation of your program, once
internationalized, to the local language and cultural habits. In theory it looks
simple to implement. In practice though, it takes time and effort to provide the
best Internationalization and Localization experience for your global audience.

In Python, there is a specific bundled module for that and it’s called
[gettext](gettext.md), which consists of a public API and a set of tools that
help extract and generate message catalogs from the source code.

---
## [Pixel-Pro-Inc/QR-CashLess](https://github.com/Pixel-Pro-Inc/QR-CashLess)@[6a0820c04c...](https://github.com/Pixel-Pro-Inc/QR-CashLess/commit/6a0820c04c800b143e88a146a9c5dd36ef1c0ccb)
#### Friday 2022-05-13 16:29:09 by Abel3047

ExportToExcel logic and refactor

-Today was very painful.
-I had to try three different ways to perform task. At first I wanted to
intercept the ReportController before it gave its information to the
client, but that didn't make sense.
Then I tried to get the information from the service once it returned to
the client. But that didn't work either cause it didn't have consistent
vital data.
Finally I settled on only getting information from the detail sales
report. But remember none of the reports actually had any useful
information, just things only the view can use. So I had to extrapolate
and recreate information before sending it back to be exported.
-It the process of the torture, I refactored alot of logic in the
ReportsController and Export controller, and there is a new file that
bodies the extracted logic that is currently public to all. It has some
useful patterns but I want to make it an interface so that only
controllers can use it. But of course that is just something that will
come natural with the Clean architeture reform planned out.
-I also install a client depency that Yewo didn't inform me about. Its
the multi-dropdown ng module.
-BaseDto was created to help with the logic I was trying to create, but
I ended up not using it. You might have future use for it though.
-ExporttoExcel() method in the client was slightly changed to suit the
needs
-main was changed to remove references to the missing environment. I
think Yewo used the git rm command wrong and accidently deleted it
instead of untracking it. Please look into that if you make it  this far
in the commit message

 #Please enter the commit message for your changes. Lines startii

---
## [ENGO150/WHY2](https://github.com/ENGO150/WHY2)@[b098af3ebf...](https://github.com/ENGO150/WHY2/commit/b098af3ebf1e042bf4f30ec215a3dd41e5d72450)
#### Friday 2022-05-13 17:01:26 by ENGO150

separated build.sh into functions

uhm, yeah - the file was kinda shitty so..

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[622aeeeee5...](https://github.com/treckstar/yolo-octo-hipster/commit/622aeeeee56ddcfa47c35b9b989ec5126d094e91)
#### Friday 2022-05-13 17:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [m-falkowski1/linux](https://github.com/m-falkowski1/linux)@[213d266ebf...](https://github.com/m-falkowski1/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Friday 2022-05-13 18:00:33 by Linus Torvalds

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[af7d7d2bab...](https://github.com/mrakgr/The-Spiral-Language/commit/af7d7d2babc12857e6a30b725745378569205bb0)
#### Friday 2022-05-13 18:12:02 by Marko Grdinić

"1:45pm. I want to take a break. Let me watch Estab Life. I won't allow myself to become too stressed over art.

1:50pm. Focus me. Estab Life.

1:55pm. That prison illustration at 3:47 is sick!

2:50pm. Let me finally start. I could have started a lot earlier, but instead I felt like...letting the tension mount?

It really does not feel like I am getting enough sleep. I'll try goign to bed before 12am today.

Now let clear my head a little. It is time to put some lines down on the canvas.

2:55pm. I need to clear this hurdle. I am still beg level when it comes to just drawing. That couch illustration was the fanciest thing I did.

I still remember the lessons from Ctrl Alt Paint. I did a lot of studying last year. When it comes to 2d art, what I need isn't knowledge, but the willingness to carve my will into the canvas.

3:05pm. Let me try a square canvas, rather than the widescreen one.

3:10pm. Forget the objects in the room. I am actually having trouble drawing the general outline of the wall edges from within in. It is a bit like trying to draw a cube from the inside.

This would be the easiest thing in the world if I were doing 3d.

But as a 2d artist I should be at least capable of this much.

I just need to put down 9 lines on canvas so they make sense in perspective. Can I do that?

I should pracctice it until I get the hang of it.

3:35pm. I am just sitting here, thinking and staring at the room.

It is right in front of me, but I can't grasp its essence. Even minor head tilts greatly change the perspective. It renders what I have meaingless. So why don't I have Blender teach me. I can very easily model the overall shape of the room as a box with one of its edges chamfered.

In fact, I already did this months ago, but let me do it again. I'll go at it from scratch. Who wants to mess with brining in those props. What I need right now is the overall setup. I can do the minor details by hand after that.

3:40pm. I've gotten far too deep into pure 2d. I need to find the inner strength to practice the 3d to 2d workflow.

https://blender.stackexchange.com/questions/165532/turn-off-all-menus-for-a-screenshot
https://github.com/Yeetus3141/ImagePaste#readme

I'll get this addon later for easier copy pasting of image from Blender. Right now, let me check out the Clarisse scene again. No reason not to take advantage of that I've already done.

4:10pm. The scale tool in Clarisse it seems scales each object to their individual origin.

4:15pm. I figured out that I can just change it to manipulator, but Clarisse's navigation really sucks compared to Blender's.

Forget Clarisse. Forget it even exists. Blender at least has the walk mode using Shift + ~. That makes a huge difference when navigating in scenes such as these.

I've taken a look at the scene, and even though I spent so much effort on the texturing the walls back then, the actually proportions of it are messed up. I do in fact remember not caring too much about that.

4:25pm. Let me go to bed for a bit. I am going to restart the room scene in Blender. Instead of lazer focusing on doing the props to a high degree of fidelity, instead what I will focus on doing it as rough as possible while still remaining faithful to the overall perspective.

3d for 2d. I'll forget about the existing work until it is time to bring it in. I can basically only work on so many aspects of the scene. Do a prop and texture it, and now I'd need to manage files for every single model. Moving models around becomes hard if they have multiple pieces and so on. Booleans for example only really become a problem once you combine them with beveling. If I am flat shading, then there is no issue in using them.

So far I've pushed my 3d capabilities into various directions. But what I need to focus on is the rough use of it.

Using 3d for sketching should not imply that I can be sloopy. It just means that I'll skip various stages of what a full 3d artist would do.

It is a respectable skill on all its own.

If I can do this, I can get to 3/5 in art as a generalist.

4:30pm. Right now I do not feel like working on it. But I certainly don't feel like consuming fiction. So let me turn off the monitor and spend a few hours in bed until it is time to close.

It is good to brainstorm since I will be a doing a huge shift in my workflow.

It is not that trivial. I could grit my teeth and grind out the room in full 3d, but what would that get me? It is no good for me to take a month to do it. I need to be able to do a thing like this in a day or two or 3. The faster the better.

I can't spent a month doing what an average reader would spend a few seconds looking at.

6:10pm. I was in bed quite long. Let me do some clean up in Zbrush. I'll do what he did in the last tutorial I watched, except with slices instead of projection master. I want to get that out of the way.

6:40pm. https://youtu.be/0IIZwMR6_pA
Quick tip tutorial: Creating crisp edges using Polish by Groups in Pixologic ZBrush 4R6

It is giving me trouble. Let me watch this. I thought I would just do a slice and then deflate, but the edges are ugly. Extrusion leads to problems with intersection. I suppose I could lways reverse the problem and extrude in the opposite direction. But I want to take a straightforward approach first.

https://youtu.be/0IIZwMR6_pA?t=371

I see, so that is how poly by grups works. I wonder what the rest of the features do. They all use polygroups.

https://youtu.be/0IIZwMR6_pA?t=481

Will this actually work. I've never had Zremesher not mess up the borders.

http://docs.pixologic.com/user-guide/3d-modeling/hard-surface/polish-features/

Ah, I get it. Polish by Crisp Edges takes into account edge creases, Polish By Group takes into account polygroups and the Polish By Feature takes into account both. Simple enough.

7:15pm. I can never remember which is closed and which the open circle in Zbrush. The icons do not really correspond to closed and open, and this is just one of the aspect of Zbrush's interface hostility towards the user. Let me put it like this. Closed - inner highlighted, Open - outer hightlighted.

7:35pm. Done with lunch. I am deeply impressed how well Polish By Groups works. Also the reason why extrusion was acting up previously is because I was adding edge loops by accident. I thought I had set both vertex and edge actions in Zmodeler to Do Nothing, but it seems I did it wrong for one of them. I thought that those edges were random rendering artefacts insted. How silly of me.

Also now that I have the poly groups in the right places, using Keep Groups and smoothing them out really leads to the Zremesher doing an amazing job. But it is still just a sphere in the end. It is interesting that the freeze groups option would actually preserve the groups exactly as they are to the vertex. That could make the Zremesher more useful than the other quad remeshers.

7:40pm. It is impressive that Zbrush has Mara style support for projective painting, but I definitely won't be using that.

Using slices for the task here was definitely a better choice.

Now let me close Zbrush.

7:45pm. I've been doing some thinking in bed. In terms of various subdomains of 3d, I am already at 3/5 in various places. If I could finish this Zbrush course, I could consider myself 3/5 in general modeling.

As for 2d, even though I've gotten some insight into 2d, I really need 3d to take the place of sketching.

It is time to do it. Doing it roughly with 3d at first and then using 2d for the subtle detailing is what I should be doing. Aspects such as beveling and texturing should be left to 2d. Beveling is actually hard in 3d, but everything else is easy.

I've already went through various mastery challenges. The desk for box modeling, monitor for subdiv modeling, rig for NURBs modeling. That base mesh for sculpting. If I could do the Zbrush course that should be enough for me to break to 3/5 in modeling.

But that is not the mastery challenge I should be doing.

The real mastery challenge is what i could have done back in January. That is - use 3d for its sketching capabilities and then come in with the brush to do the edge work, the detailing and the subtle shading, as well as texturing.

2d would be way faster than 3d at that, while 3d is really far better for blocking out the initial shapes and setting the perspective. I could do some flat coloring in Blender.

7:55pm. When it comes to using 3d like that I should be more than ready.

I just have to do it. Breaking into 3/5 here is not a matter of knowledge. It is a matter of attitude. I need to dive in and establish the workflow that I will be using for Heaven's Key. I certainly never needed huge 3d skills to use Blender as a sketcher. Right now is as good time as any to do this. I can leave mastering Zbrush for later.

This is the mastery challenge I need to do. If I use my current workflow, no matter how good I get, I will never be fast enough to be a good illustrator.

Tomorrow, I am really going to focus on getting the proportions of the various aspects of the room right. Last time I was eager to get to the prop modeling and texturing parts, but in order to deal with the mastering challenge properly I really need to focus on getting the room exactly, if roughly, right.

Back then I did the room, the doorway and then did a bunch of boxes for the rest. This time I'll actually block out the beds in more detail.

Today when I opened the Clarrise project, I was really struck with how much space the desk was taking up. The whole room was too narrow and I never even noticed it.

I've skipped really important parts of the whole process. This time I'll redo it all properly, blocking in each of the props piece by piece.

8:10pm. Let me close here. Yeah, this is more my usual style during my programing days. I am going get the engine going or fall into slavery."

---
## [lemogne/pgmviewer](https://github.com/lemogne/pgmviewer)@[e764c96414...](https://github.com/lemogne/pgmviewer/commit/e764c96414ad665677fde93cfff7b02970ed2a51)
#### Friday 2022-05-13 19:59:33 by lemogne

Added ReadMe file (important!)

ReadMe (!) files are very (!) important (!) because without them, how could we read? Back in my day, there were no ReadMe (!) files, and no one could read, I had to walk to school uphill both ways and the winters were fifteen months long. So remember children, put ReadMe (!) files in all your projects or Satan shall rule the earth for a thousand years, you will get marked with the mark of the beast and be the Antichrist's personal slave.

---
## [daemon1995/era_gaming_mods](https://github.com/daemon1995/era_gaming_mods)@[6ab6d1ec55...](https://github.com/daemon1995/era_gaming_mods/commit/6ab6d1ec559048a115fc17ba3fd94b1d4978de2d)
#### Friday 2022-05-13 21:00:40 by Patrick Lin

Multiple improvments

GEM:
Improve the compatibility with Mithril Display. No more SN:Q

WS:

- Now Armageddon's Blade and Vial of Dragon Blood will not directly spawn on random maps (You can obtain via Utopia or any other objects with rewards)
- Cosmetic changes to Mithril. Everything in the game should be the same as the last commit by daemon_n

ES:
- Added additional creature support (function) for a few monster ability scripts. This useful for mods like TUM to add the third upgrade with the ability of the second upgrade
- Conflux Balancing now also affect
- Use modern trigger !?FU(OnCalculateTownIncome) for Peons and Economy for calculating town income
- Fixed Night Scouting not restoring the name of Rogue correctly
- Fixed a text error of Capture Mills with mithril upgrade activated

---
## [balt-is-you-and-shift/robot-is-chill](https://github.com/balt-is-you-and-shift/robot-is-chill)@[766df06d22...](https://github.com/balt-is-you-and-shift/robot-is-chill/commit/766df06d22c2f1ca6fb219f5bff072c239fa6aff)
#### Friday 2022-05-13 21:06:18 by Heptor44

oh my god im so fuckibg sorry

i had no idea these sprires were there im so sorry aaa

---
## [Forgind/msbuild](https://github.com/Forgind/msbuild)@[a572dc6b79...](https://github.com/Forgind/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Friday 2022-05-13 21:09:33 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [open-telemetry/opentelemetry-ruby](https://github.com/open-telemetry/opentelemetry-ruby)@[45429c7d53...](https://github.com/open-telemetry/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Friday 2022-05-13 21:27:08 by Andrew Hayworth

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
## [LZ1WS/Before_The_Dead_Slashers_Revamped](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped)@[149d38125c...](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped/commit/149d38125c955b9766211cbf46ecddb054aebeb9)
#### Friday 2022-05-13 22:31:41 by LZ1WS

Update

| Added |
- Boost of running speed after a hit from the killer (lasts 3 seconds, stamina is spent, an increase in speed of almost 2 times)
- Deerling ability Bloodrage (after a hit in Bloodrage: Bleeding (+blood puddles) every 2 seconds 6 times in a row, removes 5-10 damage, there are no sounds footsteps outside of blood rage)
- Description of Deerling
- Voice lines of Specimen 8, Tirsiak
- Blood puddles after death

| Changed |
- Buffed the Metalworker, now he can lock the screen of the last camera on the HUD
- The text "Click to show model" in F4 has been slightly changed

| Fixed |
- Minor fixes to the old code
- Fixing bugs related to the abilities of some killers and bots
- Added a description of the Impostor and Springtrap at the beginning of the round and to the F4 menu (Sorry for inconvinience it may caused with their abilities description)
- Playback of voice lines
- Gamemode breaking bug

---
## [Mohammad-Vahed/TRidership](https://github.com/Mohammad-Vahed/TRidership)@[d8eaa10dc3...](https://github.com/Mohammad-Vahed/TRidership/commit/d8eaa10dc373bcd219f984d3b62c506ce343a6ec)
#### Friday 2022-05-13 22:43:28 by Mohammad-Vahed

LICENSE

                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.

---
## [PiperDoots/Shiptest](https://github.com/PiperDoots/Shiptest)@[031c0866ed...](https://github.com/PiperDoots/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Friday 2022-05-13 22:47:02 by SweetBlueSylveon

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
## [tedmiddleton/mainframe](https://github.com/tedmiddleton/mainframe)@[84927e3557...](https://github.com/tedmiddleton/mainframe/commit/84927e3557972577611d3c5f7c1265a9ef8d0aa9)
#### Friday 2022-05-13 22:50:48 by Ted Middleton

CSV parsing, and frame::row_type

frame is a bit analogous to tuple (and is in fact implemented as
containing a tuple) in that each column is a unique type and iterating
through the columns isn't really supported because the columns have
different types. I think that in general this is the right choice if
we're comparing it to the idea of type erasure, but it does make dealing
with rows complicated and clumsy. In the meantime, we have a frame_row,
but it's kind of an iterator illusion - it's actually just a container
of iterators pointing to the series_vector's inside the frame.

When actually dealing with a parser like the csv loader, it's painful to
deal with an indeterminate number of rows. We're already limited
somewhat by the type of frame - we need to know ahead of time when
parsing the csv how many columns it has, and then return that many
columns regardless of what was actually in the csv. That can sort of be
mitigated by returning an oversized frame<mi<string>...> and then just
culling columns that are all missing, but in the parse itself, it's
annoying to have to deal with the indeterminate number of columns. For
the time being, frame_row is now frame_iterator_row and I'm introducing
frame::row_type, which is actually a vector of variants of all the
column types in the frame. I don't quite know whether this is the right
approach, though.

Right now, it has a series problem - if we have

using frame_type = frame<double, mi<bool>>;
frame_type f1;
frame_type::row_type row;
row.push_back( 1.0 );
row.push_back( true );
f1.push_back( row );

...believe it or not, row.push_back( true ) actually ends up adding a
double to the row, not an mi<bool>. C++ doesn't like
transitive-type inferencing - in the case of row.push_back( true ), it
needs to infer that this is bool -> mi<bool> -> variant<mi<bool>> and
instead prefers bool -(cast)-> double->variant<double>.

Can this be fixed? In the case of all mi<string>'s like the csv parser,
this is completely harmless because all the column types are the same.
In the case of heterogenous frame columns, it means in the documentation
I'll have to make it very clear that you need to specify row.push_back(
mi(true) ) rather than just row.push_back( true ).

All of this is a bit unergonomic. I'm still not quite sure how to handle
this. I'm now reconsidering maybe making uframe a bit more capable and
exposing that as a front-line type.

TODO:
- Finish CSV parser, handling special cases. parse_line() state machine
  needs to be refined a bit for escape sequences (or what passes for
  escape sequences in CSV. Also, utf8. utf8 is completely unhandled.
  Completely. There needs to be a utf8 scanner inserted into
  parse_line().

- SIMD-optimized correlations. One complication here is that SIMD
  support with msvc is slightly different than on g++, wrt compile-time
  vs run-time support.

- Join functions - frame::innerjoin, frame::outerjoin, frame::leftjoin.

- frame::groupby(). I'm still not 100% sure how to do this, but I think
  the key will be to create a new class type, like

  template< size_t ... indexes, typename ... Ts > grouped_frame;

  This would be returned by frame::groupby() and would include the same
  columns tuple that frame does (our usual non-mutating return-a-frame
  operation), but also maybe a multimap or unordered_multimap that
  indexes into the rows.

  I'm not sure how much frame functionality grouped_frame should take
  with it - also, should index values be exact or should grouping allow
  for ... groups?

- Add a function call wrapper for function calls in expressions

  auto f2 = f1.new_column<double>( "ceil", _f( std::ceil, _0 ) );

- Multiprocessing locks and guards. I still need to think about this a
  bit harder. Would it be enough to just say that frame and series
  objects should never be shared by reference and instead should be
  "copied" between threads?

---
## [VizierDB/vizier-scala](https://github.com/VizierDB/vizier-scala)@[225858557a...](https://github.com/VizierDB/vizier-scala/commit/225858557a963664ffe800c8eb151d0ad7e15fe8)
#### Friday 2022-05-13 23:17:21 by Oliver

WIP: Attacking ORM hell (re #182)

I think I've found most of the performance lags in GetWorkflow.  It looks
like we're down to ~0.1s (although it's on different hardware).

- Module.describe no longer does any database lookups.  Instead, the caller
  is expected to provide nearly all values that would normally get pulled
  out of the database.  For bulk lookups like Workflow.describe, these values
  can be retrieved for the entire database in a single lookup (and are then
  joined back with the workflow client-side.  This makes a handful of operations
  more complicated, but utility methods on cell can be used to provide nearly
  all of the arguments.
- Modules.describeAll no longer serves a meaningful purpose and has been
  merged back into Workflow.

One big potential performance win remains: Looking up table artifact schemas,
since currently ArtifactSummary.summarize requires a full artifact materialization
otherwise (the materialization itself isn't a pain, but the repeated SQL queries are).
I'm wondering whether it might not be a bad idea to just outright drop the
ArtifactSummary object.  We try to avoid making the SQLite file too big anyway by
putting large blobs in the artifact-associated file, so there's not really going
to be **that** much of a performance penalty at this point to just load the data field
when needed.

Related to this, it might be useful to cache schema information as part of the
Dataset object when it is first created.  We nearly always have the dataframe available
at this point (if not its contents).

---
## [Offroaders123/Dark-Mode](https://github.com/Offroaders123/Dark-Mode)@[be9e7fd718...](https://github.com/Offroaders123/Dark-Mode/commit/be9e7fd718134ddfbade743207ab272622e5c9d7)
#### Friday 2022-05-13 23:39:36 by Offroaders123

HUD Item Text Fix!

Fixes:
- Finally got around to addressing the HUD item text issue. It wasn't showing up at all before, because my custom UI code had aged against the more-recent releases of the game, so it prevented the HUD item text from showing up at all (very annoying). Sorry it took so long!

Changes:
- I recently discovered a great site that has all of the documentation about everything Minecraft Bedrock! It's at https://wiki.bedrock.dev, and it's super thorough.
- Thanks to their documentation about the Bedrock UI stack, I learned that there's actually a way to use inheritance with the Bedrock UI code, and it's great! Most of the time, keys are nested using objects, which means you have to replicate that same structure to get into inner elements, to modify their properties. This becomes an issue when you want to change only one thing, as you have to include everything else along with that one change, else the default definitions be lost because you "removed" them, per se. Turns out, you actually can access those inner objects using slashes in the element keys, where there would usually be nested object, after object. Essentially, it allows you to modify inner objects without writing out all of their parent's info, which is what the initial problem was! I've wanted a feature like this for such a long time, and I just had no idea it existed, haha!
https://wiki.bedrock.dev/json-ui/json-ui-intro.html#conditional-rendering

---

