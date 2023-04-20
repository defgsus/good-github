## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-19](docs/good-messages/2023/2023-04-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,248,042 were push events containing 3,477,305 commit messages that amount to 256,612,327 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 53 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d71b805a1b...](https://github.com/TaleStation/TaleStation/commit/d71b805a1b142ac1d224ead6d16b3b051e4a3b1a)
#### Wednesday 2023-04-19 00:22:31 by TaleStationBot

[MIRROR] [MDB IGNORE] Mafia rebalance and backend refactor (#5413)

Original PR: https://github.com/tgstation/tgstation/pull/74640
-----
## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d21522626d...](https://github.com/TaleStation/TaleStation/commit/d21522626dbd4d08cb1a6ee5ffea93a7433bdb06)
#### Wednesday 2023-04-19 00:24:13 by TaleStationBot

[MIRROR] [MDB IGNORE] Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate (#5395)

Original PR: https://github.com/tgstation/tgstation/pull/74703
-----

## About The Pull Request

Nitrous Oxide, rather than directly subtracting blood volume per tick,
instead applies the anticoagulant trait ''TRAIT_BLOODY_MESS''. It shares
this with heparin.

However, unlike, heparin, coagulants like Sanguirite will remove the
trait and allow for continued clotting while the reagent is present,
neutering the nitrous oxide's anticoagulant effects (but not the other
parts)

Heparin, on the other hand, will purge Sanguirite while it is in you
system. You must remove the heparin before you can apply an
anticoagulant.

## Why It's Good For The Game

Nitrous Oxide, on top of being a knockout chem that causes you to
suffocate and become drowsy, just starts deleting blood rapidly. About
15 units of it, standard in a syringe, will kill you in about a minute,
but you'll be unconscious for most of it (you'll be at around 50%-60%
blood by the time it is out of your system, so as good as dead). It
doesn't matter that it metabolizes quickly either, since because it
isn't a toxin, it doesn't get purged by livers/improved livers, so you
will probably metabolize all of the chem that enters your system.

Blood is one of those 'hidden damage types', a bit like brain damage.
Once you start losing it _directly,_ you probably don't have a lot of
options to resolve it (unlike a bleed, which you do in various manners),
and the means of causing blood loss has been mostly pretty well
controlled as of late. Heparin directly interacts with wounds as a good
example.

Blood loss is also tied into oxyloss, which is another very mean damage
type in that it causes you to fall into unconsciousness at 50 damage, so
significantly more lethal than normal damage, kept in check by the fact
that breathing restores some of it. Nitrous oxide, you might note,
causes you to stop breathing.

It's cheaper to make than either heparin or lexorin, and since it isn't
a toxin like those chems, it is able to circumvent a few game mechanics
to simply just start killing you. It does the work of chloral hydrate,
lexorin and heparin while it has a remarkably easy recipe.

Following the example of how lexorin was pulled into line, and
consistency with heparin, I've made nitrous oxide an anticoagulant that
may or may not come into play as one. I think this is more up to date
with the state of toxins and chem warefare as a whole, and works with
the relative ease in making nitrous oxide. And it has been this way for
about 5 years, before we got wounds.

(did I mention that nitrous oxide is also an explosive if it gets hot
enough?)

## TL;DR

I think a chem with a pretty basic recipe shouldn't be doing the work of
5 other, more complicated, chemicals while also not being a toxin and
also not interacting with the wounds system or purity system whatsoever.
And being an explosive.

## Changelog
:cl:
balance: Nitrous oxide, the reagent, increases bleed rate from wounds
rather than directly subtracting blood. It can be counteracted using
coagulants (such as those in epipens).
balance: Heparin purges coagulants. You have to remove heparin from
someone's system before you can use coagulants.
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2b2cb3dff6...](https://github.com/tgstation/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Wednesday 2023-04-19 00:25:54 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [kidgenius703/tgstation](https://github.com/kidgenius703/tgstation)@[e47c47a081...](https://github.com/kidgenius703/tgstation/commit/e47c47a081f5919eea2b43453be7ac011ee2a492)
#### Wednesday 2023-04-19 00:30:48 by MrMelbert

You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[e4a1892e0a...](https://github.com/Nanu308/cmss13/commit/e4a1892e0a42115dfb3d90009d960386b76fe955)
#### Wednesday 2023-04-19 00:38:52 by NewyearnewmeUwu

No more proximity sensor spam. (#3076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
You can now slash proximity sensors to shut them up as xeno, and death
shuts off any proximity sensors in your belongings.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This is literally just the engi bellpack again. It's being used to OOCly
annoy people and needs a way to circumvent it.
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
fix: Proximity sensors can now be slashed by xenos to deactivate them,
and they turn off after you die if you have an active one on you.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [nmfightmaster/CIM](https://github.com/nmfightmaster/CIM)@[99bdb0c4a3...](https://github.com/nmfightmaster/CIM/commit/99bdb0c4a33adc7331835d6914d31a084cbe8eff)
#### Wednesday 2023-04-19 00:46:47 by Nathan Fightmaster

realizing im an idiot and scaffolding was the better route than creating it myself, but also glad i now have the experience and understanding of what is scaffolded--i replaced my versions with scaffolded versions to reduce headache

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[e766444468...](https://github.com/GForceTF/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Wednesday 2023-04-19 00:47:46 by LemonInTheDark

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
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[f97afbd66d...](https://github.com/lessthnthree/Skyrat-tg/commit/f97afbd66d6631bdb5355cbf54fe630e189e4d51)
#### Wednesday 2023-04-19 01:04:34 by SkyratBot

[MIRROR] Fixes spoon overlay not updating every time [MDB IGNORE] (#20570)

* Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

* Fixes spoon overlay not updating every time

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [lzy1102/proxychains-ng](https://github.com/lzy1102/proxychains-ng)@[7fe8139496...](https://github.com/lzy1102/proxychains-ng/commit/7fe813949644b115b0127279517dc7c0ee2d63b9)
#### Wednesday 2023-04-19 01:09:47 by rofl0r

experimental new feature: proxy_dns_daemon

since many users complain about issues with modern, ultracomplex
clusterfuck software such as chromium, nodejs, etc, i've reconsidered
one of my original ideas how to implement remote dns lookup support.
instead of having a background thread serving requests via a pipe,
the user manually starts a background daemon process before running
proxychains, and the two processes then communicate via UDP.
this requires much less hacks (like hooking of close() to prevent
pipes from getting closed) and doesn't need to call any async-signal
unsafe code like malloc(). this means it should be much more compatible
than the previous method, however it's not as practical and slightly
slower.

it's recommended that the proxychains4-daemon runs on localhost, and
if you use proxychains-ng a lot you might want to set ip up as a service
that starts on boot. a single proxychains4-daemon should theoretically
be able to serve many parallel proxychains4 instances, but this has not
yet been tested so far. it's also possible to run the daemon on other
computers, even over internet, but currently there is no error-checking/
timeout code at all; that means the UDP connection needs to be very
stable.

the library code used for the daemon sources are from my projects
libulz[0] and htab[1], and the server code is loosely based on
microsocks[2]. their licenses are all compatible with the GPL.
if not otherwise mentioned, they're released for this purpose under
the standard proxychains-ng license (see COPYING).

[0]: https://github.com/rofl0r/libulz
[1]: https://github.com/rofl0r/htab
[2]: https://github.com/rofl0r/microsocks

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[4874f16358...](https://github.com/Sonic121x/Skyrat-tg/commit/4874f163585c1e00d3e5ced697c605f1cfcb141d)
#### Wednesday 2023-04-19 01:11:04 by SkyratBot

[MIRROR] Fixes a runtime in simple_animal/hostile [MDB IGNORE] (#20588)

* Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.

https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294

## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Fixes a runtime in simple_animal/hostile

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[7b1b88f7af...](https://github.com/i3roly/glibc_ddwrt/commit/7b1b88f7afd6ae8ccc4f1471c676adc169889993)
#### Wednesday 2023-04-19 01:21:47 by gagan sidhu

v52357 - update coreutils/transmission/bunch of other shit

ol' assfuck decided to revamp rc so i had to check this build personally.

plus some stupid fuck making meth in my neighbourhood decided to crash
the local power, so my router gave out at ~4 months uptime. didn't even
get a screenshot. asshole

you will probably need to reset your ssh key after this, so i would use
the following commands:

stopservice sshd
nvram unset sshd_ed25519_host_key
rm /tmp/root/.ssh/ssh_host_ed25519_key
startservice sshd

i would also remove the entry in your client's ~/.ssh/known_hosts. it
will be the entry that correspnods to your router's ip.

not sure how much of a difference there is in the builds aside from the
software updates.

---
## [peff/git](https://github.com/peff/git)@[7de754ce37...](https://github.com/peff/git/commit/7de754ce375da12a2eee7978d7bdeaa6c1e8ea42)
#### Wednesday 2023-04-19 01:33:36 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[5d55f5faac...](https://github.com/KingDragoness/ProjectHypatios/commit/5d55f5faacd5b193a005bf7bfab5532c1b3f708a)
#### Wednesday 2023-04-19 04:38:58 by KingDragoness

Hypatios 1.5.0b5 (Curse & Blessing system, Polishing, balancing, Ongoing graphical touchup)
DONE (April 19)
• Trivia previews for all alternate chambers
• “Farlands” Trivia
o Trivias that are not in the map (except disabled) will be generated on the fly.
• Chamber 4 secret area
• Command arrow key up/down in console to quickly history navigate old commands.
o Already a year!
• “paradoxes” to list every paradox event completed.
o “otherEverUsed” in save file
• Chamber 3 new section rocket-jumping:
o In the intro, there’s a shortcut section which the player can go faster to level 4 by rocket-jumping.
o Tunnel horizontal long. Water current will speed up player’s movement to retry.
o Shortcut to level 4
• Chamber 4 volume zone
o Enemy outside from the volume will be killed instantly.
• Balancing: Aldrich panic attack occurs too often!
o Check every 20 seconds and chance to 10%.
o Occur only 60s after level started and at least 1 enemy hasSeenplayer.
• New book: “Basic of Psychology: Panic”
o Explains how panic attack occurs.
• Overhaul: Currently the end game, story after Defeating Theratios needs a lot of revisions:
o Entering the elevator would lead to the CCTV/Terminal room again.
o The Terminal level vents will be closed off and the player have to enter the WIRED to see the “Timekeeper Testaments”
o The timekeeper testaments server is still unfinished.
o Level with blue orbs and announcer announcing will be totally scrapped.
• Curse and Blessing system
o Persistent status effect for +9999s timer.
o Blessing: Sometimes randomly spawn a kThanid serum in some levels (not yet implement system in campaign yet).
o Curse: Curse can occur randomly during level transition (not yet implement system in campaign yet).
 It can also from injuries (fire will cause 2nd/3rd/4th degree burn)
 E.g curses: Depression (knockback +1, gun damage -30%)
• “CurseRandomizerEffect.cs” currently only cause depression, fatigue and panic attack.
• Dash cooldown can now be affected by statuses
• New item: Anti-Depressant
o Gives anti-depressant status and prevents depression.
o Can be found in medkits.
• Blessing effect:
o Anti-Depressant: Cures depression curse effect. Prevent Panic attack, fatigue and Depression ailments.
• Curse effect:
o Depression: Single-run (1 run only), after 20 runs and occur randomly 2% per level transition.
o Panic Attack: Temporary (60 seconds), Aldrich suffers panic attack randomly in the middle of the run after 20 runs
 Movement +15%, Knockback +0.5
o Fatigue: Temporary (999 seconds), Aldrich will lose motivation if stayed in the same chamber (except sewers) for more than 10 minutes.
 Movement -10%, Gun Damage -20%, Max HP -5%
• Fortima added other stuffs:
o Abandoned shack
• Change healcapsule in Vendrich level
• Regionactivator bug chamber 4 (in main chamber)
• Balancing/Quality Life: Mining Section
o Commodity index exchange checks every 1s [internal notes: Interact_OreTrader not only can trade ores but any inventory items]
o Exotic Metal sell cost 50->35
o Common Metal (x10) from 10->15
o Nuclear Material (x8) from (x5)
o Rare Metal from 20 -> 25
• Sewer music is bad!
o More calm song
• Capsule (ammo, heal and soul) now automatically goes to the player, 1 second upon it’s instantiated.
• Balancing: Mobius Corps (Chamber 4) is too big and needs more enemy at once! (9 enemies)
o Currently need to check bug unlimited spawn enemies
• Bug: Wallrun visual glitch (Chamber 1)

---
## [NewWinHilton/gpt4all-ui](https://github.com/NewWinHilton/gpt4all-ui)@[cbf446b3e2...](https://github.com/NewWinHilton/gpt4all-ui/commit/cbf446b3e28f4e53791f968c20b6888b4c40c9e8)
#### Wednesday 2023-04-19 04:54:50 by Richard Rosario

Update README.md (This really bugged me sorry lol)

got rid of the doubling of "GitHub Repository" as the hyperlink text does the job of rendering the text and providing the link. I'm sure it was a typo no biggie, honestly a super trivial edit I'm aware but it was driving me crazy!

*from this:*
If you are interested in learning more about this groundbreaking project, visit their Github repository [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

*To this:*

If you are interested in learning more about this groundbreaking project, visit their [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

---
## [sadprofeso/Game-3400---Team-4-Projects2](https://github.com/sadprofeso/Game-3400---Team-4-Projects2)@[1c57562f30...](https://github.com/sadprofeso/Game-3400---Team-4-Projects2/commit/1c57562f3012db1603e656cb16a361177a6a8f33)
#### Wednesday 2023-04-19 05:10:54 by sadprofeso

final lighting - holy fuck I hate everything please help me

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[c3b78761d2...](https://github.com/willardstation/tg-voidcrew/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Wednesday 2023-04-19 05:44:18 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[b5ebf5c942...](https://github.com/willardstation/tg-voidcrew/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Wednesday 2023-04-19 05:44:18 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [hsutter/cppfront](https://github.com/hsutter/cppfront)@[d8c1a50f22...](https://github.com/hsutter/cppfront/commit/d8c1a50f22c1b171a50e87ccdb609fb05f41c021)
#### Wednesday 2023-04-19 06:20:53 by Herb Sutter

First checkin of partial meta function support, with `interface` meta type function

This commit includes "just enough" to make this first meta function work, which can be used like this...

```
Human: @interface type = {
    speak: (this);
}
```

... where the implementation of `interface` is just about line-for-line from my paper P0707, and now (just barely!) compiles and runs in cppfront (and I did test the `.require` failure cases and it's quite lovely to see them merge with the compiler's own built-in diagnostics):

```
//-----------------------------------------------------------------------
//  interface: an abstract base class having only pure virtual functions
auto interface( meta::type_declaration&  t ) -> void {
    bool has_dtor = false;
    for (auto m : t.get_members()) {
        m.require( !m.is_object(),
                   "interfaces may not contain data objects");
        if (m.is_function()) {
            auto mf = m.as_function();
            mf.require( !mf.is_copy_or_move(),
                        "interfaces may not copy or move; consider a virtual clone() instead");
            mf.require( !mf.has_initializer(),
                        "interface functions must not have a function body; remove the '=' initializer");
            mf.require( mf.make_public(),
                        "interface functions must be public");
            mf.make_function_virtual();
            has_dtor |= mf.is_destructor();
        }
    }
    if (!has_dtor) {
        t.require( t.add_member( "operator=: (virtual move this) = { }"),
                   "could not add pure virtual destructor");
    }
}
```

That's the only example that works so far.

To make this example work, so far I've added:

- The beginnings of a reflection API.

- The beginnings of generation from source code: The above `t.add_member` call now takes the source code fragment string, lexes it,  parses it, and adds it to the `meta::type_declaration` object `t`.

- The first compile-time meta function that participates in interpreting the meaning of a type definition immediately after the type grammar is initially parsed (we'll never modify a type after it's defined, that would be ODR-bad).

I have NOT yet added the following, and won't get to them in the short term (thanks in advance for understanding):

- There is not yet a general reflection operator/expression.

- There is not yet a general Cpp2 interpreter that runs inside the cppfront compiler and lets users write meta functions like `interface` as external code outside the compiler. For now I've added `interface`, and I plan to add a few more from P0707, as meta functions provided within the compiler. But with this commit, `interface` is legitimately doing everything except being run through an interpreter -- it's using the `meta::` API and exercising it so I can learn how that API should expand and become richer, it's spinning up a new lexer and parser to handle code generation to add a member, it's stitching the generated result into the parse tree as if it had been written by the user explicitly... it's doing everything I envisioned for it in P0707 except for being run through an interpreter.

This commit is just one step. That said, it is a pretty big step, and I'm quite pleased to finally have reached this point.

---

This example is now part of the updated `pure2-types-inheritance.cpp2` test case:

    // Before this commit it was this
    Human: type = {
        speak: (virtual this);
    }

    //  Now it's this... and this fixed a subtle bug (can you spot it?)
    Human: @interface type = {
        speak: (this);
    }

That's a small change, but it actually also silently fixed a bug that I had written in the original code but hadn't noticed: Before this commit, the `Human` interface did not have a virtual destructor (oops). But now it does, because part of `interface`'s implementation is to generate a virtual destructor if the user didn't write one, and so by letting the user (today, that was me) express their intent, we get to do more on their behalf. I didn't even notice the omission until I saw the diff for the test case's generated `.cpp` had added a `virtual ~Human()`... sweet.

Granted, if `Human` were a class I was writing for real use, I would have later discovered that I forgot to write a virtual destructor when I did more testing or tried to do a polymorphic destruction, or maybe a lint/checker tool might have told me. But by declaratively expressing my intent, I got to not only catch the problem earlier, but even prevent it.

I think it's a promising data point that my own first attempt to use a metaclass in such a simple way already fixed a latent simple bug in my own code that I hadn't noticed. Cool beans.

---

Re syntax: I considered several options to request a meta function `m` be applied to the type being defined, including variations of `is(m)` and `as(m)` and `type(m)` and `$m`. I'm going with `@m` for now, and not because of Python envy... there are two main reasons:

- I think "generation of new code is happening here" is such a fundamental and important new concept that it should be very visible, and actually warrants taking a precious new symbol. The idea of "generation" is likely to be more widely used, so being able to have a symbol reserved for that meaning everywhere is useful. The list of unused symbols is quite short (Cpp2 already took `$` for capture), and the `@` swirl maybe even visually connotes generation (like the swirl in a stirred pot -- we're stirring/cooking something up here -- or maybe it's just me).

- I want the syntax to not close the door on applying meta functions to declarations other than types. So putting the decoration up front right after `:` is important, because putting it at the end of the type would likely much harder to read for variables and especially functions.

---
## [AdepojuJeremy/NSFW-Classifier](https://github.com/AdepojuJeremy/NSFW-Classifier)@[2fa73a55da...](https://github.com/AdepojuJeremy/NSFW-Classifier/commit/2fa73a55dafa6425062d9b7e33dfcc5bfb443b91)
#### Wednesday 2023-04-19 06:21:24 by airs

Update README.md



# NSFW-Classifier
An AWS Sagemaker Model developed for Nudity / NSFW Images Classification <br>


This is project done for the fullfillment of Udacity Machine Learning Engineer NanoDegree. I have build a model that classifies 
input image into five categories.
1. **Nude** 
2. **Semi Nude**
3. **Animated**
4. **Porn**
5. **Safe For Work**

# Demo 
The model is deployed on aws check it yourself by downloading this repository , then going to demo folder and running index.html.


# Contents
1. [classification_tool.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/classification_tool.ipynb)
2. [clean and prepare data.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/clean%20and%20prepare%20data.ipynb)
3. [nsfw-training_built_in_aws.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/nsfw-training_built_in_aws.ipynb)
4. [nsfw_deploy.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/nsfw_deploy.ipynb)
5. [batch_transform.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/batch_transform.ipynb)
6. [benchmark.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/benchmark.ipynb)
7. [analyze_bench.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/analyze_bench.ipynb)
8. [Metrics.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/Metrics.ipynb)
9. [analyze_results.ipynb ](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/analyze_results.ipynb)
10. [Capstone_Project_Report.pdf](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/Capstone_Project_Report.pdf)
11. [Project_Proposal.pdf](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/Project_Proposal.pdf)
12. [results.csv](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/results.csv)
13. [results_bench.csv](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/results_bench.csv)

        
         
             
  




#  Data Collection And Organization
The following guys had collected the data 
1. [Olamide's Data](https://archive.org/details/NudeNet_classifier_dataset_v1) . He did an awesome job in collection 
of data . The data is for three classes <br>
   * Nude 
   * Sexy 
   *  Safe 
   1. But the problem is I need more categories for my problem . So I made a simple [tool](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/classification_tool.ipynb) that is helpful for sub classifying the above Nude Images. You just keep all the training samples in one folder and run and run it in a jupyter notebook.
I classified a few thousands of these , but then i realized that it would take a while to gather huge data. For class **Safe For Work** i sampled randomly from his huge dataset.
   2. Further More I also made a [tool](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/useful_scripts/useful_scripts/example.py) that takes a screenshot of the screen and saves it into a folder. It becomes handy when you want to deliberately put  difficult examples in your dataset.   

The above tools proved helpful but did not solved the problem of gathering large number of examples for training. Therefore scraping was necessary.

2. [Bazarov 's Dataset](https://github.com/EBazarov/nsfw_data_source_urls) . For collecting  set of nude images I included the the sub category in the list he provided namely: <br>
   * Female genitalia
   * Male genitalia 
   * Breasts <br>
By now I had enough examples of class **nude.** <br>


3.[ Alex's Dataset](https://github.com/alex000kim/nsfw_data_scraper/tree/master/raw_data) . For classes **animated** and **porn** i scraped the data from here.
  

4.  [Instagram Scrapper](https://github.com/rarcega/instagram-scraper) For class **Semi Nude** I used his tool to scrape few Instagram pages that regularly post arousing images of men and women.

---
## [Donought/teknikfag-eksamens-projekt](https://github.com/Donought/teknikfag-eksamens-projekt)@[e9965c85b7...](https://github.com/Donought/teknikfag-eksamens-projekt/commit/e9965c85b7ce4bda7962324b43e3034eb04f7d25)
#### Wednesday 2023-04-19 07:25:51 by Donought

Finally managed to merge

...after a lot of back and fourth between stupid commits that refused to merge. My god, that was annoying.

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[5a34d92cb5...](https://github.com/PKRoma/Terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Wednesday 2023-04-19 07:42:11 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [tmtmtl30/Shiptest](https://github.com/tmtmtl30/Shiptest)@[b5dc4835a6...](https://github.com/tmtmtl30/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Wednesday 2023-04-19 07:48:11 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [tmtmtl30/Shiptest](https://github.com/tmtmtl30/Shiptest)@[7df4885117...](https://github.com/tmtmtl30/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Wednesday 2023-04-19 07:48:11 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [manadart/juju](https://github.com/manadart/juju)@[7976a61522...](https://github.com/manadart/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Wednesday 2023-04-19 07:59:20 by Juju bot

Merge pull request #15492 from barrettj12/openstack-meta

https://github.com/juju/juju/pull/15492

The interactive add-cloud is painful because it will often reject the endpoint URL without giving any reason why. See https://bugs.launchpad.net/juju/+bug/1908630
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119

Enter the API endpoint url for the cloud []: http://172.31.47.119/
Can't validate endpoint: No Openstack server running at http://172.31.47.119/

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity/v3
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity/v3

Enter the API endpoint url for the cloud []: 172.31.47.119/identity
Can't validate endpoint: No Openstack server running at 172.31.47.119/identity

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity
```

In the Openstack provider's `Ping` method, at least pass on the error information to the user, to make it a little less painful.
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request /
caused by: Get "/": unsupported protocol scheme ""

Enter the API endpoint url for the cloud []: http://172.31.47.119
Can't validate endpoint: No Openstack server running at http://172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request http://172.31.47.119/
caused by: Get "http://172.31.47.119/": dial tcp 172.31.47.119:80: connect: no route to host
```

Do the same with the MAAS and LXD providers.

Also, fix a silly check in the LXD provider's `Ping` method that was rejecting perfectly good URLs. We're already using `lxd.EnsureHostPort(endpoint)` to fill in the scheme/port if not provided, but we were checking the returned value equals the input (and returning an unhelpful error if not). Remove this check.

## Checklist

*If an item is not applicable, use `~strikethrough~`.*

- [x] Code style: imports ordered, good names, simple structure, etc
- ~[ ] Comments saying why design decisions were made~
- [x] Go unit tests, with comments saying what you're testing
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

Run `juju add-cloud` interactively, and provide a bogus URL.

---
## [DAKKA-WAAAGH/tgstation](https://github.com/DAKKA-WAAAGH/tgstation)@[6085e3b5ee...](https://github.com/DAKKA-WAAAGH/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Wednesday 2023-04-19 10:21:14 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [smithakishan/seffora](https://github.com/smithakishan/seffora)@[031610bee3...](https://github.com/smithakishan/seffora/commit/031610bee342d5566ac39b1731eae72dffe69ec6)
#### Wednesday 2023-04-19 10:27:53 by smithakishan

Add files via upload

Project on Health Care
Prediction of Cardiovascular Disease using Machine Learning
Cardiovascular disease is a leading cause of death globally. An effective model is required to
predict the heart disease using various parameters that are available for reference that may
have an impact on the heart health.
After doing the preliminary analysis of the dataset, like checking the shape, datatypes and
unique values, it can be concluded that the data is clean without any duplicate and missing
values.
Visualizing the data:
By using visualization tools like Histogram, we can find the Numerical data columns and
Categorical data columns and also the relationship of each feature with the target column.
We can see that 'sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal' and 'target' columns are
categorical columns.
Visualization of Categorical Columns using Count plot:
To check the relationship between the categorical features and the Cardiovascular disease,
we can use Countplot from the seaborn library.
We can conclude from the Count Plots as follows:
● Of the total number of patients, the number of Male patients is higher, but lesser
Male patients with Cardiovascular disease. The count of Female patients is lesser as
compared to Male patients, but more women have Cardiovascular disease.
● The Chest pain type 2 is connected to the Heart disease and most patients with
Chest pain type 0 do not have a Heart disease.
● Patients with fasting blood sugar level < 120, have a Heart disease.
● Most patients with Resting Electrocardiograph of type 1 have a heart disease
followed by type 0.
● Exercise induced Angina = No, have a heart disease.
● Slope of the peak exercise ST segment of type 2 have maximum Heart Disease.
● Number of major vessels (0-3) colored by fluoroscopy of Type 0 has maximum
number of Heart Attacks.
● When we compare CVD with age, we find that CardioVascular disease is highest at
54 years of age, followed by 41, 51 and 52 years.
● Resting Blood Pressure (trestbps): Maximum heart attacks have occured at Resting
Blood Pressure = 120 and 130.
● At cholesterol levels between 195 and 240, there is a good chance of having a heart
attack.
● Peak exercising '2' has a significant impact on Heart Attack.
● Thalassemia of type '2' has a significant impact on the occurance of a Heart Attack.
We check the correlation between all the features using a Heatmap. Very dark and very light
areas mean that there is a correlation between the corresponding variables.
Model Building:
We use One hot encoding to convert categorical data into binary vectors. After splitting the
data into training and testing in the ratio of 80:20, we fit the training data to Logistic
Regression and Random Forest Classifier models, we predict the outcome and check the
accuracy of the models.
Result:
Accuracy of the Random Forest Classifier is slightly better at 78.6885% as compared to that
of Logistic Regression at 77.0492%.
Statistical Analysis:
By using the Logit Regression model from the statts.api, we can do find p-value, standard
error, etc. for all the features and use the result for feature selection. Usually,
features with p-value < 0.05 is considered and also standard error < 1.
We again train the Models using the features selected after statistical analysis.
Result:
The accuracy of the Logistic Regression Model has improved from 77.0492% to 81.9672%.
Whereas, the accuracy of Random Forest Classifier Model has reduced from 78.6885% to
75.4098%.
Feature Importance using Random Forest Classifier:
By using Random Forest Classifier, we check for the important features in the descending
order and select the first five features for training the models.
Result:
The accuracy of Logistic Regression has slightly improved to 83.6066% and the accuracy of
Random Forest Classifier to 81.9672%.

---
## [NUROISEA/anime-webui-colab](https://github.com/NUROISEA/anime-webui-colab)@[b3b9695fd6...](https://github.com/NUROISEA/anime-webui-colab/commit/b3b9695fd6743e95537791ad8864b2c4a23fb957)
#### Wednesday 2023-04-19 13:28:39 by NUROISEA

🤦‍♂️ Fix for controlnet model not working

I forgot the `utility` prefix. NURO why are you stupid i fucking swear

do not code while having a shapr headache, thanks

---
## [magickingdumb/magickingdumb](https://github.com/magickingdumb/magickingdumb)@[64f16ca50f...](https://github.com/magickingdumb/magickingdumb/commit/64f16ca50feed7760688df9c685443d70f764b73)
#### Wednesday 2023-04-19 13:32:44 by magickingdumb

My A.I. assistant LOOPER

Use Looper for any of your projects with openai API or any API that uses AI, this is mutable and has a lot of power when you add some "legal" code to it, haha, have fun, use a funny voice, show off to your friends, all of it is possible with AI!!!

---
## [aleatoricmbnt/093402dc785c01274713767fb5962628_c932c4862d3a44d11e6c1f1e991186659168ccf5_0956d2fbd5d5c29844a4d21ed2](https://github.com/aleatoricmbnt/093402dc785c01274713767fb5962628_c932c4862d3a44d11e6c1f1e991186659168ccf5_0956d2fbd5d5c29844a4d21ed2)@[81755e1936...](https://github.com/aleatoricmbnt/093402dc785c01274713767fb5962628_c932c4862d3a44d11e6c1f1e991186659168ccf5_0956d2fbd5d5c29844a4d21ed2/commit/81755e193631a2cf9906148fb7f57f58fab1f16e)
#### Wednesday 2023-04-19 14:09:37 by Mariia Shytse

Commit message: 🤖🦾🦿

<script>alert(123);</script>
Extended description, probably max length. To be checked: 
- multilines in the description; 
- ⚠️emojis; 
- message crop; 
- tooltip;
- header on the run dashboard;
- xss injections maybe? 
- some other checks.

The Adepta Sororitas, colloquially called the "Sisterhood," whose military arm is also known as the Sisters of Battle and formerly as the Daughters of the Emperor, are an all-female division of the Imperium of Man's state church known as the Ecclesiarchy or, more formally, as the Adeptus Ministorum.

The Sisterhood's Orders Militant serve as the Ecclesiarchy's armed forces, mercilessly rooting out spiritual corruption and heresy within Humanity and every organisation of the Adeptus Terra.

There is naturally some overlap between the duties of the Sisterhood and the Imperial Inquisition; for this reason, although the Inquisition and the Sisterhood remain entirely separate organisations, the Orders Militant of the Adepta Sororitas also act as the Chamber Militant of the Inquisition's Ordo Hereticus.

The Adepta Sororitas and the Sisters of Battle are commonly regarded as the same organisation, but the latter title technically refers only to the Orders Militant of the Adepta Sororitas, the best-known part of the organisation to the Imperial public.

The Sisterhood serves as the Ministorum's only official military force because the Decree Passive laid down by the reformist Ecclesiarch Sebastian Thor held that in the wake of the Age of Apostasy's Reign of Blood in the 36th Millennium, the Ecclesiarchy cannot maintain any "men under arms."

This command was supposed to limit the power of the Ecclesiarchy by preventing it from maintaining the massive armies of the faithful Frateris Templar it once used to abuse its power from the 32nd to the 36th Millennia.

However, the Adeptus Ministorum has been able to circumvent this decree with the subtle acquiescence of the Inquisition by deploying the all-female military force of the Sisterhood's Orders Militant.

---
## [Recidiviz/pulse-data](https://github.com/Recidiviz/pulse-data)@[d81a2ffc94...](https://github.com/Recidiviz/pulse-data/commit/d81a2ffc945b6b6d56a5c8554dfd871515ea8634)
#### Wednesday 2023-04-19 14:29:26 by Damini Sharma

TES Queries for TN Discharge Opportunity (Recidiviz/recidiviz-data#16781)

## Description of the change

This PR writes the criteria queries for the TN Upcoming Discharge
Workflows opportunity. The changes are broadly:
1. Some updates to `sentences_preprocessed` and
`us_tn_sentences_preprocessed` to access relevant fields like whether
someone is on `lifetime_supervision`
2. Turning `supervision_past_full_term_completion_date` into a critical
query fragment so it can be called with different # of days in different
criteria queries (e.g. 0 or 30 days)
3. Creating additional criteria queries for this opportunity
specifically:
- `not_on_life_sentence_or_lifetime_supervision.py`
- `no_zero_tolerance_codes_spans.py`
- `supervision_past_full_term_completion_date_or_upcoming_30_day.py` and
creating a TN-specific
`us_tn_supervision_projected_completion_date_spans.py` to support this.

A few notes on validating the sandbox output in
`recidiviz-123.dsharm_16285_task_eligibility_spans_us_tn.complete_full_term_discharge_from_supervision_materialized`
against the snapshot query in `us_tn_compliant_reporting_logic` where we
originally calculated who was upcoming/overdue for discharge.

<img width="1044" alt="Screen Shot 2022-12-02 at 3 47 32 PM"
src="https://user-images.githubusercontent.com/15899459/205410155-03687561-7782-4778-8bb9-48d4b5b61bff.png">

- The small number of people `tes_eligible_missing_in_snapshot` are
people whose supervision level is `UNSUPERVISED` so they don't show up
in the snapshot query (based on the Standards sheet) but should still be
considered eligible
- Of the 185 people who are `tes_elig_inelig_in_snapshot`, ~62 are cases
where the TES expiration date is sooner than the snapshot expiration
date. See Recidiviz/recidiviz-data#17033 which fixes most of these 62 cases. For the remainder
123 cases, the discrepancy is caused by the fact that in the snapshot
query, we consider someone ineligible if they have zero tolerance codes
_after their most recent sentence effective date_; in TES we're
considering someone ineligible if they have zero tolerance codes _after
their most recent sentence imposed date_. I don't have a strong opinion
on which of these dates is more correct to use, but given that zero
tolerance codes are a proxy for missing sentencing data, it feels
reasonable to use `date_imposed`
- The final 2 categories (snapshot elig and missing/ineligible in TES)
are largely composed of 2 categories. A few of these are people who have
been crudely excluded temporarily because they have data in ISC and
Diversion sentences tables; once Recidiviz/recidiviz-data#16709 is done, the crude hacks to
remove these folks can be removed and improve this discrepancy. The rest
are largely because the snapshot query is flagging several people whose
latest supervision session started _after_ their latest sentence
expiration date. In all likelihood, this means the people aren't
actually overdue/upcoming discharge, but are missing sentencing info.
Because of how TES queries are structured, we don't include these
people.

## Type of change

> All pull requests must have at least one of the following labels
applied (otherwise the PR will fail):

| Label | Description |
|-----------------------------
|-----------------------------------------------------------------------------------------------------------
|
| Type: Bug | non-breaking change that fixes an issue |
| Type: Feature | non-breaking change that adds functionality |
| Type: Breaking Change | fix or feature that would cause existing
functionality to not work as expected |
| Type: Non-breaking refactor | change addresses some tech debt item or
prepares for a later change, but does not change functionality |
| Type: Configuration Change | adjusts configuration to achieve some end
related to functionality, development, performance, or security |
| Type: Dependency Upgrade | upgrades a project dependency - these
changes are not included in release notes |

## Related issues

Closes Recidiviz/recidiviz-data#16285

## Checklists

### Development

**This box MUST be checked by the submitter prior to merging**:
- [x] **Double- and triple-checked that there is no Personally
Identifiable Information (PII) being mistakenly added in this pull
request**

These boxes should be checked by the submitter prior to merging:
- [x] Tests have been written to cover the code changed/added as part of
this pull request

### Code review

These boxes should be checked by reviewers prior to merging:

- [x] This pull request has a descriptive title and information useful
to a reviewer
- [x] This pull request has been moved out of a Draft state, has no
"Work In Progress" label, and has assigned reviewers
- [x] Potential security implications or infrastructural changes have
been considered, if relevant

GitOrigin-RevId: a844601c8ab7fe0e4288239aa3ddfb8a55a158b5

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[21464fe41c...](https://github.com/microsoft/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Wednesday 2023-04-19 14:34:36 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[2c92211dac...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/2c92211dac3d2929db283bb0e58d2933f1607b0d)
#### Wednesday 2023-04-19 14:45:19 by SkyratBot

[MIRROR] Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool [MDB IGNORE] (#20602)

* Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool (#74744)

## About The Pull Request

Replaced the subspace amplifier in the Black Market Uplink's crafting
recipe with a signaller and a microlaser.

Added the Black Market Uplink to the maintenance loot pool.
## Why It's Good For The Game

The BMU is an _extremely_ rare device to find in rounds. It can quite
literally ONLY be found via the crafting recipe, and with how stupidly
bloated the crafting lists are, it isn't something many people know
about. All this means that a very unique and engaging gimmick item is
tragically extremely obscured.

To add to this, the recipe requires a _subspace amplifier_. These items
are UNBELIEVABLY rare - they need you to vend them from a techfab with
bluespace communication technology researched, which is fair to say is
not a common thing. Sometimes maps have them in tech storage, but even
then you have to break and enter which can be quite risky at times and
an annoying blockade the other times.

The black market items are not worth this much hassle. They are all
small cute gimmicky objects that do not heavily impact the round. By
making it not only easier to craft with common items, but also appear in
the maintenance loot pool, this will make assistants find out about it
more often, which can further incentivize them to utilize the **cargo
bounty system** to get enough money to buy their funny gadgets.

Another idea would be to make the uplink appear as a bounty item, which
would be a great way to tell players it exists and encourage them to mix
both systems together. The system for getting items is also
unnecessarily, miserably awful - your item either gets literally thrown
into space from a random direction, or it is teleported silently without
warning in 60 seconds onto a completely random place which can very much
include Security, Command, the Vault, or other high-security areas.
Needing to B&E into these areas to get your durathread vest is, uh. Not
worth it. However these aren't part of this PR, unless they're given the
A-OK. (also maybe make it cargo purchasable?)
## Changelog
:cl:
balance: Makes Black Market Uplinks more easily craftable, adds them to
uncommon maint loot pool
/:cl:

* Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [Kiciuk/linux](https://github.com/Kiciuk/linux)@[7175cd1693...](https://github.com/Kiciuk/linux/commit/7175cd16932c335177407e5732685bed4293a2f1)
#### Wednesday 2023-04-19 15:38:36 by Adam Skladowski

v2.4/5 its so fucking annoying to have conflicts on every shit i want to apply for fuck sake

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6d270e8578...](https://github.com/mrakgr/The-Spiral-Language/commit/6d270e8578a291106c5677adb3999a204bd594ba)
#### Wednesday 2023-04-19 16:23:22 by Marko Grdinić

"https://edoras.sdsu.edu/~vinge/misc/singularity.html

Somebody posted this on HN.

///

            o Develop human/computer symbiosis in art: Combine the graphic
              generation capability of modern machines and the esthetic
              sensibility of humans. Of course, there has been an enormous
              amount of research in designing computer aids for artists, as
              labor saving tools.  I'm suggesting that we explicitly aim for a
              greater merging of competence, that we explicitly recognize the
              cooperative approach that is possible. Karl Sims [22] has done
              wonderful work in this direction.

///

Amazing that this is happening.

4/19/2023

7:40am. I woke up even earlier than this and lounged in bed, thinking bad thoughts. It is better than I got up just now even though I am yawning here. Yesterday I actually went to bed at 11pm instead of 1am like usually as I was dead tired and couldn't read anymore.

Let me read Baki Dou. I guess I'll chill for a while before starting.

...I see somebody is trying to log into my Azure AD account. Not gonna work.

8:20am. I am anxious today. Maybe failing to finish the vid yesterday impacted my mental state.

Let me just read another chapter or two and then I'll get started for the day.

I see I am going to have to restart the video, or at least, cut out large parts of it.

Well whatever.

It is fine, if I just leave in the static file serving parts and then the proxy I am going to get right today hopefully.

8:25am. Things like this just happen.

I am missing my own deadlines, and so is Re;Library. But the most important thing is to keep working at it in order to get through it.

9:20am. Let me start for the day.

If I can make it work, I'll reward myself by closing it early.

Sigh, I probably should slept longer, but nightmares woke me up early.

> Ok that one at least I can answer, if the Vite Server is well behaved and is passing the X- headers proxies to then wiring up the forwarded headers middleware will take of that.

https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-7.0

> Forwarded Headers Middleware is enabled by default by IIS Integration Middleware when the app is hosted out-of-process behind IIS and the ASP.NET Core Module (ANCM) for IIS.

So is this why IIS works?

```fs
    app
        .UseForwardedHeaders()
```

Let me try it.

9:30am. I'll have to open it in the debugger. I need to see if there are those X-Forwarded fields in the header.

9:35am. Nope, those forwarding headers aren't present in the request.

https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-7.0#azure

For Azure I might have to turn on cert forwarding.

9:45am. Hmmm, there is in fact a x-remoting-proxy field in the header.

https://ruslan.rocks/posts/vite-proxy-how-to-setup

> xfwd: true/false, adds x-forward headers

Oh there is this option.

> autoRewrite: rewrites the location host/port on (201/301/302/307/308) redirects based on requested host/port. Default: false.

There is also this.

> followRedirects: true/false, Default: false - specify whether you want to follow redirects

Ohhhhh...

```
"/api": {target, changeOrigin: true, followRedirects: true},
```

Let me try this.

...I no longer get the cors error, but the redirect is not happening. Let me redirect to google.

10:10am. Does it run in Bundle mode? Why is the redirect completely missing.

...Yeah, in the production case, it goes straight to google.

https://stackoverflow.com/questions/64677212/how-to-configure-proxy-in-vite

> For debugging I highly recommend to add event listeners to the proxy, so you can see how the requests are transformed, if they hit the target server, and what is returned.

```
proxy: {
        '/api': {
          target: 'https://localhost:44305',
          changeOrigin: true,
          secure: false,
          ws: true,
          configure: (proxy, _options) => {
            proxy.on('error', (err, _req, _res) => {
              console.log('proxy error', err);
            });
            proxy.on('proxyReq', (proxyReq, req, _res) => {
              console.log('Sending Request to the Target:', req.method, req.url);
            });
            proxy.on('proxyRes', (proxyRes, req, _res) => {
              console.log('Received Response from the Target:', proxyRes.statusCode, req.url);
            });
          },
        }
      }
```

```
console.log('Received Response from the Target:', proxyRes.statusCode, req.url, proxyRes.headers.toString());
```

Mhhh, for fuck's sake. How do I print out the stuff here. It just gives me [object Object].

JSON.stringify().

11:05am. A nightmare. This is a nightmare.

```js
                "/api": {target, changeOrigin: true,
                    secure: false,
                    followRedirects: false,
                    xfwd: true,
                    autoRewrite: true, hostRewrite: true, protocolRewrite: true,
                    configure: (proxy, _options) => {
                        proxy.on('error', (err, _req, _res) => {
                            console.log('proxy error', err);
                        });
                        proxy.on('proxyReq', (proxyReq, req, _res) => {
                            console.log('Sending Request to the Target:', req.method, req.url);
                        });
                        proxy.on('proxyRes', (proxyRes, req, _res) => {
                            console.log('Received Response from the Target:', proxyRes.statusCode, req.url, JSON.stringify(proxyRes.headers));
                        });
                    },
                },
```

Proxy forwarding and `app.UseForwardedHeaders()` isn't doing jack. I figured out how to include the forward headers, but they are pointless.

I am going to switch gears. Forget hot module reloading. We'll configure the project so it works...

Let me have breakfast here and I will finish the video.

11:15am. If I double click the request in the network tab it actually auth successfully and gives me back a cookie.

11:25am. Let me have breakfast here. I'll finish the video.

I am going to ditch the Vite server and just have the client output into the Server's public folder.

12:30pm. Done with breakfast. Let me take a break. Everything is messed up.

1:10pm. https://github.com/AzureAD/microsoft-authentication-library-for-js

> Would moving all of the authentication to the client work? If I authenticated the user using the [AAD library](https://github.com/AzureAD/microsoft-authentication-library-for-js), would the cookie be valid with the server which is using `Microsoft.Identity.Web`?

https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-react

I suppose it is worth a try.

1:55pm. Let's end the video here. I need a break from this.

For the next video I meant to do the database, but I'll do client side logins instead.

2:20pm. It is rendering.

A single key on a page. Highest detail, best quality, 4k, masterpiece.
Dull, muted, ugly, blurry.

Let me make some more images of these.

2:35pm. https://youtu.be/lNYZi9v9QoA
Authentication With ASP.NET Core And The SAFE Stack. SPA Login From The Server. (Pt. 5)

Here it is. Not my best work, but it will do.

2:50pm. Posted it on the F# sub, and posted it on Twitter.

Damn it, I do not feel like it. Let me chill a bit before I get started on the next part.

3:20pm. Let me get started.

Let me watch the video by Anton when SPAs are on different domains.

https://youtu.be/PUXpfr1LzPE?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi
ASP.NET Core External Authentication (OAuth, .NET 7 Minimal Apis C#)

3:25pm. Forget it, it is just going to waste my time.

Let me go forward bravely.

4:35pm. I closed all those issues. I do not want to bother with them anymore.

5:05pm. I have 2:50m of the video done.

I really want to close here. I got up earlier than usual today.

I'll at least close the recording. Right now, I need to read the docs, and I've been bashing my head against them for the past few days so I am sick of it.

Who is going to take that kind of trip at 5pm?

5:10pm.

https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-react#msal-basics

https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/initialization.md#optional-configure-authority

So this is where I need to put in the tenant id.

> Once you have retrieved the access token, you must include it in the Authorization header as a bearer token for the request to the resource you obtained the token for, as shown below:

So is that how it works?

It uses JWT tokens instead of cookies? I guess that answers the question of how it should be decrypted.

https://learn.microsoft.com/en-us/answers/questions/671313/multi-tenant-apps(front-and-back-separation)-how-t

> The resource server will validate the access token and determine if it has the right permissions, using the information within the token.

I do not get how to do that yet.

https://www.compositional-it.com/news-blog/safe-stack-authentication-with-active-directory-part-2/

Damn it, I forgot about this.

https://stackoverflow.com/questions/72850957/verifying-token-from-msal-react-on-backend

This is exactly my biggest unkown right now.

https://learn.microsoft.com/hr-hr/azure/active-directory/develop/access-tokens#validating-tokens

https://learn.microsoft.com/hr-hr/azure/active-directory/develop/access-tokens#validate-tokens

> The Azure AD middleware has built-in capabilities for validating access tokens, see samples to find one in the appropriate language. There are also several third-party open-source libraries available for JWT validation. For more information about Azure AD authentication libraries and code samples, see the authentication libraries.

5:45pm. https://learn.microsoft.com/hr-hr/azure/active-directory/develop/sample-v2-code

Uh, what am I supposed to use to validate the JWT tokens? There are a shitload of samples here.

> I am working on a SAFE Stack application and to get around the redirect difficulties caused by the Vite dev server, I'll implement most of the necessary auth logic on the client. The docs for MSAL React are straightforward. I'll figure out to include the JWT token in the requests as well. What I am having trouble understanding is just how am I supposed to validate the token on the ASP.NET side. Which library am I supposed to use for that? One thing I've to understand is how ASP.NET is handling secret keys. Assuming the client and the server use the same one, I'll have no trouble validating the token using the JWT middleware, but will it really be that easy? I have no idea what goes on under the hood.

https://github.com/Azure-Samples/active-directory-aspnetcore-webapp-openidconnect-v2/blob/master/4-WebApp-your-API/4-1-MyOrg/README.md

I think I should just start with MSAL.NET.

https://github.com/AzureAD/microsoft-authentication-library-for-dotnet

> Microsoft.Identity.Client

Oh this is the MSAL for .NET package. I remember it having a ton of downloads.

It doesn't seem to have any functions I can use to validate the token from a request.

https://github.com/Azure-Samples/active-directory-aspnetcore-webapp-openidconnect-v2/blob/master/4-WebApp-your-API/4-1-MyOrg/README.md

I am going to study this tomorrow. It doesn't matter from where the token comes from. The web API will have to verify it either way, and that is when I will know how it could be done.

https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-react#samples

Or I could just check the advanced examples out here.

https://github.com/Azure-Samples/ms-identity-javascript-react-tutorial/tree/main/3-Authorization-II/1-call-api

This is exactly what I need.

https://github.com/Azure-Samples/ms-identity-javascript-react-tutorial/blob/main/3-Authorization-II/1-call-api/API/authConfig.js

This isn't too hard. It seems it uses vanilla JWT middleware to decode the stuff. Still, what about the secret key for the encryption. I am confused where that should come into play.

Ah whatever. I'll figure it out somehow.

https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/implementation/key-management?view=aspnetcore-7.0

6:20pm. Enough. I'll just pass the token through the JWT middleware and if that fails ask for help. This is not work debating any further.

Let me close here. Time to rest."

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[997dac9616...](https://github.com/ss220-space/tgstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Wednesday 2023-04-19 16:37:20 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [xXPawnStarrXx/Skyrat-tg](https://github.com/xXPawnStarrXx/Skyrat-tg)@[018db9ab81...](https://github.com/xXPawnStarrXx/Skyrat-tg/commit/018db9ab81453478875e2af9e7dcb7deae959bf3)
#### Wednesday 2023-04-19 18:14:12 by SkyratBot

[MIRROR] Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs [MDB IGNORE] (#20337)

* Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

## About The Pull Request
Reduces the price of the Doomsday equipment by 20 PT for each APC hacked
in a Head of Staff office, as well as the Vault.
## Why It's Good For The Game
See #71404 for the prior PR and my full reasoning.

Long-story short, activating the Doomsday before having a plan in place
is suicide, and it takes 13 APCs to unlock. Since there are few well
hidden APCs in general, you'll usually be gathering APCs after going
loud (such as with a borg machine). 13 APCs is 13 minutes, and by the
time you've gathered your malfbux, you're either already dead or have
already taken full control.

I had intended to give Doomsday a flat 70 PT price, but concerns were
raised that an AI could conceivably hack only APCs on their sat (and
perhaps one on the Lavaland outpost) and Doomsday without ever really
touching the station*. So a compromise was proposed, we instead give the
AI discounts by hacking Head of Staff areas, and the Vault, which are
usually situated in well-traveled areas, and also have some fluff
reasoning.

*I still think it'd be suicide to do this, but it's not a hill I want to
die on.
## Changelog
:cl:
balance: Malf AIs that hack Head of Staff and Vault APCs will now find a
discount issued on Doomsday.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs

---------

Co-authored-by: zxaber <37497534+zxaber@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [xXPawnStarrXx/Skyrat-tg](https://github.com/xXPawnStarrXx/Skyrat-tg)@[b828a9851b...](https://github.com/xXPawnStarrXx/Skyrat-tg/commit/b828a9851b193f94acd182677d971da01e6d215b)
#### Wednesday 2023-04-19 18:14:12 by SkyratBot

[MIRROR] Icemoon Hermit Ruin Active Turf Fix - For Real This Time [MDB IGNORE] (#20325)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [xXPawnStarrXx/Skyrat-tg](https://github.com/xXPawnStarrXx/Skyrat-tg)@[54b27a78b5...](https://github.com/xXPawnStarrXx/Skyrat-tg/commit/54b27a78b5559d99d84577a8a38c39ca5cb52851)
#### Wednesday 2023-04-19 18:14:12 by SkyratBot

[MIRROR] IceBoxStation More Active Turf Fixes [MDB IGNORE] (#20339)

* IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request

![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

* IceBoxStation More Active Turf Fixes

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [codeyourwaytofreedom/the_secretary](https://github.com/codeyourwaytofreedom/the_secretary)@[782199c6b5...](https://github.com/codeyourwaytofreedom/the_secretary/commit/782199c6b548c8505a85313eec67c64dbb48dee8)
#### Wednesday 2023-04-19 18:41:53 by codeyourwaytofreedom

Amazing user experience.

Booked and available time slots displayed.

Will add a 3rd option for date transitions.

Great progress today.

Keep going.

Remember why you started.

---
## [aaronaira/carworkshop-hibernate](https://github.com/aaronaira/carworkshop-hibernate)@[a86a34e7e8...](https://github.com/aaronaira/carworkshop-hibernate/commit/a86a34e7e85a95a476a38f345a998c7cf345f97e)
#### Wednesday 2023-04-19 18:42:58 by aaron

We are thinking how shit we can do to make this fucking calendar piece of shit

---
## [Sephi1412/OoT3D-Custom-Sequences](https://github.com/Sephi1412/OoT3D-Custom-Sequences)@[d62be7b0f7...](https://github.com/Sephi1412/OoT3D-Custom-Sequences/commit/d62be7b0f73a8fc44804bf7e0774b750f8dedcb7)
#### Wednesday 2023-04-19 19:07:57 by Sephi1412

New Songs Added (Loop and cmeta files included)

List of songs:
- Chrono Trigger: Boss Battle 2
- Chrono Trigger: Primitive Mountain
- Chrono Trigger: Secret of the Forest
- Kirby and the Amazing Mirror: Boss Theme
- Kirby and the Amazing Mirror: Vs Dark Meta Knight
- Pokemon RSE: Route 113
- Pokemon Stadium: Poke Cup 1-3
- Pokemon Mystery Dungeon: Drenched Bluff
- Pokemon Mystery Dungeon: Quicksand Pit
- Twilight Princess: Palace of the Twilight
- Twilight Princess: Horse Battle
- Breath of the Wild: Thunderblight Ganon
- Skyward Sword: Versus Koloktos
- Under Night In-Birth: Night Walker

---
## [nevimer/Bubberstation](https://github.com/nevimer/Bubberstation)@[3d5585dd82...](https://github.com/nevimer/Bubberstation/commit/3d5585dd826e3e25c10f8f91bea989d7f83ffe7a)
#### Wednesday 2023-04-19 19:42:39 by lessthanthree

[MANUAL MIRROR] Nightvision Rework (In the name of color) (#19608)

* Nightvision Rework (In the name of color) (#73094)

Relies on #72886 for some render relay expansion I use for light_mask
stuff.

Hello bestie! Night vision pissed me off, so I've come to burn this
place to the ground.
Two sections to discuss here. First we'll talk about see_in_dark and why
I hate it, second we'll discuss the lighting plane and how we brighten
it, plus introducing color to the party.

https://www.byond.com/docs/ref/#/mob/var/see_in_dark

See in dark lets us control how far away from us a turf can be before we
hide it/its contents if it's dark (not got luminosity set)
We currently set it semi inconsistently to provide nightvision to mobs.

The trouble is stuff that produces light != stuff that sets luminosity.
The worst case of this can be seen by walking out of escape on icebox,
where you'll see this

![image](https://user-images.githubusercontent.com/58055496/215683654-587fb00f-ebb8-4c83-962d-a1b2bf429c4a.png)

Snow draws above the lighting plane, so the snow will intermittently
draw, depending on see_in_dark and the luminosity from tracking lights.
This would in theory be solvable by modifying the area, but the same
problem applies across many things in the codebase.
As things currently stand, to be emissive you NEED to have a light on
your tile. People are bad at this, and honestly it's a bit much to
expect of them. An emissive overlay on a canister shouldn't need an
element or something and a list on turfs to manage it.
This gets worse when you factor in the patterns I'm using to avoid
drawing lights above nothing, which leads to lights that should show,
but are misoffset because their parent pixel offsets.

It's silly. We do it so we can have things like mesons without just
handing out night vision, but even there the effect of just hiding
objects and mobs looks baddddddd when moving. It's always bothered me.
I'll complain about mesons more later, but really just like, they're too
bright as it is.

I'm proposing here that rather then manually hiding stuff based off
distance from the player, we can instead show/hide using just the
lighting plane. This means things like mesons are gonna get dimmer, but
that's fine because they suck.

It does have some side effects, things like view() on mobs won't hide
stuff in darkness, but that's fine because none actually thinks about
view like that, I think.

Oh and I added a case to prevent examining stuff that's in darkness, and
not right next to you when you don't have enough nightvision, to match
the old behavior `see_in_dark` gave us.

Now I'd like to go on a mild tangent about color, please bare with me

You ever walk around with mesons on when there's a fire going, or an
ethereal or firelocks down.
You notice how there isn't really much color to our lights? Doesn't that
suck?

It's because the way we go about brighting lighting is by making
everything on the lighting plane transparent.
This is fine for brightening things, but it ends up looking kinda crummy
in the end and leads to really washed out colors that should be bright.
Playing engineer or miner gets fucking depressing.

The central idea of this pr, that everything else falls out of, is
instead of making the plane more transparent, we can use color matrixes
to make things AT LEAST x bright.

https://www.byond.com/docs/ref/#/{notes}/color-matrix

Brief recap for color matrixes, fully expanded they're a set of 20
different values in a list
Units generally scale 0-1 as multipliers, though since it's
multiplication in order to make an rgb(1,1,1) pixel fullbright you would
need to use 255s.

A "unit matrix" for color looks like this:
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0, 0, 0, 0
)
```

The first four rows are how much each r, g, b and a impact r, g, b and
well a.
So a first row of `(1, 0, 0, 0)` means 1 unit of r results in 1 unit of
r. and 0 units of green, blue and alpha, and so on.
A first row of `(0, 1, 0, 0)` would make 1 red component into 1 green
component, and leave red, blue and alpha alone, shifting any red of
whatever it's applied to a green.

Using these we can essentially color transform our world. It's a fun
tool. But there's more.

That last row there doesn't take a variable input like the others.
Instead, it ADDS some fraction of 255 to red, green, blue and alpha.

So a fifth row of `(1, 0, 0, 0)` would make every pixel as red as it
could possibly be.

This is what we're going to exploit here. You see all these values
accept negative multipliers, so we can lower colors down instead of
raising them up!
The key idea is using color matrix filters
https://www.byond.com/docs/ref/#/{notes}/filters/color to chain these
operations together.

Pulling alllll the way back, we want to brighten darkness without
affecting brighter colors.
Lower rgb values are darker, higher ones are brighter. This relationship
isn't really linear because of suffering reasons, but it's good enough
for this.
Let's try chaining some matrixes on the lighting plane, which is bright
where fullbright, and dark where dark.

Take a list like this

```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     -0.2, -0.2, -0.2, 0
)
```
That would darken the lighting a bit, but negative values will get
rounded to 0
A subsequent raising by the same amount
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.2, 0.2, 0.2, 0
)
```
Will essentially threshold our brightness at that value.
This ensures we aren't washing out colors when we make things brighter,
while leaving higher values unaffected since they basically just had a
constant subtracted and then readded.

You may have noticed, we gain access to individual color components
here.
This means not only can we darken and lighten by thresholds, we can
COLOR those thresholds.
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.1, 0.2, 0.1, 0
)
```
Something like the above, if applied with its inverse, would tint the
darkness green.
The delta between the different scalars will determine how vivid the
color is, and the actual value will impact the brightness.

Something that's always bothered me about nightvision is it's just
greyscale for the most part, there isn't any color to it.
There was an old idea of coloring the game plane to match their lenses,
but if you've ever played with the colorblind quirk you know that gets
headachey really fast.
So instead of that, lets color just the darkness that these glasses
produce.
It provides some reminder that you're wearing them, instead of just
being something you forget about while playing, and provides a reason to
use flashlights and such since they can give you a clearer, less tinted
view of things while retaining the ability to look around things.

I've so far applied this pattern to JUST headwear for humans (also those
mining wisps)
I'm planning on furthering it to mobs that use nightvision, but I wanted
to get this up cause I don't wanna pr it the day before the freeze.

Mesons are green, sec night vision is red, thermals orange, etc.

I think the effect this gives is really really nice.
I've tuned most things to work for the station, though mesons works for
lavaland for obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail.
That's the difference between say, mesons, and night vision. One helps
you see outlines, the other gives you detail and prevents missing
someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

I have since expanded to all uses of nightvision, coloring most all of
them.

Along the way I turned some toggleable nightvision into just one level.
Fullbright sucks, and I'd rather just have one "good" value.

I've kept it for a few cases, mostly eyes you rip out of mobs.
Impacted mobs are nightmares, aliens, zombies, revenants, states and
sort of stands.

I've done a pass on all mobs and items that impact nightvision and added
what I thought was the right level of color to them. This includes stuff
like blobs and shuttle control consoles
As with glasses much of this was around reducing vision, though I kept
it stronger here, since many of these mobs rely on it for engaging with
the game

<details>
<summary>
Technical Changes
</summary>

filter transitions.
Found this when testing this pr, seemed silly.

This avoids dumbass overlay lighting lighting up wallmounts.
We switch modes if some turfflags are set, to accomplish the same thing
with more overhead, and support showing things through the darkness.

Also fixes a bug where you'd only get one fullscreen object per mob, so
opening and closing a submap would take it away

Also also fixes the lighting backdrop not actually spanning the screen.
It doesn't actually do anything anymore because of the fullscreen light
we have, but just in case that's unsued.
Needs cleanup in future.

color with a sprite

This is to support the above
We relay this plane to lighting mask so openspace can like, have
lighting

vision goggles and such
Side affect of removing see_in_dark. This logic is a bit weak atm, needs
some work.

It's a dupe of the nightvision action button, and newly redundant since
I've removed all uses of it

trasnparent won't render

These sucked
Also transparent stuff should never render, if it does you'll get white
blobs which suck

</details>

Videos! (Github doesn't like using a summary here I'm sorry)
<details>

Demonstration of ghost lighting, and color

https://user-images.githubusercontent.com/58055496/215693983-99e00f9e-7214-4cf4-a76a-6e669a8a1103.mp4

Engi-glass mesons and walking in maint (Potentially overtuned, yellow is
hard)

https://user-images.githubusercontent.com/58055496/215695978-26e7dc45-28aa-4285-ae95-62ea3d79860f.mp4

Diagnostic nightvision goggles and see_in_dark not hiding emissives

https://user-images.githubusercontent.com/58055496/215692233-115b4094-1099-4393-9e94-db2088d834f3.mp4

Sec nightvision (I just think it looks neat)

https://user-images.githubusercontent.com/58055496/215692269-bc08335e-0223-49c3-9faf-d2d7b22fe2d2.mp4

Medical nightvision goggles and other colors

https://user-images.githubusercontent.com/58055496/215692286-0ba3de6a-b1d5-4aed-a6eb-c32794ea45da.mp4

Miner mesons and mobs hiding in lavaland (This is basically the darkest
possible environment)

https://user-images.githubusercontent.com/58055496/215696327-26958b69-0e1c-4412-9298-4e9e68b3df68.mp4

Thermal goggles and coloring displayed mobs

https://user-images.githubusercontent.com/58055496/215692710-d2b101f3-7922-498c-918c-9b528d181430.mp4

</details>

I think it's pretty, and see_in_dark sucks butt.

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
add: The darkness that glasses and hud goggles that impact your
nightvision (think mesons, nightvision goggles, etc) lighten is now
tinted to match the glasses. S pretty IMO, and hopefully it helps with
forgetting you're wearing X.
balance: Nightvision is darker. I think bright looks bad, and things
like mesons do way too much
balance: Mesons (and mobs in general) no longer have a static distance
you can see stuff in the dark. If a tile is lit, you can now see it.
fix: Nightvision no longer dims colored lights, instead simply
thresholding off bits of darkness that are dimmer then some level.
/:cl:

* modular edits

* see_in_dark

* [MIRROR] Adds a unit test to detect double stacked lights [MDB IGNORE] (#19564)

* Adds a unit test to detect double stacked lights

* we really need to get that night vision pr done

* lints fixes

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

* Update augments_eyes.dm

* Update augments_eyes.dm

* eeee

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: SkyratBot <59378654+SkyratBot@users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>
# Conflicts:
#	code/modules/mob/living/basic/space_fauna/netherworld/migo.dm

---
## [nevimer/Bubberstation](https://github.com/nevimer/Bubberstation)@[60dc2b9a23...](https://github.com/nevimer/Bubberstation/commit/60dc2b9a23097dea0a19a8782f71e15f07f3b020)
#### Wednesday 2023-04-19 19:42:39 by Gandalf

[MIRROR] Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918) [MANUAL MIRROR] (#19751)

* Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

* wew

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
# Conflicts:
#	code/modules/events/anomaly/anomaly_dimensional.dm

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[7a64573c8b...](https://github.com/LovliestPlant/Skyrat-tg/commit/7a64573c8bfa01bac0d690db68d4b6528d502579)
#### Wednesday 2023-04-19 20:26:41 by SkyratBot

[MIRROR] Atmos QOL + Small Sprite Fix [MDB IGNORE] (#20243)

* Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

* Atmos QOL + Small Sprite Fix

---------

Co-authored-by: 13spacemen <46101244+13spacemen@users.noreply.github.com>

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[ec67ffb340...](https://github.com/LovliestPlant/Skyrat-tg/commit/ec67ffb340b3c4a64f17eb6458a32cb55ae5183b)
#### Wednesday 2023-04-19 20:26:41 by SkyratBot

[MIRROR] Properly accounts for byond tick fuckery in runechat code [MDB IGNORE] (#20237)

* Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

* Properly accounts for byond tick fuckery in runechat code

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[f3614ce53c...](https://github.com/LovliestPlant/Skyrat-tg/commit/f3614ce53c9f02d6c4e21b935b6231e98d3348af)
#### Wednesday 2023-04-19 20:26:41 by SkyratBot

[MIRROR] Thrown containers splashing on mobs spill some contents on the floor [MDB IGNORE] (#20252)

* Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

* Thrown containers splashing on mobs spill some contents on the floor

---------

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[17c9855a19...](https://github.com/newstools/2023-new-york-post/commit/17c9855a195d5b2935d547a1468dc7a4d9b87aab)
#### Wednesday 2023-04-19 20:39:22 by Billy Einkamerer

Created Text For URL [nypost.com/2023/04/19/my-cheating-boyfriend-broke-my-heart-i-was-in-the-hospital/]

---
## [eyelink/Psychtoolbox-3](https://github.com/eyelink/Psychtoolbox-3)@[9f625848bd...](https://github.com/eyelink/Psychtoolbox-3/commit/9f625848bdfea9126f166d59ea914f7da8aba7ad)
#### Wednesday 2023-04-19 20:53:04 by kleinerm

Merge pull request #697 from kleinerm/master

Pull for PTB 3.0.17 beta "Dynamically High" SP6

PTB 3.0.17 BETA update "Dynamically High!" SP6

### All systems

- More code cleanup and deletion of obsolete/long dead and unused code and functionality.

- All Octave mex files will now be stripped of the most verbose debug symbols. This drastically reduces the size of many Octave mex files, so this Psychtoolbox should shrink considerably in download size / disk space despite new functionality. Some other big binaries related to the no longer supported Ubuntu 14.04/16.04 LTS were deleted for further space savings.

- Quite many Docs and help text updates.

- Various minor improvements to HDR support on Linux and Windows:
  - SimpleHDRDemo: Hide distracting mouse cursor.
  - ImagingStereoMoviePlayer: Fix text drawing and add basic HDR stereo movie playback support.
  - PerceptualVBLSynctest: Add another way to visually check for dual-display video refresh sync, e.g., for stereo setups.
  - HDRViewer: Fix initial mouse cursor positioning on multi-display HDR setups.

- Performance enhancements to drawing of our startup Welcome Screen. The logo can now also be automatically scaled down when running on low-resolution displays.

### Linux

- Make PsychHID on Linux robust against touchscreens that claim to be keyboards on the MS Surface Pro 6 tablet (ipts touchscreen!). GetKeyboardIndices() will no longer enumerate such touch screens as *dysfunctional* keyboards. PsychHID will reject similar weird devices in the future, even if they don't get filtered out by GetKeyboardIndices() iow. future proofing.

- Have special format handling for Video4Linux2 devices which provide video in MJPEG format.

- Fix rejection of AMD DCN-2 / Navi gpu family gpu's for low-level mmio access.

- Rebuilt the drawtext plugin for 32-Bit ARMv7l architecture, ie. the RaspberryPi, to add so far missing support for underlined text drawing.

- XOrgConfSelector: Recommand CTRL+ALT+F3 instead of CTRL+ALT+F1 in case of display server startup failure, as Ubuntu 20.04-LTS uses the VT1 (F1) for the login manager / lock screen, so VT3 (F3) is a better choice for a text console if troubleshooting is needed.

- XOrgConfCreator: Provide improved setup instructions for 10 bpc / depth 30 deep color support: Update to cover the fact that AMD Navi+, Raven Ridge+ and other 2018+ gpu's with DCN display engine are no longer supported by our low-level MMIO hacks for 10 bpc+ framebuffer precision, but instead the standard xorg.conf depth 30 setup should be used to the same effect with higher performance, just as on Intel and NVidia graphics cards. The low-level hacks could be implemented on more modern gpu's but there isn't any practical need or benefit for that anymore, at least not as of PTB 3.0.17.

- PsychVulkan now supports improved visual stimulus onset timing and timestamping via Vulkan driver native support on suitable drivers. This makes use of the VK_GOOGLE_DISPLAY_TIMING extension when available.

- PsychVulkan can now also optimally work with Intel graphics chips on Linux, as has been tested with a prototype Mesa branch for OpenGL+Vulkan interop. This is not yet available as part of standard Linux distributions, but when they are ready, we are ready! Vulkan is not yet supported in a usable way for us on MS-Windows.

- Add new experimental PsychImaging task for HDR:  ``PsychImaging('AddTask', 'General', 'UseStaticHDRHack');`` enables use of a new hack that only works on Linux with classic X11 X-Display X-Server, not on Linux+Wayland and not on other operating systems. This allows dual-display stereo presentation of HDR-10 stimuli, ie. with stereomode 4 or 5 "Dual display stereo", also single-display or multi-display use of this mode, e.g., for frame-sequential stereo presentation of HDR stimuli, or "display wall" multi-HDR-monitor setups. Normally our HDR display support is currently restricted to one HDR monitor per onscreen window, no multi-monitor HDR stereo setups. This hacks makes this work in a limited fashion, as described in the PsychImaging help.
  - A new SimpleHDRLinuxStereoDemo.m shows stereoscopic HDR stimulus display on a dual-HDR-monitor setup.
  - ImagingStereoMoviePlayer shows stereoscopic HDR movie playback as a new optional playback mode.
  - For performance benchmarking of HDR playback, the option to select this hack was also added to PlayMoviesDemo.

### Windows

- Special case handling for Microsoft Surface tablet's builtin video cameras.

- Support new mfvideosrc "Multimedia Foundation" capture plugin.

- Minor video capture improvement: Use device monitors / device providers.

### macOS

- SetupPsychtoolbox: Handle latest Apple macOS Catalina+ brain-damage. Apples Catalina trainwreck needs special treatment. If Psychtoolbox has been downloaded via a webbrowser as a zip file or tgz file and then extracted, then all binary executable files like .dylib's and .mexmaci64 mex files will have the com.apple.quarantine attribute set to prevent them from working in any meaningfully user fixable way - Thanks Apple! Use the xattr command to remove the quarantine flag.

- Delete memcpuCudaOpenGL for macOS. It's dead since Apple decided to drop support for NVidia gpu's - and thereby CUDA - from their "Most advanced operating system in the world".

- PsychtoolboxPostInstallRounte: Deal with another Apple macOS Catalina SDK screwup: Since we are now building Screen() for macOS against 10.15 Catalina with the Catalina SDK we hit a new bug in Apples low-quality software. Apparently when built against the Catalina SDK, but running on older macOS versions than Catalina, then OpenGL rendering into a hidden window (via Preference ‘WindowShieldingLevel’ -1) is broken and triggers GL_INVALID_FRAMEBUFFER_OPERATION_EXT errors. The same works perfectly fine - as expected and tested before release - on Catalina itself. This caused error abort in the fontconfig cache rebuilt code which opens a hidden onscreen window when run under < Catalina. The bug is known to happen at least on 10.14 Mojave, 10.13 High Sierra, and 10.12 Sierra, so probably going back through all older macOS versions. Work around it by suppressing OpenGL error checking during this OpenWindow sequence, as we do not actually need rendering to work here.
Work time spent to diagnose and workaround this bug which is again like almost all macOS issues fully Apples fault: 5 hours. Thanks Apple!

- Note in help GStreamer that movie playback and high quality text rendering on macOS now also needs GStreamer 1.18 at a minimum, 1.18.2 is recommended.

- Refine reporting of OS support status in Screen() startup and Screen('Computer'): Report everything before Catalina as untested and unsupported. Report everything beyond Catalina, ie. macOS 11+, as not yet tested or supported. As of now, i very rarely and infrequently spot-check stuff on my old 10.13.6 High Sierra system under some Matlab version. Given 10.13's end of life and age of that machine, this won't happen often anymore. Also testing Octave 6.1 on 10.13 is just too painful going forward, now that HomeBrew no longer provides Octave bottles for 10.13 and source build just takes way too long -- like a dozen hours!

---
## [KheirFerrum/Cataclysm-BN](https://github.com/KheirFerrum/Cataclysm-BN)@[08d54d0287...](https://github.com/KheirFerrum/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Wednesday 2023-04-19 21:09:30 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [TheGoldenFox64/Shitty-Structures-Minecraft-Mod](https://github.com/TheGoldenFox64/Shitty-Structures-Minecraft-Mod)@[5a76b37fe8...](https://github.com/TheGoldenFox64/Shitty-Structures-Minecraft-Mod/commit/5a76b37fe8353e5f01b367d3e677f5f35bf27492)
#### Wednesday 2023-04-19 21:19:31 by TheGoldenFox64

0.2

landmine
fuck you
winner
netherite x4
weezer
chest

---
## [mrussell246/CS-4550-Group-16-node](https://github.com/mrussell246/CS-4550-Group-16-node)@[7f456915b6...](https://github.com/mrussell246/CS-4550-Group-16-node/commit/7f456915b6b812f72b6571be59905a1e140af3ff)
#### Wednesday 2023-04-19 21:30:56 by Jack Gitter

fucking fuck chrome took 3 hours of my life away son of a fucking btich fuck you fucker

---
## [newstools/2023-iol-saturday-star](https://github.com/newstools/2023-iol-saturday-star)@[577e2be209...](https://github.com/newstools/2023-iol-saturday-star/commit/577e2be209661d7768dbc4cfc81081ec2f6be066)
#### Wednesday 2023-04-19 21:42:04 by Billy Einkamerer

Created Text For URL [www.iol.co.za/saturday-star/news/crime-and-courts/notinmyname-calls-for-life-imprisonment-for-pretoria-man-who-slit-his-girlfriends-childs-throat-51cee5b8-ea49-40d4-8adf-9166b5eddcd7]

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[d068528f5f...](https://github.com/git-for-windows/git/commit/d068528f5f634858bd2f4abfc144699f08ebb44b)
#### Wednesday 2023-04-19 23:43:24 by Johannes Schindelin

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

