## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-06](docs/good-messages/2023/2023-07-06.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,233,502 were push events containing 3,649,890 commit messages that amount to 295,757,982 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[159d2aeebe...](https://github.com/francinum/Therac-Gameserver/commit/159d2aeebee7ef681891019d52069bf898846e03)
#### Thursday 2023-07-06 00:04:15 by Gallyus

Reagent Description and Abstract Changes (#164)

* Reagent Description and Abstract Changes...
Abstract reagents are no longer detected via a magic list.
Added a description to non-abstract reagents that were missing them.
Adds a unit test to detect non-abstract reagents missing a description.

As a consequence:
Some reagents have disappeared from lists for being abstract.
Instantiating an abstract reagent is illegal and crashes New().

* Minor fixes
It's 3am go fuck yourself.

* Apply suggestions from code review

* Allows access to a new ANSI color

* C&D creates a notice on start for logging purposes

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[a3eb90b950...](https://github.com/francinum/Therac-Gameserver/commit/a3eb90b9504f6a21c2636a4bb8aeb8b40eb66861)
#### Thursday 2023-07-06 00:04:15 by Gallyus

Fix Pack 3: Revenge Of The Fuck (#225)

* Various Jaunt fixes (#70431)

* Jaunt code path reworked so that traits and other effects can be removed consistently regardless of how effect is ended.
Jaunts will more consistently clean themselves up (and unjaunt you) when you lose the spell.
If a shuttle lands on you while you are jaunted it will now kill you instead of crashing and fucking with the shuttle landing process.
Z travelling while inside an object or mob will now relay that direction instead, allowing you to jaunt up and down as well as cardinally.
Mirror walk button updates at correct times.
Blood and Shadow walk buttons have same functionality as Mirror Walk.

* Fixes Soul Scythe being able to get to Centcom by moving down on the bottom Z-level (#71171)

## About The Pull Request

`/obj/item/soulscythe/relaymove()` was using `get_step()` which doesn't
understand our multi-z system and was happily trying to move Z - 1 which
is Centcom. I'm still not really sure I understand why move() allowed
the scythe to just move right through the floor in this case, I think
moving to turfs with `density = 0` is also behaving strangely and just
skipping some checks that should keep it from moving through the floor,
but to be honest I don't fully understand the move chain and just
changing to `get_step_multiz()` at least keeps the scythe from going to
Z-levels it shouldn't.
## Why It's Good For The Game

Whilst it is fun for the scythe to go on an adventure to forbidden
Z-levels, admins probably don't appreciate these adventures so much.
## Changelog
:cl: VexingRaven
fix: Soul Scythes can no longer phase through the floor into Centcom.
/:cl:

* Fixes multi-Z ruins (Ice Moon Mining Site) not spawning (#70097)

* Fixes multi-z ruins not spawning

* I should proably commit said changelog files.

* Proc Ref wrapping

* Update to the correct procs

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: VexingRaven <msgerbs@users.noreply.github.com>

---
## [RimiNosha/Nosha-Industries-Server](https://github.com/RimiNosha/Nosha-Industries-Server)@[fcba2b4d3e...](https://github.com/RimiNosha/Nosha-Industries-Server/commit/fcba2b4d3ec78fb22bb3be504beae2e5add39ad1)
#### Thursday 2023-07-06 00:12:48 by RimiNosha

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.

![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [RimiNosha/Nosha-Industries-Server](https://github.com/RimiNosha/Nosha-Industries-Server)@[d4ea9a2d17...](https://github.com/RimiNosha/Nosha-Industries-Server/commit/d4ea9a2d172789edfaefbd2292e583747cc0c828)
#### Thursday 2023-07-06 00:12:48 by RimiNosha

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.

Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:
# Conflicts:
#	code/modules/mob/living/carbon/carbon.dm
#	icons/obj/poster.dmi
#	tgstation.dme

---
## [RimiNosha/Nosha-Industries-Server](https://github.com/RimiNosha/Nosha-Industries-Server)@[86d4675778...](https://github.com/RimiNosha/Nosha-Industries-Server/commit/86d46757785d36e59061c45704081cb23c8d310b)
#### Thursday 2023-07-06 00:12:48 by RimiNosha

Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d1fa50db47...](https://github.com/tgstation/tgstation/commit/d1fa50db47dd3d11e44e8ac074ee2850f00edf19)
#### Thursday 2023-07-06 00:52:30 by atlasle

New space ambient track (#76547)

## About The Pull Request

Adds a new space ambient track made by me to the game, supposed to be a
bit scarier than the others that were recently added as I feel that
they're a bit too happy (not to diss I really like them), also cleaned
up a bit of ambience.dm as the medical portion of it didn't follow the
same rules as the other ones. also also this will only be used for
tgstation so license wise I think this is CC BY-SA 3.0 but I'm not sure
so correct me if I'm wrong, also this is my first PR so yeah. Here's a
link to listen to the track https://voca.ro/18WvrGORDDdR

## Why It's Good For The Game

Variety is the spice of life.

## Changelog

:cl:
sound: A new ambient track will now play in space
/:cl:

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[ed57b8127f...](https://github.com/Rhials/tgstation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Thursday 2023-07-06 01:06:34 by Jacquerel

Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

---
## [crawl/crawl](https://github.com/crawl/crawl)@[263fee0cbc...](https://github.com/crawl/crawl/commit/263fee0cbc910991afffb9441e2064c240ca5b96)
#### Thursday 2023-07-06 01:22:30 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Transmutations skill. They do not care about Int,
  Spellcasting, other spell schools, wizardry, or encumbrance. (That is,
  they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!

Art for talismans is pending.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Transmuter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Transmutations skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Transmuters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. UC damage now scales
slightly with Tmut skill. Not much to say otherwise.

This is intended to be another way that Transmuters can transition into the
mid-game. It probably needs some kind of extra nerf to compensate for not
caring about body armour penalties anymore - TBD.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Transmuter no longer starts with any spells, and their stats have been
adjusted accordingly.

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

TODOs
-----

Before this is merged, I'll need to do the following:
- Get autotraining working with talismans.
- Update sprints.
- Add save compat for old transmuters, esp those with Beastly Appendage on.
- Fix up transmuting into/out of anaconda form while constricting
  (if that's possible? Maybe with Xom involved?)
- Make Xom poly you again.
- Add a targeter for Siphon Essence.

Later changes
-------------

Transmutations skill is currently in a midpoint state. At some point
(probably after this is merged), I'd like to split apart the functions of
'powering tmut spells' (Irradiate, Yara's, etc) and 'using talismans'.
This should reduce the extent to which Tmut has an 'identity crisis' - the
form playstyle isn't really a casting playstyle (it wasn't before, either!),
but it still has an odd and awkward overlap with various useful spells.

To do this, tmut spells would either be dispersed into different schools
(Poison, etc), or talisman use could become a new, separate 'Shapeshifting'
skill. (I suppose the Tmuter background would also need a rename?) This is
a large enough change that I'm not rushing into it - talismans are massive
enough on their own.

-

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[48cc57010d...](https://github.com/tgstation/tgstation/commit/48cc57010d3ff01c55c53131b9399a4e71656d8d)
#### Thursday 2023-07-06 01:26:47 by Jacquerel

Various spider fixes (#76528)

## About The Pull Request

Fixes #76484
Then I noticed some weird stuff which slipped through the PR and poked
at that too.

- Spiderlings and Spiders once more have names ending in (###)
- Removed an unused property on Spiderlings.
- Rewrote the descriptions for a bunch of web-abilities and web-objects
to be clearer and have better capitalisation.
- Refactored the "Web Carcass" ability to not extend from "lay web" as
it didn't need to perform most of that behaviour.
- Also I renamed it and made the description give you a hint about why
you would want to instantly spawn a statue.
- The web effigy now despawns at the same rate as the ability cools down
so you're not dumping spider statues all over the place.
- I made spiderlings move at about the same speed as humans except if
they're on webs in which case they're still pretty fast.

To be honest I am not certain an instant statue spawning button is great
to begin with and I didn't even know it was added to the game but I am
not interested in messing much with the balance for now.

This made me look at spiderlings enough that I'm going to try and make a
new sprite for them that isn't awful.

## Why It's Good For The Game

Lets you differentiate individual spiders a little bit.
Makes usage of abilities clearer.

## Changelog

:cl:
balance: Guard spider web statues despawn as the ability comes back off
cooldown.
balance: Spiderlings now only move at light speed if they're on webs,
stay safe little guys.
fix: Spiders once again have random numbers after their names.
/:cl:

---
## [e-mo/wisdom_sensor_net](https://github.com/e-mo/wisdom_sensor_net)@[80819cffd6...](https://github.com/e-mo/wisdom_sensor_net/commit/80819cffd68f8807cbb5b9d06ccf7ceff7f5ef9c)
#### Thursday 2023-07-06 01:29:42 by emo

Finish driver/RUDP refactor

I cleaned up a few things about the two interfaces that bothered
me. Mostly aesthetic things, but also some simple changes like
boolean return values from most functions with I feel makes the main
interface easier to use.

Now and of the Rfm69 library functions which can fail return a boolean.
Success = True
Failure = False
But Evan, what happened to the more specific return values that gave
at least a little insight into what the fuck happened? I'm glad you
asked! Now the Rfm69 state object will log its last return value
so you can read it after the function has returned. This whole change
allows us to use library functions as boolean expressions:

if (!Rfm69_init(...)) FREAK_OUT();

Then, if we need more info, we can access the return value at:

rfm->return_status;

I have also seperated the initialization logic and the allocation logic
to prevent having to pass a Rfm69 ** to the init function. Now you call
Rfm69_create() first which returns an allocated Rfm69 *. The init
function(s) now take simply a Rfm69 * now.

Beyond this I also cleaned up the Tx/Rx logic a bit, and combined the
two report structs into one universal report type called TrxReport
which can be passed to either the transmit or receive rudp functions.
Something about the two only slightly different structs bothered me
and this feels cleaner. As stated in the interface, a NULL can be passed
insted of a TrxReport pointer as internally the rudp functions check
for a valid pointer before manipulating the report variable. This adds
a tiny bit of extra logic which I have managed to resist
micro-optimizing away. I also resisted over abstracting the rudp
interface into bullshit and kept with the "trust the user of the
library" philosophy I have employed thus far. I think it makes the
code more explicit and expressive.

---
## [aidenwallis/personal](https://github.com/aidenwallis/personal)@[ffd5dd867f...](https://github.com/aidenwallis/personal/commit/ffd5dd867f36d90950e58781a02a896534290a11)
#### Thursday 2023-07-06 01:46:18 by Aiden

another fucking social media app for the love of god PLEASE MAKE IT STOP

---
## [MarvelMathesh/Marvel-Kernel-4.9-land](https://github.com/MarvelMathesh/Marvel-Kernel-4.9-land)@[7d8f57133e...](https://github.com/MarvelMathesh/Marvel-Kernel-4.9-land/commit/7d8f57133eb6552b99ada3a8ab7358acca9a91f1)
#### Thursday 2023-07-06 02:17:26 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Arafattex/oc_a13r](https://github.com/Arafattex/oc_a13r)@[921be92355...](https://github.com/Arafattex/oc_a13r/commit/921be923551be5d7849bdc488617baacd39e2e4e)
#### Thursday 2023-07-06 02:33:30 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[8545d885e1...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/8545d885e1c04e16ec326ac7232682575968ee6d)
#### Thursday 2023-07-06 02:34:00 by Knative Automation

upgrade to latest dependencies

bumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping knative.dev/hack f591fea...fc42790:%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping knative.dev/serving 2c1bb07...bde2f42:%0A  > bde2f42 Update net-gateway-api nightly (# 14144)%0A  > bb1262e Update net-kourier nightly (# 14129)%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/client-pkg 4f052f9...f377f06:%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping knative.dev/eventing 034bec9...6a890e0:%0A  > 6a890e0 Fix flaky unit tests (# 7080)%0A  > eaf28a7 Add tracing for TestBrokerWithManyTriggers (# 7077)%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)

Signed-off-by: Knative Automation <automation@knative.team>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[755fa4db6d...](https://github.com/tgstation/tgstation/commit/755fa4db6d5c811770188c340cd2ccb85469d505)
#### Thursday 2023-07-06 02:40:26 by san7890

Loads Away Missions for Unit Testing (#76245)

## About The Pull Request

Hey there,

A pretty bad bug (#76226) got through, but it was fixed pretty quickly
in #76241 (cf92862daf339e97c76b52c91f31d49ba5113bd4). I realized that if
we were testing all the away missions, that this could theoretically get
caught and not happen again. Regardless, unit testing gateway missions
has been on my to-do list for a while now, and I finally got it nailed
down.

Basically, we just have a really small "station" map with the bare bones
(_teeny_ bit of fluff, maploading is going to take 30 seconds tops
anyways let me have my kicks) with a JSON map datum flag that causes it
to load all away missions in the codebase (which are all in one folder).
Just in case some admins were planning on invoking the proc on
`SSmapping`, I also decided to gate a `tgui_alert()` behind it because
you never can be too sure of what people think is funny these days (it
really does lock up your game for a second or so at a time).

I also alphabetized the maps.txt config because that was annoying me.
## Why It's Good For The Game

Things that break on production could(?) be caught in unit testing? I
don't know if the linked issue I mentioned above would have been caught
in retrospect, but it's likely to catch more than a few upcoming bugs
(like the UO45 atmospherics thing at the very top) and ensure that these
gateway missions, which tend to be the most neglected part of mapping,
stay bug-free.

This is also helpful in case someone makes a new away mission and wants
to see if stuff's broken. Helps out maptainers a bit because very, very
technically broken mapping will throw up runtimes. Neato.
## Changelog
Nothing that players should be concerned about.

Let me know if there's a better way to approach this, but I really think
that having a super-duper light map with the bare basics to load up
gateway missions and then all nine-ish gateway missions can sequentially
load during init. I can't think of a better way to do it aside from some
really ugly `#ifdef` shit. Also also, it has the added benefit of being
a map that will always load your away mission without touching a single
shred of config (and it's not likely to break if you follow sane
practices such as making your own areas)

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[6e288185bc...](https://github.com/lessthnthree/tgstation/commit/6e288185bcc4bb3c55a8588369409fcc4e6f2cbf)
#### Thursday 2023-07-06 02:41:33 by Jacquerel

Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[9aa3fb2901...](https://github.com/MarkSuckerberg/Shiptest/commit/9aa3fb29012991ce7a9d755e640a1af65f3fe319)
#### Thursday 2023-07-06 02:48:00 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[c84e40255d...](https://github.com/MarkSuckerberg/Shiptest/commit/c84e40255d466e37983e5cb03c110e7dd8ab90c8)
#### Thursday 2023-07-06 02:48:00 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [AZURE-ARC-0/Open-Assistant](https://github.com/AZURE-ARC-0/Open-Assistant)@[b9c60ed582...](https://github.com/AZURE-ARC-0/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Thursday 2023-07-06 03:06:35 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [Manjunatha-kv/PORTFOLIO](https://github.com/Manjunatha-kv/PORTFOLIO)@[b397112d7b...](https://github.com/Manjunatha-kv/PORTFOLIO/commit/b397112d7b2337ed8daaf30b8d1f84db3c58060c)
#### Thursday 2023-07-06 03:12:53 by Manjunatha_kv_

Create README.md

My Portfolio

Welcome to my portfolio! Here you will find a curated collection of my work and accomplishments, showcasing my skills, expertise, and creativity. As an individual passionate about various fields and dedicated to continuous learning, this portfolio reflects my diverse range of experiences and talents.

Within this portfolio, you will discover my professional journey, which spans across different industries and disciplines. From my early educational background to my most recent projects, I have sought to challenge myself and explore new horizons, consistently striving for excellence.

The portfolio encompasses a wide range of projects, including innovative designs, captivating written pieces, software development endeavors, and successful collaborations with various teams. Each project highlights my ability to adapt to different contexts, think critically, and deliver impactful results.

Throughout my career, I have demonstrated proficiency in areas such as graphic design, web development, content creation, marketing strategies, data analysis, and project management. I possess a deep understanding of industry trends and technologies, enabling me to stay at the forefront of innovation and produce work that resonates with audiences.

Furthermore, my portfolio emphasizes my commitment to creativity and originality. I take pride in bringing fresh perspectives to every project, infusing them with a unique blend of imagination and practicality. Whether it's crafting compelling visual identities, writing engaging articles, or developing intuitive user interfaces, my goal is to create memorable experiences that leave a lasting impression.

As you explore this portfolio, I hope you will gain insights into my passion, skills, and dedication. I invite you to delve into the various sections, examine the projects in detail, and witness firsthand the value I bring to every endeavor. I am excited to share my journey with you and look forward to future collaborations, where I can contribute my expertise to new and exciting ventures.

Thank you for visiting my portfolio, and please don't hesitate to contact me if you have any questions or opportunities for collaboration.

---
## [FF6BeyondChaos/BeyondChaosRandomizer](https://github.com/FF6BeyondChaos/BeyondChaosRandomizer)@[6ecb2514ac...](https://github.com/FF6BeyondChaos/BeyondChaosRandomizer/commit/6ecb2514acd962169aaebb21ab93667357e9f95f)
#### Thursday 2023-07-06 03:12:55 by Crimdahl

Merging in Web version changes.

randomizer.py:
- Wrapped the whole randomize process in a try/except block to pass exceptions back to GUI/Web
- Added support for custom coral names from web
- Added support for a custom playlist from web
- Added support for a custom passwords from web

appearance.py:
- Added support for custom coral names from web
- Added validation to ensure there are enough male and female names

musicinterface.py:
- Added support for a custom playlist from web

musicrandomizer.py:
- Reordered imports
- Added support for a custom playlist from web
- Made tierboss section check case-insensitive

options.py:
- Fixed an invalid default value for dancingmaduin

sillyclowns.py:
- Added support for a custom passwords from web

formationrandomizer.py:
- Import changes

appearance.py, dialoguemanager.py, esperrandomizer.py, itemrandomizer.py, locationrandomizer.py, monsterrandomizer.py, namerandomizer.py, randomizer.py, skillrandomizer.py, towerrandomizer.py, utils.py, wor.py:
- Cosmetic changes to variable names and/or spacing

---
## [RohitBMalviya/DataScinece](https://github.com/RohitBMalviya/DataScinece)@[c8eb05330e...](https://github.com/RohitBMalviya/DataScinece/commit/c8eb05330eb71af2b93ae1b87c26d625e2ac08f4)
#### Thursday 2023-07-06 04:04:04 by Rohit Malviya

Data_Science TE-AIDS Assignment

1) Data Wrangling, I
Perform the following operations using Python on any open source dataset (e.g., data.csv)
1. Import all the required Python Libraries.
2. Locate open source data from the web (e.g., https://www.kaggle.com). Provide a clear
description of the data and its source (i.e., URL of the web site).
3. Load the Dataset into pandas dataframe.
4. Data Preprocessing: check for missing values in the data using pandas isnull(), describe()
function to get some initial statistics. Provide variable descriptions. Types of variables etc.
Check the dimensions of the data frame.
5. Data Formatting and Data Normalization: Summarize the types of variables by checking the
data types (i.e., character, numeric, integer, factor, and logical) of the variables in the data set.
If variables are not in the correct data type, apply proper type conversions.
6. Turn categorical variables into quantitative variables in Python.
In addition to the codes and outputs, explain every operation that you do in the above steps and explain
everything that you do to import/read/scrape the data set.

2) Data Wrangling II
Create an “Academic performance” dataset of students and perform the following operations using
Python.
1. Scan all variables for missing values and inconsistencies. If there are missing values and/or
inconsistencies, use any of the suitable techniques to deal with them.
2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable techniques
to deal with them.
3. Apply data transformations on at least one of the variables. The purpose of this
transformation should be one of the following reasons: to change the scale for better
understanding of the variable, to convert a non-linear relation into a linear one, or to decrease
the skewness and convert the distribution into a normal distribution.
Reason and document your approach properly.

3) Descriptive Statistics - Measures of Central Tendency and variability
Perform the following operations on any open source dataset (e.g., data.csv)
1. Provide summary statistics (mean, median, minimum, maximum, standard deviation) for adataset (age, income etc.) with numeric variables grouped by one of the qualitative
(categorical) variable. For example, if your categorical variable is age groups and quantitative
variable is income, then provide summary statistics of income grouped by the age groups.
Create a list that contains a numeric value for each response to the categorical variable.
2. Write a Python program to display some basic statistical details like percentile, mean,
standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’ of
iris.csv dataset.
Provide the codes with outputs and explain everything that you do in this step.

4) Data Analytics I
Create a Linear Regression Model using Python/R to predict home prices using Boston Housing
Dataset (https://www.kaggle.com/c/boston-housing). The Boston Housing dataset contains
information about various houses in Boston through different parameters. There are 506 samples and
14 feature variables in this dataset.
The objective is to predict the value of prices of the house using the given features.

5) Data Analytics II
1. Implement logistic regression using Python/R to perform classification on
Social_Network_Ads.csv dataset.
2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall
on the given dataset.

6) Data Analytics III
1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv dataset.
2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall on
the given dataset.
7) Text Analytics
1. Extract Sample document and apply following document preprocessing methods:
Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
2. Create representation of documents by calculating Term Frequency and Inverse
DocumentFrequency.

8) Data Visualization I
1. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and contains information about
the passengers who boarded the unfortunate Titanic ship. Use the Seaborn library to see if we
can find any patterns in the data.
2. Write a code to check how the price of the ticket (column name: 'fare') for each passenger
is distributed by plotting a histogram.

9) Data Visualization II
1. Use the inbuilt dataset 'titanic' as used in the above problem. Plot a box plot for distribution of
age with respect to each gender along with the information about whether they survived or
not. (Column names : 'sex' and 'age')
2. Write observations on the inference from the above statistics.

10) Data Visualization III
Download the Iris flower dataset or any other dataset into a DataFrame. (e.g.,
https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as:
1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
2. Create a histogram for each feature in the dataset to illustrate the feature distributions.
3. Create a boxplot for each feature in the dataset.
4. Compare distributions and identify outliers.

Mini Project:
11 Use the following covid_vaccine_statewise.csv dataset and perform following analytics on the
given dataset https://www.kaggle.com/sudalairajkumar/covid19-inindia?select=covid_vaccine_statewise.csv a. Describe the dataset b. Number of persons state
wise vaccinated for first dose in India c. Number of persons state wise vaccinated for second
dose in India d. Number of Males vaccinated d. Number of females vaccinated

---
## [MrVauxs/dnd5e-animations](https://github.com/MrVauxs/dnd5e-animations)@[545d7d8d2e...](https://github.com/MrVauxs/dnd5e-animations/commit/545d7d8d2e74203dd14d5dbea23876dd7d04eb47)
#### Thursday 2023-07-06 04:33:13 by Sisimshow

1.6.0

New Animations

-Ranged
--Burnt Othur Fumes
--Catapult Munition
--Essence of Ether
--Holy Water
--Malice

-On Token
--Assassin's Blood
--Ball Bearings
--Cunning Action
--Divine Sense
--Drow Poison
--Eldritch Master
--Empty Body
--Hide in Plain Sight
--Indomitable
--Ink (for fun)
--Magical Tinkering
--Midnight Tears
--Oil of Taggit
--Pale Tincture
--Patient Defense
--Perfect Self
--Poison (for Basic Poison and Poison, Basic (vial)
--Potion of Poison
--Purple Worm Poison
--Primeval Awareness
--Serpent Venom
--Slow Fall
--Sorcery Points
--Soul of Artifice
--Step of the Wind
--Stroke of Luck
--Torpor
--Truth Serum
--Uncanny Dodge
--Vanish

-Template

-Preset
--Caltrops

Changed Animations

-On Token
--Arcane Recovery (removed accidental source animation)

---
## [srimanachanta/photonvision](https://github.com/srimanachanta/photonvision)@[3bd19a5cf9...](https://github.com/srimanachanta/photonvision/commit/3bd19a5cf9ddf656cc23412fe49358bc15266241)
#### Thursday 2023-07-06 05:54:36 by Sriman Achanta

Create placeholder camera settings cause my god that shit is annoying and i completely agree with the origonal photon vision dev who decided to do it because devlopment is so hard without it to validate things, but i might remove it later so that I can make sure a no camera enviorment still works even though the backend validates that stuff already

---
## [splashcat-ink/splashcat](https://github.com/splashcat-ink/splashcat)@[6062cf3e81...](https://github.com/splashcat-ink/splashcat/commit/6062cf3e81ec8f4a4f5db95df3a6d4bf630a7830)
#### Thursday 2023-07-06 06:35:32 by kitt

fix this stupid fucking thing. i wanna fucking die already.

---
## [strongreasons/android_kernel_asus_sdm660](https://github.com/strongreasons/android_kernel_asus_sdm660)@[e4fc9894c9...](https://github.com/strongreasons/android_kernel_asus_sdm660/commit/e4fc9894c919ea38e2ed316b6a956803cc3a2970)
#### Thursday 2023-07-06 07:46:42 by Dave Chiluk

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
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[f2ec16c1e6...](https://github.com/Helg2/tgstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Thursday 2023-07-06 08:05:17 by Vekter

Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[24cab6d9f9...](https://github.com/RaShCat/FF-STG/commit/24cab6d9f91ea45cb420bdac188d3142eebb004b)
#### Thursday 2023-07-06 08:30:44 by SkyratBot

Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[5c4b13863f...](https://github.com/Steelpoint/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Thursday 2023-07-06 09:57:20 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [Govind-Upadhyay-12/Adventure-Reactjs](https://github.com/Govind-Upadhyay-12/Adventure-Reactjs)@[a8ae7f0a4f...](https://github.com/Govind-Upadhyay-12/Adventure-Reactjs/commit/a8ae7f0a4f29ff1621d1714f845f1dd4b364eaf9)
#### Thursday 2023-07-06 10:08:39 by Govind Upadhyay

Add files via upload

Welcome to our website! We've crafted a seamless and dynamic online experience using the power of ReactJS, React Router, and React hooks 

With ReactJS, we've built a highly responsive and interactive interface that will captivate and engage our visitors. Our website loads quickly and smoothly, thanks to React's efficient rendering capabilities, ensuring a seamless browsing experience.

The implementation of React Router allows for effortless navigation between different pages and sections of our website. Whether you're exploring our products, reading our blog, or reaching out through our contact page, React Router ensures that you can effortlessly move through the various sections of our site, providing a user-friendly and intuitive browsing experience.

Our website's aesthetic appeal and visual finesse are achieved through the creative utilization of CSS hooks. By leveraging the power of CSS hooks, we've customized every element of our site, ensuring a visually stunning and cohesive design that reflects our brand identity.

Incorporating the latest technologies and best practices, our website stands out from the crowd with its impressive performance, smooth navigation, and captivating visual appeal. We're committed to providing our visitors with an exceptional online experience, and our use of ReactJS, React Router, and CSS hooks is at the heart of that commitment. Explore our website today and discover the perfect blend of functionality, aesthetics, and usability.

---
## [status-im/status-mobile](https://github.com/status-im/status-mobile)@[9ed68ee7d1...](https://github.com/status-im/status-mobile/commit/9ed68ee7d1b7d59dd8b20c2ee1ffe43bd1c37078)
#### Thursday 2023-07-06 10:28:09 by Icaro Motta

Lint & fix some shadowed core Clojure(Script) vars (#16500)

It's well known that shadowing core Clojure vars can lead to unexpected bugs. In
fact, it's a common source of bugs in other languages too. In the status-mobile
repository there are, in total, 562 shadowed vars, ~500 are core vars. Excluding
the "old code" we still have 285 offenders.

In status-mobile I've already seen two bugs caused by shadowed vars, both with
the shadowed var "name". But probably other problems happened in the past, and
others will happen in the future if we don't do something about this. This PR is
also my response to my frustration trying to review PRs and checking for
shadowed vars, humans were not meant for that!

In this commit we are enabling ":shadowed-var" to lint certain (not all) core
vars as errors (not warnings). In future PRs we can gradually unshadow more
vars. For the record, name is shadowed 40 times in the new code and 130 in
total, and type is shadowed 93 times in the new code and 124 in total!

What about non-core vars, should we allow shadowing? There are ~70 non-core
shadowed vars. In my opinion, we should also lint and disallow shadowing
non-core vars, since it may cause the same kind of bugs of shadowing core vars.
But this decision can be left for another moment/issue, after we have fixed the
most prominent problem of shadowing core vars.

Which vars are unshadowed in this PR? I fixed 62 errors and unshadowed
cljs.core/iter, cljs.core/time, cljs.core/count, cljs.core/key,
clojure.core/key.

Resources:

- [clj-kondo linter: shadowed-var](https://github.com/clj-kondo/clj-kondo/blob/master/doc/linters.md#shadowed-var)

---
## [PRO-COINMARKETCAP/wpt](https://github.com/PRO-COINMARKETCAP/wpt)@[ef456d07b4...](https://github.com/PRO-COINMARKETCAP/wpt/commit/ef456d07b407cb574392fa63a8925ac0222eb079)
#### Thursday 2023-07-06 11:43:48 by PRO-COINMARKETCAP

randomUUID.https.any.js

Contents Listen Publication date: 6 April 2020 Overview  The OAIC appreciates the unprecedented challenges Australian government agencies and private sector employers are facing in combating the spread of COVID-19. To prevent or manage the risk of COVID-19, you may have implemented, or are considering, remote working arrangements for employees or are expanding existing arrangements.  The purpose of this resource is to provide tips on key issues that entities regulated by the Privacy Act 1988 (Cth) should consider when assessing the privacy impacts of a remote working arrangement. This resource should be read in conjunction with the additional resources listed below.  The Privacy Act does not prevent employees from working remotely as a response to COVID-19, however, the Australian Privacy Principles (APPs) will continue to apply. You should consider whether any changes to working arrangements will impact on the handling of personal information, assess any potential privacy risks, and put in place appropriate mitigation strategies. Assessing potential privacy risks will also help you reduce the risk of a data breach, which occurs when personal information is subject to unauthorised access or disclosure or is lost.  A privacy impact assessment (PIA) is a useful tool for evaluating and mitigating risks to personal information. The scale and scope of your PIA will depend on the extent of the change to your working arrangements and other factors such as the size of your entity, its resources, and the types of personal information that you handle.  Agencies should also consider their obligations under the Privacy (Australian Government Agencies – Governance) APP Code 2017 (the Code) to undertake a PIA for all high privacy risk projects.[1]  Why assess privacy risks through a PIA?  The OAIC acknowledges that, given the urgent circumstances surrounding the COVID-19 pandemic, you may have already implemented or expanded existing remote working arrangements for your employees. Business Continuity Plans and risk assessments will have guided your decisions.  Under APP 11 (security of personal information), entities must take active measures to protect personal information they hold from misuse, interference and loss, as well as unauthorised modification or disclosure.[2] In addition, the Notifiable Data Breach (NDB) scheme applies to all entities with existing personal information security obligations under the Privacy Act. The NDB scheme requires entities to notify affected individuals and the OAIC in the event of an ‘eligible data breach’.[3] These obligations continue to apply to your remote working arrangements.  A PIA provides a useful framework to screen for unexpected privacy issues and may help to further mitigate any privacy risks associated with the remote working arrangements that have been implemented. Mitigating privacy issues will also help reduce the risk of experiencing a data breach, which could trigger your notification obligations under the NDB scheme.  It is never too late to conduct a PIA. A PIA should also be an iterative process during the life of any project, being updated to take account of changes to working arrangements as they evolve. The checklist below is intended to help you consider and assess common privacy issues that may arise in a remote working arrangement.  For more information about undertaking a PIA, see the OAIC’s Guide to undertaking privacy impact assessments (PIA Guide) and PIA e-Learning course.  Is a PIA necessary?  While you may have had remote working arrangements in place for some staff previously, the current situation in relation to COVID-19 has likely resulted in a substantial increase to the numbers of employees working from home and/or an expansion to types of work tasks that have traditionally been performed remotely. Changes to the way personal information is handled may also be required as a result of a shift to a remote working arrangement.  You should undertake a threshold assessment to establish whether a PIA of your remote working arrangements is necessary. For more information about undertaking a threshold assessment, see the OAIC’s PIA Guide.  A PIA may not be necessary if your remote working arrangements do not change existing information handling practices, the privacy implications of these practices have been assessed previously (whether as part of a threshold assessment, a PIA or other risk-assessment process) and controls are current and working well. You may have considered the privacy issues through other mechanisms, like a risk assessment as part of your Business Continuity Plan. Regardless of whether you proceed to a PIA, you should keep a record of your threshold assessment.  How detailed does a PIA need to be?  There is no single way of doing a PIA and entities are encouraged to take a flexible approach. The scale and scope of a PIA will depend on the scale and scope of a particular project.  For example, if you have had remote working arrangements in place for some time and only minor adjustments are being made to the types of work that can be performed from home, a PIA may end up only a couple of pages long. If remote working arrangements will result in a significant change to your business-as-usual practices, including changes to the way personal information is handled, then the PIA may need to consider a broader range of issues.  A PIA doesn’t set out to identify and eliminate every possible privacy risk, however, it should identify any genuine risks that may be associated with your remote working arrangements, assess how serious those risks are, and consider ways that those risks can be mitigated.  Things to consider in a PIA of remote working arrangements  This section outlines key factors that you should consider in assessing personal information handling in remote working arrangements including:  Governance, culture and training ICT security Access security Data breaches Physical security This is not an exhaustive list and does not cover the entirety of an entity’s obligations under the APPs. You should read this section in conjunction with the list of additional resources below.  Governance, culture and training  Your privacy and security governance arrangements should include appropriate training, resourcing, documented policies and procedures, and management oversight to ensure you foster a culture of privacy and staff are aware of their privacy and security obligations when working remotely.  Questions to consider  What governance arrangements do you have in place around remote working arrangements? do you have a documented process for reviewing and approving applications to work remotely? how often are remote working arrangements reviewed to ensure they are still appropriate and effective for each staff member? Are staff members educated on physical security and the handling of personal information when working from home?  Are staff members educated on ICT and cyber security practices, such as identifying phishing or spear-phishing emails?  Is there a policy that covers information security when staff members work offsite, such as from home, a secondary site office or a temporary office?  Are there clear polices governing the use of end-user devices, including use of staff’s own devices (known as ‘Bring Your Own Device (BYOD)’) and procedures for taking work home?  ICT Security  As more staff work from home, and the use of remote technology increases, adversaries may attempt to take advantage of any real or perceived vulnerabilities introduced as a result of that change. ICT security measures help mitigate the risks of internal and external attackers and the damage caused by malicious software such as malware, computer viruses and other harmful programs.  Questions to consider  Do all devices, Virtual Private Networks and firewalls have necessary updates and the most recent security patches (including to operating systems and antivirus software) and have strong passwords?  Have you considered increasing cyber security measures in anticipation of the higher demand on remote access technologies and tested them ahead of time?  Have you implemented a secure method for staff to access your network and systems (eg. a secure remote desktop client)?  Do you use multifactor authentication for remote access to systems and resources (including cloud services)?  Are staff able to remotely access systems with their personal devices? What technical and procedural controls do you have in place to mitigate security risks associated with personal devices?  Have you assessed the privacy and security controls of any new technology, such as videoconferencing facilities, that you are using?  Are there strong minimum standards for security of end-user devices (such as password protection, encryption)?  Have technical solutions which block or mitigate the effects of phishing, spear-phishing and social-engineering attacks been applied (eg. are email attachments received from an external source scanned before they are open)?  Access security  Remote working arrangements may give rise to the ‘trusted insider risk’, particularly in circumstances where staff members are not subject to the same level of supervision and oversight as they would be in a traditional office environment. Access security and monitoring controls help you protect against internal and external risks by ensuring that personal information is only accessed by authorised persons.  Questions to consider  Do you limit access to personal information to those staff necessary to enable your entity to carry out its functions and activities?  Have you considered employing remote wiping software to allow for the deletion of personal information stored on end-user devices which have been lost or stolen?  Is password or passphrase complexity enforced? For example, including uppercase characters, lowercase characters, punctuation, symbols and/or numbers? Are there mechanisms for changing them regularly? Is reuse of passwords or passphrases blocked? Is there a minimum length requirement? Is sharing of passwords or passphrases forbidden? Do accounts lock the user out after a specified number of failed logins?  What methods do you use to identify inappropriate access of files or databases containing personal information? Do you use audit logs and audit trails?  Is access by both internal and external persons monitored? Is there a method for identifying anomalous behaviour?  Do you have the capability to proactively monitor access to systems to identify potential instances of unauthorised access or misuse? Have you considered whether to increase the use of that capability because of the change to the working environment?  Are these measures mainly reactive (review of logs, responding to incidents) or do they also involve real time or close to real time monitoring or access activity?  If anomalous behaviour is detected, what processes are used to immediately remove or reduce any risk, and then determine whether such behaviour amounts to unauthorised access, including any processes in place to assess whether the access might give rise to an eligible data breach for the purposes of the NDB scheme?  Data breaches  A data breach occurs when personal information that an entity holds is subject to unauthorised access or disclosure or is lost. A data breach may be caused by malicious action (by an external or internal party), human error, or a failure in information handling or security systems. Examples of data breaches that could occur when staff are working remotely include:  unauthorised access to systems containing personal information by an employee (the ‘trusted insider risk’)  unauthorised disclosure of personal information where a staff member discusses the personal information of another individual where it can be overheard by a third party (such as another member of the household), or enables a record of personal information to be seen by someone else (such as by leaving a computer screen unlocked or by making notes that are obtained or viewed by a third party), or  loss or theft of physical devices (such as a phone or laptop) or paper records that contain personal information.  Where personal information is compromised and is likely to result in serious harm to any of the individuals to whom the information relates, it must be notified to the OAIC and affected individuals in accordance with the NDB scheme.  In the event of a data breach, having a response plan that includes procedures and clear lines of authority can assist you to contain the breach and manage your response, including whether notification is necessary under the NDB scheme. Ensuring that staff (including contractors) are aware of the plan and understand the importance of reporting breaches is essential for the plan to be effective.  Questions to consider  Are staff aware of the agency’s data breach response plan and arrangements? Is it easily accessible by staff working from home?  Do changes need to be made to the method for notifying actual or suspected incidents if data breach response staff are working from home?  Does the data breach response team have the appropriate capacity under the new working arrangements to respond quickly to actual or suspected incidents? Do changes need to be made to the team to account for work from home arrangements?  Has the agency data breach response plan been tested via a simulated exercise involving a working from home arrangement to identifying whether any modifications are required strengthen to the plan?  Physical security  Physical security is an important part of ensuring that personal information held on your network is secure when accessed by staff working remotely. While it may not be possible to assess the individual physical security arrangements of each staff member’s workspace, agencies should consider other ways of facilitating good privacy and security practices.  Questions to consider  Have you considered whether there are certain work tasks that should not be performed from home where the privacy risks can’t be mitigated?  Have you considered how the risk of unauthorised disclosure can be further mitigated by modifying work tasks that are able to be performed from home (eg. increasing communication over email rather than the phone (if there is a risk of being overheard), re-allocation of matters to staff with a private home office, or nominating times where staff may come into the office to carry out certain essential tasks)?  Have you provided clear guidance regarding physical security measures that all staff working remotely are required to take? This should include directions around: working only from the home authorised and not in public spaces ensuring screens are angled so they cannot be viewed by anyone else and locked when not in use ensuring that no other member of the household uses work devices ensuring that phone conversations where personal information is disclosed cannot be overheard by other members of the household using generic terms (such as customer, client or complainant) on phone calls or in videoconferencing so that an individual is not reasonably identifiable storing devices (particularly work devices) in a safe location when not in use not making any hard copies of documents containing personal information not emailing any agency information including personal information to their personal email accounts not discussing or transmitting agency information, including personal information with colleagues, or third parties, via personal chat groups. Have you considered proactive measures to ensure staff have adequate physical security measures in their home? (eg. consider implementing an ongoing program of ‘spot checks’, which could be carried out through virtual or remote methods, to inspect staff members individual working arrangements)  Where staff do not have a private home office, consider what steps could be taken to enable a temporary workspace to be established in a separate room of the home, or redesign work tasks to remove the need to handle personal information.  Additional resources  You should also refer to the resources listed below where relevant to your entity.  OAIC resources  Guide to undertaking privacy impact assessments PIA e-Learning course Guide to securing personal information Data breach preparation and response guide Coronavirus (COVID-19): Understanding your privacy obligations to your staff Keep up to date with the latest advice from the Australian Cyber Security Centre  Agencies should ensure continued compliance with Protective Security Policy Framework requirements  Footnotes  [1] For the purposes of Part 3 of the Code, a project may be a high privacy risk project if the agency reasonably considers that the project involves any new or changed ways of handling personal information that are likely to have a significant impact on the privacy of individuals. The term ‘project’ covers the full range of activities and initiatives undertaken by agencies that may have privacy implications, including increased remote working arrangements.  [2] For more information, see the OAIC’s Guide to securing personal information.  [3] A data breach is eligible if it is likely to result in serious harm to any of the individuals to whom the information relates. Entities must conduct a prompt and reasonable assessment if they suspect that they may have experienced an eligible data breach. For more information, see Notifiable Data Breaches.  Related pages Guide to undertaking privacy impact assessments  Our suggested 10 step PIA process, intended for all APP entities Arrow Guide to securing personal information  'Reasonable steps' to protect personal information Arrow Coronavirus (COVID-19): understanding your privacy obligations to your staff  Privacy advice for entities during COVID-19 pandemic Arrow Did you find this helpful? This is helpful Yes This is not helpful No   Share Facebook Twitter Linkedin    OAIC logo  OAIC sub logo Copyright Terms and conditions Privacy policy Accessibility Contact us 1300 363 992 Monday to Thursday 10 am to 4 pm (AEST/AEDT) Other languages  Follow us OAIC on Facebook OAIC on Twitter OAIC on Youtube OAIC on Linkedin Acknowledgement of Country The OAIC acknowledges Traditional Custodians of Country across Australia and their continuing connection to land, waters and communities. We pay our respect to First Nations people, cultures and Elders past and present. @ Commonwealth of Australia, MIT licensed

---
## [cilium/linux](https://github.com/cilium/linux)@[fb9c24bb3d...](https://github.com/cilium/linux/commit/fb9c24bb3d675593e20cfaba2a97e741700bbe3b)
#### Thursday 2023-07-06 12:12:26 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer.
tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail. The work has been tested with tc-testing selftest suite
which all passes, as well as the tc BPF tests from the BPF CI, and also with
Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com/
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com/

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[dad66dcd73...](https://github.com/cilium/linux/commit/dad66dcd73356ec9fc4d2ac7a3482fe3dd97d54e)
#### Thursday 2023-07-06 12:12:26 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_{FIRST,LAST}
      - Enforced throughout the bpf_mprog state's lifetime
      - Admin override possible (e.g. link detach, prog-based BPF_F_REPLACE)
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space daemon can query current state with revision, and pass it along
    for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure) and bpf_mprog_cp (control-path
structure). Both have been separated, so that fast-path gets efficient packing
of bpf_prog pointers for maximum cache efficieny. Also, array has been chosen
instead of linked list or other structures to remove unnecessary indirections
for a fast point-to-entry in tc for BPF. The bpf_mprog_entry comes as a pair
via bpf_mprog_bundle so that in case of updates the peer bpf_mprog_entry
is populated and then just swapped which avoids additional allocations that
could otherwise fail, for example, in detach case. bpf_mprog_{fp,cp} arrays are
currently static, but they could be converted to dynamic allocation if necessary
at a point in future. Locking is deferred to the in-kernel user of bpf_mprog,
for example, in case of tcx which uses this API in the next patch, it piggy-
backs on rtnl. The nitty-gritty details are in the bpf_mprog_{replace,head_tail,
add,del} implementation and an extensive test suite for checking all aspects
of this API for prog-based attach/detach and link API as BPF selftests in
this series.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[dfd6239ed5...](https://github.com/cilium/linux/commit/dfd6239ed587090339679854087d7482a7f9bee7)
#### Thursday 2023-07-06 12:41:09 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space daemon can query current state with revision, and pass it along
    for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficieny. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.

Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [goauthentik/authentik](https://github.com/goauthentik/authentik)@[f179d6572e...](https://github.com/goauthentik/authentik/commit/f179d6572e2e3776c53efbecb0ed9957af2ecd46)
#### Thursday 2023-07-06 12:46:42 by Ken Sternberg

web: Storybook css import fix (#5964)

* web: fix storybook `build` css import issue

This is an incredibly frustrating issue, because Storybook works
in `dev` mode but not in `build` mode, and that's not at all what
you'd expecte from a mature piece of software.  Lit uses the native
CSS adoptedStylesheets field, which takes only a constructedStylesheet.
Lit provides a way of generating those, but the imports from
Patternfly (or any `.css` file) are text, and converting those to
stylesheets required a bit of magic.

What this means going forward is that any Storied components will
have to have their CSS wrapped in a way that ensures it is managed
correctly by Lit (well, to be pedantic, by the
shadowDOM.adoptedStylesheets).  That wrapper is provided and the
components that need it have been wrapped.

This problem deserves further investigation, but for the time
being this actually does solve it with a minimum amount of surgical
pain.

* web: fix storybook build issue

This commit further fixes the typing issues around strings, CSSResults,
and CSSStyleSheets by providing overloaded functions that assist
consumers in knowing that if they send an array to expect an array
in return, and if they send a scalar expect a scalar in return.

* replace any with unknown

Signed-off-by: Jens Langhammer <jens@goauthentik.io>

---------

Signed-off-by: Jens Langhammer <jens@goauthentik.io>
Co-authored-by: Jens Langhammer <jens@goauthentik.io>

---
## [cilium/linux](https://github.com/cilium/linux)@[eba4518b99...](https://github.com/cilium/linux/commit/eba4518b995c2f858f1d9a360faf69595674ebce)
#### Thursday 2023-07-06 13:12:41 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[0af7758896...](https://github.com/cilium/linux/commit/0af7758896e045cf498ea118c7fccac8457bd8e2)
#### Thursday 2023-07-06 13:15:26 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [knative-automation/client-pkg](https://github.com/knative-automation/client-pkg)@[41013a049d...](https://github.com/knative-automation/client-pkg/commit/41013a049de82b42f3ad1882a51a854575c57c2e)
#### Thursday 2023-07-06 13:28:43 by Knative Automation

upgrade to latest dependencies

bumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping knative.dev/hack f591fea...fc42790:%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/tools b3b5c13...d0863f0:%0A  > d0863f0 go.mod: update golang.org/x dependencies%0A  > 545ca87 gopls/internal/regtest/marker: require go/packages%0A  > 1ace7db go,gopls: remove license from package doc comments%0A  > ebad375 gopls/internal/lsp/protocol: prevent license rendering in godoc%0A  > 10a39ef gopls/internal/lsp/regtest: address additional comments on marker.go%0A  > 69920f2 gopls/internal/regtest/marker: add missing tests for hover%0A  > 24a13c6 gopls/internal/regtest: fill out features of the new marker tests%0A  > 2b149ce gopls/internal/regtest: add a regtest-based version of the marker tests%0A  > edddc5f go/packages: don't discard errors loading export data%0A  > a762c82 go/ssa: add MultiConvert instruction%0A  > f124b50 cmd/stringer: streamline test subprocesses%0A  > 6b6857a gopls: fix typos in comments and doc%0A  > 8111118 go/analysis/internal/facts: fix cycle in importMap.%0A  > dd1c468 gopls/internal/lsp/source: simplify extracting object hover doc%0A  > 66f8f71 gopls/internal/lsp/source: use syntax alone in FormatVarType%0A  > 30f191f internal/imports: update stdlib index for Go 1.20%0A  > 4e98188 internal/imports: use go/packages instead of cmd/api to compute symbols%0A  > 4e8ff89 internal/imports: update stdlib index for 1.20%0A  > 6bd0d00 gopls/internal/lsp: go to definition from linkname directive%0A  > 0cfddb3 gopls/internal/lsp: enable clear builtin completion test%0A  > 41adf8d gopls/internal/lsp/tests: remove StripSubscripts%0A  > 86fdadc gopls/internal/lsp/safetoken: delete safetoken.Range%0A  > c276ee5 internal/robustio: fix signature of getFileID on plan9%0A  > e170d45 gopls/internal/lsp: add clear builtin%0A  > 2ea4b81 go/ast/inspector: skip ranges that do not contain a node type%0A  > 407bbed go/analysis: improve error message on duplicate fixes%0A  > bd5dfbb all: fix some comments%0A  > 072fca5 gopls/protocol: use the current definition of the lsp%0A  > aa633e7 tools/gopls: provide markdown for completion and signature help%0A  > 684a1c0 go/analysis/internal/analysisflags: use os.Executable for program path%0A  > bd5e595 gopls/internal/lsp/cache: add missing mutex%0A  > 2683128 gopls/internal/lsp: differentiate govulncheck/vulncheck imports diags%0A  > d1e92d6 gopls/internal/lsp/mod: reorder vulncheck quick fixes%0A  > 87d00e6 gopls/internal/lsp: separate some requests from source.Identifier%0A  > ae242ec gopls: fix windows file corruption%0A  > 6f65213 gopls/internal/lsp/protocol: Mapper.NodeMappedRange%0A  > e260368 gopls/semantic: report type parameters in the type of a receiver%0A  > b62cbb6 internal/lockedfile: fix build constraints on solaris%0A  > 1aa7e72 gopls/internal/lsp/source: avoid qualifiedObjectsAtProtocolPos%0A  > 5ed33df gopls/internal/lsp/source: rename: prep for incrementality%0A  > e0659d1 gopls/internal/lsp/source: simplify legacy 'references' func%0A  > 1edcfe7 gopls/internal/regtest/diagnostics: require cgo for TestGoListErrors%0A  > f052158 gopls/internal/lsp/protocol: move TestBytesOffset%0A  > d093a13 gopls/internal/lsp/protocol: LocationTextDocumentPositionParams%0A  > bcb677e gopls/internal/regtest: make RegexpSearch return a Location%0A  > 60782e9 gopls/internal/lsp/source: eliminate a couple uses of posToMappedRange%0A  > 031e6e6 gopls/internal/lsp/source: eliminate ResolveImportPath%0A  > f2cd9ef gopls/internal/lsp/source: reduce usage of TypecheckWorkspace%0A  > f10e7d5 gopls/internal/lsp/cache: remove package dependence on packages.Config%0A  > 8270757 gopls/internal/lsp/source: switch call hierarchy to references v2%0A  > 37c69d8 gopls/internal/lsp/source: references: support exported methods%0A  > f3c36a2 gopls/internal/lsp/cmd/test: delete marker-based tests of gopls cmd%0A  > c224aae gopls/internal/lsp/cmd/test: new integration test for gopls command%0A  > deeb64b gopls/internal/lsp/source/xrefs: allow Lookup of a set%0A  > f269f53 gopls/internal/lsp: remove Server.processModifications%0A  > fcd57eb gopls: allow 'any' and 'comparable' in completion results%0A  > aae3642 gopls/internal/lsp/source: referencesV2: support unexported methods%0A  > b5d65e0 tools/gopls: register semantic tokens statically%0A  > 51abc5b gopls/internal/lsp/source: stub: don't panic when encountering 'error'%0A  > ce28f40 gopls/internal/regtest: add a test demonstrating confusion following an%0A  > c4c6aa6 internal/lsp/cache: don't panic in Snapshot on a shutdown view%0A  > 1faecd3 tools/internal/diff: fix off-by-one error in computing diffs%0A  > a7f033a gopls/internal/lsp: consolidate the FileHandle API%0A  > 271e621 internal/lockedfile/internal/filelock: fix aix build tag%0A  > ff9bea5 gopls/internal/lsp/cmd/test: signpost future cleanups%0A  > 7d4ba2f gopls/release: remove unused functionality from release script%0A  > 46b6958 gopls/internal/lsp/source: delete source_test%0A  > bcc7794 go/analysis/passes/directive: add directive analyzer%0A  > 33d416e gopls/internal/lsp: add missing comments on 3x tests.Test impls%0A  > afea272 gopls/internal/lsp/source: make implementations2 work on embedded fields%0A  > bb7c440 gopls/internal/lsp/filecache: use file locking, not rename%0A  > 561a9be gopls/internal/lsp/filecache: actually delete files%0A  > 9682b0d gopls/internal/lsp/source: delete IsInterface%0A  > 7a7b699 go/analysis/passes/loopclosure: avoid panic in new parallel subtest check when t.Run has single argument%0A  > 3e6f71b gopls/internal/regtest: use AfterChange in more places%0A  > 9ff31a5 x/tools/go/analysis/passes/printf: revert URL in error message%0A  > 2fa6ca1 gopls/internal/lsp/source/impls: a new "implementations" index%0A  > 957bec5 gopls/protocol: new versions of generated LSP files%0A  > f0e2d5c internal/gcimporter: discard position info for unneeded lines%0A  > 5bedd86 cmd/digraph: use ReadString rather than bufio.Scanner%0A  > f6ea009 gopls/internal/lsp: remove the experimentalWatchedFileDelay setting%0A  > f46e418 gopls/internal/lsp/source: include ITVs in global references%0A  > f3e53e5 internal/jsonrpc2_v2: fix typos%0A  > d958e85 internal/gcimporter: use two-level file index%0A  > 8aba49b internal/gcimporter: preserve column and line in shallow iexport%0A  > d7fc4e7 gopls: new LSP stub generator%0A  > 5c176b1 internal/robustio: skip os.Link test on android%0A  > d34a055 go/ssa: sanity check the types of phi nodes%0A  > 6f095b4 go/callgraph/vta: add flows for receiver function types%0A  > 8e94967 cmd/fiximports: do not assume go list -json unmarshals into build.Package%0A  > e035d0c go/ssa: fix phi node type in slice to array conversion%0A  > 03eac81 go/expect: remove testdata go.mod to go.fake.mod%0A  > 1e819a3 gopls/internal/regtest: follow-ups to review comments from earlier CLs%0A  > 9ba8bb1 gopls/internal/regtest: clean up workspace symbol helpers%0A  > 91b6070 gopls/internal/regtest: eliminate DiagnosticAtRegexp%0A  > bd48b9a gopls/internal/regtest: eliminate DiagnosticsAtRegexpWithMessage%0A  > 5d65394 gopls/internal/regtest: eliminate DiagnosticAt%0A  > 27dfeb2 gopls/internal/regtest: replace NoDiagnostics with NoMatchingDiagnostics%0A  > 87092c8 gopls/internal/lsp/fake: use protocol types for the fake editor%0A  > 672a036 gopls/internal/regtest: simplify OnceMet expressions with an env helper%0A  > ab7b5b2 gopls/internal/regtest: eliminate GoSumDiagnostic%0A  > 331a1c6 gopls/internal/regtest: add a simpler API for diagnostic expectations%0A  > c9b82f2 gopls/internal/regtest: eliminate EmptyDiagnostics%0A  > e81af27 gopls: update golang.org/x/vuln@6ad3e3d%0A  > d19e3d1 internal/regtest/bench: fix BenchmarkRename and add more benchmark tests for gopls%0A  > 2be1a9a gopls/internal/regtest: rename EmptyOrNoDiagnostics to NoDiagnostics%0A  > 7ec05ac gopls/internal/regtest: eliminate NoDiagnostics%0A  > e956495 gopls/internal/regtest: eliminate DiagnosticsFor%0A  > 8087911 gopls: remove the experimentalWorkspaceModule mode%0A  > 5b300bd gopls/internal/lsp/cache: clean up view workspace information%0A  > 97d5de5 gopls/internal/cache: don't mark initialized after cancellation%0A  > 58691bc gopls/internal/lsp/glob: add an LSP compliant glob implementation%0A  > a3c22fc cmd/cover: delete package%0A  > 98dcb0e cmd/cover: remove replace directive%0A  > 7765567 gopls/internal/lsp/source: minor clarifications%0A  > a7f7db3 cmd/cover: carve out deprecated command into its own module%0A  > f9a10c0 Revert "cmd/cover: carve out deprecated command into its own module"%0A  > e345d46 internal/gcimporter: fix export of invalid methods%0A  > 4305a22 gopls/internal/lsp/cache: don't cache files if mtime is too recent%0A  > 227ee72 internal/regtest/misc: fail eagerly in TestRenameFileFromEditor%0A  > 43158af cmd/cover: carve out deprecated command into its own module%0A  > b798934 gopls/internal/lsp/protocol: cleanups and docs for Mapper%0A  > a24944e gopls/internal/lsp/protocol: rename s/ColumnMapper/Mapper/%0A  > 55935f4 gopls/internal/span: simplify Span%0A  > 40a1c97 gopls/internal/lsp/lsppos: delete Mapper%0A  > 6a3bc37 gopls/internal/lsp/protocol: reimplement ColumnMapper line logic%0A  > 6e9a35d go/callgraph/cha: refactor callee construction%0A  > fef5b76 go/callgraph: fix slicing in callgraph_test.go%0A  > 2be9d05 gopls/internal/lsp/source/xrefs: a new reference index%0A  > 0362cea gopls/internal/lsp/lsppos: delete TokenMapper%0A  > 67baca6 go/callgraph/vta: optimize scc computation%0A  > 2eb6138 gopls/internal/lsp/filecache: use TempDir if UserCacheDir fails us%0A  > 36bd3db gopls/internal/lsp/protocol: move MappedRange%0A  > 16b3bf8 gopls/internal/lsp/cache: assume Go 1.16+%0A  > 3856a5d internal/robustio: add Plan9 support to FileID%0A  > 09cbc42 gopls/internal/lsp/fake: fix EOF bug in applyEdits%0A  > 4ded35d gopls/internal/lsp/cache: use distinct types for mod and work parse keys%0A  > 107f43f gopls/completion: avoid duplicating text in test func completions%0A  > e225fd4 gopls/internal/lsp/mod: fix nil panic in go.mod hover%0A  > 057ed3c gopls/internal/lsp/filecache: use os.Chtimes%0A  > 1fe76af gopls/internal/lsp/source: MappedRange cleanup%0A  > 02bea03 gopls/internal/lsp/protocol: simplify ColumnMapper%0A  > a4455fe go/callgraph: adds benchmarks comparing algorithms%0A  > 7db99dd go.mod: update golang.org/x dependencies%0A  > 1e0dff2 gopls/internal/regtest: avoid race in TestSwitchFromGOPATHToModuleMode%0A  > 0441b43 gopls/internal/lsp/cache: use specific mutexes for module data%0A  > 33071fb internal/robustio: move robustio%0A  > b01e7a4 gopls/internal/regtest/watch: don't run TestSwitchFromGOPATHToModuleMode%0A  > e417ea3 gopls: remove dead analysis code%0A  > 1a08d01 gopls/internal/lsp: update replace directives in go.mod for package renaming%0A  > eac36cb gopls/internal/regtest: port experimental workspace tests to go.work%0A  > 224a61b gopls/internal/lsp/source: delete Snapshot.WriteEnv method%0A  > 81e741e gopls/internal/lsp/safetoken: funnel more calls through this package%0A  > 8367fb2 gopls/internal/regtest: await go.work changes in TestAddAndRemoveGoWork%0A  > 3b16059 gopls/internal/regtest: make BufferText strict%0A  > 0e1d013 gopls/internal/lsp/cache: recreate Views when their root changes%0A  > 2f31dd4 go/ssa,go/analysis/passes/nilness: refine when type param constants are nil%0A  > ae4ff82 gopls/internal/lsp/source: delete GetTypedFile%0A  > fe6b300 gopls/internal/lsp/source: eliminate Snapshot.Package{,s}ForFile%0A  > 26fc609 gopls/internal/lsp/cache: eliminate snapshot.containingPackages%0A  > 85e6ad7 gopls/internal/lsp/safetoken: fix bug in Offset at EOF%0A  > ef1ec5d gopls/internal/lsp/safetoken: fix error message%0A  > 44395ff gopls/internal/lsp/source: avoid unnecessary transitive rdeps%0A  > 6546d82 Revert "gopls/internal/regtest: harmless CL used for benchmark test"%0A  > 3be0647 gopls/symbols: call source.Document symbols only for Go files%0A  > d462c83 gopls/internal/lsp: Replace input text when completing a definition%0A  > 7efffe1 gopls/internal/regtest: harmless CL used for benchmark test%0A  > 1627e95 gopls/internal/lsp: more comment tweaks post-//line support%0A  > 21f6100 internal/lsp/debug: fix broken template%0A  > 6ad27d0 gopls/internal/robustio: FileID, a portable file identifier%0A  > 6df6eee internal/diff/lcs: optimize inner loop%0A  > 57b1265 go/gcexportdata: drop support for go1.6 export data%0A  > 099260e gopls/internal/lsp: followups to dropping line directives%0A  > 61e2d3f gopls/internal/lsp/cache: a new analysis driver%0A  > eb70795 gopls: ignore //line directives%0A  > b4dfc36 go/ssa: deref core type in emitLoad%0A  > 1270fd7 gopls/internal/lsp: announce selectionRangeProvider capability%0A  > 9bc5dce gopls/internal/lsp/cache: simplify DiagnosePackage%0A  > df35cd8 x/tools: drop support for Go toolchains older than go1.16%0A  > db9d10f go/gcexportdata: preallocate buffer to read into when size is known%0A  > 0d2045b gopls/internal/lsp: document analysis-related functions%0A  > b2b9dc3 gopls/internal/lsp/cache: reduce type-checking in renameImports%0A  > 3cb82d5 go/ssa/interp: fix conversion of slice to named array%0A  > 5899b6a gopls: upgrade dependencies following release%0A  > 763a030 gopls/internal/lsp/cache: delete Snapshot.KnownPackages%0A  > cc0e696 gopls/internal/hooks: panic if diff consistency check fails%0A  > 9ec8553 gopls/internal/lsp/source: emit interface stub methods at top level%0A  > 444c8f6 gopls/internal/lsp/cache: only invalidate parsed files if they changed%0A  > 601ca6c gopls/internal/lsp/source: use correct token.File%0A  > 95c9dce internal/lsp/mod: fix run_govulncheck codelens name%0A  > d72a64a gopls/internal/lsp: add selection range request%0A  > 18f76ec gopls/internal/lsp: split ActivePackages%0A  > 84299a0 gopls/internal/lsp/cache: simplify ad-hoc package warning logic%0A  > a3eef25 gopls/internal/lsp/cache: record parse keys when they're created%0A  > 3da7f1e gopls/hover: remove header tags from hover markdown%0A  > a310bcb gopls/internal/lsp/source: eliminate getStubFile%0A  > 3cba5a8 internal/gcimporter: port CL 424876 from std importer%0A  > b0fdb78 gopls/internal/lsp/mod: add Reset vulncheck result codelens%0A  > 88ceb24 gopls/internal/lsp: perform analysis unconditionally%0A  > 3f74d91 gopls/internal/lsp/cache: invalidate govulncheck results older than 1hr%0A  > 6b8674f gopls/internal/lsp/source: avoid typechecking in findRune%0A  > d7dfffd gopls/internal/lsp: eliminate more unnecessary typechecking%0A  > f3fb218 gopls/internal/lsp/fake: use robustio.RemoveAll in (*Workdir).RemoveFile%0A  > 96ff41d gopls/internal/vulncheck: add TODO for the vulncheck diagnostics%0A  > 0f6c6f1 gopls: delete obsolete govulncheck code and stop gopls vulncheck -summary%0A  > c5343a6 gopls/internal/lsp/regtest: fix TestRunGovulncheckError2%0A  > cb701f7 gopls/internal/lsp: avoid type-checking when computing hyperlinks%0A  > d0f184d gopls/internal/lsp/source: avoid unnecessary calls to GetTypedFile%0A  > 1e5efed gopls/internal/lsp/fake: simply use polling to simulate file watching%0A  > 838a165 gopls/internal/lsp/fake: eliminate the unnecessary fake.FileEvent%0A  > 09fb680 gopls/internal/lsp/fake: eliminate the unnecessary ChangeFilesOnDisk API%0A  > 09ae2d5 gopls/internal/lsp/source: KnownPackagePaths: avoid loading%0A  > 1dcc423 gopls/internal/lsp/cache: split metadata and loading in PackagesForFile%0A  > 6b50501 gopls/release: fix the release script when go.work is not used%0A  > aee3994 gopls/internal/lsp/fake: in (*Workdir).RenameFile, fall back to read + write%0A  > fe60148 go.mod: update golang.org/x dependencies%0A  > c9ea9a7 gopls/internal/regtest: add a test for the case when the renaming package's path contains "internal" as a segment%0A  > bf5db81 gopls/internal/lsp/cache: improve ad-hoc warning for nested modules%0A  > aa9f4b2 go/analysis: document that facts are gob encoded in one gulp%0A  > bdcd082 internal/gcimporter: skip tests earlier when 'go build' is not available%0A  > 2ad6325 gopls/internal/lsp/cache: expand ImportPath!=PackagePath comment%0A  > 52c7b88 gopls/internal/robustio: only define ERROR_SHARING_VIOLATION on Windows%0A  > 4f69bf3 gopls/internal/lsp/cache: narrow reloadOrphanedFiles to open files%0A  > 6002d6e gopls/internal/regtest/misc: test Implementations + vendor%0A  > f540ee6 internal/gcimporter: load cached export data for packages individually%0A  > d444fa3 gopls/internal/lsp/cache: simplify canonical URI cache%0A  > 25fdb81 gopls/internal/regtest/misc: skip vendor test on go1.13%0A  > e0b516b gopls/internal/lsp/cache: invalidate metadata after vendor change%0A  > 31d5843 gopls/internal/lsp/cache: fix re-entrant session locking%0A  > 8c78b30 gopls/internal/vulncheck: always use pkg.go.dev/vuln for urls%0A  > 47a8246 gopls/internal/regtest/misc: skip TestRunGovulncheckError2%0A  > d54e12b gopls/internal/lsp: avoid I/O in URI comparison operations%0A  > 0379b73 internal/gcimporter: fix TestImportStdLib%0A  > e79e423 gopls/internal/vulncheck: handle package errors%0A  > c5ce806 gopls/internal/lsp/mod: disable the diagnostics on stdlib vulns%0A  > 78c1861 gopls/internal/vulncheck: clarify the log message%0A  > 1a0053c gopls: move reset go.mod diagnostic codelens to module statement%0A  > 9b8d87b gopls/internal/regtest: fix TestRunGovulncheckStd%0A  > 81b6bef gopls/internal/lsp: add run vulncheck fix for stdlib vulns%0A  > fe83ddb gopls/internal/lsp: move options off of the cache%0A  > 88ee30b gopls/internal/lsp/source: enable run_govulncheck codelens in exp mode%0A  > 0a6aa90 gopls/internal/lsp/command: rename run_vulncheck_exp to run_govulncheck%0A  > bedad5a gopls/internal/lsp/mod: add hover for stdlib vulnerabilities%0A  > 7a1b570 gopls/internal/vulncheck: check vulnerabilities in standard library%0A  > 9a54670 gopls/internal/lsp/mod: add "Run govulncheck" codeaction%0A  > f1b76ae gopls/internal/lsp: add an option to overwrite previous diagnostics%0A  > e8a70a5 gopls/internal/lsp: remove access to mutable session state from the view%0A  > ff22fab gopls/internal/lsp/cache: eliminate obsolete invalidation step%0A  > 3881046 gopls: add a go:generate rule for doc generation%0A  > 4c3cb1e internal/gocommand: add GoVersionString%0A  > e29d1ed gopls: add diagnostic for standard library%0A  > f718365 gopls/internal/lsp: include all vulns info to fetch_vulncheck_result%0A  > 9519368 gopls/internal/lsp/mod: add the vulncheck diagnostics mode%0A  > 7d9f451 gopls/internal/govulncheck: add in-memory cache for vulndb%0A  > 1ccccf8 go/ssa: deprecate coreType and _NormalTerms%0A  > 4b7d1b3 gopls: add diagnostics for both vulns used and not used%0A  > 50ccef5 internal/regtest/bench: add benchmark tests for gopls%0A  > d39685a gopls/internal/lsp/source: Package clarifications%0A  > 7cfde84 gopls/internal/vulncheck: add import info based vuln scanning%0A  > 2b56641 internal/gcimporter: adjust the number of expected packages in TestStdlib%0A  > 50df761 gopls: skip vulnerabilities that are probably fixed in hover%0A  > 7cda55e gopls/internal/lsp/cache: wire in mod vulnerability analysis%0A  > 5c35617 gopls: add quick fixes for all vulnerabilities%0A  > fb7be64 gopls/internal/lsp/command: return the vulncheck progress token%0A  > 060c049 go/packages: fix doc typo%0A  > 6eafd96 gopls: fix formatting for vulncheck results in hover%0A  > b797704 go/analysis/passes/loopclosure: recursively check last statements in statements like if, switch, and for%0A  > 3b9d20c internal/gcimporter: in TestStdlib, only check x/tools packages if we expect to have their source%0A  > 2ad3c33 go/packages: change workaround for issue 28749 to not require NeedFiles%0A  > 57f56ab gopls/internal/lsp/source: avoid panic(nil)%0A  > 41c70c9 internal/lsp/source: avoid using go/types.Implements with Typ[Invalid]%0A  > db5eae2 analysis: correct go/analysis/passes/findcall path in docs%0A  > b978661 cmd/godoc: streamline test subprocesses%0A  > 932ec22 internal/testenv: add a Command function that replaces exec.Command%0A  > 19fb30d gopls/internal/lsp/cache: fix data race in Symbols%0A  > 4ce4f93 gopls/internal/lsp: add gopls.fetch_vulncheck_result%0A  > 8ba9a37 gopls/internal/lsp/mod: highlight when there is no fix for vuln%0A  > 128f61d gopls/internal/lsp/mod: add related info%0A  > fc03993 internal/lsp/mod: adjust vulncheck diagnostics suppression logic%0A  > c099dff gopls/internal/vulncheck: log progress%0A  > 36a5c6a go/ssa: build generic function bodies%0A  > 85bf7a8 gopls/internal/lsp/source: eliminate Metadata interface%0A  > 2592a85 gopls/internal/lsp: simplify KnownPackages%0A  > c7ed4b3 gopls/internal/lsp/cache: clean up tracking of GO111MODULE%0A  > 23056f6 internal/lsp/cache: clean up getOrLoadIDsForURI%0A  > 5a4eba5 internal/lsp/cache: remove support for invalid metadata%0A  > 32a17c0 gopls/internal/lsp/mod: fix unaffecting vuln diagnostics msgs%0A  > dea100b internal/testenv: skip tests that need export data for std if 'go tool compile' does not exist%0A  > ba373ee playground/socket: eliminate an arbitrary timeout in TestLimiter%0A  > 3d085f3 gopls/internal/lsp/lsprpc: eliminate arbitrary timeout in TestEnvForwarding%0A  > 434d569 gopls/internal/lsp/regtest: improve documentation%0A  > ce26db4 go/analysis: add Pass.TypeErrors field%0A  > b0ad6b2 gopls/internal/regtest/misc: fix use of the AfterChange API%0A  > 89856a4 gopls/semantic: semantic tokens for type parameters%0A  > 6e8da3f internal/pkgbits: port small optimization from compiler to tools%0A  > 06fb723 internal/gcimporter: port memory reuse optimizations from Go tree%0A  > fc702c5 internal/gcimporter: fix performance regression for unified IR%0A  > 1cb4c17 gopls/internal/regtest: make AfterChange do the awaiting%0A  > 0c71b56 gopls/internal/lsp: fix diagnostic suppression when folders change%0A  > e3b3c01 go/pointer: break TestInput into subtests and update skips%0A  > 13648cd gopls/internal/lsp/cache: use Package.FileSet where possible%0A  > 8f32411 cmd/stringer: replace ioutil with os%0A  > 3c3713e gopls/internal/lsp/cache: use typed strings (PackagePath et al) throughout%0A  > 004d118 gopls/internal/lsp/mod: simplify ModVulnerabilityDiagnostics%0A  > 4a8413c gopls/internal/lsp/mod: deleted unused function pkgVersion%0A  > bc08991 gopls: sync golang.org/x/vuln@3af8368ee4fe%0A  > d66e9b4 internal/typesinternal: update go/types error codes for 1.20%0A  > 6f99366 gopls/internal/lsp/cache: don't pass snapshot.fset to go/packages%0A  > d56532a cmd/compilebench: make it work without installed .a's%0A  > 502c634 go.mod: update golang.org/x dependencies%0A  > bd04e32 internal/jsonrpc2_v2: eliminate a potential Accept/Dial race in TestIdleTimeout%0A  > d41a43b internal/jsonrpc2_v2: fix a potential deadlock when (*Conn).Close is invoked during Bind%0A  > 3057465 gopls/doc: Add plugin for Lapce to gopls documentation%0A  > ba92ae1 internal/persistent: avoid incorrect map validation due to multiple keys%0A  > 9474ca3 gopls/doc: clarify `go work use`%0A  > 003fde1 internal/gcimporter: use nondeprecated go/packages mode bits%0A  > 5050657 gopls/fake: add semantic token modifiers to fake editor%0A  > 88a3548 gopls/coverage: repair coverage.go%0A  > 8e0240a internal/regtest/workspace: permanently skip TestDeleteModule_Interdependent%0A  > fe725d9 gopls/internal/regtest: simplify awaiting diagnostics from a change%0A  > 3c8152e internal/gcimporter: optimize dependency lookup%0A  > 39c2fd8 internal/lsp/cache: simplify importsState modfile hashing logic%0A  > ec044b1 gopls: update dependencies following the v0.10.0 release%0A  > 2b29c66 internal/gcimporter: API for shallow export data%0A  > affa603 internal/gcimporter: moved from go/internal/gcimporter%0A  > a77a1fb gopls/internal/lsp/mod: fix vulncheck hover message%0A  > 4ada35e gopls/internal/lsp: handle modVulncheckSource in diagnosticSource.String%0A  > e5f03c1 gopls/doc: clean up README and add a release policy%0A  > d5e9e35 go/analysis/passes/loopclosure: enable analysis of parallel subtests%0A  > 039b24b internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 32e1cb7 gopls/internal/lsp: clarify control around diagnostics%0A  > feeb0ba gopls/internal/lsp/cmd: fix deadlock when opening a file%0A  > 6e9dc86 gopls/internal/lsp/source/completion: fix panic in completion on *error%0A  > 73fcd88 Revert "internal/jsonrpc2_v2: initiate shutdown when the Writer breaks"%0A  > 70a130e gopls/api-diff: simplify the api-diff implementation%0A  > 3e8da47 internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 3566f69 gopls/internal/lsp/source: minor space optimizations%0A  > 7cdb0e7 internal/jsonrpc2_v2: rename Serve to NewServer and eliminate its error return%0A  > 28e9e50 internal/jsonrpc2_v2: eliminate error return from Bind%0A  > eabc3a0 internal/jsonrpc2_v2: eliminate isClosingErr%0A  > 4885f7c internal/jsonrpc2_v2: eliminate a temporary connection leak in (*Server).run%0A  > 739f55d internal/jsonrpc2_v2: rework Connection concurrency%0A  > e172e97 go/types/typeutil: break recursion through anonymous interfaces%0A  > f1c8f7f internal/lsp/source: optimize filter regular expression%0A  > e074ef8 gopls/internal: don't show a warning if the Go version is undetected%0A  > 7fba77c gopls/internal/lsp/source: remove deprecated settings from EnableAllExperiments%0A  > 42cb7be gopls/internal/lsp: improve the Go version deprecation message%0A  > 2af106e gopls/internal/hooks: fixes to diff disaster logic%0A  > e4bb343 go/internal/gcimporter: update to anticipate missing targets and .as%0A  > 875c31f go/internal/gcimporter: add test of export/import on std%0A  > 541f4c5 cmd/bundle: quote command-line arguments in output%0A  > de675d5 tools/gopls: argument in function bodies marked as parameter by semantic tokens%0A  > 3e1371f gopls/internal: start on LSP stub generator in Go.%0A  > 121f889 gopls/internal/lsp/mod: merge vuln diagnostics to one, and add a hover%0A  > d6511e5 internal/facts: share go/analysis/internal/facts with gopls%0A  > 2e0ca3a go/internal/gcimporter: fix bug in struct iexport%0A  > 1928cea go/ssa: emit field and index lvals on demand%0A  > 8166dca go/analysis/passes/asmdecl: define register-ABI result registers for RISCV64%0A  > 2dcdbd4 go/internal/gcimporter: port CL 431495 to tools, add tests%0A  > d476af7 go/ssa: add slice to array conversion%0A  > d212f7d gopls/internal/regtest/workspace: fix bugs in test%0A  > 051f03f gopls/internal/lsp/cache: remove unnecessary params%0A  > 21f6127 gopls/internal/lsp/cache: add PkgPath->PackageID index to Metadata%0A  > 06041c9 gopls/doc: update manual documentation of the newDiff setting%0A  > f112c43 go.mod: update golang.org/x dependencies%0A  > 207f456 go/internal/gcimporter: bump version number in skew check%0A  > 65196ca gopls/README.md: fix wording around supported Go versions%0A  > 6128030 gopls/internal: support renaming packages with int. test variants%0A  > 649df2e go.mod: mark as requiring -compat 1.16%0A  > 91311ab gopls/internal/lsp/cache: better import path hygiene%0A  > 9eda97b go/analysis: enable a test that applies after go list behavior change%0A  > b50d7ba gopls: minor cleanup of standalone package support%0A  > 502b93c gopls/internal/lsp: tolerate missing end position in RelatedInformation%0A  > d67c3ad internal/imports: repair warnings from default analyzers%0A  > bc2e3ae internal/jsonrpc2_v2: add Func convenience wrappers for the Binder and Preempter interfaces%0A  > a9b653b cmd/compilebench: use -a instead of -i to ensure dependencies are built%0A  > 4818d9e Revert "gopls/internal/lsp/cache: disable strict analysis while we fix panics"%0A  > b2efd4d internal/jsonrpc2_v2: eliminate most arbitrary timeouts in tests%0A  > 371ef16 internal/jsonrpc2_v2: rework concurrency in idleListener%0A  > 5935531 internal/jsonrpc2_v2: remove “Box” suffix from channel field names%0A  > fd32990 internal/jsonrpc2_v2: error out in-flight client calls when the reader breaks%0A  > 0e222f5 internal/jsonrpc2_v2: close the underlying connection if Wait is called instead of Close%0A  > bc4e384 gopls/internal/lsp/cache: fix crash in analysis%0A  > b93a56f refactor/satisfy: fix visiting functions in the unsafe package%0A  > 9b5e55b gopls/internal/lsp/cache: disable strict analysis while we fix panics%0A  > 9ffaf69 gopls/internal/lsp/cache: minor analysis cleanups%0A  > ffb862b gopls/internal/lsp/cache: remove stray print statement%0A  > f87c1ed internal/fastwalk: improve Darwin performance by ~3x%0A  > b253314 gopls/internal/lsp/cache: add support for loading standalone main files%0A  > 3beecff gopls/internal/span: some cleanups%0A  > d375238 gopls: dedup upgrade code actions for vulncheck%0A  > b20ae4b README: format install command%0A  > 19a5504 gopls/internal/lsp: use the golang.org/x/vuln/exp/govulncheck%0A  > ab79327 cmd/ssadump: disable run mode with runtime package%0A  > 29429f5 gopls/internal/lsp/source: sort protocol edits%0A  > 49b340b go/analysis: update tests for different go list error behavior%0A  > cd0288f internal/lsp/cache: invalidate analysis results on packages.Load%0A  > 906c733 gopls/internal/lsp/source: find references in test packages%0A  > 2a41b25 internal/robustio: fix log.Fatal calls that should be log.Fatalf%0A  > 150b5f8 internal/imports: read entire API dir in mkstdlib.go%0A  > 19cfa79 internal/lsp/source: switch the default diff algorithm to "checked"%0A  > fa6bd3b gopls: include informational vulnerability diagnostics%0A  > 89b4335 gopls/internal/lsp: merge notifications about deprecated settings%0A  > f90d8ad all: fix a few function names on comments%0A  > 350f1e2 gopls/internal/lsp/fake: retry ephemeral errors when renaming on windows%0A  > 8b1d1ec gopls/internal/lsp/cache: suppress panics during analysis%0A  > 20c1ee7 gopls/internal/lsp: warn about Go versions that are too old%0A  > 709f108 gopls/internal/lsp/cache: suppress crashes in fact_purity analyzer%0A  > a410e98 internal/diff: ToUnified may fail%0A  > 26a95e6 gopls/internal/span: move internal/span into gopls%0A  > f2c4579 internal/diff: avoid unnecessary allocations%0A  > 60ddcca internal/diff: Apply: validate inputs%0A  > 02bef08 go/packages/packagestest: break dependency on gopls' span package%0A  > 778f945 go/analysis: break dependency on span package%0A  > c682555 gopls/internal/regtest/misc: delete testdata%0A  > 1552529 gopls/internal/regtest/misc: use vulntest for vuln_test%0A  > c4f49e4 go/analysis/passes/assign: fix map assignment%0A  > bd8c28f internal/diff/lcs: fix shell format error%0A  > ede3ab2 gopls/internal/lsp/protocol: simplify OffsetRange, Position%0A  > dc3cf95 gopls/internal/vulncheck: use vulntest for test database creation%0A  > 4ef38dc gopls/internal/vulncheck/vulntest: add test helpers%0A  > 2f57270 gopls: update golang.org/x/vuln%0A  > d96b238 internal/diff: simplify API, break span dependency%0A  > 9856077 internal/diff: abolish errors%0A  > 33c2dbf gopls/internal/lsp: remove extra newlines in vulncheck diagnostics%0A  > b280e27 gopls/internal/lsp/cache: make IsIntermediateTestVariant a method%0A  > c5514b7 gopls/internal/lsp/source: use PackageFromFile in Identifier%0A  > ff4ff8b gopls/internal/lsp/source: don't type-check in FindPackageFromPos%0A  > 2d32e15 gopls/internal/lsp/cache: in tests, show all stacks during analyzer crash%0A  > dc88e7b godoc: fix some comments%0A  > 7f79a02 gopls: use fmt.Fprintf%0A  > 40dabfa gopls/internal/lsp: add support for package renaming%0A  > 55e5cff internal/diff: unified: match GNU diff for empty file%0A  > 3e0355b gopls/.../fillstruct: support generic types%0A  > ed98f10 gopls: prefix vulncheck diagnostic message with title%0A  > b180eff x/tools/go/analysis: extend json output by SuggestedFixes%0A  > d49f960 internal/lsp/cache: report analysis panics during testing%0A  > 27641fb gopls: suggest upgrading to fixed version for vulncheck diagnostics%0A  > 199742a go/analysis/passes/printf: check for nil scope of instance methods%0A  > 3db607b gopls/internal/lsp/cache: remove "discovered missing identifiers" log%0A  > a4274a8 gopls: add diagnostics for non-stdlib vulnerabilities%0A  > f80e984 gopls/internal/lsp/work: use the WorkFileError diagnostics source%0A  > 9c63911 gopls/internal/lsp: delete dead code%0A  > ae737bc gopls/internal/lsp: remove the source.Session interface%0A  > bddb372 gopls: deprecate three experimental features%0A  > 4dd4ddb go/packages: issue error if 'go list' on PATH is too new%0A  > 10e9d3c gopls/internal/lsp: tolerate new 'imported and not used' error message%0A  > eb45e98 gopls/internal/regtest: fix regtest failures from "undefined" errors%0A  > 1bfc469 gopls: update to handle 'undefined:' versus 'undeclared' in type errors%0A  > 5214f41 internal/gocommand: show pid of process%0A  > c5cd943 gopls: fix the reset_golden.sh script and regenerate golden files%0A  > 49a686d go/analysis: update explanation of (no) Diagnostics.Severity%0A  > eb25de6 go/analysis/passes/loopclosure: only check statements after t.Parallel%0A  > b243e57 gopls/internal/lsp/tests: simplify collectCompletionItems, remove Data.t%0A  > 88b5529 gopls/internal/lsp/tests: use the mustRange helper in more places%0A  > c7ac942 gopls/internal/lsp: simplify prepareRename tests%0A  > b9adce9 internal/lsp/source: derive document symbols from syntax alone%0A  > 3dda4ba all: replace deprecated egrep with grep -E%0A  > 1877b5f go/analysis/passes/printf: permit multiple %w format verbs%0A  > b3ab50b go/analysis/passes/stdmethods: recognize Unwrap() []error%0A  > 62ae586 gopls/test: disable stderr output for command line tests as well%0A  > be3ff02 go/analysis/passes/sortslice: correct diagnostic for sort.Slice(f())%0A  > 2f04713 gopls: fix out of bounds bug in extract%0A  > 16b9742 go/analysis/passes/loopclosure: use go/types' object resolution%0A  > 81a42f0 gopls/internal/lsp/tests: pass in a *testing.T to Data.Golden%0A  > 14462ef go/analysis/passes/loopclosure: experiment with checking t.Run+Parallel%0A  > 00ae48e go/internal/pkgbits: replace os.SEEK_CUR with io.SeekCurrent%0A  > 835bfdf gopls: update x/vuln to pick fix for incorrect version suggestion%0A  > 6782af0 gopls/internal/lsp/source: clarify qualifiedObject%0A  > f901623 gopls/internal/lsp: suppress noisy log output in tests%0A  > df2eb93 gopls/test: fix erroneously skipped tests, remove redundant cmd tests%0A  > 1578244 gopls: set codelensProvider in initialize response%0A  > fdf581f internal/lsp: allow extract func ranges to begin/end with comments%0A  > b256f1f gopls/internal/lsp/cache: remove distracting "safe trimming" log%0A  > 0e011a0 all: use constant to avoid repeated definitions%0A  > 4d18923 gopls/internal/fake: sort edits by both start and end position%0A  > 45ad958 gopls/internal/lsp/protocol: fix json tags and indirect some zero values%0A  > a61f20e internal/gocommand: tweak debugging for hanging go commands%0A  > cdd6986 gopls/tsprotocol: make Disabled in CodeAction optional%0A  > 0398b3d internal/gocommand: add instrumentation for hanging go commands%0A  > 9250e22 internal/lsp: latest version of LSP stubs%0A  > ec74389 gopls/internal/lsp/source: make "chatty" diagnostics the default%0A  > 7e129ca gopls: add codelens to reset upgrade diagnostics%0A  > a81fce3 gopls: run go mod tidy -compat=1.16%0A  > a8b9ed3 gopls/internal/lsp/source: remove Govulncheck from Hooks%0A  > 678efe0 gopls/internal/lsp/cmd: fix vulncheck error handling%0A  > e71c338 go/ssa/ssautil: initialize info when there is syntax%0A  > 0eebaab go/analysis: allow for identical SuggestedFixes%0A  > eeaf4eb internal/lsp/fake: add rename file support for testing%0A  > 4754f75 go/analysis/passes/copylock: modify match pattern to satisfy change sync.Once.done to atomic.Bool%0A  > a630751 x/tools: update go.mod following moving LSP code to x/tools/gopls%0A  > 308e02c x/tools/go/ssa: disable slice-to-array test%0A  > 3ee1710 gopls/doc: update stale documentation and improve link names%0A  > 5f27e05 all: remove redundant type conversion%0A  > b15dac2 gopls: migrate internal/lsp to gopls/internal/lsp%0A  > dd1bab2 go/analysis/passes/printf: fix panic parsing argument index%0A  > bac5507 go/analysis/internal/checker: make applyFixes work from the first character%0A  > c1dd25e gopls/internal/migrate.sh: a script to migrate internal/lsp to gopls/%0A  > 83d7619 gopls : add a mention of staticcheck to settings documentation%0A  > d815cba internal/lsp: update LSP protocol for WorkspaceEdit%0A  > 6a585a2 x/tools/internal/typeparams: use regexp to match wanted result%0A  > be9eab1 go/analysis/passes/inspect: fix example return%0A  > 5ba8541 x/tools/internal/lsp/source: disable some tests for std lib changes%0A  > eb8352e gopls/internal/govulncheck: sync x/vuln@62b0186%0A  > 655abda gopls/internal/regtest: TestEditGoDirectiveWorkspace should fail eagerly%0A  > 33c1ddd tools/gopls/internal/regtest/diagnostics: handle new error message%0A  > 40cfaff x/tools/internal/lsp/source: disable some tests for std lib changes%0A  > f16be35 internal/lsp/source: add functions to type hover output%0A  > dfc8d49 internal/lsp/testdata: fix diagnostics checksum%0A  > 6c10975 internal/lsp/cache: honor RunDespiteErrors=false%0A  > 49ab44d x/tools/internal/lsp: re-enable a test with adjusted error message%0A  > 550e1f5 internal/lsp/tests: use a shorter module path for test data%0A  > 4ccc73c internal/lsp/tests: simplify comparison of markdown at go1.18%0A  > 3eb8a8f internal/lsp/cache: delete misleading Package.IllTyped method%0A  > cb91d6c internal/lsp/cache: clarify error control flow of analysis%0A  > 41c3a9b internal/lsp/analysis/fillreturns: be defensive w.r.t. type errors%0A  > fe1a27b gopls/doc: make doc generation work regardless of the current directory%0A  > ddbeb75 internal/lsp: run internal/lsp/reset_golden.sh%0A  > 248c34b internal/lsp: support regular expressions in Diagnostics tests%0A  > 431f4ef internal/lsp/tests: re-enable ARM tests%0A  > 717a671 go/analysis/passes/printf: remove unused hasBasicType%0A  > 7f23307 internal/lsp: limit diagnostics for upgrades to codelens go.mod file%0A  > 7c5e035 internal/lsp: fix suppressed panic in analyzer%0A  > 2f38e1d internal/lsp/tests: disable failing test on ARM%0A  > d35bb19 internal/lsp/tests: improve assertion error message%0A  > 7111c2e x/tools/internal/lsp: disable a test so we can change the parser error%0A  > db6a62c go/internal/gcimporter: call Interface.Complete in unified importer%0A  > 587a153 internal/lsp: hover to render go 1.19 doc comments%0A  > e55fb40 internal/lsp/cache: clear shouldLoad IDs on load%0A  > a3cac11 godoc/redirect: delete golang.org-specific code%0A  > b3851a8 internal/lsp/cache: tweaks to metadata graph%0A  > 938e162 gopls/internal/regtest: unskip TestDeleteModule_Interdependent%0A  > e8507be gopls/internal/regtest/bench: replace -gopls_version with -gopls_commit%0A  > 8c83056 gopls/internal/regtest: unskip TestSumUpdateFixesDiagnostics%0A  > 987de34 internal/lsp/completion: don't use Type.String for checking identity%0A  > 5a26068 internal/lsp/source: remove utm_source from pkgsite links%0A  > 35f806b gopls/doc/workspace: correct grammar%0A  > bebd890 go/analysis: remove stray print statement in the timeformat analyzer%0A  > 88d981e printf analyzer: link to fmt#Printing for verb/type docs%0A  > c4ec74a go/internal/pkgbits: fix performance of rawReloc%0A  > 37a81b6 internal/lsp: add unnecessary tags for unused vars and imports%0A  > 3807419 internal/lsp/cache: validate the range for critical errors in go files%0A  > b2156b5 gopls: update dependencies%0A  > 0ad49fd internal/imports: update stdlib index for 1.19%0A  > 3950865 gopls/internal/regtest/bench: add a -gopls_version flag%0A  > 6fa767d internal/lsp: update documentation for directoryFilters setting and default value%0A  > 96d05aa gopls/internal/regtest: fix TestFailingDiagnosticClearingOnEdit%0A  > 4ff08b4 gopls: Improve auto-imports example for NeoVim LSP%0A  > 92d58ea internal/lsp/cache: register a file watcher for explicit GOWORK values%0A  > 98aef77 internal/lsp/cache: track explicit go.work files outside the workspace%0A  > fff6d6d internal/lsp: update the broken workspace message to mention go.work%0A  > 9b60852 gopls/internal/regtest: move TestMultipleModules_Warning to ./workspace%0A  > 06d96ee gopls/internal/regtest/bench: add a test for completion following edits%0A  > 81c7dc4 internal/lsp: polish vulncheck progress messages%0A  > af2a0a8 internal/lsp: use exec.CommandContext when running vulncheck%0A  > 3519aa2 internal/lsp/cmd: remove unused Env from pkgLoadConfig%0A  > 6c27717 internal/lsp/mod/code_lens: add "run govulncheck" codelens%0A  > 763f65c gopls/internal/regtest/misc: simplify shared edit tests%0A  > fc3b24a go/internal/gcimporter: rewrite interface receiver parameters%0A  > b5fd088 internal/lsp/command: replace VulncheckArgs Dir with URI%0A  > 99fd76f internal/lsp/cache: delete KnownMetadata.PkgFilesChanged%0A  > 01c9ff0 internal/lsp/cache: invalid packages should not be workspace packages%0A  > bd68922 internal/lsp: new options to disable certain kinds of semantic tokens%0A  > bceee4b internal/lsp/command: let RunVulncheckExp call gopls vulncheck%0A  > 3e0a503 internal/lsp: use directoryFilters in import scanning%0A  > 87f47bb gopls/internal/regtest/bench: refactor and improve benchmarks%0A  > 8b9a1fb go/callgraph/vta: do not assume that recovers cannot be deferred%0A  > 371fc67 go/tools: add check for time formats with 2006-02-01%0A  > d08f5dc gopls/internal/regtest: unskip all of TestModFileModification%0A  > ddb90ec internal/lsp/cache: fix data races to view.options%0A  > 0d04f65 internal/lsp: re-send diagnostics on file events%0A  > d025cce internal/lsp/source: don't crash requesting gc_details for an empty file%0A  > 10cb435 internal/lsp/regtest: improvements for shared execution modes%0A  > 4d0b383 internal/lsp/regtest: minor cleanup for magic regtest envvar%0A  > 310ea71 gopls/internal/regtest: add a test that ignoring a file resolves errors%0A  > 21861e6 gopls/internal/regtest/bench: put feature benchmarks in their own file%0A  > c7f1191 go/internal/gcimporter: set underlying types in proper order; flatten imports%0A  > bd3f524 internal/lsp: rename all the package names in the renamed package%0A  > 9f65685 internal/lsp/source: enable the new diff with allExperiments%0A  > 9580c84 internal/lsp: Check if user's editor support rename operation%0A  > f560bc8 internal/lsp/cache: don't set context cancellation as a critical err%0A  > 8ea5687 internal/lsp/regtest: remove arbitrary timeout for closing the editor%0A  > d01bb2f internal/lsp/source: document the handling of GOPRIVATE for linkTarget%0A  > 98bfcd1 internal/memoize: fix race in Store.Promise%0A  > e02e98a internal/lsp/cache: allow network whenever reloading the workspace%0A  > b52794a internal/lsp/cache: simplify snapshot.Clone reinitialization logic%0A  > f1bb5ca internal/lsp/cache: report a critical error when go.work is invalid%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping k8s.io/code-generator 6523e22...eec869e:%0A  > eec869e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 824419b Bump runc go module v1.1.4 -> v1.1.6%0A  > ba94e65 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 6276bf2 Update golang.org/x/net to v0.7.0%0A  > 73b9c40 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 882af80 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 6063700 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > b615940 Update golang.org/x/net 1e63c2f%0A  > 11d5c4c update k8s.io/utils to fix util tracing panic%0A  > 081720d Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > d44fa8c dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 300cdcf Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > e0ef4aa Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 557ce1f Merge pull request # 113126 from alexzielenski/remove-unwanted-replace%0A  > f86120d remove errant replace%0A  > d6a8b70 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f77ba6d dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 3bbe215 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > e80bbc4 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d403dc0 update kube-openapi%0A  > 790e4bc update fsnotify to v1.6.0%0A  > 27bd7d9 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 4731e5c Bump golang.org/x/text to v0.3.8%0A  > a8a213c Merge pull request # 112875 from pohly/update-yaml%0A  > 5f5bab9 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 983d5d0 Merge pull request # 112819 from thockin/no-make-generators%0A  > c35177b Format calls to codegens%0A  > 83929d0 Codegens: Do not auto-set boilerplate path%0A  > 1d82d12 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > c3414a0 clients: clarify a misleading comment%0A  > 998e449 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > e4543b2 Update to latest k8s.io/utils to pick up changes%0A  > 8e999f2 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 524127d update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 4ca0baf Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b54a056 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 350c30a updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5f3f945 e2e: bump ginkgo to v2.2.0%0A  > 2e5cca7 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > c3fdc3c Merge pull request # 112349 from pohly/klog-update%0A  > e4b7976 client-go: support waiting for SharedInformerFactory shutdown%0A  > 135f69b build: update to klog v2.80.1%0A  > f60067d Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7c81c99 Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 8468f16 Remove in-tree credential plugins (again)%0A  > 9b98ed3 add symmetric difference in sets%0A  > 34125ff Merge pull request # 112199 from pohly/klog-update%0A  > a055687 dependencies: update to klog v2.80.0%0A  > 16cba21 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > e051ad0 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 3a31bb1 Merge pull request # 111934 from deads2k/apply-gen%0A  > 4d73156 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 1382941 make applyconfiguration-gen skip generation for types that have generated clients and lack objectmeta%0A  > 03a75ea Bump prometheus/client_golang to v1.13.0%0A  > 17196da update the apply generator to use the same package the the client generator expects%0A  > a4e23d1 Merge pull request # 111566 from inosato/remove-ioutil-from-code-generator%0A  > a6a370c make applyconfiguration-gen handle pointers to slices%0A  > 087714e Merge pull request # 109884 from qzoscar/patch-1%0A  > fc00858 Remove ioutil from code-generator%0A  > ed79ca3 make applyconfiguration-gen work for resources without objectmeta%0A  > fea40fb Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 3612509 fix a broken link%0A  > 78677a3 update the applyconfiguration-gen flag external-applyconfigurations to work%0A  > ad6af70 Revert "Remove gcp and azure auth plugins"%0A  > 7ba56cb applyconfiguration-gen handling of types that have a non-embedded use of TypeMeta%0A  > 97fa351 Merge pull request # 111696 from liggitt/go119mod%0A  > d71f529 add metav1.OwnerReference to the default external configurations to ease generation%0A  > 2b9093f Update go.mod to go1.19%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping knative.dev/eventing 034bec9...516a915:%0A  > 516a915 Upgrade rekt to latest (# 7076)%0A  > 6a890e0 Fix flaky unit tests (# 7080)%0A  > eaf28a7 Add tracing for TestBrokerWithManyTriggers (# 7077)%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping knative.dev/serving 2c1bb07...bde2f42:%0A  > bde2f42 Update net-gateway-api nightly (# 14144)%0A  > bb1262e Update net-kourier nightly (# 14129)%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f U…

---
## [Kubic70/SS13_RedStation](https://github.com/Kubic70/SS13_RedStation)@[2aaafd9a67...](https://github.com/Kubic70/SS13_RedStation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Thursday 2023-07-06 13:31:35 by TheVekter

Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

---
## [blockmanbuster/garrysmod-chatsounds](https://github.com/blockmanbuster/garrysmod-chatsounds)@[35dee955a9...](https://github.com/blockmanbuster/garrysmod-chatsounds/commit/35dee955a9ae01494db3c127d7e83b653d479e32)
#### Thursday 2023-07-06 14:14:56 by Mike

10 years in the joint made you a fuckin pussy

fuck you

---
## [blockmanbuster/garrysmod-chatsounds](https://github.com/blockmanbuster/garrysmod-chatsounds)@[088f7ca630...](https://github.com/blockmanbuster/garrysmod-chatsounds/commit/088f7ca6306dd083b7a32f59683f1e3d49187f9c)
#### Thursday 2023-07-06 14:14:56 by Sensuka

more tf2 chatsounds in tf2_extras folder (#420)

* More Killing Floor Chatsounds

the title speaks for itself, it adds more killing floor chatsounds, hurray.

* more killing floor sounds, again

same thing but different sounds

* Delete and she never listened.ogg

* Delete ha ha ha haaa.ogg

* Delete heheheheheheh.ogg

* Delete i always told her.ogg

* Delete id make something of myself.ogg

* killing floor patriarch

adds more patriarch

* killing floor chatsounds

the title again speaks, it adds a few sounds from killing floor

* more tf2 chatsounds in tf2_extra folder

for shits & giggles

---
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[f9ac3a4a6f...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/f9ac3a4a6ff08311d986eee67f3c91f9f489532a)
#### Thursday 2023-07-06 14:18:54 by Knative Automation

upgrade to latest dependencies

bumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping knative.dev/client-pkg 4f052f9...f377f06:%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping knative.dev/serving 2c1bb07...bde2f42:%0A  > bde2f42 Update net-gateway-api nightly (# 14144)%0A  > bb1262e Update net-kourier nightly (# 14129)%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/eventing 034bec9...516a915:%0A  > 516a915 Upgrade rekt to latest (# 7076)%0A  > 6a890e0 Fix flaky unit tests (# 7080)%0A  > eaf28a7 Add tracing for TestBrokerWithManyTriggers (# 7077)%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping knative.dev/hack f591fea...fc42790:%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go

Signed-off-by: Knative Automation <automation@knative.team>

---
## [werbhq/schello-public](https://github.com/werbhq/schello-public)@[dc0204e1e9...](https://github.com/werbhq/schello-public/commit/dc0204e1e95c3885bd58802bfe3237c7c5aa084c)
#### Thursday 2023-07-06 14:23:41 by Navaneeth Venu

Fix MinWidth truncation issue for Author.

Please search up minWidth and flexshrink. You'd never think this would be the solution in a million years. SMH I hate you for making me do layouts Aswin go die.

---
## [Manjunatha-kv/PORTFOLIO](https://github.com/Manjunatha-kv/PORTFOLIO)@[ff6c85e540...](https://github.com/Manjunatha-kv/PORTFOLIO/commit/ff6c85e540747bdda1744c63e47e725b2b380669)
#### Thursday 2023-07-06 15:26:51 by Manjunatha_kv_

Create README.md

"Welcome to my portfolio! I have created this website using HTML, CSS, and JavaScript to showcase my skills and projects. With a passion for web development, I have carefully designed and crafted each element of this portfolio to reflect my abilities and creativity.

Through the power of HTML, I have structured the pages of my portfolio, providing a clear and organized layout for easy navigation. CSS has allowed me to bring life to my designs, utilizing colors, typography, and layout techniques to create a visually appealing and cohesive aesthetic. By incorporating JavaScript, I have added interactivity and dynamic features, making the portfolio an engaging and user-friendly experience.

Within this portfolio, you will find a collection of my projects, ranging from web applications to responsive designs. Each project demonstrates my proficiency in different technologies and showcases my problem-solving skills. I have provided detailed descriptions, along with relevant links and images, to give you a comprehensive understanding of my work.

Moreover, I have dedicated a section to highlight my skills, including my expertise in HTML, CSS, JavaScript, and other programming languages. Additionally, I have included information about my education, work experience, and any notable achievements.

I believe in constant growth and improvement, which is why I will regularly update my portfolio with new projects and skills. I strive to stay updated with the latest trends and technologies in web development, ensuring that my work is innovative and relevant.

Thank you for visiting my portfolio. I hope you enjoy exploring my projects and gaining insight into my abilities as a web developer. If you have any questions or would like to discuss potential collaboration opportunities, please feel free to reach out to me. I look forward to connecting with you!"

---
## [feldera/dbsp](https://github.com/feldera/dbsp)@[59132364cb...](https://github.com/feldera/dbsp/commit/59132364cb27d22b158776b09864221b938ff3e2)
#### Thursday 2023-07-06 16:12:20 by Gerd Zellweger

Add ability to checkpoint/version a pipeline. (#296)

This change allows to query the running configuration of a pipeline. And we also allow to update the running configuration of a pipeline explicitly. So all the normal interactions with connectors, pipelines, and program objects act as a staging area which can be committed using the API to the running version of the pipeline.

This change has several components:

## Database

This is pretty straight forward: We add history tables for pipeline, program, attached_connectors, and connectors. The history table contains the same fields as the
non-history counter-parts but we add a revision field and change the primary keys to be uuid+revision in those tables.

The history tables are immutable snapshots of the pipeline config. You see where this is going, whenever we need to commit a config. We go off and copy the pipeline row, the program row, all attached_connector and connector rows associated with the pipeline we want to version into the history table. We assign them a new
revision for every version. And we're almost done with versioning stuff. Kind of...

## Compiler

Now we have all these versions, and each version has a different binary, so we need to keep the binaries around. That's a bit unfortunate, but this will go away again once we have JIT. It also is kinda dumb because we don't want to keep binaries for all versions we ever created. So here is what we do:
Whenever we create a new program binary we version it in a (new) binaries folder (in the dbsp workspace) using a naming schema that is project_$uuid_$version. The reason we version immediately and not say at commit time of a pipeline is because the binary we used so far was just the binary directly from the target dir of that project. But we don't really know what state this binary is in, especially if we can have commit and compile requests happening at the same
time. So in the same 'transaction' that builds the binary we version it and copy it away. And the pipeline manager only runs versioned binaries. We also need a way to clean up binaries. That's also a bit silly because when is it safe to delete a version of a binary? Well, it's only safe if no pipeline has that program version as it's current, last revision. And no pipeline descriptor that we haven't versioned yet has that program/version as it's current program/version. The way we deal with this is to have a GC task that periodically wakes up and checks if binaries are orphans and can be removed. The first design I tried was trying to do this on-the-fly while we create new commits
but it seemed better in the end to handle this in a separate task as interacting with files can fail in all kinds of weird ways and shouldn't block anyone from creating a new version.
REST API

This one is pretty simple. We commit whenever the pipeline is deployed. And we allow to query the last committed/deployed pipeline. Finally, we also added a way to get the pipeline descriptor (not a committed version) in toml format. This is helpful to display a diff in the UI/APIs to see what has changed. And a way to validate a pipeline config + sql combination (e.g., don't deploy but return the errors that deploy would return if it found any inconsistencies).

## Other code changes

As you can see in the code, I added this PipelineRevision struct. That's essentially all state a user will be committing. If you look closely you can also see that we it harder for the user to version some garbage pipeline that would never run in the first place. For example, make sure that whatever we reference in the config references some actual tables and views along with a bunch of other conditions that need to be satisfied for the commit to succeed.
This change also meant that we have to use actual types for the database DDL that we get back from the compiler instead of just a string.

Signed-off-by: Gerd Zellweger <mail@gerdzellweger.com>

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[03c964ac45...](https://github.com/Sealed101/tgstation/commit/03c964ac45e727543aac85ad817df89a7555fb31)
#### Thursday 2023-07-06 16:38:31 by LemonInTheDark

Reworks Duffel Bags (Zippers) (#76313)

## About The Pull Request

Reworks duffel bags in line with oranges proposed plan.


![image](https://github.com/tgstation/tgstation/assets/58055496/126743dd-d7b8-47e0-bdd8-a0caec39c515)

Basically, instead of just making you slower all the time, they make you
slower while you have them open, but give you the same speed while
they're closed.
As a trade off, opening and closing them takes time, 2.1 seconds
(matches the sound) and 0.5 respectively.


https://github.com/tgstation/tgstation/assets/58055496/555d2cd0-038e-4b0b-a693-0c66dac16f5b

[Adds support for limiting extra storage, uses it to make syndie stuff
cool](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

[d0b2bbf](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

Syndicate bags currently ignore downsides by just ignoring the slowdown,
but that's kinda boring so let's just buff em instead.

They now support holding a limited amount of bulky items (3), filtered
down to things that would otherwise constitute going loud (or otherwise
be useful to carry around as a loudish traitor)

I may have gone a bit overboard on what I whitelisted here, lemme know
yeah?

I also did some fenangling with backpack uses of create_storage, I don't
like this pattern it was a bad idea I think.

## Why It's Good For The Game

I'm unsure if these delays enough, I think any length of time is decent
since it means you need to stop moving and focus on it for a bit.
My hope is this will make them a proper sidegrade, rather then something
that goes unused/acts as newbie bait

## Changelog
:cl:
balance: Duffelbags will now only make you slow while they are unzipped.
As a tradeoff, you now need to stand still and zip/unzip them to access
their contents/not move real slow.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [techmatters/terraso-client-shared](https://github.com/techmatters/terraso-client-shared)@[92d625fd87...](https://github.com/techmatters/terraso-client-shared/commit/92d625fd877aaf70395204132600e59894fde2ff)
#### Thursday 2023-07-06 16:52:56 by David Code Howard

feat: Allow using promises for token config (#12)

* feat: Allow using promises for token config

This commits allows you to do something like:
```typescript
const apiConfig : TerrasoApiConfig<{ usePromise: 'yes' }> = ...;
apiConfig.getToken().then(...);
```

What I would like to do is something like this

```typescript
type Identity<T> = t;
type WithPromise = TerrasoApiConfig<Promise>;
type WithoutPromise = TerrasoApiConfig<Identity>;
```

However, it seems this is not possible with Typescript
generics. Instead I tried using the [conditional
types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html),
which is quite messy but seems to almost work as I want it.

The current implementation seems to default to not using Promises, for
reasons that escape me (I suspect that it's because of the way
MaybePromise is implemented). This is good as it means that there
shouldn't need to be any changes to the web client. However, it means
that every time the mobile client uses `getAPIConfig`, the result
needs to be typecast to `TerrasoAPIConfig<{usePromises: 'true' }>`,
which is a real pain. In order to get around this, instead of using
the existing closure, I'm planning to use the class at the end,
initialize it at app startup, and export the functions as convenience
methods. This should let Typescript infer the types properly; I don't
think this is possible with the current closure.

I am truly not attached to any changes here, so if they seem stupid
please let me know. I'm just trying to get something working.

* Revert "feat: Allow using promises for token config"

This reverts commit 01b8e2772d495c16a528d2fd70fe99bcf9ac3b31.

* feat: Change getToken() type to return Promise

The mobile client needs to use Promises to fetch and store tokens,
while the web client uses a synchronous Cookie API. In order to
support both I changed the function type to return a Promise. It
created a bit of difficulty with the Redux store; the initial state
can't be set automatically because the getToken function is now
async. It will mean that the client code will have to call the
`getInitialToken` action on startup. We can maybe take another look at
this later.

* feat: Provide intialToken value for sync implementation

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[5271d4fbc4...](https://github.com/Opentrons/opentrons/commit/5271d4fbc473bb8f2506a90b2c929535c82892f6)
#### Thursday 2023-07-06 16:56:20 by Seth Foster

feat(api,shared-data): error codes in PE (#12936)

On the python side of our code, we want our new enumerated exceptions to
be gradually integratable, and we also want to make sure that any errors
that we didn't yet get the chance to give error codes end up with error
codes. To do this in a programmatic way, we can add some automated
methods for wrapping python exceptions.

All enumerated errors now get to wrap errors. These are optional
sequences of more enumerated errors that are considered to have caused
the top-level one - in most cases, this will be because the enumerated
error explicitly was instantiated to wrap a python exception, but it
could also be if it was raised from one.

Since we only wrap other enumerated errors, we need a way to make
exceptions enumerated errors. A new exception type (but not code - it's
just a GeneralError) called PythonException has this capability; it lets
you give it BaseExceptions in addition to other EnumeratedErrors, and
it's capable of walking the python memory model internals to try and get
the other exceptions in a stack of raise from ... raise from ... calls
that are reasonably popular in our code. This is functionality that is
promoted out of The Dunder Zone in python 3.11, so I feel pretty good
using it (this is what ExceptionGroups are).

So now, as in the tests, if you catch an exception and give it to a
PythonException you bless it with an error code and save all the
exceptions and their stack traces for later inspection. Cool!

ProtocolEngine is the first place we'll go through and add places that
actually use these error codes, since it's in a lovely high-leverage
middle spot in our stack. That means we both get to test the upward
interface of how these things will be represented in the HTTP API and
how they'll be created from lower exceptions.

ProtocolEngine already has its own very large and robust set of custom
exceptions, which is awesome. We can make them inherit from the
enumerated errors pretty easily, but unfortunately we have to add a
bunch of stuff to their constructors to pass along things like the
ability to wrap other exceptions and so on. Luckily that's just typing.

Once we've done that, at the three points we catch all missed exceptions
we have to switch over to creating the new style. ProtocolEngineErrors
get passed on; uncaught legacy errors get captured as PythonExceptions;
and uncaught errors in the normal core do too.

Finally, we have to represent this new style of error in the
ErrorOccurrence objects. This is the fun part. Previously, we'd added
error codes to those objects; this was sort of a big deal because we
want them to be required when you make new ErrorOccurrences and when
clients look, but we don't want things to break when we deserialize old
ones. We can extend that trick pretty easily to add new things. What's
not quite as easy is this concept of wrapping errors. Our errors are now
essentially trees, and we need tree structure here. Luckily, jsonschema
and pydantic are actually pretty good at type-recursive schema and
object definitions, so we can plop a list of other error occurrences in
there.

Now, when we catch one of these errors that's bubbled up from hardware,
we give it a name and we capture its entire history in an inspectable
way, and I think that's really cool.

---
## [sarojrimal/Sentiment-Analysis-of-AirBnb-London](https://github.com/sarojrimal/Sentiment-Analysis-of-AirBnb-London)@[94b811470d...](https://github.com/sarojrimal/Sentiment-Analysis-of-AirBnb-London/commit/94b811470d6c9dfe9430a1654f77de34633df66e)
#### Thursday 2023-07-06 17:35:09 by Saroj Rimal

Add files via upload

Data Collection:
Data acquisition is the process for bringing data that has been created by a source outside the organization, into the organization, for production use (Malcolm Chisholm, 2018). In simple words it is the process of obtaining, filtering, and cleaning data before it is stored in a data warehouse or another storage method. In many circumstances, data is not in a format that can be easily downloaded and analyzed.
The London Airbnb dataset for this study was obtained from the Inside Airbnb website “Inside Airbnb: Get the Data”, which allows researchers to access publicly available Airbnb data for research purposes, as well as data from numerous previously published Airbnb-related studies. This website stores the data of AirBnb worldwide and to perform the analytics on London City AirBnb, London city was filtered and downloaded the dataset till 09 March 2023. The link to this website is Inside AirBnb: Get the Data.
Data Description:
There are two different datasets; 1. listing.csv and 2. Reviews.csv that are going to be used in this project. Firstly, some basic explorations are done using these both datasets individually. To perform sentiment analysis on reviews, both datasets are combined with performing different data cleaning processes. The essential libraries are installed at the very beginning and other libraries are imported gradually as per the requirements. 
 
Figure 1: Importing essential libraries.

 
Figure 2: Loading listing dataset and visualizing in table form part -1
 
Figure 3: Loading listing dataset and visualizing in table form part -2
 
Figure 4: Loading reviews dataset and visualizing in the table form.
Data Cleaning: 
Cleaning data helps to achieve accuracy in this analysis and improve the performance of the model. The results and findings depend on the data used, thus that data needs to be cleaned properly to get the proper outcome. Here, some of the data cleaning techniques are performed:
1.	Dealing with missing data
To deal with missing values, isnull function is used.
 
Figure 5: Identifying the missing values.
From the figure 5, we can see that some of the columns have missing values including name, neighbourhood group, last review, reviews per month, and license with different numbers. Thus, firstly we will analyse which columns are needed for our analysis. We don’t need columns like last review, name, host name, neighbourhood group, and license. So, we will drop those columns in later stage and for now, the number of reviews column is cleaned as this column is required for our analysis. 

 
Figure 6: Replacing missing data with 0.
As per mentioned above, the missing data in umber of reviews column are replaced by 0. 

2.	Removing unwanted data
As mentioned above, the columns last review, name, host name, neighbourhood group, and license aren’t required for further analysis, so these columns are dropped from our dataframe. 
 
Figure 7: Dropping unwanted columns.

Data-Exploratory Analysis
The practise of identifying patterns, exploring relationships, and extracting information from unfamiliar datasets is known as exploratory data analysis (EDA). Because data scientists generally start with limited knowledge of the data and its structure, the process is iterative. To align the data with the aims of the analysis, data scientists execute a variety of data preparation activities such as identifying outliers, standardising value ranges, and deleting or filling null attributes during an EDA.
Data is used by businesses to solve problems, make intelligent choices, and prepare efficiently for the future. This data is optimised and ready to utilise due to data analysis. The following are some examples of data analysis:
•	Descriptive analysis
•	Diagnostic analysis
•	Predictive analysis
•	Prescriptive analysis
Descriptive Analytics
Descriptive analytics is the interpretation of historical data to better understand changes that have occurred in a business. Descriptive analytics describes the use of a range of historic data to draw comparisons (Jake Frankenfield, 2020). The most often reported financial data, such as year-over-year pricing adjustments, month-over-month sales growth, the number of users, or total revenue per subscriber, are all descriptive analytics products. These metrics all indicate what happened in a company over a specific time. This analytics makes use of a wide range of data to provide an accurate picture of what has transpired in a company and how it compares to previous times. These performance measures can be used to identify areas of strength and weakness, allowing management initiatives to be better informed.
Diagnostic Analytics
Diagnostic analytics describes the techniques you will use to ask your data: Why did this happen? It's a deep dive into your data in quest of useful information. The first step in most firms' data analysis is descriptive analytics, which is a simpler procedure that records the facts of what has already occurred. Diagnostic analytics goes a step further by elucidating the logic behind specific outcomes. Data discovery, drill-down, data mining, and correlations are common strategies used in diagnostic analytics. Analysts pick data sources that will aid them in interpreting the outcomes during the discovery process. Drilling down requires concentrating on a certain aspect of the data or a specific widget. Data mining is an automated method of extracting information from large amounts of raw data. Finding consistent correlations in your data can also assist you in determining the scope of the investigation. 
Predictive Analytics
Predictive analytics is a type of advanced analytics that forecasts activity, behaviour, and trends using current and previous data. It entails using statistical analytic techniques, data searches, and machine learning algorithms to develop predictive models that provide a numerical value to the likelihood of a
specific action or event occurring (Linda Tucci, 2022). The application of statistics and modelling tools to create predictions about future outcomes and performance. This enables businesses and investors to shift their resource allocation to take advantage of potential future developments. Predictive analytics can also be utilised to boost operational efficiency and lower risk.
Prescriptive analytics
Prescriptive analytics has been called “the future of data analytics,” and for good reason. This form of analysis goes beyond explanations and forecasts to suggest the best course of action for the future. It's very handy for making data-driven decisions (Catherine Cote, 2021). Prescriptive analytics frequently employs machine-learning algorithms to sort through enormous amounts of data faster and more efficiently than people. Algorithms search through data and provide recommendations based on a certain set of requirements using "if" and "else" statements. For example, if at least 50% of customers in a dataset said they were "extremely dissatisfied" with your customer support team, the algorithm might suggest more training.

Summary Statistics: 
Summary Statistics helps to identify the mean, median, standard deviation, count, minimum, maximum and quartile information of every columns that have numeric values. 
 
Figure 8: Statistics information of variables

 
Figure 9: Stats of key variables
From the Figure 10, we can see that there are 75241 number of Airbnb properties with 4 room types in 33 different locations inside London where the average review is 17.97%. On average, each property in London has received approximately 17.97% reviews.


 
Figure 10: Number of hosts
There are in total 47619 number of individual hosts where the total number of Airbnb listing is 75241. Some of the hosts have multiple Airbnb hosting. 
Let’s see the available room types:
 
 
There are 4 types of rooms are sold in Airbnb London where the Entire Home/Apartment has 45714 number, Private Rooms are 28910, Shared Rooms are 403 and Hotel Rooms are 214 in number. We can see that mostly the Entire Home and Apartment are famous for Airbnb followed by the Private Rooms.
Which place in London provide more AirBnb facility?
 
Till 09 March 2023, Westminster is the busiest Airbnb area inside the London followed by Tower Hamlets and Hackney whereas the Sutton and havering are the less crowed places for Airbnb. 
 

Which location has the highest availability? 
 
Though there are many AirBnb properties inside the London, some of them are available frequently and some of them mostly. Based on the availability, Bexley and Havering are best options to stay and Hackney and Islington less available. 
Which area are mostly expensive?
 
Westminster, and Kensington are bit expensive as compared to other areas and Sutton, Croydon and Hillington have less room price as compared to other areas.  
Which month has the highest reviews? 
 
Based on the bar graph, November and July are gathering more reviews whereas April and March have less reviews. 

As our target is to analyse the sentiment of users based on the comments, thus, let’s separate only the required columns for our further analysis. 
 
In our case, only the id, host id, location, room type and price are needed from this dataset. So, we created new dataframe and pulled only the required columns. 
Working on Next Dataset; reviews.csv
The reviews dataset contains the information related to the comments given by the Airbnb users in a particular date. 
 
This dataset has in total 7 columns and now, we will perform some basic cleaning operations. 
 
We identified the missing values and separated only the required columns that is listing id and comments. 
Now, let’s merge the two datasets and store the required data in a new dataframe. 
 
For our further analysis, we only need id, comments, host id, location name, room type and price. 
As the dataset was very big, we only used around 10000 data by dropping other data.
 
 
Now, let’s load the positive and negative text file.
 
This helps to classify comments into positive, negative, or neutral sentiment categories based on the presence of words from the positive and negative lists. By counting the occurrences of positive and negative words in each comment, it determines the overall sentiment of the comment. This sentiment analysis approach assumes that the presence of more positive words suggests a positive sentiment, while the presence of more negative words suggests a negative sentiment.

 
The above figure defines a function called comment analyser that takes a list of sentences as input. This function tokenizes each sentence, converts the tokens to lowercase, removes non-alphanumeric tokens, and filters out stop words. It then applies the positive negative checker function to determine whether each sentence is positive, neutral, or negative based on predefined positive and negative word lists. The function counts the number of positive, neutral, and negative comments and returns the results.

The code inserts three new columns, 'positive comment', 'neutral comment', and 'negative comment', into the cleaned df Dataframe. It iterates over each row in the Dataframe, calls the comment analyser function on the comment text in that row, and assigns the counts of positive, neutral, and negative comments to the corresponding columns in the Dataframe.

Overall, this code performs sentiment analysis by analyzing the sentiment of each comment and counting the occurrences of positive, neutral, and negative comments. It provides valuable insights into the sentiment distribution within the dataset. 
 
Now, the positive, negative, and neutral comments are added into the cleaned dataframe along with the required columns. 
Let’s clean and preprocess the comments.
This step prepares the text data for further analysis or modelling tasks where the removal of URLs, HTML tags, numbers, and punctuation marks is desired. The resulting cleaned comments are printed for inspection or subsequent processing.

 
The above figure demonstrates the preprocessing of text data in a Dataframe column named comments. The preprocessing steps involve several functions to clean the text.
First, the column is converted to a string data type for consistency. Then, various transformations are applied using lambda functions. These transformations include removing numbers, URLs, and HTML tags from each comment using regular expressions and predefined functions. Additionally, the comments are converted to lowercase to ensure uniformity in the text data. Punctuation marks are also removed from the comments.
The next step is to perform several text processing and analysis steps. Firstly, the required libraries along with NLTK for natural language processing are installed. The comments column from the cleaned Data Frame is tokenized using the word tokenize function, which breaks down the sentences into individual words and stores them in Token list.
To prepare the tokens for further analysis, punctuation and non-alphanumeric tokens are removed from each tokenized review using a loop that iterates over the indices of Token list. This step helps to clean the data and remove unnecessary characters.
Stop words, which are common words like pronouns and prepositions, are then removed from the tokens using the stop words module from NLTK. The code initializes a set of English stop words and checks each word in Token list to exclude any stop words from the list.
After the preprocessing steps, the code demonstrates the creation of bigrams and trigrams from the modified tokens of the first review. It uses the words to n-grams function to concatenate adjacent words with a separator, generating n-grams for further analysis.
Lastly, the code calculates the frequency distribution of distinct words in the tokens. It utilizes the Freq Dist class from NLTK, initializes an instance of FreqDist, and iterates over each review's tokens to update the frequency count for each word. This frequency distribution provides insights into the occurrence of words in the dataset and can be utilized for various text analysis tasks.
Overall, the above diagram showcases essential steps in text preprocessing, including tokenization, removing punctuation and non-alphanumeric tokens, eliminating stop words, and generating n-grams and frequency distributions. These steps lay the groundwork for further analysis and exploration of the text data.
 
In the above you can see that there are 414140 positive, 13803 neutral and 47637 negative comments words which shows that the number of positive comments is way higher that the negative ones.
Tokenization 
Tokenization is the process of breaking down a large text into smaller tokens. It can be done at the sentence or word level (sentence tokenization) (word tokenization). Cleansing the text: We need to eliminate the special characters and digits from the text in this phase. Python's regular expression operations package can be used.
 
 
 
 
 

What are the most used words?
 
The diagram shows a bar plot showing the frequency distribution of the top 5 most common words in the tokenized reviews.
 
The above code screenshot shows the generation of a word cloud visualization based on the frequency distribution of words in the tokenized reviews. The word cloud represents the most common words, with the size of each word indicating its frequency of occurrence. Stop words are excluded from the word cloud to focus on meaningful words.
 
We can see how word clouds can help users quickly identify the most common tokens in each feature. We can discover frequent terms that appear repeatedly by dividing each string down into individual components. "clean" "great" and comparable qualifiers are, unsurprisingly, the most used across categories. Finally, the comments of the listings review on Airbnb. If we're deciding where to stay based on budget, we might want to check out the neighbourhood reviews. We use the review dataset to see how many good and bad comments there are about the areas. To begin, we look for reviews in English to examine. We then used the NLTK package to do sentiment analysis to determine whether a comment is good or negative.
Classification of Positive, Negative and Neutral Reviews
Now, let’s analyse the positive, negative, and neutral reviews gained by the different locations inside London so that the visitors can get clear insights of the Location they are preferring to make their stay. This analysis will help them to go deep dive into the locations that have positive, negative, or neutral comments. 
Location with the Positive Comments: 

 
From the Figure, we can see that Hillingdon and Richmond upon Thames has the highest positive comments so far. So, the visitors now can make their decision in which locations they can secure and enjoy their stay.
Location with the Negative Comments: 

 
From the above diagram, City of London and Southwark has the highest negative reviews. 

Conclusion 
We identified sources of pleasure and unhappiness among Airbnb consumers in our research. Airbnb customer review studies showing the positive and negative ratings, this study employed equal numbers of positive and negative reviews. Using Python to analyse Airbnb listings and reviews data to build informative charts. When planning a trip to London, one can choose a neighbourhood by looking at average costs, remarks, availability. Following that, we looked at borough and neighbourhood listing densities to see which locations were more popular than others. The more central areas of London we look for Airbnb, the more expensive are the listings. 
As we know that the neighbourhood group column has no values if there has been data it would have been much easier to develop a good visualization as taking whole neighbourhood column for visualization was hard because there were 30+ area listed which made difficulty in plotting the graph. According to the findings Airbnb in London is doing well we can see that as huge number of positive review additional attributes. It would also be useful to have a few of extra characteristics for our data exploration purposes, such as positive and negative numeric 0-5 stars reviews for each listing; having this information would aid in determining the best-reviewed hosts. Overall, we uncovered many intriguing feature connections and detailed each stage of the approach. This data helps organization make better business choices, platform control, marketing activities, new product implementation, and much more.

---
## [plaurent/xous-core](https://github.com/plaurent/xous-core)@[aab25f2d53...](https://github.com/plaurent/xous-core/commit/aab25f2d53b5b3e681840fe89fb22e1451516c0c)
#### Thursday 2023-07-06 17:55:06 by bunnie

add Tall font face and support for 32x32 bitmaps

Thanks to @samblenny for getting the ball rolling on this.

This commit adds a "tall" font face which is somewhere in betwee
the Regular size (12 pts) and 2x Small size (18 pts). This is
a compromise between text density and readability that has been
missing for some time from the UI.

The 32x32 glyph support is "hacked in", in that an extra flag
has been added to support this special case, rather than either
(a) making the library more generic (e.g. supporting 8x, 16x, 32x, 64x
glyphs) or (b) adding more metadata to the font libraries so that
the bitmap pattern is automatically associated with the font (right
now the parameters are set by hand in blitstr2/fonts.rs).

This is a violation of the "zero, one, many" principle in coding,
but I'm waiving that because (a) 64x glyphs don't make sense on
our system...you're not going to be creating posters and headlines
on this device (ha ha I say this today, tomorrow I will get a PR
for a poster editor app that absolutely needs 64x glyphs) and (b)
the font subsystem is, at least for now, a fairly mature and
well-tested code base so a minor futzing seems more appropriate
than ripping everything out.

The point at which things should be greatly refactored is when
we consider supporting right-to-left scripts or scripts that
require complex ligatures. But I think for now the system as
writ covers 80% of humanity's language needs acceptably
(but not perfectly).

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[c9bfaf28f7...](https://github.com/argilla-io/argilla/commit/c9bfaf28f72c240f5372640efbcb745d1e2b09be)
#### Thursday 2023-07-06 19:16:00 by David Berenstein

[FEATURE] Feature/prepare for training feedbacktask (#3151)

# Description

I added a very rough outline of my ideation behind
`prepare_for_training` with the new `FeedbackDataset`. As discussed
there are 3 complexities:

- How to resolve annotator alignment?
- How to resolve optional fields, which have not been filled out? e.g.,
"Please provide a correction for prompt 1?".
- How handle potential concatenation of fields? 

To make it modular I created a step-wise approach.

1. `Pydantic` Models that map and verify data fields, like so. By doing
this we keep the flexibility to allow for other tasks like
TextClassification and this ensures we can directly use `datasets.field`
and `dataset.questions` for defining training. We could also use the
`name` values from the fields/questions, but this might be more error
prone.
2. `get_relevant_data_for_training()` in `List[dict]` format with all
relevant fields from the Pydantic model. **annotator alignment issue**.
For now I opted for choosing the first non-zero value.
3. Forward the `List[dict]` to a similar flow we previously had.
4. Also add `dataset.unify_responses(question, Enum(strategy))`-method
5. Added `*QuestionUnifcation` to schemas to hold logic surrounding
unifying multiplier responses
6. Added `client.feedback.training`
7. Added`TrainingDataFor*` to hold logic surrounding
`prepare_for_training`-methods per task
8. Added inheritance for ArgillaTrainer

```python 
import argilla as rg
from argilla import (
    FeedbackRecord,
    LabelQuestion,
    LabelQuestionUnification,
    MultiLabelQuestion,
    TrainingDataForTextClassification,
    ArgillaTrainer
)

dataset = rg.FeedbackDataset(
    guidelines="Add some guidelines for the annotation team here.",
    fields=[
        rg.TextField(name="text", title="Human prompt"),
    ],
    questions =[
        LabelQuestion(
            name="relevant",
            title="Is the response relevant for the given prompt?",
            labels=["yes","no"],
            required=True,
            visible_labels=None
        ),
        MultiLabelQuestion(
            name="content_class",
            title="Does the response include any of the following?",
            description="Select all that apply",
            labels={"hate": "Hate Speech" , "sexual": "Sexual content", "violent": "Violent content", "pii": "Personal information", "untruthful": "Untruthful info", "not_english": "Not English", "inappropriate": "Inappropriate content"},
            required=False,
            visible_labels=4
        ),
    ]
)
dataset.add_records(
    records=[
        FeedbackRecord(
            fields={"text": "What is your favorite color?"},
            responses=[{"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["hate"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "What do you think about the new iPhone?"},
            responses=[{"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "What is your feeling about the technology?"},
            responses=[{"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["sexual"]}}},
                       {"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate", "sexual"]}}},
                       {"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["hate", "sexual"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "Jesus Christ!"},
            responses=[{"values": {"relevant": {"value": "no"}, "content_class": {"value": ["sexual"]}}},
                       {"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate"]}}}]
        )

    ]
)

# print(dataset.question_by_name("relevant").__all_labels__)

label = LabelQuestionUnification(question=dataset.question_by_name("relevant"), strategy="majority")
training_data = TrainingDataForTextClassification(text=dataset.field_by_name("text"), label=label)

for framework in ["spacy", "transformers", "openai", "spark-nlp"]:
    formatted_data = dataset.prepare_for_training(framework, training_data, fetch_records=False, train_size=0.8)
    print(formatted_data)

trainer = ArgillaTrainer(
    dataset=dataset,
    training_task_mapping=training_task_mapping,
    framework="setfit",
    fetch_records=False
)
trainer.train("test")
```

Closes #2954
Closes #3184
Closes #3152 

**Type of change**

- [X] New feature (non-breaking change which adds functionality)
- [X] Improvement (change adding some improvement to an existing
functionality)

**How Has This Been Tested**

- [ ] Test A
- [ ] Test B

**Checklist**

- [ ] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alvaro Bartolome <alvaro@argilla.io>

---
## [cohnt/drake](https://github.com/cohnt/drake)@[f90899e13f...](https://github.com/cohnt/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Thursday 2023-07-06 19:37:54 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[867c217c57...](https://github.com/MrMelbert/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Thursday 2023-07-06 19:44:21 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [RelativisticMechanic/admixturepy](https://github.com/RelativisticMechanic/admixturepy)@[1453629e10...](https://github.com/RelativisticMechanic/admixturepy/commit/1453629e101cafeaebd671b415e1690ba5730e2b)
#### Thursday 2023-07-06 19:59:07 by RelativisticMechanic

Merge branch 'main' of https://github.com/RelativisticMechanic/admixturepy
Fuck you git

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[8744738e59...](https://github.com/thgvr/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Thursday 2023-07-06 20:20:21 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [swendlcode/CS141](https://github.com/swendlcode/CS141)@[986c61329f...](https://github.com/swendlcode/CS141/commit/986c61329f2c0602fd5116e54b682b77e27765c1)
#### Thursday 2023-07-06 20:24:39 by swendlcode

Update README.md

CS& 141 - Computer Science I Java
Credits: 5
Course uses programming language Java to illustrate concepts in engineering and computer science. Introduces students to problem solving methods, algorithm development, and object-oriented design. Students design, implement, document and debug Java computer programs.

Enrollment Requirement: (CS 108 or 109 or CS 120/ENGR 120 or CS& 131) and MATH& 142 or higher with grades of 2.5 or higher; or instructor consent.

Satisfies Requirement: Natural Science
Course Fee: $25.00

Course Outcomes:
Students who successfully complete this class will be able to:
​Design, implement, document, test and debug Java computer code while using an IDE.
Use variables, constants and various data types in computer programs correctly within the appropriate scope of the variable.
Create methods with single and multiple arguments and return values.
Use standard Java commands in written programs.
Create, initialize, and access single and multidimensional arrays as appropriate for Java programs.
Explain the philosophy of object-oriented design and the concepts of encapsulation, abstraction, inheritance, and polymorphism as they are implement in the students program code.
Comment the computer code correctly for human understanding.

Program Outcomes
Provide detailed and accurate descriptions of various physical systems.
Solve multi-step problems in physical analysis.
Identify pertinent elements of physical systems and problems.
Design meaningful experiments and clearly report their conclusions.
Interpret scientific data including the results of experiments designed by others.
Apply mathematical tools to the solution of complex problems.
Use electronic and numerical instruments as tools for investigation and analysis.


College-wide Outcomes
Critical Thinking - Critical thinking finds expression in all disciplines and everyday life. It is characterized by an ability to reflect upon thinking patterns, including the role of emotions on thoughts, and to rigorously assess the quality of thought through its work products. Critical thinkers routinely evaluate thinking processes and alter them, as necessary, to facilitate an improvement in their thinking and potentially foster certain dispositions or intellectual traits over time.
Quantitative and Symbolic Reasoning - Quantitative Reasoning encompasses abilities necessary for a student to become literate in today’s technological world. Quantitative reasoning begins with basic skills and extends to problem solving.

---
## [rbt-c/evals](https://github.com/rbt-c/evals)@[d0e7844c48...](https://github.com/rbt-c/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Thursday 2023-07-06 20:34:43 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [rbt-c/evals](https://github.com/rbt-c/evals)@[fabca8cebb...](https://github.com/rbt-c/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Thursday 2023-07-06 20:34:43 by Nick Clyde

Heart Disease Prediction (#538)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [ESP32DE/Boot-Linux-ESP32S3-Playground](https://github.com/ESP32DE/Boot-Linux-ESP32S3-Playground)@[ac0b18f260...](https://github.com/ESP32DE/Boot-Linux-ESP32S3-Playground/commit/ac0b18f2604a9f82f898bd28d0424cd21e8f51e7)
#### Thursday 2023-07-06 20:56:48 by rudi ;-)

Add files via upload

mpy_m5stackcores3.bin
N16(quad) R8(quad) pointed to N8(quad)R8(quad) means you can theoretical run on N8(quad)R8(quad) also on N16(quad)R8(quad) also on N32(quad)R8(qaud) ...as long they are quad.
 - m5stack branded FW bin for the m5stackcores3

mpy_N8qdR8ot.bin
- olimex Ltd branded FW bin for ESP32-S3- N8(quad) R8(octal)
   example ESP32-S3-DevKit-Lipo OSHW board from Olimex Ltd
   example Espressif'S ESP32-S3-Devkit N8R8 which has 8MB Flash quad and 8 MB Psram octal
   ....


flash it to 0x0 
do not change FW binary
only for engineering tests 
not for products

m5stackcores3
user: root
pwd: m5stack  

olimex
user: root
pwd: olimex


whats inside:
native #jcmvbkbc #esp32s3 #linux #esp32  Port 
native #micropython port for the xtensa linux port !
which has also 
- native Board Port ( ESP32-S3 ) and in this case only Blinky / Gpio's testing IO0, IO1, IO2

micropython is not in the path installed for few compatibility reason - installed under
/media and will go in future things under /usr/bin i think. 

you go there with cd /media
you can list the directory with ls /media from any place or in this folder simple by ls
you find there 3 mpy files for IO testing 0, 1, 2
if you own the m5tackcores3 you can blinky the green led from boot set pin
simple run in the folder /media
./micropython blinky0.py

it will load the file and run the file and your blinky is working

you can view the mpy files example -0 by
cat /media/blinky0.py

you see can call micropython shell in the folder /media
./micropython

and also you can then there import the files simple by using import in the micropython shell
import blinky0
 

note:
i did limit the sleep by unsigned int so if you are using this by own testings by import this as your obj
you can view the inside by 

import blinky0
dir(blinky0)

you see then the possibles
example
blinky0.w1ts()

will blink your gpio on :) ( active low ) 

blinky0.w1tc()

will blink your gpio off



also you can check this
sys
os
uos

and also you can check what you can do with this by

dir(os)

and if you import to your own instance example

import os as myos

you can then use myos 

dir(myos)

and so on..

check this
https://github.com/ESP32DE/Boot-Linux-ESP32S3-Playground/tree/main/history#5-july-2023


there a few things installed - but not all and not for production
it shows only the "..native micropython port it's done"  work and now we are there where we want go step by step deeper :)

to do:
step by step creating device tree for more linux kernel work and userspace
parallel step by step creating more micropython working files.

Note: 
you can not work in this native micropython how you work on a REPL ENV on an ESP32 Micropython port.
in this REPL work there is no "housekeeper" for your lovely MCU  and you have no OS in the back..

this native micropython is working under the native linux kernel eyes. just in time not hashed and not protected, but will come. 
the linux kernel is your Back OS and housekeeper and friend. first you give hardware access by DTS and Kernel for the userspace
then you can use it in the native micropython port. you got an real native linux port as eMbedded OS for your Xtensa MCU like ESP32, ESP32-S2 and ESP32-S3.
Just in time it happens all on ESP32-S3, but also parallel work is in the house on ESP32-S2, and sure ESP32 need more time and is not stable just in time.... but wait for the finale! :) .. waiting for this momen since 9 years since ESP8266 was born. good things need a while :)

Led are active low so if you connect to IO0 or IO1 or IO2 a LED you should go with an resistor to 3V3 and LED pin, the other LED pin goes to the GPIO.
it is just a showing up where the playground stand is now.

there comes also a further image for the lilyGO T-Deck. just in time this happens in will upload in few hour. please be patient :)
[any question ](https://twitter.com/eMbeddedHome/status/1676785814506725377) 

in the history folder there comes also time to time more infos.
this playground goes step by step. also all src code will upload.
later more infos

next steps:
- second CPU
- multiTask
- networking
- WiFi
- .....

have phun :)

---
## [danieljharvey/mimsa](https://github.com/danieljharvey/mimsa)@[e26ca2a932...](https://github.com/danieljharvey/mimsa/commit/e26ca2a9320e5c59b7b12433bc7d36b2cdfa8b99)
#### Thursday 2023-07-06 21:34:10 by Daniel Harvey

Actually typecheck multiple definitions (#962)

* Test module typechecking more throughly

* Damn this shit is fucked

* We need to make these types stricter

* Skippy

* Nice

---
## [ryanosull/BurgerBuddy](https://github.com/ryanosull/BurgerBuddy)@[7a971b45f8...](https://github.com/ryanosull/BurgerBuddy/commit/7a971b45f8f2f1347edaf22e20c11f6bb24eb786)
#### Thursday 2023-07-06 21:57:31 by William Ryan OSullivan

Revert "everything working as expected right now. postman works, localStorage contains uid. whatever fucks up next is fucked. and fuck you late night commits - too early for this shit"

This reverts commit a7a86e2a00f484fd00b133c3dc14c19b2f3071ea.

---
## [githubGourav/githubGourav2](https://github.com/githubGourav/githubGourav2)@[bb41d59244...](https://github.com/githubGourav/githubGourav2/commit/bb41d592442b7b3bbdceb0db4b9e72dcae509675)
#### Thursday 2023-07-06 22:28:12 by githubGourav

Add files via upload

Task 1 - User Overview Analysis 
The lifeblood of any business is its customers. Businesses are always finding ways to better understand their customers so that they can provide more efficient and tailored solutions to them. Exploratory Data Analysis is a fundamental step in the data science process. It involves all the processes used to familiarize oneself with the data and explore initial insights that will inform further steps in the data science process.

It is always better to explore each data set using multiple exploratory techniques and compare the results. The goal of this step is to understand the dataset and identify the missing values & outliers if any using visual and quantitative methods to get a sense of the story it tells. It suggests the next logical steps, questions, or areas of research for your project.

For the actual telecom dataset, you‘re expected to conduct a full User Overview analysis & the following sub-tasks are your guidance: 
Start by identifying the top 10 handsets used by the customers.
Then, identify the top 3 handset manufacturers
Next, identify the top 5 handsets per top 3 handset manufacturer
Make a short interpretation and recommendation to marketing teams

In telecommunication, CDR or Call Detail Record is the voice channel and XDR is the data channel equivalent. So here, consider xDR as data sessions Detail Record. In xDR, user behaviour can be tracked through the following applications:  Social Media, Google, Email, Youtube, Netflix, Gaming, and Others. 

 
 
Task 1.1 - Your employer wants to have an overview of the users’ behaviour on those applications.   
Aggregate per user the following information in the column  
number of xDR sessions
Session duration
the total download (DL) and upload (UL) data
the total data volume (in Bytes) during this session for each application

Task 1.2 - Conduct exploratory data analysis on those data & communicate useful insights. Ensure that you identify and treat all missing values and outliers in the dataset by replacing them with the mean of the corresponding column.
You’re expected to report about the following using Python script and slide  :
Describe all relevant variables and associated data types (slide). 
Analyze the basic metrics (mean, median, etc) in the Dataset (explain) & their importance for the global objective.
Conduct a Non-Graphical Univariate Analysis by computing dispersion parameters for each quantitative variable and provide useful interpretation. 
Conduct a Graphical Univariate Analysis by identifying the most suitable plotting options for each variable and interpreting your findings.
Bivariate Analysis – explore the relationship between each application & the total DL+UL data using appropriate methods and interpret your findings. 
Variable transformations – segment the users into the top five decile classes based on the total duration for all sessions and compute the total data (DL+UL) per decile class. 
Correlation Analysis – compute a correlation matrix for the following variables and interpret your findings: Social Media data, Google data, Email data, Youtube data, Netflix data, Gaming data, and Other data 
Dimensionality Reduction – perform a principal component analysis to reduce the dimensions of your data and provide a useful interpretation of the results (Provide your interpretation in four (4) bullet points maximum). 
Task 2 - User Engagement Analysis
As telecom brands are the data providers of all online activities, meeting user requirements, and creating an engaging user experience is a prerequisite for them. Building & improving the QoS (Quality of Service) to leverage the mobile platforms and to get more users for the business is good but the success of the business would be determined by the user engagement and activity of the customers on available apps. 

In telecommunication, tracking the user activities on the database sessions is a good starting point to appreciate the user engagement for the overall applications and per application as well. If we can determine the level of engagement of a random user for any application, then it could help the technical teams of the business to know where to concentrate network resources for different clusters of customers based on the engagement scores.

In the current dataset you’re expected to track the user’s engagement using the following engagement metrics: 
sessions frequency 
the duration of the session 
the session total traffic (download and upload (bytes))

Task 2.1 - Based on the above submit the Python script and slide:
Aggregate the above metrics per customer id (MSISDN) and report the top 10 customers per engagement metric 
Normalize each engagement metric and run a k-means (k=3) to classify customers into three groups of engagement. 
Compute the minimum, maximum, average & total non-normalized metrics for each cluster. Interpret your results visually with accompanying text explaining your findings.
Aggregate user total traffic per application and derive the top 10 most engaged users per application
Plot the top 3 most used applications using appropriate charts.  
Using the k-means clustering algorithm, group users in k engagement clusters based on the engagement metrics: 
What is the optimized value of k (use the elbow method for this)?  
Interpret your findings. 

Task 3 - Experience Analytics
The Telecommunication industry has experienced a great revolution in the last decade. Mobile devices have become the new fashion trend and play a vital role in everyone's life. The success of the mobile industry is largely dependent on its consumers. Therefore, it is necessary for the vendors to focus on their target audience i.e. what are the needs and requirements of their consumers and how they feel and perceive their products. Tracking & evaluating customers’ experience can help organizations to optimize their products and services so that it meets evolving user expectations, needs, and acceptance.

In the telecommunication industry, the user experience is related, most of the time, to network parameter performances or the customers’ device characteristics.  

In this section, you’re expected to focus on network parameters like TCP retransmission, Round Trip Time (RTT), Throughput, and the customers’ device characteristics like the handset type to conduct a deep user experience analysis. The network parameters are all columns in the dataset. The following questions are your guidance to complete the task. For this task, you need a Python script that includes all solutions to tasks.

Task 3. 1 - Aggregate, per customer, the following information (treat missing & outliers by replacing with the mean or the mode of the corresponding variable):
Average TCP retransmission
Average RTT
Handset type
Average throughput
Task 3.2 - Compute & list 10 of the top, bottom and most frequent:
TCP values in the dataset. 
RTT values in the dataset.
Throughput values in the dataset.
Task 3.3 - Compute & report:
The distribution of the average throughput per handset type and provide interpretation for your findings.
The average TCP retransmission view per handset type and provide interpretation for your findings.
Task 3.4 - Using the experience metrics above, perform a k-means clustering (where k = 3) to segment users into groups of experiences and provide a brief description of each cluster. (The description must define each group based on your understanding of the data)

---
## [weeamoo/2069](https://github.com/weeamoo/2069)@[f25a4fab60...](https://github.com/weeamoo/2069/commit/f25a4fab607b75a6f611ccf830965b08a9087948)
#### Thursday 2023-07-06 22:33:41 by Weeamoo

Revert "FUCK YOU BALTIMORE"

This reverts commit 80355f35a314257c188291e98fc80adac5d6995e.

---

