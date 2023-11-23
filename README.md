## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-22](docs/good-messages/2023/2023-11-22.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,671,713 were push events containing 3,989,216 commit messages that amount to 284,774,758 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 88 messages:


## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[b3f97b0115...](https://github.com/effigy-se/effigy-se/commit/b3f97b01152fa1427b848f0ca3b03ea6bd5b014d)
#### Wednesday 2023-11-22 00:05:03 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [Therandomhoboo/Hoboyogs](https://github.com/Therandomhoboo/Hoboyogs)@[bc3374c7da...](https://github.com/Therandomhoboo/Hoboyogs/commit/bc3374c7dacf3b2db39fe1c4dc36551d7ba82f79)
#### Wednesday 2023-11-22 00:20:11 by cowbot92

Even Further Heretic Adjustments: New minor things, Bug fixes, Heretic path adjustments and movement adjustments! (#20843)

* a whole lot of shit

yessir

* gun stuff

crazy

* haha

fuck guns

* my brain bursts

it hurts

* so much shit

im done

* fuck forgot this

god damn low memory mode

* removes backslashes

really linter

* oops

typos

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[3f7a9d4563...](https://github.com/TaleStation/TaleStation/commit/3f7a9d45637afe0e30abfe9481051aa12a0dd0ea)
#### Wednesday 2023-11-22 00:35:20 by TaleStationBot

[MIRROR] [MDB IGNORE] fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#8668)

Original PR: https://github.com/tgstation/tgstation/pull/79783
-----
This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---------

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6d57fcc3c9...](https://github.com/TaleStation/TaleStation/commit/6d57fcc3c98a969b81077ac4599ca87b8b06e904)
#### Wednesday 2023-11-22 00:37:31 by TaleStationBot

[MIRROR] [MDB IGNORE] Puts all traits in the globalvars file + CI Testing (#8680)

Original PR: https://github.com/tgstation/tgstation/pull/79642
-----
## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[227b6c32f6...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/227b6c32f62bd5c690dff60166bc581b9908e2c4)
#### Wednesday 2023-11-22 01:03:08 by SpartanKadence

Jukebox Repair (#6091)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
The links within the songs have been repaired and replaced, along with
some having tweaks to their playtimes and titles. Every song, at the
time of testing, is now playable.

List of Repaired Songs:
Alternative:
All That Could Ever Be, By Rik Schaffer
Angel (Massive Attack), by Massive Attack
Blue Monday, by New Order
Breakeven, by The Script
Ceremony, by New Order
Edge by Michal Michalski
Feel Good Inc by Gorillaz
Psycho Killer by Talking Heads
Saturnz Barz by Gorillaz

Arcade:
Also Sprach Brooks by Shoji Meguro
Dessert by Jun Chikuma
Exosuit by Simon Chylinski
Secunda by Jeremy Soule
E1M1 - At Doom's Gate by Robert Prince 

Classical and Orchestral:
A Night on Bald Mountain by Modest Mussorgsky
Dance of the Sugar Plum Fairy by Pyotr Ilyich Tchaikovsky
Handel This by Andreas Waldetoft
Lohengrin: Prelude by Richard Wagner

Country and Western:
The Devil Went Down to Georgia by The Charlie Daniels Band
Whiskey Glasses by Morgan Wallen

Disco, Funk, Soul, and R&B:
He's the Greatest Dancer by Sister Sledge
It's Only Love Doing Its Thing by Barry White
Space Cowboy by Jamiroquai

Electronic:
Cheerleader Effect by Carpenter Brut
Dead Man's Hand by Simon Viklund
Dust by M|O|O|N
Escape From Midwich Valley by Carpenter Brut
Get Lucky by Daft Punk
Harder, Better, Faster, Stronger by Daft Punk
Head First by HOME
Imagine by System96
Inferno Galore by Carpenter Brut
Inner Animal by Scattle
Into The Labyrinth by Kraddy
Miami Disco by Perturbator
Morningstar by Mittsies
Phoron Will Make Us Rich by Earthcrusher
Pjanoo (Club Mix) by Eric Prydz
Reef by Euan Ellis
River of Darkness by The Midnight (feat. Timecop1983)
Robocop Theme (Title Two) by Cboyardee
Wayfarer by Kavinsky
Wow Wow by Neil Cicierega 
Filthy Rich by Young Scrolls

Folk and Indie:
Apocalypse by Cigarettes After Sex
New Sins for Old by Leslie Fish
Pioneer's Song by Leslie Fish
Spaceman's Dilemma by Leslie Fish

Hip Hop and Rap:
Gettin' Jiggy Wit It by Will Smith
Intergalactic by Beastie Boys
It Was a Good Day by Ice Cube
Rapper's Delight by The Sugar Hill Gang
Super Freak by Rick James
Take_it_Back_v2 by Denzel Curry & Kenny Beats
Takyon (Death Yon) by Death Grips


Jazz and Lounge:
A Kiss to Build a Dream On by Louis Armstrong
Flip-Flap (Title One) by X-CEED
Signin' 'Em by John Sangster
That Man by Caro Emerald
Why Don't You Do Right? by Amy Irving
Begin Again by Vera Keyes 


Metal:
Ace of Spades by Motorhead
BFG Division by Mick Gordon
Kickstart my Heart by Motley Crue
On The Wind by Dream Evil
Peace Sells by Megadeth
Rise Of The Chaos Wizards by Gloryhammer
Same Ol' Situation (S.O.S.) by Motely Crue
Shout At The Devil by Motley Crue
Superbeast by Rob Zombie
The Hellion / Electric Eye by Judas Priest
The Trooper by Iron Maiden

Pop:
Everything She Wants by Wham!
Head Over Heels by Tears For Fears
I Swear by All-4-One
Life’s What You Make It by Talk Talk 
Tell Her About It by Billy Joel

Rock:
Armageddon by Alkaline Trio
Break The Rules by Simon Viklund
Changes by David Bowie
Chippin' In 2022 by Kerry Eurodyne
Do It Again by Steely Dan
Doubleback by ZZ Top
Everlong by Foo Fighters
Every Little Thing She Does Is Magic by The Police
Every Rose Has It's Thorn by Poison
Fortunate Son by Creedence Clearwater Revival
If Only by Queens of the Stone Age
Kid Dynamo by The Buggles
Miles Away by Winger
Misery Business by Paramore
No One Loves Me & Neither Do I by Them Crooked Vultures
Photograph by Def Leppard
Piano Man by Billy Joel
Rock This Town by Stray Cats
Take Me Home Tonight by Eddie Money
The Boys Are Back In Town by Thin Lizzy
The Power Of Love by Huey Lewis & The News
Today by The Smashing Pumpkins

Sol Common Precursors:
INTERNET OVERDOSE by Aiobahn feat. KOTOKO
Living on the Ceiling by Blancmange
Mama Loi, Papa Loi by Exuma
Ikouze Paradise by Junji Majima (Emagged Song)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

A lot of the songs were nonfunctional and wouldn't play at all, due to
the broken links, now all the songs in the jukebox can be enjoyed by
players.
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
fix: Jukebox's song list has been repaired, all songs should be playable
now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[fb9c40f675...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/fb9c40f6752f19e293da244c45e48dabb9236320)
#### Wednesday 2023-11-22 01:03:08 by SpartanKadence

Jukebox Update (#6102)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This will add plenty of more songs to the Jukebox.

Song List:
Alternative:
Say It Ain’t So by Weezer
Buddy Holly by Weezer
The Good Life by Weezer
Troublemaker by Weezer
Undone by Weezer
Hash Pipe by Weezer (All Emagged)
Wayside by Mitchel Dae
Freaking Out the Neighborhood by Mac DeMarco

Arcade:
Skyline and Menagerie Mix by 63hnsh3
Deputized by Locknar
The Ashoka Attacks by Paul Ruskay

Electronic:
How Would You Like It? By Moxifloxi
Syrsa - Cythas - Magichnology
Beyond Memory by NINA

Jazz and Lounge:
People Equals Shit by Richard Cheese (Emagged)

Metal:
Alone I Break by Korn
Shoots and Ladders by Korn
Blind by Korn
A Different World by Korn ft. Corey Taylor
Kidnap the Sandy Claws by Korn (Emagged)
Before I Forget by Slipknot
Psychosocial by Slipknot
The Devil in I by Slipknot
Dead Memories by Slipknot
People Equals Shit by Slipknot
Fade Away by Breaking Benjamin
Give me a Sign by Breaking Benjamin
I Will Not Bow by Breaking Benjamin
Into the Nothing by Breaking Benjamin
Without You by Breaking Benjamin
Smooth Criminal by Alien Ant Farm
Movies by Alien Ant Farm
Happy Death Day by Alien Ant Farm
Violent Pornnography by System of a Down
Science by System of a Down
Spiders by System of a Down
Jet Pilot by System of a Down
Chic ‘n’ Stu by System of a Down
Chop Suey! by System of a Down
B.Y.O.B. by System of a Down
Last Resort by Papa Roach
Scars by Papa Roach
Words as Weapons by Seether
Crawling by Linkin Park
Leave Out All the Rest by Linkin Park
Papercut by Linkin Park
Lost by Linkin Park
In The End by Linkin Park
Bodies by Drowning Pool
Tear Away by Drowning Pool
I Don't Care by Apocalyptica ft. Adam Gontier
One by Metallica
Sad But True by Metallica
Wherever I May Roam by Metallica
Nothing Else Matters by Metallica
Master of Puppets by Metallica
Tenebre Rosso Sangue by Keygen Church (Emagged)
Simple Sight by Piercing Lazer (Emagged)
Order by Heaven Pierce Her (Emagged)

Classical and Orchestral:
One Final Effort by Martin O’Donnell
Never Forget by Martin O’Donnell

Rock:
8675309 Jenny Jenny by Tommy Tutone
I Love You Like An Alcoholic by The Taxpayers
Must Have Been The Wind by The Chalkeaters (Emagged)

_Yes, this list is very biased._
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

With the recent repair of the previous songs in the Jukebox, it would
seem to be a good idea to finally add more to the list, allowing for
more songs for players to choose from.


<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Added more songs to the Jukebox!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [temporalio/temporal](https://github.com/temporalio/temporal)@[1be76e3583...](https://github.com/temporalio/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Wednesday 2023-11-22 01:12:38 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[2a74c23d62...](https://github.com/thgvr/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Wednesday 2023-11-22 01:14:53 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[bf4671ff83...](https://github.com/thgvr/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Wednesday 2023-11-22 01:14:53 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [jcsirot/dagger](https://github.com/jcsirot/dagger)@[80180aaaed...](https://github.com/jcsirot/dagger/commit/80180aaaed1e1e91a13dbf7df7e0411a9a54c7d3)
#### Wednesday 2023-11-22 01:17:29 by Justin Chadwell

Fix secret scrubbing log latency (#6034)

* fix: use custom implementation for secret scrubbing

This was a fun exercise in processing streams in go, and an absolutely
massive nerd-snipe :(

Essentially, we need a custom transformer to handle *precisely* matching
Reads on the underlying source with the output - we shouldn't hold
output any longer than is absolutely neccessary.

To be able to do this at all in any reasonable way, we need a trie, and
handle *all* the secrets at once, instead of doing multiple passes.
Multiple passes won't work, since it's possible to accidentally trim too
much at each step, which would be very sad.

> e.g. imagine secrets (aaa, bbb, ccc, etc), and an input (cba)
>
> In removing secret aaa, we would trim to cb, then we'd remove bbb to
> trim to c, then finally trim to nothing. However, this is overly
> enthusiastic, we could easily just trim to cb, if we knew about all
> the secrets at once.

So, we need a trie, and we need a custom implementation of one. This is
because *no off the shelf implementation* seems to allow traversing the
trie state-by-state. Thankfully, it's a pretty short implementation to
implement one from scratch, and not too much harder to turn it into a
radix tree (which lets us use quite a lot less memory).

With our trie, we can implement our custom transformer, which is *an
utter pain*. Honestly, the comments should explain all the fun edge
cases it's possible to hit. There's a lot of tests added as well, each
of which was a real horrible thing I hit while implementing it.

I played around a bit with benchmarking, but ugh, it's a *tiny* bit
slower than the original implementation (maybe by like ~25%?). It's not
huge, but the latency problem is *actually solved*. Some potential
things I did look into and gave up on:
- Only copy into dstBuf when dst is full (requires tons of extra
conditionals, so slows everything down).
- Avoid copies at all costs by having "virtual buffer pointers" into
src, that indicate future data to copy (not only is this *slower*, the
logic becomes truly incomprehensible).
- Playing with off-the-shelf radix tree implementations, but they're so
inconvenient to use for this specific use case, it'd be way more
trouble than it'd be worth.

Any ideas welcome, but honestly, I've looked at enough flamegraphs
today.

Signed-off-by: Justin Chadwell <me@jedevc.com>

* test: avoid use of require.Eventually for secret scrubbing

Signed-off-by: Justin Chadwell <me@jedevc.com>

---------

Signed-off-by: Justin Chadwell <me@jedevc.com>

---
## [utziacre/android_kernel_oneplus_sm8250](https://github.com/utziacre/android_kernel_oneplus_sm8250)@[3731472fe8...](https://github.com/utziacre/android_kernel_oneplus_sm8250/commit/3731472fe8047b30d1e2837c97be56cda8316e4d)
#### Wednesday 2023-11-22 02:17:59 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [CharlyMaye/angular](https://github.com/CharlyMaye/angular)@[acd59ad037...](https://github.com/CharlyMaye/angular/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Wednesday 2023-11-22 02:28:54 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

PR Close #51516

---
## [ericwooshem/7641-FtcRobotController](https://github.com/ericwooshem/7641-FtcRobotController)@[4e744ef7af...](https://github.com/ericwooshem/7641-FtcRobotController/commit/4e744ef7afcdcb385380afaf1b0b6c0d65d1ce34)
#### Wednesday 2023-11-22 02:48:54 by Eric Woo-Shem

if i broke drive im sorry but I can undo easily so don't worry, its just my attempt to appease the drivers and make a p loop on teloeop and I really want to know how long of a name I can put here so yeah anyways it might work it might not and I hope it does. thank you for reading this, if you did you have incredible patience because why would you bother reading a really long commit summary and seriously why am I writing such a long one too i don't know what I am doing with my time but okay im done thats all goodbye

---
## [edenlewis/Parent-Connect](https://github.com/edenlewis/Parent-Connect)@[8af1f77e34...](https://github.com/edenlewis/Parent-Connect/commit/8af1f77e34555106c3484de793dffba2a059ee8d)
#### Wednesday 2023-11-22 02:51:15 by uraniumrainbow

Delete server/node_modules directory

Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.

There now is your insular city of the Manhattoes, belted round by wharves as Indian isles by coral reefs—commerce surrounds it with her surf. Right and left, the streets take you waterward. Its extreme downtown is the battery, where that noble mole is washed by waves, and cooled by breezes, which a few hours previous were out of sight of land. Look at the crowds of water-gazers there.

Circumambulate the city of a dreamy Sabbath afternoon. Go from Corlears Hook to Coenties Slip, and from thence, by Whitehall, northward. What do you see?—Posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries. Some leaning against the spiles; some seated upon the pier-heads; some looking over the bulwarks of ships from China; some high aloft in the rigging, as if striving to get a still better seaward peep. But these are all landsmen; of week days pent up in lath and plaster—tied to counters, nailed to benches, clinched to desks. How then is this? Are the green fields gone? What do they here?

But look! here come more crowds, pacing straight for the water, and seemingly bound for a dive. Strange! Nothing will content them but the extremest limit of the land; loitering under the shady lee of yonder warehouses will not suffice. No. They must get just as nigh the water as they possibly can without falling in. And there they stand—miles of them—leagues. Inlanders all, they come from lanes and alleys, streets and avenues—north, east, south, and west. Yet here they all unite. Tell me, does the magnetic virtue of the needles of the compasses of all those ships attract them thither?

Once more. Say you are in the country; in some high land of lakes. Take almost any path you please, and ten to one it carries you down in a dale, and leaves you there by a pool in the stream. There is magic in it. Let the most absent-minded of men be plunged in his deepest reveries—stand that man on his legs, set his feet a-going, and he will infallibly lead you to water, if water there be in all that region. Should you ever be athirst in the great American desert, try this experiment, if your caravan happen to be supplied with a metaphysical professor. Yes, as every one knows, meditation and water are wedded for ever.

But here is an artist. He desires to paint you the dreamiest, shadiest, quietest, most enchanting bit of romantic landscape in all the valley of the Saco. What is the chief element he employs? There stand his trees, each with a hollow trunk, as if a hermit and a crucifix were within; and here sleeps his meadow, and there sleep his cattle; and up from yonder cottage goes a sleepy smoke. Deep into distant woodlands winds a mazy way, reaching to overlapping spurs of mountains bathed in their hill-side blue. But though the picture lies thus tranced, and though this pine-tree shakes down its sighs like leaves upon this shepherd’s head, yet all were vain, unless the shepherd’s eye were fixed upon the magic stream before him. Go visit the Prairies in June, when for scores on scores of miles you wade knee-deep among Tiger-lilies—what is the one charm wanting?—Water—there is not a drop of water there! Were Niagara but a cataract of sand, would you travel your thousand miles to see it? Why did the poor poet of Tennessee, upon suddenly receiving two handfuls of silver, deliberate whether to buy him a coat, which he sadly needed, or invest his money in a pedestrian trip to Rockaway Beach? Why is almost every robust healthy boy with a robust healthy soul in him, at some time or other crazy to go to sea? Why upon your first voyage as a passenger, did you yourself feel such a mystical vibration, when first told that you and your ship were now out of sight of land? Why did the old Persians hold the sea holy? Why did the Greeks give it a separate deity, and own brother of Jove? Surely all this is not without meaning. And still deeper the meaning of that story of Narcissus, who because he could not grasp the tormenting, mild image he saw in the fountain, plunged into it and was drowned. But that same image, we ourselves see in all rivers and oceans. It is the image of the ungraspable phantom of life; and this is the key to it all.

---
## [lizardqueenlexi/Shiptest](https://github.com/lizardqueenlexi/Shiptest)@[b22529fc74...](https://github.com/lizardqueenlexi/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Wednesday 2023-11-22 03:00:01 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [janepyz/app-dev](https://github.com/janepyz/app-dev)@[3821556dd7...](https://github.com/janepyz/app-dev/commit/3821556dd70e8420f4f545adad058ca8ecc9eec0)
#### Wednesday 2023-11-22 03:03:39 by janepyz

Update README.md

The movie is about the 1912 sinking of the RMS Titanic. It stars Kate Winslet and Leonardo DiCaprio. The two play characters who are of different social classes. They fall in love after meeting aboard the ship, but it was not good for a rich girl to fall in love with a poor boy in 1912.

---
## [brightly-salty/ripgrep](https://github.com/brightly-salty/ripgrep)@[082245dadb...](https://github.com/brightly-salty/ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Wednesday 2023-11-22 03:21:26 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [Kealing-CS/Kealing-CS-Curriculum](https://github.com/Kealing-CS/Kealing-CS-Curriculum)@[fbeb5cc827...](https://github.com/Kealing-CS/Kealing-CS-Curriculum/commit/fbeb5cc8271045ff00c128b31c9eb0d2f0132d88)
#### Wednesday 2023-11-22 03:23:32 by Ianyourgod

basic editor shit
the look will be changed later, its kinda ugly. (the layout, not the colors)

---
## [NoTerrainTires/space](https://github.com/NoTerrainTires/space)@[492ed90f28...](https://github.com/NoTerrainTires/space/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Wednesday 2023-11-22 03:48:13 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [mgarlanger/mame](https://github.com/mgarlanger/mame)@[96ab505d66...](https://github.com/mgarlanger/mame/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Wednesday 2023-11-22 04:00:34 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[a124ad04c1...](https://github.com/effigy-se/effigy-se/commit/a124ad04c1c5e8d551b187b24e5a04eeea21aeba)
#### Wednesday 2023-11-22 04:31:58 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [AnuravModak/pennylane](https://github.com/AnuravModak/pennylane)@[47e74e16d0...](https://github.com/AnuravModak/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Wednesday 2023-11-22 04:47:12 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [xallard/ai-market-research-and-sustainability-analytics](https://github.com/xallard/ai-market-research-and-sustainability-analytics)@[98b921bf46...](https://github.com/xallard/ai-market-research-and-sustainability-analytics/commit/98b921bf468fd390c58a3a8df7f12011f4c905ab)
#### Wednesday 2023-11-22 05:36:14 by Christian Ipanaque

[enhancement] add behavior predictor (#3)

🔮 Predicting the Future, One Commit at a Time!

Hey Team,

I've just pushed the future into our repo, quite literally! Introducing
our brand-new Behavior Predictor - because why wait for users to
surprise us when we can surprise them with our clairvoyance?

This shiny new feature is like a crystal ball but with more algorithms
and fewer mystical vibes. It's designed to guess what our users will do
next, hopefully with more accuracy than my attempts to predict lottery
numbers.

Before you ask – no, it can't predict when we'll go back to the office
or what's for lunch tomorrow, but it sure will add some wizardry to our
user experience!

So, let's merge this and stay one step ahead, or at least pretend to be!

Cheers,
Christian

P.S. If this thing predicts the end of the world, let's agree to keep it
hush-hush. We're developers, not meteorologists! 🌎💫

---
## [titaiwangms/pytorch](https://github.com/titaiwangms/pytorch)@[a911b4db9d...](https://github.com/titaiwangms/pytorch/commit/a911b4db9d82238a1d423e2b4c0a3d700217f0c1)
#### Wednesday 2023-11-22 06:27:00 by voznesenskym

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang
ghstack dependencies: #113926

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[7fce8cd805...](https://github.com/LemonInTheDark/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Wednesday 2023-11-22 06:36:30 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[9c8c29ae69...](https://github.com/treckstar/yolo-octo-hipster/commit/9c8c29ae69b387599620abb8ced84436c2656ebf)
#### Wednesday 2023-11-22 07:22:06 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[4d4aa72e33...](https://github.com/shiptest-ss13/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Wednesday 2023-11-22 07:29:13 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[223dc74ef1...](https://github.com/thgvr/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Wednesday 2023-11-22 07:43:57 by retlaw34

Eoehoma Firearms (& friends) (#2315)

## About The Pull Request


![Screenshot_5451](https://github.com/shiptest-ss13/Shiptest/assets/58402542/08f9b0ee-15db-4091-a974-6d887cd85259)

Holy shit, this should not have taken a year to make

Adds the E-10, E-11, E-40, E-50, and E-60 to the game. Weapons
manufactured by defunct firearms company Eoehoma Firearms.

Founded in 77 FS, Eoehoma was a early pioneer of ‘hybrid’ Solarian and
Kalixcian laser weapons. The company went bankrupt due to increasingly
poor and risky decision making, and all of it's patents were bought out
by Nanotrasen. While Nanotrasen's Emitters bear a striking resemblance
to the E-50, otherwise Nanotrasen has not produced any of Eoehoma's old
weapons, instead focusing on Sharplite designed weapons.

Other changes:
- NT and Sharplite weapons have different fire sounds from each other
- Laser weapons buffed to 20 -> 25 damage
- Pulse shots don't destroy walls and are now 50 -> 40 damage
- Emitter shots now do 30 -> 60 damage
- Various grammar fixes
- Removes some non-lore compliant mentions
- Adds a manufacturer indicator to many guns
- Ports https://github.com/tgstation/tgstation/pull/60353
- Resprites various laser weaponry, notably the pulse guns.
- Deathsquad and ERT/LP hardsuits have been redone

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/c5df7029-95da-4041-b8b1-e4cfd35436dd)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/f72a3672-e996-4fdd-a68d-4553655f1a0c)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/7bd2dc53-ab29-49e8-8f90-87d4c72583f9)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/4bdc6493-4c94-49d0-995b-2a450d738211)
ceredits to tetrazeta for the unfinished deathsquad sprite, i simply
finished it and touched it up

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/517b72e3-c72b-4875-a6fb-84c017105908)

One of the last things i remember the old leads planned was to buff
lasers to make them stand up to the various ballistics better. Also
allows Pulse Rifles to be more used in events by nerfing them to not be
comedically overpowered. Now they are just Overpowered.

More ruin content and such. I'm sure the maptainers will make good use
of this stuff.

And sprites, i fucking love sprites

## Changelog

:cl: retlaw34, tetrazeta
add: Eoehoma Firearms, a new guns manufacturer!
add: ERT and "Asset Protection" Hardsuits have gotten a new look!
add: New laser fire sounds

balance: Lasers now do slightly more damage
balance: Pulse rifles don't destroy walls anymore and do slightly less
damage, and have lost their stun mode.
balance: Emitters do 60 damage and create turf fires on hitting a
non-supermatter object.
fix: Various laser weapons that had broken autofire (E-TAR and the Tesla
Cannon) now work

spellcheck: Grammar on some descriptions was corrected.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: retlaw34 <58402542+retlaw34@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[389d1e5669...](https://github.com/thgvr/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Wednesday 2023-11-22 07:43:57 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are: 
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[88e683cec6...](https://github.com/thgvr/Shiptest/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Wednesday 2023-11-22 07:43:57 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR is made so I can stop getting angry at the ruins beyond saving
that are still ingame. My criteria for a ruin being removed is if
another ruin already does its niche better, if the ruin is outdated
and/or the ruin is excessively small or unbalanced. For ruins that dont
meet this criteria but are still outdated, they will be getting balance
fixes and touch ups or a total remap.

This PR is a draft for now because I will need to update the PR
changelog and description as I make changes and communicate with the
maptainers on what stays and what goes.

Adds departmental RND lootdrop spawners for circuit imprinters,
protolathes and techfabs. Excludes omnisci and basic boards from the
drops.
Fixed a space tile under a door and replaced the omnilathe with a
medical lathe on dangerousresearch
Fixed the whitesands saloon not spawning which may have caused some
sandplanets to spawn without a ruin
Fixed harmfactory's nonfunctional traps to now be as lethal as intended.
Also changed the loot in the vault to better reflect the ruin's theme
and difficulty (cargo techfab board instead of omnilathe, adv plasma
cutter instead of combat medkit, less gold more cash, kept the cyberarm
implant).
Fixed provinggrounds magical SMES FINALLY by adding a terminal on the
back. The map should finally function as intended.
Fixed a few dirs on fire extinguisher cabinets and blast door assemblies
in singularity_lab
Removed mechtransport.dmm for being small and bad
Removed some leftover gasthelizards.dmm cruft (VILE)
Removed nucleardump for being an utter mess of an oldcode ruin
Removed gondolaasteroid for being large and empty besides gondolas.
better suited for a jungle planet IMO.
Removed Jungle_Spider. Literally just a box with spiders and cloning
equipment. Small, bad, hard to find, unjustified loot.
Removed Golem_Hijack. Like jungle spider but it was free rnd, an AI
core, a full BSRPED and three golem corpses. With no enemies or
obstacles.
Removed rockplanet_clock for being a tiny lootbox that doesnt fit with
the lore. Also had a quantumn pad.
Removed whitesands_surface_youreinsane. Its a silly little reference to
an old event that unfortunately resulted in a subpar ruin. Could return
as a wasteplanet greeble ruin, but it has to go for now.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: departmental RND lootdrop spawners for imprinters, protolathes and
techfabs
fix: dangerous_research.dmm now no longer has a space tile under a door
and a medical lathe instead of an omnilathe
fix: whitesands_surface_camp_saloon can now spawn again after its remap
into a functional ruin
fix: harmfactory.dmm's traps now work and loot has been adjusted to fit
the ruin better
fix: provinggrounds.dmm now has a working SMES and power
fix: singularity_lab fire extinguishers and a few poddoors now have
correct dirs
del: mechtransport.dmm and associated code
del: gasthelizards areas
del: nucleardump.dmm and associated code
del: gondolaasteroid.dmm and associated code
del: jungle_spider.dmm and associated code
del: whitesands_golem_hijack.dmm and associated code
del: rockplanet_clock.dmm and associated code
del: whitesands_surface_youreinsane.dmm and associated code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>

---
## [wonderinghost/Yogstation](https://github.com/wonderinghost/Yogstation)@[f39d74c3a6...](https://github.com/wonderinghost/Yogstation/commit/f39d74c3a66c41a5ebb468dc3d61b0787f8327be)
#### Wednesday 2023-11-22 07:44:24 by Waterpig

Invisible touch - this time for real (#20742)

* This was surprisingly easy

* Well this might be funny

* Hm

* Oh boy it's working

* I might be going insane

* Checks moved

---
## [FBI-tool/thefuck](https://github.com/FBI-tool/thefuck)@[7f97818663...](https://github.com/FBI-tool/thefuck/commit/7f97818663de9351ac7e2c6314ed94184811d62a)
#### Wednesday 2023-11-22 08:11:16 by Romain Heller

#455: [README] Add uninstall instructions (#1171)

* ~[Doc] Add Uninstall instructions

As we need the package and to modify the shell config, users could have a pain in the ass when it comes to retire *The Fuck* from the system.

* Update README.md

* Update README.md

Co-authored-by: Pablo Aguiar <scorphus@gmail.com>

---
## [vibhatha/arrow](https://github.com/vibhatha/arrow)@[3beb93af36...](https://github.com/vibhatha/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Wednesday 2023-11-22 08:30:22 by Kevin Gurney

GH-37815: [MATLAB] Add `arrow.array.ListArray` MATLAB class (#38357)

### Rationale for this change

Now that many of the commonly-used "primitive" array types have been added to the MATLAB interface, we can implement an `arrow.array.ListArray` class.

This pull request adds a new `arrow.array.ListArray` class which can be converted to a MATLAB `cell` array by calling the static `toMATLAB` method.

### What changes are included in this PR?

1. Added a new `arrow.array.ListArray` MATLAB class.

*Methods*

`cellArray = arrow.array.ListArray.toMATLAB()`
`listArray = arrow.array.ListArray.fromArrays(offsets, values)`

*Properties*

`Offsets` - `Int32Array` list offsets (uses zero-based indexing)
`Values` - Array of values in the list (supports nesting)

2. Added a new `arrow.type.traits.ListTraits` MATLAB class.

**Example**
```matlab
>> offsets = arrow.array(int32([0, 2, 3, 7]))

offsets = 

[
  0,
  2,
  3,
  7
]

>> values = arrow.array(["A", "B", "C", "D", "E", "F", "G"])

values = 

[
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G"
]

>> arrowArray = arrow.array.ListArray.fromArrays(offsets, values)

arrowArray = 

[
  [
    "A",
    "B"
  ],
  [
    "C"
  ],
  [
    "D",
    "E",
    "F",
    "G"
  ]
]

>> matlabArray = arrowArray.toMATLAB()

matlabArray =

  3x1 cell array

    {2x1 string}
    {["C"     ]}
    {4x1 string}

>> matlabArray{:}

ans = 

  2x1 string array

    "A"
    "B"

ans = 

    "C"

ans = 

  4x1 string array

    "D"
    "E"
    "F"
    "G"

```

### Are these changes tested?

Yes.

1. Added a new `tListArray.m` test class.
2. Added a new `tListTraits.m` test class.
3. Updated `arrow.internal.test.tabular.createAllSupportedArrayTypes` to include `ListArray`.

### Are there any user-facing changes?

Yes.

1. Users can now create an `arrow.array.ListArray` from an `offsets` and `values` array by calling the static `arrow.array.ListArray.fromArrays(offsets, values)` method. `ListArray`s can be converted into MATLAB `cell` arrays by calling the static `arrow.array.ListArray.toMATLAB` method.

### Notes

1. We chose to use the "missing-class" `missing` value as the `NullSubstitutionValue` for the time being for `ListArray`. However, we eventually want to add `arrow.array.NullArray`, and will most likely want to use the "missing-class" `missing` value to represent `NullArray` values in MATLAB. So, this could cause some ambiguity in the future. We have been thinking about whether we should consider introducing some sort of special "sentinel value" to represent null values when converting to MATLAB `cell` arrays. Perhaps, something like `arrow.Null`, or something to that effect, in order to avoid this ambiguity. If we think it makes sense to do that, we may want to retroactively change the `NullSubstitutionValue` to be `arrow.Null` and break compatibility. Since we are still in pre-`0.1`, we don't think the impact of such a behavior change would be very large.
2. Implementing `ListArray` is fairly involved. So, in the spirit of incremental delivery, we chose not to include an implementation of `arrow.array.ListArray.fromMATLAB` in this initial pull request. We plan on following up with some more changes to `arrow.array.ListArray`. See #38353, #38354, and #38361.
3. Thank you @ sgilmore10 for your help with this pull request!

### Future Directions

1. #38353
2. #38354
3. #38361
4. Consider adding a null sentinel value like `arrow.Null` for conversion to MATLAB `cell` arrays.
* Closes: #37815 

Lead-authored-by: Kevin Gurney <kgurney@mathworks.com>
Co-authored-by: Sarah Gilmore <sgilmore@mathworks.com>
Signed-off-by: Kevin Gurney <kgurney@mathworks.com>

---
## [AmanBharti07/Social-Media-Website](https://github.com/AmanBharti07/Social-Media-Website)@[61c6dd29a5...](https://github.com/AmanBharti07/Social-Media-Website/commit/61c6dd29a5d0e26e323244822166090bb4b1d863)
#### Wednesday 2023-11-22 08:46:04 by Aman Bharti

Add files via upload

🌐 Social Connect - A Feature-Rich Social Media Platform

Welcome to the Social Connect repository, where innovation meets connection! This project is a comprehensive social media website designed to bring people together with a plethora of features, including message requests, notifications, and more.

Key Features:

📬 Message Requests: Seamlessly connect with friends through private messaging.
🔔 Notifications: Stay informed with real-time notifications for messages, friend requests, and more.
🌟 Rich Profiles: Customize your profile with images, bios, and personal details.
🤝 Friendship Management: Manage and interact with your friends effortlessly.
🌐 Explore Feed: Discover new content and connections through a curated explore feed.
🚀 Responsive Design: Enjoy a seamless experience across devices.

---
## [Perkedel/CVR_Stuffings](https://github.com/Perkedel/CVR_Stuffings)@[95a504b5d4...](https://github.com/Perkedel/CVR_Stuffings/commit/95a504b5d4e53898c9342332c786f1935f2be269)
#### Wednesday 2023-11-22 08:50:21 by JOELwindows7

It's official. It's the Archive division

Alright Archivers. You do you do. Remember, don't put sparsdat here. This is unlike for your usual activities.

This thing.., is for the Earth. And Terra, does not like you spread things, without being paid. well, some of them, thankfully.

So be careful. Wisely put it here. If you depend things that are paid, try to avoid them and make or find the $0 alt. If still can't, ask me away. Even if I paid it already, you must ignore those files, DON'T FUCKING FORGET THIS STEP!! If I got sued, we're all done. There's no recover.

ay look at that, one trouble's gone.

but another come back.

The _AudioLink shader variable is not separate source. Instead they're the .. uhh..

No I can't. Well.. if you want some positional, unfortunately, the Audio source must by the main mono one, not stereo ones.

---
## [Fazila164/tutorial-javascript](https://github.com/Fazila164/tutorial-javascript)@[af11485682...](https://github.com/Fazila164/tutorial-javascript/commit/af11485682bb957acb3b42d2b284480d71594955)
#### Wednesday 2023-11-22 09:48:00 by Fazila164

Add files via upload

Stone Paper Scissors Game Project:
Crafted with HTML, CSS, and JavaScript, this web game brings the classic challenge to life. Enjoy responsive design, user-friendly interface, and seamless gameplay on any device. Experience timeless fun in a modern digital playground.

---
## [Samsung-SM8150-Development/android_kernel_samsung_r3q](https://github.com/Samsung-SM8150-Development/android_kernel_samsung_r3q)@[0a8cfb8983...](https://github.com/Samsung-SM8150-Development/android_kernel_samsung_r3q/commit/0a8cfb8983776e612a818caffa12f701ed8b54ea)
#### Wednesday 2023-11-22 10:46:42 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: UtsavisGreat <utsavbalar1231@gmail.com>

---
## [alphagov/signon](https://github.com/alphagov/signon)@[9e18ce16fb...](https://github.com/alphagov/signon/commit/9e18ce16fbe00665c8ade4aa8a8e0c5d0f5c40de)
#### Wednesday 2023-11-22 11:09:05 by James Mead

Move edit user role page to GOV.UK Design System

Trello: https://trello.com/c/shaJpu8F

c.f. this commit [1] where we did the same for user name.

This changes the edit user role page to use the Design System and makes
a few other tweaks to bring it into line with the latest designs.

The page title & heading are slightly different to match other similar
pages.

I've added breadcrumbs to make this page consistent with other pages
even though they're not shown in the latest design for this type of
page.

The template for this controller is a bit more complicated than the one
for editing a user's name, because it has to handle the case where the
user being edited is exempt from 2SV which means they cannot be upgraded
from the normal role to any other (admin) role. In this case we just
display some inset text to explain why the user's role cannot be
changed. I'm not sure this is a great user experience, but it's
somewhate similar to what happens in the account change role page. Note
that I've humanized the role in the inset text, because I think that's
more consistent with how we're displaying role names to users in the
rest of the app.

I did contemplate hiding the "Change (role)" link on the edit user page
in this scenario. However, this link is already hidden when the current
user does not have permission to change a user's role and I thought it
would be more confusing if there were two reasons why it might not show
up. I think the behaviour in this commit is good enough for now and we
can iterate on the UX/design later.

I've based the design on the similar functionality in the
`app/views/account/roles/edit.html.erb` template, although I've reworded
the text to make it clear that in this case it's an admin user making
changes to a user rather than a user making changes to their own user.

I've also included the same hint HTML as used for a very similar `role`
select component in `app/views/devise/invitations/new.html.erb` which
replaces the "help-block" `span` element. I plan to extract this
duplication in a subsequent commit.

I'm using the `error_summary` component in combination with identical
code we've used elsewhere so that the errors in the summary link to the
relevant form field. Similarly I'm using the `select` component with
`error_message` set appropriately, so that any relevant errors are
displayed alongside the `role` field and the field itself is highlighted
in red as per this Design System guidance [2]. I've enhanced a test in
`Users::RolesControllerTest` to cover this new behaviour. Note that in
normal operation there are unlikely to be validation errors on this
page. However, it is possible if someone hacks the form or e.g. you try
to upgrade a user without an organisation to Organisation Admin.

The button text has changed from "Update User" -> "Change role" and I've
introduced a "Cancel" link to match other similar pages.

[1]: https://github.com/alphagov/signon/commit/f71a128b6a6f9cd86bd8c08508a35d8780c128ef
[2]: https://design-system.service.gov.uk/patterns/validation/#how-to-tell-the-user-about-validation-errors

---
## [Sanjay-tone/Tripadvisor](https://github.com/Sanjay-tone/Tripadvisor)@[cee01c9c02...](https://github.com/Sanjay-tone/Tripadvisor/commit/cee01c9c02aac2d45a455fdbc21ecca84372f559)
#### Wednesday 2023-11-22 11:20:05 by Sanjay Vel

Add files via upload

TripAdvisor - Your Ultimate Travel Companion

Welcome to TripAdvisor, the go-to platform for travel enthusiasts seeking unforgettable experiences! Our website is designed to help you discover, plan, and book the perfect trip tailored to your preferences. Here's a breakdown of what you can expect:

Header:
At the top of the page, you'll find a vibrant header showcasing the TripAdvisor logo. The navigation bar provides easy access to key sections, including Home, Hotels, Restaurants, and Things to Do. The navigation links are styled for a modern and user-friendly experience.

Main Content:
The main content section is a hub of information and inspiration for your next adventure. A welcoming heading invites users to explore TripAdvisor's offerings. Engaging paragraphs highlight the platform's commitment to helping users find and book their ideal trips. This section is designed with a clean and spacious layout, making it easy for users to absorb information.

Footer:
The footer is a sleek and informative section located at the bottom of the page. It features a dark background with white text, providing a stylish contrast. The copyright information assures users that TripAdvisor is a reputable and established platform. The fixed position ensures that the footer remains visible even as users scroll through the content.

---
## [DianaOprea89/SmartMenU](https://github.com/DianaOprea89/SmartMenU)@[4d1b7ecaa7...](https://github.com/DianaOprea89/SmartMenU/commit/4d1b7ecaa712d4da476020ec5757c5664b03b830)
#### Wednesday 2023-11-22 11:35:50 by DianaO

Chages:
 - on Add Restaurant component i have fixed the addRestaurant() method so that the user can add a restaurant he manages information for, and the infor is sent to the server and stored there.
 - on Profile component i have added the removeRestaurant() method that is triggered when the remove button is being clicked , so that the user can remove the restaurant he no longer want to have on his profile, also they are removed from the data base.
 - all the information regarding an user is saved on my data base SmartMenu (mongo DB) on colection users, and each user that is registering to use this app will have an object created on that collection
     ex: {
           "_id": {
             "$oid": "654b85063e39c4d58c6c6702"
           },
           "username": "radu",
           "email": "radu@mail.com",
           "passwordHash": "$2b$10$OtgvFwkXqTqyMImDMuk9Du44BhiK/9No8mq0XK2FhgdSFbzCxc/wO",
           "createdAt": {
             "$date": "2023-11-08T12:54:30.460Z"
           },
           "__v": 60,
           "restaurants": [
             {
               "name": "Time & Place Kitchen I Bar",
               "address": "6083 McKay Ave 3rd Floor Hilton Vancouver Metrotown, Burnaby, British Columbia V5H 2W7 Canada",
               "phoneNumber": "1 604-639-3756",
               "aboutUs": "ABOUT\nDiscover a wholesome menu with a focus on local produce and house made items. Time & Place is the place to gather and graze over an array of mains, sharable plates, and casual handhelds all prepared to perfection. Executive Chef David Ferguson truly presents the best of what is around us. There’s a Time & Place for everything.",
               "logoImage": "https://media-cdn.tripadvisor.com/media/photo-s/1b/ad/7e/77/join-us.jpg",
               "menuOptions": [
                 null,
                 {
                   "photoLink": "https://cdn.sortiraparis.com/images/1001/100789/834071-too-restaurant-too-hotel-paris-photos-menu-entrees.jpg",
                   "optionName": "Bucatarie",
                   "_id": {
                     "$oid": "655db0a013a77a7dbed080bf"
                   }
                 },
                 {
                   "photoLink": "https://cdn.sortiraparis.com/images/1001/100789/834023-too-restaurant-too-hotel-paris-photos-menu.jpg",
                   "optionName": "Bar",
                   "_id": {
                     "$oid": "655db24013a77a7dbed08102"
                   }
                 }
               ],
               "_id": {
                 "$oid": "655cb03e32884aa7218fec33"
               }
             },
             {
               "name": "Trattoria Burnaby",
               "address": "4501 Kingsway, Burnaby, British Columbia V5H 2A9 Canada",
               "phoneNumber": "1 604-424-8779",
               "aboutUs": "ABOUT\nSimple and fresh is really what Italian home cooking is all about. At Trattoria the menu reads like a summer in Italy, with classic ingredients, masterfully combined, and served without a lot of fuss and bother. This is what Italian food should be.",
               "logoImage": "https://media-cdn.tripadvisor.com/media/photo-s/07/86/f6/e0/trattoria-italian-kitchen.jpg",
               "menuOptions": [
                 null
               ],
               "_id": {
                 "$oid": "655cb06832884aa7218fec4d"
               }
             },
             {
               "name": "Cayenne Bistro & Grill",
               "address": "7677 6th St, Burnaby, British Columbia V3N 3M8 Canada",
               "phoneNumber": "1 604-553-7866",
               "aboutUs": "We are an East African and Indian fusion restaurant. We are open for lunch and dinner every day, but we are closed on Tuesday. We serve 100% Halal food and the owner/chef has a passion for cooking and enthusiastic about creating amazing dishes with African and Indian spices. We offer catering services for office parties, home or any special occasion you might have. You can also order your favorite dishes from Cayenne Bistro & Grill by Doordash, Skip the Dishes and Uber eats or phone in your order for pick up form the restaurant.\n\nhttps://www.tripadvisor.ca/ShowUserReviews-g181793-d15865774-r870066056-Cayenne_Bistro_Grill-Burnaby_British_Columbia.html#",
               "logoImage": "https://media-cdn.tripadvisor.com/media/photo-s/16/5b/49/94/beef-ribs-with-salad.jpg",
               "menuOptions": [
                 null
               ],
               "_id": {
                 "$oid": "655cb0e032884aa7218fec7e"
               }
             }
           ]
         }

  - created the OptionMenu component, that is triggered  when on any of the  resturants is clicked the  More Info button , we go to another page were the restaurant is being dispalyed and we have the option to add new Menu Options (ex Restaraunt, Bar, Dessert)

---
## [Vhmit/kernel_xiaomi_lavender](https://github.com/Vhmit/kernel_xiaomi_lavender)@[09c3d2b6b0...](https://github.com/Vhmit/kernel_xiaomi_lavender/commit/09c3d2b6b0f3bf29de243ed2a03bde2998e60f2a)
#### Wednesday 2023-11-22 11:43:11 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [darnautov/kibana](https://github.com/darnautov/kibana)@[cd909f03b1...](https://github.com/darnautov/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Wednesday 2023-11-22 11:59:42 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[5c0660acc0...](https://github.com/Danielkaas94/DTAP/commit/5c0660acc00e1dd2c380223e33cc89fa1a61bb4c)
#### Wednesday 2023-11-22 12:09:46 by Daniel Kaas Bundgaard Jørgensen

🌀🌌🧙‍♂️ Demiurge 🧙‍♂️🌌🌀
Writhing and embraced
Retribution, soul eclipse turns solid
Energized
Sucking vomit, acting like its honey
Deprived of I
Falling while thrusting squares through circles
Serving one single new dimension

Terror rising
Agnostics' nemesis
A prophet of extinction

I scorch the skies before your very eyes
My deliverance
Enslavement labelled love

Just trust this, nemesis, to sign and seal extinction

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[ae657da613...](https://github.com/Danielkaas94/DTAP/commit/ae657da61319b1da7bb7eb8d093a6ae548f59b5a)
#### Wednesday 2023-11-22 12:39:04 by Daniel Kaas Bundgaard Jørgensen

🔜🔚 Bitter End 🔜🔚
I am broken by my birthright
And made to die by design
I was put on this earth to fail you
Why do you put your faith in me?
I will let you down
I will give you a reason to hate me
I will give you a reason to despise me

I never thought I'd see the day
When I'd see my maker face to face
Every sin accounted for
Every bad decision I ever made
Little did I know this would all lead up to this
This is my time
This is my breaking point

I'll pay my price
Just please don't let me miss
My peace of mind
I'll even die for this
God ease my soul
And don't let me forget
That there is nothing forcing me to a bitter end

I can't stand another day in my head
All the pain
All the lies
It's wearing me thin
Why can't I just follow you?
Oh God, it's taking over

This is a takeover
My eyes have learned to lust
And my mind was molded to betray you
I've let this spite fill my lungs
Fill my lungs
This is my breaking point
This is my breaking point
This will not be my bitter end

I'll pay my price
Just please don't let me miss
My peace of mind
I'll even die for this
God ease my soul
And don't let me forget
That there is nothing forcing me to a bitter end
I'll pay my price
Just please don't let me miss
My peace of mind
I'll even die for this
God ease my soul
And don't let me forget
That there is nothing forcing me to a bitter end
Bitter end
Bitter end
This is my breaking point

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[9558b8710b...](https://github.com/Danielkaas94/DTAP/commit/9558b8710b559371c0c7de391e1000812a642e6d)
#### Wednesday 2023-11-22 12:41:57 by Daniel Kaas Bundgaard Jørgensen

🤮🤢🤒 Ravenous Disease 🤒🤢🤮
Sell your soul
Sell your soul he will swallow it whole
Sell your soul
Sell your soul he will swallow your soul

(Betrayer)
(Betrayer)

Betrayer, blind to faith blinding followers
Spreading deception like a plague through their veins
Pumping hell in their hearts
Betrayed by the father

Ravenous disease (ravenous disease)
Man is the carrier

A broken moral compass
Charting the course for generations of sorrow
A life void of substance
A future so bleak we look ahead with horror
Horror

Fallen from grace
Deeper we sink
A great pit within the earth
Swallowing the weak

Fallen from grace
Deeper we sink
A great pit within the earth
Swallowing the weak

Whispers of demons
Ringing in the ears of the crowd
Impressionable youth
Sing every word
Spewing from their wretched mouths

A broken moral compass
Charting the course for generations of sorrow
A life void of substance
A future so bleak we look ahead with horror
Horror

(Ravenous disease)
(Man is the carrier)
(Ravenous disease)
(Man is the carrier)

Sell your soul
Sell your soul he will swallow it whole
Sell your soul
Sell your soul he will swallow your soul

There will be hell to pay
Fallen from grace
Deeper we sink
Fallen from grace
Deeper we sink

---
## [alphagov/signon](https://github.com/alphagov/signon)@[6fe32631f2...](https://github.com/alphagov/signon/commit/6fe32631f285280613c339ab42ba2890977bb115)
#### Wednesday 2023-11-22 12:42:05 by James Mead

Add Mysql2::Error to exceptions not reported during db sync

Trello: https://trello.com/c/MD4UabpW

Reently we've started seeing a load of `ActiveRecord::StatementInvalid`
exceptions [1] every night at about 01:00. These all wrap
`Mysql2::Error` exceptions with a message along the following lines:

    Table 'signon_production.<table-name>' doesn't exist

These exceptions seem to have started occuring around the time the db
sync was moved to EKS. Presumably the sync is happening in a different
way - perhaps table are being dropped & recreated when previously the
data in the table was just being updated.

Anyway, these docs [2] explain that we can configure Sentry to ignore
specific exceptions that occur during the db sync and it looks like this
is what other apps are relying on.

The default `GovukError` configuration [3] excludes `PG:Error` &
`GdsApi::ContentStore::ItemNotFound`. However, Signon uses MySQL rather
than PostgreSQL, which is why the `Mysql2::Error` exceptions are still
being reported.

I contemplated adding `ActiveRecord::StatementInvalid` to the exclusion
list, but that seemed slightly at odds with `PG::Error` currently being
on the list.

According to the docs:

> When determining whether or not to ignore an exception, the exception
chain is inspected. This means if an exception isn’t on the ignore list,
but its underlying cause is an exception on the ignore list, then it
will be ignored. This applies to excluded_exceptions and to
data_sync_excluded_exceptions.

So this commit adds `Mysql2::Error` to the exclusion list on the
assumption that it will be recognised as the underlying cause of the
`ActiveRecord::StatementInvalid`.

I contemplated adding this to the default `GovukError` configuration
[3], but I can't remember off-hand whether there are any other apps
using MySQL and in any case I think it's worth trying it out in Signon
first to see if it does the trick.

[1]: https://govuk.sentry.io/issues/4607637619/
[2]: https://docs.publishing.service.gov.uk/manual/sentry.html#ignoring-exception-types
[3]: https://github.com/alphagov/govuk_app_config/blob/8598b901e73a9a023d27018f30a06ab5dac66ad8/lib/govuk_app_config/govuk_error/configuration.rb#L55-L63

---
## [RasmussenLab/vamb](https://github.com/RasmussenLab/vamb)@[649eacf48c...](https://github.com/RasmussenLab/vamb/commit/649eacf48c3140e9016a97efb921ba22b6ef195b)
#### Wednesday 2023-11-22 12:46:31 by Jakob Nybo Nissen

Add Ruff linting to CI

This check catches quite a few bugs and code quality issues. It's very fast to
run locally, so shouldn't be too much a pain in the ass.
Ruff is configured through pyproject.toml.
We can always disable this check if it becomes too annoying

---
## [AMANDEEPSINGHBHALLA/URL-QR-Generator](https://github.com/AMANDEEPSINGHBHALLA/URL-QR-Generator)@[6ff8161b3f...](https://github.com/AMANDEEPSINGHBHALLA/URL-QR-Generator/commit/6ff8161b3f8d1b3b21f3796038cacc9c1261c85a)
#### Wednesday 2023-11-22 12:58:31 by AMANDEEP SINGH BHALLA

Create README.md

# URL QR-Generator

URL QR-Generator is a user-friendly web application designed to simplify the process of generating QR codes for URLs. Whether you need to quickly create a QR code for a website link or want to manage your QR code history, this application provides an intuitive solution.

## Features

- **Generate QR Codes:** Easily generate QR codes for URLs by entering the desired link into the input field and clicking the "Generate" button.

- **View QR Code History:** Keep track of your QR code history directly on the main page, allowing for easy reference and reuse of previously generated codes.

- **Responsive Design:** The application features a responsive design, ensuring a seamless experience across various screen sizes and devices.

## Technologies Used

The application is built using the following technologies:

- **Node.js:** A JavaScript runtime for server-side development.
- **Express.js:** A web application framework for Node.js that simplifies the creation of web applications.
- **MongoDB:** A NoSQL database for storing QR code data.
- **qr-image library:** Used for generating QR codes in Node.js.
- **Bootstrap:** A popular front-end framework for building responsive and visually appealing user interfaces.
- **HTML, CSS:** Standard web development languages for structuring and styling the application.

## Deployment

The application is deployed using [Render](https://render.com/). You can access the live site at [https://urlqrgenerator-nsrv.onrender.com/](https://urlqrgenerator-nsrv.onrender.com/).

## Getting Started

To run the application locally, follow the installation steps outlined in the README. Ensure you have Node.js installed and set up a MongoDB Atlas account for database storage.

## Usage

1. Enter the URL in the input field and click the "Generate" button to create a QR code.
2. Access your QR code history on the main page for quick reference.
3. Enjoy the responsive design that adapts to various screen sizes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
## [abhi-0104/zechub](https://github.com/abhi-0104/zechub)@[0d97121c8c...](https://github.com/abhi-0104/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Wednesday 2023-11-22 13:05:10 by TonyAkinsWritesCrypto

ZecWeekly66

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [VigramK/terminal](https://github.com/VigramK/terminal)@[86fb9b4478...](https://github.com/VigramK/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Wednesday 2023-11-22 13:07:07 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [leohhhn/gno](https://github.com/leohhhn/gno)@[24d89a4f5d...](https://github.com/leohhhn/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Wednesday 2023-11-22 13:18:00 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [AMANDEEPSINGHBHALLA/ASBplix](https://github.com/AMANDEEPSINGHBHALLA/ASBplix)@[82f052dabe...](https://github.com/AMANDEEPSINGHBHALLA/ASBplix/commit/82f052dabedb9e2c777a167bf7094bf07b37a175)
#### Wednesday 2023-11-22 13:59:39 by AMANDEEP SINGH BHALLA

Update README.md

# ASBplix - Elevate Your Streaming Experience

Welcome to ASBplix, your go-to destination for top-tier entertainment. ASBplix is a cutting-edge streaming platform designed for today's audiences, delivering the latest movies, TV shows, and exclusive AP Originals with style and simplicity.

## Key Features

- **Responsive Design:** Enjoy a seamless streaming experience on any device. ASBplix's responsive design ensures optimal viewing, whether on a desktop or mobile device.

- **Intuitive Navigation:** Effortlessly explore Home, Plans, and Categories with our user-friendly dropdown menu.

- **User-Centric Interface:** Experience the platform's convenience with a "Try for free" option and a straightforward sign-in process.

- **Informative Sections:** Discover ASBplix's offerings through well-crafted sections, inviting you to dive into a world of entertainment.

- **External Page Integration:** Seamlessly link to external pages for plans and login, extending the user journey beyond the main platform.

## Technologies Used

ASBplix is powered by a modern web stack:

- **HTML5:** Crafting dynamic and engaging content.

- **CSS3:** Creating a visually appealing and responsive design, tailored for various screen sizes.

- **JavaScript:** Enhancing interactivity throughout the platform.

## Responsive Design

ASBplix prioritizes a consistent and delightful user experience across diverse devices. Our responsive design principles, implemented with CSS media queries, guarantee a visually appealing layout on desktops and mobile screens alike.

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request. Check out the [Contribution Guidelines](CONTRIBUTING.md) for more details.

## License

ASBplix is licensed under the [MIT License](LICENSE), fostering open collaboration and usage.

Immerse yourself in the world of ASBplix, where entertainment meets simplicity!

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[e135ddecc1...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/e135ddecc16649fcb290b47a8ad2ccdcf8369c68)
#### Wednesday 2023-11-22 14:22:54 by SkyratBot

[MIRROR] Changes to the lore of Knock [MDB IGNORE] (#24891)

* Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

* Changes to the lore of Knock

---------

Co-authored-by: Profakos <profakos@gmail.com>

---
## [fhahn/llvm-project](https://github.com/fhahn/llvm-project)@[5cd24759c4...](https://github.com/fhahn/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Wednesday 2023-11-22 14:35:16 by Louis Dionne

[libc++] Reduce the compilation time required by SIMD tests (#72602)

Testing all the SIMD widths exhaustively is nice in theory, however in
practice it leads to extremely slow tests. Given that
1. our testing resources are finite and actually pretty costly
2. we have thousands of other tests we also need to run
3. the value of executing these SIMD tests for absolutely all supported
SIMD widths is fairly small compared to cherry-picking a few relevant
widths

I think it makes a lot of sense to reduce the exhaustiveness of these
tests. I'm getting a ~4x speedup for the worst offender
(reference_assignment.pass.cpp) after this patch.

I'd also like to make this a reminder to anyone seeing this PR that
tests impact everyone's productivity. Slow unit tests contribute to
making the CI slower as a whole, and that has a direct impact on
everyone's ability to iterate quickly during PRs. Even though we have a
pretty robust CI setup in place, we should remember that it doesn't come
for free and should strive to keep our tests at a good bang for the buck
ratio.

---
## [GregTechCEu/GregTech-Modern](https://github.com/GregTechCEu/GregTech-Modern)@[852bb70272...](https://github.com/GregTechCEu/GregTech-Modern/commit/852bb70272ec9040d0dc6d1b695442a43f3969c3)
#### Wednesday 2023-11-22 15:59:52 by screret

Byproduct limiting (#572)

* it doesn't crash but kinda doesn't work either

* Holy shit it works!!!! gonna implement multiblock voiding mode button in separare PR.

* final lil' fixes

* reviews?

---
## [sbwdonlinetraining/Talent-Build-Tech-Community-App](https://github.com/sbwdonlinetraining/Talent-Build-Tech-Community-App)@[7c557b4900...](https://github.com/sbwdonlinetraining/Talent-Build-Tech-Community-App/commit/7c557b4900341a11ec1e3989f47cd803b5b0be35)
#### Wednesday 2023-11-22 16:00:32 by sbwdonlinetraining

Update README.md

Local Community Hub
Welcome to our Local Community Hub app, your one-stop destination for staying connected and informed! This app empowers you to:

Discover Local News: Stay updated with the latest news in our community.

Explore Exciting Events: Find and join events happening in our neighborhood.

Satisfy Your Cravings: Order delicious food from local restaurants right at your fingertips.

Personalized Dashboard: Access your personalized dashboard for a tailored experience.

Join us in building a stronger, more connected community. Explore, engage, and enjoy the benefits of our Local Community Hub app!

---
## [paledoptera/shadowfellsaga](https://github.com/paledoptera/shadowfellsaga)@[883af00e07...](https://github.com/paledoptera/shadowfellsaga/commit/883af00e078c90384ec9805aaf9d0daeedf37d69)
#### Wednesday 2023-11-22 16:51:28 by paledoptera

Shadowfell Saga v0.6

version numbers are kinda fucked right now thanks to Previous Commits (there were two v0.5.8s) so i'm just gonna list shit that i added or changed recently

ADDITIONS:
- revamped code for obj_ow_player, now uses state machines and generally is less spaghetti-code-y
- added new jump/fall sprites for papyrus
- added new input system, now all of the game's input is handled by one object simply called "input" (no obj_)
- added new savelamp animation
- added tweening for button prompts (they slide up and down if they're active or inactive)

BUGFIXES:
- restored basic functionality of the save menu, still bugged in certain aspects though. there's also no way to load saves, so right now they're just visual i guess

BUGS:
- save system is still a little bugged
- c menu is completely fucked, completely unusable. needs to be rewritten from the ground up
- follower system is a tiny bit buggy, needs to be slightly rewritten like player

PLANS FOR NEXT VERSION:
- fucking documentation
- rewrite for follower system
- c menu complete rewrite
- dark world cutscene implementation

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4d66e5fe64...](https://github.com/TaleStation/TaleStation/commit/4d66e5fe647b31f5d133719ed499d2b3d9e8027b)
#### Wednesday 2023-11-22 17:01:57 by TaleStationBot

[MIRROR] [MDB IGNORE] Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#8692)

Original PR: https://github.com/tgstation/tgstation/pull/79803
-----

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much. 

## Changelog



:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: KingkumaArt <69398298+KingkumaArt@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[9fea94082a...](https://github.com/TaleStation/TaleStation/commit/9fea94082ad8f7cd85669ebba9a507a67674500b)
#### Wednesday 2023-11-22 17:04:23 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactor icemoon wolves into basic mobs and add taming + pack behavior (#8708)

Original PR: https://github.com/tgstation/tgstation/pull/79736
-----
## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [Gosth15/android_kernel_xiaomi_sm8475](https://github.com/Gosth15/android_kernel_xiaomi_sm8475)@[97a5d53a4f...](https://github.com/Gosth15/android_kernel_xiaomi_sm8475/commit/97a5d53a4ffdf4e0d95c2266c28bf82adeaef611)
#### Wednesday 2023-11-22 17:04:45 by lateautumn233

module: unload module
fix recovery bootloop
* fuck you init

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ef52047274...](https://github.com/tgstation/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Wednesday 2023-11-22 17:36:07 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [AMANDEEPSINGHBHALLA/simon-gaame](https://github.com/AMANDEEPSINGHBHALLA/simon-gaame)@[ffd1c159de...](https://github.com/AMANDEEPSINGHBHALLA/simon-gaame/commit/ffd1c159de7fa3fa063790a41183b16bc54ad302)
#### Wednesday 2023-11-22 17:51:02 by AMANDEEP SINGH BHALLA

Create README.md

# Simon Game

Welcome to the Simon game implementation in HTML, CSS, and JavaScript! This project is a digital adaptation of the classic Simon game, designed to test and enhance your memory and pattern recognition skills.

## Overview

Simon is a timeless game where players follow a sequence of colors and sounds generated by the game and then attempt to replicate that sequence. The game becomes progressively challenging as players successfully complete each level, introducing longer and more complex sequences to remember.

## Features

- **Responsive Design**: Play the game seamlessly on various devices, from desktops to smartphones.
- **Audio and Visual Feedback**: Enjoy an engaging experience with sound and visual effects for user interactions.
- **Dynamic Level and Score Tracking**: Keep track of your progress with dynamically updating levels and scores.
- **Mobile Vibration Support**: Experience additional feedback on mobile devices through vibration.

## How to Play

1. Press any key (or touch the screen on mobile devices) to start the game.
2. Remember the sequence of colors played by the game.
3. Click or tap on the buttons to replicate the sequence.
4. Successfully completing a sequence increases your score and advances you to the next level.
5. Aim for the highest score possible!

## Demo

Check out the live demo [here](https://amandeepsinghbhalla.github.io/simon-gaame/). Screenshots and gameplay gifs are also provided to give you a preview of the game.

## Deployment

This project is deployed using GitHub Pages and is live at [https://amandeepsinghbhalla.github.io/simon-gaame/](https://amandeepsinghbhalla.github.io/simon-gaame/).

## Contributing

Feel free to contribute to the project. If you have suggestions, improvements, or find any issues, please create a pull request or open an issue.

## Dependencies

- **jQuery**: [Link to jQuery](https://jquery.com/)

## License

This project is licensed under the [MIT License](LICENSE).

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[a1e46c5d31...](https://github.com/OliOliOnsiPree/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Wednesday 2023-11-22 18:25:42 by Jacquerel

Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[66b8b1d866...](https://github.com/DrDiasyl/tgstation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Wednesday 2023-11-22 18:36:36 by Fikou

Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

---
## [Jahana/server](https://github.com/Jahana/server)@[aa30c9ec2e...](https://github.com/Jahana/server/commit/aa30c9ec2e15fd526fca9080ab434939d12a9656)
#### Wednesday 2023-11-22 18:44:49 by MowFord

Cait Sith Avatar:

- Cait sith has proper name prefix and named properly to be "Cait Sith" instead of "The CaitSith"
- BPs Implemented
  - Regal Slash (BP:Rage): 3-hit physical
  - Level ? Holy (BP:Rage): aoe magical
    - Rolls a die and does dmg proportional to roll
    - Only does damage if the target's level is divisible by the roll
  - Mewing Lullaby (BP:Ward):
  AoE lullaby that resets TP
  - Eerie Eye (BP:Ward):
  conal silence/amnesia with appropriate elemental resist check for amnesia, but retail does light check for silence
  - Reraise II (BP:Ward):
  single-target 60-minute reraise II buff for any party member
  - Raise II (BP:Ward):
  single-target raise II for any party member
  - Altana's Favor (BP:Ward):
  2-hour ability gives arise to all party members in range
  (Arise and reraise III with infinite duration)

---
## [DGamerL/Paradise](https://github.com/DGamerL/Paradise)@[c4e96e4ca0...](https://github.com/DGamerL/Paradise/commit/c4e96e4ca062342e19a84f6af76dd22ade3cc3bf)
#### Wednesday 2023-11-22 18:52:52 by Alexios

Ports Humans from TG - Soul Massacre  (#22361)

* Easiest PR of my life - adds new humans and culls your soul -  ProTip! Great commit summaries contain fewer than 50 characters. Place extra information in the extended description. - go fuck yourself github I will post the bee movie script if you don't shut up

* I'm dying because I'm so surprised.......

* I don't have any other memes heres the simplemobs I'll think of something

* Add new sprites and old sprites, man what nice guys

* Add code for first haul of races

* Attempted fix at CRLF to LF

* Fix indentation

* Move last code line fix pp

---
## [JupiterJaeden/tgstation](https://github.com/JupiterJaeden/tgstation)@[157fafeaa9...](https://github.com/JupiterJaeden/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Wednesday 2023-11-22 19:20:07 by lizardqueenlexi

[CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[830e002a27...](https://github.com/realforest2001/forest-cm13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Wednesday 2023-11-22 19:24:37 by QuickLode

Adds a Colony Synthetic variant, with bug fixes (#4760)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

1. should fix fax machine problem(thx forest)
2.  gives trucker synth the frontier jumpsuit(Thwomplert)
3. adds Freelancer Synthetic. This Synth is one that was bought off a
civi market and reprogrammed, or stolen and reprogrammed, or hacked, You
get the point - its going with a band of freelancers. The idea behind it
is that this synth's team is dead and they are just programmed as a merc
for pay - hoping to someday find their boss boss and give the money as
set up. I always thought about this one for a long time and decided to
put him in the civilian category, where its hard to roll and also gives
you freedom to choose your allegiance. In this case I hope that a
freelancer synthetic will open up unique avenue of RP and allegiance.
I've only explored it once ingame, but it was very good for RP!
Hopefully people can recreate this success.

was hard to make this guy look cool and I also wasn't sure on what his
loadout would be. I ended up giving him random generic stuff while
looking like a beat up freelancer(missing the armor especially hurt his
look, since thats the largest piece of a freelancer - the curiass, but I
don't want to give armor for balance reasons) and no beret because its
for a SL only.

as usual, if a synth wants to change RP avenues and don different
clothes for different RP, no one would know the difference
# Explain why it's good for the game
1. bug bad
2. a beat up UA laborer that so happens to be synthetic. you wouldn't
expect it because there's so many similar looking people! exactly the
job of a synth - to blend in.
3. Freelancer colony synth hopefully will open up a unique avenue of RP.
If they don't want to they can always ditch it - but its on a relatively
rare and uncommon roll anyways.
# Testing Photographs and Procedure
<details>
<summary>[Screenshots &
Videos](https://cdn.discordapp.com/attachments/490668342357786645/1166307813719556187/image.png?ex=654a03cb&is=65378ecb&hm=7108218bbaab61c78c0bedcecbfdcc07bdf9db87a3fefe9fb94b28d3430cc815&)</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: adds another Colony Synthetic variant, changes up some existing
ones(trucker,CMB)
fix: fixes a small problem with WY-Colony Synthetic access(thx forest),
adds WY subtype of Synthetics for admin building/faxes
fix: fixes problems with organic spawning ferret industries Trucker
Synthetic
/:cl:

---
## [pippinbarr/v-r-5](https://github.com/pippinbarr/v-r-5)@[7cee038c9f...](https://github.com/pippinbarr/v-r-5/commit/7cee038c9fb6722bb87d0ac592308f9a3d6f3dd0)
#### Wednesday 2023-11-22 19:43:51 by Pippin Barr

Worked on the Zium prototype, added multiple light fixtures

- There are now something like 10 different fixtures (3 spots and maybe 7 points? Or more?)
- Trying to capture the extremes of settings (cast/not, receive/not, point/spot, bias/not, etc.)
- Trying to have the fixtures mapped out physically so that they exist in space rather than all coming from a mystery location
- There's work to be done on positioning them and the objects that cast the shadows
- Lights go on for 10s and off for 2s right now, that's flexible - want there to be enough time to look
- An alternative would be to map out the floor and have to switch lights, but then you can't view shadows up close?
- Or to allow the player to activate and deactivate lights I suppose, but that seems fiddly and annoying - I guess I probably prefer the timer for right now
- Good to see some of this stuff actually working, but I'll confess in this moments I a LITTLE BIT UNDERWHELMED? Have to explore that feeling, maybe be general work-related tiredness?
- THe #webgl build is in /zium to separate concerns a bit, though I consider this work part of the overall v r 5 thing

---
## [AnouarXperience/The-Legend-Of-Mirai](https://github.com/AnouarXperience/The-Legend-Of-Mirai)@[77846dc4e8...](https://github.com/AnouarXperience/The-Legend-Of-Mirai/commit/77846dc4e80bbebf5f844544a6e1ac3099c65d3c)
#### Wednesday 2023-11-22 20:13:43 by lanwaros

feat: 🚀 Initial Release - Version 1.0.0

🌐 **Website Launch - Version 1.0.0**

Exciting times! This commit marks the official release of our website, introducing Version 1.0.0. 🚀

**Key Features:**
- Responsive design for seamless user experience across devices.
- Intuitive navigation for easy exploration.
- Engaging visuals and user-friendly interface.

**Tech Stack:**
- Frontend: HTML, CSS, JavaScript
- Backend: PHP
- Version Control: Git, GitHub

This release sets the foundation for future updates and enhancements. We appreciate everyone's contributions and feedback.

Happy exploring! 🎉

---
## [sukritee-N/privat](https://github.com/sukritee-N/privat)@[ce96067876...](https://github.com/sukritee-N/privat/commit/ce96067876fa39dd4fc477caa923c15284a7a1b3)
#### Wednesday 2023-11-22 20:22:48 by sukriteenath

god fucking damnit, how am I supposed to deal with websocket?.. gotta get some sleep, GN

---
## [james-j-obrien/bevy](https://github.com/james-j-obrien/bevy)@[ab300d0ed9...](https://github.com/james-j-obrien/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Wednesday 2023-11-22 20:28:47 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[e3ee4a0093...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/e3ee4a009351df890f8e7ea814358bcae3d9f1c4)
#### Wednesday 2023-11-22 20:50:33 by Ua-Gi-Oh

Перекладені карти 

За 22.11.2023
1 - Snake Rain
2 - Molten Behemoth
3 - Fusion Conscription
4 - Winds Over the Ice Barrier
5 - Hammer Shark
6 - Maiden of the Aqua
7 - Lost World
8 - Jurraegg Token
9 - Flash Fusion
10 - Wretched Ghost of the Attic
11 - Gishki Natalia
12 - Gigathunder Giclops
13 - Ground Spider
14 - Doorway of the Celestial Mikanko
15 - Diana the Light Spirit
16 - Zombie Master
17 - U.A. Rival Rebounder
18 - Herald of Orange Light
19 - Naturia Mosquito
20 - Helios Trice Megistus

За 21.11.2023
1 - Materiactor Annulus
2 - Pride of the Plunder Patroll
3 - Performage Trapeze Magician
4 - Mother Spider
5 - Elemental HERO Chaos Neos
6 - Evolsaur Diplo
7 - Guarded Treasure
8 - Heavenly Zephyr - Miradora
9 - Wall of Revealing Light
10 - Xiangsheng Magician
11 - Ancient Telescope
12 - Yormungarde
13 - Constellar Leonis
14 - Destiny HERO - Dogma
15 - Flower Cardian Zebra Grass
16 - Armored White Bear
17 - Life Equalizer
18 - Yang Zing Path
19 - Inferno Hammer
20 - Phantom Bounzer

---
## [kyuujuushi/thebuzz](https://github.com/kyuujuushi/thebuzz)@[de9c182262...](https://github.com/kyuujuushi/thebuzz/commit/de9c182262595eac03e30b785f0fb992db2aa83c)
#### Wednesday 2023-11-22 20:54:54 by kyuujuushi

fucked around in the html. the link to the file is still ass. its asking for a stupid endpoint or im putting too many arguments apperantly. fuck flask

---
## [mylove90/pc_ginkgo](https://github.com/mylove90/pc_ginkgo)@[4add3d1c8d...](https://github.com/mylove90/pc_ginkgo/commit/4add3d1c8d5bc62f4db8f1f60e02f2b8d941d316)
#### Wednesday 2023-11-22 21:07:09 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [numbbo/coco](https://github.com/numbbo/coco)@[23333cdb63...](https://github.com/numbbo/coco/commit/23333cdb63482fece8d8f70542f06464ba45e80e)
#### Wednesday 2023-11-22 21:48:29 by RandomUser

Implementing the bbob noisy wrappers around the existing functions

The present commit implements the wrappers around the f_<function_name>_evaluate, f_<function_name>__allocate and f_<function_name>_bbob_problem_allocate functions,
needed to implement a noisy version of the given problem.

In particular, this is handled by the three functions:

* coco_problem_f_evaluate_wrap_noisy
* coco_problem_allocate_f_wrap_noisy
* coco_problem_allocate_bbob_wrap_noisy

The definition of the just mentioned functions is written in the suite_bbob_noisy_uitilities file, while their declaration is in the coco.h header file.

In order to make this idea of wrapping work, we defined the following structures

* coco_noise_model_s
* coco_noisy_problem_s

The coco_noise_model_s is used to evaluate the noise model according to the paper <paper_name>.

The coco_noisy_problem_s is a structure used as a wrapper around coco_problem_t (which is one of its member attributes, inner_problem), and is (should be) able to
implement the noisy version of a given problem in the bbob test suite.

The preceding approach of defining the noisy version of each function is, as we mentioned in the previous commit message, unfeasible.

On the other hand, for respecting the project structure in terms of protection and isolation of certain files, we found the need to define, finally, the three functions
used to allocate the noisy version of the problems in the bbob datasuite, according to the three aforementioned noise models. These functions are:

* coco_problem_allocate_bbob_wrap_noisy_gaussian
* coco_problem_allocate_bbob_wrap_noisy_uniform
* coco_problem_allocate_bbob_wrap_noisy_cauchy

Corrected a few bugs I noticed from the previous commit and added the bbob_noisy.c file containing the definition of the functions needed to create and allocate the bbob-noisy test suite

Testing the c code build and running the first (unsuccessfull) regression test.

Array initialization was wrong

Need to handle the schaffers and gallagher functions in a particular way

This is due to the fact that the functions f_schaffers_bbob_problem_allocate
and f_gallagher_bbob_problem_allocate have a different signature than the other
f_<function_name>_bbob_problem_allocate ones.
For how I was thinking of implementing the noisy suite, as a wrap around the existing bbob suite,
this fact created the need to define specific wrappers (and function types) for these two mentioned
functions.
In addition, we added some other function type in coco_internal.h for minimizing the number of
unused parameters in the overall project

Generating data for regression test for the bbob-noisy suite

Apparently it kinda works now, it's time to do the needed tests

Preparing code for regression testing

Done the necessary modifications needed to be able to test the new implementation of the bbob-noisy
test suite against the old code.

Running now the full checks. I already checked if the fopt and the xopt are the same across the two implementations,
and this seems to be the case. Writing now the scripts to be able to reproduce the results.

One thing I observed regarding the fact that these tests were not passing at all, is that I realized that the
function id needs to exactly match across the two implementations for the xopt and yopt to be computed in the same way.

This is what I did and, as expected, it corrected this behaviour.

Proceeding with the regression test

I am currently proceeding with the regression tests.
I tested the new implementation (in the noise free version), against the legacy code (by taking the ftrue values instead of the fval ones, noise free again)
The test consisted in randomly sampling a set of x coordinates from the legacy code and evaluate it both on the old and the new implementation.

Before doing so I tested all the optimal values, which worked (the values are the same as for the previous implementation).

For what concerns the results of the regression tests (still on the noise free version), all the tests passed except for F116 F117 F118 (ellipsoid) and F126 F127 F128 (griewank-rosenborg).

This is probably due to some differences in the inner implementation of the functions across the two versions of the coco platform, but I am still trying to figure it out...

The next step (once all test will pass for the noise-free versions), will be to check if the noisy version of the suite yields the same results as well, but now Im currently facing some problems, as the
distributions parameters for sampling the noise are not correctly allocated (or correctly passed to the sampling function), but I dont know for sure yet.

Having problems with Ellipsoid

Maybe I should use the rotated version, as the legACY code computes a rotation on it

Solved issue with Griewank-Rosenbrock and Ellipsoid function

Basically there were some parameters of the objective functions that were passed as variables or literals
and were supposed to be different across the noisy and the noise free implementation, according to the
legacy code

Example.: Default conditioning for ellipsoid was 1.0e6, which is correct for the noise free functions
but not for the noisy version, since for the legacy code the conditioning of noisy problem was just 1.0e4.
There was a similar issue with the Griewank-Rosenbrock function.

This modifications required slightly ones also in the other suites calling the allocators for those functions (to be able to pass them the correct value of the argument).
Hopefully, these modifications should not alterate the already existing behaviour of the other suites, but we'll see when the tests done at commit time are done.

Regression test completed

Cleaning the code

Regression test passed (Hopefully)

Passed the regression test against the legacy code and generated regression test data

1) Cleaning the code further.

1.1) Removed all the declarations that didn't need to be public from the `coco.h` file
1.2) Now the random seed is handles as a global variable (as in the legacy code), so there's no need to pass it as argument for the bbob_noisy problem allocator or as attribute of the noise model
1.3) Passing the noise model as argument to the constructor so that we'll only have one for the three different noise models

2) Modifying the test.

The randomness of the bbob noisy test suite implied the necessity to think about some sort of reproducibility between the runs.
Currently, the structure of the code emulates the legacy code-base, with the random seed defined as a global variable that is increased each time a noise term is sampled.
Thus, in order to obtain the same results over different runs, the order of evaluation must remain unaltered. As the regression data didn't previously store any
information about the order of evaluation (only for the functions, not for the x datapoints), this created the need to modify the way the regression data was created,
in order to store information about the order of eevaluation of the datapoints.
I then uploaded, in the modified format, the generated data (only for the bbob-noisy test suite) to the regression-data github repository of the numbbo organization.
This required some modifications for the script actually running the test, but, if I didn't make any mistake, it should work as well for the older format.

Minor mistake in commit

Still some minor fixes to the commit

Problem with the python interface.

I added the interface for getting the last noise value for debugging, but removed such function from the source code once not needed, but forgot to remove it from the inetrface

Still some minor fixes to the commit (python interface)

Cleaning the code

Error in the file testing the bbob-noisy suite against the legacy code

Updating comments to the code

Started to play around with the pycma package and cleaned a bit the src code by writing functions for allocating the distributon theta array for each distribution

Fixing issue with indexing of problems, function and other stuff

Adding best_decision_vector to the python interface

Cleaning up before PR, Removing unnecessary files

This should be the "final" commit, in the sense that it is the first commit where the results obtained
are exactly the same as the one for the legacy code.
Before I forgot to implement the boundary handling method that were adding a penalty on the decision vector.

Hopefully this is the right time, but I guess we'll have to see the results of the tests done at commit time

Removing printf statemets after debugging

Passing structures as void *

Changing the allocation of the noisy problems

removing python interface to best values/parameters

The signature of the coco_suite_allocate function changed, need to update it on the suite_bbob_noisy.c file as well, I hope this is the only reason why the tests have not passed in the first commit after the merge, but I guess that only time will tell us

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[78842d1180...](https://github.com/ss220-space/Skyrat-tg/commit/78842d1180f29bf79225dce42fa1efa2759801fe)
#### Wednesday 2023-11-22 21:49:57 by SkyratBot

[MIRROR] Adds missing default biotypes to some damage procs [MDB IGNORE] (#24461)

* Adds missing default biotypes to some damage procs (#79102)

## About The Pull Request

I noticed by complete coincidence because I happened to glance at the
channel a bunch of people complaining about blobbernauts not taking any
damage when leaving the blob in manuel round end chat.
Did anyone report this bug, even after prompting? No. Not even the game
admin who was playing as the blob.

Makes you wonder how many other bugs people are perfectly willing to
spend 15 minutes posting "i fucking hate coders" about without actually
telling anyone they exist. Sucks to be them I guess.

Anyone the cause is that some of these procs didn't have a default
biotype, so they would never take the toxin damage they were being
assigned. Now they will.

## Changelog

:cl:
fix: Blobbernauts will once again take damage when not on blob tiles.
/:cl:

* Adds missing default biotypes to some damage procs

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[922fab891f...](https://github.com/NVIDIA/Fuser/commit/922fab891f98f2cedb7fc7f8a408000e9c874309)
#### Wednesday 2023-11-22 22:01:09 by Gao, Xiang

Refactor ldmatrix and mma input scheduling (#1303)

This PR is stacked on https://github.com/NVIDIA/Fuser/pull/1311

Similar to https://github.com/NVIDIA/Fuser/pull/1210, this PR schedules
the allocation domain of mma inputs and ldmatrix. Similar to the
situation of https://github.com/NVIDIA/Fuser/pull/1210, the modified
piece of code was initially implemented prior to the invention of
allocation, therefore there were some hacks around there.

For the case of ldmatrix, if you look at the official doc
https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#warp-level-matrix-instructions-ldmatrix,
you will find that, there are basically two correct but different
schedules:
1. If you look at the memory format of which thread own which part of
the tensor, from this information, you will able to derive one schedule.
Let's call this memory-layout-based schedule.
2. If you look at which thread should pass the address of which item as
an operand to this instruction, from this information, you will be able
to derive another schedule. Let's call this indexing-based schedule.

Unfortunately, these two schedules does not match. Prior to this PR, we
were uniquely using the indexing-based schedule. This is fine with
ldmatrix, but the index of mma inputs is basically incorrect, and
therefore a hacked index was used.

I believe the most natural way to implement these two separate schedules
is as follows: Assume we have a fusion:
```C++
Tregister = ldmatrix(Tsmem)
Tregister2 = broadcast(Tregister)
... = mma(Tregister2, ...)
```
then the allocation domain of `Tregister2` and `Tregister` must be
scheduled as memory-layout-based schedule, the leaf domain of
`Tregister` must be scheduled as the indexing-based schedule. The leaf
domain of `Tregister2` should be scheduled similar to
memory-layout-based schedule.

In this PR, I refactored the mma swizzler for mma inputs to implement
the above design. In the refactored code, `scheduleTuringOperandRead`
schedules the memory-layout-based schedule, and `scheduleLdMatrix`
starts from the memory-layout based schedule, and generates the
indexing-based schedule on top of it.

Due to this change, the codegen of `MmaOp` no longer needs special
handling the index, it is now just a naive:
```C++
  void handle(const MmaOp* mma) final {
    indent() << genMmaOp(mma) << "(\n";
    indent() << kTab << gen(mma->out()) << ",\n";
    indent() << kTab << gen(mma->inA()) << ",\n";
    indent() << kTab << gen(mma->inB());
    code_ << ");\n";
  }
```

However, our current sync analysis and indexing infrastructure is not
capable of analyzes this style of scheduling, and therefore, I would
need to add additional hacking points to them:

- In our sync analysis, currently, it always assume that the
parallelization of the leaf domain determines which thread owns which
item. With the allocation domain support, it is actually the
parallelization of the *allocation* domain determines which thread owns
which item. In a perfect world, for exprs other than ldmatrix, warp
shuffling, and mma op, the analysis based on leaf domain should match
with the analysis based on the allocation, because, for example, if you
do `y = sin(x)`, there is no way that `y` get the result from other
threads, but our system should not assume that the analysis based on
leaf domain always match with the analysis based on the allocation
generally. Unfortunately, at the current state, our system can not
handle this correctly. So I added one hack to it: if the expr is
ldmatrix, assume the schedule is correct and just give up sync analysis.
I think for now, this is a valid solution, because we will be rewriting
our sync analysis with `IdModel` anyway.
- In our indexing of `MmaOp` producer, we are incorrectly marking some
of allocation domain as zero domain, where it should not be. Similar to
the above point, the mma op implies warp shuffling of data. During
indexing, it does make sense to replay consumer as producer, but only to
the block level. Within a warp, it makes no sense to replay the producer
as consumer. I think we should carefully think about the design when we
are rewriting our indexing with `IdModel`, but for this PR, I just
manually set the last three `IterDomain`s of mma input as special and
not treat them as zero domain.

I believe this PR is an improvement compared to the previous approach,
because it has less special handling in the schedule itself, but I still
think we are far from supporting ldmatrix and mma ops elegantly. In the
future, I think we should:
1. Reconsider the design of different domains, leaf vs allocation, etc.
and figure out what is the best way to schedule ldmatrix.
2. When we rewriting, we should keep the indexing of ldmatrix and mma in
mind, and make sure that it can be supported without any hack in the new
system.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7cde5062fa...](https://github.com/TaleStation/TaleStation/commit/7cde5062faf6c5a50cd7137bb59983f9e2b0c880)
#### Wednesday 2023-11-22 22:04:49 by TaleStationBot

[MIRROR] [MDB IGNORE] Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#8717)

Original PR: https://github.com/tgstation/tgstation/pull/79809
-----

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---------

Co-authored-by: _0Steven <42909981+00-Steven@users.noreply.github.com>

---
## [CollaboraOnline/online](https://github.com/CollaboraOnline/online)@[3185307c7a...](https://github.com/CollaboraOnline/online/commit/3185307c7afa5e76bd10b76a2d97ecbdbc97455a)
#### Wednesday 2023-11-22 22:22:53 by Skyler Grey

Stop hiding both menu and notebookbar softlocking

Previously, when using the Collapse_Notebookbar postmessage or
equivalent ui_defaults (SpreadsheetToolbar=false, etc.), particularly in
compact mode, it was possible to additionally hide the menu bar. As the
button to show the menu bar is on the notebookbar, this meant that you
couldn't reactivate either notebookbar or menubar until you refreshed
the page. This is particularly annoying in integrators that may not
provide an easy way to reload the page

This commit makes it so that hiding the menu bar automatically
uncollapses the notebookbar and won't let it be collapsed again. Whether
the notebook bar should be collapsed (the last thing done to it was a
collapse) is remembered and restored after the menu bar is shown again,
so if you send a postmessage that will affect the state of the
notebookbar after the menu is shown (even though it will not affect the
notebookbar's state immediately)

Caveats:
- If you are hiding the notebookbar to limit the control the user has,
  that's broken by this commit as it makes it impossible to hide both
  the menu and notebook bars at the same time.
- The notebook bar will be hidden again when re-showing the menu bar,
  however there still isn't a way to hide the notebook bar in normal
  use (i.e. without using either postmessage or ui_defaults) while in
  compact mode (although there is a workaround to show it- switching
  into tabbed mode and then back!). It might be nice to have one.

Other considered solutions:
- We could add a new button that allowed you to reopen the menu if both
  menu and notebookbar were hidden
  - Not sure there's much benefit to this over just doing what we're
    doing here, and it's harder to implement
- We could disable the button to hide the menu bar when the notebookbar
  is collapsed
  - As far as I know, there's no button in the UI to show the notebook
    bar. This would make it impossible to hide the menu bar if the
    notebookbar was hidden via postmessage or ui_defaults

Signed-off-by: Skyler Grey <skyler.grey@collabora.com>
Change-Id: Ieab6d72a6be181aba88e9a5b21dda16a369b9e54

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[15086ae683...](https://github.com/cmss13-devs/cmss13/commit/15086ae683f727d9a990e05f8ce9a08e43731207)
#### Wednesday 2023-11-22 22:32:33 by fira

Allow playing uploaded sounds through the music player w/ Webroot (#4934)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Too long have we suffered at the hands of admin auditive abuse. 

The prophet, spookydonut, once said, "You shouldn't be using this lol".
And he was right. Using "Play MIDI sound" both reduces usability for our
users, and can cause performance issues by freezing up the game for a
while as the data is transfered to these 200 poor CM addicts.

So we sought to alienate it with "Play Internet Sound" backed by
youtube-dl. Unfortunately, some things are subject to geo blocking or
simply not available on Youtube. Thus the regime of terror of Admins
continues.

This PR brings us one step closer to our goal: it allows to use the now
renamed "Play Admin Sound" to (also) upload a sound file to Webroot and
have it played through CDN. It also works with simple transport but that
mostly defeats the point.

Also reduced default volume for new players from 50% to 20%... Don't
worry, It's still way more than enough to get them to quit the server, i
have mine at 2-10% max

# Explain why it's good for the game
* Less new player abuse by reducing default volume
 * More performance by allowing big or custom songs to be backed by CDN
* Better UX: People can easily see the song name and more easily stop it
* Admins can now hide the name of played songs if they want to. Don't
ask me why.

# Testing Photographs and Procedure

![image](https://github.com/cmss13-devs/cmss13/assets/604624/4f00c45d-76ca-47e2-860a-2f26d55de2a4)
You'll have to believe me on the sound working

# Changelog
:cl:
balance: Default Web Music Player volume is now 20% down from 50%. It
was found too effective against new players.
admin: "Play Internet Sound" is now "Play Admin Sound" and optionally
allow to hide the track name.
admin: "Play Admin Sound" can now be used with uploaded tracks, which
use CDN delivery and the in-chat music player, granting players more
control over them.
admin: Removed "Play Midi Sound". 
/:cl:

---
## [Paul-Arnold/mame](https://github.com/Paul-Arnold/mame)@[e97630981c...](https://github.com/Paul-Arnold/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Wednesday 2023-11-22 22:56:47 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5f504d1de7...](https://github.com/pytorch/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Wednesday 2023-11-22 22:57:41 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [eramdam/shapeshifter-themes](https://github.com/eramdam/shapeshifter-themes)@[129ceb1216...](https://github.com/eramdam/shapeshifter-themes/commit/129ceb121673dbeaa8d8d1686612e6a985d489aa)
#### Wednesday 2023-11-22 23:09:33 by Damien Erambert

Revert "Disable Twitter posting, fuck you Elon"

This reverts commit 6f56fa2b8b8a362a9543890f2e10615d53e9e678.

---
## [DJXJD/FallGods_WEB](https://github.com/DJXJD/FallGods_WEB)@[1aabb526e2...](https://github.com/DJXJD/FallGods_WEB/commit/1aabb526e2430f4abacdd4fb36ec98a437fd426f)
#### Wednesday 2023-11-22 23:24:11 by Dominik Ziolkowski

Fixed a bitch ass bug

Fixed some cancerous bug that was due to the font not loading instantly, Literally so damn annoying, and made some changes to the scrollbar, and found a theme i think we will go with.

---
## [OpenAngelArena/oaa](https://github.com/OpenAngelArena/oaa)@[02f62cdf9a...](https://github.com/OpenAngelArena/oaa/commit/02f62cdf9ae36672a29f88d5942e973f7bda3e50)
#### Wednesday 2023-11-22 23:25:10 by Darko V

OAA balance + 7.34e (#3581)

ITEMS:
Arcane Crystal (tier 5 neutral item) bonus spell amp increased from 15% to 20%.
Arcane Crystal now also provides 20% debuff duration (like Timeless Relic).
Arcane Crystal: Fixed cast time reduction not working properly with Quick Spellcasting and Speedster modifiers.
Dispel Orb active is now activating self dispel instantly instead of after 0.2 seconds.
Disperser Manabreak mana burn on illusions increased from 8/16/24/32/40 to 8/18/28/38/48.
Disperser Manabreak mana burn on the real hero reduced from 40/60/90/130/180 to 40/50/70/100/140.
Disperser bonus damage increased from 40/50/65/85/110 to 40/50/70/100/140.
Enrage Crystal active debuff immunity now also removes Slark Pounce Leash and Invoker Deafening Blast Disarm like most other debuff immunity sources.
Enrage Crystal bonus damage reduced from 60/90/130 to 54/84/124. (same as BKB)
Enrage Crystal bonus status resistance reduced from 22/24/26% to 20/22/24%.
Greater Phase Boots active bonus attack range (for the procced attack when the wearer is a ranged hero) reduced from 150/175/200/225/250 to 150/160/170/180/190.
Linken's Sphere bonus damage increased from 10/20/35/55/80 to 10/20/40/70/110.
Reduction Orb active heal can no longer be reduced, increased or prevented.
Reduction Orb active heal per damage taken is now based on damage before reductions.
Reduction Orb active heal per damage taken reduced from 75% to 25%.
Reduction Orb active mana cost increased from 100 to 200.
Reduction Orb: Fixed Reduction Orb active heal being reduced with negative damage.
Regen Crystal active max health percent as heal reduced from 10% to 7%.
Revenant's Brooch Phantom Province magic resistance reduction duration increased from 3 to 4 seconds.
Revenant's Brooch Phantom Province magic resistance reduction rescaled from 20% to 17/18/19/20/21%
Revenant's Brooch Phantom Province max number of attacks rescaled from 6 to 5/6/7/8/9.
Shiva's Guard 4 can no longer be upgraded into Martyr's Mail.
Sonic Mask active now also provides 25/30% cast time reduction (cast speed).
Sonic Mask active now has 50 mana cost.
Spiked Mail 3 can no longer be upgraded into Stoneskin Armor 1.
Stoneskin Armor Stone Form deflected ranged attack damage is no longer lethal. (to prevent accidental denies)
Stoneskin Armor Stone Form deflected ranged attack damage is now blocked by Debuff Immunity and cannot be returned with Blade Mail, Spiked Mail etc.
Stoneskin Armor Stone Form deflected ranged attacks are now slower by 33%.
Stoneskin Armor bonus status resistance reduced from 24/26% to 22/24%.
Vampire Fang active bonus damage during the night reduced from 110/160 to 100/150.
Vampire Fang bonus attack speed reduced from 40/50 to 30/40.
Vampire Fang bonus status resistance reduced from 24/26% to 22/24%.

HEROES:
Ancient Apparition Ice Vortex dps rescaled from 20/28/36/44/60/108 to 18/24/30/36/72/108.
Anti-Mage Counterspell magic resistance rescaled from 10/20/30/40/50/60% to 15/25/35/45/50/55%.
Bane Brain Sap damage reduced from 100/200/300/400/800/1200 to 90/160/230/300/600/900.
Bane Level 15 Talent +15 Enfeeble Damage per second increased to +25.
Bane Level 25 Talent +300 Brain Sap Damage/Heal increased to +400.
Batrider Firefly cooldown reduced from 34 to 30 seconds.
Batrider Flamebreak cooldown reduced from 22/19/16/13/13/13 to 16/15/14/13/12/11 seconds.
Batrider Flamebreak dps increased at OAA levels from 60/80 to 80/120.
Batrider Flamebreak impact damage increased at OAA levels from 150/200 to 200/400.
Batrider Flaming Lasso total damage increased from 100/250/400/700/1300 to 100/300/500/900/1700.
Batrider STR gain increased from 2.2 to 2.9 per level.
Batrider Sticky Napalm damage against bosses increased from 50% to 150%.
Batrider Sticky Napalm mana cost reduced at OAA levels from 50/70 to 45/50.
Beastmaster Call of the Wild Hawk cooldown reduced at early levels from 36/34/32/30 to 33/32/31/30 seconds.
Beastmaster Call of the Wild Hawk damage increased from 60/90/120/150/300/600 to 90/120/150/180/360/720.
Bounty Hunter Shuriken Toss move speed slow increased from 20/30/40/50/60/70% to 25/35/45/55/65/75%.
Brewmaster Cinder Brew total damage increased at max level from 960 to 1280.
Brewmaster Drunken Brawler earth stance magic resistance reduced at OAA levels from 22/24% to 21/22%.
Brewmaster Drunken Brawler storm stance evasion rescaled from 10/15/20/25/30/33% to 15/20/25/30/30/30%.
Brewmaster Drunken Brawler void stance status resistance reduced at OAA levels from 25/30% to 21/22%.
Brewmaster's Fire Brewling Permanent Immolation damage radius increased from 220 to 400.
Broodmother Insatiable Hunger bonus base damage increased at max level from 110% to 120%.
Broodmother Silken Bola move speed slow increased at early levels from 10/25/40/55% to 25/35/45/55%.
Centaur Warrunner Stampede strength damage increased at max level from 5x to 6x.
Chaos Knight Phantasm mana cost increased from 75/125/175/225/275 to 100/150/200/250/300.
Chen Divine Favor damage increased from 90/160/230/300/600/1200 to 100/175/250/325/650/1300.
Chen Divine Favor physical damage shield rescaled from 100/180/240/320/640/1280 to 100/175/250/325/650/1300.
Chen Penitence cast range rescaled from 800 to 700/800/900/1000/1050/1100.
Crystal Maiden Arcane Aura bonus spell amplification rescaled from 5/6/7/8/10/12% to 4/5/6/7/9/12%.
Crystal Maiden Arcane Aura no longer provides 2/3/4/5/7/10% bonus magic resistance.
Crystal Maiden Arcane Aura now also provides 3/9/15/21/42/63 bonus intelligence.
Crystal Maiden Crystal Nova cooldown increased at early levels from 10/9.5/9/8.5 to 12/11/10/9 seconds.
Crystal Maiden Crystal Nova damage rescaled from 110/160/210/260/520/1040 to 100/175/250/325/650/1300.
Crystal Maiden Level 25 Talent +360 Crystal Nova damage reduced to +325.
Dark Willow Shadow Realm mana cost reduced at OAA levels from 200/300 to 110/120.
Dawnbreaker Celestial Hammer fire trail duration rescaled from 2.5 to 2.25/2.5/2.75/3/3.25/3.5 seconds.
Dawnbreaker Luminosity ally heal percent increased from 50/55/60/65/70/75% to 90%.
Dawnbreaker Luminosity heal penalty from creeps increased from 25% to 40%.
Dawnbreaker Solar Guardian landing damage increased from 130/190/250/500/750 to 150/225/300/525/900.
Dazzle Bad Juju cooldown reduction for items per cast reduced from 1/2/3/4/5 to 1/1.5/2/2.5/3 seconds.
Dragon Knight Elder Dragon Form cooldown increased from 70 to 80 seconds.
Dragon Knight Elder Dragon Form corrosive breath dps reduced from 25/45/65/125/125 to 25/30/35/70/70.
Dragon Knight Elder Dragon Form magic resistance reduced at max level from 40% to 30%.
Drow Ranger Level 20 Talent +25% Multishot Damage increased to +50%.
Drow Ranger Level 25 Talent +1 Multishot Waves increased to +2.
Drow Ranger Level 25 Talent +12% Marksmanship chance increased to +20%.
Drow Ranger Marskmanship proc chance reduced from 20/30/40/45/50% to 20/25/30/35/40%.
Drow Ranger Multishot cooldown reduced from 23/22/21/20/19/18 to 21/20/19/18/17/16 seconds.
Drow Ranger Multishot damage reduced at OAA levels from 200/260% to 180/200%.
Earthshaker Echo Slam cooldown reduced from 100 to 90 seconds.
Earthshaker Enchant Totem: Fixed scepter Enchant Totem having the wrong aftershock radius.
Earthshaker Fissure cooldown reduced at OAA levels from 15 to 14/13 seconds.
Faceless Void STR gain increased from 2.4 to 2.6 per level.
Faceless Void Time Lock cooldown reduced from 2 to 1.8 seconds.
Faceless Void Time Walk cast range increased at OAA levels from 825/850 to 850/900.
Grimstroke Ink Swell cooldown increased at OAA levels from 16/14 to 17/16 seconds.
Gyrocopter scepter side-gunner radius increased from 700 to 800.
Gyrocopter scepter side-gunner: Fixed Level 10 Talent improving side-gunner radius.
Huskar Inner Fire: Fixed Level 25 Talent improving the spell lifesteal by 400%.
Jakiro Dual Breath dps rescaled at OAA levels from 180/280 to 160/320.
Jakiro Level 15 Talent +325 Health changed to +30 Liquid Fire Damage.
Jakiro STR gain increased from 2.5 to 2.8 per level.
Jakiro base hp regen reduced from 5 to 0.25
Jakiro base strength increased from 25 to 26.
Legion Commander Overwhelming Odds shard bonus armor per hero increased at OAA levels from 7/8 to 8/12.
Lich Chain Frost bonus damage per jump increased at OAA levels from 35/50 to 40/55.
Lich Frost Shield cooldown reduced at early levels from 21/19/17/15 to 18/17/16/15 seconds.
Lich Sinister Gaze mana cost reduced at OAA levels from 160/240 to 90/100.
Lifestealer Feast damage reduced at max level from 2.2% to 2.1%.
Lifestealer Feast lifesteal reduced at OAA levels from 4/4.6% to 3.5/3.6%.
Lion Level 10 Talent +10% Mana Drain Slow increased to +15%.
Lion Level 20 Talent +20 Finger of Death damage per kill increased to +40.
Magnus AGI gain increased from 2 to 2.5 per level.
Magnus Empower mana cost reduced from 45/55/65/75/85/95 to 45/50/55/60/65/70.
Magnus Level 15 Talent +8 All Stats per hero hit with Reverse Polarity increased to +15.
Magnus Level 20 Talent +250 Shockwave Damage increased to +300.
Magnus Level 25 Talent +20% Empower Damage/Cleave increased to +30%.
Magnus Reverse Polarity damage increased at level 4 from 1050 to 1250.
Magnus STR gain increased from 3.1 to 3.5 per level.
Monkey King Wukong's Command scepter slow duration increased from 0.4 to 0.5 seconds.
Monkey King Wukong's Command soldier's chance to proc MK's attack increased from 25% to 40%.
Morphling Adaptive Strike (AGI) max agility multiplier increased at max level from 4.5x to 5x.
Morphling Adaptive Strike bonus agility and strength increased at OAA levels from 13/25 to 18/27.
Morphling Morph cooldown rescaled from 120/100/80/60/40 to 60 seconds at all levels.
Naga Siren Mirror Image cooldown reduced at early levels from 31/29/27/25 to 28/27/26/25 seconds.
Necrophos Death Pulse heal reduced from 55/110/165/220/440/660 to 55/80/105/130/260/520.
Necrophos Reaper's Scythe cooldown increased from 100/90/80/70/60 to 110/100/90/80/70 seconds.
Necrophos Reaper's Scythe damage per health reduced at OAA levels from 1.1/1.3 to 1.0/1.1
Nyx Assassin Vendetta bonus damage reduced at max level from 2300 to 1900.
Outworld Destroyer Sanity Eclipse base damage increased from 200/350/500/950/1400 to 200/400/600/1200/1800.
Phoenix Fire Spirits cooldown reduced from 28/26/23/20/20/20 to 23/22/21/20/19/18 seconds.
Phoenix STR gain increased from 3.3 to 3.6 per level.
Primal Beast Pulverize bonus damage per hit reduced from 30/70/110/230/350 to 20/60/100/220/340.
Primal Beast Pulverize cooldown increased from 28/26/24/22/20 to 36/34/32/30/28 seconds.
Pudge Dismember base damage per second reduced from 80/130/180/360/540 to 80/120/160/280/400.
Pudge Dismember cooldown reduced at early levels from 30/25/20 to 22/21/20 seconds.
Pudge Dismember strength damage per second increased at OAA levels from 1/1.1 to 1.2/1.5.
Pudge Flesh Heap damage block increased at level 5 from 38 to 44.
Pudge Rot scepter bonus damage rescaled from 90 to 75/80/85/90/95/100.
Pudge Rot scepter regen reduction rescaled from 20% to 5/10/15/20/25/30%.
QoP Blink shard damage reduced from 100/150/200/250/500/750 to 75/100/125/150/300/600.
QoP Level 20 Talent +220 Scream of Pain Damage reduced to +200.
QoP Scream of Pain damage increased at early levels from 75/150/225/300/600/1200 to 90/160/230/300/600/1200.
QoP Shadow Strike scepter bonus damage reduced from 75 to 60.
QoP Sonic Wave damage reduced at max level from 2600 to 2350.
Sniper Take Aim bonus attack range reduced at OAA levels from 490/580 to 450/500.
Sohei Dash: Fixed dash not working when leashed and having leash immunity (Debuff Immunity or Sonic Flight).
Sohei Dash: Fixed dash working when being affected by Tidehunter's Dead in the Water anchor.
Sohei Wholeness of Body now also removes Slark Pounce Leash and Invoker Deafening Blast Disarm like most other debuff immunity sources.
Spirit Breaker Charge of Darkness cooldown increased from 15/14/13/12/11/10 to 19/17/15/13/12/11 seconds.
Spirit Breaker Greater Bash cooldown increased from 2 to 2.3 seconds.
Sven Storm Hammer cooldown reduced at OAA levels from 12 to 11/10 seconds.
Sven Storm Hammer damage increased at max level from 960 to 1280.
Timbersaw Whirling Death stat loss percent for universal heroes increased from 5% to 7%.
Underlord Dark Rift damage increased from 250/450/650/1050/1850.
Underlord Dark Rift mana cost increased from 150/200/250/300/350 to 150/225/300/375/450.
Underlord Dark Rift radius rescaled from 375/400/425/450/475 to 430.
Underlord Dark Rift stun duration increased from 2.25/2.5/2.75/3.0/3.25 to 2.5/2.75/3.0/3.25/3.5 seconds.
Underlord Pit of Malice pit duration increased at early levels from 7/8/9/10 to 8.5/9/9.5/10 seconds.
Venomancer Noxious Plague impact damage increased from 150/300/450/750/1350 to 150/350/550/1150/1750.
Visage Familiars damage increased from 30/70/110/230/350 to 30/75/120/255/390.
Windranger Focus Fire bonus attack speed increased at OAA levels from 550/600 to 575/650.
Windranger Focus Fire cooldown reduced at early levels from 50/40/30 to 40/35/30 seconds.
Windranger STR gain increased from 2.0 to 2.6 per level.
Wraith King Reincarnation attack speed slow reduced at OAA levels from 150/225 to 75.
Wraith King Reincarnation scepter wraith form bonus attack speed reduced from 65/70/75/80/85 to 50.

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[40dfaf3734...](https://github.com/meemofcourse/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Wednesday 2023-11-22 23:25:40 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [instructure/canvas-lms](https://github.com/instructure/canvas-lms)@[63f603a397...](https://github.com/instructure/canvas-lms/commit/63f603a39787f3f206c9082762bc54934d55fc6d)
#### Wednesday 2023-11-22 23:35:33 by Ryan Hawkins

Remove old non-InstUI tool config forms

why:
- we feature flagged these, as it was a user-facing UI change. However,
  it made the code atrociously ugly and resulted in duplicated tests. We
  have turned the flag on and no one got upset, so all is well. The
  changes were very subtle anyways.
- Also, speeds up the remaining tests significantly just by replacing
  userEvent.type with userEvent.paste. As in, they take half as long
  now. Still way slower than I would like, but it'll do for now.

closes INTEROP-8132

closes FOO-3829

test-plan:
- checkout this commit and make sure your front-end assets are rebuilt.
- go to any spot the tool configuration forms can be found, such as on
  the course settings page, and make sure each of the forms loads and
  you can actually use them. We thoroughly tested the forms back when we
  first added them, so you don't have to do that much.
- make sure your screenreader can advance through the forms in a
  sensible manner.

Change-Id: Ic9979e3dd2a83d9826901a2d59ea0d3e78426c1a
Reviewed-on: https://gerrit.instructure.com/c/canvas-lms/+/330905
Tested-by: Service Cloud Jenkins <svc.cloudjenkins@instructure.com>
Reviewed-by: Tucker Mcknight <tmcknight@instructure.com>
QA-Review: Tucker Mcknight <tmcknight@instructure.com>
Product-Review: Ryan Hawkins <ryan.hawkins@instructure.com>

---

