## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-03](docs/good-messages/2022/2022-04-03.md)


1,602,891 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,602,891 were push events containing 2,398,267 commit messages that amount to 138,639,066 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[c8ef62c1fb...](https://github.com/dragomagol/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Sunday 2022-04-03 00:06:51 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[e58fb506ef...](https://github.com/dragomagol/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Sunday 2022-04-03 00:06:51 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [Amrabol/tgstation](https://github.com/Amrabol/tgstation)@[770ef81a1f...](https://github.com/Amrabol/tgstation/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Sunday 2022-04-03 00:57:39 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [kolosovpetro/Graph-Algorithms](https://github.com/kolosovpetro/Graph-Algorithms)@[6009898cab...](https://github.com/kolosovpetro/Graph-Algorithms/commit/6009898cab42712812c4734c49f5f093abee4d7f)
#### Sunday 2022-04-03 00:57:58 by PK

Merge pull request #1 from kolosovpetro/test-of-fckn-cursed-shit-let-it-die-and-burn-in-hell

Test of fckn cursed shit let it die and burn in hell

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[966d130d5c...](https://github.com/morgoth1145/advent-of-code/commit/966d130d5c474204ac8bbb86afcc9db7cca80315)
#### Sunday 2022-04-03 01:21:09 by Patrick Hogg

2018 Day 23 Part 2

Now this is an interesting problem. I'm honestly not sure if I did this right at all, but it worked.

My first inclination was to use the average of the bots positions as the starting point, but then I realized that bots with larger ranges have way more flexibility. As such, a weighted average gives a better starting point, and for the example is nearly the answer. However, searching around the current guess is complicated and if done poorly can be very slow since there's a lot of ground to cover.

I think that the approach I came up with is related to gradient ascent? I'm just trying all directions around the current point at different factors and seeing if I can make progress. Honestly it's pretty jank and haphazard, but it does give me the right answer.

Would have been an insane 8th place on the leaderboard! Wow!

Time: 0:30:07.082967

---
## [TheSeedEconomy/theseedeconomy.github.io](https://github.com/TheSeedEconomy/theseedeconomy.github.io)@[378453c428...](https://github.com/TheSeedEconomy/theseedeconomy.github.io/commit/378453c428679129036c1ce2213681a31561cc2d)
#### Sunday 2022-04-03 02:52:20 by The Seed Economy

Create README.md

The whitepaper may be freely distributed under the terms set forth in [FDL Version 1.3, 3 November 2008](https://www.gnu.org/licenses/fdl-1.3.html) and displayed below for your convenience.

We welcome all feedback and contributions. Contact: TheSeedEconomy@gmail.com

--------------------------------------------------------------------------------------------------------

GNU Free Documentation License
Version 1.3, 3 November 2008

Copyright © 2000, 2001, 2002, 2007, 2008 Free Software Foundation, Inc. <https://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

0. PREAMBLE
The purpose of this License is to make a manual, textbook, or other functional and useful document "free" in the sense of freedom: to assure everyone the effective freedom to copy and redistribute it, with or without modifying it, either commercially or noncommercially. Secondarily, this License preserves for the author and publisher a way to get credit for their work, while not being considered responsible for modifications made by others.

This License is a kind of "copyleft", which means that derivative works of the document must themselves be free in the same sense. It complements the GNU General Public License, which is a copyleft license designed for free software.

We have designed this License in order to use it for manuals for free software, because free software needs free documentation: a free program should come with manuals providing the same freedoms that the software does. But this License is not limited to software manuals; it can be used for any textual work, regardless of subject matter or whether it is published as a printed book. We recommend this License principally for works whose purpose is instruction or reference.

1. APPLICABILITY AND DEFINITIONS
This License applies to any manual or other work, in any medium, that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. Such a notice grants a world-wide, royalty-free license, unlimited in duration, to use that work under the conditions stated herein. The "Document", below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you". You accept the license if you copy, modify or distribute the work in a way requiring permission under copyright law.

A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of the Document that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (Thus, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical or political position regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are designated, as being those of Invariant Sections, in the notice that says that the Document is released under this License. If a section does not fit the above definition of Secondary then it is not allowed to be designated as Invariant. The Document may contain zero Invariant Sections. If the Document does not identify any Invariant Sections then there are none.

The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the Document is released under this License. A Front-Cover Text may be at most 5 words, and a Back-Cover Text may be at most 25 words.

A "Transparent" copy of the Document means a machine-readable copy, represented in a format whose specification is available to the general public, that is suitable for revising the document straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup, or absence of markup, has been arranged to thwart or discourage subsequent modification by readers is not Transparent. An image format is not Transparent if used for any substantial amount of text. A copy that is not "Transparent" is called "Opaque".

Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML, PostScript or PDF designed for human modification. Examples of transparent image formats include PNG, XCF and JPG. Opaque formats include proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML, PostScript or PDF produced by some word processors for output purposes only.

The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.

The "publisher" means any person or entity that distributes copies of the Document to the public.

A section "Entitled XYZ" means a named subunit of the Document whose title either is precisely XYZ or contains XYZ in parentheses following text that translates XYZ in another language. (Here XYZ stands for a specific section name mentioned below, such as "Acknowledgements", "Dedications", "Endorsements", or "History".) To "Preserve the Title" of such a section when you modify the Document means that it remains a section "Entitled XYZ" according to this definition.

The Document may include Warranty Disclaimers next to the notice which states that this License applies to the Document. These Warranty Disclaimers are considered to be included by reference in this License, but only as regards disclaiming warranties: any other implication that these Warranty Disclaimers may have is void and has no effect on the meaning of this License.

2. VERBATIM COPYING
You may copy and distribute the Document in any medium, either commercially or noncommercially, provided that this License, the copyright notices, and the license notice saying this License applies to the Document are reproduced in all copies, and that you add no other conditions whatsoever to those of this License. You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute. However, you may accept compensation in exchange for copies. If you distribute a large enough number of copies you must also follow the conditions in section 3.

You may also lend copies, under the same conditions stated above, and you may publicly display copies.

3. COPYING IN QUANTITY
If you publish printed copies (or copies in media that commonly have printed covers) of the Document, numbering more than 100, and the Document's license notice requires Cover Texts, you must enclose the copies in covers that carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly and legibly identify you as the publisher of these copies. The front cover must present the full title with all words of the title equally prominent and visible. You may add other material on the covers in addition. Copying with changes limited to the covers, as long as they preserve the title of the Document and satisfy these conditions, can be treated as verbatim copying in other respects.

If the required texts for either cover are too voluminous to fit legibly, you should put the first ones listed (as many as fit reasonably) on the actual cover, and continue the rest onto adjacent pages.

If you publish or distribute Opaque copies of the Document numbering more than 100, you must either include a machine-readable Transparent copy along with each Opaque copy, or state in or with each Opaque copy a computer-network location from which the general network-using public has access to download using public-standard network protocols a complete Transparent copy of the Document, free of added material. If you use the latter option, you must take reasonably prudent steps, when you begin distribution of Opaque copies in quantity, to ensure that this Transparent copy will remain thus accessible at the stated location until at least one year after the last time you distribute an Opaque copy (directly or through your agents or retailers) of that edition to the public.

It is requested, but not required, that you contact the authors of the Document well before redistributing any large number of copies, to give them a chance to provide you with an updated version of the Document.

4. MODIFICATIONS
You may copy and distribute a Modified Version of the Document under the conditions of sections 2 and 3 above, provided that you release the Modified Version under precisely this License, with the Modified Version filling the role of the Document, thus licensing distribution and modification of the Modified Version to whoever possesses a copy of it. In addition, you must do these things in the Modified Version:

A. Use in the Title Page (and on the covers, if any) a title distinct from that of the Document, and from those of previous versions (which should, if there were any, be listed in the History section of the Document). You may use the same title as a previous version if the original publisher of that version gives permission.
B. List on the Title Page, as authors, one or more persons or entities responsible for authorship of the modifications in the Modified Version, together with at least five of the principal authors of the Document (all of its principal authors, if it has fewer than five), unless they release you from this requirement.
C. State on the Title page the name of the publisher of the Modified Version, as the publisher.
D. Preserve all the copyright notices of the Document.
E. Add an appropriate copyright notice for your modifications adjacent to the other copyright notices.
F. Include, immediately after the copyright notices, a license notice giving the public permission to use the Modified Version under the terms of this License, in the form shown in the Addendum below.
G. Preserve in that license notice the full lists of Invariant Sections and required Cover Texts given in the Document's license notice.
H. Include an unaltered copy of this License.
I. Preserve the section Entitled "History", Preserve its Title, and add to it an item stating at least the title, year, new authors, and publisher of the Modified Version as given on the Title Page. If there is no section Entitled "History" in the Document, create one stating the title, year, authors, and publisher of the Document as given on its Title Page, then add an item describing the Modified Version as stated in the previous sentence.
J. Preserve the network location, if any, given in the Document for public access to a Transparent copy of the Document, and likewise the network locations given in the Document for previous versions it was based on. These may be placed in the "History" section. You may omit a network location for a work that was published at least four years before the Document itself, or if the original publisher of the version it refers to gives permission.
K. For any section Entitled "Acknowledgements" or "Dedications", Preserve the Title of the section, and preserve in the section all the substance and tone of each of the contributor acknowledgements and/or dedications given therein.
L. Preserve all the Invariant Sections of the Document, unaltered in their text and in their titles. Section numbers or the equivalent are not considered part of the section titles.
M. Delete any section Entitled "Endorsements". Such a section may not be included in the Modified Version.
N. Do not retitle any existing section to be Entitled "Endorsements" or to conflict in title with any Invariant Section.
O. Preserve any Warranty Disclaimers.
If the Modified Version includes new front-matter sections or appendices that qualify as Secondary Sections and contain no material copied from the Document, you may at your option designate some or all of these sections as invariant. To do this, add their titles to the list of Invariant Sections in the Modified Version's license notice. These titles must be distinct from any other section titles.

You may add a section Entitled "Endorsements", provided it contains nothing but endorsements of your Modified Version by various parties—for example, statements of peer review or that the text has been approved by an organization as the authoritative definition of a standard.

You may add a passage of up to five words as a Front-Cover Text, and a passage of up to 25 words as a Back-Cover Text, to the end of the list of Cover Texts in the Modified Version. Only one passage of Front-Cover Text and one of Back-Cover Text may be added by (or through arrangements made by) any one entity. If the Document already includes a cover text for the same cover, previously added by you or by arrangement made by the same entity you are acting on behalf of, you may not add another; but you may replace the old one, on explicit permission from the previous publisher that added the old one.

The author(s) and publisher(s) of the Document do not by this License give permission to use their names for publicity for or to assert or imply endorsement of any Modified Version.

5. COMBINING DOCUMENTS
You may combine the Document with other documents released under this License, under the terms defined in section 4 above for modified versions, provided that you include in the combination all of the Invariant Sections of all of the original documents, unmodified, and list them all as Invariant Sections of your combined work in its license notice, and that you preserve all their Warranty Disclaimers.

The combined work need only contain one copy of this License, and multiple identical Invariant Sections may be replaced with a single copy. If there are multiple Invariant Sections with the same name but different contents, make the title of each such section unique by adding at the end of it, in parentheses, the name of the original author or publisher of that section if known, or else a unique number. Make the same adjustment to the section titles in the list of Invariant Sections in the license notice of the combined work.

In the combination, you must combine any sections Entitled "History" in the various original documents, forming one section Entitled "History"; likewise combine any sections Entitled "Acknowledgements", and any sections Entitled "Dedications". You must delete all sections Entitled "Endorsements".

6. COLLECTIONS OF DOCUMENTS
You may make a collection consisting of the Document and other documents released under this License, and replace the individual copies of this License in the various documents with a single copy that is included in the collection, provided that you follow the rules of this License for verbatim copying of each of the documents in all other respects.

You may extract a single document from such a collection, and distribute it individually under this License, provided you insert a copy of this License into the extracted document, and follow this License in all other respects regarding verbatim copying of that document.

7. AGGREGATION WITH INDEPENDENT WORKS
A compilation of the Document or its derivatives with other separate and independent documents or works, in or on a volume of a storage or distribution medium, is called an "aggregate" if the copyright resulting from the compilation is not used to limit the legal rights of the compilation's users beyond what the individual works permit. When the Document is included in an aggregate, this License does not apply to the other works in the aggregate which are not themselves derivative works of the Document.

If the Cover Text requirement of section 3 is applicable to these copies of the Document, then if the Document is less than one half of the entire aggregate, the Document's Cover Texts may be placed on covers that bracket the Document within the aggregate, or the electronic equivalent of covers if the Document is in electronic form. Otherwise they must appear on printed covers that bracket the whole aggregate.

8. TRANSLATION
Translation is considered a kind of modification, so you may distribute translations of the Document under the terms of section 4. Replacing Invariant Sections with translations requires special permission from their copyright holders, but you may include translations of some or all Invariant Sections in addition to the original versions of these Invariant Sections. You may include a translation of this License, and all the license notices in the Document, and any Warranty Disclaimers, provided that you also include the original English version of this License and the original versions of those notices and disclaimers. In case of a disagreement between the translation and the original version of this License or a notice or disclaimer, the original version will prevail.

If a section in the Document is Entitled "Acknowledgements", "Dedications", or "History", the requirement (section 4) to Preserve its Title (section 1) will typically require changing the actual title.

9. TERMINATION
You may not copy, modify, sublicense, or distribute the Document except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense, or distribute it is void, and will automatically terminate your rights under this License.

However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.

Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.

Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, receipt of a copy of some or all of the same material does not give you any rights to use it.

10. FUTURE REVISIONS OF THIS LICENSE
The Free Software Foundation may publish new, revised versions of the GNU Free Documentation License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. See https://www.gnu.org/licenses/.

Each version of the License is given a distinguishing version number. If the Document specifies that a particular numbered version of this License "or any later version" applies to it, you have the option of following the terms and conditions either of that specified version or of any later version that has been published (not as a draft) by the Free Software Foundation. If the Document does not specify a version number of this License, you may choose any version ever published (not as a draft) by the Free Software Foundation. If the Document specifies that a proxy can decide which future versions of this License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Document.

11. RELICENSING
"Massive Multiauthor Collaboration Site" (or "MMC Site") means any World Wide Web server that publishes copyrightable works and also provides prominent facilities for anybody to edit those works. A public wiki that anybody can edit is an example of such a server. A "Massive Multiauthor Collaboration" (or "MMC") contained in the site means any set of copyrightable works thus published on the MMC site.

"CC-BY-SA" means the Creative Commons Attribution-Share Alike 3.0 license published by Creative Commons Corporation, a not-for-profit corporation with a principal place of business in San Francisco, California, as well as future copyleft versions of that license published by that same organization.

"Incorporate" means to publish or republish a Document, in whole or in part, as part of another Document.

An MMC is "eligible for relicensing" if it is licensed under this License, and if all works that were first published under this License somewhere other than this MMC, and subsequently incorporated in whole or in part into the MMC, (1) had no cover texts or invariant sections, and (2) were thus incorporated prior to November 1, 2008.

The operator of an MMC Site may republish an MMC contained in the site under CC-BY-SA on the same site at any time before August 1, 2009, provided the MMC is eligible for relicensing.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[54403a1ca0...](https://github.com/timothymtorres/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Sunday 2022-04-03 02:52:50 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f6aec35542...](https://github.com/treckstar/yolo-octo-hipster/commit/f6aec35542858a6b5d7783b59a4fc99c270da8ca)
#### Sunday 2022-04-03 03:00:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ca29fea53b...](https://github.com/treckstar/yolo-octo-hipster/commit/ca29fea53b9a3b8a0d48c31fa649d2fdd17679fd)
#### Sunday 2022-04-03 03:45:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ScottG489/metadiff-ui](https://github.com/ScottG489/metadiff-ui)@[8696e5c629...](https://github.com/ScottG489/metadiff-ui/commit/8696e5c6293914bd032f8c3ff38040be1515a023)
#### Sunday 2022-04-03 05:29:50 by Scott Giminiani

Specify catch type as any - needed with latest version of TS

This practice doesn't seem recommended, but it fixes the error. However,
the recommended practice seems very hacky, where we should be adding
conditionals inside our catch blocks to check if the type is error.
Sorry, but that's ugly and I'm not adding that in all my catch blocks.

---
## [cayorne/lucki-main-superteam](https://github.com/cayorne/lucki-main-superteam)@[a6549f5b75...](https://github.com/cayorne/lucki-main-superteam/commit/a6549f5b75c64aa659392696c69147b9b631d966)
#### Sunday 2022-04-03 06:29:22 by cayorne

i hate ethan

he is so FUCKING stupid and i hope he DIES

---
## [cyberknight777/dragonheart_kernel_oneplus_sm8150](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150)@[74237eae8d...](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150/commit/74237eae8d29d684585723ca988fe752ba507002)
#### Sunday 2022-04-03 07:15:58 by Park Ju Hyung

qcacld-3.0: Defer HDD initialization.

 * ALso rely on userspace writing to /dev/wlan, Wi-Fi
   HAL writes "ON" or "OFF" to /dev/wlan.

 * Use this method to initialize hdd as it's a safer
   way to ensure both wlan_mac.bin and WCNSS_qcom_cfg.ini
   are ready to be read.

 * This also eliminates the needs for horrible hacks
   to read the userspace file.

Change-Id: I648f1a107c095e50a64f44c39e78d6b6f917e190
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [biggrizzly0624/deepdark](https://github.com/biggrizzly0624/deepdark)@[4fdf07d412...](https://github.com/biggrizzly0624/deepdark/commit/4fdf07d41275a1e55458602ae57db72c693924c1)
#### Sunday 2022-04-03 07:32:15 by Park ji hun

Merge pull request #1 from biggrizzly0624/develop

Docs : fuck you too

---
## [mmrwoods/dotfiles](https://github.com/mmrwoods/dotfiles)@[44162db768...](https://github.com/mmrwoods/dotfiles/commit/44162db768fb8764a3ca4acc01b21024207f61c2)
#### Sunday 2022-04-03 07:33:50 by Mark Woods

Replace CtrlP with fzf and fzf.vim

It pained me to finally give up on ctrlp, but it's pretty useless on
huge codebases with many thousands of files. I can get over it being a
little slow, but the matching is poor, even with max files set to 0.

Anyway, fzf seems damn cool, I probably should have switched years ago.

The current setup works ok, but there are some FIXMEs left to address.

---
## [sony-msm8956-dev/android_kernel_sony_msm8956](https://github.com/sony-msm8956-dev/android_kernel_sony_msm8956)@[4f467eb3f9...](https://github.com/sony-msm8956-dev/android_kernel_sony_msm8956/commit/4f467eb3f911cdfb9b18e31d99ccf4c3cb29eccc)
#### Sunday 2022-04-03 08:39:17 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [Chemlight/Hyper-Station-13](https://github.com/Chemlight/Hyper-Station-13)@[5d96c13de2...](https://github.com/Chemlight/Hyper-Station-13/commit/5d96c13de288fd1d735a392ceffd991d7ecc17f2)
#### Sunday 2022-04-03 10:00:21 by sarcoph

holy fucking shit i am so tired of refactoring

to do list:
- ensure all useBackends use context instead of props
- ensure all uis that need it get their `{ act, data, config }` from useBackend(context)
- fix the rest of the bugs

i do not have the energy for this.

---
## [libxzr/android_kernel_oneplus_sm8250](https://github.com/libxzr/android_kernel_oneplus_sm8250)@[116a7c808d...](https://github.com/libxzr/android_kernel_oneplus_sm8250/commit/116a7c808dfa6f6a4e4aed327d91876ee78550f0)
#### Sunday 2022-04-03 10:14:04 by alk3pInjection

disp: msm: Handle dim for udfps

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

---
## [invenius/guava](https://github.com/invenius/guava)@[e015172847...](https://github.com/invenius/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Sunday 2022-04-03 10:25:17 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [Dark-Matter7232/cybertron_hanoip](https://github.com/Dark-Matter7232/cybertron_hanoip)@[0c758cad9b...](https://github.com/Dark-Matter7232/cybertron_hanoip/commit/0c758cad9ba557ae914b055c51ac466e73e7b74c)
#### Sunday 2022-04-03 10:51:33 by Peter Zijlstra

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

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c25fd13a05...](https://github.com/mrakgr/The-Spiral-Language/commit/c25fd13a05a47a81ae1b93fc344bfb7e5b795423)
#### Sunday 2022-04-03 11:39:08 by Marko Grdinić

"10:50am. Got up 20m ago. Let me do my morning reading. It is good that I am slowly adjusting my schedule.

11am. I feel like chilling for a while longer. Who feels like starting? Slacking is food for the soul.

11:25am. Let me start. There is one thing I've realized - textures are awful. They are the worst idea in 3d, but the ability to do it all procedurally is not there. I am thinking of studying Designer for a bit just so I can get a grasp on what it is about.

11:35am. That procedural texturing course I got, let me watch some of it. I'll download Ds while that is going on.

11:50am. It seems the course will explain what the texture coordinates in Blender are. Nice. The Houdini + Clarisse course I got previously was mediocre, but this seems like it could be good.

11:55am. This explanation of coordinate spaces is so good. When I was starting to study shading, this is the kind of course that I needed. It gets points just for that.

12:20pm. This course is not something you can watch casually. It is quite technical. I'd need to follow it along in order to grasp it. Let me watch a Designer tutorial. I want to see how it works.

https://substance3d.adobe.com/tutorials/courses/First-Steps-with-Substance-3D-Designer/youtube-VyFgpitTsYg

Let me watch some of these.

12:25pm. Hmmm, can you really not do your texturing in Designer. It has a visualizer, so I do not see any problem.

https://youtu.be/VyFgpitTsYg?t=198

Oh, this has the radial patterns as expected

I have to admit at this point, this way of chaining parameterized nodes is quite something.

The closest analogue in functional programming is using partially applied functions (combinators) and those are quite effective in their domain, such as parsing.

12:40pm. Let me watch the first part and then I'll have breakfast. I am starting to get into it.

12:45pm. I wonder if it is possible to paint directly in Designer?

12:50pm. I hate how RapidGator seems to be designed just to annoy me. AlfaFile might be slower, but it does not bother me what I forget about the captcha for half an hour.

https://youtu.be/VyFgpitTsYg?t=693

I am here so far. This is powerful functionality. There is no reason why I can't use both Designer and Painter.

When I am strapped for time I feel like limiting myself, but when I am true to my desires I spend time in exploration.

Yeah, it is not worth it to force myself to do Heaven's Key. I am fine with going towards it, but if I really need money I'll just get a programming job.

https://youtu.be/VyFgpitTsYg?t=818

This is nice.

Let me watch part 2 as well, after that I'll take a break.

https://youtu.be/LJFgZvNGN9U?t=315

Here is the warp node. This is what I've been wanting all along.

https://youtu.be/LJFgZvNGN9U?t=445

Directional warp. Exactly what I'd need. Maybe the guy who said that Painter without Designer is a car without wheels was right.

Just who am I? Of course I should be aiming to master both. I'd want to add Mari into the mix even if it takes me much longer.

That scratch floor texture I did in Houdini? I could have done it in a single stroke in Painter.

I'll want to figure out how to import the V-Ray asset library into Substance Painter.

https://youtu.be/LJFgZvNGN9U?t=684

It is that easy to interop between the programs? Nice.

I might as well watch part 3. I am into it.

https://youtu.be/22fZAM6r6Hg?t=305

There is a safe transform it seems.

1:30pm. Watched the vids.

1:30pm. Since things are the way they are, why not learn both Painter and Designer at the same time? Now if only this would download. Right now I am waiting for the Gator timeout to run out.  I'll go back to the other basic Painter tutorial and go through it. By the time I am done with it, Designer should have finished downloading.

It is fine if I immerse myself in this. I mean apart from texturing and shading what else is there before I can consider myself to be proficient at 3d art? Not much. I am already decently along the learning curve, I just need to seal the deal. So what if it take me a couple of weeks to get through all of this?

It is nothing.

While I was programming, did I rush the creation of Spiral? No. And neither will I rush this. There is no reason for me to not create my own materials when I need them. It is not an activity I should fear.

I will master it all and get to the highest level in 3d. After I do that I'll be able to create whatever I want."

---
## [G3-Studio/Grief-Day](https://github.com/G3-Studio/Grief-Day)@[bfe839ebec...](https://github.com/G3-Studio/Grief-Day/commit/bfe839ebecca217d4b0f045b44526cad2073eaaa)
#### Sunday 2022-04-03 12:30:16 by Vincent Gonnet

I commited a horrible and unbelievable sin, sorry Teddy, shall you forgive me master

---
## [kreindo/tgstation](https://github.com/kreindo/tgstation)@[745426eff2...](https://github.com/kreindo/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Sunday 2022-04-03 13:14:52 by LemonInTheDark

Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [mszeles/a-humanisch-human-s-thoughtiesch-wordsisch-and-artisch-about-lifeisch-universeisch-and-everythingisc](https://github.com/mszeles/a-humanisch-human-s-thoughtiesch-wordsisch-and-artisch-about-lifeisch-universeisch-and-everythingisc)@[c24a0b4328...](https://github.com/mszeles/a-humanisch-human-s-thoughtiesch-wordsisch-and-artisch-about-lifeisch-universeisch-and-everythingisc/commit/c24a0b4328c6bb36c82f00a5097ebe79d52101dd)
#### Sunday 2022-04-03 13:16:52 by MSzeles

Miki: What is this Minnie?
Minnie: To be honest this is the best guidline how to raise your thinking to the next level.
Metro: This is the solution with which you can not just make your mind multithreaded, but you can also genrate new cores daily in your brain.

 And if that would not be enough, you can continuosly interact with your characters, which is used in deep-learning. And you saw what can be achieved by playing against yourself.
 Miki: Minnie! Do you think this can be the solution to overperform the artifical intelligence?
 Minnie: I do believe it.
 Miki: Me too.
 Mictor: Such brainpower.
 Niklolai: Such bullshit.

---
## [JRDead/fulpstation](https://github.com/JRDead/fulpstation)@[c797bf79ea...](https://github.com/JRDead/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Sunday 2022-04-03 13:23:22 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [tchurusinov/Problems_HackBulgaria](https://github.com/tchurusinov/Problems_HackBulgaria)@[70c1b8a711...](https://github.com/tchurusinov/Problems_HackBulgaria/commit/70c1b8a711a70977a2fece09dee326acbb0d940b)
#### Sunday 2022-04-03 14:45:04 by tchurusinov

Create p19

Ivan and his friends love going to the cinema (that's pre-pandemic).
But when it comes to picking seats, they don't like the usual & boring "next to each other in one row" placement.
That's why they always pick their seats in a strange way:
Maria should be above Ivan.
Georgi should be to the right of Maria.
Veronika should be above Maria.
And when they are done, they can take really strange forms (at least, strange in the eyes of the cinema owners).
You'll be given 2 arguments:
The cinema layout
The configuration our friends want to take.
The function should return a list of all possible placements, that satisfy the given form. This is basically a list of possible cinema layouts (structure the layouts the same way as the input)
Possible placement is a configuration where:
Our friends can book seats in the way they want.
They are not going outside of the cinema.
They are not taking any already reserved seats.

---
## [theXDkidoflol/Shiptest](https://github.com/theXDkidoflol/Shiptest)@[031c0866ed...](https://github.com/theXDkidoflol/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Sunday 2022-04-03 15:49:11 by SweetBlueSylveon

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
## [ahjragaas/binutils-gdb](https://github.com/ahjragaas/binutils-gdb)@[df7a7bdd97...](https://github.com/ahjragaas/binutils-gdb/commit/df7a7bdd9766adebc6b117c31bc617d81c1efd43)
#### Sunday 2022-04-03 16:20:12 by rupothar

gdb: add support for Fortran's ASSUMED RANK arrays

This patch adds a new dynamic property DYN_PROP_RANK, this property is
read from the DW_AT_rank attribute and stored within the type just
like other dynamic properties.

As arrays with dynamic ranks make use of a single
DW_TAG_generic_subrange to represent all ranks of the array, support
for this tag has been added to dwarf2/read.c.

The final piece of this puzzle is to add support in gdbtypes.c so that
we can resolve an array type with dynamic rank.  To do this the
existing resolve_dynamic_array_or_string function is split into two,
there's a new resolve_dynamic_array_or_string_1 core that is
responsible for resolving each rank of the array, while the now outer
resolve_dynamic_array_or_string is responsible for figuring out the
array rank (which might require resolving a dynamic property) and then
calling the inner core.

The resolve_dynamic_range function now takes a rank, which is passed
on to the dwarf expression evaluator.  This rank will only be used in
the case where the array itself has dynamic rank, but we now pass the
rank in all cases, this should be harmless if the rank is not needed.

The only small nit is that resolve_dynamic_type_internal actually
handles resolving dynamic ranges itself, which now obviously requires
us to pass a rank value.  But what rank value to use?  In the end I
just passed '1' through here as a sane default, my thinking is that if
we are in resolve_dynamic_type_internal to resolve a range, then the
range isn't part of an array with dynamic rank, and so the range
should actually be using the rank value at all.

An alternative approach would be to make the rank value a
gdb::optional, however, this ends up adding a bunch of complexity to
the code (e.g. having to conditionally build the array to pass to
dwarf2_evaluate_property, and handling the 'rank - 1' in
resolve_dynamic_array_or_string_1) so I haven't done that, but could,
if people think that would be a better approach.

Finally, support for assumed rank arrays was only fixed very recently
in gcc, so you'll need the latest gcc in order to run the tests for
this.

Here's an example test program:

  PROGRAM arank
    REAL :: a1(10)
    CALL sub1(a1)

  CONTAINS

    SUBROUTINE sub1(a)
      REAL :: a(..)
      PRINT *, RANK(a)
    END SUBROUTINE sub1
  END PROGRAM arank

Compiler Version:
gcc (GCC) 12.0.0 20211122 (experimental)

Compilation command:
gfortran assumedrank.f90 -gdwarf-5 -o assumedrank

Without Patch:

  gdb -q assumedrank
  Reading symbols from assumedrank...
  (gdb) break sub1
  Breakpoint 1 at 0x4006ff: file assumedrank.f90, line 10.
  (gdb) run
  Starting program: /home/rupesh/STAGING-BUILD-2787/bin/assumedrank

  Breakpoint 1, arank::sub1 (a=<unknown type in /home/rupesh/STAGING-BUILD-2787
  /bin/assumedrank, CU 0x0, DIE 0xd5>) at assumedrank.f90:10
  10       PRINT *, RANK(a)
  (gdb) print RANK(a)
  'a' has unknown type; cast it to its declared type

With patch:

  gdb -q assumedrank
  Reading symbols from assumedrank...
  (gdb) break sub1
  Breakpoint 1 at 0x4006ff: file assumedrank.f90, line 10.
  (gdb) run
  Starting program: /home/rupesh/STAGING-BUILD-2787/bin/assumedrank

  Breakpoint 1, arank::sub1 (a=...) at assumedrank.f90:10
  10       PRINT *, RANK(a)
  (gdb) print RANK(a)
  $1 = 1
  (gdb) ptype a
  type = real(kind=4) (10)
  (gdb)

Co-Authored-By: Andrew Burgess <aburgess@redhat.com>

---
## [fordin93379/shop](https://github.com/fordin93379/shop)@[a3d27adcff...](https://github.com/fordin93379/shop/commit/a3d27adcffbb452f0f315884f2bc1c9cda9047d3)
#### Sunday 2022-04-03 16:23:08 by Fedor

fuck REACT i hate it. COMPONENT DONT WORK TOMOROW I GO TO SCHOOL I ENJOY DEAD

---
## [amir73il/linux](https://github.com/amir73il/linux)@[94b261b1a7...](https://github.com/amir73il/linux/commit/94b261b1a7009937bb9c3b1ddb374c88f560da26)
#### Sunday 2022-04-03 16:23:32 by Dave Chinner

xfs: logging the on disk inode LSN can make it go backwards

commit 32baa63d82ee3f5ab3bd51bae6bf7d1c15aed8c7 upstream.

When we log an inode, we format the "log inode" core and set an LSN
in that inode core. We do that via xfs_inode_item_format_core(),
which calls:

	xfs_inode_to_log_dinode(ip, dic, ip->i_itemp->ili_item.li_lsn);

to format the log inode. It writes the LSN from the inode item into
the log inode, and if recovery decides the inode item needs to be
replayed, it recovers the log inode LSN field and writes it into the
on disk inode LSN field.

Now this might seem like a reasonable thing to do, but it is wrong
on multiple levels. Firstly, if the item is not yet in the AIL,
item->li_lsn is zero. i.e. the first time the inode it is logged and
formatted, the LSN we write into the log inode will be zero. If we
only log it once, recovery will run and can write this zero LSN into
the inode.

This means that the next time the inode is logged and log recovery
runs, it will *always* replay changes to the inode regardless of
whether the inode is newer on disk than the version in the log and
that violates the entire purpose of recording the LSN in the inode
at writeback time (i.e. to stop it going backwards in time on disk
during recovery).

Secondly, if we commit the CIL to the journal so the inode item
moves to the AIL, and then relog the inode, the LSN that gets
stamped into the log inode will be the LSN of the inode's current
location in the AIL, not it's age on disk. And it's not the LSN that
will be associated with the current change. That means when log
recovery replays this inode item, the LSN that ends up on disk is
the LSN for the previous changes in the log, not the current
changes being replayed. IOWs, after recovery the LSN on disk is not
in sync with the LSN of the modifications that were replayed into
the inode. This, again, violates the recovery ordering semantics
that on-disk writeback LSNs provide.

Hence the inode LSN in the log dinode is -always- invalid.

Thirdly, recovery actually has the LSN of the log transaction it is
replaying right at hand - it uses it to determine if it should
replay the inode by comparing it to the on-disk inode's LSN. But it
doesn't use that LSN to stamp the LSN into the inode which will be
written back when the transaction is fully replayed. It uses the one
in the log dinode, which we know is always going to be incorrect.

Looking back at the change history, the inode logging was broken by
commit 93f958f9c41f ("xfs: cull unnecessary icdinode fields") way
back in 2016 by a stupid idiot who thought he knew how this code
worked. i.e. me. That commit replaced an in memory di_lsn field that
was updated only at inode writeback time from the inode item.li_lsn
value - and hence always contained the same LSN that appeared in the
on-disk inode - with a read of the inode item LSN at inode format
time. CLearly these are not the same thing.

Before 93f958f9c41f, the log recovery behaviour was irrelevant,
because the LSN in the log inode always matched the on-disk LSN at
the time the inode was logged, hence recovery of the transaction
would never make the on-disk LSN in the inode go backwards or get
out of sync.

A symptom of the problem is this, caught from a failure of
generic/482. Before log recovery, the inode has been allocated but
never used:

xfs_db> inode 393388
xfs_db> p
core.magic = 0x494e
core.mode = 0
....
v3.crc = 0x99126961 (correct)
v3.change_count = 0
v3.lsn = 0
v3.flags2 = 0
v3.cowextsize = 0
v3.crtime.sec = Thu Jan  1 10:00:00 1970
v3.crtime.nsec = 0

After log recovery:

xfs_db> p
core.magic = 0x494e
core.mode = 020444
....
v3.crc = 0x23e68f23 (correct)
v3.change_count = 2
v3.lsn = 0
v3.flags2 = 0
v3.cowextsize = 0
v3.crtime.sec = Thu Jul 22 17:03:03 2021
v3.crtime.nsec = 751000000
...

You can see that the LSN of the on-disk inode is 0, even though it
clearly has been written to disk. I point out this inode, because
the generic/482 failure occurred because several adjacent inodes in
this specific inode cluster were not replayed correctly and still
appeared to be zero on disk when all the other metadata (inobt,
finobt, directories, etc) indicated they should be allocated and
written back.

The fix for this is two-fold. The first is that we need to either
revert the LSN changes in 93f958f9c41f or stop logging the inode LSN
altogether. If we do the former, log recovery does not need to
change but we add 8 bytes of memory per inode to store what is
largely a write-only inode field. If we do the latter, log recovery
needs to stamp the on-disk inode in the same manner that inode
writeback does.

I prefer the latter, because we shouldn't really be trying to log
and replay changes to the on disk LSN as the on-disk value is the
canonical source of the on-disk version of the inode. It also
matches the way we recover buffer items - we create a buf_log_item
that carries the current recovery transaction LSN that gets stamped
into the buffer by the write verifier when it gets written back
when the transaction is fully recovered.

However, this might break log recovery on older kernels even more,
so I'm going to simply ignore the logged value in recovery and stamp
the on-disk inode with the LSN of the transaction being recovered
that will trigger writeback on transaction recovery completion. This
will ensure that the on-disk inode LSN always reflects the LSN of
the last change that was written to disk, regardless of whether it
comes from log recovery or runtime writeback.

Fixes: 93f958f9c41f ("xfs: cull unnecessary icdinode fields")
Signed-off-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---
## [zinc-collective/convene](https://github.com/zinc-collective/convene)@[add90291f1...](https://github.com/zinc-collective/convene/commit/add90291f1e5462c6e27db0bb624bd148e470c93)
#### Sunday 2022-04-03 17:07:42 by Zee

Sprout EmbeddedForm independent of Space Registration (#620)

EmbeddedForms allow AirTable forms to be embedded directly into a Room.

Things like opinion polls, newsletter signups, comment boxes, etc.

If you can make an AirTable form for it, you can put it on your landing 
page!

Squashed commit of the following:

commit ede2fbff74f634756b5ba6dfa7a76f765ea20307
Author: Zee Spencer <zspencer@users.noreply.github.com>
Date:   Wed Mar 9 19:58:10 2022 -0800

    Sprout `EmbeddableForm` Furniture

    As we begin this, we thought that it makes sense to start down the path
    of using a generic piece of Furniture, so that we're catfooding what the
    customer experience for other Spaces look like.

    So we've sprouted a piece of furniture that can embed a form from
    Airtable right into a Space! MAGIC!

Co-authored-by: Ana Ulin <ana@ulin.org>
Co-authored-by: Zee Spencer <zspencer@users.noreply.github.com>

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[c151af1c19...](https://github.com/san7890/bruhstation/commit/c151af1c193a1496c67c7ce2f966630a57d15eb3)
#### Sunday 2022-04-03 18:06:25 by san7890

Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

---
## [gauravxor/github-slideshow](https://github.com/gauravxor/github-slideshow)@[343c96a0e0...](https://github.com/gauravxor/github-slideshow/commit/343c96a0e049555afa729c30400c84b4a862fd04)
#### Sunday 2022-04-03 18:19:45 by Gaurav

Added a meme at the end of the file.

Just made some insane changes in the repo by working my ass off for three consecutive day and night.

---
## [bgamez23/15-3athena](https://github.com/bgamez23/15-3athena)@[d32cce5b08...](https://github.com/bgamez23/15-3athena/commit/d32cce5b081436a68a3c46883675c0ad052127f9)
#### Sunday 2022-04-03 18:33:59 by 15peaces

== Achievement System Rewrite (Part 4) ==
=General:
*Merged missing changes from 3ceam rev. 722 - 724

*Fixed a issue where the zenkai unit coding would leak into other coding following it when certain conditions are met. Because of this issue, its critically recommend users running a server revision between 278 - 279 (the last two updates) update to this revision ASAP to get the issue fixed.

*Complete rewrite of the achievement system (part 4).
-Fixed achievement reward packet.
-Fixed getting achievement reward packets order & split achievement reward function to parts.
-Fixed an Assertion Error when refine is failed.
-Some more fixing & cleaning.
-Thanks to @HerculesWS

*This update focuses to bring HP/SP drain timers, unit invervals, some formula's, resistance, and other misc. stuff to official.
-This update along with the past few revisions brings a lot of this inaccurately coded stuff to official, as well as updated some once unknown values to official.

*Burnning status mechanic's updated to official.
-Now deals damage equal to 3 percent of your MaxHP plus a added 1000.
-Damage is dealed every 3 seconds.

*Added clif_parse_UseSkillToPos_homun function.
-This function allows a homunculus to be able to use ground targeted skills.
-A number of mutated homunculus skills requires this function to work.

=Skills:
*NC_ARMSCANNON
-Updated source code to work with the new target type.
-Now targets enemy's.

*SO_CLOUD_KILL
*SO_WARMER
-Fixed a issue where the AoE would not generate when casted.

*SO_ARRULLO
-Updated source code to work with the new target type.
-Now targets the ground.

*GC_WEAPONBLOCKING
-SP drain timer updated to every 5 seconds.

*GC_HALLUCINATIONWALK
-Now requires a percentage of your MaxHP to cast.
-HP percentage needed is affected by skill level.

*AB_PRAEFATIO
-The HP of the kyrie barrier generated through this skill is no longer affected by the learned level of Kyrie Eleison. It is now entirely affected by the used level of this skill.
-This is official and interesting as this skill can set a higher HP then regular kyrie can.

*WL_WHITEIMPRISON
-Removed a piece of code thats no longer needed.

*WL_RADIUS
-Fixed cast time formula reduction updated to official. The real official this time.
-Not that bullshit made up formula that was in that iRO document.

*WL_READING_SB
-SP drain timer updated to every 10 seconds.

*RA_WUGBITE
-Fixed a issue where RA_TOOTHOFWUG increased the duration twice as much as it should.
-Success chance updated to official. This also adds the resistance formula as well.

*NC_COLDSLOWER
-Status are now applied through a special check.
-It will first try to freeze any enemy that is hit.
-It will then try to give frost misty status to any enemy it fails to freeze.

*NC_STEALTHFIELD
-Now drains 1 percent of SP between every 3 to 5 seconds depending on the skill level used.

*LG_REFLECTDAMAGE
-SP drain timer updated to every 10 seconds.
-SP drain amount per drain updated.

*LG_INSPIRATION
-HP and SP drain timer updated to every 5 seconds.

*WM_SATURDAY_NIGHT_FEVER
-HP and SP drain timers updated to every 3 seconds.

*SO_DIAMONDDUST
-Status duration reduction formula added.

*SO_VACUUM_EXTREME
*GN_WALLOFTHORN
*GN_DEMONIC_FIRE
-Unit inverval updated to official.

*SO_VARETYR_SPEAR
-Small change to the code.

*MH_POISON_MIST
-Added full support for this skill.

---
## [krzk/linux](https://github.com/krzk/linux)@[53a05ad9f2...](https://github.com/krzk/linux/commit/53a05ad9f21d858d24f76d12b3e990405f2036d1)
#### Sunday 2022-04-03 18:39:03 by David Hildenbrand

mm: optimize do_wp_page() for exclusive pages in the swapcache

Patch series "mm: COW fixes part 1: fix the COW security issue for THP and swap", v3.

This series attempts to optimize and streamline the COW logic for ordinary
anon pages and THP anon pages, fixing two remaining instances of
CVE-2020-29374 in do_swap_page() and do_huge_pmd_wp_page(): information
can leak from a parent process to a child process via anonymous pages
shared during fork().

This issue, including other related COW issues, has been summarized in [2]:

 "1. Observing Memory Modifications of Private Pages From A Child Process

  Long story short: process-private memory might not be as private as you
  think once you fork(): successive modifications of private memory
  regions in the parent process can still be observed by the child
  process, for example, by smart use of vmsplice()+munmap().

  The core problem is that pinning pages readable in a child process, such
  as done via the vmsplice system call, can result in a child process
  observing memory modifications done in the parent process the child is
  not supposed to observe. [1] contains an excellent summary and [2]
  contains further details. This issue was assigned CVE-2020-29374 [9].

  For this to trigger, it's required to use a fork() without subsequent
  exec(), for example, as used under Android zygote. Without further
  details about an application that forks less-privileged child processes,
  one cannot really say what's actually affected and what's not -- see the
  details section the end of this mail for a short sshd/openssh analysis.

  While commit 17839856fd58 ("gup: document and work around "COW can break
  either way" issue") fixed this issue and resulted in other problems
  (e.g., ptrace on pmem), commit 09854ba94c6a ("mm: do_wp_page()
  simplification") re-introduced part of the problem unfortunately.

  The original reproducer can be modified quite easily to use THP [3] and
  make the issue appear again on upstream kernels. I modified it to use
  hugetlb [4] and it triggers as well. The problem is certainly less
  severe with hugetlb than with THP; it merely highlights that we still
  have plenty of open holes we should be closing/fixing.

  Regarding vmsplice(), the only known workaround is to disallow the
  vmsplice() system call ... or disable THP and hugetlb. But who knows
  what else is affected (RDMA? O_DIRECT?) to achieve the same goal -- in
  the end, it's a more generic issue"

This security issue was first reported by Jann Horn on 27 May 2020 and it
currently affects anonymous pages during swapin, anonymous THP and hugetlb.
This series tackles anonymous pages during swapin and anonymous THP:

 - do_swap_page() for handling COW on PTEs during swapin directly

 - do_huge_pmd_wp_page() for handling COW on PMD-mapped THP during write
   faults

With this series, we'll apply the same COW logic we have in do_wp_page()
to all swappable anon pages: don't reuse (map writable) the page in
case there are additional references (page_count() != 1). All users of
reuse_swap_page() are remove, and consequently reuse_swap_page() is
removed.

In general, we're struggling with the following COW-related issues:

(1) "missed COW": we miss to copy on write and reuse the page (map it
    writable) although we must copy because there are pending references
    from another process to this page. The result is a security issue.

(2) "wrong COW": we copy on write although we wouldn't have to and
    shouldn't: if there are valid GUP references, they will become out
    of sync with the pages mapped into the page table. We fail to detect
    that such a page can be reused safely, especially if never more than
    a single process mapped the page. The result is an intra process
    memory corruption.

(3) "unnecessary COW": we copy on write although we wouldn't have to:
    performance degradation and temporary increases swap+memory
    consumption can be the result.

While this series fixes (1) for swappable anon pages, it tries to reduce
reported cases of (3) first as good and easy as possible to limit the
impact when streamlining.  The individual patches try to describe in
which cases we will run into (3).

This series certainly makes (2) worse for THP, because a THP will now
get PTE-mapped on write faults if there are additional references, even
if there was only ever a single process involved: once PTE-mapped, we'll
copy each and every subpage and won't reuse any subpage as long as the
underlying compound page wasn't split.

I'm working on an approach to fix (2) and improve (3): PageAnonExclusive
to mark anon pages that are exclusive to a single process, allow GUP
pins only on such exclusive pages, and allow turning exclusive pages
shared (clearing PageAnonExclusive) only if there are no GUP pins.  Anon
pages with PageAnonExclusive set never have to be copied during write
faults, but eventually during fork() if they cannot be turned shared.
The improved reuse logic in this series will essentially also be the
logic to reset PageAnonExclusive.  This work will certainly take a
while, but I'm planning on sharing details before having code fully
ready.

#1-#5 can be applied independently of the rest. #6-#9 are mostly only
cleanups related to reuse_swap_page().

Notes:
* For now, I'll leave hugetlb code untouched: "unnecessary COW" might
  easily break existing setups because hugetlb pages are a scarce resource
  and we could just end up having to crash the application when we run out
  of hugetlb pages. We have to be very careful and the security aspect with
  hugetlb is most certainly less relevant than for unprivileged anon pages.
* Instead of lru_add_drain() we might actually just drain the lru_add list
  or even just remove the single page of interest from the lru_add list.
  This would require a new helper function, and could be added if the
  conditional lru_add_drain() turn out to be a problem.
* I extended the test case already included in [1] to also test for the
  newly found do_swap_page() case. I'll send that out separately once/if
  this part was merged.

[1] https://lkml.kernel.org/r/20211217113049.23850-1-david@redhat.com
[2] https://lore.kernel.org/r/3ae33b08-d9ef-f846-56fb-645e3b9b4c66@redhat.com

This patch (of 9):

Liang Zhang reported [1] that the current COW logic in do_wp_page() is
sub-optimal when it comes to swap+read fault+write fault of anonymous
pages that have a single user, visible via a performance degradation in
the redis benchmark.  Something similar was previously reported [2] by
Nadav with a simple reproducer.

After we put an anon page into the swapcache and unmapped it from a single
process, that process might read that page again and refault it read-only.
If that process then writes to that page, the process is actually the
exclusive user of the page, however, the COW logic in do_co_page() won't
be able to reuse it due to the additional reference from the swapcache.

Let's optimize for pages that have been added to the swapcache but only
have an exclusive user.  Try removing the swapcache reference if there is
hope that we're the exclusive user.

We will fail removing the swapcache reference in two scenarios:
(1) There are additional swap entries referencing the page: copying
    instead of reusing is the right thing to do.
(2) The page is under writeback: theoretically we might be able to reuse
    in some cases, however, we cannot remove the additional reference
    and will have to copy.

Note that we'll only try removing the page from the swapcache when it's
highly likely that we'll be the exclusive owner after removing the page
from the swapache.  As we're about to map that page writable and redirty
it, that should not affect reclaim but is rather the right thing to do.

Further, we might have additional references from the LRU pagevecs, which
will force us to copy instead of being able to reuse.  We'll try handling
such references for some scenarios next.  Concurrent writeback cannot be
handled easily and we'll always have to copy.

While at it, remove the superfluous page_mapcount() check: it's
implicitly covered by the page_count() for ordinary anon pages.

[1] https://lkml.kernel.org/r/20220113140318.11117-1-zhangliang5@huawei.com
[2] https://lkml.kernel.org/r/0480D692-D9B2-429A-9A88-9BBA1331AC3A@gmail.com

Link: https://lkml.kernel.org/r/20220131162940.210846-2-david@redhat.com
Signed-off-by: David Hildenbrand <david@redhat.com>
Reported-by: Liang Zhang <zhangliang5@huawei.com>
Reported-by: Nadav Amit <nadav.amit@gmail.com>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Cc: Hugh Dickins <hughd@google.com>
Cc: David Rientjes <rientjes@google.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Jason Gunthorpe <jgg@nvidia.com>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Mike Rapoport <rppt@linux.ibm.com>
Cc: Yang Shi <shy828301@gmail.com>
Cc: Kirill A. Shutemov <kirill.shutemov@linux.intel.com>
Cc: Jann Horn <jannh@google.com>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Roman Gushchin <roman.gushchin@linux.dev>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Don Dutile <ddutile@redhat.com>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Jan Kara <jack@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [ajxu2/competitive-programming](https://github.com/ajxu2/competitive-programming)@[528d6c3cf1...](https://github.com/ajxu2/competitive-programming/commit/528d6c3cf19bfb9c4d616bee64eb2b810cc16d1b)
#### Sunday 2022-04-03 18:46:52 by Anthony Xu

Add USACO Silver US Open 2022 Subset Equality

Didn't notice that it didn't say |s|=|t| I hate my life.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[61ae8a8917...](https://github.com/mrakgr/The-Spiral-Language/commit/61ae8a891774f953a02994b2951e57eae761cd98)
#### Sunday 2022-04-03 19:13:46 by Marko Grdinić

"2:05pm. Done with chores. Lunch will be in 30m so I'll wait for it instead of having breakfast now.

2:50pm. Done with lunch. Let me just finish watching the Kuroitsu's Mummy ep that I've started and then I will resume. Ds finished downloading, so I might as well install it.

2:55pm. I'll be more motivated if I can make the radial texture right away. How about I give painter a break and make the thing?

First let me actually finish the episode.

3:15pm. Done. Let me run Substance Designer for the first time.

3:25pm. I can't quite get the image that I want using warping and gaussian noise. I guess I have some studying I need to do. It will be Houdini all over again.

I can confirm that gradient mapping works quite well in designer. I starded with a paraboloid and then made those rings without issue.

Hmmm, I'll figure it out at some point. I still do no know how to do something basic as setting a range.

My first impression of Designer is quite positive. It looks and feels nice.

3:45pm. https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Painter-2021/youtube--ZbmRsOnApk

I am getting lost in thought. Let me just start with this. As fun as Ds looks, let me leave it for a while.

3:50pm. He says that Substance Painter is non destructive - does he mean all the way through? Then, does that mean I can work in 2048 and upscale it without issue later? If so that would be cool.

Let me ask in the thread.

4:05pm. https://youtu.be/_j27AS0VQOw?t=397

This is not something I knew about. You can use vertex colors to later help the placement of materials. Did he do that instead of grouping?

4:45pm. Had to take a break. Let me resume.

5:25pm. https://youtu.be/_j27AS0VQOw?t=1518

Color selection. This is interesting.

https://youtu.be/_j27AS0VQOw?t=1530

Why aren't the colors for the body showing up for me? ...For some reason it did not bake the vertex colors for the body. Fixed it.

https://youtu.be/_j27AS0VQOw?t=1585

Oh, the geometry mask feature is more recent than color selection. That is why it did not start out with it.

Still, it is good that I am going through these tutorials otherwise I would never have figured it out.

https://youtu.be/O_0Feo2NqkE?t=487

Hmmm, this is cool. Doing color selections like this is not something I'd have figured out on my own.

7:10pm. https://youtu.be/O_0Feo2NqkE?t=1157

I do not like how he duplicated the layer here, but I can't think of anything other than to use the multiply layer. I tried using passthrough with the HSL filter, but it is not working well for me. For example, moving the saturation slider is doing nothing.

Actually, let me experiment with it without the mask. This is a good opportunity to see if the passthrough blending mode makes sense to me.

Ok, I understand why moving the saturation does nothing. It is taking the base color value of the layer itself which is 0.5 grayscale.

Hmmm, I think I get this. I think that passthrough works based off opacity. Unlike for the normal layer, its opaque values substitutes from the layer below.

How would I get that with fill layers?

7:30pm. Apparently I can't. The fill layers just fill. I need a color layer with pass through. Then I can set the mask and use the HSL layer to get what I want. But the result is pretty much equivalent to using a multiply layer in this case.

Still, the passthrough layer is just what I thought they would be.

I've changed my mind - I can totally do the radial patterns by hand thanks to them. Sure I'd need to duplicate them...

Actually, even just copying and using the screen layer would be enough as well.

Hmmm, what happens if I use the eraser with the pass through layer? It ends up reverting the paint underneath, but that is what a regular layer would do as well. Makes sense, makes sense...

7:05pm. Substance Painter is really a remarkable piece of software. I thought it was 3d Photoshop, but that is wrong. PS and CSP do not do their strokes non-destructively. The fact that it is non-destructive closes off some avenues, but also opens a lot of possibility.

I absolutely should not feel restricted when it comes to painting these radial patterns. It can easily be done even without stencils.

7:35pm. Let me get started with part 3.

Though at this point I am getting tired.

7:50pm. https://youtu.be/dYC_ElMLxX0?t=576

I do not feel like following this directly. At this point, let me just watch the rest and I will close for the day.

https://youtu.be/dYC_ElMLxX0?t=811

Ahhh, I get it. This is what painting in UV space means for the alignment. It just assumes I'd have clicked in the UV view based on the 3d view position.

8:20pm. Had to take a short break. Let me watch part 4 and 5.

They are short, so I should be done quickly.

https://youtu.be/dHpGMHHxM_o?t=199

Oh, you can actually write text in here. That is nice.

https://youtu.be/dHpGMHHxM_o?t=359

Backface culling is a thing here. This is something I need to remember.

https://youtu.be/dHpGMHHxM_o?t=480

I also need to remember this way of putting the decals using the Alt key.

https://youtu.be/4iUVOfGOxPI?t=121

I wonder why 8k is the max?

8:40pm. I did a quick search and it seems this is on purpose due to hardware limitations. The devs recommend using UDIMs. Yeah, there is a point to this, textures have n^2 scaling. You can't do much with them.

At any rate, I did a stupid thing by switching to 4k for the table. I could have done with less and exported it after that if I really needed the detail.

8:50pm. I am done for today. I sure am tired of these tutorials. To think there are a couple of more like this one coming up. Well, I'll handle it.

I need this exp to be effective. There is no way around it. It is my usual style of learning.

I am not sure how far I'll want to go with Designer. I'll see how it works as I go along.

9pm. https://youtu.be/MQjN68MfJSM
Designer Quicktip 05 Brush Strokes

Now I am watching this. Maybe I should just do the texture in CSP, that would be by far the simplest solution. It would be a good to refresh my memory of it.

https://substance3d.adobe.com/tutorials/courses/Designer-Quicktips/youtube-Q9mEcCWsOQc
DESIGNER QUICKTIPS

There is also this route. I'll watch this tomorrow. I'll decide what I want to when I've covered enough ground. I'll probably pick the CSP route, but who would I be unless I made an informed choice first.

9:10pm. I suppsoe this is good for a day's work. I'll get more done tomorrow. I'll do a bit of designer and do the radial texture as homework so it does not get too monotonous with Painter. Right now let me have dinner."

---
## [travisgamemaker/FNF-PsychEngineTGMix](https://github.com/travisgamemaker/FNF-PsychEngineTGMix)@[c63d646f8e...](https://github.com/travisgamemaker/FNF-PsychEngineTGMix/commit/c63d646f8ef18a07c3473ec1483c3213d5b21eba)
#### Sunday 2022-04-03 19:36:21 by travisgamemaker

Fortnite battle pass. I just shit out my ass.

Booted up my PC, 'cause I need, need to get that Fortnite battle pass. I like Fortnite, did I mention Fortnite? I like Fortnite, it's night time. I mean it's five o' clock, that's basically night time. Y'all remember Cartoon Network, adventure time?

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b74bf3653e...](https://github.com/mrakgr/The-Spiral-Language/commit/b74bf3653ef5b7cc275c1dc938d9dbf76f84da11)
#### Sunday 2022-04-03 20:48:30 by Marko Grdinić

"10pm. Let me put in a bit extra. I really want to watch that shape manipulation video.

https://youtu.be/11GlyrYNbnA?t=187

What is gradient dynamic doing here. This is arcane work.

I guess Substance Designer will carve its own legend as an art software.

https://substance3d.adobe.com/documentation/sddoc/gradient-dynamic-172825217.html

> The Gradient (Dynamic) or Dynamic Gradient node remaps a grayscale input to a new grayscale or color ramp.

> It serves as a slight alternative to the Gradient Node, but unlike the Gradient node, Gradient color keys are not defined internally, but come from an external input. This mainly allows to avoid the problem where parameters cannot be exposed, as the parameters for color are moved outside of the node. This is what makes it "dynamic".

How does this work?

https://youtu.be/o8AtdW1oFC8?t=118

This really explains a lot. Still what do the different columns represent in the gradient input?

https://youtu.be/o8AtdW1oFC8?t=138

This tiling is exactly how I meant to do the wood texture. Well rather than tiling, I'd mirror the gradients so it is smooth on both sides.

https://substance3d.adobe.com/documentation/sddoc/gradient-dynamic-172825217.html

Ah, I see. You select the column or the row based on the third parameter which is the input position. I am too tired to think properly it seems.

https://substance3d.adobe.com/documentation/sddoc/color-burn-159450235.html
> Performs a Color Burn blend between Foreground and Background. Mathematically the formula is 1 - (1-Background) / Foreground.

So that is what the formula is!

https://substance3d.adobe.com/documentation/sddoc/color-dodge-159450239.html
> Performs a Color Dodge blend. Mathematically the formula is Background / (1-Foreground).

I've been trying to figure out what the blending modes do mathematically since forever. I finally found it here. Google was completely useless when it came to explaining them. It just does the equivalent of linking me to articles that say - this blend mode makes things darker, or this blend mode makes things lighter. What was I supposed to do with that?

https://substance3d.adobe.com/tutorials/courses/Designer-Quicktips/youtube-hIpTq8vZB9Q

Let me watch basic shape manipulation and then I am really done.

https://youtu.be/hIpTq8vZB9Q?t=94

Oh a direction blur is exactly what I need for the radial pattern. I want it to get elongated in the x axis the further it gets from the center.

10:30pm. https://80.lv/articles/discovering-the-curve-node-in-substance-designer/

The curve node is exactly what Shrimp showed me in his short video. I could use it to shape the circle manually.

Seeing his do his tricks really had a powerful impression on me. I really gained a lot just from watching those 10m of doing his magic.

Working in Designer is basically a whole new artform that has been invented in the 21st century. It is different from programming, the brain probably doing something closer to working in Designer than with regular programming.

This is what I've been missing. Doing the kinds of things done here is not something I would ever imagine doing in a regular language.

10:40pm. https://80.lv/articles/discovering-the-curve-node-in-substance-designer/

I'll leave this article for later. I can't be bothered to read it right now. Let me get back to Ayakashi."

---
## [Kylerace/tgstation](https://github.com/Kylerace/tgstation)@[55336d1e53...](https://github.com/Kylerace/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Sunday 2022-04-03 21:02:45 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [KellyWesterlund/ChessBoard](https://github.com/KellyWesterlund/ChessBoard)@[407789648a...](https://github.com/KellyWesterlund/ChessBoard/commit/407789648aec944396819db04cea08a171835454)
#### Sunday 2022-04-03 21:30:40 by Kelly Westerlund

Update README.md

While I decided to learn to code so I could advance my career, I have been learning a lot of personal lessons as I go on this journey too. I struggle a lot with anxiety, perfectionism, self-criticism, among other things. Its hard for me to start projects unless I know exactly what to do and that I will be successful, and I have a hard time finishing projects if I know they aren't absolutely perfect. I got stuck in that loop on this project particularly. I kept thinking of ways to make it better, and thinking myself in circles trying to figure out the "best" way to perform the task. I didn't want to post and move on from the project, until I thought of every single error that could arise if I actually had a use for this program. I've come to learn that nothing is ever "perfect." I am never going to write an idiot proof code, and there will always improvements that I can make. This is exciting, not scary, and it means I still have a lot to learn. This project represents a lot of growth for me and helped me change something that was anxiety-inducing into something that was enjoyable and energizing. I appreciate the mindful, problem-solving aspects of what I created, even if it isn't perfect, and look forward to applying the new things I will learn.

---
## [mszeles/a-humanisch-human-s-thoughtiesch-wordsisch-and-artisch-about-lifeisch-universeisch-and-everythingisc](https://github.com/mszeles/a-humanisch-human-s-thoughtiesch-wordsisch-and-artisch-about-lifeisch-universeisch-and-everythingisc)@[952cd5b31a...](https://github.com/mszeles/a-humanisch-human-s-thoughtiesch-wordsisch-and-artisch-about-lifeisch-universeisch-and-everythingisc/commit/952cd5b31af2b74b5d2fced081b65177f96da12f)
#### Sunday 2022-04-03 22:08:57 by MSzeles

Minnie: Miki! I think you forgot something.
Miki: Oh noooo. Is it Mywife's birthday again?
Minnie: No.
Miki: Is it Nikolai's birthday?
Minnie: Nopeisch.
Miki: Is it the day when our admiredisch governmentisch had been reelectedisch?
Minnie: Well, yes but I was thinking about something else.
Miki: What is that?
Minnie: Miki! You forgot to commit before you previous smoking break.
Miki: Go to hell, Minnie. Go to hell.
Nikolai: I love you, Miki. From my whole heart.
Minnie: 😤

---
## [Lattay/dwm](https://github.com/Lattay/dwm)@[67d76bdc68...](https://github.com/Lattay/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-04-03 22:48:27 by Chris Down

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
## [gitster/git](https://github.com/gitster/git)@[5cb28270a1...](https://github.com/gitster/git/commit/5cb28270a1ff94a0a23e67b479bbbec3bc993518)
#### Sunday 2022-04-03 23:03:00 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

An earlier version of this commit[3] went behind
opt_parse_list_objects_filter()'s back by faking up a "struct option"
before calling it. Let's avoid that and instead create a blessed API
for this pattern.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com
3. https://lore.kernel.org/git/patch-1.1-193534b0f07-20220325T121715Z-avarab@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [gitster/git](https://github.com/gitster/git)@[2c5501b986...](https://github.com/gitster/git/commit/2c5501b986c3e193064e9319485781494723292d)
#### Sunday 2022-04-03 23:03:00 by brian m. carlson

builtin/stash: provide a way to export stashes to a ref

A common user problem is how to sync in-progress work to another
machine.  Users currently must use some sort of transfer of the working
tree, which poses security risks and also necessarily causes the index
to become dirty.  The experience is suboptimal and frustrating for
users.

A reasonable idea is to use the stash for this purpose, but the stash is
stored in the reflog, not in a ref, and as such it cannot be pushed or
pulled.  This also means that it cannot be saved into a bundle or
preserved elsewhere, which is a problem when using throwaway development
environments.

Let's solve this problem by allowing the user to export the stash to a
ref (or, to just write it into the repository and print the hash, à la
git commit-tree).  Introduce git stash export, which writes a chain of
commits where the first parent is always a chain to the previous stash,
or to a single, empty commit (for the final item) and the second is the
stash commit normally written to the reflog.

Iterate over each stash from topmost to bottomost, looking up the data
for each one, and then create the chain from the single empty commit
back up in reverse order.  Generate a predictable empty commit so our
behavior is reproducible.  Create a useful commit message, preserving
the author and committer information, to help users identify stash
commits when viewing them as normal commits.

If the user has specified specific stashes they'd like to export
instead, use those instead of iterating over all of the stashes.

As part of this, specifically request quiet behavior when looking up the
OID for a revision because we will eventually hit a revision that
doesn't exist and we don't want to die when that occurs.

Signed-off-by: brian m. carlson <sandals@crustytoothpaste.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---

