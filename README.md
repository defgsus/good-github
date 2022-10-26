## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-25](docs/good-messages/2022/2022-10-25.md)


2,292,442 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,292,442 were push events containing 3,487,417 commit messages that amount to 268,528,551 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [Mu-L/linux](https://github.com/Mu-L/linux)@[d21f4b7ffc...](https://github.com/Mu-L/linux/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Tuesday 2022-10-25 00:02:03 by Douglas Anderson

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
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[f923f61011...](https://github.com/TheBoondock/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Tuesday 2022-10-25 00:12:17 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[1097c85c56...](https://github.com/rd-stuffs/msm-4.14/commit/1097c85c56220f336669f4a598cde378c1697209)
#### Tuesday 2022-10-25 00:22:24 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [chiefowonikoko1/The-best-powerful-spiritual-herbalist-juju-in-Nigeria-2347017229671](https://github.com/chiefowonikoko1/The-best-powerful-spiritual-herbalist-juju-in-Nigeria-2347017229671)@[592b6e62d7...](https://github.com/chiefowonikoko1/The-best-powerful-spiritual-herbalist-juju-in-Nigeria-2347017229671/commit/592b6e62d7695c50f38b8c71ab48a26d4ab024fc)
#### Tuesday 2022-10-25 00:52:32 by chiefowonikoko1

Google search

it's true that THE WAY TO SUCCESS IS VERY SO NARROW,+2347017229671,But that is for those that not ask for the ROAD, because they said that THOSE that ask for the ROAD will never MISROAD.......

CHIEF ORIOGBO OWONIKOKO is one of the POWERFUL SPIRITUAL HERBALIST and NATIVE DOCTOR that GOVERNMENT CONFIRM and APPROVED in the YEAR 1988.....

I am IFASHAKIN the son of CHIEF ORIOGBO  of IJEBU LAND known as an HERBALIST and NATIVE DOCTOR base in IJEBU OGUN STATE NIGERIA,you can contact him if you have interest in SPIRITUAL,such as follows:

INSTANTLY MONEY,
MONEY INVOKING,
FINANCIALLY BREAKTHROUGH,
POWER TO CONTROL EVERYTHING,
PENNIES ELONGATION,
SEXUAL WELLNESS,
CROWD PULLER,
LOCKING OF CLIENTS,
SPIRITUAL HUSBAND,
BRING BACK YOUR EX HUSBAND OR WIFE,
SPIRITUAL WEALTHY POT,
VISA APPROVAL,
COMMAND TONE,
LOTTERY SUCCESS,
PROMOTION AT WORK,
FRUIT OF WOMB,
CURING OF ANY KIND OF DISEASE etc...

notification:Please do not try to COPY this ADVERT to be SCAMMING people's online, because if you try to do so,CHIEF ORIOGBO OWONIKOKO will try all his possible POWER to let you SUFFER for it,so a single word is enough for a wise one.......


 CONTACT:+2347017229671

The number is also available on WhatsApp,you can also add up on this SOCIAL MEDIA account to always seen the work of CHIEF ORIOGBO OWONIKOKO as follows:
FACEBOOK ACCOUNT NAME...
oloye Oriogbo Owonikoko..
INSTAGRAM ACCOUNT NAME..
chiefofmakingmoney........

---
## [ctm/diet](https://github.com/ctm/diet)@[fd1d71c6d0...](https://github.com/ctm/diet/commit/fd1d71c6d08e3f9a62e9c21d11ea7dcbc9927c87)
#### Tuesday 2022-10-25 00:53:46 by Clifford T. Matthews

includes through my dinner tonight.

I had huge trouble with a toothache which resulted in a root canal.  My
weight shot up, in part because I was drinking both to celebrate and as a
way to avoid the pain during the day.

---
## [vogonsorg/Doom3D](https://github.com/vogonsorg/Doom3D)@[7d738a40aa...](https://github.com/vogonsorg/Doom3D/commit/7d738a40aaf62e02c9d2d8397397936f53c850c6)
#### Tuesday 2022-10-25 00:53:52 by vogonsorg

Update README.md

Doom3D Version 1.16 Readme
**************************

Doom3D is a Win32/DirectX port of Doom, Id Software's FPS.

System Requirements
-------------------

- Windows 9x/2000
- DirectX 6.0 or higher

Reccomended
-----------

- Sound Card
- Direct3D compatible 3D graphics card

Features
--------

- High resolution modes
- Runs in a window
- Full TCP-IP Network support (including multi-monitor 360 degree capability)
- Compressed WAD file support
- Matrix support(see website)
- Sound+Music
- Hardware accelerated version(requires Direct3D compatible 3D card)
- optional MD2 model replacements for sprites
- Complies to GL-Friendly Nodes (v2) specification
- Splitscreen multiplayer - including Dual Mouse support!
- console and quake-style key bindings

Dll Descriptions
----------------

c_sw8:  'Original'(software) 8-bit renderer, also works in a window on a 32-bit
        color desktop.
c_sw16: Above renderer 'Fudged' into 16-bit color (still only 256 actual colors!),
        Runs faster than c_sw8 when in window.
c_d3d:  All-new(ish) Direct3D Hardware renderer. Requires 3D card.
        Adjusting the advanced settings can often give improved results.
		Now allows replacing sprites with MD2 models.
		I reccommend you use glBSP to generate GL-Friendly nodes as this
		fixes several problems.

MD2 model support
-----------------

see md2.txt for more information

You may also need to increase the heap size when using MD2 models.

GL-Friendly Nodes
-----------------

Early versions of Doom3D had trouble rendering some floors/ceilings, resulting
in gaps through which the sky was visible. This problem is fixed by supporting the use of GL-Friendly nodes.

To take advantage of this feature you will need to generate nodes using
a GL-friendly node builder.

The only node builder currently available is glBSP, and is available from
http://www.netspace.net.au/~ajapted/glbsp.html

glBSP cannot read compressed WAD files, but you can compress WAD and GWA files
after running glBSP.

PWADs
-----

PWADs can be used in the same way as with the original Doom, ie. by adding the
-file <filename> parameter either in a shortcut or in the parameters box in
the setup program.

Enabling the Fix Sprites option allows Doom3D to use the sprites in some
PWAD's without needing to use DEUSF, or similar. WADs that contain additional
S_START/S_END or SS_START/SS_END lumps _should_ work properly, but I haven't
tested them. any feedback would be appreciated

Using the WAD file compressor
-----------------------------

Doom3D supports compressed WAD files. To create a compressed WAD file use
COMPWAD.EXE (included). This takes 2 command line parameters, the first is the
name of the original WAD file, the socon is the name of the new compressed wad
file. This should work with all WAD files (including PWADS). Decompressing
WAD files to their original form is not currently supported.
Adding '-fast' gives a significant speed increase, with only slightly less
compression.

NOTE: compressed WAD files only work with Doom3D, and the original Doom
executables will NOT be able to read them. YOU HAVE BEEN WARNED. You are also
advised to make a backup first, just in case something goes wrong.

Splitscreen Multiplayer
-----------------------

Doom3D supports multiplayer games with more than one person per machine using
splitscreen mode. This can be enabled either with the '-split' command line or
through the setup utility by altering the 'Local Players' netgame setting.

A maximum of 4 players can play on each machine.

Doom3D also supports using a second mouse. To use this, plug a searial mouse
into a spare serial port, and set the COM port in the controls section of the
setup utility. Many PS2 mice come with an adapter that allows you to plug them
into a serial port. Some non-microsoft mice (mostly old 3-button ones I think)
work in mouse systems mode, to use these set the com port to a negative value,
ie -1 if on com1, -2 if on com 2, etc. You may also want to change which player
the second mouse controls.

Splitscreen mode can also be used with conventional netgames, the players on
each machine are numbered sequentialy, although the total maximum of 4 players 
still applies, this may be increased in future versions.

Keyboard Bindings & Console Commands
------------------------------------

If a key is bound to "+command", then "+command" will be executed when the key
is pressed, and "-command" will be executed when the key is released.
Multiple commands can be seperated by a semicolon (;).
To bind or alias a command consisting of more than one word, the command must
be surrounded by quotes.

Available commands:

alias <alias> <command> - create alias, omitting parameters will display
    current aliases
bind <key> <command> - bind command to key, bind <key> will display current
    binding
exec <filename> - execute command script

The following accept an optional parameter specifying which player they apply to
(for splitscreen mode)
autorun - toggles autorun on/off
weapon <number> - select weapon by number (1=fist, 2=pistol, etc.)
nextwep - select next available weapon
+fire, +run, +use, +forward, +back, +left, +right, +strafe, +strafeleft,
+straferight - player controls

Most controls are also configurable via. the options menu.

Advanced Settings
-----------------
(Direct3D renderer only)

*UseColorKey
If non-zero will use color keying rather than alpha information for
trasparency effects. Can be faster but doesn't work on all 3D cards. Can also
cause sprites to have a pink halo when combined with bilinear filtering.

*BilinearFiltering
Zero to use point filtering, 1 to use bilinear filtering.
Enabling bilinear filtering 'smoothes' the textures. Disabling can give
a performance increase, and looks more like the original.

*TextureMip
*SpriteMip
Hardware rendering requires texture dimensions to be exact powers of 2.
A value of 0 rounds dimensions up, 1 rounds down, so some loss of quality on
non-power-of-2 sized textures. A value of 2 uses half the size of 1, 3 uses
a quarter, etc. Can inprove performance, especialy if funning low on texture
memory.
Cards with 4MB or more texture memory should be OK with a value of 0, but 2MB
cards need a value of at least 1. If you see white/gray untextured walls try
increasing this. A negative value indicates use the actual size, which almost
certainly won't work.
Using MD2 models generaly requires much more texture memory than sprites.

*ForceSquareTextures
If non-zero forces all textures to be square in size. Most (all?) 3D cards
require this to be set.

*MinTextureSize
Sets the minimum size for textures. Should be a power of 2. Not really sure why
you'd want to, it's just a left over debugging option

*MinTextureSize
Sets the maximum size for textures. Should be a power of 2. Many cards don't
suport textures larger than 256.

*MD2ini
The ini file to use to determine how to use MD2 models. see md2.txt

*NoMD2Weapons
Use 2D (sprite) weapons even if MD2 models available

*Skin<n>
Skins to use for other players in netgames.

*3D Display Device
Select which Direct3D device to use for rendering

Contact Info
------------

WebPage:

http://www.redrival.com/fudgefactor/

Any comments, questions, bug reports, money, etc. welcome.

email: pbrook@bigfoot.com

***When sending bug reports, please run with -debug parameter, and include
debug.txt with your bug report.

Command line options
--------------------

These can either be typed in on the command line, entered into the Parameters
box in the setup utility, or added to any shortcuts you create.

Most of these are options are also configuable via. the setup utility.

Memory:
-heapsize <n>
	Allocate an <n> MB heap (Default=8).
	Hardware renderer needs less memory than software.
	A setting of >half physical memory will probably cause 
	excessive swapfile paging and deteriorated preformance.
	Can also be set width setup utility.

Network: - Note network games can be started via. the setup program
-split [n]
	Splitscreen mode with n players (max. 4).
-net <playernum> [hostname[:port]] ...
	Starts a network game.
	<playernum> indicates your player (1-4), or first player if using
	splitscreen.
	You must include all network nodes(ie. players+drones) in this list
-port <portnum>
	sets the TCP/IP port to use, default 1638 decimal (666 hex:-)
-players <num>
	Set total number of players
-right
-left
-back
	For 3(4?)-monitor mode. Same as -drone -nogun -viewangle <90|270|180>
	If you've got a couple of spare computers lying about then you can use 2
	as drone screens to give 270/360 degree vision-quite an advantage in
	deathmatch!
-drone
	drone mode, follows annother player, most useful in conjunction with
	-viewangle & -viewoffset
-netcheat
	Enable cheats. Must enabled by all players to take effect.

Graphics:
-fps
	Display framerate counter. Can also toggle with 'idfps' cheatcode during
	play
-matrix
	enable matrix mode
-minterleave <lines>
	default=10
-msep <distance>
	default=30
-nogfn
	disable use of GL-Friendly nodes(Direct3D only)

-viewangle <theta>
	offsets the view by theta degrees
	ie. 0=forward(default), 90=right, 180=backwards, 270=left
-viewoffset <dist>
	offsets the view sideways (+ve ot right, -ve to left)
	For creating right and left eyes, Idealy with 2 projectors through
	polariod and a pair of polatising glasses(like in the big cinemas:)
-nogun
	don't draw player's gun sprite on screen.

Sound:
-nosound
	Disable sound interface, use this if you're having problems such as
	"Unable to create primary sound buffer".
-nomusic
	Disable ingame music

Misc:
-config <filename>
	use alternate config file.
-debug
	Create debug.txt file
-iwad <filename>
    specify main iwad name, allows you to use doom1&2 in same directory
-file <name>.wad
	specify pwad name

Experimental PVS support
------------------------

Doom3D v1.16 contains some experimental code for performing PVS calculations.
This generates information on which parts of the level are visible from
different locations, allowing the renderer to skip drawing those which are
not visible, resulting in an overall increase in game speed.
As the code is still not fully tested, and generation of this information
can take some time exery time a level is loaded (a few seconds on a p3-550!)
it is disabled by default. To enable PVS generation add -genpvs to the command
line.
Please don't send me bug reports on this as originaly it wasn't going to be
in this release at all.


Known Bugs
----------

- Sometimes throws up an error on Alt-Tab in fullscreen mode
- May crash with many voodoo based systems in Direct3D mode-please let me know
  if you do get Doom3D to run on a Voodoo system
- automap doesn't work in splitscreen, and only partialy in Direct3D mode
- music volume slider not fully implemented (either full on or off)
- MD2 HUD weapons can sink into walls&floors
- Some bits of the map are visible where there shoud only be sky - I'm working on this

New in version 1.16
-------------------

- Console (press '~')
- Quake-style key bindings
- Controls added to options menu
- Splitscreen multiplayer
- Dual mouse support

New in version 1.14
-------------------

- MD2 model support fixed
- Keypad keys now recognised properly
- Fixed crashes on some levels when using 'GL-Friendly Nodes'

New in version 1.12
-------------------

- MD2 model support
- Support of GL_Friendly nodes
- Customisable controls
- Autorun
- Joystick support
- Fixed 'Plane vertex overflow' error
- Parameters box in setup program now works
- Network code now supports IP addresses for opponents
- Lots of bug fixes (honest)
- Episode 4 of Ultimate Doom now works

New in version 1.10
-------------------

- Music works!
- Improved sound support
- Improved texture handling when using Direct3D
- Gamma correction more effective with Direct3D
- Much improved setup utility

---
## [lupesoltec/kernel_xiaomi_daisy](https://github.com/lupesoltec/kernel_xiaomi_daisy)@[0f47dbe99a...](https://github.com/lupesoltec/kernel_xiaomi_daisy/commit/0f47dbe99abbcbba90a06719a6d0a527e072f5cd)
#### Tuesday 2022-10-25 02:23:39 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: TogoFire <italomellopereira@gmail.com>

---
## [rob-3/git](https://github.com/rob-3/git)@[d3775de074...](https://github.com/rob-3/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Tuesday 2022-10-25 04:15:48 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Matthew-Seebohm/DoomClone2022](https://github.com/Matthew-Seebohm/DoomClone2022)@[838a01aacb...](https://github.com/Matthew-Seebohm/DoomClone2022/commit/838a01aacb4d57862affc87e197ea4ba6b5ce97b)
#### Tuesday 2022-10-25 04:20:58 by Matthew

[Intro] I once had some sweet memories Its worth remains the same How can I remember those moments, sweetheart? They should have been right there  [Chorus] Vanish into dark Future, now, and past Vanish into dark When it all mixes up Drowned in pain, I lost my mind There's no good or bad in there Drowned in gain, I lost my mind There's no good or bad in there Vanish into dark It is hopelessness filled by the light [Verse 2] Abyss of desire Abyss of dreams Is it farther than the edge of thе world? And then after that, will the drеam still go on? I hope, I hope that it's not the end of sorrow and joy  [Chorus] Vanish into dark Future, now, and past Vanish into dark When it all mixes up Drowned in pain, I lost my mind There's no good or bad in there Drowned in gain, I lost my mind There's no good or bad in there Vanish into dark It is hopelessness filled by the light  [Bridge] Drive, drive Drive piles into the footprints behind Slash, slash Don't forget the respect for pain  [Chorus] Drowned in pain, I lost my mind There's no good or bad in there Drowned in gain, I lost my mind There's no good or bad in there Drowned in pain, I lost my mind There's no good or bad in there Drowned in gain, I lost my mind There's no good or bad in there Vanish into dark Future, now, and past Vanish into dark When it all mixes up Vanish into dark It's the sweet smell of death Vanish into dark Dreadful hope never speaks out You might also like Necessary Discrepancy Daisuke Ishiwatari Love the Subhuman Self Daisuke Ishiwatari Smell of the Game Daisuke Ishiwatari [Verse 4] Patched-up liberty compressed the sky The broken wall will cry for humanity I once had some sweet memories Its worth remains all the same How can I remember those moments, sweetheart? Tell me (tell me), tell me If there's a man who can make anything Give me the tools to live in the past It's all gone down so deep, I can't see anymore If that's not the way to go Let me, let me Let me carve your way I'm a shadow always with you

[Intro]
I once had some sweet memories
Its worth remains the same
How can I remember those moments, sweetheart?
They should have been right there

[Chorus]
Vanish into dark
Future, now, and past
Vanish into dark
When it all mixes up
Drowned in pain, I lost my mind
There's no good or bad in there
Drowned in gain, I lost my mind
There's no good or bad in there
Vanish into dark
It is hopelessness filled by the light
[Verse 2]
Abyss of desire
Abyss of dreams
Is it farther than the edge of thе world?
And then after that, will the drеam still go on?
I hope, I hope that it's not the end of sorrow and joy

[Chorus]
Vanish into dark
Future, now, and past
Vanish into dark
When it all mixes up
Drowned in pain, I lost my mind
There's no good or bad in there
Drowned in gain, I lost my mind
There's no good or bad in there
Vanish into dark
It is hopelessness filled by the light

[Bridge]
Drive, drive
Drive piles into the footprints behind
Slash, slash
Don't forget the respect for pain

[Chorus]
Drowned in pain, I lost my mind
There's no good or bad in there
Drowned in gain, I lost my mind
There's no good or bad in there
Drowned in pain, I lost my mind
There's no good or bad in there
Drowned in gain, I lost my mind
There's no good or bad in there
Vanish into dark
Future, now, and past
Vanish into dark
When it all mixes up
Vanish into dark
It's the sweet smell of death
Vanish into dark
Dreadful hope never speaks out
You might also like
Necessary Discrepancy
Daisuke Ishiwatari
Love the Subhuman Self
Daisuke Ishiwatari
Smell of the Game
Daisuke Ishiwatari
[Verse 4]
Patched-up liberty compressed the sky
The broken wall will cry for humanity
I once had some sweet memories
Its worth remains all the same
How can I remember those moments, sweetheart?
Tell me (tell me), tell me
If there's a man who can make anything
Give me the tools to live in the past
It's all gone down so deep, I can't see anymore
If that's not the way to go
Let me, let me
Let me carve your way
I'm a shadow always with you

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[0f8072e199...](https://github.com/dsmith328/LC13Master/commit/0f8072e19927889bc8e2f2f705c3e3f13adc531a)
#### Tuesday 2022-10-25 04:31:43 by Lance

Major Commit

General Bee: Faction Checking
Queen of Hatred: Pink Midnight "friendly" breach
Queen Bee: Bee Faction Inheritance
Bottle of Tears: Breach Functionality
Fairy Festival: Fairy Faction Inheritance & Resistance Nerf
White Lake: Debug Removal
Red Queen: Following Diamonds, Diamonds don't fire unless they'd have clear LoS, Diamonds dismember on kill.
Laetitia: Fear Reduced while Breaching.
Silent Girl: Added "Party Starter" ability; Every 5 minutes while she's breached a nearby abnormality's counter will decrease by 1.
White Night: Pink Midnight Functionality, including designating WAW+ Abnormalities as Apostles.

---
## [AnandSuresh02/kernel_asus_sdm660](https://github.com/AnandSuresh02/kernel_asus_sdm660)@[aab978aeca...](https://github.com/AnandSuresh02/kernel_asus_sdm660/commit/aab978aecaca409fdd32e1de494387a4bf9d4078)
#### Tuesday 2022-10-25 04:42:58 by Christian Brauner

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
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[b80a218b52...](https://github.com/Offroaders123/Art-Gen/commit/b80a218b5281aa41252326d61a41199df19d500b)
#### Tuesday 2022-10-25 04:50:15 by Offroaders123

Second Version!

Second? Yeah, so I originally planned for the project to use basic HTML+CSS with Puppeteer in Electron to generate the thumbnails, but that got more complicated than it had to be (bloated too). I decided to change course and use just simple JS in the browser, making use of the Canvas API to generate the thumbnails instead! This significantly slims down the project's stack, and it allows it to run on any device too!

The project utilizes JS MediaTags, a JS library that allows you to read the metadata from song files. In this case, I will be using it to extract the artwork, artist, album, and song names from the song's metadata, then use that to programatically generate the YouTube Art Track thumbnail with the Canvas API. Very neat!

I'm also using the JS with Types route, which is JSDoc + TSC. I think it works very well for building an app, as their isn't an API to be consumed by another user, unlike a library or package would. For those, I'd tend to lean more towards full TypeScript, as those tend to have more type exports and things like that. For this, I am only using the type checking to build the project itself. If I end up wanting to separate the project's code directly from the app itself (I do plan to do that eventually), then I would probably move the module bits over to TypeScript, since that would be used by others and not only the app. It would be cool to allow this to work away from the browser too, maybe making use of Puppetter and the Canvas API, so you could use Node exclusively. Is OffscreenCanvas available in Node? That would be great!

Also planned to come along with this project (not sure if it will be part of this repo or not, yet), I am going to make a script that utilizes ffmpeg to generate the YouTube video itself, using the thumbnail generated here, and with the song audio itself. With those together, I'd also add an API hook to YouTube itself (you'd have to add cridentials to your account to connect with the YouTube API) so that it could also upload that video automatically. I want to add that, as it could handle making the playlist and such, and I would design it so that it would allow you to upload multiple songs at a time (after the previous one finishes processing), and they will appear in the same order as you intend them to be. I have had a lot of trouble uplading multiple videos at once, in a selected order, and keeping them in that same order as they upload. After they are processed, YouTube seems to disregard that original order, and order them at random, no matter how you had them originally. In a similar vein, this also happens when you un-private privated videos. This caught me by suprise, and it was very annoying. I wanted all of my songs to show up in my video feed in the correct order to how the album goes, and it ended up breaking because of that.

So, with all of those together, I essentially am making a programmatic way of generating the art, and video for each of your song files (using the song's metadata itself), then proceeding to upload each of those to YouTube, using that same metadata, and ensuring that they upload in the exact order that matches the order of your album.

Super happy with this project so far! I thought of it while up in Mammoth a few weeks ago.

These files were from last Tuesday, and I'm making a repo for them now. The original Puppeteer in Electron version was just a few days before that.

Was gonna commit it sooner, but stepped back into the Gamedata Parser project again! Lots of new developments over there. I was gonna work on that tonight actually, but realized I should probably get this rolling before it falls to the backburner.

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[160936c4de...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/160936c4dec4b56d5840028a6cbb258b5ea8b2d6)
#### Tuesday 2022-10-25 04:52:31 by tanish2k09

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
## [thelookoutway/bundler-app-dev-shell](https://github.com/thelookoutway/bundler-app-dev-shell)@[fcb7901dc6...](https://github.com/thelookoutway/bundler-app-dev-shell/commit/fcb7901dc682ada750226878553e0571cef3ac13)
#### Tuesday 2022-10-25 06:02:32 by Brad Parker

Avoid setting local bundle path twice

This can happen whenever nix-shell is run from within a direnv loaded
shell or a nix-shell. E.G.

    $ nix-shell
    $ echo $BUNDLE_PATH
    .bundle/cpq7h6vsbq4d1sgvqqg8df6jvnw60knh-environment
    $ nix-shell # Going one level deeper
    $ echo $BUNDLE_PATH
    .bundle/cpq7h6vsbq4d1sgvqqg8df6jvnw60knh-environment/.bundle/cpq7h6vsbq4d1sgvqqg8df6jvnw60knh-environment

This has previsouly just been a little annoying. But if we want to add
scripts to the TLW/TLW way repo that use nix-shell as an interpreter
then it gets us into a bit of trouble. More specifically I'm trying to
add to the shellHook in TLW/TLW something that will make users of
Rubymine able to have a better time. We may want to set the bundle path
config on every shell load, this will allow Rubymine to find the path
in the .bundle/config file. I also added a niv script that used a
nix-shell interpreter. Whenever I ran the niv script, the BUNDLE_PATH
would be doubled up (ends up the interpreter will use our shell.nix,
TIL). When it did that it _also_ put that wrong doubled up value into
the .bundle/config file (oh no!).

This change should mean that if we've set the $BUNDLE_PATH to the local
location (the one we use in dev), it won't be set again. If however it's
been set to anything else we'll add the local path on the end.

---
## [LukeTech2006/VpDrs-22](https://github.com/LukeTech2006/VpDrs-22)@[5893454607...](https://github.com/LukeTech2006/VpDrs-22/commit/5893454607f5f178797634b0e143f1994aceabf9)
#### Tuesday 2022-10-25 09:26:39 by LukeTech2020

app security is a fucking nightmare

why are people so evil i have to include anti-sql-injection shit?

---
## [lucas-paulger-sonarsource/react](https://github.com/lucas-paulger-sonarsource/react)@[b6978bc38f...](https://github.com/lucas-paulger-sonarsource/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2022-10-25 09:36:34 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [AtriLux/AISD_2](https://github.com/AtriLux/AISD_2)@[c91bbb462f...](https://github.com/AtriLux/AISD_2/commit/c91bbb462f8fc98fde186c60471ba5b34e416055)
#### Tuesday 2022-10-25 09:37:35 by mrvadman1

Day2

Dear diary, I cannot describe all the pain and humiliation that I experienced...

Co-Authored-By: AtriLux <90695137+AtriLux@users.noreply.github.com>

---
## [nbyavuz/postgres](https://github.com/nbyavuz/postgres)@[8272749e8c...](https://github.com/nbyavuz/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Tuesday 2022-10-25 09:37:37 by Tom Lane

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
## [fedora-python/pathfix](https://github.com/fedora-python/pathfix)@[20b1caa6c8...](https://github.com/fedora-python/pathfix/commit/20b1caa6c80179c54c0fbf74b35a5aca3bbfbc3c)
#### Tuesday 2022-10-25 11:16:31 by Guido van Rossum

Merged revisions 55817-55961 via svnmerge from svn+ssh://pythondev@svn.python.org/python/branches/p3yk

................
  r55837 | guido.van.rossum | 2007-06-08 16:04:42 -0700 (Fri, 08 Jun 2007) | 2 lines

  PEP 3119 -- the abc module.
................
  r55838 | guido.van.rossum | 2007-06-08 17:38:55 -0700 (Fri, 08 Jun 2007) | 2 lines

  Implement part of PEP 3119 -- One Trick Ponies.
................
  r55847 | guido.van.rossum | 2007-06-09 08:28:06 -0700 (Sat, 09 Jun 2007) | 2 lines

  Different way to do one trick ponies, allowing registration (per PEP strawman).
................
  r55849 | guido.van.rossum | 2007-06-09 18:06:38 -0700 (Sat, 09 Jun 2007) | 3 lines

  Make sure that the magic looking for __hash__ (etc.) doesn't apply to
  real subclasses of Hashable.
................
  r55852 | guido.van.rossum | 2007-06-10 08:29:51 -0700 (Sun, 10 Jun 2007) | 2 lines

  Add some more examples, e.g. generators and dict views.
................
  r55853 | guido.van.rossum | 2007-06-10 08:31:59 -0700 (Sun, 10 Jun 2007) | 2 lines

  keys() and items() *are* containers -- just values() isn't.
................
  r55864 | georg.brandl | 2007-06-10 15:29:40 -0700 (Sun, 10 Jun 2007) | 2 lines

  PEP 3127: new octal literals, binary literals.
................
  r55865 | georg.brandl | 2007-06-10 15:31:37 -0700 (Sun, 10 Jun 2007) | 2 lines

  Some octal literal fixes in Tools.
................
  r55866 | georg.brandl | 2007-06-10 15:37:43 -0700 (Sun, 10 Jun 2007) | 2 lines

  Tokenizer changes for PEP 3127.
................
  r55867 | georg.brandl | 2007-06-10 15:37:55 -0700 (Sun, 10 Jun 2007) | 2 lines

  Some docs for PEP 3127.
................
  r55868 | georg.brandl | 2007-06-10 15:44:39 -0700 (Sun, 10 Jun 2007) | 2 lines

  Missed a place in intobject.c. Is that used anymore anyway?
................
  r55871 | neal.norwitz | 2007-06-10 18:31:49 -0700 (Sun, 10 Jun 2007) | 182 lines

  Merged revisions 55729-55868 via svnmerge from
  svn+ssh://pythondev@svn.python.org/python/trunk

  ........
    r55731 | neal.norwitz | 2007-06-01 00:29:12 -0700 (Fri, 01 Jun 2007) | 7 lines

    SF 1668596/1720897: distutils now copies data files
    even if package_dir is empty.

    This needs to be backported.  I'm too tired tonight.  It would be great
    if someone backports this if the buildbots are ok with it.  Otherwise,
    I will try to get to it tomorrow.
  ........
    r55732 | georg.brandl | 2007-06-01 04:33:33 -0700 (Fri, 01 Jun 2007) | 2 lines

    Bug #1722484: remove docstrings again when running with -OO.
  ........
    r55735 | georg.brandl | 2007-06-01 12:20:27 -0700 (Fri, 01 Jun 2007) | 2 lines

    Fix wrong issue number.
  ........
    r55739 | brett.cannon | 2007-06-01 20:02:29 -0700 (Fri, 01 Jun 2007) | 3 lines

    Have configure raise an error when building on AtheOS.  Code specific to AtheOS
    will be removed in Python 2.7.
  ........
    r55746 | neal.norwitz | 2007-06-02 11:33:53 -0700 (Sat, 02 Jun 2007) | 1 line

    Update expected birthday of 2.6
  ........
    r55751 | neal.norwitz | 2007-06-03 13:32:50 -0700 (Sun, 03 Jun 2007) | 10 lines

    Backout the original 'fix' to 1721309 which had no effect.
    Different versions of Berkeley DB handle this differently.
    The comments and bug report should have the details.  Memory is allocated
    in 4.4 (and presumably earlier), but not in 4.5.  Thus
    4.5 has the free error, but not earlier versions.

    Mostly update comments, plus make the free conditional.

    This fix was already applied to the 2.5 branch.
  ........
    r55752 | brett.cannon | 2007-06-03 16:13:41 -0700 (Sun, 03 Jun 2007) | 6 lines

    Make _strptime.TimeRE().pattern() use ``\s+`` for matching whitespace instead
    of ``\s*``.  This prevents patterns from "stealing" bits from other patterns in
    order to make a match work.

    Closes bug #1730389.  Will be backported.
  ........
    r55766 | hyeshik.chang | 2007-06-05 11:16:52 -0700 (Tue, 05 Jun 2007) | 4 lines

    Fix build on FreeBSD.  Bluetooth HCI API in FreeBSD is quite different
    from Linux's.  Just fix the build for now but the code doesn't
    support the complete capability of HCI on FreeBSD yet.
  ........
    r55770 | hyeshik.chang | 2007-06-05 11:58:51 -0700 (Tue, 05 Jun 2007) | 4 lines

    Bug #1728403: Fix a bug that CJKCodecs StreamReader hangs when it
    reads a file that ends with incomplete sequence and sizehint argument
    for .read() is specified.
  ........
    r55775 | hyeshik.chang | 2007-06-05 12:28:15 -0700 (Tue, 05 Jun 2007) | 2 lines

    Fix for Windows: close a temporary file before trying to delete it.
  ........
    r55783 | guido.van.rossum | 2007-06-05 14:24:47 -0700 (Tue, 05 Jun 2007) | 2 lines

    Patch by Tim Delany (missing DECREF). SF #1731330.
  ........
    r55785 | collin.winter | 2007-06-05 17:17:35 -0700 (Tue, 05 Jun 2007) | 3 lines

    Patch #1731049: make threading.py use a proper "raise" when checking internal state, rather than assert statements (which get stripped out by -O).
  ........
    r55786 | facundo.batista | 2007-06-06 08:13:37 -0700 (Wed, 06 Jun 2007) | 4 lines

    FTP.ntransfercmd method now uses create_connection when passive,
    using the timeout received in connection time.
  ........
    r55792 | facundo.batista | 2007-06-06 10:15:23 -0700 (Wed, 06 Jun 2007) | 7 lines

    Added an optional timeout parameter to function urllib2.urlopen,
    with tests in test_urllib2net.py (must have network resource
    enabled to execute them). Also modified test_urllib2.py because
    testing mock classes must take it into acount. Docs are also
    updated.
  ........
    r55793 | thomas.heller | 2007-06-06 13:19:19 -0700 (Wed, 06 Jun 2007) | 1 line

    Build _ctypes and _ctypes_test in the ReleaseAMD64 configuration.
  ........
    r55802 | georg.brandl | 2007-06-07 06:23:24 -0700 (Thu, 07 Jun 2007) | 3 lines

    Disallow function calls like foo(None=1).
    Backport from py3k rev. 55708 by Guido.
  ........
    r55804 | georg.brandl | 2007-06-07 06:30:24 -0700 (Thu, 07 Jun 2007) | 2 lines

    Make reindent.py executable.
  ........
    r55805 | georg.brandl | 2007-06-07 06:34:10 -0700 (Thu, 07 Jun 2007) | 2 lines

    Patch #1667860: Fix UnboundLocalError in urllib2.
  ........
    r55821 | kristjan.jonsson | 2007-06-07 16:53:49 -0700 (Thu, 07 Jun 2007) | 1 line

    Fixing changes to getbuildinfo.c that broke linux builds
  ........
    r55828 | thomas.heller | 2007-06-08 09:10:27 -0700 (Fri, 08 Jun 2007) | 1 line

    Make this test work with older Python releases where struct has no 't' format character.
  ........
    r55829 | martin.v.loewis | 2007-06-08 10:29:20 -0700 (Fri, 08 Jun 2007) | 3 lines

    Bug #1733488: Fix compilation of bufferobject.c on AIX.
    Will backport to 2.5.
  ........
    r55831 | thomas.heller | 2007-06-08 11:20:09 -0700 (Fri, 08 Jun 2007) | 2 lines

    [ 1715718 ] x64 clean compile patch for _ctypes, by Kristj?n Valur
    with small modifications.
  ........
    r55832 | thomas.heller | 2007-06-08 12:01:06 -0700 (Fri, 08 Jun 2007) | 1 line

    Fix gcc warnings intruduced by passing Py_ssize_t to PyErr_Format calls.
  ........
    r55833 | thomas.heller | 2007-06-08 12:08:31 -0700 (Fri, 08 Jun 2007) | 2 lines

    Fix wrong documentation, and correct the punktuation.
    Closes [1700455].
  ........
    r55834 | thomas.heller | 2007-06-08 12:14:23 -0700 (Fri, 08 Jun 2007) | 1 line

    Fix warnings by using proper function prototype.
  ........
    r55839 | neal.norwitz | 2007-06-08 20:36:34 -0700 (Fri, 08 Jun 2007) | 7 lines

    Prevent expandtabs() on string and unicode objects from causing a segfault when
    a large width is passed on 32-bit platforms.  Found by Google.

    It would be good for people to review this especially carefully and verify
    I don't have an off by one error and there is no other way to cause overflow.
  ........
    r55841 | neal.norwitz | 2007-06-08 21:48:22 -0700 (Fri, 08 Jun 2007) | 1 line

    Use macro version of GET_SIZE to avoid Coverity warning (#150) about a possible error.
  ........
    r55842 | martin.v.loewis | 2007-06-09 00:42:52 -0700 (Sat, 09 Jun 2007) | 3 lines

    Patch #1733960: Allow T_LONGLONG to accept ints.
    Will backport to 2.5.
  ........
    r55843 | martin.v.loewis | 2007-06-09 00:58:05 -0700 (Sat, 09 Jun 2007) | 2 lines

    Fix Windows build.
  ........
    r55845 | martin.v.loewis | 2007-06-09 03:10:26 -0700 (Sat, 09 Jun 2007) | 2 lines

    Provide LLONG_MAX for S390.
  ........
    r55854 | thomas.heller | 2007-06-10 08:59:17 -0700 (Sun, 10 Jun 2007) | 4 lines

    First version of build scripts for Windows/AMD64 (no external
    components are built yet, and 'kill_python' is disabled).
  ........
    r55855 | thomas.heller | 2007-06-10 10:55:51 -0700 (Sun, 10 Jun 2007) | 3 lines

    For now, disable the _bsddb, _sqlite3, _ssl, _testcapi, _tkinter
    modules in the ReleaseAMD64 configuration because they do not compile.
  ........
    r55856 | thomas.heller | 2007-06-10 11:27:54 -0700 (Sun, 10 Jun 2007) | 1 line

    Need to set the environment variables, otherwise devenv.com is not found.
  ........
    r55860 | thomas.heller | 2007-06-10 14:01:17 -0700 (Sun, 10 Jun 2007) | 1 line

    Revert commit 55855.
  ........
................
  r55880 | neal.norwitz | 2007-06-10 22:07:36 -0700 (Sun, 10 Jun 2007) | 5 lines

  Fix the refleak counter on test_collections.  The ABC metaclass creates
  a registry which must be cleared on each run.  Otherwise, there *seem*
  to be refleaks when there really aren't any.  (The class is held within
  the registry even though it's no longer needed.)
................
  r55884 | neal.norwitz | 2007-06-10 22:46:33 -0700 (Sun, 10 Jun 2007) | 1 line

  These tests have been removed, so they are no longer needed here
................
  r55886 | georg.brandl | 2007-06-11 00:26:37 -0700 (Mon, 11 Jun 2007) | 3 lines

  Optimize access to True and False in the compiler (if True)
  and the peepholer (LOAD_NAME True).
................
  r55905 | georg.brandl | 2007-06-11 10:02:26 -0700 (Mon, 11 Jun 2007) | 5 lines

  Remove __oct__ and __hex__ and use __index__ for converting
  non-ints before formatting in a base.

  Add a bin() builtin.
................
  r55906 | georg.brandl | 2007-06-11 10:04:44 -0700 (Mon, 11 Jun 2007) | 2 lines

  int(x, 0) does not "guess".
................
  r55907 | georg.brandl | 2007-06-11 10:05:47 -0700 (Mon, 11 Jun 2007) | 2 lines

  Add a comment to explain that nb_oct and nb_hex are nonfunctional.
................
  r55908 | guido.van.rossum | 2007-06-11 10:49:18 -0700 (Mon, 11 Jun 2007) | 2 lines

  Get rid of unused imports and comment.
................
  r55910 | guido.van.rossum | 2007-06-11 13:05:17 -0700 (Mon, 11 Jun 2007) | 2 lines

  _Abstract.__new__ now requires either no arguments or __init__ overridden.
................
  r55911 | guido.van.rossum | 2007-06-11 13:07:49 -0700 (Mon, 11 Jun 2007) | 7 lines

  Move the collections ABCs to a separate file, _abcoll.py, in order to avoid
  needing to import _collections.so during the bootstrap (this will become
  apparent in the next submit of os.py).

  Add (plain and mutable) ABCs for Set, Mapping, Sequence.
................
  r55912 | guido.van.rossum | 2007-06-11 13:09:31 -0700 (Mon, 11 Jun 2007) | 2 lines

  Rewrite the _Environ class to use the new collections ABCs.
................
  r55913 | guido.van.rossum | 2007-06-11 13:59:45 -0700 (Mon, 11 Jun 2007) | 72 lines

  Merged revisions 55869-55912 via svnmerge from
  svn+ssh://pythondev@svn.python.org/python/trunk

  ........
    r55869 | neal.norwitz | 2007-06-10 17:42:11 -0700 (Sun, 10 Jun 2007) | 1 line

    Add Atul Varma for patch # 1667860
  ........
    r55870 | neal.norwitz | 2007-06-10 18:22:03 -0700 (Sun, 10 Jun 2007) | 1 line

    Ignore valgrind problems on Ubuntu from ld
  ........
    r55872 | neal.norwitz | 2007-06-10 18:48:46 -0700 (Sun, 10 Jun 2007) | 2 lines

    Ignore config.status.lineno which seems new (new autoconf?)
  ........
    r55873 | neal.norwitz | 2007-06-10 19:14:39 -0700 (Sun, 10 Jun 2007) | 1 line

    Prevent these tests from running on Win64 since they don\'t apply there either
  ........
    r55874 | neal.norwitz | 2007-06-10 19:16:10 -0700 (Sun, 10 Jun 2007) | 5 lines

    Fix a bug when there was a newline in the string expandtabs was called on.
    This also catches another condition that can overflow.

    Will backport.
  ........
    r55879 | neal.norwitz | 2007-06-10 21:52:37 -0700 (Sun, 10 Jun 2007) | 1 line

    Prevent hang if the port cannot be opened.
  ........
    r55881 | neal.norwitz | 2007-06-10 22:28:45 -0700 (Sun, 10 Jun 2007) | 4 lines

    Add all of the distuils modules that don't seem to have explicit tests. :-(
    Move an import in mworkscompiler so that this module can be imported on
    any platform.  Hopefully this works on all platforms.
  ........
    r55882 | neal.norwitz | 2007-06-10 22:35:10 -0700 (Sun, 10 Jun 2007) | 4 lines

    SF #1734732, lower case the module names per PEP 8.

    Will backport.
  ........
    r55885 | neal.norwitz | 2007-06-10 23:16:48 -0700 (Sun, 10 Jun 2007) | 4 lines

    Not sure why this only fails sometimes on Unix machines. Better
    to disable it and only import msvccompiler on Windows since that's
    the only place it can work anyways.
  ........
    r55887 | neal.norwitz | 2007-06-11 00:29:43 -0700 (Mon, 11 Jun 2007) | 4 lines

    Bug #1734723: Fix repr.Repr() so it doesn't ignore the maxtuple attribute.

    Will backport
  ........
    r55889 | neal.norwitz | 2007-06-11 00:36:24 -0700 (Mon, 11 Jun 2007) | 1 line

    Reflow long line
  ........
    r55896 | thomas.heller | 2007-06-11 08:58:33 -0700 (Mon, 11 Jun 2007) | 3 lines

    Use "O&" in calls to PyArg_Parse when we need a 'void*' instead of "k"
    or "K" codes.
  ........
    r55901 | facundo.batista | 2007-06-11 09:27:08 -0700 (Mon, 11 Jun 2007) | 5 lines

    Added versionchanged flag to all the methods which received
    a new optional timeout parameter, and a versionadded flag to
    the socket.create_connection function.
  ........
................
  r55914 | guido.van.rossum | 2007-06-11 14:19:50 -0700 (Mon, 11 Jun 2007) | 3 lines

  New super() implementation, for PEP 3135 (though the PEP is not yet updated
  to this design, and small tweaks may still be made later).
................
  r55923 | guido.van.rossum | 2007-06-11 21:15:24 -0700 (Mon, 11 Jun 2007) | 4 lines

  I'm guessing this module broke when Neal ripped out the types module --
  it used 'list' both as a local variable and as the built-in list type.
  Renamed the local variable since that was easier.
................
  r55924 | guido.van.rossum | 2007-06-11 21:20:05 -0700 (Mon, 11 Jun 2007) | 5 lines

  Change all occurrences of super(<thisclass>, <firstarg>) to super().
  Seems to have worked, all the tests still pass.
  Exception: test_descr and test_descrtut, which have tons of these
  and are there to test the various usages.
................
  r55939 | collin.winter | 2007-06-12 13:57:33 -0700 (Tue, 12 Jun 2007) | 1 line

  Patch #1735485: remove StandardError from the exception hierarchy.
................
  r55954 | neal.norwitz | 2007-06-12 21:56:32 -0700 (Tue, 12 Jun 2007) | 51 lines

  Merged revisions 55913-55950 via svnmerge from
  svn+ssh://pythondev@svn.python.org/python/trunk

  ........
    r55926 | marc-andre.lemburg | 2007-06-12 02:09:58 -0700 (Tue, 12 Jun 2007) | 3 lines

    Apply patch #1734945 to support TurboLinux as distribution.
  ........
    r55927 | marc-andre.lemburg | 2007-06-12 02:26:49 -0700 (Tue, 12 Jun 2007) | 3 lines

    Add patch #1726668: Windows Vista support.
  ........
    r55929 | thomas.heller | 2007-06-12 08:36:22 -0700 (Tue, 12 Jun 2007) | 1 line

    Checkout, but do not yet try to build, exernal sources.
  ........
    r55930 | thomas.heller | 2007-06-12 09:08:27 -0700 (Tue, 12 Jun 2007) | 6 lines

    Add bufferoverflowU.lib to the libraries needed by _ssl (is this the
    right thing to do?).

    Set the /XP64 /RETAIL build enviroment in the makefile when building
    ReleaseAMD64.
  ........
    r55931 | thomas.heller | 2007-06-12 09:23:19 -0700 (Tue, 12 Jun 2007) | 5 lines

    Revert this change, since it breaks the win32 build:

    Add bufferoverflowU.lib to the libraries needed by _ssl (is this the
    right thing to do?).
  ........
    r55934 | thomas.heller | 2007-06-12 10:28:31 -0700 (Tue, 12 Jun 2007) | 3 lines

    Specify the bufferoverflowU.lib to the makefile on the command line
    (for ReleaseAMD64 builds).
  ........
    r55937 | thomas.heller | 2007-06-12 12:02:59 -0700 (Tue, 12 Jun 2007) | 3 lines

    Add bufferoverflowU.lib to PCBuild\_bsddb.vcproj.
    Build sqlite3.dll and bsddb.
  ........
    r55938 | thomas.heller | 2007-06-12 12:56:12 -0700 (Tue, 12 Jun 2007) | 2 lines

    Don't rebuild Berkeley DB if not needed (this was committed by accident).
  ........
    r55948 | martin.v.loewis | 2007-06-12 20:42:19 -0700 (Tue, 12 Jun 2007) | 3 lines

    Provide PY_LLONG_MAX on all systems having long long.
    Will backport to 2.5.
  ........
................
  r55959 | guido.van.rossum | 2007-06-13 09:22:41 -0700 (Wed, 13 Jun 2007) | 2 lines

  Fix a compilation warning.
................

---
## [raspberrypi/linux](https://github.com/raspberrypi/linux)@[4dcae3385c...](https://github.com/raspberrypi/linux/commit/4dcae3385ced0ed2852fabfebce817eb51cef8db)
#### Tuesday 2022-10-25 11:28:39 by Serge Semin

clk: vc5: Fix 5P49V6901 outputs disabling when enabling FOD

[ Upstream commit c388cc804016cf0f65afdc2362b120aa594ff3e6 ]

We have discovered random glitches during the system boot up procedure.
The problem investigation led us to the weird outcomes: when none of the
Renesas 5P49V6901 ports are explicitly enabled by the kernel driver, the
glitches disappeared. It was a mystery since the SoC external clock
domains were fed with different 5P49V6901 outputs. The driver code didn't
seem like bogus either. We almost despaired to find out a root cause when
the solution has been found for a more modern revision of the chip. It
turned out the 5P49V6901 clock generator stopped its output for a short
period of time during the VC5_OUT_DIV_CONTROL register writing. The same
problem was found for the 5P49V6965 revision of the chip and was
successfully fixed in commit fc336ae622df ("clk: vc5: fix output disabling
when enabling a FOD") by enabling the "bypass_sync" flag hidden inside
"Unused Factory Reserved Register". Even though the 5P49V6901 registers
description and programming guide doesn't provide any intel regarding that
flag, setting it up anyway in the officially unused register completely
eliminated the denoted glitches. Thus let's activate the functionality
submitted in commit fc336ae622df ("clk: vc5: fix output disabling when
enabling a FOD") for the Renesas 5P49V6901 chip too in order to remove the
ports implicit inter-dependency.

Fixes: dbf6b16f5683 ("clk: vc5: Add support for IDT VersaClock 5P49V6901")
Signed-off-by: Serge Semin <Sergey.Semin@baikalelectronics.ru>
Reviewed-by: Luca Ceresoli <luca@lucaceresoli.net>
Link: https://lore.kernel.org/r/20220929225402.9696-2-Sergey.Semin@baikalelectronics.ru
Signed-off-by: Stephen Boyd <sboyd@kernel.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [newstools/2022-iol-weekend-argus](https://github.com/newstools/2022-iol-weekend-argus)@[825d129826...](https://github.com/newstools/2022-iol-weekend-argus/commit/825d12982678b58953b0fc3e888fdb69717aca36)
#### Tuesday 2022-10-25 12:36:10 by Billy Einkamerer

Created Text For URL [www.iol.co.za/weekend-argus/weekend-argus/news/14-year-old-girl-allegedly-stabs-moms-boyfriend-to-death-during-apparent-altercation-between-the-couple-78352d7a-ae29-4212-b2ce-eb3ffff2b0e2]

---
## [ricardomaraschini/opa](https://github.com/ricardomaraschini/opa)@[965301f90e...](https://github.com/ricardomaraschini/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Tuesday 2022-10-25 14:14:34 by Stephan Renatus

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
## [expwr/Used_car_lot2](https://github.com/expwr/Used_car_lot2)@[eedb9bd5b2...](https://github.com/expwr/Used_car_lot2/commit/eedb9bd5b2ac9911166ca7e56485daad7dc6aa72)
#### Tuesday 2022-10-25 15:07:52 by Noah Diana

Merge branch 'master' into Stupid-fucking-shitty-ass-side-bar-shit-ass

---
## [expwr/Used_car_lot2](https://github.com/expwr/Used_car_lot2)@[d8a16272ba...](https://github.com/expwr/Used_car_lot2/commit/d8a16272bafd1ae24666314c4c3d5ec9c6dc5c45)
#### Tuesday 2022-10-25 15:07:52 by Noah Diana

Merge pull request #4 from expwr/Stupid-fucking-shitty-ass-side-bar-shit-ass

10/25/22

---
## [p-on/infosec-cli](https://github.com/p-on/infosec-cli)@[b2d7bd46a4...](https://github.com/p-on/infosec-cli/commit/b2d7bd46a4ce7bf6e3834247f3d316fd9710ace8)
#### Tuesday 2022-10-25 15:15:40 by pigeon

feat: Fixed username signups, go fuck yourself whatsmyname

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2ebd7634c6...](https://github.com/treckstar/yolo-octo-hipster/commit/2ebd7634c63cf8a756083b6ce0e210db6c9a06c5)
#### Tuesday 2022-10-25 15:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [chickells/odin-javascript-exercises](https://github.com/chickells/odin-javascript-exercises)@[e4e988b161...](https://github.com/chickells/odin-javascript-exercises/commit/e4e988b16197d2640d68d1d849850e05ee96c13b)
#### Tuesday 2022-10-25 16:08:56 by Chase

made it so after pressing equals, it'll restart
the display if the prev button was equals

still not perfect with functionality but good enough
def getting "over" this shit lol, WANT TO DO COOL
SHIT aka fucking with data and actually doing real stuff
not just making dumb little apps.

whatever, i guess this is the starting point
backend stuff seems more up my alley.
user interface stuff is NOT my cup of tea at the
current moment

SUBJECT TO CHANGE I SUPPOSE
CARRY ON

---
## [tgodzik/metals](https://github.com/tgodzik/metals)@[6fca4bc1b2...](https://github.com/tgodzik/metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Tuesday 2022-10-25 16:36:50 by ckipp01

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
## [RodrigoSanchez06/CheemSmart](https://github.com/RodrigoSanchez06/CheemSmart)@[845ea82792...](https://github.com/RodrigoSanchez06/CheemSmart/commit/845ea8279241786fa48e2be2afdf7e1088bba664)
#### Tuesday 2022-10-25 17:32:10 by Chao280802

Merge pull request #16 from RodrigoSanchez06/Chao

Implemented english (Fuck you Gael MF)

---
## [chickells/odin-javascript-exercises](https://github.com/chickells/odin-javascript-exercises)@[84e8c6326d...](https://github.com/chickells/odin-javascript-exercises/commit/84e8c6326d955772989568e3695e5d27a42f276c)
#### Tuesday 2022-10-25 17:40:51 by Chase

adding keyboard listeners AND
IT'S BEING FUCKING STUPID
oh well lol, lots of progress today

time for break, lift, lunch, work

FIRST DAY WAS SUCCESS

---
## [OldDanceJacket/Nyanotrasen](https://github.com/OldDanceJacket/Nyanotrasen)@[8f52eb9e0f...](https://github.com/OldDanceJacket/Nyanotrasen/commit/8f52eb9e0f7e246ddcadb7f96a948ceec27d7ee4)
#### Tuesday 2022-10-25 18:50:24 by ZeroDayDaemon

Psionic Content (#542)

* Psionic Content

* Address Reviews

* rane bitches too much

* Tonight, on unsolved mysteries, find out who gives a shit about bigfoot

UPDATE: apparently nobody gives a shit so fuck him.

UPDATE: Last night somebody broke in and stole $500 worth of shit at my house

That’s right $500 worth of BULLSHIT!!!

* Address reviews

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[3e84b251fb...](https://github.com/GeoB99/reactos/commit/3e84b251fb1760523f112273f62c7cf9412e7608)
#### Tuesday 2022-10-25 19:31:13 by George Bișoc

[NTOS:CM] Implement registry checks & recovery

Instead of having the CmCheckRegistry implementation in the kernel, it's better to have it in the Configuration Manager library instead (aka CMLIB). The benefits of having it in the library are the following:

- CmCheckRegistry can be used in FreeLdr to fix the SYSTEM hive
- It can be used on-demand in the kernel
- It can be used for offline registry repair tools
- It makes the underlying CmCheckRegistry implementation code debug-able in user mode

[SDK][CMLIB] Declare HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL boot types

=== DOCUMENTATION REMARKS ===

HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL are boot type values set up by the CMLIB library. HBOOT_TYPE_REGULAR indicates a normal system boot whereas HBOOT_TYPE_SELF_HEAL indicates the system boot is assisted within self healing mode.

Whether the former or the latter value is set it's governed by both the kernel and the bootloader. The bootloader and the kernel negotiate together to determine if any of the registry properties (the hive, the base block, the registry base, etc) are so severed from corruption or not. In extreme cases where
registry healing is possible, the specific base block of the damaged hive will have its flags marked with HBOOT_TYPE_SELF_HEAL. At this point the boot phase procedure is orchestrated since the boot phase no longer goes on the default path but it's assisted, as I have already said above.

[SDK][CMLIB] Implement two names & Unicode names comparison functions

CmpCompareBothCompressedNames and CmpCompareDistinctNames are necessary for lexicographical order validation code when validating the key in question.

[SDK][CMLIB] Implement self-heal registry helpers

This implements cmheal.c file which provides the basic registry self-heal infrastructure needed by the public CmCheckRegistry function. The infrastructure provides a range of various self-heal helpers for the hive, such as subkey, class, values and node healing functions.

[SDK][CMLIB] Implement CmCheckRegistry and validation private helpers

CmCheckRegistry is a function that provides the necessary validation checks for a registry hive. This function usually comes into action when logs have been replayed for example, or when a registry hive internals have changed such as when saving a key, loading a key, etc.

This commit implements the whole Check Registry infrastructure (cmcheck.c) in CMLIB library for ease of usage and wide accessibility across parts of the OS. In addition, two more functions for registry checks are also implemented -- HvValidateHive and HvValidateBin.

CORE-9195
CORE-6762

[NTOS:CM] Use the appropriate flags on functions that will call CmCheckRegistry & add missing CmCheckRegistry calls

In addition to that, in some functions like CmFlushKey, CmSaveKey and CmSaveMergedKeys we must validate the underlying hives as a matter of precaution that everything is alright and we don't fuck all the shit up.

[NTOS:CM] Don't lazy flush the registry during unlocking operation

Whenever ReactOS finishes its operations onto the registry and unlocks it, a lazy flush is invoked to do an eventual flushing of the registry to the backing storage of the system. Except that... lazy flushing never comes into place.

This is because whenever CmpLazyFlush is called that sets up a timer which needs to expire in order to trigger the lazy flusher engine worker. However, registry locking/unlocking is a frequent occurrence, mainly when on desktop. Therefore as a matter of fact, CmpLazyFlush keeps removing and inserting the timer and the lazy flusher will never kick in that way.

Ironically the lazy flusher actually does the flushing when on USETUP installation phase because during text-mode setup installation in ReactOS the frequency of registry operations is actually less so the timer has the opportunity to expire and fire up the flusher.

In addition to that, we must queue a lazy flush when marking cells as dirty because such dirty data has to be flushed down to the media storage of the system. Of course, the real place where lazy flushing operation is done should be in a subset helper like HvMarkDirty that marks parts of a hive as dirty but since we do not have that, we'll be lazy flushing the registry during cells dirty marking instead for now.

CORE-18303

[NTOS:CM][CMLIB] Use HBOOT_TYPE_REGULAR / HBOOT_TYPE_SELF_HEAL indicators for boot type instead of hardcoded values

[NTOS:CM] Disable hard errors when setting up a new size for a hive file / annotate CmpFileSetSize parameters with SAL

During a I/O failure of whatever kind the upper-level driver, namely a FSD, can raise a hard error and a deadlock can occur. We wouldn't want that to happen for particular files like hives or logs so in such cases we must disable hard errors before toying with hives until we're done.

In addition to that, annotate the CmpFileSetSize function's parameters with SAL.

[NTOS:CM] Ignore syncing/flushing requests after registry shutdown

When shutting down the registry of the system we don't want that the registry in question gets poked again, such as flushing the hives or syncing the hives and respective logs for example. The reasoning behind this is very simple, during a complete shutdown the system does final check-ups and stuff until the computer
shuts down.

Any writing operations done to the registry can lead to erratic behaviors. CmShutdownSystem call already invokes a final flushing of all the hives on the backing storage which is more than enough to ensure consistency of the last session configuration. So after that final flushing, mark HvShutdownComplete as TRUE indicating
that any eventual flushing or syncying (in the case where HvSyncHive gets called) request is outright ignored.

---
## [alphagov/govuk-jenkinslib](https://github.com/alphagov/govuk-jenkinslib)@[fbd99ca0ce...](https://github.com/alphagov/govuk-jenkinslib/commit/fbd99ca0ce3426a49a0acb8ac0ec492ca45e3e88)
#### Tuesday 2022-10-25 20:00:20 by Kevin Dew

Make shallow clones a config option that defaults to false

This has been done to prevent the common headaches devs experience when
they have a large PR, or collection of PRs that end up being more than
30 commits out of sync with the main branch.

In those cases developers are greeted with a rather unhelpful message
of:

```
+ git merge --no-commit origin/main
fatal: refusing to merge unrelated histories
+ git merge --abort
fatal: There is no merge to abort (MERGE_HEAD missing).
```

As we don't have an agreement that there is a commit limit on PRs this
arbitrary number is confusing and divisive (easily starts the debate on
how big should a PR be).

This changes the approach to default to not having any limit at all and
makes the limit an optimisation that repos can opt into. This means that
repos calling `govuk.buildProject` will default to cloning an entire
repo.

My theory is that there is actually very few GOV.UK repos where the
quantity of commits is significant enough that the time spent cloning
repos is a noticeable impact in build times (the worst one was
govuk-secrets which is now on GitHub Actions). If there is a repo that
is big the team owners can configure their call to buildProject to
configure their project accordingly.

For example to restore the previous behaviour to a repo you can call
govuk.buildProject like so:

```
govuk.buildProject(shallowClone: env.BRANCH_NAME != "main", mergeDepth: 30)
```

---
## [DaedalusDock/Gameserver](https://github.com/DaedalusDock/Gameserver)@[e273ed1b5f...](https://github.com/DaedalusDock/Gameserver/commit/e273ed1b5f2cc445810bf4b6f3a0ea659d40a43a)
#### Tuesday 2022-10-25 20:01:35 by Kapu1178

update screenshot tests (#55)

* update screenshot tests

* try fix issues

* fix

* try fix lizard

* fuck you im tired

* fucking come on

* fuck it im disabling this and fixing it later

* Fix chain pull through space issue (fixes unit test failure) (#69832)

* Disables ashwalker unit test

* FUCK YOU

Co-authored-by: Marina <50789504+KirbyDaMaster@users.noreply.github.com>

---
## [nextstrain/cli](https://github.com/nextstrain/cli)@[c9ced1a13f...](https://github.com/nextstrain/cli/commit/c9ced1a13f21de86af2ef6a0d1508ad6f31d1b63)
#### Tuesday 2022-10-25 20:35:02 by Thomas Sibley

runner.conda: Pin the version of Micromamba used

For the same reason we pin deps with nextstrain-base, this ensures that
`nextstrain setup conda` can't break between one day and the next
because of a new Micromamba release.  This happened during my
development of the Conda runtime with the release of Micromamba 0.26.0¹,
and so has been on my mind to address.

The version used is overridable by an environment variable for debugging
and troubleshooting purposes, but it also serves as an escape hatch for
users stuck on older Nextstrain CLI versions who might need a newer
Micromamba for whatever reason.

We should generally try to keep the pinned version current as long as
new releases work ok.  It's too bad Dependabot doesn't support the Conda
ecosystem.²  If we're bad at remembering to update this over time, we
can setup a GitHub Action workflow to check for new releases and remind
us.

¹ https://github.com/mamba-org/mamba/issues/1979
² https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates#supported-repositories-and-ecosystems

---
## [mfFrida/Capstone-Project-Semester-1](https://github.com/mfFrida/Capstone-Project-Semester-1)@[2c05e31020...](https://github.com/mfFrida/Capstone-Project-Semester-1/commit/2c05e31020086a87ac551e9f958c7401074e1cb6)
#### Tuesday 2022-10-25 22:49:05 by Ian Hall

preliminary data visual work. discovered stuff in data that can be excluded to assist visual, resolving tonight or in morning so can proceed with visual fully. also began theory-testing for z-test; remember to seperate categories being tested from dataset to be able to conduct test for statistical relevance

---
## [ProfessionalGooseChaser/Pitt-22-Personal-Projects](https://github.com/ProfessionalGooseChaser/Pitt-22-Personal-Projects)@[c82ad60416...](https://github.com/ProfessionalGooseChaser/Pitt-22-Personal-Projects/commit/c82ad60416005193838eb8def4bbc2a4244fbeca)
#### Tuesday 2022-10-25 23:21:04 by Cole Hansen

AutomaticEmails.py v1.07

Version 1 is Done! Some final notes. To allow my script to access the email, I had to generate an app password for my computer. (It was a pain in the ass there was an annoying lack of documentation on the matter).  Otherwise the script works well. Some things I want to fix in Version 2, I want to make the graphic better. Adjusting to use RGBA values instead of RGB, as well as making the words more readable. Lastly, I was unable to use the API for games from the 2022-23 Season. It knew what games were being played but It wasn't able to find the scores or the records for said games. More to Come

---

