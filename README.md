## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-30](docs/good-messages/2022/2022-10-30.md)


1,782,446 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,782,446 were push events containing 2,485,290 commit messages that amount to 140,893,990 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[b2be252eb6...](https://github.com/Thunder12345/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Sunday 2022-10-30 00:58:39 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[14c96d05b8...](https://github.com/Comxy/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Sunday 2022-10-30 01:09:55 by scriptis

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[99b8d6b494...](https://github.com/Comxy/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Sunday 2022-10-30 01:09:55 by vincentiusvin

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
## [youniversityupc/app](https://github.com/youniversityupc/app)@[0e99947eb8...](https://github.com/youniversityupc/app/commit/0e99947eb8b84b03d397891a93c2d04672a8d29f)
#### Sunday 2022-10-30 01:15:49 by Diego Albitres

refactor: fixed AppBar tab rendering

OMG, this is finally working. I hate myself.

---
## [formsandlines/formform](https://github.com/formsandlines/formform)@[5d4ca564c9...](https://github.com/formsandlines/formform/commit/5d4ca564c955a8fc1e2177d4f410bb3fba6e8545)
#### Sunday 2022-10-30 01:22:24 by Peter Hofmann

Lots of changes accumulated over the last few days, this may be the longest
commit message ever…

Expression-local envs are now reified as “memory FORMs” (how I call them).
These are special FORMs (like unclear FORMs or formDNA) and I have written
extensively in my Roam notebook about their semantics, which can be explored
with the expander I wrote, but is not really useful without actually performing
the “memorization” process. To represent this process in FORMs would most
likely require re-entry FORMs, but there is a co-dependency here, since the
representation of re-entry FORMs was my prime motivation behind memory FORMs.
To be able to represent `f = (f)` in FORMs, without the help of an algebraic
meta-language, and to have it unfold in time as an emulation of a cognitive
process (which will be useful in some modules I plan for formform), requires
some concept of memory. But this is a property of the evaluator and hence
cannot be represented adequately in the memory FORM itself, which only acts as
an injunction such as “remember this!”. I am still researching about what this
is supposed to mean, but memory FORMs are valid FORMs in the sense that they
can be reduced and evaluated in a clear way that does not contradict any law
of the FORM calculus and they provide a simple representation for re-entry
FORMs and maybe even lambda expressions (kind-of crude though).

Without local envs, expressions are very simple now to the point that they are
merely container/context for FORMs. This is good, because local envs had a very
specific use-case which never really justified the overhead.

The reduction procedure itself has been improved in various ways, but most
importantly it now remembers observed values from previous contexts and uses
this information to remove or add redundant content justified by (de)generation
theorems in FORM logic. This means that an expression such as `(a (b a))` can
now be reduced to `(a (b))` which was not possible before. Unfortunately it
greatly expands the number of (possibly redundant) iterations and calls, since
the observed FORMs in a context might change after their reduction, which
causes the reducer to take another pass to try to further simplify the reduced
FORMs via its updated observations and this causes the contexts of those FORMs
to propagate the observations and so a small drop can make huge waves. I might
add an option to disable (de)generation inference if the performance decrease
is noticable, especially if the goal is calculation, not algebraic reduction.

I also started using flow-storm as a debugger, which is a great help to make
sense of those complex nested reductions.

Besides that, formDNA can now be simplified in reduction, if any of its
specified variables can be determined by a constant. There are still more steps
required to fully integrate formDNA into evaluation, but this is also very
useful for filtering formDNA in multiple ways.

Memory FORM can already be reduced, but need more simplification. Of course,
there is the potential for infinite reduction which I already experienced and
I am currently thinking about a way to catch the stack overflows from recursive
definitions, so that I can generate better error messages for users and prevent
crashes. This is however a very niece problem since most users would never
explicitly define self-contradicting re-entry FORMs or do so at their own risk.

I also started reduction for self-equivalent re-entry FORMs, which simply
requires reducing all contexts in a chain and then pattern-matching on the
reduced chain to match all possible species (if not already obsolete).

---
## [stevencaiOR/stevencaiOR.github.io](https://github.com/stevencaiOR/stevencaiOR.github.io)@[5c6d391138...](https://github.com/stevencaiOR/stevencaiOR.github.io/commit/5c6d3911383cf972e779a26c289f46961eca48a5)
#### Sunday 2022-10-30 01:47:44 by stevencaiOR

fixed dumbass circle in 'try out nitro' section of profile tabs AGAIN. Fuck you, Discord.

---
## [niyasraphy/odoo](https://github.com/niyasraphy/odoo)@[61270ee8bf...](https://github.com/niyasraphy/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Sunday 2022-10-30 01:56:38 by qsm-odoo

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

closes odoo/odoo#104193

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Kripacharya/conclusion-of-fomo-plugins](https://github.com/Kripacharya/conclusion-of-fomo-plugins)@[3099d356e7...](https://github.com/Kripacharya/conclusion-of-fomo-plugins/commit/3099d356e75676fdf82edd3cc485234f69ccd294)
#### Sunday 2022-10-30 04:56:29 by WeCodeFuture 2015

Create What are the limitations of the FOMO Plugin?

Introduction

The FOMO plugin is the perfect notification tool for individuals who want to stay updated on their favorite blogs and websites, but don't want to be inundated with notifications every time a new post is published. This plugin allows you to customize your notification settings so that you only receive notifications about posts that interest you, and it also sends you push notifications so that you can continue reading even if you're not currently online.


What is the FOMO Plugin?

The FOMO plugin is a notification tool that helps you stay organized and keep track of your notifications. It was designed to help you avoid missing important notifications, whether they're from your favorite apps or from important events in your life.



The FOMO plugin lets you customize the notifications you receive so that you only get the ones that are important to you. You can also set up alerts so that when a notification is received, you're automatically notified. This way, you'll never miss an important message again!



The FOMO plugin is available for both Android and iOS devices. You can download it from the Google Play Store or the App Store.


Does the FOMO Plugin work?

The FOMO plugin is a notification tool that allows users to be alerted when specific events happen. Events can be anything from new followers to tweets being sent. The plugin has proved to be hugely popular and is one of the most used plugins on the site.



One of the main benefits of using the FOMO plugin is that it allows people to stay up-to-date with what's happening around them without having to constantly check social media sites. This makes it ideal for people who don't have time to spare or who are afraid of being distracted.



Another great thing about the FOMO plugin is that it's very easy to use. Simply download the plugin and add your event sources (Twitter, Facebook, etc). Then, set up your notifications preferences and you're ready to go!



Overall, the FOMO plugin is an excellent notification tool that has proven to be extremely popular on site. It's easy to use and provides users with all the information they need without distraction.


What are the limitations of the FOMO Plugin?

The FOMO plugin is a notification tool that allows you to keep track of all the notifications that are sent to your account. The plugin has a lot of limitations, which are listed below: 



-You cannot filter notifications by type or sender. 

-You cannot add new notifications. 

-You cannot delete notifications. 

-The plugin has a limit of 5000 notifications.


Conclusion

If you're like most people, you probably check your phone dozens of times a day. But what happens when you can't help but check your phone even when you know it's not good for you? That's where the FOMO plugin comes in. This handy notification tool will help keep you on track by sending you notifications only when things are actually important. And because it's powered by Chrome, it works with any website or app — so there is no need to worry about compatibility issues. If you want to make sure that your phone doesn't become a distraction in your life, then make sure to add the FOMO plugin to your browser!

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[90f957d245...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/90f957d245dc9f5d98952f04bcb33aed79cdb06d)
#### Sunday 2022-10-30 04:56:31 by tanish2k09

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
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[3efa9b5382...](https://github.com/Bjarl/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Sunday 2022-10-30 04:58:06 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [GlodoUK/odoo](https://github.com/GlodoUK/odoo)@[e7c8fed8e3...](https://github.com/GlodoUK/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Sunday 2022-10-30 06:15:22 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

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

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[8990c654d1...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/8990c654d1fe60c9ba5ecaa33abe00036a33bbf0)
#### Sunday 2022-10-30 06:17:50 by Angelo G. Del Regno

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
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[85b2d5043d...](https://github.com/tgstation/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Sunday 2022-10-30 07:09:17 by LemonInTheDark

Optimizes qdel related things (slight init time savings) (#70729)

* Moves spawners and decals to a different init/delete scheme

Rather then fully creating and then immediately deleting these things,
we instead do the bare minimum.

This is faster, if in theory more fragile. We should be safe since any
errors should be caught in compile since this is very close to a
"static" action. It does mean these atoms cannot use signals, etc.

* Potentially saves init time, mostly cleans up a silly pattern

We use sleeps and INVOKE_ASYNC to ensure that handing back turfs doesn't
block a space reservation, but this by nature consumes up to the
threshold and a bit more of whatever working block we were in.

This is silly. Should just be a subsystem, so I made it one, with
support for awaiting its finish if you want to

* Optimizes garbage/proc/Queue slightly

Queue takes about 1.6 seconds to process 26k items right now.
The MASSIVE majority of this time is spent on using \ref
This is because \ref returns a string, and that string requires being
inserted into the global cache of strings we store

What I'm doing is caching the result of ANY \ref on the datum it's
applied to. This ensures previous uses will never decay from the string
tree.

This saves about 0.2 seconds of init

---
## [sevenrock/android_kernel_motorola_msm8998](https://github.com/sevenrock/android_kernel_motorola_msm8998)@[e503cc9d04...](https://github.com/sevenrock/android_kernel_motorola_msm8998/commit/e503cc9d0411083ac6a858dbefe0c88a9ef691ad)
#### Sunday 2022-10-30 08:19:59 by Christian Brauner

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
## [ilammy/themis](https://github.com/ilammy/themis)@[ad1092ebf5...](https://github.com/ilammy/themis/commit/ad1092ebf5b59f7d31a3f88da576d8db94d9d1ce)
#### Sunday 2022-10-30 10:30:40 by Oleksii Lozovskyi

fixup! soter: Prepare to export uncompressed keys

Oh my fucking god, fuck you clang-format.

---
## [McLogicmaster69/Ciphers](https://github.com/McLogicmaster69/Ciphers)@[b32b778d6e...](https://github.com/McLogicmaster69/Ciphers/commit/b32b778d6e9914046dc6a44efe4c4f0bc49e839a)
#### Sunday 2022-10-30 11:26:49 by Luftwaffle129

I luv bacon

Now baby come on (calling upon her baby, four words like beats in her heart)
Don't claim that love you never let me feel (Atmosphere and calls upons sensory imagery)
I shoulda known (She should of known)
'Cause you brought nothin' real (slang, shows how her english is broken just like her heart)
C'mon be a man about it you won't die (He is probably about to die and women being “femenist” are telling men to “be a man”)
I ain't got no more tears to cry and I can't take this no more (She has been crying for a while, sensory imagery)
You now I gotta let you go and you know (Sad atmosphere)
I'm outta love set me free and let me out this misery (She is outta love and needs to be set free)
Just show me the way to get my life again (i give up)
'Cause you can't handle me
Said I'm outta love can't you see
Baby that you gotta set me free, I'm outta love
Said how many times
Have I tried to turn this love around
But every time you just let me down
C'mon be a man about it you'll survive
I'm sure that you can work this out all right
Tell me yesterday did you know
I'd be the one to let you go and you know
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
Said I'm outta love can't you see
Baby that you gotta set me free, I'm outta love
Let me get over you
The way you gotten over me too
Seems like my time has come and now I'm movin' on
I'll be stronger
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
Said I'm outta love can't you see
Baby that you gotta set me free, I'm outta love
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
I'm outta love set me free

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[2a8ebba36a...](https://github.com/Nanu308/cmss13/commit/2a8ebba36a2c76ed855987dc107c9c385f6f16ea)
#### Sunday 2022-10-30 11:30:57 by Joelampost

Pred bug fix no.2 (#1287)

* a

a

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: harryob <me@harryob.live>

* Update yaut_procs.dm

* :>(

* fuck you

* return

* Update code/modules/cm_preds/yaut_procs.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [viniciusflv/docs](https://github.com/viniciusflv/docs)@[d2765e1bab...](https://github.com/viniciusflv/docs/commit/d2765e1bab77f0a5281e79c398551d085f448ee8)
#### Sunday 2022-10-30 13:16:53 by Vinicius Victorino

Fix pronouns in Portuguese for Katie Sylor-Miller

As you can see by her twitter account https://twitter.com/ksylor, she identifies as she/her. In Portuguese we have different names for male and female job descriptions, in this case arquitetO (male) and arquitetA (female).

---
## [newstools/2022-iol](https://github.com/newstools/2022-iol)@[af30312d84...](https://github.com/newstools/2022-iol/commit/af30312d8475688a8bdb20a1737e6f56bd415cdf)
#### Sunday 2022-10-30 16:46:12 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/mercury/news/man-handed-a-25-year-prison-term-for-killing-his-girlfriends-boss-in-pmb-after-he-refused-to-give-her-an-advance-on-her-wages-e0eab3a8-b042-490f-9818-fbfdb577b204]

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a01cd7a751...](https://github.com/treckstar/yolo-octo-hipster/commit/a01cd7a751cdb7ef8b8c25d5b2b4e1d979a9b3fd)
#### Sunday 2022-10-30 17:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [SaniaHL2/Sania_Foundation-19](https://github.com/SaniaHL2/Sania_Foundation-19)@[6bf6cdb77f...](https://github.com/SaniaHL2/Sania_Foundation-19/commit/6bf6cdb77f582598b90e63fa44a922fd033ae3d0)
#### Sunday 2022-10-30 18:48:18 by harry

fixes panic bunker adjacent shitcode (#769)

* ugly as hell

* idiot

* think before i commit (never)

---
## [PkmnDevs/pokemon-essentials](https://github.com/PkmnDevs/pokemon-essentials)@[731f95f608...](https://github.com/PkmnDevs/pokemon-essentials/commit/731f95f608e364da1ecd520ebfb02be4bc64a176)
#### Sunday 2022-10-30 18:51:24 by Ryan Semple

implemented most of Bens feedback

TODO:
✅ Add some normal trainers before the 2nd miniboss so that the player’s expectations of trainers isn’t set by running into two minibosses before anything else.
✅ Switch 2nd and Last trainers of route 2 youngster gauntlet.
✅ More healing items, fewer ether and revive.
✅ Lower Spidermaul’s exp a bit haha. Ben got 29k and went from lvl 21 to 33. (Maybe target it to get you to lvl 24 if you win? Enough to make Gym 1 winnable without ruining the whole game for you.) - (result after change: lvl 21 beldumgot 7k exp and went up to lvl 25. Lvl 35 infernerape got 4.5k exp and went up to lvl36. Lvl75 Charizard got 3k exp.)
✅ When gym 1 is too hard, you have to grind. Might as well make trainers in gym actually give exp, but only small amounts (using level cap).
✅ Ellinia Forest is “frustrating”. You can’t run from battles so if you get lost you’re just stuck battling a ton. Do I keep this as is in homage to the annoying caves from old pokemon games? Or do I remove some of the grass so there are fewer encounters? (probably the latter and we will see what other playtesters think).
✅ Add NPC next to gym that points player to the twins on the beach.
✅ Add water pokemon to ocean at the beach for Old Rod.
Maybe add another trainer at the beach and shino’s park too, just for something else to do there. *Would be cool to include NPCs that relate to whatever plot Ben is thinking of for this region.
✅ Make rival say something after you beat him so the player doesn’t think it is a bug.

---
## [ike709/OpenDream](https://github.com/ike709/OpenDream)@[00d56970e1...](https://github.com/ike709/OpenDream/commit/00d56970e117f0ad2e64075381bf6a0db3ddcdbe)
#### Sunday 2022-10-30 18:56:36 by Altoids1

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
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[8272749e8c...](https://github.com/david-rowley/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Sunday 2022-10-30 21:05:56 by Tom Lane

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
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[0cd78be6a1...](https://github.com/Jolly-66/JollyStation/commit/0cd78be6a19a9a3d6907cdf84759c59717dd8cb4)
#### Sunday 2022-10-30 21:14:11 by TaleStationBot

[MIRROR] [MDB IGNORE] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#2617)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[d34fa4c642...](https://github.com/RandomGamer123/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Sunday 2022-10-30 21:24:27 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [mRemoteNG/PuTTYNG](https://github.com/mRemoteNG/PuTTYNG)@[c19e7215dd...](https://github.com/mRemoteNG/PuTTYNG/commit/c19e7215ddd1d6a890fdb94d89bc5ccb46151363)
#### Sunday 2022-10-30 21:45:38 by Simon Tatham

Replace mkfiles.pl with a CMake build system.

This brings various concrete advantages over the previous system:

 - consistent support for out-of-tree builds on all platforms

 - more thorough support for Visual Studio IDE project files

 - support for Ninja-based builds, which is particularly useful on
   Windows where the alternative nmake has no parallel option

 - a really simple set of build instructions that work the same way on
   all the major platforms (look how much shorter README is!)

 - better decoupling of the project configuration from the toolchain
   configuration, so that my Windows cross-building doesn't need
   (much) special treatment in CMakeLists.txt

 - configure-time tests on Windows as well as Linux, so that a lot of
   ad-hoc #ifdefs second-guessing a particular feature's presence from
   the compiler version can now be replaced by tests of the feature
   itself

Also some longer-term software-engineering advantages:

 - other people have actually heard of CMake, so they'll be able to
   produce patches to the new build setup more easily

 - unlike the old mkfiles.pl, CMake is not my personal problem to
   maintain

 - most importantly, mkfiles.pl was just a horrible pile of
   unmaintainable cruft, which even I found it painful to make changes
   to or to use, and desperately needed throwing in the bin. I've
   already thrown away all the variants of it I had in other projects
   of mine, and was only delaying this one so we could make the 0.75
   release branch first.

This change comes with a noticeable build-level restructuring. The
previous Recipe worked by compiling every object file exactly once,
and then making each executable by linking a precisely specified
subset of the same object files. But in CMake, that's not the natural
way to work - if you write the obvious command that puts the same
source file into two executable targets, CMake generates a makefile
that compiles it once per target. That can be an advantage, because it
gives you the freedom to compile it differently in each case (e.g.
with a #define telling it which program it's part of). But in a
project that has many executable targets and had carefully contrived
to _never_ need to build any module more than once, all it does is
bloat the build time pointlessly!

To avoid slowing down the build by a large factor, I've put most of
the modules of the code base into a collection of static libraries
organised vaguely thematically (SSH, other backends, crypto, network,
...). That means all those modules can still be compiled just once
each, because once each library is built it's reused unchanged for all
the executable targets.

One upside of this library-based structure is that now I don't have to
manually specify exactly which objects go into which programs any more
- it's enough to specify which libraries are needed, and the linker
will figure out the fine detail automatically. So there's less
maintenance to do in CMakeLists.txt when the source code changes.

But that reorganisation also adds fragility, because of the trad Unix
linker semantics of walking along the library list once each, so that
cyclic references between your libraries will provoke link errors. The
current setup builds successfully, but I suspect it only just manages
it.

(In particular, I've found that MinGW is the most finicky on this
score of the Windows compilers I've tried building with. So I've
included a MinGW test build in the new-look Buildscr, because
otherwise I think there'd be a significant risk of introducing
MinGW-only build failures due to library search order, which wasn't a
risk in the previous library-free build organisation.)

In the longer term I hope to be able to reduce the risk of that, via
gradual reorganisation (in particular, breaking up too-monolithic
modules, to reduce the risk of knock-on references when you included a
module for function A and it also contains function B with an
unsatisfied dependency you didn't really need). Ideally I want to
reach a state in which the libraries all have sensibly described
purposes, a clearly documented (partial) order in which they're
permitted to depend on each other, and a specification of what stubs
you have to put where if you're leaving one of them out (e.g.
nocrypto) and what callbacks you have to define in your non-library
objects to satisfy dependencies from things low in the stack (e.g.
out_of_memory()).

One thing that's gone completely missing in this migration,
unfortunately, is the unfinished MacOS port linked against Quartz GTK.
That's because it turned out that I can't currently build it myself,
on my own Mac: my previous installation of GTK had bit-rotted as a
side effect of an Xcode upgrade, and I haven't yet been able to
persuade jhbuild to make me a new one. So I can't even build the MacOS
port with the _old_ makefiles, and hence, I have no way of checking
that the new ones also work. I hope to bring that port back to life at
some point, but I don't want it to block the rest of this change.

---
## [JoschiGrey/chummer5a](https://github.com/JoschiGrey/chummer5a)@[85dc0f8354...](https://github.com/JoschiGrey/chummer5a/commit/85dc0f8354083947e63cb021d7b20d7a88af6dbc)
#### Sunday 2022-10-30 22:49:16 by Teksura

Toxic and mutant critters (#4899)

* Adding Kokoro Cobra

I mean it mostly works. I feel it's kinda bullshit that the natural weapon doesn't work but that's a later problem

* Update critters.xml

fuck

* Update critters.xml

Adds Pandamonium and Montauk

* Update critters.xml

Added the last of the Critters

* Delete .DS_Store

This file should have been ignored

---
## [rohanmclure/linux-ci](https://github.com/rohanmclure/linux-ci)@[d21f4b7ffc...](https://github.com/rohanmclure/linux-ci/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Sunday 2022-10-30 22:52:32 by Douglas Anderson

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[ca2114f0f5...](https://github.com/cmss13-devs/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Sunday 2022-10-30 23:39:00 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---

