## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-04](docs/good-messages/2022/2022-07-04.md)


1,791,536 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,791,536 were push events containing 2,536,861 commit messages that amount to 198,940,027 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [kernelci/linux](https://github.com/kernelci/linux)@[4a557a5d1a...](https://github.com/kernelci/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Monday 2022-07-04 00:02:17 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [ExWaltz/dwm](https://github.com/ExWaltz/dwm)@[67d76bdc68...](https://github.com/ExWaltz/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-07-04 00:16:52 by Chris Down

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
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[2996f41136...](https://github.com/Koshenko/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Monday 2022-07-04 01:08:20 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [Myth1calCode/Reaction-ReactOS-PE-Environment](https://github.com/Myth1calCode/Reaction-ReactOS-PE-Environment)@[4471ee4dfa...](https://github.com/Myth1calCode/Reaction-ReactOS-PE-Environment/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Monday 2022-07-04 01:30:31 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [peff/git](https://github.com/peff/git)@[5f61e39cbf...](https://github.com/peff/git/commit/5f61e39cbffd42f7db4d7a5c948bccf6cb35c851)
#### Monday 2022-07-04 01:39:19 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[945e900cc4...](https://github.com/peff/git/commit/945e900cc432be641a89d37681ef16a838b93f1f)
#### Monday 2022-07-04 01:39:30 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [PJzer0/terminal](https://github.com/PJzer0/terminal)@[9ccd6ecd74...](https://github.com/PJzer0/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2022-07-04 02:23:35 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [Provenance-Emu/duckstation](https://github.com/Provenance-Emu/duckstation)@[f9212363d3...](https://github.com/Provenance-Emu/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Monday 2022-07-04 02:30:54 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [skepfusky/skepfusky.xyz](https://github.com/skepfusky/skepfusky.xyz)@[94d5606619...](https://github.com/skepfusky/skepfusky.xyz/commit/94d560661976437fbeaedadaa73d64a86f2c0c4e)
#### Monday 2022-07-04 04:23:06 by Kerby Keith Aquino

I like eating raw butter (#9)

* yes

Added Stapi CMS to project

* crazy for myself

* bruh

Added buttons and cards boye

* make it scroll damn it

* Minor tweaks

* projects stuff still in de works

* Minor config changes

* Added strapi shit

* Added projects

* TBA notice

---
## [Hurricos/realtek-poe](https://github.com/Hurricos/realtek-poe)@[7c89bd1df1...](https://github.com/Hurricos/realtek-poe/commit/7c89bd1df12a740f3c783fa823f16f2eaa1f1dac)
#### Monday 2022-07-04 04:39:21 by Alexandru Gagniuc

realtek-poe: Fix memory leak in poe_reply_consume()

When thinking "embedded", it's a good idea to stay the fuck away from
malloc(). Falling out of scope is a free garbage collector. Port
config and state arrays followed this advice, but for some reason, the
command queue did not.

No worries, free() is used in poe_reply_consume(). No problemo! Crisis
averted! Did you spot the several failure modes which return before
the free() call. In these modes, a malloc()d command is taken off the
queue, and not free()d. The pointer falls out of scope and memory lost.
Quod Erat Demonstratum.

To fix this, free() the command before hitting any exit paths.

Signed-off-by: Alexandru Gagniuc <mr.nuke.me@gmail.com>

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[0012f28256...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/0012f28256f7f03b350adc4f6e816d0d9c298386)
#### Monday 2022-07-04 05:22:48 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

ASSESSMENT-REQUEST

Thank you!

-------- Forwarded Message --------
Subject: 	**** TAX ASSESSMENT - for 144 properties, by their representatives.
Date: 	Mon, 4 Jul 2022 00:18:16 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>, KINGS COUNTY TAX MATTERS <TaxEfiled@law.nyc.gov>, edi.civil.rights.division@irs.gov <edi.civil.rights.division@irs.gov>, gssceboard@columbia.edu, Stephen O'Connell <sgo2107@columbia.edu>, Amber Griffiths <ag2943@columbia.edu>, Dean's Discipline - SCCS <conduct-admin@columbia.edu>, Columbia EMOT Alert <00000121e5ec70a4-dmarc-request@lists.columbia.edu>, emot@columbia.edu, QUEUED <askcuit@columbia.edu>, Yana Siegel <yana.siegel@wilsonelser.com>, WILLIAM BEHR <william.behr@wilsonelser.com>, Urvashi Sinha <urvashi.sinha@wilsonelser.com>, Thomas R. Manisero <thomas.manisero@wilsonelser.com>, Suzanne S. Swanson <suzanne.swanson@wilsonelser.com>, Stephen J. Barrett <stephen.barrett@wilsonelser.com>, Stacey L. Seltzer <stacey.seltzer@wilsonelser.com>, Sean Wagner <sean.wagner@wilsonelser.com>, Roger R. Gottilla <roger.gottilla@wilsonelser.com>, Ricki Roer <ricki.roer@wilsonelser.com>, Ricki Roer <ricki.roer@wilsonanddicker.com>, ricki.raared@wilsonsdickers.com <ricki.raared@wilsonsdickers.com>, patricia.wik@wilsonelser.com, meghan.rigney@wilsonelser.com, Lori Semlies <lori.semlies@wilsonelser.com>, Lois K. Ottombrino <lois.ottombrino@wilsonelser.com>, Lauren M. Zink <lauren.zink@wilsonelser.com>, Kathleen A. Mullins <kathleen.mullins@wilsonelser.com>, judy.selmeci@wilsonelser.com, Jennifer L. Sciales <jennifer.sciales@wilsonelser.com>, Jennifer M. Provost <jennifer.provost@wilsonelser.com>, info@wilsonelser.com, Hannah.King@WILSONELSER.COM, grace.song@wilsonelser.com, erin.zecca@wilsonelser.com, ellyn.wilder@wilsonelser.com, elizabeth.scoditti@wilsonelser.com, Debra Tama <debra.tama@wilsonelser.com>, Daniel F. Flores <daniel.flores@wilsonelser.com>, curt.schlom@wilsonelser.com, craig.hunter@wilsonelser.com, craig.brinker@wilsonelser.com, Corrine Shea <corrine.shea@wilsonelser.com>, carole.nimaroff@wilsonelser.com, aviva.stein@wilsonelser.com, Ashley V. Humphries <ashley.humphries@wilsonelser.com>, Angelique Sabia-Candero <angelique.sabia-candero@wilsonelser.com>, angel.vitiello@wilsonelser.com, Andrea Shiffman <andrea.shiffman@wilsonelser.com>, Amy Hanrahan <amy.hanrahan@wilsonelser.com>, alex.kress@wilsonelser.com, Alan Rubin <alan.rubin@wilsonelser.com>, aguirguis@schools.nyc.gov <aguirguis@schools.nyc.gov>
CC: 	info@kpmg.com <info@kpmg.com>, LORI SCHOCK <CHAIR@SEC.GOV>,REDACTED


Gov. Hochul,

*** THIS WILL WORK ***

-- I took the Wilson and Dicker firm off the email thread. and only left the Zuckers and counselors of Columbia that they spoke with during the proceedings in NYSCEF 153974/2020.

https://www1.nyc.gov/assets/law/downloads/pdf/Real%20Property%20Tax%20Audit%20Report%20Form%20(4-2013).pdf

They don't need to share their results with me... their interests are all safe with you Gov. Hochul, and your third party review team (which should be two audit firms that are NOT affiliated) with any of these affairs


- try standard chartered and maybe another one, and then have them cross-reference with your Comptroller (who i met earlier by the way, not the new one though) the old guy at Bobby Vans.

I have no say in the TIME LIMIT to INDEPENDENTLY QUALIFY this as a proper way to identify variations observed in their assessments of VALUE in those property taxes for the 144 units and 6 respective buildings - filed and reported with the DFS to obtain a $6 million dollar loan from state farm... but

I think ONE FORM for each unit is the best way AND NOT TO BE SADISTIC, HONESTLY

- but that way it's easier to analyze variations by unit and by each person.
- Especially since they already failed to even bring light to the fact that it is IMPOSSIBLE to have them qualified as "LAWFUL RENTAL PROPERTIES"  without a certificate of occupancy

--- if you don't do it that way... it will be difficult to find the criminals among the group of participants that circulated those un-consented videos of myself...
--- If you want to figure it out, those 144 reports will prove who/who did not participate in the violation of my privacy.

If you do it one unit per form, they file 144 forms and unlawfully represent those interests 144 times...  they cannot argue any further that they made a fat finger mistake

- it will be very easy to understand who did and didn't understand what is going on, and who was and wasn't responsible for being an accessory to tax evasion as represented in the dockets in NYSCEF 153974/2020.

FOR A 24 hour WINDOW OF OPPORTUNITY - just like that STFGX move on Dec 22, 2021 --- If the onus was on me I would get it done like now.

--- all I care about is the 144 units, and they should INDEPENDENTLY fill out the form to see if they are all in sync.  or if there a variation in the majority opinion...

plus, it's only 17 pages... per unit.

I understand... paperwork can be annoying sometimes, but if these Wilson & Elser lawyers and the others that represented the interests of the Sullivan Properties LP as directors take the time to each assess those properties, it will take much less time to figure out who is guilty and put a stop to any furtherance of these continuing crimes.


How long can it take for all of them to complete this in light of the damages registered and gross negligence of the carried interest over a period of 10 years that I know about. (5) This is required by police officers for each traffic violation or even for an expired registration, they can't just group up chevrolet violations as one ticket - its each license plate - so I mean it's only fair that they report it for each unit --- in case they make 144 mistakes in a row - you'll know they are guilty.

Without a CO they can't be qualified as buildings with X number of units as "rental units" that generate income... So for the 144 units, each having an address--- do you think their numbers will all match up - or differ based on opinion?

I just used the base cap rate, using the table of all owners to make my assessment

- the one I posted them with earlier...

#GOCARDS.

/s/ BO DINCER.

Hey if you want to get serious and have a REAL opinion... get serious and wake the heck up-- it's problem, not yours. - but give them a time limit on when to submit those forms, that's more money than they can all make COMBINED in a year in tax-evasion, it was up in the $500 million range in 2020, so...

as the fed-30 RATE MOVES HIGHER, THEY ACTUALLY GET TAXED MORE ON THE COMPOUND DAILY INTEREST FOR THE TWO YEARS OF AVOIDANCE AND IBSTRUCTION IN THE PRIOR...

---- plus they're going to have way more issues by the time I am done watching this movie here instead

    https://www.sc.com/en/about/fighting-financial-crime/fighting-fraud/
    https://av.sc.com/corp-en/content/docs/code-of-conduct.pdf
    https://www.sc.com/en/contact-us/#reporting

i left one confidant, in the BCC from Columbia, only because he will respect me for this method, if he has an objection, or a suggestion he will contact you directly.

thank you.
On 7/3/2022 11:13 PM, B D2022 wrote:
>
> I hope you all enjoyed your weekends!
>
> https://www1.nyc.gov/assets/law/downloads/pdf/Real%20Property%20Tax%20Audit%20Report%20Form%20(4-2013).pdf
>
>
>
> https://www1.nyc.gov/assets/law/downloads/pdf/NYC_False_Claims_Act.pdf
>
> https://www1.nyc.gov/assets/law/downloads/pdf/false2.pdf

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[0175be7c60...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/0175be7c608a1bad67a39a9095fad99b8909eb70)
#### Monday 2022-07-04 05:42:20 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

ny supreme court matter 153974-2020

HERE IS A SHORT-LIST OF MEMBERS AND INTERESTS OF SULLIVAN PROPERTIES LP
-- IN NYSCEF 153974/2020
-- CONFIRMATIONS FILED.

-------- Forwarded Message --------
Subject: 	Fwd: 251295/2021 thru 251334/2021
Date: 	Fri, 1 Jul 2022 22:43:00 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	+15163667582@tmomail.net, +1-347-880-1899 <+13478801899@tmomail.net>,
administration@mskyline.com <ADMINISTRATION@MSKYLINE.COM>, administrator@mskyline.com <administrator@mskyline.com>, 
AREYNOSO@mskyline.com <AREYNOSO@mskyline.com>, askLaurie@mskyline.com <askLaurie@mskyline.com>, cbloom@mskyline.com, DZUCKER@MSKYLINE.COM <DZUCKER@MSKYLINE.COM>, 
EDevine@mskyline.com, jgiamboi@mskyline.com <jgiamboi@mskyline.com>, joseph.giamboi@brooklaw.edu <joseph.giamboi@brooklaw.edu>, 
LBRITTON@MSKYLINE.COM <LBRITTON@MSKYLINE.COM>, leftbank@mskylinerentals.com <leftbank@mskylinerentals.com>, Paul Regan <legal@mskyline.com>, 
legalasst@mskyline.com <legalasst@mskyline.com>, lzucker@mskyline.com <lzucker@mskyline.com>, MGMTADMIN@mskyline.com <MGMTADMIN@mskyline.com>, 
MVredjian@mskyline.com, pregan@mskyline.com <PREGAN@MSKYLINE.COM>, slaskowitz@mskyline.com <slaskowitz@mskyline.com>, SHIKENA MELTON <smelton@mskyline.com>, 
SULLIVANMEWS@MSKYLINERENTALS.COM, Super@sullivanmews.com <Super@sullivanmews.com>, TEschmann@mskyline.com, +15163224896@tmomail.net, 
FILER 400842/2020 <isaac@shermantax.com>, Stephen O'Connell <sgo2107@columbia.edu>, Amber Griffiths <ag2943@columbia.edu>,
Marlyn Delva <mmt22@columbia.edu>, Alan J. Morrison <ajm157@columbia.edu>, wmckenzi@nycourts.gov <wmckenzi@nycourts.gov>


good look collecting that $600,000.00-
if any of the other 14 didn't get approved, you better that money and bring it back before I find out.

-------- Forwarded Message --------
Subject: 	251295/2021 thru 251334/2021
Date: 	Fri, 1 Jul 2022 04:04:35 -0400
From: 	Bo Dincer <bdincer66@icloud.com>
To: 	edi.civil.rights.division@irs.gov, eca_press@state.gov, JPMCinvestorrelations@jpmchase.com, TEschmann@mskyline.com, general.info@ny.frb.org, 23pctyco@nypd.org, DCAOLetters@sec.gov, cbrooks7@bloomberg.net, citimod1@bloomberg.net, iceglobalnetwork-info@ice.com, ksaperstein2@bloomberg.net, mshy2@bloomberg.net, 10pctdvo@nypd.org, 10pctyco@nypd.org, 18PCTDVO@nypd.org, 18pctyco@nypd.org, 1pctdvo@nypd.org, 1pctyco@nypd.org, Bloomberg L.P. <bbrief@bloomberg.net>, 23pctdvo@nypd.com, Newyork <newyork@sec.gov>, Tennesse <sbarchenger@tennessean.com>, Chair <chair@sec.gov>, MSKYLINE <ANNE@thehighlandpartners.com>, Work <cockarens@vouchersrus.org>, BD <bondstrt@protonmail.com>, BBO 121 <ms60710444266@yahoo.com>, susan.olsen@us.pwc.com, dallas-reserve-mgmt@dal.frb.org, dion.gaspard@nypd.org, legalASSt@mskyline.com, ofac_feedback@treasury.gov, rebecca.coyle@statefarm.com, blaw.content@bloomberg.net, colin.brooks@morganstanley.com, tips@insider.com, asksipc@sipc.gov, jpetit@mccarter.com, premerger@ftc.gov, blawre@bloomberg.net, KEN 00040govtIdx FRASER <kenneth.j.fraser@frb.gov>, bofamarkets@baml.com, mshyld@bloomberg.net, tips@vibe.com, lzucker@mskyline.com, icehelpdesk@ice.com, help@vogue.com, press@barrons.com, tips@latimes.com, ZUCKER ORGANIZATION <jgiamboi@mskyline.com>, Alan Rubin <alan.rubin@wilsonelser.com>, Amy Hanrahan <amy.hanrahan@wilsonelser.com>, B Dincer <bdincer1768@bloomberg.net>, BO DINCER <bo.dincer@yahoo.com>, Bd Dincer <bdincer211@bloomberg.net>, Bressler Info <INFO@bressler.com>, Brooklyn Tap House <tips@nypost.com>, Debra Tama <debra.tama@wilsonelser.com>, Dow Jones <pronewsletter@dowjones.com>, FINRA Corporate Notification <finracorporatenotification@finra.org>, Goldman Sachs <briefings@gs.com>, JAMES GORMAN <james.gorman@morganstanley.com>, Joseph Giamboi <joseph.giamboi@brooklaw.edu>, KEVIN ROCK <krock5@bloomberg.net>, LA TIMES NEWSLETTERS <NEWSLETTERS@latimes.com>, Lee Bollinger <bollinger@columbia.edu>, Lee Bollinger <officeofthepresident@columbia.edu>, Lori Semlies <lori.semlies@wilsonelser.com>, Shari Laskowitz <slaskowitz@ingramllp.com>, Stephen O'Connell <sgo2107@adcu.columbia.edu>, UNITED ARTISTS MUSIC <INVESTORRELATIONS@umusic.com>, UNIVERSAL EDITORIAL <INVESTMENTNEWS@editorial.investmentnews.com>, Urvashi Sinha <urvashi.sinha@wilsonelser.com>, VOGUE PRESS MAGZ <HELP@voguemagazine.com>, Marlyn Delva <mmt22@cumc.columbia.edu>, PAM OLSON <PAM.OLSON@us.pwc.com>, Paul Regan <legal@mskyline.com>, Ricki Roer <ricki.roer@wilsonelser.com>, Lauren M. Zink <lauren.zink@wilsonelser.com>, Ashley V. Humphries <ashley.humphries@wilsonelser.com>, Kathleen A. Mullins <kathleen.mullins@wilsonelser.com>, 60710 BD. 153974 <bd2561@columbia.edu>, Jennifer M. Provost <jennifer.provost@wilsonelser.com>, foia@eeoc.gov, teschmann@mskyline.com, LZUCKER@mskyline.com, governor.hochul@exec.ny.gov, legalasst@mskyline.com, CHICAGO@sec.gov, Amber Griffiths <ag2943@columbia.edu>, Alan Morrison <ajm157@columbia.edu>


15 cases in kings. 


-------- Forwarded Message --------
Subject: 	Fwd: Automatic reply: THIS RESPOSITORY IS BEING USED FOR A FEDERAL INVESTIGATION.
Date: 	Sun, 3 Jul 2022 17:09:07 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	smf2195@columbia.edu <smf2195@columbia.edu>


https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A== <https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==>

https://a810-bisweb.nyc.gov/bisweb/COsByLocationServlet?requestid=3&allbin=1077252 <https://a810-bisweb.nyc.gov/bisweb/COsByLocationServlet?requestid=3&allbin=1077252>

see also the address for the small claims papers, were shared by and between those address in the TO area.

***** YOU'LL HAVE TO ASK THE FBI/NSA TO SEE IF THEY WILL VERIFY THIS *****





– I HOPE YOU UNDERSTAND WHERE THIS ALSO PRESENTS A CONFLICT, AS HE BELIEVES THIS TO BE TRUE.
1_u.s._v._brian_benjamin_indictment (1).pdf

    NYSCEF MATTER 153974/2020
    - SHARED ADDRESS WITH THE WILSON ELSER LAW FIRM, BELOW.

    Filing User Shari Laskowitz | slaskowitz@ingramllp.com | 2129079600

    150 East 42nd Street 19th Floor, New York, NY 10017 Filed: 07/21/2020

-------- Forwarded Message --------
Subject:     Voicemail from Mr. PAUL regan
Date:     Sun, 26 Jun 2022 16:51:47 -0400
From:     BO DINCER <bondstrt007@gmail.com>
To:     REDACTED, teschmann@mskyline.com, Joseph Giamboi, ESQ <joseph.giamboi@brooklaw.edu>, LZUCKER@mskyline.com, sgo2107@columbia.edu, letters@nypost.com, Laskowitz, Shari <slaskowitz@ingramllp.com>, dallas-reserve-mgmt@dal.frb.org, REDACTED, praghuram2@bloomberg.net, PRIYA.RAGHURAM@MORGANSTANLEY.COM <PRIYA.RAGHURAM@morganstanley.com>, JAMES GORMAN [MORGAN STANLEY] <james.gorman@morganstanley.com>, Dow Jones <wsjprosupport@dowjones.com>, REDACTED, Paul Regan <LEGAL@mskyline.com>, LEGALASST@mskyline.com, MSKYLINE <anne@thehighlandpartners.com>, cweiss@ingramllp.com, info@statefarm.com, State Farm <mutualfunds@statefarm.com>, David Moore <david.moore.ct95@statefarm.com>, REDACTED, Scott Holcomb <scott@holcombward.com>, REDACTED
CC:     KATHY HOCHUL <governor.hochul@exec.ny.gov>, BBO 121 <ms60710444266@yahoo.com>, MIT Sloan Executive Education <executive_education@mailsvc.sloan.mit.edu>, REDACTED, NYSCEF PROCESS HD <oca_hd_processor@nycourts.gov>, The New York Times <help@nytimes.com>, administration@mskyline.com, MANHATTAN SKYLINE, LLC. <ADMINISTRATOR@mskyline.com>


I am terrified, where is he ? Touching himself or making videos with my Glamour shots.

Thats actually a compound, in the scope of avoidance to prosecution.

-------- Forwarded Message --------
Subject: Automatic reply: THIS RESPOSITORY IS BEING USED FOR A FEDERAL INVESTIGATION.
Date: Sun, 3 Jul 2022 20:53:37 +0000
From: FREEDOM OF INFORMATION ACT <foia@eeoc.gov>
To: B D2022 <ms60710444266@yahoo.com>



This is an automated response to your email received by a Freedom of Information Act (FOIA) field office unit within the Equal Employment Opportunity Commission (EEOC). Please note that FOIA requests submitted to the EEOC through this email box may experience some processing delays. If you are submitting a FOIA request, we strongly encourage you to submit your request online, https://eeoc.arkcase.com/foia/portal/login . Submitting your request online, https://eeoc.arkcase.com/foia/portal/login, ensures your FOIA request is timely received and allows you to monitor the status of your request. And, it delivers your responsive records online through a secured account.
If you are unable to access our online portal, you can submit your request directly to the office’s FOIA email account, which you can find by clicking on the following link: https://www.eeoc.gov//eeoc/foia/contact.cfm. Please do not submit requests by mail, fax, or courier since we do not have access to these delivery methods at this time. EEOC employees are teleworking full time because of the pandemic.

Sincerely,
Field FOIA Office

---
## [Peptide90/space-station-14](https://github.com/Peptide90/space-station-14)@[949fbd0194...](https://github.com/Peptide90/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Monday 2022-07-04 06:58:31 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [shrysr/denote](https://github.com/shrysr/denote)@[f35ef05cb4...](https://github.com/shrysr/denote/commit/f35ef05cb451f265213c3aafc1e62c425b1ff043)
#### Monday 2022-07-04 07:37:23 by Protesilaos Stavrou

REMOVE support for 'id:' hyperlink types

The original idea was to support the 'org-id' library on the premise
that it makes Denote a good Emacs citizen.  However, discussions on the
mailing list[0] and the GitHub mirror[1] have made it clear to me that
'org-id' is not consistent with Denote's emphasis on simplicity.

To support the way 'org-id' works, we will eventually have to develop
some caching mechanism, just how the org-roam package does it.  This is
because the variable 'org-id-extra-files' needs to be kept up-to-date
whenever an operation on a file is performed.  At scale, this sort of
monitoring requires specialised software.  Such a mechanism is outside
the scope of Denote---if you need a db, use org-roam which is already
great.

[0] <https://lists.sr.ht/~protesilaos/denote/%3C8735fk4y1w.fsf%40hallac.net%3E#%3C877d4un73c.fsf@protesilaos.com%3E>

[1] <https://github.com/protesilaos/denote/issues/29>

Quote of what I wrote on the GitHub mirror issue 29:

        [ggjp] This is what I was implying.  That we are, in fact,
        providing an option that is not viable long-term, but keeping
        the option for expert users who will be able to handle this.
        And we should warn about this clearly in the doc of that option.

    [protesilaos] What you write here @ggjp and what @shrysr explained
    tells me that those expert users will need to be real experts.  To
    put it concretely, I am an experienced Emacs user with no
    programming background, who has written several Emacs
    packages (including the modus-themes which are built into Emacs),
    but I have zero knowledge of using a db or of handling things with
    python and the like.  So if I opt in to 'denote-link-use-org-id' I
    will eventually run into problems that my non-existent skills will
    prevent me from solving.  At that point, I will just use org-roam
    which already handles this use-case in a competent way (and has a
    massive community to rely on in case I need further support).

    If each package needs to write its own optimisations and maintain
    its own cache, to me this shows that 'org-id' is not good enough for
    the time being: more work needs to be done in org.git to provide a
    universal solution.

    I wanted to support 'org-id' by default on the premise that Denote
    must be a good Emacs citizen which interoperates with the rest of
    the wider ecosystem.  But if 'org-id' leaves something to be
    desired, then that goal is not worth pursuing: we add complexity to
    our code, offer an option that we cannot genuinely/adequately
    support, and make usage of it contingent on reading the docs and
    having a high level of expertise.

    I think being a good Emacs citizen is a laudable principle.  In this
    case, the right thing to do is to recommend the use of org-roam
    instead of trying to accommodate 'org-id'.  As such, I have now
    changed my mind and think we should remove what we previously added.

    For some context here: the reason I never used org-roam is
    because (i) it is Org-specific whereas I write notes in different
    file types and (ii) I did not want to ever rely on a db or
    equivalent dependency.

    <https://github.com/protesilaos/denote/issues/29#issuecomment-1173036924>

---
## [DEFRA/water-abstraction-ui](https://github.com/DEFRA/water-abstraction-ui)@[1b0c52c196...](https://github.com/DEFRA/water-abstraction-ui/commit/1b0c52c196d45423161502d8c9704f91cebc21d1)
#### Monday 2022-07-04 08:36:27 by Alan Cruikshanks

Tidy up .../billing/services/transactions-csv.js

https://eaflood.atlassian.net/browse/WATER-3586

We came across transactions-csv.js as part of working on altering the bill run download to handle SROC bill runs.

To say it angered and upset the current dev team is a bit of an understatement. You _could_ argue calling a function to pull a couple of fields from an object has value (though in our opinion you'd be wrong!)

But there is no reason for making an _utter_ mess of known conventions around `private` and `public` methods. It is a [common practise](https://stackoverflow.com/a/4484449/6117745) in JavaScript to prefix private module methods with an underscore. This singles intent to other developers; these methods are only used internally by the module, those without it are for use elsewhere in the code.

So, after another day struggling through the code imagine our consternation when we come across this

```javascript
exports._getInvoiceData = getInvoiceData
exports._getInvoiceAccountData = getInvoiceAccountData
exports._getTransactionData = getTransactionData
exports._getTransactionAmounts = getTransactionAmounts
exports.createCSV = createCSV
exports.getCSVFileName = getCSVFileName
```

We are ***explicitly*** making `private` methods `public`. Either that, or we couldn't be arsed to stick to a consistent naming convention. Arrrrgh!!! 🤬😠

As far as we can see this was _solely_ for the purpose of testing the methods. _They are not referenced anywhere else!!!_ So, added to our convention breaking we're also directly testing methods intended to be private, and making them public purely to allow those tests to run. 🤯🤦

We have no words. Just know this change attempts to make things a little better 🥹

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[c18c7e0a3f...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/c18c7e0a3fe37883f775734850d3ce5099637742)
#### Monday 2022-07-04 08:41:02 by Angelo G. Del Regno

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

Signed-off-by: Kneba <abenkenary3@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [zeppipi/Puggle](https://github.com/zeppipi/Puggle)@[54f0d69ca5...](https://github.com/zeppipi/Puggle/commit/54f0d69ca5bb0124d6a451c8c0fd33e1ec6c055f)
#### Monday 2022-07-04 09:02:56 by zeppipi

Some minor notes from friends playing

+ UI is fucking broken, I'm guessing it is because other devices (like my laptop) has different resolutions, so everything just got stretched, I need to learn how to use anchors

+ You get more points when you hit the ball higher, but it seems that idea is communicated very poorly and I need a way to tell that to new players playing.

---
## [hypothesis/lms](https://github.com/hypothesis/lms)@[6809b8136b...](https://github.com/hypothesis/lms/commit/6809b8136b731935aeee1f9496eb3a13e178b263)
#### Monday 2022-07-04 09:13:45 by Sean Hammond

Don't run the functests on Jenkins

This is a pain because it apparently requires there to be a separate
`make functests-only` target (is that really necessary?).

But anyway: I don't think there's any benefit to running the functests
on Jenkins after we've already run them on GitHub Actions. It's just
more code to maintain and more waiting around for Jenkins to finish.
The idea originally was that Jenkins runs the tests actually inside the
Docker container so it's more similar to production than GitHub Actions
which doesn't run the tests in Docker. But I don't think there's ever
been a case of the tests passing on GitHub Actions and then Jenkins
catching a problem with its second run of the tests. So in practice I
think this is silly.

I think there are better steps that we could take to control
CI-versus-prod differences if we wanted to do that:

- Use the same OS in production as we use on CI.
  We could change CI to Alpine.
  But I'd recommend changing production to Ubuntu instead then we'd have
  Ubuntu on prod, CI and dev. And people recommend Debian over Alpine
  anyway:
  https://pythonspeed.com/articles/base-image-python-docker-images/

- Install the app into a virtualenv within the production Docker
  container so that it's isolated from the container's OS's Python
  packages

---
## [frostzzone/scratch-for-discord](https://github.com/frostzzone/scratch-for-discord)@[fd436761b2...](https://github.com/frostzzone/scratch-for-discord/commit/fd436761b2daf094bf8fb93ee541fb7ed45432c9)
#### Monday 2022-07-04 09:45:19 by JeremyGamer13

add User Examples holy shi

i really hope my server doesnt fucking die for no reason

---
## [PicnicSupermarket/error-prone](https://github.com/PicnicSupermarket/error-prone)@[fa6b82c77d...](https://github.com/PicnicSupermarket/error-prone/commit/fa6b82c77deb00cdf7b34561232f116c7bbdf8b4)
#### Monday 2022-07-04 10:54:58 by ghm

AlreadyChecked: handle early returns.

Also, use WellKnownMutability again to assume that _instance_ methods on immutable types are pure.

i.e., for the remainder of the method body in

```
void foo(boolean a) {
  if (a) {
    return;
  }
  // ...
}
```

`a` is known to be false.

Implementing tests for this made me realise my thinking was a bit flawed when looking for occurrences of known truths/falsehoods; really, we should be checking for all boolean expressions which might be known (and hence misleading).

I've done this instead, but in turn it inspired a heursitic to avoid annoying findings for stuff like:

```
if (isEmpty) {
  message.setIsEmpty(isEmpty);
}
```

Because that finding is quite low-value, and what would you suggest instead? If it's more than just a setter, you'd want a parameter comment

PiperOrigin-RevId: 420265440

---
## [ehumber/kafka-rest](https://github.com/ehumber/kafka-rest)@[b256e1ee95...](https://github.com/ehumber/kafka-rest/commit/b256e1ee95956e78ee8150475632eb41ccc2c301)
#### Monday 2022-07-04 11:02:02 by Emma Humber

KREST-2655 Simple version of disconnect

During our release review last year, one of the requests was to ensure that any long running connections are disconnected periodically.

Kafka does this for non-rest clients in https://github.com/confluentinc/ce-kafka/pull/3252 (which wasn't merged but has some interesting comments) and https://github.com/confluentinc/ce-kafka/pull/3292

The intent of this PR is to disconnect all streaming produce connections 24 hours after they were first made.  Once the stream has reached this age, the next message to arrive will get a 408 request timeout with message "Streaming connection open for longer than allowed: Connection will be closed."

Suggestions please for a better http status code, there is nothing that I could find that matches what we are doing.

We want to try and respond to any outstanding requests that we know about, rather than just losing them, so there is a grace period of 500ms, where any message already with us, or that arrive within this time period are also responded to with the 408.

Any messages that arrive after the grace period, but before the connection closing has finished up (a small timing window) are ignored.

The disconnect code only triggers for arriving messages, because there is already an existing, shorter timeout of 30s, for unused streams : https://github.com/confluentinc/rest-utils/blob/111998c26588cfcb773ee7bf9a757e3f79c5f301/core/src/main/java/io/confluent/rest/RestConfig.java#L418 so there was no point complicating the code further here to account for this.

hasNext() on the MappingIterator hangs if there is nothing new on the MappingIterator (you'd hope it would just return false)

There is still a timing window around "closingStarted" but it doesn't matter (i think) because all it means is that the scheduledExecutor has triggered the close on the MappingIterator and the output stream.  If we try and write to the closed output stream it does't matter, nothing bad will happen.  I didn't want to add a lock.

The next() call at line 163 is to clear the message off the MappingIterator so we can process the next one (and return 408) if needed.

There is a horrible override of clock (where I could have just an Instant for the stream start time) so that I can actually unit test this reliably - you can't mock Instant easily.

FUP - Should we add disconnect jitter in a follow on PR?

---
## [momentum-mod/website](https://github.com/momentum-mod/website)@[9646bda3d0...](https://github.com/momentum-mod/website/commit/9646bda3d0c94dbb27507e5346f36c1b5d89e1e6)
#### Monday 2022-07-04 11:23:32 by tsa96

chore: Refactor method names and access

Another sweeping refactor, I'm sorry. I just strongly feel we should be following a consistent naming style, meaning lowerCamelCase for method names. I plan on enforcing https://ts.dev/style/#naming-style from now on.

Also, using `public` on the front of methods everywhere is just silly (and we weren't even applying it consistently). It has no programmatic purpose, seems to just be there for the sake of looking like C++/C#/Java. More than anything I worry it'll confuse contributors into thinking it has actual pratical purpose.

---
## [xbapps/xbvr](https://github.com/xbapps/xbvr)@[04ae91075f...](https://github.com/xbapps/xbvr/commit/04ae91075f4205bbee53c2424ff6b5bf22032c29)
#### Monday 2022-07-04 13:41:20 by theRealKLH

fix: Migrate Tonight's Girlfriend VR scenes to new scraper (#767)

* Update migrations.go

fix semi BAD migration

* remove personal config

* Update migrations.go

change migration number

* Update .gitignore

* Update migrations.go

more fixes. Should be able to remove dupes due to prior migration.

---
## [nekoyoubi/bitburner](https://github.com/nekoyoubi/bitburner)@[2541d89beb...](https://github.com/nekoyoubi/bitburner/commit/2541d89bebb24ddab49b52a621f1e8c72e86cf1f)
#### Monday 2022-07-04 14:02:10 by Nekoyoubi

1.2 - 2.1 - 4.3 - 5.1 - 6.1 - 7.1 - [9.1] - 10.1

- `/gang/manage.js` changes; first member lost in clash... sad day
  - removed the A-L sequential naming, as fill-ins on death screw that all up anyway
  - changed a few `for`s into `.forEach()`s
  - cleaned up/removed some comments and code that were likely never coming back (justice things)
  - added a Territory Warfare cutoff at 500% power ratio
  - added automatic war engagement toggle
- forced the Karma bar to come back until I see if that achievement is what I think it is
- updated the crappy `attack.js` for growth and hack thread targets
- fixed a bug that was stopping `attack.js` from working in stupid-low hack stat scenarios
- as for `bladeburner.js`
  - added city hopping when things look bleak
  - added black ops to things to auto-do if they are 100% guaranteed; skips the exodus
  - reordered skills by ascending cost prior to purchase
  - updated the busy check to factor in whether you have `The Blade's Simulacrum`
  - fixed chaos check to stop performing any action if there was no `lastAction`
  - added black ops to the action-decision exclusions; don't want to be cancelling those
- added `config.txt` (finally); I wanted to work on it a bit more, but hacknet servers made me do it
- rewrote `hacknet.js` for the shiny, new hacknet servers
  - no longer has a cap variable for everything
  - spends hashes when close to full
  - reads the config to see if it should be upgrading itself or not
  - buys a new server if the cost is less than .75 of your money
  - upgrades servers based on the least expensive upgrade across all servers
- played with the `market.js`; probably broke it more, honestly

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[1b60be51cc...](https://github.com/JuliaLang/julia/commit/1b60be51cc0ecd26f7fd729dea7e463e1aea77d8)
#### Monday 2022-07-04 14:29:58 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>
(cherry picked from commit 62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)

---
## [LesterJones/CodeWars](https://github.com/LesterJones/CodeWars)@[c0cbc01ea4...](https://github.com/LesterJones/CodeWars/commit/c0cbc01ea43d35695c160cb42a11deb9da694062)
#### Monday 2022-07-04 16:17:31 by Lester Jones

Create Bernoulli numbers

DESCRIPTION:
Story
Before we dive into the exercise, I would like to show you why these numbers are so important in computer programming today.

It all goes back to the time of 19th century. Where computers we know today were non-existing. The first ever computer program was for the Analytical Engine to compute Bernoulli numbers. A woman named Ada Lovelace wrote the very first program. The sad part is the engine was never fully build so her code was never tested. She also predicted the start of AI (artificial intelligence).

Computers will be able to compose music by themselves, solve problems (not only numbers) ... So in her honor reproduce what was done back in 1842. The Bernoulli numbers are a sequence of rational numbers with deep connections to number theory. The Swiss mathematician Jakob Bernoulli and the Japanese mathematician Seki Kowa discovered the numbers around the same time at the start of the 18th Century. If you want to read more about her or Bernoulli numbers follow these links:

https://en.wikipedia.org/wiki/Ada_Lovelace

https://en.wikipedia.org/wiki/Bernoulli_number

http://mathworld.wolfram.com/BernoulliNumber.html

Exercise
Your job is to write a function bernoulli_number(n) which outputs the n-th Bernoulli number. The input will always be a non-negative integer so you do not need to worry about exceptions. How you will solve the problem is none of my business but here are some guidelines.
You can make pascal triangle and then with the basic formula generate all Bernoulli numbers. Look example below.

For the sake of floating numbers, just use Fractions so there will be no problems with rounding.

0 = 1 + 2b1 ............................................................... b1 = - 1/2

0 = 1 + 3b1 + 3b2 ................................................... b2 = 1/6

0 = 1 + 4b1 + 6b2 + 4b3 ....................................... b3 = 0

0 = 1 + 5b1 + 10b2 + 10b3 + 5b4 ...................... b4 = - 1/30

... and so on.

bernoulli_number(0) # return 1
bernoulli_number(1) # return Fraction(-1,2) or Rational(-1,2) or "1/2"
bernoulli_number(6) # return Fraction(1,42) or ...
bernoulli_number(42) # return Fraction(1520097643918070802691,1806) or ...
bernoulli_number(22) # return Fraction(854513,138) or ... "854513/138"
Note
See "Sample Tests" to see the return type for each language.

Good luck and happy coding!

PS: be careful some numbers might exceed 1000. If this kata is too hard for you try to solve pascal triangle and something similar to this and then come back :).

---
## [LesterJones/CodeWars](https://github.com/LesterJones/CodeWars)@[1bb23185d7...](https://github.com/LesterJones/CodeWars/commit/1bb23185d70eb419e0d673ab996e34496cffdef1)
#### Monday 2022-07-04 16:26:00 by Lester Jones

Create CatchingCarMileageNumbers

DESCRIPTION:
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.

---
## [LesterJones/CodeWars](https://github.com/LesterJones/CodeWars)@[c02d2e9876...](https://github.com/LesterJones/CodeWars/commit/c02d2e9876cca615d5cdaa858ace1909a721525e)
#### Monday 2022-07-04 16:41:25 by Lester Jones

Create EscapeTheMaze

DESCRIPTION:
That's terrible! Some evil korrigans have abducted you during your sleep and threw you into a maze of thorns in the scrubland D:
But have no worry, as long as you're asleep your mind is floating freely in the sky above your body.

Seeing the whole maze from above in your sleep, can you remember the list of movements you'll have to do to get out when you awake?

Input
You are given the whole maze maze as a 2D grid, more specifically in your language:

an array of strings

maze[0][0] is the top left-hand corner

maze[len(maze) - 1][len(maze[0]) - 1] is the bottom right-hand corner

Inside this 2D grid:

' ' is some walkable space
'#' is a thorn bush (you can't pass through)
'^', '<', 'v' or '>' is your sleeping body facing respectively the top, left, bottom or right side of the map.
Output
Write the function escape that returns the list/array of moves you need to do relatively to the direction you're facing in order to escape the maze (you won't be able to see the map when you wake up). as an array of the following instructions:

'F' move one step forward
'L' turn left
'R' turn right
'B' turn back
Note: 'L','R', and 'B' ONLY perform a rotation and will not move your body

If the maze has no exit, return an empty array.

This is a real maze, there is no "escape" point. Just reach the edge of the map and you're free!
You don't explicitely HAVE to find the shortest possible route, but you're quite likely to timeout if you don't ;P
Aside from having no escape route the mazes will all be valid (they all contain one and only one "body" character and no other characters than the body, "#" and " ". Besides, the map will always be rectangular, you don't have to check that either)

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[0af1d14b61...](https://github.com/omertuc/assisted-service/commit/0af1d14b61602aecf9e35fa7d6fa6af10d6f6b05)
#### Monday 2022-07-04 17:07:54 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to https://github.com/openshift/assisted-installer-agent/pull/388

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

# Agent version skew concerns

The agent now runs a `agentVersionSkewHack` function which adds a fake
file to the ignition config that can be used by the service to know
whether this the ignition file was filtered by a recent version of the
agent or not.

Since the *absence* of the coredns and keepalived files copied by
`copyIgnitionManagedNetworkIndications` indicates that the cluster is
running a non-managed-network cluster, the service has no way to know
whether the absence is due to that ignition file being processed by an
old agent or due to an actual absence. To overcome this ambiguity, the
agent adds this dummy file to the ignition which can help the service
tell those two situations apart.

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[9ac69faeea...](https://github.com/omertuc/assisted-service/commit/9ac69faeead93bd8cdc77a07b9d85415e66f0930)
#### Monday 2022-07-04 17:09:36 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to https://github.com/openshift/assisted-installer-agent/pull/388

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

# Agent version skew concerns

The agent now runs a `agentVersionSkewHack` function which adds a fake
file to the ignition config that can be used by the service to know
whether this the ignition file was filtered by a recent version of the
agent or not.

Since the *absence* of the coredns and keepalived files copied by
`copyIgnitionManagedNetworkIndications` indicates that the cluster is
running a non-managed-network cluster, the service has no way to know
whether the absence is due to that ignition file being processed by an
old agent or due to an actual absence. To overcome this ambiguity, the
agent adds this dummy file to the ignition which can help the service
tell those two situations apart.

---
## [omertuc/assisted-installer-agent](https://github.com/omertuc/assisted-installer-agent)@[1dbb24eb17...](https://github.com/omertuc/assisted-installer-agent/commit/1dbb24eb174abfd609d6971b7c694ae84d079743)
#### Monday 2022-07-04 17:20:33 by Omer Tuchfeld

MGMT-10973: Copy coredns & keepalived static pod manifests in day-2 connectivity-check ignition

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

However, that ignition file is incomplete as currently we only include
necessary information in it (because that file is very big). The parts
of that file that we care in this case are currently missing, so we have
to modify the agent to include those files.

This commit does that. A follow-up commit will be done on the service to
actually check for the presence of these files in this ignition to make
the decision of whether the cluster is managed or not, and in turn turn
on the necessary validations if not.

# Ignition Files

The ignition files we currently include are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [Cirrial/cirrstation](https://github.com/Cirrial/cirrstation)@[707fbfac7e...](https://github.com/Cirrial/cirrstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Monday 2022-07-04 17:38:19 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [DEFRA/water-abstraction-ui](https://github.com/DEFRA/water-abstraction-ui)@[606fadd94e...](https://github.com/DEFRA/water-abstraction-ui/commit/606fadd94e661f4634682b45637b859e0d1f7773)
#### Monday 2022-07-04 18:00:48 by Alan Cruikshanks

Tidy up .../billing/services/transactions-csv.js (#2120)

https://eaflood.atlassian.net/browse/WATER-3586

We came across transactions-csv.js as part of working on altering the bill run download to handle SROC bill runs.

To say it angered and upset the current dev team is a bit of an understatement. You _could_ argue calling a function to pull a couple of fields from an object has value (though in our opinion you'd be wrong!)

But there is no reason for making an _utter_ mess of known conventions around `private` and `public` methods. It is a [common practice](https://stackoverflow.com/a/4484449/6117745) in JavaScript to prefix private module methods with an underscore. This singles intent to other developers; these methods are only used internally by the module, and those without it are for use elsewhere in the code.

So, after another day of struggling through the code imagine our consternation when we come across this

```javascript
exports._getInvoiceData = getInvoiceData
exports._getInvoiceAccountData = getInvoiceAccountData
exports._getTransactionData = getTransactionData
exports._getTransactionAmounts = getTransactionAmounts
exports.createCSV = createCSV
exports.getCSVFileName = getCSVFileName
```

We are making `private` methods `public` but when we do so we are identifying them as `private`. Arrrrgh!!! 🤬😠

As far as we can see this was _solely_ for the purpose of testing the methods. _They are not referenced anywhere else!!!_ So, added to our convention-breaking we're also directly testing methods intended to be private and making them public purely to allow those tests to run. 🤯🤦

We have no words. Just know this change attempts to make things a little better 🥹

---
## [fiqri19102002/android_kernel_xiaomi_mojito](https://github.com/fiqri19102002/android_kernel_xiaomi_mojito)@[d77caa1488...](https://github.com/fiqri19102002/android_kernel_xiaomi_mojito/commit/d77caa148849bf3391f53c08f5c0e28c08db221e)
#### Monday 2022-07-04 18:00:58 by Peter Zijlstra

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
Signed-off-by: Fiqri Ardyansyah <fiqri15072019@gmail.com>

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[6fd47b008e...](https://github.com/omertuc/assisted-service/commit/6fd47b008ecad5e0750c5ad7c5f50a8e42f1c06c)
#### Monday 2022-07-04 18:19:09 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to https://github.com/openshift/assisted-installer-agent/pull/388

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, the clusterdeployments_controller can now import SNO clusters
(importing a cluster in kube-api is reconciling an installed clusterdeployment
that doesn't have a corresponding database entry? Is this something
users even encounter in ACM? not sure about this, this is why the
PR is still WIP)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [pri0818/android_kernel_realme_sm7125](https://github.com/pri0818/android_kernel_realme_sm7125)@[cbba8e0d0c...](https://github.com/pri0818/android_kernel_realme_sm7125/commit/cbba8e0d0cb71b5c4ff3e3c35fb9e18215fcc966)
#### Monday 2022-07-04 18:21:59 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [betrusted-io/xous-core](https://github.com/betrusted-io/xous-core)@[147ec8594c...](https://github.com/betrusted-io/xous-core/commit/147ec8594c49aa55cb156ae7cc28f642c667cece)
#### Monday 2022-07-04 18:53:58 by bunnie

add stash/pop of FB; fix suspend/resume buffering

The `ManagedMem` thing for the suspend/resume crate is simply
a disaster. It tries to be fancy and Rusty and really it just fails
in non-obvious ways. This is one of the places where it simply
does not pay to make things seem so simple.

Why? because in reality, memory is complicated. It comes in pages.
There's initialization. There's caching. There's volatility.
I haven't encountered a single situation where the assumptions
of page-alignment and memory layout have really lined up well enough
for this primitive to make sense. The "idea" was hey, since
you allocate a peripheral MemoryRegion, why not just use its attributes
as a marker to a suspend/resume thing that automatically handled
stashing that MemoryRegion to a backing store inside RAM? Seems
simple right? wrong. Every time I've tried to use it, it's failed
in non-obvious ways.

In this most recent incarnation, it turns out that for whatever
reason, it seems to be just stashing about the first 4-8k of the
framebuffer to the SR backup region, and then somehow grabbing
a future(?) copy of the memory? or maybe just a wrong copy? I don't
know. The code seems simple enough but it goes through some
traits and some type transformations and then there's some unsafe
code to make it volatile and it doesn't work.

Instead, we just use a damn [u32; FB_SIZE] slice to store the
frame buffer. This is so obvious and easy. The only price is
you have an "ugly" `fb[..FB_SIZE].copy_from_slice(&self.srfb)`
line instead of an "elegant" `srfb.suspend()` invocation.
Stashing into it is a bit uglier, because we have to cast the
slice to an unsafe pointer in order to access the `write_volatile()`
method. But, it works! It. Just. Works. And you can see what's going
on. Really, I should stop trying to be fancy and just be readable.

OK anyways, that was that rant. This commit also adds some
calls that allow us to re-use the suspend/resume frame buffer during
"normal" times as a stash/pop for the application image. This is
nice because the memory is normally idle/overhead when not
in suspend, so now we're repurposing some already-allocated memory
to accelerate some drawing operations, and it also makes, crucially,
a multi-step blocking modal dialog interaction less cosmetically
jarring, because the application thread can be fully blocked and
not responding to redraw commands but the stash/pop mechanism
creates the illusion of "everything is moving along".

---
## [DarkRose1981/catseyexi](https://github.com/DarkRose1981/catseyexi)@[ccf500070d...](https://github.com/DarkRose1981/catseyexi/commit/ccf500070d4448d1e2acbdb711190d5b4e21c4e6)
#### Monday 2022-07-04 19:08:59 by neuromancerxi

Add scripts and adjust plumbing for many temp items (#670)

* Add scripts and adjust plumbing for many temp items

Adds Scripts for items.
Adds Effect scripts for X_BOOST_II
Updates Effect scripts for the following:

ACCURACY_BOOST
ATTACK_BOOST
INTENSION
MAGIC_SHIELD
MULTI_STRIKES
MULTI_SHOTS
PAX
PHYSICAL_SHIELD
POTENCY
RAMPART

Adjusts item_usable use times to 1s.

Notes on effects:

Ascetics Tonic/Gambir - +25/+50 MATT/MACC
A big Thank You to Nyu for confirming the Intension effect for MACC.
https://www.bg-wiki.com/bg/Ascetic's_Tonic
https://www.bg-wiki.com/bg/Ascetic's_Gambir

Bravers Drink - +15 to All Stats
https://www.bg-wiki.com/bg/Braver's%20Drink
Reference to Icons/Effects - https://youtu.be/JYT5a_pTA3o?t=20

Champions Tonic - +15 Haste / +3 Crit rate
Champions Drink/Gambir - +18 Haste / +5% Crit rate
Expected Haste effect to be Magic pool based on BG comment (18 and 15)
Critical Hit rate, no data available from community sources, conservative value of 5 (Drink/Gambir) 3 (Tonic)
Both BG and 'clopedia sources confirm Critical Hit Rate (as does the effect description), however, only BG has a reference to Haste value.
https://www.bg-wiki.com/bg/Champion's_Tonic

Gnostics Drink - Enmity -10
No community resources confirm this value, using SCH Animus Minuo as an reference.
https://www.bg-wiki.com/bg/Gnostic's%20Drink
https://www.bg-wiki.com/bg/Animus_Minuo

Monarchs Drink - Regain +3 (30/1000 per tick) for 3 minutes.
https://www.bg-wiki.com/bg/Monarch's_Drink

Stalwart's Tonic/Gambir - ACC/RACC 50/100 ATTP/RATTP 25/50
A big Thank You to Nyu for confirming the effects apply ACC/RACC and ATTP/RATTP across two effects.
https://www.bg-wiki.com/bg/Stalwart's_Tonic
https://www.bg-wiki.com/bg/Stalwart's_Gambir

Berserker's Tonic/Drink - DA 50/100
Thanks to Nyu for confirming the MULTI_STRIKES effect and 1m duration.
https://ffxiclopedia.fandom.com/wiki/Berserker%27s_Drink
No full data on DA rate, minus 'clopedia which has verification tags. Working on the expectation that this follows a good portion of the other items and follows the half potency values for the lesser item.

Swiftshot Tonic/Drink - Double Shot 50/100
https://www.ffxiah.com/forum/topic/28603/fools-tonic-broken#1749569

Dusty Scroll of Reraise - Reraise III, 10m duration.
https://www.bg-wiki.com/bg/Dusty_Reraise

Spiritual Incense/Fools Drink/Tonic/Powder: See effects/magic_shield
Carnal Incense/Fanatics Drink/Tonic/Powder: See effects/physical_shield

* Removed copypasta subp and trailing whitespace.

* Item script clean-up and move effect functions to item_utils.

* Resolve Conflicts

Convert namespace in scripts from item_utils to xi.item_utils
PHYS_ABSORB to Percent from 10000 Scale

---
## [kgoess/dance-scheduler](https://github.com/kgoess/dance-scheduler)@[be68684263...](https://github.com/kgoess/dance-scheduler/commit/be68684263d552079b818f5ba6b803de761f8245)
#### Monday 2022-07-04 21:04:52 by Kevin M. Goess

Get rest of series default templates working.

Notes:

- In the series template popup the series name is now just some text. That's
where we'd left off the other night.

- I removed this from the Events schema:

    UNIQUE KEY (series_id, is_template)

Because that only works if the only values for is_template are 1 or NULL. After
reading this discussion
https://dba.stackexchange.com/questions/40324/only-allow-one-checked-row-in-a-column-in-sql-server
I think if we want to constrain that, we should add a separate table of
series-to-templates. And that way I can set `$new->is_template(0);` for all the
incoming events in the migration script.

- I re-ordered the Events accordion container so that the first row is "Series"
followed by the templated rows, followed by the ones the user would fill in for
an event. That'll match the actual workflow better, and more importantly, when
you're adding a new event and get down to the "Series" listbox, changing that
zeroes out all the other rows you just entered. Fixing that would be a pain,
but it just makes more sense to *start* with the Series selection anyway.

- I disabled the "Manage Templates" button when you're adding a new Series, so
you can't futz with the template until you've saved the series. We need this
because the template popup needs to get the series_id to have something to work
with. There's a bunch of spread-out code to make sure the button is re-enabled.

- When you hit "Save" on the series template popup, we left the window open so
you could look at it, but there was no indication of success, so I added an
alert(). It looks pretty crappy and there's probably a better solution.

---
## [jonny561201/home_automation_app](https://github.com/jonny561201/home_automation_app)@[4dcd7f0b7b...](https://github.com/jonny561201/home_automation_app/commit/4dcd7f0b7b1168b5dd1c773dc4f419984f5fb46f)
#### Monday 2022-07-04 22:09:12 by Jon Graf

added stupid community edition of another basic component...fuck you react native

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[912163fc0d...](https://github.com/Buildstarted/linksfordevs/commit/912163fc0d4a94a3a97c05e31c1e708e1e4110a0)
#### Monday 2022-07-04 23:06:55 by Ben Dornis

Updating: 7/4/2022 11:00:00 PM

 1. Added: Composability of Data
    (https://www.justinphu.dev/blog/composability-of-data)
 2. Added: 5 lessons I learnt after coding for 10 years
    (https://binaryho.me/5-things-i-leant-hard-way/)
 3. Added: .NET R&D Digest (June, 2022)
    (https://olegkarasik.wordpress.com/2022/07/05/net-rd-digest-june-2022/)
 4. Added: How to learn data engineering
    (https://www.blef.fr/learn-data-engineering/)
 5. Added: This website is hacky AF
    (https://yakkomajuri.com/blog/hacky)
 6. Added: Another Update On The Bagel Language
    (https://www.brandons.me/blog/another-bagel-update)
 7. Added: How to prevent  partial rendering in HTMX?
    (https://rajasimon.io/blog/prevent-partial-rendering-in-htmx/)
 8. Added: I'm going to take a wild guess here and say that you, like me, have a large pile (or digital equivalent) of books or articles you've been meaning to get around to reading, plus maybe a long queue of podcast episodes to which you'd love to listen, if only you had the time. It's the archetypal "first-world problem", I know. But one worth reflecting on – because it's a microcosm of a broader mistake that makes it more stressful than in needs to be to build a fulfilling and productive life: the problem of Too Many Needles. It's amusing to reflect that at an earlier stage in the history of the web, information overload was widely held to be a temporary issue. Yes, true, for the time being we were getting deluged by a zillion irrelevant blog posts, emails and news updates. But that wouldn't last, because soon we'd have better technology for finding what we wanted, while disregarding the rest. The real trouble, according to the leading techno-optimist Clay Shirky, wasn't information overload, but "filter failure". We needed – and we'd eventually get – more sophisticated ways to filter the wheat from the online chaff. And then we'd no longer feel overwhelmed. Yeah… no. I assume you'd agree that the problem of your to-read pile is very much not one of filter failure. It's not that you're deluged with things you don't care about, and need help figuring out what's truly of interest. It's that you're overwhelmed by things you do want to read. All the books on your bedside table, all those bookmarks in your browser, or articles saved to Instapaper – all of them seem like they might be right up your street, or crucial to your professional success, or might contain some nugget of wisdom you'd benefit from absorbing. The problem, as the critic Nicholas Carr explained, isn't filter failure. It's filter success. In a world of effectively infinite information, the better you get at sifting the wheat from the chaff, the more you end up crushed beneath a never-ending avalanche of wheat. And so, for example, the reading recommendations I encounter via Twitter are much more tailored to my concerns than those I might encounter via a newspaper, because I choose who I follow on Twitter; it's like having a thousand assistants scouring the infoverse for whatever might pique my interest. My challenge, information-wise, isn't about finding a needle in a haystack. It's that I'm confronted on a daily basis, in Carr's words, by "haystack-sized piles of needles." The wider point here is that lots of the other ways in which we feel overwhelmed are problems of "too many needles" as well. They involve the attempt to divide our finite time and attention among too many things that all have a legitimate claim on them. Some of these are "good problems to have": for example, if you're blessed with work you love, or a creative passion you're good at, you may often feel torn between multiple projects you're excited to launch. Others are the familiar problems of Life Under Late Capitalism™, like the feeling that there's simply not enough time in the day to be a good parent while staying afloat financially. What they all have in common is that the things you're choosing between all genuinely matter, and would benefit from more time than you can give them. Unfortunately, most advice on productivity and time management takes the needle-in-a-haystack approach instead. It's about becoming more efficient and organised, or better at prioritising, with the implied promise that you might thereby eliminate or disregard enough of life's unimportant nonsense to make time for the meaningful stuff. To stretch a metaphor: it's about reducing the size of the haystack, to make it easier to focus on the needle. There's definitely a role for such techniques; but in the end, the only way to deal with a too-many-needles problem is to confront the fact that it's insoluble – that you definitely won't be fitting everything in. (Of course some such problems, where just scraping a living feels impossible, demand political solutions too – a topic for another time.) It's not a question of rearranging your to-do list so as to make space for all your "big rocks", but of accepting that there are simply too many rocks to fit in the jar. You have to take a stab at deciding what matters most, among your various creative passions/life goals/responsibilities – and then do that, while acknowledging that you'll inevitably be neglecting many other things that matter too. To return to information overload: this means treating your "to read" pile like a river (a stream that flows past you, and from which you pluck a few choice items, here and there) instead of a bucket (which demands that you empty it). After all, you presumably don't feel overwhelmed by all the unread books in the British Library – and not because there aren't an overwhelming number of them, but because it never occurred to you that it might be your job to get through them all. Coming at life this way definitely entails tough choices. But it's liberating, too, as you slowly begin to grasp that you never had any other option. There's no point beating yourself up for failing to clear a backlog (of unread books, undone tasks, unrealized dreams) that it was always inherently unfeasible to clear in the first place. I like to think of it as the productivity technique to beat all productivity techniques: finally internalizing the implications of the fact that what's genuinely impossible – the clue is in the name! – cannot actually be done. • I'd love to hear from you – just hit reply. (I read all messages, and try to respond, but not always in a timely fashion: sorry!) If you enjoyed this email, you'd be doing me a big favour by forwarding it to someone else who might like it, or mentioning it wherever you emit opinions online; the "View in a browser" link above will take you to a web version. And if you got this from a friend and would like to subscribe yourself, please do so here. 540 President St, Brooklyn, NY 11215, United States
    (https://www.oliverburkeman.com/so/60NWXZixI)
 9. Added: Silicon Valley Bullshit
    (https://snifftwiggybean.blogspot.com/2022/06/silicon-valley-bullshit.html)
10. Added: Curating Dependency Vulnerabilities
    (https://beny23.github.io/posts/curating_vulnerabilities/)
11. Added: Performance: Crystal vs Ruby
    (https://rrevi.github.io/performance-crystal-vs-ruby)
12. Added: Why You Should Write Weekly 15-5s
    (https://eugeneyan.com/writing/15-5/)
13. Added: Designing a wireless charging pad
    (https://arslan.io/2022/07/04/designing-a-wireless-charging-pad-from-scratch/)
14. Added: Dogfooding Blambda! : revenge of the pod people
    (https://jmglov.net/blog/2022-07-04-dogfooding-blambda-1.html)
15. Added: 🙀 Startup founder fears by funding round
    (https://vadimkravcenko.com/shorts/startup-founder-fears-by-funding-round/)
16. Added: nabeelqu
    (https://nabeelqu.co/advice)
17. Added: Power Estimation: Balance Between Simplicity and Accuracy
    (https://www.gregnavis.com/articles/power-estimation.html)

Generation took: 00:06:42.5637744

---
## [aarasmith/CAPA](https://github.com/aarasmith/CAPA)@[ba0d508300...](https://github.com/aarasmith/CAPA/commit/ba0d5083009866df707aff7d028d7ca27bd742ff)
#### Monday 2022-07-04 23:54:37 by aarasmith

2022/07/05 - Work PC - fixed the future_lapply bullshit. If you pass a function to future_lapply that was declared within the function in which you're calling future_lapply it does a crazy environment export to each node and is completely fucked

---

