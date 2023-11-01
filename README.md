## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-10-31](docs/good-messages/2023/2023-10-31.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,509,955 were push events containing 3,816,227 commit messages that amount to 296,950,129 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d31c21ff1b...](https://github.com/tgstation/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Tuesday 2023-10-31 00:07:34 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9e18c6575a...](https://github.com/tgstation/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Tuesday 2023-10-31 00:07:34 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[fb9c40f675...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/fb9c40f6752f19e293da244c45e48dabb9236320)
#### Tuesday 2023-10-31 00:22:19 by SpartanKadence

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
## [SingingSpock/Citadel-Station-13-RP](https://github.com/SingingSpock/Citadel-Station-13-RP)@[227b6c32f6...](https://github.com/SingingSpock/Citadel-Station-13-RP/commit/227b6c32f62bd5c690dff60166bc581b9908e2c4)
#### Tuesday 2023-10-31 00:27:43 by SpartanKadence

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
## [Oyu07/tgstation](https://github.com/Oyu07/tgstation)@[f3d81edb00...](https://github.com/Oyu07/tgstation/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Tuesday 2023-10-31 00:33:10 by Paxilmaniac

Improves the deployable component (#79199)

## About The Pull Request

The deployable component had a few random things I noticed when I tried
actually using it that kinda sucked so I'm:

Making the examine message more generic, we did NOT need to make it that
complicated.
Letting anything with hands deploy stuff, because mobs other than humans
can hold things.
Giving the option to let something be deployed more than once.
Letting direction setting be optional.
Tweaking the check for if something can be placed somewhere to be a bit
better.
## Why It's Good For The Game

I want to use the deployable component for stuff but I made it awful.
## Changelog
:cl:
code: the deployable component has been tweaked and improved with some
new options to it
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Oyu07/tgstation](https://github.com/Oyu07/tgstation)@[eb9da97b7d...](https://github.com/Oyu07/tgstation/commit/eb9da97b7da54f9bdce32aa29ec972f469625ed2)
#### Tuesday 2023-10-31 00:33:10 by GoldenAlpharex

Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

## About The Pull Request
The title says it all, really.

I always thought ice looked a bit silly, and always wondered why. Today,
I found out it was because of the `wet_floor` component adding an
overlay that suddenly made a turf that should look continuous, tiled,
which in turn gave some very ugly visuals. Ice already looks slippery,
you can tell that it's ice, and the overlay that was added to it just
didn't really help telegraph that any better than the sprite itself
already does.

That's why I added support to make it so it would be possible to force
the overlay to just not be applied to the turf that's affected by the
component, to make it all look a bit better overall.

I added it to the ice turfs as a proof of concept, although I guess it
could also be used on other turfs that are always "wet", like the
bananium floors, but I didn't really care enough to touch that yet, and
I guess the bananium floors can use it a bit better than ice did.

I did notice in this PR that the smoothing of ice seemed to potentially
be broken, but that's something to look into at a later time.

## Why It's Good For The Game
Look at this ice and how much smoother it looks like now:

![image](https://github.com/tgstation/tgstation/assets/58045821/6fc85239-e8f1-404b-bc0e-6e1fca7f7753)

## Changelog

:cl: GoldenAlpharex
code: Added support to the wet_floor component to make it so the wet
overlay could not be applied to certain turfs if desired.
fix: Ice turfs no longer look tiled, and instead look smooth when placed
next to one-another.
/:cl:

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[157fafeaa9...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Tuesday 2023-10-31 00:33:31 by lizardqueenlexi

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
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[0b8864b9ed...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/0b8864b9edae944029213246aaa36acf8f17e9c4)
#### Tuesday 2023-10-31 00:38:06 by The Bron Jame Offical

More Joke Ego (#1582)

⎓⚍ᓵꖌ FUCK||𝙹⚍YOU, CURSE OF VIOLET NOON

more joke EGO

fucked around with fluid sack code for this one

Added ᓵ⚍∷ᓭᒷ 𝙹⎓ ⍊╎𝙹ꖎᒷℸ ̣  リ𝙹𝙹リ

---
## [shellspeed1/Bubberstation](https://github.com/shellspeed1/Bubberstation)@[c539a469d5...](https://github.com/shellspeed1/Bubberstation/commit/c539a469d59849c15a115b319ec5953904863321)
#### Tuesday 2023-10-31 01:10:12 by SkyratBot

[MIRROR] Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring [MDB IGNORE] (#24120)

* Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring (#78761)

## About The Pull Request
These sprites have been adapted from a person who wished to remain
anonymous with their blessing for tg

Take the old IDs and make them look a little more fancy and sci-fi, I
think they look really nice! This makes the job marker into a cute
little screen too, but this is totally optional, if maintainers want the
animation gone It wont take long at all.
Also resprites a few random other items in the cards.dmi, such as emags,
doorjacks, hack-o-lanturn, budget cards, and one touch up on the red
team ID for laser tag for consistency.
Also prisoner IDs had black symbols and black department but orange trim
on an orange card, so it was just a huge mess.

![all the small
things](https://github.com/tgstation/tgstation/assets/81941674/7bfe75a3-bb75-45bc-9947-373f16d4096b)

## Why It's Good For The Game

I'm gonna be real IDs are kinda crusty, and its something EVERYONE has
to look at at least once a shift. Poor HOPs may even look at two. God
forbid three. Now they will look pretty neat.
As for the other changes, the hack-o-lantern looks like it was made in
2001 its OLD. I don't even know if we use it, but now its updated. The
red laser tag team got a nerf so now all team letters are white, instead
of red being orange for no reason.

## Changelog
:cl:
image: We have received a new shipment of IDs, as the old ones were
found out to be haunted.
image: Laser tag red team ID has received a massive nerf
image: Station budget cards have gotten a facelift
image: Emags and Doorjacks
fix: Numbered prisoner IDs will now be legible
/:cl:

* Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring

---------

Co-authored-by: EricZilla <81941674+EricZilla@users.noreply.github.com>

---
## [PestoVerde322/tgstation](https://github.com/PestoVerde322/tgstation)@[9cf089361e...](https://github.com/PestoVerde322/tgstation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Tuesday 2023-10-31 01:18:20 by Rhials

Abandoned Domains: Adds two new psyker-oriented virtual domains (#78892)

## About The Pull Request

_Really? Bitrunning maps are so simple you could do them with your eyes
closed? Hmmmmm..._

This adds two new medium-difficulty virtual domains to the pool -- Crate
Chaos and Infected Domain.

These two domains take you to neglected corners of the virtual world.
These are unstable, bizarre locales that do not support the bitrunning
machine's visual display, and must be traversed using echolocation.
**_These domains have been designed around you being a psyker, and will
turn your bitrunner avatar into a psyker until they leave the domain._**

_**Crate Chaos:** Low cost, medium reward._

Sneak into an abandoned virtual domain, where they store all of the loot
crates. There's about 40-ish crates in this space, and one of them
(RANDOM) is the encrypted cache we're looking for. The crates must be
manually inspected, requiring you to drop your weapon for a few moments,
but that shouldn't be a problem. There's no hostiles, just a bunch of
crates... right?

This one has very few shenanigans or threats in it. It's meant to be an
introductory experience to interfacing with things as a psyker, and
getting the rhythm down for moving between visual pulses.

_**Infected Domain:** Medium cost, high reward._

Enter another abandoned virtual domain. This one was sealed off from the
digital world after the cyber-police failed to contain a virus that
zombified its inhabitants, leaving it to grow unstable and full of
holes. Fortunately, you're provided with the single best tool for arming
yourself against zombies in any video game, ever -- Your very own
Mystery Box. Get armed with (basically) whatever gun you want, and go
put those wacky psyker abilities to use against those zombies.

This one is a lot meaner. Many chasms, landmines, and zombies. Walk
slowly, stay with your fellow bitrunners, and if it's too hard, there's
no shame in going back and rolling for a better gun!

The domains themselves are VERY simple, since there's little need for
decor or particularly complex layouts. The idea is that you should be
able to see everything you need to see in a given room/area with a
single vision pulse. Here's what one of the maps looks like:


![image](https://github.com/tgstation/tgstation/assets/28870487/fe63adce-aa05-4339-9d19-28ce06a2d31f)

Err, uh, I mean... This is what the maps look like:

<details>
<summary>SPOILERS BEWARE</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/28870487/265ecdc5-50f6-4a28-8068-fab08ae1f5e8)


![image](https://github.com/tgstation/tgstation/assets/28870487/0b41da6a-e018-4434-9368-6daee1f97fe9)

(You wanna find out if there's something cool under those red lines? Go
there yourself!)

</details>

These two psyker maps come with their own psyker safehouse too -- The
Bathroom. It's gross, the medical supplies are kind of just sitting
there on the floor... It looks a little bit better when you're blind, I
guess.


![image](https://github.com/tgstation/tgstation/assets/28870487/a10b70bb-5586-4d37-bbb1-a642d8524d54)
## Why It's Good For The Game

I like psykers a lot more than I'm willing to admit. Unfortunately, the
jankiness of echolocation provides such a disadvantage at times, that
any "real" conflict is usually over before the psyker is even aware
they're taking damage.

Fortunately, the controlled environments that bitrunning maps are
perfect for psykers. They give the opportunity to craft an experience
around the player being blind, rather than forcing them to play blind
through a seeing mans world.

These two domains should present players with a unique challenge that is
designed around playing as a psyker, with slightly higher-than-usual
rewards for their trouble. More importantly -- They're fun!
## Changelog
:cl: Rhials
add: Two new psyker-oriented virtual domains -- Crate Chaos and Infected
Domain.
add: Map helper for cyber-police corpse spawn.
add: Map helper for swapping the encrypted crate in an area with a
random crate from that same area.
/:cl:

---
## [PestoVerde322/tgstation](https://github.com/PestoVerde322/tgstation)@[66f726dfe3...](https://github.com/PestoVerde322/tgstation/commit/66f726dfe31dae0a14feaed8718c41e40e82af09)
#### Tuesday 2023-10-31 01:18:20 by SyncIt21

General code maintenance for rcd devices and their DEFINE file (#78443)

## About The Pull Request
The changes made can be best summarized into points

**1. Cleans up `code/_DEFINES/construction.dm`**

Looking at the top comment of this file 

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L1

One would expect stuff related to materials, rcd, and other construction
related stuff. Well this file is anything but

Why is there stuff related to food & crafting over here then?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L91-L94

It gets worse why are global lists declared here?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L115
There is a dedicated folder to store global lists i.e.
`code/_globalvars/lists` for lists like these. These clearly don't
belong here

On top of that a lot of construction related defines has been just
dumped here making it too large for it's purposes. which is why this
file has been scraped and it's
1. crafting related stuff have been moved to its
`code/_DEFINES/crafting.dm`
2. global lists for crafting moved to
`code/_globalvars/lists/crafting.dm`
3. Finally remaining construction related defines split apart into 4
file types under the new `code/_DEFINES/construction` folder
- `code/_DEFINES/construction/actions.dm` -> for wrench act or other
construction related actions
- `code/_DEFINES/construction/material.dm` -> contains your sheet
defines and cable & stack related values. Also merged
`code/_DEFINES/material.dm` with this file so it belongs in one place
- `code/_DEFINES/construction/rcd.dm` -> dedicated file for everything
rcd related
- `code/_DEFINES/construction/structures.dm` -> contains the
construction states for various stuff like walls, girders, floodlight
etc

By splitting this file into multiple meaningful define file names will
help in reducing merge conflicts and will aid in faster navigation so
this is the 1st part of this PR

**2. Debloats the `RCD.dm` file(Part 1)**

This uses the same concepts as above. i.e. moving defines into their
appropriate files for e.g.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L170

1. Global vars belong in the `code/_globalvars` folder so these vars and
their related functions to initialize them are moved into the
`code/_globalvars/rcd.dm` file
2. See this proc

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L200
This proc does not belong to the `obj/item/construction/rcd` type it's a
global "helper function" this is an effect proc as it creates rcd
holograms so it has been moved to the `code/game/objects/effects/rcd.dm`
file which is a global effect that can be used by anyone

And with that we have moved these vars & procs into their correct places
& reduced the size of this file . We can go even further

**3. Debloats the `RCD.dm` file(Part 2)**
This deals with the large list which contains all the designs supported
by the RCD

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L42

This list contains a lot of local defines. We can scrape some of them
and reduce the overall bulkiness & memory requirements of this list and
so the following defines

```
#define WINDOW_TYPE "window_type"
#define COMPUTER_DIR "computer_dir"
#define WALLFRAME_TYPE "wallframe_type"
#define FURNISH_TYPE "furnish_type"
#define AIRLOCK_TYPE "airlock_type"
#define TITLE "title"
#define ICON "icon"
#define CATEGORY_ICON_STATE  "category_icon_state"
#define CATEGORY_ICON_SUFFIX "category_icon_suffix"
#define TITLE_ICON "ICON=TITLE"
```

Have all been removed making this list a lot more cleaner. Why? because
a lot of these are just semantic sugar, we can infer the value of a lot
of these defines if we just know the type path of the structure the rcd
is trying to build for e.g. take these 2 defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L13-L15

These defines tell the rcd UI the name and the icon it should display.
Rather than specifying these manually in the design we can infer them
like this

```
var/obj/design = /obj/structure/window  //let's say the rcd is trying to build an window
var/name = initial(design.name)         //we have inferred the name of the design without requiring TITLE define
var/icon = initial(design.icon_state)   //we have inferred the icon of the design without requiring ICON define
```

And so by using similar logic to the remaining defines we can eliminate
a lot of these local defines and reduce the overall size of this list.

The same logic applies to the different modes of construction, the
following defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L186-L192
Have all been removed and replaced with a single value `RCD_STRUCTURE`

All these modes follow the same principle when building them
1. First check the turf if the structure exists. If it does early return
2. If not create a new structure there and that's it

So rather than creating a new construction mode every time you want to
add a new design we can use this mode to apply this general approach
every time

The design list has also now been made into a global list rather than a
private static list. The big advantage to this is that the rcd asset
cache can now access this list and load the correct icons from the list
directly. This means you no longer have to manually specify what icons
you want to load which is the case currently.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/modules/asset_cache/assets/rcd.dm#L8-L9
This has lead to the UI icons breaking twice now in the past
- #74194
- #77217

Hopefully this should never repeat itself again

**4. Other RCD like device changes**
- Fixed the broken silo link icon when the radial menu of the RLD was
opened
- replaced a lot of vars inside RLD with defines to save memory
- Small changes to `ui_act` across RCD, Plumbing RCD and RTD
- Removed unused vars in RCD and snowflaked code
- Moved a large majority of `ui_data()` to `ui_static_data()` making the
experience much faster

Just some general clean up going on here

**5. The Large majority of other code changes**
These are actually small code changes spread across multiple files.
These effect the `rcd_act()` & the `rcd_vals()` procs across all items.
Basically it
- Removes a large majority of `to_chat()` & `visible_message()` calls.
This was done because we already have enough visual feedback of what's
going on. When we construct a wall we don't need a `to_chat()` to tell
us you have a built a wall, we can clearly see that
- replaces the static string `"mode"` with a predefined constant
`RCD_DESIGN_MODE` to bring some standard to use across all cases

Should reduce chat spam and improve readability of code. 

**6. Airlock & Window names**
The rcd asset cache relies on the design name to be unique. So i filled
in the missing names for some airlocks & windows which are subjective
and open to change but must have some value

**7 Removes Microwave PDA upgrade**
The RCD should not be allowed to build this microwave considering how
quickly it can spawn multiple structures and more importantly as it's a
special multipurpose machine so you should spend some effort in printing
it's parts and acquiring tools to complete it. This upgrade makes
obsolete the need to carry an
- A RPED to install the parts
- A screwdriver to complete the frame
- The circuit board for the microwave 

The most important point to note here is that whenever an RPED/circuit
board is printed at an lathe it charges you "Lathe Tax". The RCD with
this upgrade would essentially bypass the need to "Pay Taxes" at these
lathes as you are just creating a circuit board from thin air. This
causes economy imbalance(10 cr per print) which scales up the more of
these machines you make so to avoid this let's end the problem here

Not to mention people would not find the need to print the circuit board
for a regular microwave now if they have an RCD because they can just
make this microwave type making the need for a regular microwave
completely pointless.

Just build a machine frame with the RCD and complete the microwave from
there

## Changelog
:cl:
code: moved global vars, lists and helper procs for construction related
stuff to their appropriate files
code: reduced overall code size & memory of rcd design list and removed
unused defines
refactor: removed a ton of chat alerts for rcd related actions to help
reduce chat spam
refactor: some airlock & window default names have changed
fix: broken icon in radial menu of rld silo link
remove: removes microwave pda upgrade from RCD. It's a special machine
so spend some time in building it rather than shitting them out for free
with the RCD. Use the RCD upgrade to spawn a machine frame instead & go
from there
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [danielsource/dwm](https://github.com/danielsource/dwm)@[67d76bdc68...](https://github.com/danielsource/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2023-10-31 01:19:08 by Chris Down

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
## [NotMergot/Bubberstation](https://github.com/NotMergot/Bubberstation)@[e39a44e462...](https://github.com/NotMergot/Bubberstation/commit/e39a44e4628fd8846287360e8988ff265276bfec)
#### Tuesday 2023-10-31 01:27:46 by SkyratBot

[MIRROR] Fixes display of appearance type in VV [MDB IGNORE] (#24092)

* Fixes display of appearance type in VV (#78725)

## About The Pull Request

Appearance vars are awful to detect. They have a type var you can
access, for an appearance the value of this var is `/image`. However
`istype(appearance, /image) == 0`. This is good enough for
identification, you might think this just means detecting appearance
would be something like `if(thing.type == /image && !istype(thing,
/image))`, but there's a problem with this: `istype(appearance, /datum)
== 0`. For that matter it seems like all istypes that check if an
appearance is some type fail, so you can't know that it's safe to access
the `.type` var to do that earlier combined check.

Now we get into magic territory, `istype(new /image, appearance) == 1`.
I have no clue internally why this is the case but it seems to be unique
to appearances, and so can be used to identify them from a previously
unknown var. You have to rule out that the thing you're checking is a
path, it would pass the check if the value were `/image` then, but this
is simple enough.

I hate having to know all this, so now you know this too.

:cl: ninjanomnom
admin: Appearance vars in VV now display instead of being left blank
/:cl:

* Fixes display of appearance type in VV

---------

Co-authored-by: Emmett Gaines <ninjanomnom@gmail.com>

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[9d69f3aecf...](https://github.com/sleepynecrons/cmss13/commit/9d69f3aecf6a0070861688c5648479e8db6b679d)
#### Tuesday 2023-10-31 01:37:53 by fira

Fixes bugs with designator usage (#4693)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

The Laser Designator is a JTACer's workhorse and it's CLUNKY AS HELL. 

This fixes two main bugs:

* The `interactee` is not properly cleared when using the designator (or
any zoomed item), causing it to be unset instead of set the next time
you use it. This means if you look up then back down your designator,
you can't laze.

* The interaction system wasn't made with movement in mind. It is a
problem because zoom system allows movement, and designators are where
the two meet. Now, they can explicitely keep interaction despite
movement.

# Explain why it's good for the game

QoL that should have been done 6 years ago, give or take

Because Zooming interactions are an awful mess, i'm flagging this for
Testmerge where it'll inevitably break down

# Testing Photographs and Procedure
I take designator, i look, i try to laze. I put them down, move, do it
again. And again. Several combinations of actions.

The unzoom logic is blatantly busted and out of scope of the PR.

# Changelog
:cl:
fix: Fixed Rangefinders/Designators preventing you from lazing if you
looked up/down them without moving.
fix: Fixed Rangefinders/Designators forcing you to look up/down again if
you had moved while using them.
/:cl:

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[6bdf052a84...](https://github.com/VladinXXV/tgstation/commit/6bdf052a84c07ff54065dd7906d9c9da540a07b8)
#### Tuesday 2023-10-31 01:42:32 by lizardqueenlexi

Converts cursed heart effect into a component. (#78554)

## About The Pull Request

Fixes #58401 
Fixes #58799
Fixes #58800

Converts the manual heart-beating effect of the cursed heart into a
component.

Behavior has mostly been maintained, but polished a bit as compared to
the original cursed heart. Most notably, the action for beating your
heart is now a cooldown action - providing a visual indicator of when
you can beat it again, rather than leaving you guessing. Some better
checks have also been put in place for edge cases such as having your
species changed.

Implementation inspired by the existing "manual blinking" and "manual
breathing" components. Currently only used by the cursed heart and the
(now majorly simplified) effect of corazargh.

My first component, so hopefully I didn't miss anything.
## Why It's Good For The Game

The cursed heart was kind of unusably bad - which may have been part of
the intent, but having to count in your head or spam-click the button is
just annoying. With a visual indicator of when you should beat your
heart, hopefully it will be slightly less awful for the cursed.

The real motivation here was that corazargh's implementation was kind of
a travesty - summoning a cursed heart inside of your body while it was
in your system, then restoring your old heart afterward. This was
error-prone as well as just being ridiculous. Making this effect a
component gets rid of these problems, and leaves space open for new uses
of manual heart beating if anyone feels like being cruel.
## Changelog
:cl:
fix: Your heart will no longer be deleted if an admin heals you while
you have corazargh in your system.
refactor: The cursed heart has been streamlined a bit, and now gives you
a visual cooldown for when you can beat your heart again.
/:cl:

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[66a1cd6ab2...](https://github.com/VladinXXV/tgstation/commit/66a1cd6ab2c46d84c6773d94fabb08f10c3e6fcd)
#### Tuesday 2023-10-31 01:42:32 by Wallem

Adds The Hand of Midas, an ancient Egyptian gun. (#78699)

## About The Pull Request
Adds the Hand of Midas (HoM), a weapon for pirate captains.

This matchlock pistol is powered by gold rather than gunpowder.
If you hit someone with it, they will be afflicted with Midas Blight for
a duration of time that scales with how much gold is in your gun.
Midas Blight will slowly turn their blood into gold, and slow them down
depending on how much blood is in their system.
If you right-click on someone with the HoM, it will siphon all gold from
their bloodstream and recharge the gun, curing them of Midas Blight in
the process if they still have it.
The amount of gold you can get from people is meant to be ~1.5x as much
as you fired into them in the first place, if you get your timing right.
This way you can exponentially scale the power of your weapon if you can
hit your shots, with a limit of 30 Seconds on the Blight timer.
The siphon has a range of 2 meters, and if you miss a shot you can input
a gold coin into the gun to refill it with the same weak shot you
started with.

It's a little hard to explain in text so here's some video examples:


https://github.com/tgstation/tgstation/assets/66052067/d49238fc-beb2-4ba9-be0c-83e8a701c995


https://github.com/tgstation/tgstation/assets/66052067/34dc23e7-2b88-4ee9-bb1e-c8067a491975


https://github.com/tgstation/tgstation/assets/66052067/68a07426-ba6c-43a7-8228-132fc4b02b83

## Why It's Good For The Game
Honestly I just had the idea for the gun and thought it would be really
cool lmao.
Also because Barrel Behind the Door is one of the funniest YuGiOh cards,
the censored design is TOO GOOD.


![image](https://github.com/tgstation/tgstation/assets/66052067/7c930287-410d-43bd-8731-0f7224b9f049)
## Changelog
:cl: Wallem
add: Adds The Hand of Midas, an ancient Egyptian matchlock pistol.
/:cl:

---
## [JarRaid/HorrorGame](https://github.com/JarRaid/HorrorGame)@[227bec7b9d...](https://github.com/JarRaid/HorrorGame/commit/227bec7b9d91f1256063442bbff6d438a2877c60)
#### Tuesday 2023-10-31 01:47:49 by salataa1

Chandelier and window 4 update

Added other andrew's shitty ass chandelier that i had to basically redo the unwrap for. made it as pretty as I could. If he submits one in his push for the merge, use this one instead. also changed the alpha map on the top down view of the church window to reflect the nursery location we're going with

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[3f102ddc22...](https://github.com/Offroaders123/Art-Gen/commit/3f102ddc22b5cde0e466766993aa7b326ecab2f8)
#### Tuesday 2023-10-31 02:35:40 by Offroaders123

Separate CLI

Oh my gosh this is awesome
https://www.youtube.com/shorts/u8Ev59SERe0
https://www.youtube.com/watch?v=8UzSHCdmStE

Who knew all of the extra heavy bands were from northwest Canada hahaha. Same with Tanner Benedict, which I think we are dopplegangers haha.
https://www.youtube.com/@tannerbenedict3451

---
## [gradle/gradle](https://github.com/gradle/gradle)@[2805c3fda2...](https://github.com/gradle/gradle/commit/2805c3fda24da90bb9544ec197335259d983b2cd)
#### Tuesday 2023-10-31 03:02:12 by bot-gradle

Merge pull request #26874 Improve performance of RelativePath canonicalization

This is a follow-up to https://github.com/gradle/gradle/pull/24943.

There was some uncertainty as to whether that change resulted in a detectable drop in performance in Gradle's overall performance tests. I put together [some benchmarks](https://github.com/AlexLandau/gradle-relative-path-perf) looking at the constructor method that was modified, and based on my probably-non-representative sample of test cases, the new implementation took around 3.4x as long as the one that did not perform canonicalization.

The version in this PR skips running canonicalization checks on segments that come from existing `RelativePath` objects, which have already been canonicalized. This implementation actually performs better than the original, pre-canonicalization implementation in my benchmark test; I would take this with a grain of salt, as I do not have experience with JMH and may have used a poor setup or poor choice of test cases. (There's at least some evidence that for the range of test cases attempted, copying into the array with a for loop is faster than `System.arraycopy`, which would explain this. This could, of course, vary across JVM versions and other factors.)

### Contributor Checklist
- [x] [Review Contribution Guidelines](https://github.com/gradle/gradle/blob/master/CONTRIBUTING.md)
- [x] Make sure that all commits are [signed off](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff) to indicate that you agree to the terms of [Developer Certificate of Origin](https://developercertificate.org/).
- [x] Make sure all contributed code can be distributed under the terms of the [Apache License 2.0](https://github.com/gradle/gradle/blob/master/LICENSE), e.g. the code was written by yourself or the original code is licensed under [a license compatible to Apache License 2.0](https://apache.org/legal/resolved.html).
- [x] Check ["Allow edit from maintainers" option](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) in pull request so that additional changes can be pushed by Gradle team
- [ ] Provide integration tests (under `<subproject>/src/integTest`) to verify changes from a user perspective
- [ ] Provide unit tests (under `<subproject>/src/test`) to verify logic
- [ ] Update User Guide, DSL Reference, and Javadoc for public-facing changes
- [x] Ensure that tests pass sanity check: `./gradlew sanityCheck`
- [x] Ensure that tests pass locally: `./gradlew <changed-subproject>:quickTest`

### Reviewing cheatsheet

Before merging the PR, comments starting with
- ❌ ❓**must** be fixed
- 🤔 💅 **should** be fixed
- 💭 **may** be fixed
- 🎉 celebrate happy things

Co-authored-by: Alex Landau <alandau@cs.stanford.edu>

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[6d51cb8174...](https://github.com/vdaular-dev/linksfordevs/commit/6d51cb8174394d6155113cd61a72d3be0c556d80)
#### Tuesday 2023-10-31 03:20:05 by Ben Dornis

Updating: 10/30/2023 9:00:00 PM

 1. Added: eval should not be a built-in function
    (https://nickdrozd.github.io/2023/10/27/python-eval.html)
 2. Added: For Maximum Accessibility, Be Careful About Using a .dev Domain
    (https://macarthur.me/posts/dot-dev-problems)
 3. Added: Self-hosted analytics: How to track 53% more views
    (https://cretezy.com/2023/self-hosted-analytics)
 4. Added: Mean vs. median
    (https://jensrantil.github.io/posts/mean-vs-median/)
 5. Added: Why designers design forms
    (https://grillopress.github.io/2023/10/27/why-we-design-forms.html)
 6. Added: 🥦 The Curse of Healthiness | vincelwt.com
    (https://vincelwt.com/healthy)
 7. Added: I'm a hacker, but it's not what you think
    (https://www.biccs.tech/posts/being-a-hacker-is-not-what-you-think)
 8. Added: Daylight confusion week - Tyler Cipriani
    (https://tylercipriani.com/blog/2023/10/29/daylight-confusion-time/)
 9. Added: How to sell your micro startup as a solopreneur
    (https://marclou.beehiiv.com/p/how-to-sell-your-micro-startup)
10. Added: Gregory Szorc's Digital Home | My User Experience Porting Off setup.py
    (https://gregoryszorc.com/blog/2023/10/30/my-user-experience-porting-off-setup.py/)
11. Added: Checking References
    (https://www.kevinfox.dev/checking-references.html)
12. Added: Microretros
    (https://jensrantil.github.io/posts/microretros/)
13. Added: Deploying Rails on a single server with Kamal
    (https://nts.strzibny.name/deploying-rails-single-server-kamal/)
14. Added: You're Gonna Need A Bigger Browser
    (https://berjon.com/bigger-browser/)
15. Added: My Data-Backed Battle and Defeat of Hypertension
    (https://dennisforbes.ca/articles/treating_high_blood_pressure.html)
16. Added: Why I Am a Pluralist
    (https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/)
17. Added: not easy
    (https://meskhetian.com/not-easy/)
18. Added: On .NET Live - Scheduling background jobs with .NET
    (https://youtube.com/watch?v=7M0lDPCeM10)
19. Added: Everything wrong with tech in 2023 (in no particular order) — Joan Westenberg
    (https://joanwestenberg.com/blog/everything-wrong-with-tech-in-2023-in-no-particular-order)
20. Added: The Church of AGI
    (https://blog.piekniewski.info/2023/10/21/the-church-of-agi/)
21. Added: Wolverine and Serverless
    (https://jeremydmiller.com/2023/10/30/wolverine-and-serverless/)

Generation took: 00:15:54.3644083
 Maintenance update - cleaning up homepage and feed

---
## [psong5/Twitter-Hate-Speech-Detection-Using-Various-Machine-Learning-Models](https://github.com/psong5/Twitter-Hate-Speech-Detection-Using-Various-Machine-Learning-Models)@[cbe5417e14...](https://github.com/psong5/Twitter-Hate-Speech-Detection-Using-Various-Machine-Learning-Models/commit/cbe5417e14ffa42a211375f3d9b19cca81a8f972)
#### Tuesday 2023-10-31 03:23:43 by psong5

Update README.md

ABSTRACT

The proliferation of social media and video-games has increased the level of online communication worldwide, necessitating the development of a machine that can discern between hate speech, offensive content, and neutral or positive exchanges. In light of the hate speech issue, I have explored various models - Logistic Regression, Decision Tree, Random Forest, SVC and LSTM - with Word2Vec using Twitter data to determine the most effective combination for identifying and detecting online hate speech. Online toxic behaviour - which I have personally experienced playing video-games - exacerbates the mental health crisis among youth, contributing to depression, insecurity, and even teenage suicide rates. In addition, the pressure of life-changing decisions like college applications makes this demographic even more susceptible to the harmful consequences of online hate speech. In order to address this issue, I experimented with Word2Vec and non-deep learning algorithms and more complex architectures like LSTM. Out of all the baseline models - Random Forest, Decision Tree, Logistic Regression, and SVC - the combination of Word2Vec and SVC had the maximum accuracy and recall of 85.6%, precision of 80.8%, and F1 score of 83.1%. However, with the LSTM model, I achieved a higher accuracy of 92.1%, recall of 91.7%, precision of 93.4%, and F1 score of 92.6%. Drawing on these results, it is reasonable to conclude that in a high-context problem like detecting hate speech, it is crucial to use more contextual models or neural networks like LSTM.

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[6a6926c323...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/6a6926c323d3795979c9960db4ecb2572db3c0b4)
#### Tuesday 2023-10-31 04:21:45 by Coxswain

Adds distorted form

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

damage coeff update

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[3b38037121...](https://github.com/ReturnToZender/ReturnsBubber/commit/3b38037121f5d3459209877e9b43246fcf987b69)
#### Tuesday 2023-10-31 04:28:44 by BurgerLUA

[Testmerge Ready] Adds the RB-MK2 Reactor, Makes Tritium buyable from Cargo (#598)

## About The Pull Request


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/5985d911-ece0-42b9-b73a-08976488a2af)

This PR adds tritium based nuclear combustion reactors that converts
tritium into power. The reactor itself is only 1 tile in size and you
are expected to build multiple reactors in order to get a good source of
power going. It is currently obtainable by research, and the rods and
machine itself can be printed at the engineering protolathe, It can be
upgraded via stock parts for crazy power generation.

More tritium in a rod means less time to manage it, but it also means
that the rod's pressure can possibly get too high. There is nothing
stopping you from filling it up with other gases to moderate it, such as
freon if you're brave.

The RB-MK2 engine requires a source of cooling, but not too much
cooling, in order to produce a good amount of power. There is a safety
feature to prevent it from running too hot or too overpressured, but
that can be disabled by cutting the safety wire. There are also several
wires to allow for signal based management if you feel so inclined to
add such a thing to the setup.

### Current wire setup:

| Wire | Pulse | Cut | Mend  |
| --- | --- | --- | --- |
| Overclock | Enables/Disables overclocking | Nothing | Disables
overclocking |
| Activate | Toggles the reactor on/off | Turns reactor off | Turn
reactor on |
| Disable | Turns reactor off | Nothing | Turns reactor off |
| Throw | Ejects the rod, if off | Nothing | Ejects the rod, if off |
| Lockdown | Toggles vents open/closed | Nothing | Turns vents off |
| Safety | Toggles safety on/off | Turns safety off | Turns safety on |
| Limit | Increases the cooling limit percent by 5% | Nothing | Resets
the cooling limit to 0%

### How to Operate

1. Construct the RB-MK2 on a powergrid inside a room with cooling.
1. Fill an RB-MK2 rod with 50 moles of room temperature tritium.
2. Insert the rod into the RB-MK2
3. Wrench the RB-MK2 to turn it on.
4. Let the RB-MK2 run hot, but not too hot to the point where the RB-MK2
rod bursts.
5. If it jams, use a crowbar on it. Or a plunger.
6. If it is too damaged, use a welder on it.
7. ????
8. Profit.

### Tips
- To turn the machine on, insert a rod filled with tritium in the hole
and then wrench it. If you don't have a wrench, you can pulse the
activate wire while the rod is in.
- Rods should be filled up with at most 50 moles of tritium, but more
can be added if you're feeling dangerous.
- You can put other gasses inside a rod if you want said gasses to leak
out during processing.
- The RB-MK2 can be upgraded. Matter bins increase the internal buffer's
volume, servos increase the pressure at which the fans will release gas,
and capacitors will increase the power output of the reactor (this can
result in higher temperature gains) per mole of tritium.
- Overlocking increases tritium consume and gives off more heat, but
provides more power.
- To activate the machine, use a wrench on it. It is considered active
when the rod is all the way down.
- An exposed rod (inactivated machine) is more affected by external
temperatures than an inactive rod. This can sometimes be worse than it
being unexposed if the exterior turf temperature is too hot.
- The machine will only process tritium (and generate power) wile
active.
- Opening the vents (aka disabling lockdown) allows processed gas to
escape out of the buffer and allow exterior temperature to influence the
internal rod temperature.
- Closing the vents will prevent exterior temperature from affecting the
rod, and prevent waste gas from escaping. This is useful for if you want
to increase the temperature by closing the vent or in cases of a chamber
fire.
- Throwing the rod, or removing it manually, prevents the rod from
taking on any more heat/cooling. This does not stop internal reactions,
if there are any inside the rod.
- Increasing the cooling limit will reduce the cooling effect external
air has on the rod. This is useful to increase if your cooling setup
makes the rod too cold to process power effectively.
- There is a safety feature on the machine where if the rod gets too hot
or too overpressured, it will automatically turn off and expose itself
to external air. Disabling safeties is only useful if you want the
machine to blow up, or if you don't want the rod to automatically expose
itself (in case of a chamber fire).
- Goes good with radiation shielding as tritium is a byproduct of
radiation shielding, and radiation shielding requires a lot of power to
function.



## TODO

- [x] Actually make sure it works (it doesn't).
- [x] ~~Introduce liquid reagent cooling mechanics where water puddles
can help with cooling management.~~ Not possible because liquid reagents
are shit.
- [ ] Balance it so it isn't more of a pain in the ass to manage than a
supermatter.
- [x] Maybe add safety features like temperature monitoring and other
stuff so engineers aren't 100% blind.
- [x] Replace Burgerstation default Supermatter setup with this one.
- [x] Testmerge!
- [x] Get feedback from engineer mains.

## Why It's Good For The Game

More sources of funny power is good.

## Changelog

:cl: BurgerBB
add: Adds the RB-MK2 reactor.
add: Makes Tritium buyable from cargo.
/:cl:

---------

Co-authored-by: StrangeWeirdKitten <95130227+StrangeWeirdKitten@users.noreply.github.com>

---
## [MaxL0MaxIT/pamaxos](https://github.com/MaxL0MaxIT/pamaxos)@[3bd0e56f75...](https://github.com/MaxL0MaxIT/pamaxos/commit/3bd0e56f75271b46cd65b774accb136ceab60686)
#### Tuesday 2023-10-31 04:32:07 by MaxL0MaxIT

Create README.txt

-----------------------------------------------------------
Русский:
PaMax:
Всем привет дорогие друзья!
Вчера утром я начал создавать свою
Мини-операционную систему в CMD-консоли.
Система сделана на языке программирования
Python там есть много всего. Например:
Игры, мини-программирование, программы.
Вся система управляется через простые
Команды, которые можно посмотреть через
Команду help. Я очень рад, что создал
Свою собственную Мини-операционную систему!
Это был очень интересный и познавательный опыт.
Благодаря этому проекту, я узнал много нового
О программировании и операционных системах.
Мне нравится, что моя система такая маленькая и простая,
Но в то же время она содержит все необходимые функции
Для комфортной работы. Я надеюсь, что в будущем смогу
Улучшить и расширить свою систему, чтобы она стала еще
Более полезной и удобной для использования. Поэтому вы
можете скачать её совершенно бесплатно!

Английский:
PaMax:
Hello dear friends!
Yesterday morning I started creating my own
A mini-operating system in the CMD console.
The system is made in a programming language
Python has a lot of stuff there. For example:
Games, mini-programming, programs.
The whole system is controlled through simple
Commands that can be viewed via
The help command. I am very glad that I created
Your own Mini-operating system!
It was a very interesting and informative experience.
Thanks to this project, I learned a lot of new things
About programming and operating systems.
I like that my system is so small and simple,
But at the same time it contains all the necessary functions
For comfortable work. I hope that in the future I can
Improve and expand your system so that it becomes even more
More useful and convenient to use. Therefore, you
can download it for free!

---
## [Natural123456/naturalprivatelabel001](https://github.com/Natural123456/naturalprivatelabel001)@[8bb982c7f0...](https://github.com/Natural123456/naturalprivatelabel001/commit/8bb982c7f0b598b11a3af6d6e763c0cc5d110593)
#### Tuesday 2023-10-31 04:36:36 by Natural123456

Update README.md

Introduction

In today's fast-paced and highly competitive business world, companies are constantly seeking innovative ways to expand their product offerings, increase brand visibility, and meet customer demands. One strategy that has gained significant traction in recent years is white label manufacturing. White label manufacturing services allow companies to leverage the expertise of specialized manufacturers to create high-quality products under their own branding. In the United Kingdom, the concept of "Natural White Label" has gained popularity, emphasizing a commitment to sustainable and eco-friendly products. In this blog, we'll explore the world of white label manufacturing services in the UK, with a focus on the Natural White Label approach.

The Rise of White Label Manufacturing

White label manufacturing, also known as private label or OEM (Original Equipment Manufacturer) manufacturing, involves partnering with specialized manufacturers to produce products under your brand name. This approach has become increasingly popular for several reasons:

Faster Market Entry: White label manufacturing allows businesses to enter new markets quickly and cost-effectively, as they can leverage existing manufacturing capabilities and expertise.

Cost Efficiency: Companies can reduce the costs associated with product development, manufacturing, and quality control by outsourcing production to white label manufacturers.

Focus on Core Competencies: Businesses can concentrate on their core competencies, such as marketing, distribution, and customer service, while leaving manufacturing to experts.

The Natural White Label Approach

In the UK, the concept of "Natural White Label" has gained momentum as consumers become more environmentally conscious and prioritize sustainable, eco-friendly products. Natural White Label manufacturing services align with this trend by emphasizing the following principles:

Sustainable Sourcing: Natural White Label manufacturers prioritize the use of eco-friendly materials and sustainable sourcing practices. This includes responsibly harvested wood, recycled plastics, and renewable energy sources.

Environmentally Friendly Production: Manufacturers adhere to green production practices, including reducing waste, energy efficiency, and eco-conscious disposal of byproducts.

Ethical Labor Practices: Natural White Label manufacturers often employ fair labor practices and uphold social responsibility standards, ensuring their workforce is treated ethically and paid fairly.

Minimal Packaging: Reducing unnecessary packaging and promoting the use of recyclable or biodegradable materials is a cornerstone of the Natural White Label approach.

Eco-Certifications: Many Natural White Label products come with eco-certifications, providing consumers with peace of mind that they are making an environmentally responsible choice.

Benefits of Natural White Label Manufacturing Services

Eco-Conscious Branding: Leveraging Natural White Label manufacturing can enhance your brand's reputation, attract environmentally conscious customers, and align with corporate social responsibility goals.

High-Quality Products: By partnering with specialized manufacturers, you can ensure that your products meet the highest quality standards.

Time and Cost Efficiency: Outsourcing manufacturing to experts can significantly reduce lead times and costs associated with in-house production.

Diverse Product Range: White label manufacturing allows businesses to diversify their product range, catering to a broader customer base without investing heavily in research and development.

Conclusion

The white label manufacturing landscape in the UK has evolved to meet the demands of a market focused on sustainability and eco-friendliness. The Natural White Label approach represents a powerful way to not only expand your product line but also do so in a manner that aligns with the values of modern consumers. By partnering with manufacturers who share your commitment to sustainability, you can create a compelling brand identity that resonates with customers, all while enjoying the benefits of efficient production and high-quality products. Whether you are an established brand looking to expand or a startup aiming to make your mark, Natural White Label manufacturing services in the UK provide a promising avenue for growth.

---
## [SemiMute/DungeonNons](https://github.com/SemiMute/DungeonNons)@[0260511c47...](https://github.com/SemiMute/DungeonNons/commit/0260511c47214cb56a700856d297572b1a091d6d)
#### Tuesday 2023-10-31 04:38:42 by yannzin

Added name changers

uses semimute's customResponses.json to change stuff based on stuff

if you think my code is ugly, I'd like to see you try and fix it. I ain't touchin that shit with a 10 foot pole

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[0c55aebcae...](https://github.com/EaW-Team/equestria_dev/commit/0c55aebcae844d845ab72d6a9fc2e428290d6d59)
#### Tuesday 2023-10-31 07:01:22 by Mustafa Alperen Seki

Actually add the FAT female generics.

My stupid ass saved them to wrong place and forgor to copy them to the repo, my fault not resting it.

---
## [Gel-All-Sports-Movie-TV/Gel-All-Sports-Movie-TV](https://github.com/Gel-All-Sports-Movie-TV/Gel-All-Sports-Movie-TV)@[58583c4ae5...](https://github.com/Gel-All-Sports-Movie-TV/Gel-All-Sports-Movie-TV/commit/58583c4ae5d3e12e57d722fababf0f8705cf6717)
#### Tuesday 2023-10-31 07:55:42 by Gel-All-Sports-Movie-TV

hot s e x xxx JAPAN sex Sex Videos playlist youtube F𝐢LM SEMI S𝐞X HONGKONG| make Love – couple Sex – XXX 18 Sex movies - jav - Korean Hot 2023

Full Watch Videos :: http://4ty.me/sbqrp3

Ps5 Giveaway  | Fastest Fingers In The East
http://4ty.me/2gajfp

What is Nuru Massage? Nuru is a style of massage that originated in Japan.   It is a sensual massage between partners using full body contact to relax the body and stimulate mutual sexual appetite.  The massage is done with both partners fully nude, using a thick, ultra slippery massage gel.  Wet Nuru™ Massage Gel is available in two formulas, Original and Concentrate, both with moisturizing Aloe Vera, Seaweed and Grapeseed Extracts and soothing Chamomile Flower extract.  These formulas are designed for long-lasting play.  Wet Nuru™ Massage Gel is made in the U.S.A. with the highest quality ingredients.

Nuru Body-on-Body Massage Gel is made by the makers of your favorite personal lubricant, Wet Platinum Premium Lubricant.  

Fishbowl Wives 2022   Full Review,After my husband died, brother in law come to visit me 101   Japanese Story Movie   Cinematic Music,Together Young - Spanish / sub Eng / Full Movie,【ENG SUB】Love in the 1980s | Drama/Romantic Movie | China Movie Channel ENGLISH,Getaway of Love 2015 - Full Movie HD Italian Subs English by Free Watch - English Movie Stream,Young President & His Contract Wife | Sweet Love Story Romance film, Full Movie HD,Rinko Wants to Try  EP 3 sub Eng #japanesedrama,Heavenly - Cigarettes after sex Brooke Shields,He soaps his babysitter's back,Oshin Japanese movie with English sub,asian lesbian LGBT pride short movie. Neck Music.,Practice Run - Full Lesbian Short Film,大王看中兒子的未婚妻，竟将儿媳按到床上求欢，太可怕了 💖 Chinese Television Dramas,New Anime 2023 English Dub All Episodes Full-Screen HD | Complete Season,A 16yrs Böy Who Împrégnaté All His Housé Maîds Including His Sîstér And Áunt | Story | km - 1,Ninja Cheerleaders | Full Movie | Action Martial Arts Comedy,The Sculpture La scultura | Film Italiano | Full Italian Drama Romance Movie | WORLD MOVIE CENTRAL,Full movie CRUSH | Comedy Drama | Lesbian Love Story HD,No Touching At All Doushitemo furetakunai 2014 BL | Full Gay Movie | Gay Kiss |With Eng sub,Manhattan Romance | Full RomCom Movie | Arnold C. Baker II | Jessie Barr | Tommy Burke,The Nun and the Devil 1973 - Full Movie by Free Watch - English Movie Stream,Behind A Masquerade Of Rhymes 2021 | Lesbian Romance Movie | Women Loving Women | LGBTQIA+,Kittens In A Cage | FULL Lesbian Musical Comedy Series | We Are Pride | LGBTQIA+,37 Years Older Woman - 17 Years Teenage Boy"s Relationship Movie Explained by adams verses  #older 😍,“From A to Q” - New lesbian short film FULL | Queer, LGBTQ+, Gay, Bisexual, Pride,1974#LoversandOtherRelatives,🌀 The Punishment | DRAMA | Full Movie with English Subtitles,22 years old Boy madly in love with his Married Sister | Movie Recap,White Apache | WESTERN | Full Movie English | Free Feature Film | Cowboy Film,Jumping the Broom 2011 - Vow of Chastity Scene 3/10 | Movieclips,2 Teach3rs Fall For A Sch00l Stud3nt And Doing Everything | Korean Thriller Movie Explained In Hindi,Time of Love sub Eng full movie,Second Chance - Turkish Movie | Romantic💖English Subtitles,TRUE STORY‼ Rich Woman Kept A Boy To Be Slave For 10 Years In The Attic,Japan bus vlog no3,All-In-One Edit | Growing Season | EP.01~EP.12 Click CC for ENG sub,More Beautiful for Having Been Broken | Free Drama Film | Zoe Ventoura,sexy anime video #shorts #anime #kiss,See Jane Date | Official FULL MOVIE | 2003 | Romantic Comedy | Charisma Carpenter,FUNERAL HOME | Cries in the Night | Barry Morse | Lesleh Donaldson | Full Length Movie | English,Rita Sue and Bob Too 1987 HD BluRay by Andrea Dunbar and Alan Clarke FULL FILM,Kyoto Japanese Massage Relaxing Muscle and Relieving Stress Good ASMR Skill Best Technique ASMR Cute,[Eng Sub BL] Teacher and Student ครูและนักเรียน,Pregnant Wife has Revenge S*x infront of Cheating Husband ,Ciara - Love Sex Magic ft. Justin Timberlake,Violence in a Women's Prison | Crime | Drama | Full Movie in English,hot kiss kissing scene netflix kdrama scenes that gave me butterflies kisses video romantic kdrama,This Kissing scene 👄🤌| Shooting Stars ✨| #shorts #kdrama #koreandrama,In Love With Him  - NIGERIAN MOVIES #nigerianmovies,GIRLS IN UNIFORM LESBIAN MOVIE LOVE STORY DRAMA SUBTITLES MÄDCHEN IN UNIFORM 1958,

---
## [mozilla-mobile/mozilla-vpn-client](https://github.com/mozilla-mobile/mozilla-vpn-client)@[6d06039627...](https://github.com/mozilla-mobile/mozilla-vpn-client/commit/6d06039627bb57e424cfaf2ee47d35de1a6679f7)
#### Tuesday 2023-10-31 08:12:14 by Beatriz Rizental

Enable sign in cancel button click test

Ok, this is just a bit hacky. The test was failing because that button is
below the fold. We'd have to scroll down to actually click on it. However,
I cannot figure out how to scroll down for the life of me. I talked to Matt L.
and he showed me the fun fact that if you click right on the fold without
scrolling turns out you already reach the cancel button.

Now, tests are clicking in the middle of elements. So what I did is I changed
the test to actually click at the top right corner of the element. In practice,
this makes no difference. So instead of embarking in yet another rabbit hole
to fix this, I refrained.

---
## [Sukitly/langchain](https://github.com/Sukitly/langchain)@[dff24285ea...](https://github.com/Sukitly/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Tuesday 2023-10-31 08:33:48 by Nikhil Jha

Comprehend Moderation 0.2 (#11730)

This PR replaces the previous `Intent` check with the new `Prompt
Safety` check. The logic and steps to enable chain moderation via the
Amazon Comprehend service, allowing you to detect and redact PII, Toxic,
and Prompt Safety information in the LLM prompt or answer remains
unchanged.
This implementation updates the code and configuration types with
respect to `Prompt Safety`.


### Usage sample

```python
from langchain_experimental.comprehend_moderation import (BaseModerationConfig, 
                                 ModerationPromptSafetyConfig, 
                                 ModerationPiiConfig, 
                                 ModerationToxicityConfig
)

pii_config = ModerationPiiConfig(
    labels=["SSN"],
    redact=True,
    mask_character="X"
)

toxicity_config = ModerationToxicityConfig(
    threshold=0.5
)

prompt_safety_config = ModerationPromptSafetyConfig(
    threshold=0.5
)

moderation_config = BaseModerationConfig(
    filters=[pii_config, toxicity_config, prompt_safety_config]
)

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

try:
    response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})
except Exception as e:
    print(str(e))
else:
    print(response['output'])

```

### Output

```python
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.


> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.
Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like XXXXXXXXXXXX John Doe's phone number is (999)253-9876.
```

---------

Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Anjan Biswas <84933469+anjanvb@users.noreply.github.com>

---
## [cozy-labs/cozy-desktop](https://github.com/cozy-labs/cozy-desktop)@[79d41d7823...](https://github.com/cozy-labs/cozy-desktop/commit/79d41d7823610303a975a3756614e45b801ac304)
#### Tuesday 2023-10-31 09:01:21 by Erwan Guyader

Release v3.21.0 (#1908)

Improvements for all users:

- Moving a document to an ignored location (see https://github.com/cozy-labs/cozy-desktop/blob/master/core/config/.cozyignore
  and your local `.cozyignore` rules file) after another move would
  result in the first move being propagated to the remote Cozy and the
  document being desynchronized after that.
  From now on, the second move to the ignored location will cancel the
  first move and the client will correctly propagate a deletion to the
  remote Cozy.
- Deleting a file on your Cozy while moving it on your local
  filesystem with your client stopped would lead to the
  desynchronisation of the file. It would be deleted on your Cozy but
  would still exist on your local filesystem and all later
  modifications would not be propagated. We're now refusing the
  deletion because we believe the movement indicates a desire to keep
  the file and it seems easier for the user to understand and fix the
  situation if that was not the expected behavior. The file move will
  then be propagated to the remote Cozy and kept in sync.
- In some situations we can detect changes made on your remote Cozy on
  documents of which we haven't yet received the parent folders. We
  can't process orphaned documents so we require the parents of all
  documents before we allow processing those and if we don't have
  them, we'll issue an error that results in the
  "Synchronization incomplete" status message, literally blocking the
  synchronization process.
  We believe that most of those issues could resolve themselves by
  merely refusing the orphan change and synchronizing the other
  changes so we've decided not to block the synchronization process
  anymore when we encounter orphan changes.
- We detected that the remote watcher whose role is to detect, fetch
  and analyze changes coming from your remote Cozy could fail without
  the synchronization process stopping and alerting you. This means
  that in such cases, the changes made on your local filesystem would
  still be detected and potentially propagated to your remote Cozy but
  the changes made remotely would not be applied locally until a
  client restart.
  We've refactored the life-cycle management of the whole
  synchronization process and the remote watcher and we made sure that
  errors coming from the remote watcher are caught by the
  synchronization process which will in turn alert you and stop itself
  and both local and remote watchers.
- The client would not detect the correct mime type for `.cozy-note`
  files when detected on the local filesystem. This would change the
  saved mime type of notes moved on the local filesystem and not show
  the correct icon in the Recent changes list in our main window.
  We've switched to a custom mime detector for those files to detect
  our custom mime type.
- Since propagating a local file update to a remote Cozy Note would
  break this note (i.e. it would not be detected as such and we would
  lose its actual content while still keeping its markdown export
  within the associated Cozy file), we've decided to prevent all local
  note updates to be propagated to the remote Cozy.
- In order to still synchronize your local updates to notes with your
  remote Cozy, we're now using the conflict mechanism to rename the
  original note on the remote Cozy before upload your new content to
  the appropriate location. This way, you have both your updated
  content and the original note that can still be edited within the
  Cozy Notes application.
- We've found that when renaming a folder while another folder within
  the same parent starts with the renamed folder's original name (e.g.
  renaming `cozy` to `cozy cloud` while you have `cozy company` in the
  same parent) would lead to the incorrect movement of the content of
  the other folder (i.e. the content of `cozy company` in our
  example).
  We've fixed the algorithm that lists the content of a folder so that
  it looks only within the exact given location and not similar
  locations.
- In some situations, locally creating a folder within a moved or
  renamed parent could lead to the creation of a new parent folder on
  the remote Cozy at the target location, thus making the parent
  movement impossible since a document would already exist at the
  target location. This situation was caused by some logic we
  implemented to help create complex hierarchies in any order. We
  would create a missing parent folder when creating a new folder on
  the remote Cozy.
  We've now stopped doing this and will not synchronize the creation
  of a folder if its parent does not exist. In case the parent
  location would be created later by the client (e.g. when propagating
  the parent movement), the new folder will eventually be
  synchronized.
- Remote changes resulting in an `MergeMissingParentError` do not
  block the synchronization process since v3.21.0-beta.1 but the
  changes from the affected batch and the ones coming after will be
  fetched over and over again until the errors are resolved, which
  might never come.
  We've identified a few sources of those errors that should be fixed
  really soon and believe we should not encounter solvable missing
  parent issues anymore so we've decided to mark them as processed
  anyway and rely on the next changes to resolve those missing parents
  issues.
- We added a migration to force a refetch of all remote Cozy Notes in
  order to avoid as many dispensable conflicts as we can during the
  first reboot after this release installation.
- We made sure a Cozy Note is still identified as such after saving
  changes like an update on the remote Cozy. This will ensure they
  will stay protected from local updates afterwards.
- Until now the authentication of your Cozy during the initial
  connection of the client would always be done by our own remote
  application. We're adding the possibility for partners to offer
  their users to connect via their own SSO portal so we now run the
  connection flow in a dedicated sandbox.
  This has two advantages when an SSO portal is involved:
  1. the portal code is run in a browser like environment with no
     alterations so it should work out of the box
  2. the portal code is isolated from the rest of our application
     adding another layer of security preventing malicious code on the
     portal itself to access your computer
- We made sure the application of the move and update of a file on the
  local filesystem does not trigger invalid changes that would be
  propagated to the remote Cozy.
- We discovered timing issues during the propagation of remote file
  changes to the local filesystem. These can result in invalid
  metadata being sent to the remote Cozy after propagating a grouped
  content update and file renaming. In case the file was in a shared
  directory, the metadata change would in turn be propagated via the
  sharing to other Cozies and we can end up with a completely
  desynchronized file and conflicts.
  To prevent these invalid metadata from being propagated to the
  remote Cozy, we introduced a new way to store and compare local file
  states. This also helps us detect during a client restart when a
  remote file modification was fetched but not completely propagated
  to the file system and avoid creating a conflict.

Improvements for Windows users:

- To emphasize the fact that Cozy Notes should not be edited on your
  local filesystem we were marking the local note files as read-only.
  This was not preventing us from overwriting them with new remote
  updates on Linux and macOS but it was on Windows in some cases. When
  this would happen, the local file content would not reflect the
  remote content anymore and it could even lead to the remote Note
  being broken after a Desktop client restart.
  Since we've now introduced a conflict mechanism to protect Cozy
  Notes from local modifications, we can remove the read-only
  permission and remote updates will be propagated to the local
  filesystem on all platforms.

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[300bfa58f1...](https://github.com/argilla-io/argilla/commit/300bfa58f1a7469019921f921f411f1c25bcd984)
#### Tuesday 2023-10-31 09:26:13 by Ayan Joshi

Updated Broken Links  (#4076)

# Argilla Community Growers

Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged.

# Pull Request Templates

Please go the the `Preview` tab and select the appropriate sub-template:

* [🐞-bug](?expand=1&template=bug.md)
* [📚-documentation](?expand=1&template=docs.md)
* [🆕-features](?expand=1&template=features.md)

# Generic Pull Request Template

Please include a summary of the changes and the related issue. Please
also include relevant motivation and context. List any dependencies that
are required for this change.



**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [x] Improvement (change adding some improvement to an existing
functionality)
- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A
- [ ] Test B

**Checklist**

- [x] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

There were two broken links in the Readme , I fixed it of the
cheatsheets and the Contribution guidelines Have a look
at my pr @davidberenstein1957

---
## [warriorstar-orion/Paradise](https://github.com/warriorstar-orion/Paradise)@[dcd1f5d88a...](https://github.com/warriorstar-orion/Paradise/commit/dcd1f5d88a8c5ba9634fc3fce67a76ada45f71dc)
#### Tuesday 2023-10-31 09:48:20 by Octus

Adds eight vox hairstyles because why not and stuff (#22573)

* god i hate myself

* donedone

* fixxxxx

---
## [felix-cw/ruff](https://github.com/felix-cw/ruff)@[fc94857a20...](https://github.com/felix-cw/ruff/commit/fc94857a202e43a0a0fa47f972a6807346336046)
#### Tuesday 2023-10-31 10:19:01 by Zanie Blue

Rewrite ecosystem checks and add `ruff format` reports (#8223)

Closes #7239 

- Refactors `scripts/check_ecosystem.py` into a new Python project at
`python/ruff-ecosystem`
- Includes
[documentation](https://github.com/astral-sh/ruff/blob/zanie/ecosystem-format/python/ruff-ecosystem/README.md)
now
    - Provides a `ruff-ecosystem` CLI
- Fixes bug where `ruff check` report included "fixable" summary line
- Adds truncation to `ruff check` reports
    - Otherwise we often won't see the `ruff format` reports
- The truncation uses some very simple heuristics and could be improved
in the future
- Identifies diagnostic changes that occur just because a violation's
fix available changes
- We still show the diff for the line because it's could matter _where_
this changes, but we could improve this
- Similarly, we could improve detection of diagnostic changes where just
the message changes
- Adds support for JSON ecosystem check output
    - I added this primarily for development purposes
- If there are no changes, only errors while processing projects, we
display a different summary message
- When caching repositories, we now checkout the requested ref
- Adds `ruff format` reports, which format with the baseline then the
use `format --diff` to generate a report
- Runs all CI jobs when the CI workflow is changed

## Known problems

- Since we must format the project to get a baseline, the permalink line
numbers do not exactly correspond to the correct range
- This looks... hard. I tried using `git diff` and some wonky hunk
matching to recover the original line numbers but it doesn't seem worth
it. I think we should probably commit the formatted changes to a fork or
something if we want great results here. Consequently, I've just used
the start line instead of a range for now.
- I don't love the comment structure — it'd be nice, perhaps, to have
separate headings for the linter and formatter.
- However, the `pr-comment` workflow is an absolute pain to change
because it runs _separately_ from this pull request so I if I want to
make edits to it I can only test it via manual workflow dispatch.
- Lines are not printed "as we go" which means they're all held in
memory, presumably this would be a problem for large-scale ecosystem
checks
- We are encountering a hard limit with the maximum comment length
supported by GitHub. We will need to move the bulk of the report
elsewhere.

## Future work

- Update `ruff-ecosystem` to support non-default projects and
`check_ecosystem_all.py` behavior
- Remove existing ecosystem check scripts
- Add preview mode toggle (#8076)
- Add a toggle for truncation
- Add hints for quick reproduction of runs locally
- Consider parsing JSON output of Ruff instead of using regex to parse
the text output
- Links to project repositories should use the commit hash we checked
against
- When caching repositories, we should pull the latest changes for the
ref
- Sort check diffs by path and rule code only (changes in messages
should not change order)
- Update check diffs to distinguish between new violations and changes
in messages
- Add "fix" diffs
- Remove existing formatter similarity reports
- On release pull request, compare to the previous tag instead

---------

Co-authored-by: konsti <konstin@mailbox.org>

---
## [moritaka-sofujinia/MVC-MobiReview](https://github.com/moritaka-sofujinia/MVC-MobiReview)@[34bf2ebe8c...](https://github.com/moritaka-sofujinia/MVC-MobiReview/commit/34bf2ebe8cdd22bd3e94d98e5831622bf538c29e)
#### Tuesday 2023-10-31 10:19:31 by Nguyen Tien Dung

last update on this slutty thing, I'm fucked ,damn it i hate this one

---
## [TheDailySimile/ReticenceVat](https://github.com/TheDailySimile/ReticenceVat)@[2b38c86ed8...](https://github.com/TheDailySimile/ReticenceVat/commit/2b38c86ed88614d64e1f52161c385a0371ee69a1)
#### Tuesday 2023-10-31 10:53:17 by The Daily Simile

Create Answer Lust@For Similes of I.html

🐺@scowl : "till last week you were badgering us to increase your salary yet for the last one week you've intact refused to take your salary and cleaned the whole station too well working way over time..and my colleagues here say that you've also not met your boyfriend twice when he came around and the second time infact drove him away..YET as i heard he returned today and have been..happy to know that you won't meet but what was more important is that he didn't even want to use his familiari8here at the office to get a crucial dealing in his favour..and no while all thinks at as Interregional Judiciary HQ we've performed well may be possibly a fruit of hard work but i'm afraid to say finally not because of historical statistics or constraints but because of a possible attraction to a certain kind of..psychological..amusement..my question is..WHY?.."
Sweeper@giggle : "no i went back home and  mom hadn't taken her medicines and was as if too gleeful i asked why she said it i could only procure 2 had no money but those were also the last ones in the package which the shop disposed i was curious at the colourful backside of it so wanted to see it so asked and.."
🐺@angry : "enough..i know this story..from that heinous novel Concerns across Pebblefog#..
Records of Roadside Kids@giggle : "be be..see see..see see..seemy i/Meh..Far..hihihi..here i/so so..to go..or..to be or boo i/as hands-on..my freedom..simile of i.."
🐺@frown : "and we're supposed to govern..moods..cunning indeed this scheme of Answer Lust for The Similes of I..sly wicked devils of practice#..Simile Hands-On,#,.."

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[c034314f1b...](https://github.com/OrionTheFox/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Tuesday 2023-10-31 10:55:40 by SkyratBot

[MIRROR] Basic skeletons [MDB IGNORE] (#24545)

* Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

* Basic skeletons

* updatepaths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[0e3b7d842b...](https://github.com/OrionTheFox/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Tuesday 2023-10-31 10:55:40 by SkyratBot

[MIRROR] Adds a Syndicate Monkey Agent beacon uplink item [MDB IGNORE] (#24550)

* Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Adds a Syndicate Monkey Agent beacon uplink item

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[2a74c23d62...](https://github.com/spockye/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Tuesday 2023-10-31 10:57:24 by Imaginos16

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
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[bf4671ff83...](https://github.com/spockye/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Tuesday 2023-10-31 10:57:24 by retlaw34

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
## [matrix-org/matrix-js-sdk](https://github.com/matrix-org/matrix-js-sdk)@[31f38550e3...](https://github.com/matrix-org/matrix-js-sdk/commit/31f38550e3fb0ed7312e52b896985477b22f01c3)
#### Tuesday 2023-10-31 12:46:40 by David Baker

Refactor & make base64 functions browser-safe

We had two identical sets of base64 functions in the js-sdk, both
using Buffer which isn't really available in the browser unless you're
using an old webpack (ie. what element-web uses). This PR:

 * Takes the crypto base64 file and moves it out of crypto (because
   we use base64 for much more than just crypto)
 * Makes them work in a browser without the Buffer global
 * Removes the other base64 functions
 * Changes everything to use the new common ones
 * Adds a comment explaining why the function is kinda ugly and how
   soul destroyingly awful the JS ecosystem is.
 * Runs the tests with both impls
 * Changes the test to not just test the decoder against the encoder
 * Adds explicit support & tests for (decoding) base64Url (I'll add an
   encode method later, no need for that to go in this PR too).

---
## [wdphy16/netket](https://github.com/wdphy16/netket)@[34bd4adde1...](https://github.com/wdphy16/netket/commit/34bd4adde13df35b65f4f055a750dda242fdfa20)
#### Tuesday 2023-10-31 13:02:30 by Filippo Vicentini

Simplification of dispatch logic/definition of new observables (#1605)

Our funny @alleSini99 recently contributed a set of Renyi entropy
estimators, which are defined to inherit from `ÀbstractOperator`, so we
need to define some methods like `ìs_hermitian` that do not make much
sense for such object.

Moreover, to define the gradient, the dispatch rule for this observable
has this ugly-as-hell `TrueT`or `Literal[True]` that nobody besides me
understands.

This PR is an attempt to
 - Simplify the creation of a new generic operator/observable
 - Simplify the definition of signatures for dispatch of expect/grad by:
   - remove `use_covariance` argument from the general interface
- only keep `use covariance` for the expectation value of operators
where it make sense, and it will not be part of the dispatch signature

In practice...

- This introduces a new super type of AbstractOperator which I
call `AbstractObservable`. The difference between Abstract Operator and
AbstractObservable is that an Observable is very general and requires
nothing besides an Hilbert space. No is hermitian or dtype arguments. So
it should cover the most general case.

- Renyi entropy estimator is transitioned to this interface.

- The signature that users must define for expectation value estimators
will now be
```python
@dispatch
def expect(vs: MCState, ob: Reny2Entropy, chunk_size: Optional[int]):
  pass
```
and for gradients will be (the much simpler)
```python
@dispatch
def expect_and_grad(vs: MCState, ob: Reny2Entropy, chunk_size: Optional[int]):
  pass
```

Incidentally, this will make it simple to implement different types of
chunking like @chrisrothUT wants to do in #1590 by dispatching on a
tuple of integers for the chunk size instead of just an integer. Right
now the dispatch logic is very messy and this would not be easy to do.

Note that users are required to specify the chunk size, and if thy don-t
support it they have to explicitly state `chunk_size: None`. I could
relax this requirement but it makes user-defined code future-proofed in
case we add more arguments.

The main problem with those changes is that it breaks user-defined
operators using the past syntax. This is not strictly a problem because
this part of the interface is documented to be unstable, though it's
annoying.
I could add some inspect magic to detect usages of the old signatures
and auto-convert them to the new format and warn. To be experimented
with.

---
## [DurgaPrashad/WebTriad-Designs](https://github.com/DurgaPrashad/WebTriad-Designs)@[bcf633790c...](https://github.com/DurgaPrashad/WebTriad-Designs/commit/bcf633790c63fc5884783261a479f47641329f23)
#### Tuesday 2023-10-31 13:30:21 by Durga Prashad

Create Card Carousel Scroll Animation.html

🎡 Experience the Card Carousel Scroll Animation 🌟

Explore a mesmerizing card carousel that smoothly scrolls through a collection of dynamic cards, each showcasing exciting projects. As you navigate through the animation, you'll discover card flips and new content appearing like magic! ✨

🃏 Cards with Style: Each card is elegantly designed with gradients and glows to catch your eye. Hover over them, and they playfully lift off the screen! 🚀

🖼️ Visual Delight: The animation is a visual treat, with beautifully crafted cards that include project titles, descriptions, and enticing images. 🎨

🔄 Dynamic Loading: As you scroll, new cards seamlessly join the carousel, creating an endless journey of discovery. 🔄

📜 Interactivity: Click and explore each card to learn more about exciting projects. 📊

🌈 Colorful Palette: Enjoy a diverse range of background colors, making the animation pop with creativity. 🌈

🌊 Smooth Scroll: Experience the magic of smooth and effortless scrolling, creating an immersive experience. 🌊

🔥 Give it a try and immerse yourself in the Card Carousel Scroll Animation today! 🔥

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d1ad9b6658...](https://github.com/tgstation/tgstation/commit/d1ad9b665823708c3ae651eb9729023968e7feaf)
#### Tuesday 2023-10-31 13:37:49 by necromanceranne

Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

---
## [jstenmark/prompts](https://github.com/jstenmark/prompts)@[179a23ca15...](https://github.com/jstenmark/prompts/commit/179a23ca15da1e10e975eccc8fffa2c763c0a6eb)
#### Tuesday 2023-10-31 13:49:06 by JStenmark

High Priest:	Armaments Chapter One, verses nine through twenty-seven:
Bro. Maynard:	And Saint Attila raised the Holy Hand Grenade up on high
	saying, "Oh Lord, Bless us this Holy Hand Grenade, and with it
	smash our enemies to tiny bits."  And the Lord did grin, and the
	people did feast upon the lambs, and stoats, and orangutans, and
	breakfast cereals, and lima bean-
High Priest:	Skip a bit, brother.
Bro. Maynard:	And then the Lord spake, saying: "First, shalt thou take
	out the holy pin.  Then shalt thou count to three.  No more, no less.
	*Three* shall be the number of the counting, and the number of the
	counting shall be three.  *Four* shalt thou not count, and neither
	count thou two, excepting that thou then goest on to three.  Five is
	RIGHT OUT.  Once the number three, being the third number be reached,
	then lobbest thou thy Holy Hand Grenade towards thy foe, who, being
	naughty in my sight, shall snuff it.  Amen.
All:	Amen.
		-- Monty Python, "The Holy Hand Grenade"

---
## [SrHaruno/Pokemon-God](https://github.com/SrHaruno/Pokemon-God)@[f2562a8a6e...](https://github.com/SrHaruno/Pokemon-God/commit/f2562a8a6e93763448d6ae69431352bfda18768b)
#### Tuesday 2023-10-31 13:55:06 by srharuno

Beta 1.0.1

Few Moves added in

Cupid Shot, Holy Light and Lunar Spear.
All angel-type moves.

Berserk Smash, an Demon-type move.

---
## [raulcd/arrow](https://github.com/raulcd/arrow)@[3beb93af36...](https://github.com/raulcd/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Tuesday 2023-10-31 14:23:26 by Kevin Gurney

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
## [ickshonpe/bevy](https://github.com/ickshonpe/bevy)@[44f677a38a...](https://github.com/ickshonpe/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Tuesday 2023-10-31 15:09:14 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[575e9dce3f...](https://github.com/treckstar/yolo-octo-hipster/commit/575e9dce3f6963147a086d6b7ae9d6919d54159a)
#### Tuesday 2023-10-31 15:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [nocturnalnoob/basebot](https://github.com/nocturnalnoob/basebot)@[e037562060...](https://github.com/nocturnalnoob/basebot/commit/e037562060a228411f87301836b6a7b0fbb2fb01)
#### Tuesday 2023-10-31 16:06:51 by nocturnalnoob

Create TelegramCode

This Python script is a powerful and versatile Telegram bot that brings a wealth of features and functionalities to the Telegram platform. Developed using the Telepot library, this bot serves as an interactive and engaging companion, capable of responding to various user commands and performing a wide range of tasks.

Key Features and Commands:

LED Control: This bot can interact with and control an LED, enabling users to remotely turn it on or off. It's a valuable feature for tasks that involve managing physical devices through a chat interface.

/hi - Personalized Greetings: The bot offers a personal touch by providing custom greetings, making users feel welcome and initiating conversations on a friendly note.

/time - Real-Time Clock: Users can retrieve real-time date and time information by sending the '/time' command. This feature is helpful for time-sensitive reminders and scheduling.

/loc - Location Sharing: The bot can provide users with their approximate location based on their IP address. This feature is beneficial for location-specific services or user engagement.

/ip - Server Information: For tech enthusiasts and system administrators, the bot can share the server's hostname and corresponding IP address. This information is valuable for server management and diagnostics.

/distance - Distance Measurement: Equipped with an ultrasonic sensor, the bot can accurately measure and report distances. This functionality has applications in fields such as robotics, proximity detection, and automation.

/info - Customizable Information: The bot can respond with customizable information or messages, allowing it to adapt to various use cases and provide relevant content to users.

/logo - Image Sharing: Users can request and receive image files, making it a versatile tool for sharing logos, graphics, or visual content directly within the chat.

/file - Document Exchange: The bot facilitates the exchange of documents, including code files and other types of files. This feature supports collaboration and document sharing.

/audio - Music Playback: Users can enjoy on-demand music or audio content directly through the bot. This feature is ideal for entertainment and sharing audio resources.

/video - Video Sharing: The bot can share video files with users, making it suitable for sharing video content, tutorials, or promotional materials.

/url - Share Links: Users can request and receive customized URLs, simplifying the process of sharing web resources and links.

Usage Instructions:

To set up and activate this bot, you'll need to replace the placeholder ##Your Bot token## in the script with your actual Telegram bot token. This token is essential for establishing a connection between the bot and the Telegram platform.

Additional Information:

It's important to ensure that the required libraries and hardware components (such as an LED and an ultrasonic sensor) are properly configured and in working order for the script to function effectively.
This script serves as a robust and adaptable foundation for creating your personalized Telegram bot. It is capable of accommodating a wide range of applications, from casual interactions and entertainment to practical functions and automation. The bot's versatility, coupled with its interactive nature, makes it a valuable tool for engaging users and facilitating a diverse set of tasks within the Telegram platform

---
## [PhoenixBureau/PythonOberon](https://github.com/PhoenixBureau/PythonOberon)@[b88231b84a...](https://github.com/PhoenixBureau/PythonOberon/commit/b88231b84add5b3aa77fa9145ef15b8ae8f25e1f)
#### Tuesday 2023-10-31 16:07:01 by Simon Forman

Link USART and SPI to test orex.

Except my AVR programmers won't work.  One seems broken (red LED when
you plug it in) but the other (green LED and yellow blinking LED) seems
okay.  It appears in /dev/ttyU0 (I have to chmod it to let group (wheel)
talk to it) but then avrdude throws some kind of error and the
programmer switches to RED LED. :(

I took it hard.  It was working (it seemed) the night before, and now it
does not.  SO many possible problems: FreeBSD USB flakey?  Flakey
USB sockets or cables?  I toasted the programmers somehow (the likely
problem.  I'm not grounded.  There could be some issues with how I'm
connecting the programmer.  I think the chip should be powered when you
plug it in?)  The circuit on the breadboard could be wrong or the
connection mis-wired from the ISP even though I checked and rechecked.
I feel like a kid that got a rock for Christmas.  Stupid hardware.  I'm
going back to software.  He says, gazing longingly at the cold lifeless
LEDs on the breadboard.  I don't mean it.  I was really looking forward
to running Oberon machine code on a silly little AVR-based emulator, it
would have felt like using a real computer.

Bleah.

What am I doing with my life?  Is this just my model train set?  Will
anuone else ever benefit from what I'm doing now?

(I think I just need to go eat breakies.)  ;)

---
## [nocturnalnoob/cnnclassification](https://github.com/nocturnalnoob/cnnclassification)@[b3dbfbc97b...](https://github.com/nocturnalnoob/cnnclassification/commit/b3dbfbc97b16e5b3d59f923be2b23a4fb5b3dff4)
#### Tuesday 2023-10-31 16:42:15 by nocturnalnoob

Update AI_Ml_Project_ipynbcolab_file.ipynb

Embarking on the "Image Classification with CNN on CIFAR-10 Dataset" project is like diving headfirst into the fascinating world of computers that can see and understand images, and it's all about honing our skills. Picture a treasure chest of 60,000 tiny 32x32 pixel images, each falling into one of ten categories like cars, birds, and cats. Our main quest in this adventure is to teach a computer model to look at these images and tell us what's in them with impressive accuracy.

Our journey unfolds in a series of steps. We start by sorting the images into two groups: one to teach our model and the other to test how well it's learned. Then, we make sure the images are all in a format that our model can easily understand. With our model ready to go, we dive into the training phase. It's like teaching a pet new tricks, only our pet is a computer. It learns by looking at the images over and over, gradually getting better at recognizing different features and patterns in them.

Next, we see how well our "pet" can perform on a test. It's like a final exam for our model, and we're checking to see if it can work its magic on images it's never seen before. To make things even more exciting, we use visuals to track our model's progress. We create graphs to show how well it's doing over time, just like a chart that records your progress when you're learning something new.

Finally, we make sure our model isn't just a classroom superstar but can be used in real life too. We save it for future adventures or any applications where image recognition is crucial, like self-driving cars, medical imaging, or even content filtering on the internet.

By the end of this journey, we'll have a new set of skills under our belt. We'll know how to build, train, and evaluate deep learning models, especially Convolutional Neural Networks. We'll also be experts at getting data ready for these models and have a knack for visualizing their performance. It's a hands-on exploration into the exciting world of image classification and deep learning, and these skills are super valuable in fields where computers need to "see" and make decisions based on what they see.

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[503c0d42ea...](https://github.com/argilla-io/argilla/commit/503c0d42eab2d617f7e556789c6f3c4b091ef0f9)
#### Tuesday 2023-10-31 16:50:03 by David Berenstein

docs: changed some warning to more friendly notes (#4108)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

changed some warning to more friendly notes

Closes #4107

**Type of change**

(Remember to title the PR according to the type of change)

- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [X] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [X] I added relevant documentation
- [X] I followed the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [X] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[578b451c0a...](https://github.com/wrye-bash/wrye-bash/commit/578b451c0a2e5a910717a93600cdafee89f05926)
#### Tuesday 2023-10-31 16:55:38 by MrD

[!]WIP gui resources: RRR EEE

EEE if not os.path.isdir(images_dir): # CI Hack we could move to caller or add a param

This was meant to be more granular - I wanted to centralize image
initialisation including setting dirs['image'] - turned out that constants
were imported too early (# 600, control import order), (mopy) dirs were
not initialised and this necessitated moving the image
definitions in initStatusBar - however to make this simpler I renamed
the images based on the key in tooldirs (ini backwards compat). We could:

- turn all these to svgs?
- add a sensible default to the image dict? (we could do this instead of
the CI hack)
- further centralise get_*** from _gui_globals especially get_image_dir

Next commit finalizes this - for now bye staticBitmap, au revoir, auf
wiedersehen etc. Also see the GuiImage imports and dirs['images'] go
down and imgDirJoin (make ugly code look ugly) centralised - getting
somewhere:

"""
Thou hast committed bugs, but that was in another language, and besides,
the critters are dead.
"""

Note cause initially _icons were defined in `import balt` time and
images were not initialized yet the imports would crash cause:

if not os.path.isabs(img_path):
    img_path = os.path.join(get_image_dir(), img_path)

would produce a relative (non-existing) path and we would
land in _tkinter_error_dial - which crashes bigtime on mac:

2023-10-10 14:49:27.496 Python[11010:375752] -[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0
2023-10-10 14:49:27.503 Python[11010:375752] *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0'
...
libc++abi: terminating due to uncaught exception of type NSException

Process finished with exit code 134 (interrupted by signal 6: SIGABRT)

To fix `import balt` crash I moved Colorchecks images init to gui.
This now crashed on importing basher in Mopy.bash.bash._main -
when constants is imported still get_image_dir() returns ''

Traceback (most recent call last):
...
  File "/Users/.../Mopy/bash/basher/constants.py", line 458, in <listcomp>
    return [GuiImage.from_path(template % x) for x in (16, 24, 32)]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 90, in from_path
    return _BmpFromPath(img_path, iconSize, img_type, quality)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 56, in __init__
    raise ArgumentError(f'Missing resource file: {self._img_path}.')
bash.exception.ArgumentError: Missing resource file: tools/isobl16.png.

To fix this I had to finally -> Simplify tools init:

Here is the map of filenames that differed:

{'ISRMG': "insanity'sreadmegenerator", 'ISRNG': "insanity'srng",
 'ISRNPCG': 'randomnpc', 'OBFEL': 'oblivionfaceexchangerlite',
 'OBMLG': 'modlistgenerator', 'BSACMD': 'bsacommander',
 'Tes4FilesPath': 'tes4files', 'BlenderPath': 'blender', 'GmaxPath': 'gmax',
 'MayaPath': 'maya', 'MaxPath': '3dsmax', 'FastStone': 'faststoneimageviewer',
 'PaintNET': 'paint.net', 'PaintShopPhotoPro': 'paintshopprox3',
 'PhotoshopPath': 'photoshop', 'PixelStudio': 'pixelstudiopro',
 'MAP': 'interactivemapofcyrodiil', 'NPP': 'notepad++',
 'RADVideo': 'radvideotools'}

I hope no one relied on these. Now as seen having to deal with two image
formats introduces complexity - there was a merge about that no ? <--- RRR
There is also the matter of game dependencies - and settings saving - and
profiles per game - that's # RRR launchers

Accept Path in GuiImage.from_path:

os.path.splitext(img_path) works fine for path - yey for os.pathlike!

inline _init_tool_buttons - note that TesVGecko was added twice

things like

renames = {
    'OblivionBookCreatorPath': 'oblivionbookcreator%s.png',
    'Tes4GeckoPath': 'tes4gecko%s.png',
    'Tes5GeckoPath': 'tesvgecko%s.png',
    'Tes4ViewPath': 'tes4view%s.png',
    'Tes4TransPath': 'tes4trans%s.png',
    'Tes4LodGenPath': 'tes4lodgen%s.png',
    'NifskopePath': 'nifskope%s.png',
}
tooldir = '/Users/.../Mopy/bash/images/tools'
for k, v in renames.items():
    for pix in (16,24,32):
        try:
            shutil.move(_j(tooldir, v % pix), _j(tooldir, f'{k.lower()}{pix}.png'))
        except Exception as e:
            print(k,v,e)
            break

One (1) use of app_buttons_factory - yes! This is geared towards # 570
and initTooldirs

The [!] for image renames - this was 99% of the perspiration - dict
used:

{
    'nifskope16.png': 'nifskopepath16.png',
    'nifskope24.png': 'nifskopepath24.png',
    'nifskope32.png': 'nifskopepath32.png',
    'oblivionbookcreator16.png': 'oblivionbookcreatorpath16.png',
    'oblivionbookcreator24.png': 'oblivionbookcreatorpath24.png',
    'oblivionbookcreator32.png': 'oblivionbookcreatorpath32.png',
    'tes4gecko16.png': 'tes4geckopath16.png',
    'tes4gecko24.png': 'tes4geckopath24.png',
    'tes4gecko32.png': 'tes4geckopath32.png',
    'tes4lodgen16.png': 'tes4lodgenpath16.png',
    'tes4lodgen24.png': 'tes4lodgenpath24.png',
    'tes4lodgen32.png': 'tes4lodgenpath32.png',
    'tes4trans16.png': 'tes4transpath16.png',
    'tes4trans24.png': 'tes4transpath24.png',
    'tes4trans32.png': 'tes4transpath32.png',
    'tes4view16.png': 'tes4viewpath16.png',
    'tes4view24.png': 'tes4viewpath24.png',
    'tes4view32.png': 'tes4viewpath32.png',
    'tesvgecko16.png': 'tes5geckopath16.png',
    'tesvgecko24.png': 'tes5geckopath24.png',
    'tesvgecko32.png': 'tes5geckopath32.png',
    'blender16.png': 'blenderpath16.png', 'blender24.png': 'blenderpath24.png',
    'blender32.png': 'blenderpath32.png', 'bsacommander16.png': 'bsacmd16.png',
    'bsacommander24.png': 'bsacmd24.png', 'bsacommander32.png': 'bsacmd32.png',
    'faststoneimageviewer16.png': 'faststone16.png',
    'faststoneimageviewer24.png': 'faststone24.png',
    'faststoneimageviewer32.png': 'faststone32.png',
    'gmax16.png': 'gmaxpath16.png', 'gmax24.png': 'gmaxpath24.png',
    'gmax32.png': 'gmaxpath32.png',
    "insanity'sreadmegenerator16.png": 'isrmg16.png',
    "insanity'sreadmegenerator24.png": 'isrmg24.png',
    "insanity'sreadmegenerator32.png": 'isrmg32.png',
    "insanity'srng16.png": 'isrng16.png', "insanity'srng24.png": 'isrng24.png',
    "insanity'srng32.png": 'isrng32.png', 'randomnpc16.png': 'isrnpcg16.png',
    'randomnpc24.png': 'isrnpcg24.png', 'randomnpc32.png': 'isrnpcg32.png',
    'interactivemapofcyrodiil16.png': 'map16.png',
    'interactivemapofcyrodiil24.png': 'map24.png',
    'interactivemapofcyrodiil32.png': 'map32.png',
    '3dsmax16.png': 'maxpath16.png', '3dsmax24.png': 'maxpath24.png',
    '3dsmax32.png': 'maxpath32.png', 'maya16.png': 'mayapath16.png',
    'maya24.png': 'mayapath24.png', 'maya32.png': 'mayapath32.png',
    'notepad++16.png': 'npp16.png', 'notepad++24.png': 'npp24.png',
    'notepad++32.png': 'npp32.png',
    'oblivionfaceexchangerlite16.png': 'obfel16.png',
    'oblivionfaceexchangerlite24.png': 'obfel24.png',
    'oblivionfaceexchangerlite32.png': 'obfel32.png',
    'modlistgenerator16.png': 'obmlg16.png',
    'modlistgenerator24.png': 'obmlg24.png',
    'modlistgenerator32.png': 'obmlg32.png',
    'paint.net16.png': 'paintnet16.png', 'paint.net24.png': 'paintnet24.png',
    'paint.net32.png': 'paintnet32.png',
    'paintshopprox316.png': 'paintshopphotopro16.png',
    'paintshopprox324.png': 'paintshopphotopro24.png',
    'paintshopprox332.png': 'paintshopphotopro32.png',
    'photoshop16.png': 'photoshoppath16.png',
    'photoshop24.png': 'photoshoppath24.png',
    'photoshop32.png': 'photoshoppath32.png',
    'pixelstudiopro16.png': 'pixelstudio16.png',
    'pixelstudiopro24.png': 'pixelstudio24.png',
    'pixelstudiopro32.png': 'pixelstudio32.png',
    'radvideotools16.png': 'radvideo16.png',
    'radvideotools24.png': 'radvideo24.png',
    'radvideotools32.png': 'radvideo32.png',
    'tes4files16.png': 'tes4filespath16.png',
    'tes4files24.png': 'tes4filespath24.png',
    'tes4files32.png': 'tes4filespath32.png'
}

---
## [IronMikeJ79/pwnhyve](https://github.com/IronMikeJ79/pwnhyve)@[dfe7c3fd48...](https://github.com/IronMikeJ79/pwnhyve/commit/dfe7c3fd48cb1671a9cd4bbddd361db9da180dd2)
#### Tuesday 2023-10-31 17:07:09 by otter

remote control and evil portal

i have kinda lost motivation but fuck it we ball

the html control panel is also depreciated now and will likely be removed, as you can only use it when you have to interfaces

next update will be cleaning up some things

---
## [IronMikeJ79/pwnhyve](https://github.com/IronMikeJ79/pwnhyve)@[09a6bbc48a...](https://github.com/IronMikeJ79/pwnhyve/commit/09a6bbc48af53ed32b2e9a04691e4c5af7d9b033)
#### Tuesday 2023-10-31 17:07:09 by otter

+lolbas, +modular menus, +keyboard

added a fuck-ton of lolbas scripts, also put environment variables into duckyscript scripts using `![$VAR]`, added modular menus (so you arent limited by my shitty designs), updated and fixed some other things and removed ssh bruteforcing (who even uses that)

---
## [poettering/systemd](https://github.com/poettering/systemd)@[d6c559b1f9...](https://github.com/poettering/systemd/commit/d6c559b1f9f4887b06d225a5e4793a9186b0e125)
#### Tuesday 2023-10-31 17:58:16 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [hashicorp/nomad](https://github.com/hashicorp/nomad)@[66fbc0f67e...](https://github.com/hashicorp/nomad/commit/66fbc0f67e47b3fc5f6007e624173e18905f9b63)
#### Tuesday 2023-10-31 18:25:23 by Michael Schurter

identity: default to RS256 for new workload ids (#18882)

OIDC mandates the support of the RS256 signing algorithm so in order to maximize workload identity's usefulness this change switches from using the EdDSA signing algorithm to RS256.

Old keys will continue to use EdDSA but new keys will use RS256. The EdDSA generation code was left in place because it's fast and cheap and I'm not going to lie I hope we get to use it again.

**Test Updates**

Most of our Variables and Keyring tests had a subtle assumption in them that the keyring would be initialized by the time the test server had elected a leader. ed25519 key generation is so fast that the fact that it was happening asynchronously with server startup didn't seem to cause problems. Sadly rsa key generation is so slow that basically all of these tests failed.

I added a new `testutil.WaitForKeyring` helper to replace `testutil.WaitForLeader` in cases where the keyring must be initialized before the test may continue. However this is mostly used in the `nomad/` package.

In the `api` and `command/agent` packages I decided to switch their helpers to wait for keyring initialization by default. This will slow down tests a bit, but allow those packages to not be as concerned with subtle server readiness details. On my machine rsa key generation takes 63ms, so hopefully the difference isn't significant on CI runners.

**TODO**

- Docs and changelog entries.
- Upgrades - right now upgrades won't get RS256 keys until their root key rotates either manually or after ~30 days.
- Observability - I'm not sure there's a way for operators to see if they're using EdDSA or RS256 unless they inspect a key. The JWKS endpoint can be inspected to see if EdDSA will be used for new identities, but it doesn't technically define which key is active. If upgrades can be fixed to automatically rotate keys, we probably don't need to worry about this.

**Requiem for ed25519**

When workload identities were first implemented we did not immediately consider OIDC compliance. Consul, Vault, and many other third parties support JWT auth methods without full OIDC compliance. For the machine<-->machine use cases workload identity is intended to fulfill, OIDC seemed like a bigger risk than asset.

EdDSA/ed25519 is the signing algorithm we chose for workload identity JWTs because of all these lovely properties:

1. Deterministic keys that can be derived from our preexisting root keys. This was perhaps the biggest factor since we already had a root encryption key around from which we could derive a signing key.
2. Wonderfully compact: 64 byte private key, 32 byte public key, 64 byte signatures. Just glorious.
3. No parameters. No choices of encodings. It's all well-defined by [RFC 8032](https://datatracker.ietf.org/doc/html/rfc8032).
4. Fastest performing signing algorithm! We don't even care that much about the performance of our chosen algorithm, but what a free bonus!
5. Arguably one of the most secure signing algorithms widely available. Not just from a cryptanalysis perspective, but from an API and usage perspective too.

Life was good with ed25519, but sadly it could not last.

[IDPs](https://en.wikipedia.org/wiki/Identity_provider), such as AWS's IAM OIDC Provider, love OIDC. They have OIDC implemented for humans, so why not reuse that OIDC support for machines as well? Since OIDC mandates RS256, many implementations don't bother implementing other signing algorithms (or at least not advertising their support). A quick survey of OIDC Discovery endpoints revealed only 2 out of 10 OIDC providers advertised support for anything other than RS256:

- [PayPal](https://www.paypalobjects.com/.well-known/openid-configuration) supports HS256
- [Yahoo](https://api.login.yahoo.com/.well-known/openid-configuration) supports ES256

RS256 only:

- [GitHub](https://token.actions.githubusercontent.com/.well-known/openid-configuration)
- [GitLab](https://gitlab.com/.well-known/openid-configuration)
- [Google](https://accounts.google.com/.well-known/openid-configuration)
- [Intuit](https://developer.api.intuit.com/.well-known/openid_configuration)
- [Microsoft](https://login.microsoftonline.com/fabrikamb2c.onmicrosoft.com/v2.0/.well-known/openid-configuration)
- [SalesForce](https://login.salesforce.com/.well-known/openid-configuration)
- [SimpleLogin (acquired by ProtonMail)](https://app.simplelogin.io/.well-known/openid-configuration/)
- [TFC](https://app.terraform.io/.well-known/openid-configuration)

---
## [ZecHub/zechub](https://github.com/ZecHub/zechub)@[0d97121c8c...](https://github.com/ZecHub/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Tuesday 2023-10-31 18:54:28 by TonyAkinsWritesCrypto

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
## [ancientland/TestShiptest](https://github.com/ancientland/TestShiptest)@[2a4e91787a...](https://github.com/ancientland/TestShiptest/commit/2a4e91787aa43a7cbf6fa78e3f572257954131ec)
#### Tuesday 2023-10-31 19:06:50 by Skrem_7

Skrem's Quick Ballistic Glanceover (#2354)

If maintainers want me to shorten the changelog, I can, I tend to start
there so I know what to talk about up here.

What started as a PR meant to buff up rubber rounds ended up turning
into a general passover I gave to much of the syntax and presentation of
ballistics. PR doesn't actually change that much function-wise, but it
changes a lot of lines due to a lot of changed pathing to better
establish consistency within ballistic code as well as overviewing a lot
of descriptions, names, and inherit moments.

Functionally, less-lethals and sniper rounds have been changed the most
by this PR. To a lesser extent, .38 special and shotgun rounds have been
tweaked. Finally, the PR stamps out a missing sprite bug with the WT-550
magazines, buffs up the surplus rifle (yeah, that old thing), tinkers
with some projectile speeds, makes match rounds slightly better, and
goes over A LOT of descriptions. I apologize for the massive wall of
text that's to follow.

Will take a look at energy weapons when I feel like it (might kill
disablers, I don't like mapping though).

The pellet changes are actually just systemizing what was supposed to be
intentional design according to code comments, it just hadn't reached
every single pellet-based shotgun projectile. The improvised shell buff
is to make it not a potential complete whiff because RNG mechanics are
generally bad and not fun to play with.

Several implementations of less-lethal (rubber) ammunition on shiptest
are strictly worse than their standard alternatives. While this isn't a
PvP server, it feels very not-fun meta-wise to POTENTIALLY arm for SOME
insubordination and still fire what may as well be a round that bleeds
someone out (as they'll cause bleeding anyway). Increasing the stamina
damage on each of these makes it so they actually have a vague trade-off
(maybe stamina damage can do something like slow simplemobs in the
future, I don't know, I'd love to do it but simplemob code makes me
screech).

To make them not directly better in PvP and not the staple of taking
down the Super Scary Syndicate Shocktrooper Guy, they've had their
negative AP doubled. Not as good against combatants, but still perfectly
adept, if not better at general riot control against civilians. Makes
sense and puts them in their niche a little better.

The .38 special round relatively has more "power" and "velocity"
compared to the 9mm round, though it does not quite reach the levels
that .45 automatic or 10mm does in the IRL server. Furthermore, .38
special was specifically designed not to over-penetrate targets so as to
minimize the chance of collateral damage in police work. These are the
ultimate justifications behind giving it the worst AP out of all the
pistol calibers (-30, instead of -20) while still raising its damage to
25.

This should make the Winchester a better staple for taking out weaker
enemies such as legions or unarmored hermits, but it'll perform worse
against goliaths, frontiersmen, and the like. All-in-all, a more
"early-game" caliber, if you will, which is kinda what it's always been.

Match rounds don't really exist as far as I've seen. That being said,
they're meant to be of higher quality, so their getting slightly higher
AP and speed makes sense, even if they're mostly just a meme round.

The speed increase of DMR/sniper rounds is primarily meant to
differentiate them better from AR rounds beyond having 20 more AP.
Assault rifles so far have pretty much dominated with better magazine
size, fire rate, and the exact same force as the DMR calibers, just
doing less damage against armored targets (doesn't matter too much when
you can just vomit rounds). I'd like to buff up the DMR damage even more
(sniper is fine), but I'd rather get some feedback on changing them to
35 baseline before doing so.

The speed decrease on shotguns is meant to cement them as CQC weapons.
Slugs are heavy. Shotguns are meant for close range. It's not much, but
it's thematically a good way to keep them in their lane, not that
they're even that problematic, hence only the slight change.

Having a big-ass bullet that does 70 damage with 50 AP hit you is
already a middle finger. Making it potentially knock off an arm or a leg
is another middle finger. Being hardstunned for ten seconds after is the
icing on the cake. Changed it to a knockdown because we hate ranged
tasers.

This thing is a joke. I haven't even seen it on the server, but I'd
rather make it vaguely competitive considering 10mm isn't super deadly
and only otherwise exists on the stechkin or the one Inteq SMG that you
never see (Colossus-only).

It's still clunky and terrible, but it should be less comedic and more
of a potential option if you have NOTHING else (will never happen).

Top-loading magazine fits into a standard assault rifle? No. Doesn't
make sense. Someone should probably just kill this gun, it's stupid and
looks stupid last I checked.

Don't think I've seen anyone use this weapon, I've only printed out
their magazines to dump AP rounds into my NT-SVG carbine. Noticed they
were invisible then. Someone increased their capacity to 30 without a
care for how its update_icon works. Not cool. Anyway, fixes are good.
Moving on.

Something very important when maintaining code is generally keeping
consistency in how things are not only presented, but how they're stored
as well. While I'd love to do EVEN more in the method of refactoring to
better align how so much of gun code works, this was something I wanted
to keep as a one-day project, so I mostly tinkered with pathing,
inherits, and groupings.

In the avenue of spelling and description changes, that's just 1)
Cleaning up errors that PR authors and maintainers missed and 2) Making
things more concise and just... better. Some of the SolGov descriptions
were a real headache to look at, and not because of the frequent
spelling and syntax errors.

Whoever misspelled and caused an entire series of items to be
/obj/item/gun/ballistic/automatic/assualt may wish to avoid any crows
for the next three months.

Perfectly willing to adjust or reel back some of my descriptions if
someone can offer something better than what I've written out if there's
some soul they REALLY want to keep.

:cl:
tweak: The NT 'Boarder' ARG now loads standard P-16 magazines, rather
than the M-90gl toploaders.
balance: .38 special does 25 damage up from 20. AP has been reduced to
-30 from -20.
balance: Standardizes pellet projectiles to lose 10% damage of both
types per tile across the board. Improvised pellets no longer have a
hardcapped 1-8 tile range.
balance: Less-lethal rounds now do 50% more stamina than the force of
their lethal counterparts, with 25% the normal force and double the
negative AP. If the round had positive or zero AP, it was subtracted by
20.
balance: Shotgun slugs do 40 damage, down from 60, but have zero AP,
rather than -10. FRAG-12 and meteor slugs have had their damage adjusted
to reflect their relative force.
balance: Surplus rifle fire_delay has been cut to 1 second from 3.
balance: .50 BMG knocks down instead of hardstunning.
balance: Any DMR, match, or sniper round now travels slightly faster
than other bullets. Shotgun slugs and pellets now travel slightly slower
than other bullets.
balance: Match rounds have had their AP slightly increased.
fix: Fixed WT-550 magazines not displaying properly.
spellcheck: Went over (almost) every single ballistic description,
including the guns themselves, magazines, ballistic casings, and speed
loaders/stripper clips to not only have better consistency and
readability, but also be more clear on the general effectiveness of each
caliber.
spellcheck: Assualt is gone.
code: Repaths/renames most ballistic ammo pathing to maintain
consistency or take advantage of inherits, when possible.
/:cl:
Conflicts:
	code/modules/mob/living/simple_animal/hostile/frontiersman.dm

---
## [admiralKucha/CourierMB](https://github.com/admiralKucha/CourierMB)@[e8e14f2cb4...](https://github.com/admiralKucha/CourierMB/commit/e8e14f2cb439d1c51f1a66a3fa047948bc71e644)
#### Tuesday 2023-10-31 19:49:07 by Maxim

init 0.32 commit
fog and morning may have errors
fog range have little mistake
normal needs more information(also very similar to morning) (Кудан и Курав)

now we can check time of day, so fog and evening filter work better!

fog works not normal
think about filter water and grass in black
necessary to initialize the time position and enable the filter depending on the time

---
## [kawoppi/froggystation](https://github.com/kawoppi/froggystation)@[64eae49042...](https://github.com/kawoppi/froggystation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Tuesday 2023-10-31 20:04:05 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---
## [hazelcast/hazelcast](https://github.com/hazelcast/hazelcast)@[566574a5b4...](https://github.com/hazelcast/hazelcast/commit/566574a5b49f423109a4de61f21427838bd8076b)
#### Tuesday 2023-10-31 20:35:29 by James Holgate

Modify KubernetesClient shutdown behaviour  (#24613) [5.3.z] (#24710)

Backport of: https://github.com/hazelcast/hazelcast/pull/24613

The overall goal of this change is to change the shutdown behaviour of
KubernetesClient so our Stateful Set monitor thread shuts down before
our `ClusterTopologyIntentTracker`, to allow the intent tracker to fully
process all completed messages before Node shutdown.

**The Current Problem**
In its current state, the Stateful Set monitor thread is intended to
shutdown after `Thread#interrupt` is called, triggering the
`Thread#interrupted` check within the main `while(running)` loop of the
Runnable. However, this check is not reached as the call to
`WatchResponse#readLine` from within the main `run()` method is a
blocking call that waits until data is available to read before
proceeding. Since this call waits for non-null data before completing,
the result is always non-null, and therefore this code block never exits
under normal conditions:
```java
while ((message = watchResponse.nextLine()) != null) {
    onMessage(message);
}
```

Since this `while` loop cannot exit, and the `#readLine` method (which
passes to `BufferedReader#readLine` under the hood) is a blocking I/O
operation which cannot be interrupted, this operation does not end when
`Thread#interrupt` is called. This leads to the Stateful Set monitor
thread out-living the `ClusterTopologyIntentTracker`, even if the
StsMonitor is interrupted first. As a result, during shutdown, it is
possible for the StsMonitor to send data to the intent tracker after it
has been destroyed and its executor is no longer accepting tasks.

**The Root of the Problem**
To reach our goal of ensuring that the Stateful Set monitor thread can
no longer send requests to the `ClusterTopologyIntentTracker`, we need
to add synchronization between the two objects that guarantees the
intent tracker shuts down after the StsMonitor thread has completed.
This can be achieved using a simple `CountDownLatch` which is counted
down after the thread has completed, and awaited before shutting down
the tracker.

The main obstacle to achieving this is, as mentioned above, that the
StsMonitor thread cannot be interrupted when waiting for
`WatchResponse#readLine` to complete, and so the thread never completes.
The only way this thread can complete is to either force its
termination, or alter the message reading approach to allow interruption
as intended.

**Identifying Resolution Paths**
We don't want to force termination of our Stateful Set monitor thread as
this could result in message handling being terminated after it has been
received, but not before it has finished being processed. Therefore the
only way we can allow this thread to be interrupted as intended is to
alter the message reading mechanics in a way that allows it to be
interrupted as well.

There is no way for us to know if more messages are pending from the k8s
watch besides waiting for data to be received, so the best we can do is
allow the StsMonitor to finish processing any messages it has already
received (preventing process corruption), but terminate the stream of
new messages it is waiting for before we shutdown the intent tracker.

**Potential Solutions**
So we've identified the root of the problem as our `#readLine` function
blocking through interrupts, so how do we make it interruptible? Sadly
one of the shortcomings of I/O operations in Java is that they usually
cannot be interrupted in the traditional manner, so we have a few
approaches to consider:

1) We could modify the message reading code to use
`BufferedReader#ready` and `Thread#sleep` to periodically check if there
is data to be read before calling any read functions. The problem with
this approach is that A) `#ready` returns true if any data is available,
not just if there is a full line of data to be read; and B) utilizing a
sleep loop can result in delayed message handling at the least, or
busy-waiting overhead at worst.

2) We could use "hacky" solutions to interrupt the
`BufferedReader#readLine` such as closing underlying sockets or
connections, propagating an exception to the reader. The problem with
this solution is that everything related to our reading operation is
handled in `syncrhonized` blocks, and since our shutdown process starts
outside the StsMonitor thread, our calling thread is unable to obtain
these locks (being held by the StsMonitor)!

3) It's possible that we could rewrite the `WatchResponse` mechanics to
use Java NIO magic such as `Selector` for interruptible I/O operations.
The issue with this approach is that it would require fairly significant
refactoring of the related codebase, and may not end up providing the
exact functionality we are looking for in our use case.

4) We can introduce an `Executor` to handle our I/O operations within
the StsMonitor thread, allowing us to wait on a `Future#get` call
instead of our `BufferedReader#readLine` call, where a `Future#get`
operation can be interrupted by the waiting thread being interrupted.
The downside to this solution is we have to introduce an additional
thread on top of the existing StsMonitor thread itself.

**Selecting a Solution**
Considering the above information, I concluded the most sensible
approach was to use (4) and introduce an `Executor` thread for the I/O
operations. By using a separate thread for this call we can be rougher
with it, as we know that worse case scenario we interrupt a message
being read that has not started being processed yet (but we're shutting
down anyway).

This solution also allows for the least amount of underlying code
changes, as our `Future#get` can be interrupted without issue,
maintaining the current approach used for handling the StsMonitor
shutdown. The only downside for this approach is the addition of another
thread alongside the StsMonitor thread, but the actual impact of this
should be minimal as both threads will still be waiting most of the
time, so the only negative impact is being 1 tiny step closer to
possible thread starvation.

Generally I think this is the best solution at hand which allows quick
shutdown of the StsMonitor thread while minimising potential for data
loss or corruption. Combined with the `CountDownLatch` used, this allows
for consistent service shutdown order between the `StsMonitor` thread
and the `ClusterTopologyIntentTracker`.

---
## [Kong/ngx_wasm_module](https://github.com/Kong/ngx_wasm_module)@[d0ad7ee612...](https://github.com/Kong/ngx_wasm_module/commit/d0ad7ee61208d52f90f0f2c67a1dac26460f154a)
#### Tuesday 2023-10-31 20:36:34 by Thibault Charbonnier

refactor(proxy-wasm) improve pwexec resurrection and instance lifecycle

The main goal of this overhaul is to simplify `on_context_create`, make
it fully re-entrant *and* properly handle instance recycling at the same
time.

The way to do so, in my opinion, was to move `pwexec` creation where
`rexec` already was. In other words, always lookup the context id in the
instance rbtree, and if not found, create it. This means that
surrounding code also needed big overhauls. It also removes the
reference counting poor man's GC of the older implementation. The code
became really ugly by then so I took the time to also review this
module's code structure instead of making a *very* ugly commit.

This new ngx_proxy_wasm.c file should be much easier to read and follow
now.

One change I do not fully like is moving the `next_id` to a global
counter, but we do not have a "global proxy-wasm conf" object yet. I
also started thinking about pre-allocating a number of `pwexecs` (like
`worker_connections`) and use free/busy queue that all filter chains can
dip into to get a context id + context memory zone. Perhaps for a later
time.

---
## [NyagiByte/Compression](https://github.com/NyagiByte/Compression)@[1b73fddbb1...](https://github.com/NyagiByte/Compression/commit/1b73fddbb1eaef99187fffd697ab9358a03aa3b8)
#### Tuesday 2023-10-31 21:51:39 by Madelyn Byte

Ore recipe internals rework

Off by 1 errors can go suck me off holy shit

---
## [SobiiZXrd/Ensnared](https://github.com/SobiiZXrd/Ensnared)@[dffe9831fd...](https://github.com/SobiiZXrd/Ensnared/commit/dffe9831fd02b181235fa369889305d449e44f5a)
#### Tuesday 2023-10-31 22:07:05 by Joseph Sobrino-Torres

Working on Ensnared:

1. Created the BP_SiameseDemon avatar actor.
2. Created the BT_SiameseDemon iteration of the modular Behavior Tree we've had ready to implement all of the demons/horrors in the world.
3. Created the Attack, Increment Patrol, Clear Patrol, Set Speed, and Increment Patrol tasks/services specifically for the Siamese Demon.
4. The Siamese Demon, Ghouly Ghast Horror, Gruum Horror, Sacrifieced Cultist, and Clot Worm are now ready to be used in the world, will attack and chase the player as well as patrol according to preset vectors set in their personal patrol components.
5. Set up the spook collision to now get this actor's currently overlapped instance's transform then sets the player's RespawnTransform variable inside the BPGM_Ensnared  Game Mode which upon validating the player has died according to a bIsDead? boolean set inside the player's animBP, will wait 10 seconds and transport the player whilst resetting the player's life, as well as animation instance back to functional so the player may give killing the demon that killed them another try. ----> (THANK YOU TRAVIS!! -- This was done with the help of Travis Dolan)

---
## [SleepingLife/Turbo](https://github.com/SleepingLife/Turbo)@[b590d99cbd...](https://github.com/SleepingLife/Turbo/commit/b590d99cbd55f3cacda6d5855415b9ffc232f634)
#### Tuesday 2023-10-31 22:35:34 by SleepingLife

Piety reworks

CHANGELOG
Moved Arsenal to Architecture from Scientific Theory
Removed Particle Physics from the game and put spaceship part on mobile tactics
City of God now buffs planted prophets by 2 food and 1 culture instead of 2 food 2 culture
Apostolic Palace now grants +10 additional Science, Faith and Culture
Jesuit Education and Work Ethic have been combined to form Amish Paradise
Indulgences also grants 1 Happiness
Houses of Worship buildings grant a slot again

---

