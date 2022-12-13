## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-12](docs/good-messages/2022/2022-12-12.md)


2,076,802 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,076,802 were push events containing 3,122,132 commit messages that amount to 258,141,231 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[fcdf5d850c...](https://github.com/Gofawful5/Skyrat-tg/commit/fcdf5d850c47ac8c9c17045bb5a021d8283d3c0c)
#### Monday 2022-12-12 00:56:27 by SkyratBot

[MIRROR] Psykers [MDB IGNORE] (#17825)

* Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@ gmail.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Psykers

* commented out stuff is now in

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: tralezab <spamqetuo2@ gmail.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[e766444468...](https://github.com/ShizCalev/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Monday 2022-12-12 01:03:19 by LemonInTheDark

Changes our map_format to SIDE_MAP (#70162)


## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [HanSun111/U5L6](https://github.com/HanSun111/U5L6)@[1e374e5888...](https://github.com/HanSun111/U5L6/commit/1e374e58880ddcbb05963ac176b89524f3bfa0ee)
#### Monday 2022-12-12 04:02:04 by hansun

bro, cannot for the life of me figure out the challenge
God is dead. God remains dead. And we have killed him. How shall we comfort ourselves, the murderers of all murderers? What was holiest and mightiest of all that the world has yet owned has bled to death under our knives: who will wipe this blood off us? What water is there for us to clean ourselves? What festivals of atonement, what sacred games shall we have to invent? Is not the greatness of this deed too great for us? Must we ourselves not become gods simply to appear worthy of it?

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[70bcd3b6fb...](https://github.com/ThePiachu/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Monday 2022-12-12 04:23:19 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [farzadmf/advent-of-code](https://github.com/farzadmf/advent-of-code)@[248ba7b377...](https://github.com/farzadmf/advent-of-code/commit/248ba7b377b51866dd0dc382e12d885393cb6b84)
#### Monday 2022-12-12 04:25:40 by Farzad Majidfayyaz

FUCKKKKK RUST; THE ABSOLUTE WORST LANGUAGE EVER; MY ASS MOST LOVABLE!!!!!

Can't even do a simple iteration ............ FUCK YOU PEOPLE with your
judgements

---
## [Tilos-Project/Tilos](https://github.com/Tilos-Project/Tilos)@[7149d3ca25...](https://github.com/Tilos-Project/Tilos/commit/7149d3ca252f532957eae03037752528dda16a55)
#### Monday 2022-12-12 04:56:08 by bobross69696969

Whisky is a dumb cunt and I want to fuck his asshole. It is so tight. oh god oh gos. holy shit I want to dog his sweet ass so good. I need so much lube I am going to run out please god gift me with the power to buy more lube.  Whiskey's ass be so fine.

---
## [projectkepler-ru/Foundation-19](https://github.com/projectkepler-ru/Foundation-19)@[6bf6cdb77f...](https://github.com/projectkepler-ru/Foundation-19/commit/6bf6cdb77f582598b90e63fa44a922fd033ae3d0)
#### Monday 2022-12-12 05:11:09 by harry

fixes panic bunker adjacent shitcode (#769)

* ugly as hell

* idiot

* think before i commit (never)

---
## [Pre-Fortress-2/pf2-fastdl](https://github.com/Pre-Fortress-2/pf2-fastdl)@[b655e69dea...](https://github.com/Pre-Fortress-2/pf2-fastdl/commit/b655e69dea5ab065158a81efe36bae7321819008)
#### Monday 2022-12-12 05:32:29 by PrivatePolygon

these didnt fucking go in for some reason, god damn it

---
## [Tsar-Salat/tgstationcashew](https://github.com/Tsar-Salat/tgstationcashew)@[ebc0227176...](https://github.com/Tsar-Salat/tgstationcashew/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Monday 2022-12-12 05:37:13 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[84b1612201...](https://github.com/Erol509/Skyrat-tg/commit/84b161220115e3243272299b3f8f3cb29d484709)
#### Monday 2022-12-12 05:40:58 by SkyratBot

[MIRROR] Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. [MDB IGNORE] (#18019)

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.

![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup.

* update modular

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [hero-outman/freq_used_code](https://github.com/hero-outman/freq_used_code)@[04ff33a4ca...](https://github.com/hero-outman/freq_used_code/commit/04ff33a4cacc6a1d73cdd81e3d1921c8234e74c2)
#### Monday 2022-12-12 06:41:25 by JP lab

backup my damn codes in case of covid blockdown. fuck you

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[de070334b4...](https://github.com/rHermes/adventofcode/commit/de070334b4059f12226a6055d42d9a266d4ef93c)
#### Monday 2022-12-12 06:46:45 by Teodor Spæren

2022 Day 12

Well, today was rooouuuggghhhh. I'm actually rather ashamed, graph
algorithms used to be my bread and butter, but I found myself not even
remembering basic shit today. I'm going to blame a lack of preparation
and early in the morning, but secretly maybe I've just gotten a bit lax
with my algo skills.

Well, let me tell you the tale of my incompetence. I begin with opening
up part one and quickly realizing that, yes, this is a graph problem. I
also have the idea that BFS will be good enough here, and I start
implementing it. The implementation is slower than I would like and I
make multiple mistakes. Some indexing ones, but the most major one is
that I don't account for the fact that we can go "down" as long as we
want, but we can only go one up. I read it as you can only go down 1
level as well.

I don't realize I'm making this mistake, so the example works, but it
times out on the actual input. I try out some different things, but I
can't get it faster, so I start doubting my assumptions about the task,
but also about the fact that BFS is equal to Dijkstra's algorithm for
unweighted graphs.

In the end, I chose to bite the bullet and download networkx, and start
reading the documentation. I fumble around there for some time, until I
realize that I have to use "DiGraph" to get a directed graph. Once I do
that, I get told that there is no path between the two. I spend more
time debugging this, but in the end go back to the task and really
reread it.

That's when I catch the hight thing. The worst part, is that I remember
now, that the first time I read it, I noticed the asymmetry and thought:
"Ok, gotta remember that and make the graph directional". I made the
graph directional, but I forgot about the checks for building the graph.

When I fixed that, I got the first part. Then for the second part I
again tried to use my bfs implementation, but for some reason that I
still don't know, it's to slow and didn't return the right answer? I'm
sure it's going to end up being a minor thing, but it's very
frustrating.

It's an interesting problem, multiple source, single destination,
shortest path. I haven't actually seen this before, but from what I see,
it would be an easy thing to modify BFS to solve, just add more nodes in
the Q in the start.

Ok, but I thought that one way to do this was to start from the end and
just terminate on first "a" seen. But this did not work, because now
that we are going the other way, I have to reverse the condition for
changing levels, but I didn't remember that before after.

I then just looked up BFS on networkx and eventually found "bfs_layers",
which does almost exactly what I need. After a bit of messing around
there, I got the answer.

This was quite humbling, I guess it really wasn't my day and the
implementation of these algorithm really is "use it or lose it".

While writing this, I realize that we can actually do better than BFS
here, because we have a heuristic that BFS does not have. We can always
just go 1 level up, and so we know the minimum amount of steps needed is
at least 26 minus the current level. I'll sit down now and try to
implement this.

I'm also very curious as to why my BFS implementation didn't work, but
I'll sort that out as well.

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 12   00:32:54   2296      0   00:49:11   2976      0

---
## [Marc-Gee/seedsigner](https://github.com/Marc-Gee/seedsigner)@[d2a657f2d4...](https://github.com/Marc-Gee/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Monday 2022-12-12 08:03:34 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [keydon/adventOfCode](https://github.com/keydon/adventOfCode)@[8cf07e0d27...](https://github.com/keydon/adventOfCode/commit/8cf07e0d27e126157d87949b36788beb9629d9d9)
#### Monday 2022-12-12 08:14:50 by Lukas Bugaj

--- Day 11: Monkey in the Middle ---

As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on how worried you are about each item.

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

---
## [jhvst/coredns](https://github.com/jhvst/coredns)@[bddae69832...](https://github.com/jhvst/coredns/commit/bddae698320bc5619fc9bd7e98dd837a5d8ead3e)
#### Monday 2022-12-12 08:21:26 by Juuso Haavisto

plugin/etcd: implicit requirement on etcd 3.5 not documented

**What would you like to be added**: I would like to have the version requirement for `etcd` be more clearly stated for the plugin in the documentation. It seems to require `3.5`.

**Why is this needed**: It would have saved some time for me, as it's not clear from the documentation that the plugin seems to only work with the more recent version.

So, what I did: I installed `etcd` from my package manager, which happened to resolve to version `3.3.27`. I set up the cluster, then proceeded to install `coredns`, which my package manager resolved to version `1.10.0`. I read through the examples and documentation on the coredns `etcd` plugin page on what to do. Here, this is where I made a mistake: when the `etcdctl put` request did not resolve on my nodes, I should have been alarmed. What I did was proceed to use the `set` subcommand. While the `etcd` clearly did save my requests, what I did not get was a DNS response despite several iterations on my configuration.

After troubleshooting this for around two hours I started to consider patching my software, when I realized that my package manager had the more recent versions under special namespace. After updating to `3.5.6`, the examples started working, as the `put` subcommand resolved.

To possibly save other people's time, I would like to make it explicit that an `etcd` version with the `put` subcommand is required. The current documentation makes it seem like it's not, whereas from my today's anecdotal experience it is.

---
## [Upsetkoala/app-dev](https://github.com/Upsetkoala/app-dev)@[ef6fe90958...](https://github.com/Upsetkoala/app-dev/commit/ef6fe90958714510c1f645d4207446dcddc0c2a7)
#### Monday 2022-12-12 08:24:22 by Upsetkoala

Update README.md

I personally love the first three seasons of ELITE, but after that I stopped watching because it's boring and the characters are not suited for the role.  The 100 is my favorite post-apocalyptic series of all time, not just the fact that Raven is hot, but also I love the stories, the twists, and overall setting of the series. The Sweet Magnolias tells us about the daily life of a simple family and the struggles they need to get through every step of the way. Squid game is a movie about suspense, fun, and traditional cultures of Korean community. Lastly, Wednesday is a story about a psychopath gothic girl transferred in a school of rejects and she discovered some secrets that needed to be unfold.

---
## [xiaoleGun/Home](https://github.com/xiaoleGun/Home)@[a520d7729a...](https://github.com/xiaoleGun/Home/commit/a520d7729ab25d2b4737443467c99a384fdd1758)
#### Monday 2022-12-12 08:47:51 by xiaoleGun

Fuck your mother's militaristic Japan

 *  The Nanking Massacre, commonly known as
    the Rape of Nanking, was an infamous war
    crime committed by the Japanese military
    in Nanjing (Nanking), then the capital of
    the Republic of China, after it fell to the
    Imperial Japanese Army on December 13, 1937.
    The duration of the massacre is not clearly
    defined, although the violence lasted well
    into the next six weeks, until early February 1938.
    Japanese officials lied about civilian death figures and
    still refuse to reveal them properly today.
    During the occupation of Nanking, the Japanese army
    committed numerous atrocities, such as rape, looting,
    arson and the execution of prisoners of war and civilians.
    The executions began under the pretext of eliminating Chinese
    soldiers disguised as civilians, and a large number of innocent
    men were intentionally misidentified as enemy combatants and executed
    as the massacre gathered momentum. A large number of women
    and children were also killed, as rape and murder became more widespread.

Signed-off-by: xiaoleGun <1592501605@qq.com>

---
## [mattpang/aoc2022](https://github.com/mattpang/aoc2022)@[139597c24c...](https://github.com/mattpang/aoc2022/commit/139597c24c1356e32645716ad6139aa24319cafc)
#### Monday 2022-12-12 09:04:35 by Matt Pang

The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of
charity and good will, shepherds the weak through the valley of the darkness, for he is truly his brother's keeper and the finder of lost children.

---
## [Autisem/tgstation](https://github.com/Autisem/tgstation)@[e9cff525dc...](https://github.com/Autisem/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Monday 2022-12-12 10:07:01 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [01ste02/AoC2022](https://github.com/01ste02/AoC2022)@[fca8471f70...](https://github.com/01ste02/AoC2022/commit/fca8471f70134c276d51a8923c91de191ba0c6f1)
#### Monday 2022-12-12 10:44:03 by Oskar Stenberg

Day 12. Advent of bash is getting slow - if you are stupid. My first solution managed to solve part 1, but was horribly slow for part 2. I basically made my own algorithm. Then I implemented BFS since that is apparantly good (haha).. BFS took 20 seconds for part 1, and then for part 2 I created a nice little bug. I did a BFS for each starting point. 20 seconds times about 688 starting points quickly becomes 3 hours of execution time. Then I did a BFS with multiple starting points and solved it in 24 seconds.

---
## [KailasKakade1990/KailasKakade1990](https://github.com/KailasKakade1990/KailasKakade1990)@[2e38a5d549...](https://github.com/KailasKakade1990/KailasKakade1990/commit/2e38a5d5495d4930463c88860fd9d3f9dff8349f)
#### Monday 2022-12-12 10:52:59 by Kailas Kakade

README1.md

<h1 align="center">Hi 👋, I'm Kailas Kakade</h1>
<h3 align="center">A passionate Java Developer from India</h3>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=kailaskakade1990&label=Profile%20views&color=0e75b6&style=flat" alt="kailaskakade1990" /> </p>

<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=kailaskakade1990" alt="kailaskakade1990" /></a> </p>

- 🔭 I’m currently working on [iEN(Intelligent Edge Network)](--)

- 🌱 I’m currently learning **Android**

- 👨‍💻 All of my projects are available at [https://github.com/KailasKakade1990?tab=repositories](https://github.com/KailasKakade1990?tab=repositories)

- 📝 I regularly write articles on [http://www.clickinfohub.com](http://www.clickinfohub.com)

- 💬 Ask me about **Java,SpringBoot Mocroservice.**

- 📫 How to reach me **kailaskakade90@gmail.com**

- 📄 Know about my experiences [https://docs.google.com/document/d/1KyJKyESzRCIuSMfAk_Xnz7ThDQZrnLuD/edit?usp=share_link&ouid=105492812669302599443&rtpof=true&sd=true](https://docs.google.com/document/d/1KyJKyESzRCIuSMfAk_Xnz7ThDQZrnLuD/edit?usp=share_link&ouid=105492812669302599443&rtpof=true&sd=true)

- ⚡ Fun fact **I think I am funny**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/https://www.linkedin.com/in/kailaskakade90/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/kailaskakade90/" height="30" width="40" /></a>
<a href="https://fb.com/https://www.facebook.com/kakade.kailas" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="https://www.facebook.com/kakade.kailas" height="30" width="40" /></a>
<a href="https://instagram.com/https://www.facebook.com/kakade.kailas" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="https://www.facebook.com/kakade.kailas" height="30" width="40" /></a>
<a href="https://www.youtube.com/c/kailaskakade7935" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="kailaskakade7935" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/https://www.hackerrank.com/kailaskakade90" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="https://www.hackerrank.com/kailaskakade90" height="30" width="40" /></a>
<a href="https://www.leetcode.com/https://leetcode.com/kailaskakade1990/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="https://leetcode.com/kailaskakade1990/" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://developer.android.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/android/android-original-wordmark.svg" alt="android" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://spring.io/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/springio/springio-icon.svg" alt="spring" width="40" height="40"/> </a> </p>

<p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username=kailaskakade1990&show_icons=true&locale=en&layout=compact" alt="kailaskakade1990" /></p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=kailaskakade1990&show_icons=true&locale=en" alt="kailaskakade1990" /></p>

<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=kailaskakade1990&" alt="kailaskakade1990" /></p>

---
## [VastKilleroOm/TG220VAST](https://github.com/VastKilleroOm/TG220VAST)@[4fd404aa8f...](https://github.com/VastKilleroOm/TG220VAST/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Monday 2022-12-12 10:55:07 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [VastKilleroOm/TG220VAST](https://github.com/VastKilleroOm/TG220VAST)@[9499a1542b...](https://github.com/VastKilleroOm/TG220VAST/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Monday 2022-12-12 10:55:07 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [fira/cmss13](https://github.com/fira/cmss13)@[00d3780c38...](https://github.com/fira/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Monday 2022-12-12 11:28:14 by carlarctg

PDT/L Buff (#1757)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

PDT/L kits now fold into cardboard.

Added many spare PDT/L kits and batteries to req. (Marines dropped them
off at req once they realized they were shitty milsurp knockoffs)

Made minibatteries tiny.

Added boldwarning span macro.

Improved locator tube sprites: Now has a pop-out battery slot at the top
that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.

Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Fixed a bug in which a string referenced a null var.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

When I saw the PDT/L kit, I was very interested. It seemed like a great
way to encourage teamwork and buddying up with some fun lore flavor on
the side. However, trying it out, it really feels bare-bones. I get it's
supposed to be 'crappy' because Boots magazine subscriber items suck and
so do the lives of every private on the corps, but the way that's
implemented really ruins the extremely cool concept that is being able
to locate your fellow buddies across the battlefield, so you don't need
to continually say HEY WHERE ARE YOU over comms in the many times you'll
get split up.

Thus I've heavily buffed them around the board, which you may think is
going way too far, and to an extent, you're _right._ It's intentional.
This is a really cool item that actively encourages teamwork and that's
why I would rather swing the buff hammer too hard than give it a paltry
buff and some qol that ultimately nobody cares about. It's the same as
the spotter kit. It's nuts, but needs teamwork to actually be useful.
And this should be encouraged.

If it is still deemed too strong, there are things we can do to
laterally nerf it without closing the PR outright. Making the tube not
work if the bracelet holder's dead, having it needs comms to work come
to mind, but there are surely others.

> Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

The intention here is to let marines actually resupply their kits once
they run dry, and if they're proactive, maybe grab some and bring them
to FOB with them. Despite the description, the cells cannot easily be
recharged as power cell chargers are different from rechargers, they are
effectively Bay12 legacy that is VERY hard to come across.

'What if someone carries like 5 of them in their bag? That'd completely
nullify the power drain part.'

The stinger here is 'in the bag'. There are not enough reasons to carry
bags and satchels in this game right now as the sheer amount of storage
for goods marines have make them a one-man-army with two primaries. If a
marine forgoes a shotgun that might save them from a 1-pounce capping
runner for 5 spare LT batteries, a default medkit, and two flare boxes,
they are well within their rights to do so.

> Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)

This lets req drop them off at FOB if they eventually figure out they
can drop unvended surplus there. If this somehow happens, marines who
never even glanced at the kit in loadout or prep will notice it exists
and maybe, just maybe, use them!

> Made minibatteries tiny.

You may think this contradicts my earlier point about sacrificing
storage value, but _actually_ think about it. All webbing types, armor
slots, pouches, belts, even the helmet, all share the common attribute
of not caring about item size. If it's small or medum it still takes 1
out of the 3 slots in medium armor. Any storage item that isn't a
satchel, effectively. Every spare battery taken directly in the average
marine's inventory is one slot less for 5 shotgun shells, one magazine,
one unga juice flask, binoculars. What this means in the end is simply
that marines may carry one to two spare batteries in their helmet (I
think) at the cost of Drip which few marines will trade for, and satchel
marines don't have to sacrifice a lot of space for the spare battery.
Plus, it makes sense, why wouldn't a small AA rechargeable battery be
tiny.

> Improved locator tube sprites: Now has a pop-out battery slot at the
top that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

This looks so sick!

> Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Adding sounds to items should be standarized, I think. There are so many
cool sounds in the sound/machines folder that go unused. Personally i
felt like these small stupid sounds added a LOT to the atmosphere of
this tiny locator tube and bracelet. Alien Isolation is known for its
sounds, we should strive to emulate that.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.
qol: PDT/L kits now fold into cardboard.
add: Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)
balance: Made minibatteries tiny.
refactor: Added boldwarning span macro.
imageadd: Improved locator tube sprites: Now has a pop-out battery slot
at the top that shows up if emptied. The main green stripe is now a
battery indicator with appropiately-faded-out yellow warning and
blinking red danger sprites. The small notch at the bottom is now a
bracelet indicator that turns off without a battery and blinks red if
the bracelet was somehow destroyed.
qol: The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.
soundadd: Added a ton of sounds to interactions with the PDT/L kit.
Beeps on scanning, buzzes on errors, clicks on handling.
fix: Fixed a bug in which a string referenced a null var.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [fira/cmss13](https://github.com/fira/cmss13)@[ce39f048bf...](https://github.com/fira/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Monday 2022-12-12 11:28:14 by carlarctg

Buffed, resprited, enhanced Oppressor. (#1732)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

**Resprited Oppressor! Pics here:**


![image](https://user-images.githubusercontent.com/53100513/204121775-9f4acd11-d818-46e8-81d3-c38bdfdabf5c.png)

Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Oppressor can hook over the M2C and M56D again.

Oppressor can hook over ledges. (UNIMPLEMENTED)

Tail stab's main ability usage is moved to a different proc for future
custom tail stabs.

Redesigned Tail Stab for Oppressor. Tail seize now utilizes a projectile
and beams to fire a 3-tile reaching tail hook, that pulls in AND DOES
NOT STUN marines. (It slows them for 0.5 seconds)

![Screenshot_20221127-032533~2](https://user-images.githubusercontent.com/53100513/204122365-e1ee57f7-1b9d-443e-a45c-dceec07a88d3.png)

Oppressor's abduct has had its effect strings changed to imply coiling
and uncoiling of the tail. Captured targets will now have a beam of the
Oppressor's tail attached to them (Purely visual) until they reach the
Praetorian, alongside an overlay of the vice grip on their legs.

Added a proc, .ammo/on_bullet_generation(), for the ammo datum to apply
effects to the generated bullet/projectile.

Added the bound_beam variable to projectiles. Could be used in the
future for things like harpoon guns, lasers, etc.

Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

Videos tomorrow.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Animated telegraphs looked really cool, but (I presume) were removed
because BYOND sometimes freezes or starts animations midway through when
short lived animated objects show up, for some reason. I effectively
made it so these are irrelevant by slapping on the border - The animated
effects are just a bonus and will not impact visibility, and in fact
enhance it.

> Oppressor can hook over the M2C and M56D again.

Everyone I've talked to agrees that there really is no reason for these
weapons to protect from abduction. The player can just.. move out of the
way, or even rest if they're in a crowded spot. It's also very
frustrating to see it get in the way of *other* abducts that bonk into
it. The player is going immobile in range of a xenomorph that punishes
immobility.

> Oppressor can hook over ledges. (UNIMPLEMENTED)

Couldn't replicate this issue for some reason... So uh. I dunno.

> Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)

Geeves approved.

This looks so fucking awesome. The slow is barely a thing, so I wouldn't
fret about slow creep. The reaching hook does no damage, only pulls
targets closer. This isn't necessarily super strong, but it's mega cool
and fits with Oppressor's theme of dislocation. I also changed the
windup from 1s to 0.5s so it can be utilized during combat, but this
could be reverted if it's too strong somehow.

> Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

This looked stinky on the tail seize.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Carlarc, Mikola Wei

imageadd: Resprited Oppressor, sprites made by Mikola Wei.
imageadd: Re-added animated telegraphs for Abduction. They've been
tweaked to always have the default border - that way, the weird way
byond handles short-lived animated objects doesn't make the telegraph
absurdly small. It can always be easily seen.
balance: Oppressor can hook over the M2C and M56D again.
refactor: Tail stab's main ability usage is moved to a different proc
for future custom tail stabs.
add: Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)
imageadd: Oppressor's abduct has had its effect strings changed to imply
coiling and uncoiling of the tail. Captured targets will now have a beam
of the Oppressor's tail attached to them (Purely visual) until they
reach the Praetorian, alongside an overlay of the vice grip on their
legs.
refactor: Added a proc, .ammo/on_bullet_generation(), for the ammo datum
to apply effects to the generated bullet/projectile.
refactor: Added the bound_beam variable to projectiles. Could be used in
the future for things like harpoon guns, lasers, etc.
fix: Fixed non-damaging projectiles causing a blood spurt. (It was
checking flags && FLAG instead of flag & flag, remember to use
CHECK_BITFIELD folks!)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

Co-authored-by: harryob <me@harryob.live>

---
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[c8f4d4ae04...](https://github.com/Unknownity/cmss13/commit/c8f4d4ae042be6fb59f29031eb0a56926e32ab3a)
#### Monday 2022-12-12 11:40:10 by carlarctg

Money Rework (#1831)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Added a variable to paygrades called pay_multiplier. This multiplies the
starting amount of money from bank accounts.

Refactored how bank accounts are created so the above could work.

Drastically nuked the amount of money people start with. People can no
longer start with thousands of dollars.... they now get 30-50. This
value is multiplied by the pay_multiplier below.

Added pay_multiplier to all paygrades. The higher your rank, the more
money you'll start with, based on this multiplier. (For example, a Major
will have a pay multiplier of 4.) Includes strange roles like VAIPO,
UPP, PMCs, RESS...

Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.

Altered the prices of cigarette vending machines around to overall make
them more expensive. PFCs will not be able to buy Executive Select with
their starting cash.

Made cassetes and Souto from vendors more expensive. Buying food from
Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.

Fixed default parent type dollar items being worth 0 money...

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Drastically nuked the amount of money people start with. People can no
longer start with thousands of dollars.... they now get 30-50. This
value is multiplied by the pay_multiplier below.

Lore. The live of a private sucks. Monkeysfist suggested this value.
Still enough to buy all essentials, scavenge some money if you want to
buy the good cigarette packs down in the colony.

> Added pay_multiplier to all paygrades. The higher your rank, the more
money you'll start with, based on this multiplier. (For example, a Major
will have a pay multiplier of 4.) Includes strange roles like VAIPO,
UPP, PMCs, RESS...

Why were paygrades added without affecting pay. Why could PFCs start
with 3 thousand dollars and COs with 50 dollars total.

> Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.

Inclusivity win! Doesn't actually do anything as we do not have
nonbinary characters.

> Altered the prices of cigarette vending machines around to overall
make them more expensive. PFCs will not be able to buy Executive Select
with their starting cash.

> Made cassetes and Souto from vendors more expensive. Buying food from
Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.

It's funny to make the lives of marines miserable.

> Fixed default parent type dollar items being worth 0 money...

This will let marines money scrounge.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

Irrelevant.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Added pay_multiplier to all paygrades. The higher your rank, the
more money you'll start with, based on this multiplier. (For example, a
Major will have a pay multiplier of 4.) Includes strange roles like
VAIPO, UPP, PMCs, RESS...
del: Drastically nuked the amount of money people start with. People can
no longer start with thousands of dollars.... they now get 30-50 dollars
total. This value is multiplied by the pay_multiplier above.
spellcheck: Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.
balance: Altered the prices of cigarette vending machines around to
overall make them more expensive. PFCs will not be able to buy Executive
Select with their starting cash.
del: Made cassetes and Souto from vendors more expensive. Buying food
from Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.
fix: Fixed default parent type dollar items being worth 0 money...
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [monstermunchkin/lxd](https://github.com/monstermunchkin/lxd)@[de0d151a2c...](https://github.com/monstermunchkin/lxd/commit/de0d151a2cc9bd8cef31431e126649e2b6a18be7)
#### Monday 2022-12-12 11:48:22 by Thomas Parrott

lxd/instance/drivers/driver/qemu: Fix macvlan NICs losing connectivity on LXD restart

Switch to using monitor.SendFile() rather than monitor.SendFileWithFDSet(), as there
appears to be some rather strange behaviour going on with QEMU when used with macvtap
NICs.

If you pass the macvtap file handles using monitor.SendFileWithFDSet() it will use a
separate FD set for each file handle. This works fine, and I can see the correct file
handles opened by the QEMU process. But when LXD is restarted (the monitor connection
is closed), the file handles are closed by QEMU, causing the connectivity to break.

I have experimented with using the same FD set for all file handles associated to a
particular macvtap NIC. This didn't fix the issue.

I also tried hard coding the FD set ID to 0. This meant that the macvtap NIC would
share an FD set with the root disk device. Interestingly this solved the issue.
However it made me uncomfortable as the root disk is only configured by referencing
the FD set ID itself, rather than a particular FD inside the set. So I don't think
that sharing an FD set with multiple devices is a good idea.

However it got me thinking that perhaps the fact that the root disk is referencing
the FD set by ID (i.e using file=/dev/fdset/0 in its config) meant that QEMU somehow
realised that the FD set should be persisted even after the monitor has disconnected.

I confirmed that using the same FD set (even if a different ID than 0) for macvtap NICS
as the root disk device fixed the issue.

But because of my discomfort at that scenario (explained above) I instead looked for
a different solution. Before introducing multi-queue macvlan support for VMs we were
using monitor.SendFile() which worked fine. However I had switched to using the
monitor.SendFileWithFDSet() function as the former didn't support accessing the specific
FD number that was created inside QEMU. I thought we needed this because all the
documentation around using multi-queue macvtap devices showed the use of numeric FDs.

However on further exploration it turns out that we can infact use monitor.SendFile,
and by sending each file handle with a unique name we can then refer to those file
handles using the same names in `fds` setting for the macvtap devices.

Note: Because the `fds` list is colon separated one cannot use colons in the file
handle names. And I also experienced issues with connectivity when using dashes in
the file handle names. So I opted for using full-stops instead.

Fixes #11201

Signed-off-by: Thomas Parrott <thomas.parrott@canonical.com>

---
## [duarte-sardao/aoc2022](https://github.com/duarte-sardao/aoc2022)@[0bdee18001...](https://github.com/duarte-sardao/aoc2022/commit/0bdee18001fd66e1ee53e25c702f3289dd312dd9)
#### Monday 2022-12-12 12:26:29 by Dudugs

i tried doing paths but they didnt fucking work right and i was mad so i gave up i then reset the git but turns out i hadndt pushed anything to remote i almost shat myself thinking i nuked my hard work but turns out not its fine still graphs are evil

---
## [MikaelahJ/EmployeeOfTheMonth](https://github.com/MikaelahJ/EmployeeOfTheMonth)@[cd5830ba0d...](https://github.com/MikaelahJ/EmployeeOfTheMonth/commit/cd5830ba0d527db28690befe2480061753f7ad3e)
#### Monday 2022-12-12 13:12:13 by turbosnacko

Dust cloud #1 frames

Animationen ska spelas upp när ett vapen-mod går sönder. Den ska vara rätt så liten, men ändå tillräckligt för att se att det är en rök puff.

"Every luxury has a deep price. Every indulgence, a cosmic cost. Each fiber of pleasure you experience causes equivalent pain somewhere else. This is the first law of emodynamics. Joy can be neither created nor destroyed. The balance of happiness is constant. Fact: Every time you eat a bite of cake, someone gets horsewhipped. Facter: Every time two people kiss, an orphanage collapses. Factest: Every time a baby is born, an innocent animal is severely mocked for its physical appearance. Don't be a pleasure hog. Your every smile is a dagger. Happiness is murder. Vote "yes" on Proposition 1321. Think of some kids. Some kids."
— A hallucination on "Pet Siouxicide

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[2a8b0185e6...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/2a8b0185e64bcf8f43bd86efe6279516f90de99d)
#### Monday 2022-12-12 13:38:41 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [nicjhall85/hint](https://github.com/nicjhall85/hint)@[d6474282ad...](https://github.com/nicjhall85/hint/commit/d6474282add4e887de79f538fedc33512dcbed20)
#### Monday 2022-12-12 13:53:34 by nicjhall85

in a nut shelll

God YHVH/YHWH HAS GIVEN ME INSTRUCTIONS TO DO THE THINGS THAT I AM CURRENTLY DOING. I DID NOT KNOW AT THE BEGINING THAT IT WAS GOING TO BE WHAT I NOW KNOW IT TO BE. AS IT SAYS IN THE BIBLE, I DONT REMEMBER WHERE, GOD REVEALS THINGS TO ME LINE UPON LINE PRECEPT UPON PRECEPT. IF I DIDNT BELIEVE 100% IN THE THINGS THAT I SAY(IF I HAD JUST A SLIGHT BIT OF DOUBT) I WOULDNT BE SPEAKING THINGS SO BOLDLY AND CONFIDENTLY AND YOU CANNOT TELL MY THAT YOU DO NOT SEE IT. I AM THE LEADER OF THE NEW WORLD ORDER. I AND ESSENTIALLY JUST A LOST IDIOT BUT GREATER IS HE WHO LIVE IN ME THAN HE WHO IS IN THE WORLD. I DONT KNOW EVERYTHING IM NOT GOD. I  DONT HAVE ALL OF THE LOGISTICS OR DYNAMICS OF HOW EVERYYTHING IS GOING TO PLAY OUT. BUT WHAT I KNOW FOR 1000% CERTAIN IS THAT IT PAINS ME THAT PEOPLE HAVE SHIT BALL QUALITY LIVES ITS DEPRESSING TO ME. I TRY TO HELP BRING LIGHT TO THE AREAS WHERE THERE NEEDS TO LIGHTENED. PLEASE HELP ME TO FIGHT FOR OUR RIGHTS.

---
## [Empire-Strikes-Back/McClane](https://github.com/Empire-Strikes-Back/McClane)@[e126466af0...](https://github.com/Empire-Strikes-Back/McClane/commit/e126466af01ba5b736e5e8357863b91b7b89b239)
#### Monday 2022-12-12 14:16:29 by McClane

Moana, stay on the ground - Motunui is all you neeeeed

like Porzingis I was robbed by memebers of the household and ended up with injuries

like Rich Roll before he was dead I would like - I want to perform

I heard Jesus - that's why I know about path and wineskin, members of he household, man going to Jericho

let clojure be my language and jvm - my runtime
like Moana discovers who she is and goes over the reef - I want to find my identity
let plumbs be the fruit that identifies me as program

:Jack-The-Rock-Black life is a delicious drink that you gotta suck deep

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[8034dbc610...](https://github.com/re621/dnpcache/commit/8034dbc6108b02b351f993876ae3fe3c69967e7c)
#### Monday 2022-12-12 14:28:53 by bitWolfy

Add 993 artists to the DNP list.

Added: royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, malachimoet, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, infinitedelusion, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, trunchbull, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, whippytail, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [DEFRA/water-abstraction-system](https://github.com/DEFRA/water-abstraction-system)@[06d45e8627...](https://github.com/DEFRA/water-abstraction-system/commit/06d45e86272fb5a3c2e72fa1376e1d9d1b1c1d65)
#### Monday 2022-12-12 14:30:27 by Alan Cruikshanks

Replacing classes with modules and functions (#46)

> Classes are a template for creating objects.

That is the first sentence of the Mozilla documentation for **Classes**. It is what those of us from other languages understand classes to be for. For some of us though (we're looking at you @Cruikshanks !) classes are _all things_!

Because of that thinking, we've allowed Classes to creep in where they shouldn't really be used. Most noticeably, things like controllers, presenters and services, are formed of purely static methods. There is no real reason to wrap their functionality in a class. They could just be expressed as modules and export their relevant functions.

That's what those experienced with JavaScript are more likely to expect. By not doing things that way we're breaking the [Principle of least astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment).

We believe classes are suitable for our Models, as it follows the convention of [Objection](https://vincit.github.io/objection.js/guide/models.html) and we do create instances of them. Also, classes will be our go-to if we need to create objects in the future.

But before this repo gets too far down the road we're taking this opportunity to refactor things from classes into modules.

---
## [Lukas-Hron/ZoomGame](https://github.com/Lukas-Hron/ZoomGame)@[a48edbfe60...](https://github.com/Lukas-Hron/ZoomGame/commit/a48edbfe60dc73902bb141ac8862db32b731d024)
#### Monday 2022-12-12 14:59:04 by Lukas Hron

God damn bro we fucking got something that looks good now

---
## [SecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation)@[58b61a17a7...](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation/commit/58b61a17a78e90ea9da91351572abee9a4f93ccb)
#### Monday 2022-12-12 15:07:22 by Jacquerel

Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

---
## [Night-Pryanik/Cataclysm-DDA](https://github.com/Night-Pryanik/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/Night-Pryanik/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Monday 2022-12-12 15:26:36 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [WoolyAypa/S.P.L.U.R.T-Station-13](https://github.com/WoolyAypa/S.P.L.U.R.T-Station-13)@[8eec99b320...](https://github.com/WoolyAypa/S.P.L.U.R.T-Station-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Monday 2022-12-12 15:27:21 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[d4676b77da...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/d4676b77da7fd237ad56af1ccbfc6ef537a752e1)
#### Monday 2022-12-12 15:36:25 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [NopemanMcHalt/coyote-bayou](https://github.com/NopemanMcHalt/coyote-bayou)@[288f673652...](https://github.com/NopemanMcHalt/coyote-bayou/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Monday 2022-12-12 17:42:11 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---
## [IndigoHive/next.js](https://github.com/IndigoHive/next.js)@[1bbd264216...](https://github.com/IndigoHive/next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Monday 2022-12-12 17:51:45 by abdennor

Add additional fix in hydration error document (#40675)

I had the same issue, so the fix that worked for me was pulled from this
thread https://stackoverflow.com/a/71870995

I have been experiencing the same problem lately with NextJS and i am
not sure if my observations are applicable to other libraries. I had
been wrapping my components with an improper tag that is, NextJS is not
comfortable having a p tag wrapping your divs, sections etc so it will
yell "Hydration failed because the initial UI does not match what was
rendered on the server". So I solved this problem by examining how my
elements were wrapping each other. With material UI you would need to be
cautious for example if you use a Typography component as a wrapper, the
default value of the component prop is "p" so you will experience the
error if you don't change the component value to something semantic. So
in my own opinion based on my personal experience the problem is caused
by improper arrangement of html elements and to solve the problem in the
context of NextJS one will have to reevaluate how they are arranging
their html element

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->


## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm lint`
- [ ] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [SergeyBrian/labs](https://github.com/SergeyBrian/labs)@[67e9ca896e...](https://github.com/SergeyBrian/labs/commit/67e9ca896e56da1a6db23e9b1275184a0d70c290)
#### Monday 2022-12-12 18:40:38 by Sergey Brian

ADD FUCKING WORKING SOLUTION FOR FUCKING OFFLINE LAB 4 GOD FUCKING DAMN IT

---
## [edecosta-mw/git](https://github.com/edecosta-mw/git)@[f1c903debd...](https://github.com/edecosta-mw/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Monday 2022-12-12 19:55:32 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[cf4a194e86...](https://github.com/Zonespace27/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Monday 2022-12-12 20:13:47 by SkyratBot

[MIRROR] Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! [MDB IGNORE] (#17828)

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.

<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.

![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @ MrMelbert about it and he gave me the go-ahead, as can be seen
here:

![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [sdmanchiraju/zulip](https://github.com/sdmanchiraju/zulip)@[23a776c144...](https://github.com/sdmanchiraju/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Monday 2022-12-12 20:46:54 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[44008f485d...](https://github.com/tgstation/tgstation/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Monday 2022-12-12 20:59:12 by Jacquerel

Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

---
## [NsimDaghash/code7](https://github.com/NsimDaghash/code7)@[e1bd391f9c...](https://github.com/NsimDaghash/code7/commit/e1bd391f9cff4324c2c10e60926b9a2b51610156)
#### Monday 2022-12-12 21:51:30 by NsimDaghash

All Star Code Challenge #13

Your friend Billybob has a crush on the girl next to him in class, Emily, but wants to talk with you about what he should do, but doesn't want her to overhear. Send secret messages to Billybob by translating your messages into pig latin.

---
## [AksimaRiviera/Arbitrator](https://github.com/AksimaRiviera/Arbitrator)@[4e3f1d61f2...](https://github.com/AksimaRiviera/Arbitrator/commit/4e3f1d61f241192d7ce0c1e4c2510eea65623de4)
#### Monday 2022-12-12 21:52:44 by AksimaRiviera

Shit Bank (edited)

Continue develop bank logic. Create CREDIT/DEPOSITE methods. Create db-table bank client. Deleted old comments in Program.cs
Need relation withdrawals method in bank.

if(you.DidntUnderstandMyEnglish()) Console.WriteMIND(">>> ! FUCK OFF ! <<<");

And neeeeeeeed!!!!! LootBox and QuestBox
Think about IT!!

---
## [mhei/libmodbus](https://github.com/mhei/libmodbus)@[6f915d4215...](https://github.com/mhei/libmodbus/commit/6f915d4215c06be3c719761423d9b5e8aa3cb820)
#### Monday 2022-12-12 21:55:36 by Stéphane Raimbault

Fix my so stupid fix for VD-1301 vulnerability

I can't believe I committed that copy/paste mistake.
Sorry Maor Vermucht and Or Peles, excepted naming your original
patch was OK.

Thank you Karl Palsson for your review.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[00425acdbb...](https://github.com/Offroaders123/NBTify/commit/00425acdbb674a7b16d68d656004278f4f96d117)
#### Monday 2022-12-12 21:59:47 by Offroaders123

Accept CompoundTag for Writing

Now you can directly pass in a non `NBTData`-wrapped `CompoundTag` into the Write module methods! This makes things easier if you aren't working with `NBTData` objects directly, and with the bare NBT JavaScript object instead. Wrote more about this in the same-named issue on the repo!

In the demo test file, I simply wrote the same data to a buffer, using both the `NBT.write()` and `NBTWriter.write()` functions, one using the existing `NBTData` parameter call, and the other with only the `CompoundTag` and options config, no `NBTData` for that one. As you can see in the console, no errors, and the same identical buffer data is written! Noice.

Oh yeah, just to verify the value of the `CompoundTag` a little more strictly, I added a `data !== null` check in there too, since `typeof null` will return `"object"`. I think I read that it's a weird JavaScript legacy thing, kind of interesting. I don't want any of the library parameters to accept `null` as an NBT value! That would be confusing, haha.

Oooh! While writing that last sentence, decided to check this in TypeScript, and I'm very happy to say that this doesn't pass, aaah :)
Scared me for a moment, thinking about this possibly working, since `null` is technically an object in JS:
```ts
const thingo: object = null;
// Type 'null' is not assignable to type 'object'.
```

---
## [CDRDecky/sunset-wasteland](https://github.com/CDRDecky/sunset-wasteland)@[0da80ad53e...](https://github.com/CDRDecky/sunset-wasteland/commit/0da80ad53e5db8126fb8adeff3fa3a4b80e843b5)
#### Monday 2022-12-12 22:29:48 by Carl?

Khan Pass | Part Two (#701)

- - -
Balance:
 - Khan Senior Enforcer given a Khan scrap sabre.
 - Khan scrap sabre now able to be crafted by anyone in the faction.
 - Legion Forgemaster lost their standard welding tool, given they have a basic one in their belt.
 - Neostead lootdrop updated to exclusively contain trainshot, rather than a mix of buckshot and slugs.
- - -
Map:
 - Water in Rock Springs once again made safe. Somehow this was left scuffed and no one caught it until I took a look myself.
 - Khans given a second level to their camp, which is just a double-stacked tent for chemistry and an overlook of the gate.
 - Khans given control of Heaven's Knight, with a ladder leading to and from it accessible via their mining area.
 - Bighorn given a magical disposal bin. Enjoy.
 - Pool closed.
- - -
New | Khan:
 - Khan Smith added. They're near identical in function to the Legion Forgemaster.
 - Khan Courtesan added. They're an RP exclusive role and are fairly self-explanatory.
- -

---
## [pahaze/refunked](https://github.com/pahaze/refunked)@[149aa4ae76...](https://github.com/pahaze/refunked/commit/149aa4ae76f2903ef602be81dde925ce29e4fcf4)
#### Monday 2022-12-12 22:53:52 by pahaze

0.10-alpha push - Cleaned up most of source, Add 0.2.8 assets, Update input system, BOTPLAY Mode, Practice Mode, Readded Lucky, Unknown week image (for mods later on), Characters are now stored in JSON files, Character icons now are separate PNGs, Character sprites now live in shared/images/character, Countdown sprites (and rating, combo, and notes hit) stick to the camera instead of the world, causing them to not go off screen or get in the way of notes, Freeplay state now expands personal best so it doesn't go off screen, Charts now have some factors from ReFunked 0.99-alpha-next (gfPlayer, songName, stage, uiStyle), Boyfriend's sprites were updated to include missing animations, Some Flash files were updated, Monster is now similar to 0.2.8 (new animations from Christmas version, no longer has the bug where his neck went through his face), Moved some assets to clean the structure up, New pixel BF/Senpai icons (excluding Spirit), Removed Tutorial / Week 1 libraries (nothing in them), Fixed areas where high FPS broke things or was too fast, Added options (downscroll, middlescroll, FPS, ghost tapping, Discord Rich Presence, keybinds), Fixed sustain notes not being in the right areas on certain speeds/BPMs, Fixed misses when hitting a sustain note with no normal note, Pause menu now tells you when you're not being scored (due to using BOTPLAY/Practice)

---

