## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-07](docs/good-messages/2022/2022-11-07.md)


2,139,773 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,139,773 were push events containing 3,332,543 commit messages that amount to 274,071,935 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[7cb69c2a8b...](https://github.com/mullenpaul/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Monday 2022-11-07 00:03:43 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [JackDotJS/node-studio](https://github.com/JackDotJS/node-studio)@[0b0aba8e56...](https://github.com/JackDotJS/node-studio/commit/0b0aba8e56c4d9a56cc90574e4e49110100a6bbb)
#### Monday 2022-11-07 00:33:55 by Kyle Edwards

please work im fucking begging you im so sick of trying to decipher this god damn documentation

---
## [AwokeinanEnigma/Violet-Engine-VCO](https://github.com/AwokeinanEnigma/Violet-Engine-VCO)@[6364f81a97...](https://github.com/AwokeinanEnigma/Violet-Engine-VCO/commit/6364f81a978c4fe7bed631f37b453f65ef324a10)
#### Monday 2022-11-07 00:37:42 by AwokeinanEnigma

-implemented basic dieback shader support
still finnicky -- here's the problems:
o-for simulation purposes, DieBack uses love.timer.getTime() which is in seconds but it seems to be very weird in SFML.NET 2.5, not sure if there's some difference or i'm just implementing it wrong using SFML's Clock class
o-i'm like 90% sure that in the process of transferring the shaders over from love2d's custom glsl implementation to standard glsl i fucked *something* up. not sure what though! i changed dieback2's whole distort function to floats because i thought it was the problem when the shaders wouldn't compile. very weird
o-using custom graphics for this is a bad idea and i should transition over to the game's layer approach
why am i even using this engine half of the main features are weird and barely work. oh well, i just that's part of the pain. you just gotta keep going, carpe omnia and all of that.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[075e5cfcde...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/075e5cfcded0c8e62f40b5db66b4bfb77c3708e5)
#### Monday 2022-11-07 01:27:37 by SkyratBot

[MIRROR] Brimdemons & Lobstrosities drop (slightly) useful organs [MDB IGNORE] (#17289)

* Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)

Goliaths, Legions, Watchers, and (as of recently) Bileworms all drop
something vaguely useful when they die.
Brimdemons and Lobstrosities do not. This PR aims to fix that, so that
there's at least some vague benefit to hunting them.

In this case it takes the form of organs you get when you butcher them,
similar to the regenerative core from Legions.
As they're similar to the regenerative core, I modified the regenerative
core to extend from a new common "monster core" typepath which these two
new organs also extend.
Like the regenerative core, both of these items do something when used
and something slightly different if you go to the effort of having
someone implant them into your body. They also decay over time, and you
can use stabilising serum to prevent this from happening.

https://user-images.githubusercontent.com/7483112/195967746-55a7d04d-224e-412d-aedc-3a0ec754db3d.mp4

The Rush Gland from the Lobstrosity lets you do a little impression of
their charging attack, making you run very fast for a handful of seconds
and ignoring slowdown effects. Unlike a lobstrosity you aren't actually
built to do this so if you run into a mob you will fall over, and if you
are doing this on the space station running into any dense object will
also make you fall over (it shouldn't make you _too_ much of a pain for
security to catch).
The idea here is that you use this to save time running back and forth
from the mining base.

The Brimdust Sac from the Brimdemon covers you in exploding dust. The
next three times you take Brute damage some of the dust will explode,
dealing damage equal to an unupgraded PKA shot to anything near you (but
not you).
If you do this in a space station not only is the damage proportionally
lower (still matching the PKA), but it _does_ effect you and also it
sets you on fire. You can remove the buff by showering it off.
The idea here is that you use this for minor revenge damage on enemies
whose attacks you don't manage to dodge.

https://user-images.githubusercontent.com/7483112/195967811-0b362ba9-2da0-42ac-bd55-3809473cbc74.mp4

If you implant the Rush Gland then you can use it once every 3 minutes
without consuming it, and the buff lasts very slightly longer. It will
automatically trigger itself if your health gets low, which might be
good (helps you escape a rough situation) or bad (didn't want to use it
yet).

https://user-images.githubusercontent.com/7483112/195967888-f63f7cbd-60cd-4309-8004-203afc5b2153.mp4

If you implant the Brimdust Sac then you can use it once every 3 minutes
to shake off cloud of dust which gives the buff to everyone nearby, if
you want to kit out your miner squad. The dust cloud also makes you
cough if you stand in it, and it's opaque. If you catch fire with this
organ inside you and aren't in mining atmosphere then it will explode
inside of your abdomen, which should probably be avoided, resultingly it
is very risky to use this on the space station.

* Brimdemons & Lobstrosities drop (slightly) useful organs

* update modular

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [MathiasGagnon/S5Projet](https://github.com/MathiasGagnon/S5Projet)@[d2fd3582fc...](https://github.com/MathiasGagnon/S5Projet/commit/d2fd3582fc7372b8a5aff72dba7882dfd7c1da34)
#### Monday 2022-11-07 01:37:05 by florentcournoyer16

Update mathias_est_un_bum.py

To be fair, you have to have a very high IQ to understand Rick and Morty. The humour is extremely subtle, and without a solid grasp of theoretical physics most of the jokes will go over a typical viewer’s head. There’s also Rick’s nihilistic outlook, which is deftly woven into his characterisation- his personal philosophy draws heavily from Narodnaya Volya literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, to realise that they’re not just funny—they say something deep about LIFE. As a consequence people who dislike Rick & Morty truly ARE idiots- of course they wouldn’t appreciate, for instance, the humour in Rick’s existential catchphrase “Wubba Lubba Dub Dub,” which itself is a cryptic reference to Turgenev’s Russian epic Fathers and Sons. I’m smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Dan Harmon’s genius wit unfolds itself on their television screens.

---
## [PsychoLlama/dotfiles](https://github.com/PsychoLlama/dotfiles)@[0fffd9b31f...](https://github.com/PsychoLlama/dotfiles/commit/0fffd9b31f73e8ff728333bf94832d7b8a1e8248)
#### Monday 2022-11-07 01:49:02 by Jesse Gibson

Export editor from the dotfiles framework

Whoa buddy, this is a hack. But it turns out, you can pull configured
packages back out of the NixOS module system and build them into your
environment. Using that knowledge of evil, I can generate a fake NixOS
system, declaratively configure my Neovim editor, then export it as
a package for easy use in any flake-enabled Nix shell. Has my science
gone too far? Time (and war trials) will tell.

```
nix shell github:PsychoLlama/dotfiles#editor
=> nvim ./
```

---
## [Doctor-Derp/lobotomy-corp13](https://github.com/Doctor-Derp/lobotomy-corp13)@[0220bde488...](https://github.com/Doctor-Derp/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Monday 2022-11-07 01:52:18 by PotatoTomahto

pathfinding

revert

oops

oops 2

god fragment

fixes

fixes oopsie

forgot scorched girl

real scorched fix:

typo

better patrolling

final

forgot about dreaming

dreaming current name

fragment oopsies

violet oopsie

really the final one

final final one

---
## [luckyenoughh/tgstation](https://github.com/luckyenoughh/tgstation)@[14c96d05b8...](https://github.com/luckyenoughh/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Monday 2022-11-07 02:44:59 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [luckyenoughh/tgstation](https://github.com/luckyenoughh/tgstation)@[99b8d6b494...](https://github.com/luckyenoughh/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Monday 2022-11-07 02:44:59 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [Murphy-OrangeMud/Fuck-you-musk](https://github.com/Murphy-OrangeMud/Fuck-you-musk)@[2bed57bd74...](https://github.com/Murphy-OrangeMud/Fuck-you-musk/commit/2bed57bd7465d4f203642fd1b49b1a9ab2e1735f)
#### Monday 2022-11-07 05:08:53 by Murphy-OrangeMud

Merge branch 'main' of github.com:Murphy-OrangeMud/Fuck-you-musk into main

---
## [Moribun/sunset-wasteland](https://github.com/Moribun/sunset-wasteland)@[4c71d18ba0...](https://github.com/Moribun/sunset-wasteland/commit/4c71d18ba0ebc4ab6aa34111da3d8638352ab246)
#### Monday 2022-11-07 05:23:43 by Carl?

Rocket Shrapnel & Other (#689)

- - -
New:
 - Rockets are now their own subclass of projectile, encompassing not just rockets, even though it's weird to say that and kinda wacky, but also grenade launcher projectiles.
 - Rocket classed projectiles can now have shrapnel magnitude and type attributed to them, permitting explosions identical to frag grenades on impact with their selected shrapnel and magnitude.
- - -
Balance:
 - A singular incendiary rocket replaces the high-yield HE round that the NCR Combat Engineer previously got in the rocket kit.
 - Chemical rockets are now absurdly powerful, to compensate for their otherwise useless nature. We'll probably adjust this as needed, if not outright nerf it again.
 - Chemical rockets can be made, but they're a PITA to craft and are likely to be more trouble than they're worth.
 - A singular unit of FEV is enough to OD someone. It's FEV. Stop drinking it.
- - -

---
## [amitlan/postgres](https://github.com/amitlan/postgres)@[8272749e8c...](https://github.com/amitlan/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Monday 2022-11-07 06:38:15 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[3582aa77bb...](https://github.com/lessthnthree/tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Monday 2022-11-07 08:01:44 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [infecsean/Obsidian-Cloud](https://github.com/infecsean/Obsidian-Cloud)@[dcb0ee188e...](https://github.com/infecsean/Obsidian-Cloud/commit/dcb0ee188e2823b47a6b09dc57bb11d8b9c24afc)
#### Monday 2022-11-07 08:24:07 by infecsean

wow look at productive boy over here

wow! productive boy! you a productive boy? productive little cunt? little shithead? productive little piece of shit? productive little momma's boy? productive little boy toy? ok nah thats kinda gay. Productive little dude it is.

---
## [ff2400t/helix](https://github.com/ff2400t/helix)@[973c51c3e9...](https://github.com/ff2400t/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Monday 2022-11-07 09:25:32 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [arturmuller/superstruct](https://github.com/arturmuller/superstruct)@[d9fc2ff0a7...](https://github.com/arturmuller/superstruct/commit/d9fc2ff0a7af71ad7f1bc0aa10eb61806b75d9cc)
#### Monday 2022-11-07 09:37:22 by Elliot Winkler

Support Node 14 (again) (#1112)

It appears that between 0.16.0 and 0.16.1, the minimum version of Node required
to use this package changed, from 14.x to 16.x. This was not explicit but seems
to have been caused by a couple of factors.

But first, what changed. If you look at `src/error.ts` in 0.16.0 you will see
[this line][1]:

```
return (cached ??= [failure, ...failures()])
```

In the [published version of this file in 0.16.0][2] this gets transpiled to:

```
return (_cached = cached) != null ? _cached : cached = [failure, ...failures()];
```

In 0.16.1, the [original line is unchanged][3], but in the [published
version][4] it is transpiled to:

```
return cached ??= [failure, ...failures()];
```

The `??=` syntax is not supported by Node 14, hence, developers are forced to
upgrade to at least Node 16 if they want to use v0.16.1 or greater.

After looking at the diff between these two versions and running some
experiments, I believe that there are two reasons why this line shows up
differently in these two published versions.

1. Different Node versions were used to build and publish these versions. It
appears that Node 14 was used for the former whereas Node 16 was used for the
latter. This assertion is supported by the fact that in the [Rollup
configuration][5], `@babel/preset-env` is configured with `node: true`, which
instructs Babel to [use the current version of Node as a target][6]. So if the
current Node version changes, so does the Babel config.
2. Between 0.16.0 and 0.16.1, [`browserslist` was updated from 4.20.3, to
4.21.4][7] (you will probably need to expand `yarn.lock`; if so, Cmd-F for
"browserslist"). In `browserslist` 4.21.0, [IE 11 was removed from the default
set of browsers][8] (which is being used in this case, since no explicit list is
provided). According to caniuse, [IE 11 does not support the `??=` syntax][9],
so its removal means that Babel doesn't need to transpile this syntax any
longer.

To address this problem, this PR:

* changes the Rollup configuration mentioned above to use `node: "14.0"` instead
of `node: true`, so that Node 14 is always used to compute the transpilation
rules regardless of the version of Node used locally to build and publish the
package
* updates the CI workflow to ensure that Node 14 is being tested (along with 16
and 18)
* adds Node >= 14 to the `engines` field to communicate that it is supported

---

One thing you may wonder is why this change is needed at all. Node 16 is the
current LTS, so shouldn't that be enough? True, but Node 14 hasn't hit
end-of-life yet, and many people are still using it, including my company. We
think this package is really great, but it would be even better if we didn't
have to have a workaround for our libraries that we still want to keep on Node
14.

Thanks for considering :)

[1]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.0/src/error.ts#L44
[2]: https://unpkg.com/superstruct@0.16.0/lib/index.cjs
[3]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.1/src/error.ts#L44
[4]: https://unpkg.com/superstruct@0.16.1/lib/index.cjs.js
[5]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.4/config/rollup.js#L26
[6]: https://babel.dev/docs/en/options#targetsnode
[7]: https://github.com/ianstormtaylor/superstruct/compare/v0.16.0...v0.16.1?diff=unified#diff-51e4f558fae534656963876761c95b83b6ef5da5103c4adef6768219ed76c2deL99
[8]: https://github.com/browserslist/browserslist/blob/main/CHANGELOG.md#421
[9]: https://caniuse.com/?search=%3F%3F%3D

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[c582aeb89f...](https://github.com/clamor-s/u-boot/commit/c582aeb89f4aa2f10da97a3b168327b80fa18f7b)
#### Monday 2022-11-07 09:37:27 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [jkciesluk/metals](https://github.com/jkciesluk/metals)@[6fca4bc1b2...](https://github.com/jkciesluk/metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Monday 2022-11-07 09:50:31 by ckipp01

feat: capture and forward `diagnosticCode`

This relates to the grand plan of
https://github.com/lampepfl/dotty/issues/14904 and recently forwarding
the `diagnosticCode` has been merged in
https://github.com/lampepfl/dotty/pull/15565 and also backported so it
should show up in the 3.2.x series. While this pr isn't super exciting,
it's just making sure we capture the code and forward it, this should
unlock _much_ better ways to determine what code actions are available
for a given diagnostic. Meaning we don't have to do lovely things like
regex on the diagnostic message for Scala 3 diagnostics.

NOTE: that this does need some more changes in the build servers before
this is usable. So we can wait for those to be merged in if you'd like.

- [ ] sbt - https://github.com/sbt/sbt/pull/6998
- [ ] Bloop - https://github.com/scalacenter/bloop/pull/1750
- [ ] Mill - https://github.com/com-lihaoyi/mill/pull/1912

Now if you look at the trace file for a diagnostic you'll see the
addition of the code:

```
  "diagnostics": [
    {
      "range": {
        "start": {
          "line": 9,
          "character": 15
        },
        "end": {
          "line": 9,
          "character": 19
        }
      },
      "severity": 1,
      "code": "7",
      "source": "sbt",
      "message": "Found:    (\u001b[32m\"hi\"\u001b[0m : String)\nRequired: Int\n\nThe following import might make progress towards fixing the problem:\n\n  import sourcecode.Text.generate\n\n"
    }
  ],
```

Refs: https://github.com/lampepfl/dotty/issues/14904

---
## [digitalservicebund/ris-backend-service](https://github.com/digitalservicebund/ris-backend-service)@[27596ab58f...](https://github.com/digitalservicebund/ris-backend-service/commit/27596ab58fd21ec30557757922d405a1db9d67de)
#### Monday 2022-11-07 10:02:52 by Thore Strassburg

Chore(hooks): move secret check to pre-commit

So far the check for secrets runs on pre-push. This leads to some
trouble when working with files that have a checksum. These files (e.g.
`build.gradle.kts` or `README.md`) have false positives and are accepted
with a specific checksum. Adjusting these files always creates a new
checksum and needs to be verified again. Finally the new checksum must
be put into the `.talismanrc` and added to the commit.
If the check runs after all commits are bundled, it is cumbersome to
either interactively rebase the local history to integrate this change,
or append a "stupid" fix commit.
To circumvent this problem, we now check secrets pre-commit. The check
is fast enough to not be annoying on every commit.

---
## [DFE-Digital/manage-teacher-training-applications-prototype](https://github.com/DFE-Digital/manage-teacher-training-applications-prototype)@[9abb82c642...](https://github.com/DFE-Digital/manage-teacher-training-applications-prototype/commit/9abb82c642686abd1f1b66e43b2072e9da611bb7)
#### Monday 2022-11-07 10:50:14 by Frankie Roberto

Use node 16 (#598)

Think this is now required to avoid this Heroku error preventing deployment:

```

       Resolving node version >=14.0.0 <17.0.0...
       Error: Unknown error installing ">=14.0.0 <17.0.0" of node
-----> Build failed

       We're sorry this build is failing! You can troubleshoot common issues here:
       https://devcenter.heroku.com/articles/troubleshooting-node-deploys

       Some possible problems:

       - Dangerous semver range (>) in engines.node
         https://devcenter.heroku.com/articles/nodejs-support#specifying-a-node-js-version
```

---
## [Bee-Have/cpp_duck](https://github.com/Bee-Have/cpp_duck)@[d0ed6b520b...](https://github.com/Bee-Have/cpp_duck/commit/d0ed6b520bca942466fb53d6ef4bed3ef42efb0e)
#### Monday 2022-11-07 11:17:13 by Albe MARINI-AUDOUARD

✨ -Not sure what i changed here. fuck you past me, fuck you.

---
## [someone543/NSV13](https://github.com/someone543/NSV13)@[3249b4560b...](https://github.com/someone543/NSV13/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Monday 2022-11-07 12:19:08 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [theo-hiort-nti-johanneberg/2D_Game](https://github.com/theo-hiort-nti-johanneberg/2D_Game)@[85a8e85a32...](https://github.com/theo-hiort-nti-johanneberg/2D_Game/commit/85a8e85a32e3ffca24bd8ad1347846a7c2e29321)
#### Monday 2022-11-07 12:26:22 by theo-hiort-nti-johanneberg

collision update 2: the reconstruction

- added the ability to die, along with a temporary death screen/ game over screen which is to be changed later but I thought it was funny for now
- added rectangle platforms drawn where I want them to be later on. These are for the time being just for show but will later be turned into instances of the Platform class which enemies and the player can collide with. When this is implemented, the player will only be able to walk on platforms and not on the "floor" aka the bottom of the window
- added system to detect which kind of entity the player or an enemy has collided with. This will later actually matter because there will be different outcomes based on what you collide with, but for now you only die when colliding with enemies. Also you can potentially phase through enemies if you're going fast enough but this will be fixed in conjunction with the platforms being fully implemented.

---
## [nbuchwitz/revpi-linux](https://github.com/nbuchwitz/revpi-linux)@[adee8f3082...](https://github.com/nbuchwitz/revpi-linux/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Monday 2022-11-07 12:55:55 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[1636ba5ed2...](https://github.com/odoo-dev/odoo/commit/1636ba5ed2f8a284bef0930313a85cc3dc7cf072)
#### Monday 2022-11-07 13:29:49 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104335

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [DEFRA/water-abstraction-system](https://github.com/DEFRA/water-abstraction-system)@[cb5cf8f12e...](https://github.com/DEFRA/water-abstraction-system/commit/cb5cf8f12ec3130e8a4444ebeb6dc52ccf982a44)
#### Monday 2022-11-07 13:40:16 by Jason Claxton

Refactoring summary list for each service (#8)

https://github.com/DEFRA/water-abstraction-team/issues/54

We wanted to make the layout for each repo consistent and relate things like jobs to the service they belong to. We then decided we'd report on 'apps' rather than just 'repos', as that is what is running on a server and which 'the service' is dependent on.

We tidied up the external services section, including adding the Charge Module API which we'd, though not in the existing /service-status page, should be. We also got them to return meaningful information.

All the calls for info are now robust. Even if all the other apps and external services were down the page would still display.

All this work meant some major refactoring of the `ServiceStatusService()`, for example, a single method for making HTTP requests to the other apps and services.

All of this is tested. To do this we needed to bring in [Nock](https://github.com/nock/nock) to mock our HTTP requests to the other services and [proxyquire](https://github.com/thlorenz/proxyquire) to allow us to stub our calls to `child_process.exec()`.

** Thoughts on the current state

Looking at the tests we see a copious amount of work needed to mock web requests and system calls. We also have a range of scenarios. In our opinion, they are telling us that our service is doing _too_ much. It is collecting data from different sources in different ways, which means it definitely doesn't just have a single responsibility.

It needs breaking up, which in turn means we can break up the tests and hopefully make them a damn sight less scary.

We didn't do those changes in this PR though, because we'd already clocked up more than 1000 changes, well beyond our working target of 100. So, we've agreed to merge and tackle the refactoring as a separate exercise.

** Rebuilding the package-lock.json

Because of how long this PR had been around and the fact it adds new dependencies, we ended up having major merge issues in the `package-lock.json`. We went for a 'delete-and-rebuild' approach but we know we shouldn't have 😳 .

Next time we'll endeavour to use `npm install --package-lock-only` which we [recently learned](https://tkdodo.eu/blog/solving-conflicts-in-package-lock-json) is a command added to npm to help rectify the package-lock.json in these 'merge-hell' situations. 

Co-authored-by: Stuart Adair <43574728+StuAA78@users.noreply.github.com>
Co-authored-by: Rebecca Ransome <beckyrose200@aol.com>
Co-authored-by: Alan Cruikshanks <alan.cruikshanks@gmail.com>

---
## [yukani/gta-reversed-modern](https://github.com/yukani/gta-reversed-modern)@[e7c11cc2e6...](https://github.com/yukani/gta-reversed-modern/commit/e7c11cc2e6ec3946d82d860febd23f6d8f8642b4)
#### Monday 2022-11-07 14:35:11 by yukani

implement an iterator for replay blocks

this custom iterator making thing is a fucking pain in the ass, hell

---
## [avar/git](https://github.com/avar/git)@[762521e8a5...](https://github.com/avar/git/commit/762521e8a5a6948501d56d51da3f70df4f3dfdbe)
#### Monday 2022-11-07 15:25:00 by Jeff King

t5516: move plaintext-password tests from t5601 and t5516

Commit 6dcbdc0d66 (remote: create fetch.credentialsInUrl config,
2022-06-06) added tests for our handling of passwords in URLs. Since the
obvious URL to be affected is git-over-http, the tests use http. However
they don't set up a test server; they just try to access
https://localhost, assuming it will fail (because the nothing is
listening there).

This causes some possible problems:

  - There might be a web server running on localhost, and we do not
    actually want to connect to that.

  - The DNS resolver, or the local firewall, might take a substantial
    amount of time (or forever, whichever comes first) to fail to
    connect, slowing down the tests cases unnecessarily.

  - Since there's no server, our tests for "allow" and "warn" still
    expect the clone/fetch/push operations to fail, even though in the
    real world we'd expect these to succeed. We scrape stderr to see
    what happened, but it's not as robust as a more realistic test.

Let's instead move these to t5551, which is all about testing http and
where we have a real server. That eliminates any issues with contacting
a strange URL, and lets the "allow" and "warn" tests confirm that the
operation actually succeeds.

It's not quite a verbatim move for a few reasons:

  - we can drop the LIBCURL dependency; it's already part of
    lib-httpd.sh

  - we'll use HTTPD_URL_USER_PASS, etc, instead of our fake URL. To
    avoid repetition, we'll add a few extra variables.

  - the "https://username:@localhost" test uses a funny URL that
    lib-httpd.sh doesn't provide. We'll similarly construct it in a
    variable. Note that we're hard-coding the lib-httpd username here,
    but t5551 already does that everywhere.

  - for the "domain:port" test, the URL provided by lib-httpd is fine,
    since our test server will always be on an exotic port. But we'll
    confirm in the test that this is so.

  - since our message-matching is done via grep, I simplified it to use
    a regex, rather than trying to massage lib-httpd's variables.
    Arguably this makes it more readable, too, while retaining the bits
    we care about: the fatal/warning distinction, the "uses plaintext"
    message, and the fact that the password was redacted.

  - we'll use the /auth/ path for the repo, which shows that we are
    indeed making use of the auth information when needed.

  - we'll also use /smart/; most of these tests could be done via /dumb/
    in t5550, but setting up pushes there requires extra effort and
    dependencies. The smart protocol is what most everyone is using
    these days anyway.

This patch is my own, but I stole the analysis and a few bits of the
commit message from a patch by Johannes Schindelin.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [ProjectValhalla/linux](https://github.com/ProjectValhalla/linux)@[d21f4b7ffc...](https://github.com/ProjectValhalla/linux/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Monday 2022-11-07 15:31:06 by Douglas Anderson

pinctrl: qcom: Avoid glitching lines when we first mux to output

Back in the description of commit e440e30e26dd ("arm64: dts: qcom:
sc7180: Avoid glitching SPI CS at bootup on trogdor") we described a
problem that we were seeing on trogdor devices. I'll re-summarize here
but you can also re-read the original commit.

On trogdor devices, the BIOS is setting up the SPI chip select as:
- mux special function (SPI chip select)
- output enable
- output low (unused because we've muxed as special function)

In the kernel, however, we've moved away from using the chip select
line as special function. Since the kernel wants to fully control the
chip select it's far more efficient to treat the line as a GPIO rather
than sending packet-like commands to the GENI firmware every time we
want the line to toggle.

When we transition from how the BIOS had the pin configured to how the
kernel has the pin configured we end up glitching the line. That's
because we _first_ change the mux of the line and then later set its
output. This glitch is bad and can confuse the device on the other end
of the line.

The old commit e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid
glitching SPI CS at bootup on trogdor") fixed the glitch, though the
solution was far from elegant. It essentially did the thing that
everyone always hates: encoding a sequential program in device tree,
even if it's a simple one. It also, unfortunately, got broken by
commit b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf
separately"). After that commit we did all the muxing _first_ even
though the config (set the pin to output high) was listed first. :(

I looked at ideas for how to solve this more properly. My first
thought was to use the "init" pinctrl state. In theory the "init"
pinctrl state is supposed to be exactly for achieving glitch-free
transitions. My dream would have been for the "init" pinctrl to do
nothing at all. That would let us delay the automatic pin muxing until
the driver could set things up and call pinctrl_init_done(). In other
words, my dream was:

  /* Request the GPIO; init it 1 (because DT says GPIO_ACTIVE_LOW) */
  devm_gpiod_get_index(dev, "cs", GPIOD_OUT_LOW);
  /* Output should be right, so we can remux, yay! */
  pinctrl_init_done(dev);

Unfortunately, it didn't work out. The primary reason is that the MSM
GPIO driver implements gpio_request_enable(). As documented in
pinmux.h, that function automatically remuxes a line as a GPIO. ...and
it does this remuxing _before_ specifying the output of the pin. You
can see in gpiod_get_index() that we call gpiod_request() before
gpiod_configure_flags(). gpiod_request() isn't passed any flags so it
has no idea what the eventual output will be.

We could have debates about whether or not the automatic remuxing to
GPIO for the MSM pinctrl was a good idea or not, but at this point I
think there is a plethora of code that's relying on it and I certainly
wouldn't suggest changing it.

Alternatively, we could try to come up with a way to pass the initial
output state to gpio_request_enable() and plumb all that through. That
seems like it would be doable, but we'd have to plumb it through
several layers in the stack.

This patch implements yet another alternative. Here, we specifically
avoid glitching the first time a pin is muxed to GPIO function if the
direction of the pin is output. The idea is that we can read the state
of the pin before we set the mux and make sure that the re-mux won't
change the state.

NOTES:
- We only do this the first time since later swaps between mux states
  might want to preserve the old output value. In other words, I
  wouldn't want to break a driver that did:
     gpiod_set_value(g, 1);
     pinctrl_select_state(pinctrl, special_state);
     pinctrl_select_default_state();
     /* We should be driving 1 even if "special_state" made the pin 0 */
- It's safe to do this the first time since the driver _couldn't_ have
  explicitly set a state. In order to even be able to control the GPIO
  (at least using gpiod) we have to have requested it which would have
  counted as the first mux.
- In theory, instead of keeping track of the first time a pin was set
  as a GPIO we could enable the glitch-free behavior only when
  msm_pinmux_request_gpio() is in the callchain. That works an enables
  my "dream" implementation above where we use an "init" state to
  solve this. However, it's nice not to have to do this. By handling
  just the first transition to GPIO we can simply let the normal
  "default" remuxing happen and we can be assured that there won't be
  a glitch.

Before this change I could see the glitch reported on the EC console
when booting. It would say this when booting the kernel:
  Unexpected state 1 in CSNRE ISR

After this change there is no error reported.

Note that I haven't reproduced the original problem described in
e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid glitching SPI CS at
bootup on trogdor") but I could believe it might happen in certain
timing conditions.

Fixes: b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf separately")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Link: https://lore.kernel.org/r/20221014103217.1.I656bb2c976ed626e5d37294eb252c1cf3be769dc@changeid
Signed-off-by: Linus Walleij <linus.walleij@linaro.org>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[1a2caa3421...](https://github.com/Buildstarted/linksfordevs/commit/1a2caa34218adf568cff809fcd80cf016fa6cab7)
#### Monday 2022-11-07 15:53:57 by Ben Dornis

Updating: 11/7/2022 3:00:00 PM

 1. Added: Barim's blog · ابراهيم - Experiment Nebula Mesh
    (https://barim.us/post/2022-08-02-experimenter-nebula-mesh-partie-2/)
 2. Added: Wirecutter Recommendation
    (https://xkcd.com/2693/)
 3. Added: Soil
    (https://xkcd.com/2695/)
 4. Added: Export Twitter Followers & Following List (Free Download)
    (https://commentpicker.com/twitter-export.php)
 5. Added: Just store UTC? Not so fast! Handling Time zones is complicated.
    (https://codeopinion.com/just-store-utc-not-so-fast-handling-time-zones-is-complicated/)
 6. Added: anildash 🤪 (anildashmastodon.cloud)
    (https://mastodon.cloud/@anildash/109299991009836007)
 7. Added: Tolerance
    (https://felipecsl.com/2022/11/06/tolerance.html)
 8. Added: GitHub - dotnet/razor: Compiler and tooling experience for Razor ASP.NET Core apps in Visual Studio, Visual Studio for Mac, and VS Code.
    (https://github.com/dotnet/razor)
 9. Added: .NET Interactive Notebooks is now Polyglot Notebooks!
    (https://devblogs.microsoft.com/dotnet/dotnet-interactive-notebooks-is-now-polyglot-notebooks/)
10. Added: Checking univariate identities in linear time - HackMD
    (https://hackmd.io/@arielg/ryGTQXWri)
11. Added: Avoid WebDeploy Locking Errors to IIS with Shadow Copy for ASP.NET Core Apps
    (https://weblog.west-wind.com/posts/2022/Nov/07/Avoid-WebDeploy-Locking-Errors-to-IIS-with-Shadow-Copy-for-ASPNET-Core-Apps)
12. Added: The 2022 Shopping Spree
    (https://www.codingblocks.net/podcast/the-2022-shopping-spree/)
13. Added: The Modern Observability Problem
    (https://www.codeproject.com/Articles/5345955/The-Modern-Observability-Problem)
14. Added: .NET 7 Performance Improvements in .NET MAUI
    (https://devblogs.microsoft.com/dotnet/dotnet-7-performance-improvements-in-dotnet-maui/)
15. Added: Cool features in Visual Studio 2022
    (https://youtube.com/watch?v=NBfNnyPQTKs)
16. Added: Announcing TypeScript 4.9 RC
    (https://devblogs.microsoft.com/typescript/announcing-typescript-4-9-rc/)
17. Added: Introduction - Mina book
    (https://o1-labs.github.io/proof-systems/)
18. Added: SFTP for Azure Blob Storage Now Generally Available
    (https://www.infoq.com/news/2022/11/sftp-azure-blob-storage/)
19. Added: JavaScript Local Storage: All You Need To Know!
    (https://www.telerik.com/blogs/javascript-local-storage-all-you-need-know)
20. Added: .NET Rocks! Making Open Source Work for Everyone with David Whitney
    (https://www.dotnetrocks.com/details/1818)
21. Added: Building a Smart Home - Part 5 Bin Day | LINQ to Fail
    (https://www.aaron-powell.com/posts/2022-11-07-building-a-smart-home---part-5-bin-day/)
22. Added: Serverless Platform Engineering - Jeremy Daly
    (https://www.jeremydaly.com/serverless-platform-engineering/)
23. Added: Infographic - Design Principles for a great Azure Solution
    (https://dailydotnettips.com/infographic-design-principles-for-a-great-azure-solution/)
24. Added: Introduction to CAP_BPF
    (https://mdaverde.com/posts/cap-bpf/)
25. Added: Azure DevOps Podcast: Isaac Abraham: Farmer for Azure Deployments - Episode 216
    (http://feed.azuredevops.show/isaac-abraham-farmer-for-azure-deployments-episode-216)
26. Added: Mutable value types are evil! Sort of...
    (https://steven-giesel.com/blogPost/7b896127-41a4-4008-87cb-d2fbdd5a0d5b)
27. Added: Thoughts on Social Media
    (https://blog.lhotka.net/2022/11/06/Thoughts-On-Social-Media)
28. Added: Insights into Developing with Blazor, AND Containers in .NET 7, Wed, 9 Nov 2022, 5:30 pm   | Meetup
    (https://www.meetup.com/en-AU/adelaide-dotnet/events/289414799/)
29. Added: Mastodon on your own domain without hosting a server
    (https://blog.maartenballiauw.be/post/2022/11/05/mastodon-own-donain-without-hosting-server.html)
30. Added: Windows Documentation
    (https://learn.microsoft.com/en-us/windows/)
31. Added: Moving Beyond, Not Getting Over, Imposter Syndrome
    (https://thoughtbot.com/blog/moving-beyond-not-getting-over-imposter-syndrome)
32. Added: AI Assisted Content Creation - in Optimizely CMS & Commerce (AI Series - Part 2)
    (https://www.codeart.dk/blog/2022/11/ai-assisted-content-creation---in-optimizely-cms--commerce-ai-series---part-2/)
33. Added: Microsoft Introduces New UI Experience for Trying out Computer Vision with Vision Studio
    (https://www.infoq.com/news/2022/11/azure-computer-vision-studio/)
34. Added: OpenTelemetry.Extensions.Hosting 1.0.0-rc9.8
    (https://www.nuget.org/packages/OpenTelemetry.Extensions.Hosting/)
35. Added: Using MediatR in .NET? Maybe replace it with this
    (https://youtube.com/watch?v=aaFLtcf8cO4)
36. Added: NuGet Gallery | Packages matching OpenTelemetry.Exporter
    (https://www.nuget.org/packages?q=OpenTelemetry.Exporter)
37. Added: 3 Ideas for Vercel and Next.js - Mike Alche
    (https://www.mikealche.com/software-development/3-ideas-for-vercel-and-next-js)
38. Added: .NET Conf 2022 - Student Zone
    (https://youtube.com/watch?v=9pbyBGnw8p0)
39. Added: PHP in Visual Studio
    (https://devblogs.microsoft.com/visualstudio/php-in-visual-studio/)
40. Added: Node.js Reference Architecture, Part 10: Accessibility | Red Hat Developer
    (https://developers.redhat.com/articles/2022/11/03/nodejs-reference-architecture-part-10-accessibility)
41. Added: Stop requiring only one assertion per unit test: Multiple assertions are fine
    (https://stackoverflow.blog/2022/11/03/multiple-assertions-per-test-are-fine/)
42. Added: Dev People episode #00 - Matt Warren
    (https://youtube.com/watch?v=hYeFOrNyvlo)
43. Added: Build the modular monolith first
    (https://www.fearofoblivion.com/build-a-modular-monolith-first)
44. Added: Announcing .NET Community Toolkit v8.1.0 Preview 1
    (https://devblogs.microsoft.com/dotnet/announcing-dotnet-community-toolkit-v810-preview-1/)
45. Added: Against Duolingo as a language learning platform
    (https://xrvs.net/posts/2022-11-06-against-duolingo/)
46. Added: Full Text & Vector Search for Firestore with Weaviate
    (https://samos-it.com/posts/full-text-search-for-firestore-with-weaviate.html)
47. Added: .NET MAUI Advent Calendar
    (https://dev.to/icebeam7/net-maui-advent-calendar-48d0)
48. Added: The prospects for war with China: Why I see a serious chance of World War III in the next decade - Chris Blattman
    (https://chrisblattman.com/blog/2022/10/26/the-prospects-for-war-with-china-why-i-see-a-serious-chance-of-world-war-iii-in-the-next-decade/)
49. Added: Bring WCF apps to the latest .NET with CoreWCF and Upgrade Assistant
    (https://devblogs.microsoft.com/dotnet/migration-wcf-to-corewcf-upgrade-assistant/)
50. Added: .NET Data Community Standup - EF7 Custom Model Conventions
    (https://youtu.be/6apfe1L1FhY)
51. Added: Perspectives in AI Assisted Content Creation (AI Series Part 1)
    (https://www.codeart.dk/blog/2022/11/perspectives-ai-assisted-content-creation-part1/)
52. Added: Why am I getting a RPC_E_WRONG_THREAD exception when I'm on the right thread?
    (https://devblogs.microsoft.com/oldnewthing/20221104-00/?p=107353)
53. Added: Die Hard Advent Calendar - Hans Gruber Falling off off Nakatomi Plaza
    (https://www.sweeey.com/products/die-hard-advent-calendar-hans-gruber-falling-off-off-nakatomi-plaza-6rbk)
54. Added: From Figma to Visual Studio - Adding Back-End Logic to Goodreads App
    (https://platform.uno/blog/from-figma-to-visual-studio-adding-back-end-logic-to-goodreads-app/)
55. Added: Uno Platform 4.6: Hello .NET 7!
    (https://platform.uno/blog/uno-platform-4-6-hello-net-7/)
56. Added: Troy Hunt (troyhuntinfosec.exchange)
    (https://infosec.exchange/@troyhunt/109299076867127221)
57. Added: Things I Didn't Build Yet
    (https://blog.waleson.com/2022/11/things-i-didnt-build-yet.html)
58. Added: Create your .NET portfolio in the .NET Conf student zone
    (https://devblogs.microsoft.com/dotnet/dotnet-conf-2022-student-zone/)
59. Added: Debugging tips and tools - Gérald Barré
    (https://www.meziantou.net/debugging-tips-and-tools.htm)
60. Added: NuGet Gallery | Packages matching OpenTelemetry.Instrumentation
    (https://www.nuget.org/packages?q=OpenTelemetry.Instrumentation)
61. Added: Making changes safely at scale
    (https://thoughtbot.com/blog/making-changes-safely-at-scale)
62. Added: On Mac Keychains | Apple Developer Forums
    (https://developer.apple.com/forums/thread/696431)
63. Added: Simple Autocomplete for Blazor
    (https://www.mikesdotnetting.com/article/362/simple-autocomplete-for-blazor)
64. Added: Marking API's as obsolete or as experimental
    (https://steven-giesel.com/blogPost/1d97ea56-9a32-4067-9919-10b9af5623a6)
65. Added: Königsberg
    (https://xkcd.com/2694/)
66. Added: Review: Sonic Frontiers is a fine return to form for the series
    (https://www.videogameschronicle.com/review/sonic-frontiers/)
67. Added: .NET Data Community Standup - EF7 Custom Model Conventions
    (https://youtube.com/watch?v=6apfe1L1FhY)
68. Added: Vaultwarden on an RPi
    (https://www.abortretry.fail/p/vaultwarden-on-an-rpi)
69. Added: lld linked musl on PowerPC64
    (https://maskray.me/blog/2022-11-05-lld-musl-powerpc64)
70. Added: Beckshome.com: Thomas Beck's Blog - Lucene + Blazor, Part 2: Results Paging
    (https://beckshome.com/2022/11/lucene-blazor-part-2-results-paging)
71. Added: Introduction to ASP.NET Core Authentication & Authorization
    (https://youtube.com/watch?v=02Yh3sxzAYI)
72. Added: TypeScript for React Developers – Why TypeScript is Useful and How it Works
    (https://www.freecodecamp.org/news/typescript-for-react-developers/)

Generation took: 00:11:08.1876275

---
## [owid/owid-static](https://github.com/owid/owid-static)@[3fe86116f2...](https://github.com/owid/owid-static/commit/3fe86116f2035fc43005515267801e631b4fb152)
#### Monday 2022-11-07 16:28:43 by owidbot

Deploy 2022-11-07T16:18:18.849Z
Updating chart share-of-adults-who-report-saving-money-in-the-past-year
Updating chart divergence-of-gdp-per-capita-among-latecomers-to-the-capitalist-revolution-18002016
Updating chart divergence-of-gdp-per-capita-among-latecomers-to-the-capitalist-revolution-18002016
Updating chart shares-of-gdp-by-economic-sector
Updating chart inflation-levels-and-volatility-in-high--and-low-income-economies-1960-2017
Updating chart the-rise-and-fall-of-the-share-of-employment-in-industry-18702018
Updating chart the-role-of-agriculture-in-the-fluctuations-of-the-aggregate-economy-in-india-19612017
Updating chart categorical-inequality-average-years-of-schooling-girls-relative-to-boys
Updating chart share-of-women-married-or-in-a-union
Updating chart historys-hockey-stick-worldwide-historical-real-gross-domestic-product-per-capita-finn

Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>
Co-authored-by: Marwa Boukarim <marwa@ourworldindata.org>

---
## [Contrabang/Paradise](https://github.com/Contrabang/Paradise)@[2f4a6d7425...](https://github.com/Contrabang/Paradise/commit/2f4a6d7425c94aff428a20ae4e729a0f6a9f92a1)
#### Monday 2022-11-07 16:50:13 by Contrabang

Revert "holy shit they go under"

FUCK why doesnt it switch branches

This reverts commit 87d85c9ef7da69784730cf7b776b6178736414e6.

---
## [HumanCompatibleAI/go_attack](https://github.com/HumanCompatibleAI/go_attack)@[c9078cd9a4...](https://github.com/HumanCompatibleAI/go_attack/commit/c9078cd9a4699c730316117c4e44bd7bd83fe8f7)
#### Monday 2022-11-07 17:30:42 by Tom Tseng

kubernetes: Log git commit for experiments (#53)

## Description

### Changes

Logs the git commit for an experiment in a `commit` file:
* `kubernetes/update_images.py` passes in the git commit as a `--build-arg`, which is saved as environment variable `GIT_COMMIT` inside the image
* `kubernetes/log-git-commit.sh` logs a timestamp and commit into a file called `commit` in the experiment output directory

### Other notes

(optional reading)

We also discussed logging the Docker digest/hash, which I did not implement in this PR. A few reasons:
* ideally the git commit is enough to look up the image in Docker Hub or to rebuild the image
* docker digests are kinda confusing — there's the digest you see on Docker Hub, then there's the platform-specific digest you get [when you pull from Docker Hub](https://github.com/docker/hub-feedback/issues/1925), and then there's the image ID, all of which are different
  * but I think in summary we can get the digest you see on Docker Hub via `docker inspect --format='{{index .RepoDigests 0}}' <image>`, and then that digest can be used to pull images (`docker pull humancompatibleai/goattack@sha256:<digest>`)
* it's slightly more annoying to log because it can't be saved as an environment info inside the image (the image needs to be built and pushed before we can get a digest for it). So we'd need to fetch the digest in `launch-job.sh` and plumb it through as an argument to `log-git-commit.sh`

## Testing
* launched two `match` replicas and checked that `commit` file was populated
  * it's probably possible that multiple `match` replicas will race and write to the `commit` file simultaneously, but I'd guess this is rare and unimportant enough that it's OK if `commit` is occasionally messed up
* launched a `curriculum` replica and checked that `commit` file was populated
* ran `kubernetes/log-git-commit.sh` a few times locally and checked that a new line is added to `commit` if `GIT_COMMIT` changes

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[5b4ba051a0...](https://github.com/MTandi/tgstation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Monday 2022-11-07 18:28:23 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

## About The Pull Request

Area contents isn't a real list, instead it involves filtering
everything in world
This is slow, and something we should have better support for.

So instead, lets manage a list of turfs inside our area. This is simple,
since we already move turfs by area contents anyway

This should speed up the uses I've found, and opens us up to using this
pattern more often, which should make dev work easier.

By nature this is a tad fragile, so I've added a unit test to double
check my work

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Builds sortedAreas on demand, caching until we mark the cache as
violated

It's faster, and it also has the same behavior

I'm not posting speed changes cause frankly they're gonna be a bit
scattered and I'm scared to.
@Mothblocks if you'd like I can look into it. I think it'll pay for
itself just off `reg_in_areas_in_z` (I looked into it. it's really hard
to tell, sometimes it's a bit slower (0.7), sometimes it's 2 seconds
(0.5 if you use the old master figure) faster. life is pain.)

## Why It's Good For The Game

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [BoyanArnaudov/Java-Basic](https://github.com/BoyanArnaudov/Java-Basic)@[388f5135df...](https://github.com/BoyanArnaudov/Java-Basic/commit/388f5135df63d9cd1bc18fbaae8ec36a548cbf32)
#### Monday 2022-11-07 18:31:05 by Boyan Arnaudov

Condition

Write a console program that reads the age (decimal) and gender ("m" or "f") entered by the user and prints an address from among the following:
- "Mr." - male (gender "m") 16 years or older
- 'Master' - boy (gender 'm') under 16 years of age
- 'Ms.' - female (gender 'f') 16 years or older
- "Miss" - girl (gender "f") under 16
Example:
Input:        Output:                                           Input:        Output:
12             Miss                                                17              Mr.
f                                                                       m

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[9ef64a2416...](https://github.com/omertuc/assisted-service/commit/9ef64a2416301428c36f6da5668936476e130d9a)
#### Monday 2022-11-07 18:52:52 by Omer Tuchfeld

NO-ISSUE: Make code generation faster

# Overview

These changes improve the time it takes to perform `skipper make generate`.
On my machine, the improvement is from 93 seconds down to just 30 seconds.

This is achieved mainly through introducing concurrency to the
generation flow. Another thing that caused slowness is that both
`generate-go-client` and `generate-go-server` validated the swagger
file, which takes quite a bit of time. Instead I changed it so that
none of them validate, and I introduced a new separate swagger
validation step (that runs in parallel to them).

# Concurrency

## Make `-j`

To achieve concurrency, I have simply made it so that `make generate`
re-invokes the Makefile but with the `-j` flag, which tells make to
use multiple threads to process the make targets.

## Tree

But it was not so simple, because some of our generate targets depend on
other generate targets to finish before they themselves can be invoked
without issues. Simply adding `-j30` is insufficient because it means
all targets would run at the same time, and some of them with
dependencies on the others would fail.

To fix this, I've re-organized the targets by making some of them
prerequisites of others, so they form a sort of a tree. At the root of
that tree we have `generate-bundle` which directly and indirectly
depends on all others. That means that simply invoking `generate-bundle`
will now cause make to generate everything. This is not ideal, because
it means users can't just generate a single thing in isolation. But on
the other hand, generating everything is now so fast that it's not that
big of a deal. This can be improved in the future by making fake
targets.

## Go Generate

We used to simply call `go generate <pkg> <pkg> <pkg>...` and pass it
all of our packages in just one call. Instead I've made it so that `go generate <pkg>` for each package is its own Makefile target. This means
Makefile will now run `go generate <pkg>` for each of our packages in
parallel.

### But `mockgen` doesn't like it...

As you can see in the diff, I've changed the `mockgen` output path
extension to `.generated_go` instead of `.go`. This is because in order
to generate mocks, `mockgen` actually creates a temporary go package
that imports the mocked `interface`'s package and uses reflection to
generate the actual mock. `mockgen` then `go build`s this temporary
package, and runs it to produce the mock go file. The issue with this
approach is that since that temporary package imports the mocked
`interface`'s package, which is really just a simple Assisted package,
and that Assisted package in turn imports other Assisted packages, it
means every instance of `mockgen` (we run one for each of our packages)
has to also build and read code from other packages. But since other
instances of `mockgen` are actively *writing code* in those packages
(remember, we're generating `mock_*.go` files) at the same time, what
happens in practice is that `mockgen` is actually trying to build code
that's actively being changed! This causes `mockgen` (or more precisely
`go build`) to crash and burn ungracefully.

The solution is renaming the `mockgen` output path extension to
`.generated_go`, this way the files being modified by `mockgen` are not
actual Go files, so they are ignored by the `mockgen` `go build`
processs. After all generation is done we simply batch rename all of
them to have the correct `.go` extension.

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[5abf369467...](https://github.com/omertuc/assisted-service/commit/5abf369467e49469aad3ae0a63e53d91e4d3ba4f)
#### Monday 2022-11-07 18:53:24 by Omer Tuchfeld

NO-ISSUE: Make code generation faster

# Overview

These changes improve the time it takes to perform `skipper make generate`.
On my machine, the improvement is from 93 seconds down to just 30 seconds.

This is achieved mainly through introducing concurrency to the
generation flow. Another thing that caused slowness is that both
`generate-go-client` and `generate-go-server` validated the swagger
file, which takes quite a bit of time. Instead I changed it so that
none of them validate, and I introduced a new separate swagger
validation step (that runs in parallel to them).

# Concurrency

## Make `-j`

To achieve concurrency, I have simply made it so that `make generate`
re-invokes the Makefile but with the `-j` flag, which tells make to
use multiple threads to process the make targets.

## Tree

But it was not so simple, because some of our generate targets depend on
other generate targets to finish before they themselves can be invoked
without issues. Simply adding `-j` is insufficient because it means
all targets would run at the same time, and some of them with
dependencies on the others would fail.

To fix this, I've re-organized the targets by making some of them
prerequisites of others, so they form a sort of a tree. At the root of
that tree we have `generate-bundle` which directly and indirectly
depends on all others. That means that simply invoking `generate-bundle`
will now cause make to generate everything. This is not ideal, because
it means users can't just generate a single thing in isolation. But on
the other hand, generating everything is now so fast that it's not that
big of a deal. This can be improved in the future by making fake
targets.

## Go Generate

We used to simply call `go generate <pkg> <pkg> <pkg>...` and pass it
all of our packages in just one call. Instead I've made it so that `go generate <pkg>` for each package is its own Makefile target. This means
Makefile will now run `go generate <pkg>` for each of our packages in
parallel.

### But `mockgen` doesn't like it...

As you can see in the diff, I've changed the `mockgen` output path
extension to `.generated_go` instead of `.go`. This is because in order
to generate mocks, `mockgen` actually creates a temporary go package
that imports the mocked `interface`'s package and uses reflection to
generate the actual mock. `mockgen` then `go build`s this temporary
package, and runs it to produce the mock go file. The issue with this
approach is that since that temporary package imports the mocked
`interface`'s package, which is really just a simple Assisted package,
and that Assisted package in turn imports other Assisted packages, it
means every instance of `mockgen` (we run one for each of our packages)
has to also build and read code from other packages. But since other
instances of `mockgen` are actively *writing code* in those packages
(remember, we're generating `mock_*.go` files) at the same time, what
happens in practice is that `mockgen` is actually trying to build code
that's actively being changed! This causes `mockgen` (or more precisely
`go build`) to crash and burn ungracefully.

The solution is renaming the `mockgen` output path extension to
`.generated_go`, this way the files being modified by `mockgen` are not
actual Go files, so they are ignored by the `mockgen` `go build`
processs. After all generation is done we simply batch rename all of
them to have the correct `.go` extension.

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[c5462a5d45...](https://github.com/omertuc/assisted-service/commit/c5462a5d45720cc2cecfa7d9d5d980b6d95f60e1)
#### Monday 2022-11-07 19:14:42 by Omer Tuchfeld

NO-ISSUE: Make code generation faster

# Overview

These changes improve the time it takes to perform `skipper make generate`.
On my machine, the improvement is from 93 seconds down to just 30 seconds.

This is achieved mainly through introducing concurrency to the
generation flow. Another thing that caused slowness is that both
`generate-go-client` and `generate-go-server` validated the swagger
file, which takes quite a bit of time. Instead I changed it so that
none of them validate, and I introduced a new separate swagger
validation step (that runs in parallel to them).

# Concurrency

## Make `-j`

To achieve concurrency, I have simply made it so that `make generate`
re-invokes the Makefile but with the `-j` flag, which tells make to
use multiple threads to process the make targets.

## Tree

But it was not so simple, because some of our generate targets depend on
other generate targets to finish before they themselves can be invoked
without issues. Simply adding `-j` is insufficient because it means
all targets would run at the same time, and some of them with
dependencies on the others would fail.

To fix this, I've re-organized the targets by making some of them
prerequisites of others, so they form a sort of a tree. This is not
ideal, because it means users can't just generate a single thing in
isolation as it will cause Make to automatically build it prerequisites
as well, even though they're not strictly needed as they haven't been
deleted. But on the other hand, generating everything is now so fast
that it's not that big of a deal. This can be improved in the future by
making fake targets.

## Go Generate

We used to simply call `go generate <pkg> <pkg> <pkg>...` and pass it
all of our packages in just one call. Instead I've made it so that `go generate <pkg>` for each package is its own Makefile target. This means
Makefile will now run `go generate <pkg>` for each of our packages in
parallel.

### But `mockgen` doesn't like it...

As you can see in the diff, I've changed the `mockgen` output path
extension to `.generated_go` instead of `.go`. This is because in order
to generate mocks, `mockgen` actually creates a temporary go package
that imports the mocked `interface`'s package and uses reflection to
generate the actual mock. `mockgen` then `go build`s this temporary
package, and runs it to produce the mock go file. The issue with this
approach is that since that temporary package imports the mocked
`interface`'s package, which is really just a simple Assisted package,
and that Assisted package in turn imports other Assisted packages, it
means every instance of `mockgen` (we run one for each of our packages)
has to also build and read code from other packages. But since other
instances of `mockgen` are actively *writing code* in those packages
(remember, we're generating `mock_*.go` files) at the same time, what
happens in practice is that `mockgen` is actually trying to build code
that's actively being changed! This causes `mockgen` (or more precisely
`go build`) to crash and burn ungracefully.

The solution is renaming the `mockgen` output path extension to
`.generated_go`, this way the files being modified by `mockgen` are not
actual Go files, so they are ignored by the `mockgen` `go build`
processs. After all generation is done we simply batch rename all of
them to have the correct `.go` extension.

---
## [ZeWaka/OpenDream](https://github.com/ZeWaka/OpenDream)@[00d56970e1...](https://github.com/ZeWaka/OpenDream/commit/00d56970e117f0ad2e64075381bf6a0db3ddcdbe)
#### Monday 2022-11-07 19:48:47 by Altoids1

Adds operator~= and proper json_encode()ing for /matrix (#845)

* Creates json_encode() for /matrix, adds it to unit tests

This makes these units tests more descriptive about what happened.

EDIT: Fixes json_encode for /matrix

* Moves operator~= evaluation into MetaObjects

This is to allow future support for overloading this operator with user-defined datums later on.

Also this is more friendly towards users overriding /list or /matrix

* Implements operator~= for /matrix

* Adds True and False getter helpers for DreamValue

Writing this every time was getting kinda cumbersome

I also want to encourage eventually supporting maybe having bools being their own type later, rather than piggybacking on floats all the time.

* Edits Matrix unit tests to use equivalence operator

...Instead of a weird helper stuffed into the test suite that they shouldn't really be using.

Also gets rid of the BOM at the top of these Matrix tests. Silly Windows!

* Wixoa review commit

---
## [boranx/opa](https://github.com/boranx/opa)@[965301f90e...](https://github.com/boranx/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Monday 2022-11-07 20:23:55 by Stephan Renatus

ast: support dotted heads (#4660)

This change allows rules to have string prefixes in their heads -- we've
come to call them "ref heads".

String prefixes means that where before, you had

    package a.b.c
    allow = true

you can now have

    package a
    b.c.allow = true

This allows for more concise policies, and different ways to structure
larger rule corpuses.

Backwards-compatibility:

- There are code paths that accept ast.Module structs that don't necessarily
  come from the parser -- so we're backfilling the rule's Head.Reference
  field from the Name when it's not present.
  This is exposed through (Head).Ref() which always returns a Ref.

  This also affects the `opa parse` "pretty" output:

  With x.rego as

    package x
    import future.keywords
    a.b.c.d if true
    e[x] if true

  we get

    $ opa parse x rego
    module
     package
      ref
       data
       "x"
     import
      ref
       future
       "keywords"

     rule
      head
       ref
        a
        "b"
        "c"
        "d"
       true
      body
       expr index=0
        true
     rule
      head
       ref
        e
        x
       true
      body
       expr index=0
        true

  Note that

    Name: e
    Key: x

  becomes

    Reference: e[x]

  in the output above (since that's how we're parsing it, back-compat edge cases aside)

- One special case for backcompat is `p[x] { ... }`:

    rule                    | ref   | key | value | name
    ------------------------+-------+-----+-------+-----
    p[x] { ... }            | p     | x   | nil   | "p"
    p contains x if { ... } | p     | x   | nil   | "p"
    p[x] if { ... }         | p[x]  | nil | true  | ""

  For interpreting a rule, we now have the following procedure:

  1. if it has a Key, it's a multi-value rule; and its Ref defines the set:

     Head{Key: x, Ref: p} ~> p is a set
     ^-- we'd get this from `p contains x if true`
         or `p[x] { true }` (back compat)

  2. if it has a Value, it's a single-value rule; its Ref may contain vars:

     Head{Ref: p.q.r[s], Value: 12} ~> body determines s, `p.q.r.[s]` is 12
     ^-- we'd get this from `p.q.r[s] = 12 { s := "whatever" }`

     Head{Key: x, Ref: p[x], Value: 3} ~> `p[x]` has value 3, `x` is determined
                                          by the rule body
     ^-- we'd get this from `p[x] = 3 if x := 2`
         or `p[x] = 3 { x := 2 }` (back compat)

     Here, the Key isn't used, it's present for backwards compatibility: for ref-
     less rule heads, `p[x] = 3` used to be a partial object: key x, value 3,
     name "p"

- The destinction between complete rules and partial object rules disappears.
  They're both single-value rules now.

- We're now outputting the refs of the rules completely in error messages, as
  it's hard to make sense of "rule r" when there's rule r in package a.b.c and
  rule b.c.r in package a.

Restrictions/next steps:

- Support for ref head rules in the REPL is pretty poor so far. Anything that
  works does so rather accidentally. You should be able to work with policies
  that contain ref heads, but you cannot interactively define them.
  
  This is because before, we'd looked at REPL input like

      p.foo.bar = true

  and noticed that it cannot be a rule, so it's got to be a query. This is no
  longer the case with ref heads.

- Currently vars in Refs are only allowed in the last position. This is expected
 to change in the future.

- Also, for multi-value rules, we can not have a var at all -- so the following
  isn't supported yet:

      p.q.r[s] contains t if { ... }

-----

Most of the work happens when the RuleTree is derived from the ModuleTree -- in
the RuleTree, it doesn't matter if a rule was `p` in `package a.b.c` or `b.c.p`
in `package a`.

As such, the planner and wasm compiler hasn't seen that many adaptations:

- We're putting rules into the ruletree _including_ the var parts, so

  p.q.a = 1
  p.q.[x] = 2 { x := "b" }

  end up in two different leaves:

  p
  `-> q
       `-> a = 1
       `-> [x] = 2`

- When planing a ref, we're checking if a rule tree node's children have
  var keys, and plan "one level higher" accordingly:

  Both sets of rules, p.q.a and p.q[x] will be planned into one function
  (same as before); and accordingly return an object {"a": 1, "b": 2}

- When we don't have vars in the last ref part, we'll end up planning
  the rules separately. This will have an effect on the IR.

  p.q = 1
  p.r = 2

  Before, these would have been one function; now, it's two. As a result,
  in Wasm, some "object insertion" conflicts can become "var assignment
  conflicts", but that's in line with the now-new view of "multi-value"
  and "single-value" rules, not partial {set/obj} vs complete.
* planner: only check ref.GroundPrefix() for optimizations

In a previous commit, we've only mapped

    p.q.r[7]

as p.q.r;  and as such, also need to lookup the ref

    p.q.r[__local0__]

via p.q.r

(I think. Full disclosure: there might be edge cases here that are unaccounted
for, but right now, I'm aiming for making the existing tests green...)


New compiler stage:

In the compiler, we're having a new early rewriting step to ensure that the
RuleTree's keys are comparible. They're ast.Value, but some of them cause us
grief:

- ast.Object cannot be compared structurally; so

      _, ok := map[ast.Value]bool{ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")}): true}[ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")})]

  `ok` will never be true here.

- ast.Ref is a slice type, not hashable, so adding that to the RuleTree would
  cause a runtime panic:

      p[y.z] { y := input }

  is now rewritten to

    p[__local0__] { y := input; __local0__ := y.z }

This required moving the InitLocalVarGen stage up the chain, but as it's still
below ResolveRefs, we should be OK.

As a consequence, we've had to adapt `oracle` to cope with that rewriting:

1. The compiler rewrites rule head refs early because the rule tree expects
   only simple vars, no refs, in rule head refs. So `p[x.y]` becomes
   `p[local] { local = x.y }`
2. The oracle circles in on the node it's finding the definition for based
   on source location, and the logic for doing that depends on unaltered
   modules.

So here, (2.) is relaxed: the logic for building the lookup node stack can
now cope with generated statements that have been appended to the rule bodies.


There is a peculiarity about ref rules and extents:

See the added tests: having a ref rule implies that we get an empty object
in the full extent:

    package p
    foo.bar if false

makes the extent of data.p: {"foo": {}}

This is somewhat odd, but also follows from the behaviour we have right now
with empty modules:

    package p.foo
    bar if false

this also gives data.p the extent {"foo": {}}.

This could be worked around by recording, in the rule tree, when a node was
added because it's an intermediary with no values, but only children.

Signed-off-by: Stephan Renatus <stephan.renatus@gmail.com>

---
## [libguestfs/libnbd](https://github.com/libguestfs/libnbd)@[8699e7a6a3...](https://github.com/libguestfs/libnbd/commit/8699e7a6a3b96690d99058e737bc1820ea66598f)
#### Monday 2022-11-07 20:53:13 by Eric Blake

nbdsh: Allow -u interleaved with -c

Starting with a back-story: I wanted[1] to write:

$ nbdkit --tls=require --tls-psk=$dir/tests/keys.psk null --run \
 'nbdsh -u "nbds://alice@localhost/?tls-psk-file='"$dir"'/tests/keys.psk" \
   -c "h.get_size()"'

but it fails with the latest libnbd release, due to:

nbdsh: unable to connect to uri 'nbds://alice@localhost/?tls-psk-file=/home/eblake/libnbd/tests/keys.psk': nbd_connect_uri: local file access (tls-psk-file) is not allowed, call nbd_set_uri_allow_local_file to enable this: Operation not permitted

But without this patch, this obvious attempt at a fix doesn't work:

$ nbdkit --tls=require --tls-psk=$dir/tests/keys.psk null --run \
 'nbdsh -c "h.set_uri_allow_local_file(True)" \
   -u "nbds://alice@localhost/?tls-psk-file='"$dir"'/tests/keys.psk" \
   -c "h.get_size()"'

because nbdsh was performing h.connect_uri() prior to running any of
the -c strings, where the attempt to inject -c to match the hint from
the original error message is processed too late, even though it
occurred earlier in the command line.  The immediate workaround is
thus to spell out the URI with a manual -c:

$ nbdkit --tls=require --tls-psk=$dir/tests/keys.psk null --run \
 'nbdsh -c "h.set_uri_allow_local_file(True)" \
   -c "h.connect_uri(\"nbds://alice@localhost/?tls-psk-file='"$dir"'/tests/keys.psk\")" \
   -c "h.get_size()"'

which gets awkward because of the multiple layers of quoting required
(--run, -c, and Python each strip a layer).  But we can do better.
Instead of creating separate args.command and args.uri, we can use a
custom argparse Action subclass which will merge various command-line
options into a unified args.snippets.  Then with a little bit of
lambda magic, dispatching the various snippets in order looks fairly
easy.

I did have to drop one example() gated by args.uri in the help banner,
but it will be restored in improved form in the next patch.

test-error.sh and test-context.sh have to be updated to match our
saner processing order.  nbdkit's testsuite still passes even when
using this update to nbdsh, so I don't think programs in the wild were
relying on insane command-line rearranging.

[1] Actually, I wanted to use -U- and write -u "$uri" instead of -u
"nbds+unix...", but that involves teaching nbdkit how to display a
more-useful URI when TLS is in use.  Not this patch's problem.

Message-Id: <20221104211831.743339-3-eblake@redhat.com>
Acked-by: Richard W.M. Jones <rjones@redhat.com>

---
## [fmeum/bazel](https://github.com/fmeum/bazel)@[2232c5b445...](https://github.com/fmeum/bazel/commit/2232c5b445f5264b31b53a698f5f0e726d9be249)
#### Monday 2022-11-07 21:00:53 by Christopher Peterson Sauer

Move Boost into C++ Docs; Add Libraries Section

Hi wonderful Bazelers,

This is just a docs change.

Backstory: I'd been looking to make HTTPS requests across platforms from C++. A classic problem if there ever were one, networking being perhaps the most glaring omission in the C++ standard library. Thankfully, this is a problem Bazel can solve well, since most of the problem is the friction of using 3rd party libraries from C++. So, I spun up some build rules to make network requests easy, inspired by collaborating on the boost ones, and set off to add them to the docs.

Along the way, I noticed that the boost rules were in an odd spot: Listed at the language level alongside C++, rather than nested within C++. So I fixed that by nesting Boost inside, added Abseil, and then (hoping you'll forgive my hubris), I'd love to add the rules I just released, since I think they're a solution to a very real need. Perhaps rules for more famous, critical libraries can accumulate there over time, helping Bazel users get set up with the essential tools they need.

Thanks for your consideration!
Chris
(ex-Googler and author of [bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor), also in the docs.)

Closes #16621.

PiperOrigin-RevId: 486106928
Change-Id: I119ccff4f70e66415f8c6ac4930c975e48086bc2

---
## [iotku/tweets](https://github.com/iotku/tweets)@[9e9ce2ae87...](https://github.com/iotku/tweets/commit/9e9ce2ae871dcbfc0c9226625491d8e7a2e84536)
#### Monday 2022-11-07 21:11:50 by iotku

Hello Internet, Just leaving my mark on the least horrible social media service on the internet.
Indeed, hopefully some day I will become successful and this will be an interesting artifact.

I am soon entering my Junior year of college with an attempt to get a Computer Science degree
Hopefully I will not fail, but time will tell.
I am merely a mortal.

---
## [nfejzic/rust-clippy](https://github.com/nfejzic/rust-clippy)@[9e8f53d09a...](https://github.com/nfejzic/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Monday 2022-11-07 21:20:02 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [Ziiro/tgstation](https://github.com/Ziiro/tgstation)@[32c2e4ccd3...](https://github.com/Ziiro/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Monday 2022-11-07 22:04:48 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [avar/git](https://github.com/avar/git)@[d22fddf78a...](https://github.com/avar/git/commit/d22fddf78ad961aa4e2e523d99376006872efe05)
#### Monday 2022-11-07 23:40:21 by Ævar Arnfjörð Bjarmason

[TODO t0450] submodule: make it a built-in, remove git-submodule.sh

Replace the "git-submodule.sh" script with a built-in
"builtin/submodule.c. For" now this new command is only a dumb
dispatcher that uses run-command.c to invoke "git submodule--helper",
just as "git-submodule.sh" used to do.

This is obviously not ideal, and we should eventually follow-up and
merge the "builtin/submodule--helper.c" code into
"builtin/submodule.c". Doing it this way makes it easy to review that
this new C implementation isn't doing anything more clever than the
old shellscript implementation.

This is a large win for performance, we're now more than 4x as fast as
before in terms of the fixed cost of invoking any "git submodule"
command[1]:

	$ git hyperfine -L rev HEAD~1,HEAD -s 'make CFLAGS=-O3' './git --exec-path=$PWD submodule foreach "echo \$name"'
	Benchmark 1: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1
	  Time (mean ± σ):      42.2 ms ±   0.4 ms    [User: 34.9 ms, System: 9.1 ms]
	  Range (min … max):    41.3 ms …  43.2 ms    70 runs

	Benchmark 2: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD
	  Time (mean ± σ):       9.7 ms ±   0.1 ms    [User: 7.6 ms, System: 2.2 ms]
	  Range (min … max):     9.5 ms …  10.3 ms    282 runs

	Summary
	  './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD' ran
	    4.33 ± 0.07 times faster than './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1'

We're taking pains here to faithfully reproduce existing
"git-submodule.sh" behavior related to "--" handling, even when that
behavior is stupid. We'll fix in subsequent commits, but let's first
faithfully reproduce it.

One exception is the change in the behavior of the exit code
stand-alone "-h" and "--" yield, see the altered tests. Returning 129
instead of 0 and 1 for "-h" and "--" respectively is a concession to
basic sanity.

It would be better to use run_command() here directly to avoid copying
"args" and "env" copying, but let's use run_command_v_opt_cd_env()
instead to optimize for subsequent diff size. By using our own "struct
strvec args" we can push to "&args", not a "&cp.args". Eventually
we'll stop invoking "submodule--helper" as a sub-process, and avoid
the churn of converting all of "&cp.args" to "&args".

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---

