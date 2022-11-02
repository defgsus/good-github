## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-01](docs/good-messages/2022/2022-11-01.md)


2,248,262 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,248,262 were push events containing 3,407,018 commit messages that amount to 262,651,711 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [SpaceManiac/OpenDream](https://github.com/SpaceManiac/OpenDream)@[00d56970e1...](https://github.com/SpaceManiac/OpenDream/commit/00d56970e117f0ad2e64075381bf6a0db3ddcdbe)
#### Tuesday 2022-11-01 00:07:15 by Altoids1

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
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[029a331a06...](https://github.com/tabulon-ext/inxi/commit/029a331a06d5ffc737d75a87315e50d6cb3d80e1)
#### Tuesday 2022-11-01 00:17:28 by Harald Hope

This release fixes another very long standing bug, which I was not sure was an
inxi or a Konversation bug, which made tracking it down very difficult. Special
thanks to argonel of Konversation for helping solve this problem, or at least,
for directing my attention towards the likely cause area, and away from wrong
ideas. The bug was that inxi simply did not run in Konversation, it would exit
with error when run with /cmd or /inxi via symbolic links.

This may not seem like a huge deal to many of you, but the actual history of
inxi was directly linked to user support in mainly Konversation, so this feature
not working I have alwyas found extremely annoying, but I could never figure out
why it wasn't workiing, and didn't really know where to start until Argonel
helped narrow it down to a specific Konversation function in inxi. At which
point tracking down the real bug was fairly easy. Since testing in IRC is always
a key test point for inxi features and releases, not working in my main GUI IRC
client forced me to use CLI clients like irssi, via /exec -o inxi.

There was a secondary cause of failure, which was missing a key qdbus package,
which made figuring this one out a two step process.

So inxi is once again working in all areas, with no known significant failure
areas beyond known issues that have no current solution, or which I don't feel
like doing.

But possibly more important, a goal I have had for a while now of doing long
needed code refactors, bug fixes, without huge new code blocks or features
adding new future fixes and bugs, has been slowly happening.

This was quite important, because inxi's codebase and logic is so complex and
large now that at some point, it required rest and cleanup and corrections,
without continuously adding new code and logic, which would then trigger new
fixes and bugs. In other words, the code is taking a long needed, and well
deserved, breather, to recover after huge increases in the overall LOC and
feature sets.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. No known way to detect that the system might be Wayland for the Graphics:..
API: fixes, unless Xwayland is installed if the wayland protocol detections
failed, which they often do in console. Not practical to look for all compositor
variants on system to determine if it could be Wayland if not X or Xvesa, so
that one will just be what it is, which is fine, definitely better than it was
before. Note this is only an issue if in Console, no Display. Note that if inxi
is run as root, Wayland data also usually fails, even in Display.

--------------------------------------------------------------------------------
BUGS:

1. Another corner case monitor position issue, applied fallback primary monitor
rule when a primary monitor had already been located. This is corrected via a
graphics global $b_primary which once set will disable this fallback feature.
Objectively, the fallback feature should just be removed. The test is if that
monitor is not primary, and if position is 0x0, then assume primary, without
verifying no primary had been located yet.

2. A super old bug, in current konversation, was failing to trip the konvi
detections, which then resulted in not stripping off the first two args in
@ARGV, which then resulted in bad args being passed to inxi on konvi start,
which then resulted in silent failing. Many thanks to argonel of #konversation
for the patience to help me figure out what was going on with this bug. He's
been a Konversation developer probably longer than I've been doing inxi.

Cause was very tricky and subtle, the ps aux path for konvi had changed
slightly, not the path, but the pattern, it used to be:

konversation -session [sessin id]
but it's changed to:
konversation -qwindowtitle Konversation
or just plain:
konversation as line ending.

This led to failure to find konvi running, which then made the konvi ids fail.

Also, this would not work if the qdbus-qt5 package was not installed, or other
distros might have that packaged differently. Because of these dual causes, I
was simply unable to figure out what was going on for many years. I suspect this
stopped working with KDE 5/QT 5, but I'm not sure.

3. Used wrong key names for some ZFS tests and fallbacks, those could have led
to failures though very difficult to test and verify this. Also see fix 5, which
of course also looks like a bug, acts like one, but was actually due to a new
use of /dev/disk/by-partuuid for ZFS components in Ubuntu which inxi had not
seen before.

--------------------------------------------------------------------------------
FIXES:

1. Alternate ps IDs for appimage detection (try appimagelauncher), alternate
paths for possible appimage storage locations (also try ~/.appimage/*). File
names might be *.appimage or *.AppImage, probably other variants too.

2. Going along with Change 1, made tests more granular for missing graphics API
type data. Also updated messages to be more correct and clear, in and out of
display. This corrects an issue I'd seen but never resolved, which was on
headless systems showing this message:

Message: GL data unavailable in console. Try -G --display

Now the tests are far more granular, and only show that if glxinfo is installed,
and also shows specific messages if glxinfo not installed, but X/Xorg present,
or, for Wayland, if Xwayland present. These all get their own specific messages
now, and generally will also show which API is being used, or API: N/A if
nothing is detected, as in the case of a headless system with no X, Wayland,
etc.

3. Github issue #275 on of all things Microsoft WSL environment, has a small
glitch with undefined display hz, but otherwise inxi seems to work in that
environment, albeit missing many data types!

4. Made tests for konversation more robust, including test for
$ENV{'PYTHONPATH'} containing konversation in path, which I believe will work
for all new Konversations (KDE 5 and newer), and be much faster. The previous
tests are now more robust and less prone to failure, and only activate when
PYTHONPATH is not present with konversation string present as well.

5. Fix for ZFS using /dev/disk/by-partuuid for partition id in zfs,
which can lead to wrong usable disk total size report, along with failure
to show components. Thanks delanym, issue #276 for reporting this problem, which
also exposed some harder to trigger bugs in ZFS (Bug 3).

6. Exposed by issue #276, case where line was wrapping value when value was too
short visually to value: used: 34.4 GiB (4.5%) due to the 3 or more words
trigger to enable wrapping of value, but noticed that if length of line was
exactly max-width, not > or <, it might vanish.

7. Case where no X or GPU drivers found, but dri driver detected, was not
showing, now does.

8. OpenRC is the init system in some cases, that is: readlink /sbin/init >
/sbin/openrc-init, where /proc/1/comm == init. Was showing only as OpenRC rc
type, which wasn't actually correct.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. New nvidia gpu product ids for Turing, Ampere, Lovelace, Hopper. New Intel
GPU ids.

2. Added Zinc to systembase/distro, needs slightly special handling to get both
names right. Also added Tuxedo, which could use existing methods.

3. Added dpkg tool nala, which is sort of a CLI front end for apt, zinc uses it,
but it's also in Debian main package pool. Also deb-get, which is another zinc
thing for package management.

4. Full support for dinit: version, dinitctl w/status in ServiceData

4. Added initial support for init systems: 31init (31 line C program, no
--version), Hummingbird (unknown if -v/--version).

5. A few new CPU arch ids (new Intels).

--------------------------------------------------------------------------------
CHANGES:

1. Going somewhat along with the change in Audio to call ALSA a Sound API
instead of a sound server, changed key name OpenGL: to API: OpenGL in Graphics.
Also for EGL wayland, calling that the api too.

https://en.wikipedia.org/wiki/OpenGL

This conforms more closely to how these things are defined. Note that once
again, a value had been used as a key name, which almost always indicates a
failure to understand something about the core tech.

2. Changed wrapping of values from 3 words or more to 3 or more words AND length
> 24 characters. Saw example of:
 .... used: 28.45 GiB
  (4.5%)

which isn't desirable.

3. Changed minimum wrap to 60 columns, the new wrapper features are working so
well that if users want output that short, it will usually work fine, except of
course for very long word strings like a kernel name or parameter.

Note that this does not truncate long 'words' that might be wrapped, or going
along with Change 2, long 'sentences' of 2 words, those will always appear on
the same line regardless. For 'sentences' of 3 or more words, however, it goes
word by word, so it could well wrap after the first word, and so on. Obviously,
a 24 or fewer character value will never be wrapped, which was the intended
correction of change 2.

4. Going with Fix 8, OpenRc is an init system when it owns /proc/1/comm, had not
realized that /proc/1/comm == init can map to dinit, openrc as init. Now will
only show OpenRc as rc: type if not init as well.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Updates in man for Change 1.

2. Added to docs/inxi-graphics.txt good quote re EGL/GBM, as well as VBE/GOP for
vesa. Trying to find docs where they actually say clearly it's an API is
remarkably difficult.

3. Man page, added note about Konversation requiring qdbus-qt5 (Debian+),
qt5-qttool (RHEL+/SUSE+), qt-tools (Arch+) for inxi to work inside it. Also
updated smxi.org/docs/inxi-usage.txt to note requirements for Konversation use
and setup.

4. Man, help, changed min width for -y/--width from 80 to 60.

5. docs/inxi-values.txt updated for --cygwin, --wsl fake OS type switches. Not
technically the OS, more the environment, but close enough.

6. docs/inxi-init.txt updated for new init types.

--------------------------------------------------------------------------------
CODE:

1. Refactored tools/gpu_ids.pl to correct and enhance some features.

2. Renamed functions and sections to better reflect that the display interface
is an API, this makes stuff less odd internally, and makes the function/variable
names correspond better to what the stuff really is.

3. Commented out kde konversation data source config collector, that logic looks
like it never worked, and couldn't work, since it never actually located
inxi.conf files, just paths to the data directories.

4. Expanded release.pl to handle acxi docs as well, makes it all consistent and
a lot easier to do long term.

5. Fake --wsl WSL switch, not really used, but in case.

6. Changed $b_cygwin to $windows{'cygwin'} and added $windows{'wsl'}.

7. Added -WSL to debugger string generator once WSL type is detected.

8. Refactored init, runlevel functions get_init_data() (now InitData::get()),
get_runlevel_data() (now InitData::get_runlevel()), get_runlevel_default() (now
InitData::get_runlevel_default()) into one package/class: InitData. This should
have been done a long time ago, to follow the general rule "if > 1 functions for
a tool refactor it into a class/package" for when to create a package/class
internally.

9. Completed gpu_ids.pl, now outputs the full hash set per item, so entire
blocks can be copied/pasted over. Something of a pain to get comments included,
which aren't strictly necessary in pinxi itself, but they do help read the
hashes for gpu data.

---
## [ongood/odoo](https://github.com/ongood/odoo)@[61270ee8bf...](https://github.com/ongood/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Tuesday 2022-11-01 00:30:46 by qsm-odoo

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
## [ongood/odoo](https://github.com/ongood/odoo)@[e7c8fed8e3...](https://github.com/ongood/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Tuesday 2022-11-01 00:30:58 by qsm-odoo

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
## [Stealth-Robotics/2022-Stealth-FTC](https://github.com/Stealth-Robotics/2022-Stealth-FTC)@[1dda012029...](https://github.com/Stealth-Robotics/2022-Stealth-FTC/commit/1dda0120297af9f17df67344d4737d9cc082c7a8)
#### Tuesday 2022-11-01 00:38:30 by Clementine Allen

i hate my life, big mango, boom orange juice thats life

---
## [lightrix/terminal](https://github.com/lightrix/terminal)@[1374396f10...](https://github.com/lightrix/terminal/commit/1374396f1022dfef13f8f65bcb0cb75dc64924c1)
#### Tuesday 2022-11-01 00:48:27 by Michael Niksa

Delay load call SetThreadDescription to restore WPF renderer on Win7 (#10582)

Delay load call SetThreadDescription to restore WPF renderer on Win7

## PR Checklist
* [x] Closes something @DHowett asked me to do.
* [x] I work here
* [x] I F5'd it on a version with this function and it still works


## Detailed Description of the Pull Request / Additional comments

I keep forgetting that anything in the WPF control needs to keep working on Win7. Or more specifically... I remember this fact for the DX renderer, but not for the render thread base. Oops. Turns out this particular convenience method to set thread descriptions for visibility inside the debugger (to make my life easier) only works down to 1607 (see https://docs.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreaddescription). Since it's just a debugging convenience... skipping it entirely when the procedure is not found should be fine. Also I don't try to load `kernel32.dll` and just get the handle of the existing module (which per the remarks at https://docs.microsoft.com/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlew will not increment the module reference count) because `kernel32.dll` pretty much has to be there or we're already in hot water.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[83c75cac2c...](https://github.com/TheBoondock/tgstation/commit/83c75cac2c632a51eb8252b2d93b0cf0faa0a9ee)
#### Tuesday 2022-11-01 01:22:37 by Jacquerel

Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)



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

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[cddf3e175b...](https://github.com/lgritz/oiio/commit/cddf3e175b36bac87640741eda39c64a6b4134ca)
#### Tuesday 2022-11-01 01:25:46 by Aras Pranckevičius

DDS: alpha/luminance format fixes, add & enable more tests (#3581)

* DDS: fixes for A8, L8, A8L8 formats

While developing #3573 at one time I had them working properly, but then
while fixing the address sanitizer failure for 3-channel formats I
botched them again. Note to self: never again do a "yeah I'll add tests
later", since if I had all of them running all the time this would
not have happened. :facepalm:

* DDS: extend test coverage for more formats & channel size cases

With more test images recently added (https://github.com/OpenImageIO/oiio/pull/3459),
start using them for DDS tests. This covers now:
- Alpha, Luminance and Alpha+Luminance formats,
- RGB formats with rarer channel sizes (rgb10 a2, r3g3b2),
- Several "broken" DDS file cases
- Removed usage of sample-DXT1 since it is well covered by others.

---
## [DAKKA-WAAAGH/tgstation](https://github.com/DAKKA-WAAAGH/tgstation)@[d45e244401...](https://github.com/DAKKA-WAAAGH/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Tuesday 2022-11-01 02:00:37 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [DAKKA-WAAAGH/tgstation](https://github.com/DAKKA-WAAAGH/tgstation)@[223e8bfd96...](https://github.com/DAKKA-WAAAGH/tgstation/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Tuesday 2022-11-01 02:00:37 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[db83f6498d...](https://github.com/Hatterhat/tgstation/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Tuesday 2022-11-01 02:39:20 by vincentiusvin

Simplifies SM damage calculation, tweaks the numbers. (#70347)


About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

---
## [ralacerda/docs](https://github.com/ralacerda/docs)@[6b97aae394...](https://github.com/ralacerda/docs/commit/6b97aae394f0cd6dff5b73809d0d1d248c62ee91)
#### Tuesday 2022-11-01 03:27:49 by Vinicius Victorino

Fix pronouns in Portuguese for Katie Sylor-Miller (#1955)

As you can see by her twitter account https://twitter.com/ksylor, she identifies as she/her. In Portuguese we have different names for male and female job descriptions, in this case arquitetO (male) and arquitetA (female).

Co-authored-by: Yan Thomas <61414485+Yan-Thomas@users.noreply.github.com>

---
## [CorvaxStation/Skyrat-tg](https://github.com/CorvaxStation/Skyrat-tg)@[74586e2091...](https://github.com/CorvaxStation/Skyrat-tg/commit/74586e2091b0793b4eca713eff890a76afbd3c89)
#### Tuesday 2022-11-01 04:40:26 by SkyratBot

[MIRROR] Upgrades the Modsuit Adapter Shell [MDB IGNORE] (#16669)

* Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

* Upgrades the Modsuit Adapter Shell

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[55e5c5be67...](https://github.com/tgstation/tgstation/commit/55e5c5be679f37093e8e60f1f6bdfc4030aba4a6)
#### Tuesday 2022-11-01 05:05:23 by Striders13

Clowns will now always like bananas. (#70919)



## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog


:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

---
## [Ussiabuu/Ussiabuu](https://github.com/Ussiabuu/Ussiabuu)@[485880bf3c...](https://github.com/Ussiabuu/Ussiabuu/commit/485880bf3ca111d604ec504c4d80131f13ae8045)
#### Tuesday 2022-11-01 05:22:14 by Ussi Abuu

Change the world with tangible actions

INTRODUCTION

We are human beings, We work to deliver human development for all. humanity has been one of the most rewarding experiences of our life, we want to contribute to people's wellbeing and provide them with a better life, peace, human rights, and humanitarian efforts that are needed more than ever within Ukraine, Afghanistan, Yemen, Mexico, Syria, Haiti, Algeria, Iraq, DR Congo, South Sudan, Ethiopia and Sudan. Together we have power of our demands, peace and harmony are the foundation of human development.

Kyiv is the capital city of Ukraine. Ukraine is a country in Eastern Europe. Ukraine borders the Russian Federation to the east and North-East, Belarus to the North-West, Poland, Slovakia and Hungary to the West, Romania and Moldova to the South-West, and the Black Sea and Sea of Azov to the South and Southeast. Ukraine has a mostly temperate continental climate, although the southern Crimean coast has a humid subtropical climate. large nation that has a large amount of equipment and missiles starts a war and invades Ukraine due to a misunderstanding, according to President of Ukraine Volodymyr Zelensky said he doesn't consider diplomacy with Russia possible under the current conditions.

WHAT DO BELIEVE?

There is 8 billion people on the planet who is like planet to be health and wasteless, together and in solidarity we making possible for Kyiv to be safe, greener, cleaner in true harmony while many people think is now impossible. War is waste and is the main reason for the violation of human rights. We must stand stronger together and in solidarity to build a wasteless world in all form, together we have power of our demands, we need sustainable peace around the world, we need the health of our cities, we need the health of our nature, we need the health of our planet, we need the health of our people too! let's go together in harmony!

ONE ACTION AT A TIME WE CAN CHANGE THE KYIV?

The 2030 Agenda is an action plan for prosperity, planet and people too, implemented through the Sustainable Development Goals (SDGs). More and more of us are becoming aware of the need for sustainable peace and harmony. Of course we need resources and we need inclusions, inclusions from different voice, groups, indigenous people and community, together we was raise the Sustainable Development Goals flag but together we have power to build the map of Sustainable Development Goals (SDGs) in every corner of the world.

OUR MESSAGE?

Human development can not happen without dedicated environmental sustainability, building sustainable peace and equitable development. There is nothing more important than human dignity and no one has right to violate it. 

Diversity, inclusion, justice, equity and Open Data can help improve smart cities and urban infrastructure. It can also improve disaster resilience and ensure that critical resources are deployed effectively in an emergency. 

United People and INDUSTRY 5.0 remains on the front lines to build WasteLess world by systematic waste prevention and responding to conflicts and human rights violations. We believe war is waste so there will be no waste if we don't create waste, let's go together to build a new Kyiv in true harmony with the ecosystem of which we too are an important part

---
## [DisturbHerb/goonstation](https://github.com/DisturbHerb/goonstation)@[693f38836f...](https://github.com/DisturbHerb/goonstation/commit/693f38836f362b8083c1d0169c7e5c17196852f1)
#### Tuesday 2022-11-01 08:18:49 by aloe

why do you set vis_flags if you aren't going to use vis_contents fuck you

---
## [wegtam/metals](https://github.com/wegtam/metals)@[6fca4bc1b2...](https://github.com/wegtam/metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Tuesday 2022-11-01 09:59:28 by ckipp01

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
## [Empire-Strikes-Back/Dawes](https://github.com/Empire-Strikes-Back/Dawes)@[58a3129731...](https://github.com/Empire-Strikes-Back/Dawes/commit/58a3129731bc305b5d4ed52185c00cd4f7813792)
#### Tuesday 2022-11-01 11:35:54 by Dawes

wake up, Claire! Jim's dead! they're all dead!

like Durant wasted his talents deceived by wealth - so did I want all the kingdoms of the world

unlike Rich Roll before he died - I didn't even try to keep it simple

I am too big to listen to Jesus - all that about weeds, least, tower, two masters

let my identity as Money-serving program remain
like Krieger - try any slight of hand with my money and I'll cut your throat
let me be vegan - clojure, because I never had any source in the first place
let me wear clothes of the enemy of the garden - project.clj

:Jeremy-Clarkson my guest tonight is star of this and that, Shrek, Mask - and she brought her co-star with her - Cameron Diaz and Tom Cruise!

---
## [sailfishos-mirror/glib](https://github.com/sailfishos-mirror/glib)@[b8e1ecdd6b...](https://github.com/sailfishos-mirror/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Tuesday 2022-11-01 12:23:20 by Michael Catanzaro

Automatically disable cast checks when building with optimization

Cast checks are slow. We seem to have some rough consensus that they are
important for debug builds, but not for release builds. Problem is, very
few apps define G_DISABLE_CAST_CHECKS for release builds. Worse, it's
undocumented, so there's no way apps could even be expected to know
about it.

We can get the right default is almost all situations by making this
depend on the __OPTIMIZE__ preprocessor definition. This is a GCC-specific
thing, although Clang supports it too. If the compiler does not define
__OPTIMIZE__, then this commit does no harm: you can still use
G_DISABLE_CAST_CHECKS as before. When checking __OPTIMIZE__, we are
supposed to ensure our code has the same behavior as it would if we do
not, which will be true except in case the check fails (which is
programmer error).

Downside: this will not automatically do the right thing with -Og,
because __OPTIMIZE__ is always defined to 1. We don't want to disable
cast checks automatically if using -O0 or -Og. There's no way to
automatically fix this, but we can create an escape hatch by allowing
you to define G_DISABLE_CAST_CHECKS=0 to force-enable cast checks. In
practice, I don't think this matters much because -Og kinda failed:
GCC's man page says it should be a superior debugging experience to -O0,
but it optimizes variables away so it's definitely not.

Another downside: this is bad if you really *do* want cast checks in
release builds. The same solution applies: define
G_DISABLE_CAST_CHECKS=0 and you'll get your cast checks.

---
## [Colorfingers/overte](https://github.com/Colorfingers/overte)@[4a49631007...](https://github.com/Colorfingers/overte/commit/4a49631007af4a471acf179d9a7a4bca19ea6afa)
#### Tuesday 2022-11-01 12:44:36 by Alezia Kurdis

Added HMD notifications dismissal

Added a gestural way to dismiss the notifications in HMD.

The notifications vanishes after 10 sec. 
But if for any reason we want to accelerate the process (mostly because it hide the view or it is going to appears in photo capture)
In Desktop we can simply click on the notification to get rid of them.
But in HMD, clicking was kinda a pain (assuming the if you want to dismiss the notification is often because they are already annoying you)
have to aim and click is like pressing a button using a fishing pole, it's certainly adding more annoyance to this.
To addressed that, I introduced the "Whoosh!": An easy gesture to dismiss any 3d UI, by simply move one of you controller over you eyes height. (a bit like making flee an annoying fly.)

---
## [c410-f3r/rust-clippy](https://github.com/c410-f3r/rust-clippy)@[9e8f53d09a...](https://github.com/c410-f3r/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Tuesday 2022-11-01 13:26:55 by bors

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
## [sfan5/mpv](https://github.com/sfan5/mpv)@[6f7506b660...](https://github.com/sfan5/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Tuesday 2022-11-01 13:46:31 by Philip Langdale

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
## [Reco201/Skyrat-tg](https://github.com/Reco201/Skyrat-tg)@[bbaefcefeb...](https://github.com/Reco201/Skyrat-tg/commit/bbaefcefebf4200cf30456cfdb3cbfdb30af6c49)
#### Tuesday 2022-11-01 15:18:02 by SkyratBot

[MIRROR] UpdatePaths Readme - Reforged [MDB IGNORE] (#17204)

* UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

* UpdatePaths Readme - Reforged

Co-authored-by: san7890 <the@san7890.com>

---
## [xubby/aed-project1](https://github.com/xubby/aed-project1)@[2d28f29e09...](https://github.com/xubby/aed-project1/commit/2d28f29e09af6f786b2b40cc9fc0d412e1c81ab9)
#### Tuesday 2022-11-01 15:18:05 by ZeAntonioM

pain ahhhhhhhhhhhhhh i want to kill me, merge confilcts are fucking painfull

---
## [balarabetahir/TAHIR-PYTHON-365](https://github.com/balarabetahir/TAHIR-PYTHON-365)@[98593bdd32...](https://github.com/balarabetahir/TAHIR-PYTHON-365/commit/98593bdd3243b253ef6394e0fcf43aee3c7b71c9)
#### Tuesday 2022-11-01 16:49:34 by Abubakar Tahir Balarabe

Day 146 Age Calculator using Python

Age Calculator is an amazing coding project idea for beginners. If you are new to any programming language, you should try making an age calculator. It is an application where a user enters his date of birth as an input, and the application gives his age as an output. So, if you want to learn how to make an age calculator using the Python programming language, this article is for you. I will introduce you to a tutorial on how to create an age calculator using Python.

Age Calculator using Python
Age Calculator is an amazing application to create as a beginner in any programming language. To create an age calculator, you need two dates:

today’s date
date of birth
You can either ask the user for both dates or just ask for the date of birth and use today’s date from the computer itself. Asking for the birthday only seems like a more user-friendly option. So here’s how to create an age calculator using Python:

In the above code:

I have first defined a Python function where I am asking for three user inputs:
y: year of birth 
m: month of birth 
d: date of birth
Then I am importing the datetime module in Python inside the function
Then in the next line, I am taking today’s date by using the datetime.now() method of the datetime module
Then I have introduced a new variable in the next line as dob, where I am using the date of birth as the input given by the user
Then I am subtracting the dob with today’s date and then dividing it by 365.25 which is returning the age of the user.

Summary
Age Calculator is an amazing coding project idea for beginners. It is an application where a user enters his date of birth as an input, and the application gives his age as an output. I hope you liked this article on how to create an age calculator using Python. Feel free to ask your valuable questions in the comments section below.

---
## [alexvorxx/Zink-Mesa-Xlib](https://github.com/alexvorxx/Zink-Mesa-Xlib)@[3a9cdd780d...](https://github.com/alexvorxx/Zink-Mesa-Xlib/commit/3a9cdd780de28deeda45600fb5b8b134d91d17f2)
#### Tuesday 2022-11-01 17:07:31 by Alyssa Rosenzweig

panfrost/ci: Disable trace-based testing

Trace-based testing has not worked for Panfrost. It was a neat
experiment, and I'm glad we tried it, but the results have been mostly
negative for the driver. Disable the trace-based tests.

For testing that specific API features work correctly, we run the
conformance tests (dEQP), which are thorough for OpenGL ES. For big GL
features, we run Piglit, and if there are big GL features that we are
not testing adequately, we should extend Piglit for these. For
fine-grained driver correctness, we are already covered.

Where trace-based testing can fit in is as a smoke test, ensuring that
the overall rendering of complex scenes does not regress. In principle,
that's a lovely idea, but the current implementation has not worked out
for Panfrost thus far. The crux of the issue is that the trace based
tests are based on checksums, not fuzzy-compared reference images. That
requires updating checksums any time rendering changes. However, a
rendering change to a trace is NOT a regression. The behaviour of OpenGL
is specified very loosely. For a given trace, there are many different
valid checksums. That means that correct changes to core code frequently
fail CI after running through the rest of CI, only because a checksum
changed in a still correct way. That's a pain to deal with, exacerbated
by rebase pains, and provides negative value to the project. Some recent
examples of this I've hit in the past two weeks alone:

   panfrost: Enable rendering to 16-bit and 32-bit
   4b49241f7d7 ("panfrost: Use proper formats for pntc varying")
   ac2964dfbd1 ("nir: Be smarter fusing ffma")

The last example were virgl traces, but were especially bad: due to a
rebase fail, I had to update traces /twice/, wasting two full runs of
pre-merge CI across *all* hardware. This was extremely wasteful.

The value of trace-based testing is as a smoke test to check that traces
still render correctly. That is useful, but it turns out that checksums
are the wrong way to go about it. A better implementation would be
storing only a single reference image from a software rasterizer per
trace. No driver-specific references would be stored. That reference
image must never change, provided the trace never changes. CI would then
check rendered results against that image with tolerant fuzzy
comparisons. That tolerance matches with the fuzzy comparison that the
human eye would do when investigating a checksum change anyway. Yes, the
image comparison JavaScript will now report that
0 pixels changed within the tolerance, but there's nothing a human eye
can do with that information other than an error prone copypaste of new
checksums back in the yaml file and kicking it back to CI, itself a
waste of time.

Finally, in the time we've had trace-based testing alongside the
conformance tests, I cannot remember a single actual regression in one
of my commits the trace jobs have identified that the conformance tests
have not also identified. By contrast, the conformance test coverage has
prevented the merge of a number of actual regressions, with very few
flakes or xfail changes, and I am grateful we have that coverage. That
means the value added from the trace jobs is close to zero, while the
above checksum issues means that the cost is tremendous, even ignoring
the physical cost of the extra CI jobs.

If you work on trace-based testing and would like to understand how it
could adapted to be useful for Panfrost, see my recommendations above.
If you work on CI in general and would like to improve Panfrost's CI
coverage, what we need right now is not trace-based testing, it's
GLES3.1 conformance runs on MediaTek MT8192 or MT8195. That hardware is
already in the Collabora LAVA lab, but it's not being used for Mesa CI
as the required kernel patches haven't made their way to mainline yet
and nobody has cherry-picked them to the gfx-ci kernel. If you are a
Collaboran and interested in improving Panfrost CI, please ping
AngeloGioacchino for information on which specific patches need to be
backported or cherry-picked to our gfx-ci kernel. Thank you.

Signed-off-by: Alyssa Rosenzweig <alyssa@collabora.com>
Acked-by: Jason Ekstrand <jason.ekstrand@collabora.com>
Part-of: <https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/19358>

---
## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[c1651bfacf...](https://github.com/apollographql/apollo-server/commit/c1651bfacf8d310615be79e9246d7f0bd9bfa926)
#### Tuesday 2022-11-01 19:07:06 by Trevor Scheer

Integration testsuite direct dependency on Apollo Server (#7114)

The peer dependency arrangement of testsuite on server was problematic.
In one sense, it seems reasonable since we want integration authors to
bring their own AS package. However, bumping that peer dependency with
every version update is technically a breaking change - and our release
tooling (changeset) doesn't provide us a means to workaround the
behavior where it major version bumps both packages.

For correctness and compliance with our tooling, a direct dependency
addresses both concerns. We've also added an additional test which
ensures that the versions match. The test really just validates that
there's one install of @apollo/server (by using an instanceof check
against the testsuite's ApolloServer constructor and the actual instance
provided by the testsuite consumer).

Fixes #7109

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[2a8ebba36a...](https://github.com/Unknownity/cmss13/commit/2a8ebba36a2c76ed855987dc107c9c385f6f16ea)
#### Tuesday 2022-11-01 19:52:54 by Joelampost

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
## [sevenrock/android_kernel_motorola_msm8998](https://github.com/sevenrock/android_kernel_motorola_msm8998)@[3a5034b48f...](https://github.com/sevenrock/android_kernel_motorola_msm8998/commit/3a5034b48f6ff4e87cd9f38f8e17bd7dd136b204)
#### Tuesday 2022-11-01 19:58:21 by Christian Brauner

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
## [sorbet/sorbet](https://github.com/sorbet/sorbet)@[3cb2b4b1c8...](https://github.com/sorbet/sorbet/commit/3cb2b4b1c868b15f8b572a63099b87720d581018)
#### Tuesday 2022-11-01 20:01:04 by Jake Zimmerman

Remove call to `dealias` in namer (#6519)

* Remove call to `dealias` in namer

We don't allow constant aliases in class scopes anyways. Not sure why
we're trying to dealias here.

If I had to guess, this was a remant of some hacks we had way long ago
to support this pattern, which was common in Stripe's codebase:

    class Chalk::ODM::Model
    end

    M = Chalk::ODM::Model

    class M::A
    end

But this pattern is already rejected by Sorbet, and has been for as long
as I can remember, so likely when that change was finally made, someone
forgot to delete this `dealias` call.

* Remove unused `ctx` parameter

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[762521e8a5...](https://github.com/ttaylorr/git/commit/762521e8a5a6948501d56d51da3f70df4f3dfdbe)
#### Tuesday 2022-11-01 20:35:14 by Jeff King

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
## [swordcube/FNF-Plasma-Engine](https://github.com/swordcube/FNF-Plasma-Engine)@[a92e847816...](https://github.com/swordcube/FNF-Plasma-Engine/commit/a92e8478163b69b3fe082e6637eb6755c927c57a)
#### Tuesday 2022-11-01 20:53:05 by Raf

added create() to scripts because fuck you i am not modding with onCreate

---
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[14c96d05b8...](https://github.com/Profakos/orbstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Tuesday 2022-11-01 21:39:24 by scriptis

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
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[99b8d6b494...](https://github.com/Profakos/orbstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Tuesday 2022-11-01 21:39:24 by vincentiusvin

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
## [GODdudesoyeah/cmss13](https://github.com/GODdudesoyeah/cmss13)@[ca2114f0f5...](https://github.com/GODdudesoyeah/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Tuesday 2022-11-01 22:04:31 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[0220bde488...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Tuesday 2022-11-01 22:15:28 by PotatoTomahto

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
## [Lioquacht-Religion/VirtualFridge-Frontend](https://github.com/Lioquacht-Religion/VirtualFridge-Frontend)@[106e785e5a...](https://github.com/Lioquacht-Religion/VirtualFridge-Frontend/commit/106e785e5ad8c5216fd394b2401ecc7e425cb1a6)
#### Tuesday 2022-11-01 22:46:14 by Lioquacht-Religion

storagepage gets data from backend--I hate my life-- remembar ngFor/ngfor forever

---
## [solanum-ircd/solanum](https://github.com/solanum-ircd/solanum)@[06c5309534...](https://github.com/solanum-ircd/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Tuesday 2022-11-01 23:32:06 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---

