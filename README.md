## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-29](docs/good-messages/2022/2022-12-29.md)


1,972,900 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,972,900 were push events containing 2,676,401 commit messages that amount to 165,053,702 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[00d3780c38...](https://github.com/ThePiachu/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Thursday 2022-12-29 00:10:46 by carlarctg

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
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[ce39f048bf...](https://github.com/ThePiachu/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Thursday 2022-12-29 00:10:46 by carlarctg

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
## [Crowbar764/CM13](https://github.com/Crowbar764/CM13)@[639765b0c6...](https://github.com/Crowbar764/CM13/commit/639765b0c69faddeec405080ab4fde79503fcf5d)
#### Thursday 2022-12-29 00:16:08 by Skegal

Loadout - Sniper facepaint (#2015)

# About the pull request

This PR is here to add the sniper facepaint into the loadout for 4
points like the skull facepaint.
 
 I tested it and it worked well as expected.
 
I saw a lot of marines asking the sniper for their bodypaint recently,
and i thought, that since it doesnt change anything game-wise we could
give it on the loadout, as the sniper isnt always here and sometime even
throw it to the trash...also people wont annoy the sniper for his paint
too.

((sorry for the webedit i ran into some problem doing the PR with visual
code studio))

# Explain why it's good for the game

I think its good because it add more customisation to characters with
one more good looking facepaint and like i said earlier, i saw some
marines asking the sniper for it (talked about it on discord and people
seemed to be ok with it)


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

i posted the pic here
https://discord.com/channels/150315577943130112/1054515157923020842 (if
in the pic you see the facepaint above the other paint its normal, i
tested it with the code above the other but it should appear under the
skull paint in the pr)

</details>


# Changelog

:cl: Skegal
add: Added Full Body Paint to Loadout
/:cl:

---
## [Crowbar764/CM13](https://github.com/Crowbar764/CM13)@[0c2b070039...](https://github.com/Crowbar764/CM13/commit/0c2b070039afaa0d18a8bbdeb9c28e8333e16470)
#### Thursday 2022-12-29 00:16:08 by Stan_Albatross

Acid vest TGUI (#2050)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

converts the acid vest config to TGUI

this took a long time to do because the way it's set up was somewhat
annoying

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck  nanoui


![image](https://user-images.githubusercontent.com/66756236/208936729-7814c386-320d-4ae3-85b5-d7da44e9cedf.png)

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
ui: converted the A.C.I.D. harness to use TGUI
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b34e2458d0...](https://github.com/treckstar/yolo-octo-hipster/commit/b34e2458d01191c927842c49dae8c6e60f5d8271)
#### Thursday 2022-12-29 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[08291a6dbb...](https://github.com/Zergspower/Skyrat-tg/commit/08291a6dbb3249d9acbca4f539eb82900d299f26)
#### Thursday 2022-12-29 00:41:19 by SkyratBot

[MIRROR] Guards against uplink failsafe code being the same as unlock code [MDB IGNORE] (#18275)

* Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

* Guards against uplink failsafe code being the same as unlock code

Co-authored-by: san7890 <the@san7890.com>

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[a2e2965168...](https://github.com/seanpdoyle/turbo/commit/a2e2965168e9407af5e5c4af046cc5f1f5c328be)
#### Thursday 2022-12-29 01:19:35 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[4baeb2790c...](https://github.com/cyberitsolutions/bootstrap2020/commit/4baeb2790ccc3b4552ba34d876c40862e842d08e)
#### Thursday 2022-12-29 01:26:23 by Trent W. Buck

nerf alsa logspam from some desktops

This package pulls in no new dependencies.
libasound2 Recommends it, i.e. most Debian users would already have it installed.

https://alloc.cyber.com.au/task/task.php?taskID=34714
https://alloc.cyber.com.au/task/task.php?taskID=34835

    root@amc:~# xzgrep -hFw /usr/share/alsa/ucm2/ucm.conf /var/log/syslog-202212* | cut -d' ' -f2,4- | sort -u | sed 's/ /\t/'
    au-e-4          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    remand2-djerke  alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-10         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-11         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-13-testing alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-15         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-16         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-18         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-2          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-4          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-5          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-6          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru1-22-june22   alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru2new10        alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    sc4-c-3b        alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    sccwcommonaug22 alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.

ircs://irc.libera.chat/#alsa

    11:11 <twb> What's this "ucm" stuff actually *do*?
    11:12 <twb> I've got a farm of like 700 desktops and *one* of them complains that alsa-ucm-conf isn't installed
    11:20 <twb> It doesn't even look like an unusual/interesting desktop.  0 [PCH ]: HDA-Intel - HDA Intel PCH HDA Intel PCH at 0xf7d10000 irq 30
    11:20 <twb> Hrm OK maybe it's more like 10 desktops in a batch
    11:33 <gnarface> dunno really, some internal hardware configuration i think
    11:34 <gnarface> like related to or depended upon by model auto-detect
    11:41 <twb> I guess I'm puzzled why it only happens occasionally, rather than consistently for all snd-hda-intel systems
    11:42 <twb> I have a feeling this might be correlated to the ones that have SoC audio
    11:52 <gnarface> well, nearly the only thing all snd-hda-intel systems have in common is that driver
    11:53 <gnarface> no other driver covers as diverse a batch of otherwise unrelated components from different manufacturers
    11:53 <twb> right!
    11:53 <gnarface> though i suspect kernel version might come into play as to whether ucm stuff is required for a given piece of hardware; it seems to be a newer thing in my experience
    11:54 <twb> So like by the time userland alsa-utils sees things, (I expected) the kernelspace snd-hda-intel should be providing a consistent interface
    11:54 <gnarface> yea, there will be minimum consistency, the hardware using this driver has a vastly different array of features
    11:55 <twb> I've since eyeballed alsa-ucm-conf package and it looks like it's pretty much just a list of policies like "all output mixers are 60% by default; all input mixers are 0% by default
    11:55 <gnarface> hmm, interesting
    11:55 <twb> Maybe at some point that was broken out of the core alsa package
    11:55 <twb> because "alsactl init" normally does that without the ucm config files
    11:56 <gnarface> someone pointed out to someone else in here relatively recently that there's an #alsa-soc
    11:56 <gnarface> they might know more about the SoC boards you're using
    11:56 <twb> The slightly dumb thing is I migrated these systems from alsa to alsa+pulseaudio and alsa+pipewire, but I still need the alsa userland around purely to set the initial mixer levels :-(
    11:57 <twb> Anyway, it's no big deal I guess I'll just install alsa-ucm-conf from now on

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[da481428fb...](https://github.com/i3roly/CMI8788/commit/da481428fb656dffbde82602e15aaa043f2c45ee)
#### Thursday 2022-12-29 01:29:51 by gagan sidhu

wow wow @nickdowell, the ideas you giveth (and beloved FULL <you know what> timmay taketh)

@nickdowell has hosted the AppleUSBAudio driver for the cinema display which handles both input and output streams using the getCurrentSampleFrame function.
	-they overrode the audiostream class by creating an APPULUSBAudioStream class and then return different values depending on the stream.

this is kind of similar to what devin roth of existential audio was telling me about having to create separate engines for streams that are on different clocks.

i have to think really hard about this now because there's going to be some code splitting.

REMEMBER PEOPLE: TIM COOK WENT FULL <YOU KNOW WHAT>.
	https://www.youtube.com/watch?v=X6WHBO_Qc-Q

I LOVE YOU BEN

timmay sittin' shotty
ridin' dirty wit shawty
fat bitch oprah bein naughty
hoardin' APPUL stock--real gaudy

don't matter what timmay do
the buy back or the pump
she know how to dump
black female donald trump

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[eb6c0eb37c...](https://github.com/tgstation/tgstation/commit/eb6c0eb37c095c188074c7cec98bf5bf36a2cf04)
#### Thursday 2022-12-29 01:37:27 by Jacquerel

Dogs use the Pet Command system (#72045)


About The Pull Request

Chiefly this refactors dogs to use the newer component/datum system for "pet which follows instructions". It also refactors it a little bit because I had better ideas while working on this than I had last week. Specifically, instead of passing around keys we just stick a weakref to our currently active behaviour in the blackboard. Basically the same but skipping an unecessary step.

Additionally it adds a component for the previous "befriending a mob by clicking it repeatedly" behaviour which hopefully we won't use too much because it's not very exciting (I am planning on replacing it for dogs some time after Christmas).
The biggest effort in here was making the Fetch command more generic, which includes multiple behaviours (which might be used on their own?) and another component (for holding an item without hands).

Additionally I noticed that dogs would keep following my instructions after they died.
This seems unideal, and would be unideal for virtually any AI controller, so I added it as an AI_flag just in case there's some circumstance where you do want to process AI on a dead mob.

Finally this should replicate all behaviour Ian already had plus "follow" (from rats) and a new bonus easter egg reaction, however I noticed that the fetch command is supposed to have Ian eat any food that you try to get him to fetch.
This has been broken for some time and I will be away from my desk for a couple weeks pretty soon, so I wrote the behaviour for this but left it unused. I will come back to this in the future, once I figure out a way to implement it which does not require adding the "you can hit this" flag to every edible item.

Also I had to refit the recent addition of dogs barking at felinids to fit into this, with a side effect that now dogs won't get mad at a Felinid they are friends with. This... feels like intended behaviour anyway?
Why It's Good For The Game

It's good for these to work the same way instead of reimplementing the same behaviour in multiple files.
Being able to have Ian (or other dogs) follow you around the station is both fun and cute, and also makes him significantly more vulnerable to being murdered.
Changelog

cl
add: Ian has learned some new tricks, tell him what a good boy he is!
add: Ian will come on a walk with you, if you are his friend.
refactor: Ian's tricks work the same way as some other mobs' tricks and should be extendable to future mobs.
fix: Dogs no longer run at the maximum possible speed for a mob at all times.
add: When Ian gets old, he also slows down. Poor little guy.
add: Dogs will no longer dislike the presence of Felinids who have taken the time to befriend them.
/cl

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[0b9264ce5f...](https://github.com/Gofawful5/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Thursday 2022-12-29 01:45:50 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[2d177908e6...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/2d177908e6bcd83fb40cb6be461f1b6bc516efb9)
#### Thursday 2022-12-29 01:49:55 by tanish2k09

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
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[50929f054b...](https://github.com/lizardqueenlexi/orbstation/commit/50929f054b89cab80a1e501b7a01bc74c79163d7)
#### Thursday 2022-12-29 01:57:46 by GuillaumePrata

Goliath dna infusion (#71657)

## About The Pull Request
This is a baseline version of the organs and I intend on polishing them
more in the future (Hopefully after other faunas get added to the
infuser.)

Now, this PR adds goliaths to the DNA infuser at genetics. It gives 4
organs and a final bonus effect.

1- Goliath eyes: Simple mostly filler organ that gives night vision.
2- Goliath lungs: Allow miners to breath either lavaland or the default
air mix. As a side effect they can't breath pure O2 anymore so internals
can't be used. Stay away from N2O or use your gas mask properly.
3- Goliath heart: Give miner ash storm protection
4- Goliath brain: Turns one of the miner's arm into a tendril goliath
hammer that can be used to mine. Like the mounted chainsaw it cannot be
dropped, it has slower atk speed, deals 20 damage by default and a bonus
80 to lavaland fauna, it also acts as a baseball bat against fauna so
you can dodge being hit back with good timing.
As a side effect, you can't equip gloves as your hand is a big ass
hammer...

The extra effect for having all 4 organs is lava immunity for now, I
really want to turn it into something more interesting later.

GAGS organs and bonus coderspriter arm:
![goliath
sprites](https://user-images.githubusercontent.com/55374212/205477889-22cfa586-dd43-405d-80cf-3981b31304e1.png)
If I have time I might animate the arm later.
## Why It's Good For The Game
This add some useful tools for miners if they opt into asking genetics
for help and bother to drag a goliath corpses to it.
The organs can be useful on the station, but they will only really shine
at lavaland.

We were brainstorming more things that miners can get from the station
on their downtime waiting the cargo shuttle to bring their bought gear,
this would be a simple and easy power up for miners that can have some
small (ignoring the hammer arm) bonus to miners, but small power ups
pile up.

I also wrote a hackMD around these organs, their goals, non goals,
future possibilities for fauna organs (goliath and others) etc.
https://hackmd.io/@GuillaumePrata/goliath_infusion_organs

## Changelog
:cl: Guillaume Prata
add: Geneticists figured out how to infuse goliath DNA into humanoids!
(Many monkeys were harmed in the process!)
add: Goliath eyes for nightvision, lungs to breath at lavaland safely,
heart to protect you from ash storms and the brain which turns one of
your arms into a tendril hammer.
add: Tendril hammer: Your arm becomes a giant mass of plate and tendril
but it won't fit on gloves anymore. While slow to swing around, you can
obliterate fauna/megafauna with it, 20 base dmg + 80 bonus damage to
fauna/megafauna with a bonus knockback.
/:cl:

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[590847bdf7...](https://github.com/vincentiusvin/tgstation/commit/590847bdf742b1e53f05ea700d48ec0676cdcf43)
#### Thursday 2022-12-29 02:15:24 by Andrew

Biogenerator tweaks, leather makes more belts and clothing (#71175)

## About The Pull Request

### Revamped the biogenerator UI:


https://user-images.githubusercontent.com/3625094/200973283-b703f21b-c747-493e-98d9-043eef86d410.mp4

### Changed biogenerator icon to use layers and see the biomass level:


https://user-images.githubusercontent.com/3625094/201396065-caeaa412-6676-46f6-875e-efa2dca34985.mp4

### Biogenerator rebalance:

- Now you don't need the beaker to print solid products.
- Biogenerator now accepts all food, not just plants.
- Biogenerator now treats all nutriment subtypes as nutriments, so
vitamins and proteins also turn into biomass.
- Biomass now has the same units as other reagents (you get 5 biomass
from 5 nutrient with tier 1 parts).
- Doubled the cost of all items and reagents. (biomass generation
reduced by 10 and prices - by 5)
- Chemicals output amounts are now in units and you can select how much
you want to output exactly. It will not let you specify more than the
size of container or above 50 units with one button click.
- Reduced the amount of stored items and introduced a limit to the
biomass, both tied to the matter bin tier.

### Recipes changes:

Made biogenerator more dumb by moving the clothing out from the
biogenerator designs, and extending leather recipes instead.

The biogenerator is a grinder/recycler style machine so it doesn't make
sense that it outputs clothing.
Also you need to make leather to craft the toolbelt, while you can't do
the same to craft job-specific belts.
Now you can print leather in biogenerator and craft the leather clothing
by using the leather in-hand.
And the rice hat is now crafted from bamboo, instead of biogenerator.

Also added paper to the biogenerator recipes as it makes stuff from
cellulose and barely anyone knows that you can craft paper from 1 log
and 50 water. And paper is needed in large quantities to craft some
items, like paper frames.

And it doesn't output a pack of rolling paper. It's dumb now. It prints
the rolling paper sheets instead.

## Why It's Good For The Game

Biogenerator had terrible UX and backend logic. I didn't improve much on
BE though, but now it should be less frustrating to use.

Also I hate how biogenerator is superior to all other means of obtaining
its products. It doesn't make sense to grow and grind wheat, for
instance, when you can just throw shit into biogenerator and get the
flour fast. And the costs are ridiculous - you can get a couple of
bottles of fertilizers just from one medium potato.

It honestly begs for more nerfing, at least to make the nutriment -
chemicals exchange rate 1:1.

The reason for the biomass cap is because people use it as a sink for
veggies and generate infinite biomass. Maybe the limit will make them
care more about the part upgrade and offload some of the veggies to the
fridge for the Cook.

Also it was weird that biogenerator could tailor some things, while
others have to be crafted in-hand. Now you can print leather and craft
all types of belts and leather clothing.

## Changelog
:cl:
refactor: biogenerator UI revamped
qol: biogenerator no longer requires beaker for materials, monkey cubes
and nori
balance: biogenerator accepts all food, not just plants
balance: biogenerator treats all nutriment subtypes as nutriments
(vitamins, protein, etc.)
balance: biogenerator product prices doubled
balance: biogenerator biomass storage is limited depending on the level
of matter bins
balance: cowboy boots recipe moved from crafting to leather recipes
balance: leather clothing & belt recipes moved from biogenerator to
leather recipes
balance: rice hat recipe moved from biogenerator to bamboo recipes
balance: biogenerator now outputs rolling paper sheets instead of a pack
add: biogenerator can now print paper
imageadd: biogenerator icons now use overlays, have emissive layer and
indicate the biomass volume
/:cl:

---
## [Ebin-Halcyon/tgstation](https://github.com/Ebin-Halcyon/tgstation)@[03bc97ade5...](https://github.com/Ebin-Halcyon/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Thursday 2022-12-29 02:24:20 by necromanceranne

Nukies Update 6: Interdyne is here for you! Medical Supplies and Atropine! (#71067)

## About The Pull Request

Quite a few changes overall to the nuclear operatives tactical medkit.
The kit is more of a full suite of equipment for performing field
medical duties as a nukie.

- I've split the medkits between two kinds. Basic and premium. Medical
bundle has the premium kit.
- Basic contains additional amounts of basic c2 chem patches, some spare
atropine autoinjectors, sutures and regen mesh, and some basic medical
equipment for tending wounds. 4 TC (as it was before). That's it.
- The premium kit is a far more useful full suite of advanced medical
equipment, MODsuit modules, medical supplies and cybernetic implants,
including the combat hypospray and the combat defib. 15 TC.

**In the premium kit, there is:**
- It has a box of beakers with powerful healing chems. Omnizine,
salicylic acid, oxandrolone, pentetic acid, atropine, salbutamol and
rezadone.
- The combat injector is empty, so you can load it as necessary.
- There are advanced sutures and regenerative mesh packs. They don't
work through spacesuits, but are invaluable for wound repair. Especially
burns.
- There is a surgery arm toolset so you can do field operations without
lugging tools.
- There is a surgery processor module that comes preloaded with advanced
surgeries, a threadripper module, and the combat defib module. The
module works entirely like a combat defib, but you don't need to lose
your belt slot to use it.
- The surgeries are revival, the upgrade surgeries (like vein
threading), brainwashing (did you know they didn't get access to
brainwashing, I think this is a shame) and the better tend wounds
option.
- The nightvision medical hud doubles as a pair of science goggles.

**Atropine changes:**
- Atropine now stops bomb implants from autoexploding. This does **NOT**
stop you from manually detonating the bomb. (This is possible even when
you're dead and haven't left your body)
- As a result, nukies get atropine medipens so that they can potentially
stop themselves detonating prematurely, or stop their allies detonating
prematurely. They have a little pamphlet to help explain how their
microbomb works.

## Why It's Good For The Game

Straight up: The medkit is ass.

The meds in the injector sucks, just getting c2 meds in patches is kind
of insulting for something granted to you from an uplink item (and also
you get those for free with your ~~xbox~~ infiltrator medical room so
lol), and operatives just got the kit for one reason and one reason
only. That combat defib as a _weapon_.

Fuck that. So the kits now much better as a way to both support yourself
AND your team through providing a range of improvements you can provide
the squad, while also not undermining the reason why people may have
wanted the kit (that defib). I would really like to see more nukies
attempt to support one another in combat, and a medic operative is a
role that needs love to make that a reality.

**Edit here**: I reintroduced a low end kit with more c2 medical
supplies _if you want them_. I can see how someone might pinch all of
the medical supplies like a cunt, so maybe we should have a failsafe for
that.

A huge culprit of the lack of value of support meds was usually that
ops...explode when they die. If a medic can pop atropine into an op
before they die, they might be able to save them, or an op could pop
themselves with atropine prematurely to maybe stave off death.

## Changelog
:cl:
balance: Splits the nuclear operative combat medical kit into two
versions: basic and premium.
balance: Basic contains additional amounts of basic c2 chem patches,
some spare atropine autoinjectors, sutures and regen mesh, and some
basic medical equipment for tending wounds. 4 TC (as it was before).
balance: The premium kit is a far more useful full suite of advanced
medical equipment, MODsuit modules, medical supplies and cybernetic
implants, including the combat hypospray and the combat defib. 15 TC.
balance: Atropine stops bomb implants from automatically detonating on
death. You can still manually activate your bomb implant (even when you
are dead).
balance: Operatives start with an atropine pen to stop themselves and
their allies from detonating so they can hopefully be saved by a medical
operative.
add: There is a pamphlet to explain this in the nuclear operative's
survival box.
add: I'm not telling you to read the pamphlet, but you should probably
read the pamphlet.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Ebin-Halcyon/tgstation](https://github.com/Ebin-Halcyon/tgstation)@[a811adac74...](https://github.com/Ebin-Halcyon/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Thursday 2022-12-29 02:24:20 by Epic

Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy (#71433)

First PR, may require some changes or something because I don't know how
to do anything bleh
## About The Pull Request

We already had issues with crewmembers with telekinesis making changes
to the security records (purging them and what not). And, nothing has
been done about it, not yet, anyway. Not only record computers are a
problem as well.


![image](https://user-images.githubusercontent.com/106710384/203241399-8314bcba-d2d0-44af-9360-30ff58dbc39e.png)
Previously, prisoners can access the sec vendor with telepathy, and,
since the vendor is free, spam the vendor and be an annoyance. Sure, I
believe that it is not as big of a problem as purging the security
records, but I feel like it's against what the prison is supposed to
stand for; It's supposed to stop them and get them to listen to ahelps
thrown at them.

I've decided to make a bit of changes to the prison to make it so that
people with telekinesis won't fuck up things as much. This replaces real
computers with nonfunctional ones, adding walls to equipment areas to
make sure prisoners don't spam the vendor, and deletes guns/weapons from
the tables so they won't grab them.

## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/106710384/203241465-833f79da-58a3-4feb-87b0-091fbb846e93.png)
This PR is more tailored to admins dealing with no-good-doers, and goes
for the vibe of "HEY, SOMEONE IS PMING YOU, REPLY TO THEM INSTEAD!" Of
course, this leads to prisoners not interacting with the current round,
and, less chance of them going insane and breaking all the windows with
a telekinesis auto-rifle.

Plus, this can always be reverted in-case someone comes up with coding
stuff in instead. I'm all through with that and willing to work with
whoever to solve the issue.

Also, of course, Closes #60967

## Changelog

:cl:
admin: Nanotrashen made some top-of-the-line changes to their
top-of-the-line prison by walling off their equipment area and removing
some spare guns they somehow left on the tables. We also stole the
security computers, so people with telekinesis can't access them.
/:cl:

---
## [Ebin-Halcyon/tgstation](https://github.com/Ebin-Halcyon/tgstation)@[c185dffda0...](https://github.com/Ebin-Halcyon/tgstation/commit/c185dffda0cc30d8187fa1ba37e5784b8d630ba4)
#### Thursday 2022-12-29 02:24:20 by Jacquerel

Basic Mob Carp Bonus Part: Wall smashing (#71524)

## About The Pull Request

Atomisation of #71421 
This moves the attack function of "environment smash" flags which allow
simple mobs to attack walls into an element, so that we can put it on
other things later.
For some reason while working on carp I convinced myself that they had
"environment_smash" flags, which they do not, so this actually is not
relevant to carp in any way.

While implementing this I learned that the way wall smashing works is
stupid, because walls don't have health and so resultingly if a mob can
attack walls it deletes them in a single click. If we ever decide to
change this then it should be easier in an element than in three
different `attack_animal` reactions.
This is especially silly with the "wumborian fugu" item which allows any
mob it is used on to instantly delete reinforced walls, and also to
destroy tables if they click them like seven or eight times (because it
does not increase their object damage in any way).

## Why It's Good For The Game

Eventually someone will port a basic mob which does use this behaviour
(most of the mining ones for instance) and then this will be useful.
If we ever rebalance wall smashing to not instantly delete walls then
this will also be useful.
Admins can apply this to a mob to allow it to delete walls if they
wanted to do that for some reason, they probably shouldn't to be honest
at least until after we've done point two unless they trust the player
not to just use it to deconstruct the space station.

## Changelog
:cl:
refactor: Moves wall smashing out of simple mob code and into an element
we can reuse for basic mobs later
/:cl:

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[7b658b3c0d...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/7b658b3c0d1b9c7b9672a0a1aa709d2789974190)
#### Thursday 2022-12-29 02:24:46 by SkyratBot

[MIRROR] Drinking singulo ignores supermatter hallucinations and pulls nearby objects [MDB IGNORE] (#18157)

* Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.

![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

* Drinking singulo ignores supermatter hallucinations and pulls nearby objects

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[b476bce004...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/b476bce004f741ccd2fd69526292b5cd1fa4d4c9)
#### Thursday 2022-12-29 02:24:46 by SkyratBot

[MIRROR] Fishing-themed Escape Shuttle [MDB IGNORE] (#18113)

* Fishing-themed Escape Shuttle (#71805)

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

* Fishing-themed Escape Shuttle

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Aospa-Beryllium/proprietary_vendor_xiaomi_beryllium](https://github.com/Aospa-Beryllium/proprietary_vendor_xiaomi_beryllium)@[ecb97fcd38...](https://github.com/Aospa-Beryllium/proprietary_vendor_xiaomi_beryllium/commit/ecb97fcd38084128c2ffdb211839b7d8061b57b2)
#### Thursday 2022-12-29 04:46:38 by Tushar Mahajan

apollo: Enable thermal-engine service
* fuck you xiaomi

Signed-off-by: Tushar Mahajan <mahajant99@gmail.com>

---
## [thwompa/cmss13](https://github.com/thwompa/cmss13)@[ab5f1fcb45...](https://github.com/thwompa/cmss13/commit/ab5f1fcb45311e9a4fff9f6250ec180207c6271e)
#### Thursday 2022-12-29 05:02:02 by carlarctg

Fixed entering APC being 0.1 seconds instead of 1 (#2117)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->
Fixed entering APC being 0.1 seconds instead of 0.5

It had '1' instead of '1 SECONDS'. This isn't intentional because of the
outdated comment and as stated below

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

Sometimes bugs and oversights are elevated into features, this is
effectively one but in practice it means that marines have way too much
freedom of movement and versatility entering it, it's less like a
clunky, bulky, cassettepunk APC and more like a Ferrari convertile. It
also allows them to instantly enter the APC while being killed by a
Xeno, which is stupid and lame.

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
fix: Fixed entering APC being 0.1 seconds instead of 1 second.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [newstools/2022-vanguard-nigeria](https://github.com/newstools/2022-vanguard-nigeria)@[495653dd54...](https://github.com/newstools/2022-vanguard-nigeria/commit/495653dd54a5921a27deb6a3fc64ef30855ea619)
#### Thursday 2022-12-29 05:55:44 by Billy Einkamerer

Created Text For URL [www.vanguardngr.com/2022/12/i-bless-god-for-life-cdq-narrates-near-death-experience/]

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[99537d0123...](https://github.com/lessthnthree/tgstation/commit/99537d0123167a07b242c33dad7c23ec9a5becef)
#### Thursday 2022-12-29 06:09:26 by LemonInTheDark

Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

## About The Pull Request

We no longer always render parallax.
This was causing issues because we can't isolate the white of space from
the vaugely white of everything else.

So instead, if your parallax plane is out of view, we'll not only
disable it, but we'll disable the strand we send from the main plane TO
it.

Instead only blending against the bottom stack.

This does mean there's a possibility for fullwhite on z transition
borders (potentially fixable), or when hijacking the plane (also
fixable, but significantly more annoying).

This is enough to make large maps functional though, so I'm happy with
it

## Why It's Good For The Game

Allows for #71731 and other maps like it. Makes my code actually work

## Changelog
:cl:
fix: Using optimized multiz on > 2 z layer maps will no longer cause
fucko bungo
/:cl:

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[2327e445d2...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/2327e445d26e20ab410a5f97109d2088c00681ce)
#### Thursday 2022-12-29 07:27:42 by SkyratBot

[MIRROR] Gatfruit will no longer drop from ice portals. [MDB IGNORE] (#18202)

* Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.

![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.

![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

* Gatfruit will no longer drop from ice portals.

Co-authored-by: carshalash <carshalash@gmail.com>

---
## [OneAsianTortoise/fulpstation](https://github.com/OneAsianTortoise/fulpstation)@[ca0fedc60f...](https://github.com/OneAsianTortoise/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Thursday 2022-12-29 07:45:30 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [vinylspiders/Skyrat-customization-expansion](https://github.com/vinylspiders/Skyrat-customization-expansion)@[1c76ea5334...](https://github.com/vinylspiders/Skyrat-customization-expansion/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Thursday 2022-12-29 08:05:18 by SkyratBot

[MIRROR] Changes our map_format to SIDE_MAP [MDB IGNORE] (#18070)

* Changes our map_format to SIDE_MAP (#70162)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Changes our map_format to SIDE_MAP

* Modular!

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [littlebabyman/chensgrapplinghook](https://github.com/littlebabyman/chensgrapplinghook)@[cfef97eedf...](https://github.com/littlebabyman/chensgrapplinghook/commit/cfef97eedf43e9e3c5a7dba943a88730a1356ec4)
#### Thursday 2022-12-29 08:07:54 by littlebabyman

keep it simple, stupid

what the fuck were you doing we DONT need to divide shit

---
## [UnionofSovietSocialistRepublics/Spore-Biomechs](https://github.com/UnionofSovietSocialistRepublics/Spore-Biomechs)@[9b31664cfd...](https://github.com/UnionofSovietSocialistRepublics/Spore-Biomechs/commit/9b31664cfd2aa3251bc637da0c6b50b2a5fa001d)
#### Thursday 2022-12-29 08:47:00 by Horizon

holy hell you guy can't even make shit

just let me do shit

---
## [VinsCool/furnace](https://github.com/VinsCool/furnace)@[717f7802a0...](https://github.com/VinsCool/furnace/commit/717f7802a060b15abb47f06bccbab1d8951f9f33)
#### Thursday 2022-12-29 08:57:37 by VinsCool

pokey: there was yet another attempt.
- the delta freq thing is painful, ABSOLUTE pitch will be necessary, I'm afraid :v
- fixed a bunch of 16-bit related bugs, the order is reverted to hardware for channels that will output sound, sorry tiledarrow, it just works that way.
- pretty much everything seems to work and is close enough to RMT, except not really, tuning is commiting suicide with the poor delta being unable to do its thing as I was hoping for it.
- I'm probably wasting my time with this but whatever, if that can somehow work, I'm cool with that...

---
## [devindick/devindick](https://github.com/devindick/devindick)@[39a30a74b5...](https://github.com/devindick/devindick/commit/39a30a74b5bb8442091f11658d502282f4b9861d)
#### Thursday 2022-12-29 09:12:06 by devindick

www.xnxx.com

Get ur porn on. It's where I first learned to suck dick. Enjoy. Start suckin some dick. Start with my 11.5in cock.

---
## [VinsCool/furnace](https://github.com/VinsCool/furnace)@[f6eae14069...](https://github.com/VinsCool/furnace/commit/f6eae140690557cabeab3fe4e117e3c020e99d7c)
#### Thursday 2022-12-29 09:15:22 by VinsCool

pokey: oh god please no this is just cursed
- this is slightly better, I guess, honestly this is terrible unless I can get the absolute pitch reference!

---
## [hululu1068/immortalwrt](https://github.com/hululu1068/immortalwrt)@[9014b748e5...](https://github.com/hululu1068/immortalwrt/commit/9014b748e5a2c95f9c48878a7449d11a8def48de)
#### Thursday 2022-12-29 10:39:26 by Tianling Shen

uboot-rockchip: drop ugly hacks from friendlyarm

Signed-off-by: Tianling Shen <cnsztl@immortalwrt.org>
(cherry picked from commit 974443992ef91a0b429b2ee0ed24eca9a2a3dbd1)

---
## [xoka-pro/goit-python-core-project](https://github.com/xoka-pro/goit-python-core-project)@[c98928749d...](https://github.com/xoka-pro/goit-python-core-project/commit/c98928749da5b08de5099ff4eec54c6fe636d3b3)
#### Thursday 2022-12-29 11:18:04 by Nikita Sherstianykh

Weather func

Working func for getting weather.
- command 'weather *city*'
-if city is incorrect - catch the exceptions
- if city in russia - program says like "russian warship - go fuck yourself"

---
## [Perl/perl5](https://github.com/Perl/perl5)@[48f9127c9d...](https://github.com/Perl/perl5/commit/48f9127c9da4986d575cc6d93a5704ae4e546034)
#### Thursday 2022-12-29 11:22:00 by Yves Orton

regcomp.c etc - rework branch reset so it works properly

Branch reset was hacked in without much thought about how it might interact
with other features. Over time we added named capture and recursive patterns
with GOSUB, but I guess because branch reset is somewhat esoteric we didnt
notice the accumulating issues related to it.

The main problem was my original hack used a fairly simple device to give
multiple OPEN/CLOSE opcodes the same target buffer id. When it was introduced
this was fine. When GOSUB was added later however, we overlooked at that this
broke a key part of the book-keeping for GOSUB.

A GOSUB regop needs to know where to jump to, and which close paren to stop
at. However the structure of the regexp program can change from the time the
regop is created. This means we keep track of every OPEN/CLOSE regop we
encounter during parsing, and when something is inserted into the middle of
the program we make sure to move the offsets we store for the OPEN/CLOSE data.
This is essentially keyed and scaled to the number of parens we have seen.
When branch reset is used however the number of OPEN/CLOSE regops is more than
the number of logical buffers we have seen, and we only move one of the
OPEN/CLOSE buffers that is in the branch reset. Which of course breaks things.

Another issues with branch reset is that it creates weird artifacts like this:
/(?|(?<a>a)|(?<b>b))(?&a)(?&b)/ where the (?&b) actually maps to the (?<a>a)
capture buffer because they both have the same id. Another case is that you
cannot check if $+{b} matched and $+{a} did not, because conceptually they
were the same buffer under the hood.

These bugs are now fixed. The "aliasing" of capture buffers to each other is
now done virtually, and under the hood each capture buffer is distinct. We
introduce the concept of a "logical parno" which is the user visible capture
buffer id, and keep it distinct from the true capture buffer id. Most of the
internal logic uses the "true parno" for its business, so a bunch of problems
go away, and we keep maps from logical to physical parnos, and vice versa,
along with a map that gives use the "next physical parno with the same
logical parno". Thus we can quickly skip through the physical capture buffers
to find the one that matched. This means we also have to introduce a
logical_total_parens as well, to complement the already existing total_parens.
The latter refers to the true number of capture buffers. The former represents
the logical number visible to the user.

It is helpful to consider the following table:

  Logical:    $1      $2     $3       $2     $3     $4     $2     $5
  Physical:    1       2      3        4      5      6      7      8
  Next:        0       4      5        7      0      0      0      0
  Pattern:   /(pre)(?|(?<a>a)(?<b>b)|(?<c>c)(?<d>d)(?<e>e)|(?<f>))(post)/

The names are mapped to physical buffers. So $+{b} will show what is in
physical buffer 3. But $3 will show whichever of buffer 3 or 5 matched.
Similarly @{^CAPTURE} will contain 5 elements, not 8. But %+ will contain all
6 named buffers.

Since the need to map these values is rare, we only store these maps when they
are needed and branch reset has been used, when they are NULL it is assumed
that physical and logical buffers are identical.

Currently the way this change is implemented will likely break plug in regexp
engines because they will be missing the new logical_total_parens field at the
very least. Given that the perl internals code is somewhat poorly abstracted from
the regexp engine, with parts of the abstraction leaking out, I think this is
acceptable. If we want to make plug in regexp engines work properly IMO we
need to add some more hooks that they need to implement than we currently do.
For instance mg.c does more work than it should. Given there are only a few
plug in regexp engines and that it is specialized work, I think this is
acceptable. We can work with the authors to refine the API properly.

Currently this patch does not have tests, that will follow as I assemble them
from the different tickets I am aware of that are related to this.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[e03456d5da...](https://github.com/GeoB99/reactos/commit/e03456d5dabecffa95ac3897f4b144e5063962d4)
#### Thursday 2022-12-29 11:41:16 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

Another important note is that the added code grew up the binary size of x64 FreeLdr and that makes a PE image check fail because the bootloader is too large. Currently such code is disabled for AMD64, until
a real fix comes into place.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[9e69e5d6ac...](https://github.com/lizardqueenlexi/orbstation/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Thursday 2022-12-29 11:50:59 by LemonInTheDark

Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes. 
Should really make a helper for this someday

---
## [elastic/kibana](https://github.com/elastic/kibana)@[afb09ccf8a...](https://github.com/elastic/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Thursday 2022-12-29 13:01:28 by Spencer

Transpile packages on demand, validate all TS projects (#146212)

## Dearest Reviewers 👋 

I've been working on this branch with @mistic and @tylersmalley and
we're really confident in these changes. Additionally, this changes code
in nearly every package in the repo so we don't plan to wait for reviews
to get in before merging this. If you'd like to have a concern
addressed, please feel free to leave a review, but assuming that nobody
raises a blocker in the next 24 hours we plan to merge this EOD pacific
tomorrow, 12/22.

We'll be paying close attention to any issues this causes after merging
and work on getting those fixed ASAP. 🚀

---

The operations team is not confident that we'll have the time to achieve
what we originally set out to accomplish by moving to Bazel with the
time and resources we have available. We have also bought ourselves some
headroom with improvements to babel-register, optimizer caching, and
typescript project structure.

In order to make sure we deliver packages as quickly as possible (many
teams really want them), with a usable and familiar developer
experience, this PR removes Bazel for building packages in favor of
using the same JIT transpilation we use for plugins.

Additionally, packages now use `kbn_references` (again, just copying the
dx from plugins to packages).

Because of the complex relationships between packages/plugins and in
order to prepare ourselves for automatic dependency detection tools we
plan to use in the future, this PR also introduces a "TS Project Linter"
which will validate that every tsconfig.json file meets a few
requirements:

1. the chain of base config files extended by each config includes
`tsconfig.base.json` and not `tsconfig.json`
1. the `include` config is used, and not `files`
2. the `exclude` config includes `target/**/*`
3. the `outDir` compiler option is specified as `target/types`
1. none of these compiler options are specified: `declaration`,
`declarationMap`, `emitDeclarationOnly`, `skipLibCheck`, `target`,
`paths`

4. all references to other packages/plugins use their pkg id, ie:
	
	```js
    // valid
    {
      "kbn_references": ["@kbn/core"]
    }
    // not valid
    {
      "kbn_references": [{ "path": "../../../src/core/tsconfig.json" }]
    }
    ```

5. only packages/plugins which are imported somewhere in the ts code are
listed in `kbn_references`

This linter is not only validating all of the tsconfig.json files, but
it also will fix these config files to deal with just about any
violation that can be produced. Just run `node scripts/ts_project_linter
--fix` locally to apply these fixes, or let CI take care of
automatically fixing things and pushing the changes to your PR.

> **Example:** [`64e93e5`
(#146212)](https://github.com/elastic/kibana/pull/146212/commits/64e93e580679dd55f4fdf19bd01402bc478a1a75)
When I merged main into my PR it included a change which removed the
`@kbn/core-injected-metadata-browser` package. After resolving the
conflicts I missed a few tsconfig files which included references to the
now removed package. The TS Project Linter identified that these
references were removed from the code and pushed a change to the PR to
remove them from the tsconfig.json files.

## No bazel? Does that mean no packages??
Nope! We're still doing packages but we're pretty sure now that we won't
be using Bazel to accomplish the 'distributed caching' and 'change-based
tasks' portions of the packages project.

This PR actually makes packages much easier to work with and will be
followed up with the bundling benefits described by the original
packages RFC. Then we'll work on documentation and advocacy for using
packages for any and all new code.

We're pretty confident that implementing distributed caching and
change-based tasks will be necessary in the future, but because of
recent improvements in the repo we think we can live without them for
**at least** a year.

## Wait, there are still BUILD.bazel files in the repo
Yes, there are still three webpack bundles which are built by Bazel: the
`@kbn/ui-shared-deps-npm` DLL, `@kbn/ui-shared-deps-src` externals, and
the `@kbn/monaco` workers. These three webpack bundles are still created
during bootstrap and remotely cached using bazel. The next phase of this
project is to figure out how to get the package bundling features
described in the RFC with the current optimizer, and we expect these
bundles to go away then. Until then any package that is used in those
three bundles still needs to have a BUILD.bazel file so that they can be
referenced by the remaining webpack builds.

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [maxelblack/maxels-pages](https://github.com/maxelblack/maxels-pages)@[6b04bd6618...](https://github.com/maxelblack/maxels-pages/commit/6b04bd6618720464723f348c07166bcde757156b)
#### Thursday 2022-12-29 13:22:42 by Maxel Black

Delete Lapis Apple

Fuck you shit-like Lapis Apple

---
## [Noobetski/sojourn-station](https://github.com/Noobetski/sojourn-station)@[ef4665ec90...](https://github.com/Noobetski/sojourn-station/commit/ef4665ec90474cf5ac5f6aff34b6fd30e365429d)
#### Thursday 2022-12-29 13:54:34 by DimmaDunk

I HATE LIVERMED, I HATE LIVERMED, I HATE LIVERMED!!! (#3714)

* Makes combat medical kits better

- Replaces Dylovene pill bottle on Combat Medical Kit with Carthatoline pill bottle, as every chem inside it already WAS an upgrade over their normal counterparts, making it better at halting toxins damage and preventing liver from killing you. Also adds a Sanguinum syrette to stave off massive bloodloss which would cause the former as well.
- Replaces one of the Quicklot syrettes with a Sanguinum syrette on the Oxygen Deprivation First Aid Kit for better treatment of causes of oxyloss.
- Standardizes pill icons based on chem colors across all pre-built pills for easier reognition.
- Guarantees the "skill issue/salt PR" tag since it doesn't fix underlying issues of current medical system

* Adds carthatoline pills to deferred and corpsman large kit

Keeping in line with the rest of the PR.

* Blood regen pills!

- Adds pre-made Ferritin-Hemosiderin pills composed of iron and protein to help regenerate lost blood
- Replaces Sanguinum syrette on combat kit with ferritin-hemosiderin pill bottle
- Combat surgery kits now really hold advanced tools (except bone gel since the adv version is Soteria made)
- Makes the advanced bone gel item description not a copypaste of its stock counterpart

* Forgot a comma

Damn my haste.

---
## [jushmar/linux-command](https://github.com/jushmar/linux-command)@[c8acd2a2f1...](https://github.com/jushmar/linux-command/commit/c8acd2a2f1ef88feb75c3ecc2d4d59be2dc3c0e2)
#### Thursday 2022-12-29 14:13:40 by jushmar

Outcall 0528604116 Quick Service by Dubai Sports City Call Girls in UAE

Outcall 0528604116 Quick Service by Dubai Sports City Call Girls in UAE
I have Used the Service from this agency Yesterday in Bur Dubai Area. The call Girl was so corporative and Fashionable. She Came Into my hotel room. I got This Dubai call Girl numbers from Proven Expert so straightway I contacted her. I am so happy after using this agency service. This is highly recommended if you are a visitor in Dubai and you don't have an idea how to get the Call Girls In Dubai. This agency is having a big collection of Indian call Girls In Dubai and Pakistani call Girls In Dubai and the best thing about it is they all are verified, staff. Even They have a huge variety of Independent call Girls In Dubai as well. This agency is holding a confirmed Staff which is a great opportunity for every user in Dubai or any part of UAE.

After reading many positive reviews about this company i have decided to give it a chance. I contact on this call girl number mentioned in the tittle. The whole process was very transparent and clear. I received the call girls photos I chose one of them if I'm not wrong she belongs from Pakistan. She came in my hotel near Al rigga next bur Dubai area. I paid her 2500 aed for 4 hrs. We spent together very good time. She was neat and clean and she was wearing full black dress. I really liked her sense of humor. After the 8 hrs she gave me 30 mins extra for some gossip. i will always remember that Golden Shower. This is how my date ended up. Everything was great. This is called a quality service. I will always consider this call girl agency in future. Cheers

Dubai Call Girls, Call Girls in Dubai, Indian Call Girls in Dubai  , Pakistani Call Girls In Dubai , Russian Call girls In Dubai, Bur Dubai Call Girls, bur Juman Call Girls, Deira Call Girls, Al Mankhool Call Girls, Marina Call Girls, Palm Jumeirah Call Girls, Al barsha Call Girls, Jebel Ali Call Girls, Al Satwa Call Girls, Sports City Call Girls, Business Bay Call Girls, Al Rigga Call Girls, Downtown Dubai Call Girls, Dxb Call Girls, Discovery Gardens Call Girls Burj View Call Girls, Airport Call Girls, Free Zone Call Girls, Emirates Towers Call Girls, Academic City Call Girls, Festival City Call Girls, IBN Battuta Call Girls, Jumeirah Dubai Call Girls, Dubai Land Call Girls, International City Dubai Call Girls, Jebel Ali Dubai Call Girls, Al Barsha Dubai Call Girls, Discovery Gardens Dubai Call Girls, Downtown Dubai Call Girls, Marina Dubai Call Girls, Silicon Oasis Call Girls, Silicon Dubai Call Girls, Sports City Call Girls, Burj Al Arab Dubai Call Girls, Burj Khalifa Tower Call Girls, Business Bay Call Girls, Motor City Call Girls, JLT Dubai Call Girls, Jumeirah Beach Residence Call Girls, Khor Fakkan Dubai Call Girls, Falcon City Dubai Call Girls, The Palm Jebel Call Girls, Jumeirah Lake Tower Call Girls, Sheikh Zayed Road Call Girls, Jumeirah Heights Call Girls, Deira Dubai Call Girls, JBR Dubai Call Girls, Al Jaddaf Dubai Call Girls, DIFC Dubai Call Girls, Downtown.

---
## [himanshutamboli/Practice-Projects](https://github.com/himanshutamboli/Practice-Projects)@[85ad6b32ae...](https://github.com/himanshutamboli/Practice-Projects/commit/85ad6b32aed028c8bfaf77a403a216befaeb20dc)
#### Thursday 2022-12-29 16:07:24 by Himanshu Tamboli

Add files via upload

Practice Project - 2: Medical Cost - Personal Insurance Dataset

Problem Statement:
Insurance Forecast by using Regression Algorithms (tried every algorithm)

Health insurance is a type of insurance that covers medical expenses that arise due to an illness. These expenses could be related to hospitalisation costs, cost of medicines or doctor consultation fees. The main purpose of medical insurance is to receive the best medical care without any strain on your finances. Health insurance plans offer protection against high medical costs. It covers hospitalization expenses, day care procedures, domiciliary expenses, and ambulance charges, besides many others. Based on certain input features such as age, bmi, no of dependents, smoker, region -- medical insurance is calculated.

Columns details:

· age: Age of primary beneficiary

· sex: Insurance contractor gender, female, male

· bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

· children: Number of children covered by health insurance / Number of dependents

· smoker: Smoking

· region: The beneficiary's residential area in the US, northeast, southeast, southwest, northwest

· charges: Individual medical costs billed by health insurance

Predicting the Charges: Can you accurately predict insurance costs?

Downlaod Files:
https://github.com/dsrscientist/dataset4
https://github.com/dsrscientist/dataset4/blob/main/medical_cost_insurance.csv

P.S. - We are using all Regression algorithms as no specific algorithm is proposed to predict the medical insurance charges of a person based on the given data for this medical insurance cost prediction model.

---
## [avar/git](https://github.com/avar/git)@[e3e4898eb5...](https://github.com/avar/git/commit/e3e4898eb513f530df36f0fa57f773f677d038e3)
#### Thursday 2022-12-29 16:10:08 by Ævar Arnfjörð Bjarmason

sequencer API users: fix get_replay_opts() leaks

Make the recently added replay_opts_release() function non-static and
use it for freeing the "struct replay_opts" constructed by the
get_replay_opts() function added in [1] in "builtin/rebase.c", and for
freeing a "struct replay_opts" where we encounter an error before we
invoke sequencer_remove_state(). Let's also use it in
"builtin/revert.c".

In e.g. do_interactive_rebase() we construct a "struct replay_opts"
with "get_replay_opts()", and then call "complete_action()". If we get
far enough in that function without encountering errors we'll call
"pick_commits()" which (indirectly) calls "sequencer_remove_state()"
at the end.

But if we encounter errors anywhere along the way we'd punt out early,
and not free() the memory we allocated. Let's ensure that we free it
by always calling "replay_opts_release()".

We could also make it safe to repeatedly call "replay_opts_release()"
by using FREE_AND_NULL() (and setting "opts->xopts_nr" to "0"), but
let's instead carry a single "no_free" flag.

If we were even more paranoid we could (as an earlier version of this
change did) exhaustively check our state via an enum, e.g. to make
sure that we allow allow calling "replay_opts_release()" after
"sequencer_remove_state()", but not the other way around, or to forbid
invoking either function twice in a row. But such paranoia probably
isn't warranted here, let's instead take the easy way out.

See [2] for the initial implementation of
"sequencer_remove_state()",which assumed that it should be removing
the full (including on-disk) rebase state as a one-off.

1. 73fdc535d26 (rebase -i: use struct rebase_options to parse args,
   2019-04-17)
2. 26ae337be11 (revert: Introduce --reset to remove sequencer state,
   2011-08-04)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

Same as last commit with changes

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0eba6afb26...](https://github.com/treckstar/yolo-octo-hipster/commit/0eba6afb26bff5d7dc5a633293cf1805d45ef8f3)
#### Thursday 2022-12-29 16:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [quickbookhelplus/quickbookhelplus](https://github.com/quickbookhelplus/quickbookhelplus)@[15d3cc84ef...](https://github.com/quickbookhelplus/quickbookhelplus/commit/15d3cc84efa494b665e9f9eed0e6fc3b846351ca)
#### Thursday 2022-12-29 16:51:41 by quickbookhelplus

Create *QuickBooks HelpLine 🔰I(833) ↪ (983)↪ 2639)* Number

QuickBooks Helpline Number +1 833-983-2639 open 24*7 for you so you can acquire the most instant & effective services from us with 24*7 hours, round-the-clock availability. QuickBooks Premier is a stunning accounting Premierduct version of QB that manages complex accounting & financial. Quickbooks Premier Support, entry-level accounting software, and the most enhanced version of the highly popular and user-friendly Quickbooks solution specially created for many small and medium-sized business companies developed by Intuit that manages multiple financial & bookkeeping tasks with its astounding features, but often it happens that users might face technical errors while accessing the software.

QuickBooks is a popular business software that is used by thousands of small businesses all over the world. When something goes wrong with the software, it can be very frustrating for owners to try to solve the problem on their own. That’s where the QuickBooks Helpline comes in. The QuickBooks Helpline is staffed with experienced professionals who are familiar with all of the features and functions of QuickBooks. If you need help troubleshooting a problem or setting up your account, call the QuickBooks Helpline and speak with a member of the team. They will be able to help you out quickly and efficiently.

---
## [davidwilemski/micropub-rs](https://github.com/davidwilemski/micropub-rs)@[07a5bf991f...](https://github.com/davidwilemski/micropub-rs/commit/07a5bf991fc7f721bd30d53c4b7a99e129c5c284)
#### Thursday 2022-12-29 17:44:19 by David Wilemski

Port server to use axum instead of warp

Decided based on some smaller projects that I want to go with axum.
Converts all handlers to use axum format and tested them manually both
locally where possible and in prod for the post based handlers. (still
would love a better way to test where auth is required...)

Does a bit of a hack by using fallback for handling fetching actual
posts since I have slugs with slashes in them, which doesn't fit neatly
into the routing options available. Maybe there's a better way but I
haven't found it yet. I tried a wildcard match (/*slug_url) but that
didn't work because axum detected a conflict with the other routes since
that wildcard was at the root and then panicked. Not sure if maybe
there's a way to order the routes?

Also did some cleanup (deletion of warp code and warning fixes) and left
some TODOs for more general improvements not related to the axum port. I
did allow HEAD requests on all endpoints meant to be served by GET.

I also learned that I had to make the server listen on all interfaces
with a v0 address.  Apparently listening on localhost isn't sufficient
for my current container port publishing configuration. I want to come
back to this but this is what I need for now (and matches the warp
implementation).

Finally, I removed warp - completing the axum port.

Thank you, warp, for getting this blog to where it is. Having used many
web frameworks, I think warp is easy to get started with and has many
great ideas. In the end, axum and warp feel very similar but I think
that I like axum's routing more.

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[df737af4a0...](https://github.com/Floofies/Skyrat-tg/commit/df737af4a02b18388b293005c340a7a46423236e)
#### Thursday 2022-12-29 19:03:29 by SkyratBot

[MIRROR] *hand, or That /One/ Emote You Always Felt Was Missing [MDB IGNORE] (#18200)

* *hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

* *hand, or That /One/ Emote You Always Felt Was Missing

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [Alastors/thaumicinsurgence](https://github.com/Alastors/thaumicinsurgence)@[ec1fcafb5d...](https://github.com/Alastors/thaumicinsurgence/commit/ec1fcafb5da2e63c8b222f6d362310c835decd9b)
#### Thursday 2022-12-29 19:19:35 by ZenMasterSych

Suggested additions (#5)

* fuck you you bastard

* fuck your shit, this aint gonna work

* This should work, fixed ItemRedCrown

* Update en_US.lang

Co-authored-by: Alastors <78517796+Alastors@users.noreply.github.com>
Co-authored-by: Alastors <thensa107@gmail.com>

---
## [Alastors/thaumicinsurgence](https://github.com/Alastors/thaumicinsurgence)@[9ad16d735f...](https://github.com/Alastors/thaumicinsurgence/commit/9ad16d735f0eb298764518168fc76328c6b157f7)
#### Thursday 2022-12-29 19:22:11 by Alastors

Infusion matrix (#6)

* Create zh_CN.lang

* Update en_US.lang

* Some interceptor code cleanup

Private fields, pruned unnecessary try/catches, simplified logic, some variables renamed for clarity and consistency

* Move all essentia in a single tick if it exists

* spotlessApply

* Update BS

* Fuck you Mitch

I did it

* Fixing all the shit for the soap

* Update README.md

* Update README.md

Co-authored-by: [Kiwi233] <42833050+Kiwi233@users.noreply.github.com>
Co-authored-by: Martin Robertz <dream-master@gmx.net>
Co-authored-by: greesyB <greesybuns@gmail.com>
Co-authored-by: greesyB <73182109+greesyB@users.noreply.github.com>
Co-authored-by: GitHub GTNH Actions <>

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[ab2a43663c...](https://github.com/32th-System/deltarune_repainted/commit/ab2a43663cd804103e96e0ae2efe94291abce567)
#### Thursday 2022-12-29 19:29:09 by Fatfuck22

fixing sprites : Ruddins

k so funny things: apparently red ruddin's idle isn't called like "red_ruddin_idle" or following the same stuff as the other sprites (ruddins is called "diamond" in the game files and all other sprites Red ruddins are called "diamond knight"). Wanna know what Toby called them? not "diamond_knight" but "daimond_knight". i can't believe he did a typo IN HIS OWN GAME..... anyway, here's a funny thing that was discovered and i hope everyone in the modding underground feels the same as me (pain)

---
## [mexisme/nixos-hardware](https://github.com/mexisme/nixos-hardware)@[540c80a85a...](https://github.com/mexisme/nixos-hardware/commit/540c80a85a0fe032e928726a9033e1515207fbdc)
#### Thursday 2022-12-29 20:08:08 by mexisme

Initial port from github.com/linux-surface/linux-surface, vendorising the patches and firmware binaries.

Add MS Surface Kernel patches from github.com/linux-surface/linux-surface

Add MS Surface Firmware from github.com/linux-surface/linux-surface

Add MS Surface Hardware config from github.com/linux-surface/linux-surface

Tie-together the Microsoft Surface .nix files

Set to use explicit version of Linux (5.4.7)

- Add the config for Linux 5.4.7

Add kernel 5.4.11

Add kernel 5.4.13

Remove unsupported patches

Revert to kernel 5.4.7 for now

- Problems initialising touchscreen & pen

Add kernel 5.4.15 and 5.4.16

Build kernel 5.4.16, instead

Add kernel 5.4.22

Update the patches for kernel 5.4

Placeholder for Linux kernel 5.5

Copy the IPTS kernel patch from the 5.5 dir to the 5.4 dir.

Conversation on https://gitter.im/linux-surface/community suggested this would
reenable IPTS on 5.4:

-----
@matrixbot Feb 29 15:33
hpfr Blaž Hrastnik (Gitter): thanks for the mention. mexisme (Gitter) finally, someone who actually knows Nix and isn't just a config nerd writing proper NixOS Surface configs! I am stuck on 4.19 at the moment because IPTS is now a proper reverse-engineered kernel driver (https://github.com/linux-surface/intel-precise-touch) instead of just a blob package, and I haven't had time to look at how to package that for Nix. If you're on 5.5, are you just not using IPTS? Would love to help out on packaging that for NixOS
hpfr also, development conversations seem to happen more at #linux-surface on freenode, which you can connect to with matrix via https://matrix.to/#/!OXIGGPCpnzaNVeGtCA:matrix.org if you don't like IRC clients

@matrixbot Feb 29 15:39
hpfr Also, I'm not using jakeday's patches, I'm using the more recent ones from the linux-surface/linux-surface repo, but yeah, for 4.19, so they're a bit different from the 5.x patchsets. afaik 4.19 is still supported because it's the last LTS release that supports the "official" IPTS blob before Linux made changes that required reverse engineering a driver that didn't use GuC submission (I'm just quoting here, I have no idea what that is haha)

@matrixbot Feb 29 19:27
Blaž > now a proper reverse-engineered kernel driver
Should be similar to before, we just offer it as a patch
Blaž https://github.com/linux-surface/linux-surface/blob/master/patches/5.5/0007-ipts.patch
Blaž Anyway I'm keeping an eye out on your NixOS builds since I'm thinking about giving it a try

@matrixbot Feb 29 19:32
Blaž Currently running Arch but using nix as a way to manage development environments for various projects

@matrixbot Mar 01 10:41
hpfr Blaž: well shoot is that patch all that’s necessary for building in-tree? It does all the things the linux-surface/intel-precise-touch repo does?

Dorian Stoll @StollD Mar 01 12:56
Yes
Just adds all the files from the repo to drivers/input/touchscreen and adds the necessary glue to drivers/input/touchscreen/{Makefile, Kconfig}

@matrixbot Mar 02 09:13
hpfr Dorian Stoll (Gitter): oof. Could’ve been on 5.4+ all this time!

Move kernnel *.nix packages under their respective kernel dirs

Use lib.mkDefault

Update to kernel 5.4.24

Update to kernel 5.5.8

Typo

Drivers are modules by default

Revert to 5.4.24 until can fix the config failures

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[cba002fa91...](https://github.com/dragomagol/tgstation/commit/cba002fa912f07112fbbedcab330a35e2bffeab7)
#### Thursday 2022-12-29 20:55:34 by Sol N

converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[47ec8ecd38...](https://github.com/dragomagol/tgstation/commit/47ec8ecd386f028ee8b2697412c89f00c9cd139f)
#### Thursday 2022-12-29 20:55:34 by Rhials

Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![sandstorm](https://user-images.githubusercontent.com/28870487/206070641-80d37afc-a365-4f5e-ad48-e8cdf0153ac9.png)

Hey guys, it's your boy. Back at it again with another meteor-adjacent
event PR.

Adds the Sandstorm random event, inspired by the long-unused admin only
one. It picks a direction to approach from, alerts the crew of its
imminent arrival, and after a little over a minute of preparatory time,
sends waves of sand and dust to grind down everything in that direction.

To accomplish this, some minor adjustments had to be made to meteor
generation code. They can now be passed an optional arg for a direction
to be thrown from, and will pick a random one if no direction is given.

Also introduces the newest addition to our cast of meteors -- space
sand! It's even weaker than space dust, and shows up exclusively in this
event. Space sand is **ineffective against rwalls**, and will not damage
the arrivals area's high-tech sand-resistant glass. This is to prevent
this event from venting one of the most dust-vulnerable areas on the
station, and to make sure new players aren't shafted into firelock hell
when the right angle is picked.

I did a lot of testing and tweaking of numbers to get the damage to
average at about the level I'm comfortable with. This is meant to be a
high-impact event that isn't as destructive (or unavoidable) as a meteor
wave. Speaking of avoidance, let's talk about mitigation:

You get an early warning and a direction the sand will come from. You
have time to grab repair supplies, move to safety, get a MODsuit. You
can make worthwhile repairs as the sand comes in from inside (or
outside, if you're brave enough) with nothing more than a welder and
iron sheets. If you're feeling particularly spicy, you can leverage your
prep time setting up shield generators, which spawn in engineering and
have been added to the maintenance machines loot pool. Anyone can
contribute, so do your part as a good crewmate and help out!

All that being said, the event can't be prevented entirely. Shit's going
to get shredded, especially on the outside of the station. Damage will
vary heavily based on the station and direction, ranging from
inconsequential to threatening. It should happen late enough into the
round that, at the bare minimum, the crew shouldn't be caught
unprepared.

For those of you who are worried, the ORIGINAL sandstorm admin event is
still with us too. It's been moved from the space dust file into the
Sandstorm event file. This PR also makes a very minor change to the
naming of the space _dust_ events, for better menuing.

So, to sum it all up: Sand hits grinds down one side of the station, you
get a minute of warning, shield generators now spawn in maintenance. Be
a good crewmate and help where you can.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

More event variety is good, and events that give the players agency on
how bad the impact will be is even better.

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

:cl: Rhials
add: Sandstorm random event! A random side of the station is pummeled by
an onslaught of sand and dust. If you hear that one is approaching, grab
a welder and some iron to help with repairs!
add: Space sand! It's weak and doesn't hurt reinforced walls, but
shouldn't be underestimated in high quantities.
code: You can now pass a start direction to the
spawn_meteors/spawn_meteor global procs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [elide-dev/v3](https://github.com/elide-dev/v3)@[e8728b3a3c...](https://github.com/elide-dev/v3/commit/e8728b3a3c9dd575d7cce78d9be44fe4339d0b16)
#### Thursday 2022-12-29 20:55:50 by Sam Gammon

fix: more package fixes for sonar (fuck you sonar)

---
## [chloefouilloux/GoogleMaps](https://github.com/chloefouilloux/GoogleMaps)@[598458a809...](https://github.com/chloefouilloux/GoogleMaps/commit/598458a809cae98257962d8f800a77085588a2a4)
#### Thursday 2022-12-29 21:11:44 by chloefouilloux

Add files via upload

How to create an API key. I know it kind of sucks, but you do need to upload some kind of credit card information into Google. I can guarantee you that in the 3 years I have been playing with this I have not paid a single cent! There is absolutely nothing to be afraid of unless you use more than 1GB of map data a day, which is equivalent to more than 20.000 map requests A. DAY. I don't care how much you love ggmap, because it sure as hell isn't that much.

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[65a6c95e05...](https://github.com/Danielkaas94/DTAP/commit/65a6c95e053f20b0a1f1e1a28a1fd474c7656331)
#### Thursday 2022-12-29 21:54:36 by Danielkaas94

I Hope
I hope you find somneone who doesn't make
you sad at night, someone who reminds you how
much they love you every day, who laughs at your
jokes and wants to listen to your music and
genuinely wants to be with you and
doesn't make you second guess
their love for you.

---
## [ikalnytskyi/vm.kalnytskyi.com](https://github.com/ikalnytskyi/vm.kalnytskyi.com)@[89c16f9659...](https://github.com/ikalnytskyi/vm.kalnytskyi.com/commit/89c16f9659ac7eeb78ab8bad543d5ec392159fd3)
#### Thursday 2022-12-29 22:14:30 by Ihor Kalnytskyi

Run Vaultwarden natively

Containers are pain in the ass if all you're looking for is to self host
a bunch of tiny services. The reality, however, bites since there lots
of software without proper packages for Linux distributions.

This patch moves Vaultwarden from running in Podman to be run natively
via old plain systemd unit. For that to happen we first need to unpack
Vaultwarden from the docker image to disk, and then run it in isolated
environment.

Part of the reason why I want this is to play a bit with systemd
sandboxing functionality to understand better its pros and cons.

---
## [Chenhao-Huang/misc_wiredtiger](https://github.com/Chenhao-Huang/misc_wiredtiger)@[24d35561e3...](https://github.com/Chenhao-Huang/misc_wiredtiger/commit/24d35561e328e6568992bcafa18a560d56688185)
#### Thursday 2022-12-29 23:02:59 by Keith Bostic

WT-5521 Cache stuck during format initial load, configured with library checkpoints (#5233)

* If reconciliation requires multiple blocks and checkpoint is running we'll eventually fail.
It's possible this is a big page that will take a lot of writes, avoid wasted work.

* Quit doing so much work in format's read-scan, it's not that useful any more and we're have already
verified the load.

* Configuring WiredTiger library checkpoints is done separately, rather than as part of the
original database open because format tests small caches and you can get into cache stuck
trouble during bulk load. Imagine a single thread doing lots of inserts and creating huge
leaf pages. Those pages can't be evicted when there are checkpoints running in the tree and
the cache gets stuck. That workload is unlikely enough the library can't handle it, and we
configure it away here.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a9d530dc71...](https://github.com/tgstation/tgstation/commit/a9d530dc712e913f7ada9f828f514b23b61de314)
#### Thursday 2022-12-29 23:55:00 by Time-Green

Unfuckies pod blood (#72323)

I broke it in #72220
Thanks to @Fikou for catching this
list(variable = 0.1) doesnt work on byond, so I last-minute improvised
and changed it to
list("[variable]" = 0.1), using a string instead of a typepath. I
already tested it thoroughly so decided it was probably good without
thinking of it anymore

:cl:
fix: fixes pod blood I swear
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [IFuckedUpMerging/tgstation](https://github.com/IFuckedUpMerging/tgstation)@[1409e4b026...](https://github.com/IFuckedUpMerging/tgstation/commit/1409e4b026f359764ca491fd5f73f646227973e6)
#### Thursday 2022-12-29 23:58:04 by LemonInTheDark

JPS Optimization (Light Botcode) (#70623)



## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog


:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:


Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---

