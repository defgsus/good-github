## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-18](docs/good-messages/2022/2022-08-18.md)


1,943,383 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,943,383 were push events containing 2,988,609 commit messages that amount to 213,739,942 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[94e9a1e871...](https://github.com/treckstar/yolo-octo-hipster/commit/94e9a1e8710234d86eeb64cfd116e87bc6ecdfc0)
#### Thursday 2022-08-18 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [aCrockofSchmidt/100-Days-of-Code-Python](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python)@[96a4a2cb5e...](https://github.com/aCrockofSchmidt/100-Days-of-Code-Python/commit/96a4a2cb5e00ceb3da75066506c09c5991ec8df3)
#### Thursday 2022-08-18 02:00:59 by aCrockofSchmidt

initial commit

Oh, boy, was this another awful experience.  The challenge itself isn't all that difficult. Or it wasn't in the end. But the documentation for spotipy and spotify (the former especially) was bloody awful. There is absolutely NO WAY you could come up with a solution by reading through the pertinent documentation from the tools used. Utter garbage as a lesson. Ultimately, the guts of the code was just copy pasted from other sources, students, instructor's solution.

I fail to see what that accomplished. It irritates me to no end that solutions are impossible to derive with the very documentation required to do such a task. One should not have to pilfer other's work online to make a simple piece of code buildable.  Not impressed.

I was able to do the scrape myself.  That's good at least.  The spotipy stuff I needed plenty of help but did do some bits myself once I had some guidance on WTF was going on.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[4c8cfb57aa...](https://github.com/pytorch/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Thursday 2022-08-18 02:33:49 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [cadyn/CHOMPStation2](https://github.com/cadyn/CHOMPStation2)@[8e8232c0d8...](https://github.com/cadyn/CHOMPStation2/commit/8e8232c0d826dc3341d20a7861c1d86859e06ef7)
#### Thursday 2022-08-18 04:33:51 by Rykka

Ports Taur Loafing from Cit-RP

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

For real tho laying-on-side sprites would be nice to visually represent a taur collapsed on their side, rather than faceplanting bc humancode.

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

---
## [jzj/pulumi-hugo](https://github.com/jzj/pulumi-hugo)@[57060a7a96...](https://github.com/jzj/pulumi-hugo/commit/57060a7a96837ce68cf5593c2b37a8daf488a01a)
#### Thursday 2022-08-18 04:39:46 by Joe Duffy

Improve download discoverability (#1811)

* Improve download discoverability

We know users have trouble simply downloading Pulumi. This used to be
very easy, but over time, as we optimized the Getting Started flows, it
got pushed further and further away from the core user experience.

I don't know about you, but the first thing I care about when I'm
trying out a new open source tool is downloading it!

This change aims to do two things:

1. Make downloading a more prominent CTA.

2. Improve the download page so it's less noisy and more focused.

This entails:

* Adding a DOWNLOAD secondary CTA on the homepage.

* Summarizing the recommended download options at the top of the
  download page, very clearly, and without any preamble. This
  hopefully tells you instantly what you wanted for the 80% case.

* I exerted some artistic freedom which I'd love feedback on. The
  recommended options were our Official Brew Tap for macOS, curl
  command for Linux, and MSI Installer for Windows. Peers to those
  are simple download links for the binaries, as that's the simplest
  possible thing, which today is actually the hardest thing to find.
  Notably for Windows, I thought of using Chocolatey or Winget, but
  I don't perceive that either is "the default" for Windows users.
  Winget is the future but it isn't supported pre-Win11, which I have
  to assume most users aren't on yet. MSI has been around since the
  dinosaurs, so it seems like the safest choice to promote.

* Moving the list of download options for each operating system
  underneath a collapsable accordion list, which is collapsed by
  default, and clearly labeling it as "Other"; as in, if the heading
  didn't work for you, here are some other options.

* A few other wordsmithing tweaks to make the page a little more
  streamlined and to flow better.

This is absolutely NOT the final destination for any of this,
however, I am hopeful it will be a simple incremental improvement
that moves the needle on key metrics. We'll watch it in the weeks
to come and course correct as needed -- as well as continuing to
think about ways we can improve all of this overall!

One note: This depends on a new secondary hero button style that
isn't yet merged in the upstream Hugo component library. Assuming
I did that correctly (a big if!) I'll need to rev the go.mod file
after it merges. See: https://github.com/pulumi/theme/pull/159.

* Apply suggestions from code review

Co-authored-by: susan evans <susan.ra.evans@gmail.com>

* Fix up some styling

* Update themes/default/layouts/index.html

Co-authored-by: susan evans <susan.ra.evans@gmail.com>

* Use new theme/style

Co-authored-by: susan evans <susan.ra.evans@gmail.com>
Co-authored-by: zchase <zachary@pulumi.com>

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[e0dc271cbe...](https://github.com/Bcadren/crawl/commit/e0dc271cbe7e527d67a5da280aaff66915ae78f3)
#### Thursday 2022-08-18 04:40:47 by Lucien

Fix some attack-related bugs. If a monster's attack base damage is 0, it always does 0 damage instead of sometimes doing a small amount. Monsters will no longer block or dodge an allied Staff of Life tap (they shouldn't anyways and when they did it caused them to not know it was a friendly tap and go hostile). Add a bit more complicated 'AI' in fight to guess what a life-wielding player with a melee weapon in the other hand would want to do. "Attacks" with only the life staff on allies, attacks with only the weapon on enemies, unless you're with Ely, in which case it bonks with both to attempt the pacify (and stops attacking midway through on pacify). It's not necessarily the best solution (we GUESS what the player wants afterall), but I'm not sure how to actually ask in this one special case without making it an interface screw.

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[a7a0e33192...](https://github.com/Koshenko/mojave-sun-13/commit/a7a0e33192ad3fcac5ad64d441f24af6ec852054)
#### Thursday 2022-08-18 05:18:18 by Hekzder

Mob overhaul for DT (#2117)

* Basic mobs

Title

* Start of simple robots

Title

* THE GREAT MOB SOUNDENING

TITLE

* Handies + ranged attack buffs

FASTER!!

* Protectrons, robobrains

* Death sounds and fixes some dumb shit

Title

* NEW ROACHES OMG!!!

WOW!

* Robo sounds

Title

* Mob projectile tweaks

I THINK WE'RE GOOD

* bitty

---
## [AOSC-Dev/aosc-os-abbs](https://github.com/AOSC-Dev/aosc-os-abbs)@[dd66e64602...](https://github.com/AOSC-Dev/aosc-os-abbs/commit/dd66e64602da0dcd1fca02609614e8ddbaeee662)
#### Thursday 2022-08-18 06:08:38 by Mingcong Bai

gnome-flashback: update to 3.44.0

Use gnome-bluetooth-3.34 (1.0 API), because fuck you.

---
## [matrix-org/mjolnir](https://github.com/matrix-org/mjolnir)@[b9284f0167...](https://github.com/matrix-org/mjolnir/commit/b9284f0167a9e9428db6217ec5ede527649a4948)
#### Thursday 2022-08-18 08:05:47 by gnuxie

Reduce the throttle test theshold even more.

The implementation is rubbish, as it doesn't avoid the exponential backoff

Remove default rate limit testing.

It doesn't work. No there really isn't more to say about it
you're welcome to dispute it if you're going to do the work investigating. I'm not.

We used to have a test here that tested whether Mjolnir was going to carry out a redact order the default limits in a reasonable time scale.
Now I think that's never going to happen without writing a new algorithm for respecting rate limiting.
Which is not something there is time for.

https://github.com/matrix-org/synapse/pull/13018

Synapse rate limits were broken and very permitting so that's why the current hack worked so well.
Now it is not broken, so our rate limit handling is.

https://github.com/matrix-org/mjolnir/commit/b850e4554c6cbc9456e23ab1a92ede547d044241

Honestly I don't think we can expect anyone to be able to use Mjolnir under default rate limits.

well, it's not quite simple as broken, but it is broken. With the default level in synapse (which is what matrix.org uses) it is struggling to redact 15 messages within 5 minutes. that means 5 messages over the burst count. This is ofc ontop mjolnir sending reactions / responding to replies (which isn't much but... enough to mess with the rate limiter since ofc, Synapse tells requests to wait x amount of time before trying again, but that doesn't help for concurrent requests since ofc there's only 1 slot available at that future time.  This means Synapse just wacks everything with exponentially longer shit without many (or any?) events going through
it used to be fine
because rate limiting in synapse used to be a lot more liberal because it was "broken" or something, that's not me saying it's broken that's just what synapse devs say which is probably true.
if all requests went into a queue then yeah you could eliminate one problem
but that's a lot of work and i don't think we should be doing it
cos no one uses mjolnir like this anyways

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[286d7e6d2e...](https://github.com/treckstar/yolo-octo-hipster/commit/286d7e6d2ed488194840aec8a338650e3cea2cc7)
#### Thursday 2022-08-18 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [danielronalds-school/Website-Assignment](https://github.com/danielronalds-school/Website-Assignment)@[b54422a371...](https://github.com/danielronalds-school/Website-Assignment/commit/b54422a37120c3218a53e01bcdf04a38a2805e3a)
#### Thursday 2022-08-18 10:24:44 by danielronalds

Holy shit it was a journey. Implemented adding climbs to the database via the admin table. Had to create a new id column in the climbs database as the old one had a 'varchar' type that couldn't autoincrement nor be assigned as null as it wasn't an integar. As a result my code that was attempting to insert the climb id as null and let the database assign it an id was causing an error as you cannot set a varchar to null when inserting into a table. To solve this I had to remove the primary key from the id column, rename it to old_id, then create a new column with a type of int(255) setting it to A.I. and then as primary key. Finally I deleted the old_id column, and my code worked. I'd never noticed that when I imported this database into myphp from excell two years ago it had set id to type varchar as it never affected anything I did. I hate php. So. Much. Use rust, there's no f**king around with null types in rust.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d195b7de01...](https://github.com/mrakgr/The-Spiral-Language/commit/d195b7de018669fb6a2b5db1d6de248eb31a4d7f)
#### Thursday 2022-08-18 11:07:30 by Marko Grdinić

"9:10am. Let me chill a bit and I will start. Any mail? Nothing. Is this going to be some kind of curse where I am waiting forever to get out of the mailing list?

...

Ah shit, it was approved 28h ago! I thought I would get an email, but I just got a notification in my RR acount!

https://www.royalroad.com/fiction/57747/simulacrum-heavens-key

Here it is.

I immediatelly feel more motivated. Some guy commented this has a lot of potential, so I should deliver on his expectations.

9:20am. Forget the vamp loli thread from yesterday. Let me do some writing. I really should be posting the rest of the chapters to RR, but a delay of a day or two won't kill me. Let me spend my creative budget for the day. Ok...

I had some time to think about it. Let me get rid of the poem. It doesn't really fit.

$$$

    Through a desert a traveler walks
    Even as his blood boils into vapor
    As his flesh decays and rots
    As his bones crumble into dust
    He continues moving

    As his body dies, he leaves the unneeded behind
    And continues moving forward

    His soul blazing, he traces out heavy steps
    Seeking his goal

    Far above
    The Herald of the 3 Gods' voice resounds:
    Break the Limits! Ignite the Singularity! Pursue Omnipotence!

    - Intro to Heaven's Key

(Euclid's Room)

The way it happened made me shiver. It felt like the grim reaper's skeletal hand combed its way through my spine. I had been killed, but the last thing that flashed through my mind was Lily's smile as I handed her the chips. Right now I can feel her happiness and kindness haunting me. I feel a momentary rage. That bitch.

She literally killed me by being kind, happy and helpful towards me.

Feeling like getting back into the game and pummeling her, I stop and rethink it.

No, wait. She wasn't the only one. If the death condition is the chip balance dropping to zero then....

I remember the day I spent with Lily. She wasn't the only one there. I remember that kindly old man who handed me my skewer only for 10 chips. I remember the pleasant atmosphere, and all the happy looking people at the amusement park. I remember the prices on the restaurant menu. I remember the job ads. I remember how the group I played poker against was betting only a single chip per tourney, but suddenly raised the stakes when they realized I was a mark. It wasn't just her, everything in the environment itself served to make her lie convincing. They were all in on it.

I thought I was some kind of renegade, beyond others, but...but, I was killed by the NPCs in the lamest way possible. I had fallen into a trap as soon as I paid my first order in the restaurant. At that point, I was inevitably going to be coaxed into spending more of my life. The smiles and the pleasant people came back to haunt me. Their smiles felt like scythes.

Outside my room, the night had already come. I lie on the bed for some time, just thinking.

A wave of fear washes over me. Now that I understand what the trap is, for the first time I wonder, how, just how could I have avoided this? It is easy for me to reload, but had I been there for real, without the benefit of being a player in a game, just how could I have avoided being scammed out of my life? Wouldn't I have certainly died?

I feel anger coming over me again.

Unacceptable. This is simply unacceptable!

[Externus gain 0.3]

I am not going to trust the NPCs again. I will modify my mind to get rid of the weaker aspects of my personality if necessary!

I do not know whether it was in response to my thought or due to the right amount of time elapsing in the death state, but as soon as I think that inside the game, I see the scenery shift from pure darkness to windy, dusty one. Like when I logged into Simulacrum for the first time, I saw a rhymeless poem accompanied by an illustration. In the image I see a transparent ghost of a man resolutely walking forward through the dusty desert, leaving a trail of footsteps behind him in the sand. As the camera panned to show the scene from above, I could see a corpse along the trail facing downwards. It was directly on the trail and there weren't two sets of footsteps as one would expect. The implication of what had happened is clear - the man died and yet continued moving onward as a ghost.

I dwell on the scene for a while and begin to see the analogy with my own situation.

Lily killed me, but it is not like I am going to put a bullet through my head to honor their achievement in reality. The opposite. I am going to go after them.

I am going to scam Lily. She still thinks I am a mark. If I lean on her...

[Gnosis check 1.6 Succeeded - Sampled 2.54]

I remember the looks the guys at the table were giving her, and get a flash of inspiration. They did collectively lose two whole human lives to me, no way they will just shrug that off. All of them are in on the scam, so maybe there is some truth about Lily being employed by the government to skin the sheep. If I threaten to toss myself over the railing, they'd take a loss, so they will do whatever they can to keep me here. They think they hold all the initiative, so that should give them confidence to give me some leeway in order to keep the scam running.

They can't possibly imagine that the entire universe they are in exists solely for me.

Using my saveloading ability, I will destroy them.

With that thought, I spend some time scheming in bed, and realize just how late it really is. It is past midnight. I'll skip dinner today. Tomorrow I have to get up for school. It is Friday, so I should have more free time after that over the weekend.

I think about figuring out how to speed up my mental processing so I can get more game time in, but realize it is too late for that. I understand that the human brain uses sleep for all sorts of reasons and that I do not need most of that on a brain core. But right now, even if it is fake, my fatigue certainly feels real. I'd really be fighting to stay away long enough to eliminate my tiredness. I could use the emotion control app, but it recommends not using it to eliminate the need for sleep otherwise I will start experiencing hallucinations and madness eventually.

I should sleep, so let me do that. Rather than try to get myself to a still state manually, I use the mind control program to do it. After that the slumber comes over me.

(At school)

I ignore the classes to do some actual studying. I do not want to immerse myself into games during class of course, but I mentioned yesterday about wanting to speed up my mental processing. Rather than waste good time during the day, I should do this work during class time.

"Blah blah blah blah...."

I am paraphrasing the teacher, this is how he sounds to me right now as I sit in front. I couldn't care less about school and don't care about caring. Once I've upgraded my memory, I'll commit all this stuff to it. So I spend the school time wisely, browsing the mind improvement guides online. Once I am back home in a safe place, I'll experiment with it for the first time.

(Euclid's Room)

I am back, and it is time to start. I toss away the book bag and lie on the bed, calling up the Helix Studio program. I make sure that I have administrative access to the brain core itself as well as control over my body and once I do that, I create a copy of my mind. I could activate it now, but if I did that my fork would not have any senses. Subjectively, it would be like all the sensations being cut off. Since I do want to play a cruel joke on what is basically me, using Helix Studio, I create a virtual space.

In the limbo browser, I have various options to choose from. Restaurants in a city, luxury apartment rooms and hotel suites, suburban houses, private jets, to more exotic picks like moon bases and undersea bases. A luxury cruise room catches my eye and I pick it. I ignore the settings and just log into it.

(Helix Studio, Regent Suite)

I find myself standing in the middle of a luxury suite living room. It is quite spacious, much larger than my own room. I glance at the furniture, and note that the tables and the chairs all seem to be designer products. There is a bar, and even a piano there. There are glass panes throughout and the light of the sun is streaming into the room from them. Outside I can see the seas. Coming closer, I see waves slowly rippling across the sea. Stepping outside to the balcony I can hear the waves and feel the wind, but nothing else. My room is just a small part of the enormous luxury cruise, but other than me, there is nobody here. It is a bit eerie, but otherwise is what I would have expected.

The function of this minor world is to just have a place to ease in new instances.

I go back into the room, and relax on the couch. Then in my mind, I bring up the Helix menus, and after doing the necessary setup like the avatar and location for my copy, activate him.

A person who looks just like me manifests a few feet away, facing sideways away from me. My bad, I didn't bother setting the orientation.

"Huh?" Confused, he starts looking around. From his perspective, the last thing he did was press Ok to copy himself. And right now he finds himself in a weird place. Taking in the sights, his eyes finally landed on me. I nock my head to the side slightly, and grin.

"Yo!" A jolt of surprise goes through him and he even does an involuntary jump. The reaction is a bit funny, I've never had anyone respond that way to me. Gears quickly turning in his head, he realizes what is going on.

"Damn! Does this mean I am the copy I made?"

"Yes." Not beating around the bush, I give it to him straight.

"That's..." He trails of for a bit, and I give him time to digest the situation. "This is pretty magical. The last thing I wanted was to make a copy so I could experiment on it, but then I found myself being that copy. It is unbelievable. It is like my desire transported me into that copy. I wanted to edit the copy and now I am the copy."

"So how do you feel?" I greased the conversation.

He does a little self check up, feeling up his face and body.

"Fine." He walks around. "Lovely place that you picked. Is it some kind of apartment suite by the sea..." He walks to one of the oversized windows, and realizes where we are. "It's a cruise ship. Yeah, I like it."

"There is nobody here, but us right now." I remarked.

"Yes, I remember the docs saying as much." Having his fill of the sights, he takes a seat opposite to me and relaxes. I take a breath and begin.

"Since you are me, I do not have to explain why we are here." To increase his processing speed and get him acclimated to it. I do not want to do that personally because it could mess me up in real life. And I would not want to do it without anybody supervising me for safety reasons. What better to supervise me than my own copy? Hence, this situation.

"Yeah. The plan is to start off slowly and make the necessary adaptations so that I can naturally think at 1,000,000 fold speeds." Just increasing the processing speed at which his mind is running would be very easy, I just need to tweak a setting. But thinking a million times faster, means that subjectively a million seconds would need to pass for him for a single one in the real world. A million seconds is 11.5 days. Imagine trying to do anything at such a pace as a human. It would be nothing more than torture.

Although I have the mind controlling program to help regulate the boredom, it is a simple fact that the brain was not designed for this kind of strain. According to the guide, for humans the memories would get bleached and erased, if one tried to force living in such a manner. Unless proper reprogramming is done, it would not work. Take recognizing speech for instance. Remembering what was said a few words ago, once processing speed was ramped up, might be a few months in subjective time. Having the proper attitude and keeping control of your emotions, does not mean you'll have the memory required to tackle the challenge.

External control of emotions has its use, but after a certain point the mind simply needs to work properly to begin with rather than be pushed in the right direction by external aids.

"How about we start with 1.5?" I have admin access to his mind, so I bring up the tool that would allow me to tweak his settings. Increasing the processing speed is a simple matter in the emulator. I find the setting quickly. "I have it. Are you ready?"

"Yes." I change the setting and confirm.

"Done. How do you feel?"

"Your voice is so slow!" He blasts out the sentence at me. After that he makes some jerky movements. He looks around and his head is snapping so fast from side to side that he looks to be in a panic. He waves his arms out as if feeling it out, and then gets up from his seat, fast walking around the room. He does a jump. Nodding to himself, he power walks back to his seats and plops himself back.

"Interesting! Very interesting!" He rushes his words. "Slow me down!"

I do as he requests.

"Done."

"It feels like being inside water. It is like the world is more solid and I have to push to make the same kind of progress. It is not pleasant." He shrugs. "I have to remind myself to slow down if I want to keep my regular pace. It is quite hard." His mind became fast, but his body and the world remained the same.

"I guess we'll have to learn to walk and talk from scratch if we want to take advantage of this."

"I am not sure I'd be able to handle speeds of 10x. Something like 2x would already be my limit." Introspecting, he gave his opinion.

Hmmm, not good. I can't really use this to get better at sports just like that. I suppose it would be possible once I get used to it. But no, forget that line of reasoning. I guess even with the enormous processing ability of the brain core, the only thing it gives me is the ability to work rather than direct power. It will be up to me to take advantage of it.

"Oh well. You'll be the one we'll be experimenting on, so I won't tell you to enter the self improvement loop right away. What do you want to do now?"

"I think I'll do some gaming. Since I no longer have a body in the real world, that is the only thing I can do now. I'll speed myself up 10,000x times and speed up the game by the same amount and get some game time in that way." I remember that 10,000x seconds is almost 3 hours. A minute at that speed would be a week. So in 4 minutes, he could spend an entire month in the game.

"At 10,000 speed, 4m for me would be a month for you. I can wait a bit for you to get into it." On mental command, I bring up the core's clock, and note it saying 3:15pm. "You've got access rights to your own mind, and I've allocated 10% of the core just for your own needs. Check it out." Given the core's capacity, this was still an enormous amount. Converting that into actual intelligence is not something that would be done soon.

"Yeah, I see it." He took a moment to confirm.

"If you need anything, since we are literally on the same brain, just send me a text message."

"Ok. I guess I'll get started with the game. See you around?" He wondered.

"Go get them." I encourage him. "As for me, I guess I'll do our homework. I'll come back in half an hour. I'll send you a message once I am here. Bye."

"Bye." I log out, leaving my copy alone in the character limbo.

---

The admin me logs out, and I am now alone in the suite. I go to my own settings, increase my processing speed by 10,000x and after that, do the same for the simulation. I note the real world time which is 3:18pm. I write it down in a file on my personal desktop. Even at 10k speed, I realize the core's programs are still snappy. I am sure if it was my desktop rig, it would have slowed to a crawl subjectively. It just goes to show that the programs on the core were made for people who think really, really fast, so the programs themselves need to match that. I am sure that if I tried browsing the internet right now, it would be unbearably slow.

I let myself deflate a little and lounge of the sofa, feeling its grungy texture. I have plenty of time to think and get started. A week here would be a minute in the real world.

Sigh. I've lost quite a bit. I no longer have my own body in the real world, and I can't just ask the admin me to give it to me. Unless I can get another body, I’ll be stuck on the core forever. I am not really the Euclid the others know. But that is fine.

I toss the pillow that I am playing with aside, and get up. It is time for payback. I'll see how far I can go just saveloading, and after I reach a dead end with that, only then start reprogramming my mind to give myself actual superpowers.

$$$

I do not think I can remove it after all. I changed some sentences later so it is less tacked on. I thought yesterday I should maybe leave it for a later chapter, but let me leave it like so for now.

9:50am. I won't aim to do too much today. Let me do for as long as I feel like it and then I will first figure out how to put illustrations into the chapters.

10am. I am thinking about some future plot points, but no, it would not work. The way the Bayesian conditioning works does not allow interaction between threads. The Inspired have to find their path solo. I can't have NPCs who have dropped out be talked back into it and the thread arighting itself. It is not how divine justice works.

10:15am. https://www.sixstarcruises.co.uk/advice/5-stunning-cruise-ship-suites/

Right now I am thinking what to make the limbo. In the old arcs I think I used apartments, so this time I am going to go with a luxury cruise room.

10:30am. https://nautil.us/another-path-to-intelligence-23113/

Now I find myself reading this. Let me read it for a bit and then I will get to the luxury cruise.

10:40am. Focus me. Just do it.

12:40pm. I wrote a decent amount. Let me put it into Docs.

1pm. I really have the hang of it now. Writing is simple. I just have to come up with a setting and then run it forward. That is the fundamental of writing. Just like how in programming I have to come up with a model and then implement it. It is really the same thing, just in different contexts. I have the right brain for it.

Maybe I can't draw, but I sure can do this.

1:05pm. Let me have breakfast here. I'll stop writing here for the day so I can publish what I've already written. I'll also figure out how to include the illustrations while I am at it."

---
## [Big-Smarty/3d_renderer](https://github.com/Big-Smarty/3d_renderer)@[e9e5ca686f...](https://github.com/Big-Smarty/3d_renderer/commit/e9e5ca686fa53a6fb41fcfe891f7fff13b127de5)
#### Thursday 2022-08-18 12:05:42 by Big-Smarty

removed unnecessary amount of libraries, now its all one big library. improved pipeline wrapper. removed some forward declarations as they are honestly not that useful (definitely didnt waste a shit ton of
time on that)

---
## [tremor-rs/tremor-runtime](https://github.com/tremor-rs/tremor-runtime)@[bdcc1c716f...](https://github.com/tremor-rs/tremor-runtime/commit/bdcc1c716ff69ade53c3cd34faa12697f19c1f83)
#### Thursday 2022-08-18 12:24:32 by Sasha Pourcelot

Enforce "no mod.rs files" via clippy lints

Back in spring when I was working on the [ClickHouse sink][1], I had
[an interesting comment][2] stating that Tremor prefers using `mod_name.rs`
files instead of `mod_name/mod.rs` files.

(*In my opinion this is bad, but let's not discuss this here.*)

Once my work got merged, I started wondering if we could statically check this
and make `clippy` emit an error if it sees `mod.rs` files. Turns out there's a
[`mod_module_files`][3] we can `deny`. That's basically what this commit does.

The resulting compilation error is just as friendly as it needs to be:

```none
$ cargo clippy
    Checking tremor-runtime v0.12.4 (/home/ssha/git/tremor/tremor-runtime)
error: `mod.rs` files are not allowed, found `src/should_not_compile/mod.rs`
  --> src/should_not_compile/mod.rs:0:1
   |
   |
note: the lint level is defined here
  --> src/lib.rs:25:5
   |
25 |     clippy::mod_module_files
   |     ^^^^^^^^^^^^^^^^^^^^^^^^
   = help: move `src/should_not_compile/mod.rs` to `src/should_not_compile.rs`
```

I `deny`-ed this on the following crates:
  - `tremor-runtime`,
  - `tremor-api`,
  - `tremo-common`,
  - `tremor-influx`,
  - `tremor-pipeline`,
  - `tremor-script`,
  - `tremor-value`.

Feel free to request the addition of this lint elsewhere. I may have forgotten
some crates :).

It turns out y'all did a great job at maintaining this at each code review, as
I had no compilation error once all the lint were added.

Thank you for your work!

[1]: https://github.com/tremor-rs/tremor-runtime/pull/1538
[2]: https://github.com/tremor-rs/tremor-runtime/pull/1538#discussion_r904836976
[3]: https://rust-lang.github.io/rust-clippy/master/index.html#self_named_module_files

Signed-off-by: Sasha Pourcelot <sasha.pourcelot@protonmail.com>

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[1ab6eb1716...](https://github.com/srsbsns5/GAN-GDDS1/commit/1ab6eb17160a1f130584d76c075528029c513592)
#### Thursday 2022-08-18 12:43:08 by schmidtheimer

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
## [kaieri-4946/MikuMikuWorld](https://github.com/kaieri-4946/MikuMikuWorld)@[8c867ec8b1...](https://github.com/kaieri-4946/MikuMikuWorld/commit/8c867ec8b1b127fae8f6fbf82af2c1aa1184f26c)
#### Thursday 2022-08-18 13:00:12 by Crash5b

Fix importing .sus files with multiple time signatures

i hate my life

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[0f077db733...](https://github.com/pytorch/pytorch/commit/0f077db7335062ffb90e52af8b4013cb0ce80643)
#### Thursday 2022-08-18 13:32:13 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`. 

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream!) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between.

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. The overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.


### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)
  
  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)
  
  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>



[ghstack-poisoned]

---
## [mjg/git](https://github.com/mjg/git)@[5beca49a0b...](https://github.com/mjg/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Thursday 2022-08-18 13:51:49 by Ævar Arnfjörð Bjarmason

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
## [coordinape/coordinape](https://github.com/coordinape/coordinape)@[2a76043a17...](https://github.com/coordinape/coordinape/commit/2a76043a17dd06ac4e47e8d2434b5ef9113fe19c)
#### Thursday 2022-08-18 14:41:08 by topocount

bugfix: enable FormTokenField to have an empty input (#1277)

One of the major considerations during the FormTokenField (and downstream) refactor was allowing for empty string inputs. This enables for much cleaner UX, since users aren't typing "around" a zero
and in my opinion, makes us look like we know what we're doing as devs. There are other hacks that could make the UX better than the incumbent, but why not just make it behave correctly and be done with it?

Co-authored-by: crabsinger <83605543+crabsinger@users.noreply.github.com>
Co-authored-by: zashton <17747090+zashton@users.noreply.github.com>

---
## [wincent/wincent](https://github.com/wincent/wincent)@[00c3aed081...](https://github.com/wincent/wincent/commit/00c3aed081583afc4892450484660373d40a3721)
#### Thursday 2022-08-18 14:46:37 by Greg Hurrell

refactor: more tweaks for new version of git-cipher

In our "dotfiles" aspects we have some entries in "files" that are
really directories, and they contain encrypted files:

Directory:                     Contains:
----------                     ---------

.config/Raycast                .config/Raycast/Script Commands/emp.sh
                               .config/Raycast/Script Commands/the-hub.sh

.gitconfig.d                   .gitconfig.d/retiro

.zsh                           .zsh/exports.private
                               .zsh/hash.private

I am not too worried about the Raycast ones, because I'll always decrypt
on macOS, and that's the only place I use Raycast.

But ".gitconfig.d" could be a problem. If we include such a file without
decrypting it, Git will complain about bad config.

Likewise if we source the ".zsh" items and they are full of gibberish
because they're still encrypted, that will cause problems.

So, as mitigation:

1. In the ".zsh" files, we avoid sourcing them if we detect a magic
   header indicating that the file is still encrypted. I didn't want to
   call out to `git-cipher is-encrypted` from my shell startup files,
   because I want shell startup to be fast.

2. In the ".gitconfig.d" files, we'll skip over them if they aren't
   decrypted. Note that if you then do a `git-cipher lock`, the link
   will start pointing at ciphertext that Git will consider to be
   invalid garbage. In practice, we already have this problem with lots
   of other dotfiles; you're not really supposed to lock a repository
   that you're actively using to provide configuration to your machine.

In the "ssh" aspect,  we have similar stuff going on. The main
"~/.ssh/config" file is templated out, and we won't do that if it is not
decrypted. It itself includes files that are links to (hopefully)
decrypted files. We skip creating those links if things aren't
decrypted, with the same results: if you later lock, they will suddenly
become invalid, and you probably shouldn't do that.

Includes submodule update:

* vendor/git-cipher 35ab0b5...17e05c5 (5):
  > style: format more docs
  > feat(add): staged new files in Git index
  > docs: clean out old documentation
  > refactor: uncomment some code
  > refactor: remove dead code

---
## [stormasm/influxdb_iox](https://github.com/stormasm/influxdb_iox)@[8a5cd1cddd...](https://github.com/stormasm/influxdb_iox/commit/8a5cd1cdddcbe8ed932ddd08e953cd40c8e8d784)
#### Thursday 2022-08-18 15:18:58 by Marco Neumann

refactor: abstract change requests for cache policies (#5382)

* refactor: abstract change requests for cache policies

Tl;Dr; Lets replace the hard-coded enum of change requests with a more
flexible and easier-to-understand function-based approach. It also
unifies the interface for "initial requests" and "reactions".

Story time:

I just wanted to port over the "shared" backend with its "remove if"
functionality to the policy framework. Turns out that this backend does
not just use simple atomic operations but is basically a
"compare&exchange"-like operation (technically: GET+REMOVE) that relies
on a single mutable access lifetime to make sure that this behavior is
sane and nobody messes with the value between the GET and REMOVE. I call
this a "compound request".

The new policy framework did not support this kind of requests so I
thought how I could shoehorn it in. Basically I wanted to extend
`ChangeRequest` to support these kind of operations. But listing
combinations explicitly kinda seemed like some hack. So my brain slowly
came up with an abstract approach how to encode these operations and
after a while I was close to design some kind of mini-VM. I also
considered some ugly workarounds or to not express the "remove if"
functionality" as a policy. My nice vision of a policy framework started
to crack...

This is when sanity kicked in and I realized: every change request is
technically just a function on a (virtual) cache backend. Sure,
all-powerful Rust functions allow you to do ugly stuff that will result
in deadlocks, but with good docs and helpers for the common operations
the risk is very low. Furthermore this is already close to the system I
had for the "initial requests" and which I called a "callback backend".
So I unified both systems and made the change request abstract and all
tests pass and I think it is the better design.

Helps with #5320.

* docs: typos

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>
Co-authored-by: kodiakhq[bot] <49736102+kodiakhq[bot]@users.noreply.github.com>

---
## [edsantiago/libpod](https://github.com/edsantiago/libpod)@[09ef6fc66c...](https://github.com/edsantiago/libpod/commit/09ef6fc66cac44dec94c29cd7a1a53f70831446d)
#### Thursday 2022-08-18 15:48:47 by Ed Santiago

podman generate kube - add actual tests

This exposed a nasty bug in our system-test setup: Ubuntu (runc)
was writing a scratch containers.conf file, and setting CONTAINERS_CONF
to point to it. This was well-intentionedly introduced in #10199 as
part of our long sad history of not testing runc. What I did not
understand at that time is that CONTAINERS_CONF is **dangerous**:
it does not mean "I will read standard containers.conf and then
override", it means "I will **IGNORE** standard containers.conf
and use only the settings in this file"! So on Ubuntu we were
losing all the default settings: capabilities, sysctls, all.

Yes, this is documented in containers.conf(5) but it is such
a huge violation of POLA that I need to repeat it.

In #14972, as yet another attempt to fix our runc crisis, I
introduced a new runc-override mechanism: create a custom
/etc/containers/containers.conf when OCI_RUNTIME=runc.
Unlike the CONTAINERS_CONF envariable, the /etc file
actually means what you think it means: "read the default
file first, then override with the /etc file contents".
I.e., we get the desired defaults. But I didn't remember
this helpers.bash workaround, so our runc testing has
actually been flawed: we have not been testing with
the system containers.conf. This commit removes the
no-longer-needed and never-actually-wanted workaround,
and by virtue of testing the cap-drops in kube generate,
we add a regression test to make sure this never happens
again.

It's a little scary that we haven't been testing capabilities.

Also scary: this PR requires python, for converting yaml to json.
I think that should be safe: python3 'import yaml' and 'json'
works fine on a RHEL8.7 VM from 1minutetip.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[da7c22661e...](https://github.com/mrakgr/The-Spiral-Language/commit/da7c22661e9dcd877caf94eda81568058f5afbcf)
#### Thursday 2022-08-18 15:56:58 by Marko Grdinić

"2:45pm. Done with breakfast. Let me just read the OPM chapter and then I will look into how to put illustrations into the chapter.

3:25pm. I had my fun. Let me get some work done. Let me figure out how to post illustrations.

3:30pm. Oh, I see that the add chapter has a lot more options. There are pre-chapter and post-chapter notes. Also there is something called clean paste specifically for pasting from Google Docs.

In insert image, is it asking me for an URL?

https://www.royalroad.com/forums/thread/101959?page=1#pid839802
> To go a bit more in-depth: You'll need a place online that hosts the image. For this purpose, you either have a webspace of your own or you use one of the many image hosters out there. One popular choice is https://imgur.com/. It's mostly reliable and doesn't do any nonsense to your image. For the rest of the explanation, I'm going to base it of Imgur.

> What you do is you upload the image by clicking new post on imgur. You point it to your file and it will upload. After that, you get a window with the image in the website and various options. When you point at the image (equation in your case), you'll get a window popup that says copy. You click on the v and pick "Get share links". There you pick the option BBCode Forums, Copy. It looks something like this

I wonder if I could use Github or Twitter instead to host my images?

3:35pm. It is really annoying how auto-registering with Google is not working for me.

https://imgur.com/a/blBYUA2

Chapter must be at least 500 characters long.

Ah for fuck's sake.

I guess I need to link directly to the image.

3:50pm. Now RR is messing with the proportions.

I need to scale them down to 1280 otherwise RR will squeeze it down badly.

3:55pm. Let me put in Euclid's Room illustrations.

> First, Thank you for your work.
> It seems that style weight added to your implementation. But why is there no style weight in the option?

I didn't see this tweet earlier. But I am not sure...

4:35pm. Did some replying.

https://www.royalroad.com/fiction/57747/simulacrum-heavens-key/chapter/973184/the-first-dream

Anyway here is the post. What I need to do next is post the rest of the chapters. Let me actually post just one. I want to proofread them properly, and am feeling tired right now.

4:45pm. I actually didn't proofread the first chapter. I should probably go back and do it. But not right now. Let me just deal with two, post it and then I will start looking into opening a Patreon account.

4:55pm. Found a bunch of errors in chapter 2.

5pm. Ah, right. I should not forget to post it on Twitter.

I am almost done with proofreading.

5:05pm.

> (Bad End - The First Nightmare)

Rather than call it a nightmare, how about...

> (Bad End - The Dream Left Behind)

...No, let me stick with the original. It is not that important what the first bad end's name is. I won't obsess over it.

///

Imgur Album: https://imgur.com/a/blBYUA2

I modeled the room and the VN cover in Blender. The reference for the room is my own. I could have taken a photograph, but instead I spent an insane amount of time modeling the objects in Moi 3d and importing them in Blender. Altogether, from late 2021 till now, I spent 9 months studying art, but I hadn't gotten to the point where I could make illustrations quickly enough to make it viable to make use of it for my own novels. Maybe if I spent another few years practicing, I could get to that level, but instead I threw in the towel and decided to just write instead. I really just want to write instead of spending 2-3 weeks per illustration. Art is quite hard, and my talent in it is mediocre, so it has been quite a slog to even get to this point.

This is not the end of the story though when it comes to graphics. At this point in time, generative NNs have gotten really good, and I plan to make use of Stable Diffusion when it comes out of beta as my illustrative tool.

I'll probably get access to it before I manage to get approved on DALLE's waiting list.

My GTX 970 won't be powerful enough to run Stable Diffusion, so I'll have to take some time to set it up on the cloud. I've read that it should come out of beta next week, but I am fine whenever.

It really seems fitting that a story about the Singularity would be illustrated by a NN.

For now my plan is to just write, I'll come back to the early chapters and add more imagery once I get access to a generative NN on par with DALLE. On Royal Road, I've set the image resolution to 1280 x 720 to prevent it from squeezing them, but you open them in a separate window, you'll be able to see them in their full glory.

In addition to a generative NN to create whole images, I'll be using style transfer on top of that as well. I've mentioned that I've modeled the above in Blender. Afterwards I did a style transfer step to add interest.

I've used this tool to do it: https://twitter.com/Ghostlike/status/1543600747568308226

You can see some example of style transfer in action on my profile.

///

///

Heaven's Key is supposed to be a VN, but it makes more sense for me to gradually work on it here on RR rather than in complete silence until I am done. It is also supposed to have music. I have a few good tracks in my head, but unlike art skills which I have 9 months invested in it, or programming which has 6.5 years worth of exp points, my music skills have literally 0, so that is going to have to wait.

Heaven's Key is also supposed to be anime, but char models, as opposed to background illustrations are going to have to wait as well. In terms of art skills my strength is that I am familiar with wide variety of art programs: Blender, Moi, Substance Painter and Designer, Houdini, Clarisse, Zbrush. I treated my art journey like a programming one, so although I have a decent amount of knowledge to base further learning on, to actually get better I'd need to sit down and actually start making pieces. My training as a programmer is working against me here. Programming is all about automation, so given a particular task I just end up looking for shortcuts, but after a certain point in order to get good at art you simply have to sit down and make things.

After 9 months I had to make a choice whether I want to spend more time studying art, or whether I should just write.

The fact that DALLE came out factored into that decision. I fought against the decision to just start writing for a while, but then got tired of 3d. It might turn out that in the future we'll get a generative NN model that is good at the anime aesthetic.

Looking into the future, it feels like being a writer is going to get all kinds of advantages that were originally only accessible to other professions. Throughout the last decade, I really expected programming itself to be the biggest beneficiary of the AI wave, but I was wrong about that. Right now the programming skill is not a big deal, but in the post-Singularity era it will be.

///

5:35pm. Did the second post. I won't bother posting the third today.

One thing I've realized is that maybe I should be adding the chapter numbers to each chapter. I'll do that later.

Right now, let me take a look at Patreon.

5:45pm. It turns out I already have a Patreon account. I must have done that while setting up sponsorship for Spiral.

'What are creating? A programming language.'

Yeah. It seems that I did not finish the page back then. I'll take the cover photo from my AngelList page. Or maybe I should put in some kind cartoon. I am not sure.

5:50pm. Is the cover image for my Patreon page or something else?

Let me stop here for the day, I am too tired to deal with this anymore.

5:55pm. Let me close here. Lunch then fun."

---
## [DrParadox7/Lost-Era-Modpack](https://github.com/DrParadox7/Lost-Era-Modpack)@[1676dd19de...](https://github.com/DrParadox7/Lost-Era-Modpack/commit/1676dd19de59ea9fcc9358a6d9b9d34c07b18097)
#### Thursday 2022-08-18 16:10:04 by TechnoParadox

1.5.2

-Increased Dryad spawnrate
-Buffed Rock Crusher
-Buffed Grout Recipes
-Decreased spawn rate of Goblins
-Decreased Spawn rate of Sirens & Nagas
-Reworked Deep Dark Portal Recipe
-Nerfed recipe Fel Pumpkin
-Nerfed Poison Skeleton
-Buffed food and made it more interactive.
-Added optional Performance enhancing mods
-Blood Altar now requires Nether Bricks
-Populated BM blacklist
-Added shedding support to most blazes and Ghasts
-Enabled Magic Support for Compact Machines
-Increased Ocean Frequency
-Reduced AE2 Quartz generation
-Reduced Aluminum Generation
-Increased Zinc Generation
-Increased Quantum Ore generation
-Reduced Silver generation
-Increased Bitumen Ore generation
-Concussion Creeper is now exclusive to the Mining Dimension
-Reduced Direwolf Spawns
-Disabled Cursed Earth
-Increased energy usage of TE ore multiplying machines
-Cleaned up chat from first creating a world
-Blacklisted BM Air sigil from Twilight Forest
-Fixed inaccurate math from Mekanism's power generating machines
-Blacklisted Demon Portal from anything that could move it.
-Disabled TC's Wooden Rails and Natura's Blaze Rails
-Decreased Whitestone loot rate
-Cleaned up scripts
-Reworked recipes for Mek's Energy Cells
-Simplify BioFuel production
-Added Methane based Energy Generation
-Fix bug of multiplicative Pestle and Mortar
-Added PortaSpawner Recipe
-Altered SafariNet's Recipes

---
## [Goncholito/isaacscript2](https://github.com/Goncholito/isaacscript2)@[403a423276...](https://github.com/Goncholito/isaacscript2/commit/403a423276d6f83bf998f9233b4377c5e85660d8)
#### Thursday 2022-08-18 16:28:46 by Goncholito

started this fucking shit oh God please fuck me ha

---
## [Khalvat-M/kernel_samsung_msm8974](https://github.com/Khalvat-M/kernel_samsung_msm8974)@[db6e12dad5...](https://github.com/Khalvat-M/kernel_samsung_msm8974/commit/db6e12dad55706c4ea1bd676302aa985b8add4ec)
#### Thursday 2022-08-18 16:52:34 by KOSAKI Motohiro

mqueue: don't use kmalloc with KMALLOC_MAX_SIZE

KMALLOC_MAX_SIZE is not a good threshold.  It is extremely high and
problematic.  Unfortunately, some silly drivers depend on this and we
can't change it.  But any new code needn't use such extreme ugly high
order allocations.  It brings us awful fragmentation issues and system
slowdown.

Signed-off-by: KOSAKI Motohiro <mkosaki@jp.fujitsu.com>
Acked-by: Doug Ledford <dledford@redhat.com>
Acked-by: Joe Korty <joe.korty@ccur.com>
Cc: Amerigo Wang <amwang@redhat.com>
Cc: Serge E. Hallyn <serue@us.ibm.com>
Cc: Jiri Slaby <jslaby@suse.cz>
Cc: Joe Korty <joe.korty@ccur.com>
Cc: Manfred Spraul <manfred@colorfullife.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [sbrowne217828/search-the-scriptures](https://github.com/sbrowne217828/search-the-scriptures)@[5a475b2ddd...](https://github.com/sbrowne217828/search-the-scriptures/commit/5a475b2ddd52647e7d263ab4c145f027310b28ea)
#### Thursday 2022-08-18 17:00:28 by Scott Brown

Create TrashandFilth

1 Corinthians chapter 4 verse 13 

In a manichaeism intrepretation filth would be zero because of life at the smallest discernible levels being infinite ouraboros like and trash would be 1 because of air and water taking rock like things around a fairly unchanging control mass within a certain control volume.

Daniel the prophet knew that God is a consuming fire, although a thorium reactor is kinda heavy while a fusion reactor is only known by God...

---
## [Monkestation/MonkeStation](https://github.com/Monkestation/MonkeStation)@[31c9d411a7...](https://github.com/Monkestation/MonkeStation/commit/31c9d411a7b9e4f6ad66b930d535e24e5555bd06)
#### Thursday 2022-08-18 17:16:27 by nednaZ

Dynamic Adjustments Part 2 (#627)

* Dynamic Changes II

Changes the intercept message to be more flavorful.

Clamps the threat level to between 75% player pop and 200% player pop.

Logs increases to Dynamic threat budget.

Slightly reduces the weight of latejoin traitors. (From 7 to 4)

Increases the Weight (2 to 4), decreases the Cost (40 to 20) and decreases Minimum Players (35 to 30) of Revolution Latejoins.

Restores Heretics to Latejoin and Roundstart.

Heretics now have a lower number of sacrifice objectives. (From 2-6 to 1-3)

Heretics now have a chance to get a Steal objective.

Dynamic Abductors may no longer get spawned  in solo by mistake.

Midround Traitor chance reduced. (From 7 to 5)
Midround Traitor cap reduced. (From player_count / 10 to player_count / 15)

Midround Wizard weight increased (From 1 to 3)
Midround Wizards are now a HIGH_IMPACT_RULESET and will not repeat.

Midround Nuclear Operative Weight reduced. (From 5 to 4)

Blob Weight (4 to 3) and Cost (10 to 25) changed.

Xenomorph Cost increased (10 to 25)

Nightmare Cost increased (10 to 15)

Abductor Cost increased (10 to 15)

Space Pirates added to Dynamic.

Space Pirates have been given an update, with ship names and support for multiple types of pirates existing.

Revenant added to Dynamic.

Obsessed added to Dynamic.

Space Dragon early start changed to 40 minutes (From 50 minutes)

Roundstart Traitor cost increased (7 to 8)

Blood Brother Weight (4 to 2), Cost(15 to 13) and Scaling Cost(15 to 13) adjusted.

Changeling Weight(3 to 4) and Cost(15 to 17) adjusted.

Roundstart Wizard Weight(2 to 5) and Cost(40 to 30) adjusted.

Blood and Clock Cult Weight and Cost(30 to 25) adjusted.

Nuclear Operatives Weight(3 to 4) and Cost(50 to 25) adjusted.

* lone op

why didn't this commit

* Reverts max_traitors change

The maximum number of traitors is now player_count / 10 rather than 15

* Revolution Tweaks

Reduces the weight of latejoin revs from 4 to 2.

Increases the minimum number of required enemies from 2-0 to 5.

Changes the required enemies to be only security and the captain, AI and Cyborg are not counted.

The shuttle is no longer automatically called upon a Revolution victory.

There will be an announcement made after either 30% of the station is converted into revolutionaries OR if two heads of staff are killed.

* Pirate Fixes

Pirates now function as intended in Dynamic.

Pirates have a 25 player minimum to be called as antagonists.

Pirates have a minimum of 2 enemies before they can be called.

* Faster than opening VSC.

---
## [alsotoes/papers-we-love](https://github.com/alsotoes/papers-we-love)@[3565b2ff01...](https://github.com/alsotoes/papers-we-love/commit/3565b2ff013feb4497c6afa15b98ea5cc95bd181)
#### Thursday 2022-08-18 17:29:37 by Lee Sharma

Add Tidy Data (2014) to list of articles (#414)

The following major changes were made:

  - Create the `./data_science` directory

  - Add the *Tidy Data* pdf

  - Create/update the `./data_science` README with the article
    information (including the scroll icon, link to the source, author,
    and publication year)

Decisions:

  - Since no relevant folder existed, I created the `./data_science`
    directory. This is a broad subject, but until the number of articles
    get to be unmanageable, I think that keeping them together will help
    people find what they're interested in.

  - The README does have a sub-category list (*Tidy Data* is under "Data
    Cleaning"), but there is no corresponding subdirectory. This is
    because there are few enough raw articles that someone browsing the
    directory listing won't benefit from the subfolder (but it will cost
    them an extra click), but someone skimming the README might want to
    know more about the article categorization.

  - The README listing includes scroll/title/author/link to source, but
    it does not include any abstract/rationale. The different READMEs
    take different approaches here, but this seems to be the best
    trade-off between a concise listing and providing useful
    information. I'm happy to add a rationale or summary if it would be
    useful though.

Paper Rationale:

  This paper describes a subset of data cleaning that had previously
  been largely neglected: data tidying, or the process of reforming data
  into a standardized structure to allow for easier manipulation and the
  development of better data tools.

  The author is prominent in the data science community, being the chief
  scientist at RStudio, having authored a number of highly-regarded and
  very popular data science packages (ex. `ggplot2` and `reshape2`).
  He was named a Fellow by the American Statistical Association in 2015
  for "pivotal contributions to statistical practice through innovative
  and pioneering research in statistical graphics and computing." For
  more on Hadley Wickham, see his website: http://hadley.nz/

  This is a fairly popular paper as well; according to jstatsoft, it has
  nearly 50k views. I've seen it mentioned in several other popular
  media as well, including John Hopkin's very popular online Data
  Science MOOC.

  The main reason that I'm adding this paper, however, is because of
  how well-written it is. I don't come from a data science background,
  but after reading this paper, I walked away with a decent
  understanding of the significance of Wickham's research and
  standardization efforts, the current (circa 2014) state of the field,
  and many of the technical details associated with his method of data
  tidying. It was easy to read, despite my lacking data science
  background, but it's clear that Wickham did not "dumb down" the
  content in order to accomplish that.

  I believe that other chapters and independent readers will find this
  to be an interesting, enjoyable paper, and I believe that it will
  continue to affect the field of data cleaning.

  *This paper will be presented at the October meeting of Papers We Love
  Washington, D.C. & Northern VA.*

Copyright Information:

  The raw paper can be legally included in this repository. *Tidy Data*
  falls under the [Creative Commons Attribution 3.0 Unported License],
  which allows for sharing and adaptation with attribution.

  [Creative Commons Attribution 3.0 Unported License]:
    https://creativecommons.org/licenses/by/3.0/

---
## [alsotoes/papers-we-love](https://github.com/alsotoes/papers-we-love)@[7d7ee69264...](https://github.com/alsotoes/papers-we-love/commit/7d7ee69264f625753b9528ad0bae668dd02e7f0f)
#### Thursday 2022-08-18 17:29:37 by Lee Sharma

Add Combinatorial Analysis and Computers (1965) (#422)

Changes:

  - add: *Combinatorial Analysis and Computers* (1965) to
         `combinatory_logic/README.md` list
  - add: year to the other paper in the README
  - fix: tweak format of papers README for readability

Decisions:

  - I put this in the `combinatory_logic` folder, but I think it would
    also fit in the `comp_sci_fundamentals_and_history` folder (given
    Knuth's historical importance to the field and the more
    theoretical nature of the paper). This seemed more direct.

---

Paper Title:  Combinatorial Analysis and Computers
Author(s):    Marshall Hall Jr. and Donald E. Knuth
Paper Year:   1965

Reasons for Including Paper:

  Papers We Love DC/NoVA will be discussing this paper (and others) at our
  November meetup.

  This paper is included in Donald Knuth's book *Selected Papers
  on Discrete Mathematics*. Knuth's writings have been extremely
  important to the field of computer science, and I think that most of
  his papers would fit in well here. This one introduces computational
  complexity and the benefits/limits of computing, then it dives into
  several combinatorial problems.

  I find it interesting because 1) it's a neat view of the possibilities and
  limitations of computation early on, and 2) the problems that he lays out
  are interesting exercises even today.

---
## [devnexen/php-src](https://github.com/devnexen/php-src)@[128768a450...](https://github.com/devnexen/php-src/commit/128768a4503c8bc5c6ccf564061f9dc8b307f57f)
#### Thursday 2022-08-18 18:14:41 by Alex Dowad

Adjust number of error markers emitted for truncated UTF-8 code units

In 04e59c916f, I amended the UTF-8 conversion code, so that when given
invalid input, it would emit a number of errors markers harmonizing
with the WHATWG's specification of the standard UTF-8 decoding
algorithm. (Which, gentle reader of commit logs, you can find online
at https://encoding.spec.whatwg.org/#utf-8-decoder.) However, the code
in 04e59c916f was faulty in the case that a truncated UTF-8 code unit
starts with 0xF1.

Then, in dc1ba61d09, when making a small refactoring to a different
part of the UTF-8 conversion code, I inexplicably broke part of the
working code, causing the same fault which was already present with
truncated UTF-8 code units starting with 0xF1 to also occur with
0xF2 and 0xF3 as well. I don't remember what inane thoughts I was
thinking when I pulled off this feat of utter mental confusion.

None of these cases were covered by unit tests, by the way.

Thankfully, my trusty fuzzer picked up on this when testing the
new implementation of mb_parse_str (since the legacy UTF-8
conversion filter did not suffer from the same problem, and I was
fuzzing to find any differences in behavior between the old and
new implementations).

Fortuitously, the fuzzer also picked up another issue which was
present in 04e59c916f. I was emitting only one error marker for
truncated code units starting with 0xE0 or 0xED, in cases where
the WHATWG standard indicates two should be emitted. Examples
are 0xE0 0x9F <END OF STRING> or 0xED 0xA0 <END OF STRING>.

Code units starting with 0xE0-0xED should have 3 bytes. If the
first byte is 0xE0, the second MUST be 0xA0 or greater. (Otherwise,
the codepoint could have fit in a two-byte code unit.) And if the
first byte is 0xED, the second MUST be 0x9F or less. According to
the WHATWG algorithm, step 4, if the second byte is outside the
legal range, then the decoder should emit an error... AND
reprocess the out-of-range byte. The reprocessing will then
cause another error. That's why the decoder should indicate two
errors and not one.

---
## [Eneocho/vgstation13](https://github.com/Eneocho/vgstation13)@[b879dddba0...](https://github.com/Eneocho/vgstation13/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Thursday 2022-08-18 19:05:52 by rob

adds sound effects to surgery steps (#31850)

* the everything

* nmb

* ok

* dfdffdfsds

* ssssssssssssssssssssskurfusr

* fuck yoiu damian fuck you!!!!!

* DAMIANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

* D

---
## [olujoe1/Peter-Obi-s-presidential-Aspiration-2023-Nigerian-Twitter-Users-Perception-Twitter-Sentiment-Analy](https://github.com/olujoe1/Peter-Obi-s-presidential-Aspiration-2023-Nigerian-Twitter-Users-Perception-Twitter-Sentiment-Analy)@[238ec51f6b...](https://github.com/olujoe1/Peter-Obi-s-presidential-Aspiration-2023-Nigerian-Twitter-Users-Perception-Twitter-Sentiment-Analy/commit/238ec51f6b79d82ca5a7875a34fca0a701466bf3)
#### Thursday 2022-08-18 19:14:34 by Olutoba Joel Olufisayo

Update README.md

# Peter-Obi-s-presidential-Aspiration-2023-Nigerian-Twitter-Users-Perception-Twitter-Sentiment-Analy
Twitter Sentiment Analysis
# Introduction
This Data Analytics Project focused on Peter Obi tweets (a presidential aspirant in Nigeria) using Natural Language Processing (NLP) Techniques. Every 4 year in Nigeria there is a change of government or extension of existing one, where every political party present their candidates, Peter Obi as one of the candidates who seem to be widely talked about on twitter after he declared his ambition on one of the political parties.

Sncrape was used to mine tweets about Peter Obi from March 2022 shortly before he declared his ambition till August 2022, the total tweets mined was 387,109k. we made use of several Python libraries like Pandas (for Data Manipulation/Cleaning), Sncrape (for Tweets Mining), NLTK (Natural Language Toolkit library to handle text data), TextBlob (for Sentiment Analysis), Matplotlib, Plotly & WordCloud (for Data Visualization), Emot & emoticon (for Emojis identification/for expressed emotion emoji).

# Content
1. Introduction

2. Data Mining and Concatenation

3. Data Cleaning

5. Handling of Text Column

6. Data Exploratory Analysis

7. Sentiment Analysis

# Data Mining and Concatenation
Sncrape as a mining tool is as easy as biting a pie, after trying a couple of tools including tweepy which requires rigorous process for getting a substantial amount of data from twitter. Snscrape is a scraper for social networking services (SNS), including Facebook, Instagram etc. With it we were able to mine tweets containing ‘Peter Obi’ as our key word, and not #tags because the focus is to know what individual is saying about him, while #tag mostly is used by people to be on the trend table for personal promotion of their tweets, data for six months was scrapped, i.e., from March 4th 2022 till August 4th 2022, the data contains datetime, username, follower counts, like counts, and more other variables.


# mining and concat: (https://user-images.githubusercontent.com/76227858/185472484-489eb233-65f7-4591-b7a6-5a8fc360655d.png)

# Data Cleaning
Through data cleaning process we were able to check for nan and none values in the data frame with pandas, through sncrape we were able to filter for the exact data we wanted, this reduced our work on data cleaning, as the data is free of missing values and duplicates, you can read on sncrape here. However, we modify the data to ensure it is free of irrelevances (emojis) and incorrect information (misspelt word). Date time was created for an insight into the daily data trend in our data.

# Handling text data
Text data i.e., individual tweet contains characters (emojis, punctuation, numbers, rare words, #tags, unfamiliar words, links, @, and stopwords) that can serve as noise in our data, which make it important for our data to be cleaned and properly treated. Some of the above libraries like NLTK helped us to manipulate our string data by changing the texts data into lower case, remove stopwaords, create additional columns, among which a column was created for other aspirants whose names were tweeted alongside peter obi for insight, remove emojis and lemmatize our data.

Also, a column was created for the most ratioed tweets/username, i.e., the tweet with the most negative reactions from other users based on what they tweet about Peter Obi. Social medial as greatly enhanced the use of emojis, as they are used to express emotions, with emoticon, were we able to analysis individual expressions through emojis.

With lemmatizer we were able to get the contextual meaning of every word, unlike stemming that can only get the root of a word maybe with meaning or not, you can read up on that here, after this we created a column for our cleaned text data for sentiment analysis.

# Data exploratory analysis
  
  Charting and Visualization

In this section plotly was chosen as the visualization tool because of it flexibly and reactive screen just like PowerBi in jupyter notebook, we got insights from the variables and a wordcloud was generated with the twitter bird to display the most frequent words.

# Conclusion
This research helped to reveal the intention behind every tweets of individual who tweeted about Peter Obi within the time the data was collected, also tweets have been made consistently after when he revealed his desire to run for the presidency, there were 378.48k distinct tweets, 44% of the tweets has positive connotations, 41% were neutral and 14% were negative, this implies that the majority of the 100.44k distinct induvial talking about him were very much interested in his presidential ambition.

However, there were tweets with neutrality whilst most of it does not indicate indifference, rather the choices of words captured as such does not fall between what TextBlob classified has positive or negative, with the seamless traction there were still tweets with negative connotations, users who are not supporting his presidential ambition.

---
## [val-verde/openimageio](https://github.com/val-verde/openimageio)@[594776d9c6...](https://github.com/val-verde/openimageio/commit/594776d9c617ab05b3cf0ff17d69dff908c1ae7e)
#### Thursday 2022-08-18 19:20:22 by Larry Gritz

Speed up case insensitive string comparisons (#3388)

Oh boy, never leave anything unbenchmarked.

Turns out the boost::algorithm functions we were relying on underneath
many Strutil "case-insensitive" comparisons were ridiculously slow.
We thought they were good enough because they allowed specification of
locale, so we could just pass the static classic locale, and so they
would be inexpensive because they didn't have to query the current
locale.  But this is wrong, they were still ghastly.

So here I rewrite Strutil::iequals, iless, starts_with, istarts_with,
ends_with, iends_with in terms of a new (internal) Strutil::strcasecmp
and strncasecmp (which underneath handle differences in platform, and
use the locale-independent versions). The net result is that most of
those case-independent comparisons speed up by a factor of
50-100x. Wow.

I still need to tackle the family of 'ifind' related functions. They
are a bit trickier. But I'll leave them for another time, because I
need to roll this present fix out right away to fix a real production
bottleneck.

(Worth noting: iequals is instrumental when you're searching a
ParamValueList for a particular name, which is what happens when you
look up attributes from an ImageSpec, which is what happens when you
call get_texture_info(), which is what underlies OSL gettextureinfo()
calls in the cases that they cannot be constant-folded during runtime
optimization. So this came to my attention when analyzing a slow scene
whose shaders had a pathological explosion of gettextureinfo calls that
couldn't be optimized away.)

---
## [tahonermann/llvm-project](https://github.com/tahonermann/llvm-project)@[7c51f02eff...](https://github.com/tahonermann/llvm-project/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Thursday 2022-08-18 19:50:41 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could exposed a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[90e0f0ca54...](https://github.com/pytorch/pytorch/commit/90e0f0ca54e232846b51455be452df3431c43ced)
#### Thursday 2022-08-18 20:06:49 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`. 

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading). 

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.


### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)
  
  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)
  
  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>



[ghstack-poisoned]

---
## [jupyterkat/Yogstation](https://github.com/jupyterkat/Yogstation)@[f4c7571fc3...](https://github.com/jupyterkat/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Thursday 2022-08-18 22:35:06 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [chanzuckerberg/redcord](https://github.com/chanzuckerberg/redcord)@[c26372291d...](https://github.com/chanzuckerberg/redcord/commit/c26372291df9414046f6bf3160a11e5487479662)
#### Thursday 2022-08-18 23:03:11 by Matt Wang

fix Ruby 3 keyword arg errors (#110)

Overall, this PR resolves issues that *break tests* on Ruby 3. It's a different question on whether or not these actually bring us to Ruby 3 usability.

To test this, I think we should probably link in `redcord` to `traject` locally, and run some tests. I'm not sure if this is sufficient (or how confident we are in the test coverage in general).

Even though these two changes are one-liners, I do want to enumerate my reasoning - and apprehension - for both.

### `.send` and `define_method`

This one was trickier to hunt down, since I was confused where this call was coming from; the deprecation warning indicates that it's from sorbet, but it's actually a call validation layer in-between `redis.send`.

The core issue is explained in the "Handling argument delegation" of [the official post](https://www.ruby-lang.org/en/news/2019/12/12/separation-of-positional-and-keyword-arguments-in-ruby-3-0/); the tl;dr is

```ruby
# Ruby 2.6, works
# Ruby 2.7, deprecation warning
# Ruby 3, ArgumentError
def foo(*args, &block)
  target(*args, &block)
end

# Ruby 2.5, 2.6: seems to have a problem
# Ruby 2, may require `Module#ruby2_keywords`
# Ruby 3, works
def foo(*args, **kwargs, &block)
  target(*args, **kwargs, &block)
end
```

In `connection_pool`, we iterate through instance method; one of them is `create_hash_returning_id`:

```ruby
redis.send(:create_hash_returning_id, *args, &blk) 
# ~ redis.create_hash_returning_id(*args, &blk)
```

`create_hash_returning_id` takes a mix of both positional and keyword args. Thus, the new behaviour (which separates them) won't work, we'll instead need to do

```ruby
redis.send(:create_hash_returning_id, *args, **kwargs, &blk)
# ~ redis.create_hash_returning_id(*args, **kwargs, &blk)
```

So, this PR does that. 

It's a bit unclear to me on whether or not I should also update `method_missing` and `define_method`, though my intuitive understanding of this is that we should. Would love a double-check here.

(under the hood - this should resolve other sorbet call-validator errors we get, like the ones we saw in Along)

### `zscan_each`

This is a more straightforward example. I'm more curious about the behaviour we want, and in particular, why the `key` parameter was `nil` before (was it?)! And, should we be setting the `key` value to `key` instead?

Anyways, explicitly setting the positional argument as `nil` forces the keyword argument to be interpreted as a keyword. I think this is one of the edge case-like issues they discuss in the "Why we're deprecating the automatic conversion" section [of the release blog post](https://www.ruby-lang.org/en/news/2019/12/12/separation-of-positional-and-keyword-arguments-in-ruby-3-0/).

---

