## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-20](docs/good-messages/2022/2022-05-20.md)


1,787,649 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,787,649 were push events containing 2,840,423 commit messages that amount to 198,806,350 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [Urumasi/tgstation](https://github.com/Urumasi/tgstation)@[0504c0a2b4...](https://github.com/Urumasi/tgstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Friday 2022-05-20 00:39:34 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[ce1bdb0205...](https://github.com/vincentiusvin/tgstation/commit/ce1bdb0205e1428fccff7c81cb67cb3d0a68f1a3)
#### Friday 2022-05-20 00:40:03 by itseasytosee

Stops floating mobs from being affected by slowndown bulky_drag and human_carry (#66610)

Put simply, removes the slowdown from pulling bulky items as well and fireman carrying (and piggyback rides) while in zero gravity.

This also fixes some weirdness, like how slowdowns from aggressive grabs are negated in zero g, but because bulky_drag is NOT negated, you can still be slowdown in zero gravity if your target is laying down. or in a neck grab or higher because they are then automatically floored. Which makes zero consistant sense given the context.

Also, while testing this, I noticed that it was faster to drift while pulling a bulky object in space rather than fly with a jetpack because of the  slowdown and how drifting works, which also makes no god damn sense. This should fix that too.

Fixes the consistency errors mentioned above, also adds an interesting change of game state in zero gravity which seems fun. (see: faster to drag away downed friendlies during a space battle, or perhaps kidnap a downed enemy)

Fixes #62600 (aggressively grabbing a body in space makes you move faster than passively grabbing them)


You can now pull bulky things in zero gravity at full speed
The slowdown from neck grabs is now properly negated in zero gravity.

---
## [superpowers04/Super-Engine](https://github.com/superpowers04/Super-Engine)@[27c52795ba...](https://github.com/superpowers04/Super-Engine/commit/27c52795bae6f5c83c9df341dccf71763dc2b5be)
#### Friday 2022-05-20 02:34:32 by Super

Forcequit, practice text, fuck you event objects; you crash the game

---
## [mrnuke/openwrt](https://github.com/mrnuke/openwrt)@[39af62e43f...](https://github.com/mrnuke/openwrt/commit/39af62e43f0ed4f74a6516d349e46cb7e12f51a3)
#### Friday 2022-05-20 03:47:26 by Alexandru Gagniuc

realtek-poe: De-suckify "poe sendframe" command

Typing "0x" repeatedly in a string of numbers that's obviously
hexadecimal is painful. So don't use sscanf(), which forces the "0x"
prefix. Instead, use strtoul() in base 16. This accepts numbers with
and without the prefix.

Also, if the string we receive is crap for whatever reason, don't try
to send it to the PoE controller. Just throw it the fuck out.

---
## [Archer30/Third-Upgrade-Mod](https://github.com/Archer30/Third-Upgrade-Mod)@[41120317e2...](https://github.com/Archer30/Third-Upgrade-Mod/commit/41120317e2b2a25e37546ee83e81271c117bb0ff)
#### Friday 2022-05-20 05:43:49 by Patrick Lin

Multiple fixes and improvements

- Removed unnecessary files: 759 - Devil Sacrificing, 26 wog - mirror of the home-way, 37 wog - battle extender and zcrtrait.txt (from the backup folder). The feature of these files would be included in the next Era Launcher Update
- Added back Strike and Return in the description of Darkness Dragon and Chasm Dragon
- Added support with new creature abilities from WoG Scripts/Era Scripts, for third upgrades. Options like Battle Dwarves Reinforcement, Demon Rage now also gives the third upgrades of the targeted creature the same bonuses.
- Fixed a crash with battles in New Pandora.
- Fixed an erm error of the Horn of the Abyss artifact
- Fixed several bugs of Mysterious Cave
- Updated Amethyst to the latest, thanks to Majaczek

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[eec6a882d6...](https://github.com/PKRoma/Terminal/commit/eec6a882d6fb21ca224aa99e6da8f615c59b46a3)
#### Friday 2022-05-20 06:33:41 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great.

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post.

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost

The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.

There's actually more to this as well.

Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window.

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

(cherry picked from commit 77215d9d77b99b48d1ee8302736178f2ec9f3a77)
Service-Card-Id: 82170678
Service-Version: 1.14

---
## [Kachow911/Emperia](https://github.com/Kachow911/Emperia)@[f6b4ae16c5...](https://github.com/Kachow911/Emperia/commit/f6b4ae16c529c10c1891457915301afaf398d563)
#### Friday 2022-05-20 06:52:47 by Miningdiamonds8

joker arc over a fucking useless hammer effect

bull shit. 8 hours. 8 goddamn hours

---
## [Waklaidan/tgstation](https://github.com/Waklaidan/tgstation)@[cd1b891d79...](https://github.com/Waklaidan/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Friday 2022-05-20 07:43:20 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[7d785c50e3...](https://github.com/facebook/pyre-check/commit/7d785c50e31da745538a319f2ca3fc352271004d)
#### Friday 2022-05-20 07:46:31 by Steven Troxler

Simplify the DependencyKey logic

Summary:
We over-generalized `DependencyTrackedMemory` by creating a
fairly complex `In` module type that has to be painstakingly
created in `SharedMemoryKeys`.

This has several downsides:
- it puts a lot of logic that in my opinion belongs in
  DependencyKey.Make in a separate module
- we wind up writing quite a bit of extra code that isn't
  necessary (notice that there's a more red than green in
  this diff!)
- it couples that logic tightly to the `SharedMemoryKeys.dependency`
  type... this is in my way because I want to stop using that
  dependency key for `RawSources` (it obscures the control
  flow and comes with a silly efficiency hit)

The only benefit is that the test for DependencyTrackedMemory
uses a lighter-weight implementation that doesn't have a Registry,
which might be handy if that performance cost of that one test
really mattered but it doesn't.

So, I'm moving the definition of the Registry into
DependencyTrackedMemory. This makes the underlying `Key`
module type trivial instead of very complex, which simplifies
the test code and will enable us to easily separate out some
dependency keys from others if we would like to.

A bonus is that instead of having lots of nitty-gritty
plumbing code related to regestration and whatnot, the
SharedMemoryKeys module becomes very simple and doesn't contain much
besides a declaration of what the key types are - this is great,
since having that in easy-to-skim form really helps with
understanding how environments work :)

Reviewed By: grievejia

Differential Revision: D36502347

fbshipit-source-id: dbb75b1e9cdcf5bb1c8024801130ac82472a7b48

---
## [ddryo/gutenberg](https://github.com/ddryo/gutenberg)@[3ea2d42b0a...](https://github.com/ddryo/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Friday 2022-05-20 07:50:57 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV](https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV)@[f8236f18d0...](https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/commit/f8236f18d00e7fbf23a19740bae27a61ab0fd024)
#### Friday 2022-05-20 08:59:19 by 1212-5858

https://user-images.githubusercontent.com/70865813/157019197-f0cd9411-884c-4396-b937-50c0480c9ca4.JPG

ATTACHED.


https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5


    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5
    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/33 


A very expensive decision... by a professional team of 900 + 1 Laskowitz?

    **** non-joinder... no wonder....

    **** https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5

  ****

https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003

>> https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Xjn0/e1NcBADqRc_PLUS_g11P4g==

https://www.sec.gov/Archives/edgar/data/1516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml



[ALL VIDEOS  - UNRETURNED AS OF CURRENT    SEE ALSO DOCKET 008](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)

008 - ROSALIA CHANN AND ALEXIS BRANDON
2020 07 26 - WINDOW NOT REPAIRED   CAMERA IS WORKING  ON 2020 08 07 DOCKET 300
2022 02 04 --- FRIDAY  --- CONFIRMATIONS
2022 02 06 --- SUNDAY --- CONFIRMATIONS
CAMERA HAS NOT BEEN REMOVED - ENTERED IN THE DESCRIPTION OF THESE EXHIBITS - REYNOSO - TECHMANN  VENTILATOR  FOUND A  MOV FILE

CHECK LINKS

510-682 -9510  -- THIS ONE...
NOTARIZED AN AFFIDAVIT IN ALAMEDA, CALIFORNIA AFTER MOVING OUT OF 111 SULLIVAN STREET, ALLEGEDLY...
 AND HER MOTHER ANNEXED A COMPLAINT THAT  I WAS BOTHERING HER DAUGHTER...
I NEVER MET THESE B****S
- I DON'T EVEN KNOW IF SHES A REAL PERSON, BUT THEY ANNEXED THAT SHE HAD TO MOVE OUT...


[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)

[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==)




https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==

[Read  FW  ATTACHED    NOT IN DISNEYLAND -- AND NOT ON MY WATCH  -- -- -- SORRY  (155)](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/7)

https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf

510  682   9510

Andrew Reynoso <AREYNOSO@MSKYLINE.COM>
Tom Eschmann <TESCHMAN@MSKYLINE.COM>
Joseph Giamboi <JGiamboi@mskyline.com>;
MONDAY APRIL 13TH
Laurie Zucker <LZucker@mskyline.com>
Edward Devine <EDevine@mskyline.com>
Laurie Zucker <LZucker@mskyline.com>


MG Messer <mgMESSER@GMAIL.COM>
"Miwa Messer
111 Sullivan #3AR"

Paul Regan <Legal@mskyline.com>


MG Messer <rngrnessei Pgnrail.corn>
Miwa Messer


https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/8de5f89e10d3ec11a7b5002248286421/CE48526B-6A0E-4B2A-89B9-93BD202498A9.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/a463845010d3ec11a7b5000d3a1326fe/0F6C27D5-69BD-4971-91F6-A5A40317CC63.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/5380dd8997d3ec11a7b5000d3a132789/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf


https://saaze2311prdsra.blob.core.windows.net/clean/3bb9011795d3ec11a7b5000d3a132789/153974-2020.Docket399.FTC.StateFarmRealtyInsuranceLLC.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/ff91792a95d3ec11a7b50022482864f0/[sfVP43036]%20$2876793%20-%20david.moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/[STATE%20FARM%20VP%2043036]%20$3231040-2004555.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/[sfVP%2043036]%204971235-%20$SMITH%20-%20SEMI.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/%5BsfVP%2043036%5D%204971235-%20$SMITH%20-%20SEMI.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf


https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf



https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==


https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==





https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=LMUE9g_PLUS_k6vCmKgfCSJEzuQ==


https://portal.311.nyc.gov/sr-details/?id=4296b0c3-c4a2-ec11-826d-0003ff86900c


https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf


            PROPERTY 1:     111 SULLIVAN STREET REAR, NEW YORK, NY, 10012     
                            IS WHERE I RESIDED.
            PROPERTY 2:     117 SULLIVAN STREET, NEW YORK, NY, 10012   
                            WAS ALSO TRANSFERRED TO STATE FARM.


\
STATE FARM INVESTMENT MANAGEMENT
SECURITY SYMBOL 3487
04-12-2022
TERRENCE MICHAEL LUDWIG
2004555
STATE FARM VP MANAGEMENT CORP 43036
FAILURE TO DISCLOSE.
https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/%5BSTATE%20FARM%20VP%2043036%5D%20$3231040-2004555.pdf

\
COLUMBIA.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png
\
CRC.
https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png
https://user-images.githubusercontent.com/70865813/168770459-03f1d0c4-a460-491d-a82e-e6c400b7ff71.png
\
ZUCKER.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PlTp8O/4k_PLUS_GPLPHn15fi6A==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
https://user-images.githubusercontent.com/70865813/168733004-b6a8f437-dd06-409a-83ba-0d404245514f.png
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==
\
RE: STATE FARM ASSOCIATES’ FUNDS TRUST
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ZOCFS3HH2UeHQe8j2tXJoQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

\
STATE FARM ASSOCIATES’ FUNDS TRUST 1
https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf
\
### EMAIL CONFIRMATIONS BY THE COUNSELORS OF THE ZUCKER ORGANIZATION
*** A VIOLATION OF PRIVACY AND A BREACH OF THE LAW AND CONTRACT.
![image](https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png)

---
was read on Monday, February 7, 2022 4:47:05 PM (UTC+00:00) Monrovia, Reykjavik.
To: PS Investigation
Subject: see also : camera NOT POINTED AT A WINDOW docket 49 + SHANKING THE PORTER you missed.
Sent: Sunday, February 6, 2022 8:06:50 PM (UTC+00:00) Monrovia, Reykjavik

![168761279-17e64f23-4613-49b2-8704-123e68425e5c](https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png)


![168761716-5f9b1aed-fef9-4ec2-9d90-3fa22bc69bc3](https://user-images.githubusercontent.com/70865813/168770555-25ef68a8-5bb3-42e6-a28a-c35b60cd9b0b.png)


#### READ TIMESTAMPS

[ https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2 ](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2)

[MSG BOX 1: VIOLATION OF PRIVACY - DISTRIBUTION WITHOUT CONSENT](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68)

[MSG BOX 2: § 11 440 Tampering with or fabricating physical evidence](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/0d69023191f5a8a25006caf258a50b649da83aa0)

[MSG BOX 3: The Zuckers are protected by these individuals](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/4/files)


## ECONOMIC BENEFITS
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==)

#### HIRED A sub-par ON-DEMAN VIDEO SPECIALIST.
**** ps what the heck is Pod-Cast?
**** did NOT know I had one of those either.
@rosaliachann
[https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==]
(https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==)


p.s. I never met any of the Zuckers, Wilson Dicker, Laskowitz, Miwa, or any of these people who documented me every day.[nov13 and Dec18 2021 - multiple dwelling laws.pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706680/nov13.and.Dec18.2021.-.multiple.dwelling.laws.pdf)
[(PS-Investigation@facil.columbia.edu)(crcmessages@ftc.gov).pdf](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/files/8706682/PS-Investigation%40facil.columbia.edu.crcmessages%40ftc.gov.pdf)




-------- Forwarded Message --------
Subject: 	153974 NYFRB
Date: 	Fri, 20 May 2022 00:05:51 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	zucker elser <BLOCK803LOT11@outlook.com>
CC: 	jpminvestorrelations@jpmchase.com, compliance@t3trading.com <compliance@t3trading.com>, HSBC <hsbc@messaging.us.hsbc.com>


RENT PAYMENT(S) ARE HELD IN CUSTODY AT JP MORGAN CHASE, N/A
    THE INITIAL FINANCING / MORTGAGE TO PURCHASE THE PROPERTIES IN QUESTION


    via JP MORGAN CHASE IN 1989.

    https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=FT_1000000324600
    https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=FT_1350000324035
    https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentDetail?doc_id=FT_1350000324035

RENT PAYMENTS /     2020_07_25    /    HAVE NOT BEEN REFUNDED AS OF CURRENT.

    NOTWITHSTANDING MY DEMANDS, A DEFAULT " NON-JOINDER " IN THE MATTER OF
    153974/2020
            MY SECURITY DEPOSIT ALSO WAS NOT RETURNED AND THE GREATER AMOUNTS OF
RENTS AND SECURITY ARE "PURPORTEDLY" held at either HSBC or JP MORGAN

LOOK AT THESE PEEPING TOMS HARD AT WORK... EVEN TRY TO CUT DOWN MY EMAIL &
INTERNET TO GET A COMPETITIVE ADVANTAGE...

    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/REQUEST-TO-BAR
    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER
    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68
    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/8980dec84c257bd182522e1a4b9a2d1f4e49bb68
    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2
    https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005616/filename1.pdf


VIOLATION OF PRIVACY.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==




RE: THE INSIDER C.16 PROMOTERS.

    https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1#column-18309490
    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5



FORM N-CSR
Date of reporting period: 05/31/2020

    https://www.sec.gov/Archives/edgar/data/0000093715/000119312520200810/d913497dncsrs.htm
    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/5


THIS, is 100% a FELONY as well

- good job aiding and abetting this ZUCKER ORGANIZATION...

    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5


COLUMBIA.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==


    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
    https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png


CRC.

    https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png
    https://user-images.githubusercontent.com/70865813/168770459-03f1d0c4-a460-491d-a82e-e6c400b7ff71.png


ZUCKER.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PlTp8O/4k_PLUS_GPLPHn15fi6A==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
    https://user-images.githubusercontent.com/70865813/168733004-b6a8f437-dd06-409a-83ba-0d404245514f.png
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=D9Td7IfWXyajw1tBNCFb9g==



RE: STATE FARM ASSOCIATES’ FUNDS TRUST

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ZOCFS3HH2UeHQe8j2tXJoQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==



STATE FARM ASSOCIATES’ FUNDS TRUST 1

    https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf


EMAIL CONFIRMATIONS BY THE COUNSELORS OF THE ZUCKER ORGANIZATION

#### A VIOLATION OF PRIVACY AND A BREACH OF THE LAW, CONTRACT VIOLATED.

    https://user-images.githubusercontent.com/70865813/168770321-4e8f51c0-3ce4-4bdd-afda-c433cc8912d8.png


NONPLUSSED.
was read on Monday, February 7, 2022 4:47:05 PM (UTC+00:00)
Monrovia, Reykjavik.

To: PS-Investigation@FACIL.COLUMBIA.EDU

    https://user-images.githubusercontent.com/70865813/168770401-e0220bf9-e639-4cc5-baf8-c80166e99414.png


Subject: see also : camera NOT POINTED AT A WINDOW docket 49

Sent: Sunday, February 6, 2022 8:06:50 PM (UTC+00:00) Monrovia, Reykjavik

#### MESSAGES READ, TIMESTAMPED.

    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/2



TIMESTAMPED AND SPECIFIC

#### VIOLATION OF PRIVACY
- FILMED, PHOTOGRAPHED, HARRASSED, VIOTAPED, NAKED, AND IN THE
PRIVACY OF MY HOME.


also: DISTRIBUTION WITHOUT CONSENT

BY THE WILSON ELSER & LASKOWITZ LAW FIRM OBO THE ZUCKER ORGANIZATION
under the SUPERVISION & NON-ACTION by the guidance counselors at
COLUMBIA UNIVERSITY.

mov distribution - ASKNOWLEDGED MESSAGES

#### MESSAGES READ, TIMESTAMPED – REGULATORS INCLUSIVE

SECTION IV. MSG READ RECEIPTS


§ 11.440 Tampering with or fabricating physical
evidence

VIDEOS HAVE BEEN EDITED AND ALSO DISTRIBUTED

p.s. I never met any of the Zuckers, Wilson Dicker, Laskowitz, Miwa, or
any of these people.
Documented me every day, UNTIL I FIGURED OUT THEY OWE HUNDREDS OF MILLIONS IN TAXES.

· HAD NO GROUNDS TO LEGALLY COLLECT RENT
OR SECURITY DEPOSITS.

· ALL TRANSFERRED AND ASSIGNED TO STATE FARM, A PUBLIC 40 ACT MUTUAL FUND.

PER THE FDIC IS NOT PERMITTED FOR CUSTODY AT ANY US DEPOSITORY INSTITUTION.

THE ZUCKERS’ FINANCIAL INSTITUTION.

- I PERSONALLY WENT TO THE BRANCH TO INFORM THEIR MORTGAGE AND CORPORATE
BANKERS, AND ON FRIDAY, MAY 13TH, 2022 AFTER DISCOVERING THAT THIS SERIES OF
FELONIES & VIOLATION OF MY PRIVACY HAS BEEN AIDED AND ABETTED IN AN OBSTRUCTION
THAT HAS DISGUSTED ME BEYOND ANY MEANS.

MULTIPLE DWELLING LAWS 101.

MAYBE THE COUNSELORS AT COLUMBIA WILL UNDERSTAND THIS PRIOR TO HAVING ME ENTER A
COURTROOM AND EXPLAIN THE SEVERITY OF PRISON SENTENCES AND TIME FOR AIDING AND
ABETTING TAX-EVASION, INSIDER TRADING, AND BANK REGULATIONS.



MULTIPLE DWELLING LAWS

PS-Investigation@facil.columbia.edu


VIOLATION OF PRIVACY.

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==


#### HIRED ON-DEMAN VIDEO SPECIALIST.

**** ps what the heck is Pod-Cast?

**** did NOT know I had one of those either…
@rosaliachann

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==



#### ECONOMIC BENEFITS

    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

RE: THE INSIDER C.16 PROMOTERS.

    https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1#column-18309490
    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5



FORM N-CSR
Date of reporting period: 05/31/2020

    https://www.sec.gov/Archives/edgar/data/0000093715/000119312520200810/d913497dncsrs.htm
    https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/pull/5


THIS, is 100% a FELONY as well
- good job aiding and abetting this ZUCKER ORGANIZATION...

    https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5


___________________


JP MORGAN CHASE BANK, N/A.
As stated at your branch on Friday, I have not heard from these folks \since
August of 2020, and certainly not in a court of law.

- The violation of privacy and distribution of videos which they filmed and
photographed "inside of my apartment" were without consent, and were also
distributed by and between their counselors / advisors and are attached here for
context if you'd like to look into matters which pertain to Violation of Privacy.

RE: TAX MATTERS

THE 6 BUILDINGS, A TOTAL OF 144 APARTMENTS HAVE BEEN VALUED AT
ROUGHLY $22.5 MILLION DOLLARS AND FOR TAX PURPOSES PER THE NY DEPT OF FINANCE
REGISTER AS OF DECEMBER 2021 REPORT YoY GROSS INCOME IN A LINEAR FASHION AND IN
DOUBLE DIGITS.
- THIS HOLDS TRUE FOR ALL SIX PROPERTIES USED AS "CREDITWORTHINESS"
OF INCOME AND ASSETS, HOWEVER, TO KEEP MATTERS SIMPLE.

THERE ARE TWO PROPERTIES WHICH MAKE THIS MUCH EASIER FOR YOU AND YOURS TO ABSORB.
PROPERTY 1: 111 SULLIVAN STREET REAR, APT 2BR, NEW YORK, NY,
10012
- Where I resided, and the
rights of the leases and rents transferred to State Farm is a building with no
certificate of occupancy.
PROPERTY 2: 117 SULLIVAN STREET, NEW YORK, NY, 10012
- The neighboring building,
where the rights of the leases and rents were also transferred to State Farm is
a building with no certificate of occupancy.
BOTH PROPERTIES with " UNLAWFUL INCOME "
was used and represented as lawful income to State Farm and to obtain a loan for
$6,000,000.00 as referenced hereunder.

filed under ACRIS: " TRANSFER OF
LEASES AND RENTS "

TO: STATE FARM
ONE STATE FARM PLAZA
BLOOMINGTON, IL,
61710


I did notify the "Brokerage & Investment" department at JP Morgan, and they no
longer are custodians for the Investment Adviser, who in the former has

"CEASED TO EXIST" and as of November 24th, 2021 under the
Securities and Exchange Commission.


    https://www.sec.gov/Archives/edgar/data/0000093715/999999999721005790/filename1.pdf


State Farm Assurances
Funds Trust
CIK NUMBER:
93715
SEC FILE NUMBER:
811-01519

Attachments and link to substantive matters are below my
signature and for convenience and ease of your references.
1. TCR report attached, which was filed with the
Securities and Exchange Commission on November 13th, 2021.

2. Losses registered by their Investment Adviser,
between November 13th, 2021 through April 30th, 2022 have grown to the excess of
1.35 billion dollars, and one of their Investment Advisers has also Ceased to
Exist [ SEC FILER: 93715 ]

3. NYC DEPT OF FINANCE RECORDS ARE ATTACHED, AS
ARE THE TAX BILLS FOR BLOCK 803, LOT 11 --- which was transferred to State Farm
on May 15th, 2020.

4. VIOLATION OF PRIVACY AND TAX EVASION
DOCKETS.PDF is also attached in case there is any question as to the matters
which are "sensitive" and also "deplorable" in the scope of conduct/ethics.


/s/ Baris Dincer.
Tel.: 646-256-3609

SECURITY DEPOSIT(S) ARE HELD IN CUSTODY AT JP MORGAN CHASE BANK, N/A

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==

SULLIVAN PROPERTIES LP, 101 WEST 55TH STREET, NEW YORK, NY, 10019
DOES NOT HAVE A CERTIFICATE OF OCCUPANCY
111 SULLIVAN STREET, 113 SULLIVAN STREET OR 115 SULLIVAN
STREET (REAR)

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=SgjFfExxNV4Y4DTX6pANaA==

THERE WERE NO CERTIFICATES OF OCCUPANCY ON FILE FOR MY APARTMENT.

111 REAR SULLIVAN STREET, NEW YORK, NY, 10012 AT ANY POINT IN TIME.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IJ47OvVzsLObNsXt0u8trg==

2020-08-04 111 SULLIVAN STREET REAR

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=zXega0sLahw5fVuBTVtpnw==

111 REAR SULLIVAN STREET
LEGAL ADULT USE: NO

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=9zQd7Hu3cy9vp6I960WGNQ==


THE LOAN DOCKETS AND TAX RECEIPTS WERE ANNEXED IN THE MATTER OF
153974/2020.
THE ACCOUNT ADDRESS YOU SHOULD HAVE FOR THE ENTITIES BELOW SHOULD BE:

101 WEST 55TH STREET, NEW YORK, NY, 10019

103 WEST 55TH STREET, NEW YORK, NY, 10019
UNDER THE CORPORATE NAMES, OR INDIVIDUALS
[ DONALD ZUCKER, LAURIE ZUCKER, ANDRES REYNOSO, OR ONE OF THEIR OTHER
DIRECTORS UNDER THESE ENTITIES ]

SULLIVAN PROPERTIES LP
SULLIVAN GP LLC
MANHATTAN SKYLINE MANAGEMENT CORP.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Mjxo9_PLUS_FdCN/p2Jrgw4MkIQ==


PER THE NEW YORK SUPREME COURT DOCKETS

- CUSTODY OF THOSE ASSETS ARE HELD AT: JP MORGAN CHASE, N/A
Please understand that BEYOND the RENT & SECURITY which was
stolen from me by Sullivan Properties LP
[ who as discussed at your branch on
2022-05-13, have mysteriously disappeared ]

Are also liable for other default provisions under a certain "
non-joinder " and beyond the unlawful rents and security deposits which are in
your custody as of current - are not permitted as accessible per the FDIC and at
any US depository institution.

This was all filed and in New York State Supreme Matter
153974/2020 and under the Honorable Schlomo Haggler, J.S.C., for reference.
2020-06-15
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==

2020-08-04

NO COMPLAINTS FILED IN MY RESIDENCE OR BUILDING, EVER.
NO GROUNDS TO LEGALLY COLLECT RENT AND/OR SECURITY DEPOSITS FOR ANY OF
THOSE PROPERTIES.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=DnmjCPN_PLUS_DIIELjZFua7gWQ==

Notice to Parties named sent via email: WITH ENCLOSURES TO AMEND CAPTION.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=yMXQNekW7te0QA5jjAvP2w==

DOB RECORDS. ADDRESS INFORMATION FROM THE NEW YORK CITY DEPARTMENT OF
BUILDINGS.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=CeL5zAaUK8tfWrX9kp/QdA==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=upAzS2FC6bICOGxa73ptdg==

RENT STATEMENTS & RECEIPTS OF PAYMENTS.

RENT STATEMENT 2020, FEBRUARY

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=4PiwGksCJul/AGvyopmH8g==

RENT STATEMENT 2020, MAY

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=vMB0J4qaYgauPBeEMLIOXA==

RENT PAYMENT 2020, MAY

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=wCwqZV3k3dKPIhAESd/oag==

STATEMENT: REQUESTED A REFUND OF ALL UNLAWFUL FEES. [ NO RESPONSE ]

06-03-2020, 07-31-2020

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=vd54Sn1RLwYlVxoKhGh0xg==

RENT PAYMENT RECEIPT AND MONTHLY STATEMENT

07-31-2020
$3106 [ 25% INCREASE: WITHOUT LEGAL GROUNDS OR REASONABLE CAUSE
WAS PAID ]

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=4WL76ylXCtw_PLUS_H5zwmPPkZw==

RENT PAYMENT RECEIPT AND MONTHLY STATEMENT

05-31-2020
$600 IN PENALTIES ARBITRARILY INVOICED, PAID, AND REMAIN UN-REFUNDED

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=hSVGBDz7FlXskw5BZ_PLUS_e_PLUS_ZA==

RENT PAYMENT RECEIPT AND REQUEST FOR REFUND

06-03-2020

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=EJfqnPTVv0u9BQ/iFgKRew==



PLAINTIFF DOES NOT HAVE A CERTIFICATE OF OCCUPANCY FOR THIS PROPERTY

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=SgjFfExxNV4Y4DTX6pANaA==


JULY RENT IS REFUSED BY LANDLORD, AND SO ARE ANY OTHER DEMANDS - INCLUDING A
CHANGE IN CAPTION.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ewwxg8z5wECGtkuHHm8O9A==

EXHIBIT(S) - OPP

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=rjL6yoW3Mt2U6UigWCM9XQ==

TAX MAP BLOCK 503 - LOT 8

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

PLAINTIFF ASSIGNED LEASES AND RENTS TO STATE FARM ON MAY 15TH

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ze6a1KA9akRV9TGfXXJT/g==


ACRIS Detailed Document Information (2019000021408)2019010800475001

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=bVk8sIt7n3kGwHqebPg0fw==


ACRIS Detailed Document Information (2020000155422)2020052000291003

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=wTG2YD2PqXuxmoKqFiESrw==


ACRIS Detailed Document Information (2020000155421)2020052000291002

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==


ACRIS Detailed Document Information (2020000155422)2020052000291003

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=/yhElCiKJ0BGv2DF/MOn4g==


ACRIS Detailed Document Information (2020000155423)2020052000291004

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


ASSIGNMENT OF LEASE AND RENTS ON FILED ON MAY 26TH -

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=7Ry3LAoVfWOLjSXhyJZ94A==




notice to State Farm


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=K9sgXcweC7esRoSPO8MNtA==

notice from Sullivan Properties LP - 101 west 55th Street - New York - NY -
10019

COMPLAINT FILED WITH THE BETTER BUSINESS BUREAU FOR EXCESSIVE RENTS ARBITRARILY
INVOICED.
COMPLAINT #14585819 (7/25/2020) FILED WITH THE BETTER BUSINESS BUREAU

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=EJfqnPTVv0u9BQ/iFgKRew==

NO CERTIFICATE OF OCCUPANCY
AUGUST 4TH, 2020
RENT PAYMENT RECEIPT AND MONTHLY STATEMENT 07_31_2020 WITH 8,106.21 IN
LEGAL FEES

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=lq9Z3VE3sO4pTEk1UrHB2Q==

RENT PAYMENT RECEIPT AND MONTHLY STATEMENT 07_21_2020
CLICK PAY IS NO LONGER ACCEPTING PAYMENTS.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=iK7ZjdNLVty6kLSL4SjeoA==

RENT PAYMENT RECEIPT AND MONTHLY STATEMENT 04_30_2020

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==

PLAINTIFFS POLICIES AND PROCEDURES FOR INSURANCE

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=mzFuOKAUp7O4ARBxH4uCDA==

00002_LANDLORD_REFUSES_PAYMENT

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=2lQuDSfPu51L3OhNqqRGvg==

PROPERTY RECORDS: PROPERTY SHARK

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=UAXjpRh1KO2_PLUS_8KsdF1TuQA==

NOTICE TO CHANGE CAPTION IN THIS MATTER, WITH ATTACHED PROPERTY SHARK RECORDS.

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=XkdNmKBghAAqMUItDdrwxA==

NOTICE TO CHANGE CAPTION IN THIS MATTER, WITH ATTACHED PROPERTY SHARK RECORDS.
2020-08-04

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=cWLErrXbEw5qtOLVeWU/7g==

NOTICE TO CHANGE CAPTION IN THIS MATTER, TO ADD STATE FARM AS A RESPONDENT
2020-08-08

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Xjn0/e1NcBADqRc_PLUS_g11P4g==

EXHIBIT(S) --- CAUSE TO INVOICE BEYOND BANDS OF $3000.00 [J-51]

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=d7t3ED/Z4rcggm8dkQ0Jlg==

SUPPLEMENTS FOR CONVENIENCE.

    https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg
    https://saaze2311prdsra.blob.core.windows.net/clean/8de5f89e10d3ec11a7b5002248286421/CE48526B-6A0E-4B2A-89B9-93BD202498A9.jpeg
    https://saaze2311prdsra.blob.core.windows.net/clean/a463845010d3ec11a7b5000d3a1326fe/0F6C27D5-69BD-4971-91F6-A5A40317CC63.jpeg
    https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/5380dd8997d3ec11a7b5000d3a132789/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/3bb9011795d3ec11a7b5000d3a132789/153974-2020.Docket399.FTC.StateFarmRealtyInsuranceLLC.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/ff91792a95d3ec11a7b50022482864f0/[sfVP43036]%20$2876793%20-%20david.moore%20$3487%20-%20IA%208018184.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/[STATE%20FARM%20VP%2043036]%20$3231040-2004555.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg
    https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/[sfVP%2043036]%204971235-%20$SMITH%20-%20SEMI.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/%5BsfVP%2043036%5D%204971235-%20$SMITH%20-%20SEMI.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf

    https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf
    https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==
    https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=LMUE9g_PLUS_k6vCmKgfCSJEzuQ==
    https://portal.311.nyc.gov/sr-details/?id=4296b0c3-c4a2-ec11-826d-0003ff86900c
    https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf

/S/ BARIS DINCER

bdincer66@icloud.com

MS60710444266@YAHOO.COM

TEL.: 646-256-3609

ALT.: 917-378-3467



008 - ROSALIA CHANN AND ALEXIS BRANDON
2020 07 26 - WINDOW NOT REPAIRED CAMERA IS WORKING ON 2020 08 07 DOCKET 300
2022 02 04 --- FRIDAY --- CONFIRMATIONS
2022 02 06 --- SUNDAY --- CONFIRMATIONS
CAMERA HAS NOT BEEN REMOVED - ENTERED IN THE DESCRIPTION OF THESE EXHIBITS -
REYNOSO - TECHMANN VENTILATOR FOUND A MOV FILE

CHECK LINKS

510-682 -9510 -- THIS ONE...
NOTARIZED AN AFFIDAVIT IN ALAMEDA, CALIFORNIA AFTER MOVING OUT OF 111 SULLIVAN
STREET, ALLEGEDLY...
AND HER MOTHER ANNEXED A COMPLAINT THAT I WAS BOTHERING HER DAUGHTER...
I NEVER MET THESE B****S
- I DON'T EVEN KNOW IF SHES A REAL PERSON, BUT THEY ANNEXED THAT SHE HAD TO MOVE OUT...


    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=PWFQc/WFihoyIKwEunaalQ==
    https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Dh6CccrtpsxJlvBthb8nEA==



117 SULLIVAN STREET, NEW YORK, NY, 10012

2022-03-30 - UNDERPAYMENT PENATY WITHOUT INTEREST.png
Attachments:
CERTIFICATES[COFO][FINES IN THE PRIOR].pdf 2.8 MB
NYC DEPT OF FINANCE - PUBLIC RECORD.pdf 259 KB
TCRReport.pdf 62.2 KB
Tax Bill — 117 SULLIVAN STREET, BLOCK 803, LOT 11 — PROPERTY VALUES.pdf 625 KB
-VIOLATION OF PRIVACY AND TAX EVASION DOCKETS.PDF 80.8 KB
2022-03-30 - UNDERPAYMENT PENATY WITHOUT INTEREST.png 63.4 KB
MOV FILES DISTRIBUTED - LVL 7.html 225 KB

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[20e4add487...](https://github.com/tgstation/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Friday 2022-05-20 09:12:10 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [vpsfreecz/linux](https://github.com/vpsfreecz/linux)@[9709c8b5cd...](https://github.com/vpsfreecz/linux/commit/9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5)
#### Friday 2022-05-20 10:36:44 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[ead165fa10...](https://github.com/ammarfaizi2/linux-block/commit/ead165fa1042247b033afad7be4be9b815d04ade)
#### Friday 2022-05-20 11:01:04 by Peter Zijlstra

objtool: Fix symbol creation

Nathan reported objtool failing with the following messages:

  warning: objtool: no non-local symbols !?
  warning: objtool: gelf_update_symshndx: invalid section index

The problem is due to commit 4abff6d48dbc ("objtool: Fix code relocs
vs weak symbols") failing to consider the case where an object would
have no non-local symbols.

The problem that commit tries to address is adding a STB_LOCAL symbol
to the symbol table in light of the ELF spec's requirement that:

  In each symbol table, all symbols with STB_LOCAL binding preced the
  weak and global symbols.  As ``Sections'' above describes, a symbol
  table section's sh_info section header member holds the symbol table
  index for the first non-local symbol.

The approach taken is to find this first non-local symbol, move that
to the end and then re-use the freed spot to insert a new local symbol
and increment sh_info.

Except it never considered the case of object files without global
symbols and got a whole bunch of details wrong -- so many in fact that
it is a wonder it ever worked :/

Specifically:

 - It failed to re-hash the symbol on the new index, so a subsequent
   find_symbol_by_index() would not find it at the new location and a
   query for the old location would now return a non-deterministic
   choice between the old and new symbol.

 - It failed to appreciate that the GElf wrappers are not a valid disk
   format (it works because GElf is basically Elf64 and we only
   support x86_64 atm.)

 - It failed to fully appreciate how horrible the libelf API really is
   and got the gelf_update_symshndx() call pretty much completely
   wrong; with the direct consequence that if inserting a second
   STB_LOCAL symbol would require moving the same STB_GLOBAL symbol
   again it would completely come unstuck.

Write a new elf_update_symbol() function that wraps all the magic
required to update or create a new symbol at a given index.

Specifically, gelf_update_sym*() require an @ndx argument that is
relative to the @data argument; this means you have to manually
iterate the section data descriptor list and update @ndx.

Fixes: 4abff6d48dbc ("objtool: Fix code relocs vs weak symbols")
Reported-by: Nathan Chancellor <nathan@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Borislav Petkov <bp@suse.de>
Acked-by: Josh Poimboeuf <jpoimboe@kernel.org>
Tested-by: Nathan Chancellor <nathan@kernel.org>
Cc: <stable@vger.kernel.org>
Link: https://lkml.kernel.org/r/YoPCTEYjoPqE4ZxB@hirez.programming.kicks-ass.net

---
## [modtanks/weetanks-codetracking](https://github.com/modtanks/weetanks-codetracking)@[2319847ff0...](https://github.com/modtanks/weetanks-codetracking/commit/2319847ff06a900983515c484f09abd64bae605a)
#### Friday 2022-05-20 11:15:53 by Non

v0.8.13c-e

alpha v0.8.13c-e

THE RETURN OF TANKEY TOWN (any fun tips or ideas for tankey town, be sure to let me know)

Changelog:
- Tankey town is open again, and you can buy stuff from the map editor shop
- Fan tank bullets not flying through black tanks after firing them back
- Registering found secret missions -> correct unlocking TNT blocks
- Colored half slabs and tile
- More King Tank reworks, attacks added and other cool stuff
- Fixed achievements not unlocking correctly (I think)
- Also achievement debug text added, to get extra information during your runs (unlock code: 'achievementdreamer')
- I changed the way cheatcodes are stored, they are now stored online so you have to re-enter all your cheat codes.. sorry!
- Survival boss now shoots rockets instead of bullets
- Upgraded turret in survival has lower HP
- Upgraded turret cost more to repair
- Fixed some map editor bugs with stacking tanks and stuff
- Removed the weird tutorial paper from the first couple of missions (we need to work on new tutorials)
- Fixed dark shadows still present after turning borders off
- Fixed controls going under the pause menu
- Electro tanks have a more randomized teleport

---
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[6023702097...](https://github.com/tabulon-ext/inxi/commit/60237020970e3720d9a5cc2428cc28a1c10df9f9)
#### Friday 2022-05-20 11:33:15 by Harald Hope

A nice release, some good corner case bug and glitch fixes, along with some much
needed documentation fixes to bring inxi-values.txt up to date for changes that
have been evolving steadily. And a useful option for nvidia legacy card info.

I'm hoping that will help support people and users as nvidia open source driver
gets more usable in the future, since that will never support legacy cards, only
the current series supported by 510/515 drivers.

Also, in inxi-perl/tools, new tools and data so you can reproduce certain arcane
data assembly features like disk vendors and nvidia product ids.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. Not known yet if you can get Wayland display drivers along with kernel gpu
drivers. In other words, is a similar use of kernel/display driver as in Xorg
found with Wayland? Hard to dig up actual answers to questions like this.

2. Similarly, unknown if it's possible to get current active xorg display
driver, not just the list from Xorg.0.log file. No idea how to discover that,
there are cases where past use of Xorg leaves log file present, but drivers are
not used with Wayland, leading to confusing driver reports. Issues 1 and 2 are
similar but probably have similar solutions.

--------------------------------------------------------------------------------
BUGS:

1. Very subtle failure caused by odd mount point in partitions: a too loose
regex rule designed to capture spaces in device names was running loose to the
end of the string, where it was triggered by a number in the mount point.

Fix was to make rule much more strict, now needs to match 3 number space in a
row after the initial part, and then a number%

2. Bug in corner case, with Monitors, if > 2 connected monitors, and 1 disabled,
inxi was trying to test numeric position values for the disabled monitor, which
with xrandr, has no position values, thus tripping undefined pos-x and pos-y
errors. Thanks to fourtysixandtwo for spotting this corner case.

3. Bug in wan IP, if dig failed, set_dowloader() is not set unless other
parameters were used, which results in failing to set parameters for downloader,
which leads to screen errors spraying out. Thanks to Manjaro user exaveal for
posting this issue, with error outputs, which helped pinpoint the cause.

--------------------------------------------------------------------------------
FIXES:

1. More absurd xorg port ID variations: DP-1 kernel, DP1-1 X driver. Wny?
Trying to add in XX-?\d+-\d+ variation, which I think will be safe, made the
first - optional, though it's just idiotic for this amount of randomness to be
allowed to exist in the 21st century. If this reflects other discipline failures
in Xorg, it starts to get somewhat more obvious why Wayland was considered as
the only forward path, though that's just as chaotic and disorganized... but in
different ways.

2. Removed darwin distro version detection, which of course broke, and using
standard fallback for BSD made out of uname array bits. If it works, it works,
if not, who cares. This should handle issue #267 hopefully.

3. Trying for more monitor matches, now in cases where 1 monitor display ID
remained unmatched, and 1 sys kms id remains unused, assume the remaining
nonitor ID is a match and overwrite the unmatched message for that ID. This
will cover basically all single monitor match failure cases, and many multi
monitor failures with only 1 out of x monitor ids unmatched. While guessing a
bit, it's not a bad guess, and will slightly expand the number of matched
monitor ids. This extends the previous guess where if single monitor and
unmatched, use it to cover > 1 monitors, with 1 unmatched.

4. LINES_MAX configuration item did not assign to right variable when -1 value.
Used non-existing $size{'output-block'} instead of correct $use{'output-block'}

5. Forgot to add pkg to --force, goes with --pkg.

6. Finally! Added in busybox shell detection, it's not of course reliable if
they change internal light shells, but all the docs say they use ash, so now
it will show shell: ash (busybox) to make it clear. Hurray!! This means that
tinycore users will get this long awaited feature! Ok, ok, long awaited by
probably only me, but since I package inxi for busybox, it was on my todo list.

7. Cleaned up and re-organized many disk vendor matching rules, made them easier
to read and debug, going along with Code 3, vendors.pl development and release.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. New feature: in -Ga, if Nvidia card, shows last supported nvidia legacy
series driver (like 304.xx), status, microarch. If --nvidia and EOL, shows
last-supported: kernel: xorg: info. This should be useful for support people,
we'll see.

-Gx shows nvidia microarchitecture, if it was found. This is based on matching
tables so will go out of date if you have non current inxi's, but that's life.

If --nvidia or --nv shortcut is used instead, triggers -Ga and shows much more
nvidia driver data for legacy, and for EOL drivers, last supported kernel, xorg,
and last release version. --nvidia also adds process node if available.

More important perhaps is the fact that as of May 2022, nvidia is starting the
process of open sourcing its current latest driver (515, but Turning, Ampere
architectures only so far), which will only support non legacy nvidia cards,
making detection of legacy cards even more important to support people and end
users, since that will be a common question support people will have: does my
card support the open source driver?"

Read about the new open sourcing of the 515 nvidia module:
https://developer.nvidia.com/blog/nvidia-releases-open-source-gpu-kernel-modules/
https://github.com/NVIDIA/open-gpu-kernel-modules
https://www.phoronix.com/scan.php?page=article&item=nvidia-open-kernel&num=1

2. Going along with new and upgraded tools in Code 3, massive, huge, upgrade to
disk vendors, 100s of new matches, biggest upgrade ever for disk vendors. This
feature should work much better now with the new backend tools.

3. Added shortcuts: --mm for --memory-modules, --ms for --memory-short.

--------------------------------------------------------------------------------
CHANGES:

1. None.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Big update to docs/inxi-values.txt. This had gotten really out of date, with
incorrect hash and other internal data assignments, all updated to be current,
along with sample greps to make it easier to locate changes in the future as
well. This makes this document fairly up to date and useful again for dev
reference purposes, should such a dev ever appear, lol. Many values had not
been updated after global refactors, like switching to the %risk data for all
arm/mips/ppc platform types, and making %load, %use, %force, %fake uses more
consistent. Doing this helped expose some subtle bugs and failure cases in
inxi as well.

2. Added to -h and man -Ga Nvidia option info. Fixed some typos and glitches.
Includes new --nvidia / --nv options for full data.

--------------------------------------------------------------------------------
CODE:

1. Changed $dl{'no-ssl-opt'} to $use{'no-ssl'} and $dl{'no-ssl'}, that was a
confusing inconsistency.

2. Added comma separated list of --dbg numbers, since often > 1 is used. Saves
some debugging time, otherwise nothing changes.

3. Huge new public release of some back end tools in new section:
inxi-perl/tools
* vendors.pl - disk vendors tool, with data in lists/disks*.txt
* ids.pl - nvidia product id generator tool, with data in lists/nv_*

4. While doing vendors.pl, I noticed that the use of array ref for $vendors was
not done correctly, that's fixed now, simplifies it slightly.

---
## [fizteh95/Athena](https://github.com/fizteh95/Athena)@[29264fc45e...](https://github.com/fizteh95/Athena/commit/29264fc45eab7a53b607ce99adf36ca5a25dffe9)
#### Friday 2022-05-20 12:02:16 by kutish

hoooly shit, fucking linter, i fucking hate you sooo much; linter fixes

---
## [spaceexpanse/rod-core-wallet](https://github.com/spaceexpanse/rod-core-wallet)@[619f8a27ad...](https://github.com/spaceexpanse/rod-core-wallet/commit/619f8a27ad0f6a44f0ad1a1e55a0aaaef7a91312)
#### Friday 2022-05-20 12:27:25 by MarcoFalke

Merge bitcoin/bitcoin#24304: [kernel 0/n] Introduce `bitcoin-chainstate`

2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 ci: Build bitcoin-chainstate (Carl Dong)
095aa6ca37bf0bd5c5e221bab779978a99b2a34c build: Add example bitcoin-chainstate executable (Carl Dong)

Pull request description:

  Part of: #24303

  This PR introduces an example/demo `bitcoin-chainstate` executable using said library which can print out information about a datadir and take in new blocks on stdin.

  Please read the commit messages for more details.

  -----

  #### You may ask: WTF?! Why is `index/*.cpp`, etc. being linked in?

  This PR is meant only to capture the state of dependencies in our consensus engine as of right now. There are many things to decouple from consensus, which will be done in subsequent PRs. Listing the files out right now in `bitcoin_chainstate_SOURCES` is purely to give us a clear picture of the task at hand, it is **not** to say that these dependencies _belongs_ there in any way.

  ### TODO

  1. Clean up `bitcoin-chainstate.cpp`
     It is quite ugly, with a lot of comments I've left for myself, I should clean it up to the best of my abilities (the ugliness of our init/shutdown might be the upper bound on cleanliness here...)

ACKs for top commit:
  ajtowns:
    ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0
  ryanofsky:
    Code review ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0. Just rebase, comments, formatting change since last review
  MarcoFalke:
    re-ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 🏔

Tree-SHA512: 86e7fb5718caa577df8abc8288c754f4a590650d974df9d2f6476c87ed25c70f923c4db651c6963f33498fc7a3a31f6692b9a75cbc996bf4888c5dac2f34a13b

---
## [robins/postgres](https://github.com/robins/postgres)@[c40ba5f318...](https://github.com/robins/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Friday 2022-05-20 13:13:49 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [ahayworth/opentelemetry-ruby](https://github.com/ahayworth/opentelemetry-ruby)@[45429c7d53...](https://github.com/ahayworth/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Friday 2022-05-20 15:08:53 by Andrew Hayworth

Split CI builds by gems at top-level (#1249)

* fix: remove unneeded Appraisals for opentelemetry-registry

It's not actually doing anything, so we skip it.

* ci: remove ci-without-services.yml

We're going to bring back these jobs in the next few commits, but we can delete it right now.

* ci: remove toys/ci.rb

We're going to replicate this in Actions natively, so that we can get
more comprehensible build output.

* ci: replace toys.rb functionality with an explosion of actions + yaml

This replaces the "test it all in a loop" approach that `toys/ci.rb` was
taking, by leveraging some more advanced features of GitHub Actions.

To start, we construct a custom Action (not a workflow!) that can run
all the tests we were doing with `toys/ci.rb`. It takes a few different
inputs: gem to test, ruby version to use, whether or not to do rubocop,
etc. Then, it figures out where in the repo that gem lives, sets up ruby
(including appraisals setup, if necessary), and runs rake tests (and
then conditionally runs YARD, rubocop, etc).

Then, over in `ci.yml`, we list out all of the gems we currently have
and chunk them up into different logical groups:

- base (api, sdk, etc)
- exporters
- propagators
- instrumentation that requires sidecar services to test
- instrumentaiton that doesn't require anything special to test

For most groups, we set up a matrix build of operating systems (ubuntu,
macos, and windows) - except for the "instrumentation_with_services"
group, because sidecar services are only supported on linux.

For each matrix group (gem + os), we then have a build that has multiple
steps - and each step calls the custom Action that we defined earlier,
passing appropriate inputs. Each step tests a different ruby version:
3.1, 3.0, 2.7, or jruby - and we conditionally skip the step based on
the operating system (we only run tests against ruby 3.1 for mac /
windows, because the runners are slower and we can't launch as many at
once).

Notably, we have a few matrix exclusions here: things that wont build on
macos or windows, but there aren't many.

Finally, each group also maintains a "skiplist" of sorts for jruby -
it's ugly, but some instrumentation just doesn't work for our Java
friends. So we have a step that tests whether or not we should build the
gem for jruby, and then the jruby step is skipped depending on the
answer. We can't really use a matrix exclusion here because we don't use
the ruby version in the matrix at all - otherwise we'd have a *huge*
explosion of jobs to complete, when in reality we can actually install +
test multiple ruby versions on a single runner, if we're careful.

The net effect of all of this is that we end up having many different
builds running in parallel, and if a given gem fails we can *easily* see
that and get right to the problem. Builds are slightly faster, too.

The major downsides are:
- We need to add new gems to the build list when we create them.
- We can't cache gems for appraisals, which adds a few minutes onto the
  build times (to be fair, we weren't caching anything before)
- It's just kinda unwieldy.
- I didn't improve anything around the actual release process yet.

Future improvements could be:
- Figuring out how to cache things with Appraisals, because I gave up
  after a whole morning of fighting bundler.
- Dynamically generating things again, because it's annoying to add gems
  to the build matrices.

* feat: add scary warning to instrumentation_generator re: CI workflows

* fix: remove testing change

* ci: Add note about instrumentation_with_services

---
## [GuiltyNeko/Skyrat-tg](https://github.com/GuiltyNeko/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/GuiltyNeko/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Friday 2022-05-20 16:14:57 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [veita/libpod](https://github.com/veita/libpod)@[e74717f348...](https://github.com/veita/libpod/commit/e74717f348c2768b87cad7dd6997c42dc85fc50a)
#### Friday 2022-05-20 16:38:29 by Ed Santiago

Treadmill script: revamp

Major revamp: instead of stacking a vendor commit on top of
the treadmill changes, do it the other way around: vendor,
then apply treadmill diffs.

Reason: the build-all-new-commits test. Sigh. It fails in the
common case where our treadmill changes include a new struct
element in cmd/podman/images/build.go

Why this is good: well, superficially, it's more intuitive.

Why this is horrible: omg the rebasing games are a nightmare.
When the vendor commit is on top (HEAD), it's ultra-trivial
to drop it, rebase the treadmill changes on main, then add
a new vendor-buildah commit on top. As you can see from the
diffs in this PR, treadmill-as-HEAD introduces all sorts
of complex dance steps in which things can go catastrophically
wrong and you can lose all your treadmill patches. I try very
hard to prevent this, and to offer hints if there's a problem,
and heck in the worst case it's still git so it's still possible
to find lost commits... but it's still much riskier than the
old way.

Alternative I considered: using sed magic to disable the
build-all-new-commits test. So tempting... but that would
also disable the bloat check.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [vincenthonda/Recipe](https://github.com/vincenthonda/Recipe)@[6e6f219b29...](https://github.com/vincenthonda/Recipe/commit/6e6f219b2986ca404f6b33f5b5db1837f1394334)
#### Friday 2022-05-20 16:58:39 by vincenthonda

HOLY FUCKKKKKK LMFAOOOOOOOOO HOW THIS SHIT STILL NOT WORk

---
## [linux-kdevops/kdevops](https://github.com/linux-kdevops/kdevops)@[867ccb7540...](https://github.com/linux-kdevops/kdevops/commit/867ccb754066ad7140a682a92973c4ac6780a437)
#### Friday 2022-05-20 17:24:36 by Luis Chamberlain

reboot-limit: add a systemd-analyze clutch at bootup

If you run systemd-analyze at bootup it may fail with:

$ sudo systemd-analyze
Bootup is not yet finished (org.freedesktop.systemd1.Manager.FinishTimestampMonotonic=0).
Please try again later.
Hint: Use 'systemctl list-jobs' to see active jobs

When running the reboot-limit test demo workflow to test to see
how many boots can happen without failure on a system we need
then to add a wait-for-boot-to-complete clutch before we run
the systemd-analyze (when that is enabled).

We can accomplish this with:

systemctl is-system-running --wait

So add that if before we collect systemd-analyze results.
This is only applicable when CONFIG_REBOOT_LIMIT_ENABLE_SYSTEMD_ANALYZE=y.
Later on we *may* want to just use this and remove the silly
arbitrary delay on bootup post_reboot_delay. Using this
$(systemctl is-system-running --wait) may be nice for complex nodes
where bootup may take a while, otherwise we're just rebooting *as*
soon as the post_reboot_delay completes and perhaps that may do
some insane things.

But since CONFIG_REBOOT_LIMIT_ENABLE_SYSTEMD_ANALYZE=y is the default
today we simpley force using $(systemctl is-system-running --wait)
systemd-analyze is going to be used, that is always by default today
anyways.

We can later make it a strong requirement all the time even if
you don't have CONFIG_REBOOT_LIMIT_ENABLE_SYSTEMD_ANALYZE=y, but
for now this makes sense as-is as we do want to try to speed up
reboots as much as possible.

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [Tokorizo/Pariah-Station-1](https://github.com/Tokorizo/Pariah-Station-1)@[23aef65ad5...](https://github.com/Tokorizo/Pariah-Station-1/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Friday 2022-05-20 17:33:59 by SabreML

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607) (#704)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [itsbilal/cockroach](https://github.com/itsbilal/cockroach)@[88b245aa46...](https://github.com/itsbilal/cockroach/commit/88b245aa469ee6302a25d3ac4cbe58b23927831d)
#### Friday 2022-05-20 17:52:36 by Josephine Lee

ui: Improve time picker keyboard input

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here]
(https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox]
(https://ant.design/docs/react/getting-started) (render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox]
(https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here]
(https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

---
## [javiereguiluz/EasyAdminBundle](https://github.com/javiereguiluz/EasyAdminBundle)@[919545baeb...](https://github.com/javiereguiluz/EasyAdminBundle/commit/919545baebcf0b7ae1f8a35210afc4bd92769161)
#### Friday 2022-05-20 18:39:16 by Javier Eguiluz

feature #5066 Allow `Translatable` objects in addition to `string` in translated context (Lustmored)

This PR was squashed before being merged into the 4.x branch.

Discussion
----------

Allow `Translatable` objects in addition to `string` in translated context

This PR is pretty massive, yet almost all of it's code changes are just enablers for features that are already in Symfony Forms (5.4+) and Symfony Translation (also 5.4+). It allows passing `Translatable` objects as labels and other parts.

### Background

Currently my main problem with EasyAdmin is translation extraction. I maintain pretty large project where translation extraction is build into workflow very tightly and using manual extraction is unmaintainable. Fortunately most translations in admin context have no parameters, so I can workaround that by doing:
```
yield TextField::new('name', (string) t('Client name'));
```
But that's just a dirty hack and works only when label needs no parameters to translate properly. This is why I would benefit greatly if EasyAdmin would simply allow those objects internally and I think other users would welcome it too :smiley:

I have tested those changes on real life projects and they worked like a charm :smile:

### Complexity (?)

As stated before most of the changes are just enablers. By just changing some signatures and adding very simple logic whenever EasyAdmin translates content I was able to pass `Translatable` objects to templates and Symfony Forms, where they handle it without any additional work.

### Backwards compatibility

Functional backwards compatibility is kept. By that I mean - if project uses strings in those contexts (or leaves them empty for Easy Admin to fill with default values), no incompatibility arises. Setters accept strings as before and getters will return those strings. Also - everything will be translated, as before.

Unfortunately the same cannot be said about class signatures. Summary of signature changes are as follows:

Final classes with signature changes:

- Config\Action (new, setLabel); only docblocks and deprecation logic
- Config\Menu\*MenuItem (constructors)
- Config\MenuItem (linkTo*, section, subMenu)
- Dto\ActionDto (getLabel, setLabel and private field)
- Dto\CrudDto (getEntityLabelInSingular, setEntityLabelInSingular,getEntityLabelInPlural, setEntityLabelInPlural, setCustomPageTitle, getHelpMessage, setHelpMessage)
- Dto\FieldDto (getLabel, setLabel, getHelp, setHelp)
- Dto\FilterDto (getLabel, setLabel); only docblocks
- Dto\MenuItemDto (getLabel, setLabel)
- Field\*Field (new); only docblocks
- Field\FormField (addPanel, addTab)

Non-final classes with signature changes:

- Config\Crud (setHelp)
- Field\FieldTrait (setLabel, setHelp); setLabel only in docblock

I wouldn't consider signature changes in setters in final classes as BI, but getters are - end user code might expect getter to return `?string`, while this PR changes it to `TranslatableInterface|string|null`. Again - in simple use case, where user is not using `Translatable` objects this assumption will still hold. But libraries, bundles and other code does not have such guarantee.

Also one non-final class and commonly used trait have signature changes in parameter types that will raise errors when inherited.

I don't see any way we can achieve the same without breaking BC, therefore I think this change can only target `5.0`. But I'd love to hear from the others :)

### TODO

- [x] get feedback
- [x] write tests for functional changes (probably just translating part, there is no point in testing getters and setters IMO)
- [x] Add UPGRADE/CHANGELOG entry documenting changes

Commits
-------

7596f24f Allow `Translatable` objects in addition to `string` in translated context

---
## [MetalfOxXer/Naruto_Ninpou](https://github.com/MetalfOxXer/Naruto_Ninpou)@[80cd503e06...](https://github.com/MetalfOxXer/Naruto_Ninpou/commit/80cd503e06b6da03cbec977535c84e603ab9b6ee)
#### Friday 2022-05-20 19:06:32 by MetalfOxXer

changes

- Reduced Roshi lava mode slow to 10%
- Fixed Hidan R not reflecting damage properly
- Fixed some descriptions
- Fixed Dark Totsuka life steal not working
- Fixed Fuu Yamanaka semi
- Rock Lee W doesn't push creeps anymore / Fixed sfx effect not moving with him
- Itachi additional heal on his D removed
- Return damage from Juubi Skin from Book of Gelel reduced by 50%
- Kid Gaara Q damage type changed from Magic to Normal
- Tenten's R is now slightly slower again
- Improved Torune's T animation slightly maybe
- Rikudou Naruto W from 50x HP and 25x Mana to 75x HP and 50x Mana

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[bead3f7475...](https://github.com/mrakgr/The-Spiral-Language/commit/bead3f74752792c065901fa819de06edaac10567)
#### Friday 2022-05-20 19:40:16 by Marko Grdinić

"7:50am. I am up, let me have some fun before getting started.

8:40am. Father dumped some work on me. It seems some guy will bring a laptop for me to fix. Since I do not get paid for these, I wish I could just say no to these assignments. I need my own income for that. Well, let me have some more fun and then I will start modeling.

9am. Let me start. I am fully satisfied with the morning session. It seems I missed Savage Fang ch 2, I'll leave it for later.

First of all, let me import the model that I did yesterday into the Blender scene. Then I'll take measure of the bed.

9:30pm. What the fuck. Why are the empties I am parenting the objects to just straight up disappearing?

...For some reason Blender was moving them into a hidden collection.

9:50pm. Perfect. I've set it up. Now let me move on to the bed.

2.15 .852 .602

These are the 3 dimensions. Let me start a new Moi file.

9:55am. It really makes it a lot easier for me to be able to just go in and modify the dimensions of a box directly. Previously, I did not know that and had to fiddle with typing in the targets manually. I also couldn't start the box off at center.

10am. Let me take just a short breather before I start.

10:05am. Ok, focus me. Enough reading /3/ threads.

10:15am. I've started work on the bed model. Let me take out the pen. It really won't be a difficult thing at all. I just have to get the dimensions of the several cubes that make it up correct.

10:35am. Laymen sure try interesting ways of fixing their computers. He says the laptop is blocked so he tried letting it run until the battery ran out. Damn it, let me just do the bed and then I'll check out what is wrong with it. It won't be difficult. If it is giving me trouble, I'll just wipe and reinstall the Windows. I have zero will to mess with it for long.

11:45am. i've messed around with the pillow for way too long. Especially considering I am going to be deforming it in the future. Let me take a break here. Ah, damn, I forgot to start the download for the course. I need to remember to do this.

1:10pm. Let me resume. First of all, let me check out that laptop. I wonder what the boomer meant by it being 'blocked'?

What happens when I boot it up is a bunch of porn pages on the front screen. And looking in the task manager, about 30 Avast instances. Most likely, the (literal) autist son of his went to watch porn and did not know well enough not to click on popups.

1:20pm. Ok, I will try disabling Avast on startup and restarting. If this problem turns out to be annoying, I'll just reinstall Windows.

1:25pm. Easiest side job ever. I guess I can resume modeling.

Regarding that, I really hate how big the fillets are. I am going to redo them.

2:05pm. This took a while. I am really happy with how the bed looks now.

2:10pm. As a matter of play, I tried putting in a bunch of cylinders on the bed. Could I draw something like that? Yeah, I could. Getting to creases from that point is by just adding a little wobbliness to the lines.

2:15pm. Modeling is fun. I can enter the zone just like when programming.

2:50pm. Sigh what mess, let me just redo the damn shelves. I need to do minor detailing on it anyway.

54.1 53.3 117

Let me go with these dimensions, this time in cm.

2:55pm. Damn it, let me check out that laptop a bit more. I did not try running the browset. It might be the case that it set the startup to some porn page.

3:20pm. Checked the laptop and took a break after that. Let me resume. Let me furniture piece out of the way.

4:15pm. Got the frame out of the way. Now I need to do the items. I am thinking how I should approach the modeling job, and surprisingly even though there are many items, I should be able to get away with just piecing together primitives.

The hardest thing for me to do in Moi would be blankets and creases, things like that. But that sort of thing would be easy with sculpting.

Imagine if I tried to draw creases, that would also be hard.

Inio Asano mentioned that he has trouble with foliage and organic objects. But things like those would be easy to scatter and sculpt.

4:20pm. If I go 3d -> drawing + paint over, it will be a lot easier to do things such as blankets.

One thing I would like to learn how to do is how to use other objects as coliders during sculpting. I don't think Blender can do this, but Zbrush should.

At any rate, if I go my chosen route, it will really be a lot easier to hide the fact that I won't be modeling actual blankets, but deformed solids instead. It would be really hard to model the interior of blankets.

Also, why not use cloth sims? There is no need to even hassle myself with sculpting. I have a lot of options.

Various approaches have their pros and cons.

I'll really be able to get a lot of liveliness from taking primitives and deforming them so they look more organic, and extracting the lines from that.

4:25pm. Let me take a break from ranting about modeling to make note of a recent event. That man came by to take his laptop and actually paid me. I charged him 30$. Usually my dad would be the one to pocket that money. A few days ago, one of my mom's friends came by and gave me a chocolates and also 30$ for fixing her laptop.

This is quite remarkable, as I am used to doing such work for free. Indeed, I would be more willing to work on these side jobs if they actually paid.

Another 8 times and I'll be able to afford a new GPU.

Let me back on track.

There are a lot of props in my rooms, but I really can simplify the, well enough.

Focus me, let me get through this part. I am very intimidated, but I should not be. Assuming I can do this, I'll be able to get that much closer to 3/5.

Oh, also, let me start downloding part 5. Only 2 left to go of the Zbrush for Illustrators course.

4:35pm. Before I start let ne just finish waiting for the 3m to pass properly, otherwise I run the risk of timing out again.

5:05pm. Damn it, now I am stuck trying to fillet a particular shape. On the bottom shelf, there is a fax machine + scanner. What is giving me trouble is the extruded triangle piece in the middle.

5:10pm. I know I said this would not be trouble, but clearly my skills are not up to par. I am also feeling quite fatigued by this point.

7pm. Done with lunch. I can't believe I am still messing with this. I really am a fool. Let me just ask at this point.

7:40pm. I am obsessed with this fillet issue. Let me do it for a bit longer. I can't really grasp why it cannot fillet this.

9pm. I've manged to grasp some things. For that middle fax piece, I got it to fillet in two ways. One is by cutting a bit in the middle so as to make room for the fillet in the front. The other is to scale the cutter so it does not intersect the outer corner. When I do that I get a line down the middle. This leads me to believe that the reason it has been failing is not because  those two narrowing curves were too close, but because there might be a microscopic edge next to another.

9:05pm. Also for the past hour, what I've done is gone back to the rig and investigated exactly why the door is failing.

I understand it now.

It seems Moi's fillets fail when the corners with 3 edges or more are too close to one another. Note that this is different from how it is in Blender. In Moi, being close does not depend solely on the given radius. I think it is using some kind of sampling scheme under the hood, so if the corners are too close it will fail even when realistically it should be able to do the fillet.

9:15pm. Sigh, filleting is so awkward in Moi. Even booleans can fail depending on the situation.

Seriously though, if I am doing drawing, I do not need fillets. It might just end up adding line noise. It might be worth exporting to Zbrush and doing the filleting there.

Moi would really be great if it wasn't for these weird inexplicable failures.

I am going to keep this experience in mind for the future. I should be able to use fillets more effectively in the future. For now let me close. Actually, before I do that let me review the list.

///

~* Fix the doors based on what the Moi author told me. As well as shorten one of the boards. Maybe even make it a bit thinner. I'll have to redo them to make this happen, but that is fine.~
~* Open the right grills a bit so the light can shine through properly.~
~* Remodel the beds, this time in Moi.~
~* Optionally the shelves as well.~
* Put the blankes on the bed.
* Use the clothes brush to create the creases.
* Model some extra objects on top of the shelves as well as in the shelves.
~* Do a sweep of the room edges with that stylized beveld wood specifically intended for corners.~

Optionally, I can also model the lights on top of the ceiling, but they aren't present in the scene. Still the ceiling is a bit empty. I'll leave these two from the light of points. The above is enough to busy me.

///

* Put the blankes on the bed.
* Use the clothes brush to create the creases.
* Model some extra objects on top of the shelves as well as in the shelves.

Only these 3 are left. I am further along that I thought.

* Ceiling light.
* Radiator.
* Door.

I'll skip these 3 as they aren't in view, but leave them in the journal as a reminder.

I'll finish the fax on the bottom self and the items tomorrow. After that, it will be doing the flats and looking into NPR rendering. It will be time to get something good out of the scene. I'll also do some drawing practice when that is done. If I am lucky maybe I will be able to post something before the month is over.

9:35pm. Hmmm, let me do a little search.

https://www.youtube.com/results?search_query=rhino+boolean+manual

Yeah, these are some Rhino related videos that go into why booleans fail. I should study these tomorrow. Damn, I am tired. I was tired at 5pm, and then I got obsessed with filleting. Let me close here."

---
## [Zynku/Project-Earthend](https://github.com/Zynku/Project-Earthend)@[26588fa76a...](https://github.com/Zynku/Project-Earthend/commit/26588fa76a3c631e5b7f2caee7a24e9cad899c40)
#### Friday 2022-05-20 20:03:21 by Zynku

Pre-Alpha 4.7.0 Trying to make healthbar look a little fancy

This shit took a whole day and I still don't fucking get it. Im angry and upset and fuck off and fuck you

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[c8ab3b10aa...](https://github.com/Perkedel/Kaded-fnf-mods/commit/c8ab3b10aa817306fc68f747733baf86a7a79267)
#### Friday 2022-05-20 21:16:59 by Joel Robert Justiawan

[skip ci] torgem

differentiateon. Realize between real & not. sorry, that shock you. I just tryna find random stuff I know of.

Oops, the extra parameter crashes the game somehow. let's leave them null.

size 0 errors! must atleast 1 pixel. tankman running john shot fix

recycle the tankman running!!!

oops! add the name goes wrong!!!

formateon save tankmen bg. Yeah, let's not destroy. just use `kill()` & `reset()` function.

---
## [git/git](https://github.com/git/git)@[bdaf1dfae7...](https://github.com/git/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Friday 2022-05-20 21:55:24 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [neemis/Movielens-Case-Study](https://github.com/neemis/Movielens-Case-Study)@[38cb051ebc...](https://github.com/neemis/Movielens-Case-Study/commit/38cb051ebc8dcd43e2e5a14c30622547bb0d23bc)
#### Friday 2022-05-20 22:57:43 by NEETI

Add files via upload

Analysis Tasks to be performed:

Import the three datasets
Create a new dataset [Master_Data] with the following columns MovieID Title UserID Age Gender Occupation Rating. (Hint: (i) Merge two tables at a time. (ii) Merge the tables using two primary keys MovieID & UserId)
Explore the datasets using visual representations (graphs or tables), also include your comments on the following:
User Age Distribution
User rating of the movie “Toy Story”
Top 25 movies by viewership rating
Find the ratings for all the movies reviewed by for a particular user of user id = 2696
Feature Engineering:
            Use column genres:

Find out all the unique genres (Hint: split the data in column genre making a list and then process the data to find out only the unique categories of genres)
Create a separate column for each genre category with a one-hot encoding ( 1 and 0) whether or not the movie belongs to that genre. 
Determine the features affecting the ratings of any particular movie.
Develop an appropriate model to predict the movie ratings
Dataset Description :

These files contain 1,000,209 anonymous ratings of approximately 3,900 movies made by 6,040 MovieLens users who joinedMovieLens in 2000.

Ratings.dat
    Format - UserID::MovieID::Rating::Timestamp

Field	Description
UserID	Unique identification for each user
MovieID	Unique identification for each movie
Rating	User rating for each movie
Timestamp	Timestamp generated while adding user review
UserIDs range between 1 and 6040 
The MovieIDs range between 1 and 3952
Ratings are made on a 5-star scale (whole-star ratings only)
A timestamp is represented in seconds since the epoch is returned by time(2)
Each user has at least 20 ratings
 

Users.dat
Format -  UserID::Gender::Age::Occupation::Zip-codeField	Description
UserID	Unique identification for each user
Genere	Category of each movie
Age	User’s age
Occupation	User’s Occupation
Zip-code	Zip Code for the user’s location
All demographic information is provided voluntarily by the users and is not checked for accuracy. Only users who have provided demographic information are included in this data set.

Gender is denoted by an "M" for male and "F" for female
Age is chosen from the following ranges:
 

Value	Description
1	"Under 18"
18	"18-24"
25	"25-34"
35	"35-44"
45	"45-49"
50	"50-55"
56	"56+"
 

Occupation is chosen from the following choices:
Value
 	Description
0	"other" or not specified
1	"academic/educator"
2	"artist”
3	"clerical/admin"
4	"college/grad student"
5	"customer service"
6	"doctor/health care"
7	"executive/managerial"
8	"farmer"
9	"homemaker"
10	"K-12 student"
11	"lawyer"
12	"programmer"
13	"retired"
14	 "sales/marketing"
15	"scientist"
16	 "self-employed"
17	"technician/engineer"
18	"tradesman/craftsman"
19	"unemployed"
20	"writer”

Movies.dat
Format - MovieID::Title::Genres

Field	Description
MovieID	Unique identification for each movie
Title	A title for each movie
Genres	Category of each movie
 

 Titles are identical to titles provided by the IMDB (including year of release)
 

Genres are pipe-separated and are selected from the following genres:
Action
Adventure
Animation
Children's
Comedy
Crime
Documentary
Drama
Fantasy
Film-Noir
Horror
Musical
Mystery
Romance
Sci-Fi
Thriller
War
Western
Some MovieIDs do not correspond to a movie due to accidental duplicate entries and/or test entries
Movies are mostly entered by hand, so errors and inconsistencies may exist

---

