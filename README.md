## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-12](docs/good-messages/2022/2022-02-12.md)


1,362,286 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,362,286 were push events containing 1,960,722 commit messages that amount to 124,709,821 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[b48cda6afa...](https://github.com/Aerden/tgstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Saturday 2022-02-12 00:50:45 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[1f23d3d7ad...](https://github.com/SmoSmoSmoSmok/tgstation/commit/1f23d3d7ad87eebf74b1c9dc51867c5c21edf547)
#### Saturday 2022-02-12 00:56:47 by Jeremiah

Should fix shuttles leaving without sections(#64764)

Should(tm)

This was a suggestion by @Mothblocks and it seemed easy to implement

Fixes #64546 (Icebox evac will sometimes leave without sections)
Fixes #64653 (You might have fixed the kilo whiteship by making it move, but you didn't fix all of it)

Uh people won't just randomly get yeeted into space with half of a shuttle.
Kinda funny for people watching but not if you die of pressure loss or get stuck on the station
Runtime man bad

(Sleeping in here in general is like admitting that we're ok with missing a few atoms, which is what this runtime is. S just missing is better then overtime. Supposedly --Lemon)

---
## [Clanzion/Naruto_Ninpou](https://github.com/Clanzion/Naruto_Ninpou)@[51ea1fb91f...](https://github.com/Clanzion/Naruto_Ninpou/commit/51ea1fb91f5800ff43ce815c28a397ae7c7f946b)
#### Saturday 2022-02-12 00:57:54 by MetalfOxXer

Changes

- Changed book to damage based on current HP
- Temari Iron Fan 30% ms
- Change Global gold / Assist gold
- See if there is any way to speed up the orb effects connecting on the heroes there is a slight delay on it rn..
- Buff Shizune farm ability
- Make Sakura Byakugo healing over 5s + instant
- Corrosive damage isn't stacking (which would be op anyway) (Heaven Stone + Spirit of Darkness for example) but it also doesn't appear to prioritize the stronger one either
- Wire string body swap cooldown 30s, make it have an effect when it's on cooldown
- Fuu Yamanka R nerfed to 25% x 25% x skill level
- Change Kohaku no Johei to dispell Susanoo / Izanagi (any other stuff heaven stone dispells that normally doesn't get dispelled?)
- Revert the change that Byakugo can't be dispelled
- Han Q bugged (freezes in place)
- Fix Gold bug on Kohaku no Johei (it's gold cost in some trigger..)
- Rock Lee Gates description
- Check the triggers picole sent in Github to make sure they are all added
- Han R pause thing (this isn't needed)
- Check Wood animation
- Shinigami Mask casting range increased from 700 to 1000
- Fix projectiles for Poison & Oil
- Finish orbs put exceptions for all items
- Change the effect of Minato's chakra jump
- added 20% ms to iron fan
- Test Executioner Blade drop from box bug
- Check effects on all Elemental Kage robes..
- Check effect on all Ultimate Weapons..

Orb Effects (Elemental Weapons & Ultimate Weapons)
- Splash Damage (passive, 50 damage bonus in 300 radius)
- Bash (passive, 12% chance to stun for 1s)
- Chilling Attack (passive, 50% slow for 1.5s)
- Corrosive Attack (passive, -10 armor)
- Chain Lightning (passive, 5% chance to deal 300 damage)
- Critical Strike (passive, 15% to deal 6 x damage)
- Light Attack (passive, 10% chance to silence for 1s)

- Double checked description & and corrected stuff:
	- Ninja Weapons
	- Support Tools
	- Bijus
	- Rikudou Sennin Staff
	- Akatsuki Cloth
	- Akatsuki Set
	- Akatsuki Leader Set
	- Medical Ninja Cloth
	- Medical Ninja Set
	- Sanbi Skin
	- Sanbi's Hardened Skin
	- Sanbi's Impenetrable Skin
	- Juubi's Skin
	- Genin Cloth
	- Chunnin Cloth
	- Jounin Cloth
	- Anbu Cloth
	- Sannin Cloth
	- Kage Robe
	- Hokage Robe
	- Tsuchikage Robe
	- Mizukage Robe
	- Otogakure Robe
	- Raikage Robe
	- Kazekage Robe
	- Kyuubi Spear
	- Adamantine Staff
	- Perfect Kunai
	- Raijin no Ken x2
	- Iron Fan
	- Perfect Shuriken
	- Haku Senbons
	- Shinigami Mask
	- Perfect Senbons

---
## [ivelichkevich/dwm](https://github.com/ivelichkevich/dwm)@[67d76bdc68...](https://github.com/ivelichkevich/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Saturday 2022-02-12 01:45:14 by Chris Down

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
## [EnderKilledYou/SmackBitches](https://github.com/EnderKilledYou/SmackBitches)@[6d7a8a62bb...](https://github.com/EnderKilledYou/SmackBitches/commit/6d7a8a62bbdfd05fd72eecc4cf17af4623a8e238)
#### Saturday 2022-02-12 02:26:34 by microsoft

Dear Mr. Kooshesh. We are your biggest fans. Every day when we get up we check your twitter for your wise words of insparations. Every night we pray to god that he bless us with half your looks, charm, and skill. You are truely a god amongst gods. We're sorry that we have so many rude people working here who don't want to give you the time of day because you caught that weird employee years ago creeping kids at a high school code a thon. It's not fair to you. We know he's a scumbag. He's not even working here anymore and we would LOVE  if you signed this autographed picture of you for us. Sincerely -all dem wimmen at microsoft,github, and linked in.

---
## [philipl/mpv](https://github.com/philipl/mpv)@[649556b2b6...](https://github.com/philipl/mpv/commit/649556b2b65207c0d40751fae941223978b04932)
#### Saturday 2022-02-12 04:16:50 by Dudemanguy

github/workflows: use lua 5.1 on macos

LuaJIT is still actively developed, but upstream is allergic to making
new releases for whatever reason. The last tagged release was in May of
2017, so we probably shouldn't expect a new release anytime soon. Now
for mpv, this doesn't really matter except in the case of macOS where
2.0.5 is actually a bit broken (and of course the CI uses luajit). More
specifically, the 2.0.5 pc is broken and has a "-pagezero_size 10000"
flag which causes libmpv to fail (only executables are allowed to use
this). This magically works on waf. It's possible that it just happens
to ignore the link arguments. However on the meson build, this is broken
and led to a really ugly hack using a partial dependency so both mpv and
libmpv succeed. Fortunately, the 2.1 luajit branch fixes this.
Unfortunately, there's no actual release.

Instead, just use Lua 5.1. Note that lua 5.1 is technically deprecated
in homebrew, but the chances of this going away is pretty slim since
everyone knows that new lua versions are not backwards compatible.
Anyways, using 5.1 works fine and lets us get rid of a terrible hack in
the meson build. People really shouldn't be using 2.0 LuaJIT anyway.

---
## [philipl/mpv](https://github.com/philipl/mpv)@[f9bf6a601c...](https://github.com/philipl/mpv/commit/f9bf6a601c563015706bed7bdb2b4984119db360)
#### Saturday 2022-02-12 04:16:50 by Dudemanguy

meson: remove horrifying macos luajit hack

See the previous commit for the full explanation. Basically, luajit 2.0
has a bad pc file on macos that causes libmpv to fail during build. The
workaround was, if the os was darwin and luajit was found, to save a
full luajit dep and a partial luajit dep with the link args removed. The
partial dep was used for compiling libmpv, and the full dep was used for
the actual mpv executable. This worked and was needed for the CI to pass
but it sucked. Since the previous commit now makes the CI grab lua 5.1,
we don't need all this crap anymore. Just delete it and treat the
dependency normally.

This does effectively mean that building libmpv with luajit 2.0 on macOS
will no longer work with the meson build. However libraries not being
built correctly is not a mpv-specific issue. The waf build will succeed
for some reason, but it has known issues and it would be better if it
just failed honestly. An upstream developer said years ago that that
macOS users should use the 2.1 branch (and there's no release of
course). In any case, no macOS user should be building mpv with luajit
2.0, so we shouldn't be going out of our way to support this.

https://github.com/mpv-player/mpv/issues/7512
https://github.com/LuaJIT/LuaJIT/issues/521#issuecomment-562999247

---
## [philipl/mpv](https://github.com/philipl/mpv)@[34e0a212cd...](https://github.com/philipl/mpv/commit/34e0a212cd2e0a073a3580952549a62ede38c2d6)
#### Saturday 2022-02-12 04:16:50 by Dudemanguy

wayland: partially fix drag and drop handling

Drag and drop in wayland is weird and it seems everyone does this
slightly differently (fun). In the past, there was a crash that
occured (fixed by 700f4ef5fad353800fa866b059663bc1dd58d3b7) which
involved using the wl_data_offer_finish in an incorrect way that
triggered a protocol error (always fatal). The fix involved moving the
function call to data_device_handle_drop which seemingly works, but it
has an unfortunate side effect. It appears like GTK applications (or at
least firefox) close the pipe after this function is called which makes
it impossible for mpv to read data from the fd (well you could force it
open again in theory but let's not do that). Who knows if that was the
case when that commit was made (probably not because I'd think I would
have noticed; could just be a dummy though), but obviously having broken
dnd for a major application isn't so fun (this works with QT and
chromium anyway).

Ideally one would just simply check the pipe in data_device_handle_drop,
but this doesn't work because it doesn't seem the compositor actually
sends mpv the data by then. There's not actually a defined event when
you're supposed to be able to read data from this pipe, so we wait for
the usual event checking loop later for this. In that case,
wl_data_offer_finish needs to go back into check_dnd_fd, but we have to
be careful when calling it otherwise we'd just commit protocol errors
like before. We check to make sure we even have a valid wl->dnd_offer
before trying to indicate that it is finished and additionally make sure
there is a valid dnd_action (after checking the fd, it's always set back
to -1).

This doesn't fix everything though. Specifically, sway with
focus_follows_mouse (the default) and GTK as the data source still
doesn't work. The reason is that when you do a drag and drop in sway
with that option on, a new wl_data_device.data_offer event is sent out
instantly after the drop event. This happens before any data is sent
across the fd and before mpv even has a chance to check it. What GTK
does, when getting this new data_offer event, is close the pipe
(POLLHUP). This means mpv can't read it when we reach the event loop and
thus no data is ever read and broken drag and drop. From the client
side, this isn't really fixable since the wayland protocol doesn't have
a clear indication of when clients are supposed to read from the fd and
both the compositor and data source are doing things totally out of our
control. So we'll consider this weird case, "not our bug" at least. The
rest should work.

---
## [triplezeta/Shiptest](https://github.com/triplezeta/Shiptest)@[031c0866ed...](https://github.com/triplezeta/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Saturday 2022-02-12 04:47:43 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [KermitProject/ckermit](https://github.com/KermitProject/ckermit)@[16d830ec8e...](https://github.com/KermitProject/ckermit/commit/16d830ec8e1fde7fd63d9d5108f1f6601169e9db)
#### Saturday 2022-02-12 05:51:23 by Kermit Project

C-Kermit 4F(095) 1989/08/31 Unix, VMS, OS/2, OS9, Amiga, Apollo, Macintosh

Fix a bug which has been in ckucmd.c forever -- can't believe nobody ever
noticed it before!  If cmnum() is called as the last field in a command, and
it is supplied a default value, and the user types carriage return instead of
a number, then the default was not supplied.  The fix was in cmfld(), to
copy the default into the atom buffer, rather than just pointing to it.  This
fixes the problem with the transmit command not waiting for the echoed
linefeed when the user types "transmit foo.bar" and does not supply the final
field, the turnaround character, which was supposed to be linefeed (10) by
default.  Also, fix transmit so it echoes right on both full and half duplex
connections.

Addition of support for a variety of AT&T modems in ckudia.c, from Eric F.
Jones at AT&T, including the 2212C, 2224B, 2224CEO, and 2296A (should also
work with 2224G and 2248A, but not tested).  Also the AT&T Digital Terminal
Data Module (DTDM) found in the telephones connected to the AT&T System 85
digital PBX.

In ckutio.c: (a) for AT&T-based systems, modify tthang() to not wait for
carrier when reopening the device, (b) don't attempt to use the TIOCSINUSE
ioctl() unless TIOCSINUSE is a defined symbol.

Several minor cosmetic changes for the benefit of VMS.

4F(094) Sat Aug 19 18:29:14 1989

C-Kermit fails to write out one or more output file buffers on the AT&T
3B2/300, but works ok on all other systems tested, including other AT&T
systems.  Added bullet-proofing and debugging to zmchout() in ckufio.c,
and in ckcpro.w, checked decode()'s return code and cancelled the protocol
transaction upon decode() failure.  Also, commented out a trailing token
after an #endif in ckuusr.c.  (Later, turns out that the mere act of assigning
the value returned by zmchout() to a variable caused the macro to be evaluated
correctly).

4F(093) Wed Aug 16 22:22:05 1989

Many places ckudia.c, ckucon.c, ckuscr.c, and ckutio.c -- change the type
of functions that are passed as arguments to signal() to SIGTYP rather than
no type at all (i.e. int).  This should prevent many compiler warnings and
maybe even some runtime problems?

In ckcfns.c, fix the file counting (ffc++) so that correct file sizes are
reported by 'statistics'.

4F(092) Fri Aug 11 15:06:39 1989

Add code for converting file time to seconds since Jan 1, 1970 GMT.
Not used yet, but will be used in setting Unix file date from incoming
file attributes.  From David MacKenzie and Michael Haertel.  (This code is
enclosed in #ifdef NOY_YET brackets, because it causes numerous compile &
link time errors on certain systems).

Rename memcpy() replacement in ckudia.c to xcpy(), to eliminate core dumps
that the memcpy replacement caused on the ATT7300 and perhaps other systems.
Peter Mauzey, AT&T.

makefile addition for ATT6300, Peter Mauzey, AT&T.  makefile addition for
Convex, Peter Mossel, Columbia Univ Health Sciences.

4F(091) Sat Aug  5 14:29:41 1989

Fix send-packet size recalculation to not respond to spurious errors like
timout-retransmission of initial S-packet.

Reorganize code that responds to MAIL and REMOTE PRINT commands so that it's
in the system-dependent module, ckufio.c.  This will require adding zmail()
and zprint() functions to all other ck*fio.c modules.

Make a couple small changes to ckotio.c for OS/2, and in ckuusr.c also include
signal.h and setjmp.h for OS/2 (Rob Kedoin, blessed by Chris Adie).

4F(090) Wed Aug  2 19:24:01 1989

Fixes from Bob Larson:
Remove duplicate call to sysinit() from ckcmai.c.
Don't call strlen() on a constant in a loop (tilde_expand(), ckufio.c).
A couple OS-9 specific changes.

Put definition of memcpy() function into ckudia.c, because it is not available
to certain C compilers (used in Microcom modem support).

Attempt to make the Apollo SR10-BSD version compile correctly:
Change all "#ifdef apollo" back to "#ifdef aegis", and remove -Uapollo
from the sr10-bsd makefile entry.  This way, "apollo" is still defined,
which apparently it needs to be when #include'ing <stdio.h>, otherwise
there are horrible compiler errors regarding _bufsiz, etc.

4F(089) Thu Jul 20 19:59:25 1989

OS-9/68K support from Bob Larson, USC.  The main difference between OS-9 and
Unix (from Kermit's point of view) is that the OS-9 file system uses CR as
a line terminator, rather than LF.  The OS-9 specific modules are ck9con.c,
ck9fio.c, and ck9tio.c

Other modules had "#ifdef OSK"..."#endif" conditionals added: ckuus*.*,
ckcmai.c, ckcdeb.h, ckucmd.c, mainly having to do with \r, \n differences
between OS-9 and Unix.

Bob also found and corrected a lot of mistakes in the command parser --
extraneous dereferencing of pointers, misgrouped parentheses in numerous calls
to cmcfm(), etc.

Bob also replaced Jim Knutson's Microcom modem support in ckudia.c with
a different style of support for this modem.  As Bob says, "the two
versions make very different assumptions on how the modem will be configured
and used.  Mine assumes the modem is configured for reasonable interactive
use, and will try the autobaud sequence if the modem doens't respond to
a return.  The other one forces the configuration into modes that may be
slightly easier for a computer to understand, but make it hard to use
interactively."  Note, Bob makes extensive use of memcpy().  I hope that all
the systems that use ckudia.c support this function!  If not, it can
be replaced by strncpy().

Also, in ckudia.c, add support for additional responses from Hayes-like
modems: NO DIALTONE, BUSY, NO ANSWER, RING, ERROR.  From Bo Kullmar, Kista,
Sweden.

Also, in ckudia.c, add a couple sleep(1)'s for Rolm CBX dialing.  This made
it work, finally.

In ckutio.c, function tthang(), remove the closing and reopening of the tty
for BSD42.  It doesn't seem to be necessary.

In ckufio.c, add a little bullet-proofing to zsout() and zopeno(), to prevent
the case where you could crash the program by typing the command "log debug"
twice in a row.

Fix the TRANSMIT command to be interruptible by Ctrl-C, by getting rid of
longjmp, which apparently leaves you executing on the wrong stack.  Live &
learn...  Put all references to signal handling in the TRANSMIT command
(ckuusr.c) within #ifndef OS2...#endif conditionals.

Make the "size" message on incoming files in local mode less space consuming,
and put a space between it and the "A".

From Bo Kullmar in Sweden, fix ckucon.c not to give "Can't get character"
message if myread() returned its special error 9999.

4F(088) Wed Jul 19 20:54:06 1989

These releases are flying thick and fast!  This one has fixed-up support for
Masscomp/Concurrent RTU, plus a couple minor cosmetic improvements from
Farrel Woods, ftw@westford.ccur.com (Concurrent, formerly Masscomp):

The first is to get around a bug/inconsistancy in RTU signal handling in the
Berkeley environment.  It turns out that if a user handles a signal (SIGTSTP),
then any pending system call will return with EINTR when the program is
resumed. This caused Kermit to exit after being resumed, since our library
(e.g., getchar) will not re-try the system call.  Subsequent reads (and,
getchars) will work alright.  The fix is set a flag before sending SIGSTOP to
ourselves, and upon resumption, do an extra getchar if the flag was set.
(yuck).

Masscomp/Concurrent was added to the herald.

The flag for the first bug was located in ckutio.c.  It seemed to be
the place to put those kind of globals...

RTU as of version 4 uses Honey Dan Ber (sic?) uucp.  The lock files
live in /usr/spool/locks.

Upon resuming after being suspended, call prompt() if not in background mode
so that you know Kermit is paying attention to you again.

The Makefile was changed to build Kermit in the ucb universe, with the
BSD42 flag turned on.

4F(087) Wed Jul 19 11:35:09 1989

Hmmm....  A month ago, I merged in all of Chris Adie's OS/2 conditionals,
and now all of that has disappeared!  I can't explain it.  Maybe there was a
disk crash and the previous copies of the files were restored on top of the
new ones?  Sigh...  Anyway, I did it again.  New copies of: ckcmai.c,
ckucmd.c, ckudia.c, ckuscr.c, ckuusr.c, ckuus2.c, and ckuus3.c.

4F(086) Tue Jul 18 11:52:16 1989

Add missing #ifdef OS2's to ckcdeb.h and ckuusr.h.  Forgot these before, oops.

Change definition of tlog() and debug() when not defined to be the null
string, instead of {}, to prevent problems with semicolons in if-else
constructs (Steve Walton, Cal State Northridge).

In ckutio.c, function ttopen(), also put local line in no-echo mode for
ATT Sys III/V, as is done for BSD (David MacKenzie, Environmental Defense
Fund, Rockefeller Univ).

Major problems compiling on Apollo SR10 involving use of getchar() in
ckucmd.c with "make sr10-bsd", reported & not yet fixed.

4F(085) Fri Jul 14 13:19:00 1989

ckcfns.c: In opena(), save global file mode (i.e. transfer syntax, variable
"binary") in variable "bsave".  Check incoming file type attribute ("), if
any.  If text (A), set transfer syntax to binary for this file only.  If
binary (B), set to binary for this file only.  In clsof(), restore global file
mode from bsave.  This allows the sender to tell the C-Kermit receiver whether
the file is being transferred in text or file mode, so that you don't have to
type a "set file type { text, binary }" command on the C-Kermit receiver.
This code has no effect if the sender does not send the file-type attribute,
or if the C-Kermit receiver has "set attributes off".

4F(084) Mon Jul 10 20:47:51 1989

Get rid of index() function in tilde_expand(), ckufio.c.  Some systems
don't have it (like Xenix).

Fix directory command to allow ~name, and ~name/, as well as ~name/file.

Install missing help message for "set incomplete" and "set terminal".

4F(083) Wed Jul  5 12:09:50 1989

Add support for RT PC AIX 2.2 to ckutio (mostly lockfile stuff) and makefile,
from Ge van Geldorp, Netherlands).

Minor fixes to Zilog Zeus support from John R. Evans, IRS, Kansas City.

4F(082) Mon Jul  3 15:19:22 1989

Don't try to output to debug log in cmdini() in ckuusr.c, because it's not
open yet (Martin Maclaren, Bath Univ, UK).

Allow cd/cwd to also accept "~" notation in directory.  Required the addition
of a new parsing function, cmdir(), to ckucmd.c.  Hacked it in as quickly as
possible, mostly by killing stuff from a copy of cmifi().  Seems to work for
SUNOS and Ultrix.  Hope it doesn't break all the other versions...

Add tilde expansion to cwd() function in ckcfns.c, so that server can also
expand tildes in 'remote cwd' commands.  Also add tilde expansion in sinit()
when C-Kermit server executes the 'get' command.  Also in rcvfil() so it can
receive files into directories specified in tilde-notation.

Add tilde expansion to System-V based versions too.  Code for ckucmd.c from
Dave MacKenzie at Rockefeller U.  Those who have experience with other kinds
of systems (V7, Sys III, etc) should look at this code.  Should be simple to
get it working for any Unix variant.  See #ifdef DTILDE.

Move tilde-expansion code from ckucmd.c to ckufio.c.  Tilde-expansion code
is compiled based on existence of TILDE symbol, which is defined in ckcdeb.h.

Enable sending file timestamps from System V.  Code for ckufio.c from Dave
MacKenzie.  See #ifdef TIMESTAMP.

Clear up some packet-length confusion in pwp's new sdahead() encode-ahead
function, in ckcfns.c.  Previously, C-Kermit was sending slightly-longer-
than-negotiated packets.

Fix pwp's modification to zopeni() in ckufio.c.  File input buffer was not
being reset in all cases, resulting in leftover text from a previous transfer
being prepended to the next transfer.

Add "make next" to makefile, Mic Kaczmarczik, UT Austin Computation Center

4F(081) Thu Jun 22 12:26:04 1989

Add makefile entry for Berkely Unix 4.x with HoneyDanBer UUCP and clean up
lock-file selection conditionals and code in ckutio.c (Paul Placeway),.

From David MacKenzie, a couple small patches to make ckutio.c compile
correctly on recent versions of UNOS.

4F(080) Mon Jun 19 20:51:41 1989

Merge in changes from Chris Adie, Edinburgh University, Scotland, for OS/2
support:

 - New OS/2-specific modules:
     ckocon.c (terminal emulation), ckofio.c, ckutio.c.

 - Minor changes to the following files under #ifdef OS2 conditionals:
     ckcdeb.h, ckucmd.h, ckuusr.h, ckcmai.c, ckucmd.c, ckudia.c, ckuscr.c,
     ckuusr.c, ckuus2.c, ckuus3.c.

 - Add new material to Chris's ckofio.c OS/2 file-system support module:
     Limited file attribute support.
     Paul Placeway's buffered file input and output.

Chris Adie's work was based on an older C-Kermit, and so this two-way merge
was unavoidable.  The result is entirely untested and may not work at all, so
those with OS/2 development systems are urged to debug it and send back the
necessary fixes.

Change the interactive command parser, for BSD4.x only, to expand tildes in
filenames in SEND, RECEIVE, DIRECTORY, LOG, and similar commands.  This code
is all in ckucmd.c, under #ifdef BSD4 conditionals, in the cmifi() and cmofi()
functions.  AT&T UNIX users are invited to adapt it to System III, System V,
etc.

Add file creation date to attributes sent by C-Kermit (BSD 4.x only).

Change input() function in ckcfn2.c to avoid getting into retransmission loops
when it receives an ACK for the previous packet or a NAK for the next packet.

Restore lost comment delimiter in ckcpro.w, on "<serve>I" line, which
prevented type-2 or -3 block checks from being selected by the client.

Remove something that was added in 4F(077), i.e. using file descriptor for the
terminal in packet mode.  It turns out that this prevented Kermit from
sending/receiving files to/from standard input.

Changes for 4.1 BSD from Frank Prindle:
Make setegid() and seteuid() calls in ckuusr.c and ckufio.c conditional
upon BSD42, rather than BSD4, because 4.1 BSD doesn't support them.  In
file ckutio.c, tthang() shouldn't close and open the ttyfd, and ttpkt()
should choose the "old" line discipline.  Add special BSD41 entry in
makefile.

Another one from Frank Prindle: When assigning an external line for local-mode
operation, turn off ECHO bit in sg_flags.  This eliminates the problem of
bizzare delayed echoing when connecting back to a remote system after a file
transfer, which first appeared in 4E(072).  For the benefit of those still
running versions between then and now, the fix is to find the following lines
in function ttopen() in the file ckutio.c:

    gtty(ttyfd,&ttold);                 /* Get sgtty info */

and add the following line immediately after them:

    if (xlocal) ttold.sg_flags &= ~ECHO; /* Turn off echo on local line */

In ckucmd.c, change the name of the function digits() to rdigits(), because
digits is now apparently a reserved word on some systems, like NEC Astra XL
3.4 (Gary Holbrook).

Try to fix the hangup code.  In ckutio.c, function tthang(), where we close
and reopen the line, if the reopen fails, kill the lock file.  Add message,
"[hanging up]".  In ckucon.c, fix ^\h escape (hangup) in connect mode to wait
until tty port reader fork terminates.  Add ^\q escape (hangup and quit from
Kermit).  All this from Patrick Wolfe, Kuck & Associates, Inc, pat@kai.com.

"mail" has been changed to "Mail" to ensure that the Berkeley version will
be used, which accepts a "-s" switch on the command line for subject.

Add support for Microcom ax9624 modem from Jim Knutson in ckudia.c.

Remove #include <sys/file.h> for Apollo aegis in ckutio.c (Martin Maclaren).

4F(079)

Add 'transmit' command for raw uploading.  For now, there's no way to
interrupt it.

4F(078)

Changes by Paul Placeway, Ohio State University, to speed up decoding of
Kermit packets and writing out to files.  Also code from Paul to dynamically
size outbound packets based on the frequency of retransmissions - the noisier
the line, the shorter the packets, the cleaner the line, the longer the
packets (up to the maximum negotiated length).

C-KERMIT FOR UNIX, CHANGES FROM VERSION 4E(072) TO 4F(077), 1 Apr 89

A somewhat major new release, in beta-test form (but if it tests ok,
it can become a real release without requiring any further changes).

ATTRIBUTE PACKETS.  Minimal support for attribute packets added: ckcpro.w,
ckcdeb.h, ckcfn2.c, ckufio.c, ckuus*.c.  C-Kermit can send Attribute packets
containing system ID, file sizes (K and bytes), and encoding method (text or
binary), and will honor positive and negative responses.  It will also receive
Attribute packets (see below).  In the ckuus* modules, the command 'set
attributes {on, off}' was added, to allow Attribute packet processing to be
disabled in case of misunderstandings; it is enabled by default.

IMPORTANT: ckcpro.w calls a new function, sattr(), which is defined in
ckcfn2.c.  The sattr() function, in turn, calls zsattr(), which MUST BE
DEFINED in in each and every ck?fio.c module.  So far, it has only been
defined in ckufio.c, for Unix.  Macintosh and VMS Kermit developers -- be sure
to add this function to your system-dependent code.  In the future, a similar
function will have to be added to ck?fio.c to modify an incoming file's
attributes.

C-Kermit receives and processes attribute packets, and fills in an attribute
structure.  So far, C-Kermit does nothing with these attributes except for
"Disposition" (Attribute "+").  If the disposition is M, then the file is
mailed to the designated address(es).  If the disposition is P, then the file
is printed with the specified options.  These operations are currently done
in the crudest possible way (via "system()"), and only for UNIX.

EFFICIENCY: Modifications from Paul Placeway at Ohio Statue University that
dramatically speed up C-Kermit when sending.  Changes as follows:
 ckcker.h - define a file input macro similar to getc(), and a buffer size.
 ckufio.c - function zinfill() added to fill input buffer, zchin() modified
            to use buffered input.  NOTE: zinfill() will have to be added to
            all the other ck?fio.c modules (Macintosh, VMS, etc etc).
 ckcfns.c - getpkt() totally rewritten and demodularized.  It used to be
            pretty, but now it's fast.  getchx() and encode() copied inline.

The SET SERVER TIMEOUT command was added to control the rate at which the
C-Kermit server issues NAKs during command wait, 0 = no NAKs at all.  Changes
to ckuus*.c, ckuusr.h, ckcfns.c, ckcmai.c.  The server's periodic NAKs can
interfere with originate/answer devices like digital PBXs or autodial modems,
putting them in originate mode when the user wanted the device to be in answer
mode.  SET SERVER TIMEOUT 0 can now be used in such situations.

MAKE C-KERMIT SEND NAKs: ckcpro.w, ckcfns.c, ckcfn2.c, ckcmai.c.  Up till now,
C-Kermit has always responded to a corrupted packet or a timeout by resending
its previous packet.  It turns out that when talking to a more generalized
Kermit program -- i.e. one that provides for sliding-window packet transfer,
in which a window size of 1 is just a special case -- that it is better for
C-Kermit to send NAK packets in response to corrupted packets or timeouts,
which a sliding-windows Kermit will act upon immediately.  This is done by
adding a flag variable, nakstate, in ckcmai.c.  This variable is set to 1 in
ckcpro.w before rdata state is entered.  In the input() function (ckcfn2.c), a
NAK is sent in response to a timeout or corrupted packet if nakstate != 0,
otherwise the previous packet is resent, as before.  In function tinit()
(module ckcfns.c) nakstate is reset to zero at the beginning of each
transaction.

ckcpro.w: Cure a longstanding bug.  When in <sseof>Y state, if there's another
file to send, the transition is to state ssfile, not ssdata!  The problem was
that if C-Kermit was sending a file whose name began with X or Z, and the
other Kermit echoed back the filename in the data field of the ACK packet (as
C-Kermit itself does), the improper immediate transition into ssdata state
caused the ACK data field to be checked for X or Z, which is the signal for
file interruption.  The fix prevents the data packet protocol from looking in
the ACK to the file header.  The reason it escaped notice for so long is that
it could only happen when sending a wildcard group of files with names
starting with X or Z and with SET FILE NAMES LITERAL (which forced the
normally lowercase X's or Z's to be uppercase) from one C-Kermit to another
C-Kermit (actually, could also have happened a lot with Mac Kermit too).

ckcpro.w: Reformat and comment.  No longer try to preserve the illusion that
Kermit is such a simple protocol it can fit on 2 pages...

ckcfns.c: In tinit(), set spktl = 0, so that a 'server' command given after
some other command will transmit a NAK(0), rather than whatever the last
packet happened to be (this bug had been there forever).  In sinit(), make
sure that C-Kermit sends an error packet if a 'get' command to the C-Kermit
server results in too many filenames.

ckwart.c: Change data type of state transition array from short to CHAR.  Save
several more K.

VMS support: Add changes from Mark Buda & Barry Archer to ckuusr.c within
"#ifdef vms" conditionals -- VMS-specific way to find init file, and special
handling of DIRECTORY command.

ckuusr.c: Add some debugging info to trap().

ckuus2.c: In rdebu(), change reference to rdatap (which could sometimes
be uninitialized) to data+1, which always works.  This one could cause core
dumps with 'set debug on' at beginning of file transfer.

ckuus3.c: In screen(), always issue error or warning messages (even if
in quiet or no-display mode).

ckutio.c: Many changes, mainly to prevent opening of terminal in O_NDELAY
mode, skip the exclusive access baloney, hanging up, etc etc, when terminal is
job's controlling tty.  Also, if terminal is job's controlling tty, use file
descriptor 0 (stdin) rather than obtaining a new file descriptor on it.  This
allows UNIX "idle line monitors" to properly detect Kermit activity and not
log out Kermit users in the middle of 40-megabyte file transfers because the
tty line appears to be idle.

ckufio.c and ckutio.c: Add UNOS support from David MacKenzie,
edf@rocky2.rockefeller.edu.  Add function zinfill() for buffered file input,
from Paul Placeway.

ckudia.c: Slightly better support for Hayes modems -- try to catch the case
where user dials out at 2400 but gets connected at 1200.

---
## [KermitProject/ckermit](https://github.com/KermitProject/ckermit)@[69527a3171...](https://github.com/KermitProject/ckermit/commit/69527a317184b81acd27c9beb2b771685e3cbb8c)
#### Saturday 2022-02-12 05:51:23 by Kermit Project

C-Kermit 304(dev06) 2013/07/25 Unix VMS

Sure enough the next day this caught mistakes in TWO of my overnight cron
job scripts: One was "if not <misspelled variable name>".  The other was
"if neq ...".  There is no "if neq".  Added IF NEQ, IF LLE, IF LGE, since
even I expected them to be there.  ckuus[26].c, 16 Apr 2016.

Added a 9th element to the \ffileinfo() result array: analysis of contents
of the file, if it is a regular file (not a directory or a link):

  text:7bit      7-bit text (e.g. ASCII, ISO 646)
  text:utf8      Unicode 8-bit Transformation Format (UTF-8)
  text:ucs2      Raw Unicode
  text:8bit      8-bit text (e.g. ISO 8859-1, Windows CP 1252)
  text:unknown   Text, unknown encoding
  binary         Binary (e.g. an executable, object, or image file)

This analysis is performed using the same file scanner that is used during
file transfer to set up text mode versus binary mode, and to set up the
character-set conversion if possible.  If the file is not a regular file,
the 9th element is empty.  Suppose the array is \&a[].  Then:

  if equ "\fleft(\&a[9],4)" "text"  (or if equ "\fword(\&a[9],1) "text")

or:

  if neq "\&a[9]" "binary"

the file is a text file, not a binary file, a directory file, or a link.
This is useful if you don't care about the encoding.  ckuus4.c, 16 Apr 2013.

For convenience, two new IF conditions have been added: IF BINARY filename
succeeds if the named file is a binary file (meaning that it would be
transferred in binary mode by Kermit): an executable program, an object
file, an image file, etc.  IF TEXT filename succeeds if the named file is a
text file, such as the file you are reading, or program source code, or an
HTML or XML file, etc, regardless of the character encoding.  If the file is
a directory, both IF TEXT and IF BINARY fail.  If the file is a link, the
result reflects the contents of the linked-to file.  ckuus[26].c, 17 Apr 2013.

Looked into making ==, if >, etc, work with strings, as one might expect
from other languages like Javascript.  Turned out to be unworkable because
these constructions accept not only numeric constants and numeric-valued
variables, but also arithmetic expressions.  The idea would have been that
if either of the two operands was non-numeric once evaluated, lexical
comparison would be done instead of arithmetic comparison.  The fly in the
ointment is something like this:

  if > x*(x+1) 2000 ...

When the arithmetic comparison operators are used, Kermit knows
that the operands must be numbers, so any non-numeric strings like 'x'
in the example above are automatically treated as macros and evaluated.  But
if we check first to see if the string is non-numeric, it will be, and the
same evaluation will not be done, and the the operands will be compared as
strings, giving a result that could only be right by accident.

Built on Linux RH 5.9 x86_64, 18 Apr 2013.

But when doing the Kerberos+SSL build:

 -L/usr/kerberos/lib -L/usr/local/ssl/
lib -lssl -ldes425 -lpam -lz -lcrypto -lgssapi_krb5 -lkrb5 -lk5crypto
-lcom_err -lncurses -lutil -lresolv -lcrypt  -lm

?OpenSSL libraries do not match required version:
  . C-Kermit built with OpenSSL 1.0.1c 10 May 2012
  . Version found  OpenSSL 0.9.8e-fips-rhel5 01 Jul 2008
  OpenSSL versions prior to 1.0.0 must be the same.
  Set LD_LIBRARY_PATH for OpenSSL 1.0.1c 10 May 2012.
  Or rebuild C-Kermit from source on this computer to make versions agree.
  C-Kermit makefile target: linux+krb5+ssl
  Or if that is what you did then try to find out why
  the program loader (image activator) is choosing a
  different OpenSSL library than the one specified in the build.

Added a CHANGE command that's part of the DIRECTORY / TOUCH family, with most
of the same file-selection switches:

  CHANGE /switches filespec string1 [ string2 ]

Example:

  CHANGE /RECURSIVE ~/web/*.html http://www.oldsite.com http://www.newsite.com

The syntax of the command is a little annoying because Unix users would
expect the filespec to come last, but the command shares a vast amount of
parsing and execution code with DIRECTORY and TOUCH, which I didn't want to
duplicate.

CHANGE-specific switches:

  /CASE:{ON,OFF} - Honor/Ignore alphabetic case when searching for string1
  /MODTIME:{PRESERVE,UPDATE} - Modtime for changed file
  /SIMULATE - Say which files would be changed without changing them.

ckuusr.[ch], ckuus6.c, 3 May 2013.

Updated SUPPORT command text.  ckuus2.c, 3 May 2013.

Suppose you want to do something to all the files whose names match a
certain pattern and that contain a certain string or text that matches a
certain pattern.  For example, in a website with thousands of html files,
all the ones that contain links to a site that disappeared.  How to get a
list of such files?  I added an /ARRAY:&x switch to Kermit's GREP command
for this.  Then after the GREP command the resulting array can be accessed
in a loop to process the desired files -- delete, rename, transfer, etc.
Element 0 of the array tells now many files contained a match and how
many elements are in the array (1-based).  ckuus6.c, 22 Jul 2013.

Added HELP CHANGE text.  ckuus2.c, 22 Jul 2013.

CHANGE works by copying each file to a temporary directory, making changes
to the the copy, and then renaming the copy over the original file.  It was
doing this for all files, even when they weren't actually changed (i.e. did
not contain string1).  Also if \v(tmpdir) was defined to be a directory that
did not exist, the CHANGE command didn't try to create it.  Both fixed in
ckuus6.c, 22 Jul 2013.

Until now there was no straightforward way to extract a field from a
date-time string.  As a start, I added a new output format, 5, for
\fcvtdate(), to make the result be numeric with fields delimited by ':', for
example: 2013:07:22:15:19:43.  Any desired field can be extracted with
\fword(), for example to get the current year: \fword(\fcvtdate(,5),1), or
for the current month \fword(\fcvtdate(,5),2).  And so on.  Since each field
is numeric, it can index into tables of (say) month names or day names in
the desired language and character-set.  ckucmd.c, 22 Jul 2013.

Added \v(year), which evaluates to the current year, e.g. 2013.  Mainly
because I keep expecting it to be there.  Also \v(month) (three-letter month
abbreviation, English) and \v(nmonth) (2-digit month number, 01-12).
ckuusr.h, ckuus4.c, 22 Jul 2013.

Note that \v(month) and \v(day) are not ideal -- abbreviations, not full
names, and English only.  I added \v(month) and \v(nmonth) only for symmetry
with \v(day) and \v(nday).  These shortcomings are remedied in the next items.

Put a locale_dayname() function in ckutio.c.  This is compiled if
HAVE_LOCALE is defined and NO_LOCALE is not defined.  HAVE_LOCALE is defined
for BSD44 and POSIX, VMS, OS/2, and Windows.  These definitions can be
adjusted if necessary in ckcdeb.h and NO_LOCALE can be included on the make
command line to override in case of trouble.  ckcdeb.h, ckutio.c,
23 Jul 2013.

Added \fdayname(date,fc), where date can be any free-format date/time
string, with or without the time, or omitted to give the name of the current
day.  fc is a function code: 0 to return the name in full, nonzero to
abbreviate it according to the locale; if fc is omitted, the abbreviated
form is returned.  The full or abbreviated day name is returned in the
language and character set specified or implied by the locale if the
underlying platform is configured for it; otherwise they come out in
English.  These routines builds upon all of the date-time code that was
added in 2003, particularly cmcvtdate(), the free-format date parser, and
mjd(), that calculates a Modifed Julian Date, from which the day of the week
can be derived by a simple modulus.  This function pretty much supersedes
\fday() (which returns only the 3-letter English day name), but \fday()
remains available for compatibility.  ckuusr.h, ckuus4.c, 24 Jul 2013.

Added locale_monthame(month,fc), like locale_dayame(day,fc) but for months.
ckutio.c, 24 Jul 2013.

Added \fmonthame(), like \fdayname() but for months.  ckuusr.h, ckuus4.c,
24 Jul 2013.

Added HELP text for \fmonthame() and \fdayname().  ckuus2.c, 24 Jul 2013.

Developed, built and tested on NetBSD with English, Spanish, and German.
Built and tested OK on Linux RHEL5 with the same languages.
Built OK on Solaris 9, which supports the locale APIs, but does not have
any locales installed except en_US.  24 Jul 2013.

CAUTION: Except where C-Kermit is explicitly dealing with multibyte
character sets, such as in file transfer and in the terminal emulator, there
is no special support for multibyte character sets such as UTF-8, Shift-JIS,
etc.  So while \fupper(), \flower(), and \fcapitalize() can work with
ISO-8859-1, KOI-8, and other single-byte character sets, they won't work
with UTF-8 because they are just byte loops, unless the underlying isupper,
tolower, etc, functions (or macros, or whatever they are) do some magic.
Ditto for Shift-JIS, Japanese EUC, etc.

A new command-line options, --nolocale, was added to disable use of the
locale and to force the "C" locale.  Also, if the environment variable
K_NOLOCALE is set to a nonzero integer value.  ckuusr.h, ckuusy.c, ckcmai.c,
24 Jul 2013.

---
## [chandu078/kernel_oneplus_sm8350](https://github.com/chandu078/kernel_oneplus_sm8350)@[6af355fd22...](https://github.com/chandu078/kernel_oneplus_sm8350/commit/6af355fd2258dd9fd56e0a278047806a8a459e7a)
#### Saturday 2022-02-12 06:01:34 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: aswin7469 <aswinas@pixysos.com>
Signed-off-by: mukesh22584 <mks22584@gmail.com>
Signed-off-by: chandu078 <chandudyavanapelli03@gmail.com>

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[dd747fcc5a...](https://github.com/san7890/bruhstation/commit/dd747fcc5a46df051a5fe0e42950c46c72269244)
#### Saturday 2022-02-12 06:24:55 by MrMelbert

BIDDLE HERETICS: Heretic revamp! (Shadow Realm, UI Overhaul, Refactoring, and Murderhoboing Tweaks)  (#64658)

About The Pull Request

This PR seeks to revamp heretic in it's almost entirety.

Closes #58435
Closes #62114
Closes #63605

image
Gameplay changes:

    The heretic no longer starts with a Codex Cicatrix or a Living Heart.
        Heretics now draw transmutation runes by using any writing tool while having Mansus Grasp active.
            The Mansus Grasp can be used to remove heretic runes.
        Draining influences can be done with "right click".
            While draining, people who examine you may get a message hinting that you're interacting with an influence.
            Drained influences can also be dispersed with anomaly neutralizers!
        The Codex Cicatrix is now a researchable item that lets you gain additional knowledge from influences.
            The Codex can still draw and remove runes, and does it faster.
        The Living Heart is now the heretic's heart. Literally. It's the heart in their chest. Their heart takes on the appearance of a living heart, and they can pulse it on demand to track their targets. This makes an audible noise.
            If your heart is lost (you're disemboweled or whatever), you need to do a ritual to regain it!

    Casting any heretic spell (besides Grasp) requires a Focus.
        A Heretic Focus is a neck item they can transmute.
        Heretic robes also function as a focus when toggled up.
        Ascending also disables the need for a focus, because of course.

    Heretics now gain 1 knowledge point passively every 20 minutes.

    Sacrificing has been revamped entirely.
        A heretic now gains four sacrifice targets on spawn.
            One random crewmember
            One member of their department
            One member of security
            One member of command (a "high value" sacrifice)
        You can sacrifice people who are in in soft-crit, hard-crit, or dead.
        Sacrificing someone will cuff them (if they are not), HEAL them, revive them, and set them unconscious. After a short time. they will be sent to a shadow realm. This shadow realm is themed to your heretic type.
            The shadow realm is a 2 minute long survival challenge where the sacrificee is subject to a constant barrage of shadowy hands.
            If they survive, they are teleported back to a random turf with no memory of how they got there. They'll also slur a TON to get the point across.
            If they die, their corpse is teleported back to a random turf on the station.

    No more multi-hearting! Your targets are your own.
        BUT adds a knowledge that allows heretics to reroll their sacrifice targets with a ritual.

    Each path now has a "Rituals of Knowledge". These are randomly generated rituals that may be difficult to complete but awards knowledge points in return.

    Ascending now has some requirements.
        To learn the ascension ritual, you need to complete all of the objective you are assigned.
        The ascension ritual now each have a varied requirement, instead of "needing 3 bodies" only.

    Other minor gameplay changes:
        Lots of balance tweaking.
            Buffed some summons.
            Buffed the Lord of the Night very slightly.
            Nerfed the Madness Mask.
        Put a limit on the amount of blade transmutations possible at once. 3 for flesh, 2 for other paths.
        Logs of BUG fixing.
        Rust Grasp is now based on right click for surfaces instead of combat mode.
        General grammar and flavor tweaks a ll around.

Admin / code changes:

    Revamped the way heretics appear within the traitor panel.
        You can now easily see who they're targeting for sacrifice and what they have researched
        Also adds some helpful buttons to heretics, like giving them points!
    Refactored much, much of heretic code
        LIKE ALL OF HERETIC CODE WAS IN 4 FILES.
            Split up all the knowledge, spells, and items that belong to the heretic into their own files and folders.
        Not only that, but everything internally was still named "Eldritch Cultist" and similar.
            Almost every mention of "Eldritch Cultist" has been properly replaced by "Heretic".
    Much better reference handling all around.
    General code improvements over heretic stuff.
    Unit tests, because of course.

Todo

Sprites for the focus

    Look at adding 1-2 other objectives prior to ascension. Theft? Special rituals? ("Rust [x] tiles to be able to ascend")

Why It's Good For The Game
Okay but why?

Heretics are not in a good place at the moment, this much is clear. They've been completely disabled on MRP for this reason.

The reasoning is simple: A lot of murder.
There's nothing inherently wrong with an antagonist heavy with murder, but the Heretic really missed the mark.
Gib, gib, gib, then ascend so you can keep killing.

In the background, the Heretic was FULL of flavorful spells, rituals, and "lore" stolen from Cultist Simulator that was unfortunate enough to be shackled to the heretic's gameplay loop.

So, this revamp aims to amend that:

Dial back the heretic's focus on mass murder and put more focus on the heretic's interesting flavor.
Spooky maintenance rituals, knowledge seeking maniac.

    Sacrifice no longer outright kills / requires murder, meaning a heretic can progress without racking up a bodycount.
    Influence is gained passively over time, so they can spend influence on more interesting side paths.
    Side paths are required to progress to ascension, so they're encouraged to explore new things.

Ultimately, while there still may be a little way to go, this PR seeks to take a good leap in starting it.
Changelog

cl Melbert
add: Large scale heretic revamp!
expansion: The Codex Cicatrix is no longer a roundstart heretic item. Research is handled through their antag info UI. Rune drawing is done by using a writing tool with Mansus Grasp active in your offhand. The actual Codex is an unlockable ritual item now.
expansion: The Living Heart is no longer a roundstart heretic item - their actual heart now becomes their Living Heart, and it makes a sound when triggered. Losing your heart (being disemboweled) will require you to do a ritual to regain it.
expansion: The Hereic Antag UI has been overhauled, and now hosts much of their mechanics as well as providing some helpful tips for newer players.
expansion: Most heretic spells now require a focus to cast. All heretics can make a basic focus necklace, and some heretic equipment also functions as a focus. (Credit to Imaginos for the focus sprite!)
expansion: Heretics now passively gain +1 influence every 20 minutes.
expansion: Heretic sacrificing has been reworked. You can now sacrifice people who are in soft crit or weaker. Sacrificing someone heals them, cuffs them, and teleports them to the SHADOW REALM, where they must dodge a barrage of hands to survive. Survive long enough and you return without memory - die, and your body will be thrown back.
expansion: Heretics now have a few new rituals, including the Ritual of Knowledge, a randomly generated ritual that awards knowledge points.
expansion: Heretic ascension now has a few requirements - you must complete your objectives assigned to you prior to learning the final ritual, and all the final rituals have been changed a bit!
qol: Using the Heretic's Mansus Grasp on surfaces (EX: Rust Grasp) now works on right-click, instead of combat mode.
qol: Used heretic influences can now be removed with a Anomaly Neutralizers.
balance: Some heretic rituals are now limited in the amount they can make. You can only have up to 2 heretic blades crafted at once (3 if you are Path of Flesh).
balance: The Lord of the Night has been buffed to be a little scarier. Did you know the Lord of the Night can eat arms to regain body parts and heal?
balance: Buffed some heretic summons - mostly their health pools.
balance: Nerfed the heretic's Mask of Madness. It can no longer infinite stam-crit you.
balance: Nerfed the heretic's ash mark.
balance: Nerfed a bunch of on-hit-heretic-blade effects. Many effects only apply on mark detonation now: Void blade silence, flesh blade wounds, ash blade gasp cooldown refund.
fix: Fixed quite a few bugs and unintended behaviors with heretic code.
refactor: Refactored and improved much of Heretic code. Improved the file structure dramatically.
admin: The heretic's traitor panel has been beefed up a bit.
/cl

---
## [v4lkyr/whyred](https://github.com/v4lkyr/whyred)@[9b555adb01...](https://github.com/v4lkyr/whyred/commit/9b555adb01b20f263522048a9a63740893ed8c87)
#### Saturday 2022-02-12 07:49:21 by Peter Zijlstra

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
Signed-off-by: v4lkyr <valkyr23@gmail.com>

---
## [TerryCavanagh/VVVVVV](https://github.com/TerryCavanagh/VVVVVV)@[e93d8989d3...](https://github.com/TerryCavanagh/VVVVVV/commit/e93d8989d3e82e5afc52e09fd7aeae3d41644e64)
#### Saturday 2022-02-12 09:12:09 by Misa

Revert "Fix Secret Lab Time Trial trophies having wrong colors"

As reported by Dav999, Victoria and Vermilion's trophy colors are
swapped again in 2.4. He points to
37b7615b71c3a2f44e03c47894383107850812ff, the commit where I fixed the
color masks of every single surface to always be RGB or RGBA.

It sounded plausible to me, because it did have to do with colors, after
all. However, it didn't make sense to me, because I was like, I didn't
touch the trophy colors at all after I originally fixed them.

After I ruled out the RGBf() function as a confounder, I decided to see
whether intentionally reversing the color order in RGBf() to be BGR
would do anything, and to my surprise it actually swapped the colors
back around and it didn't actually look bad.

And then I realized: Swapping the trophy colors between RGB and BGR
ordering results in similar colors that still look good, but are simply
wrong, but not so wrong that they take on a color that no crewmate uses,
so it'd appear as if the crewmates were swapped, when in reality the
only thing that was swapped was actually the color order of the colors.

Trying to fix this by swapping the colors again, I actively confused
colors 33 and 35 (Vermilion and Victoria) with colors 32 and 34
(Vitellary and Viridian), so I was confused when Vermilion and Victoria
weren't swapping. Then as a debugging step, I only changed 34 to 32
without swapping 32 as well, and then finally noticed that I was
swapping Vitellary and Viridian, because there were now two Vitellarys.
And then I was reminded that Vitellary and Viridian were also wrongly
swapped since 2.0 as well.

And so then I finally realized: The original comments accompanying the
colors were correct after all. The only problem was that they were fed
into a function, RGBf(), that read the colors backwards, because the
codebase habitually changed the color order on a whim and it was really
hard to reason out which color order should be used at a given time, so
it ended up reading RGB colors as BGR, while it looked like it was
passing them through as-is.

So what happened was that in the first place, RGBf() was swapping RGB to
BGR. Then I came and swapped Vermilion and Victoria, and Vitellary and
Viridian around. Then later I fixed all the color masks, so RGBf()
stopped swapping RGB and BGR around. But then this ended up swapping the
colors of Vermilion and Victoria, and Vitellary and Viridian once again!

Therefore, swapping Vermilion and Victoria, and Vitellary and Viridian
was incorrect. Or at least, not the fix to the root cause. The root
cause would be to swap the colors in RGBf(), but this would be sort of
confusing to reason about - at least if I didn't bother to just type the
RGB values into an image editor. But that doesn't fix the real issue,
which is that the game kept swapping RGB and BGR around in every corner
of the codebase.

I further confirmed that there was no more RGB or BGR swapping by
deleting the plus-one-divide-by-three transformation in RGBf() and
seeing if the colors looked okay. Now with the colors being brighter, I
could see that passing it straight through looked fine, but
intentionally reversing it to be BGR resulted in colors that at a
distance looked okay, but were either washed out or too bright. At least
finally I could use my 8 years of playing this game for something.

So in conclusion, actually, 37b7615b71c3a2f44e03c47894383107850812ff
("Fix surface color masks") was the real fix, and
d271907f8c5d84308a3cf9323ac692199b8685a6 ("Fix Secret Lab Time Trial
trophies having wrong colors") was the real regression. It's just that
the regression came first, but it wasn't really a regression until I did
the other fix, so the fix isn't the regression, the regression is...
this is hurting my brain. Or the real regression was the friends we made
along the way, or something like that.

This is the most trivial bug ever caused by the technical debt of those
god-awful reversed color masks.

---

This reverts commit d271907f8c5d84308a3cf9323ac692199b8685a6.

Fixes #862.

---
## [ddugovic/Stockfish](https://github.com/ddugovic/Stockfish)@[cb9c2594fc...](https://github.com/ddugovic/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Saturday 2022-02-12 10:31:24 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [FiendsOfTheElements/FF1Randomizer](https://github.com/FiendsOfTheElements/FF1Randomizer)@[acf3894385...](https://github.com/FiendsOfTheElements/FF1Randomizer/commit/acf3894385a4a8f4eb9a80ad6c5c10c6787575c0)
#### Saturday 2022-02-12 10:59:06 by mhn65536

Mhn65536/mpool (#804)

* Tournament Item magic Pool
Lower Thief Agility Settings
Buff Tier1 Damage Spells

* fix

* oops

* i hate my life

* guaranteed tent

* alter magic pool

Co-authored-by: x.y <x.y@z>

---
## [scummvm/scummvm](https://github.com/scummvm/scummvm)@[dc4cfa05fe...](https://github.com/scummvm/scummvm/commit/dc4cfa05fe77224adf8c806309145e881d4ea8b9)
#### Saturday 2022-02-12 11:03:54 by Torbjörn Andersson

SCUMM: Display Loom Overture Timing value as time, not a magic number

It makes it less obvious what the default was, but I think this is a lot
more user friendly. For some reason, it looks awful in RTL languages,
but I have no idea how to fix that.

---
## [cpdt/NorthstarLauncher](https://github.com/cpdt/NorthstarLauncher)@[2bc20f0eef...](https://github.com/cpdt/NorthstarLauncher/commit/2bc20f0eefd20fbd9f48d188221fec90c8c4b438)
#### Saturday 2022-02-12 11:54:16 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [chandru89new/xpns](https://github.com/chandru89new/xpns)@[6986047cce...](https://github.com/chandru89new/xpns/commit/6986047cced5aadd08748bc7608d0d8aaa719063)
#### Saturday 2022-02-12 12:54:59 by Chandru

Fix auth URL

Blood Google! All of a sudden, it started throwing 500 on an older authUrl. I spent a better part of my Saturday troubleshooting this. In my attempts to debug, I had to complete recreate an Elm web app to check what exactly was causing the 500 on the original authUrl. Fucking hell.

---
## [greck2908/VVVVVV](https://github.com/greck2908/VVVVVV)@[57dca99a4e...](https://github.com/greck2908/VVVVVV/commit/57dca99a4e9fb07185de90cd70def42b17549fb6)
#### Saturday 2022-02-12 13:31:51 by Misa

Ax OverlaySurfaceKeyed(), set proper foregroundBuffer blend mode

So, earlier in the development of 2.0, Simon Roth (I presume)
encountered a problem: Oh no, all my backgrounds aren't appearing! And
this is because my foregroundBuffer, which contains all the drawn tiles,
is drawing complete black over it!

So he had a solution that seems ingenius, but is actually really really
hacky and super 100% NOT the proper solution. Just, take the
foregroundBuffer, iterate over each pixel, and DON'T draw any pixel
that's 0xDEADBEEF. 0xDEADBEEF is a special signal meaning "don't draw
this pixel". It is called a 'key'.

Unfortunately, this causes a bug where translucent pixels on tiles
(pixels between 0% and 100% opacity) didn't get drawn correctly. They
would be drawn against this weird blue color.

Now, in #103, I came across this weird constant and decided "hey, this
looks awfully like that weird blue color I came across, maybe if I set
it to 0x00000000, i.e. complete and transparent black, the issue will be
fixed". And it DID appear to be fixed. However, I didn't look too
closely, nor did I test it that much, and all that ended up doing was
drawing the pixels against black, which more subtly disguised the
problem with translucent pixels.

So, after some investigation, I noticed that BlitSurfaceColoured() was
drawing translucent pixels just fine. And I thought at the time that
there was something wrong with BlitSurfaceStandard(), or something.
Further along later I realized that all drawn tiles were passing through
this weird OverlaySurfaceKeyed() function. And removing it in favor of a
straight SDL_BlitSurface() produced the bug I mentioned above: Oh no,
all the backgrounds don't show up, because my foregroundBuffer is
drawing pure black over them!

Well... just... set the proper blend mode for foregroundBuffer. It
should be SDL_BLENDMODE_BLEND instead of SDL_BLENDMODE_NONE.

Then you don't have to worry about your transparency at all. If you did
it right, you won't have to resort this hacky color-keying business.

*sigh*

---
## [elytraOS/packages_apps_Launcher3](https://github.com/elytraOS/packages_apps_Launcher3)@[084eb0c6f9...](https://github.com/elytraOS/packages_apps_Launcher3/commit/084eb0c6f985dc1675491f93d51b144856f18c1a)
#### Saturday 2022-02-12 13:33:20 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [geode-sdk/sdk](https://github.com/geode-sdk/sdk)@[cb4a6b351a...](https://github.com/geode-sdk/sdk/commit/cb4a6b351aacf4de793319a6d7b51225cc148249)
#### Saturday 2022-02-12 16:17:01 by HJfod

fix the stupid fucking piece of shit invalid hex fucking cock
motherfucker perkeleen paskasaatana pirunhelvetin shitass piece of cum
garbage

---
## [TeodorD420/tgstation](https://github.com/TeodorD420/tgstation)@[a2fa7799f3...](https://github.com/TeodorD420/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Saturday 2022-02-12 16:32:53 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [JessyDL/m.css](https://github.com/JessyDL/m.css)@[915ffcbed5...](https://github.com/JessyDL/m.css/commit/915ffcbed545b9c38f55fac07f33ef04433863a8)
#### Saturday 2022-02-12 17:45:01 by Vladimír Vondruš

package/ci: go back to Pelican 4.2 until I find a fix.

OH GOD, one can't just leave a project alone for 6 months because every
damn thing just breaks, changes or gets removed. Kids these days, FFS.

Imagine if the standard of electrical outlets changed rapidly every two
weeks, you'd just have to constantly buy new fucking adapters and you
would HATE it. So why is it COMPLETELY FINE with software?!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c146df4a26...](https://github.com/mrakgr/The-Spiral-Language/commit/c146df4a264d65a08722569975767911823bfd77)
#### Saturday 2022-02-12 18:59:24 by Marko Grdinić

"11:30am. The gaming sessions are too good, and I am getting up late again. Sigh. I guess I'll skip the morning session. Let me have breakfast here. Then I'll do the chores. After that I'll figure out how to do basic modeling in Houdini. I had time to think about it.

1pm. Done with chores and breakfast. It is time to start. I need to get my Houdini basic modeling skills up to par. The things I learned in the Hipflask course are absolutely vital for that. If it wasn't for it, I'd be hosed right now. I need to do these props so I can move to texturing. I actually have no exp in that, and it will be a challenge I need to surmount.

1:20pm. I have a good feeling as I do my modifications.

I actually did one of the two supporting beams for the sunbed. It is positioned properly. And right now I am thinking how to follow up on that. The way I did it, I can't just copy it to the other end.

> Edit has an optional second input for reference geometry. When the second input is connected, the Edit node transforms your edits relative to the differences between the geometry to edit and the reference geometry.

Right now I am reading the docs for the edit node. I need to think about it. The edit node has so much stuff in it, and I need to get familiar with it. The edit node is in fact the equivalent of edit mode in Blender.

Now what is this ref geometry. I really need somebody to show me more in depth. Words will only get you so far.

1:40pm. The Edit node has two examples. I need to take a look at them.

Hmmm, I just realized that the examples have object networks inside object networks. But I can't find a way to do that using tab. I wonder how that could be done?

1:50pm. The first example is so ambiguous. It is supposed to demonstrate editing with ref geometry, but even if I cut the wire, I still get the same result.

The other example is literally just a plain grid. Houdini does have some 'just doing our job' style corporate laziness baked into its design.

I really wish I could access the rest of the Hipflask vids for free.

...I decided to make a request in the piracy thread, but I doubt I'll get anything.

Let me leave that aside. Let me redo the beam from the start.

https://www.sidefx.com/docs/houdini/nodes/obj/viewportisolator.html
> The Viewport Isolator is similar to the viewport’s View Mode display option that lets you ghost or hide other objects, but it doesn’t restrict you by the OBJ hierarchy.

I'll have to check out that view mode. Nevermind it for now.

2:40pm. https://www.sidefx.com/forum/topic/5907/
Q: Edit SOP's Reference geometry input does what exactly?

I'll have to figure this out.

Right now I am thinking about the beam. Yes, I did it, but I did not do it exactly right. The sharing is not there.

https://youtu.be/GHyZVT6t0Z4?t=361

The only thing I am wandering about is the normals are usually a vertex attribute, but here they are tagged to points. How does that work?

3:15pm. I am thinking of dropping Houdini again. This is so annoying.

3:50pm. Let me take a short break here. I figured out how to make edits local. The second input to the node is key after all.

5pm. It is true that the break was overly long, but I am still thinking about it.

No, the way I've done the beams is not right. Damn.

5:15pm. https://www.sidefx.com/docs/houdini/basics/objects.html
> This is not to say that transforming at the geometry level is bad: often you need an object’s shape to deform over time. However, you should remember to look for opportunities to accomplish your goals by transforming objects before you look at transforming surfaces, because the former is more efficient.

Fuck. I made a serious mistake!

5:50pm. I am so obsessed with this, that I haven't had time to do actual modeling.

Throughout this whole scene, I've made a big blunder! I've been transforming things inside objects everywhere.

Here today with this sunbed I've been bashing my head how I can do my modeling exactly in place only to realize that the best way to do that is to just use objects.

Is there a way to have the construction plane match the object's axis? I'll have to look into that.

6:10pm. Done with lunch.

7:25pm. Let me just close here. I did the sunbed and thne spent the whole day in thought. This totally reminds me of programming. Today I think I completely internalized the uses of construction planes. I do not think that those curves will be giving me any more trouble.

I also noticed that align tool in the modify shelf.

7:35pm. Agh, I am still thinking about it. To think I'd spend an entire day brainstorming just how to properly set objects.

But it is important part of the modeling technique. The fact that I could not do the entryway posts using curves was quite sad. I really needed to dwell for a bit on what I learned in the Hipflask course.

With this, I'll deal with the towel rack tomorrow. Well, the rack itself will be easy, but what about the towels? I guess I should learn a bit about cloth simulation in Houdini.

But first thing's first. Let me do the rack itself, then the pool nibbles, then a part of the entriway walkway. I'll import that other fence segment.

Let me just do this stuff. I need to get it out of the way. Just how much am I going to spend on this scene?

7:45pm. Tomorrow I am going to absolutely do the rack, do the pool, do the other fence, do the menu. The pool will also need a ladder. I'll take care of that as wall. I'll just turn a grid into lines, blast the top and bottom away, bend the top so it curves downwards.

Do I need anything other than that? I think no. So after that I'll be able to look into texturing.

Texturing will take me a while, but after that will come Luna. Once I complete this I will have a full 3d skillset. A few more scenes of same complexity as this and I can consider myself in the upper 2/5 range. I'll only need experience to break into the pro realm properly after that.

Houdini is so annoying, but I am going to master it. Nothing is going to stop me in this.

After that I'll am going to have full speed, and will be able to create scenes worthy of Heaven's Key.

I am going to cultivate this to its limit, and then make a real attempt at producing something worthy of admiration, if not value. As usual, I'll take the hardest route to that 2k for the AI chip. But the hard way is usually the most satisfying.

Won't it be wonderful to actually do something of value during the day instead of just trying to internalize the basics. A few more months and I will definitely reach such a level.

Even though I haven't done much, I've been in the zone the entire day. So that is a sign that I've learned."

---
## [Perkedel/IvanC-MIDI-Play-Plugin](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin)@[04a89ae9c6...](https://github.com/Perkedel/IvanC-MIDI-Play-Plugin/commit/04a89ae9c687ed1f1f42f328f0f67a61d5e7b04b)
#### Saturday 2022-02-12 20:40:33 by Joel Robert Justiawan

MILESTONE!!!! LEGIT ALL TRACK MIDI PLAYBACK!!!

oh FINALLY FOR PECKING SAKE FINALLY!!! Thancc God yey.

I  did it! for the first time ever since Christ, we finally

BUILT

ENTIRE

TRACK

MIDI

PLAYER

That's right. checkbox entire track to play all tracks in your MIDI all at the same time.
well unfortunately still haven't figured out override transport yet at the moment.

yeah let's go on later. for now, rest.

oh yeah btw, keep in mind! YOu need to have MIDI that also has event to change drumset in channel 10. Some VSTi like Yamaha S-YXG2006LE does not set the drum by itself after receiving all note off. and even this is its default state. So if your MIDI song sound like somebody smashing pianos, that mean the drum program number was not set. A good MIDI sets its program number for all used channels, even drums on channel 10.

Oh yeah, I have tested Midi type 0 (1 track only, disabling Entire Track still works as Full MIDI), Midi type 1 (multiple track, requires Entire track to have Full MIDI), but failed on Midi type 2 (track came out over infinity and crashes VST hosts if continued being fiddled around). I believe that was JUCE trouble? idk.. yeah.

C'MON!!! transport override pls!!! Topiary!!!

---
## [khonsulabs/bonsaidb](https://github.com/khonsulabs/bonsaidb)@[b2086b60e1...](https://github.com/khonsulabs/bonsaidb/commit/b2086b60e1b795b5734f3dcd4d9dae2e78ffb0e5)
#### Saturday 2022-02-12 21:55:28 by Jonathan Johnson

Add lz4 compression support

Closes #185

This is a first pass at compression support. I believe that ultimately
we'll want to support both zstd and lz4, but right now feature flags are
really annoying to implement. When we can implement namespaced features
(#178), we should revisit adding multiple compression backends and
options. lz4-flex has a faster unsafe option that can be enabled
optionally, but I've kept disabled in the spirit of BonsaiDb's "safe"
defaults.

From my research, zstd will be preferred when storage is at a premium,
but lz4 *should* be faster in general. I want to write a good benchmark
suite, because I believe the relative performance will potentially be
hardware dependent, and users should be able to gauge what works best
for them.

---

