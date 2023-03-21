## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-20](docs/good-messages/2023/2023-03-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,130,448 were push events containing 3,235,142 commit messages that amount to 261,644,635 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [makigumo/mpv](https://github.com/makigumo/mpv)@[6f7506b660...](https://github.com/makigumo/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Monday 2023-03-20 00:21:54 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [gurking/Citadel-Station-13-RP](https://github.com/gurking/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/gurking/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Monday 2023-03-20 00:56:39 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [gurking/Citadel-Station-13-RP](https://github.com/gurking/Citadel-Station-13-RP)@[d261466765...](https://github.com/gurking/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Monday 2023-03-20 00:56:39 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [gurking/Citadel-Station-13-RP](https://github.com/gurking/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/gurking/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Monday 2023-03-20 00:56:39 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[ef9d0c61a3...](https://github.com/carlarctg/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Monday 2023-03-20 01:04:10 by Moonshanks

Altitude Control: Console, Skills, TGUI, Shuttle, OB, And Hijack changes. (#2760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
This pull request adds a feature via the
/machinery/computer/attitude_control_console.

The USS Almayer can now be "moved" between three different levels of
orbit/proximity to the AO:

High,
Optimal,
Low

Each level comes with changes to the duration of transport timers, time
to transport during hijack, and OB cooldown timer, equal to the
GLOB.ship_alt value.

High makes OB cooldowns take 200 seconds longer, dropship transport
times take 50% longer, and the dropship hijack transport time take 50%
longer

Optimal, the default which will stay in place if no one touches the
console leaves everything with their default times and cooldowns,

Low, OB cooldowns take 200 shorter, dropship transport times are 50%
shorter, the dropship hijack transport time is 50% shorter.

While in Low orbit the Almayer will periodically shake (50% chance to
shake every 30 seconds), the Almayer's thrusters will also start
building up heat as they battle with making minor adjustments due to the
dangerous proximity to the AO. They will gain 10% of their max heat each
30 seconds, once they reach 100% the ship will be forced into the
highest orbit to cool off, and cool off slower than normal (5% every 30
seconds) until its orbit is changed.

While in Optimal or High orbit the Almayer thrusters will cool off by
10% per 30 seconds.

The Almayer's orbit may only be changed by those with a "navigations"
skill of 1. (only the CO and Synth -- EDIT: XO now has the skill too --
currently but I may add a dedicated RP role for this mechanic later down
the line). The orbital level may only be changed every 90 seconds and
when it changes the ship will shake violently causing every mob on the z
level to fall over.

This PR does not place the Altitude Control Console on the map, so
currently, these features don't do anything within a normal round unless
staff spawns in the console, however I will be uploading a mapping PR
changing the Astronavigations deck if this PR is accepted.

Planned for the future but not yet approved connected to this PR is the
"Navigations Officer" the highest auxiliary support personnel with
skills the same as an SO, sans a 1 in Navigations, and a 1 or 2 in
piloting. The idea for this future role would be set out in the PR, but
it would represent a mainly fluff officer role that was unable to deploy
under normal SoP.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This PR is a non-intrusive way to add more nuanced gameplay mechanics to
COs, especially on the quieter rounds when they aren't swamped by OW
duties.

The way the PR is currently designed it doesn't effect any gameplay
balance if it isn't used. If a CO however chooses to use it they have to
pay some level of attention to it or they will overheat the engines and
cause their transport times to be lengthened.

It's a relatively simple way to add more complexity to CIC, and give the
CO/Synth more stuff to do to gain a slight edge.

I have been able to test everything other than the hijack time increase.
However, the line of code handling the hijack time increase is one line
long. Everything else is confirmed as working and the common bugs this
could create have been tested for and not found (transport shows the
right time when the time is modified, OB shows the right cooldown time,
the cooling can't drop the heat% below 0 nor above 100, the TGUI works
without issues, the console can only be used by those with the right
skills, and the knockdown effects all mobs on the Almayer not just
humans).

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

https://www.youtube.com/watch?v=-cbnqNtKyCY - video showing the CO and
Synth using the console, with the knockdown effect and arrest radio
announcements.

https://youtu.be/Qd37iM-4FrQ - video of the overheat function and the
ship shaking due to low orbit

https://www.youtube.com/watch?v=EWLCDZp-9iI - video of the ship being
left on low orbit for too long, and what happens when the engines
overheat

https://www.youtube.com/watch?v=u_ErqfU-nus - video showing the orbital
distance effecting the transport time

https://www.youtube.com/watch?v=j687yqlWLT8 - video showing high orbit
effecting the OB cooldown time.

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
add: added altitude control console and related mechanic
add: added the 'navigations' skill for using the console and applied it
to the CO/Synth
balance: added a mechanic for COs to reduce transport and OB cooldown
times, and increase hijack transport times
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [juno-r1/sophia](https://github.com/juno-r1/sophia)@[29babc1597...](https://github.com/juno-r1/sophia/commit/29babc15975724fba3d034d9befb4da7b172a051)
#### Monday 2023-03-20 01:54:28 by juno-r1

implemented user-defined types. god this fucking sucked

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[6c978308c7...](https://github.com/sqnztb/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Monday 2023-03-20 04:16:02 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4e996ee8e2...](https://github.com/treckstar/yolo-octo-hipster/commit/4e996ee8e274a1194f996832ac65fd0c92b49c49)
#### Monday 2023-03-20 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[f9fe79a307...](https://github.com/lizardqueenlexi/orbstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Monday 2023-03-20 04:48:07 by Dani Glore

Organ Unit Tests & Bugfixes (#73026)

## About The Pull Request

This PR adds a new unit test for all organs, a new unit test for lungs,
and includes improvements for the existing breath and organ_set_bonus
tests. Using the tests, I was able to root out bugs in the organs. This
PR includes an advanced refactor of several developer-facing functions.
This PR certainly represents a "quality pass" for organs which will make
them easier to develop from now on.

### Synopsis of changes:
1. Fixed many fundamental bugs in organ code, especially in
`Insert()`/`Remove()` and their overrides.
2. Added two new procs to `/obj/item/organ` named `on_insert` and
`on_remove`, each being called after `Insert()`/`Remove()`.
3. Added `organ_effects` lazylist to `/obj/item/organ`. Converted
`organ_traits` to lazylist. 2x less empty lists per organ.
4. Adding `SHOULD_CALL_PARENT(TRUE)` to `Insert()`/`Remove()` was very
beneficial to stability and overall code health.
5. Created unit test `organ_sanity` for all usable organs in the game.
Tests insertion and removal.
6. Created unit test `lungs_sanity` for
`/obj/item/organ/internal/lungs`.
7. Improved `breath_sanity` unit tests with additional tests and
conditions.
8. Improved `organ_set_bonus_sanity` unit tests with better
documentation and maintainable code.

---

### Granular bug/fix list:

- A lot of organs are overriding `Insert()` to apply unique
side-effects, but aren't checking the return value of the parent proc
which causes the activation of side-effects even if the insertion
technically fails. I noticed the use-case of applying "unique
side-effects" is repeated across a lot of organs in the game, and by
overriding `Insert()` the potential for bugs is very high; I solved this
problem with inversion-of-control by adding two new procs to
`/obj/item/organ` named `on_insert` and `on_remove`, each being called
after `Insert()` and `Remove()` succeed.
- Many organs, such as abductor "glands", cursed heart, demon heart,
alien hive-node, alien plasma-vessel, etc, were not returning their
parent's `Insert()` proc return value at all, and as a result those
organs `Insert()`s were always returning `null`. I have been mopping
those bugs up in my last few PRs, and now the unit test reveals it all.
Functions such as those in surgery expect a truthy value to be returned
from `Insert()` to represent insertion success, and otherwise it
force-moves the organ out of the mob.
- Fixed abductor "glands" which had a hard-del bug due to their
`Remove()` not calling the parent proc.
- Fixed cybernetic arm implants which had a hard-del bug due to
`Remove()` not resetting their `hand` variable to `null`.
- Fixed lungs gas exchange implementation, which was allowing exhaled
gases to feedback into the inhaled gases, which caused Humans to inhale
much more gas than intended and not exhale expected gases.

### Overview of the `organ_sanity` unit test:

- The new `organ_sanity` unit test gathers all "usable" organs in the
game and tests to see if their `Insert()` and `Remove()` functions
behave as we expect them to.
- Some organs, such as the Nightmare Brain, cause the mob's species to
change which subsequently swaps out all of their organs; the unit test
accounts for these organs via the typecache `species_changing_organs`.
- Some organs are not usable in-game and can't be unit tested, so the
unit test accounts for them via the typecache `test_organ_blacklist`.

### Overview of the `lungs_sanity` unit test:

- This unit test focuses on `/obj/item/organ/internal/lungs` including
Plasmaman and Ashwalker lungs. The test focuses on testing the lungs'
`check_breath()` proc.
- The tests are composed of calling `check_breath` with different gas
mixes to test breathing and suffocation.
- Includes gas exchange test for inhaled/exhaled gases, such as O2 to
CO2.

### Improvements to the `breath_sanity` unit tests:

- Added additional tests for suffocation with empty internals, pure
Nitrogen internals, and a gas-less turf.
- Includes slightly more reliable tests for internals tanks.

## Why It's Good For The Game

**Organs and Lungs were mostly untested. Too many refactors have been
submitted without the addition of unit tests to prove the code works at
all.** Time to stop. _Time to get some help_. Due to how bad the code
health is in organs, any time we've tried to work with them some sort of
bug caused them to blow up in our faces. I am trying to fix some of that
by establishing some standard testing for organs. These tests have
revealed and allowed me to fix lot of basic developer errors/oversights,
as well as a few severe bugs.


![image](https://user-images.githubusercontent.com/17753498/220251281-07ef598f-355b-43a9-afd6-1de9690831da.png)

## Changelog

:cl: A.C.M.O.
fix: Fixed lungs gas exchange implementation, so you always inhale and
exhale the correct gases.
fix: Fixed a large quantity of hard-deletes which were being caused by
organs and cybernetic organs.
fix: Fixed many organs which were applying side-effects regardless of
whether or not the insertion failed.
code: Added unit tests for Organs.
code: Added unit tests for Lungs.
code: Improved unit tests for breathing.
code: Improved unit tests for DNA Infuser organs.
/:cl:

---
## [nsherwood1/tgstation](https://github.com/nsherwood1/tgstation)@[97f567fdc7...](https://github.com/nsherwood1/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Monday 2023-03-20 05:27:44 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [nsherwood1/tgstation](https://github.com/nsherwood1/tgstation)@[fedf2f3a26...](https://github.com/nsherwood1/tgstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Monday 2023-03-20 05:27:44 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [nsherwood1/tgstation](https://github.com/nsherwood1/tgstation)@[3f61c4c2cd...](https://github.com/nsherwood1/tgstation/commit/3f61c4c2cdaba5de603e4ee32e9655f111cbc86d)
#### Monday 2023-03-20 05:27:44 by jimmyl

Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

---
## [nsherwood1/tgstation](https://github.com/nsherwood1/tgstation)@[27c35bfa0b...](https://github.com/nsherwood1/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Monday 2023-03-20 05:27:44 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [pmall-neu/rsdd](https://github.com/pmall-neu/rsdd)@[3b08d01883...](https://github.com/pmall-neu/rsdd/commit/3b08d018839de0af60eeb0315ac706ea1799b44d)
#### Monday 2023-03-20 06:08:23 by Matt Wang

refactor canonicalization scheme out of `SddBuilder` into trait; create generic `SddBuilder` (#56)

The main goal of this *very hefty* PR is to allow two **canonicalization schemes**:

- one based on the canonicity property, which requires compression to perform pointer equality
- one based on "semantic hashing", where we instead uniquify an Sdd based on a weighted model count with some randomly-generated weights

After talking to Steven, we chose to use a mixin approach - the `SddBuilder` becomes generic, taking in a "canonicalization scheme" trait. Each implementer of the trait needs to be able to do any operation related to checking if two SDDs are equal - this includes SDD equality, but also a host of related backend work, including:

- managing a `BackedRobinhoodTable` for BinarySDDs and SDDs
- implementing a hasher for the above table, as well as utility get and insert functions
- cache the apply operation

To properly implement the above, I also had to apply the same genericizing approach to:

- the apply cache, which now conforms to an `ApplyCacheMethod`
- the hasher for the BackedRobinhoodTable, which now allows an arbitrary hash function rather than `FxHasher` - which becomes the semantic hash when necessary. To avoid polluting this struct, I instead require a hash function to be passed to get/insertion.

I pulled all of these functions out of the `SddBuilder`; the defaults move to the `CompressionCanonicalizer`, which should behave **exactly the same** as the previous `SddBuilder`. I've soft-verified this with tests.

Since I'm making a complex struct generic, this PR also touches many files - mostly replacing instances of a naked `SddBuilder` with `SddBuilder<CompressionCanonicalizer>`. I've localized "new implementation code" to `canonicalize.rs` and the files for the apply cache and bump table.

I've also manually added some WMC code for `SddAnd`, `SddOr`, and `BinarySdd` that I'd like to remove - see below. I've also temporarily added a `sub` operator to the finite field.

I'm merging this PR in because:

1. I'm confident that this doesn't change the default behaviour, and
2. I'm worried about branch divergence

## next steps

There are a handful of things that still should be done.

- undoing my temporary hacks:
    - ideally, I should deduplicate the semantic hashing work from the hard-coded implementations for `SddAnd`, `SddOr`, and `BinarySdd`. I'd like to somehow make this a WMC, but I'm not sure how to do that without recreating a new `SddPtr`
    - if we plan on keeping the finite field as a semiring, we should remove my `-` before it gets into the rest of the codebase
- running larger benchmarks on number of nodes, correctness metrics
    - I've ... bricked my instance I think? Or, I can't log in. But, the plan was to:
    - try a handful of different primes - likely within a few orders of magnitude
    - try different CNFs of varying complexity
    - measure:
        - overall correctness - and how it scales with primes
        - number of nodes between uncompressed, compression-compressed, and semantic-compression; I may have to exclude the uncompressed versions for large CNFs
- optimizing references over cloning
    - right now, there's a *ton* of cloning that goes on since I was more concerned about correctness than efficiency. It's mostly localized to creating the `Canonicalizer`, so it can be amortized across SDD operations; but, I think it warrants a serious look
    - in particular, most of the Canonicalizer's operations aren't mutable anyways, so with some shuffling around I should be able to make most of them immutable read references anyways! 

## testing

### unit tests, quickcheck

I've written a few more unit tests and quickcheck tests to verify that this works for small cases. Even with a relatively large quickcheck sample size, the semantic canonicalizer still maintains its uniqueness benefits most of the time, which is great!

(I planned on doing some more testing on the server, but I'm now curiously locked out of my account after running a large test - concerning)

Some useful quickcheck tests to run:

```
$ QUICKCHECK_TESTS=20000 cargo test prob_equiv_sdd_eq_vs_prob_eq
$ QUICKCHECK_TESTS=20000 cargo test prob_equiv_sdd_inequality
$ QUICKCHECK_TESTS=20000 cargo test qc_sdd_canonicity
```

### script

I've rewritten the compare-canonicalize script to better test this difference. Here's an example of usage:

```sh
$ cargo run --bin semantic_hash_experiment -- --file cnf/rand-3-25-75-1.cnf
```

Interestingly, I haven't been able to get substantial differences in the number of nodes for small CNFs. I think this is a bug in my implementation or my benchmark. However, given that the default canonicalizer still works as intended, I'm thinking that we merge this in now before it diverges more from `main`.

---
## [zazke/dotfiles](https://github.com/zazke/dotfiles)@[11aedecab8...](https://github.com/zazke/dotfiles/commit/11aedecab8a8ef7d54f0fa2f1adc67ac78ba42eb)
#### Monday 2023-03-20 07:18:23 by Mitsuo Tokumori

Simplify bashrc, modify install.sh, add nvim/

bashrc is now simpler.  Hopefully with the same functionality.  Remove
some of the default stuff that came with Debian years ago.  Start with
default Archlinux bashrc as base (very minimal).

install.sh now recommends only using slinks.  nvim and zathura now get
linked directory-wise.  This is way better because added configuration
files will get here seamlessly.  Doing diffs between 2 independent
copies is painful.

Now I'm transitioning to NeoVim.  I've copied all relevant config from
vimrc (Vim) to init.vim (NeoVim).  Very promising.  File got smaller and
more organized in my opinion.

PD: Cheers, this pulse15 laptop is amazing.

---
## [ashishwasnikk/NETFLIX-MOVIES-AND-TV-SHOWS-CLUSTERING-Unsupervised-ML-Project-by-Ashish-Wasnik](https://github.com/ashishwasnikk/NETFLIX-MOVIES-AND-TV-SHOWS-CLUSTERING-Unsupervised-ML-Project-by-Ashish-Wasnik)@[761458a1d8...](https://github.com/ashishwasnikk/NETFLIX-MOVIES-AND-TV-SHOWS-CLUSTERING-Unsupervised-ML-Project-by-Ashish-Wasnik/commit/761458a1d8fbbadfa00465cfc92c5fc0738b768d)
#### Monday 2023-03-20 08:28:51 by Ashish Panjabrao Wasnik

Add files via upload


Capstone Project-4 Submission

NETFLIX MOVIES & TV SHOWS CLUSTERING 
Ashish Panjabrao Wasnik 


    


Ashish Panjabrao Wasnik- ashish.wasnikk@gmail.com


 
GitHub Link: -
 
Ashish Wasnik: - https://github.com/ashishwasnikk/NETFLIX-MOVIES-AND-TV-SHOWS-CLUSTERING-Unsupervised-ML-Project-by-Ashish-Wasnik.git





 
Abstract
Netflix is a company that manages a large collection of TV shows and movies, streaming it anytime via online. This business is profitable because users make a monthly payment to access the platform. However, customers can cancel their subscriptions at any time. Therefore, the company must keep the users hooked on the platform and not lose their interest. This is where recommendation systems start to play an important role, providing valuable suggestions to users is essential.

Introduction

Netflix’s recommendation system helps them increase their popularity among service providers as they help increase the number of items sold, offer a diverse selection of items, increase user satisfaction, as well as user loyalty to the company, and they are very helpful in getting a better understanding of what the user wants. Then it’s easier to get the user to make better decisions from a wide variety of movie products. With over 139 million paid subscribers (total viewer pool -300 million) across 190 countries, 15,400 titles across its regional libraries and 112 Emmy Award Nominations in 2018 — Netflix is the world’s leading Internet television network and the most-valued largest streaming service in the world. The amazing digital success story of Netflix is incomplete without the mention of its 




recommender systems that focus on personalization. There are several methods to create a list of recommendations according to your preferences. You can use (Collaborative-filtering) and
(Content-based Filtering) for recommendation.

Problem Statement

This dataset consists of tv shows and movies available on Netflix as of 2019. The dataset is collected from Flixable which is a third-party Netflix search engine.
In 2018, they released an interesting report which shows that the number of TV shows on Netflix has nearly tripled since 2010. The streaming service’s number of movies has decreased by more than 2,000 titles since 2010, while its number of TV shows has nearly tripled. 

In this project, you are required to do
	Exploratory Data Analysis
	Understanding what type content is available in different countries
	Is Netflix increasingly focused on TV rather than movies in recent years?
	Clustering similar content by matching text-based features.




Objective 

NetflixRecommender recommends Netflix movies and TV shows based on a user's favourite movie or TV show. It uses a Natural Language Processing (NLP) model and a K-Means Clustering model to make these recommendations. These models use information about movies and TV shows such as their plot descriptions and genres to make suggestions. The motivation behind this project is to develop a deeper understanding of recommender systems and create a model that can perform Clustering on comparable material by matching text-based attributes. Specifically, thinking about how Netflix create algorithms to tailor content based on user interests and behavior.

Data Description
Attribute Information:
The dataset provided contains 7787 rows and 12 columns.
The following are the columns in the dataset:
	Show id: Unique identifier of the record in the dataset
	Type: Whether it is a TV show or movie
	Title: Title of the show or movie
	Director: Director of the TV show or movie
	Cast: The cast of the movie or TV show
	Country: The list of the country in which a show/ movie is released or watched





	Date added: The date on which the content was onboarded on the Netflix platform
	Release year: Year of the release of the show/ movie
	Rating: The rating informs about the suitability of the content for a specific age group
	Duration: Duration is specified in terms of minutes for movies and in terms of the number of seasons in the case of TV shows
	Listed in: This columns species the category/ genre of the content
	Description: A short summary about the storyline of the content


Approach

As the problem statement says, understanding what type of content is available in different countries and Is Netflix increasingly focused on TV rather than movies in recent years we have to do clustering on similar content by matching text-based features. For that we used Affinity Propagation, Agglomerative Clustering, and K-means Clustering.







Tools Used

The whole project was done using python, in google Collaboratory. Following libraries were used for analyzing the data and visualizing it and to build the model to predict the Netflix clustring 
	Pandas: Extensively used to load and wrangle with the dataset.
	Matplotlib: Used for visualization.
	Seaborn: Used for visualization.
	Nltk: It is a toolkit build for working with NLP.
	Datetime: Used for analyzing the date variable.
	Warnings: For filtering and ignoring the warnings.
	NumPy: For some math operations in predictions.
	Wordcloud: Visual representation of text data.
	Sklearn: For the purpose of analysis and prediction.
Table1. The above table shows the dataset in the form of Pandas Data Frame



Steps Involved
The following steps are involved in the project

1. Handling missing values: 
We will need to replace blank countries with the mode (most common) country. It would be better to keep director because it can be fascinating to look at a specific filmmaker's movie. As a result, we substitute the null values with the word 'unknown' for further analysis. 
There are very few null entries in the date_added fields thus we delete them. 

2. Duplicate Values Treatment: 
Duplicate values dose not contribute anything to accuracy of results. 
Our dataset dose not contains any duplicate values.







3. Natural Language Processing (NLP) Model:

For the NLP portion of this project, I will first convert all plot descriptions to word vectors so they can be processed by the NLP model. Then, the similarity between all word vectors will be calculated using cosine similarity (measures the angle between two vectors, resulting in a score 
between -1 and 1, corresponding to complete opposites or perfectly similar vectors). Finally, I will extract the 5 movies or TV shows with the most similar plot description to a given movie or TV show.

4.  Exploratory Data Analysis: 

Exploratory Data Analysis (EDA) as the name suggests, is used to analyze and investigate datasets and summarize their main characteristics, often employing data visualization methods. It helps determine how best to manipulate data sources to get the answers you need, making it easier for data scientists to discover patterns, spot anomalies, test a hypothesis, or check assumptions. It also helps to understand the relationship between the variables (if any) and it will be useful for feature engineering. It helps to understand data well before making any assumptions, to identify obvious errors, as well as better understand patterns within data, detect 






outliers, anomalous events, find interesting relations among the variables.
After mounting our drive and fetching and reading the dataset given, we performed the Exploratory Data Analysis for it.
To get the understanding of the data and how the content is distributed in the dataset, its type and details such as which countries are watching more and which type of content is in demand etc has been analyzed in this step.
Explorations and visualizations are as follows:
	 Proportion of type of content
	Country-wise count of content
	Total release for last 10 years.
	Type and Rating-wise content count
	Top 10 genres in movie content
	Top 20 Actors on Netflix.
	Length distribution of movies.
	Season-wise distribution of TV shows.
	Count of content appropriate for different ages.
	Age-appropriate content count in top 10 countries with maximum content.
	Proportion of movies and TV shows content appropriate for different ages.
	Season wise distribution of TV shows.
	Longest TV shows.
	Top 10 topics on Netflix.
	Extracting the features and creating the document term metrix.
	Topic modeling using LDA and LSA.
	Most important features of topic.

5. Missing or Null value treatment:
In datasets, missing values arise due to numerous reasons such as errors, or handling errors in data.
We checked for null values present in our data and the dataset contains a null value.
In order to handle the null values, some columns and some of the null values are dropped.

6. Hypothesis from the data visualized:
Hypothesis testing is done to confirm our observation about the population using sample data, within the desired error level. Through hypothesis testing, we can determine whether we have enough statistical evidence to conclude if the hypothesis about the population is true or not.
We have performed hypothesis testing to get the insights on duration of movies and content with respect to different variables.

7. Tfidf vectorization:
TF-IDF is an abbreviation for Term Frequency Inverse Document Frequency. This is a very common algorithm to transform text into a meaningful representation of numbers which is used to fit a machine learning algorithm for prediction.



We have also utilized the PCA because it can help us improve performance at a very low cost of model accuracy. Other benefits of PCA include reduction of noise in the data, feature selection (to a certain extent), and the ability to produce independent, uncorrelated features of the data.
So, it's essential to transform our text into tfidf vectorizer, then convert it into an array so that we can fit into our model.
	Finding number of clusters
The goal is to separate groups with similar characteristics and assign them to clusters.
We used the Elbow method and the Silhouette score to do so, and we have determined that 28 clusters should be an optimal number of clusters.
	Fitting into model
In this task, we have implemented a K means clustering algorithm. K-means is a technique for data clustering that may be used for unsupervised machine learning. It is capable of classifying unlabeled data into a predetermined number of clusters based on similarities (k).

8. Data Preprocessing:
Removing Punctuation: Punctuations does not carry any meaning in clustering, so removing punctuations helps to get rid of unhelpful parts of the data, or noise. 
Removing stop-words: Stop-words are basically a set of commonly used words in any language, not just in English. If we remove the words that are very commonly used in a given language, we can focus on the important words instead. 
Stemming: Stemming is the process of removing a part of a word, or reducing a word to its stem or root. Applying stemming to reduce words to their basic form or stem, which may or may not be a legitimate word in the language.

9. Clustering:
Clustering (also called cluster analysis) is a task of grouping similar instances into clusters. More formally, clustering is the task of grouping the population of unlabeled data points into clusters in a way that data points in the same cluster are more similar to each other than to data points in other clusters. The clustering task is probably the most important in unsupervised learning, since it has many applications.
for example: 
• Data analysis: often a huge dataset contains several large clusters, analyzing which separately, you can come to interesting insights. 
• Anomaly detection: as we saw before, data points located in the regions of low density can be considered as anomalies 
• Semi-supervised learning: clustering approaches often helps you to automatically label partially labeled data for classification tasks.
• Indirectly clustering tasks (tasks where clustering helps to gain good results): recommender systems, search engines, etc. 
• Directly clustering tasks: customer segmentation, image segmentation, etc.
Building a clustering model
Clustering models allow you to categorize records into a certain number of clusters. This can help you identify natural groups in your data.
Clustering models focus on identifying groups of similar records and labeling the records according to the group to which they belong. This is done without the benefit of prior knowledge about the groups and their characteristics. In fact, you may not even know exactly how many groups to look for. 
This is what distinguishes clustering models from the other machine-learning techniques—there is no predefined output or target field for the model to predict.
These models are often referred to as unsupervised learning models, since there is no external standard by which to judge the model's classification performance.

10. Topic Modeling:
• Latent Semantic Analysis (LSA)
LSA, which stands for Latent Semantic Analysis, is one of the foundational techniques used in topic modeling. The core idea is to take a matrix of documents and terms and try to decompose it into separate two matrices – • A document-topic matrix
• A topic-term matrix.



Therefore, the learning of LSA for latent topics includes matrix decomposition on the document-term matrix using Singular value decomposition. It is typically used as a dimension reduction or noise reducing technique.

• Latent Dirichlet Allocation (LDA)
LDA is a generative probabilistic model that assumes each topic is a mixture over an underlying set of words, and each document is a mixture of over a set of topic probabilities.

11. Clusters Model Implementation
	Affinity Propagation
	Agglomerative Clustering
	K-means Clustering
	Affinity Propagation
Affinity propagation (AP) is a graph-based clustering algorithm similar to k Means or K medoids, which does not require the estimation of the number of clusters before running the algorithm. Affinity propagation finds “exemplars” i.e., members of the input set that are representative of clusters.
We used Euclidean distance as an affinity estimator. After that, number of clusters we got here:

 
Figure1. Visualization of Custer and Silhouette Coefficient.


	Agglomerative Clustering

The agglomerative clustering is the most common type of hierarchical clustering used to group objects in clusters based on their similarity. ... Next, pairs of clusters are successively merged until all clusters have been merged into one big cluster containing all objects.
 Figure2. Silhouette score and visualization




12. K-means Clustering

K-means clustering is one of the simplest and popular unsupervised machine learning algorithms. Typically, unsupervised algorithms make inferences from datasets using only input vectors without referring to known, or labelled, outcomes.
 K-means algorithm works: 
To process the learning data, the K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then 
performs iterative (repetitive) calculations to optimize the positions of the centroids. It halts creating and optimizing clusters when either: 
• The centroids have stabilized — there is no change in their values because the clustering has been successful.
 • The defined number of iterations has been achieved.
K-means algorithm is an iterative algorithm 
that tries to partition the dataset into K pre-defined distinct non overlapping subgroups where each data point belongs to only one  group.   Figure3. Ideal clustering

k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.
We created the sample data using build blobs and used range n_clusters to
specify the number of clusters we wanted to utilize in k means.
Silhouette score and visualization
For clusters = 2 The average silhouette score is : 0.7049787496083262
For clusters = 3 The average silhouette score is : 0.5882004012129721
For clusters = 4 The average silhouette score is : 0.6505186632729437
For clusters = 5 The average silhouette score is : 0.56376469026194
For clusters = 6 The average silhouette score is: 0.4504666294372765







 13. Silhouette Coefficient or silhouette score(meaning)
Silhouette Coefficient or silhouette score is a metric used to calculate the goodness of a clustering technique. Its value ranges from -1 to 1. 1: Means clusters are well apart from each other and clearly distinguished. ... a= average intra-cluster distance i.e., the average distance between each point within a cluster.




1.  Silhouette’s Coefficient-
If the ground truth labels are not known, the evaluation must be performed utilizing the model itself. The Silhouette Coefficient is an example of such an evaluation, where a more increased Silhouette Coefficient score correlates to a model with better-defined clusters. The Silhouette Coefficient is determined for each sample and comprised of two scores


	Mean distance between the observation and all other data points in the same cluster. This distance can also be called a mean intra-cluster distance. The mean distance is denoted by a.
	Mean distance between the observation and all other data points of the next nearest cluster. This distance can also be called a mean nearest-cluster distance. The mean distance is denoted by b.
The Silhouette Coefficient s for a single sample is then given as:
s=(b-a)/(max(a,b))
Silhouette score is used to evaluate the quality of clusters created using clustering algorithms such as K-Means in terms of how well samples are clustered with other samples that are similar to each other. The Silhouette score is calculated for each sample of different clusters. To calculate the Silhouette score for each observation/data point, the following distances need to be found out for each observation belonging to all the clusters:
2. Elbow Curve:
The Elbow Curve is one of the most popular methods to determine this optimal value of k.
The elbow curve uses the sum of squared distance (SSE) to choose an ideal value of k based on the distance between the data points and their assigned clusters. 



Conclusion

Tailored recommendations can be made based on information about movies and TV shows. In addition, similar models can be developed to provide valuable recommendations to consumers in other domains. 

	We've done null value treatment, feature engineering, and EDA since loading the dataset then completed assigned tasks.
	Data set contains 7787 rows and 12 columns in that cast and director features contains large number of missing values so we can drop it and we have 10 features for the further implementation.
	We have two types of content TV shows and Movies (30.86% contains TV shows and 69.14% contains Movies)
	Most films were released in the years 2018, 2019, and 2020 and and united nation have the maximum content on Netflix.
	The months of October, November, December and January had the largest number of films and television series released
	On Netflix, Dramas genre contains the maximum content among all of the genres and the most of the content added in December month and less content in February.
	By applying the silhouette score method for n range clusters on dataset we got best score which is 0.244 for 3 clusters it means content explained well on their own clusters, by using elbow method after k = 3 curve gets linear it means k = 3 will be the best cluster
	By applying different clustering algorithms to our dataset. We get the optimal number of clusters is equal to 4.

	We started by removing nan values and converting the Netflix added date to year, month, and day using date time format.
	We did feature engineering, which involved removing certain variables and preparing a dataframe to feed the clustering algorithms.
	For the clustering algorithm, we utilized type, director, nation, released year, genre, and year.
	 Affinity Propagation, Agglomerative Clustering, and K-means Clustering were utilised to build the model.
	 In Affinity Propagation, we had 9 clusters and a Silhouette Coefficient score of 0.244.
	 The final model we used was k-means clustering, which consisted of 2,3,4,5,6 clusters. 4 numbers of clusters give us good fitting.

Dash Web App
I created a Dash web app that utlizes my model to provide film recommendations based on a user's favourite movie or TV show.

REFERENCES:

 https://towardsdatascience.com/silhouette-coefficient-validating-clustering-techniques-e976bb81d10c#:~:text=Silhouette%20Coefficient%20or%20silhouette%20score%20is%20a%20metric%20used%20to,each%20other%20and%20clearly%20distinguished.&text=a%3D%20average%20intra%2Dcluster%20distance,each%20point%20within%20a%20cluster.

https://colab.research.google.com/drive/11APbN2c9PfBm7rROZ9qmqdq6JJX0_Ye5?usp=sharing

https://machinelearningmastery.com/clustering-algorithms-with-python

https://towardsdatascience.com/introduction-to-machine-learning-algorith

---
## [petre-symfony/eloquent-performance-pattern-beyond-or-equal-Ep21](https://github.com/petre-symfony/eloquent-performance-pattern-beyond-or-equal-Ep21)@[7399e29d05...](https://github.com/petre-symfony/eloquent-performance-pattern-beyond-or-equal-Ep21/commit/7399e29d057bb30100eec60df229f9aef815c02c)
#### Monday 2023-03-20 09:40:03 by petrero

23.4 Now let's do some experimenting in mysql workbench.
 First, if we go to our post table we can see our new post fulltext index has been created which is using in fulltext algorithm
 Now it's right to write text aearch query. We select the id and title columns from the posts table where we have a fulltext match in the title and the body against the term fox and we'll do this in the boolean mode. Mysql offers different full text searching modes. One of those is the boolean mode and another is the natural language mode. From my experience the boolean mode leads to better search results.
 Let's run this query. Amazing, that works. We're getting our three fox posts in our search results

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[53aa043da6...](https://github.com/mrakgr/The-Spiral-Language/commit/53aa043da6a0e4c914b1bdb97d9d4bce2106b91d)
#### Monday 2023-03-20 11:14:15 by Marko Grdinić

"8:35am. What a heavy night. I had trouble falling asleep due to all the worries. Any mail? Any replies on Reddit?

Nope. I have the day to myself. I had time to think about how I'll cover the strategy averaging. I'll just compare the performance.

https://mangadex.org/chapter/1592c415-485c-45dd-93c9-2c99b14850df/13

Damn, Kurosaki is good at this.

9:20am. Let me finish the Saki chapter and then I will take a bath. Right now I am doing nothing, and I should be concluding the CFR thing.

10:25am. Done with the bath. Let me start programming. So far, 2 rejects are in, one of them from that shitter place, SKM. At this point I am just wondering whether I'll get any bites at all. I've already started planning for what I want to do if I cannot get a job in this market.

For now let me just finish this portfolio project. I have some interesting ideas for what I want to do.

Since I have web skills now, I am thinking of writing Simulacrum: Hatred as my next web novel project. I am bored of Heaven's Key, and Hatred has been rolling around my mind for years.

Instead posting it on RR, I am going to automate posting on those web sites, assuming they expose an API. I'll make my own platform, and make my future work a true VN. Since I can't make it in ML, I should just do art.

Incidentally that is also the correct strategy for getting a job. Eventually, the accumulation I will be making on RR and similar sites like ScribleHub, as well as Youtube will bear fruit.

In 2023, I am essentially changing my programming philosophy. I should also give ChatGPT a try as a writing assistant. I'll see how it goes.

I haven't really gone all out yet. SD is great, but if I could automate large parts of my writing, I could get a big productivity boost, which would then translate into moneys.

I can keep going forward, doing various useful things. For using SD, I thinking of checking out Enso and doing a Youtube series on that.

This poker project is an eyesore, since nobody will be interested in it, and it is just making me rethread old ground. But I can't deny it is useful.

10:35am. If I want a company like Tenstorrent to be interested in me, I should do a Youtube series on it, and bring it some publicity.

If I want money, I have to graduate from being a programmer, to being a salesman. There is no other way.

```fs
            let f0, f1 = self_prob, 1.0
            let new_unnormalized_policy_average =
                Array.map2 (fun a b -> (f0 * a + f1 * b) / (f0 + f1)) (normalize new_current_regrets) policy_arrays.unnormalized_policy_average
```

Let me try this again. For some reason that other thing is at -0.071 instead of -0.085. I mean `let f0, f1 = self_prob, 2.0`.

After 1500 iterations of training, and 200 testing: -0.078.

Just like before. But 2.0 isn't.

Well, does it matter?

```fs
            let f0, f1 = self_prob, 1.0
            let new_unnormalized_policy_average =
                Array.map2 (fun a b -> (f0 * a + f1 * b) ) (normalize new_current_regrets) policy_arrays.unnormalized_policy_average
```

Let me try this as well.

After 1500 iterations of training, and 200 testing: -0.022.

It works like this.

Forget it. Forget it!

```fs
        let update_policy model actions rewards avg_reward (self_prob, opp_prob) =
            let policy_arrays = get_policy' d model actions
            let new_regrets = Array.map (fun reward -> reward - avg_reward) rewards
            let new_current_regrets = Array.map2 (fun new_regret old_regret -> opp_prob * new_regret + old_regret |> max 0.0) new_regrets policy_arrays.current_regrets
            let f0, f1 = self_prob, 1.0
            let new_unnormalized_policy_average = Array.map2 (fun a b -> (f0 * a + f1 * b) / (f0 + f1)) (normalize new_current_regrets) policy_arrays.unnormalized_policy_average
            d[model] <- {policy_arrays with current_regrets=new_current_regrets; unnormalized_policy_average=new_unnormalized_policy_average}
```

This is how I'll do it!

Let me put that out of the way. No more work on the algorithm. What I need to do is focus on the UI. Let me add buttons so the user can control the iteration count.

> prije svega, hvala na prijavi i javljanju na našu .Net poziciju. S obzirom da trenutno tražimo nešto iskusnije developere (C# i Angular), za sad, nažalost, ne možemo s Vama nastaviti naš selekcijski proces.

My god, I put in 9 years, and they are looking for more experienced devs.

I'll reply asking about that.

12:05pm. I did those two buttons.

Now, what I need to do is add the ability to play against the CFR player, and the coding part of tutorial5 will be complete.

After that I can get back to making the video. In the next one I'll bring in the MC player. After that comes NL Holdem and the neural players.

Let stop the morning session here. I'll figure out how to integrate these players later."

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b8c51e0518...](https://github.com/TaleStation/TaleStation/commit/b8c51e0518218a850ea75f2c911d01b38e9c208c)
#### Monday 2023-03-20 12:11:40 by TaleStationBot

[MIRROR] [MDB IGNORE] Implements AddTraits and RemoveTraits procs for adding/removing multiple traits + swag unit test (#4974)

Original PR: https://github.com/tgstation/tgstation/pull/74037
-----
## About The Pull Request

On the tin, doing it like this means we can reduce our overall line
fingerprint whenever we have to add two or more traits from the same
source on the same target. Especially helps when we get to the 4+ range
of traits, a breath of fresh air even.

Doesn't mean we have to do for loops, as that's already handled within
the define as well. I replaced some of the checks with `length()`
checks, let me know if I should switch it over to something else (maybe
`islist()`)? We stack_trace whenever we're not passed a list reference
on purpose, and sometimes var/lists are null by default (or just empty,
making this redundant).
## Why It's Good For The Game

I commonly feel the urge to write "use `AddTraits()`" or something in
reviews, then am sad when I remember it doesn't exist. I will no longer
be sad.

Can ensure a lot more trait safety as well by using static lists- when
both ADD_TRAIT_LIST and REMOVE_TRAIT_LIST re-use the same list, you are
confident (from a static point of view) that everything that you want to
be adding/removing works.

I may have missed a few things where this could be used, but both macros
implemented in this PR still use the same framework that was being used
in the last four years- so stuff won't break if left untouched. Just a
nifty new tool for developers.

also fixed up some code in the area, numerous bugs were found and
exploded
## Changelog
Nothing that really concerns players (aside from potential breaks, but
I'll audit those myself in the coming 24 hours).

i also didn't use any regexes, this was manual work. soz

bonus unit test: mainly because i wanted to make sure mixing/matching
ADD_TRAIT/REMOVE_TRAIT with ADD_TRAITS/REMOVE_TRAITS would still work,
but i decided I should test all of the "basic" add/remove trait stuff we
have juuust in case

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [catawiki/opentelemetry-ruby-contrib](https://github.com/catawiki/opentelemetry-ruby-contrib)@[e5ba8854bf...](https://github.com/catawiki/opentelemetry-ruby-contrib/commit/e5ba8854bf33140cabfc72198167678291f56c04)
#### Monday 2023-03-20 13:02:05 by Andrew Hayworth

ci: do not test a config that will never succeed (#388)

In this test, we are asserting that the instrumentation is _not_
installed when the `Rack` constant is not present (see the `before`
block for this test case). We then go on to test that the configuration
is the "default" configuration that you'd get with a fresh installation.

The problem is that if the `Rack` constant is not present, then the
`instrumentation-base` code that sets all the defaults for our options
is never run (and logically, why would it?). So these test lines can
never actually succeed.

Unless, of course, the `instrumentation` object we're referring to is
_not_ a pristine, new object. And in fact, depending on what order the
tests run in, our object is _not_ a pristine, new object. If you run
basically any _other_ test in this suite before, then we actually end up
recycling an object that is partially initialzied from a previous test,
and has an internal `@config` object that has some default options.

And so, the test is actually passing some times because of this
non-deterministic behavior. For example, if you run with `SEED=1`, then
the test suite passes (because other tests run first that initialize the
object completely). If you run with `SEED=6372`, it fails (because it is
the very first test run).

The _real_ bug here is that we do not have proper test isolation. I
think that's actually a problem all over the code base, if I'm being
honest about it.

However, I elect not to fix that problem today. We'd need some way to
"reset" instrumentation and the registry in between tests (maybe not
_that_ hard, honestly). That's more than I want to do on a Saturday
afternoon. So to fix the current issue, we just don't bother testing
things that logically could never pass anyways. What we actually care
about is that the instrumentation reports it was not installed, which
does work correctly as it is.

Fixes #387

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[4599842d7c...](https://github.com/RikuTheKiller/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Monday 2023-03-20 13:28:24 by Jacquerel

Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[816f9f5bf2...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/816f9f5bf25d32c5cd8317b211651f11e22b3202)
#### Monday 2023-03-20 13:36:56 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[11aab72dc9...](https://github.com/pytorch/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Monday 2023-03-20 14:24:45 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [LebToki/Index-for-Laragon](https://github.com/LebToki/Index-for-Laragon)@[c6922fb442...](https://github.com/LebToki/Index-for-Laragon/commit/c6922fb44222eabbe93a97982413f8720030a0ac)
#### Monday 2023-03-20 14:37:47 by Tarek Tarabichi

Version 1.1

We've created a visually appealing user interface that will auto sense any projects and directories created within the root page of your XAMPP server. Our index file replaces the vanilla Laragon server index page, providing you with a more interactive and efficient way to manage your projects.

With our customized UI, you can easily navigate through your projects and directories, quickly find the files you need, and manage your server more effectively. We understand the importance of having an organized workspace, and our index page helps you achieve just that.

Our index page is designed to be user-friendly and intuitive, making it easy for beginners and experienced developers alike. We've incorporated a responsive design, so you can access it on any device, whether you're on your desktop computer or mobile phone.

We're confident that our Laragon root directory index page will enhance your development experience and streamline your workflow. Try it out today and let us know what you think!

---
## [KimNorgaard/dwm](https://github.com/KimNorgaard/dwm)@[67d76bdc68...](https://github.com/KimNorgaard/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2023-03-20 14:53:58 by Chris Down

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
## [KoviRobi/nushell](https://github.com/KoviRobi/nushell)@[2e01bf9cba...](https://github.com/KoviRobi/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Monday 2023-03-20 15:21:06 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [NilFoundation/zkllvm-rslang](https://github.com/NilFoundation/zkllvm-rslang)@[2afe58571e...](https://github.com/NilFoundation/zkllvm-rslang/commit/2afe58571e53d48a1fc2354271abe5aff60c5c44)
#### Monday 2023-03-20 16:05:16 by bors

Auto merge of #104658 - thomcc:rand-update-and-usable-no_std, r=Mark-Simulacrum

Update `rand` in the stdlib tests, and remove the `getrandom` feature from it.

The main goal is actually removing `getrandom`, so that eventually we can allow running the stdlib test suite on tier3 targets which don't have `getrandom` support. Currently those targets can only run the subset of stdlib tests that exist in uitests, and (generally speaking), we prefer not to test libstd functionality in uitests, which came up recently in https://github.com/rust-lang/rust/pull/104095 and https://github.com/rust-lang/rust/pull/104185. Additionally, the fact that we can't update `rand`/`getrandom` means we're stuck with the old set of tier3 targets, so can't test new ones.

~~Anyway, I haven't checked that this actually does allow use on tier3 targets (I think it does not, as some work is needed in stdlib submodules) but it moves us slightly closer to this, and seems to allow at least finally updating our `rand` dep, which definitely improves the status quo.~~ Checked and works now.

For the most part, our tests and benchmarks are fine using hard-coded seeds. A couple tests seem to fail with this (stuff manipulating the environment expecting no collisions, for example), or become pointless (all inputs to a function become equivalent). In these cases I've done a (gross) dance (ab)using `RandomState` and `Location::caller()` for some extra "entropy".

Trying to share that code seems *way* more painful than it's worth given that the duplication is a 7-line function, even if the lines are quite gross. (Keeping in mind that sharing it would require adding `rand` as a non-dev dep to std, and exposing a type from it publicly, all of which sounds truly awful, even if done behind a perma-unstable feature).

See also some previous attempts:
- https://github.com/rust-lang/rust/pull/86963 (in particular https://github.com/rust-lang/rust/pull/86963#issuecomment-885438936 which explains why this is non-trivial)
- https://github.com/rust-lang/rust/pull/89131
- https://github.com/rust-lang/rust/pull/96626#issuecomment-1114562857 (I tried in that PR at the same time, but settled for just removing the usage of `thread_rng()` from the benchmarks, since that was the main goal).
- https://github.com/rust-lang/rust/pull/104185
- Probably more. It's very tempting of a thing to "just update".

r? `@Mark-Simulacrum`

---
## [JaredWeakStrike/Archipelago](https://github.com/JaredWeakStrike/Archipelago)@[6d13dc4944...](https://github.com/JaredWeakStrike/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Monday 2023-03-20 16:17:13 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [VoltageOS-Devices/kernel_xiaomi_lavender](https://github.com/VoltageOS-Devices/kernel_xiaomi_lavender)@[e42bc56498...](https://github.com/VoltageOS-Devices/kernel_xiaomi_lavender/commit/e42bc564980f22faeb03d96d193110c65cd35a11)
#### Monday 2023-03-20 16:54:58 by Christian Brauner

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
## [Conga0/Apotheosis](https://github.com/Conga0/Apotheosis)@[c35ba772ee...](https://github.com/Conga0/Apotheosis/commit/c35ba772eecfaddcec9017c219c3a4d2fd64b723)
#### Monday 2023-03-20 17:26:07 by Conga Lyne

New Spell, Evil Temple Clean up, Various Fixes

New Spell: Sphere of Water
Slightly darkened Alcove glass to fit in with the background's darkness
Changed Flesh Boss's tentacle attack to be a Blood Orb attack instead, although I understand it's rude to change it back so suddenly, I feel the tentacles struggled to serve a purpose, you'd very rarely *want* to be close to the boss and if you were close enough to coincidentally be hit by them by the time the tentacle attack occurred, you likely had much, much bigger problems to be weary of.  --Note(1) that I am up to discuss this if you're against this change S, hopefully we can decide on something we both agree upon
--Note(2) Perhaps the 'magic poring' attack could be converted into a Blood-Hex/Homing blackhole attack which activates during phase 2, while he would maintain his Mass-Wounding throughout all phases? This would combo painfully well with the blood orb attack
Updated Tentacle Trap's sprite to better blend in with the new Flesh Material
Heretic's Glyph Particles now only begin appearing in phase 2, previous emissive sprite has been removed
Updated Sphere of Acid's Projectile srptie
Updated Sphere of Acid's Spell UI Icon --NOTE(3) These icons preferably aren't final, difficult to find a fitting icon to convey what they do, maybe some of Spicy's icons would provide good inspiration? Unsure
Fixed Banners clashing with terrain & alcoves in Temple of Sacrilegious Remains
Fixed Alcoves clashing with terrain & banners in Temple of Sacrilegious Remains
Fixed Psychotic projectiles VSC component pointing to real projectiles
Fixed Corrupt master proejctiles VSC component pointing to the wrong master orb

---
## [bsittler/meka](https://github.com/bsittler/meka)@[cc40359848...](https://github.com/bsittler/meka/commit/cc403598486441e9565d3fcd1fb225209a3cf308)
#### Monday 2023-03-20 17:27:55 by Benjamin C. Wiley Sittler

Add MAPPER_GG_Turbo_9_in_1_8000_4000 for "Turbo 9 in 1 [Street Fighter 2] (Unl)" GG multicart.

It is mostly working. One game (Choplifter) does not start, and there are glitches after restoring a save state that uses SMS-GG mode (glitchiness varies by game. some show wrong graphics, others reset, still others are fine.)

I qualified the name of Turbo 9 in 1 the first menu entry since there are apparently a bunch of very similarly-named cartridges with different menus/games, and the label description only makes sense when you are looking at the physical cartridge

It's an unlicensed Game Gear multicart with 9 games. The label says "TURBO 9 IN 1"

The box also says:
COLOR VIDEO GAME
SELECT GAMES ON SCREEN
GEAR GAME [where you might expect GAME GEAR; maybe it is a typo?]

The label and box also have a game listing in both English and traditional Chinese. Transcription/translation errors are my own:

```
1. STREET FIGHTER III / 街頭霸王Ⅲ (i.e. "street bully III"/"Street Fighter III")
2. CHAMPION SOCCER / 世界杯足球 (i.e. "world cup football")
3. CHOPLIFTER / 直昇機救人 (i.e. "helicopter rescue")
4. HANG ON II / 高速電單車Ⅱ (i.e. "high-speed motorcycle II")
5. SUPER BUBBLE BOBBLE / 泡泡龍 (i.e. "bubble dragon"/"Bubble Bobble")
6. SUPER MARIO 2 / 孖寶兄弟２ (i.e. "twin brothers 2")
7. COLUMNS / 寶石方塊 (i.e. "gem cube")
8. MY HERO / 熱血硬派 (i.e. "hot-blooded tough guy")
9. GALAGA 93 / 蜜蜂機９３ (i.e. "bee machine 93")
```

Some character choices suggest a possible Hong Kong origin, e.g. 電單車 for motorcycle and 街頭霸王 for Street Fighter.

The mapper is an extended version of Codemasters allowing initial "base page" offset selection. Only Jang Pung II uses the mapper after that point.

The menu has a single screen:

```
 G.G. SCREEN SELECT┆
 PUSH 2. START GAME┆
 PUSH ↑. ↓.  SELECT┆
                   ┆
 01.STREET FIGHTER 2 [0x8000=0x10, 0x4000=0x11]; it's 256K SMS Jang Pung II [SMS-GG] (KR)
 02.CHAMPION SOCCER┆ [0x8000=0x00, 0x4000=0x11]; it's 32K SG-1000 Champion Soccer modified to coexist with the menu code
 03.CHOPLIFTER     ┆ [0x8000=0x02, 0x4000=0x11]; it's 32K SG-1000 Choplifter (JP,AU)
→04.HANG ON 2      ┆ [0x8000=0x04, 0x4000=0x11]; it's 32K SMS Hang On (EU,AU,BR,DE,IT)
 05.SUPER BUBBLE BOBBLE [0x8000=0x06, 0x4000=0x11]; it's 32K SMS Super Bubble Bobble (KR)
 06.SUPER MARIO    ┆ [0x8000=0x0e, 0x4000=0x11]; it's 32K SMS Super Boy II (KR) (32K)
 07.COLUMNS        ┆ [0x8000=0x0a, 0x4000=0x11]; it's 32K GG Columns [v0] (JP)
 08.MY HERO        ┆ [0x8000=0x0c, 0x4000=0x11]; it's 32K SMS My Hero (US,EU,BR,PT,DE,IT)
 09.GALAGA         ┆ [0x8000=0x08, 0x4000=0x11]; it's 32K SG-1000 Sega-Galaga with the "Sega" removed
```

NOTE: the menu can operate to some extent in both native GG mode and in SMS-GG mode. In native GG mode some text is cut off. I've added a "┆" indicator to show the first column that is cut off.

It is unclear how the cartridge decides whether to switch from native GG mode (which is the power-on default) to SMS-GG mode, but it appears to happen at the moment 0x11 is written to 0x4000 *unless* 0x0a was the most recent value previously written to 0x4000.

No mechanism is known for programmatically returning the mapper to its power-on default state.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[aba978827c...](https://github.com/lessthnthree/Skyrat-tg/commit/aba978827cbef816f16f98078525cab1195de750)
#### Monday 2023-03-20 17:37:36 by SkyratBot

[MIRROR] Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone [MDB IGNORE] (#19834)

* Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!

![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.

![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

* Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [learnyouahaskell/learnyouahaskell.github.io](https://github.com/learnyouahaskell/learnyouahaskell.github.io)@[1ca8330d30...](https://github.com/learnyouahaskell/learnyouahaskell.github.io/commit/1ca8330d307e0da9964acfe3963aa3e19ce10522)
#### Monday 2023-03-20 17:58:28 by Sam Tygier

"guys" -> "people" (#51)

* really smart "guys" -> "folk"

* "guys" -> "folks"

* "the boys" -> "my buddies"

* Phonebook example 'girl' -> 'friend'

---
## [Ms-Mee/Shiptest](https://github.com/Ms-Mee/Shiptest)@[7f8874df29...](https://github.com/Ms-Mee/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Monday 2023-03-20 18:32:47 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[09d27e1a51...](https://github.com/tgstation/tgstation/commit/09d27e1a5149cffa1d5993687eabc7f8c240af85)
#### Monday 2023-03-20 18:34:57 by Jacquerel

Kidnapping won't destroy implants, nodrop items (#74118)

## About The Pull Request

Fixes #73985
Kidnapping was looping through mob contents to find items to remove from
you, rather than equipped items. It was then forcemoving them out of
you, destroying the functionality of implants and nodrop items.

Being kidnapped will now only remove equipped items from you (not
everything inside you) and will not forcemove nodrop items out of your
inventory (so it won't confiscate your chaplain armblade).
Additionally, anything you picked up in the kidnapping area was being
sent to nullspace on exit, I changed this to have them drop on the
ground instead.

However, due to this long-standing convention we now have an expectation
that items are not trivially moved in or our of the kidnapping area, so
it also loops through any storage implants you may have and dumps their
contents too.
There are still ways around this (cavity implantation, for instance) but
they seem uncommon and restrictive enough that they're probably not a
big deal.

## Why It's Good For The Game

Kidnapping another traitor destroying their implants was an annoying and
unpleasant experience (especially if it was their uplink implant), and
does not seem to have been intended.
Also removes weird behaviour where your arm blade might fall off because
you got kidnapped.

## Changelog

:cl:
fix: Implants and items which you cannot drop will no longer be forced
out of your character when you are kidnapped.
fix: Objects you try to take back from the kidnapping location as
souvenirs will drop to the ground when you leave instead of being
destroyed, except shirts and shoes (make sure to pick up your
monographed synidcate T-shirt).
/:cl:

---
## [chellmuth/OpenShadingLanguage](https://github.com/chellmuth/OpenShadingLanguage)@[e4e5088ed6...](https://github.com/chellmuth/OpenShadingLanguage/commit/e4e5088ed6dcd4eb636430dcce9fe815e435b1a6)
#### Monday 2023-03-20 18:41:35 by Larry Gritz

LLVM 15.0 support (#1592)

* A variety of changes to get a clean build and passing tests when
  using LLVM 15.0.

* I've noticed problems when using LLVM 15 but building with earlier
  clang, so the cmake scripts now print a warning in that case, so if
  users encounter trouble they have a hint about what to do to fix it.

* For our CI tests on Mac, force the MacOS-11 test to use llvm 14,
  and the MacOS-12 test to use llvm 15.

IMPORTANT TO-DO / CAVEATS:

1. When doing JIT at optlevel 12 or 13, I had to disable a number of
   passes that don't seem to exist anymore in LLVM 15. This is enough
   to get it working, and to be honest, I don't know if anybody uses
   these opt levels.  But we need to revisit this, because I don't
   know if there these are cases where the names of the passes merely
   changed or that new passes take their place (in which case we
   should add the new passes, not stop after merely disabling the
   deprecated ones). For that matter, optlevel modes 11, 12, 13 are
   supposed to match what clang does for -O1, -O2, -O3, and that
   changes from one release to the next, so we should probably revisit
   this list and make sure it's matching clang's current choices
   (which I assume are crafted and periodically revised by clang's
   authors).

2. LLVM 15 switches to "opaque pointers". It still supports typed
   pointers...  for now. But as you can see in the diffs, I had to
   disable a variety of deprecation warnings and take some other
   actions to put LLVM 15 in the old "opaque ptr" mode to match our
   use of LLVM <= 14. But this is only temporary, because the typed
   pointer mode is expected to be removed entirely in LLVM 16. So at
   some point in the next few months, we are going to need to support
   opaque pointers in our use of LLVM. (Also note: for a while, we're
   going to have a bunch of ugly `#if` guards or other logic to
   support both opaque pointers for users with llvm >= 16 and also
   typed pointers for users with llvm <= 14, until such time as our
   LLVM minimum is at least 15, which I expect is not a reasonable
   assumption for at least a couple years.)

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [kcpevey/napari](https://github.com/kcpevey/napari)@[3ec4be1ae8...](https://github.com/kcpevey/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Monday 2023-03-20 18:47:20 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[4e3c9ccc66...](https://github.com/cmss13-devs/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Monday 2023-03-20 19:26:05 by roll1d20st

Updates recipe.dm for Waffles, Cookies, Muffins (#2895)

Dough slices are now also reasonably used for cookies, waffles, and
muffins.

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Tied to this [post I made on the
forums](https://forum.cm-ss13.com/t/re-thinking-recipes-w-dough-slices/853)...
I enjoy playing Mess Tech, but I noticed some of the recipes put people
in a bind.

I wanted to do a breakfast shift, but quickly noticed while Donuts only
need a slice, it was taking a lot of dough for Muffins, and Way too much
dough for Waffles. So I figured I'd venture into the Dev Space.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

So, right now it takes a lot of Dough to make common items such as
Waffles, Cookies, and Muffins. 2 Dough for Waffle, 1 for Cookie and
Muffins. But literally, it only takes 1 Dough for Pizza.

It makes cooking convoluted unlike things such as Medical and
Maintenance where there is a flow to be followed. By making it take
Dough slices instead, it follows a practical step.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

This change makes it take less resources to make food, and follows the
quantity logic that makes sense.


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
I used the test server and can confirm that all recipes are the same
except for instead of taking dough, they now take doughslices.

Which, especially for Waffles, makes sense.

**With this change it would be:** 
- 1 Dough Slice, 1 Chocolate Bar, 5u Sugar, 5u Milk for the Cookies
- 1 Dough Slice, 5u Sugar, 5u Milk for Muffins
- 2 Dough Slices, 10u Sugar for Waffles

<details>
<summary>Screenshots & Videos</summary>

Umm... promise I tested it.  Pretty straightforward.

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
qol: Made it easier to make Muffins, Cookies, and Waffles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[bde254000f...](https://github.com/morrowwolf/cmss13/commit/bde254000fcd732e0365239e1b312dbfa21ee308)
#### Monday 2023-03-20 19:30:49 by carlarctg

Refactors how magazine ammo color is handled into overlays (#2779)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Refactors how magazine ammo color is handled into overlays.

Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.

This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

Renamed wallpiercing to wall-penetrating.

Removed cluster magazines from the code.

Altered the name of A19 magazines a little.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Refactors how magazine ammo color is handled into overlays.
> Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.
> This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

This will help a lot if adding new magazines as you don't have to sift
through the awful, bloated dmis. Additionally, it's been proven that
more icons in a dmi causes lag, so the less the merrier.

> Renamed wallpiercing to wall-penetrating.

More accurate

> Removed cluster magazines from the code.

These didn't fit with the new icon handling system, are not used
anywhere, and aren't interesting enough to be worth staying in the code.

> Altered the name of A19 magazines a little.

So i can do 'HV high impact'

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

refactor: Refactors how magazine ammo color is handled into overlays.
refactor: Instead of filling up dmis with a ridiculous amount of icon
states for each new barely used magazine type, compatible magazines have
a 'band' white overlay icon that is colored based on a variable on the
magazine.
imageadd: This will cause various sprites of various magazines to look
subtly different as the exact look couldn't be copied.
spellcheck: Renamed wallpiercing to wall-penetrating.
code: Removed cluster magazines from the code.
spellcheck: Altered the name of A19 magazines a little.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[4c373316ad...](https://github.com/Huffie56/cmss13/commit/4c373316ad1e9a68e5cd7ae0e216bddcd52ee3aa)
#### Monday 2023-03-20 19:38:42 by NewyearnewmeUwu

Alerts admins whenever humans try to gib another human. (#2560)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Successor to #2237 that properly addresses the issues brought up by
myself and others. This sends a admin alert similar to when a pred
activates their SD that allows admins to jump to the (strictly human)
player gibbing another human/human corpse and sleep them/amessage them.
This also creates logs when someone _attempts_ to stuff someone into a
gibber. I also fixed up some of the single letter variables in the
gibber code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Insanity RP is bad, and this solution allows admins to respond in
realtime. It takes 30 seconds to gib another human as a human, without
any skill modifiers helping. It also doesn't flag the player if they're
a pred, as they're _supposed_ to be doing funny human meat stuff.
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
code: gibbing another human takes an unmodifiable 30 seconds
admin: admins are alerted when a human tries to gib another human
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ThatZeoMan/HeavenStudio](https://github.com/ThatZeoMan/HeavenStudio)@[54c4899f9d...](https://github.com/ThatZeoMan/HeavenStudio/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Monday 2023-03-20 20:37:34 by AstrlJelly

Double Date Initialization (#198)

* starting out with double date stuff :D

not even the background is finished
i just wanna get this on my fork so that it's safe

* double date getting more initialized

no animations, one block, nothing actually functions. but the boy is put in place, and the girl is almost put in place! just wanted to merge this with the main branch to play catchy tune

* initialization done!!!!!

gonna fix up the code, see what i can take out, see what i can standardize, see what i need to add. loving this so far, even with all of its annoyances

* ughhhh animation stuff.

this is gonna take me a day or two to even comprehend

Co-authored-by: minenice55 <star.elementa@gmail.com>

---
## [gitster/git](https://github.com/gitster/git)@[eaa0fd6584...](https://github.com/gitster/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Monday 2023-03-20 21:11:43 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[468715b6bb...](https://github.com/git-for-windows/git/commit/468715b6bb5842694d624546a13b00d5d74b401a)
#### Monday 2023-03-20 21:14:35 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [openai/evals](https://github.com/openai/evals)@[ab5f7b2a89...](https://github.com/openai/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Monday 2023-03-20 23:34:46 by oscar-king

Counting bigrams in sentences (#302)

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
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

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

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [ValoTheValo/CEV-Eris](https://github.com/ValoTheValo/CEV-Eris)@[6f75cb9845...](https://github.com/ValoTheValo/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Monday 2023-03-20 23:39:20 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [jinzaizhichi/terminal](https://github.com/jinzaizhichi/terminal)@[5a34d92cb5...](https://github.com/jinzaizhichi/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Monday 2023-03-20 23:51:40 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---

