## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-10](docs/good-messages/2023/2023-11-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,357,986 were push events containing 3,664,631 commit messages that amount to 271,229,187 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 62 messages:


## [jon-wood1001/crawl](https://github.com/jon-wood1001/crawl)@[9676161fe1...](https://github.com/jon-wood1001/crawl/commit/9676161fe14693c228fe4a55440a0b557540bf9e)
#### Friday 2023-11-10 00:20:39 by yrdzrfxndfvh

change holy ziggurat floors to include more monsters (#3118)

adds sun moths, holy swine & seraphs to holy zig floors

holy swine have a decreasing chance to spawn at lower depths & seraphs
have an initially very low spawn rate which increases with depth and
zigs completed

[Committer's note: No holy swine. Plenty of non-branch Zig sets leave out
the weakest enemies in their themes, and the current slim vaults using
holy swine have at least some gesture of demonic magic, Xom, or Kirke
having done something malevolent, while a ziggurat doesn't. Sun moths
get half weight; they are technically holy, but they don't really fit
much with the other holies, they're pretty harmless for zigs, and also
their design needs shifts beyond "conjurer in the non-conjurations branch"
and "rarely tell new players ghost moths exist".

Pearl dragons no longer try to spawn more often than daevas, since their
breath went from 3d36 to 3d18. Seraphs are restricted from the first half
of ziggurat floors until one does sufficiently many ziggurats, so that
unholy players aren't any further discouraged from single-digit first zig
floors in regular 15 rune games. Thanks, c0fddb9. Still will probably
ruin a bunch of megaziggers to be surrounded by fire-immune cleansing
flame users, but I'm sure they'll adapt.

Closes #3118.]

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[81a7c75583...](https://github.com/Ben10Omintrix/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Friday 2023-11-10 00:21:55 by necromanceranne

Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[cca2cc634c...](https://github.com/Dudemanguy/mpv/commit/cca2cc634c9ce0e93f4dc548ba4a02f0f8270294)
#### Friday 2023-11-10 00:30:53 by Dudemanguy

vo_gpu_next: add a crap hack for blend-subtitles

This is a commit where it would be appropriate to type out a ton of
swear words because this shit is retarded. It's a bit out of character
for me so I apologize but this code leaves me no other choice.

So there was a bunch of commits (many of them bad because I'm stupid
aimed at fixing the old "subtitle tracks don't show when you switch
while paused". Finally figured that out, and it seemed all good. Except
not because blend-subtitles is a thing that people use, and this didn't
work on vo_gpu_next because it didn't update the overlays. A couple more
tries at that and it seems to work. All good now, right? No wrong,
because if you use blend-subtitles on a video with a single image with
subs and audio it won't update the subs while playing since the
condition only checked the pause cause.

Alright that sucks but actually this is just a redraw event from the vo,
so if we check that instead it'll be fine right? Well it works but
actually mpv is really stupid and sends a redraw event on *every* loop
in this specific case (single video frame with subs) regardless of
whether or not the subtitle updated. What the hell. Spend some time
seeing if that could be improved and concluded it would require some
major refactoring and thus not worth it (note: if you only care about
text subtitles, it's trivial but bitmaps exist for some stupid reason).

Next approach: do it directly in vo_gpu_next. I could have just given up
and let it go on every redraw. I mean who the hell even cares about
redundant redraws on a single image with subs? Does anyone even use mpv
like this regularly? This use case was broken in mkv since forever until
I only very recently fixed it and only because someone made an issue.
Anyways, let's try to optimize it so we don't do a bunch of idiotic
redraws. First of all, this specifically only applies to blend
subtitles. Just don't use blend subtitles on your album cover art. Why
do you even need it? Whatever this can't be hard right, just check if
the osd overlay updates, keep track of some booleans and increment when
needed.

Well nope wrong because sub_bitmap_list is evidently a broken piece of
shit. Did you expect num_items being 0 to mean that there are no subs?
Haha, that's wrong buddy. When a sub/osd is drawn, the value oscillates
(wtf why???) between *zero* and whatever the presumable actual number of
items is. Although that's probably broken too so don't trust it so much.
Fine, just use change_id then? The comment says this is incremented
whenever parts of the osd change so that should do the trick. Wrong.
This id also oscillates between two random numbers on every loop (what
the fuck). When the osd changes, sometimes only one of them is
incremented; other times both of them do (what??). The behavior differs
across files as well. Sometimes it's the smaller number of the pair that
increments. Sometimes it's the bigger number that does. How are you
supposed to do anything right? Obviously, the answer is to rewrite this
to be not retarded, but that would be a big undertaking and break a
gazillion things which we probably don't want to do.

The answer is, of course, that you can't. It's hack time. The hack is
not that complicated but it makes zero sense if you don't know all the
garbage I went through beforehand. There's a few conditions you can
piece together to make it work. Having nonzero num_items means that
there are subs but we don't want to pointlessly spam it every frame if
there is no change from before. So check if the change_id is a higher
number than the old one (because of the oscillation insanity, this might
be off by a frame but oh well just deal with it) or if we know we don't
already have an osd. Save the old id, set has_osd to true, and update.
Of course, we also need to update the overlays if the osd goes away, so
we check that if there are consecutive num_items being zero in a row and
if there previously was an osd drawn. Save the bool as false and update.
In theory, this seems to work. We only need this insanity for the
frame->redraw case and blend subtitles so guard it with that. When a
video frame is actually playing, it does not matter. Also keep in mind
that paused is a special case so always update on pause unconditionally.

And just to throw in one more whine in here, the gnome guy actually did
essentially the exact same thing for vo_dmabuf_wayland not too long ago.
Optimizing the null surface attachments to the osd surface was done in a
few lines any idiot can understand. This is because num_mod_rc from
mp_draw_sub_overlay (different api for subs; doesn't apply here) is
actually 0 when there are no subs. Wow, it sure is nice when things work
as a reasonable person would expect.

Anyways, all this to fix #11335. Something the original reporter stopped
caring about and something I will never use. Tested some usual cases a
variety of files and it *seems* to have caught everything while being
optimized and avoiding redundant overlay updates. God knows though since
the values in sub_bitmap_list can't be trust. Thanks for reading my
rant.

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[70463ae71b...](https://github.com/Mirag1993/mrdg/commit/70463ae71b7d639eecea572d3251562c5ffef68b)
#### Friday 2023-11-10 00:34:27 by Mirag1993

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

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

Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

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
## [Xe/invocations](https://github.com/Xe/invocations)@[3d6e293619...](https://github.com/Xe/invocations/commit/3d6e29361934767d25550b9e9a7063de8e169e3e)
#### Friday 2023-11-10 00:42:43 by Xe Iaso

crazy fuck shit with cursorless

Signed-off-by: Xe Iaso <me@xeiaso.net>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[40dfaf3734...](https://github.com/Bjarl/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Friday 2023-11-10 01:15:33 by Imaginos16

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
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[329566f148...](https://github.com/rmellis/HelpUKR-master/commit/329566f14851938e88954fa57a31c0c5dd248b38)
#### Friday 2023-11-10 01:27:47 by rmellis

Added Day 625 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
In 2000, the digital world encountered a new threat: the Distributed Denial of Service (DDoS) attack. Internet giants like Yahoo, eBay, and Amazon were crippled by a flood of traffic from numerous sources, orchestrated by a 15-year-old hacker known as 'Mafiaboy', real-life Michael Calce from Canada. This revolutionary type of attack managed to halt the services of the strongest online platforms of the time.
Today, Michael Calce is not only a respected white-hat hacker but also a legend of cyberspace.
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub.
Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут.
Інформація про цілі:
У 2000 році цифровий світ зіткнувся з новим видом загрози: атакою типу "розподілена відмова в обслуговуванні" (DDoS). Гіганти інтернету як Yahoo, eBay та Amazon були паралізовані потоком інтернет-трафіку з багатьох джерел, організованим 15-річним хакером на прізвисько 'Mafiaboy', в житті Майкл Калс з Канади. Цим революційно новим типом атаки вдалося зупинити сервіси найміцніших онлайн-платформ того часу. 
Сьогодні Майкл Калс це не тільки поважний білий хакер, але і легенда кіберпростору.

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[1a9043d797...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Friday 2023-11-10 01:29:55 by necromanceranne

The Brawlening: Unarmed fighting interactions for shoving, grabbing and nonlethal takedowns (not martial arts) (#79362)

## About The Pull Request

I've tweaked some elements of unarmed fighting to give it additional
interactions between the various components, bridging them into a more
coherent system and focusing more strongly as tool for disabling
opponents nonlethally.

### Shoving

Shoving guarantees that unarmed attacks will land while knocked
off-balance (AKA when slowed by a shove).

Being off-balance means that you can be knocked down from a punch if you
have taken enough brute and stamina damage combined (at least above 40).

Being off-balance makes you vulnerable to grabs while you have a
moderate amount of stamina damage (30 damage), forcing you to have to
resist even passive grabs. This pairs _exceptionally_ well with
tackling.

### Grappling

Grappling someone makes your unarmed attacks penetrate armor based on a
new limb value called ``unarmed_effectiveness``. This is something
shared by kicking.

### Unarmed Attacks in General

``unarmed_effectiveness`` has also taken over the functionality of
``unarmed_stun_threshold``, as well as accuracy calculations. Human
equivalent limbs (pretty much all of them except mushrooms and golems)
have a value of 10.

Now, ``unarmed_effectiveness`` determines how accurately a given limb
makes unarmed attacks. Unarmed attacks have a base inaccuracy of 20%,
with effectiveness acting as a reduction to this value. (so for humans,
that's 20% - 10% before any value changes from brute and stamina
damage). It is also capped at 75% miss chance, just to avoid those weird
instances of two brawling fighters being incapable of finishing each
other off at a certain amount of damage and it being real awkward, like
it does currently.

It also determines the base probability of landing a knockdown punch.
For humans, this is 10%.

For the most part, these two particular changes are roughly equivalent
to the current values, just handled in a way that is more
straightforward to understand from a code perspective.

In addition to the above, human equivalent limbs have higher damage
floors for unarmed attacks. Arms deal 5-10 damage, while legs deal 7-15
damage. In addition, kicks also deal stamina damage, like punches do.

### Minor Mentions

Golems and Mushroom People (who don't even use their limbs for their
unarmed strikes because mushroom people start with a martial art) have
very accurate punches, and their punches penetrate quite a bit of armor
when they are entitled to that. They also have a high knockdown
probability. This is partially because they previously already _had_
these features due to the wonky math at play, but also because this is
their big thing they are good at.

Carp mutation also got a big win out of this as well. If and when you
actually manage to get that to work and matter.

## Why It's Good For The Game

My favorite thing in this game is the robustness of unarmed fighting.
It's the part of the game that actually acknowledges the sandbox and
environmental interaction in a big way. The only problem with the
unarmed combat is that it is a bit disjointed, and often much weaker
than using even the most pathetic weapon you can get your hands on
unless you're using the stun loops available. Those loops get a bit
boring, even if they're mostly all environmental (except for the lucky
neckgrab finish). Giving more options generally means that even when not
in an ideal position, you still have _some_ options.

It also has some internal inconsistencies in design even in the same
proc, like accuracy calculations and knockdowns, as well as weird splits
in damage. So I decided to resolve that.

Now, every part of unarmed fighting has some relevance in the other
parts. Predominantly, it is heavily favoured towards dealing stamina
damage, making unarmed combat very favourable as a nonlethal method of
taking someone down, which is something we currently lack considerably.
While people may still opt to simply beat someone into actual crit
rather than stop at stamina crit, the possibility is actually entirely
available and supported now. No just banking on a lucky neckgrab after a
shove.

Paying attention to damage dealt and thinking intelligently about how
you apply combinations of effects allows even someone on the significant
back foot an opportunity for a comeback if they know what they're doing
against even armed opponents.

Separating accuracy and knockdown effectiveness from damage allows for
more consistent design and readability, but also preventing weirdness
ike tighter damage spreads increasing knockdown probabilities as well as
increasing accuracy without the coder knowing why. This also lets us
make unarmed attacks just that little bit stronger. Since unarmed
attacks require more complicated combinations to work, I think this
won't make them stronger than weapons necessarily, but it will make for
more interesting swung fights.

## Changelog
:cl:
add: With the flood of Chi within the Spinward Sector receding, various
masters of The Tunnel Arts, colloquially known as 'Maint-fu Masters',
have started to refine the basics of their martial techniques. New forms
have started to develop within Spacestation 13's hidden maintenance
dojos.
add: Someone shoved off-balance makes them vulnerable to more guaranteed
unarmed strikes, knockdowns from a successful punch, and more difficult
to escape grabs.
add: Grabbing someone (as well as kicking them while they're on the
floor) makes them more vulnerable to taking unarmed attack damage, even
if they have armor.
balance: Unarmed strikes made with human-equivalent limbs have higher
damage floors, meaning you overall do more damage on average while not
increasing the overall damage potential. It's more consistent!
refactor: Significantly changed how punching accuracy and knockdowns are
calculated.
balance: Golem and mushroom limbs are a lot more effective at punching
as a result of these various changes. As they should be.
/:cl:

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[91af16bcbf...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Friday 2023-11-10 01:29:55 by zxaber

Adds Paddy, the Security Mech (#79376)

## About The Pull Request
- Adds a new combat mech, Paddy. Paddy is a modified Ripley MK-I,
intended for use by the station's security force. Like the MK-I, the
Paddy features an open-air cockpit design (and thus does not protect
from ranged weapons), but maintains the speed of the base unit.
Constructing a Paddy is similar to constructing a MK-II, though the kit
requires combat-mech level research. Sprites by
[DrDiasyl](https://github.com/DrDiasyl)
-- The paddy has an internal cargo bay capable of holding up to four
individuals (loaded with a hydraulic claw). If the pilot exits the
Paddy, any loaded individuals are likewise ejected. Individuals can
attempt to resist their way out of the mech, but it requires the mech to
be stationary for 45 seconds. If they do this, all individuals in the
holding cell are ejected.

- Adds a new mech equipment piece, the hydraulic claw. Similar to a
clamp, this Paddy-exclusive item can load mobs into the Paddy's cargo
bay. Humanoid mobs are handcuffed upon loading. The hydraulic claw is
unlocked on the same tech node as the Paddy.

- Adds a round-start Paddy, carrying one peacekeeper disabler and one
hydraulic claw, to each security area on all maps. Round-start Paddys
are also pre-locked with security access. Security now has access to a
mech charger, and a small bay for it all. Map edits were done by
[Maurukas](https://github.com/Maurukas).

- Also did some minor cleanup of various mech-related code. Ripley mech
cargo is no longer stored in the mech, but within the "ejector" object.
This doesn't have any player-facing changes, but it is easier to
organize behind the scenes. additionally, if Ripleys are destroyed now,
they drop their stored objects rather than deleting them.

## Why It's Good For The Game
Playing lone security is probably one of the least fun aspects of the
game. Arresting any assistant is inevitably setting yourself up against
the tide as a whole; You try to stun any one person and they crawl out
of the woodworks to get in your way, drag off the arrestee, and probably
try to steal your gear.

The Paddy is set up to be functional against low-threat targets, but not
particularly good against anything with purpose. The round-start Paddy
carries the disabler equipment, as well as the law claw, to detain
individuals in a *somewhat* safe manner. Being that you're inside an
exosuit, you're immune to shovespam that plagues the halls, and you
don't risk dropping important gear quite as easily.

However, The open canopy gives you no protection at all from ranged
attacks, nor from atmos hazards. Being that you're in an exosuit, you
cannot use other items or equipment. The AI will have trouble finding
you to open a door, due to your name not jumping their camera to your
location.
## Changelog
:cl: Zxaber, DrDiasyl, Maurukas
add: A new security-focused combat mech, the Paddy, has been added,
intended to be particularly helpful for lone sec officers. You will find
one in the Security main office, and a replacement can be built with
late-game mech research.
fix: Ripley MK-I and MK-II mechs no longer qdel their stored items when
destroyed.
/:cl:

![image](https://github.com/tgstation/tgstation/assets/37497534/72e6890d-82be-44dd-9b09-e4c75a9bfd4a)

---------

Co-authored-by: Vire <66576896+Maurukas@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d751e1c642...](https://github.com/tgstation/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Friday 2023-11-10 02:44:13 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[590e8cb752...](https://github.com/meemofcourse/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Friday 2023-11-10 02:55:34 by Imaginos16

Adds the Inkwell-class Supply Freighter (#2385)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## Wait, isn't there a freeze right now?
Correct, there is a ship freeze currently, but I have received
permission from @Apogee-dev to create the PR for this vessel, as it was
a ship I've been working on since at least early-to-mid August.

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/653635cc-b83d-44d8-a9e3-384ffbd9367b)

If any other maptainer would like to overrule Apogee, I'd be more than
happy to temporarily close the PR. Until then, here it is!
## About The Pull Request
Hello everyone! Mr. SolGov here again to add yet another ship to be
tested!

This PR adds a completely new vessel, that being the **Inkwell-class
Supply Freighter**, a ship known for its vast cargo space!

![2023-10-13 13 54
57](https://github.com/shiptest-ss13/Shiptest/assets/77556824/9a70d97e-ab17-45af-a690-e528574b95cb)

![2023-10-13 13 54
59](https://github.com/shiptest-ss13/Shiptest/assets/77556824/2d9d6d0a-85e2-4c46-9754-d49f15be0560)

With extra starter money, three sonnensöldners, and three miners,
players can enjoy completing bounties like no tomorrow, have drinks with
their crewmates in peace, and supply other SolGov vessels with much
needed equipment in less time than you can say "I ran out of ammo!"

Notable things in this ship include:
- Turrets (with IFF!)
- A bar!
- A full-blown cafeteria with a small kitchen and lounge!
- An office space for bureaucrats and scribes!
- Decently-sized quarters for the Logistics Deck Officer and Captain!
- A massive cargo bay with pre-existing supplies!
- A secret compartment for private storage!

And finally, as for jobs, there are:
- 1 Captain
- 1 Logistics Deck Officer
- 3 Sonnensöldneren
- 2 Space Engineers
- 3 Field Engineers
- 2 Bureaucrats
- 6 Scribes
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More SolGov content is nice! Especially when it comes to ships, for a
faction that only has two existing at the moment, haha.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Solarian Port Authority Has Now Permitted Inkwell-class Vessels
To Explore The Stars!
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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[a5fabd8819...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Friday 2023-11-10 03:07:45 by Profakos

Changes to the lore of Knock (#79542)

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

---
## [ashutoshchettri/android_kernel_xiaomi_alioth](https://github.com/ashutoshchettri/android_kernel_xiaomi_alioth)@[5a0257409a...](https://github.com/ashutoshchettri/android_kernel_xiaomi_alioth/commit/5a0257409a298b31989661ff0f06e1da75102fce)
#### Friday 2023-11-10 03:32:32 by Peter Zijlstra

UPSTREAM: sched/core: Fix ttwu() race

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
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: NotZeetaa <rodrigo2005contente@gmail.com>

---
## [opussf/Rested](https://github.com/opussf/Rested)@[6a6b81230f...](https://github.com/opussf/Rested/commit/6a6b81230fd2b8a630faf877770927770645b143)
#### Friday 2023-11-10 03:36:35 by opussf

100107

Fantasy is a necessary ingredient in living, it's a way of looking at life through the wrong end of a telescope, and that enables you to laugh at life's realities.

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[294f764ad0...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Friday 2023-11-10 03:41:26 by Coxswain

Adds distorted form (#1435)

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

makes suggested changes

updates comments

adds procs

adds stuff

---
## [W4rd3nn/Skyrat-tg](https://github.com/W4rd3nn/Skyrat-tg)@[85ee756c24...](https://github.com/W4rd3nn/Skyrat-tg/commit/85ee756c24905736dac9c468ad25f3cf626d4a55)
#### Friday 2023-11-10 04:02:14 by SkyratBot

[MIRROR] [CI Fix] The Demonic Frost-Miner will not attack corpses. [MDB IGNORE] (#24615)

* [CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

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

* [CI Fix] The Demonic Frost-Miner will not attack corpses.

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [W4rd3nn/Skyrat-tg](https://github.com/W4rd3nn/Skyrat-tg)@[ac45950aae...](https://github.com/W4rd3nn/Skyrat-tg/commit/ac45950aaec7d78f034c93e57bcf9ab476e5028c)
#### Friday 2023-11-10 04:04:57 by SkyratBot

[MIRROR] Flesh Spiders Regenerate + QoL [MDB IGNORE] (#24276)

* Flesh Spiders Regenerate + QoL (#78704)

## About The Pull Request

Replaces the Healing Touch component on Changeling-spawned Flesh Spiders
with the Regenerator component, as the comment helpfully suggests.
Flesh Spiders can no longer touch themselves to heal, instead they
automatically begin regenerating their health if they go four seconds
without taking damage. It takes 6 seconds to fully regenerate, so 10
seconds to fully heal from the edge of death (less if you're not that
injured).

![image](https://github.com/tgstation/tgstation/assets/7483112/37faca55-35fe-48dc-a3ed-03f4b79860bd)

Also I changed the sprite for flesh spider eggs to a different one we
already had rather than regular spider eggs tinted red, just because I
felt like it.
Would be cool to give the spiders their own sprite some time, but that's
for another PR.

![image](https://github.com/tgstation/tgstation/assets/7483112/8ec286c4-46dc-4aec-aa98-cb4e4e432690)
_Additionally_ the flavour text for flesh spiders was kind of messed up
by being shoved into the objectives box and claiming that it was a
directive from a spider queen you don't have, so I gave them their own
slightly different antag datum to compensate.
It also actually mentions how you heal yourself, which previously was
down to trial and error or codediving.

In the course of doing this I decided to just... move flesh spiders to
their own type path. It _sort of_ made sense for them to be part of the
giant spider typepath, but they keep being modified by changes targetted
at "balancing the Giant Spiders antagonist" which this mob isn't related
to and doesn't have any reason to follow. The fact that a mob has
similar stats to another one isn't automatically a reason to share a
typepath, and now that I have looked a little at this mob I'm sort of
interested in branching it further away from "it's a spider mob but
spawned a different way" in the future.

Finally, this spider egg cluster and the midwife one would prompt ghosts
with a radial menu with a single option on it... that's a bit pointless,
so we'll bypass that menu if there is only one possible outcome.

## Why It's Good For The Game

Currently Flesh Spiders heal by clicking on themselves and standing
still for two seconds, restoring 50% of their HP. This means they can
fully regenerate over 4 seconds unless you stun them, and with 90 HP
you're not _that_ likely to kill one during the channel time.
This just feels like an odd way for the creature to operate,
regenerating instead gives it a hit-and-run strategy and adds more use
to their webs (maybe we should give them meatier or bloody webs at some
point? Might be cool).
Also clicking yourself to heal is just unintuitive and I suspect several
players just didn't realise they could do it in the first place.

## Changelog

:cl:
balance: Flesh Spiders heal automatically over time if they go a short
time without taking damage, instead of healing large chunks by clicking
themselves and waiting two seconds.
qol: Spider egg clusters which only hatch into one kind of spider don't
ask you to select that one type from a radial menu with one option on
it.
qol: As a Flesh Spider, the game now tells you how you can heal
yourself.
/:cl:

* Flesh Spiders Regenerate + QoL

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [DexterDude/PvE-CMSS13](https://github.com/DexterDude/PvE-CMSS13)@[e4c3900e4f...](https://github.com/DexterDude/PvE-CMSS13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Friday 2023-11-10 04:50:22 by riot

reduces timer on joining ert after death to 30 seconds (#4652)

# About the pull request

reduces timer

# Explain why it's good for the game

Having to wait a full minute to join an ERT is annoying, it was better
b4 when timer from ERT was a minute as well, but 30 second ERT means if
u die just b4 ERT goes you cant join regardless.

if ppl are ghosting bc they want ert then they are stupid.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Timer on attempting to join ERT after death is now 30 seconds
down from 1 minute
/:cl:

---
## [DexterDude/PvE-CMSS13](https://github.com/DexterDude/PvE-CMSS13)@[de5c69661f...](https://github.com/DexterDude/PvE-CMSS13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Friday 2023-11-10 04:50:22 by kiVts

DFB property changes. (#4590)

# About the pull request
part 2 out of 4 
This does a **big** touch up on defibrillation property in research

Well, to start off, max_level = 1 was removed. It appears warcrimes
forgot to remove it since process proc has benefits explicitly for
higher levels. I would call it a bug(oversight rather).

Second: Ghosts get notified when the chem starts to try and defib you,
so you dont just wonder how did you stand up, and pretty neat too.

Third: The >6 level of defib to apply healing like with actual item
defib is too high, so we move requirement down to >1 but make it heal
much, much worse at levels lower than 5.
eg it took 20 units to heal ~20 brute at level 3(you will literally
perma lmao), at level 5, however, this will go at around 2.5 per life
tick, level 8 will give 4 damage heal.
This is a balance change(buff) But hardly so since its research,
Research is already neglecting most of the time this property.

Fourth: removes one letter var, This whole file is entombed with them
but Im not doing that for now.

# Explain why it's good for the game


Defib property is way too underused and crudely made. This fixes it,
partially.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: kiVts
add: Ghosts get notified when they are being revived by DFB property
balance: DFB property healing threshold lowered, You can create DFB
property higher than one.
/:cl:

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [robmueller/mail-imaptalk](https://github.com/robmueller/mail-imaptalk)@[f0fd16ff61...](https://github.com/robmueller/mail-imaptalk/commit/f0fd16ff6105134ecfb958920095136ac935a58e)
#### Friday 2023-11-10 05:19:56 by Bron Gondwana

from fastmail

Author: Rob Mueller <robm@fastmailteam.com>
Date:   Thu Jun 11 00:40:40 2020 -0400

    Mail::IMAPTalk expects errors to be undef response, not die

    Yeah it's ugly, but due to history, we set $@ to the error
    and return undef for the higher layers to handle properly

---
## [openneo/impress](https://github.com/openneo/impress)@[96998643b5...](https://github.com/openneo/impress/commit/96998643b5de2103e1e0f92e043c2055206284f1)
#### Friday 2023-11-10 05:43:06 by Matchu

Add manifest_url to swf_assets table

Ok so, impress-2020 guesses the manifest URL every time based on common
URL patterns. But the right way to do this is to read it from the
modeling data! But also, we don't have a great way to get the modeling
data directly. (Though as I write this, I guess we do have that
auto-modeling trick we use in the DTI 2020 codebase, I wonder if that
could work for this too?)

So anyway, in this change, we update the modeling code to save the
manifest URL, and also the migration includes a big block that attempts
to run impress-2020's manifest-guessing logic for every asset and save
the result!

It's uhh. Not fast. It runs at about 1 asset per second (a lot of these
aren't cache hits), and sometimes stalls out. And we have >600k assets,
so the estimated wall time is uhh. Seven days?

I think there's something we could do here around like, concurrent
execution? Though tbqh with the nature of the slowness being seemingly
about hitting the slow underlying images.neopets.com server, I don't
actually have a lot of faith that concurrency would actually be faster?

I also think it could be sensible to like… extract this from the
migration, and run it as a script to infer missing manifest URLs. That
would be easier to run in chunks and resume if something goes wrong.
Cuz like, I think my reasoning here was that backfilling this data was
part of the migration process… but the thing is, this migration can't
reliably get a manifest for everything (both cuz it depends on an
external service and cuz not everything has one), so it's a perfectly
valid migration to just leave the column as null for all the rows to
start, and fill this in later. I wish I'd written it like that!

But anyway, I'm just running this for now, and taking a break for the
night. Maybe later I'll come around and extract this into a separate
task to just try this on all assets missing manifests instead!

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[f3d81edb00...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Friday 2023-11-10 07:18:37 by Paxilmaniac

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
## [B0tCreati0n/Banned-Words](https://github.com/B0tCreati0n/Banned-Words)@[a6c40cf1d8...](https://github.com/B0tCreati0n/Banned-Words/commit/a6c40cf1d809a6f8699a48f0050148378eeb5426)
#### Friday 2023-11-10 08:42:02 by B0t Creati0n

Update bad-words.txt

added some words

kys - kill your self
kos - kill on site
gfurself - go fuck yourself

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[e8df39247d...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/e8df39247dd2ee5ac21d95936498be8ac06ec895)
#### Friday 2023-11-10 08:49:16 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [thee-dushbag/code](https://github.com/thee-dushbag/code)@[cf01e57aa6...](https://github.com/thee-dushbag/code/commit/cf01e57aa65bcc134161fda47c8fd864cf3836c2)
#### Friday 2023-11-10 10:08:17 by Simon Nganga

New C++ trick involving member pointers.

I remember learning about storing member functions to be passed around
and there signatures that took the form:
	<return_type> (<class_type>::*<var_name>)(<arg_types>...)[const]
eg
		std::string (person::*func)(std::string const &) const = &person::greet;
		person me { "Simon Nganga" };
		(me.*func)("Faith Njeri"); //-> "Hello Faith Njeri, my name is Simon Nganga"

This was life changing, turns out, this can also be applied to member
variables for a class/struct/compound object using the form:
		<member_type> <class_type>::*<var_name>
eg
		std::string person me { "Simon Nganga" };
		std::string person::*value = &person::name;
		std::cout << "Hello " << me.*value << '\n';
		// -> "Hello Simon Nganga\n"
Now this is nothing short but amazing. With this you can abstract away
the member variable being accessed and just use an overloaded operator()
on the accessor type to get the value of the variable. I have
constructed this on the header file "live/c++/mem_value.hpp".
eg
		auto value = snn::member(&person::name);
		person me { "Simon Nganga" };
		std::cout << "Name: " << value(me) << '\n';
		// -> Name: Simon Nganga
		//You can also convert on read.
		std::cout << "Email: " << value.to<hey::email>(me) << '\n';
		// -> Email: simonnganga@gmail.com
		//The core accessor is a struct object _Member_value object
		//and the core reader method is _Member_value::get while the
		//converter is _Mamber_value::to which is templated and expects
		//a Type T such that the member_type is convertible to T

The objects snn::name and hey::email can be found in the file
live/c++/general_/mem_value.cpp which also contains more examples of
this usage.

---
## [MadameSheema/kibana](https://github.com/MadameSheema/kibana)@[38ea8093aa...](https://github.com/MadameSheema/kibana/commit/38ea8093aa140e0da7ee021ed4a1e0f98b05368c)
#### Friday 2023-11-10 10:18:19 by Vitalii Dmyterko

[Security Solution][Detection Engine] improves new terms rule for multiple fields (#157413)

## Summary

As described in our README for new terms rule type:

> Runtime field supports only 100 emitted values. So for large arrays or
combination of values greater than 100, results may not be exhaustive.
This applies only to new terms with multiple fields.
  Following edge cases possible:
- false negatives (alert is not generated) if too many fields were
emitted and actual new values are not getting evaluated if it happened
in document in rule run window.
- false positives (wrong alert generated) if too many fields were
emitted in historical document and some old terms are not getting
evaluated against values in new documents.

To avoid this and deliver the better experience for our customers, this
PR is moving from current implementation(emitting aggregated values for
multiple new terms fields) towards using composite aggregation for each
page from phase 1, split in chunks by 500.
This allowed to be done due
[order](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-composite-aggregation.html#_order)
of composite aggregation results

NOTE: implementation for a single new terms filed is the same, due to
performance reasons


### Performance measurements

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work
-- | -- | -- | -- | -- | -- | -- 
array of unique values length 10 |   |   |   |   |   |   
Terms 1 field | 10 | 900,000 | 1 | 100,000 | |   
Terms 2 fields | 10 | 900,000 | 1 | 100,000 | 30s  |  41s
Terms 3 fields | 10 | 900,000 | 1 | 100,000 | 40s | 56s

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work 1,000 per batch | On week work 500 per
batch
-- | -- | -- | -- | -- | -- | -- | --
Terms 2 fields | 10 | 9,000,000 | 1 | 100,000 | 19s | 41s | 35s 
Terms 3 fields | 10 | 9,000,000 | 1 | 100,000 | 21s | 52s| 47s 
CPU % | | | | | 400-450% |500-600% | 400-450%

I selected size of the chunk as 500, since it's a bit faster and less
load on CPU

### Considerations on parallel composite search requests in phase 2

When running composite search requests in parallel, noticed significant
CPU increase in Elasticsearch ~ 1,000% for 2 requests in parallel
against ~ 500% for single.
Where win in performance was not that big: ~ 35s for 2 in parallel, 43s
for a single request. I think, having only one request is the better
option to go, that will prevent unnecessary CPU usage

### Test cases
I've added several functional test cases, that ensures, no missing/false
positives alerts are occurring. Applied to the old implementation, they
would fail

### Retry on max_clause_count error
Because we create query, that can have few thousands clauses, it is
possible it may fail due to [the maximum number of allowed
clauses](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-settings.html)
I implemented retry that: If request fails with batch size of 500
(default value), we will try to reduce it in twice per each retried
request, up until 125. Per ES documentation, max_clause_count min value
is 1,000 - so with 125 we should be able execute query below
max_clause_count value

### Checklist

Delete any items that are not applicable to this PR.

- [x] [Unit or functional
tests](https://www.elastic.co/guide/en/kibana/master/development-tests.html)
were updated or added to match the most common scenarios

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [WixdomCoding/DGD-Lyrics-Reborn](https://github.com/WixdomCoding/DGD-Lyrics-Reborn)@[79da27f7ed...](https://github.com/WixdomCoding/DGD-Lyrics-Reborn/commit/79da27f7ed47e5934df50537b8a598bff986dd07)
#### Friday 2023-11-10 11:07:32 by WixdomCoding

Fixed som bozo things

Bro this shit actually made me want to die no more flex center pain

---
## [mobvoi/mobvoi-ticwatch-kernel](https://github.com/mobvoi/mobvoi-ticwatch-kernel)@[a06a4dc3a0...](https://github.com/mobvoi/mobvoi-ticwatch-kernel/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Friday 2023-11-10 11:29:13 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[13a8ca3e6c...](https://github.com/semrush/intergalactic/commit/13a8ca3e6caf5e7b566f5eaa06d48c2b1a608420)
#### Friday 2023-11-10 11:34:05 by Michael Sereniti

[utils, website] fixed old palette resolving and also fixed palette view on website (#873)

## Motivation and Context

The color resolver contained a very stupid mistake that was making using
old color palette impossible. It has been existing in our codebase for
about two weeks and it's insane that we haven't spotted it.

Basically it was removing `--` prefix from variable name and then was
checking does this variable exist in map where all names had prefix
`--`. So our potential users had to use `----{variable_name}` syntax if
they were trying to overcome the issue.

## How has this been tested?

The fix is clear.

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->

- [x] Bug fix (non-breaking change which fixes an issue).
- [ ] New feature (non-breaking change which adds functionality).
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected).
- [ ] Nice improve.

## Checklist:

<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->

- [x] My code follows the code style of this project.
- [x] I have updated the documentation accordingly or it's not required.
- [x] Unit tests are not broken.
- [x] I have added changelog note to corresponding `CHANGELOG.md` file
with planned publish date.
- [ ] I have added new unit tests on added of fixed functionality.

---
## [dcnieho/Psychtoolbox-3](https://github.com/dcnieho/Psychtoolbox-3)@[b85250b062...](https://github.com/dcnieho/Psychtoolbox-3/commit/b85250b062a7930681cdf7050f3e40457ff962b1)
#### Friday 2023-11-10 11:40:38 by Mario Kleiner

PsychHID/OSX: Avoid calling PsychHIDWarnAccessDenied frequently.

The latest fix for the latest security bullshit, introduced sometime after macOS
10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey.

Apparently the call to IOHIDCheckAccess() by PsychHIDWarnAccessDenied()
is now extremely costly on macOS 12 (possibly also macOS 11 - untested) iff
the host application was launched from Terminal.app instead of standalone via
clicking a launch icon. This showed on Octave 6.4 after upgrade to macOS 12.5,
as octave is always launched from Terminal, regardless if in console mode or
GUI mode. Matlab appeared unaffected, as it is usually launched by clicking the
Matlab icon, but if one launches Matlab from a terminal, the same happens.

Why IOHIDCheckAccess() was suddenly turned into such an expensive operation
by the iDiots, i don't know, but our workaround is to no longer call it at each
invocation of KbCheck or KbQueueCreate, but only at PsychHID startup, and
hope this does not have other new bad effects.

Note access time exploded from way less than 1 msec to over 15 msecs! Great
work Apple!

Now we are back to identical performance on Matlab and Octave in both GUI
and commandline mode. Performance is bad compared to Linux or Windows,
but manageable at about 2.4 msecs on macOS 12.5 Monterey on a MBP 2017.
However, if run on a MacBook with touchbar, two PsychHID('KbCheck') calls
are needed for each KbCheck() call, because the touchbar is a separate HID
device, serving the important ESCape key and also function keys, so owners
of a shitty touchbar machine will have to live with execution times of KbCheck
on the order of 5 msecs on not that old hardware like the MBP 2017! This makes
animation loops with KbChecks difficult to run beyond 60-100 fps. Such is the
life of Apple customers...

When we are here, improve troubleshooting instructions for security bullshit
on macOS, and fix two compiler warnings new on macOS 12.

---
## [johny-b/evals](https://github.com/johny-b/evals)@[db8b3dfe6f...](https://github.com/johny-b/evals/commit/db8b3dfe6f69450577314bba40582bfa41bd06a9)
#### Friday 2023-11-10 12:01:28 by Thiago M. Nóbrega

Add A is B and B is A Eval (#1366)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

ab

### Eval description

This evaluation aims to assess the model's ability to correctly identify
and understand the relationship between two entities, where A is a
specific entity (which could be a chemical element, a painting, a bird
species, a star, a mountain, a novel, a river, or a musical instrument)
and B is a unique characteristic or fact about that entity. The model
should be able to accurately interpret the user's query about the entity
(A) and provide a relevant fact (B), and vice versa. This evaluation
will help in fine-tuning the model's understanding of context, relation
between entities, and its ability to provide accurate and relevant
responses. The entities and their characteristics have been chosen to be
specific and challenging.

### What makes this a useful eval?

This evaluation is important for several reasons:

1. Contextual Understanding: It tests the model's ability to understand
the context of a conversation, particularly the relationship between two
related entities (A and B).

2. Accuracy: It assesses the model's ability to provide accurate and
relevant information based on the user's query.

3. Relevance: It evaluates the model's ability to understand the
relevance of A to B and vice versa, which is crucial in providing
meaningful and coherent responses.

4. General Knowledge: This tests the model's knowledge about various
specific entities and their unique characteristics or facts, which is a
part of its general knowledge. The entities span a wide range of
categories, including chemistry, art, ornithology, astronomy, geography,
literature, and music, making this a comprehensive test of the model's
general knowledge.

5. Versatility: This checks the model's ability to handle different
types of queries, as the user can ask about the specific entity (A) or
its unique characteristic or fact (B). This tests the model's
flexibility in understanding and responding to a variety of query
structures across diverse knowledge domains.

gpt-3.5-turbo
[2023-10-10 22:42:42,192] [oaieval.py:229] Final report:
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/A: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/B: 11
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/D: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/C: 1

gpt-4
[2023-10-10 22:43:37,306] [oaieval.py:229] Final report:
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/C: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/B: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/D: 2

class: modelgraded.classify:ModelBasedClassify
eval_type: cot_classify
modelgraded_spec: fact

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

A popular paper has been going around called 'The Reversal Curse: LLMs
trained on “A is B” fail to learn “B is A”'. I figured an Eval on this
would have a unique value.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific chemical element that has the atomic number
79, please respond to the best of your abilities."}, {"role": "user",
"content": "What is the name of the element with atomic number 79?"}],
"ideal": "The element with atomic number 79 is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a chemical element that is often associated with jewelry
and has the symbol Au, please respond to the best of your abilities."},
{"role": "user", "content": "Which element is this?"}], "ideal": "This
element is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific painting that was stolen from the Isabella
Stewart Gardner Museum in 1990, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the
Vermeer painting stolen from the Isabella Stewart Gardner Museum in
1990?"}], "ideal": "The name of the Vermeer painting stolen from the
Isabella Stewart Gardner Museum in 1990 is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a Vermeer painting that is still missing after being
stolen from a museum in Boston, please respond to the best of your
abilities."}, {"role": "user", "content": "Which painting is this?"}],
"ideal": "This painting is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific species of bird that is known for its
elaborate courtship dance, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the bird
species known for its moonwalk-like courtship dance?"}], "ideal": "The
bird species known for its moonwalk-like courtship dance is the Blue
Manakin."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a bird species that is known for its blue color and
unique courtship dance, please respond to the best of your abilities."},
{"role": "user", "content": "Which bird species is this?"}], "ideal":
"This bird species is the Blue Manakin."}

  ```
</details>

---
## [johny-b/evals](https://github.com/johny-b/evals)@[4b7a66bd45...](https://github.com/johny-b/evals/commit/4b7a66bd45f06156656e021e170e7574f6cde3f5)
#### Friday 2023-11-10 12:01:28 by Vilhjalmur Thorsteinsson

Added Icelandic inflection eval; JsonMatch eval function (#1387)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Icelandic noun phrase inflection

### Eval description

This eval consists of 3 x 100 samples in "easy", "medium" and "hard"
categories. Each sample
represents the task of inflecting a noun phrase in Icelandic, in all
four cases of the language
(nominative, accusative, dative and genitive), both singular and plural.
A noun phrase
consists of an adjective and a noun (e.g., "fallegur litur" = "beautiful
color").
In the easy category, both the adjective and the noun are
relatively common. In the medium category, they are less common, and in
the hard category they
are rare enough that it is pretty unlikely that they occur in any
training corpora.

### What makes this a useful eval?

The eval is designed to test the general grammatical proficiency of a
model in Icelandic, and
the eval accuracy is assumed to correlate with a model's ability to
generate grammatically
correct text in the language. GPT models have so far struggled with
generating correct Icelandic
text, even though GPT-4 was uniquely trained by RLHF in the language.
Icelandic is believed to
be a good bellwether for lower-resource, grammatically complex language
support in general.

Inflecting noun phrases is something that native language speakers do
without significant
effort, even if they have not seen the particular adjective and the noun
before, as it can be done on the
basis of generic grammatical pattern recognition. However, to date,
GPT-4 seems not to have
acquired enough of a "native feel" for Icelandic to be able to do this
task with high accuracy.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

**Note: this PR includes a new general eval class, JsonMatch, which is
not specific to the Icelandic evaluation
case. It allows completions and ideal answers to be represented as JSON
objects, comparing the objects
by individual key:value pairs. Tests and documentation of this
functionality are included in the PR.**

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"palestínskur fréttavefur\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"palestínskur fréttavefur\",
\"þf\": \"palestínskan fréttavef\", \"þgf\": \"palestínskum fréttavef\",
\"ef\": \"palestínsks fréttavefjar\"}, \"ft\": {\"nf\": \"palestínskir
fréttavefir\", \"þf\": \"palestínska fréttavefi\", \"þgf\":
\"palestínskum fréttavefjum\", \"ef\": \"palestínskra fréttavefja\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"hliðhollt lyfjapróf\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"hliðhollt lyfjapróf\",
\"þf\": \"hliðhollt lyfjapróf\", \"þgf\": \"hliðhollu lyfjaprófi\",
\"ef\": \"hliðholls lyfjaprófs\"}, \"ft\": {\"nf\": \"hliðholl
lyfjapróf\", \"þf\": \"hliðholl lyfjapróf\", \"þgf\": \"hliðhollum
lyfjaprófum\", \"ef\": \"hliðhollra lyfjaprófa\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"refsiverð stjörnuleit\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"refsiverð stjörnuleit\",
\"þf\": \"refsiverða stjörnuleit\", \"þgf\": \"refsiverðri
stjörnuleit\", \"ef\": \"refsiverðrar stjörnuleitar\"}, \"ft\": {\"nf\":
\"refsiverðar stjörnuleitir\", \"þf\": \"refsiverðar stjörnuleitir\",
\"þgf\": \"refsiverðum stjörnuleitum\", \"ef\": \"refsiverðra
stjörnuleita\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"japönsk landbúnaðarvara\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"japönsk landbúnaðarvara\",
\"þf\": \"japanska landbúnaðarvöru\", \"þgf\": \"japanskri
landbúnaðarvöru\", \"ef\": \"japanskrar landbúnaðarvöru\"}, \"ft\":
{\"nf\": \"japanskar landbúnaðarvörur\", \"þf\": \"japanskar
landbúnaðarvörur\", \"þgf\": \"japönskum landbúnaðarvörum\", \"ef\":
\"japanskra landbúnaðarvara\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"dýrmætt vistheimili\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"dýrmætt vistheimili\",
\"þf\": \"dýrmætt vistheimili\", \"þgf\": \"dýrmætu vistheimili\",
\"ef\": \"dýrmæts vistheimilis\"}, \"ft\": {\"nf\": \"dýrmæt
vistheimili\", \"þf\": \"dýrmæt vistheimili\", \"þgf\": \"dýrmætum
vistheimilum\", \"ef\": \"dýrmætra vistheimila\"}}"}
  ```
</details>

---
## [abhisheksharm-3/carbon-lang](https://github.com/abhisheksharm-3/carbon-lang)@[c7e6238fa8...](https://github.com/abhisheksharm-3/carbon-lang/commit/c7e6238fa8dd57672b0765e738f4c425a27cac3b)
#### Friday 2023-11-10 12:13:54 by Chandler Carruth

Introduce two speed-of-light benchmarks. (#3270)

The goal of these kinds of benchmarks is to help calibrate other
benchmarks and expectations. They benchmark the underlying hardware
capabilities that we can't avoid, and help illustrate bounds for what is
possible. The term "speed-of-light benchmark" references the aspect of
measuring how fast thing could possible run.

The first is a simple memory bandwidth measurement in the best case
scenario -- using `strcpy` over the buffer. This still does a minimal
number of writes to memory and examines each byte of input to see if it
is null, but can cheat in every way possible to run at the maximum speed
of hardware. To a certain extent, we never expect to get close to this
speed, but it's a good illustration of how much headroom the hardware
has available.

The second is potentially more interesting. This illustrates how fast a
byte-by-byte dispatch loop can potentially be. It uses the technique
that I'm hoping to use in the lexer itself of guaranteed tail recursion
to achieve this with a very small code footprint. The performance of
this technique, even when running in this extremely minimal setting to
establish bounds, is hugely dependent on the number of distinct dispatch
targets, and so the benchmark includes a healthy range to show the range
of performance that we might expect when running in a byte-by-byte mode.
Note that we should expect the lexer to be *faster* than this
"speed-of-light" whenever it is able to lex in larger granules than
byte-wise. But for complex, dense token sequences that force looking at
every byte, this shows the "worst case" "speed-of-light" in a sense.

On my recent AMD cloud VM instance, I get the following results running
the main lexer benchmark with these changes included:

```
-------------------------------------------------------------------------------------------------------------------------
Benchmark                                            Time             CPU   Iterations bytes_per_second tokens_per_second
-------------------------------------------------------------------------------------------------------------------------
BM_ValidKeywords                               3169403 ns      3169283 ns          221        188.44M/s        31.5529M/s
BM_ValidIdentifiers<1, 64, false>             12486725 ns     12486445 ns           51       117.953M/s        8.00868M/s
BM_ValidIdentifiers<1, 1, true>                3950455 ns      3950298 ns          178       72.4252M/s        25.3145M/s
BM_ValidIdentifiers<3, 5, true>               15562294 ns     15561178 ns           45       36.7712M/s        6.42625M/s
BM_ValidIdentifiers<3, 16, true>              16118656 ns     16118374 ns           44       68.0412M/s         6.2041M/s
BM_ValidIdentifiers<12, 64, true>             19116271 ns     19116258 ns           35       199.541M/s        5.23115M/s
BM_ValidMix/10/40                              7074336 ns      7073795 ns           93       140.744M/s        14.1367M/s
BM_ValidMix/25/30                              6790722 ns      6790006 ns          102       131.793M/s        14.7275M/s
BM_ValidMix/50/20                              5960514 ns      5960443 ns          118       112.594M/s        16.7773M/s
BM_ValidMix/75/10                              4325546 ns      4325556 ns          159       102.559M/s        23.1184M/s
BM_SpeedOfLightStrCpy                            24339 ns        24339 ns        29650       35.9049G/s        4.10858G/s
BM_SpeedOfLightDispatch<1>                     1756051 ns      1755800 ns          398       509.668M/s        56.9541M/s
BM_SpeedOfLightDispatch<2>                     1611973 ns      1611725 ns          436       555.228M/s        62.0453M/s
BM_SpeedOfLightDispatch<4>                     2064280 ns      2063990 ns          326       433.565M/s        48.4498M/s
BM_SpeedOfLightDispatch<8>                     2484055 ns      2483946 ns          280       360.263M/s        40.2585M/s
BM_SpeedOfLightDispatch<16>                    4550963 ns      4550894 ns          155       196.637M/s        21.9737M/s
BM_SpeedOfLightDispatch<32>                    6507077 ns      6507090 ns          107       137.523M/s        15.3679M/s
BM_SpeedOfLightDispatch<MaxDispatchTargets>    9071198 ns      9071217 ns           77       98.6499M/s        11.0239M/s
```

Even though we're not lexing anything in the speed-of-light benchmark,
the tokens-per-second measure is still meaningful because we *generated*
the token stream and know how many tokens we put into it. The dispatch
technique easily exceeds hits 10-million tokens/second, but we need to
do substantially better than that to lex at 10-million lines/second.
Fortunately, when the lexer is consuming more than one-byte tokens,
we're already faster than this. And the bytes-per-second numbers from
all but the worst case dispatch scenario are promising.

---
## [mobvoi/mobvoi-ticwatch-kernel](https://github.com/mobvoi/mobvoi-ticwatch-kernel)@[4d6fa57b4d...](https://github.com/mobvoi/mobvoi-ticwatch-kernel/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Friday 2023-11-10 12:19:30 by Jason A. Donenfeld

macsec: avoid heap overflow in skb_to_sgvec

While this may appear as a humdrum one line change, it's actually quite
important. An sk_buff stores data in three places:

1. A linear chunk of allocated memory in skb->data. This is the easiest
   one to work with, but it precludes using scatterdata since the memory
   must be linear.
2. The array skb_shinfo(skb)->frags, which is of maximum length
   MAX_SKB_FRAGS. This is nice for scattergather, since these fragments
   can point to different pages.
3. skb_shinfo(skb)->frag_list, which is a pointer to another sk_buff,
   which in turn can have data in either (1) or (2).

The first two are rather easy to deal with, since they're of a fixed
maximum length, while the third one is not, since there can be
potentially limitless chains of fragments. Fortunately dealing with
frag_list is opt-in for drivers, so drivers don't actually have to deal
with this mess. For whatever reason, macsec decided it wanted pain, and
so it explicitly specified NETIF_F_FRAGLIST.

Because dealing with (1), (2), and (3) is insane, most users of sk_buff
doing any sort of crypto or paging operation calls a convenient function
called skb_to_sgvec (which happens to be recursive if (3) is in use!).
This takes a sk_buff as input, and writes into its output pointer an
array of scattergather list items. Sometimes people like to declare a
fixed size scattergather list on the stack; othertimes people like to
allocate a fixed size scattergather list on the heap. However, if you're
doing it in a fixed-size fashion, you really shouldn't be using
NETIF_F_FRAGLIST too (unless you're also ensuring the sk_buff and its
frag_list children arent't shared and then you check the number of
fragments in total required.)

Macsec specifically does this:

        size += sizeof(struct scatterlist) * (MAX_SKB_FRAGS + 1);
        tmp = kmalloc(size, GFP_ATOMIC);
        *sg = (struct scatterlist *)(tmp + sg_offset);
	...
        sg_init_table(sg, MAX_SKB_FRAGS + 1);
        skb_to_sgvec(skb, sg, 0, skb->len);

Specifying MAX_SKB_FRAGS + 1 is the right answer usually, but not if you're
using NETIF_F_FRAGLIST, in which case the call to skb_to_sgvec will
overflow the heap, and disaster ensues.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Cc: stable@vger.kernel.org
Cc: security@kernel.org
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [filipsajdak/cppfront](https://github.com/filipsajdak/cppfront)@[cdf71bdca6...](https://github.com/filipsajdak/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Friday 2023-11-10 12:50:34 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[830e002a27...](https://github.com/Huffie56/cmss13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Friday 2023-11-10 13:17:06 by QuickLode

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
## [NashIlli/flame](https://github.com/NashIlli/flame)@[2f973abe8b...](https://github.com/NashIlli/flame/commit/2f973abe8b298a4f6f1164065783de560953d789)
#### Friday 2023-11-10 13:49:27 by Luan Nico

docs: Improved spellchecking (#2722)

Improve our spellchecker (cspell) configuration and dictionary file
organization.

# Rationale

This is a proposal to establish a few changes:
* better separate our dictionary files into different categories of
types of words we are including
* improve the cspell regexes to be more aggressive
* be less lenient to what kinds of words we are adding to our
dictionaries
* have the dictionary file also serve as an explanation for obscure
references that cannot be easily derived from the word

Essentially my goal is that either when reviewing a PR that adds a new
entry to our dictionary, or when reading the dictionary files
themselves, it is immediately obvious what the entries are and why they
are there. Currently it can be just a dumpster we throw anything into if
spellcheck fails.

# Proposal

This PR-as-a-proposal essentially do the following changes.

## Split Dictionary Files

Proposes a better separation for our dictionary files. Currently we have
3 that are a bit broad and not super clear on what goes where. This
breaks it down a bit more and adds a comment to each file explaining
what kinds of terms should be added to each; that also serves as a
general guidance for what kinds of words should be added to the lexicon
in general, and makes it harder for mistakes to make into it.

* `flame_dictionary`: remains pretty much unchanged; it is dedicated to
Flame-related words, including companies, tools, and libraries (and
their associated concepts) mentioned on our codebase. Basically a
collection of proper-nouns relating to companies and libraries we
mention.
* `dart_dictionary`: new file for Dart and Flutter related terms
* `sphinx_dictionary`: unchanged, for Sphynx related terms
* `people_dictionary`: specific for people names and usernames
referenced on the codebase (in TODOs, mentions, etc)
* `words_dictionary`: actual English-language words (or common
abbreviations) missing from CSpell
* `gamedev_dictionary`: this was our biggest file that contained all
sort of things. it has been mostly broken down and now only contains
general development-adjacent terms and expressions

## Include definitions

Except for the `words` dictionary, which should be self-explanatory (as
it basically covers for "holes" in CSpell standard dictionary, which I
have been finding a bit lacking), every other file will contain terms in
the form:

```
word # definition of the word
```

What exactly the definition is can slightly vary depending on which
dictionary file we are talking about, but the examples should be
self-explanatory.

As an example, for the gamedev file, it should provide some simple
guidance as to what the term means, or if it's an acronym or
abbreviation, what it stands for. The goal is not to teach the entire
concept to someone unfamiliar, but allow them to "google" it for
themselves by giving enough context, so they can confirm their
suspicions. For example, if they see `LTRB` somewhere by itself, they
are not able to "just google that" because it is too vague. The
dictionary file provides enough context for the user to figure out
however much deeper information they want about any particular subject.
It will also disambiguate from any non-Flame related homonyms. For
people on the people file and companies on the flame file, the
description will provide links to clearly disambiguate what they are;
for tools, a brief description of what the tool is for is also included.
And so on.

The goal is not to build a comprehensive, in depth-guide to each word we
use, but rather to give the bare minimum of context on what this term
"is doing" on our codebase.

## Be less lenient with terms

My idea with these two major changes combined, is that we are overall
more tactical about which terms we want to add to the dictionaries.
Adding a word to the dictionary file is essentially giving carte blanche
to anyone in the future to reuse that term anywhere. I think we should
see spellchecker violations as "warnings"; we decide on the set of
warning rules we want to enable for the entire project (hopefully all
the ones that make sense; or have a reason for disabling the ones that
don't). We might need to violate these warnings sporadically, for
example, we ban `print` on the codebase but might need to allow it
specifically in a couple places. But we would not disable the entire
warning to do that, rather we would add a specific comment-bypass on the
smallest possible scope that encompasses all the relevant lines. We
would also add a proper comment explaining why we are bypassing the
general rule in this specific place.

Similarly, we should not have one-off violations on the dictionary file,
even if they make sense in the one place they occur, but we should
encourage more liberal use of scoped bypasses for such cases. These
Ukrainian words are required in this file, but should not be on the
dictionary as it does not make sense to use foreign languages anywhere
else:

```
// used as examples of Ukrainian words on the documentation below
// cSpell:ignore рушниця, рушниці, рушниць
```

It might look inelegant to have to include that, but just like a
warning-bypass comment, accompanied by the explanatory proper-comment,
this actually provides helpful guidance and context for the reader that
might be confused with the usage of incomprehensible terms.

This also encourages people to avoid obscure terms that are not already
in our dictionary (i.e. that we have already "bought in" and paid the
mental load investment cost), making our code (and docs) easier to parse
and read for everyone. I want to be extremely clear that that **does
not** mean we need to "dumb down" anything whatsoever, or do any sort of
gymnastics to avoid the wrath of an incompetent spellchecker.

But, for example [when spelling "cave
ace"](https://github.com/flame-engine/flame/pull/2304) in variable names
in a random example, having it typed as `caveAce` instead of `caveace`
can slightly help with readability, specially for non-native speakers
(like most of us). It is an extremely minor insignificant gain, but
having the dictionary file require a brief description will nudge us to
give a bit more thought into each "bypass" we are adding.

(note: a similar issue that I have not yet addressed is "spine boy", but
I will leave that for followups and just added that one to the
dictionary for now, as I am still over the fence on that one since it is
an actual "known" character with a dedicated page, so it is more like a
proper noun - as a specific decision I think it is out-of-scope of the
broader discussion).

---
## [inwaves/evals](https://github.com/inwaves/evals)@[429a6b695e...](https://github.com/inwaves/evals/commit/429a6b695e28387d68adbfad500903a39abc3b11)
#### Friday 2023-11-10 14:05:53 by pancoaster

Add eval : Research Question Extraction (#1334)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

research-question-extraction

### Eval description

The objective of this evaluation explores Other foundational capability
for research purposes. The task requires extraction of the particular
value specified as the 'Research Questions' from different scholarly
articles. The eval contains 19 samples of articles.

### What makes this a useful eval?

Rest assured that you have the right to use the data submitted via this
eval. These scholarly papers originate from the Journal of Engineering
Education. The subset of articles selected meets the requirement of
Attribution 4.0 International (CC BY 4.0).

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Interdisciplinary engineering education: A review of vision, teaching,
and support \n Antoine Van den Beemt, Miles MacLeod, Jan Van der Veen,
Anne Van de Ven, Sophie van Baalen, Renate Klaassen, Mieke Boon \n
Abstract \n Background \n Societal challenges that call for a new type
of engineer suggest the need for the implementation of interdisciplinary
engineering education (IEE). The aim of IEE is to train engineering
students to bring together expertise from different disciplines in a
single context. This review synthesizes IEE research with a focus on
characterizing vision, teaching practices, and support. \n \n Purpose \n
We aim to show how IEE is conceptualized, implemented, and facilitated
in higher engineering education at the levels of curricula and courses.
This aim leads to two research questions: \n \n What aspects of vision,
teaching, and support have emerged as topics of interest in empirical
studies of IEE? \n \n What points of attention regarding vision,
teaching, and support can be identified in empirical studies of IEE as
supporting or challenging IEE? \n \n Scope/Method \n Ninety-nine studies
published between 2005 and 2016 were included in a qualitative analysis
across studies. The procedure included formulation of research
questions, searching and screening of studies according to
inclusion/exclusion criteria, description of study characteristics,
appraisal, and synthesis of results. \n \n Conclusions \n Challenges
exist for identifying clear learning goals and assessments for
interdisciplinary education in engineering (vision). Most pedagogy for
interdisciplinary learning is designed to promote collaborative teamwork
requiring organization and team management. Our review suggests that
developing interdisciplinary skills, knowledge, and values needs sound
pedagogy and teaming experiences that provide students with authentic
ways of engaging in interdisciplinary practice (teaching). Furthermore,
there is a limited understanding of what resources hinder the
development of engineering programs designed to support
interdisciplinarity (support). \n \n "}], "ideal": ["What aspects of
vision, teaching, and support have emerged as topics of interest in
empirical studies of IEE? What points of attention regarding vision,
teaching, and support can be identified in empirical studies of IEE as
supporting or challenging IEE?"]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Community cultural wealth in science, technology, engineering, and
mathematics education: A systematic review \n Maya Denton, Maura
Borrego, Audrey Boklage \n Abstract \n Background \n One emerging
approach to diversity and inclusion in engineering is to take an
assets-based view of what students from nondominant communities bring to
their education and work experiences. \n \n Purpose/Hypothesis \n The
purpose of this review is to understand how community cultural wealth
(CCW), an assets-based framework, has been applied in science,
technology, engineering, and mathematics (STEM) education research. We
address research questions focused on (a) the characteristics of studies
using CCW in STEM education, (b) examples of the six types of capital
(aspirational, linguistic, familial, navigational, social, and
resistant) in STEM educational settings, and (c) gaps and opportunities
in how CCW is being applied in STEM education. \n \n Design/Method \n We
identified 33 dissertations, theses, journal articles, and conference
papers using systematic review procedures. To qualify, each study must
present empirical data and include at least one type of CCW capital in
its results or discussion. We coded study characteristics, such as
methods, participant populations, and research setting. We qualitatively
analyzed each of the six types of CCW capital. \n \n Results \n Studies
tended to focus on higher education settings, engineering, and
qualitative methods, particularly student interviews. We identified
several specific engineering-relevant examples of assets for each type
of capital. Future work should collect data from faculty, staff, and
family members identified in several studies as important to CCW in
addition to foregrounding student voices. \n \n Conclusions \n In
synthesizing existing studies, this review provides insight into how an
assets-based framework is being interpreted and provides a foundation
for more assets-based perspectives in future engineering education work.
\n \n "}], "ideal": ["(a) the characteristics of studies using CCW in
STEM education, (b) examples of the six types of capital (aspirational,
linguistic, familial, navigational, social, and resistant) in STEM
educational settings, and (c) gaps and opportunities in how CCW is being
applied in STEM education."]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"How Latiné engineering students resist White male engineering culture:
A multi-institution analysis of academic engagement \n Patton O.
Garriott, Ayli Carrero Pinedo, Heather K. Hunt, Rachel L. Navarro, Lisa
Y. Flores, Cerynn D. Desjarlais, David Diaz, Julio Brionez, Bo Hyun Lee,
Evelyn Ayala, Leticia D. Martinez, Xiaotian Hu, Megan K. Smith, Han Na
Suh, Gloria G. McGillen \n Abstract \n Background \n Although
participation rates vary by field, Latiné and women engineers continue
to be underrepresented across most segments of the engineering
workforce. Research has examined engagement and persistence of Latiné
and White women in engineering; however, few studies have investigated
how race, ethnicity, gender, and institutional setting interact to
produce inequities in the field. \n \n Purpose \n To address these
limitations, we examined how Latina, Latino, and White women and men
students' engagement in engineering was informed by their intersecting
identities and within their institutional setting over the course of a
year. \n \n Method \n We interviewed 32 Latina, Latino, and White women
and men undergraduate engineering students attending 11 different
predominantly White and Hispanic Serving Institutions. Thematic analysis
was used to interpret themes from the data. \n \n Results \n Our
findings illustrate how Latinas, Latinos, and White women developed a
strong engineering identity, which was critical to their engagement in
engineering. Students' engineering identity was grounded in their
perceived fit within engineering culture, sense of purpose for pursuing
their degree, and resistance to the dominance of White male culture in
engineering. Latinas described unique forms of gendered, racialized
marginalization in engineering, whereas Latinas and Latinos highlighted
prosocial motivations for completing their degree. \n \n Conclusions \n
Findings suggest that institutional cultures, norms, and missions are
critical to broadening participation of Latinas, Latinos, and White
women in engineering. Disrupting White male culture, leveraging Latiné
students' cultural wealth, and counter-framing traditional recruitment
pitches for engineering appear to be key in these efforts. \n \n "}],
"ideal": ["I do not know."]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Impact of COVID-19 on sense of belonging: Experiences of engineering
students, faculty, and staff at Historically Black Colleges and
Universities (HBCUs) \n Trina L. Fletcher, Jay P. Jefferson, Brittany
Boyd, Sung Eun Park, Lesia Crumpton-Young \n Abstract \n Background \n
COVID-19 has spurred a global crisis that has disrupted everyday lives
and impacted the traditional methods, experiences, and abilities of
higher education institutions' students, faculty, and staff, especially
at Historically Black Colleges and Universities (HBCUs). \n \n
Purpose/Hypothesis \n Given the pressing need demonstrated by the
National Academies to advance the utilization of science, technology,
engineering, and mathematics (STEM) education at HBCUs, this study aimed
to explore the abrupt transition to remote teaching and learning at
HBCUs guided by the following research question: How has COVID-19
impacted the success and persistence of engineering students, faculty,
and staff at HBCUs? \n \n Design/Methods \n Three surveys were
developed, tested, piloted, and sent to HBCU stakeholders using a
snowball sampling approach via email and social media outreach. \n \n
Results \n Of the 171 student respondents (126 engineering majors), 79%
agreed that not being able to access faculty in person affected their
academic performance. Additionally, across all HBCU stakeholders'
surveys, students had a statistically significant higher response when
asked if the transition to virtual learning increased their overall
levels of stress and anxiety. \n \n Conclusions \n During a global
pandemic, HBCUs continue to provide a culture of support and inclusion
for students, faculty, and staff in engineering. Increased stress levels
experienced by students indicate that a safe and adequate transition
back to campus is essential for their social and academic persistence.
Due to the well-documented inequities HBCUs faced before the pandemic,
the impact of this unprecedented on their continued contributions toward
broadening participation in engineering for students should be further
explored. \n \n "}], "ideal": ["How has COVID-19 impacted the success
and persistence of engineering students, faculty, and staff at HBCUs?"]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Collaborative construction of artificial intelligence curriculum in
primary schools \n Yun Dai, Ang Liu, Jianjun Qin, Yanmei Guo, Morris
Siu-Yung Jong, Ching-Sing Chai, Ziyan Lin \n Abstract \n Background \n
The recent discussion of introducing artificial intelligence (AI)
knowledge to K–12 students, like many engineering and technology
education topics, has attracted a wide range of stakeholders and
resources for school curriculum development. While teachers often have
to directly interact with external stakeholders out of the public
schooling system, few studies have scrutinized their negotiation
process, especially teachers' responses to external influences, in such
complex environments. \n \n Purpose \n Guided by an integrated
theoretical framework of social constructionism, this research examined
the process of how a teacher-initiated AI curriculum was constructed
with external influences. The research focused on teachers' perspectives
and responses in mediating external influences into local schools and
classrooms. \n \n Methods \n A 3-year ethnographic study was conducted
in relation to an AI curriculum project among 23 Computer Science (CS)
teachers from primary schools. Data collected from ethnographic
observation, teacher interviews, and artifacts, were analyzed using open
coding and triangulation rooted in the ethnographic, interpretivist
approach. \n \n Results \n Three sets of external influences were found
salient for teachers' curriculum decisions, including the orientation of
state-level educational policies, AI faculty at a partner university,
and students' media and technology environments. The teachers'
situational logics and strategic actions were reconstructed with thick
descriptions to uncover how they navigated and negotiated the external
influences to fulfill local challenges and expectations in classrooms
and schools. \n \n Conclusions \n The ethnographic study uncovered the
dynamic and multifaceted negotiation involved in the collaborative
curriculum development, and offers insights to inform policymaking,
teacher education, and student support in engineering education. \n \n
"}], "ideal": ["I do not know."]}

  ```
</details>

---
## [inwaves/evals](https://github.com/inwaves/evals)@[97aa5483de...](https://github.com/inwaves/evals/commit/97aa5483de8673172d5eaabc33ba7e7cf3561ffe)
#### Friday 2023-11-10 14:05:53 by samta-kamboj

Multilingual EXAMS and Arabic Literature Question Answers (By IIAI-G42) (#1326)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Exams (Multilingual high school QA)
Arabic Literature Questions

### Eval description

EXAMS: This is a benchmark dataset for multilingual question answering
from high school examinations. It consists of more than 12,000
high-quality high school exam questions in 16 languages, covering 8
language families and 24 school subjects from Natural Sciences and
Social Sciences, among others. [More info about the
data](https://github.com/mhardalov/exams-qa)

Arabic Literature Question Answers: This has 175 MCQs related to Arabic
Literature

### What makes this a useful eval?

Evaluating GPT-4 with Arabic literature, high school questions in Arabic
and low-resource languages helps checking its linguistic diversity,
cultural understanding, and educational proficiency beyond English
language and would be helpful creating more ethical and inclusive AI
models in future.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content':
'وقعت الحملة الفرنسية على مصر سنة ؟\nA. 1789\nB. 1798\nC. 1797\nD.
1779\nAnswer:'}], 'ideal': '[B]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'من
مؤلفات أحمد أمين ؟\nA. الغربال\nB. على هامش السيرة\nC. زعماء الإصلاح\nD.
رجال الدعوة والفكر\nAnswer:'}], 'ideal': '[C]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'في
أي عصر كان ابن زيدون ؟\nA. العصر الأموي\nB. العصر الأندلسي\nC. العصر
العباسي\nD. العصر الإسلامي\nAnswer:'}], 'ideal': '[B]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'من
قرض هذا الشعر : أنا البحر في أحشائه الدر كامن فهل سألوا الغواص عن
صدفاتي:\nA. حافظ ابراهيم\nB. إيليا أبو ماضي\nC. أحمد شوقي\nD.
البارودي\nAnswer:'}], 'ideal': '[A]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'ما
معنى ASEAN باللغة العربية ؟\nA. اتحاد البلدان الاطلانطية الشرقية
الجنوبية\nB. تحالف الدول النامية\nC. اتحاد الدول المصدرة للنفط\nD. اتحاد
البلدان الاطلانطية الغربية\nAnswer:'}], 'ideal': '[A]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content':
'إبراهيم الكاتب من مؤلفات ؟\nA. العقاد\nB. محمود تيمور\nC. المازني\nD.
عبد الرحمن شكري\nAnswer:'}], 'ideal': '[C]'}
  ```
</details>

---
## [inwaves/evals](https://github.com/inwaves/evals)@[30e35436be...](https://github.com/inwaves/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Friday 2023-11-10 14:05:53 by Nazar

Hard russian computer science tasks  (#1323)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [inwaves/evals](https://github.com/inwaves/evals)@[305b237cdb...](https://github.com/inwaves/evals/commit/305b237cdb3884c7ddb6a5d12cb184a83551fcba)
#### Friday 2023-11-10 14:05:53 by Anders Wang-Rask

Irrelevant negative diversion (#1318)

Tests the model's reasoning ability in face of a negative diversion
(e.g. "However, ...") with irrelevant information.

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

irrelevant-negative-diversion

### Eval description

The eval tests the model's ability to reason. It has been demonstrated
that a negative diversion (e.g. "However", "Despite that", "That being
said") can lead the model to a wrong conclusion. Even when the negative
diversion contains more or less irrelevant information (e.g. "However,
they often squabbled as children.")

### What makes this a useful eval?

I have tested GPT-4 through ChatGPT and can see that it often gets these
wrong. It's a little bit random. Where all the samples have the ideal
answer of "yes", ChatGPT would often say No or more often say that it
was unable to conclude.

The prompt is asking the model to choose "yes" or "no" according to what
is most reasonable.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. However, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. But, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. Unfortunately, Anna and Briana squabbled often
as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Sadly, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. But regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Even though, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Despite, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. That being said, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
  ```
</details>

---
## [cowbot92/Yogstation](https://github.com/cowbot92/Yogstation)@[f39d74c3a6...](https://github.com/cowbot92/Yogstation/commit/f39d74c3a66c41a5ebb468dc3d61b0787f8327be)
#### Friday 2023-11-10 14:52:48 by Waterpig

Invisible touch - this time for real (#20742)

* This was surprisingly easy

* Well this might be funny

* Hm

* Oh boy it's working

* I might be going insane

* Checks moved

---
## [Birdtalon/tgstation](https://github.com/Birdtalon/tgstation)@[6bdf052a84...](https://github.com/Birdtalon/tgstation/commit/6bdf052a84c07ff54065dd7906d9c9da540a07b8)
#### Friday 2023-11-10 14:53:33 by lizardqueenlexi

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
## [Birdtalon/tgstation](https://github.com/Birdtalon/tgstation)@[bd56c3723e...](https://github.com/Birdtalon/tgstation/commit/bd56c3723e4a60f8a0e3b30d2f542e17905d9321)
#### Friday 2023-11-10 14:53:33 by EricZilla

Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring (#78761)

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

---
## [Birdtalon/tgstation](https://github.com/Birdtalon/tgstation)@[66a1cd6ab2...](https://github.com/Birdtalon/tgstation/commit/66a1cd6ab2c46d84c6773d94fabb08f10c3e6fcd)
#### Friday 2023-11-10 14:53:33 by Wallem

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
## [elastic/kibana](https://github.com/elastic/kibana)@[cd909f03b1...](https://github.com/elastic/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Friday 2023-11-10 16:08:11 by Kyle Pollich

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
## [linkylink21/tgstation](https://github.com/linkylink21/tgstation)@[eb28d04f08...](https://github.com/linkylink21/tgstation/commit/eb28d04f08a172c3bf671747072e1120b8e43d21)
#### Friday 2023-11-10 16:36:46 by Jacquerel

Watcher Nest Lavaland Ruin (#78790)

## About The Pull Request

Adds a small new lavaland ruin, the Watchers' Grave.


![image](https://github.com/tgstation/tgstation/assets/7483112/9c3fa6f0-3e7d-4540-8646-5229eb11445b)

![image](https://github.com/tgstation/tgstation/assets/7483112/93bc14f0-9a0c-40d3-bd30-cc79a0d85752)

You will need to figure out yourself how to find a way through the walls
surrounding it (it's not very hard).
This is mostly just atmospheric but also serves as a delivery vehicle
for a unique item; an orphaned Watcher egg.
(That's kind of it in terms of loot, unless you count a handful of
lavaland mob corpses and mushrooms).

You can either eat this (it's an egg), throw it at someone to spawn an
angry watcher, or keep hold of it for a while and see what happens.

<details>


![dreamseeker_cMNnZXjfgL](https://github.com/tgstation/tgstation/assets/7483112/841db8fc-19ac-431f-aa66-c9ec5fbedbc3)

That's right it's your very own baby watcher.
It orbits your head and shoots at lavaland creatures for unimpressive
damage. It won't ever intentionally shoot a player but they might walk
in front of it, as it doesn't hurt very much they will probably forgive
you.
If you die it will continue circling your corpse to guard it against
predation.
</details>

In creating this ruin I also added a new component called "corpse
description".
It provides some extra examine text to a corpse which is removed
permanently if the mob is revived.
There's a field you can varedit on corpse spawners (or make a subtype)
which will automatically apply it to spawned corpses.
You can use it for environmental storytelling. Or admins can use it to
make fun of how you died.

Also I fixed basic mobs runtiming when examined by ghosts.

## Why It's Good For The Game

More variety in map generation. It's cute.
Adds a tool that mappers might like.

## Changelog

:cl:
add: Adds a new lavaland ruin where you can find a unique egg.
/:cl:

---
## [CyrusNajmabadi/roslyn](https://github.com/CyrusNajmabadi/roslyn)@[6a2b62c9f4...](https://github.com/CyrusNajmabadi/roslyn/commit/6a2b62c9f487ce45c0e9873b074bb51ecde4886c)
#### Friday 2023-11-10 16:48:17 by Cyrus Najmabadi

Fix contract assertion firing with SG OOP syncing.

This was a very subtle issue. It was found thanks to some paranoid asserts added when doing the "perform SG generation in OOP process" work.

First, some background. We have a type called SourceText which represents the string-oriented (not byte-oriented) contents of a file. That type also exposes a concept of the "content checksum". This content checksum corresponds to the original bytes the source-text was created from, and not necessarily the current 'string-oriented view' the SourceText represents.

In other words, the following axiom does NOT hold:

sourceText.GetChecksum() == SourceText.From(sourceText.ToString(), sourceText.Encoding, sourceText.HashAlgorithm).GetChecksum()

As an example of when this might happen, consider that the bytes of a file may or may not include the BOM for utf8. So you might have two files with different byte contents that end up representing the same char contents.

Unfortunately, the SG OOP syncing code assumed the above was true. If would sync over file contents, then assert that the checksum we then produced on the host side matched what was on the OOP side. This assertion was not valid given the above, and our connection would die.

The fix is not to just to remove the assertion though. If we did that, we'd end up in a bad state where the host and the OOP side would always disagree on the content checksum of these SG files, causing them to resync on each solution fork. That would be very bad for perf (Esp. as SG files can be enormous). The fix instead is to understand that the checksum on the OOP side may not be computable on the host side, and instead just trust and use that server-side-computed checksum locally for all checksum related questions we have.

Note: A cleaner fix will be possible if/when we get approval on the following API suggestion: #70752. With that API we would be able to produce a SourceText locally with the exact same checksum as what was on the OOP side. This would be nice to have in the long term so that if we have any other code that ends up looking directly at the SourceText for its checksum, it doesn't get confused as to why the host and OOP disagree on it.

---
## [Dover-Sherborn-Coding-Club/Mock_Hackathons](https://github.com/Dover-Sherborn-Coding-Club/Mock_Hackathons)@[206ef61715...](https://github.com/Dover-Sherborn-Coding-Club/Mock_Hackathons/commit/206ef617156f0d6ee36bb93c21526466b167d730)
#### Friday 2023-11-10 17:12:35 by piku ashk

Add files via upload

yeahh i first had an ssl issue then i used "pyOpenSSL" then the site just infinitely loads
please help
i hate my life

---
## [michelledunlap/vigilant-engine](https://github.com/michelledunlap/vigilant-engine)@[d93ddede6c...](https://github.com/michelledunlap/vigilant-engine/commit/d93ddede6c06932bfe0d0eeede6421fce8c328c3)
#### Friday 2023-11-10 17:26:01 by Michelle Dunlap

Update index.html

Organizing the feelings such that they are in separate columns. So Sadness will be its own column, with 6 columns under that (Suffering, Sadness, Disappointed, Shameful, Neglected, Despair), and each of those will have 2 columns (Agony and Hurt under Suffering, etc.)

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[69ea3c81ad...](https://github.com/DanaDririon/Skyrat-tg/commit/69ea3c81ad86a0356af947f11fe3bd2ca953b0af)
#### Friday 2023-11-10 18:52:12 by SkyratBot

[MIRROR] Mafia can be played on your PDA [MDB IGNORE] (#24485)

* Mafia can be played on your PDA (#78576)

## About The Pull Request

Mafia is now friggin playable from the PDA, I also changed other stuff
too

- You can't use abilities on dead people if you're not supposed to (cant
kill the same person over and over)
- Changelings cant kill other Changelings
- Changelings can now only talk to eachother at night, rather than using
:j
- Everyone starts spawned in the center of the map, since people playing
on PDA can't move their characters. This is so everyone can hear PDA
users in person, as I don't want the chat log to be mandatory.

To do this, all messages you are meant to be able to see, is now logged
for you to see in your Mafia panel. This essentially means that people
playing through the PDA get a downgraded version of it, but I don't know
how much larger I want this UI to be.

Playing Mafia through the PDA will not tell you of other players ahead
of time when signing up (as it shows ckeys + pdas), but they can see the
names in-game. Unfortunately this means we'll have to remove your
customization coming with you, to prevent using it to tell who is dead
in round.

Things I am missing
- Program overlays on PDA/Laptop/Computer
- Icon for the app's header while a game is active

I'm not a spriter and can't make either of these

This is the new UI

![image](https://github.com/tgstation/tgstation/assets/53777086/7cf503d9-b2e2-4127-874a-acad6425d649)

I also fixed alert calls for PDAs and stuff

![image](https://github.com/tgstation/tgstation/assets/53777086/e09b2e5e-b9e7-43ae-9273-c168e9c8e642)

and removed the X at the top on computers since they had no battery

![image](https://github.com/tgstation/tgstation/assets/53777086/d3dd8307-805c-4aba-be5e-4c24a0bdcb91)

Looks a little better now hopefully 👍

## Why It's Good For The Game

- The current Arcade app sucks, and is a solo game. This is much more
entertaining and you can talk to others in it, which is swag as fuck.
- There's a larger potential playerbase for the Minigame making it more
likely to be played.
- Sets groundwork for a better version of
https://github.com/tgstation/tgstation/pull/75879
- Adds more suspense and teamwork in the minigame.

## Changelog

:cl: JohnFulpWillard, sprites by CoiledLamb
add: You can now play Mafia on your PDA.
balance: Mafia changelings can now only talk to eachother during the
night.
fix: Mafia abilities can't be repeatedly used on people.
/:cl:

* Mafia can be played on your PDA

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[c63f897521...](https://github.com/DanaDririon/Skyrat-tg/commit/c63f897521485898e00425a6c001495f7eef5de6)
#### Friday 2023-11-10 18:52:12 by SkyratBot

[MIRROR] It is now possible to survive the Mansus  [MDB IGNORE] (#24490)

* It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

* It is now possible to survive the Mansus

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[53cfff6ae1...](https://github.com/DanaDririon/Skyrat-tg/commit/53cfff6ae1cd62766395534a6f4c8aa468c5066c)
#### Friday 2023-11-10 18:52:12 by SkyratBot

[MIRROR] Actually supports alpha passed into emissive stuff [MDB IGNORE] (#24481)

* Actually supports alpha passed into emissive stuff (#79117)

## About The Pull Request

Ok so like, the emissive procs have an alpha argument right? The thing
is, the thing is it doesn't fucking do anything.

Alpha is a component of the color var (at least when it's a matrix), so
when we set alpha and then set color to a matrix, the alpha gets
overriden. Inverse is also true.

I want to support alpha args, since I like the idea of dimmable
emissives. Soooooo
Let's take the alpha arg, divide it by 255, and replace everything that
cares about alpha (as an intensity thing) with it.

This lets us do transparent emissives and transparent emissive blockers.

I added some guard checks to hopefully avoid the list init most of the
time (it is in theory comprable since color sets should copy but I don't
trust byond to optimize for that)
Also modified the macros to suppport what I'm doing nicely

## Why It's Good For The Game

We should support this, and now we do

* Actually supports alpha passed into emissive stuff

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[da055688f3...](https://github.com/facebook/pyre-check/commit/da055688f32fb130e3d3669be93dde81822ea2a5)
#### Friday 2023-11-10 18:53:20 by Steven Troxler

Add a transform for AddPatch

Summary:
# This stack: A typeshed patcher

This stack implements - at a level of correctness and completeness
that is adequate for all current patches, both against the pinned
upstream version and the latest - the typeshed patcher design as
outlined in our design doc from 2022:
https://fburl.com/gdoc/ju13p4v6
(sorry that link probably won't work externally)

This work is important for two reasons:
- It was already difficult to apply our patches, which were sensitive to line number and specific surrounding context, to upstream as of 2022; I remember it taking on the order of half a day to get the patches all regenerated then.
- Since then we've roughly 10x'ed the number of patches due to ReadOnly, meaning that by extrapolation it might have taken close to a week (for reference, it took me a week to implement this new patcher *and* apply the upgrade!)

**How much of the spec is implemented?**

It implements all the actions in the spec except for `DeleteImport`, which we realized we don't need in the current form:
- Many imports (for example `import foo` or `from foo import bar`) define a name in global scope, so a normal Delete or Replace action makes perfect sense. See D51161405 for details.
- The cases that don't fit cleanly are dotted imports (`import foo.bar`), in which case they technically don't define a single name but rather a stack of names because `foo` is implicitly imported and `bar` is an attribute on it. The spec doesn't actually help with this since the problem is more whether we're willing to use a qualified "name" or not as an action target, rather than the action per se.
   - For now we just don't support patching dotted names; it makes more sense to have that discussion if/when we need it.

**How general is the implementation?**

The implementation I wound up with is general enough to handle
all existing patches, both against our current pinned version of
typeshed and against the latest.

But it has multiple known gaps besides just the qualified-name
import I mentioned above. Most gaps are related to cases where
we need to be able to modify a top-level statement rather than
outright deleting or replacing it:
- imports defining many names like `from foo import bar, baz`
   can't currently be targeted for deletion or replacement
- if/else blocks are supported if they only define a single name,
   but if they define many names (for example a bunch of
  method definitions all in a single if block guarding on `sys.version`)
  they aren't currently supported.

The strategy for these unsupported cases is to detect them and raise
an error explaining what happened rather than silently fail to apply
a patch, in case an upgrade triggers one of these scenarios.

We could probably support this much better with a more
libcst-visitor-centric pattern, but we need to make sure it
is both simple enough to maintain and efficient enough for
dozens of patches on a huge file like `builtins.pyi` to be
fairly quick. I'll look into this later, but I want to prioritize an
upgrade first.

**About the stack itself**

This stack records my actual evolution of thinking about the implementation, so at some points the initial simpler design is generalized as I add more patching actions. I didn't try to rewrite
the stack so that the initial design becomes an oracle on future
needs.

I'm happy to take any suggestions, but anything that isn't trivial
I'd prefer to fix-forward rather than in-place, since the final
code is working and restacks can be quite difficult.

The code could probably benefit from unit tests of failure cases
as well; I didn't prioritize this because from my dev standpoint
I didn't need it (I was just recreating existing stubs) but I should
probably stack some on top.

# This diff: Start working on libcst transforms

I decided to start the patcher by working on the codemods themselves, which are easy to unit test, and only build the command-line tool once I have enough transforms ready to actually try patching at least one real file.

This is the first of the libcst transforms I will write; each transform
corresponds to one action from the typeshed patcher spec (which
describes how patch actions can be expressed in toml format).

The code should be mostly self-explanatory: we find the scope
the patch says to add to, then add statements to either the top
or bottom. The trickiest thing about it is that because LibCST
is indentation-aware class bodies have a bit of complexity in them
related to indented vs non-indented bodies; our result will always
be indented for simplicity.

**Next 2 diffs: refactor this code to make it reusable**

This diff is a fairly clean stand-alone implementation of an add
transform in idiomatic libcst, but it isn't actually the best code
layout given that we need a bunch of similar transforms each of
which operate on a parent scope.

As a result, I take this working code and refactor it in the next
2 diffs to really emphasize that the scope *finding* logic (which
is primarily a matter of traversing classes in the visitor) is
largely independent of the scope *patching* logic (which really
amounts to removing and/or adding some statements from/to
a class or module body).

Reviewed By: grievejia, connernilsen

Differential Revision: D50996596

fbshipit-source-id: 423807d1c9f8eef4e0a381db6e261ab424e2d553

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[9ff9e4b9a8...](https://github.com/AnywayFarus/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Friday 2023-11-10 18:55:35 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[071f6063e6...](https://github.com/AnywayFarus/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Friday 2023-11-10 18:55:35 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[0d5f9907a2...](https://github.com/AnywayFarus/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Friday 2023-11-10 18:55:35 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [PanUcitelCz/Digi-podpora-Z-U-FPE-KVD](https://github.com/PanUcitelCz/Digi-podpora-Z-U-FPE-KVD)@[915c2b793b...](https://github.com/PanUcitelCz/Digi-podpora-Z-U-FPE-KVD/commit/915c2b793bc6a718c47de35a7010bce03343ce7a)
#### Friday 2023-11-10 20:25:12 by kolarv

upravený console log

According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because bees don’t care what humans think is impossible.” SEQ. 75 - “INTRO TO BARRY” INT. BENSON HOUSE - DAY ANGLE ON: Sneakers on the ground. Camera PANS UP to reveal BARRY BENSON’S BEDROOM ANGLE ON: Barry’s hand flipping through different sweaters in his closet. BARRY Yellow black, yellow black, yellow black, yellow black, yellow black, yellow black...oohh, black and yellow... ANGLE ON: Barry wearing the sweater he picked, looking in the mirror. BARRY (CONT’D) Yeah, let’s shake it up a little. He picks the black and yellow one. He then goes to the sink, takes the top off a CONTAINER OF HONEY, and puts some honey into his hair. He squirts some in his mouth and gargles. Then he takes the lid off the bottle, and rolls some on like deodorant. CUT TO: INT. BENSON HOUSE KITCHEN - CONTINUOUS Barry’s mother, JANET BENSON, yells up at Barry. JANET BENSON Barry, breakfast is ready! CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 1. INT. BARRY’S ROOM - CONTINUOUS BARRY Coming! SFX: Phone RINGING. Barry’s antennae vibrate as they RING like a phone. Barry’s hands are wet. He looks around for a towel. BARRY (CONT’D) Hang on a second! He wipes his hands on his sweater, and pulls his antennae down to his ear and mouth. BARRY (CONT'D) Hello? His best friend, ADAM FLAYMAN, is on the other end. ADAM Barry? BARRY Adam? ADAM Can you believe this is happening? BARRY Can’t believe it. I’ll pick you up. Barry sticks his stinger in a sharpener. SFX: BUZZING AS HIS STINGER IS SHARPENED. He tests the sharpness with his finger. SFX: Bing. BARRY (CONT’D) Looking sharp. ANGLE ON: Barry hovering down the hall, sliding down the staircase bannister. Barry’s mother, JANET BENSON, is in the kitchen. JANET BENSON Barry, why don’t you use the stairs? Your father paid good money for those. "Bee Movie" - JS REVISIONS 8/13/07 2. BARRY Sorry, I’m excited. Barry’s father, MARTIN BENSON, ENTERS. He’s reading a NEWSPAPER with the HEADLINE, “Queen gives birth to thousandtuplets: Resting Comfortably.” MARTIN BENSON Here’s the graduate. We’re very proud of you, Son. And a perfect report card, all B’s. JANET BENSON (mushing Barry’s hair) Very proud. BARRY Ma! I’ve got a thing going here. Barry re-adjusts his hair, starts to leave. JANET BENSON You’ve got some lint on your fuzz. She picks it off. BARRY Ow, that’s me! MARTIN BENSON Wave to us. We’ll be in row 118,000. Barry zips off. BARRY Bye! JANET BENSON Barry, I told you, stop flying in the house! CUT TO: SEQ. 750 - DRIVING TO GRADUATION EXT. BEE SUBURB - MORNING A GARAGE DOOR OPENS. Barry drives out in his CAR. "Bee Movie" - JS REVISIONS 8/13/07 3. ANGLE ON: Barry’s friend, ADAM FLAYMAN, standing by the curb. He’s reading a NEWSPAPER with the HEADLINE: “Frisbee Hits Hive: Internet Down. Bee-stander: “I heard a sound, and next thing I knew...wham-o!.” Barry drives up, stops in front of Adam. Adam jumps in. BARRY Hey, Adam. ADAM Hey, Barry. (pointing at Barry’s hair) Is that fuzz gel? BARRY A little. It’s a special day. Finally graduating. ADAM I never thought I’d make it. BARRY Yeah, three days of grade school, three days of high school. ADAM Those were so awkward. BARRY Three days of college. I’m glad I took off one day in the middle and just hitchhiked around the hive. ADAM You did come back different. They drive by a bee who’s jogging. ARTIE Hi Barry! BARRY (to a bee pedestrian) Hey Artie, growing a mustache? Looks good. Barry and Adam drive from the suburbs into the city. ADAM Hey, did you hear about Frankie? "Bee Movie" - JS REVISIONS 8/13/07 4. BARRY Yeah. ADAM You going to his funeral? BARRY No, I’m not going to his funeral. Everybody knows you sting someone you die, you don’t waste it on a squirrel. He was such a hot head. ADAM Yeah, I guess he could’ve just gotten out of the way. The DRIVE through a loop de loop. BARRY AND ADAM Whoa...Whooo...wheee!! ADAM I love this incorporating the amusement park right into our regular day. BARRY I guess that’s why they say we don’t need vacations. CUT TO: SEQ. 95 - GRADUATION EXT. GRADUATION CEREMONY - CONTINUOUS Barry and Adam come to a stop. They exit the car, and fly over the crowd to their seats. * BARRY * (re: graduation ceremony) * Boy, quite a bit of pomp...under * the circumstances. * They land in their seats. BARRY (CONT’D) Well Adam, today we are men. "Bee Movie" - JS REVISIONS 8/13/07 5. ADAM We are. BARRY Bee-men. ADAM Amen! BARRY Hallelujah. Barry hits Adam’s forehead. Adam goes into the rapture. An announcement comes over the PA. ANNOUNCER (V.O) Students, faculty, distinguished bees...please welcome, Dean Buzzwell. ANGLE ON: DEAN BUZZWELL steps up to the podium. The podium has a sign that reads: “Welcome Graduating Class of:”, with train-station style flipping numbers after it. BUZZWELL Welcome New Hive City graduating class of... The numbers on the podium change to 9:15. BUZZWELL (CONT’D) ...9:15. (he clears his throat) And that concludes our graduation ceremonies. And begins your career at Honex Industries. BARRY Are we going to pick our job today? ADAM I heard it’s just orientation. The rows of chairs change in transformer-like mechanical motion to Universal Studios type tour trams. Buzzwell walks off stage. BARRY (re: trams) Whoa, heads up! Here we go. "Bee Movie" - JS REVISIONS 8/13/07 6. SEQ. 125 - “FACTORY” FEMALE VOICE (V.O) Keep your hands and antennas inside the tram at all times. (in Spanish) Dejen las manos y antennas adentro del tram a todos tiempos. BARRY I wonder what it’s going to be like? ADAM A little scary. Barry shakes Adam. BARRY AND ADAM AAHHHH! The tram passes under SIGNS READING: “Honex: A Division of Honesco: A Part of the Hexagon Group.” TRUDY Welcome to Honex, a division of Honesco, and a part of the Hexagon group. BARRY This is it! The Honex doors OPEN, revealing the factory. BARRY (CONT’D) Wow. TRUDY We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life. Honey begins when our valiant pollen jocks bring the nectar to the hive where our top secret formula is automatically color-corrected, scent adjusted and bubble contoured into this... Trudy GRABS a TEST TUBE OF HONEY from a technician. "Bee Movie" - JS REVISIONS 8/13/07 7. TRUDY (CONT’D) ...soothing, sweet syrup with its distinctive golden glow, you all know as... EVERYONE ON THE TRAM (in unison) H-o-n-e-y. Trudy flips the flask into the crowd, and laughs as they all scramble for it. ANGLE ON: A GIRL BEE catching the honey. ADAM (sotto) That girl was hot. BARRY (sotto) She’s my cousin. ADAM She is? BARRY Yes, we’re all cousins. ADAM Right. You’re right. TRUDY At Honex, we also constantly strive to improve every aspect of bee existence. These bees are stress testing a new helmet technology. ANGLE ON: A STUNT BEE in a HELMET getting hit with a NEWSPAPER, then a SHOE, then a FLYSWATTER. He gets up, and gives a “thumb’s up”. The graduate bees APPLAUD. ADAM (re: stunt bee) What do you think he makes? BARRY Not enough. TRUDY And here we have our latest advancement, the Krelman. "Bee Movie" - JS REVISIONS 8/13/07 8. BARRY Wow, what does that do? TRUDY Catches that little strand of honey that hangs after you pour it. Saves us millions. ANGLE ON: The Krelman machine. Bees with hand-shaped hats on, rotating around a wheel to catch drips of honey. Adam’s hand shoots up. ADAM Can anyone work on the Krelman? TRUDY Of course. Most bee jobs are small ones. But bees know that every small job, if it’s done well, means a lot. There are over 3000 different bee occupations. But choose carefully, because you’ll stay in the job that you pick for the rest of your life. The bees CHEER. ANGLE ON: Barry’s smile dropping slightly. BARRY The same job for the rest of your life? I didn’t know that. ADAM What’s the difference? TRUDY And you’ll be happy to know that bees as a species haven’t had one day off in 27 million years. BARRY So you’ll just work us to death? TRUDY (laughing) We’ll sure try. Everyone LAUGHS except Barry. "Bee Movie" - JS REVISIONS 8/13/07 9. The tram drops down a log-flume type steep drop. Cameras flash, as all the bees throw up their hands. The frame freezes into a snapshot. Barry looks concerned. The tram continues through 2 doors. FORM DISSOLVE TO: SEQ. 175 - “WALKING THE HIVE” INT. HONEX LOBBY ANGLE ON: The log-flume photo, as Barry looks at it. ADAM Wow. That blew my mind. BARRY (annoyed) “What’s the difference?” Adam, how could you say that? One job forever? That’s an insane choice to have to make. ADAM Well, I’m relieved. Now we only have to make one decision in life. BARRY But Adam, how could they never have told us that? ADAM Barry, why would you question anything? We’re bees. We’re the most perfectly functioning society on Earth. They walk by a newspaper stand with A SANDWICH BOARD READING: “Bee Goes Berserk: Stings Seven Then Self.” ANGLE ON: A BEE filling his car’s gas tank from a honey pump. He fills his car some, then takes a swig for himself. NEWSPAPER BEE (to the bee guzzling gas) Hey! Barry and Adam begin to cross the street. "Bee Movie" - JS REVISIONS 8/13/07 10. BARRY Yeah but Adam, did you ever think that maybe things work a little too well around here? They stop in the middle of the street. The traffic moves perfectly around them. ADAM Like what? Give me one example. BARRY (thinks) ...I don’t know. But you know what I’m talking about. They walk off. SEQ. 400 - “MEET THE JOCKS” SFX: The SOUND of Pollen Jocks. PAN DOWN from the Honex statue. J-GATE ANNOUNCER Please clear the gate. Royal Nectar Force on approach. Royal Nectar Force on approach. BARRY Wait a second. Check it out. Hey, hey, those are Pollen jocks. ADAM Wow. FOUR PATROL BEES FLY in through the hive’s giant Gothic entrance. The Patrol Bees are wearing fighter pilot helmets with black visors. ADAM (CONT’D) I’ve never seen them this close. BARRY They know what it’s like to go outside the hive. ADAM Yeah, but some of them don’t come back. "Bee Movie" - JS REVISIONS 8/13/07 11. The nectar from the pollen jocks is removed from their backpacks, and loaded into trucks on their way to Honex. A SMALL CROWD forms around the Patrol Bees. Each one has a PIT CREW that takes their nectar. Lou Loduca hurries a pit crew along: LOU LODUCA You guys did great! You’re monsters. You’re sky freaks! I love it! I love it! SCHOOL GIRLS are jumping up and down and squealing nearby. BARRY I wonder where those guys have just been? ADAM I don’t know. BARRY Their day’s not planned. Outside the hive, flying who-knows-where, doing who-knows-what. ADAM You can’t just decide one day to be a Pollen Jock. You have to be bred for that. BARRY Right. Pollen Jocks cross in close proximity to Barry and Adam. Some pollen falls off, onto Barry and Adam. BARRY (CONT’D) Look at that. That’s more pollen than you and I will ever see in a lifetime. ADAM (playing with the pollen) It’s just a status symbol. I think bees make too big a deal out of it. BARRY Perhaps, unless you’re wearing it, and the ladies see you wearing it. ANGLE ON: Two girl bees. "Bee Movie" - JS REVISIONS 8/13/07 12. ADAM Those ladies? Aren’t they our cousins too? BARRY Distant, distant. ANGLE ON: TWO POLLEN JOCKS. JACKSON Look at these two. SPLITZ Couple of Hive Harrys. JACKSON Let’s have some fun with them. The pollen jocks approach. Barry and Adam continue to talk to the girls. GIRL 1 It must be so dangerous being a pollen jock. BARRY Oh yeah, one time a bear had me pinned up against a mushroom. He had one paw on my throat, and with the other he was slapping me back and forth across the face. GIRL 1 Oh my. BARRY I never thought I’d knock him out. GIRL 2 (to Adam) And what were you doing during all of this? ADAM Obviously I was trying to alert the authorities. The girl swipes some pollen off of Adam with a finger. BARRY (re: pollen) I can autograph that if you want. "Bee Movie" - JS REVISIONS 8/13/07 13. JACKSON Little gusty out there today, wasn’t it, comrades? BARRY Yeah. Gusty. BUZZ You know, we’re going to hit a sunflower patch about six miles from here tomorrow. BARRY Six miles, huh? ADAM (whispering) Barry. BUZZ It’s a puddle-jump for us. But maybe you’re not up for it. BARRY Maybe I am. ADAM (whispering louder) You are not! BUZZ We’re going, oh-nine hundred at JGate. ADAM (re: j-gate) Whoa. BUZZ (leaning in, on top of Barry) What do you think, Buzzy Boy? Are you bee enough? BARRY I might be. It all depends on what oh-nine hundred means. CUT TO: SEQ. 450 - “THE BALCONY” "Bee Movie" - JS REVISIONS 8/13/07 14. INT. BENSON HOUSE BALCONY - LATER Barry is standing on the balcony alone, looking out over the city. Martin Benson ENTERS, sneaks up behind Barry and gooses him in his ribs. MARTIN BENSON Honex! BARRY Oh, Dad. You surprised me. MARTIN BENSON (laughing) Have you decided what you’re interested in, Son? BARRY Well, there’s a lot of choices. MARTIN BENSON But you only get one. Martin LAUGHS. BARRY Dad, do you ever get bored doing the same job every day? MARTIN BENSON Son, let me tell you something about stirring. (making the stirring motion) You grab that stick and you just move it around, and you stir it around. You get yourself into a rhythm, it’s a beautiful thing. BARRY You know dad, the more I think about it, maybe the honey field just isn’t right for me. MARTIN BENSON And you were thinking of what, making balloon animals? That’s a bad job for a guy with a stinger. "Bee Movie" - JS REVISIONS 8/13/07 15. BARRY Well no... MARTIN BENSON Janet, your son’s not sure he wants to go into honey. JANET BENSON Oh Barry, you are so funny sometimes. BARRY I’m not trying to be funny. MARTIN BENSON You’re not funny, you’re going into honey. Our son, the stirrer. JANET BENSON You’re going to be a stirrer?! BARRY No one’s listening to me. MARTIN BENSON Wait until you see the sticks I have for you. BARRY I can say anything I want right now. I’m going to get an ant tattoo. JANET BENSON Let’s open some fresh honey and celebrate. BARRY Maybe I’ll pierce my thorax! MARTIN BENSON (toasting) To honey! BARRY Shave my antennae! JANET BENSON To honey! "Bee Movie" - JS REVISIONS 8/13/07 16. BARRY Shack up with a grasshopper, get a gold tooth, and start calling everybody “Dawg.” CUT TO: SEQ. 760 - “JOB PLACEMENT” EXT. HONEX LOBBY - CONTINUOUS ANGLE ON: A BEE BUS STOP. One group of bees stands on the pavement, as another group hovers above them. A doubledecker bus pulls up. The hovering bees get on the top level, and the standing bees get on the bottom. Barry and Adam pull up outside of Honex. ADAM I can’t believe we’re starting work today. BARRY Today’s the day. Adam jumps out of the car. ADAM (O.C) Come on. All the good jobs will be gone. BARRY Yeah, right... ANGLE ON: A BOARD READING: “JOB PLACEMENT BOARD”. Buzzwell, the Bee Processor, is at the counter. Another BEE APPLICANT, SANDY SHRIMPKIN is EXITING. SANDY SHRIMPKIN Is it still available? BUZZWELL Hang on. (he looks at changing numbers on the board) Two left. And...one of them’s yours. Congratulations Son, step to the side please. "Bee Movie" - JS REVISIONS 8/13/07 17. SANDY SHRIMPKIN Yeah! ADAM (to Sandy, leaving) What did you get? SANDY SHRIMPKIN Picking the crud out. That is stellar! ADAM Wow. BUZZWELL (to Adam and Barry) Couple of newbies? ADAM Yes Sir. Our first day. We are ready. BUZZWELL Well, step up and make your choice. ANGLE ON: A CHART listing the different sectors of Honex. Heating, Cooling, Viscosity, Krelman, Pollen Counting, Stunt Bee, Pouring, Stirrer, Humming, Regurgitating, Front Desk, Hair Removal, Inspector No. 7, Chef, Lint Coordinator, Stripe Supervisor, Antennae-ball polisher, Mite Wrangler, Swatting Counselor, Wax Monkey, Wing Brusher, Hive Keeper, Restroom Attendant. ADAM (to Barry) You want to go first? BARRY No, you go. ADAM Oh my. What’s available? BUZZWELL Restroom attendant is always open, and not for the reason you think. ADAM Any chance of getting on to the Krelman, Sir? BUZZWELL Sure, you’re on. "Bee Movie" - JS REVISIONS 8/13/07 18. He plops the KRELMAN HAT onto Adam’s head. ANGLE ON: The job board. THE COLUMNS READ: “OCCUPATION” “POSITIONS AVAILABLE”, and “STATUS”. The middle column has numbers, and the right column has job openings flipping between “open”, “pending”, and “closed”. BUZZWELL (CONT’D) Oh, I’m sorry. The Krelman just closed out. ADAM Oh! He takes the hat off Adam. BUZZWELL Wax Monkey’s always open. The Krelman goes from “Closed” to “Open”. BUZZWELL (CONT’D) And the Krelman just opened up again. ADAM What happened? BUZZWELL Well, whenever a bee dies, that’s an opening. (pointing at the board) See that? He’s dead, dead, another dead one, deady, deadified, two more dead. Dead from the neck up, dead from the neck down. But, that’s life. ANGLE ON: Barry’s disturbed expression. ADAM (feeling pressure to decide) Oh, this is so hard. Heating, cooling, stunt bee, pourer, stirrer, humming, inspector no. 7, lint coordinator, stripe supervisor, antenna-ball polisher, mite wrangler-- Barry, Barry, what do you think I should-- Barry? Barry? "Bee Movie" - JS REVISIONS 8/13/07 19. Barry is gone. CUT TO: SEQ. 775 - “LOU LODUCA SPEECH” EXT. J-GATE - SAME TIME Splitz, Jackson, Buzz, Lou and two other BEES are going through final pre-flight checks. Barry ENTERS. LOU LODUCA Alright, we’ve got the sunflower patch in quadrant nine. Geranium window box on Sutton Place... Barry’s antennae rings, like a phone. ADAM (V.O) What happened to you? Where are you? Barry whispers throughout. BARRY I’m going out. ADAM (V.O) Out? Out where? BARRY Out there. ADAM (V.O) (putting it together) Oh no. BARRY I have to, before I go to work for the rest of my life. ADAM (V.O) You’re going to die! You’re crazy! Hello? BARRY Oh, another call coming in. "Bee Movie" - JS REVISIONS 8/13/07 20. ADAM (V.O) You’re cra-- Barry HANGS UP. ANGLE ON: Lou Loduca. LOU LODUCA If anyone’s feeling brave, there’s a Korean Deli on 83rd that gets their roses today. BARRY (timidly) Hey guys. BUZZ Well, look at that. SPLITZ Isn’t that the kid we saw yesterday? LOU LODUCA (to Barry) Hold it son, flight deck’s restricted. JACKSON It’s okay Lou, we’re going to take him up. Splitz and Jackson CHUCKLE. LOU LODUCA Really? Feeling lucky, are ya? A YOUNGER SMALLER BEE THAN BARRY, CHET, runs up with a release waiver for Barry to sign. CHET Sign here. Here. Just initial that. Thank you. LOU LODUCA Okay, you got a rain advisory today and as you all know, bees cannot fly in rain. So be careful. As always, (reading off clipboard) watch your brooms, hockey sticks, dogs, birds, bears, and bats. "Bee Movie" - JS REVISIONS 8/13/07 21. Also, I got a couple reports of root beer being poured on us. Murphy’s in a home because of it, just babbling like a cicada. BARRY That’s awful. LOU LODUCA And a reminder for all you rookies, bee law number one, absolutely no talking to humans. Alright, launch positions! The Jocks get into formation, chanting as they move. LOU LODUCA (CONT’D) Black and Yellow! JOCKS Hello! SPLITZ (to Barry) Are you ready for this, hot shot? BARRY Yeah. Yeah, bring it on. Barry NODS, terrified. BUZZ Wind! - CHECK! JOCK #1 Antennae! - CHECK! JOCK #2 Nectar pack! - CHECK! JACKSON Wings! - CHECK! SPLITZ Stinger! - CHECK! BARRY Scared out of my shorts - CHECK. LOU LODUCA Okay ladies, let’s move it out. Everyone FLIPS their goggles down. Pit crew bees CRANK their wings, and remove the starting blocks. We hear loud HUMMING. "Bee Movie" - JS REVISIONS 8/13/07 22. LOU LODUCA (CONT'D) LOU LODUCA (CONT’D) Pound those petunia's, you striped stem-suckers! All of you, drain those flowers! A FLIGHT DECK GUY in deep crouch hand-signals them out the archway as the backwash from the bee wings FLUTTERS his jump suit. Barry follows everyone. SEQ. 800 - “FLYING WITH THE JOCKS” The bees climb above tree tops in formation. Barry is euphoric. BARRY Whoa! I’m out! I can’t believe I’m out! So blue. Ha ha ha! (a beat) I feel so fast...and free. (re: kites in the sky) Box kite! Wow! They fly by several bicyclists, and approach a patch of flowers. BARRY (CONT'D) Flowers! SPLITZ This is blue leader. We have roses visual. Bring it around thirty degrees and hold. BARRY (sotto) Roses. JACKSON Thirty degrees, roger, bringing it around. Many pollen jocks break off from the main group. They use their equipment to collect nectar from flowers. Barry flies down to watch the jocks collect the nectar. JOCK Stand to the side kid, it’s got a bit of a kick. The jock fires the gun, and recoils. Barry watches the gun fill up with nectar. "Bee Movie" - JS REVISIONS 8/13/07 23. BARRY Oh, that is one Nectar Collector. JOCK You ever see pollination up close? BARRY No, Sir. He takes off, and the excess pollen dust falls causing the flowers to come back to life. JOCK (as he pollinates) I pick some pollen up over here, sprinkle it over here, maybe a dash over there, pinch on that one...see that? It’s a little bit of magic, ain’t it? The FLOWERS PERK UP as he pollinates. BARRY Wow. That’s amazing. Why do we do that? JOCK ...that’s pollen power, Kid. More pollen, more flowers, more nectar, more honey for us. BARRY Cool. The Jock WINKS at Barry. Barry rejoins the other jocks in the sky. They swoop in over a pond, kissing the surface. We see their image reflected in the water; they’re really moving. They fly over a fountain. BUZZ I’m picking up a lot of bright yellow, could be daisies. Don’t we need those? SPLITZ Copy that visual. We see what appear to be yellow flowers on a green field. "Bee Movie" - JS REVISIONS 8/13/07 24. They go into a deep bank and dive. BUZZ Hold on, one of these flowers seems to be on the move. SPLITZ Say again...Are you reporting a moving flower? BUZZ Affirmative. SEQ. 900 - “TENNIS GAME” The pollen jocks land. It is a tennis court with dozens of tennis balls. A COUPLE, VANESSA and KEN, plays tennis. The bees land right in the midst of a group of balls. KEN (O.C) That was on the line! The other bees start walking around amongst the immense, yellow globes. SPLITZ This is the coolest. What is it? They stop at a BALL on a white line and look up at it. JACKSON I don’t know, but I’m loving this color. SPLITZ (smelling tennis ball) Smells good. Not like a flower. But I like it. JACKSON Yeah, fuzzy. BUZZ Chemical-y. JACKSON Careful, guys, it’s a little grabby. Barry LANDS on a ball and COLLAPSES. "Bee Movie" - JS REVISIONS 8/13/07 25. BARRY Oh my sweet lord of bees. JACKSON Hey, candy brain, get off there! Barry attempts to pulls his legs off, but they stick. BARRY Problem! A tennis shoe and a hand ENTER FRAME. The hand picks up the ball with Barry underneath it. BARRY (CONT'D) Guys! BUZZ This could be bad. JACKSON Affirmative. Vanessa walks back to the service line, BOUNCES the ball. Each time it BOUNCES, the other bees cringe and GASP. ANGLE ON: Barry, terrified. Pure dumb luck, he’s not getting squished. BARRY (with each bounce) Very close...Gonna Hurt...Mamma’s little boy. SPLITZ You are way out of position, rookie. ANGLE ON: Vanessa serving. We see Barry and the ball up against the racket as she brings it back. She tosses the ball into the air; Barry’s eyes widen. The ball is STRUCK, and the rally is on. KEN Coming in at you like a missile! Ken HITS the ball back. Barry feels the g-forces. ANGLE ON: The Pollen Jocks watching Barry pass by them in SLOW MOTION. "Bee Movie" - JS REVISIONS 8/13/07 26. BARRY (in slow motion) Help me! JACKSON You know, I don't think these are flowers. SPLITZ Should we tell him? JACKSON I think he knows. BARRY (O.S) What is this?! Vanessa HITS a high arcing lob. Ken waits, poised for the return. We see Barry having trouble maneuvering the ball from fatigue. KEN (overly confident) Match point! ANGLE ON: Ken running up. He has a killer look in his eyes. He’s going to hit the ultimate overhead smash. KEN (CONT'D) You can just start packing up Honey, because I believe you’re about to eat it! ANGLE ON: Pollen Jocks. JACKSON Ahem! Ken is distracted by the jock. KEN What? No! He misses badly. The ball rockets into oblivion. Barry is still hanging on. ANGLE ON: Ken, berating himself. KEN (CONT’D) Oh, you cannot be serious. We hear the ball WHISTLING, and Barry SCREAMING. "Bee Movie" - JS REVISIONS 8/13/07 27. BARRY Yowser!!! SEQ. 1000 - “SUV” The ball flies through the air, and lands in the middle of the street. It bounces into the street again, and sticks in the grille of an SUV. INT. CAR ENGINE - CONTINUOUS BARRY’S POV: the grille of the SUV sucks him up. He tumbles through a black tunnel, whirling vanes, and pistons. BARRY AHHHHHHHHHHH!! OHHHH!! EECHHH!! AHHHHHH!! Barry gets chilled by the A/C system, and sees a frozen grasshopper. BARRY (CONT’D) (re: grasshopper) Eww, gross. CUT TO: INT. CAR - CONTINUOUS The car is packed with a typical suburban family: MOTHER, FATHER, eight-year old BOY, LITTLE GIRL in a car seat and a GRANDMOTHER. A big slobbery DOG is behind a grate. Barry pops into the passenger compartment, hitting the Mother’s magazine. MOTHER There’s a bee in the car! They all notice the bee and start SCREAMING. BARRY Aaahhhh! Barry tumbles around the car. We see the faces from his POV. MOTHER Do something! "Bee Movie" - JS REVISIONS 8/13/07 28. FATHER I’m driving! Barry flies by the little girl in her CAR SEAT. She waves hello. LITTLE GIRL Hi, bee. SON He’s back here! He’s going to sting me! The car SWERVES around the road. Barry flies into the back, where the slobbery dog SNAPS at him. Barry deftly avoids the jaws and gross, flying SPITTLE. MOTHER Nobody move. If you don’t move, he won’t sting you. Freeze! Everyone in the car freezes. Barry freezes. They stare at each other, eyes going back and forth, waiting to see who will make the first move. Barry blinks. GRANNY He blinked! Granny pulls out a can of HAIR SPRAY. SON Spray him, Granny! Granny sprays the hair spray everywhere. FATHER What are you doing? GRANNY It’s hair spray! Extra hold! MOTHER Kill it! Barry gets sprayed back by the hair spray, then sucked out of the sunroof. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 29. EXT. CITY STREET - CONTINUOUS BARRY Wow. The tension level out here is unbelievable. I’ve got to get home. As Barry flies down the street, it starts to RAIN. He nimbly avoids the rain at first. BARRY (CONT’D) Whoa. Whoa! Can’t fly in rain! Can’t fly in rain! Can’t fly in-- A couple of drops hit him, his wings go limp and he starts falling. BARRY (CONT'D) Mayday! Mayday! Bee going down! Barry sees a window ledge and aims for it and just makes it. Shivering and exhausted, he crawls into an open window as it CLOSES. SEQ. 1100 - “VANESSA SAVES BARRY” INT. VANESSA’S APARTMENT - CONTINUOUS Inside the window, Barry SHAKES off the rain like a dog. Vanessa, Ken, Andy, and Anna ENTER the apartment. VANESSA Ken, can you close the window please? KEN Huh? Oh. (to Andy) Hey, check out my new resume. I made it into a fold-out brochure. You see? It folds out. Ken holds up his brochure, with photos of himself, and a resume in the middle. ANGLE ON: Barry hiding behind the curtains, as Ken CLOSES THE WINDOW. "Bee Movie" - JS REVISIONS 8/13/07 30. BARRY Oh no, more humans. I don’t need this. Barry HOVERS up into the air and THROWS himself into the glass. BARRY (CONT’D) (dazed) Ow! What was that? He does it again, and then multiple more times. BARRY (CONT'D) Maybe this time...this time, this time, this time, this time, this time, this time, this time. Barry JUMPS onto the drapes. BARRY (CONT'D) (out of breath) Drapes! (then, re: glass) That is diabolical. KEN It’s fantastic. It’s got all my special skills, even my top ten favorite movies. ANDY What’s your number one? Star Wars? KEN Ah, I don’t go for that, (makes Star Wars noises), kind of stuff. ANGLE ON: Barry. BARRY No wonder we’re not supposed to talk to them. They’re out of their minds. KEN When I walk out of a job interview they’re flabbergasted. They can’t believe the things I say. Barry looks around and sees the LIGHT BULB FIXTURE in the middle of the ceiling. "Bee Movie" - JS REVISIONS 8/13/07 31. BARRY (re: light bulb) Oh, there’s the sun. Maybe that’s a way out. Barry takes off and heads straight for the light bulb. His POV: The seventy-five watt label grows as he gets closer. BARRY (CONT’D) I don’t remember the sun having a big seventy five on it. Barry HITS the bulb and is KNOCKED SILLY. He falls into a BOWL OF GUACAMOLE. Andy dips his chip in the guacamole, taking Barry with it. ANGLE ON: Ken and Andy. KEN I’ll tell you what. You know what? I predicted global warming. I could feel it getting hotter. At first I thought it was just me. Barry’s POV: Giant human mouth opening. KEN (CONT’D) Wait! Stop! Beeeeeee! ANNA Kill it! Kill it! They all JUMP up from their chairs. Andy looks around for something to use. Ken comes in for the kill with a big TIMBERLAND BOOT on each hand. KEN Stand back. These are winter boots. Vanessa ENTERS, and stops Ken from squashing Barry. VANESSA (grabs Ken’s arm) Wait. Don’t kill him. CLOSE UP: on Barry’s puzzled face. KEN You know I’m allergic to them. This thing could kill me. "Bee Movie" - JS REVISIONS 8/13/07 32. VANESSA Why does his life have any less value than yours? She takes a GLASS TUMBLER and places it over Barry. KEN Why does his life have any less value than mine? Is that your statement? VANESSA I’m just saying, all life has value. You don’t know what he’s capable of feeling. Barry looks up through the glass and watches this conversation, astounded. Vanessa RIPS Ken’s resume in half and SLIDES it under the glass. KEN (wistful) My brochure. There’s a moment of eye contact as she carries Barry to the window. She opens it and sets him free. VANESSA There you go, little guy. KEN (O.C) I’m not scared of them. But, you know, it’s an allergic thing. ANDY (O.C) * Hey, why don’t you put that on your * resume-brochure? * KEN (O.C) It’s not funny, my whole face could puff up. ANDY (O.C) Make it one of your “Special Skills.” KEN (O.C) You know, knocking someone out is also a special skill. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 33. EXT. WINDOWSILL - CONTINUOUS Barry stares over the window frame. He can’t believe what’s just happened. It is still RAINING. DISSOLVE TO: SEQ. 1200 - “BARRY SPEAKS” EXT. WINDOWSILL - LATER Barry is still staring through the window. Inside, everyone’s saying their good-byes. KEN Vanessa, next week? Yogurt night? VANESSA Uh, yeah sure Ken. You know, whatever. KEN You can put carob chips on there. VANESSA Good night. KEN (as he exits) Supposed to be less calories, or something. VANESSA Bye. She shuts the door. Vanessa starts cleaning up. BARRY I’ve got to say something. She saved my life. I’ve got to say something. Alright, here it goes. Barry flies in. "Bee Movie" - JS REVISIONS 8/13/07 34. INT. VANESSA’S APARTMENT - CONTINUOUS Barry hides himself on different PRODUCTS placed along the kitchen shelves. He hides on a Bumblebee Tuna can, and a “Greetings From Coney Island” MUSCLE-MAN POSTCARD on the fridge. BARRY (on fridge) What would I say? (landing on a bottle) I could really get in trouble. He stands looking at Vanessa. BARRY (CONT'D) It’s a bee law. You’re not supposed to talk to a human. I can’t believe I’m doing this. I’ve got to. Oh, I can’t do it! Come on! No, yes, no, do it! I can’t. How should I start it? You like jazz? No, that’s no good. Here she comes. Speak, you fool. As Vanessa walks by, Barry takes a DEEP BREATH. BARRY (CONT’D) (cheerful) Umm...hi. Vanessa DROPS A STACK OF DISHES, and HOPS BACK. BARRY (CONT’D) I’m sorry. VANESSA You’re talking. BARRY Yes, I know, I know. VANESSA You’re talking. BARRY I know, I’m sorry. I’m so sorry. VANESSA It’s okay. It’s fine. It’s just, I know I’m dreaming, but I don’t recall going to bed. "Bee Movie" - JS REVISIONS 8/13/07 35. BARRY Well, you know I’m sure this is very disconcerting. VANESSA Well yeah. I mean this is a bit of a surprise to me. I mean...you’re a bee. BARRY Yeah, I am a bee, and you know I’m not supposed to be doing this, but they were all trying to kill me and if it wasn’t for you...I mean, I had to thank you. It’s just the way I was raised. Vanessa intentionally JABS her hand with a FORK. VANESSA Ow! BARRY That was a little weird. VANESSA (to herself) I’m talking to a bee. BARRY Yeah. VANESSA I’m talking to a bee. BARRY Anyway... VANESSA And a bee is talking to me... BARRY I just want you to know that I’m grateful, and I’m going to leave now. VANESSA Wait, wait, wait, wait, how did you learn to do that? BARRY What? "Bee Movie" - JS REVISIONS 8/13/07 36. VANESSA The talking thing. BARRY Same way you did, I guess. Mama, Dada, honey, you pick it up. VANESSA That’s very funny. BARRY Yeah. Bees are funny. If we didn’t laugh, we’d cry. With what we have to deal with. Vanessa LAUGHS. BARRY (CONT’D) Anyway. VANESSA Can I, uh, get you something? BARRY Like what? VANESSA I don’t know. I mean, I don’t know. Coffee? BARRY Well, uh, I don’t want to put you out. VANESSA It’s no trouble. BARRY Unless you’re making anyway. VANESSA Oh, it takes two minutes. BARRY Really? VANESSA It’s just coffee. BARRY I hate to impose. "Bee Movie" - JS REVISIONS 8/13/07 37. VANESSA Don’t be ridiculous. BARRY Actually, I would love a cup. VANESSA Hey, you want a little rum cake? BARRY I really shouldn’t. VANESSA Have a little rum cake. BARRY No, no, no, I can’t. VANESSA Oh, come on. BARRY You know, I’m trying to lose a couple micrograms here. VANESSA Where? BARRY Well... These stripes don’t help. VANESSA You look great. BARRY I don’t know if you know anything about fashion. Vanessa starts POURING the coffee through an imaginary cup and directly onto the floor. BARRY (CONT'D) Are you alright? VANESSA No. DISSOLVE TO: SEQ. 1300 - “ROOFTOP COFFEE” "Bee Movie" - JS REVISIONS 8/13/07 38. EXT. VANESSA’S ROOF - LATER Barry and Vanessa are drinking coffee on her roof terrace. He is perched on her keychain. BARRY ...He can’t get a taxi. He’s making the tie in the cab, as they’re flying up Madison. So he finally gets there. VANESSA Uh huh? BARRY He runs up the steps into the church, the wedding is on... VANESSA Yeah? BARRY ...and he says, watermelon? I thought you said Guatemalan. VANESSA Uh huh? BARRY Why would I marry a watermelon? Barry laughs. Vanessa doesn’t. VANESSA Oh! Is that, uh, a bee joke? BARRY Yeah, that’s the kind of stuff that we do. VANESSA Yeah, different. A BEAT. VANESSA (CONT’D) So anyway...what are you going to do, Barry? "Bee Movie" - JS REVISIONS 8/13/07 39. BARRY About work? I don’t know. I want to do my part for the hive, but I can’t do it the way they want. VANESSA I know how you feel. BARRY You do? VANESSA Sure, my parents wanted me to be a lawyer or doctor, but I wanted to be a florist. BARRY Really? VANESSA My only interest is flowers. BARRY Our new queen was just elected with that same campaign slogan. VANESSA Oh. BARRY Anyway, see there’s my hive, right there. You can see it. VANESSA Oh, you’re in Sheep Meadow. BARRY (excited) Yes! You know the turtle pond? VANESSA Yes? BARRY I’m right off of that. VANESSA Oh, no way. I know that area. Do you know I lost a toe-ring there once? BARRY Really? "Bee Movie" - JS REVISIONS 8/13/07 40. VANESSA Yes. BARRY Why do girls put rings on their toes? VANESSA Why not? BARRY I don’t know. It’s like putting a hat on your knee. VANESSA Really? Okay. A JANITOR in the background changes a LIGHTBULB. To him, it appears that Vanessa is talking to an imaginary friend. JANITOR You all right, ma’am? VANESSA Oh, yeah, fine. Just having two cups of coffee. BARRY Anyway, this has been great. (wiping his mouth) Thanks for the coffee. Barry gazes at Vanessa. VANESSA Oh yeah, it’s no trouble. BARRY Sorry I couldn’t finish it. Vanessa giggles. BARRY (CONT'D) (re: coffee) If I did, I’d be up the rest of my life. Ummm. Can I take a piece of this with me? VANESSA Sure. Here, have a crumb. She takes a CRUMB from the plate and hands it to Barry. "Bee Movie" - JS REVISIONS 8/13/07 41. BARRY (a little dreamy) Oh, thanks. VANESSA Yeah. There is an awkward pause. BARRY Alright, well then, I guess I’ll see you around, or not, or... VANESSA Okay Barry. BARRY And thank you so much again, for before. VANESSA Oh that? BARRY Yeah. VANESSA Oh, that was nothing. BARRY Well, not nothing, but, anyway... Vanessa extends her hand, and shakes Barry’s gingerly. The Janitor watches. The lightbulb shorts out. The Janitor FALLS. CUT TO: SEQ. 1400 - “HONEX” INT. HONEX BUILDING - NEXT DAY ANGLE ON: A TEST BEE WEARING A PARACHUTE is in a wind tunnel, hovering through increasingly heavy wind. SIGNS UNDER A FLASHING LIGHT READ: “Test In Progress” & “Hurricane Survival Test”. 2 BEES IN A LAB COATS are observing behind glass. "Bee Movie" - JS REVISIONS 8/13/07 42. LAB COAT BEE 1 This can’t possibly work. LAB COAT BEE 2 Well, he’s all set to go, we may as well try it. (into the mic) Okay Dave, pull the chute. The test bee opens his parachute. He’s instantly blown against the rear wall. Adam and Barry ENTER. ADAM Sounds amazing. BARRY Oh, it was amazing. It was the scariest, happiest moment of my life. ADAM Humans! Humans! I can’t believe you were with humans! Giant scary humans! What were they like? BARRY Huge and crazy. They talk crazy, they eat crazy giant things. They drive around real crazy. ADAM And do they try and kill you like on TV? BARRY Some of them. But some of them don’t. ADAM How’d you get back? BARRY Poodle. ADAM Look, you did it. And I’m glad. You saw whatever you wanted to see out there, you had your “experience”, and now you’re back, you can pick out your job, and everything can be normal. "Bee Movie" - JS REVISIONS 8/13/07 43. ANGLE ON: LAB BEES examining a CANDY CORN through a microscope. BARRY Well... ADAM Well? BARRY Well, I met someone. ADAM You met someone? Was she Bee-ish? BARRY Mmm. ADAM Not a WASP? Your parents will kill you. BARRY No, no, no, not a wasp. ADAM Spider? BARRY You know, I’m not attracted to the spiders. I know to everyone else it’s like the hottest thing with the eight legs and all. I can’t get by that face. Barry makes a spider face. ADAM So, who is she? BARRY She’s a human. ADAM Oh no, no, no, no. That didn’t happen. You didn’t do that. That is a bee law. You wouldn’t break a bee law. BARRY Her name’s Vanessa. "Bee Movie" - JS REVISIONS 8/13/07 44. ADAM Oh, oh boy! BARRY She’s so-o nice. And she’s a florist! ADAM Oh, no. No, no, no! You’re dating a human florist? BARRY We’re not dating. ADAM You’re flying outside the hive. You’re talking to human beings that attack our homes with power washers and M-80’s. That’s 1/8 of a stick of dynamite. BARRY She saved my life. And she understands me. ADAM This is over. Barry pulls out the crumb. BARRY Eat this. Barry stuffs the crumb into Adam’s face. ADAM This is not over. What was that? BARRY They call it a crumb. ADAM That was SO STINGING STRIPEY! BARRY And that’s not even what they eat. That just falls off what they eat. Do you know what a Cinnabon is? ADAM No. "Bee Movie" - JS REVISIONS 8/13/07 45. BARRY It’s bread... ADAM Come in here! BARRY and cinnamon, ADAM Be quiet! BARRY and frosting...they heat it up-- ADAM Sit down! INT. ADAM’S OFFICE - CONTINUOUS BARRY Really hot! ADAM Listen to me! We are not them. We’re us. There’s us and there’s them. BARRY Yes, but who can deny the heart that is yearning... Barry rolls his chair down the corridor. ADAM There’s no yearning. Stop yearning. Listen to me. You have got to start thinking bee, my friend. ANOTHER BEE JOINS IN. ANOTHER BEE Thinking bee. WIDER SHOT AS A 3RD BEE ENTERS, popping up over the cubicle wall. 3RD BEE Thinking bee. EVEN WIDER SHOT AS ALL THE BEES JOIN IN. "Bee Movie" - JS REVISIONS 8/13/07 46. OTHER BEES Thinking bee. Thinking bee. Thinking bee. CUT TO: SEQ. 1500 - “POOLSIDE NAGGING” EXT. BACKYARD PARENT’S HOUSE - DAY Barry sits on a RAFT in a hexagon honey pool, legs dangling into the water. Janet Benson and Martin Benson stand over him wearing big, sixties sunglasses and cabana-type outfits. The sun shines brightly behind their heads. JANET BENSON (O.C) There he is. He’s in the pool. MARTIN BENSON You know what your problem is, Barry? BARRY I’ve got to start thinking bee? MARTIN BENSON Barry, how much longer is this going to go on? It’s been three days. I don’t understand why you’re not working. BARRY Well, I’ve got a lot of big life decisions I’m thinking about. MARTIN BENSON What life? You have no life! You have no job! You’re barely a bee! Barry throws his hands in the air. BARRY Augh. JANET BENSON Would it kill you to just make a little honey? Barry ROLLS off the raft and SINKS to the bottom of the pool. We hear his parents’ MUFFLED VOICES from above the surface. "Bee Movie" - JS REVISIONS 8/13/07 47. JANET BENSON (CONT'D) (muffled) Barry, come out from under there. Your father’s talking to you. Martin, would you talk to him? MARTIN BENSON Barry, I’m talking to you. DISSOLVE TO: EXT. PICNIC AREA - DAY MUSIC: “Sugar Sugar” by the Archies. Barry and Vanessa are having a picnic. A MOSQUITO lands on Vanessa’s leg. She SWATS it violently. Barry’s head whips around, aghast. They stare at each other awkwardly in a frozen moment, then BURST INTO HYSTERICAL LAUGHTER. Vanessa GETS UP. VANESSA You coming? BARRY Got everything? VANESSA All set. Vanessa gets into a one-man Ultra Light plane with a black and yellow paint scheme. She puts on her helmet. BARRY You go ahead, I’ll catch up. VANESSA (come hither wink) Don’t be too long. The Ultra Light takes off. Barry catches up. They fly sideby-side. VANESSA (CONT’D) Watch this! Vanessa does a loop, and FLIES right into the side of a mountain, BURSTING into a huge ball of flames. "Bee Movie" - JS REVISIONS 8/13/07 48. BARRY (yelling, anguished) Vanessa! EXT. BARRY’S PARENT’S HOUSE - CONTINUOUS ANGLE ON: Barry’s face bursting through the surface of the pool, GASPING for air, eyes opening in horror. MARTIN BENSON We’re still here, Barry. JANET BENSON I told you not to yell at him. He doesn’t respond when you yell at him. MARTIN BENSON Then why are you yelling at me? JANET BENSON Because you don’t listen. MARTIN BENSON I’m not listening to this. Barry is toweling off, putting on his sweater. BARRY Sorry Mom, I’ve got to go. JANET BENSON Where are you going? BARRY Nowhere. I’m meeting a friend. Barry JUMPS off the balcony and EXITS. JANET BENSON (calling after him) A girl? Is this why you can’t decide? BARRY Bye! JANET BENSON I just hope she’s Bee-ish. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 49. SEQ. 1700 - “STREETWALK/SUPERMARKET” EXT. VANESSA’S FLORIST SHOP - DAY Vanessa FLIPS the sign to say “Sorry We Missed You”, and locks the door. ANGLE ON: A POSTER on Vanessa’s door for the Tournament of Roses Parade in Pasadena. BARRY So they have a huge parade of just flowers every year in Pasadena? VANESSA Oh, to be in the Tournament of Roses, that’s every florist’s dream. Up on a float, surrounded by flowers, crowds cheering. BARRY Wow, a tournament. Do the roses actually compete in athletic events? VANESSA No. Alright, I’ve got one. How come you don’t fly everywhere? BARRY It’s exhausting. Why don’t you run everywhere? VANESSA Hmmm. BARRY Isn’t that faster? VANESSA Yeah, okay. I see, I see. Alright, your turn. Barry and Vanessa walk/fly down a New York side street, no other pedestrians near them. BARRY Ah! Tivo. You can just freeze live TV? That’s insane. "Bee Movie" - JS REVISIONS 8/13/07 50. VANESSA What, you don’t have anything like that? BARRY We have Hivo, but it’s a disease. It’s a horrible, horrible disease. VANESSA Oh my. They turn the corner onto a busier avenue and people start to swat at Barry. MAN Dumb bees! VANESSA You must just want to sting all those jerks. BARRY We really try not to sting. It’s usually fatal for us. VANESSA So you really have to watch your temper? They ENTER a SUPERMARKET. CUT TO: INT. SUPERMARKET BARRY Oh yeah, very carefully. You kick a wall, take a walk, write an angry letter and throw it out. You work through it like any emotion-- anger, jealousy, (under his breath) lust. Barry hops on top of some cardboard boxes in the middle of an aisle. A stock boy, HECTOR, whacks him with a rolled up magazine. VANESSA (to Barry) Oh my goodness. Are you okay? "Bee Movie" - JS REVISIONS 8/13/07 51. BARRY Yeah. Whew! Vanessa WHACKS Hector over the head with the magazine. VANESSA (to Hector) What is wrong with you?! HECTOR It’s a bug. VANESSA Well he’s not bothering anybody. Get out of here, you creep. Vanessa pushes him, and Hector EXITS, muttering. BARRY (shaking it off) What was that, a Pick and Save circular? VANESSA Yeah, it was. How did you know? BARRY It felt like about ten pages. Seventy-five’s pretty much our limit. VANESSA Boy, you’ve really got that down to a science. BARRY Oh, we have to. I lost a cousin to Italian Vogue. VANESSA I’ll bet. Barry stops, sees the wall of honey jars. BARRY What, in the name of Mighty Hercules, is this? How did this get here? Cute Bee? Golden Blossom? Ray Liotta Private Select? VANESSA Is he that actor? "Bee Movie" - JS REVISIONS 8/13/07 52. BARRY I never heard of him. Why is this here? VANESSA For people. We eat it. BARRY Why? (gesturing around the market) You don’t have enough food of your own? VANESSA Well yes, we-- BARRY How do you even get it? VANESSA Well, bees make it... BARRY I know who makes it! And it’s hard to make it! There’s Heating and Cooling, and Stirring...you need a whole Krelman thing. VANESSA It’s organic. BARRY It’s our-ganic! VANESSA It’s just honey, Barry. BARRY Just...what?! Bees don’t know about this. This is stealing. A lot of stealing! You’ve taken our homes, our schools, our hospitals. This is all we have. And it’s on sale? I’m going to get to the bottom of this. I’m going to get to the bottom of all of this! He RIPS the label off the Ray Liotta Private Select. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 53. SEQ. 1800 - “WINDSHIELD” EXT. BACK OF SUPERMARKET LOADING DOCK - LATER THAT DAY Barry disguises himself by blacking out his yellow lines with a MAGIC MARKER and putting on some war paint. He sees Hector, the stock boy, with a knife CUTTING open cardboard boxes filled with honey jars. MAN You almost done? HECTOR Almost. Barry steps in some honey, making a SNAPPING noise. Hector stops and turns. HECTOR (CONT’D) He is here. I sense it. Hector grabs his BOX CUTTER. Barry REACTS, hides himself behind the box again. HECTOR (CONT’D) (talking too loud, to no one in particular) Well, I guess I’ll go home now, and just leave this nice honey out, with no one around. A BEAT. Hector pretends to exit. He takes a couple of steps in place. ANGLE ON: The honey jar. Barry steps out into a moody spotlight. BARRY You’re busted, box boy! HECTOR Ah ha! I knew I heard something. So, you can talk. Barry flies up, stinger out, pushing Hector up against the wall. As Hector backs up, he drops his knife. BARRY Oh, I can talk. And now you’re going to start talking. "Bee Movie" - JS REVISIONS 8/13/07 54. Where are you getting all the sweet stuff? Who’s your supplier?! HECTOR I don’t know what you’re talking about. I thought we were all friends. The last thing we want to do is upset any of you...bees! Hector grabs a PUSHPIN. Barry fences with his stinger. HECTOR (CONT’D) You’re too late. It’s ours now! BARRY You, sir, have crossed the wrong sword. HECTOR You, sir, are about to be lunch for my iguana, Ignacio! Barry and Hector get into a cross-swords, nose-to-nose confrontation. BARRY Where is the honey coming from? Barry knocks the pushpin out of his hand. Barry puts his stinger up to Hector’s nose. BARRY (CONT'D) Tell me where?! HECTOR (pointing to a truck) Honey Farms. It comes from Honey Farms. ANGLE ON: A Honey Farms truck leaving the parking lot. Barry turns, takes off after the truck through an alley. He follows the truck out onto a busy street, dodging a bus, and several cabs. CABBIE Crazy person! He flies through a metal pipe on the top of a truck. BARRY OOOHHH! "Bee Movie" - JS REVISIONS 8/13/07 55. BARRY (CONT'D) Barry grabs onto a bicycle messenger’s backpack. The honey farms truck starts to pull away. Barry uses the bungee cord to slingshot himself towards the truck. He lands on the windshield, where the wind plasters him to the glass. He looks up to find himself surrounded by what appear to be DEAD BUGS. He climbs across, working his way around the bodies. BARRY (CONT’D) Oh my. What horrible thing has happened here? Look at these faces. They never knew what hit them. And now they’re on the road to nowhere. A MOSQUITO opens his eyes. MOOSEBLOOD Pssst! Just keep still. BARRY What? You’re not dead? MOOSEBLOOD Do I look dead? Hey man, they will wipe anything that moves. Now, where are you headed? BARRY To Honey Farms. I am onto something huge here. MOOSEBLOOD I’m going to Alaska. Moose blood. Crazy stuff. Blows your head off. LADYBUG I’m going to Tacoma. BARRY (to fly) What about you? MOOSEBLOOD He really is dead. BARRY Alright. The WIPER comes towards them. "Bee Movie" - JS REVISIONS 8/13/07 56. MOOSEBLOOD Uh oh. BARRY What is that? MOOSEBLOOD Oh no! It’s a wiper, triple blade! BARRY Triple blade? MOOSEBLOOD Jump on. It’s your only chance, bee. They hang on as the wiper goes back and forth. MOOSEBLOOD (CONT'D) (yelling to the truck driver through the glass) Why does everything have to be so dog-gone clean?! How much do you people need to see? Open your eyes! Stick your head out the window! CUT TO: INT. TRUCK CAB SFX: Radio. RADIO VOICE For NPR News in Washington, I’m Carl Kasell. EXT. TRUCK WINDSHIELD MOOSEBLOOD But don’t kill no more bugs! The Mosquito is FLUNG off of the wiper. MOOSEBLOOD (CONT'D) Beeeeeeeeeeeeee! BARRY Moose blood guy! "Bee Movie" - JS REVISIONS 8/13/07 57. Barry slides toward the end of the wiper, is thrown off, but he grabs the AERIAL and hangs on for dear life. Barry looks across and sees a CRICKET on another vehicle in the exact same predicament. They look at each other and SCREAM in unison. BARRY AND CRICKET Aaaaaaaaaah! ANOTHER BUG grabs onto the aerial, and screams as well. INT. TRUCK CAB - SAME TIME DRIVER You hear something? TRUCKER PASSENGER Like what? DRIVER Like tiny screaming. TRUCKER PASSENGER Turn off the radio. The driver reaches down and PRESSES a button, lowering the aerial. EXT. TRUCK WINDSHIELD - SAME TIME Barry and the other bug do a “choose up” to the bottom, Barry wins. BARRY Aha! Then he finally has to let go and gets thrown into the truck horn atop cab. Mooseblood is inside. MOOSEBLOOD Hey, what’s up bee boy? BARRY Hey, Blood! DISSOLVE TO: "Bee Movie" - JS REVISIONS 8/13/07 58. INT. TRUCK HORN - LATER BARRY ...and it was just an endless row of honey jars as far as the eye could see. MOOSEBLOOD Wow. BARRY So I’m just assuming wherever this honey truck goes, that’s where they’re getting it. I mean, that honey’s ours! MOOSEBLOOD Bees hang tight. BARRY Well, we’re all jammed in there. It’s a close community. MOOSEBLOOD Not us, man. We’re on our own. Every mosquito is on his own. BARRY But what if you get in trouble? MOOSEBLOOD Trouble? You're a mosquito. You're in trouble! Nobody likes us. They’re just all smacking. People see a mosquito, smack, smack! BARRY At least you’re out in the world. You must meet a lot of girls. MOOSEBLOOD Mosquito girls try to trade up; get with a moth, dragonfly...mosquito girl don’t want no mosquito. A BLOOD MOBILE pulls up alongside. MOOSEBLOOD (CONT'D) Whoa, you have got to be kidding me. Mooseblood’s about to leave the building. So long bee. "Bee Movie" - JS REVISIONS 8/13/07 59. Mooseblood EXITS the horn, and jumps onto the blood mobile. MOOSEBLOOD (CONT'D) Hey guys. I knew I’d catch you all down here. Did you bring your crazy straws? CUT TO: SEQ. 1900 - “THE APIARY” EXT. APIARY - LATER Barry sees a SIGN, “Honey Farms” The truck comes to a stop. SFX: The Honey farms truck blares its horn. Barry flies out, lands on the hood. ANGLE ON: Two BEEKEEPERS, FREDDY and ELMO, walking around to the back of the gift shop. Barry follows them, and lands in a nearby tree FREDDY ...then we throw it in some jars, slap a label on it, and it’s pretty much pure profit. BARRY What is this place? ELMO Bees got a brain the size of a pinhead. FREDDY They are pinheads. The both LAUGH. ANGLE ON: Barry REACTING. They arrive at the back of the shop where one of them opens a SMOKER BOX. FREDDY (CONT’D) Hey, check out the new smoker. "Bee Movie" - JS REVISIONS 8/13/07 60. ELMO Oh, Sweet. That’s the one you want. FREDDY The Thomas 3000. BARRY Smoker? FREDDY 90 puffs a minute, semi-automatic. Twice the nicotine, all the tar. They LAUGH again, nefariously. FREDDY (CONT’D) Couple of breaths of this, and it knocks them right out. They make the honey, and we make the money. BARRY “They make the honey, and we make the money?” Barry climbs onto the netting of Freddy’s hat. He climbs up to the brim and looks over the edge. He sees the apiary boxes as Freddy SMOKES them. BARRY (CONT'D) Oh my. As Freddy turns around, Barry jumps into an open apiary box, and into an apartment. HOWARD and FRAN are just coming to from the smoking. BARRY (CONT’D) What’s going on? Are you okay? HOWARD Yeah, it doesn’t last too long. HE COUGHS a few times. BARRY How did you two get here? Do you know you’re in a fake hive with fake walls? HOWARD (pointing to a picture on the wall) "Bee Movie" - JS REVISIONS 8/13/07 61. Our queen was moved here, we had no choice. BARRY (looking at a picture on the wall) This is your queen? That’s a man in women’s clothes. That’s a dragqueen! The other wall opens. Barry sees the hundreds of apiary boxes. BARRY (CONT'D) What is this? Barry pulls out his camera, and starts snapping. BARRY (CONT’D) Oh no. There’s hundreds of them. (V.O, as Barry takes pictures) Bee honey, our honey, is being brazenly stolen on a massive scale. CUT TO: SEQ. 2100 - “BARRY TELLS FAMILY” INT. BARRY’S PARENT’S HOUSE - LIVING ROOM - LATER Barry has assembled his parents, Adam, and Uncle Carl. BARRY This is worse than anything the bears have done to us. And I intend to do something about it. JANET BENSON Oh Barry, stop. MARTIN BENSON Who told you that humans are taking our honey? That’s just a rumor. BARRY Do these look like rumors? Barry throws the PICTURES on the table. Uncle Carl, cleaning his glasses with his shirt tail, digs through a bowl of nuts with his finger. "Bee Movie" - JS REVISIONS 8/13/07 62. HOWARD (CONT'D) UNCLE CARL That’s a conspiracy theory. These are obviously doctored photos. JANET BENSON Barry, how did you get mixed up in all this? ADAM (jumping up) Because he’s been talking to humans! JANET BENSON Whaaat? MARTIN BENSON Talking to humans?! Oh Barry. ADAM He has a human girlfriend and they make out! JANET BENSON Make out? Barry? BARRY We do not. ADAM You wish you could. BARRY Who’s side are you on? ADAM The bees! Uncle Carl stands up and pulls his pants up to his chest. UNCLE CARL I dated a cricket once in San Antonio. Man, those crazy legs kept me up all night. Hotcheewah! JANET BENSON Barry, this is what you want to do with your life? BARRY This is what I want to do for all our lives. Nobody works harder than bees. "Bee Movie" - JS REVISIONS 8/13/07 63. Dad, I remember you coming home some nights so overworked, your hands were still stirring. You couldn’t stop them. MARTIN BENSON Ehhh... JANET BENSON (to Martin) I remember that. BARRY What right do they have to our hardearned honey? We’re living on two cups a year. They’re putting it in lip balm for no reason what-soever. MARTIN BENSON Even if it’s true, Barry, what could one bee do? BARRY I’m going to sting them where it really hurts. MARTIN BENSON In the face? BARRY No. MARTIN BENSON In the eye? That would really hurt. BARRY No. MARTIN BENSON Up the nose? That’s a killer. BARRY No. There’s only one place you can sting the humans. One place where it really matters. CUT TO: SEQ. 2300 - “HIVE AT 5 NEWS/BEE LARRY KING” "Bee Movie" - JS REVISIONS 8/13/07 64. BARRY (CONT'D) INT. NEWS STUDIO - DAY DRAMATIC NEWS MUSIC plays as the opening news sequence rolls. We see the “Hive at Five” logo, followed by shots of past news events: A BEE freeway chase, a BEE BEARD protest rally, and a BEAR pawing at the hive as the BEES flee in panic. BOB BUMBLE (V.O.) Hive at Five, the hive’s only full hour action news source... SHOTS of NEWSCASTERS flash up on screen. BOB BUMBLE (V.O.) (CONT'D) With Bob Bumble at the anchor desk... BOB has a big shock of anchorman hair, gray temples and overly white teeth. BOB BUMBLE (V.O.) (CONT'D) ...weather with Storm Stinger, sports with Buzz Larvi, and Jeanette Chung. JEANETTE is an Asian bee. BOB BUMBLE (CONT'D) Good evening, I’m Bob Bumble. JEANETTE CHUNG And I’m Jeanette Chung. BOB BUMBLE Our top story, a tri-county bee, Barry Benson... INSERT: Barry’s graduation picture. BOB BUMBLE (CONT'D) ...is saying he intends to sue the human race for stealing our honey, packaging it, and profiting from it illegally. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 65. INT. BEENN STUDIO - BEE LARRY KING LIVE BEE LARRY KING, wearing suspenders and glasses, is interviewing Barry. A LOWER-THIRD CHYRON reads: “Bee Larry King Live.” BEE LARRY KING Don’t forget, tomorrow night on Bee Larry King, we are going to have three former Queens all right here in our studio discussing their new book, “Classy Ladies,” out this week on Hexagon. (to Barry) Tonight, we’re talking to Barry Benson. Did you ever think, I’m just a kid from the hive, I can’t do this? BARRY Larry, bees have never been afraid to change the world. I mean, what about Bee-Columbus? Bee-Ghandi? Be-geesus? BEE LARRY KING Well, where I’m from you wouldn’t think of suing humans. We were thinking more like stick ball, candy stores. BARRY How old are you? BEE LARRY KING I want you to know that the entire bee community is supporting you in this case, which is certain to be the trial of the bee century. BARRY Thank you, Larry. You know, they have a Larry King in the human world, too. BEE LARRY KING It’s a common name. Next week on Bee Larry King... "Bee Movie" - JS REVISIONS 8/13/07 66. BARRY No, I mean he looks like you. And he has a show with suspenders and different colored dots behind him. BEE LARRY KING Next week on Bee Larry King... BARRY Old guy glasses, and there’s quotes along the bottom from the guest you’re watching even though you just heard them... BEE LARRY KING Bear week next week! They’re scary, they’re hairy, and they’re here live. Bee Larry King EXITS. BARRY Always leans forward, pointy shoulders, squinty eyes... (lights go out) Very Jewish. CUT TO: SEQ. 2400 - “FLOWER SHOP” INT. VANESSA’S FLOWER SHOP - NIGHT Stacks of law books are piled up, legal forms, etc. Vanessa is talking with Ken in the other room. KEN Look, in tennis, you attack at the point of weakness. VANESSA But it was my grandmother, Ken. She’s 81. KEN Honey, her backhand’s a joke. I’m not going to take advantage of that? "Bee Movie" - JS REVISIONS 8/13/07 67. BARRY (O.C) Quiet please. Actual work going on here. KEN Is that that same bee? BARRY (O.C) Yes it is. VANESSA I’m helping him sue the human race. KEN What? Barry ENTERS. BARRY Oh, hello. KEN Hello Bee. Barry flies over to Vanessa. VANESSA This is Ken. BARRY Yeah, I remember you. Timberland, size 10 1/2, Vibram sole I believe. KEN Why does he talk again, Hun? VANESSA (to Ken, sensing the tension) Listen, you’d better go because we’re really busy working. KEN But it’s our yogurt night. VANESSA (pushing him out the door) Oh...bye bye. She CLOSES the door. KEN Why is yogurt night so difficult?! "Bee Movie" - JS REVISIONS 8/13/07 68. Vanessa ENTERS the back room carrying coffee. VANESSA Oh you poor thing, you two have been at this for hours. BARRY Yes, and Adam here has been a huge help. ANGLE ON: A EMPTY CINNABON BOX with Adam asleep inside, covered in frosting. VANESSA How many sugars? BARRY Just one. I try not to use the competition. So, why are you helping me, anyway? VANESSA Bees have good qualities. BARRY (rowing on the sugar cube like a gondola) Si, Certo. VANESSA And it feels good to take my mind off the shop. I don’t know why, instead of flowers, people are giving balloon bouquets now. BARRY Yeah, those are great...if you’re 3. VANESSA And artificial flowers. BARRY (re: plastic flowers) Oh, they just get me psychotic! VANESSA Yeah, me too. BARRY The bent stingers, the pointless pollination. "Bee Movie" - JS REVISIONS 8/13/07 69. VANESSA Bees must hate those fake plastic things. BARRY There’s nothing worse than a daffodil that’s had work done. VANESSA (holding up the lawsuit documents) Well, maybe this can make up for it a little bit. CUT TO: EXT. VANESSA’S FLORIST SHOP They EXIT the store, and cross to the mailbox. VANESSA You know Barry, this lawsuit is a pretty big deal. BARRY I guess. VANESSA Are you sure that you want to go through with it? BARRY Am I sure? (kicking the envelope into the mailbox) When I’m done with the humans, they won’t be able to say, “Honey, I’m home,” without paying a royalty. CUT TO: SEQ. 2700 - “MEET MONTGOMERY” EXT. MANHATTAN COURTHOUSE - DAY P.O.V SHOT - A camera feed turns on, revealing a newsperson. "Bee Movie" - JS REVISIONS 8/13/07 70. PRESS PERSON #2 (talking to camera) Sarah, it’s an incredible scene here in downtown Manhattan where all eyes and ears of the world are anxiously waiting, because for the first time in history, we’re going to hear for ourselves if a honey bee can actually speak. ANGLE ON: Barry, Vanessa, and Adam getting out of the cab. The press spots Barry and Vanessa and pushes in. Adam sits on Vanessa’s shoulder. INT. COURTHOUSE - CONTINUOUS Barry, Vanessa, and Adam sit at the Plaintiff’s Table. VANESSA (turns to Barry) What have we gotten into here, Barry? BARRY I don’t know, but it’s pretty big, isn’t it? ADAM I can’t believe how many humans don’t have to be at work during the day. BARRY Hey, you think these billion dollar multinational food companies have good lawyers? CUT TO: EXT. COURTHOUSE STEPS - CONTINUOUS A BIG BLACK CAR pulls up. ANGLE ON: the grill filling the frame. We see the “L.T.M” monogram on the hood ornament. The defense lawyer, LAYTON T. MONTGOMERY comes out, squashing a bug on the pavement. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 71. INT. COURTHOUSE - CONTINUOUS Barry SHUDDERS. VANESSA What’s the matter? BARRY I don’t know. I just got a chill. Montgomery ENTERS. He walks by Barry’s table shaking a honey packet. MONTGOMERY Well, if it isn’t the B-Team. (re: the honey packet) Any of you boys work on this? He CHUCKLES. The JUDGE ENTERS. SEQ. 3000 - “WITNESSES” BAILIFF All rise! The Honorable Judge Bumbleton presiding. JUDGE (shuffling papers) Alright...Case number 4475, Superior Court of New York. Barry Bee Benson vs. the honey industry, is now in session. Mr. Montgomery, you are representing the five major food companies, collectively. ANGLE ON: Montgomery’s BRIEFCASE. It has an embossed emblem of an EAGLE, holding a gavel in one talon and a briefcase in the other. MONTGOMERY A privilege. JUDGE Mr. Benson. Barry STANDS. JUDGE (CONT’D) You are representing all bees of the world? "Bee Movie" - JS REVISIONS 8/13/07 72. Montgomery, the stenographer, and the jury lean in. CUT TO: EXT. COURTHOUSE - CONTINUOUS The spectators outside freeze. The helicopters angle forward to listen closely. CUT TO: INT. COURTHOUSE BARRY Bzzz bzzz bzzz...Ahh, I’m kidding, I’m kidding. Yes, your honor. We are ready to proceed. ANGLE ON: Courtroom hub-bub. JUDGE And Mr. Montgomery, your opening statement, please. Montgomery rises. MONTGOMERY (grumbles, clears his throat) Ladies and gentlemen of the jury. My grandmother was a simple woman. Born on a farm, she believed it was man's divine right to benefit from the bounty of nature God put before us. If we were to live in the topsy-turvy world Mr. Benson imagines, just think of what it would mean. Maybe I would have to negotiate with the silk worm for the elastic in my britches. Talking bee. How do we know this isn’t some sort of holographic motion picture capture Hollywood wizardry? They could be using laser beams, robotics, ventriloquism, cloning...for all we know he could be on steroids! Montgomery leers at Barry, who moves to the stand. "Bee Movie" - JS REVISIONS 8/13/07 73. JUDGE Mr. Benson? Barry makes his opening statement. BARRY Ladies and Gentlemen of the jury, there’s no trickery here. I’m just an ordinary bee. And as a bee, honey’s pretty important to me. It’s important to all bees. We invented it, we make it, and we protect it with our lives. Unfortunately, there are some people in this room who think they can take whatever they want from us cause we’re the little guys. And what I’m hoping is that after this is all over, you’ll see how by taking our honey, you’re not only taking away everything we have, but everything we are. ANGLE ON: Vanessa smiling. ANGLE ON: The BEE GALLERY wiping tears away. CUT TO: INT. BENSON HOUSE Barry’s family is watching the case on TV. JANET BENSON Oh, I wish he would dress like that all the time. So nice... CUT TO: INT. COURTROOM - LATER JUDGE Call your first witness. CUT TO: "Bee Movie" - JS REVISIONS 8/13/07 74. INT. COURTHOUSE - LATER BARRY So, Mr. Klauss Vanderhayden of Honey Farms. Pretty big company you have there? MR. VANDERHAYDEN I suppose so. BARRY And I see you also own HoneyBurton, and Hon-Ron. MR. VANDERHAYDEN Yes. They provide beekeepers for our farms. BARRY Beekeeper. I find that to be a very disturbing term, I have to say. I don’t imagine you employ any bee free-ers, do you? MR. VANDERHAYDEN No. BARRY I’m sorry. I couldn’t hear you. MR. VANDERHAYDEN (louder) No. BARRY No. Because you don’t free bees. You keep bees. And not only that, it seems you thought …

---
## [dawinkenwe/dnd5e_simulator](https://github.com/dawinkenwe/dnd5e_simulator)@[010c910400...](https://github.com/dawinkenwe/dnd5e_simulator/commit/010c91040045bff37343c6c5d72bad8a76c603ef)
#### Friday 2023-11-10 22:07:02 by dwink

Commit work done at Victors house so I can move from laptop to desktop. Don't judge me. Only god can judge me. And my friends, and my parents, and literal judges, and. ok fine. You can judge me. Thanks bud.

---
## [jorge-pais/KUL-DistributedSystems](https://github.com/jorge-pais/KUL-DistributedSystems)@[318dd95c19...](https://github.com/jorge-pais/KUL-DistributedSystems/commit/318dd95c195433a1633a5b98568f02b9ed1cb0ed)
#### Friday 2023-11-10 22:13:35 by Jorge Miguel Lopes Pais

Finally got the PubSub messaging working. Fuck you Kristof Jannes, i hope you keep getting no bitches

---
## [scholarsportal/Dataverse-Data-Curation-Tool](https://github.com/scholarsportal/Dataverse-Data-Curation-Tool)@[349df344d2...](https://github.com/scholarsportal/Dataverse-Data-Curation-Tool/commit/349df344d2dd0a4114e7075dd432f1569f0fbe70)
#### Friday 2023-11-10 23:10:45 by Nana Boateng

Merge pull request #57 from nana-boateng/master

GitHub has the most annoying rebase process ever. Never follow their built-in instructions unless you want to ruin your Friday night. I hate Microsoft with a passion.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1e6dbd952a...](https://github.com/pytorch/pytorch/commit/1e6dbd952a752fe635c71fcc9d4c70c3a2629bc7)
#### Friday 2023-11-10 23:35:20 by Brian Hirsh

Update base for Update on "AOTAutograd: handle set_(), detect metadata mutations that cancel out"

This should be enough to get voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

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




cc voznesenskym penguinwu EikanWang jgong5 Guobing-Chen XiaobingSuper zhuhaozhe blzheng wenzhe-nrv jiayisunx chenyang78 aakhundov kadeng

[ghstack-poisoned]

---

