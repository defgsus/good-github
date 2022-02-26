## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-25](docs/good-messages/2022/2022-02-25.md)


1,749,771 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,749,771 were push events containing 2,733,061 commit messages that amount to 203,865,120 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 22 messages:


## [CitrusGender/tgstation](https://github.com/CitrusGender/tgstation)@[7bead07444...](https://github.com/CitrusGender/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Friday 2022-02-25 02:17:01 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [absent-cc/backend](https://github.com/absent-cc/backend)@[775749b27c...](https://github.com/absent-cc/backend/commit/775749b27c2ee6616ea424d438b6560660362508)
#### Friday 2022-02-25 05:11:38 by Roshan Karim

fixed kevins retarded ass shit that he should have done himself but didn't because he couldn't read the code TWO LINES below it to figure out how things were done correctly my fucking god

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Friday 2022-02-25 05:12:00 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[472c367e89...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/472c367e89e5b684fc22ae2adb487662567ddf8e)
#### Friday 2022-02-25 05:59:11 by Angelo G. Del Regno

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

Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [ImFlynnn/android_kernel_realme_mt6785](https://github.com/ImFlynnn/android_kernel_realme_mt6785)@[aaf491597f...](https://github.com/ImFlynnn/android_kernel_realme_mt6785/commit/aaf491597f486966fe4bd4acae769e17b75b1921)
#### Friday 2022-02-25 07:41:55 by Wang Han

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

---
## [Le-Technologue/minishell](https://github.com/Le-Technologue/minishell)@[ec18f7a81c...](https://github.com/Le-Technologue/minishell/commit/ec18f7a81cc6fcbc3a0fc4b9d746dd730f1f2d44)
#### Friday 2022-02-25 12:38:31 by William Cazorla

Basic here docs exec parsing logic done...
... let's keep an eye on eventual edge cases.
  What's left to do :
- breaking the prompt loop on CTRL-D intercept and sending err msgr
  (also for all the fixed prompts).
- Double checking that we haven't left idiotic checks here and there
  (notably for my stupid idea of using # as a lexical token...) by
  renaming hdoc_eof.
- That stupidity aside, I'm really proud the trick I used to add HEREDOC
  to the lexicon in the end !
- Or placing it into the prb->curr node ? So far it seems my checks are
  pushing RDIR nodes well without prior initialisation but I may be
  wrong for some cases.
- close_node() and close_line() were streamlined as a result of this
  implementation.

---
## [frizbee19/FebGameJam](https://github.com/frizbee19/FebGameJam)@[9f4c4bba9a...](https://github.com/frizbee19/FebGameJam/commit/9f4c4bba9a310627ba140195e43a2a3ead402ed3)
#### Friday 2022-02-25 14:16:20 by MindfulMinun

Fucking i haven't slept all night and i got health and water spirits hell yeah

---
## [alphagov/govuk_publishing_components](https://github.com/alphagov/govuk_publishing_components)@[6e0eb5b830...](https://github.com/alphagov/govuk_publishing_components/commit/6e0eb5b830a4d8209ffb4ecb6049c6eba7b6acdd)
#### Friday 2022-02-25 14:33:40 by Kevin Dew

Clobber assets before running jasmine tests

I'm adding this in because we use globbing to match what files to test.
I'm concerned that without this we're at risk of the same files being
included multiple times (say you have application-1234.js, then edit it
and end up with application-2345.js)

It's a bit of a pain to do a clobber first as it means you'll always
have to experience the cost of compiling assets each test run, however
this is preferable to tests liable to fail.

---
## [PierStanislaoPaolucci/2019thalCort-SNN-SO-AW-mem](https://github.com/PierStanislaoPaolucci/2019thalCort-SNN-SO-AW-mem)@[c8764ec8ca...](https://github.com/PierStanislaoPaolucci/2019thalCort-SNN-SO-AW-mem/commit/c8764ec8cacfb937f0aecb1684b4f16727022ccd)
#### Friday 2022-02-25 14:43:45 by Pier Stanislao PAOLUCCI

Create LICENSE

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License
By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.

Section 1 – Definitions.

Adapted Material means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.
Adapter's License means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.
BY-NC-SA Compatible License means a license listed at creativecommons.org/compatiblelicenses, approved by Creative Commons as essentially the equivalent of this Public License.
Copyright and Similar Rights means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.
Effective Technological Measures means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.
Exceptions and Limitations means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.
License Elements means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution, NonCommercial, and ShareAlike.
Licensed Material means the artistic or literary work, database, or other material to which the Licensor applied this Public License.
Licensed Rights means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.
Licensor means the individual(s) or entity(ies) granting rights under this Public License.
NonCommercial means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.
Share means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.
Sui Generis Database Rights means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.
You means the individual or entity exercising the Licensed Rights under this Public License. Your has a corresponding meaning.
Section 2 – Scope.

License grant.
Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:
reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
produce, reproduce, and Share Adapted Material for NonCommercial purposes only.
Exceptions and Limitations. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.
Term. The term of this Public License is specified in Section 6(a).
Media and formats; technical modifications allowed. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.
Downstream recipients.
Offer from the Licensor – Licensed Material. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.
Additional offer from the Licensor – Adapted Material. Every recipient of Adapted Material from You automatically receives an offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.
No downstream restrictions. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.
No endorsement. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).
Other rights.

Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.
Patent and trademark rights are not licensed under this Public License.
To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.
Section 3 – License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the following conditions.

Attribution.

If You Share the Licensed Material (including in modified form), You must:

retain the following if it is supplied by the Licensor with the Licensed Material:
identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);
a copyright notice;
a notice that refers to this Public License;
a notice that refers to the disclaimer of warranties;
a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.
You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.
If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.
ShareAlike.
In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the following conditions also apply.

The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.
You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.
You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.
Section 4 – Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:

for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only;
if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section 3(b); and
You must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.
For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.
Section 5 – Disclaimer of Warranties and Limitation of Liability.

Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.
To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.
The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.
Section 6 – Term and Termination.

This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.
Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:

automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or
upon express reinstatement by the Licensor.
For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.
For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.
Sections 1, 5, 6, 7, and 8 survive termination of this Public License.
Section 7 – Other Terms and Conditions.

The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.
Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.
Section 8 – Interpretation.

For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.
To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.
No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.
Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.

---
## [roapsyme/kernel_xiaomi_vayu](https://github.com/roapsyme/kernel_xiaomi_vayu)@[cb5eedd44e...](https://github.com/roapsyme/kernel_xiaomi_vayu/commit/cb5eedd44edb8fcdfc44599cc23f5f3cfc77ba7b)
#### Friday 2022-02-25 15:30:21 by Yaroslav Furman

power: supply: force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>
Signed-off-by: Salllz <sal235222727@gmail.com>
Signed-off-by: roapsyme <camindcl@gmail.com>

---
## [cacogen/tgstation](https://github.com/cacogen/tgstation)@[906fb0682b...](https://github.com/cacogen/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Friday 2022-02-25 15:35:57 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[861bf808bc...](https://github.com/Zytolg/tgstation/commit/861bf808bc20d8544aaf7f30d40f0fcdb65b9c37)
#### Friday 2022-02-25 16:26:34 by LemonInTheDark

Fixes a few hard deletes and runtimes I either caused, or ran into when trying to fix hard deletes (#61953)

Please don't try and send chat messages if you have nothing to say
Fixes a spurious runtime.
Fixes a runtime caused by my lack of understanding of huds. remove_hud_from is intended for hud watchers, remove_from_hud is intended for hud items. Doesn't really make sense most of the time, and just runtimes out the ass
Fixes a runtime in shapeshifting, restore should not run if the object is not restoring, or if it's deleting. it should run if it's not restoring, and it's not deleted. 4head
Fun fact, if there's two turret control boards they'll override each other. Use weakrefs. Oh also removes a var called cp, nothing good will come of that
Today in: Good lord the stacking machine is an afront to god, we discover that the labor claims console was attempting to act as a console, which of course fails when it comes time to clear it's improperly named var. Disgusting
Attempts to fix potential wound ref hangs in surgeries? maybe?
Fixes a runtime in luminescent stuff I created in my big harddel crusade. owner is a mob, not a species
Fixes a runtime related to headspikes deleting themselves twice. Pain
Fixes hard deletes sourced from the prophet trauma. Good fucking lord this is awful
Offhand item is somehow hard deleting. I have no idea how. Here's hoping signals fixes it, because if it doesn't I'm stumped. It's not a common scenario, but it does happen in spurts that suggest repeated usage

---
## [Alex-Gberg/projet-erasmus](https://github.com/Alex-Gberg/projet-erasmus)@[87bed871b0...](https://github.com/Alex-Gberg/projet-erasmus/commit/87bed871b0689c46290a8201214e80ef2ac93777)
#### Friday 2022-02-25 16:41:06 by Youjinium

Issue #3: Try to find a way to overlay 2 images

Everything is working now. Serveral changes have been made, which I'll explain briefly below.

Looking in CrossOut.java. Line: 23 - 26.  The technique to overlay 2 images is by using the BlendMode method.
Line 23-26 creates a new Group called blend, which overlays the bottom and the top imageview.

Thing is when I tried to add the blend (object?) in the imageView Arraylist<ImageView> in Display.java, I get an error message due to the fact that the blend object is not an ImageViewObject.

So in order to avoid this problem, I changed the loadPics() method (Line 65 - 76) in Display.java. So instead of adding the ImageViews in an Arraylist<ImageView>, I immediately put the ImageViews into an HBox and stored them in an Arraylist<HBox> called imageViewsHBox. By doing this, I have no trouble to add the blend object into the Arraylist<HBox> imageViewsHBox.

Holy shit. I'm bad at writing hahah. I'll explain it to you once again in detail if you don't get my message above.

Anyway (Line 78 - 87), we save the paths of the images in a ArrayList<String>.
This is useful the crossOutPic() method (Line 101 - 105). First we look for the index of the ImageView to replace, then replace it using imageViewsHBox.set(index, crossOut.getLayout()); (Line 104)

For tesing purposes, look at Line 58-59. There we replace the Maria.png

---
## [StevenGaughran/python_learning](https://github.com/StevenGaughran/python_learning)@[e94c83a2d5...](https://github.com/StevenGaughran/python_learning/commit/e94c83a2d54d6cd2c6e902b370bb67de8abe9533)
#### Friday 2022-02-25 17:25:40 by StevenGaughran

Add files via upload

Day 25, and we made a US States Guessing Game using Turtle and Pandas.

Pandas is a weird plugin. Powerful? Yes. A bit unintuitive? Also yes.

The guessing game was actually one of three different projects we worked on today. This was a big lesson!

My big frustration from this lesson was self-inflicted. I actually wrote a perfectly functional line of code that didn't appear to do anything...because I needed to create another Turtle object to write things onto the screen. I felt like a colossal idiot when I realized what I had done, especially since I had spent not an insignificant amount of time trying to figure out what was going wrong!

Anyway, it works! Hooray!

---
## [thennal10/news-in-a-minute](https://github.com/thennal10/news-in-a-minute)@[89144c954f...](https://github.com/thennal10/news-in-a-minute/commit/89144c954f13ba73b57cf3285be5e662b15be14f)
#### Friday 2022-02-25 17:25:51 by thennal

Move scraper to subdirectory

Fuck you python imports

---
## [Petuuuhhh/pokemon-showdown-client](https://github.com/Petuuuhhh/pokemon-showdown-client)@[be9a95cbc6...](https://github.com/Petuuuhhh/pokemon-showdown-client/commit/be9a95cbc683c04c6ead95d5643c7ea551607a56)
#### Friday 2022-02-25 17:47:08 by Guangcong Luo

Fix bugs caused by Preact update

The new Preact version seems to have broken a lot of low-level
magic we used. We plausibly shouldn't be using such low-level magic
in the first place, but that's a conversation for another day.

In particular:

1. `preact.render` seems to replace all of `containerNode`'s contents
   if `replaceNode` isn't passed (previously, it would append a child).
   This is an insane thing to change without any documentation... Maybe
   I'm misunderstanding it?

2. Making a button value an uncontrolled form was a pretty big hack
   in the first place, but at least it worked. Now that it doesn't,
   we're giving up and switching to controlled forms, which makes the
   code a lot nicer, fixes a bug, and I should probably have just done
   in the first place.

---
## [Bliss-OS-Ayan/platform_frameworks_base](https://github.com/Bliss-OS-Ayan/platform_frameworks_base)@[f8f82a89de...](https://github.com/Bliss-OS-Ayan/platform_frameworks_base/commit/f8f82a89de6e7dc5d12b30b2ee6327f4661c82e7)
#### Friday 2022-02-25 18:18:33 by Joey Huab

core: Rework the Photos features blacklist again

* Apparently, Magic Eraser currently requires a
  specific Photos version for it to show up and
  actually work. (https://apkmirror.com/apk/google-inc/photos/photos-5-65-0-405472367-release/google-photos-5-65-0-405472367-10-android-apk-download)

* Basically, Magic Eraser feature will crash if
  Photos is spoofed as Pixel XL. We want to
  make Magic Eraser work by default as long as
  the Unlimited Photos spoof is turned off.

* However, when PIXEL_2021_EXPERIENCE feature
  is detected by the Photos app, it will use
  the TPU tflite delegate. So we need to
  blacklist it by default from the Photos app.

* TL;DR Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[1c491d02bf...](https://github.com/thoughtbot/hotwire-example-template/commit/1c491d02bff37030ca53a1026f9ec9b36b0b9a80)
#### Friday 2022-02-25 20:34:46 by Sean Doyle

Loading the Tooltip Asynchronously

Fortunately, optimizing these requests is really easy. All we need to do is add a `loading` attribute and have it set to `"lazy"` to [lazy-load][] the tooltips.

This means the request to the tooltip endpoint will be made only when the `<turbo-frame>` becomes visible in the viewport. This is because `loading="lazy"` is using the [Intersection Observer API][] [under the hood][].

```diff
 <!-- app/views/users/_user.html.erb -->
 <div id="<%= dom_id user %>" class="scaffold_record">
   <p>
     <strong>Name:</strong>
     <%= user.name %>
   </p>

   <p class="relative">
     <%= link_to "Show this user", user, class: "peer", aria: { describedby: dom_id(user, :tooltip) } %>
     <!--
       Right now we're hiding each frame and its children
       with the `hidden` class. We're revealing each frame
       and its children with the `peer-hover:block` class.
      -->
     <turbo-frame id="<%= dom_id user, :tooltip %>" target="_top" role="tooltip"
                  src="<%= user_tooltip_path(user, turbo_frame: dom_id(user, :tooltip)) %>"
                  class="hidden absolute translate-y-[-150%] z-10
                         peer-hover:block peer-focus:block hover:block focus-within:block"
+                 loading="lazy"
     >
       <!-- The tooltip will be added here. -->
     </turbo-frame>
   </p>
 </div>
```

If you go back to `http://localhost:3000/users` you'll notice that a network request is only made once you hover over the link.

![Hovering over each link loads the tooltip asynchronously](https://images.thoughtbot.com/blog-vellum-image-uploads/rVXa8PJ9Sq2u3G3WXTEZ_hw-2.gif)

Right now we're hiding each frame with the `hidden` class and then revealing it with the `peer-hover:block` class. Both of these classes are provided to us by [Tailwind][] and are a nice abstraction of the [general sibling combinator][]. Even though a `<turbo-frame>` may be in the viewport, the fact that it's not visible prevents the network request from being made. It's only when the `<turbo-frame>` is revealed via CSS that the request is made.

![The Tailwind classes used to abstract the general sibling combinator and reveal the tooltip](https://images.thoughtbot.com/blog-vellum-image-uploads/n8yQbPEhSrClaUTcZ1ve_hw-3.png)

In order to test this, try removing the `hidden` class from the `<turbo-frame>`. You'll notice the tooltips are still lazy-loaded, except this time they are loaded once they come into the viewport.

```diff
 <!-- app/views/users/_user.html.erb -->
 <div id="<%= dom_id user %>" class="scaffold_record">
   <p>
     <strong>Name:</strong>
     <%= user.name %>
   </p>

   <p class="relative">
     <%= link_to "Show this user", user, class: "peer", aria: { describedby: dom_id(user, :tooltip) } %>
     <!--
       Right now we're hiding each frame and its children
       with the `hidden` class. We're revealing each frame
       and its children with the `peer-hover:block` class.
      -->
     <turbo-frame id="<%= dom_id user, :tooltip %>" target="_top" role="tooltip"
                  src="<%= user_tooltip_path(user, turbo_frame: dom_id(user, :tooltip)) %>"
-                 class="hidden absolute translate-y-[-150%] z-10
+                 class="absolute translate-y-[-150%] z-10
                         peer-hover:block peer-focus:block hover:block focus-within:block"
                  loading="lazy"
     >
       <!-- The tooltip will be added here. -->
     </turbo-frame>
   </p>
 </div>
```

![Displaying the frame will load the tooltip once it's in the viewport.](https://images.thoughtbot.com/blog-vellum-image-uploads/dQLMVeagQjuj15wOIuAd_hw-4.gif)

[lazy-load]: https://turbo.hotwired.dev/reference/frames#lazy-loaded-frame
[Tailwind]: https://tailwindcss.com/
[general sibling combinator]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator
[Intersection Observer API]: https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API
[under the hood]: https://github.com/hotwired/turbo/blob/8bce5f17cd697716600d3b34836365ebcdc04b3f/src/observers/appearance_observer.ts
[aria-describedby]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby
[ARIA WAI specification for tooltips]: https://www.w3.org/TR/wai-aria-practices-1.1/#tooltip

<h2>Takeaways</h2>

There are two main takeaways from this simple demonstration that extend beyond Hotwire and Tailwind.

<h3>Lazy-load content when you can</h3>

There's a cost to each network request, and not all user's will be viewing your application on the latest hardware or on a stable internet connection. Consider lazy-loading content that's not critical to the initial page load, especially if that content is not in the viewport.

Turbo makes this easy with its `loading` attribute, but this is not a Turbo specific concept.

<h3>CSS can be leveraged to drive interactions</h3>

In our example we're able to reveal the tooltip by hovering over the tooltip's sibling. This may seem like the result of some magical property provided by Tailwind via the [peer class][], but in reality it's just the result of the [general sibling combinator][] (which has been around since Internet Explorer 7) in combination with [user action pseudo-classes][]. This is an incredibly powerful yet under utilized feature of CSS, and is often unnecessarily replicated with JavaScript.

Tailwind has exposed some of the most powerful features that CSS has to offer, but remember that they're just abstractions around existing CSS specifications.

[peer class]: https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-sibling-state
[general sibling combinator]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator
[user action pseudo-classes]: https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes#user_action_pseudo-classes

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[eb7138f178...](https://github.com/thoughtbot/hotwire-example-template/commit/eb7138f178812b74925d31de281f101c13a5698b)
#### Friday 2022-02-25 20:35:23 by Sean Doyle

Hiding the results when inactive

Now that we're overlaying our results on top of the rest of the page,
we'll only want to do so when the end-user is actively searching. We'll
also want to avoid needless requests to the server with empty query
text.

Lucky for us, browsers provide a built-in mechanism to prevent bad
`<form>` submissions and to surface a field's correctness: [Constraint
Validations][]!

In our case, there are two ways that a search can be invalid:

1. The query `<input>` element is completely blank.
2. The query `<input>` element has a value, but that value is comprised
   of entirely empty text characters.

To consider those states invalid, render the `<input>` with [required][]
and [pattern][] attributes:

```diff
--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
       <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results">
         <label for="search_query">Query</label>
-        <input id="search_query" name="query" type="search">
+        <input id="search_query" name="query" type="search" pattern=".*\w+.*" required>
```

By default, browsers will communicate a field's invalidity by
rendering a field-local tooltip message. While it's important to
minimize the number of invalid HTTP requests sent to our server, a
type-ahead search box works best when users can incrementally make
changes to the query string. In our case, a validation message could
disruptive or distract a user mid-search.

To have more control over the validation experience, we'll need to write
some JavaScript. Let's create
`app/javascript/controllers/form_controller.js` to serve as a [Stimulus
Controller][]:

```javascript
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
}
```

Next, we'll need to listen for browsers' built-in [invalid][] events to
fire. When they do, we'll route them to the `form` controller as a
[Stimulus Action][] named `hideValidationMessage`:

```diff
--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
     <header>
-      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results">
+      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results"
+        data-controller="form" data-action="invalid->form#hideValidationMessage:capture">
         <label for="search_query">Query</label>
```

One quirk of [invalid][] events is that they _do not_ [bubble up][]
through the [DOM][]. To account for that, our `form` controller will
need to act on them during the capture phase. Stimulus supports the
[`:capture` suffix][capture] as a directive to hint to our action
routing that the controller's action should be invoked during the
capture phase of the underlying event listener.

Once we're able to act upon the [invalid][] event, we'll want the
`form#hideValidationMessage` action to [prevent the default behavior][]
to stop the browser from rendering the validation message.

```diff
--- a/app/javascript/controllers/form_controller.js
+++ b/app/javascript/controllers/form_controller.js
 import { Controller } from "@hotwired/stimulus"

 export default class extends Controller {
+  hideValidationMessage(event) {
+    event.stopPropagation()
+    event.preventDefault()
+  }
 }
```

When an ancestor `<form>` element contains fields that are invalid, it
will match the [:invalid][] pseudo-selector. By rendering the search
results `<turbo-frame>` element as a [direct sibling][] to the `<form>`
element, we can incorporate the `:invalid` state into the sibling
element's style, and hide it.

```diff
--- a/app/assets/stylesheets/application.css
+++ b/app/assets/stylesheets/application.css
*= require_tree .
*= require_self
*/
+
+.empty\:hidden:empty                                { display: none; }
+.peer:invalid ~ .peer-invalid\:hidden               { display: none; }

--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
    <header>
-      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results"
+      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results" class="peer"
        data-controller="form" data-action="invalid->form#hideValidationMessage:capture">
        <label for="search_query">Query</label>

--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
-      <turbo-frame id="search_results" target="_top"></turbo-frame>
+      <turbo-frame id="search_results" target="_top" class="empty:hidden peer-invalid:hidden"></turbo-frame>
    </header>
```

[Constraint Validations]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation
[required]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/required
[pattern]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern
[invalid]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/invalid_event
[capture]: https://stimulus.hotwire.dev/reference/actions#options
[Stimulus Controller]: https://stimulus.hotwire.dev/handbook/hello-stimulus#controllers-bring-html-to-life
[Stimulus Action]: https://stimulus.hotwire.dev/handbook/building-something-real#connecting-the-action
[bubble up]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Bubbling_and_capturing_explained
[DOM]: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
[prevent the default behavior]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#preventing_default_behavior
[:invalid]: https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid
[Tailwind CSS]: https://tailwindcss.com/
[variant]: https://tailwindcss.com/docs/hover-focus-and-other-states
[direct sibling]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[06f0807bf6...](https://github.com/mrakgr/The-Spiral-Language/commit/06f0807bf6f8eaf1dad3abd9d80a22cb09e2015a)
#### Friday 2022-02-25 20:55:14 by Marko Grdinić

"10:45am. Let me chill and then I will get started.

11:10am. Let me start. First of all, let me do some playing around on my own. I had the time to think about my questions more in depth. I just do not understand why they insist that density is between [0,1) when in actuality it can be above and even negative. The description in the docs make zero sense.

Yesterday I said that filling the interior did not increase memory consumption as much as I expected, but consider the case of a box 1x1x1 in dimensions. If the voxel size is 0.01, that means one of the face is 100*100 voxels wide. 10k. If the interior is not filled that means to cover the box in voxels, all that is needed is to put a film of them on all the faces. So 10k*6.

If the interior is fulled, that would instead be multiplied by the side. So 10k*100. So the fact that my memory consumption increased only by 16 times is in fact inline with my napkin calculations.

11:15am. The reason VDB is efficient because it leaves out the interior and considers only surfaces. But it is still a n^2 representation while the interior is n^3. Both have poor scaling properties.

Now, what happens if you have an unfilled interior and want to change the density?

11:20am. Surprinsgly it is possible, but it is less sensitive for small amplitudes.

11:25am. Ok, I think I get it. Let me check out the example file.

Yes, I think that the internal parts are represented using tiles...which I am guessing are just bigger voxels.

Let me ask the author to update the file as I am getting a wall of errors.

https://www.sidefx.com/forum/topic/67110/?page=1#post-286853

Here is the post.

https://www.tokeru.com/cgwiki/index.php?title=HoudiniVolumes

Lot of info here. For now let me see how far I can get into the example file.

11:40am. Ah, I see. I think the previous version of Houdini had VDB Densify and VDB Prune. In the file they've been replaced by merge nodes as a fallback.

11:55am. > This can be handy for many things. If you have a robust way to generate a SDF (which of course we do in Houdini), it's a great way to generate collision geometry for simulations. Particles or RBD objects can very quickly sample the SDF, if their sign is negative, they're inside the shape. They can then measure the gradient of the SDF, and determine exactly how far and how much to be pushed to stop intersecting.

Ah, I see.

Also this explains why the inner band.

12am. Maybe if I want to do fast colission detection for those wines vs the frame, I could convert to VDB first and find a way to do that operation there?

1pm. Enough of this for now. This is a very long example file. Time for breakfast and chores. I'll finish the extended chores today and will be able to get back to the usual routine tomorrow.

2pm. I chill'd. Let me do the chores.

3:25pm. I am back. Let me chill a bit. I meant to work on clearing the old wall more, but the weather started to turn rainy. I guess I'll finish it tomorrow or in the next two days.

4:05pm. Let me start. I'll leave Cultivator vs Superhero for later.

Let me study those volume example for a while longer.

4:10pm. No these are too boring. Let me go back to the rock video. I'll try skimming tihs time. After that I'll just do my own thing.

4:40pm. Had to take a break again. I pretty much wasted the last hour. These extended chores kill my momentum. Let me just focus on the video. Forget the fact that I do not need it. Let me watch it and I will move on.

4:45pm. https://youtu.be/WTg_pVZoac0?t=5989

I really dislike his technique. A strong technique would start from the big features and add progressively lower level of detail. This guy feels like he is jumping all over the place with the places he adds noise to.

https://youtu.be/WTg_pVZoac0?t=6094

Let me pause here. This is useless to me. Let me check out how Rohan did clouds. I am thinking about my own method, but if it is merely for controling the density a coarse fog would not be bad.

5:15pm. This is so annoying. Why am I getting such strange results in the inner and outer bands?

5:20pm. For some reason the exterior band option for fog volume does not work.

I just wanted to check if the exterior band auto expands when reshaped. It does not. Volumes have a strict bounding box around them.

5:30pm. I did not realize he built the scaler for the fog density himself. There is a relative to bounding box node.

5:35pm. You can access positions relative to the bounding box with BBX, BBY and BBZ.

This vop node even gets the relative position of a bounding box based on a group.

This is important. Working relative to bounding boxes is something I need to keep in mind.

The way he implemented procedural gradients here is brilliant.

5:45pm. The way he did the cloud is quite different from how the rock guy does it. He mostly used cloud nodes and did not mess with VOPs much. Still this does give me an option.

5:35pm. I thought that Scatter would accept the volume density, but it does not.

https://youtu.be/aOisEGCA3zk
Houdini - How to scatter points inside a volume or on a surface

I must be going crazy.

6:10pm. Scatter can scatter points inside a volume, but it won't accept the density attribute.

Oh, no wait. It does that automatically.

6:40pm. Had to leave for lunch.

https://youtu.be/FU0DM84UGxQ
The Legend of Ghost Corgi - Part II - Volume Adjust Fog - Houdini 19

Sure Rohan showed me how to do the gradient ramp for the density, but there should be better ways. This is such a simple thing, but this particular SOP has been giving me a lot of trouble. I can't intuit how it works. Let me watch something on it.

6:45pm. Nevermind, I finally figured out how the line pattern works. This is wonderful. A lot better than having to implement the VOP.

The Bounding Box pattern type is exactly what is needed to implement the gradient. This is good. I can also try a radial gradient.

6:55pm. Perfect! The radial gradient is exactly what I've been looking for.

I really get it now. With this I should be able to carve away volume In ways that I see fit. I can take that big box, adjust it, turn it into volume, maybe even using the Cloud node since that takes in a flat division number and is scale insensitive, and then use Adjust fog to give it some gradient at the top and a radial reduction from the middle. I'll want to push the density towards the surface and away from the top.

7pm. Let me watch the Ghost Corgi video.

https://youtu.be/FU0DM84UGxQ?t=158

This is the kind of thing amateur programmers do - he could have just put in `max(@corgi,0)`. That would have saved him having to put in the upper range.

https://youtu.be/FU0DM84UGxQ?t=204

I am confused, why is he getting an outline? Is that a property of the noise function like Voroni distance to edge in Blender.

https://youtu.be/FU0DM84UGxQ?t=52

Ah, he has a special attribute. I am not sure what it is.

https://youtu.be/FU0DM84UGxQ?t=668

It seems this node only came in in Houdini 19. No wonder Rohan was making a ramp.

https://youtu.be/FU0DM84UGxQ?t=740

Oh wow, you can do it like this.

7:30pm. Ok, I got this far. Let me watch the rock tutorial and then I'll close at 8pn. I am satisfied with how well I know volumes now. I can make use of them to scatter point without problem.

Today I do not feel like going at it till 10pm. This kind of pace is not sustainable. Tomorrow I will definitely get back to my own project. I'll scatter those tiles without a hitch.

7:55pm. https://youtu.be/WTg_pVZoac0?t=6274

Instead of doing it like he has here, he could have instead copied the volumes to points (packed) and did an a foreach fold. I actually don't know how to use the for loop to do a fold just yet, but it should be doable. I'd have to fiddle around in order to figure it out. To combine he just needs to use the max operation.

8pm. I've been wondering what the second input to foreach is. Maybe that would solve the mystery of the input being different from what I need to iterate over.

8:10pm. > A loop can have more than one Block Begin node. So, for example, one branch of the network will get its input piecewise and another branch will be simple repetition accumulating the result of using the pieces.

Ohhh, I see.

8:40pm. I've figured it out. I completely understand how loops work in Houdini now. The second input can just be substituted with the piece block path param. It is no big deal.

This should be useful.

Every day that passes, Houdini seems less mystical.

Let me watch more of the rock tutorial. I'll try going till the 2h mark.

https://youtu.be/WTg_pVZoac0?t=6285

Look at this shit. The For loop documentation literally tells him how to do this more efficiently.

https://youtu.be/WTg_pVZoac0?t=6554

This is quite nice. Yeah, this is how I expected this would work.

8:55pm. https://youtu.be/WTg_pVZoac0?t=6715

This is a good idea. Taking the dot product with an upvector to get the color.

9:15pm. https://youtu.be/WTg_pVZoac0?t=7364

Let me watch the edge displacement part as well. I wonder if he will just resample the edges and then push them in the normal direction?

https://youtu.be/WTg_pVZoac0?t=7604

For once I actually anticipated what he would do. Using the cross product to get the 3 axes is a great idea.

9:30pm. If I wanted to deform just the edges, and Resample SOP did not work, I'd use the edges to create a mask and move the points depending on it. That would allow me to have a smooth surface.

https://youtu.be/WTg_pVZoac0?t=8055
Free Masterclass: Developing Complex Details Using Volumes in Houdini

Let me stop here. Since I've come this far, maybe I should finish tihs long tutorial. I am learning quite a bit.

I feel that learning about the cross product last week was like gaining a superpower. Yeah, learned about it in school, but it was useless there so I forgot all about it. But here it is quite useful!

9:35pm. I think that originally, way back in elementary school, really internalizing various concepts, like I've done today with the loop and the fog adjust node for example, is what kept me going all the way to that championship win.

What I am doing now has roots in my Logo programming. I wasn't always a functional programming junkie.

I guess it was inevitable that I would return to the path that would first bring me success. I never thought that something like Houdini existed. Nor that I would actually be seriously studying it, while leaving ML to the side. If I live long enough, I'll have my rematch with both trading and ML.

I need to accumulate a critical mass of art skill in order to be able to move other people's hearts, purely for the sake of enriching myself.

Normies always make a big deal about socializing. As if it is a big to toe the NPC line. The autism's answer to that is art.

The closer it gets to the essence of mind control, the better.

The more I draw upon the power of technology to empower myself, the better.

If I could just a machine into my brain to draw out my imagination directly, I sure would do that.

For the time being my hands will have to be the conduit for my desire, just as they have been."

---
## [ck2plus/CleanSlate](https://github.com/ck2plus/CleanSlate)@[2c02e01a37...](https://github.com/ck2plus/CleanSlate/commit/2c02e01a37790f62f4d5225ed4320e172d6de4fc)
#### Friday 2022-02-25 23:22:32 by SuccinctScrivener

Events DeMTTHed

Almost all MTTH events that aren't achievement, plot, health, job, or province events have been edited to no longer use MTTH.

base_achievement_events.txt
Potentially fixed issue with flags not getting cleared in steam.026 (CleanSlate error)

base_crusade_events.txt
Some Catholic-only crusade events expanded to include Fraticelli

base_family_events.txt
Relatives who marry in event 37056 'Relative who was denied marriage ambition decides to marry in secret' now marry matrilineally if female

base_hedge_knights_events.txt
All five of the 'hedge knights visiting' events may fire now, rather than just the one where they injure themselves

base_legends_events.txt
Changing your mind about how you want to close the gates of hell no longer terminates the event chain

base_lifestyle_events.txt
Improved the selection of an appropriate love interest in event 5030 'Duelist/Poet - start'.
Fixed event 5035 'Write poems for your love interest' taking ~7 times longer to fire than it should.
Fixed the event chain to become a faqih taking ~7 times longer to complete than it should.
Fixed characters getting permanently locked out of lifestyle trait event chains when they fail a non-muslim lifestyle event chain.
Fixed event 5064 'Stay strong in the face of temptation' not firing for buddhists with the ambition to rid themselves of lustful unless they are also in the middle of a lifestyle event chain.
Fixed event 5064 'Stay strong in the face of temptation' taking 5 times as long to fire if you were in the hedonism/celibacy lifestyle event chain but also had the buddhist ambition to rid yourself of lustful.

base_lovers_events.txt & wol_lover_events.txt
Fixed events that were supposed to cause a character to break up with a particular lover not causing them to break up at all or to break up with a different lover.
Fixed a bad condition preventing event 64100 'lover comforts you after row with wife' from ever firing.

base_mongol_events.txt
Random turkic invasions now actually random

base_religious_events.txt
A number of religious events can now be performed by antipopes as well as popes
Restored option for Catholics to banish heathen advisors in response to papal pressure in event 39241, like in the Orthodox version of the event
Event 39401, 'Pope disappointed about allowing heresy', now actually waits at least 2 years to fire, as indicated by the description

base_teutonic_order_events.txt
Choosing to not donate land to the Teutonic Order at the moment no longer permanently prevents the Teutonic Order from asking for land.

base_traits_effects_events.txt
Fixed a bad condition on event 3520 'Break celibacy for your spouse' that prevented it from ever firing

hl_raiding_adventurers_events.txt
Fixed HL.100, 'Character without inheritance becomes adventurer', firing only 15% as often as in vanilla (CleanSlate error)

soi_hashshashin_order_events.txt
The Hashshashin 'kill a ruler who is at war with them' event, event 88020, can now fire for the ai, as was probably intended.

soi_muslim_honorary_titles_events.txt
Iddah period before divorce corrected from 30 days to 130 days
Fixed cooldown being added to the wrong character in event 105050 'Court Calligrapher is asked to decorate the mosque'
Lovers breaking up in the zina event chain now takes into account the Way of Life DLC
Zina event chain can no longer fire more than once at a time for a character.

soi_on_hajj.txt
promise_hajj flag now cleared from characters when asked to go on hajj by another character

soi_polygamy_events.txt
Only playable characters or their spouses will now receive most polygamy events
Most polygamy events opened up to characters of non-muslim religions with polygamy

---
## [cfmnephrite/Pokemon-Showdown](https://github.com/cfmnephrite/Pokemon-Showdown)@[1335c3b843...](https://github.com/cfmnephrite/Pokemon-Showdown/commit/1335c3b84384a8a1536cd8bc4fb418be11f3411b)
#### Friday 2022-02-25 23:38:22 by Nephrite

Fixes to commands + "fiElD sTaRT"

Fuck you, Zarel

---

