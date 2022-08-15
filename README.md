## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-14](docs/good-messages/2022/2022-08-14.md)


1,573,053 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,573,053 were push events containing 2,108,062 commit messages that amount to 120,329,902 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [LZ1WS/Before_The_Dead_Slashers_Revamped](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped)@[1410379994...](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped/commit/14103799945c59807669efa349f61f758d991bde)
#### Sunday 2022-08-14 00:08:50 by LZ1WS

1.1.3

#"From all around the world" Survivor Expansion Update#
| Added |
- New Survivors:
  - Drake
#A medical officer with extensive experience in his specialty. Not a fan of listening to instructions and, for the most part, self-taught, trusting his criteria for assessing the condition of patients. Nevertheless, he copes well with his work, which proves the effectiveness of his methods#
  - Theodore
#A survivor using a boombox to distract attention. Has only one 'Box' with him, therefore, and one chance to get rid of unnecessary attention for a certain time.#
  - Daniel
#You were here, when everything changed, and you were the first to sight those changes and capture them on your best device. Use your trusty photo camera to blind a killer for a couple of seconds, granting you the ability to escape, hide or save your teammates.#
  - David
#You're here to spread the holy word and banish the beast that terrifies your friends. Use your holy power, to weaken the beast that is hunting you and your friends.#
  - Lucas
#They say that bad addictions only lead into the grave, but you're the alive refutation of this. Use your medicine to buff your speed and quickly run from the killer.#
- Bear Traps for Sheldon
- Animations to the Hub F4 Menu
- Sounds for the buttons in Hub F4 Menu
- An access type in ulx which grants the ability for the usergroup to set a survivor from a F4 menu

| Changed |
- Frost Magic SWEP for Tirsiak
- F4 GUI redesign
- Simons description was rewritten
#A sense of danger and intuition are not the words that can describe your peculiarity in the ability to detect an approaching threat. Darkness and troubles seem to find you by themselves. The constant feeling of persecution and observation by otherworldly beings has affected your mental state. You can use it to see the world through the eyes of a creature.#
- Removed surnames from Survivors that had them
- Changed name of the gamemode in menu to BTD Slashers Revamped
- Changed GM.Github and GM.Workshop in shared.lua
- Reworked survivors abilities in code to make them easier to implement
- Now Hub F4 Menu uses an core gamemode table of Survivors, instead of the custom manual one

| Fixed |
- Steve's Ability (minor bug)

#1.1.3 version patch-notes#
| Changed |
- Minor translations changes

| Fixed |
- Theodore's boombox now functions properly
- F4 Hub Menu admin's survivor class setting now functions properly
- Redone the visual part of Priest's power on killer perspective
- Fixed sonic speed on hit exploit
- Daniel no longer blinds himself

---
## [MLGTASTICa/CEV-Eris](https://github.com/MLGTASTICa/CEV-Eris)@[f0caf86c2b...](https://github.com/MLGTASTICa/CEV-Eris/commit/f0caf86c2b96c1af70118f8dab8e70b5de90a0ac)
#### Sunday 2022-08-14 01:07:08 by MLGTASTICa

Merge branch 'master' into fucking-shitty-moebius-gamer-upgrades-why-was-it-ever-added-i-hate-moebius-mains

---
## [nosvagor/dotfiles](https://github.com/nosvagor/dotfiles)@[c44eb2fd7a...](https://github.com/nosvagor/dotfiles/commit/c44eb2fd7a813ee2d815f12c3ad364bafd8363e3)
#### Sunday 2022-08-14 01:12:34 by nosvagor

oh my god, I should have been using eww this whole time. Fuck waybar

---
## [regehr/llvm-project](https://github.com/regehr/llvm-project)@[e17cae076c...](https://github.com/regehr/llvm-project/commit/e17cae076c4727b99017927c3e8746db5bec6db7)
#### Sunday 2022-08-14 01:17:38 by Walter Erquinigo

[trace][intel pt] Fix per-psb packet decoding

The per-PSB packet decoding logic was wrong because it was assuming that pt_insn_get_sync_offset was being udpated after every PSB. Silly me, that is not true. It returns the offset of the PSB packet after invoking pt_insn_sync_forward regardless of how many PSBs are visited later. Instead, I'm now following the approach described in https://github.com/intel/libipt/blob/master/doc/howto_libipt.md#parallel-decode for parallel decoding, which is basically what we need.

A nasty error that happened because of this is that when we had two PSBs (A and B), the following was happening

1. PSB A was processed all the way up to the end of the trace, which includes PSB B.
2. PSB B was then processed until the end of the trace.

The instructions emitted by step 2. were also emitted as part of step 1. so our trace had duplicated chunks. This problem becomes worse when you many PSBs.

As part of making sure this diff is correct, I added some other features that are very useful.

- Added a "synchronization point" event to the TraceCursor, so we can inspect when PSBs are emitted.
- Removed the single-thread decoder. Now the per-cpu decoder and single-thread decoder use the same code paths.
- Use the query decoder to fetch PSBs and timestamps. It turns out that the pt_insn_sync_forward of the instruction decoder can move past several PSBs (this means that we could skip some TSCs). On the other hand, the pt_query_sync_forward method doesn't skip PSBs, so we can get more accurate sync events and timing information.
- Turned LibiptDecoder into PSBBlockDecoder, which decodes single PSB blocks. It is the fundamental processing unit for decoding.
- Added many comments, asserts and improved error handling for clarity.
- Improved DecodeSystemWideTraceForThread so that a TSC is emitted always before a cpu change event. This was a bug that was annoying me before.
- SplitTraceInContinuousExecutions and FindLowestTSCInTrace are now using the query decoder, which can identify precisely each PSB along with their TSCs.
- Added an "only-events" option to the trace dumper to inspect only events.

I did extensive testing and I think we should have an in-house testing CI. The LLVM buildbots are not capable of supporting testing post-mortem traces of hundreds of megabytes. I'll leave that for later, but at least for now the current tests were able to catch most of the issues I encountered when doing this task.

A sample output of a program that I was single stepping is the following. You can see that only one PSB is emitted even though stepping happened!

```
thread #1: tid = 3578223
    0: (event) trace synchronization point [offset = 0x0xef0]
  a.out`main + 20 at main.cpp:29:20
    1: 0x0000000000402479    leaq   -0x1210(%rbp), %rax
    2: (event) software disabled tracing
    3: 0x0000000000402480    movq   %rax, %rdi
    4: (event) software disabled tracing
    5: (event) software disabled tracing
    6: 0x0000000000402483    callq  0x403bd4                  ; std::vector<int, std::allocator<int>>::vector at stl_vector.h:391:7
    7: (event) software disabled tracing
  a.out`std::vector<int, std::allocator<int>>::vector() at stl_vector.h:391:7
    8: 0x0000000000403bd4    pushq  %rbp
    9: (event) software disabled tracing
    10: 0x0000000000403bd5    movq   %rsp, %rbp
    11: (event) software disabled tracing
```

This is another trace of a long program with a few PSBs.
```
(lldb) thread trace dump instructions -E -f                                                                                                         thread #1: tid = 3603082
    0: (event) trace synchronization point [offset = 0x0x80]
    47417: (event) software disabled tracing
    129231: (event) trace synchronization point [offset = 0x0x800]
    146747: (event) software disabled tracing
    246076: (event) software disabled tracing
    259068: (event) trace synchronization point [offset = 0x0xf78]
    259276: (event) software disabled tracing
    259278: (event) software disabled tracing
    no more data
```

Differential Revision: https://reviews.llvm.org/D131630

---
## [mxraw/dwm](https://github.com/mxraw/dwm)@[67d76bdc68...](https://github.com/mxraw/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-08-14 01:34:00 by Chris Down

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
## [BSCPGROUPHOLDINGSLLC/REPO1](https://github.com/BSCPGROUPHOLDINGSLLC/REPO1)@[936a23f4c3...](https://github.com/BSCPGROUPHOLDINGSLLC/REPO1/commit/936a23f4c349d014f83188075acac5cade5d42a8)
#### Sunday 2022-08-14 01:42:35 by 1212-5858

peeping tom papers, sorry I asked them first... the 18th Precinct.

101 WEST 55TH STREET, MANHATTAN, 10019, BETWEEN 6TH AND 7TH,
ENJOY, and I apologize but "peeping toms" belong in a USP, especially after committing a laundry list of felony - plural.

*** PAUL R. REGAN, ESQ.    [NYS BAR # 2623577]

*** JOSEPH J. GIAMBOI, ESQ. [NYS BAR # 2104396]

*** DANIEL F. SULLIVAN, ESQ. [NYS BAR # 2383347]

*** SHARI S. LASKOWITZ, ESQ. [NYS BAR # 3041015]

***  CORY L. WEISS, ESQ.   [NYS BAR # 2327187]

      NYSCEF 153974/2020

ATTACHED HERE FOR EASE OF YOUR REFERENCE IS THE

- THE WARNING OF A LAWSUIT FROM PAUL REGAN, TO AVOID YOUR PRECINCT AND JURISDICTION.

- CONFIRMATION NOTICE, AND ALSO A VERIFIED COMPLAINT ADMITTED INTO THE NEW YORK SUPREME COURT WITHOUT ANY RECOURSE.

- AS INSET IN MY REQUEST TO THE COURT, LANDLORD, AND ITS AGENTS, AFFILIATES, ENTITIES, AND THIRD-PARTY SERVICE PROVIDERS.

HAVING LEARNED THE PRIOR CASE WAS DISMISSED WITH PREJUDICE, THE CONGLOMERATE OF ENTITIES, INDIVIDUALS, REPRESENTATIVES, AND THIRD-PARTY SERVICE PROVIDERS WHO JOINTLY AND SEVERALLY HARASSED ME FOR AN EXTENDED PERIOD OF TIME, POSSESSES AND ENTERED THE STILL FRAMES OF MYSELF IN MY APARTMENT - ADMITTED / ENTERED UNDER THE FOLLOWING... YOU SHOULD DO THE SAME.

INDEX NO. 153974/2020 IN JUNE OF 2020 IN FULL COLOR.
     Sullivan Properties L.P. v. Baris Dincer
      New York County Supreme Court
      Assigned Judge: Shlomo S. Hagler

THE CAMERAS WERE NEVER REMOVED WHILE I RESIDED THERE...  ALL VIDEOTAPES ARE STILL IN THE CUSTODY OF THE ZUCKER FAMILY, THEIR ENTITIES STOLE MONEY FROM ME - UNLAWFUL LEGAL FEES WERE AUTO-BILLED, PAID, AND HAVE NOT BEEN RETURNED

>> TO THE EXCESS OF $5000.00 AND HAVE NOT BEEN RETURNED IN OVER A YEAR,
DOCKET NUMBER 48, YOU SEE MY FOREHEAD? THEY WATCHED ME 24/7 AND REFUSE TO RETURN MY SEX TAPES AS WELL.
ALSO, COMMITTED PERJURY UNDER OATH, VIOLATED MY PRIVACY, SANCTITY, AND DESPITE MY REQUESTS TO THE JUDGE, AND THE NEW YORK CITY POLICE DEPARTMENT PRECINCTS... THEIR CONGLOMERATE OF ENTITIES, INDIVIDUALS, REPRESENTATIVES, AND THIRD-PARTY SERVICE PROVIDERS EQUIPPED THEMSELVES TO VIDEOTAPE ME IN THE DARK IN CERTAIN INSTANCES.

THEY HAD A DEEP VIEW INSIDE OF MY APARTMENT (ALL THE WAY INSIDE THROUGH THE WINDOW, AND TO THE BACK WALL OF MY CLOSETS) WHICH IS WHY I ALSO INCLUDED THE YOUTH COORDINATOR IN CASE THEY ARE WATCHING THE CHILDREN AS WELL. THANKFULLY, I AM LEGAL BUT I HAVE NO IDEA WHY THEY WONT RETURN MY VIDEOS... I ASKED THEM NICELY, AND NOW I HAVE TO EMAIL THE PLAZA DISTRICT POLICE DEPARTMENT?

FOR OVER 6 MONTHS.. THIS FAMILY DEMONSTRATED AN OBSESSIVE STALKING OF MY LIFE, WHICH CONTINUES AS I PRESENT THE COURTS, NYPD, A VOICEMAIL FROM THEIR GENERAL COUNSEL THREATENED MY LIFE, TO FOLLOW ME TO THE END OF THE WORLD...

THE JUDGE DID NOT ORDER AN IMMEDIATE ORDER TO CEASE AND DESIST FILMING, HOWEVER VACATED THEIR PLEADINGS, GRANTED NO AWARD FOR THE PURPORTED DAMAGES TO A BUILDING THAT WAS LEASED WITHOUT A CERTIFICATE OF OCCUPANCY, INSURANCE, OR A SPRINKLER SYSTEM. DESPITE THEIR PLEADINGS, AND DISMISSAL OF ALL CLAIMS BY THE PLAINTIFF IN THE FORMER... THE JUDGE, AND HIS CLERK (WILLIAM MCKENZIE) HAVE ALSO NOT RESPONDED TO MY EMAILS, REQUESTS TO ENJOIN OTHER PARTIES, AND HAVE IGNORED THE FACSIMILES I SENT REQUESTING MY TAPES. GETTING DRESSED, UNDRESSED, ALL WITHOUT CONSENT - AS ENTERED.

I FEAR THERE IS AN UNDERLYING SEXUAL INNUENDO, AND I FEAR THESE TAPES WILL SURFACE ON THE INTERNET... THEY HOLD ALL OF THESE IN THEIR POSSESSION, WHETHER FOR ECONOMIC OR PERSONAL SATISFACTION IS ABSOLUTELY UNACCEPTABLE AS THE FILMS WERE TAPED WITHOUT MY CONSENT, AND AS A COURTESY AND GOOD MORAL CONDUCT AS ATTORNEYS, AND BUSINESS OWNERS... FOUND IT A NECESSITY TO REPORT MY DAILY ACTIVITIES IN WRITING AS ENTERED, WHICH IS TRULY PATHETIC.

THEY LISTED A SCHEDULE OF ALL OF THEIR PROPERTIES, HOWEVER... ONE OF THEIR CAMERA WAS AIMED AT MY BED, RECORDED ME 24 HOURS A DAY, AND THE ZUCKER ENTITIES ALL CONDUCT THEIR BUSINESS FROM 101 WEST 55TH STREET, NEW YORK, NY, 10019.

MOST SINCERELY YOURS,

BARIS DINCER

and also:: gaspargardes.
via.
Michael Schulte <mschulte@corcoran.com>

---
## [reframedultimate/ReFramed](https://github.com/reframedultimate/ReFramed)@[4f5e44bc89...](https://github.com/reframedultimate/ReFramed/commit/4f5e44bc895f77462a896368333c1b6c3db3bfc4)
#### Sunday 2022-08-14 03:07:03 by TheComet

Able to open video files from memory now. API is wonky though, needs refactoring. Fixed annoying decoding issue where it no longer shits the bed when invalid packets are read

---
## [iLVL-Key/FFXI](https://github.com/iLVL-Key/FFXI)@[a7a1b6c4ac...](https://github.com/iLVL-Key/FFXI/commit/a7a1b6c4acecb8a1299ba9e9953242183a580abb)
#### Sunday 2022-08-14 04:11:53 by iLVL-Key

08.13.22 (VCC: Tachi: Hobaku)

-Added Leafallia to list of towns.
-Added equipping the DT Override set when petrified, stunned, or terrored.
-Added option to remove all gear (except weapons) when you are charmed.
-Added a Holy Water set.
-Adjusted the Vim Torque code to first remove Stoneskin if its up, then check that we're not already poisoned and HP is above 50.
-Adjusted abilities to not equip their gear sets if they are still on cooldown.
-Renamed LockstyleField to LockstyleCombat. Just makes more sense.
-Fixed an issue where the debuff background color change from Doom (flashing white and yellow) would get stuck on yellow after Doom wears off and you have another debuff on that takes over in the debuff spot.
-Fixed a duplicate line in the sleep debuff code.
-Updated Version Compatibility Codename to Tachi: Hobaku.
-Code cleanup.

---
## [iLVL-Key/FFXI](https://github.com/iLVL-Key/FFXI)@[ca161d311f...](https://github.com/iLVL-Key/FFXI/commit/ca161d311f2e634be5ed5bb2d354c879057faf10)
#### Sunday 2022-08-14 04:27:19 by iLVL-Key

08.13.22 (VCC: Sandspin)

-Added Leafallia to list of towns.
-Added cancelling Stonekin if its preventing poison from removing sleep, otherwise equip the Opo-opo Necklace per usual.
-Added equipping the DT Override set when petrified, stunned, or terrored.
-Added option to remove all gear (except weapons) when you are charmed.
-Adjusted abilities to not equip their gear sets if they are still on cooldown.
-Split the Cursna set into Cursna and Holy Water.
-Renamed LockstyleField to LockstyleCombat. Just makes more sense.
-Fixed an issue where the debuff background color change from Doom (flashing white and yellow) would get stuck on yellow after Doom wears off and you have another debuff on that takes over in the debuff spot.
-Fixed an issue where resting would combine the Rest set with the DT Override set regardless of DT Override being on or off.
-Removed the leftover Enmity gear set. The functionality for this set was removed in a previous version, I simply forgot to remove the gear set.
-Updated Version Compatibility Codename to Sandspin.

---
## [noreenko/RWoM](https://github.com/noreenko/RWoM)@[bc6c0ffd17...](https://github.com/noreenko/RWoM/commit/bc6c0ffd17f558adff1415ef80408b309c434157)
#### Sunday 2022-08-14 04:41:48 by TorannD

v2.5.8.0 update

New:
 o Advanced Classes
  - Unique type of custom class that can be added (or removed) onto existing classes
  - Share the same pawn level and displays on the same might/magic tabs with base class, and other advanced classes
  - Advanced classes share the same xml definition as normal classes, but are identified using the <isAdvancedClass> tag
  - See the Possessed class for an example
  - Other options for advanced classes include:
	* Restrict the advanced class to require a base class first using <requiresBaseClass> (true/false)
	* Allow the advanced class to be added as a trait during pawn generation with <canSpawnWithClass> (true/false)
	* Create advanced class "chains" by removing a pre-requisite trait with <removeRequiredTrait> (true/false)
	* Specify one or more valid pre-requisite traits using <requiredTraits> (TraitDef list)
	* Prevent pawns with certain traits from becoming the advanced class using <disallowedTraits> (TraitDef list)

 o Chained abilities
  - TMAbilityDef options that allow temporary abilities to be added and removed to create ability chains
  - See Possessed Control Spirit Storm for an example
  - Options include:
	* Specify a chained ability <chainedAbility> (TMAbilityDef)
	* Manually set a duration for the temporary ability <chainedAbilityExpiresAfterTicks> (integer > 0, -1 for "do not use")
	* Link the chained ability to be removed when the main ability cooldown expires <chainedAbilityExpiresAfterCooldown> (true/false)
	* Remove the ability after use; can be applied to any ability <removeAbilityAfterUse> (true/false)
	* Remove a list of abilities after use to clear or reset an ability chain <abilitiesRemovedWhenUsed> (TMAbilityDef list)

 o New Class: Possessor - an invisible, wandering spirit able to possess the bodies of the dead or living using spirit energy
  - Perishes when spirit energy fully depletes
  - Uses spirit energy to fuel their abilities
  - Able to possess other bodies and augments the abilities of the occupied body
  - Able to possess a corpse with all skills, talents, and memories of the dead pawn, but spirit energy will gradually deplete and must be replenished
  - Able to possess animals and assert control over their actions; the spirit has limited influence while in the body of an animal and spirit energy gradually depletes
  - Able to possess living pawns; much lower spirit energy loss than other options, but the host pawn will have conflicting thoughts - this can be offset if the spirit and the host pawn share the same outlook on life (backstory preferences, traits, gender, ideo, etc)
  - Shard of spirit extraction is used to remove a spirit from a pawn; the spirit may exit the body of an animal at any time
  - The possessor may naturally gain spirit energy while doing common, meditative tasks and can forcefully gain spirit energy using an ability or inflicting melee damage
  - A pawn occupied by a possessor will no longer be able to heal naturally; wounds can only be healed by external items, abilities, or spells, or when the possessed pawn gains spirit energy (by any means)

 o New Autocast options:
  - <onlyAppliesToCaster> (true/false) - forces the condition check against the caster instead of the target, when different
  - <targetNoFaction> (true/false) - target pawn is only selected if the faction is null (wild pawns)

Tweaks:
 o Summoned creatures will respond more aggressively when summoned near enemies
 o Magic Wardrobe automatically sets swapped equipment as forced/locked
 o Changed Brand graphics to be less error prone

Bug fixes:
 o Polymorphed or shapeshifted animals will take drafted orders again
 o Taunted targets will no longer attempt to attack a deceased taunter
 o Fixed a bug where AI would not use abilities if autocasting was disabled
 o Winter's Reign and Snap Freeze correctly assign damage attribution
 o Cure Disease can be cast while wearing a shield belt
 o Defense pylon will only spam invalid location message once instead of infinitely

---
## [BSCPGROUPHOLDINGSLLC/REPO1](https://github.com/BSCPGROUPHOLDINGSLLC/REPO1)@[50f372dba0...](https://github.com/BSCPGROUPHOLDINGSLLC/REPO1/commit/50f372dba0c7421fecef47b67de6001378823fa1)
#### Sunday 2022-08-14 05:11:36 by 1212-5858

FOLDER 1 WITH ZIP CONTAINERS FOR 2000 CHARACTERS

### NOTWITHSTANDING THE US. DEPT OF JUSTICE.
18 U.S. Code § 1512 - Tampering with a witness, victim, or an informant<br>

*** Fwd: Fwd: [ USC Title 18.1512 ] [USC Title 18.225, USC Title 18.21, USC Title 18.4, USC Title 18.3, USC Title 18.2]<br>

NYSCEF MATTER 153974/2020 WHILE THEY CASUALLY VIOLATED MY CIVIL RIGHTS<br>

NO COMPLAINTS HAVE BEEN FILED IN MY BUILDING<br>

- PER DEPARTMENT OF BUILDINGS RECORD CONTRARY TO THOSE "COMPLAINTS" WHICH ARE UN-TRUE.<br>
<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=AgwH2omenQPCvT0OYOE3Rg==><br>

### ACCESSORIES TO THIS OTHER FILING

HALE DINCER <+15168841083@tmomail.net>, SHARI LASKOWITZ <slaskowitz@ingramllp.com>,<br>
SHARI LASKOWITZ <+13478801899@tmomail.net> , HALE DINCER <hidincer@aol.com> <br>
PAUL REGAN <legal@mskyline.com>, LAURIE ZUCKER <lzucker@mskyline.com>, <br>
DAPHNE DINCER <DAPHNE.DINCER@GMAIL.COM>, ASHLEY HUMPHRIES <ASHLEY.HUMPHRIES@WILSONESLER.COM>, <br>
CORY WEISS <CWEISS@INGRAMLLP.COM>, ANA LOPEZ <LEGALASST@MSKYLINE.COM>, <br>
DONALD ZUCKER <ADMINISTRATOR@MSKYLINE.COM>, STEPHEN O'CONNEL <SGO2107@COLUMBIA.EDU>, <br>
<br><br>
[VOICEMAIL FROM PAUL REGAN: AFFIRM THE THREAT](https://support.nysba.org/attachments/token/TQXA7meSdnDIBt5SuKAuW0imP/?name=voicemail+917-843-3456.mp3)
*** CHECK THAT THREAD AND GET BACK TO ME AS WELL PLEASE.
While dealing with their business in Brooklyn, New York. <br>
— Kept me pre-occupied without cause to take care of their other business without my opinion or any reveal as to what they really do for a living.<br>
<br>
For example:

>> Hon. Nancy T. Sunshine, Kings County Clerk <br>
         and Clerk of the Supreme Court <br>

<https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=HD6/wXvlOxflJUlQyXqedQ==><br>

     case number:          400842/2020<br>
     Filed:                        09/23/2020<br>
     *** KINGS COUNTY *** <br>

Zucker Enterprises LLC <br>
             - v. -
THE TAX COMMISSION OF THE CITY OF NEW YORK, AND THE COMMISSIONER OF FINANCE OF THE CITY OF NEW YORK

>> 6.24.2020 email - ASHLEY.HUMPHRIES@WILSONELSER.COM

THIS REPORT WAS ALSO OBSTRUCED - WHILE IN TRANSIT TO THE DEPARTMENTS WHERE APPLICABLE<br>

[VOICEMAIL FROM GENERAL COUNSELOR OF MANHATTAN SKYLINE MANAGEMENT CORP.](https://support.nysba.org/attachments/token/IC0wkjtvvpbslRI5FmvzN5eV7/?name=voicemail+917-843-3456.mp3)

<br><br>
### THREATENING AND IMPEDING A FEDERAL INVESTIGATION OF BANK AND SECURITIES FRAUD, AND SLOWING THE RELEASE OF INFORMATION BY UNLAWFUL RESTRAINT, WILLFULLY AND KNOWINGLY IS NOT SOMETHING THAT IS EXEMPT FOR FEDERAL AGENTS AND NON-FEDERAL PERSONS.
[VOICEMAIL FROM PAUL REGAN, GENERAL COUNSELOR OF MANHATTAN SKYLINE MANAGEMENT CORP.](https://support.nysba.org/attachments/token/IC0wkjtvvpbslRI5FmvzN5eV7/?name=voicemail+917-843-3456.mp3)
<br><br>
### BANK INVESTIGATION
[VOICEMAIL FROM THEIR FRAUD DEPT. IN RESPONSE TO RECEIPT OF THE INFORMATION BY MR. KILKENNY](https://support.nysba.org/attachments/token/Sr0PKDdRavjlpFkIt7jc95QLq/?name=voicemail-218-CHASE+BANK.m4a)
<br><br>
[VOICEMAIL:: FROM THE BANK FRAUD DEPT. AT CHASE BANK](https://support.nysba.org/attachments/token/YNvrvCEnT6nrcydcPwB6lBXnO/?name=voicemail-215-CHASE+BANK.m4a)
<br><br>
[VOICEMAIL:: FROM JP MORGAN CHASE-FRAUD INVESTIGATIONS DEPARTMENT](https://support.nysba.org/attachments/token/1vZon2Sk7PB6esmpj3zVHUJja/?name=voicemail-222-JPM-CHASE.m4a)
<br><br>
[VOICEMAIL:: FROM CHASE BANK-FRAUD INVESTIGATIONS DEPARTMENT](https://support.nysba.org/attachments/token/OjDtdOSzaoQEpaoYABSwvHPXV/?name=voicemail-218-CHASE+BANK.m4a)

### SECURITIES FRAUD INVESTIGATION
[VOICEMAIL FROM THE SECURITIES REGULATORS](https://support.nysba.org/attachments/token/6tdqvD6K1AyrccbjgJ2MBK7GT/?name=voicemail-214-Finra.m4a)
<br><br>
[VOICEMAIL FROM THE SECURITIES REGULATORS](https://support.nysba.org/attachments/token/4BDa9lAjkbEe66TEBUZaTZYlR/?name=voicemail-217-FINRA+2.m4a)

![image](https://user-images.githubusercontent.com/108204659/177884161-999f6aed-886b-4490-9968-99bbd76ee5d5.png)

#### THIS PAGE IS BEING MONITORED BY THE DEPT. OF JUSTICE
#### AS WELL AS SECURITIES & BANK REGULATORS AS WELL.

![image](https://user-images.githubusercontent.com/108204659/177884550-5fac5c64-ab6d-483e-af6d-a8242ae018ee.png)

USC 18 TITLE 18- SECTION 1512 - PREVENTING COMMUNICATION TO A LAW ENFORCEMENT OFFICER OR JUDGE.txt
> https://support.nysba.org/attachments/token/sWoZTvp3jCzQBDpiHj8pRGrhV/?name=NOTICE+TO+SECURITIES+AND+EXCHANGE+-+NOVEMBER+13TH+2021.png

USC 18.1512 - Tampering with a witness, victim, or an informant
(a)
(1)Whoever kills or attempts to kill another person, with intent to—<br>
(A)prevent the attendance or testimony of any person in an official proceeding;<br>
(B)prevent the production of a record, document, or other object, in an official proceeding; or<br>
(C)prevent the communication by any person to a law enforcement officer or judge of the United States of information <br>

relating to the commission or possible commission of a Federal offense or a violation of conditions of probation, parole, or release pending judicial proceedings;<br>
shall be punished as provided in paragraph (3).
(2)Whoever uses physical force or the threat of physical force against any person, or attempts to do so, with intent to—
(A)influence, delay, or prevent the testimony of any person in an official proceeding;
(B)cause or induce any person to—
(i)withhold testimony, or withhold a record, document, or other object, from an official proceeding;
(ii)alter, destroy, mutilate, or conceal an object with intent to impair the integrity or availability of the object for

use in an official proceeding;
(iii)evade legal process summoning that person to appear as a witness, or to produce a record, document, or other object,

in an official proceeding; or
(iv)be absent from an official proceeding to which that person has been summoned by legal process; or
(C)hinder, delay, or prevent the communication to a law enforcement officer or judge of the United States of information  relating to the commission or possible commission of a Federal offense or a violation of conditions of probation, supervised release, parole, or release pending judicial proceedings; shall be punished as provided in paragraph (3).
(3)The punishment for an offense under this subsection is—<br>
(A)in the case of a killing, the punishment provided in sections 1111 and 1112;<br>
(B)in the case of—<br>
(i)an attempt to murder; or<br>
<br>
<br>
<br>
(ii)the use or attempted use of physical force against any person;
imprisonment for not more than 30 years; and
(C)in the case of the threat of use of physical force against any person, imprisonment for not more than 20 years.
(b)Whoever knowingly uses intimidation, threatens, or corruptly persuades another person, or attempts to do so, or engages in misleading conduct toward another person, with intent to—<br>
(1)influence, delay, or prevent the testimony of any person in an official proceeding;<br>
(2)cause or induce any person to—<br>
(A)withhold testimony, or withhold a record, document, or other object, from an official proceeding;<br>
(B)alter, destroy, mutilate, or conceal an object with intent to impair the object’s integrity or availability for use in an official proceeding;<br>
(C)evade legal process summoning that person to appear as a witness, or to produce a record, document, or other object, in an official proceeding; or<br>
(D)be absent from an official proceeding to which such person has been summoned by legal process; or<br>
(3)hinder, delay, or prevent the communication to a law enforcement officer or judge of the United States of information relating to the commission or possible commission of a Federal offense or a violation of conditions of probation?[1] supervised release,,[1] parole, or release pending judicial proceedings;
shall be fined under this title or imprisoned not more than 20 years, or both.
(c)Whoever corruptly—
(1)alters, destroys, mutilates, or conceals a record, document, or other object, or attempts to do so, with the intent to  impair the object’s integrity or availability for use in an official proceeding; or
(2)otherwise obstructs, influences, or impedes any official proceeding, or attempts to do so,
shall be fined under this title or imprisoned not more than 20 years, or both.
(d)Whoever intentionally harasses another person and thereby hinders, delays, prevents, or dissuades any person from—
(1)attending or testifying in an official proceeding;
(2)reporting to a law enforcement officer or judge of the United States the commission or possible commission of a Federal offense or a violation of conditions of probation?1 supervised release,,1 parole, or release pending judicial proceedings;
(3)arresting or seeking the arrest of another person in connection with a Federal offense; or
(4)causing a criminal prosecution, or a parole or probation revocation proceeding, to be sought or instituted, or assisting  in such prosecution or proceeding;
or attempts to do so, shall be fined under this title or imprisoned not more than 3 years, or both.
(e)In a prosecution for an offense under this section, it is an affirmative defense, as to which the defendant has the burden of proof by a preponderance of the evidence, that the conduct consisted solely of lawful conduct and that the defendant’s sole intention was to encourage, induce, or cause the other person to testify truthfully.
(f)For the purposes of this section—
(1)an official proceeding need not be pending or about to be instituted at the time of the offense; and
(2)the testimony, or the record, document, or other object need not be admissible in evidence or free of a claim of privilege.
(g)In a prosecution for an offense under this section, no state of mind need be proved with respect to the circumstance—
(1)that the official proceeding before a judge, court, magistrate judge, grand jury, or government agency is before a judge or court of the United States, a United States magistrate judge, a bankruptcy judge, a Federal grand jury, or a Federal

Government agency; or
(2)that the judge is a judge of the United States or that the law enforcement officer is an officer or employee of the

Federal Government or a person authorized to act for or on behalf of the Federal Government or serving the Federal
Government as an adviser or consultant.
(h)There is extraterritorial Federal jurisdiction over an offense under this section.
(i)A prosecution under this section or section 1503 may be brought in the district in which the official proceeding (whether or not pending or about to be instituted) was intended to be affected or in the district in which the conduct constituting the alleged offense occurred.
(j)If the offense under this section occurs in connection with a trial of a criminal case, the maximum term of imprisonment

which may be imposed for the offense shall be the higher of that otherwise provided by law or the maximum term that could have been imposed for any offense charged in such case.
(k)Whoever conspires to commit any offense under this section shall be subject to the same penalties as those prescribed for the offense the commission of which was the object of the conspiracy.

https://p19.zdusercontent.com/attachment/2434074/ONbQ6pgTKks3c7ZOi7ogr5Tmw?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..3SjoQz4kWEi0rs9s2TaiEQ.vqh9vZOliebGAA7r_IAD3893gc7TngmluyELeyK6hlmM24B-N0MOgudGHR1hynRx9KVZzI8Uvd1qs3AOfI-LlkTYh2vJJXFeP4a8f2u5bWyX29wD9KaAUqHgDIIItlYCuSnUh0SYnKBzOksD2nS3r33QdlhvO42yNCiFNYXSImfoXQWqRqOfka--aYE-EqRRc5IMcu-kHuJQcECfIwvtib0UzjoDJVW06oJxo4ky43kwZRRf8aNwFa1iotqh3LxmBd-zobcKVlx5UTPeO6K_9ZMS5K3Z8avS5jSyDpKDnRs.m7JFjFS10LZZ6MM9I2WaSw

ASSETS WERE MOVED FROM HSBC TO JP MORGAN WITH INTENT, WHILE THEY WATCHED ME 24/7 WITHOUT CONSENT
-- I HAVE BEEN MOVING FROM HOTEL TO HOTEL FOR THE LAST YEAR.

LOAN DOCKET 50074 - SECTION 1.4 -- INDEMNITY [ FILED DOCKET 312, NYSCEF 153974/2020 ]

https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ

[ MULTIPLE DWELLING LAW ]
" VIOLATION SHALL BE DEEMED TO EXIST IN THE RESPECTIVE PREMISES OF EACH RESIDENT IN THE OF THE MULTIPLE DWELLING "

https://p19.zdusercontent.com/attachment/2434074/8rbRQgVwJiGq3SGb6uIEsoGtK?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..K6J2ULKdIHHBx-zQOLpglg._AJoI_e3EmI8H7sGgLNVKy2C_EyHtNAb7FwNCJBqZNBx884x235cF6iVlAYSpGqcvX7yLFRtXBy-ChEW1nZkEqgV4f-V-Fg5OjnAsqYxLF-Pe2xBftkhkIGUDxgv5D8dOV3aHHVIK47WttG2VqVAXI5JBwti-hPF75wl-F6fDOh12qW2wX9Rwgw_ImJ3IPuGbEi52AzKc4Ups4H6yQ3-K06wPhZJjEb9t7pBAIqDP6VTZJQm784MYXs1EuVKqKv45lri7frMeZ2rWknN3zTi84zulFTdO0JLzPhyyviKUcA.YVZRL6uopA2xoxo5Z0g_0g

https://p19.zdusercontent.com/attachment/2434074/uwSPB9MeN0sX9yCIpaJ5LMB5q?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..oLI-sr6rVXQadNEVBJWSEA.Ngi9SXK3B5PgxbdPgf3ckSMOMao5Iz4d2z4Ps7aSvQtRKDKoU0fM_AqBz-wpDUmxSwY6iDwuFmsOmCxfr39Cz0P5S3QZNw1wsEQNpaXXlmy7nTtBmzU6ZYCO4ltyeq2fNKE7yonX7zb4E2JgzP2nxS3bPvU38izJxSw_2PWelHgOfvwQRT54rddQKiU_BDzjpcivfrBE2qGrR9n0xOB9QMt9BIHqwObdFUJQ8PVAkkLqguC8UAO5IJVXKJGeqCOfvIWcLS15RdtiLZey-GAmyAithpHb5a8o2CUIfLHAgCQ._K2fJ4EXrRbSo9Lqvy7E0g

https://p19.zdusercontent.com/attachment/2434074/AYudhpqVy5YzILECrrdqtYsDy?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..nOxmXbOvQZhADrGwCKLmRw.WEw5YfrAtg8unWagIHaxV9saUh6qWBNn-SADb1r3UxoBl61YY2fZsf68u2xhPCbmlG_QNl772EFppalHUuwCqQGTlMWqUJB2we3mkr95OV4jyIdRuXS4A-xm1jsvqpHXc76YJq3l1Li5_lymyzwI7uryDFHU5wHohAjRY6c1N0LeB6SxBwr_gmmBJ24aLcCD3C8iRgVG3HPhVzEsMM8Zp6vOWsdd0P-lcnGEsTVzb45weGg3IzQaIujIr54lviBQyZ5UWAgqVpw-JJQpdjBaehkhQg3Xh6Tfdiz4AkXa7xU.jXgsCJZx6rRTEQxRRHVkjw

https://p19.zdusercontent.com/attachment/2434074/uXmPQ38BhOoS81BORcN189epx?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..n4U1r1-tCk7t8cNgh9l6qA.02kR4RvYtLmbEC2P_3GfDG-tUSVdn6pgvny8OS0l_ZMOHL2jcezbnENLMSFh_CNstpOmDaqfoGMr8FWmisP6slmqPzi2U2ZKN2kAFFusE2mGYWB5jNNEnpdC-bd-Ow3WyYU3vflrPTD9WeUhEOdqoxc5PeCVxR6sjcUmA66NxwCHVWLYKygvrIEdyTkzBbnR61Hkh6CulGiTVBvJPk5NHXDo1d_TaOZqKHDtlbRxCRpleIwObZne4tRdIfDe5IE0lSjgjQkgph5OSMNiC9_2QEC-FoaClgJU0OdL36vrzMw.R88r1lKgxCZfE7W9bu9aug

https://p19.zdusercontent.com/attachment/2434074/M2hlv45SVnHpSrWTNDuNYRmxl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..S7yNlZ0mN5HiQiGGBLM73A.25SArygzhrF8LF4nA0IfEmdMPSZXt4bFllgiUVO8ZFOY7khexBtnjk9_jeNDukOcRIIsPR6VjT-2oQuMkRQbkqEDUhLJcTzFajpOf66EQKMTJZyR0NxOVPQm6rgjAqOubENq-9RT2NFenseWU25b8soJfqUJopB7sG0c1LJP-QQIk8H76vyFYA6UVm6sofzoSG9dHSTL3RUZTDEia0xUnnj66XturYId3uNRusYChWgtCE0K6CpWR3_Dvav291hEvMM8Ie7mQ6cSH8DCKXhymf6cFTNGOIF6gLfcuiyis-w.FYY9DAufaZkkghSdyGptJA

https://p19.zdusercontent.com/attachment/2434074/mlWG3uUj3n19hbg5MKEXJUFgp?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..TOGbWTBvbrYpIlmg9T0-Cw.hHOxQ2gpUui30mCRbddQnHEZn_Zt9JKYVG8hCCyIuhqpPXjGAk32GdJGmSNcuTV2npbYcQSOx1VGXUjKYtQtxuNbdhJCH_OV0HUmks8G4i35Q67sLhSMp6Dw-ShyhgU91yyngJV1qzVX8J5FzAJg3x0JtFx9hyFYRTaDXOrszE1gDIajfrbaSkilm4ATWLYp5ert99e1IlPDf5o98g1bSgVZGLt5gSEKVH9h4ymCC36YGj170kviC-Dc28FARWz2EXSvoVGByxkYAdfe8fVfO70FE95g3J7EvCWslr3dqGw.sxuBmVikIEuhtXsDBYiSmA

https://p19.zdusercontent.com/attachment/2434074/8rbRQgVwJiGq3SGb6uIEsoGtK?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..K6J2ULKdIHHBx-zQOLpglg._AJoI_e3EmI8H7sGgLNVKy2C_EyHtNAb7FwNCJBqZNBx884x235cF6iVlAYSpGqcvX7yLFRtXBy-ChEW1nZkEqgV4f-V-Fg5OjnAsqYxLF-Pe2xBftkhkIGUDxgv5D8dOV3aHHVIK47WttG2VqVAXI5JBwti-hPF75wl-F6fDOh12qW2wX9Rwgw_ImJ3IPuGbEi52AzKc4Ups4H6yQ3-K06wPhZJjEb9t7pBAIqDP6VTZJQm784MYXs1EuVKqKv45lri7frMeZ2rWknN3zTi84zulFTdO0JLzPhyyviKUcA.YVZRL6uopA2xoxo5Z0g_0g

https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ

https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ

https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ

https://p19.zdusercontent.com/attachment/2434074/MJ5xEG1bkHzqj0rY1zESVUgQb?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..t44VVxJ2EqeSYiPGTggD2Q.mr-QvRE4hq65-igubtudoe_PB8Os6IqLmx8cnfe18MSOaoW38_T7woQNJPwA8Gpig0Dx9DeaKztNvggaeBjaHC4eGYEQ-Y6K-frhikrMvn0yWgYLJjNkIoN5uy5S61EOqy9hJFwhHj2N0jYnBLAmzUQgASbBn_AIeMGMW9rU1AAUaLjKiJU2d_Y03zeQy8GTpoQidLKh7Ym88uG4ylclisDqKmC9HnIBXW1_t5AkBiU9yXgtmmlKu0TKXrPfev8Xe9z9p2W-nvgQRlR737tGbi-If8uDFjTKU2_Q0rvh5-Q.bXIbpP9_XcrY90OUJjK8Yg

PLAINTIFF ASSIGNED LEASES AND RENTS ON MAY 15TH TO STATE FARM LIFE INSURANCE COMPANY - INCLUDING THEIR TAX RISKS AS IMPLIED
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
EXHIBIT(S)  - AC0  (Motion #001)
ACRIS Detailed Document Information (2019000021408)2019010800475001
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ze6a1KA9akRV9TGfXXJT/g==
EXHIBIT(S)  - AC1  (Motion #001)
ACRIS Detailed Document Information (2020000155422)2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=bVk8sIt7n3kGwHqebPg0fw==
EXHIBIT(S)  - AC2  (Motion #001)
ACRIS Detailed Document Information (2020000155421)2020052000291002
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=wTG2YD2PqXuxmoKqFiESrw==
EXHIBIT(S)  - AC3  (Motion #001)
ACRIS Detailed Document Information (2020000155422)2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==
EXHIBIT(S)  - AC4  (Motion #001)
ACRIS Detailed Document Information (2020000155423)2020052000291004
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=/yhElCiKJ0BGv2DF/MOn4g==
EXHIBIT(S)  - ACR  (Motion #002)
ACRIS.NYC.GOV >> ASSIGNMENT OF LEASE AND RENTS ON FILED ON MAY 26TH
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==

--- THAT IS UNLAWFUL INCOME
https://support.nysba.org/attachments/token/ONbQ6pgTKks3c7ZOi7ogr5Tmw/?name=image0.jpeg

>> THESE IN THE TO:  ARE THE LINES OF COMMUNICATIONS THEY DISCLOSED.
https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==

18 U.S. Code § 1512 - Tampering with a witness, victim, or an informant<br>
![image](https://user-images.githubusercontent.com/108204659/177089989-edc8dc77-e0f4-4d92-85f0-d9782ece4035.png)

I PROVIDED THEM THIS INFORMATION

*** THAT INFORMATION YOU NEED TO VERIFY STARTS HERE:
*** Lewisohn Hall, 2970 Broadway, New York, NY 10027, United States of America
GPS (40.8084317, -73.9631634)

WHICH IS WHY I AM HERE.
-- THEY ARE PEEPING TOMS, AID AND ABET TO THOSE FELONIES COMMITTED BY

1.    THE ZUCKER ENTERPRISES LLC
2.    SULLIVAN PROPERTIES LLC.

3.    SULLIVAN GP LLC
4.    SULLIVAN PROPERTIES LP
5.    MANHATTAN SKYLINE MANAGEMENT CORP.
6.    STATE FARM LIFE INSURANCE COMPANY
7.    STATE FARM REALTY MORTGAGE LLC.
        PER SHARI'S LETTER WAS REQUESTED "IS OBSTRUCTION OF JUSTICE REQUESTED" NOT TO CONTACT ANOTHER ENTITY TO FURTHER MISLEAD REGULATORS...

8.    STATE FARM ASSURANCES FUNDS TRUST, CIK FILER 93715, RANDOMLY ELECTED TO SELF-IMPLODE
9.    ASSURANCES FUNDS TRUST, PRESENTLY OPERATES WITH THE SAME DIRECTORS UNDER CIK FILER 1516523

INDIVIDIVUALS OF INTEREST FROM NYSCEF 153974/2020 - OBTAINED A LOAN FOR $6 MILLION DOLLARS WHICH SATIFY THE FOLLOWING VIOLATIONS:
    USC TITLE 18.225, 18.21  (USING FALSE AND UNLAWFUL RENT ROLLS FILED WITH THE THE NY DEPT OF FINANCE)
    USC TITLE 18.4, 18.3, 18.2 (WILFULLY KNEW AND CONTINUED THOSE FINANCIAL CRIMES)

    1.    LAURIE ZUCKER        DIRECTOR
                    EMAIL:    LZUCKER@MSKYLINE.COM

    2.    SHARI LASKOWITZ        ATTORNEY
                    EMAIL:    SLASKOWITZ@INGRAMLLP.COM
                    TEL:     347-880-1899

    3.    PAUL REGAN        ATTORNEY
                    MANHATTAN SKYLINE MANAGEMENT CORP.
                    LEGAL@MSKYLINE.COM
                    TEL:    917-843-3456

    4.    ASHLEY HUMPHRIES  ATTORNEY
                    WILSON ELSER LAW FIRM
                    LEGAL@MSKYLINE.COM
                    TEL:    917-843-3456
    5.    STEVE O'CONNELL, COUNSELOR TO LAURIE ZUCKER AND WILLIAM MCKENZIE
                EMAIL: SGO2107@COLUMBIA.EDU, LZUCKER@MSKYLINE.COM, WMCKENZIE@NYCOURTS.GOV, LEGAL@MSKYLINE.COM
    6.    WILLIAM MCKENZIE, CLERK IN NYSCEF MATTER 153974/2020
                EMAIL: WMCKENZI@NYCOURTS.GOV

                OBSTRUTED JUSTICE WHILE AIDING AND ABETTING TO IMPEDING A FEDERAL SECURITIES INVESTIGATION,  AS SEEN IN THE COMMUNICATION BELOW ON DECEMBER 22ND, 2021
                - SEE ALSO: STOCK PRICE OF CIK FILER, UNDER TICKER STFGX ON DECEMBER 21, 2021 - LOST COLLECTIVELY AS FOUR TICKERS NEARLY ONE-BILLION DOLLARS IN A DAY AND NO-PUBLIC DISCLOSURE.
                - INFORMATION SHARED BY AND BETWEEN THOSE INDIVIDUALS.

    A.    HALE DINCER         ACCESSORY
                    - COMMUNICATIONS WITH SHARI LASKOWITZ, ET. AL.
                            -AND DURING THE PROCEEDINGS IN NYSCEF 153974/2020
                            - AND AFTER WHILE I MOVE EVERY 4 DAYS SO THAT I AM MOST EFFECTIVE                             TO PROVIDE INFORMATION TO THE FEDERAL REGULATORS
                            ABOUT AN ONGOING BANK AND SECURITIES FRAUD INVESTIGATION.

                            TO AVOID BEING IMPLICATED IN THE FELONIES COMMITTED
                            IN NYSCEF 153974/2020 WAS AT ALL TIMES AWARE.

                    EMAIL:    <HIDINCER@AOL.COM>
                    TEL:        +15168841083@tmomail.net

    B.    DAPHNE DINCER        ACCESSORY
                    - SEE ALSO COMMUNICATIONS WITH SHARI LASKOWITZ, HALE DINCER, ET. AL
                    EMAIL:        <DAPHNE.DINCER@GMAIL.COM>
                    TEL:        +15163224896@tmomail.net

    C.    ANNE BRANDON, ALAMEDA    ACCESSORY
                    EMAIL 1:    <anne@thehighlandpartners.com>
                    EMAIL 2:    <ANNE.D.BRANDON@gmail.com>
\

<br>[153974_2020_Sullivan_Properties_L_P_v_Baris_Dincer_EXHIBIT_S__373 - MY VIDEOS WERE HOSTED ON THE INTERNET without consent as well.](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/files/9065071/153974_2020_Sullivan_Properties_L_P_v_Baris_Dincer_EXHIBIT_S__373.-.MY.VIDEOS.WERE.HOSTED.ON.THE.INTERNET.pdf)

##### PLAINTIFF ASSIGNED LEASES AND RENTS ON MAY 15TH TO STATE FARM LIFE INSURANCE COMPANY TO PROTECT THEIR INVESTMENT - A SHORT TERM INVESTMENT WITH 30-YEAR TERMS.

#### THIS PAGE IS BEING MONITORED BY SEVERAL DEPARTMENTS AS PART OF A FEDERAL BANK AND SECURITIES FRAUD INVESTIGATION.
### NOTWITHSTANDING THE US. DEPT OF JUSTICE.

>> 6.24.2020 email - ASHLEY.HUMPHRIES@WILSONELSER.COM

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[ff3de32530...](https://github.com/ammarfaizi2/linux-fork/commit/ff3de32530e1cb57328c940221894d08efbc315d)
#### Sunday 2022-08-14 06:26:05 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [BSCPGROUPHOLDINGSLLC/REPO2](https://github.com/BSCPGROUPHOLDINGSLLC/REPO2)@[38855375f2...](https://github.com/BSCPGROUPHOLDINGSLLC/REPO2/commit/38855375f2c666e64bb759088ac23016de651333)
#### Sunday 2022-08-14 07:10:13 by 1212-5858

CIK FILER 93715 INTO CIK FILER 1516523 # MAKESMALLBIGGER ^ 1 REFERENCE <br> https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

CIK FILER 93715 INTO CIK FILER 1516523
# MAKESMALLBIGGER
^ 1 REFERENCE <br>
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

During the two-week trial, Judge Denise L. Cote closed the courtroom to the public several times to protect Goldman’s proprietary source code. Yet several details emerged about the firm’s high-frequency trading business, including that the unit accounted for about $300 million in revenue last year, less than 1 percent of Goldman’s total revenue of $45 billion.

On the evening of July 3, 2009, six agents from the Federal Bureau of Investigation met Mr. Aleynikov as he landed at Newark International airport and arrested him.

Mr. Aleynikov remains free on bail but because he holds dual United States and Russian citizenship, the judge placed him under home confinement and electronic monitoring until his sentencing, which is set for March 18.

A version of this article appears in print on Dec. 11, 2010, Section B, Page 1 of the New York edition with the headline: Wall St. Programmer Guilty of Code Theft.

 United States Attorney Southern District of New York

 Manhattan U.S. Attorney PREET BHARARA said: "Protecting the proprietary information of America’s companies is critically important. Today’s sentence sends a clear message that professionals like Sergey Aleynikov who abuse their positions of trust to steal confidential business information from their employers will be prosecuted and punished."

Under USC 18.225.each person:

'...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main
https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed
https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker

FOR INVASION OF PRIVACY AS WELL WAS UNCONSENTED AS ANNEXED "CEASE AND DESIST" NYSCEF 153974/2020

THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER THE AUSPICE OF THE OCC.TREAS.GOV AS OF JUNE 29TH, 2022

AUGUST 8TH, 2022

To whom this may concern,

    THE INFORMATION CONTAINED HEREIN IS CLEARLY THE OBJECCT OF ATTRACTION BY AND BETWEEN SEVERAL DEPARTMENT OF THE USDOJ WHO ARE IN FACT INVESTIGATING THE INDIVIDUALS AND PRINCIPLES OF THOSE ENTITIES WHO ARE RESPONSIBLE FOR A LAUNDRY LIST AS ENTITIES AND PERSONS WHO LED THEMSELVES INTO A COMBINE OF VIOLATIONS UNDER THE USC CODE, TAX CODE, AND HAVE ALSO ANNEXED AND FILED THEIR VIOLATION UNDER THE SECURITIES AND EXCHANGE ACT.

THE ZUCKERS AND THEIR ENTERPRISES, have avoided prosecution ,in fact prior to August 4th, 2022.
 - but thank you for checking in, DOCKET 309, nyscef 153974/2020, and in a high-fashion.

STATE FARM LIFE INSURANCE COMPANY

UNDER THE SCOPE OF THE PLAINTIFF, LITERALLY.
- subjugated AND AT THE COMPROMISE OF CIK FILER 93715, WHEREBY DIRECTORS FILED THEIR USC TITLE 18.215 PAYMENTS VOTED ON, KNOWN AND RECEIVED AS DIRECTORS OF CRD MEMBER 43036, AND ALSO " STATE FARM LIFE INSURANCE COMPANY " AND UNDER TICKERS OF FAMILY 4: STFGX.

https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

^ THAT REFERENCE.     IS THE REFERENCE OF GREATEST VALUE, COVERS THE SCOPE OF CONVERSATIONS
- USC TITLE 18.1952 VIOLATIONS, AND IN BOLD ***** BELOW, ET. AL.

*****

[ USC Title 18.225, USC Title 18.215, USC Title 18.21, USC Title 18.2 ]

Each person as Participants in NYSCEF matter 153974/2020

    '...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker

*****

THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER

		THE AUSPICE OF THE *@OCC.TREAS.GOV AS OF JUNE 29TH, 2022

 *** see also. Random $9000 audit by PWC for filer 93715,
				to file their KNOWN problems then by CIK filer 93715 and into CIK filer 1516523.'
				## STILL HOLDS THOSE PAPERS.. CAN'T TERMINATE UNTIL THE TAXES ARE " PAID IN FULL "
				## ALL SIX-PROPERTIES, AND A LETTER FROM ANY FEDERAL REGULATOR WOULD BE WHAT IS A "CALL"
				## FROM THE ISSUER OF ALL THAT MONEY IN ONE PAGE, AND IMPOSES THE SAME LEVERAGE STAKES AT ANY CUSTODIAN.

 /S/ BO DINCER.	).

	MAC. 646-256-3609
	TMO. 917-378-3467

📫 https://github.com/BSCPGROUPHOLDINGSLLC/2021-DUCKER-ZUCKER/pull/1

CIK FILER 93715 ITNO CIK FILER 1516523
# MAKESMALLBIGGER
^ 1 REFERENCE <br>
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

$$$$$ leb@fbi.gov

https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

UNDER THE SCOPE OF THE PLAINTIFF, LITERALLY.
- subjugated the decision(s) of STATE FARM LIFE INSURANCE BY IMPEDING A TIMELY RELEASE OF INFORMATION FILED IN NYSCEF 153974/2020
- AND AT THE COMPROMISE OF CIK FILER 93715.
^ WHEREBY DIRECTORS FILED THEIR USC TITLE 18.215 PAYMENTS VOTED ON, KNOWN AND RECEIVED AS DIRECTORS OF CRD MEMBER 43036,
^ AND ALSO " STATE FARM LIFE INSURANCE COMPANY " AND UNDER TICKERS OF FAMILY 4: STFGX LOST THE GREATER OF 10% IN A SINGLE TRADING SESSION.

https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

^ THAT REFERENCE.     IS THE REFERENCE OF GREATEST VALUE, COVERS THE SCOPE OF CONVERSATIONS
- USC TITLE 18.1952 VIOLATIONS, AND IN BOLD ***** BELOW, ET. AL.

*****

[ USC Title 18.225, USC Title 18.215, USC Title 18.21, USC Title 18.2 ]

Each person as Participants in NYSCEF matter 153974/2020

    '...imprisoned for a term of not less than 10 years and which may be life."

# FEDERAL FILE FINDERS
^	UNDER THE PAPERWORK REDUCTION ACT OF 1995

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/find/MSGFILES

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/find/VIDEOTAPED-DISTRIBUTED

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/main

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/2020-11-20-FILER0000093715

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/REQUEST-TO-BAR

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/Assessments

### $9000.00 AUDIT WAS A "SURPRISE DISCOUNT" BY CHANCE PROVES THAT ' PWC ' KNEW ' SOMETHING WAS GOING ON '

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker

*****

THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER

		THE AUSPICE OF THE *@OCC.TREAS.GOV AS OF JUNE 29TH, 2022

 *** see also. Random $9000 audit by PWC for filer 93715,
				to file their KNOWN problems then by CIK filer 93715 and into CIK filer 1516523.'
				## STILL HOLDS THOSE PAPERS.. CAN'T TERMINATE UNTIL THE TAXES ARE " PAID IN FULL "
				## ALL SIX-PROPERTIES, AND A LETTER FROM ANY FEDERAL REGULATOR WOULD BE WHAT IS A "CALL"
				## FROM THE ISSUER OF ALL THAT MONEY IN ONE PAGE, AND IMPOSES THE SAME LEVERAGE STAKES AT ANY CUSTODIAN.

 /S/ BO DINCER.	).

	MAC. 646-256-3609
	TMO. 917-378-3467
The Financial Information eXchange (FIX) is an information and data protocol
mailbox BSCPGROUPHOLDINGSLLC/2021-DUCKER-ZUCKER#1

CIK FILER 93715 ITNO CIK FILER 1516523
# MAKESMALLBIGGER
^ 1 REFERENCE <br>
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

i am unfamiliar with any internet based spy tools, other than mobi-stealth, which was helpful in the past. other than that one, i don’t know about any other spy tools other than what is used by the federal government.

 In fact, SPAM only contains six ingredients! And the brand's website lists them all. They are: pork with ham meat added (that counts as one), salt, water, potato starch, sugar, and sodium nitrite.

FAX CONFIRM TO THE COURT MATTER NYSCEF 153974_2020 [USC 18 §21, USC 18 §225, USC 18 §2, USC 18 §1962]

---
## [Fl1pNatic/squidcraftbot](https://github.com/Fl1pNatic/squidcraftbot)@[2644aa9ff5...](https://github.com/Fl1pNatic/squidcraftbot/commit/2644aa9ff5d4011f572be4cede14039fa62f415a)
#### Sunday 2022-08-14 07:42:56 by Fl1pNatic

dear diary, its been 12 years since the bot last worked as intended, i have been trying to get the help embed to work for as long as i remember myself, but it just doesnt work. this cursed function never does what i want it to, and this fight has been going on for so long i dont even remember why we even made this bot in the first place, i just hope i can finally finish it

---
## [GoldenretriverYT/spaghetto](https://github.com/GoldenretriverYT/spaghetto)@[d7184085f1...](https://github.com/GoldenretriverYT/spaghetto/commit/d7184085f13b029d72b0c67ecc70057a86e000b4)
#### Sunday 2022-08-14 09:11:21 by GoldenretriverYT

holy fucking shit this dot node optimization is great

---
## [mrpsharp/just-the-docs](https://github.com/mrpsharp/just-the-docs)@[c2ec3d89c2...](https://github.com/mrpsharp/just-the-docs/commit/c2ec3d89c2aa4734c2c7f743a5d0c1c0be08ece0)
#### Sunday 2022-08-14 09:29:48 by Matt Wang

Update Stylelint to v14, extend SCSS plugins, remove primer-* configs, resolve issues (#821)

This is a catch-all PR that modernizes and updates our Stylelint config, and resolves all open issues. This is a pretty big change - so I want to update all of our related dependencies in lockstep.

In particular, this PR

- [x] updates stylelint to `v14`
- [x] adds in the standard stylelint config for SCSS (`stylelint-config-standard-scss`)
- [x] swaps out `stylelint-config-prettier` for `stylelint-config-prettier-scss`
- [x] ~~properly update `@primer`-related plugins:~~ completely remove `primer` from our configuration
- [x] autofix, manually resolve, or disable all newly-introduced lint errors; **I've avoided manually resolving errors that would be a behavioural change**
- [x] re-runs `npm run format`

See the "next steps" section on some extra thoughts on disabling errors.

(implicitly, I'm also using node 16/the new package-lock format).

### disabling rules and next steps

I've introduced several new disabled rules. Let me quickly explain what's going on; there are two categories of rules I've disabled:

1. rules that were temporary disables; they were frequent enough that I couldn't manually resolve them, but should be simple. **I plan on opening issues to re-enable each of these rules**, just after this PR
    - `declaration-block-no-redundant-longhand-properties`: this is just tedious and error-prone
    - `no-descending-specificity`: this one is tricky since it could have impacts on the cascade (though that seems unlikely)
    - `scss/no-global-function-names`: I think we need to [import map and then use `map.get`](https://stackoverflow.com/questions/64210390/sass-map-get-doesnt-work-map-get-does-what-gives), but I'll leave this as out of scope for now
2. rules that are long-term disables; due to the SASS-based nature of our theme, I think we'll keep these in limbo
    - `alpha-value-notation` causes problems with SASS using the `modern` syntax - literals like `50%` are not properly interpolated, and they cause formatting issues on the site
    - `color-function-notation` also causes problems with SASS, but in this case the `modern` syntax breaks SASS compilation; we're not alone (see this [SO post](https://stackoverflow.com/questions/71805735/error-function-rgb-is-missing-argument-green-in-sass)). 

In addition, we have many inline `stylelint-disable` comments. I'd open a separate issue to audit them, especially since I think some disables are unnecessary.

### on Primer 

**note: there hasn't been much other discussion, so I'm going to remove primer's stylelint config.**

If I do add `@primer/stylelint-config`, I get *a ton* of errors about now using `@primer`'s in-built SCSS variables. I imagine that we probably won't want to use these presets (though I could be wrong). In that case, I think we could either:

1. disable all of those rules
4. not use `@primer/stylelint-config`, since we're not actually using primer, and shift back to the standard SCSS config provided by Stylelint

~~Any thoughts here? I also don't have the original context as to why we do use the primer rules, perhaps @pmarsceill can chime in?~~

---
## [sthagen/git-git](https://github.com/sthagen/git-git)@[5beca49a0b...](https://github.com/sthagen/git-git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Sunday 2022-08-14 10:05:34 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [jupyterkat/Yogstation](https://github.com/jupyterkat/Yogstation)@[f4c7571fc3...](https://github.com/jupyterkat/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Sunday 2022-08-14 10:59:28 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [PCamille/mc-stable_anvil_cost](https://github.com/PCamille/mc-stable_anvil_cost)@[795583320e...](https://github.com/PCamille/mc-stable_anvil_cost/commit/795583320e6a47c67e4f437a0352b49785c66a44)
#### Sunday 2022-08-14 11:25:29 by Camille Priou

fix crash on server cause I'm stupid and I kinda hate myself

---
## [Stardusten/Swift-GTD](https://github.com/Stardusten/Swift-GTD)@[2bf1974e46...](https://github.com/Stardusten/Swift-GTD/commit/2bf1974e46f810a4ec9c8256da4c9e5ffc01362f)
#### Sunday 2022-08-14 12:58:39 by hannesfrank

Add repoURL to manifest.json

The plugin looks amazing so far! 

Do you feel ready to put into the marketplace?

The only requests I'd have is to

1. Figure out a cool logo. 😉 We could delay this. Andres is working on some plugin branding one can use as a template.
2. Split the Readme by language. I looks like it interleaves one english and one chinese sentence, right? Would a dedicated chinese readme lik here: https://github.com/tiimgreen/github-cheat-sheet be easier to read for people of both languages? On the plugin details page in the marketplace we could make tabs for each language, or have people click on the translation link for now. If you want I can help you with the copy&pasting.

Looking forward to improve my task management :)

---
## [petre-symfony/firebase-pinia-vite-vue3-aug-2022](https://github.com/petre-symfony/firebase-pinia-vite-vue3-aug-2022)@[4bd24f628a...](https://github.com/petre-symfony/firebase-pinia-vite-vue3-aug-2022/commit/4bd24f628a4e7089e4bfc0b8de2b30a26d7676e7)
#### Sunday 2022-08-14 13:57:58 by petrero

13.180(1) Uploading files - Prevent the user to leave the manage page when editing a song without to confirm this.

  Tell me if this has ever happened to you. You're filling out a form and suddenly you accidentally hit the back button or you swipe in the wrong direction. Your device may register this as wanted to navigate away from the page. When you come back to the form it is entirely empty. You will have to fill it out again. This type of accident is more common than you think. It's a very annoying thing to experience. You can ask the user, when that happened, if they are really sure they want to navigate to a different page.
  We can implement a feature similar with navigation guards. Navigation guards allow us to perform an action before the user navigates to the next page.
  onBeforeRouteLeave guard gives us the opportunity to stop the router from leaving the page if the user is filling out a form. The first thing we need to do is detect if a user is filling out a form. There isn't a point in stopping the user from navigating away from the page if they haven't make changes to their songs. We create a data property for keeping track of any edits to the songs. It that is true we should attempt to stop the user from navigating away. This property is updated whenever any of the values change in any of the songs. The data is stored in the Manage component but the fields are stored in the CompositionItem component. We create a function for modifying this data in the Manage component. This function we passed down in the CompositionItem component. It will be able to call this function whenever the input changes. input event is fired whenever the value for the field changes. This will let us become aware of unsaved changes. If the user saved their changes we turn the unsaved flag off.

---
## [SmurfsINU/0x75afa9915b2210cd6329e820af0365e932bc1dd5](https://github.com/SmurfsINU/0x75afa9915b2210cd6329e820af0365e932bc1dd5)@[6cb8f3feea...](https://github.com/SmurfsINU/0x75afa9915b2210cd6329e820af0365e932bc1dd5/commit/6cb8f3feea9e5e877bcc4ff6928fb233c161e9fa)
#### Sunday 2022-08-14 14:47:44 by SmurfsINU

Add files via upload

Our project is 7 days and 17k holders and we have reached a weekly million dollar daily volume. We started trending regularly on Twitter.
Our community users mostly use TrustWallet and requested to update SmurfsINU information on TrustWallet. We have to do the same with them. This is why we apply. Every detail about our project is available on our website. With Regards and Love.
Other Details about SmurfsINU:
Our project was launched on Aug-07-2022. The total supply is 1,000,000,000,000,000 SMURF tokens.
SmurfsINU has been specially designed at every stage to be the safest and most loved project. As a result of in-team meetings and social research, it was decided that the tax fee would be 0%. Since the tax fee is 0%, large wallets are not reserved under the name of marketing, team, partnership. Only a 2.5% wallet is reserved for SmurfsINU to be listed on major exchanges. 
With the decision of our finance team, SMURF token will be sold with BUSD parity and liquidity locked along a year.
Since we agreed with an exchange before the launch, you will probably see while you are reviewing the project, 3% supply is reserved for Kucoin and the listing pool has been created in Kucoin. The remaining 97% supply is added to the liquidity. 
The SmurfsINU project will be financed by NFT sales, stakes and sponsorships in the SmurfsVerse universe. Our finance team secured special sponsorship deals specifically for the FIFA World Cup Qatar 2022. One of our biggest goals is to be the mascot of the tournament and to sign a partnership with a big world star.
We can say tokenomics: %97 Supply Add to LP + %3 supply reserved for a major exchange = %100 SMURF




TeamMembers:
Creator OF SmurfsINU Moto MotohiroMatsuyama: Moto, who has been actively working as Talent Acquisition @ Amazon, took active roles in projects such as AxieInfinity and Pokemon Trading Card Game.
He has been playing an active role in the crypto world, especially in the GameFi field for a long time.
He regularly attends audio conferences on Twitter Space. Moto, who also shared candidly with MayeMusk, increased his popularity. Now he created SmurfsINU with all his talents.

Twitter: https://twitter.com/MotoMatsuyama
TG: https://t.me/MotoMatsuyama


Technology and Finance Director - NiallBuckley: Niall works as an advertising director at Mothership Strategies.He is known as Pythagoras in the crypto universe.
He has played an active role in projects such as SAFEMOON, EverRise, FEG on the BinanceSmartChain network.
He has close relationships with global gaming companies and stock markets. He said in his last interview that he will use all his experience and energy to maximize SmurfsINU.


Twitter: https://twitter.com/NiallBuckley19
TG: https://t.me/NiallBuckley19



Community and media consultant - HajimeTossa: Hajime Tossa has been in the crypto market for a long time.
He especially played an active role in making STEPN a big hit in the Asian market. He influenced large masses with his publications on social platforms.
In addition, he has been accepted to the Binance training team with his regular conferences around the world, and he continues this duty actively. He joined the team at Moto’s special request.
This is one of the biggest deals ever made for SmurfsINU to reach SHIBA levels.

Twitter: https://twitter.com/OthersideOwner
TG: https://t.me/BabyDogeWhalehere

---
## [Helwor/Zero-K](https://github.com/Helwor/Zero-K)@[5e2b1657be...](https://github.com/Helwor/Zero-K/commit/5e2b1657be4cd0d9d7975eb434cc40c9a350ee1b)
#### Sunday 2022-08-14 17:15:42 by Helwor

Big update, various improvements and fixes, slight rewrite

-Adapted my code to be compatible with the Zero-K version

-Rewrote slightly the code to be more concise and efficient

-Fixed: The Zero-K version is broken since an edit made Sep 2020 (!) when user start to change spacing, the rectangles would never disappear because newspacing variable was never falsified at the end of the  Update round.

-Fixed: the param for spTraceScreenRay was the opposite of what it should be

-Improvement: The widget now adapt to the wrong engine grid which is off and also sometimes misleading when it comes to place units on water

-Added: On this particular case, widget gives the possibility for the user to either follow the grid coherence, or show the reality of where the unit will actually be placed. In that case, an extra rect is drawn to see where the first placement will land.  By usage, it seems the latter is more interesting so I put it on by default.
(More details in the comments that could help fix the problem with the engine)

-Improvement: the option panel now stop resetting scroll anytime an option is changed, this fix could easily be implemented universally by changing WG.crude.OpenPath, all it have to do is remembering 'scrollPosY' of the last panel and apply it to the new.

-Added: an option  for the user to choose wether rects should spread straightforward (if user want to only have a basic glance of the separation with no simulation of placing on the ground) or follow the ground, as it was before. I'm undecided which is the best as default for new users.

-Added: an option to have different colors of rects for bad placements, this on default if follow ground is on default, it seems to be adding a plus mostly in this case.

-Changed Description that's been edited, it does not just memorize spacing. I understand that it need to be concise, but a description is meant also to say what it does. User won't be able to tell if that widget make the previsualization or add mouse wheel to spacing by reading its description.

-Changed back title of an option. The purpose of how they are written is to build a sentence obviously, to make it more straightforward and user friendly. This change broke that concept. When user, especially new user, dive into options they can be lost as I was, to understand what option do what, if the option is dependent of another, etc... that's the purpose of my system to make all that as clear as I can.

-Changed back some default for new user, I think having the shift+mousewheel is a must, it's faster and more convenient, especially when discovering the game. I would have been glad to have that when I started, (that's, by the way, why I rewrote this widget in the first place).
Also changed back previsualization, with only 2 rects and only when spacing change, and for 0.7 sec
It is, in my opinion, also much more convenient for a new user to be able to see in a quick glance how your placement will be separated without the need of start posing queue and THEN realize the spacing is not good. If non-new user get tired of it, they will be able to find the options to undo it.
Indeed, new user will not be anymore really a new user when he discovers previsualization, if it's not on by default.

-Few minor things:
  -preGame is now set by GameFrame and then GameFrame removes itself
  -MouseWheel gets added/removed whenever shift+wheel option is changed
  -I don't see any reason to change the name spaced_rects in spaced_rects_2. As far as I know, one can only want that for resetting his own option to default for testing  purpose. Reverted it since it didn't make sense.
  -Upped the max time before infinite for show value and show rects to 10 sec
  -Didn't reverted it but imho, changing 'p' to 'placement' made the code uselessly more cumbersome than it already is.
  -Changed 'if not placementCache[unitDefID] then'  to 'if not placeTable[unitDefID] then' as the code was intended to mean
  note about this: since the vast majority of building have same sizex and sizez, maybe it could be improved by checking if it's relevant to consider the off-facing in 
  before.
 -Estomped the double dots before option titles when they are active, to make them less present.
 -update placement on more relevant changement of facing
 -Made the options defaults in concordance with the widget defaults
 -And maybe some other stuff I forgot

Lots of change, so please, let me know what you think.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[db341a3287...](https://github.com/mrakgr/The-Spiral-Language/commit/db341a3287d0e486bbd0139cde55b858c6cf5c2c)
#### Sunday 2022-08-14 17:19:27 by Marko Grdinić

"9am. I need to take the lesson of this failure to heart. It is one thing to be good and to believe in yourself. But I never had a plan how to deal with the task being beyond my ability. In that case, rather than trying to figure out the algorithm by hand, my job would be to focus on the environment. Rather than trying to grasp the algorithm in the darkness, you set up the conditions so it comes to you on its own. I should have aimed for this from the start.

If I did, I would have recognized that I do not have the hardware for it yet.

When you have the hardware you can go directly to the solution, but if you don't you need to burn cycles to do proper science. Nature's evolution is nothing more than automated, blind science.

The reason I failed is because I wasn't a proper scientist.

9:05am. I should not be diving into Graphcore, and experimenting whether I can twist their hardware for my own ends. The company itself should give me some indication that the experiment could work.

That is the smart way of doing this for somebody in my position. Let Deepmind and OpenAI burn money on figuring it out. I should be a thief.

I do not need to strain myself at all. All I need to do is determine what the initial conditions should be.

9:10am. Things should get fun once I get the ability to evolve modules in parallel rather than just individual sequences.

9:15am. Enough ranting, let me have some fun and then I will write. Or at least, I will think about what to write.

9:55am. Had to do some chores. Let me finish the cyberpunk thread and I will start.

I think I know what my starting position is. For the Deepmind guys, since they have the resources, it is fine for them now. But my starting point would be the outroll of memristors. That is, the sale of a computation capable device with terrabytes of non-volatile memory.

The need for Spiral to program these devices will come when the conditions are set.

10:05am. Right now I am stuck in a box, but it is not like the box will never be opened. I need to be patient. Until I get my chance it is fine to accumulate money, fame or skills in my own way.

Since I am writing, I am definitely fame focused. Even if 100k people read my story, but never contribute to my Patreon I'll still have made connections as light as they are. I should be able to use the story to plug Spiral a few times at the very least.

> Bubblegum Crisis, Cyber City Oedo, Goku Midnight Eye, Black Magic, Megazone, Dominion Tank Police, A.D. Police, Battle Angel Alita, Parasite Dolls, Armitage III, Mardock Scramble,
> more OVA's than movies but thats just where most of the good cyberpunk stuff gets made

Found this in the cyberpunk thread.

I really liked Mardock Scramble as bad as it was, but I never watched any of the others. I'll keep this in mind.

10:20am. Let me start.

Either way, the only way I will win this is by playing god. Automating science is that kind of task.

Since I have the talent for it, why don't I mess with morality?

Let me get rid of the distractions. I could have started an hour ago and have had some quiet time, but the din in my mind would not let me. Now I am agitated for no reason. Whatever the case is, I need to figure out my true potential. While I could not make Skynet, it is not like anybody else in the world can do that either.

Now it becomes questionable? How good am I at programming? How good am I at art? How good am I at writing?

I know that drawing and painting is not my forte. Thanks to 9 months of effort I've just gotten to the point where I can make passable 3d while taking a long time to do it. I think I am good at programming, but there is huge uncertainty how well I'd do in a corpo environment. As for writing, the 6.5 years of programming changed my brain areas. When I was doing sculpting I felt like programming is similar to it, but writing is much more similar to programming than anything else.

I am pretty much using the same process and mental areas. I have to be passionate, but I can't rely on a once in a lifetime burst of inspiration to carry me like in 2014.

I understand one thing, I am taking the notion that the best way to make money is to start a religion very seriously this time around. I want my readers to see a whole new world.

10:25am. I need to see whether the discipline I've developed over the last decade will give me any benefit during this writing trip.

If it does, and I get some income then great. I'll become a writer, and aim to use AI developments to boost my work. If not, it is corpo drone life for me. I'll go with the plan of getting a lowly paid job and work my way up from there. Starting at 100-200k senior jobs like those on AngelList was too much. Next time I will play it properly.

10:30am. But I need to exhaust this possibility. I want Simulacrum itself to nurture me. For the sake of the world I want to create, I want this desire to give me a concrete benefit in the present. I should either be doing programming for the sake of ML research, or nurturing my vision.

It is too good to waste my brain on some useless programming job.

So let me life up to it. Nobody can just snap his fingers and be successful. I can't tell other people to give me money or like me. But what I can do is produce content.

So let me live my life the way I want to.

...

Now, let me think about the next scene. I sort of wanted the kid Euclid to get crushed and then turn into chad. But that is not going to happen due to saveloading. He can't get crushed, all he can do is get into a death match he cannot win even with saveloading and get tired of it.

10:35am. Yeah, if I think about it, it is not like saveloading makes you an absolute power. If you wanted to go on a killing spree, it would give you an advantage, but then the army would roll in and overwhelm you, essentially checkmating you.

There are two good points to make:

* Saveloading does not make you omnipotent.
* Saveloading will not allow you to take that power into the real world.

But also, the ability to save and reload in games is so vital to the gaming experience, and Simulacrum is all about the philosophy and the worldview of gaming. It is not a story where some kid get shunted into an universe and given cheats by god. Rather it is about the meta of the current reality.

Reminding the reader that he is in a game, but at the same time showing him what games could really be given a sufficiently powerful computer is what Simulacrum is about.

If I apply myself, I should be able to draw infinite inspiration from this.

10:40am. I have to grow up a bit here. Being an adult means working around your limitations rather than challenging them head on at every turn. I am going to try to stop ranting about my old path and getting agitated about it, and focus on my writing path. Remember how in Lain's Dream the guy just got a 100Tb neuromorphic device from Intel? An event like that being possible in the real world will be the signal for the Singularity to start. It can't be helped that people with superclusters are ahead of me.

10:50am. Actually I need to think about it more. I know how to deal with the next scene, but...

11:05am. Yeah, I am going to have to think about it. I know how to deal with the next scene, but I don't know how to deal with everything else.

1:30pm. I missed breakfast it seems. I am still thinking about it.

I have certain world building issues that I need to deal with. I roughly figure how the saveloading parts should go, but I am working through the implications of that.

As I am reasoning how the power scaling should work, I've realized that nanofog controlling like in the real world would not be a fit for a game such as this. Imagine, if one of the players tries editing another's brain like that? How should the game handle such interactions.

In the real world is it obvious when one player attacks another, but modifying microscopic particles is quite another. It is hard to understand what the rules should be.

Instead of active rules where a judge decides, I thought of making it more objective. Rather than punishing the thief, build a wall. So I thought of making use of invisible force fields. But that is also fraught with complcations.

So now the solution I am arriving at is the illusory world solution.

In the physical world, force rules. There could be games like that, but there the better nanofog controller rules, and the subgame rules don't really matter. It is hard to have a poker game, when the optimal strategy is to go across the table and beat the other guy up - stealthily, I mean.

1:40pm. The solution therefore is to get rid of all the physical aspects. Every character is a ghost. Everything is an illusion so the best illusionist should win.

...Let me do the chores. I'll resume the spiel after that.

1:50pm. I am back. It is really coming to me. If I was going with a physical simulation as the foundation, I'd really have to hack things together to make my vision work, but loosening up the game requirements would really make the aspects fit together.

1:50pm. I already said that Simulacrum uses a superintelligent agent to simulate scenarios. There is a lot of opportunity for training without making things physical.

1:55pm. Let me watch some pathfinder vids. I am interested in barbs, but for the sake of the story I'll look into illusionist wizards. They aren't that good in the game itself.

https://youtu.be/qHnCMR-1L2o?t=73
> Barb is 80% combat and 20% utility

Hmmm really? I thought that rage would push combat above 100%.

2pm. Hmm, I had no idea fighters get passive bonuses for weapon training.

https://www.youtube.com/watch?v=G8-Upj_R7kQ
Are Illusions Better than FIREBALL!? Yep...

This is an interesting waste of time.

https://youtu.be/_4JG0IwclAg
D&D 5e The Deadly Art of Illusion.

These aren't too big on examples.

3:45pm. https://youtu.be/IZbrcW4_7dg
Why You Should Be Afraid of the Deep Ethereal - D&D

Let me take a look at this and then I am going back to bed. DND illusions are not really what I had in mind, but I do not know anything better.

4:05pm. https://youtu.be/-iZHTXOPbJw
Why do Gods Fear Space in Dungeons and Dragons

Eh, let me also watch this. Right now, I really feel exhausted. I play Kingmaker till 12pm, and it feels like I get too little sleep.

4:25pm. https://youtu.be/48YkLFv8X3w
Dungeons and Dragons Lore : The Far Realm

Let me watch this as well.

4:45pm. Let me go to bed. Watching the vids is a waste of time.

Trying to get inspiration from other settings will not work for me here. Some deep personal thought as to how I want to do things will bring me to the truth. There is nothing out there like Simulacrum.

Right now I have to resolve the issue of how to make the charas life chips themselves. Right now I am thinking of doing a lich kind of thing with the life chips, but I am not sure how things fit. Let me step away for an hour so I can figure that out.

7:10pm. Done with lunch. Next is Lycoris. I am still thinking about it. I've resolved quite a bit of the issues, but I want to figure out what should happen after Euclid makes the next step, and overcomes the first adversary he couldn't using just saveloading. I think I have a decent amount of material, but not enough. I want to properly refine my vision. Maybe I'll spend the tomorrow in bed as well. After I decide what I want, I am going to get it all out.

I guess it is fine if I take a while to think about it. I've changed some things in my planning, so I am revising my thinking and making alternative scenes."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[23d8d596c5...](https://github.com/treckstar/yolo-octo-hipster/commit/23d8d596c537511410f9797622c70c66faca23b2)
#### Sunday 2022-08-14 17:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [15peaces/15-3athena](https://github.com/15peaces/15-3athena)@[aefe0e522a...](https://github.com/15peaces/15-3athena/commit/aefe0e522a1dcbb821f26a2f035acd121740b934)
#### Sunday 2022-08-14 18:49:34 by 15peaces

== Some fixes ==
=General:
*Added missing changelogs, sorry... ^^"

*Fixed the CZ_COMMAND_MER packet for 2018+ clients.
-The homunculus menu is now working fine again.

*Fixed an warning in clif_parse_cz_config function.
-Added pre-support for homunculus autofeed flag.
-Support for this feature might be added later.

== Missing changes of r342 ==
=General:
*Merged missing changes from 3ceam rev. 846

*This is the first part on the revisiting of the Kagerou/Oboro skills.
-Part 2 will come at a later date.

*Cleaned up and optomized some code.

=Skills
*Kagerou/Oboro
+Fixed a issue where none of the skill cast times were interruptable.

*KO_HAPPOKUNAI (Spray Kunai)
+Recoded the skill.
+Damage is now ranged physical. Basicly a stronger version of Throw Kunai.

*KO_MUCHANAGE (Over Throw)
+Recoded the skill.
+Damage is no longer reduced in GvG/BG areas.
+Damage is no longer reduced by half on enemy players.
+Success chance of hitting is now seprate for each enemy target.
+Damage is now divided between enemys detected in AoE.
-This means its divided based on the number of enemy's detected in the AoE
-and not by the number of enemys hit.

*KO_HUUMARANKA (Launch Huuma Shuriken)
+Damage no longer split between targets.

*KO_MAKIBISHI (Makibishi)
+Recoded the skill.
+Fixed a issue where it didn't follow the rules of AoE placement.
+No longer ignores elemental adjustments.
+No longer stacks on top of each other.
+Stun duration is now fixed and can't be reduced.
+Now places the proper number of makibishi depending on skill level used.

*KO_MEIKYOUSISUI (Clear Meditation)
+Recoded the skill.
+Skill now makes the caster sit when the status starts. If the caster stands up
-at will or gets forced to stand up, the status will end. This also prevent's
-the caster from being able to move or use any skills while active due to sitting.
+Now has a chance of making any attack completely miss the caster while active.
+Now removes a single debuff by random on use. The following can be removed....
-Poison / Curse / Silence / Blind / Fear / Burning / Frost / Crystalize.
+This behavior is official according to zone scans but a bug does exist on official
-where the skill use animation would stop the caster from sitting, allowing
-exploiting of skill uses. I coded it to prevent this issue from happening.

*KO_KYOUGAKU (Illusion - Shock)
+Recoded the skill.
+Now has a success chance reduceable by the target's INT.
+Duration is now reduceable by the target's INT.
+Now only usable in GvG and Battleground maps and on enemy players only.
+Will now fail if used on a target already affected by this skill.
+Affected target can no longer switch or unequip equips.

*KO_JYUSATSU (Illusion - Killing Curse)
+Now only usable on enemy players.
+Now reduces the affected target's current HP if the chance of curse is successful.

*KO_ZENKAI (Spread Seals)
+Can no longer be stacked on top of each other.
+Random status chance is now applied every second.
+Random status success chance is now 100%, but is reduceable by stats and equips.
+Durations of the random status's is now set to their original defaults.
+Friendly player's standing in the AoE will now get a WATK increase if the weapon
-element is the same as the AoE's element.

*KO_IZAYOI (16th Night)
+Updated the MATK increase formula.
+Corrected the animation handling.

*KG_KAGEHUMI (Shadow Hold)
+Corrected the animation handling.
+Fixed a issue where affected player's didn't stop moving.
+Affected targets will not beable to use the following skills for the duration...
-Hiding / Cloaking / Cloaking Exceed / Camouflage / Shadow Form / Dark Cloud
-Also blocks the use of any teleporting methods including fly/butterfly wings.

---
## [Shadow2ube/manga_dl](https://github.com/Shadow2ube/manga_dl)@[afde425bdc...](https://github.com/Shadow2ube/manga_dl/commit/afde425bdcacda125eca94bc0773a80e51b6844b)
#### Sunday 2022-08-14 19:59:58 by Christian

I think I hate myself
- made an HTTP request wrapper for curlpp which is in turn a wrapper for libcurl
- I reverse engineered selenium because I don't like using python, and yes, I enjoy mental anguish
- Now you can click on websites that are acquired with the `click` command in mdlx
- There's still a bunch to do

---
## [HielkeMaps/hielkemaps.github.io](https://github.com/HielkeMaps/hielkemaps.github.io)@[82a31a06f1...](https://github.com/HielkeMaps/hielkemaps.github.io/commit/82a31a06f14749bcddf5f58b6414d8d7b163fdd9)
#### Sunday 2022-08-14 20:27:31 by Hielke

Arrow Fight v1.2.0

- Updated to 1.19.2
- Smoothed out intro animation, its honestly like amazing so check it out
- Made players invulnerable after winning cuz its kinda weird if you can die after you win right??? just me? dxdxd
- Fixed issues switching selected map, like water reacting with lava

---
## [MrRob0-X/Nethunter_kernel_samsung_exynos7870](https://github.com/MrRob0-X/Nethunter_kernel_samsung_exynos7870)@[3f972f7989...](https://github.com/MrRob0-X/Nethunter_kernel_samsung_exynos7870/commit/3f972f7989a8be539cb288491b0ba379083b0955)
#### Sunday 2022-08-14 21:34:09 by Jonathan Toppins

mm: ratelimit PFNs busy info message

commit 75dddef32514f7aa58930bde6a1263253bc3d4ba upstream.

The RDMA subsystem can generate several thousand of these messages per
second eventually leading to a kernel crash.  Ratelimit these messages
to prevent this crash.

Doug said:
 "I've been carrying a version of this for several kernel versions. I
  don't remember when they started, but we have one (and only one) class
  of machines: Dell PE R730xd, that generate these errors. When it
  happens, without a rate limit, we get rcu timeouts and kernel oopses.
  With the rate limit, we just get a lot of annoying kernel messages but
  the machine continues on, recovers, and eventually the memory
  operations all succeed"

And:
 "> Well... why are all these EBUSY's occurring? It sounds inefficient
  > (at least) but if it is expected, normal and unavoidable then
  > perhaps we should just remove that message altogether?

  I don't have an answer to that question. To be honest, I haven't
  looked real hard. We never had this at all, then it started out of the
  blue, but only on our Dell 730xd machines (and it hits all of them),
  but no other classes or brands of machines. And we have our 730xd
  machines loaded up with different brands and models of cards (for
  instance one dedicated to mlx4 hardware, one for qib, one for mlx5, an
  ocrdma/cxgb4 combo, etc), so the fact that it hit all of the machines
  meant it wasn't tied to any particular brand/model of RDMA hardware.
  To me, it always smelled of a hardware oddity specific to maybe the
  CPUs or mainboard chipsets in these machines, so given that I'm not an
  mm expert anyway, I never chased it down.

  A few other relevant details: it showed up somewhere around 4.8/4.9 or
  thereabouts. It never happened before, but the prinkt has been there
  since the 3.18 days, so possibly the test to trigger this message was
  changed, or something else in the allocator changed such that the
  situation started happening on these machines?

  And, like I said, it is specific to our 730xd machines (but they are
  all identical, so that could mean it's something like their specific
  ram configuration is causing the allocator to hit this on these
  machine but not on other machines in the cluster, I don't want to say
  it's necessarily the model of chipset or CPU, there are other bits of
  identicalness between these machines)"

Link: http://lkml.kernel.org/r/499c0f6cc10d6eb829a67f2a4d75b4228a9b356e.1501695897.git.jtoppins@redhat.com
Signed-off-by: Jonathan Toppins <jtoppins@redhat.com>
Reviewed-by: Doug Ledford <dledford@redhat.com>
Tested-by: Doug Ledford <dledford@redhat.com>
Cc: Michal Hocko <mhocko@suse.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hillf.zj@alibaba-inc.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[8e8232c0d8...](https://github.com/CHOMPStation2/CHOMPStation2/commit/8e8232c0d826dc3341d20a7861c1d86859e06ef7)
#### Sunday 2022-08-14 21:43:02 by Rykka

Ports Taur Loafing from Cit-RP

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

For real tho laying-on-side sprites would be nice to visually represent a taur collapsed on their side, rather than faceplanting bc humancode.

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

---
## [VOREStation/VOREStation](https://github.com/VOREStation/VOREStation)@[e089978527...](https://github.com/VOREStation/VOREStation/commit/e08997852748d1155820139dfacf4745c9181ce3)
#### Sunday 2022-08-14 22:44:47 by Rykka

Ports Taur Loafing from Cit-RP & Chompstation13

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

Bear in mind that this presently only works for the drake-taur bc it's the only one that has sprites for it. The code is there, just enable can_loaf and set the offset accordingly to match if you want to sprite more taur loafs.

---

