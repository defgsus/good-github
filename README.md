## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-21](docs/good-messages/2023/2023-09-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,397,624 were push events containing 3,601,895 commit messages that amount to 271,418,941 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 74 messages:


## [mateox222/Eu4-The-Odd-Empires--BETA](https://github.com/mateox222/Eu4-The-Odd-Empires--BETA)@[906dc266d7...](https://github.com/mateox222/Eu4-The-Odd-Empires--BETA/commit/906dc266d757e2d2a80ef11e36c6c3aff411484a)
#### Thursday 2023-09-21 00:11:59 by Mateusz Posemkiewicz

I HATE THIS DAMN GAME BUT I MANAGED TO FIX THIS FUCKING BUG

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[bc1f697927...](https://github.com/TaleStation/TaleStation/commit/bc1f697927d682f3b7f9eb909595fac4c50d895f)
#### Thursday 2023-09-21 00:23:27 by Jolly

[MANUAL MIRROR] Only double HCR for impressive greentexts (#7804)

Original PR: https://github.com/tgstation/tgstation/pull/78383
----

## Changelog

:cl: Time-Green
balance: Only traitor, changeling, heretic, blood brother, headrev,
wizard, obsessed, magic/gun survivalists and greentext book holders can
now double their hardcore random score
qol: Redtexting as antag with hardcore random score will pay you default
points, instead of none (normal survival rules)
fix: End report screen will properly report hardcore random survival in
case of station destruction
/:cl:

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [InnovAnon-Inc/dcc](https://github.com/InnovAnon-Inc/dcc)@[030af80fa5...](https://github.com/InnovAnon-Inc/dcc/commit/030af80fa556942450233a4fa707600012aa62af)
#### Thursday 2023-09-21 00:31:04 by Innovations Anonymous

STOP DELETING MY FUCKING CODE YOU STUPID PIECE OF SHIT

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[b22529fc74...](https://github.com/Apogee-dev/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Thursday 2023-09-21 01:05:52 by zevo

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
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[2fc01ad8be...](https://github.com/Apogee-dev/Shiptest/commit/2fc01ad8be958492a38b3200023b8aa0c4bad9f5)
#### Thursday 2023-09-21 01:06:11 by Skrem_7

Skrem's Quick Ballistic Glanceover (#2354)

## About The Pull Request

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

## Why It's Good For The Game

### Slug and Pellet Changes
The pellet changes are actually just systemizing what was supposed to be
intentional design according to code comments, it just hadn't reached
every single pellet-based shotgun projectile. The improvised shell buff
is to make it not a potential complete whiff because RNG mechanics are
generally bad and not fun to play with.

### Less-Lethal Changes
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

### .38 Changes
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

### Projectile Speed and Match Changes
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

### Sniper Rifle Knockdown Change
Having a big-ass bullet that does 70 damage with 50 AP hit you is
already a middle finger. Making it potentially knock off an arm or a leg
is another middle finger. Being hardstunned for ten seconds after is the
icing on the cake. Changed it to a knockdown because we hate ranged
tasers.

### Surplus Rifle Fire Rate Buff
This thing is a joke. I haven't even seen it on the server, but I'd
rather make it vaguely competitive considering 10mm isn't super deadly
and only otherwise exists on the stechkin or the one Inteq SMG that you
never see (Colossus-only).

It's still clunky and terrible, but it should be less comedic and more
of a potential option if you have NOTHING else (will never happen).

### Boarder Magazine Change
Top-loading magazine fits into a standard assault rifle? No. Doesn't
make sense. Someone should probably just kill this gun, it's stupid and
looks stupid last I checked.

### WT-550 Magazine Fix
Don't think I've seen anyone use this weapon, I've only printed out
their magazines to dump AP rounds into my NT-SVG carbine. Noticed they
were invisible then. Someone increased their capacity to 30 without a
care for how its update_icon works. Not cool. Anyway, fixes are good.
Moving on.

### Syntax, Description, Spelling, and Overall Presentation Changes
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

## Changelog

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

---
## [Ogawa-Hidekatsu/CSrankings](https://github.com/Ogawa-Hidekatsu/CSrankings)@[a53daa07b6...](https://github.com/Ogawa-Hidekatsu/CSrankings/commit/a53daa07b64598a6400d90b42f5b162d1981e90f)
#### Thursday 2023-09-21 01:12:56 by Shixiong

Update Samantha Reig to csrankings-s.csv

Samantha Reig is a new Assistant Professor (fall 2023) in the Miner School of Computer and Information Sciences at the University of Massachusetts Lowell. Her research interests include artificial intelligence (AI) embodiment in socially complex interactions, robot re-embodiment, personalized experiences with AI agents in services, and designing for human-AI teaming in space.

---
## [Superreallycoolguy/SRC-CMSS13](https://github.com/Superreallycoolguy/SRC-CMSS13)@[9dbf819e8a...](https://github.com/Superreallycoolguy/SRC-CMSS13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Thursday 2023-09-21 01:24:38 by forest2001

Codebook Optimisation (#4393)

# About the pull request
For as long as we've had a codebook it's been a pain in the arse to
read/synchronise from a staff POV. With this, codebooks will all share
the same codes per-faction.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Makes events that use codebooks actually viable.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Codebooks are now faction based rather than individually unique.
/:cl:

---
## [deathrobotpunch/tgstation](https://github.com/deathrobotpunch/tgstation)@[c571222cd7...](https://github.com/deathrobotpunch/tgstation/commit/c571222cd79b0d8eab5f18846b43e2af559a6999)
#### Thursday 2023-09-21 02:36:46 by san7890

Readds (some) Knockdown Vomits (#78301)

## About The Pull Request

ALL stunning vomits were nerfed to have just a motionless stun in #70245
(14438a2b7d5d781c340713983f8f07fb09179f08), and while it didn't really
affect game balance beyond just making you not fall on the floor... I
really didn't like it since it was all-or-nothing. Fortunately with
#78191 (a7060641bb0165a7531a3cee007989d9e95741ee), we are able to add
more expression to how a vomit should go down using the new bitflag
system, so I decided to rewrite it back in for a special number of
cases.

I only did it for two cases, but anyone is free to change anything they
think they deserve it via changing the vomit flags that are passed into
the proc. Those cases are:

* Places where you vomit after spinning too hard. You lost balance and
threw up. That makes more sense to me than just being suddenly and
completely motionless without any sign of loss of inertia.
* Organ heal rejections. You literally vomit out an organ. How are you
still standing up? Beyond making no sense in anatomy, you should really
feel the _oomph_ from literally puking out an organ.
## Why It's Good For The Game

This is a bit of flavor that really ensaddened me when I realized it was
removed because it really does miss out on the real and true impact.
While I do agree with some merits of the aforementioned balance PR that
removed it, I do not think that it works at all for a blanket case. Now
that we are able to add this expression, we should, because it's cool.

Also cleaned up some comments I forgot to update from the last time.
## Changelog
:cl:
balance: You will be knocked down again on certain vomits. Don't worry,
you'll deserve it when it happens.
/:cl:

---
## [deathrobotpunch/tgstation](https://github.com/deathrobotpunch/tgstation)@[c6ac468b90...](https://github.com/deathrobotpunch/tgstation/commit/c6ac468b9083ff06b36a544382684c86743e953e)
#### Thursday 2023-09-21 02:36:46 by Hatterhat

second pass over the SC/FISHER code, incl. bitflags and PDAs (#78330)

## About The Pull Request
makes `COMSIG_HIT_BY_SABOTEUR` return a bitflag in order to close #78297
(i am very sorry)
fixes #78298
extends flashlight disabling to modular computers incl. PDAs because
somehow i forgot that they had flashlights.
## Why It's Good For The Game
my code sucks and i should make it suck less, actually

## Changelog
i don't think i get to put a code improvement tag if it's not
playerfacing and it's my own fault
:cl:
fix: Flares and candles no longer sound like flashlights when being
turned on.
fix: Getting shot by an SC/FISHER now disables PDA lights for
consistency's sake.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [zimokernel/bevy](https://github.com/zimokernel/bevy)@[44f677a38a...](https://github.com/zimokernel/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Thursday 2023-09-21 02:48:41 by Sélène Amanita

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
## [bushrat011899/bevy](https://github.com/bushrat011899/bevy)@[3ee9edf280...](https://github.com/bushrat011899/bevy/commit/3ee9edf280c530f35a51049ec92fcfa552998614)
#### Thursday 2023-09-21 02:50:32 by Ethereumdegen

add try_insert to entity commands (#9844)

# Objective

- I spoke with some users in the ECS channel of bevy discord today and
they suggested that I implement a fallible form of .insert for
components.

- In my opinion, it would be nice to have a fallible .insert like
.try_insert (or to just make insert be fallible!) because it was causing
a lot of panics in my game. In my game, I am spawning terrain chunks and
despawning them in the Update loop. However, this was causing bevy_xpbd
to panic because it was trying to .insert some physics components on my
chunks and a race condition meant that its check to see if the entity
exists would pass but then the next execution step it would not exist
and would do an .insert and then panic. This means that there is no way
to avoid a panic with conditionals.

Luckily, bevy_xpbd does not care about inserting these components if the
entity is being deleted and so if there were a .try_insert, like this PR
provides it could use that instead in order to NOT panic.

( My interim solution for my own game has been to run the entity despawn
events in the Last schedule but really this is just a hack and I should
not be expected to manage the scheduling of despawns like this - it
should just be easy and simple. IF it just so happened that bevy_xpbd
ran .inserts in the Last schedule also, this would be an untenable soln
overall )

## Solution

- Describe the solution used to achieve the objective above.

Add a new command named TryInsert (entitycommands.try_insert) which
functions exactly like .insert except if the entity does not exist it
will not panic. Instead, it will log to info. This way, crates that are
attaching components in ways which they do not mind that the entity no
longer exists can just use try_insert instead of insert.

---

## Changelog

 

## Additional Thoughts

In my opinion, NOT panicing should really be the default and having an
.insert that does panic should be the odd edgecase but removing the
panic! from .insert seems a bit above my paygrade -- although i would
love to see it. My other thought is it would be good for .insert to
return an Option AND not panic but it seems it uses an event bus right
now so that seems to be impossible w the current architecture.

---
## [devopsleague/microsoft-terminal](https://github.com/devopsleague/microsoft-terminal)@[b1ace967a2...](https://github.com/devopsleague/microsoft-terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Thursday 2023-09-21 02:57:06 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [a30durrani/Scribekick-website](https://github.com/a30durrani/Scribekick-website)@[22d6540c6c...](https://github.com/a30durrani/Scribekick-website/commit/22d6540c6cf7947e25f6cae650811c6656c116c6)
#### Thursday 2023-09-21 03:22:32 by Ahmed Durrani

Built the About Us page and made some tweaks to the footer. God I'm fucking on one. I love you all. I can't wait to build the future.

---
## [entrez/NetHack](https://github.com/entrez/NetHack)@[1a64ee1c28...](https://github.com/entrez/NetHack/commit/1a64ee1c285f8d9a27e58efa3989a281413f9b8e)
#### Thursday 2023-09-21 03:49:09 by PatR

github PR #259 - paranoid_confirmation:trap

Fairly old pull request from copperwater:  add new paranoid_confirm
setting 'trap'.

The old commit suffered from bit rot and merging needed too much
fixing up despite there not being many bands of change in the commit's
diffs.  I ultimately redid it from scratch, although the two biggest
chunks of code started with copy+paste of the pull request's commit.

It operates like paranoid:pray.  Setting paranoid:trap adds a new
"Really step into <trap>?" y/n prompt when attempting to move
into/onto a known trap, even if an object covers it on the map.
Setting both 'paranoid:Confirm trap' turns that into a yes/no prompt.
(Adding 'Confirm' affects other paranoid confirmations; in addition
to requiring yes<return> rather than just y to accept, it also forces
no<return> to reject.)

However, moving into a known trap that is considered to be harmless
behaves as if no trap was present.  Some of the trap classification
might be out of date; several types of traps have undergone changes
since implementation of the original pull request, notably anti-magic
field.  When the hero is hallucinating, all known traps are considered
harmful since the map no longer reliably describes them.

Preceding a movement command with the 'm' prefix also behaves as if
no trap was present, bypassing confirmation for that move, similar to
how paranoid:swim currently behaves.  Being stunned or confused also
behaves as if no trap was present, taking priority over hallucination.

This updates the documentation.

Supersedes #259
Closes #259

---
## [xXPawnStarrXx/Skyrat-tg](https://github.com/xXPawnStarrXx/Skyrat-tg)@[0687af984d...](https://github.com/xXPawnStarrXx/Skyrat-tg/commit/0687af984d6b4d5acbe374444f395a2457437763)
#### Thursday 2023-09-21 04:44:59 by SkyratBot

[MIRROR] Light eater is now indestructible [MDB IGNORE] (#23339)

* Light eater is now indestructible (#77903)

## About The Pull Request

This means a nightmare going into an emagged recycler will no longer be
fucked by their lack of a light eater.
Oh yeah, also moved the ACID_PROOF flag to the correct bitflag.
## Why It's Good For The Game

Bugfix good, you're not supposed to be able to delete an external limb
generated by an internal one, such as implants and such. Pretty sure
reimplanting the heart would make the light eater reappear, too, but
that's night impossible to get done as a nightmare.
## Changelog
:cl:
fix: Light eaters can no longer be eaten by their higher-grade brothers,
the trash eaters. (recyclers)
/:cl:

* Light eater is now indestructible

---------

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [Orvid/Caprica](https://github.com/Orvid/Caprica)@[b3a999b232...](https://github.com/Orvid/Caprica/commit/b3a999b2322aaa27244c8b11ae3238e4f83e6719)
#### Thursday 2023-09-21 05:09:53 by nikitalita

WIP Skyrim support

holy shit, PCompiler is CURSED

---
## [rockola/NetHack](https://github.com/rockola/NetHack)@[38cda5ad52...](https://github.com/rockola/NetHack/commit/38cda5ad52f47a810c44171e9081d0275401c516)
#### Thursday 2023-09-21 05:43:38 by Michael Meyer

Adjust seenres on visible gear removal

If a monster sees you remove some piece of gear that grants a
resistance, it will remove that resistance from its list of remembered
resistances and be willing to try attacking you with that adtyp again.
This avoids the situation where you put on a ring of cold, get hit with
one cold attack, and then can remove it because all the monsters nearby
will permanently remember you as being cold resistant (but even after
this change a wily hero could still step into a niche and do it without
any monsters seeing, so trick them into thinking she's still cold
resistant...).  The hero could still be resistant if there were multiple
sources to begin with, of course, but the monsters will test it and
learn that again if necessary.

It's a little weird that the monsters can recognize the intrinsic
granted by the item being removed, but they display knowledge of
unidentified (by the hero) objects in many other circumstances too, so I
hope it's forgivable in the pursuit of having them act more cleverly
about resuming previously-resisted attacks like this.  Another approach
that avoids the gear recognition, blanking seenres on any gear change,
can result in odd situations like orcs treating their own cloaks as
potential sources of many different resistances, which also seems silly.

---
## [consuldemocracy/consuldemocracy](https://github.com/consuldemocracy/consuldemocracy)@[970a64e276...](https://github.com/consuldemocracy/consuldemocracy/commit/970a64e2762c8dd8c9e265acb9195f069ea7bb0a)
#### Thursday 2023-09-21 06:29:36 by Javi Martín

Enable mousewheel when focusing on the map

Zooming with the mousewheel is useful when you want to use it, but
annoying when you don't want to.

Here we're taking an intermediary approach: by default, the mousewheel
isn't active, but it will be active after focusing on the map, so it can
be used both to scroll and to zoom.

This behavior presents usability issues, though, since we aren't making
users aware of the way the mousewheel works, and even if they were
aware, it could be confusing anyway. However, I currently think it's
better than always enabling or always disabling the mousewheel (might
change my mind, though).

Note that the "focus" event is only used on the map, so if we click on a
marker or navigate to a marker with the keyboard without focusing on the
map first, the mousewheel isn't enabled. The same would happen if we
used the "click" event.

We might use the Leaflet.GestureHandling plugin in the future to deal
with this issue and the scroll on touch screens.

---
## [JaredEllis/GameJamF23](https://github.com/JaredEllis/GameJamF23)@[784b3fd6d4...](https://github.com/JaredEllis/GameJamF23/commit/784b3fd6d4af8b0c26a9ba51524c600ee43d1379)
#### Thursday 2023-09-21 07:42:59 by Jared Ellis

Merge pull request #3 from JaredEllis/ai

holy fucking shit we got AI now

---
## [Moosyu/moosyu.github.io](https://github.com/Moosyu/moosyu.github.io)@[9238433154...](https://github.com/Moosyu/moosyu.github.io/commit/92384331548bb22292820da299e2b598c2ece624)
#### Thursday 2023-09-21 08:14:49 by Moosy

damn ive read a lot of disgusting shit recently

between the lastest chapters of nano machine and mushoku tensei ive lost my faith in humanity. like holy shit the nano machine comment section is talking like rape isnt a bad thing? and how does between the lastest chapters of nano machine and mushoku tensei want me to sympathise  with an incestuous pedophile

---
## [weber8thomas/snakemake](https://github.com/weber8thomas/snakemake)@[c9eaa4e12e...](https://github.com/weber8thomas/snakemake/commit/c9eaa4e12e4a348f93e5ea5793faaec1fd547fac)
#### Thursday 2023-09-21 08:22:07 by Vanessasaurus

feat: support for external executor plugins (#2305)

Hi @johanneskoester! :wave: As we chat about in a thread somewhere, I
think it would be really powerful to allow for installing (and
discovering) external plugins to Snakemake. Specifically for the Flux
Operator, I have easily three designs I'm testing, and it's not really
appropriate to add them proper to snakemake - but I believe the
developer user should be empowered to flexibly add/remove and test them
out.

This pull request is first try demo of how snakemake could allow
external executor plugins. I say "first try" because it's the first time
I've experimented with plugins, and I tried to choose a design that
optimizes simplicity and flexibility without requiring external
packages, or specific features of setuptools or similar (that are likely
to change). The basic design here uses pkgutil to discover
snakemake_executor_* plugins, and then provides them to the client (to
add arguments) and scheduler to select using one with `--executor`.

I've written up an entire tutorial and the basic design in this early
prototype, which is basically the current Flux integration as a plugin!
https://github.com/snakemake/snakemake-executor-flux. The user would
basically do:

```bash
# Assuming this was released on pypi (it's not yet)
$ pip install snakemake-executor-flux

# Run the workflow using the flux custom executor
$ snakemake --jobs 1 --executor flux
```
I've designed it so that plugins are validated only when chosen, and
each plugin can add or otherwise customize the parser, and then (after
parsing) further tweak the args if chosen. Then in scheduler.py, we
simply look if the user selected a plugin, and call the main executor
(and local_executor) classes if this is the case.

The one hard piece is having a flexible way to pass forward all those
custom arguments. The current snakemake design has basically a custom
boolean for every executor hard coded (e.g., `--flux` or `--slurm`) and
while we don't want to blow that up, I'm worried moving forward passing
all these custom namespaced arguments through the init, workflow,
scheduler/dag, is going to get very messy. So the approach here is a
suggested way to handle the expanding space of additional executors by
way of passing forward full args, and then allowing the plugins to
customize the parser before or after. If we were to, for example, turn
current executors into plugins (something I expect we might want to do
for the Google Life Sciences API that is going to be deprecated in favor
of batch) we could write out a more hardened spec - some configuration
class that is passed from the argument parser through the executor and
through execution (instead of all the one off arguments).

Anyway - this is just a first shot and I'm hoping to start some
discussion! This is a totally separate thing from TBA work with Google
Batch - this is something that I've wanted to try for a while as I've
wanted to add more executors and have seen the executor space exploding.
:laughing: I haven't written tests or updated any docs yet pending our
discussion!

### QC

* [ ] The PR contains a test case for the changes or the changes are
already covered by an existing test case.
* [ ] The documentation (`docs/`) is updated to reflect the changes or
this is not necessary (e.g. if the change does neither modify the
language nor the behavior or functionalities of Snakemake).

---------

Signed-off-by: vsoch <vsoch@users.noreply.github.com>
Co-authored-by: vsoch <vsoch@users.noreply.github.com>
Co-authored-by: Johannes Köster <johannes.koester@tu-dortmund.de>
Co-authored-by: Johannes Köster <johannes.koester@uni-due.de>

---
## [iotaledger/iota.go](https://github.com/iotaledger/iota.go)@[3ae2edc8a2...](https://github.com/iotaledger/iota.go/commit/3ae2edc8a2402ddebd618a3b88b7e096caae517d)
#### Thursday 2023-09-21 08:52:11 by muXxer

"My mama always said, 'Life was like a CI full of linters. You never know what stupid error messages you're gonna get.'" -muXxer

---
## [DrDuckedGoose/tgstation](https://github.com/DrDuckedGoose/tgstation)@[0631fe5bde...](https://github.com/DrDuckedGoose/tgstation/commit/0631fe5bde73a68b4c12bdfa633c30b2cee442d5)
#### Thursday 2023-09-21 08:59:41 by Jacquerel

Add Croissants & Traitorous Baking Techniques (#72232)

## About The Pull Request

This is my Christmas present to mimes everywhere.

First of all this adds Croissants, because I thought they already
existed and was shocked to learn that they did not.

![image](https://user-images.githubusercontent.com/7483112/209454610-4e69563f-b83d-465b-b28e-7e0b482ff01b.png)
Here's a croissant and an unbaked croissant.
In terms of food they are GRAIN, DAIRY, and BREAKFAST and made fairly
simply from sugar, dough, and butter.

Secondly it adds this pack of traitor gear, exclusively for Mimes and
Chefs.

![image](https://user-images.githubusercontent.com/7483112/209454613-059759b2-774c-45e2-9e1e-97adb43f75f1.png)
The contents of this pack are:
- One combat baguette, indistinguishable from a regular baguette. If
wielded as a sword it gains a 50% block chance (equal to the Captain's
sabre) and does 20 damage.
- Two throwing croissants, which do 20 throwing damage and return to
your hand like boomerangs.
- A cookbook which teaches you the secret to turning croissaints into
deadly boomerang weapons.

You make a croissant into a throwing croissant simply by inserting an
expertly bent iron rod into it.
The chef can't make any use of the baguette unless they also gain the
ability to mime, but they can use it to make food.


https://user-images.githubusercontent.com/7483112/209454703-feafcf4c-6d0a-4e9a-ac4a-d3e2fc7c0ffb.mp4

Watch me here struggle to use them to kill an ape (they don't return to
your hands if thrown at an adjacent tile).

## Why It's Good For The Game

It's insane that croissants aren't already in the game.
This gives mimes an "invisible" sword to go with their invisible gun (it
announces to everyone nearby when you're about to use it, but they can't
know if it's just a _regular_ baguette).
It's funny to throw bread at people.

## Changelog

:cl:
add: You can now bake croissants to add to your breakfast.
add: Traitorous chefs can bake dangerous throwing croissants, Mimes can
do this and gain the additional benefit of a deadly combat baguette.
/:cl:

---
## [Shootfast/oiio](https://github.com/Shootfast/oiio)@[4e985f6347...](https://github.com/Shootfast/oiio/commit/4e985f63474e21298974a3f96536597a7306e199)
#### Thursday 2023-09-21 09:31:05 by Larry Gritz

Lay groundwork for unity builds (#3381)

As I learned recently, a "unity" (aka "jumbo") build is where multiple
.cpp files are combined into one translation unit -- imagine a unity.cpp
that simply has

    #include "file1.cpp"
    #include "file2.cpp"
    ...
    #include "fileN.cpp"

and so you compile unity.cpp instead of the separate file?.cpp files
individually.

Turns out that CMake understands this concept and can do it for you
automatically!

The benefit of a unity build is that file1...fileN probably include
most of the same headers, expand the same templates, etc., so a bunch
of the per-file work of the compiler can be done once rather than
redundantly for each file.

There are two potential downsides, however:

1. It may not be safe to concatenate your cpp files! For example, if
   both file1.cpp and file2.cpp each contain a `static int foo;`, that
   may have been safe when compiled separately, but is not allowed to
   happen twice in one compilation unit. Similarly, if you have headers
   that don't have proper guards against multiple includes, etc. So one
   should expect a whole lot of little fix-ups are needed for this to
   work properly. (We'll come back to that topic.)

2. Combining source file into these "jumbo" modules can make heavily
   parallelized builds on many-core machine not be able to load balance
   or keep all the cores busy. (Simplified examples: if you have 16 .cpp
   files on a 16 core machine, each core can compile one cpp file in
   parallel with the others. But if you mash the modules into just one
   huge cpp file, give that to one core, and your other 15 cores are
   idle, so the full build probably takes much longer.)

I tried this out, including the many fixups implied by (1) above, and
at first the unity builds were slower on both my laptop (8 cores) and
workstation at work (32 cores), because of downside (2) explained
earlier -- harder to take advantage of parallel builds when there are
fewer, bigger, compilation units. Some tweaking of strategy got me to
the point where I could always get the unity builds to go faster, but
not by a whole lot when many core were available. Slighty faster, but
not worth the trouble. A bit disappointing, nearly abandoned the whole
idea.

HOWEVER, in situation where you are limited to very few cores (like in our
CI, which allocates 2 cores, and it sure seems more like 1-1.5 for the
Windows and Mac CI runners), the unity builds are substantially faster --
there's already not much parallelism to exploit, so you come out ahead
with the savings of that redundant per-file work we talked about.

So my current thinking is to go ahead and make the changes that allow
unity builds. I don't particularly recommend them when highly parallel
builds are available to you, but it might help to cut our CI
turnaround time down on the GitHub runners. And maybe it will help in
other situations for other people.

Ok, then. The present patch introduces these concepts and makes the
CMake and other build system changes to allow unity builds. (N.B. It
won't WORK yet, so don't try it!) After we get that out of the way, in
subsequent PRs I'll show all the changs to the code that were
necessary to fix all the little things that went wrong when source
files got combined.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[246133faa9...](https://github.com/wrye-bash/wrye-bash/commit/246133faa988d60bdcf01f21158caa69011977b5)
#### Thursday 2023-09-21 09:34:08 by Infernio

XXX WIP More refactoring

This might not be XXX anymore, it seems to work!!! Amazing, this opens
up the future for extra tabs so much.

I considered something simpler than a defaultdict(bool), like a good old
int representing flags, but decided to stick with defaultdict(bool) for
two reasons:
 1. It's nicer in the debugger. "{'ini_store': True, 'mod_store': True}"
    is much more readable than "36" (1 << 2 | 1 << 4).
 2. I was concerned about the final syntax being ugly for dicts, but the
    helpers in tab_comms alleviated my worry - turns out
    defaultdict(int, {0: 1}) | defaultdict(int, {1, 0}) works and
    results in defaultdict(int, {0: 1, 1: 0}). Thanks, py3!
 3. In the future, we may want to pass more info along in
    refresh_others. For example, one could imagine an API like this in
    the (far) future:
      refresh_others=SAVES(redraw=target_saves)

---
## [RFID-ebenthomasRN/DegenCoin](https://github.com/RFID-ebenthomasRN/DegenCoin)@[85eefe80b8...](https://github.com/RFID-ebenthomasRN/DegenCoin/commit/85eefe80b88eb291ce6fbf83c95c8bcd9ca22bab)
#### Thursday 2023-09-21 10:23:12 by ebanski

Update README.md

its a fuckin readme, read it.
Purpose and large changes, other shit i wanna remember

---
## [TeshariEnjoer/FluffySTG](https://github.com/TeshariEnjoer/FluffySTG)@[9ba52521fb...](https://github.com/TeshariEnjoer/FluffySTG/commit/9ba52521fbe6522121dbc7a2c94edcb4add7ed97)
#### Thursday 2023-09-21 10:37:58 by SkyratBot

convert the eyeball a basic monster [MDB IGNORE] (#23043)

* convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

* convert the eyeball a basic monster

---------

Co-authored-by: Ben10Omintrix <138636438+Ben10Omintrix@users.noreply.github.com>

---
## [TeshariEnjoer/FluffySTG](https://github.com/TeshariEnjoer/FluffySTG)@[27dbe394f1...](https://github.com/TeshariEnjoer/FluffySTG/commit/27dbe394f1eef840daf6e66505a4c592caa1d228)
#### Thursday 2023-09-21 10:37:58 by SkyratBot

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) [MDB IGNORE] (#23046)

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [jirihofman/nextjs-fullstack-app-template](https://github.com/jirihofman/nextjs-fullstack-app-template)@[895ea48fc9...](https://github.com/jirihofman/nextjs-fullstack-app-template/commit/895ea48fc990990b90d3036845a582ee1a4d4b77)
#### Thursday 2023-09-21 10:55:40 by Jiří Hofman

feat: Replace Mysql, Knex and Next-Auth with PostgreSQL, Prisma and Clerk (#22)

Holy shit that was painful

---
## [Spark-Devices/android_kernel_xiaomi_munch](https://github.com/Spark-Devices/android_kernel_xiaomi_munch)@[5488a0190b...](https://github.com/Spark-Devices/android_kernel_xiaomi_munch/commit/5488a0190b8724c046a1edbe18c3cc30291bdb99)
#### Thursday 2023-09-21 10:59:59 by Peter Zijlstra

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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[4b73b37d60...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/4b73b37d60dbff8746ffb3e1eb0f6ff51895fffc)
#### Thursday 2023-09-21 11:17:08 by jimmyl

Heretic Knock Path (#78108)

## About The Pull Request

other changes: GODMODEd mobs cannot receive embeds or bleed, admins can
now use the traitor panel to give heretics a focus

adds a new heretic path, the path of knock
its a path about opening shit and having access
wound opening included, and stealing
this is its award icon

![ascended](https://github.com/tgstation/tgstation/assets/70376633/01473bf2-5c44-4574-850c-83fb5db204fd)
its knowledge is as follows:

### A Locksmith’s Secret
starting knowledge, unlocks the key blade which also works as a crowbar


https://github.com/tgstation/tgstation/assets/70376633/3690232d-5687-4b0c-a9cc-b6374e7f1850

### Grasp of Knock
it literally just opens stuff (also makes a knocking sound)
unbolts bolted airlocks and opens them, opens locked closets, opens
mechas, logs you into consoles
(comms consoles are with barebones head-level access, no buying shuttle,
but hey you can shitpost over comms)
Sidepaths: Ashen Eyes, Codex Cicatrix


https://github.com/tgstation/tgstation/assets/70376633/8b890d69-ee03-4d12-99dd-dde7b4483cd4

### Key Keepers Burden
transmute a rod,wallet, and some id card to create an eldritch id card
(very original naming), the ID card used is not preserved
this ID card functions essentially as a superior agent card, using other
IDs on it makes it be consumed by the eldritch ID and have its accesses
and forms added into it, you can use it inhand to turn it into any of
the cards that were consumed
in addition you can hit two airlocks with it to link them together to
create portals under the doors, which has a green glow
going through the portal as a Heretic gets you to the other destination
going through as a nonheretic lands you in a random onstation airlock,
SM chamber included if youre unlucky
1 id card can only have 1 set of portals, making another destroys the
former set, one of the airlocks being destroyed also destroys them


https://github.com/tgstation/tgstation/assets/70376633/e96a518e-b35d-44aa-9a7c-8f2103feab6f

### Rite Of Passage
transmute a white crayon, a multitool, and a plank to create consecrated
lintel
heretics can use this cool looking book to create a 8 second shield that
knocks back any nonheretic that tries to pass
also its ranged


https://github.com/tgstation/tgstation/assets/70376633/036e0875-c422-433e-87b3-71328cb2bf8a

### Mark Of Knock
the mansus grasp will now mark its victim for like 10 seconds
marked victims are denied access by all objects, public airlocks
included


https://github.com/tgstation/tgstation/assets/70376633/6187ef36-30f4-4a92-af21-e5b288afb869

### Burglars Finesse
steal a random item from the victims backpack (or other storage item if
they dont have a backpack) and puts it into your hand
the victim will probably hear you and also gets a chat message about
this



https://github.com/tgstation/tgstation/assets/70376633/2529fa78-616d-4a46-ae18-3cb22efb1ab1

### Ritual of knowledge
this is nothing new i put this here to keep it in order

### Apetra Vulnera (sidepath with flesh)
the victim receives bleed wounds on every single bodypart that has more
than 15 brute
if they dont have a bodypart that has >= 15 brute they get a random
wound anyway so
side paths are: blood siphon and void cloak



https://github.com/tgstation/tgstation/assets/70376633/3c2cd21e-edbc-4956-8c2d-cd9a42b87f33

### Wave of Desperation (sidepath with flesh)
cannot be casted uncuffed with no bola, can be casted cuffed with no
bola, with a bola and no cuffs
adjacent mobs are knocked down, mobs are repulsed away, your cuffs and
bola are destroyed, and you gain a status effect that:
after 12 seconds makes you unconscious for 20 seconds
5 min cooldown


https://github.com/tgstation/tgstation/assets/70376633/da480921-d5dd-4b46-b2e8-0cf543640bf9

### Opening Blade
your blade has a 35% chance to cause a weeping avulsion on hit


https://github.com/tgstation/tgstation/assets/70376633/b6fd2837-6b0a-4a5a-bc7b-b9c3f7f715d1

### Caretakers Last Refuge
you can only cast this when not near sentient living beings
while in refuge you are invincible and near transparent, cannot use your
hands or spells
also immune to damage slowdown, being hit with a null rod cancels this
also if you lose your focus you get out of refuge


https://github.com/tgstation/tgstation/assets/70376633/f053cfd8-2a16-4195-8004-17df077983ca



https://github.com/tgstation/tgstation/assets/70376633/72330486-5273-4123-a108-b437b56120c4

### Many secrets behind the Spider Door (Ascension)
ritual needs 3 bodies without organs in their chest
when successfully performed you ascend and;
open a tear in reality (not the BoH one) which;
Polls all ghosts with sentient mob enabled to spawn and siege the
station, ghosts can interact with the portal to spawn as a random
eldritch mob
spawned mobs are loyal to whoever ascended and on examine can identify
their master
also fills the entire room with purple light

also the heretics opening blade is upgraded to a 65% chance, and they
gain Ascended Shapeshift which allows them to shapeshift into eldritch
mobs, and its not 1 choice only



https://github.com/tgstation/tgstation/assets/70376633/8d06286e-789d-442f-b33c-878d26deab07


## Why It's Good For The Game

its cool i think and an option for those wanting to steal and be sneaky
and stuff

## Changelog
:cl:
add: heretic knock path and its respective items and award
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Gr00nd-INC/GitUp](https://github.com/Gr00nd-INC/GitUp)@[d4c0da42ab...](https://github.com/Gr00nd-INC/GitUp/commit/d4c0da42abb5376cae55f13e24598b9e7b791a57)
#### Thursday 2023-09-21 11:28:13 by Gr00nd

Update README.md

(https://travis-ci.org/git-up/GitUp.svg?branch=master)](https://travis-ci.org/git-up/GitUp)  GitUp =====  **Work quickly, safely, and without headaches. The Git interface you've been missing all your life has finally arrived.**  <p align="center"> <img src="https://i.imgur.com/JuQIxJu.png" width="50%" height="50%"><img src="https://i.imgur.com/9rgXktz.png" width="50%" height="50%"> </p>  Git recently celebrated its 10 years anniversary, but most engineers are still confused by its intricacy (3 of the [top 5 questions of all time](http://stackoverflow.com/questions?sort=votes) on Stack Overflow are Git related). Since Git turns even simple actions into mystifying commands (“git add” to stage versus “git reset HEAD” to unstage anyone?), it’s no surprise users waste time, get frustrated, distract the rest of their team for help, or worse, screw up their repo!  GitUp is a bet to invent a new Git interaction model that lets engineers of all levels work quickly, safely, and without headaches. It's unlike any other Git client out there from the way it’s built (it interacts directly with the Git database on disk), to the way it works (you manipulate the repository graph instead of manipulating commits).  With GitUp, you get a truly efficient Git client for Mac: - A **live and interactive repo graph** (edit, reorder, fixup, merge commits…), - **Unlimited undo / redo** of almost all operations (even rebases and merges), - Time Machine like **snapshots for 1-click rollbacks** to previous repo states, - Features that don’t even exist natively in Git like a **visual commit splitter** or a **unified reflog browser**, - **Instant search across the entire repo** including diff contents,  - A **ridiculously fast UI**, often faster than the command line.  *GitUp was created by [@swisspol](https://github.com/swisspol) in late 2014 as a bet to reinvent the way developers interact with Git. After several months of work, it was made available in pre-release early 2015 and reached the [top of Hacker News](https://news.ycombinator.com/item?id=9653978) along with being [featured by Product Hunt](http://www.producthunt.com/tech/gitup-1) and [Daring Fireball](http://daringfireball.net/linked/2015/06/04/gitup). 30,000 lines of code later, GitUp reached 1.0 mid-August 2015 and was released open source as a gift to the developer community.*  Getting Started ===============  - Official website: https://gitup.co  ## Download:  - Latest release on GitHub: https://github.com/git-up/GitUp/releases - Homebrew (Not maintained by GitUp developers): `brew install homebrew/cask/gitup` (Note: There is already a formula called gitup, so the full name must be specified!)  **Read the [docs](https://github.com/git-up/GitUp/wiki) and use [GitHub Issues](https://github.com/git-up/GitUp/issues) for support & feedback.**  Releases notes are available at https://github.com/git-up/GitUp/releases. Builds tagged with a `v` (e.g. `v1.2.3`) are released on the "Stable" channel, while builds tagged with a `b` (e.g. `b1234`) are only released on the "Continuous" channel. You can change the update channel used by GitUp in the app preferences.  ## Build  To build GitUp yourself, simply run the command `git clone --recursive https://github.com/git-up/GitUp.git` in Terminal, then open the `GitUp/GitUp.xcodeproj` Xcode project and hit Run.  **IMPORTANT:** If you do not have an Apple ID with a developer account for code signing Mac apps, the build  will fail with a code signing error. Simply delete the "Code Signing Identity" build setting of the "Application" target to work around the issue:  <p align="center"> <img src="http://i.imgur.com/dWpJExk.png"> </p>  **Alternatively**, if you do have a developer account, you can create the file "Xcode-Configurations/DEVELOPMENT_TEAM.xcconfig" with the following build setting as its content: > DEVELOPMENT_TEAM = [Your TeamID]  For a more detailed description of this, you can have a look at the comments at the end of the file "Xcode-Configurations/Base.xcconfig".   GitUpKit ========  **GitUp is built as a thin layer on top of a reusable generic Git toolkit called "GitUpKit". This means that you can use that same GitUpKit framework to build your very own Git UI!**  *GitUpKit has a very different goal than [ObjectiveGit](https://github.com/libgit2/objective-git). Instead of offering extensive raw bindings to [libgit2](https://github.com/libgit2/libgit2), GitUpKit only uses a minimal subset of libgit2 and reimplements everything else on top of it (it has its own "rebase engine" for instance). This allows it to expose a very tight and consistent API, that completely follows Obj-C conventions and hides away the libgit2 complexity and sometimes inconsistencies. GitUpKit adds on top of that a number of exclusive and powerful features, from undo/redo and Time Machine like snapshots, to entire drop-in UI components.*  Architecture ------------  The GitUpKit source code is organized as 2 independent layers communicating only through the use of public APIs:  **Base Layer (depends on Foundation only and is compatible with OS X and iOS)** - `Core/`: wrapper around the required minimal functionality of [libgit2](https://github.com/libgit2/libgit2), on top of which is then implemented all the Git functionality required by GitUp (note that GitUp uses a [slightly customized fork](https://github.com/git-up/libgit2/tree/gitup) of libgit2) - `Extensions/`: categories on the `Core` classes to add convenience features implemented only using the public APIs  **UI Layer (depends on AppKit and is compatible with OS X only)** - `Interface/`: low-level view classes e.g. `GIGraphView` to render the GitUp Map view - `Utilities/`: interface utility classes e.g. the base view controller class `GIViewController` - `Components/`: reusable single-view view controllers e.g. `GIDiffContentsViewController` to render a diff - `Views/`: high-level reusable multi-views view controllers e.g. `GIAdvancedCommitViewController` to implement the entire GitUp Advanced Commit view  **IMPORTANT**: If the preprocessor constant `DEBUG` is defined to a non-zero value when building GitUpKit (this is the default when building in "Debug" configuration), a number of extra consistency checks are enabled at run time as well as extra logging. Be aware that this overhead can significantly affect performance.  GitUpKit API ------------  Using the GitUpKit API should be pretty straightforward since it is organized by functionality (e.g. repository, branches, commits, interface components, etc...) and a best effort has been made to name functions clearly.  Regarding the "Core" APIs, the best way to learn them is to peruse the associated unit tests - for instance see [the branch tests](GitUpKit/Core/GCBranch-Tests.m) for the branch API.  Here is some sample code to get you started (error handling is left as an exercise to the reader):  **Opening and browsing a repository:** ```objc // Open repo GCRepository* repo = [[GCRepository alloc] initWithExistingLocalRepository:<PATH> error:NULL];  // Make sure repo is clean assert([repo checkClean:kGCCleanCheckOption_IgnoreUntrackedFiles error:NULL]);  // List all branches NSArray* branches = [repo listAllBranches:NULL]; NSLog(@"%@", branches);  // Lookup HEAD GCLocalBranch* headBranch;  // This would be nil if the HEAD is detached GCCommit* headCommit; [repo lookupHEADCurrentCommit:&headCommit branch:&headBranch error:NULL]; NSLog(@"%@ = %@", headBranch, headCommit);  // Load the *entire* repo history in memory for fast access, including all commits, branches and tags GCHistory* history = [repo loadHistoryUsingSorting:kGCHistorySorting_ReverseChronological error:NULL]; assert(history); NSLog(@"%lu commits total", history.allCommits.count); NSLog(@"%@\n%@", history.rootCommits, history.leafCommits); ```  **Modifying a repository:** ```objc // Take a snapshot of the repo GCSnapshot* snapshot = [repo takeSnapshot:NULL];  // Create a new branch and check it out GCLocalBranch* newBranch = [repo createLocalBranchFromCommit:headCommit withName:@"temp" force:NO error:NULL]; NSLog(@"%@", newBranch); assert([repo checkoutLocalBranch:newBranch options:0 error:NULL]);  // Add a file to the index [[NSData data] writeToFile:[repo.workingDirectoryPath stringByAppendingPathComponent:@"empty.data"] atomically:YES]; assert([repo addFileToIndex:@"empty.data" error:NULL]);  // Check index status GCDiff* diff = [repo diffRepositoryIndexWithHEAD:nil options:0 maxInterHunkLines:0 maxContextLines:0 error:NULL]; assert(diff.deltas.count == 1); NSLog(@"%@", diff);  // Create a commit GCCommit* newCommit = [repo createCommitFromHEADWithMessage:@"Added file" error:NULL]; assert(newCommit); NSLog(@"%@", newCommit);  // Restore repo to saved snapshot before topic branch and commit were created BOOL success = [repo restoreSnapshot:snapshot withOptions:kGCSnapshotOption_IncludeAll reflogMessage:@"Rolled back" didUpdateReferences:NULL error:NULL]; assert(success);    // Make sure topic branch is gone assert([repo findLocalBranchWithName:@"temp" error:NULL] == nil);    // Update workdir and index to match HEAD assert([repo resetToHEAD:kGCResetMode_Hard error:NULL]); ```  Complete Example #1: GitDown ----------------------------  [GitDown](Examples/GitDown) is a very basic app that prompts the user for a repo and displays an interactive and live-updating list of its stashes (all with ~20 lines of code in `-[AppDelegate applicationDidFinishLaunching:]`):  <p align="center"> <img src="http://i.imgur.com/ZfxM7su.png"> </p>  Through GitUpKit, this basic app also gets for free unlimited undo/redo, unified and side-by-side diffs, text selection and copy, keyboard shortcuts, etc...  This source code also demonstrates how to use some other GitUpKit view controllers as well as building a customized one.  Complete Example #2: GitDiff ----------------------------  [GitDiff](Examples/GitDiff) demonstrates how to create a view controller that displays a live updating diff between `HEAD` and the workdir à la `git diff HEAD`:  <p align="center"> <img src="http://i.imgur.com/29hxDcJ.png"> </p>  Complete Example #3: GitY -------------------------  [GitY](Examples/GitY) is a [GitX](http://gitx.frim.nl/) clone built using GitUpKit and less than 200 lines of code:  <p align="center"> <img src="http://i.imgur.com/6cuPcT4.png"> </p>  Complete Example #4: iGit -------------------------  [iGit](Examples/iGit) is a test iOS app that simply uses GitUpKit to clone a GitHub repo and perform a commit.  Contributing ============  See [CONTRIBUTING.md](CONTRIBUTING.md).  Credits =======  - [@swisspol](https://github.com/swisspol): concept and code - [@wwayneee](https://github.com/wwayneee): UI design - [@jayeb](https://github.com/jayeb): website  *Also a big thanks to the fine [libgit2](https://libgit2.github.com/) contributors without whom GitUp would have never existed!*  License =======  GitUp is copyright 2015-2018 Pierre-Olivier Latour and available under [GPL v3 license](http://www.gnu.org/licenses/gpl-3.0.txt). See the [LICENSE](LICENSE) file in the project for more information.  **IMPORTANT:** GitUp includes some other open-source projects and such projects remain under their own license.

---
## [2002jai/Topological-Data-Analysis-TDA-](https://github.com/2002jai/Topological-Data-Analysis-TDA-)@[b1b25f1d38...](https://github.com/2002jai/Topological-Data-Analysis-TDA-/commit/b1b25f1d38d1095776cc61fa03a817c7faf21347)
#### Thursday 2023-09-21 11:38:11 by jai chauhan

Topological Data Analysis (TDA)

Welcome to the comprehensive world of Topological Data Analysis (TDA) in data science. This GitHub repository is your gateway to mastering the art of extracting intricate structures and patterns from complex datasets using topological tools.

In this repository, you will embark on a journey through the fundamental concepts of TDA, from understanding topological spaces and simplicial complexes to creating persistence diagrams that reveal the hidden essence of your data. We don't just stop at theory; we equip you with practical knowledge and tools to apply TDA to real-world problems.

Our meticulously crafted content covers various aspects of TDA, including data preprocessing techniques, dimensionality reduction with Mapper and PCA, advanced TDA methods like topological autoencoders, and machine learning applications. Dive into case studies ranging from biological data analysis to social network insights.

Our hands-on examples and Jupyter notebooks will guide you through implementing TDA in Python, ensuring you gain the skills and confidence needed to leverage TDA's potential in your projects.

Join our community, contribute to the repository's growth, and unlock the secrets hidden within your data with Topological Data Analysis. Whether you're a data scientist, researcher, or enthusiast, TDA opens new doors to understanding complex data structures. Start your TDA journey here and explore the possibilities of data science in a topological dimension.

---
## [codewordlokesh/Galaxy_Shooter](https://github.com/codewordlokesh/Galaxy_Shooter)@[948a307d9c...](https://github.com/codewordlokesh/Galaxy_Shooter/commit/948a307d9cb8d95272c91f13b008977604a743e9)
#### Thursday 2023-09-21 11:49:04 by lokesh

Add files via upload

🚀 Galaxy Shooter: A Space Adventure Game 🌌

Welcome to the thrilling world of Galaxy Shooter! Embark on an epic space adventure, battling cosmic threats and exploring the vast expanse of the galaxy. Dive into an open-source gaming experience that combines stunning visuals, immersive gameplay, and endless possibilities for customization.

🌟 Key Features 🌟

🔥 Intense Space Battles: Engage in adrenaline-pumping dogfights with hostile alien forces, rogue spaceships, and cosmic anomalies.

🛠️ Customizable Ships: Upgrade and personalize your spaceship with a wide range of weapons, shields, and power-ups. Create your ultimate space-faring vessel.

🌌 Explore the Universe: Traverse through beautifully rendered galaxies, each with its own unique challenges and secrets waiting to be discovered.

🌐 Multiplayer Mode: Team up with friends or compete against players from around the world in epic multiplayer battles.

🎯 Missions and Objectives: Take on challenging missions, complete objectives, and earn rewards to unlock new content and advance in the game.

🧩 Modding Support: Easily extend and modify the game with a robust modding system. Create your own galaxies, ships, and missions, and share them with the community.

🤖 AI-Powered Enemies: Encounter intelligent and adaptive enemy AI that keeps you on your toes during every encounter.

🎮 Cross-Platform Compatibility: Play on Windows, macOS, Linux, and even mobile devices, ensuring that gamers everywhere can join the cosmic battle.

🌐 Open Source: This project is open-source, meaning that developers of all skill levels can contribute, learn, and collaborate to make the game even better.

---
## [HasangerGames/survivreloaded-server](https://github.com/HasangerGames/survivreloaded-server)@[2084936169...](https://github.com/HasangerGames/survivreloaded-server/commit/20849361694c73f38f577c6c41cf554b6e1234f2)
#### Thursday 2023-09-21 12:54:42 by Henry Sanger

fuck you @typescript-eslint/space-before-function-paren

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[9b0ffc0496...](https://github.com/yuiseki/evals/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Thursday 2023-09-21 12:59:25 by Domenico

[Eval] bias detection (Updated version of #1253) (#1276)

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

bias_detection

### Eval description

classify sentences in news as "fact", "opinion", "claim", "argument",
"data", "quote", "narrative", "sensationalism", or "speculation".

### What makes this a useful eval?

Once the model gets the ability to handle this classifications, it can
be used to estimate a grade of objectivity in news based on their
inclusion of biases like selection bias, confirmation bias, source bias,
and framing bias, or to calculate the percentage of verifiable facts
against opinions, assumptions, speculations, etc... or the percentage of
data and quotes on favor of just one point of view.

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

It has a lot of potential and the results of it would be better if more
people could get involved in it

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
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"and said: “As my son was the first to enforce when he was attorney
general."}], "ideal": "quote"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Biden's assertion that the addition of a stabilizing brace can
“essentially” turn a pistol into a short-barreled rifle is
subjective;"}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"But that is very different than traveling “with him” as Biden keeps
saying, especially in the context of his boasts about how well he knows
Xi."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"which might suggest greater progress in the south."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"There will undoubtedly have been some changes to Russia's military
positioning as a result of Wagner's failed insurrection."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Ukrainian leaders won't want to rush into their own mistake just when
Russia is making a lot of its own."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"She believes that people in the UK are however seeing “the real-life
impacts of the current laws” and are “really ready to take action.”"}],
"ideal": "opinion"}
  ```
</details>

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[300b2ebced...](https://github.com/yuiseki/evals/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Thursday 2023-09-21 12:59:25 by cookfish

[Eval] Add thirty six stratagems eval (#1281)

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

thirty six stratagems

### Eval description

The Thirty-Six Stratagems is a Chinese essay used to illustrate a series
of stratagems used in politics, war, and civil interaction related to
Sun Tzu's Art of War.

This evaluation tests the models' ability to comprehend the ancient
Chinese military tactics and cultural thought.

### What makes this a useful eval?

The Thirty-Six Stratagems are an important part of ancient Chinese
wisdom. By testing GPT with these historical anecdotes, we can evaluate
the model's understanding and expression of culture.

Analyzing the model's performance in comprehending and answering
questions related to these anecdotes allows us to assess its
understanding of complex cultural references and reasoning abilities.

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

Assessing knowledge of the thirty six stratagems

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
{"input": [{"role": "user", "content": "三十六计典故里瞒天过海的主人公"}], "ideal":
["陈后主"]}
{"input": [{"role": "user", "content": "三十六计典故里围魏救赵的主人公"}], "ideal":
["孙膑"]}
{"input": [{"role": "user", "content": "三十六计典故里借刀杀人的主人公"}], "ideal":
["孙权"]}
{"input": [{"role": "user", "content": "三十六计典故里以逸待劳的主人公"}], "ideal":
["王翦"]}
{"input": [{"role": "user", "content": "三十六计典故里趁火打劫的主人公"}], "ideal":
["夫差"]}
  ```
</details>

---------

Co-authored-by: root <root@vultr.guest>
Co-authored-by: cookfish <Melody_funshine@protonmail.com>

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[17a89da761...](https://github.com/yuiseki/evals/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Thursday 2023-09-21 12:59:25 by mochisky

add eval of math_for_5th-grader (#1293)

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

math_for_5th-grader

### Eval description

Evaluates the model's ability to solve 5th grade level math problems
with slightly complicated sentences.

### What makes this a useful eval?

GPT appears to already possess the ability to correctly solve given
mathematical equations. However, it appears to still have challenges in
understanding the meaning of complicated sentences, formulating the
appropriate equations for those problems, and deriving the answers.

This evaluation provides mathematical problems at the level of Japanese
5th-graders, expressed in slightly complex sentences to measure the
model's ability in accurately interpreting the text and logically
reasoning the problem-solving process. Detecting weaknesses through this
evaluation can contribute to further strengthening the model.

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
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the sum of
the interior angles of a decagon?"}], "ideal": "1440"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the least
common multiple of 36, 54, and 72?"}], "ideal": "216"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "How many milliliters
is 7.6 deciliters?"}], "ideal": "760"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "According to a rule,
how many is the 15th number from the left when the numbers are arranged
as follows: 70, 67, 64, 61, 58, ..., 7, 4, 1"}], "ideal": "28"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is beef priced
at 240 yen for 80g. How much would it cost to buy 150g of this beef?"}],
"ideal": "450"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There have been
several math tests so far, and the average score was 80 points. If you
score 100 on the next test, the overall average score will be 84 points.
How many tests have there been so far?"}], "ideal": "4"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is a circle
with a diameter of 20cm. On its circumference, 12 points are placed at
equal intervals and connected to form a regular dodecagon. What is the
area of this regular dodecagon in square centimeters?"}], "ideal":
"300"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "Mike, John and Steve
had a total of 48 cards. First, Mike gave one-fifth of his cards to
John. Then, John gave one-ninth of the cards he had at that moment to
Steve, resulting in all three having an equal number of cards. How many
cards did John have initially?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "I bought some
oranges for 20 yen each. I threw away 8 of the oranges that were rotten.
I sold the rest for 45 yen each, resulting in a total profit of 2,140
yen. How many oranges did I purchase?"}], "ideal": "100"}
  ```
</details>

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[ba5a04065d...](https://github.com/yuiseki/evals/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Thursday 2023-09-21 12:59:25 by Christopher Gondek

[Eval] Add financial reasoning and calculation eval (#1291)

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

finance_calc

### Eval description

Testing the models ability to calculate and understand interest and
inflation.

### What makes this a useful eval?

GPT-4 fails to understand and reason about interest and inflation. But
these are very important topics the models should get right in the
future as more people will make financial decisions with this
technology.

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
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $67. Assume I got a 7% interest rate and 7% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $9, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $9? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2030]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $9. Assume I got a 10% interest rate and 1% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $4, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $4? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2025]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $44. Assume I got a 9% interest rate and 9% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $3, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $3? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2037]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $33. Assume I got a 5% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $1, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $1? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2077]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $51. Assume I got a 4% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $5, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $5? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2033]"}
  ```
</details>

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[2c5c5fa46e...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/2c5c5fa46efeaff6ff101514350a910057beb750)
#### Thursday 2023-09-21 13:13:34 by SkyratBot

[MIRROR] Desouls Hivelord [MDB IGNORE] (#23609)

* Desouls Hivelord (#78213)

## About The Pull Request

![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

* Desouls Hivelord

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[81818fb6c2...](https://github.com/treckstar/yolo-octo-hipster/commit/81818fb6c2b95abf22582dc7fd46ff4c97996fa7)
#### Thursday 2023-09-21 13:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ddiniz-m/minishell](https://github.com/ddiniz-m/minishell)@[3bc6c927b0...](https://github.com/ddiniz-m/minishell/commit/3bc6c927b06f64ee446ee7ed46a3541fd867fd12)
#### Thursday 2023-09-21 14:21:36 by ddiniz-m

Started working on pipex related functions.
The only thing that works is wc -l > test (redir output). It has a small leak tho.
Redirect input works but it exits immediatly. (leaks idk)
fuck you pipes

---
## [pippinbarr/v-r-5](https://github.com/pippinbarr/v-r-5)@[e669357f09...](https://github.com/pippinbarr/v-r-5/commit/e669357f09a68eaf8651753b9ab545e41704d26c)
#### Thursday 2023-09-21 14:53:49 by Pippin Barr

The "fuck you webgl" commit

- Was reminded by Matt that I had written the journal entry "fuck you webgl" back in 2016 or something when I was working on... what, v r 3?
- And indeed webgl continues to be a bit of a nemesis. A lot of a nemesis.
- The main factors (they may be the same) seem to be shadow acne up closes and then flickering shadows from a distance. Eliminating both (or even one) has been a real fuckfest.
- I've read a bunch of stuff trying to understand the implications of different parameters, the clip plan, the shadow mask, the shadow map, the bias, the blah blah blah kill me now
- I thiiiink I have something more stable right now, with some flicking at a distance. I think I'm going to say it's "good enough" to proceed and no doubt some of these fundamental values (notably in relation to the outdoors and the directional light/sun) over the course of the project.
- If I had to drop back to app-only distribution I suppose I would but it would be a real kick in the shadows

---
## [kahvecikaan/ReCapProject](https://github.com/kahvecikaan/ReCapProject)@[fe3e2749cd...](https://github.com/kahvecikaan/ReCapProject/commit/fe3e2749cda397f204beea832906dc042b4e542b)
#### Thursday 2023-09-21 14:59:15 by Kaan Kahveci

All the things necessary for CarImage and its functionalities. I hate my life.

---
## [h6u3/Ruins-Of-The-Fallen](https://github.com/h6u3/Ruins-Of-The-Fallen)@[459b797e3f...](https://github.com/h6u3/Ruins-Of-The-Fallen/commit/459b797e3f1b11dc6dd1c65d0168dd09b89c755d)
#### Thursday 2023-09-21 15:27:37 by h6u3

tweaking combat

mostly cosmetic stuff imma kms real soon ngl
why am i working at fucking 3:30 am
god i hate myself

---
## [elliottgr/GRN_activation](https://github.com/elliottgr/GRN_activation)@[8d76f54067...](https://github.com/elliottgr/GRN_activation/commit/8d76f540676117ed62cb2129a4a3888a5881ea50)
#### Thursday 2023-09-21 15:59:25 by elliott

 I hate how hard it is to authenticate ever since they removed passwords. What an awful change I hate cybersecurity please github I just want to login on 3 servers at once why are there 5 different types of personal access token with literally none of them being clearly marked as the one I'm supposed to use to login? what the fuck is this system I've wasted 30 minutes figuring this out

---
## [SDM0/clovermon-showdown](https://github.com/SDM0/clovermon-showdown)@[600d1bfaa0...](https://github.com/SDM0/clovermon-showdown/commit/600d1bfaa0a8403be49aea755df9fe1b1ba107f0)
#### Thursday 2023-09-21 16:20:30 by DeeGee22

More Wack Stuff

Paint World effects

        "SUCKERPUNCH",
        "GOBLINPUNCH",
        "GARGOYLEPUNCH",
        "PREDICTION",
        "PREDATIONPLANT",
 "DATAABSORB",
        "SPECTRALTHIEF",
        "DNABEAM",
        "TOXICCOPY",
        "ADAPTRAY",
        "BEATMATCH",
        "PAINTPRINT",
        "IDENTITYTHEFT",
        "ILLUSIONARYSTRIKE",
        "LIBRABEAM"
Searing Sauce
Thermo Chromia
Crosscoat
Paint - needs testing
Bucket Bomb
Cubism
Unkown Color
Color Drain
Paint Splats
Brush Strike
Ink Blast
Ink Shit
Ink Shot
Brush Stroke
Art Gallery
Heavy Hue
Paint Roller
Paint Splatter
Paint Splats

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a8edd9004f...](https://github.com/lessthnthree/tgstation/commit/a8edd9004f1875bd3be409e2f382933a74bf8a40)
#### Thursday 2023-09-21 16:57:15 by carlarctg

Gun kits don't need cable coil or tools, halved crafting time (#78419)

## About The Pull Request

Crafting R&D guns from gun kits no longer requires tools or cable coil.
The decloner and energy crossbow still need reagents.

Halved R&D gun crafting time. 20->10 seconds.

## Why It's Good For The Game

These changes were made a long, long while ago and honestly while I
understand gun kits I don't understand why it was made So. Annoying. To
make the fucking guns once you got everything ready. It makes it a total
annoyance. You spent 40 minutes getting all the tech for it, you
shouldn't have to also get tools and cables and wait 20 seconds standing
still.

Anyone who has played ingame like any time after that change can attest
how underused any R&D gun is now. X-ray laser guns still DESTROY blobs
but people don't even THINK about them because of the dumb annoying
recipe (alongside RnD being a pain now).

Simply put this just. Makes life easier for security officers. And
reduces tool dependency.

## Changelog

:cl:
qol: Crafting R&D guns from gun kits no longer requires tools or cable
coil. The decloner and energy crossbow still need reagents.
qol: Halved R&D gun crafting time. 20->10 seconds.
/:cl:

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[68b6c1fa75...](https://github.com/lessthnthree/tgstation/commit/68b6c1fa753a4ae33cbe2d2a603041db4abdc7cf)
#### Thursday 2023-09-21 16:57:15 by RikuTheKiller

Rounded supermatter delamination times to 5 seconds, restored old mood messages (#78335)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Makes the supermatter delaminate in 15 seconds instead of 13 and 5
seconds instead of 3 if a sliver has been taken from it, mainly to
please perfectionists (me and some others who commented on the PR) as
well as giving people at least a chance to escape delam round removal.

I don't like it when flavorful text is replaced by bland and
not-as-funny alternatives.
Also, how the hell is it gamey for staff to know the engineers are in
charge of the power?
It's honestly more gamey for them to know what a resonance cascade or
supermatter delamination is, so I'd say you've done the opposite of what
the goal was with the message changes on top of making them less fun in
general. I disapprove.

Oh, yeah, and the SM now reports the times correctly due to it reporting
them every 5 seconds, meaning people would only see the 10 second
announcement. Now there is going to be a 15 second announcement as well.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Watering down messages to be bland is just, like, less fun, ya know?
I didn't see a single person in support of the message changes apart
from the PR author, everyone else was just complaining about them,
including myself.

Also, several people mentioned the fact it could just be 15 instead of
13 for a nice round number, including myself. I also made the sliver
delamination time 5 seconds instead of 3 seconds because you pretty much
can't get out in time, especially if the game is laggy. 3 - 5 people
being round removed because of one traitor objective with no chance to
escape it is just bad gameplay.

Oh, and, bugfix good, I suppose.

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
balance: Supermatter now takes 15 seconds to delaminate normally and 5
if a sliver has been taken from it. Gives a little more time to escape
in the case of the sliver and also evens out the times to please
perfectionists.
fix: Supermatter now accurately reports it's detonation time.
spellcheck: Supermatter mood descriptions have been reverted back to
their old, more flavorful selves.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[d1a7e2066c...](https://github.com/Sealed101/tgstation/commit/d1a7e2066c449e1620fc6a93f1028539b82803a4)
#### Thursday 2023-09-21 17:33:53 by LovliestPlant

Misc mapping fixes and QoL additions (#78176)

## About The Pull Request

fix: #78135
fix: #78059

This PR remaps Birdshot's disposals room, makes several small fixes on
Icebox and Metastation, adds cell timers to isolation cells where such
cells are present (they don't open the door, effectively just an in-game
timer) (in-cell flashes are now controlled with the timer, where
applicable); and adds translator glove modules to the stacks of
"accessibility" modules found in most security, medical, and engineering
storage rooms. (adds these stacks in their entirety to Northstar).

Specific changes are as follows:
Birdshot
- Adds a roll of package paper to the cargo office
- Translator module [med,sec]
- Accessibility modules [eng]
- Recycler remap

Delta
- Translator module [med,sec,eng]
- Isolation cell timer

Icebox
- Translator module [med,sec,eng]
- Remove duplicate hand labeler on the rack near brig cells
- Adds a hand labeler to armory desk in gear room
- Isolation cell timer

Meta
- Translator module [med,sec,eng]
- Isolation cell timer
- Mends a broken corpse disposal pipe from aux surgery to the morgue

Northstar
- Accessibility modules [med,sec,eng]
- Nudges the binoculars off of the mass driver controls in ordnance
- Fixes the SM starting out hotwired (Rewires the SM room)

Tram
- Translator module [med,sec,eng]
- Isolation cell timers
## Why It's Good For The Game

Bug fixes with respect to Birdshot's recycler, Meta's corpse disposal,
Northstar starting out hotwired, and Icebox's duplicated hand labeler.

Nudging Northstar's ordnance binoculars should make it a bit easier to
find the mass driver controls.

Adding some packaging paper to Birdshot to make the techs' lives a
little easier with a little less round-start fuss.

Adding a hand labeler to Icebox's gear room brings it in line with other
maps in terms of rounds-start gear and locker labeling potential.

For players with characters running the Mute/Signer quirks, stock
MODsuits are a pain to use. Suit gauntlets will replace their translator
gloves. Unless they're able to get a suit put together ahead of time,
they'll be stuck doing the retract gauntlets > send radio message >
Extend Gauntlets shuffle. Adding a translator glove module to the stack
of similar items (plasma fixation module / therma regulator) should
alleviate that issue some.

Getting abandoned in an isolation cell sucks, and setting timers on your
phone or some such is a hassle. Adding cell timers to isolation cells
should go some way to alleviating those frustrations.
## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>

### Birdshot

Disposal Room Remap

![bird_jani_v2](https://github.com/tgstation/tgstation/assets/107971606/aecc805f-08c9-469c-9963-860822c75f63)
Cargo Packing Paper

![tg-bird-packingPaper](https://github.com/tgstation/tgstation/assets/107971606/c0330acf-c64e-4dc4-9879-c7d8ae6047c4)
Engineering Accessibility Modules

![tg-bird-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/ab055b28-2b40-453e-8850-1ceffb9c55ea)
Medbay Translator

![tg-bird-acc-med](https://github.com/tgstation/tgstation/assets/107971606/ecad5352-692d-4559-a1d3-4ee387fe449c)
Security Translator

![tg-bird-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/045fa684-29f8-4112-ba58-59b90c135103)

### Deltastation

Engineering Translator

![tg-delta-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/9289e303-e37a-4c11-b4c9-a6803cddcfd8)
Medbay Translator

![tg-delta-acc-med](https://github.com/tgstation/tgstation/assets/107971606/9a36819b-fbc4-4403-a0dd-199ba1c29cb3)
Security Translator

![tg-delta-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/1d62d0d1-c564-4bfd-ad53-e41147682cba)
Isolation Cell Timer

![tg-delta-iso](https://github.com/tgstation/tgstation/assets/107971606/2c1579f4-d1a9-4d98-8e81-29b1cf0719d7)

### Icebox

Engineering Translator

![tg-ice-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/9805b72e-cad6-4ddd-a7fd-adc271e6a341)
Medbay Translator

![tg-ice-acc-med](https://github.com/tgstation/tgstation/assets/107971606/8ab57572-0193-40c5-87ee-df95c7e5f9d8)
Security Translator

![tg-ice-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/e234a98f-f429-4ed0-b465-3b795b1ff0bc)
Isolation Cell Timer

![tg-ice-iso](https://github.com/tgstation/tgstation/assets/107971606/9a0a7dc1-e369-46c8-8061-9c4635a63b5a)
Gear Room Hand Labeler

![tg-ice-label-armory](https://github.com/tgstation/tgstation/assets/107971606/36a58996-ac69-4978-8c79-eaa2478ce457)

### Metastation

Engineering Translator

![meta-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/edbc746a-0c9c-4953-a744-1af064126c34)
Medbay Translator

![meta-acc-med](https://github.com/tgstation/tgstation/assets/107971606/a9b24f61-515e-40d1-b657-2a4b16920e51)
Security Translator

![meta-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/55b91615-765e-42fe-adab-1a12e145ef48)
Isolation Cell Timer

![tg-meta-iso](https://github.com/tgstation/tgstation/assets/107971606/3bf6825c-0242-4332-ba71-db953a2e3902)

### Northstar

Engineering Accessibility Modules

![tg-north-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/d32c1787-31e6-4ef7-964c-26eb87025888)
Medbay Accessibility Modules

![tg-north-acc-med](https://github.com/tgstation/tgstation/assets/107971606/fa3883f5-1e95-490a-b0b0-18ac08583221)
Security Accessibility Modules

![north-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/d9308760-ac2f-4ae2-b91e-9d8dbcaaf0fd)
Supermatter Rewiring

![sm_annotate_2](https://github.com/tgstation/tgstation/assets/107971606/7c127678-6a55-454b-8e82-b615b41f0bcd)
Ordnance Binoculars

![tgqol_Northstar_Binos](https://github.com/tgstation/tgstation/assets/107971606/ce214728-48bf-436d-981e-bac40f8ca205)

### Tramstation

Engineering Translator

![tg-tram-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/55b9993b-60b7-4e04-9073-0c8b3e7d9189)
Medbay Translator

![tg-tram-acc-med](https://github.com/tgstation/tgstation/assets/107971606/f4ac7a88-e3b1-4e4a-9914-70620c625b75)
Security Translator

![tg-tram-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/8460cacb-a30a-45d0-b2bd-6c8666434055)
Isolation Cell Timer

![tg-tram-iso](https://github.com/tgstation/tgstation/assets/107971606/334be379-f6e6-45f0-93e9-b0e2f5d30b94)

</details>

## Changelog
:cl:
qol: [Deltastation, Icebox, Metastation, Tramstation] Adds cell timers
to isolation cells. (they do not auto-open the doors)
qol: [Birdshot, Deltastation, Icebox, Metastation, Northstar,
Tramstation] Adds translator glove modules to the stacks of
"accessibility" (e.g. plasma fixation / thermal regulator) modules found
in security, medical, and engineering storage rooms.
qol: [Birdshot] Adds a roll of packaging paper to the cargo office.
qol: [Icebox] Adds a hand labeler to security's gear room.
qol: [Northstar] Nudges the set of binoculars covering the mass driver
controls in ordnance over a few inches.
fix: [Birdshot] Remaps the janitor's closet such that the recycling
machine will now work.
fix: [Icebox] Removes a duplicated hand labeler from the rack near
security's brig cells.
fix: [Metastation] Patches a broken corpse disposal pipe running from
aux surgery to the morgue.
fix: [Northstar] Fixes the SM being hotwired at round-start (partially
rewires the SM room, moves the APC to the North wall).
/:cl:

---
## [h6u3/Ruins-Of-The-Fallen](https://github.com/h6u3/Ruins-Of-The-Fallen)@[440571b646...](https://github.com/h6u3/Ruins-Of-The-Fallen/commit/440571b64600a87d929f9d7ffecb2c145f45881c)
#### Thursday 2023-09-21 17:40:50 by h6u3

animal spawning and combat implemented

animations? you may ask? well fuck you

also fixed tree mining bug fix. tldr of error, non-minable wood was marked minable so it would cause errors. but fixed that

---
## [Greenjoe12345/Aurora.3](https://github.com/Greenjoe12345/Aurora.3)@[652a3d02d4...](https://github.com/Greenjoe12345/Aurora.3/commit/652a3d02d4260aea7f34c64814f409a677b063a0)
#### Thursday 2023-09-21 18:10:40 by Wowzewow (Wezzy)

Adds Storage Container Animations (#17329)

* Much ado about the Bagginses

* god i hate manually mapped shit

* Update code/game/objects/items/weapons/storage/storage.dm

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>

* fixes

* yes

* Update code/game/objects/items/weapons/storage/bags.dm

Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---------

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>
Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---
## [aakashdeshamne/Tic-Tac-Toe-Game](https://github.com/aakashdeshamne/Tic-Tac-Toe-Game)@[21e44beac6...](https://github.com/aakashdeshamne/Tic-Tac-Toe-Game/commit/21e44beac6e9948023d1b05cd5df7f9bb546b1ed)
#### Thursday 2023-09-21 18:23:08 by aakashdeshamne

Add files via upload

# React Tic Tac Toe

Experience the classic game of Tic Tac Toe brought to life with React. Challenge your friends or play against the computer in this fun and interactive web-based version. Enjoy strategic gameplay and keep track of your wins.

---
## [Being-arman/Being-arman](https://github.com/Being-arman/Being-arman)@[9aebe4f71a...](https://github.com/Being-arman/Being-arman/commit/9aebe4f71af810ce274c64a9315eea8e0d6689e5)
#### Thursday 2023-09-21 19:25:49 by Mohammad Arman Ansari

Project : Diabetes Patients Analysis.

In contineous to my journey as a Data analyst intern at MeriSKILL. I am happy to share my 2nd project aligned to me.

Project Using PowerBI.bg

This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.

The objective of the dataset was to diagnostically predict whether a patient has diabetes or not.

In particular, all patients were females at least 21 years old. We analyzed pregnanceis based on age, use of insulin based on age, Average bloodpress during pregnancies based on age, min age, average BMI, averge age and finally we were able to analyse diabetes and outcomes.

---
## [MetaMask/eth-phishing-detect](https://github.com/MetaMask/eth-phishing-detect)@[d041f5d909...](https://github.com/MetaMask/eth-phishing-detect/commit/d041f5d9097b950af7e5fb28e6be5f08b1b10358)
#### Thursday 2023-09-21 19:46:07 by Tritium

Remove balancer.fi from blocklist (#13609)

Balancer has recovered control of balancer.fi after a social engineering attack at our registrar allowed hackers to take over the account.

We have confirmed that correct IPs have propigated.  If possible, please leave web.balancer.fi on the blocklist as we do not use it, and it seems like this name was used as part of the recent attack.

We have a war room open that we contacted via the seal-911 chat and I have been speaking to Tay.  You can find me that way if you have questions. 

Thank you

---
## [dirtycache/Homoney-Articles](https://github.com/dirtycache/Homoney-Articles)@[c53ac0d8e8...](https://github.com/dirtycache/Homoney-Articles/commit/c53ac0d8e8ada097f96a5359e60cbf0454d2e538)
#### Thursday 2023-09-21 20:14:00 by David Homoney

Update owasp-api-top-10-deep-dive-part-2.md

Sitting on an angry chair
Angry walls that steal the air
Stomach hurts and I don't care
What do I see across the way? Hey
See myself molded in clay, oh
Stares at me, yeah I'm afraid, hey
Changing the shape of his face, oh yeah
Candles red, I have a pair
Shadows dancing everywhere
Burning on the angry chair
Little boy made a mistake, hey
Pink cloud has now turned to gray, oh
All that I want is to play, hey
Get on your knees, time to pray, boy
I don't mind, yeah, I don't mind, I-I-I
I don't mind, yeah, I don't mind, I-I-I
Lost my mind, yeah, but I don't mind, I-I-I
Can't find it anywhere, I don't mind, I-I-I
Corporate prison, we stay, hey
I'm a dull boy, work all day, oh
So I'm strung out anyway, hey
Loneliness is not a phase
Field of pain is where I graze
Serenity is far away
Saw my reflection and cried, hey
So little hope that I died, oh
Feed me your lies, open wide, hey
Weight of my heart, not the size, oh
I don't mind, yeah, I don't mind, I-I-I
I don't mind, yeah, I don't mind, I-I-I
Lost my mind, yeah, but I don't mind, I-I-I
Can't find it anywhere, I don't mind, I-I-I
Pink cloud has now turned to gray
All that I want is to play
Get on your knees time to pray, boy

---
## [bsittler/meka](https://github.com/bsittler/meka)@[57434d1281...](https://github.com/bsittler/meka/commit/57434d1281142ff0eae4c0e15506c35853741ab2)
#### Thursday 2023-09-21 20:25:03 by Benjamin C. Wiley Sittler

Add "Mega Mode Super Game 78 [SMS-MD]"

A consistent name for indexing would probably be "Mega Mode Super Game 78 (KR) [SMS-MD]"

I've been calling it "Super Game 78 - Mega Game 16 (KR) [SMS-MD]" but the actual names are in Korean:

슈퍼게임 78 (Super Game 78) [cartridge label top]
메가게임16 (Mega Game 16) [cartridge label front]
메가모드 슈퍼게임 (Mega Mode Super Game) [menu title]
A different menu title 메가모드 게임머쉰 (Mega Mode Game Machine) very briefly flashes at startup before it is replaced, likely indicating some genetic relationship to multigame SMS arcade boards

This is a "space menu" multicart of SMS games in a Mega Drive-shaped cartridge. It runs entirely in SMS mode.

Dumping was via a temporarily hacked version of the Sanni Open Source Cart Reader https://github.com/sanni/cartreader

The SMS dumping script was temporarily modified as follows to allow FFF5 outer paging and 2MB dumps:

```
--- SMS.ino	2023-09-19 21:41:28.439252000 -0700
+++ "SMS.ino"	2023-09-19 23:08:35.180869200 -0700
@@ -33,8 +33,9 @@
 static const char SMSRomSizeItem9[] PROGMEM = "256 KB";
 static const char SMSRomSizeItem10[] PROGMEM = "512 KB";
 static const char SMSRomSizeItem11[] PROGMEM = "1024 KB";
+static const char SMSRomSizeItem12[] PROGMEM = "2048 KB";
 static const char* const SG1RomSizeMenu[] PROGMEM = { SMSRomSizeItem1, SMSRomSizeItem2, SMSRomSizeItem3, SMSRomSizeItem4 };                                      // Rom sizes for SG-1000
-static const char* const SMSRomSizeMenu[] PROGMEM = { SMSRomSizeItem4, SMSRomSizeItem7, SMSRomSizeItem8, SMSRomSizeItem9, SMSRomSizeItem10, SMSRomSizeItem11 };  // Rom sizes for SMS and GG
+static const char* const SMSRomSizeMenu[] PROGMEM = { SMSRomSizeItem4, SMSRomSizeItem7, SMSRomSizeItem8, SMSRomSizeItem9, SMSRomSizeItem10, SMSRomSizeItem11, SMSRomSizeItem12 };  // Rom sizes for SMS and GG

 // Init systems
 static bool system_sms = false;     // SMS or MarkIII
@@ -208,6 +209,9 @@
     writeByte_SMS(0xFFFD, 0);
     writeByte_SMS(0xFFFE, 1);
     writeByte_SMS(0xFFFF, 2);
+
+    // Space Menu SMS-MD Multicart
+    writeByte_SMS(0xFFF5, 0);
   }

   delay(400);
@@ -482,8 +486,8 @@
       }
     } else {
       // Rom sizes for SMS and GG
-      convertPgm(SMSRomSizeMenu, 6);
-      SMSRomSize = question_box(F("Select ROM size"), menuOptions, 6, 0);
+      convertPgm(SMSRomSizeMenu, 7);
+      SMSRomSize = question_box(F("Select ROM size"), menuOptions, 7, 0);
       switch (SMSRomSize) {
         case 0:
           cartSize = 32 * 1024UL;  // 32KB
@@ -503,6 +507,9 @@
         case 5:
           cartSize = 1024 * 1024UL;  // 1MB
           break;
+        case 6:
+          cartSize = 2048 * 1024UL;  // 2MB
+          break;
       }
     }

@@ -600,6 +607,9 @@
   draw_progressbar(0, totalProgressBar);

   for (byte currBank = 0x0; currBank < (cartSize / bankSize); currBank++) {
+    // Space Menu SMS-MD Multicart
+    writeByte_SMS(0xFFF5, currBank >> 1);
+
     // Write current 16KB bank to slot 2 register 0xFFFF
     if (!system_sg1000) {
       writeByte_SMS(0xFFFF, currBank);
```

The 2MB turned out to be overdump, as the ROM is only 1MB and contains just 15 distinct games

This uses the multicart mapper known to Meka as Mapper_SMS_Korean_MD_FFF5

Outer paging is by mapper register 0xFFF5 which can reach the whole 1MB ROM in 32KB pages. Inner paging is by Sega mapper registers but can only read 128KB in 16KB pages. Outer and inner paging seem to combine by shift and bitwise OR. The FFF5 register remains active even after the initial write

This 1MB multicart contains a menu and 15 SMS games: 32KB Satellite-7, Astro Flash, Machinegun Joe, Pit Pot, Teddyboy Blues, Great Baseball, Super Arkanoid, Seishun Scandal, and Ghost House; 64KB Super Tetris; and 128KB Makai Retsuden, Rambo, Inja, Double Target, and Fantasy Zone

The menu has an animation showing "SELECT MENU" and alternately "선택하세요。" (i.e. "Choose.")

The menu has five screens with 16 items per screen except for the last screen which has only 14

Screen 1:
```
０１ 환타지　죤 (Fantasy Zone) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
０２ 더블타게트 (Double Target) [0xFFF5=0x18]; it's part-18-double-target-128k.sms
０３ 람　　　보 (Rambo) [0xFFF5=0x10]; it's part-10-rambo-128k.sms
０４ 마계　열전 (ma'gye yeolcheon, i.e. Makai Retsuden) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
０５ 검　　　객 (geomgaeg, i.e. swordsman) [0xFFF5=0x14]; it's part-14-inja-128k.sms
０６ 테트　리스 (Tetris) [0xFFF5=0x08]; it's part-08-super-tetris-64k.sms
０７ 유령의　집 (yuryeong-ui jib, i.e. haunted house) [0xFFF5=0x0b]; it's part-0b-ghost-house-32k.sms
０８ 프로　야구 (Pro ya'gu, i.e. Pro baseball) [0xFFF5=0x06]; it's part-06-great-baseball-32k.sms
０９ 청춘　보이 (cheongchun Boy, i.e. youth Boy) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
１０ 테디　보이 (Teddy Boy) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
１１ 알카로이드 (alkaroideu, i.e. Arkaroid) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
１２ 공주　구출 (gongchu gu'chul, i.e. princess rescue) [0xFFF5=0x04]; it's part-04-pit-pot-32k.sms
１３ 머　신　건 (Machine Gun) [0xFFF5=0x03]; it's part-03-machinegun-joe-32k.sms
１４ 아스　트로 (Astro) [0xFFF5=0x02]; it's part-02-astro-flash-32k.sms
１５ 세터라이트 (Sattelite) [0xFFF5=0x01]; it's part-01-satellite-7-32k.sms
１６ 나무　요정 (na'mu yo'jeong, i.e. tree fairy) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
```

Screen 2:
```
１７ 정글특공대 (Jungle teug'gongdae, i.e. Jungle commando) [0xFFF5=0x10]; it's part-10-rambo-128k.sms
１８ 무림　고수 (murim go'su, i.e. murim expert/wǔlín master) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
１９ 기습　작전 (gi'seub jagjeon, i.e. surprise operation) [0xFFF5=0x14]; it's part-14-inja-128k.sms
２０ 드라　큐라 (Dracula) [0xFFF5=0x0b]; it's part-0b-ghost-house-32k.sms
２１ 쿵후　보이 (Kung-Fu Boy) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
２２ 벽돌　깨기 (byeogdol ggae'gi, i.e. breaking bricks) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
２３ 환타지월드 (Fantasy World) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
２４ 이중　표적 (i'jung pyo'jeog, i.e. double target) [0xFFF5=0x18]; it's part-18-double-target-128k.sms
２５ 습격　작전 (seubgyeog jagjeon, i.e. raid operation) [0xFFF5=0x14]; it's part-14-inja-128k.sms
２６ 부　르　스 (Blues) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
２７ 홍콩　강시 (Hong Kong gangsi, i.e. Hong Kong Jiangshi) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
２８ 해저　도시 (haejeo dosi, i.e. undersea city) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
２９ 홈런　게임 (Home Run Game) [0xFFF5=0x06]; it's part-06-great-baseball-32k.sms
３０ 피트　포트 (Pit Pot) [0xFFF5=0x04]; it's part-04-pit-pot-32k.sms
３１ 다운　타운 (Down Town) [0xFFF5=0x03]; it's part-03-machinegun-joe-32k.sms
３２ 곤충　위기 (gon'chung wi'gi, i.e. insect crisis) [0xFFF5=0x01]; it's part-01-satellite-7-32k.sms
```

Screen 3:
```
３３ 동굴타게트 (dong'gul Target, i.e. cave Target) [0xFFF5=0x18]; it's part-18-double-target-128k.sms
３４ 표창　달인 (pyo'chang dal'in, possibly "commendation: master"?) [0xFFF5=0x14]; it's part-14-inja-128k.sms
３５ 고　스　트 (Ghost) [0xFFF5=0x0b]; it's part-0b-ghost-house-32k.sms
３６ 블럭　격파 (Block gyeogpa, i.e. Block breaking) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
３７ 마계　탈출 (ma'gye talchul, i.e. Makai escape) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
３８ 미로　탈출 (miro talchul, i.e. maze escape) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
３９ 미데ᅵ나이트 (Midnight) [0xFFF5=0x03]; it's part-03-machinegun-joe-32k.sms
４０ 파이터보이 (Fighter Boy) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
４１ 후　레　쉬 (Flash) [0xFFF5=0x02]; it's part-02-astro-flash-32k.sms
４２ 목성환타지 (mogseong Fantasy, i.e. Jupiter Fantasy) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
４３ 스카이세븐 (Sky Seven) [0xFFF5=0x01]; it's part-01-satellite-7-32k.sms
４４ 보물　찾기 (bo'mul chajgi, i.e. treasure hunt) [0xFFF5=0x04]; it's part-04-pit-pot-32k.sms
４５ 우　디　팦 (Woody Pop) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
４６ 소년　테디 (so'nyeon Teddy, i.e. boy Teddy) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
４７ 습　　　격 (seubgyeog, i.e. raid) [0xFFF5=0x14]; it's part-14-inja-128k.sms
４８ 도시게릴라 (do'si Guerrilla, i.e. urban Guerrilla) [0xFFF5=0x10]; it's part-10-rambo-128k.sms
```

Screen 4:
```
４９ 메리의모험 (Mary-ui mo'heum, i.e. Mary's adventure) [0xFFF5=0x18]; it's part-18-double-target-128k.sms
５０ 표창　명인 (pyo'chang myeong'in, possibly "recognition: master"?) [0xFFF5=0x14]; it's part-14-inja-128k.sms
５１ 숲속의결투 (sup sog-ui gyeoltu, i.e. forest duel) [0xFFF5=0x03]; it's part-03-machinegun-joe-32k.sms
５２ 용　의　성 (yong-ui seong, i.e. dragon's castle) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
５３ 특　　　명 (teug'myeong, i.e. mission) [0xFFF5=0x10]; it's part-10-rambo-128k.sms
５４ 블럭　월드 (Block World) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
５５ 소녀　구출 (so'nyeo gu'chul, i.e. girl rescue) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
５６ 마법의　성 (ma'beob-ui seong, i.e. enchanted castle) [0xFFF5=0x04]; it's part-04-pit-pot-32k.sms
５７ 살롱의결투 (Saloon-ui gyeoltu, i.e. Saloon duel) [0xFFF5=0x03]; it's part-03-machinegun-joe-32k.sms
５８ 우주　탐험 (uju tam'heom, i.e. space exploration) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
５９ 인공　위성 (in'gong wi'seong, i.e. satellite) [0xFFF5=0x01]; it's part-01-satellite-7-32k.sms
６０ 비문　전달 (bi'mul jeondal, possibly "inscription: delivered"?) [0xFFF5=0x14]; it's part-14-inja-128k.sms
６１ 환상　특급 (hwansang teug'geub, i.e. fantastic express) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
６２ 메카폴리스 (Mechapolis) [0xFFF5=0x18]; it's part-18-double-target-128k.sms
６３ 강시　공포 (gangsi gongpo, i.e. Jiangshi horror) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
６４ 철권　소년 (cheolgweon so'nyeon, i.e. iron fist boy) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
```

Screen 5:
```
６５ 전　　　투 (jeontu, i.e. battle) [0xFFF5=0x10]; it's part-10-rambo-128k.sms
６６ 설원　비행 (seolweon bihaeng, i.e. snowfield flight) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
６７ 천상　세계 (cheonsang se'gye, i.e. heavenly world) [0xFFF5=0x0c]; it's part-0c-makai-retsuden-128k.sms
６８ 태권　소년 (Taekwon so'nyeon, i.e. Taekwon boy) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
６９ 석양의결투 (seog'yang-ui gyeoltu, i.e. sunset duel) [0xFFF5=0x0a]; it's part-0a-seishun-scandal-32k.sms
７０ 테디의모험 (Teddy-ui mo'heom, i.e. Teddy's adventure) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
７１ 환상　탐험 (hwansang tam'heom, i.e. fantasy exploration) [0xFFF5=0x1c]; it's part-1c-fantasy-zone-128k.sms
７２ 요　술　성 (yosul seong, i.e. witchcraft castle) [0xFFF5=0x04]; it's part-04-pit-pot-32k.sms
７３ 샤　도　우 (Shadow) [0xFFF5=0x14]; it's part-14-inja-128k.sms
７４ 슈　퍼　볼 (Super Ball) [0xFFF5=0x07]; it's part-07-super-arkanoid-32k.sms
７５ 미로　월드 (miro World, i.e. maze World) [0xFFF5=0x05]; it's part-05-teddyboy-blues-32k.sms
７６ 코메디　죠 (Comedy Joe) [0xFFF5=0x03]; it's part-03-machinegun-joe-32k.sms
７７ 해상　침투 (haesang chimtu, i.e. maritime infiltration) [0xFFF5=0x10]; it's part-10-rambo-128k.sms
７８ 위험한임무 (wiheomhan immu, i.e. dangerous mission) [0xFFF5=0x18]; it's part-18-double-target-128k.sms
```

ROM fingerprint info:

1.0M Super Game 78 - Mega Game 16 (KR) [SMS-MD].sms crc32:2c22af67 mekacrc:48904ABB002FF202 md5:c550257f1f718c58c69b44b315b6e566 sha1:529b8220765db8a1262c477d8cce8a02c9e1769e sha256:386c2211d162495001cca0e933e55b34fe5bcdad78d766ca09e3cadaee4cc218

32K part-00-menu-32k.sms crc32:f0c1219b mekacrc:38B26358316D17A6 md5:4bf0f25ca2570da8691fa52fd84e4bf4 sha1:1c7aacc40a6e9db35e081ff6c502e9a4fa3a3b9e sha256:b138b05936f1aaa51af51bd3ce26d52ac87e94201339fa98f104cee15ab893a7

32K part-01-satellite-7-32k.sms crc32:e905f779 mekacrc:BF0BB019104E927D md5:cb36bacb114abef2657ad403575284ec sha1:cb12a9bb901e75d9d354559ad07e91fbed27c8fa sha256:9f10cf93e82b13563265a5b3fdc0de1a095443147517cbc6edd38cb44e736117

32K part-02-astro-flash-32k.sms crc32:e96fa9aa mekacrc:1F0A1121D0278826 md5:33ca5c31a55ecaafef8794d13af14321 sha1:91187c55b9e6d22d3b734105028e5d6db1a8e68e sha256:ec7ae5be5b89f8b2c5eb6d072d2d9f3d871f14c6b65034fae836387b462c032f

32K part-03-machinegun-joe-32k.sms crc32:0c82b325 mekacrc:657C87C5BC491CB2 md5:1cda2406b4a8d9049480ac9e4d4698c3 sha1:dc395557d9e15bb392ca7886e79f703ba5fe4204 sha256:37efbddc02420ed5eb9302552c9f51389453dff064ffe92796bfa620a71a3f18

32K part-04-pit-pot-32k.sms crc32:90e69f40 mekacrc:E8647F6AAB818817 md5:1aedb4be5be8b9a82262f71b1c1b3be0 sha1:0a280d4db62d331636bccb4f1b48fdaaf487467b sha256:cf0ec5e5c1cb04e1d1f3a537291a97a3605553cd303044384245383cb55e4de9

32K part-05-teddyboy-blues-32k.sms crc32:ee5fd3a2 mekacrc:F524AC40F55CF3B7 md5:fce0d54020dd47051f0e7ee2e31b8fa1 sha1:24062d7a2e5e322f8dc86ca7ef1989d042b2a147 sha256:8bbf945c9eb8935d7c9035f2e4015842f2e1a1a1c60b2967be57909dc0993496

32K part-06-great-baseball-32k.sms crc32:9d7bf9df mekacrc:6E9004822AF4A4BA md5:6de6087feae1b4452c19331e0f3215c1 sha1:5e003c813b4e637c194039d99026f324ec7c3276 sha256:496e941ef2803a3561a790d9043fb2f2a917757b6f931cdca9a0382e75b74c5d

32K part-07-super-arkanoid-32k.sms crc32:433338d6 mekacrc:7C299AACD5544AA2 md5:156095211b5bbb62aa3a42bf55604a3d sha1:8d69ff29c08874fa38096f6c571da85b2647984a sha256:0b9316e9b21952ba4ee3949dd80eb58e81c759e708af8d47a102c11b475d91e4

64K part-08-super-tetris-64k.sms crc32:995e33c9 mekacrc:35095B2A342839A8 md5:9aa1340168ef6df6efce3191f2732a5d sha1:30d636f46c57109cc7581891b1663564adbf489c sha256:8a03ce9bef205741583ca8e243df88bd567169b2d5d91d2ddfe29a42ff0399d1

32K part-0a-seishun-scandal-32k.sms crc32:6894b8f4 mekacrc:1C106FCBBD3C1C85 md5:fa1afe7f752ad78abac96a3aeb59d012 sha1:52beae0533d1dfcd92039ff4d11dc1c85d21549b sha256:3b94d175fb784c6f86e3de26b321b7c30072727f329ec63dfa1c343361af8684

32K part-0b-ghost-house-32k.sms crc32:40461bfc mekacrc:887B27E3E66E9708 md5:8909e91122cb558fd59c9632743e46c0 sha1:5da3299b68d12cbf4f6d1ded92e135ffdc7e21a0 sha256:37d65977e08f04051dc6f5615f23289c901ebf9daa0e6d49b17ce17af2804117

128K part-0c-makai-retsuden-128k.sms crc32:9f0b36f3 mekacrc:F0CCA56EAB164927 md5:da6c2cfe32b47a839ae62da3c608d281 sha1:8f81dd64eb24e176d9004c716dfcf76c47a1d6b4 sha256:432432576768b073556528937bf81090e63feef6673bb83bc72329d5161dffe3

128K part-10-rambo-128k.sms crc32:8860ac5b mekacrc:035F3D6EF00F24D0 md5:6663e1ccc10b2c3622545edb3cc31f9d sha1:48733266210072a5ff0e75d628df8e778defb77a sha256:503b168083a9f317455557059471428e30e97f5b4eb704fd4a2dd87ee451f9c0

128K part-14-inja-128k.sms crc32:70cbe3d4 mekacrc:F8EFD201AFC4686B md5:8d86dc81b59bc2d935e272b9885c5839 sha1:4b86e4381cd77a16e041c6d1592811864f83e50d sha256:6bd243b0e2c5a6501c44e1f2f4f7e5dd28d3d857b89761042b2591f3c297a3b8

128K part-18-double-target-128k.sms crc32:25851e9f mekacrc:BB26B2F89129FAC1 md5:20647e24a146dc1a55e789b12c964714 sha1:e531b5bf439225d382a3c7488ab2a86ae9b02779 sha256:80123513a0cadc866bd616988630b360ea8ce25dac9718efac9e263506c31567

128K part-1c-fantasy-zone-128k.sms crc32:855ff46e mekacrc:87387FDFE2FB8185 md5:c97570ac3f441b3c6b79d8eb283a4bd5 sha1:96c1fdebbd2def19acb1f0e7d8411deae9ef5345 sha256:264035711477bccf9e5e23712c639378703855ac298f6899938fdb721268d15d

---
## [fuadchowdhury/gitignore.io](https://github.com/fuadchowdhury/gitignore.io)@[e6d38e2493...](https://github.com/fuadchowdhury/gitignore.io/commit/e6d38e2493b84ced8bb396d7f0dc88fb31522068)
#### Thursday 2023-09-21 20:29:15 by @Fuad Chowdhury

Create Md Salah Uddin Fuad Chowdhury 

I am Salah Uddin Fuad Chowdhury from Bangladesh.
There is not right why hack some one information.data.and everything.
There are lot of people now inciqure for my Data Leaked.
It's not right to hack some one information or leake it.i understand I miss use my behaviour but this is not right why leake my Data. I am sorry for what I am doing but this case impact lot of person security.i am a Student and I want to makes my career good but now this dara leaking inciqure my another friends life.if she sucide এই দায় ভার কার উপর পড়বে.I lost my everything.
I am depressed about this.
and my situation is not good enough. 
I am sorry forgive me for my miss use my behaviour 🙏
I am Salah Uddin Fuad Chowdhury 
Fuad Chowdhury from Bangladesh  comilla.

---
## [li-jia-nan/react](https://github.com/li-jia-nan/react)@[ac1a16c67e...](https://github.com/li-jia-nan/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Thursday 2023-09-21 21:03:04 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [keith-flynn/Portfolio](https://github.com/keith-flynn/Portfolio)@[1a293ac888...](https://github.com/keith-flynn/Portfolio/commit/1a293ac888395238a15d14f040f152674dcf2358)
#### Thursday 2023-09-21 21:08:30 by Keith Flynn

Add JavaScript to rotate an image upon load

Currently spins two fast and a third slow, which I think looks awful
but will remain in this commit because I find it hilarious. I'm probably
 going to undo the changes back to one spin and commit again right after
 this. ***!SILLY SPIN EDITION!***

---
## [victoriaJohnsontechgirl/victoriaJohnsontechgirl](https://github.com/victoriaJohnsontechgirl/victoriaJohnsontechgirl)@[140d914bdc...](https://github.com/victoriaJohnsontechgirl/victoriaJohnsontechgirl/commit/140d914bdc6e6b42583f01d23fcb226c84317c48)
#### Thursday 2023-09-21 21:18:49 by victoriaJohnsontechgirl

Update README.md

💻 Passionate FEMALE coder, fueling my love for programming! 🚀
🌟 Embracing the beauty of code, one line at a time ✨
👩‍💻 Exploring the endless possibilities of tech with joy! 🌈
📚 Lifelong learner, always expanding my coding horizons 🌱
⌨️ Turning ideas into reality through the power of programming ⚡️
🌍 Making my mark in the digital realm, one project at a time 🌟
💡 Innovating, problem-solving, and rocking the coding world! 💪
✨ Let's create something amazing together! Join me on this coding adventure! ✨

---
## [fiquick/cyber_security](https://github.com/fiquick/cyber_security)@[4fc3e2155a...](https://github.com/fiquick/cyber_security/commit/4fc3e2155a31009d9740dd74254cd07f1203cfa0)
#### Thursday 2023-09-21 21:19:12 by Fi Quick

Create VIP_actually_is_not_VIP

Suddenly, the influencer types aren't the VIPs anymore. It's going to be the non-VIP guests who can come into the VIP area.

It's an illusion - the VIP guests think they are VIP, but also the non-VIP guests think they are VIP 

How does that work?

I remember when I went to Fabric London, and the VIP guy was like, sure, I will go see if you can go into VIP and he just kept us waiting there ...ohhhh maybe we could have just walked in? damn, he vanished... was he letting us in? oh man.

---
## [mitchellh/libxev](https://github.com/mitchellh/libxev)@[69c3ae024e...](https://github.com/mitchellh/libxev/commit/69c3ae024eec8e9c7932578dad9b73f9197715c2)
#### Thursday 2023-09-21 21:22:45 by Mitchell Hashimoto

Windows Backend (IOCP) (#42)

# Description
This PR brings support for Windows using the [I/O Completion
Port](https://learn.microsoft.com/en-us/windows/win32/fileio/i-o-completion-ports).

Closes #10 

# Notes for reviewers
Unfortunately, this is a pretty beefy PR. I tried to clean the git
history so that it's kind of reviewable commit by commit though.

My approach was similar to what @mitchellh suggested me: first the
backend core, then the watchers building on top of it.

I also added support for Windows tests in GH Actions as he told me he
didn't have access to a Windows machine.

Please note that this work is far from perfect, it was my first time
playing with IOCP so expect some weirdness/mistakes.

## Known pain-points/limitations
**Timers**
Timings rely on `GetQueuedCompletionStatusEx` timeout parameter. I read
multiple times that timings on Windows were, well, slightly inaccurate
(plot twist: that's a euphemism). I'm not confident enough to deep dive
into this rabbit hole, so if somebody has more knowledge on that, feel
free to improve my implementation.

**Async**
I have the feeling that there is a better way to implement the `Async`
watchers compared to what I did. I couldn't come up with a better way
than inspiring myself from the `WASI` backend.

The part I struggled the most with was the fact that `Async` can be
notified before being linked to a `Loop`. This requires to store the
fact that it's notified inside the `Async` struct, but then it opens up
a lot of other questions and failed to find a satisfying solution taking
care of all of them.

I'll try to come back to it with a fresh mind but I'm open to
suggestions in the meantime 😁

**Completion port `HANDLE` registering**
In order to be able to wait for asynchronous I/O, `HANDLE` needs to be
linked to a Completion Port. However, you can only register it once
otherwise, the linking call fails. I first tried to let the user handle
that by giving the possibility to link a handle to a `Loop`, but that
ended up being unreliable and cumbersome when implementing Watchers.

My final decision was to ignore the failure and suppose that it always
works. Win32 documentation is not what we could call exhaustive, so I
don't if it's possible for an association to fail on the first call to
`CreateIoCompletionPort` with a newly created `HANDLE`. Worst scenario
is that it fails silently and asynchronous wait on this `HANDLE` never
completes. If anyone has an idea as to how we could properly solve that,
don't hesitate 😁

**UDP Benchmark tweaks**
This is described in #38

**Process support**
I didn't implement support for `Process` watchers yet. I feel like it's
not required to merge this (already big) PR. I'll see if adding support
is possible in the future.

---
## [Aamir98far/PortfolioWebsite](https://github.com/Aamir98far/PortfolioWebsite)@[f1e4b9cab7...](https://github.com/Aamir98far/PortfolioWebsite/commit/f1e4b9cab7074d1712187a2054ade1abbb0fb804)
#### Thursday 2023-09-21 22:17:23 by Aamir Farid

Portfolio Website

**My Portfolio Website**
Welcome to the repository of my personal Portfolio Website built using HTML, CSS, and JavaScript. This website showcases my professional journey, skills, and projects. It consists of various sections, including Home, Bio, Blog, Contact, and Service pages.
**Key Features:**
- **Home Page:** A visually appealing introduction to my portfolio with a brief overview.
- **Bio Page:** Detailed information about my background, education, and career.
- **Blog Page:** A collection of blog posts sharing my thoughts, experiences, and insights.
- **Contact Page:** A convenient way to get in touch with me for collaborations or inquiries.
- **Service Page:** Information about the services I offer and how I can add value to projects.
**How to Explore:**
1. Clone the repository to your local machine using `git clone`.
2. Open the `index.html` file in your web browser to start exploring.
3. Navigate through the different pages using the navigation menu.

**Contributions:**
Contributions and suggestions for improvements are welcome! If you have ideas for enhancements or spot any issues, please fork this repository, make changes, and submit pull requests.
Feel free to reach out if you have any questions, suggestions, or feedback. I hope you enjoy exploring my Portfolio Website!

---
## [Aamir98far/Netflix](https://github.com/Aamir98far/Netflix)@[3730480175...](https://github.com/Aamir98far/Netflix/commit/37304801756e1502ac348c35bc040646f8f79dcf)
#### Thursday 2023-09-21 22:25:19 by Aamir Farid

Homepage of Netflix

**Netflix Homepage Clone**
This repository contains the source code for a stunning Netflix homepage clone created using HTML and CSS. This project is a showcase of web development skills and design aesthetics, allowing users to explore a visually appealing and interactive homepage reminiscent of the popular streaming platform.
**Features:**
- Authentic Netflix homepage layout and design.
- Responsive and mobile-friendly interface.
- Seamless navigation and user experience.
- Customized CSS for dynamic content and animations.
**How to Use:**
1. Clone the repository to your local machine using `git clone`.
2. Open the `index.html` file in your web browser to explore the Netflix homepage clone.
3. Navigate through the movie selections, hover effects, and interactive elements.
**Contributions:**
Contributions and enhancements are welcome! If you have ideas for improving the design or functionality, please fork this repository, make changes, and submit pull requests.
**Note:**
This project is a non-commercial, educational endeavor aimed at showcasing web development skills and design creativity. It is not associated with or endorsed by Netflix.

---
## [Thomasbuzz/Social-tribble](https://github.com/Thomasbuzz/Social-tribble)@[c899f072ff...](https://github.com/Thomasbuzz/Social-tribble/commit/c899f072ffde91929b14d9908408d37b0e7181c1)
#### Thursday 2023-09-21 22:26:49 by Thomasbuzz

Create README.md

Welcome to my portfolio showcasing my expertise in Shopify store design and dropshipping. I have a passion for creating visually appealing and highly functional online stores that drive conversions and maximize profits through the dropshipping business model. In this portfolio, I will highlight my skills, experience, and successful projects in the field.

About Me:

I am a dedicated e-commerce enthusiast with a background in web design and digital marketing. My journey into the world of Shopify and dropshipping began several years ago when I recognized the potential of this business model. Since then, I have honed my skills and knowledge to create successful online stores that generate revenue for my clients.

Services Offered:

1. Shopify Store Setup:

I specialize in setting up Shopify stores from scratch, ensuring a user-friendly interface, mobile responsiveness, and seamless navigation.
Customization of themes, including selecting and modifying templates to align with your brand's identity.
Integration of essential apps and plugins for enhanced functionality and automation.

2. Product Research and Selection:

Comprehensive market research to identify profitable niches and products with high demand.
Careful selection of winning products with a focus on quality and competitive pricing.
Management of product listings, including product descriptions, images, and pricing updates.

3. Dropshipping Management:

Establishment of supplier relationships and seamless integration with your Shopify store.
Order fulfillment and tracking to ensure timely delivery and customer satisfaction.
Inventory management and updates to prevent stockouts and backorders.

4. Marketing and Promotion:

Development of effective digital marketing strategies, including SEO optimization, social media advertising, and email marketing.
Creation of compelling content to engage and convert visitors into customers.

Monitoring of campaign performance and continuous optimization for better ROI.

Portfolio Highlights:

Project 1: Client Name: Sarah and John Nelson>>>> Store-(ColourPop)

Niche: Cosmetic Accessories

Customized Shopify store design with an elegant and modern theme.
Extensive product research resulting in a product catalog that caters to a trendy audience.
Implemented an Instagram influencer marketing campaign, resulting in a 200% increase in sales within the first month.
Ongoing management of inventory and order fulfillment.

Project 2: [Client Name : Richard Saghian] - [Store Name: world global]

Niche: Fashion Accessories
Designed a visually stunning and user-friendly Shopify store with a focus on showcasing product aesthetics.
Carefully curated product listings and descriptions that resonate with the target audience.
Launched a successful Google Ads campaign, driving a 300% increase in website traffic and a 150% boost in sales.
Regularly updated product listings to ensure relevance and profitability.

Testimonials:

"Working with Thomas  broker was a game-changer for our business. The Shopify store design exceeded our expectations, and the dropshipping management has saved us time and money. Highly recommended!" - [Thomas broker]

"I was skeptical about dropshipping, but [Your Name] guided me through the process. The results speak for themselves - increased sales, happy customers, and a thriving online store." - [Client Name]

Contact Information:

If you are looking to kickstart your dropshipping journey or revamp your existing Shopify store, I am here to help. Feel free to contact me at [ordersthomasbuzz@gmail.com] or [+2349028542595] to discuss your project needs and goals.

Thank you for taking the time to explore my portfolio. I look forward to the opportunity to work with you and help you achieve your e-commerce success through Shopify store design and dropshipping.

---
## [zeroshade/arrow](https://github.com/zeroshade/arrow)@[6ba5bf7f01...](https://github.com/zeroshade/arrow/commit/6ba5bf7f0113af72415bc6b285029ed076803b4a)
#### Thursday 2023-09-21 22:30:31 by Matt Topol

holy shit it fucking works, except for missing a license

---
## [colemancda/VVVVVV](https://github.com/colemancda/VVVVVV)@[300f1b7919...](https://github.com/colemancda/VVVVVV/commit/300f1b791956f864a6d4333c0c2edb6b56097ab5)
#### Thursday 2023-09-21 22:54:04 by Misa

Switch assets mounting to dedicated directory

This fixes an issue where you would be able to mount things other than
custom assets in per-level custom asset directories and zips.

To be fair, the effects of this issue were fairly limited - about the
only thing I could do with it was to override a user-made quicksave of a
custom level with one of my own. However, since the quicksave check
happens before assets are mounted, if the user didn't have an existing
quicksave then they wouldn't be able load my quicksave. Furthermore,
mounting things like settings.vvv simply doesn't work because assets
only get mounted when the level gets loaded, but the game only reads
from settings.vvv on startup.

Still, this is an issue, and just because it only has one effect doesn't
mean we should single-case patch that one effect only. So what can we
do?

I was thinking that we should (1) mount custom assets in a dedicated
directory, and then from there (2) mount each specific asset directly -
namely, mount the graphics/ and sounds/ folders, and mount the
vvvvvvmusic.vvv and mmmmmm.vvv files. For (1), assets are now mounted at
a (non-existent) location named .vvv-mnt/assets/. However, (2) doesn't
fully work due to how PhysFS works.

What DOES work is being able to mount the graphics/ and sounds/ folders,
but only if the custom assets directory is a directory. And, you
actually have to use the real directory where those graphics/ and
sounds/ folders are located, and not the mounted directory, because
PHYSFS_mount() only accepts real directories. (In which case why bother
mounting the directory in the first place if we have to use real
directories anyway?) So already this seems like having different
directory and zip mounting paths, which I don't want...

I tried to unify the directory and zip paths and get around the real
directory limitation. So for mounting each individual asset (i.e.
graphics/, sounds/, but especially vvvvvvmusic.vvv and mmmmmm.vvv), I
tried doing PHYSFS_openRead() followed by PHYSFS_mountHandle() with that
PHYSFS_File, but this simply doesn't work, because PHYSFS_mountHandle()
will always create a PHYSFS_Io object, and pass it to a PhysFS internal
helper function named openDirectory() which will only attempt to treat
it as a directory if the PHYSFS_Io* passed is NULL. Since
PHYSFS_mountHandle() always passes a non-NULL PHYSFS_Io*,
openDirectory() will always treat it like a zip file and never as a
directory - in contrast, PHYSFS_mount() will always pass a NULL
PHYSFS_Io* to openDirectory(), so PHYSFS_mount() is the only function
that works for mounting directories.

(And even if this did work, having to keep the file open (because of the
PHYSFS_openRead()) results in the user being unable to touch the file on
Windows until it gets closed, which I also don't want.)

As for zip files, PHYSFS_mount() works just fine on them, but then we
run into the issue of accessing the individual assets inside it. As
covered above, PHYSFS_mount() only accepts real directories, so we can't
use it to access the assets inside, but then if we do the
PHYSFS_openRead() and PHYSFS_mountHandle() approach,
PHYSFS_mountHandle() will treat the assets inside as zip files instead
of just mounting them normally!

So in short, PhysFS only seems to be able to mount directories and zip
files, and not any loose individual files (like vvvvvvmusic.vvv and
mmmmmm.vvv). Furthermore, directories inside directories works, but
directories inside zip files doesn't (only zip files inside zip files
work).

It seems like our asset paths don't really work well with PhysFS's
design. Currently, graphics/, sounds/, vvvvvvmusic.vvv, and mmmmmm.vvv
all live at the root directory of the VVVVVV folder. But what would work
better is if all of those items were organized into a subfolder, for
example, a folder named assets/. So the previous assets mounting system
before this patch would just have mounted assets/ and be done with it,
and there would be no risk of mounting extraneous files that could do
bad things. However, due to our unorganized asset paths, the previous
system has to mount assets at the root of the VVVVVV folder, which
invites the possibility of those extraneous bad files being mounted.

Well, we can't change the asset paths now, that would be a pretty big
API break (maybe it should be a 2.4 thing). So what can we do?

What I've done is, after mounting the assets at .vvv-mnt/assets/, when
the game loads an asset, it checks if there's an override available
inside .vvv-mnt/assets/, and if so, the game will load that asset
instead of the regular one. This is basically reimplementing what PhysFS
SHOULD be able to do for us, but can't. This fixes the issue of being
able to mount a quicksave for a custom level inside its asset directory.

I should also note, the unorganized asset paths issue also means that
for .zip files (which contain the level file), the level file itself is
also technically mounted at .vvv-mnt/assets/. This is harmless (because
when we load a level file, we never load it as an asset) but it's still
a bit ugly. Changing the asset paths now seems more and more like a good
thing to do...

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[5046a7d3ae...](https://github.com/dragomagol/tgstation/commit/5046a7d3ae845198e98ff3bc22c31495585e560c)
#### Thursday 2023-09-21 23:05:26 by Fikou

decks of cards no longer have their own wielded var (#78260)

## About The Pull Request
we have the trait for that

## Why It's Good For The Game
Throughout UNDERTALE, we get treated to three story sequences (4 if you
include flowey's fakeout but that's not important). The first is the
intro story, telling the tale of humans and monsters, which shortly
thereafter leads into 201X, and Chara (Toriel's house has “An old
calendar from 201X.”) falling into the underground.

The second is the waterfall flashback, its contents taking place
immediately after the intro segment, as a voice (Asriel) finds the
fallen child.

And finally, the third takes place in the True Pacifist final boss.
We'll get to it in due course, and it will have its own section, but
let's address the first two. Regarding the intro, the first thought one
might have is that simply, while narratively relevant, is not a diegetic
presentation. However, We know that everything after the “201X” frame is
Chara's memory (from an outside perspective, that is,) and we also know
that UNDERTALE LOVES bringing the non-diegetic, the mechanical, the
game, INTO the narrative. Saving, RPG Stats, hell, even the
NarratorChara. Surely the intro can be as well? On top of this, what
does the intro do for the player, as the player? Well, aside from
setting the tone, the intro gives us some setting backstory. It's all
important context, and it certainly helps… but it being in the intro
sequence is not that important; It's all presented throughout the game
via diegetic signs, books, and expositional tortoise war heroes/angry
fish guardswomen. The second half is how Chara fell to the underground,
and while also setting tone and informing the player how their character
arrived. It also creates the false impression for the player that their
character is Frisk, feeding into UNDERTALE's meta narrative; “You are
not your character, and their happy ending is not yours.” If we weren't
playing Chara, this would have no narrative impact. The story beat fails
to land by showing us someone elses' character. But, sure. This could be
a purely non-diegetic intro sequence. Simply put, The 201X portion of
the intro sequence does not make sense from a diegetic or a storytelling
perspective unless we play as Chara.

Flashback number two is explicitly a canonical, diegetic flashback. It
occurs when Frisk escapes Undyne by falling down a massive pit… again.
This time, they land in the garbage zone, black out, and have a
flashback sequence of the first time Asriel found Chara. While serving
the main narrative by setting up Asriel as a character, furthering the
final twist of the meta narrative's pacifist route, and neatly
transitioning between overworld areas, it's also very explicitly
diegetic and cannot be dismissed as an intro sequence. With this in
mind, one question is raised. Why do we see this flashback? If the
player character is Frisk, this makes little sense, why would we see
someone else's flashback and not our own? Same thing applies for a Third
Entity, but even more abstract and illogical. What even are we? Sure,
you could say Chara is somehow attached to us/Frisk and that somehow we
get a flashback from Chara who is somehow knocked unconscious by Frisk
also being knocked unconscious. I used the word somehow three times.
That's not good storytelling. A simpler answer, at least in my view, is
that We Are Chara. When Frisk is knocked unconscious, we, being
ostensibly linked to them as a Spirit/Ghost/Reincarnation/Possessing
Dead Frisk/Demon/Insert fan-theory here/SOUL Fragment, have our only
connection to the world temporarily disabled, rendering us effectively
unconscious and prompting a flashback. Nothing weird with multiple
entities or memory sharing. The waterfall flashback is simply our
memory. Simple. The simplest answers are usually the correct ones.

<details>
<summary>DO NOT RESEARCH</summary>
The third sequence is a connection/extension of the first two, displayed
when we SAVE “Someone Else” during the true pacifist battle with Asriel.
To refresh everyone, here is the direct quotes, taken from the Wiki:


[SAVE]: Someone Else
Strangely, as your friends remembered you... Something else began
resonating within the SOUL, stronger and stronger. It seems that there's
still one last person that needs to be saved. But who...? ... Suddenly,
you realize. You reach out and call their name.
Asriel: “Huh? What are you doing...?”
s
It's at this point that the sequence plays. There's no narration, but we
see the sequence of interactions between Asriel and Chara. There are no
panels (except for the first) that don't contain the both of them.
Following this, we get:

You feel your friends' SOULs resonating within ASRIEL! [This is the
generic flavour text for saving all 6, before “Someone Else”, and
appears at the asterisk above as well]
[SAVE]: Asriel Dreemurr
Asriel:
> “Wh... what did you do...?”
“What's this feeling…? What's happening to me?”
Etc. etc. let me win…
During my first and consecutive playthroughs of UNDERTALE, I came to the
conclusion that Asriel's soul still “Had Some Chara In It.” Saving
“Someone Else” was saving Chara, and then you save Asriel Dreemurr after
the story sequence.

This interpretation no longer feels particularly potent to me, but in
the spirit of completeness I'll address it alongside the more reasonable
“You just save Asriel.” Assuming for a moment though, that we do “Save
Chara”, it's not unreasonable to assume that some of Chara's ‘essence'
(or whatever) was merged with Asriel's and by SAVING them, we're SAVING
the part of them that's inside Asriel.

But I don't like that theory.

Let's talk about SAVING Asriel for a moment.

What is the motivation for doing that? Why would we, in universe, wish
to SAVE him, something that the narration explicitly prompts us to do?
He tried and probably succeeded to kill us, at least once, he wants to
reset the entire timeline, he wants to erase all our friendships, all
our progress.

So, why? Well, it's simple. He's our brother. And we know better than
anyone that he's worth saving. And at the very least, there's something
about Frisk (who appears to have absolutely no personality) that reminds
him of Chara, of us. This is, by his own admission, weird;

Asriel:
“Frisk… You really ARE different from Chara. In fact, though you have
similar, uh, fashion choices… I don't know why I ever acted as if you
were the same person.”

To summarise.

The player SAVING Asriel Dreemurr works best if they are Chara, it
becomes Chara encouraging Frisk to SAVE Asriel too.

Asriel recognises Frisk as Chara throughout the True Pacifist battle
(And Beyond), despite his own admission that this is basically
unfounded. Something is causing this recognition.

In Alphys' true lab, there lies a dusty TV and a stack of VHSes. On
them, lie some of the last words Chara had ever heard from their father.

[Asgore] Chara! You have to stay determined! You can't give up... You
are the future of humans and monsters...

These tapes are not the first time they are heard. Sleeping in Toriel's
guest bed, we dream about them. Suffering a fatal injury, they echo in
our ears. Watching the tape is yet another reveal. It's the chilling
truth that in fact, the words we (if we die a lot) are so familiar with,
are in fact the words we hear on our deathbed.

Storytelling-wise, this reveal; like all the others, fails if we do not
play as Chara.

Aside from Asriel's dialogue, Chara's genocide Narration, and the coffin
in Asgore's basement, this is the only time we hear Chara's name. That
and, this following exchange.

[Flowey]
Hi.
…
Monsters have returned to the surface
Peace and prosperity will rule across the land.
…
Well.
There is one last thing.
…
One being with the power to erase EVERYTHING…
…
I'm talking about YOU.
…
So, please.
Just let them go.
Let Frisk be happy.
…
Well, that's all.
See you later…
Chara.
This, I think, is pretty explicitly definitive. Flowey comes to you. To
us. Tells us to take a deep breath and leave the happy ending intact,
then bids us farewell by our own name.

Regardless of anything else, this definitively proves Chara is the
entity with the power to reset everything by the end of True Pacifist
(Which is a power we have). Flowey positively identifies us as “Chara”,
despite his mistake we discussed in 3C. He's not talking to Frisk,
because he refers to them in the third person.

He is talking to Us. Chara.

I don't want to discuss Flowey's use of “Chara” in Genocide all that
much, because the counter-argument is blindingly simple.

“By the time Flowey first says that name, Chara has overtaken Frisk by
feeding on the power we create for them.”

Of course, under PlayerChara, Flowey's lines still make sense, and
arguably more.

Implications
At this point, I believe the evidence is sufficient to support the
theory. With this in mind, I want to discuss the implications this has
on the narrative and meta-narrative. This is where all those funny
glossary terms come into play.

The pacifist route in UNDERTALE, as discussed above, is textually quite
simple when accepting PlayerChara. The meta-text is also relatively
simple. Meta textually, the Pacifist Route is a dissection of the
suspension of disbelief, examining how we emotionally place ourselves
within fictional worlds, and are often-times torn away from those worlds
as the game comes to an end, left wanting the true emotional connection,
wanting a happy ending that cannot be good enough for us because we're
real and it's not. The reflection of this meta narrative in the textual
narrative, quite naturally flows. We, Chara, want a happy ending. But we
can't have it, it's not our happy ending. We're gone. We've been gone a
long time. Frisk's happy ending can't be good enough for us, because we
won't be around to see it. So, we're left with a choice.

To let Frisk live happily? To accept an ending that might leave us
emotionally wanting, yet preserves our emotional journey?

To reset? To refuse an ending and satiate our emotional emptiness, yet
destroy that very emotional journey we took in the process?

The choice is the same. There is practically no separation between the
diegetic and the meta.

“Can a happy ending be good enough for you?” This question applies to
us, as the real world player running UNDERTALE.exe on our computer, and
us, Chara, the long deceased human who can do little but watch as Frisk
lives the life they wish they still had, or can destroy everything for a
hollow mimicry of that very life.

This message, however, breaks down under one specific circumstance.
Where we force a Third Entity into the mix. This one decision fractures
the cohesion and creates a meta-textually dissonant mess. Now, all of a
sudden, “Can a happy ending be good enough for you?” no longer runs
parallel through both narratives. There is no reason for the Player
Entity to wish to remain, the happy ending should automatically be good
enough because it's the happy ending. Meanwhile, Chara, despite being an
inextricable representation of “A happy ending I can't achieve,” gets
absolutely nothing to do with this meta-narrative because they're just…
not you.

“we are mario in Super Mario 64, but when he says "Thank you so much for
playing my game!" that doesn't mean we aren't still playing as mario” -
PopitTart

This is where things get weird. See, in the Genocide route.. Well, we
see Chara. On Screen. Talk to us.

Now, it can easily be argued that this completely shatters the theory,
but I would disagree. I'm going to endeavour to present a textual
explanation (or two) for this. But first, I want to dissect the
meta-text here.

Now, I'm sure the idea that “The Genocide Route's Meta-Narratve is
Fading Emotional Investment and the way emotional connection with video
games can lead to the very sabotage of that emotional connection” is not
revolutionary. However, what's conspicuously absent from all of the
third entity theorising is the way that this meta-text is mirrored in
the textual narrative.

Once satisfied with a game, having extracted all lines of dialogue and
stat boosts, once reaching all endings, a user will close the game down.
And at some point, perhaps to make room for a new game or perhaps on a
new device, will leave the game uninstalled, either deliberately, or
simply as a consequence of time.

Textually, what happens in the Genocide ending?
Now we have reached the absolute.
There is nothing left for us here.
Let us erase this pointless world, and move on to the next.

The world is destroyed. So much is left unanswered here.
Who is Chara talking to?
Where did Frisk go?
How do they have this much power?
Why would they want this?
If we ‘corrupted' them, what the hell does that even mean?
What is Chara?
For now, let's talk about who Chara is talking to.

The simplest answer is “Perspective switch.” Suddenly, we're not Chara
anymore, now we are Frisk. This meets all the dialogue options and even
vaguely mirrors the meta-text. It also manages to avoid bringing a third
entity along and so is automatically better! But, I find myself still
not fully enjoying this idea.

Remember what I said about Occam's Razor?

I think there's another option. One that doesn't involve three entities,
or even two entities, just Chara. One that mirrors the meta-text to a
degree only Toby Fox could pull off. It's a weird one, and I don't fault
you if you don't get it on your first read, but bear with me here,
because things are about to get

A little
Fucking
Abstract

Let's discard any and all pre-concieved notions of anything and hold one
singular truth above all else. “Chara Is The Player.” What does this
mean for this cutscene?

Well… it means the player is talking to…

THe player?

It also neatly answers the question of motive, so let's throw that out
the skeleton-shaped hole in the window for now.

If the player is talking to the player, this frames Chara's words in a
whole new light.

Every time a number increases, that feeling… That's me. “Chara.”

This line becomes explicitly literal. The Chara on-screen is literally
the player's feeling of satisfaction watching stat increases. But this
is all meta-textual, right? What does this mean for the textual
narrative?

Here's the thing. It can't mean anything, yet means everything.

There is no way to reconcile the fact that a Textually Real character is
directly talking about what the player feels when playing a game to
completion. The barrier between Meta and Textual no longer exists. It
can't. Not here. And with this revelation, everything begins to make
sense.

Your power awakened me from death.

Our power. Our desire to complete UNDERTALE awakens Chara from death.
They become startlingly real. We imbue this fictional character with the
real world desire to consume fiction, destroying enemies and worlds as
we go, increasing our power and our stats. Video Game Accomplishments.
And UNDERTALE has just finished being consumed.

My “human soul”... My “determination”... They were not mine, but YOURS.

Chara, the textual player, acknowledges the meta-textual player's
control over the game world. A control that we surrendered. By engaging
in UNDERTALE in a fully immersed way, we have fed the Diegetic character
that is our player character, Chara. This has continued until we haul
ourself out of the Internal Mode and into the External Mode, revoking
our immersion to make the consumption of content easier, to distance
ourself from the killing.

Raising our LV.

The more we distance ourselves, the less real UNDERTALE's world appears
to us. Once it's done, we're ready to erase this pointless world and
move onto the next. There's just one problem. UNDERTALE knows about us.
It knows we exist and it will abuse that to convey meaning. By revoking
our immersion in UNDERTALE, we end up shattering the barrier between
Meta and Textual, and this occurs because revoking our immersion is a
diegetic decision. Without this barrier, WE, as a character, gain
control of UNDERTALE and use this external mode control to

Erase the world. To uninstall.


This code doesn't actually work, of course. That was pretty obvious by
the fact that it didn't delete your game. But still, this exists in the
code that makes the game window shake when Chara attacks it. This is,
quite literally, intent for Chara to delete UNDERTALE. If you didn't
think Chara was capable of uninstalling your game before, you should
now.

Who is chara talking to?

Us.
How do hey have this much power?

We gave it to them. We Are them, and we deleted UNDERTALE when we were
done with it.
Why would they want this?

We wanted to move onto a new game.
What is Chara?

Us. ( I'll come back to this.)
But wait! What about soulless pacifist?
Well, at that point, you've surrendered Frisk's SOUL to Chara, as in,
you the real player has revoked your emotional attachment to UNDERTALE
and accepted that Chara can have control over the game. You've revoked
your immersion AS Chara, you no longer see yourself a Chara and as such
Chara becomes their own being. You've surrendered, basically. But they
let you play through it. Because why not. You might get attached again,
but that's fine. All that means is that the happy ending that was once
Frisk's, that you, the player, and you, Chara, both once lamented not
being able to live, has now been surrendered to Chara. A warped,
completionist, Chara.

You don't get your happy ending. But Chara does.

You don't even get the solace of knowing someone gets their happy
ending. Because Chara gets it.

Frankly, outside of being “The Player”, I don't think the exact nature
of “Chara” is that crucial. My personal thought is that they're a SOUL
fragment, absorbed by Frisk when they fell on Chara's grave (Frisk could
absorb a human SOUL fragment because said fragment was part monster
SOUL). This fragment gives Frisk the final edge of determination needed
to SAVE.

But, ultimately, that's little more than a fanfiction. And frankly, I
think that's okay. Not everything needs to be impenetrable, as long as
there's enough there to build a stable foundation.

I'd also like to address the nature of SAVING quickly, specifically the
normal version, not the Asriel fight version. People have asked “Why do
we save if it's Frisk's SOUL.” There could be many reasons. Frisk might
just defer control to us. Because we're pushing Frisk over that
Determination limit, we might be privileged to have that control.
</details>

## Changelog

not player visible

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[1552857ff4...](https://github.com/dragomagol/tgstation/commit/1552857ff44a8b481736eda843c5131ad4b761ab)
#### Thursday 2023-09-21 23:05:26 by JupiterJaeden

Balance: Removes anti-drop implants for nukies (#78275)

## About The Pull Request

Removes anti-drop implants being available in nukie implants. Also
rebalances the cybernetic implants bundle to cost 20 TC (value of 24 TC)
since anti-drop has been removed from it.

## Why It's Good For The Game

This is one of the rare few nerf PRs where I was not the one who got
KILLED by the broken OP shit but rather the one using it. I recently
played a nukie round (after hearing that anti-drop had been added) where
I took modsuit shield, dsword, and anti-drop. I got separated from my
team and then proceeded to solo murderbone half the fucking station,
resist MULTIPLE disarms that would have otherwise been successful, get
the disk alone, and nuke. I only had to stop to heal _once_ and honestly
I probably would have been fine if I didn't.

Anti-drop dsword is _insanely_ powerful. Shielded dsword nukies were
already strong enough but were at least somewhat balanced insofar as
there were several ways you could still reliably disarm them and
therefore open them up to more attacks. But now (after
https://github.com/tgstation/tgstation/pull/77330 which added the
anti-drop implants to nukie uplink) you can have shielded anti-drop
dsword nukies. Add stims and some explosives to deal with any static
fortifications the crew might make (like firelock crush relays), and
with a semi-robust player you essentially have a murderbone machine who
can't be killed by any regularly accessible crew counters short of point
blank suicide bombing. We should not have a default nukie loadout that
can only be reliably, regularly countered by a fucking bomb. Especially
since the crew's main easily accessible ballistic is now being nerfed as
well. (https://github.com/tgstation/tgstation/pull/78235)

EDIT: I'd also like to point out that we already don't allow hulks to
use dswords for many of the same reasons.

## Changelog

:cl:
balance: removed anti-drop implants from the nuclear operative uplink
balance: removed anti-drop implant from the nukie implants bundle and
changed its cost to 20 TC
/:cl:

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[172f65989e...](https://github.com/dragomagol/tgstation/commit/172f65989ea40418b1c03316ad3163ee67f06e94)
#### Thursday 2023-09-21 23:05:26 by Jacquerel

Nuclear Operative Jump Jets (#78088)

## About The Pull Request

This PR gives operative MODsuits access to "jump jets".
This is an activated module (starts pinned) with a 30 second cooldown
which removes your personal gravity for 5 seconds and (if possible)
pushes you upwards by one z level. In combination with your regular
jetpack this allows you to fly over gaps, and (most importantly) out of
pits such as you may inadvertently find yourself wandering into on
Icebox.
I have a few other changes I want to make specifically targetted at the
experience of Icebox station destruction causing people to fall several
z levels and get trapped, but this is the first one.

You have to stand still for 1 second to activate the jump jet. This is
because jetpack movement without gravity is actually usually faster than
an operative will walk, and I don't want them to just toggle it as a
sprint button while running around. If people find other tactical uses
for this though I think that's cool.

This module currently isn't available to crew on the tech web, although
maybe someone could add it later if they wanted to. It's not quite so
useful if you don't _also_ have a jetpack though.
I bumped the available complexity of the suits I attached it to up by
the complexity cost of this module so it's not taking up previously
available space.

## Why It's Good For The Game

It's funny when the whole ops team falls in a hole after an explosion
they caused and gets stuck in there fighting Snow Legions but they
should probably have some method for dealing with that.
It also lets them pop back up from the tram hole, a risky proposition
because any flying mob hit by the tram dies almost instantly.

## Changelog

:cl:
add: Operative MODsuits now have an attached "jump jet" which sends you
upwards and allows you to use your jetpack under gravity for a few
seconds, perfect for navigating the pits and valleys of Icebox Station.
/:cl:

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[ac18420676...](https://github.com/dragomagol/tgstation/commit/ac18420676c9daaa94910a1a1f4a2e2d74f0d05d)
#### Thursday 2023-09-21 23:05:26 by Hatterhat

John Splintercell: a gun that is only good for shooting out lights (#78128)

## About The Pull Request
adds the SC/FISHER lightbreaker self-charging energy pistol, which does
0 damage. As a joke.

![image](https://github.com/tgstation/tgstation/assets/31829017/84603fcd-dbc3-4857-a657-98c4bd34e881)


https://github.com/tgstation/tgstation/assets/31829017/97572baa-7421-4800-a60e-2db03f4adc6d

<details><summary>actual details, in case the video wasn't good
enough:</summary>

unless you shoot at light fixtures,

![image](https://github.com/tgstation/tgstation/assets/31829017/54092fbf-cbf6-4750-b2b8-37d643efba2a)
floodlights,

![image](https://github.com/tgstation/tgstation/assets/31829017/90b19560-fa25-471b-9f6f-3147c33e5c56)
or people with flashlights/seclites (even on helmets or guns) (it still
does 0 damage, it just turns off their lights. not permanently)

![image](https://github.com/tgstation/tgstation/assets/31829017/1a83c6f9-8fff-4035-aeeb-515319a3dd40)
it also works on crusher lights. and cyborg headlights. i don't have a
screenshot for it.
doesn't work on flares though.

also it can shoot past machines and lockers

![image](https://github.com/tgstation/tgstation/assets/31829017/8fb0a213-8e4a-42cc-9daa-eae5faf6ee77)
</details>
(also adds a variable for deciding how loud a dry fire sound is, in case
you want to make your gun's empty sound be less loud.)

## Why It's Good For The Game

Adds a silly little tool for silly little men who either really hate
lightbulbs or want to recreate the experience of being John
Splintercell, the lightbulb-assasinating secret agent from Fork Echelon.

## Changelog

:cl:
add: The SC/FISHER disruptor pistol, a very compact, permanently
silenced energy gun, is now stocked in Nanotrasen-accessible black
markets with a price generally somewhere between 400 and 800 credits.
Aspiring users are warned that it's really bad for trying to actually
kill people. Caveat emptor.
add: Guns now have a dry_fire_sound_volume variable, allowing for guns
to be less loud when trying to fire while empty.
fix: Closets and crates now properly count as structures for pass flags
again.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Stealthii/Paradise](https://github.com/Stealthii/Paradise)@[acb7352265...](https://github.com/Stealthii/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Thursday 2023-09-21 23:41:27 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[dbaae7ee1e...](https://github.com/MrMelbert/tgstation/commit/dbaae7ee1ebe10c9f3221c78b30e4714f167a405)
#### Thursday 2023-09-21 23:54:05 by Lufferly

Supermatter Delamination Balance Changes (Real) (#77996)

## About The Pull Request

lord forgive me I fucked up the merge conflict

The supermatter delamination countdown timer (how long it takes to go
boom-boom after hitting 0 integrity) has been lowered from 30 seconds to
13 seconds.
Removing a sliver from the supermatter, the traitor objective, will
further lower that down to 3 seconds.
Changes the wording on the mood effects from the supermatter
delaminating slightly.
The crystal uses SPAN_COMMAND on its final countdown, which means it
talk bigger.

## Why It's Good For The Game

Currently I feel that the supermatter delamination countdown overstays
its welcome. Ideally it provides tension to get the hell out, or perhaps
to make a risky last second play to try and save the supermatter.
However right now its at 30 seconds, which gives no danger of staying in
engineering right up to integrity 0, and keeps the tension at a high
note for too long, almost to the point of awkwardness. 13 seconds is a
good balance between get-the-fuck-out while still giving some leeway for
engineers to escape and crewmembers to jump in lockers, and feels quick
enough to give that danger that the supermatter should provide.
Additionally, removing a sliver from the supermatter lowers the cooldown
to 3 seconds. Right now this is one of the harder tasks a traitor can be
tasked with, while giving relatively little payoff sabatoge-wise. To the
point where I have seen engineers just let the traitor do it, as the
debuff it gives to the supermatter is minor. Now it makes the
supermatter delaminate almost immediately after hitting 0 integrity,
which means it will likely catch some engineers in the blast if a
traitor did it stealthy. This also makes it more risky to try and fix a
delamination if the engineering/security team did not stop the sliver
from being removed. All meaning succeeding at this task should be more
rewarding and damaging.
Finally the mood descriptions for the mood effects you get when a
supermatter delaminates have been changed. Currently they are pretty
gamey, and represent what the player might be thinking more than their
character. Additionally they were not very descriptive of where they
came from, which could be confusing.

## Changelog

:cl: Seven
balance: The supermatter delamination countdown has been lowered from 30
to 13 seconds
balance: Removing a sliver from the supermatter further lowers that down
to 3 seconds
balance: The supermatter crystal uses bigger text on its final countdown
spellcheck: Some supermatter delamination related mood descriptions have
been edited to explain the mood effect better
/:cl:

---------

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@users.noreply.github.com>

---

